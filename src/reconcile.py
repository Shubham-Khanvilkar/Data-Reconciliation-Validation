from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUT = ROOT / "output"
TOLERANCE = 1000.0


def load_source(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["as_of_date"])
    required = {"account_id", "as_of_date", "position_value", "cash_value", "total_value"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns in {path.name}: {sorted(missing)}")
    return df


def reconcile(a: pd.DataFrame, b: pd.DataFrame, tolerance: float = TOLERANCE) -> pd.DataFrame:
    a = a.copy()
    b = b.copy()
    a["source_a_calculated"] = a["position_value"] + a["cash_value"]
    b["source_b_calculated"] = b["position_value"] + b["cash_value"]

    dup_a = a[a.duplicated("account_id", keep=False)][["account_id"]].drop_duplicates()
    dup_b = b[b.duplicated("account_id", keep=False)][["account_id"]].drop_duplicates()

    merged = a.merge(b, on="account_id", how="outer", suffixes=("_a", "_b"), indicator=True)
    merged["variance"] = merged["total_value_a"].fillna(0) - merged["total_value_b"].fillna(0)
    merged["abs_variance"] = merged["variance"].abs()

    def classify(row):
        if row["_merge"] == "left_only":
            return "Missing in Source B"
        if row["_merge"] == "right_only":
            return "Missing in Source A"
        if row["account_id"] in set(dup_a.account_id):
            return "Duplicate in Source A"
        if row["account_id"] in set(dup_b.account_id):
            return "Duplicate in Source B"
        if row["abs_variance"] > tolerance:
            return "Value Mismatch"
        return "Matched"

    merged["status"] = merged.apply(classify, axis=1)
    return merged


def main() -> None:
    a = load_source(DATA / "source_a.csv")
    b = load_source(DATA / "source_b.csv")
    result = reconcile(a, b)
    OUTPUT.mkdir(exist_ok=True)
    exceptions = result[result["status"] != "Matched"].copy()
    result.to_csv(OUTPUT / "reconciliation_detail.csv", index=False)
    exceptions.to_csv(OUTPUT / "exceptions.csv", index=False)

    print("RECONCILIATION CONTROL")
    print("=" * 24)
    print(f"Source A records: {len(a)}")
    print(f"Source B records: {len(b)}")
    print(f"Matched: {(result.status == 'Matched').sum()}")
    print(f"Exceptions: {len(exceptions)}")
    print(f"Total Source A: {a.total_value.sum():,.2f}")
    print(f"Total Source B: {b.total_value.sum():,.2f}")
    print(f"Net variance: {a.total_value.sum() - b.total_value.sum():,.2f}")
    print("\nException breakdown:")
    print(exceptions["status"].value_counts().to_string())


if __name__ == "__main__":
    main()
