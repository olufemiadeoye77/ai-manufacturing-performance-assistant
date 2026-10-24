
"""
Stage 7: Production KPI Monitoring and Exception Reporting.

Uses existing KPI, exception detection, and explanation modules.
Sample data and default thresholds are illustrative only.
"""

from pathlib import Path

from src.kpi_calculator import load_production_data, calculate_kpis
from src.exception_detector import detect_exceptions
from src.explanation_engine import generate_explanations


PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPORT_DIR = PROJECT_ROOT / "reports"
REPORT_FILE = REPORT_DIR / "production_exception_report.md"


def monitor_production(records=None, thresholds=None):
    """Calculate KPIs and detect and explain exceptions."""

    if records is None:
        records = load_production_data()

    if not records:
        raise ValueError("No production records were provided.")

    results = []

    for record in records:
        kpi = calculate_kpis(record)
        exceptions = detect_exceptions(kpi, thresholds)
        explanations = generate_explanations(kpi, exceptions)

        results.append({
            "kpi": kpi,
            "exceptions": exceptions,
            "explanations": explanations,
        })

    return results


def build_monitoring_report(results):
    """Format the monitoring results as a Markdown report."""

    flagged = [item for item in results if item["exceptions"]]
    total_exceptions = sum(
        len(item["exceptions"]) for item in results
    )

    lines = [
        "# Production KPI Monitoring and Exception Report",
        "",
        "## Summary",
        "",
        f"- Production records analysed: {len(results)}",
        f"- Records requiring review: {len(flagged)}",
        f"- Total exceptions detected: {total_exceptions}",
        "",
        "## Record-by-record results",
        "",
    ]

    for item in results:
        kpi = item["kpi"]
        exceptions = item["exceptions"]

        lines.extend([
            f"### {kpi['date']}",
            "",
            f"- Throughput: {kpi['throughput_tonnes']:.2f} tonnes",
            f"- Capacity utilisation: {kpi['capacity_utilization_pct']:.2f}%",
            f"- DOC residual oil: {kpi['doc_residual_oil_pct']:.2f}%",
            f"- DOC moisture: {kpi['doc_moisture_pct']:.2f}%",
            f"- Solvent consumption: {kpi['solvent_litres_per_tonne']:.2f} L/t",
            "",
        ])

        if exceptions:
            lines.extend([
                "**Status: REVIEW REQUIRED**",
                "",
                "Exceptions:",
            ])

            for exception in exceptions:
                lines.append(f"- {exception}")

            lines.extend(["", "Investigation guidance:", ""])

            for explanation in item["explanations"]:
                lines.extend([
                    f"### {explanation['exception']}",
                    "",
                    f"- Why it matters: {explanation['why_it_matters']}",
                    "- Suggested checks:",
                ])

                for check in explanation["recommended_checks"]:
                    lines.append(f"  - {check}")

                lines.extend([
                    f"- Note: {explanation['note']}",
                    "",
                ])
        else:
            lines.extend([
                "**Status: No configured exceptions detected**",
                "",
            ])

    lines.extend([
        "## Important limitations",
        "",
        "- This report supports investigation; it does not diagnose root causes.",
        "- Default thresholds are provisional and require plant validation.",
        "- Verify flagged readings against reliable operating records.",
        "- No alert does not guarantee that a process is safe or optimal.",
        "- The sample data is illustrative, not verified plant performance.",
        "",
    ])

    return "\n".join(lines)


def generate_monitoring_report(thresholds=None):
    """Analyse production records and save the monitoring report."""

    results = monitor_production(thresholds=thresholds)
    report = build_monitoring_report(results)

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text(report + "\n", encoding="utf-8")

    flagged_count = sum(
        1 for item in results if item["exceptions"]
    )
    total_exceptions = sum(
        len(item["exceptions"]) for item in results
    )

    print("Production monitoring report generated.")
    print(f"Records analysed: {len(results)}")
    print(f"Records requiring review: {flagged_count}")
    print(f"Total exceptions: {total_exceptions}")
    print(f"Report saved to: {REPORT_FILE}")

    return results


if __name__ == "__main__":
    generate_monitoring_report()
