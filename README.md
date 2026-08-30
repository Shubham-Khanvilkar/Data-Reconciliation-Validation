Build the complete repository:

Data-Reconciliation-Validation

Create a production-quality portfolio project demonstrating reporting controls, reconciliation and data-quality analysis using synthetic data.

TECH STACK:

Python 3.12
Pandas
FastAPI
SQLite
SQL
Pydantic
pytest

PROJECT:

Data-Reconciliation-Validation/
├── README.md
├── requirements.txt
├── .gitignore
├── app/
│   ├── main.py
│   ├── schemas.py
│   └── services/
│       ├── validation.py
│       ├── reconciliation.py
│       ├── comparison.py
│       └── quality.py
├── data/
│   ├── source_a.csv
│   ├── source_b.csv
│   └── reporting_extract.csv
├── sql/
│   ├── validation.sql
│   ├── reconciliation.sql
│   └── quality_checks.sql
├── tests/
│   ├── test_validation.py
│   ├── test_reconciliation.py
│   ├── test_quality.py
│   └── test_api.py
└── docs/
    ├── reconciliation_methodology.md
    └── data_quality_framework.md

GENERATE SYNTHETIC REPORTING DATA.

Create two independent reporting sources:

SOURCE A
SOURCE B

Both should contain:

date
region
advisor_id
client_segment
inflows
outflows
nna

Create intentional discrepancies in Source B.

DO NOT make all records identical.

IMPLEMENT:

1. Record-count comparison
2. Total-value comparison
3. NNA comparison
4. Date comparison
5. Region comparison
6. Advisor comparison
7. Missing-record detection
8. Duplicate detection
9. Value mismatch detection
10. Threshold-based exception detection

RECONCILIATION FORMULA:

difference = source_a_nna - source_b_nna

Exception:

ABS(difference) > 0.01

Return:

records_compared
matched_records
exception_records
total_source_a
total_source_b
total_difference
exception_details

DATA QUALITY CHECKS:

Missing transaction IDs
Duplicate IDs
Missing dates
Invalid dates
Missing region
Missing advisor
Missing client segment
Negative inflows
Negative outflows
Invalid numeric values
Unexpected nulls

Create a validation status:

PASS
WARNING
FAIL

CREATE FASTAPI:

GET /health
GET /api/validation/report
GET /api/reconciliation/report
GET /api/reconciliation/exceptions
GET /api/quality/summary

CREATE SQL QUERIES for every major validation/reconciliation operation.

CREATE PYTEST TESTS proving:

- duplicates are detected
- negative values are detected
- mismatched records are detected
- reconciliation exceptions are detected
- clean data passes validation
- API endpoints work

README MUST explain:

Business problem
Why reconciliation matters
Validation framework
Exception methodology
SQL approach
Python implementation
API
Testing
Architecture

Do not claim this is professional financial-services experience.

State clearly that the project uses synthetic data.

Run all tests before completion.
