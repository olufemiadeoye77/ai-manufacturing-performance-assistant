
import unittest

from src.exception_detector import detect_exceptions


class TestExceptionDetector(unittest.TestCase):

    def make_kpi(self, **overrides):
        kpi = {
            "date": "2026-10-19",
            "throughput_tonnes": 25.0,
            "capacity_utilization_pct": 50.0,
            "doc_residual_oil_pct": 2.8,
            "doc_moisture_pct": 9.5,
            "solvent_litres_per_tonne": 200.0,
        }
        kpi.update(overrides)
        return kpi

    def test_normal_record_has_no_alerts(self):
        result = detect_exceptions(self.make_kpi())
        self.assertEqual(result, [])

    def test_high_residual_oil_is_flagged(self):
        result = detect_exceptions(
            self.make_kpi(doc_residual_oil_pct=3.4)
        )
        self.assertIn("HIGH DOC RESIDUAL OIL", result)

    def test_high_moisture_is_flagged(self):
        result = detect_exceptions(
            self.make_kpi(doc_moisture_pct=11.5)
        )
        self.assertIn("HIGH DOC MOISTURE", result)

    def test_high_solvent_consumption_is_flagged(self):
        result = detect_exceptions(
            self.make_kpi(solvent_litres_per_tonne=268.18)
        )
        self.assertIn("HIGH SOLVENT CONSUMPTION", result)

    def test_low_utilization_is_flagged(self):
        result = detect_exceptions(
            self.make_kpi(capacity_utilization_pct=44.0)
        )
        self.assertIn("LOW CAPACITY UTILIZATION", result)


if __name__ == "__main__":
    unittest.main()
