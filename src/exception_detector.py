"""
AI Manufacturing Performance Assistant
Manufacturing exception detection module.

This educational prototype uses synthetic production data.
Thresholds are provisional and should be validated before real-world use.
"""

try:
    from .kpi_calculator import load_production_data, calculate_kpis
except ImportError:
    from kpi_calculator import load_production_data, calculate_kpis


def detect_exceptions(kpi_data):
    """
    Detect manufacturing exceptions from one KPI record.

    Expected KPI fields:
    - doc_residual_oil_pct
    - doc_moisture_pct
    - solvent_litres_per_tonne
    - capacity_utilization_pct

    Returns a list of exception messages.
    """
    exceptions = []

    if kpi_data["doc_residual_oil_pct"] > 3.0:
        exceptions.append("HIGH DOC RESIDUAL OIL")

    if kpi_data["doc_moisture_pct"] > 11.0:
        exceptions.append("HIGH DOC MOISTURE")

    if kpi_data["solvent_litres_per_tonne"] > 250.0:
        exceptions.append("HIGH SOLVENT CONSUMPTION")

    if kpi_data["capacity_utilization_pct"] < 50.0:
        exceptions.append("LOW CAPACITY UTILIZATION")

    return exceptions


def detect_exceptions_for_records(kpi_records):
    """
    Detect exceptions across multiple KPI records.

    Returns a list of dictionaries containing each record's date
    and its detected exceptions.
    """
    results = []

    for record in kpi_records:
        exceptions = detect_exceptions(record)

        if exceptions:
            results.append({
                "date": record.get("date", "Unknown"),
                "exceptions": exceptions,
            })

    return results


if __name__ == "__main__":
    print(
        "Exception detector loaded successfully. "
        "Run the automated tests to verify its behaviour."
    )
