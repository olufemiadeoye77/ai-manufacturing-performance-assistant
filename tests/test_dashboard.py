"""Tests for the manufacturing KPI dashboard."""

import unittest

from src.dashboard import collect_dashboard_data


class TestDashboard(unittest.TestCase):

    def test_dashboard_data_is_loaded(self):
        results = collect_dashboard_data()
        self.assertGreater(len(results), 0)

    def test_dashboard_records_contain_kpis_and_exceptions(self):
        results = collect_dashboard_data()

        for item in results:
            self.assertIn("kpi", item)
            self.assertIn("exceptions", item)

    def test_expected_sample_exception_is_detected(self):
        results = collect_dashboard_data()

        flagged = [
            item for item in results
            if item["kpi"]["date"] == "2026-10-21"
        ]

        self.assertEqual(len(flagged), 1)
        self.assertEqual(len(flagged[0]["exceptions"]), 4)


if __name__ == "__main__":
    unittest.main()