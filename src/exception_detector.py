"""
AI Manufacturing Performance Assistant
Stage 7: Configurable production exception detection.

This educational prototype uses sample production data.
Thresholds are provisional and must be validated before operational use.
"""


DEFAULT_THRESHOLDS = {
    "doc_residual_oil_pct_max": 3.0,
    "doc_moisture_pct_max": 11.0,
    "solvent_litres_per_tonne_max": 250.0,
    "capacity_utilization_pct_min": 50.0,
}


def detect_exceptions(kpi_data, thresholds=None):
    """
    Detect manufacturing exceptions from one KPI record.

    Optional thresholds override the default limits.
    Returns a list of exception messages.
    """
    limits = DEFAULT_THRESHOLDS.copy()

    if thresholds is not None:
        unknown = set(thresholds) - set(limits)
        if unknown:
            raise ValueError(
                f"Unknown threshold(s): {', '.join(sorted(unknown))}"
            )
        limits.update(thresholds)

    exceptions = []

    if (
        kpi_data["doc_residual_oil_pct"]
        > limits["doc_residual_oil_pct_max"]
    ):
        exceptions.append("HIGH DOC RESIDUAL OIL")

    if (
        kpi_data["doc_moisture_pct"]
        > limits["doc_moisture_pct_max"]
    ):
        exceptions.append("HIGH DOC MOISTURE")

    if (
        kpi_data["solvent_litres_per_tonne"]
        > limits["solvent_litres_per_tonne_max"]
    ):
        exceptions.append("HIGH SOLVENT CONSUMPTION")

    if (
        kpi_data["capacity_utilization_pct"]
        < limits["capacity_utilization_pct_min"]
    ):
        exceptions.append("LOW CAPACITY UTILIZATION")

    return exceptions


def detect_exceptions_for_records(kpi_records, thresholds=None):
    """Return dated exception results for records with alerts."""
    results = []

    for record in kpi_records:
        exceptions = detect_exceptions(record, thresholds)

        if exceptions:
            results.append({
                "date": record.get("date", "Unknown"),
                "exceptions": exceptions,
            })

    return results


if __name__ == "__main__":
    print("Stage 7: Configurable exception detector loaded.")
    print("Run the automated tests to verify its behaviour.")
