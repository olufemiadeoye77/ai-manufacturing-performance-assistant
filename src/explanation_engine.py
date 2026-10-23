
"""
AI Manufacturing Performance Assistant
Manufacturing explanation engine.

Converts detected manufacturing exceptions into explanations
and suggested investigation steps.

Educational prototype using synthetic production data.
Thresholds are provisional and require operational validation.
"""

try:
    from .kpi_calculator import load_production_data, calculate_kpis
    from .exception_detector import detect_exceptions
except ImportError:
    from kpi_calculator import load_production_data, calculate_kpis
    from exception_detector import detect_exceptions


EXCEPTION_GUIDANCE = {
    "HIGH DOC RESIDUAL OIL": {
        "field": "doc_residual_oil_pct",
        "threshold": 3.0,
        "unit": "%",
        "comparison": "above",
        "why_it_matters": (
            "Higher residual oil in de-oiled cake may indicate "
            "that extraction performance needs investigation."
        ),
        "checks": [
            "Review solvent-to-feed ratio and solvent distribution.",
            "Check feed condition and preparation.",
            "Review extractor operation and relevant process readings.",
            "Confirm the laboratory result and sampling method.",
        ],
    },
    "HIGH DOC MOISTURE": {
        "field": "doc_moisture_pct",
        "threshold": 11.0,
        "unit": "%",
        "comparison": "above",
        "why_it_matters": (
            "High de-oiled cake moisture may affect product quality, "
            "storage stability, and downstream handling."
        ),
        "checks": [
            "Review the desolventizer-toaster operating conditions.",
            "Check drying performance and temperature readings.",
            "Review steam supply and material residence time.",
            "Confirm the moisture result using an approved method.",
        ],
    },
    "HIGH SOLVENT CONSUMPTION": {
        "field": "solvent_litres_per_tonne",
        "threshold": 250.0,
        "unit": "L/tonne",
        "comparison": "above",
        "why_it_matters": (
            "Higher solvent use per tonne may increase operating costs "
            "and warrants a review of solvent balance and recovery."
        ),
        "checks": [
            "Verify solvent usage and feed throughput measurements.",
            "Check for leaks or unexplained solvent losses.",
            "Review solvent recovery and condensate systems.",
            "Check inventory, tank levels, and measurement records.",
        ],
    },
    "LOW CAPACITY UTILIZATION": {
        "field": "capacity_utilization_pct",
        "threshold": 50.0,
        "unit": "%",
        "comparison": "below",
        "why_it_matters": (
            "Low utilization means recorded throughput is below "
            "half of the configured rated daily capacity."
        ),
        "checks": [
            "Review actual feed availability and feed quality.",
            "Check downtime, stoppages, and operating hours.",
            "Review bottlenecks and equipment operating conditions.",
            "Confirm the rated capacity and production records.",
        ],
    },
}


def explain_exception(kpi_data, exception):
    """Explain one detected exception using its KPI evidence."""

    if exception not in EXCEPTION_GUIDANCE:
        raise ValueError(f"Unknown exception type: {exception}")

    guidance = EXCEPTION_GUIDANCE[exception]
    field = guidance["field"]

    if field not in kpi_data:
        raise ValueError(f"Missing required KPI field: {field}")

    observed_value = float(kpi_data[field])

    return {
        "date": kpi_data.get("date", "Unknown"),
        "exception": exception,
        "observed_value": observed_value,
        "threshold": guidance["threshold"],
        "unit": guidance["unit"],
        "why_it_matters": guidance["why_it_matters"],
        "recommended_checks": guidance["checks"],
        "note": (
            "This is an investigation guide, not a confirmed root cause. "
            "Thresholds are provisional and should be validated."
        ),
    }


def generate_explanations(kpi_data, exceptions):
    """Generate explanations for all exceptions in one KPI record."""

    return [
        explain_exception(kpi_data, exception)
        for exception in exceptions
    ]


def format_explanation_report(kpi_data, explanations):
    """Format explanations as a readable production report."""

    lines = [
        "MANUFACTURING EXCEPTION EXPLANATION",
        "=" * 42,
        f"Date: {kpi_data.get('date', 'Unknown')}",
        f"Throughput: {kpi_data['throughput_tonnes']:.2f} tonnes",
        "",
    ]

    if not explanations:
        lines.append("No exceptions detected for this record.")
        return "\n".join(lines)

    for number, item in enumerate(explanations, start=1):
        lines.extend([
            f"{number}. {item['exception']}",
            (
                f"   Observed: {item['observed_value']:.2f}"
                f"{item['unit']}"
            ),
            (
                f"   Provisional threshold: "
                f"{item['comparison'] if 'comparison' in item else ''}"
                f"{item['threshold']:.2f}{item['unit']}"
            ),
            f"   Why it matters: {item['why_it_matters']}",
            "   Suggested investigation:",
        ])

        for check in item["recommended_checks"]:
            lines.append(f"   - {check}")

        lines.extend([
            f"   Note: {item['note']}",
            "",
        ])

    return "\n".join(lines)


def main():
    """Run the explanation engine on the supplied synthetic dataset."""

    records = load_production_data()
    print("AI Manufacturing Performance Assistant")
    print("Stage 2: Manufacturing Explanation Engine")
    print("=" * 42)

    for record in records:
        kpi_data = calculate_kpis(record)
        exceptions = detect_exceptions(kpi_data)
        explanations = generate_explanations(kpi_data, exceptions)

        if explanations:
            print()
            print(format_explanation_report(kpi_data, explanations))
            print("-" * 42)


if __name__ == "__main__":
    main()
