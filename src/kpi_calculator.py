import csv
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "sample_production.csv"


def load_production_data(file_path=DATA_FILE):
    """Load production records from a CSV file."""
    with open(file_path, "r", newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        records = list(reader)

    if not records:
        raise ValueError("The production dataset contains no records.")

    return records


def calculate_kpis(record, rated_capacity_tpd=50):
    """Calculate key performance indicators for one production record."""
    throughput = float(record["throughput_tonnes"])
    solvent_used = float(record["solvent_used_litres"])
    residual_oil = float(record["doc_residual_oil_pct"])
    doc_moisture = float(record["doc_moisture_pct"])

    if rated_capacity_tpd <= 0:
        raise ValueError("Rated capacity must be greater than zero.")

    if throughput <= 0:
        raise ValueError("Throughput must be greater than zero.")

    if solvent_used < 0:
        raise ValueError("Solvent usage cannot be negative.")

    if not 0 <= residual_oil <= 100:
        raise ValueError("Residual oil percentage must be between 0 and 100.")

    if not 0 <= doc_moisture <= 100:
        raise ValueError("DOC moisture percentage must be between 0 and 100.")

    return {
        "date": record["date"],
        "throughput_tonnes": throughput,
        "capacity_utilization_pct": round(
            throughput / rated_capacity_tpd * 100, 2
        ),
        "doc_residual_oil_pct": residual_oil,
        "doc_moisture_pct": doc_moisture,
        "solvent_used_litres": solvent_used,
        "solvent_litres_per_tonne": round(
            solvent_used / throughput, 2
        ),
    }


def main():
    records = load_production_data()

    print("AI Manufacturing Performance Assistant")
    print("=" * 45)
    print(f"Production records loaded: {len(records)}")
    print()

    for record in records:
        kpi = calculate_kpis(record)

        print(f"Date: {kpi['date']}")
        print(f"Throughput: {kpi['throughput_tonnes']:.1f} tonnes")
        print(
            "Capacity utilization: "
            f"{kpi['capacity_utilization_pct']:.2f}%"
        )
        print(f"DOC residual oil: {kpi['doc_residual_oil_pct']:.2f}%")
        print(f"DOC moisture: {kpi['doc_moisture_pct']:.2f}%")
        print(
            "Solvent consumption: "
            f"{kpi['solvent_litres_per_tonne']:.2f} L/tonne"
        )
        print("-" * 45)


if __name__ == "__main__":
    main()
