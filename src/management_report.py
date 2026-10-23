
from pathlib import Path
import sys

# Locate the project root and make it available for imports.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.kpi_calculator import load_production_data, calculate_kpis
from src.exception_detector import detect_exceptions

REPORT_FILE = PROJECT_ROOT / "reports" / "management_report.md"


def generate_report():
    records = load_production_data()

    if not records:
        raise ValueError("No production records were found.")

    results = []

    for record in records:
        kpi = calculate_kpis(record)
        alerts = detect_exceptions(kpi)
        results.append((kpi, alerts))

    count = len(results)

    average_throughput = sum(
        kpi["throughput_tonnes"] for kpi, _ in results
    ) / count

    average_utilization = sum(
        kpi["capacity_utilization_pct"] for kpi, _ in results
    ) / count

    average_solvent = sum(
        kpi["solvent_litres_per_tonne"] for kpi, _ in results
    ) / count

    flagged_records = [
        (kpi, alerts) for kpi, alerts in results if alerts
    ]

    lines = [
        "# Manufacturing Performance Management Report",
        "",
        "## 1. Purpose",
        "",
        "This report analyzes synthetic manufacturing data using "
        "Python-calculated KPIs and provisional exception rules.",
        "",
        "## 2. Overall Summary",
        "",
        f"- Production records analyzed: {count}",
        f"- Average throughput: {average_throughput:.2f} tonnes/day",
        f"- Average capacity utilization: {average_utilization:.2f}%",
        f"- Average solvent consumption: {average_solvent:.2f} L/tonne",
        f"- Records requiring review: {len(flagged_records)}",
        "",
        "## 3. Daily Findings",
        "",
        "| Date | Throughput (t) | Utilization (%) | "
        "DOC residual oil (%) | DOC moisture (%) | Solvent (L/t) | Status |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]

    for kpi, alerts in results:
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
        lines.append("No exceptions were detected using the current rules.")
    else:
        for kpi, alerts in flagged_records:
            lines.append(f"### {kpi['date']}")
            for alert in alerts:
                lines.append(f"- {alert}")
            lines.append("")

    lines.extend([
        "## 5. Management Follow-up",
        "",
        "- Verify flagged measurements and confirm data quality.",
        "- Review DOC residual oil against approved product specifications.",
        "- Investigate moisture readings against approved process limits.",
        "- Check solvent usage, throughput records, and possible losses.",
        "- Review capacity utilization against the operating plan.",
        "- Record findings and corrective actions after human review.",
        "",
        "## 6. Limitations",
        "",
        "All data in this demonstration is synthetic. Thresholds are "
        "provisional examples, not approved plant limits. Alerts identify "
        "records for review; they do not prove that a process fault occurred. "
        "This report is not a substitute for plant procedures or safety controls.",
        "",
    ])

    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")

    print("Management report generated successfully.")
    print(f"Records analyzed: {count}")
    print(f"Records requiring review: {len(flagged_records)}")
    print(f"Report saved to: {REPORT_FILE}")


if __name__ == "__main__":
    generate_report()
