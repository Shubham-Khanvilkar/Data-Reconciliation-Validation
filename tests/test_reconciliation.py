import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from reconcile import reconcile


def test_matching_record_is_matched():
    a = pd.DataFrame([{"account_id": "A1", "as_of_date": "2026-08-28", "position_value": 100, "cash_value": 20, "total_value": 120}])
    b = a.copy()
    result = reconcile(a, b)
    assert result.loc[0, "status"] == "Matched"


def test_variance_becomes_exception():
    a = pd.DataFrame([{"account_id": "A1", "as_of_date": "2026-08-28", "position_value": 100, "cash_value": 20, "total_value": 120}])
    b = pd.DataFrame([{"account_id": "A1", "as_of_date": "2026-08-28", "position_value": 100, "cash_value": 20, "total_value": 2500}])
    result = reconcile(a, b, tolerance=1000)
    assert result.loc[0, "status"] == "Value Mismatch"


def test_missing_record_is_detected():
    a = pd.DataFrame([{"account_id": "A1", "as_of_date": "2026-08-28", "position_value": 100, "cash_value": 20, "total_value": 120}])
    b = pd.DataFrame([{"account_id": "A2", "as_of_date": "2026-08-28", "position_value": 100, "cash_value": 20, "total_value": 120}])
    result = reconcile(a, b)
    assert set(result.status) == {"Missing in Source B", "Missing in Source A"}
