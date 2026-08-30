# Data Reconciliation & Validation

An independent analytics engineering portfolio project demonstrating data reconciliation, validation, exception detection, comparison, and reporting controls using synthetic financial-services-style data.

## Business Problem

Reporting teams often receive data from multiple sources. Before management reporting is distributed, analysts need to validate the data, compare sources, identify exceptions, and investigate discrepancies.

This project simulates that workflow using two synthetic reporting sources.

## What This Project Demonstrates

- Data reconciliation
- Data validation
- Source-to-source comparison
- Exception detection
- Data-quality controls
- KPI validation
- SQL analysis
- Python/Pandas
- REST API development
- Automated testing
- Reporting controls

## Reconciliation Methodology

The project compares Source A and Source B using:

- Date
- Region
- Advisor
- Client segment
- NNA

The core calculation is:

`Difference = Source A NNA - Source B NNA`

A record is flagged as an exception when:

`ABS(Difference) > 0.01`

## Validation Checks

The validation framework checks for:

- Missing transaction IDs
- Duplicate transaction IDs
- Missing dates
- Invalid dates
- Missing regions
- Missing advisors
- Missing client segments
- Negative inflows
- Negative outflows
- Invalid numeric values
- Unexpected null values
- Record-count differences
- Reporting-total differences

## Project Architecture

```text
Reporting Sources
       |
       v
Data Validation
       |
       v
Source Comparison
       |
       v
Reconciliation Engine
       |
       +----> Matched Records
       |
       +----> Exceptions
       |
       v
Management Reporting
       |
       v
FastAPI
