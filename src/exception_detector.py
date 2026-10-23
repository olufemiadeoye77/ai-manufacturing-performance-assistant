from kpi_calculator import load_production_data, calculate_kpis


def detect_exceptions(kpi):
    alerts = []

    if kpi["doc_residual_oil_pct"] > 3.0:
        alerts.append("HIGH DOC RESIDUAL OIL")

    if kpi["doc_moisture_pct"] > 11.0:
        alerts.append("HIGH DOC MOISTURE")

    if kpi["solvent_litres_per_tonne"] > 250.0:
        alerts.append("HIGH SOLVENT CONSUMPTION")

    if kpi["capacity_utilization_pct"] < 50.0:
        alerts.append("LOW CAPACITY UTILIZATION")

    return alerts


def main():
    records = load_production_data()

    print("AI Manufacturing Performance Assistant")
    print("EXCEPTION DETECTION REPORT")
    print("=" * 45)

    for record in records:
        kpi = calculate_kpis(record)
        alerts = detect_exceptions(kpi)

        print(f"\nDate: {kpi['date']}")

        if alerts:
            print("Status: REVIEW REQUIRED")
            for alert in alerts:
                print(f"- {alert}")
        else:
            print("Status: No exceptions detected")

    print("\nException detection completed.")


if __name__ == "__main__":
    main()
