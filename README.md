# AI Manufacturing Performance Assistant

**A Python-based manufacturing KPI analysis and exception detection prototype.**

## 1. Project Overview

This project demonstrates how production data can be processed to calculate key performance indicators (KPIs), identify potential operational exceptions, and prepare a management summary.

It is designed around a fictional solvent extraction manufacturing scenario using synthetic production data. It is an educational portfolio project and is not connected to a live plant or production control system.

## 2. Project Objectives

- Calculate production capacity utilization.
- Calculate solvent consumption per tonne processed.
- Review DOC residual oil and DOC moisture values.
- Flag records that exceed provisional review thresholds.
- Generate a management-oriented performance report.
- Demonstrate Python programming, data analysis, automated testing, and industrial process knowledge.

## 3. Project Structure

```text
ai-manufacturing-performance-assistant/
├── data/
│   └── sample_production.csv
├── src/
│   ├── __init__.py
│   ├── kpi_calculator.py
│   ├── exception_detector.py
│   └── management_report.py
├── tests/
│   ├── test_kpi_calculator.py
│   └── test_exception_detector.py
├── reports/
│   └── management_report.md
├── results_kpi.txt
├── exception_report.txt
├── README.md
├── .gitignore
└── requirements.txt
```

Some files will appear as the project develops.

## 4. Technology

- Python 3
- CSV data processing
- Python standard-library `unittest`
- Markdown reporting
- GitHub for version control and portfolio publication

No third-party Python packages are required for the current prototype.

## 5. Key Performance Indicators

**Capacity utilization**

Throughput divided by rated daily capacity, multiplied by 100.

The demonstration uses a rated capacity of 50 tonnes per day.

**Solvent consumption**

Solvent used in litres divided by throughput in tonnes.

The output is expressed in litres per tonne processed.

## 6. Provisional Exception Rules

| Indicator | Rule for review |
|---|---|
| DOC residual oil | Above 3.0% |
| DOC moisture | Above 11.0% |
| Solvent consumption | Above 250 L/tonne |
| Capacity utilization | Below 50% |

These thresholds are configurable demonstration assumptions, not approved plant operating limits. Actual limits must be validated against plant procedures, product specifications, and engineering requirements.

## 7. How to Run

Open CMD in the project root directory.

Run the KPI calculator:

```cmd
python src\kpi_calculator.py
```

Run exception detection:

```cmd
python src\exception_detector.py
```

Generate the management report:

```cmd
python src\management_report.py
```

Run automated tests:

```cmd
python -m unittest discover -s tests -p "test_*.py" -v
```

## 8. Outputs

- `results_kpi.txt` — saved KPI calculation output.
- `exception_report.txt` — saved exception detection output.
- `reports/management_report.md` — management summary generated from the sample dataset.

The report should be regenerated after the underlying data or calculation rules change.

## 9. Safety and Limitations

- All sample records are synthetic.
- The program is a decision-support demonstration, not a certified process monitoring system.
- Exception flags indicate records requiring review; they do not prove that a process fault has occurred.
- Recommendations should be checked by qualified personnel before operational action.
- The current version does not connect to plant control systems, PLCs, SCADA, or a live enterprise database.

## 10. Future Development

- Add more data validation and automated tests.
- Improve management reporting and visualizations.
- Add AI-assisted explanations with human review.
- Explore secure integration with cloud services and manufacturing data systems.

## 11. Project Status

**Prototype in development.** Features and test results should be verified against the current repository before being described as complete.

## 12. Author and Repository

Author: Olufemi Adeoye

Repository: https://github.com/olufemiadeoye77/ai-manufacturing-performance-assistant
