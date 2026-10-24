
import unittest

from src.scenario_analysis import calculate_scenario


class TestScenarioAnalysis(unittest.TestCase):

    def test_current_consumption_is_calculated(self):
        result = calculate_scenario(25, 5000, 180)
        self.assertEqual(result["current_litres_per_tonne"], 200)

    def test_potential_savings_are_calculated(self):
        result = calculate_scenario(25, 5000, 180)
        self.assertEqual(result["target_solvent_litres"], 4500)
        self.assertEqual(result["potential_litres_saved"], 500)

    def test_reduction_percentage_is_calculated(self):
        result = calculate_scenario(25, 5000, 180)
        self.assertEqual(result["reduction_percent"], 10)

    def test_cost_savings_are_calculated(self):
        result = calculate_scenario(25, 5000, 180, 1000)
        self.assertEqual(result["estimated_cost_savings"], 500000)

    def test_cost_is_optional(self):
        result = calculate_scenario(25, 5000, 180)
        self.assertIsNone(result["estimated_cost_savings"])

    def test_zero_throughput_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_scenario(0, 5000, 180)

    def test_negative_solvent_use_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_scenario(25, -100, 180)

    def test_zero_target_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_scenario(25, 5000, 0)

    def test_negative_cost_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_scenario(25, 5000, 180, -10)


if __name__ == "__main__":
    unittest.main()
