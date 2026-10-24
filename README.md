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

## Stage 4: KPI Dashboard and Data Visualisation

The project includes a Python-based dashboard that visualises synthetic manufacturing production data.

### Dashboard features

- Daily production throughput compared with rated capacity.
- DOC residual oil and moisture indicators.
- Specific solvent consumption in litres per tonne.
- Daily capacity utilisation.
- Summary of records requiring review and detected exceptions.

### Generate the dashboard

Install Matplotlib if it is not already installed:

```bash
python -m pip install matplotlib
```

Run the dashboard from the project root:

```bash
python -m src.dashboard
```

The dashboard image is generated at:

`reports/manufacturing_kpi_dashboard.png`

### Run automated tests

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

The current test suite contains 21 automated tests.

### Important limitations

The dataset contains synthetic production records. Thresholds are provisional examples and must be validated against approved plant specifications before operational use. The dashboard supports monitoring and investigation; it does not independently diagnose process faults.

## Stage 5: Structured Investigation Recommendations

The project includes a rule-based recommendation engine that provides
structured investigation guidance for detected manufacturing KPI
exceptions.

### Features

- Assigns High or Medium priority to detected exceptions.
- Lists possible causes for investigation.
- Suggests recommended checks.
- Identifies evidence that should be collected.
- Integrates recommendations into the generated management report.
- Includes automated tests for recommendation generation and report integration.

### Supported exceptions

- High DOC residual oil.
- High DOC moisture.
- High solvent consumption.
- Low capacity utilization.

### Generate the management report

From the project root, run:

```bash
python -m src.management_report
```

The report is generated at:

`reports/management_report.md`

### Run automated tests

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

**Current test status:** 35 automated tests passed.

### Important limitations

Recommendations are rule-based investigation guidance. Possible causes
are not confirmed diagnoses. Production data is synthetic, and all
thresholds require validation against approved plant specifications
before operational use. Human review and approved plant procedures
remain essential.


## Stage 5: Recommendation Engine and Management Reporting

The project now includes a rule-based recommendation engine and an automated management report.

### Recommendation Engine
- Generates suggested checks for high DOC residual oil.
- Flags high DOC moisture.
- Recommends investigation of high solvent consumption.
- Supports review of low capacity utilization.

Recommendations are guidance for investigation and are not confirmed diagnoses.

### Management Reporting
The report combines KPIs, detected exceptions, explanations, and recommendations.

Report location: `reports/management_report.md`

The latest recorded run analyzed five synthetic records, identified one record requiring review, and detected four exceptions.

### Automated Testing
The latest recorded test run passed all 35 tests.

Run the tests with:

`python -m unittest discover -s tests -p "test_*.py" -v`

### Limitations
This is an educational decision-support prototype using synthetic data. Recommendations require qualified human review. The application is not connected to live plant systems, PLCs, SCADA, or enterprise production databases.




## Stage 6: Manufacturing What-If Scenario Analysis

This stage introduces a Python module for comparing recorded solvent consumption with a proposed operating target.

### Features
- Calculates current solvent consumption in litres per tonne.
- Estimates target solvent requirements at the same throughput.
- Calculates potential solvent savings in litres.
- Calculates the percentage reduction against recorded solvent use.
- Supports optional cost-savings estimates when a cost per litre is supplied.
- Rejects invalid inputs, including zero throughput and negative solvent consumption.

### Example Scenario
- Throughput: 25 tonnes
- Recorded solvent use: 5,000 litres
- Current consumption: 200 L/t
- Proposed target: 180 L/t
- Potential solvent savings: 500 litres
- Potential reduction: 10%

These are illustrative scenario estimates, not guaranteed or verified plant savings.

### Files
- `src/scenario_analysis.py` — scenario calculation module.
- `tests/test_scenario_analysis.py` — automated tests.
- `results_scenario.txt` — saved example output.

### Run the Scenario
`python src/scenario_analysis.py`

### Run the Tests
`python -m unittest discover -s tests -p "test_*.py" -v`

### Limitations
The scenario analysis is an educational decision-support tool. Actual savings depend on operating conditions, solvent losses, process performance, and verified plant data. Any proposed target should be assessed and approved by qualified plant personnel.



## Stage 6: Manufacturing What-If Scenario Analysis

This stage introduces a Python module for comparing recorded solvent consumption with a proposed operating target.

### Features
- Calculates current solvent consumption in litres per tonne.
- Estimates target solvent requirements at the same throughput.
- Calculates potential solvent savings in litres.
- Calculates the percentage reduction against recorded solvent use.
- Supports optional cost-savings estimates when a cost per litre is supplied.
- Rejects invalid inputs, including zero throughput and negative solvent consumption.

### Example Scenario
- Throughput: 25 tonnes
- Recorded solvent use: 5,000 litres
- Current consumption: 200 L/t
- Proposed target: 180 L/t
- Potential solvent savings: 500 litres
- Potential reduction: 10%

These are illustrative scenario estimates, not guaranteed or verified plant savings.

### Files
- `src/scenario_analysis.py` — scenario calculation module.
- `tests/test_scenario_analysis.py` — automated tests.
- `results_scenario.txt` — saved example output.

### Run the Scenario
`python src/scenario_analysis.py`

### Run the Tests
`python -m unittest discover -s tests -p "test_*.py" -v`

### Limitations
The scenario analysis is an educational decision-support tool. Actual savings depend on operating conditions, solvent losses, process performance, and verified plant data. Any proposed target should be assessed and approved by qualified plant personnel.



## Stage 6: Manufacturing What-If Scenario Analysis

This stage introduces a Python module for comparing recorded solvent consumption with a proposed operating target.

### Features
- Calculates current solvent consumption in litres per tonne.
- Estimates target solvent requirements at the same throughput.
- Calculates potential solvent savings in litres.
- Calculates the percentage reduction against recorded solvent use.
- Supports optional cost-savings estimates when a cost per litre is supplied.
- Rejects invalid inputs, including zero throughput and negative solvent consumption.

### Example Scenario
- Throughput: 25 tonnes
- Recorded solvent use: 5,000 litres
- Current consumption: 200 L/t
- Proposed target: 180 L/t
- Potential solvent savings: 500 litres
- Potential reduction: 10%

These are illustrative scenario estimates, not guaranteed or verified plant savings.

### Files
- `src/scenario_analysis.py` — scenario calculation module.
- `tests/test_scenario_analysis.py` — automated tests.
- `results_scenario.txt` — saved example output.

### Run the Scenario
`python src/scenario_analysis.py`

### Run the Tests
`python -m unittest discover -s tests -p "test_*.py" -v`

### Limitations
The scenario analysis is an educational decision-support tool. Actual savings depend on operating conditions, solvent losses, process performance, and verified plant data. Any proposed target should be assessed and approved by qualified plant personnel.
