
"""
AI Manufacturing Performance Assistant
Stage 4: KPI Dashboard and Data Visualisation

Creates a PNG dashboard from synthetic production data.
Thresholds are provisional examples, not approved plant limits.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from src.kpi_calculator import load_production_data, calculate_kpis
from src.exception_detector import detect_exceptions


PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "reports"
OUTPUT_FILE = OUTPUT_DIR / "manufacturing_kpi_dashboard.png"

RATED_CAPACITY_TPD = 50.0


def collect_dashboard_data():
    """Load production data and calculate KPIs and exceptions."""

    records = load_production_data()

    if not records:
        raise ValueError("No production records were found.")

    results = []

    for record in records:
        kpi = calculate_kpis(record)
        exceptions = detect_exceptions(kpi)

        results.append({
            "kpi": kpi,
            "exceptions": exceptions,
        })

    return results


def create_dashboard():
    """Create and save the manufacturing KPI dashboard."""

    results = collect_dashboard_data()

    dates = [item["kpi"]["date"] for item in results]
    throughput = [
        item["kpi"]["throughput_tonnes"] for item in results
    ]
    utilization = [
        item["kpi"]["capacity_utilization_pct"] for item in results
    ]
    residual_oil = [
        item["kpi"]["doc_residual_oil_pct"] for item in results
    ]
    doc_moisture = [
        item["kpi"]["doc_moisture_pct"] for item in results
    ]
    solvent_rate = [
        item["kpi"]["solvent_litres_per_tonne"] for item in results
    ]

    average_throughput = float(np.mean(throughput))
    average_utilization = float(np.mean(utilization))
    average_solvent = float(np.mean(solvent_rate))

    flagged_records = [
        item for item in results if item["exceptions"]
    ]

    total_exceptions = sum(
        len(item["exceptions"]) for item in results
    )

    # Create a dashboard with four charts and a summary row.
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle(
        "AI Manufacturing Performance Assistant",
        fontsize=18,
        fontweight="bold",
    )

    x = np.arange(len(dates))

    # Chart 1: Throughput and rated daily capacity.
    ax = axes[0, 0]
    ax.bar(x, throughput, label="Actual throughput")
    ax.axhline(
        RATED_CAPACITY_TPD,
        linestyle="--",
        label="Rated capacity (50 t/day)",
    )
    ax.set_title("Daily Production Throughput")
    ax.set_ylabel("Tonnes per day")
    ax.set_xticks(x)
    ax.set_xticklabels(dates, rotation=25, ha="right")
    ax.legend()
    ax.grid(axis="y", alpha=0.25)

    # Chart 2: DOC quality indicators.
    ax = axes[0, 1]
    ax.plot(
        x, residual_oil, marker="o", label="DOC residual oil"
    )
    ax.plot(
        x, doc_moisture, marker="s", label="DOC moisture"
    )
    ax.axhline(
        3.0, linestyle="--", label="Residual oil threshold (3%)"
    )
    ax.axhline(
        11.0, linestyle=":", label="Moisture threshold (11%)"
    )
    ax.set_title("DOC Quality Indicators")
    ax.set_ylabel("Percentage (%)")
    ax.set_xticks(x)
    ax.set_xticklabels(dates, rotation=25, ha="right")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.25)

    # Chart 3: Solvent consumption per tonne.
    ax = axes[1, 0]
    ax.bar(x, solvent_rate, label="Solvent consumption")
    ax.axhline(
        250.0,
        linestyle="--",
        label="Provisional threshold (250 L/tonne)",
    )
    ax.set_title("Specific Solvent Consumption")
    ax.set_ylabel("Litres per tonne")
    ax.set_xticks(x)
    ax.set_xticklabels(dates, rotation=25, ha="right")
    ax.legend(fontsize=8)
    ax.grid(axis="y", alpha=0.25)

    # Chart 4: Capacity utilisation.
    ax = axes[1, 1]
    ax.bar(x, utilization, label="Capacity utilisation")
    ax.axhline(
        50.0,
        linestyle="--",
        label="Provisional threshold (50%)",
    )
    ax.set_title("Daily Capacity Utilisation")
    ax.set_ylabel("Utilisation (%)")
    ax.set_ylim(0, 100)
    ax.set_xticks(x)
    ax.set_xticklabels(dates, rotation=25, ha="right")
    ax.legend(fontsize=8)
    ax.grid(axis="y", alpha=0.25)

    summary = (
        f"Records: {len(results)}     "
        f"Average throughput: {average_throughput:.2f} t/day     "
        f"Average utilisation: {average_utilization:.2f}%     "
        f"Average solvent: {average_solvent:.2f} L/tonne     "
        f"Records flagged: {len(flagged_records)}     "
        f"Exceptions: {total_exceptions}"
    )

    fig.text(
        0.5,
        0.025,
        summary,
        ha="center",
        fontsize=9,
        wrap=True,
    )

    fig.text(
        0.5,
        0.005,
        "Synthetic data. Thresholds are provisional and require validation.",
        ha="center",
        fontsize=8,
    )

    fig.tight_layout(rect=[0, 0.07, 1, 0.94])

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_FILE, dpi=160, bbox_inches="tight")
    plt.close(fig)

    print("Dashboard generated successfully.")
    print(f"Production records analysed: {len(results)}")
    print(f"Records requiring review: {len(flagged_records)}")
    print(f"Total exceptions detected: {total_exceptions}")
    print(f"Dashboard saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    create_dashboard()
