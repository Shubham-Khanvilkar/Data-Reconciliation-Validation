# Data Reconciliation & Validation

Independent portfolio project simulating a daily reporting-control process with synthetic wealth-management-style data.

## Objective
Compare two reporting sources, validate record-level balances, classify exceptions, and produce an auditable reconciliation summary.

## Controls demonstrated
- Record-count reconciliation
- Key/record matching
- Balance validation
- Absolute and percentage variance checks
- Missing-record detection
- Duplicate-key detection
- Exception classification
- Control-status summary
- CSV exception output
- SQL validation queries

## Exception logic
A record is an exception when the source values do not reconcile within the configured tolerance, when a record is missing from either source, or when a duplicate business key is detected.

## Technology
Python, Pandas, SQL, CSV, Git/GitHub

## Run locally
```bash
pip install -r requirements.txt
python src/reconcile.py
```

## Structure
```text
Data-Reconciliation-Validation/
├── README.md
├── requirements.txt
├── data/
│   ├── source_a.csv
│   └── source_b.csv
├── src/
│   └── reconcile.py
├── sql/
│   └── reconciliation_queries.sql
└── tests/
    └── test_reconciliation.py
```

## Portfolio disclaimer
All data is synthetic. This is an independent portfolio project and is not professional Morgan Stanley or financial-services employment experience.
