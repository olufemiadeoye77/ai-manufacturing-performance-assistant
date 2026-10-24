
from pathlib import Path
import sys

# Locate the project root and make it available for imports.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.kpi_calculator import load_production_data, calculate_kpis
from src.exception_detector import detect_exceptions
from src.explanation_engine import generate_explanations
from src.recommendation_engine import generate_recommendations

REPORT_FILE = PROJECT_ROOT / "reports" / "management_report.md"


def generate_report():
    """Generate a management report with KPIs, exceptions, and explanations."""

    records = load_production_data()

    if not records:
        raise ValueError("No production records were found.")

    results = []

    for record in records:
        kpi = calculate_kpis(record)
        alerts = detect_exceptions(kpi)
        explanations = generate_explanations(kpi, alerts)
        recommendations = generate_recommendations(alerts)

        results.append({
            "kpi": kpi,
            "alerts": alerts,
            "explanations": explanations,
            "recommendations": recommendations,
        })

    count = len(results)

    average_throughput = sum(
        item["kpi"]["throughput_tonnes"] for item in results
    ) / count

    average_utilization = sum(
        item["kpi"]["capacity_utilization_pct"] for item in results
    ) / count

    # Arithmetic mean of the daily L/tonne values.
    average_daily_solvent_rate = sum(
        item["kpi"]["solvent_litres_per_tonne"] for item in results
    ) / count

    flagged_records = [
        item for item in results if item["alerts"]
    ]

    total_exceptions = sum(
        len(item["alerts"]) for item in results
    )

    lines = [
        "# Manufacturing Performance Management Report",
        "",
        "## 1. Purpose",
        "",
        "This report analyzes synthetic manufacturing data using "
        "Python-calculated KPIs, provisional exception rules, and a "
        "rule-based explanation engine.",
        "",
        "The explanations suggest areas for investigation. They do not "
        "identify confirmed root causes.",
        "",
        "## 2. Overall Summary",
        "",
        f"- Production records analyzed: {count}",
        f"- Average throughput: {average_throughput:.2f} tonnes/day",
        f"- Average capacity utilization: {average_utilization:.2f}%",
        (
            "- Average daily solvent consumption rate: "
            f"{average_daily_solvent_rate:.2f} L/tonne"
        ),
        f"- Records requiring review: {len(flagged_records)}",
        f"- Total exceptions detected: {total_exceptions}",
        "",
        "## 3. Daily Findings",
        "",
        "| Date | Throughput (t) | Utilization (%) | "
        "DOC residual oil (%) | DOC moisture (%) | Solvent (L/t) | Status |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]

    for item in results:
        kpi = item["kpi"]
        alerts = item["alerts"]

        status = "REVIEW REQUIRED" if alerts else "No exception detected"

        lines.append(
            f"| {kpi['date']} "
            f"| {kpi['throughput_tonnes']:.2f} "
            f"| {kpi['capacity_utilization_pct']:.2f} "
            f"| {kpi['doc_residual_oil_pct']:.2f} "
            f"| {kpi['doc_moisture_pct']:.2f} "
            f"| {kpi['solvent_litres_per_tonne']:.2f} "
            f"| {status} |"
        )

    lines.extend([
        "",
        "## 4. Exceptions Requiring Review",
        "",
    ])

    if not flagged_records:
        lines.append(
            "No exceptions were detected using the current provisional rules."
        )
    else:
        for item in flagged_records:
            kpi = item["kpi"]

            lines.append(f"### {kpi['date']}")
            lines.append("")
            lines.append(
                f"**Throughput:** {kpi['throughput_tonnes']:.2f} tonnes"
            )
            lines.append("")

            for alert in item["alerts"]:
                lines.append(f"- {alert}")

            lines.append("")

    lines.extend([
        "## 5. Explanations and Recommended Investigations",
        "",
    ])

    if not flagged_records:
        lines.append("No investigation recommendations were generated.")
        lines.append("")
    else:
        for item in flagged_records:
            kpi = item["kpi"]

            lines.append(f"### {kpi['date']}")
            lines.append("")

            for explanation in item["explanations"]:
                lines.append(f"#### {explanation['exception']}")
                lines.append("")

                lines.append(
                    f"- **Observed value:** "
                    f"{explanation['observed_value']:.2f}"
                    f"{explanation['unit']}"
                )
                lines.append(
                    f"- **Provisional threshold:** "
                    f"{explanation['comparison']} "
                    f"{explanation['threshold']:.2f}"
                    f"{explanation['unit']}"
                )
                lines.append(
                    f"- **Why it matters:** "
                    f"{explanation['why_it_matters']}"
                )
                lines.append("")
                lines.append("**Suggested investigation:**")
                lines.append("")

                for check in explanation["recommended_checks"]:
                    lines.append(f"- {check}")

                lines.append("")
                lines.append(
                    f"> **Caution:** {explanation['note']}"
                )
                lines.append("")

    lines.extend([
        "## 6. Structured Investigation Recommendations",
        "",
        "The following recommendations are generated from the detected "
        "exceptions. Possible causes require verification and are not "
        "confirmed diagnoses.",
        "",
    ])

    if not flagged_records:
        lines.append("No investigation recommendations were generated.")
        lines.append("")
    else:
        for item in flagged_records:
            kpi = item["kpi"]

            lines.append(f"### Production date: {kpi['date']}")
            lines.append("")

            for recommendation in item["recommendations"]:
                lines.append(
                    f"#### {recommendation['exception']}"
                )
                lines.append("")
                lines.append(
                    f"**Priority:** {recommendation['priority']}"
                )
                lines.append("")

                lines.append("**Possible causes to investigate:**")
                lines.append("")
                for cause in recommendation["possible_causes"]:
                    lines.append(f"- {cause}")
                lines.append("")

                lines.append("**Recommended checks:**")
                lines.append("")
                for check in recommendation["recommended_checks"]:
                    lines.append(f"- {check}")
                lines.append("")

                lines.append("**Evidence to collect:**")
                lines.append("")
                for evidence in recommendation["evidence_to_collect"]:
                    lines.append(f"- {evidence}")
                lines.append("")


    lines.extend([
        "## 7. Management Follow-up",
        "",
        "- Verify flagged measurements and confirm data quality.",
        "- Compare results with approved product specifications and "
        "validated operating limits.",
        "- Review process records and investigate potential causes.",
        "- Document findings and corrective actions after human review.",
        "- Confirm any proposed operational change through the plant's "
        "approved procedures.",
        "",
        "## 8. Limitations",
        "",
        "All production data in this demonstration is synthetic. "
        "Thresholds are provisional examples, not approved plant limits. "
        "The explanations are rule-based investigation guidance, not "
        "AI-verified diagnoses or proof of process failure.",
        "",
        "The report is not a substitute for plant procedures, qualified "
        "engineering judgment, or safety controls. Validate all thresholds, "
        "calculations, and recommendations before using real plant data.",
        "",
    ])

    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")

    print("Management report generated successfully.")
    print(f"Records analyzed: {count}")
    print(f"Records requiring review: {len(flagged_records)}")
    print(f"Total exceptions detected: {total_exceptions}")
    print(f"Report saved to: {REPORT_FILE}")


if __name__ == "__main__":
    generate_report()
