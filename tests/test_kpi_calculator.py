
import unittest

from src.kpi_calculator import calculate_kpis


class TestKPICalculator(unittest.TestCase):

    def setUp(self):
        self.record = {
            "date": "2026-10-19",
            "throughput_tonnes": "25",
            "doc_residual_oil_pct": "2.8",
            "doc_moisture_pct": "9.5",
            "pkc_oil_pct": "14.5",
            "pkc_moisture_pct": "8.8",
            "solvent_used_litres": "5000",
        }

    def test_capacity_utilization(self):
        result = calculate_kpis(self.record)
        self.assertEqual(result["capacity_utilization_pct"], 50.0)

    def test_solvent_consumption(self):
        result = calculate_kpis(self.record)
        self.assertEqual(result["solvent_litres_per_tonne"], 200.0)

    def test_date_is_preserved(self):
        result = calculate_kpis(self.record)
        self.assertEqual(result["date"], "2026-10-19")

    def test_zero_throughput_is_rejected(self):
        record = self.record.copy()
        record["throughput_tonnes"] = "0"

        with self.assertRaises(ValueError):
            calculate_kpis(record)


if __name__ == "__main__":
    unittest.main()
