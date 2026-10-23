
import unittest

from src.explanation_engine import (
    explain_exception,
    generate_explanations,
    format_explanation_report,
)


class TestExplanationEngine(unittest.TestCase):

    def setUp(self):
        self.kpi_data = {
            "date": "2026-10-21",
            "throughput_tonnes": 22,
            "doc_residual_oil_pct": 3.4,
            "doc_moisture_pct": 11.5,
            "solvent_litres_per_tonne": 268.18,
            "capacity_utilization_pct": 44.0,
        }

    def test_high_residual_oil_explanation(self):
        result = explain_exception(
            self.kpi_data, "HIGH DOC RESIDUAL OIL"
        )
        self.assertEqual(result["observed_value"], 3.4)
        self.assertEqual(result["threshold"], 3.0)
        self.assertTrue(result["recommended_checks"])

    def test_high_moisture_explanation(self):
        result = explain_exception(
            self.kpi_data, "HIGH DOC MOISTURE"
        )
        self.assertEqual(result["observed_value"], 11.5)
        self.assertEqual(result["threshold"], 11.0)

    def test_high_solvent_explanation(self):
        result = explain_exception(
            self.kpi_data, "HIGH SOLVENT CONSUMPTION"
        )
        self.assertAlmostEqual(result["observed_value"], 268.18)
        self.assertEqual(result["unit"], "L/tonne")

    def test_low_utilization_explanation(self):
        result = explain_exception(
            self.kpi_data, "LOW CAPACITY UTILIZATION"
        )
        self.assertEqual(result["observed_value"], 44.0)
        self.assertEqual(result["threshold"], 50.0)

    def test_unknown_exception_is_rejected(self):
        with self.assertRaises(ValueError):
            explain_exception(self.kpi_data, "UNKNOWN EXCEPTION")

    def test_missing_kpi_field_is_rejected(self):
        incomplete_data = {
            "date": "2026-10-21",
            "throughput_tonnes": 22,
        }
        with self.assertRaises(ValueError):
            explain_exception(
                incomplete_data, "HIGH DOC RESIDUAL OIL"
            )

    def test_multiple_explanations_are_generated(self):
        exceptions = [
            "HIGH DOC RESIDUAL OIL",
            "HIGH DOC MOISTURE",
        ]
        results = generate_explanations(
            self.kpi_data, exceptions
        )
        self.assertEqual(len(results), 2)

    def test_report_contains_exception_and_date(self):
        explanations = generate_explanations(
            self.kpi_data, ["HIGH DOC RESIDUAL OIL"]
        )
        report = format_explanation_report(
            self.kpi_data, explanations
        )
        self.assertIn("2026-10-21", report)
        self.assertIn("HIGH DOC RESIDUAL OIL", report)
        self.assertIn("Suggested investigation", report)

    def test_empty_explanations_report_no_exceptions(self):
        report = format_explanation_report(self.kpi_data, [])
        self.assertIn("No exceptions detected", report)


if __name__ == "__main__":
    unittest.main()
