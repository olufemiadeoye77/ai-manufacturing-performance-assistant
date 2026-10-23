
"""
AI Manufacturing Performance Assistant
Version 0.3 — Manufacturing Explanation Engine

Uses synthetic production data.
Thresholds are provisional examples and must be validated
against approved plant operating limits before real-world use.
"""

try:
    from .kpi_calculator import load_production_data, calculate_kpis
    from .exception_detector import detect_exceptions
except ImportError:
    from kpi_calculator import load_production_data, calculate_kpis
    from exception_detector import detect_exceptions


# Keep these thresholds consistent with exception_detector.py.
EXCEPTION_GUIDANCE = {
    "HIGH DOC RESIDUAL OIL": {
        "field": "doc_residual_oil_pct",
        "threshold": 3.0,
        "unit": "%",
        "comparison": "above",
        "why_it_matters": (
            "High residual oil in de-oiled cake may indicate that "
            "extraction performance needs investigation."
        ),
        "checks": [
            "Verify the laboratory result and sampling method.",
            "Review solvent-to-feed ratio and solvent distribution.",
            "Check feed preparation and material condition.",
            "Review extractor operating conditions.",
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
            "Verify the moisture result and sampling method.",
            "Review desolventizer-toaster operating conditions.",
            "Check drying performance and relevant temperature readings.",
            "Review steam supply and material residence time.",
        ],
    },
    "HIGH SOLVENT CONSUMPTION": {
        "field": "solvent_litres_per_tonne",
        "threshold": 250.0,
        "unit": "L/tonne",
        "comparison": "above",
        "why_it_matters": (
            "High solvent consumption per tonne may increase operating "
            "costs and warrants investigation of solvent usage and recovery."
        ),
        "checks": [
            "Verify solvent usage and throughput measurements.",
            "Review solvent inventory and tank-level records.",
            "Check for leaks or unexplained solvent losses.",
            "Review solvent recovery system performance.",
        ],
    },
    "LOW CAPACITY UTILIZATION": {
        "field": "capacity_utilization_pct",
        "threshold": 50.0,
        "unit": "%",
        "comparison": "below",
        "why_it_matters": (
            "Low capacity utilization means recorded throughput is below "
            "half of the configured rated daily capacity."
        ),
        "checks": [
            "Verify the plant's rated daily capacity.",
            "Review feed availability and feed quality.",
            "Check operating hours, downtime, and stoppages.",
            "Investigate equipment bottlenecks and process constraints.",
        ],
    },
}


def explain_exception(kpi_data, exception):
    """Return an explanation for one detected exception."""

    if exception not in EXCEPTION_GUIDANCE:
        raise ValueError(f"Unknown exception type: {exception}")

    guidance = EXCEPTION_GUIDANCE[exception]
    field = guidance["field"]

    if field not in kpi_data:
        raise ValueError(f"Missing required KPI field: {field}")

    observed_value = float(kpi_data[field])
    threshold = guidance["threshold"]
    comparison = guidance["comparison"]

    return {
        "date": kpi_data.get("date", "Unknown"),
        "exception": exception,
        "field": field,
        "observed_value": observed_value,
        "threshold": threshold,
        "comparison": comparison,
        "unit": guidance["unit"],
        "why_it_matters": guidance["why_it_matters"],
        "recommended_checks": guidance["checks"],
        "note": (
            "This is an investigation guide, not a confirmed root cause. "
            "Thresholds are provisional and require operational validation."
        ),
    }


def generate_explanations(kpi_data, exceptions):
    """Generate explanations for all exceptions in a KPI record."""

    return [
        explain_exception(kpi_data, exception)
        for exception in exceptions
    ]


def format_explanation_report(kpi_data, explanations):
    """Create a readable report for one production record."""

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
                f"   Threshold: {item['comparison']} "
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
    """Run the explanation engine against the sample dataset."""

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
