
"""Tests for the Stage 5 investigation recommendation engine."""

import unittest

from src.recommendation_engine import generate_recommendations


class TestRecommendationEngine(unittest.TestCase):

    def test_high_residual_oil_recommendation(self):
        results = generate_recommendations(
            ["HIGH DOC RESIDUAL OIL"]
        )

        self.assertEqual(len(results), 1)
        self.assertEqual(
            results[0]["exception"],
            "HIGH DOC RESIDUAL OIL",
        )
        self.assertEqual(results[0]["priority"], "High")
        self.assertTrue(results[0]["recommended_checks"])
        self.assertTrue(results[0]["evidence_to_collect"])

    def test_high_solvent_recommendation(self):
        results = generate_recommendations(
            ["HIGH SOLVENT CONSUMPTION"]
        )

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["priority"], "High")
        self.assertTrue(results[0]["possible_causes"])

    def test_all_four_exceptions_are_supported(self):
        exceptions = [
            "HIGH DOC RESIDUAL OIL",
            "HIGH DOC MOISTURE",
            "HIGH SOLVENT CONSUMPTION",
            "LOW CAPACITY UTILIZATION",
        ]

        results = generate_recommendations(exceptions)

        self.assertEqual(len(results), 4)

    def test_empty_exception_list_returns_empty_list(self):
        self.assertEqual(generate_recommendations([]), [])

    def test_unknown_exception_is_rejected(self):
        with self.assertRaises(ValueError):
            generate_recommendations(["UNKNOWN EXCEPTION"])

    def test_non_list_input_is_rejected(self):
        with self.assertRaises(TypeError):
            generate_recommendations("HIGH DOC RESIDUAL OIL")

    def test_each_recommendation_has_required_fields(self):
        results = generate_recommendations(
            ["HIGH DOC MOISTURE"]
        )

        required_fields = {
            "exception",
            "priority",
            "possible_causes",
            "recommended_checks",
            "evidence_to_collect",
        }

        self.assertTrue(required_fields.issubset(results[0].keys()))


if __name__ == "__main__":
    unittest.main()
