
import unittest

from src.production_monitor import (
    monitor_production,
    build_monitoring_report,
)


class TestProductionMonitor(unittest.TestCase):

    def make_record(self, **overrides):
        record = {
            "date": "2026-10-19",
            "throughput_tonnes": "25",
            "solvent_used_litres": "5000",
            "doc_residual_oil_pct": "2.8",
            "doc_moisture_pct": "9.5",
        }
        record.update(overrides)
        return record

    def test_normal_record_has_no_exceptions(self):
        results = monitor_production([self.make_record()])

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["exceptions"], [])
        self.assertEqual(results[0]["explanations"], [])

    def test_abnormal_record_generates_exceptions(self):
        record = self.make_record(
            date="2026-10-21",
            throughput_tonnes="22",
            solvent_used_litres="5900",
            doc_residual_oil_pct="3.4",
            doc_moisture_pct="11.5",
        )

        results = monitor_production([record])

        self.assertEqual(len(results[0]["exceptions"]), 4)
        self.assertEqual(len(results[0]["explanations"]), 4)

    def test_custom_threshold_changes_detection(self):
        record = self.make_record(doc_residual_oil_pct="3.2")

        results = monitor_production(
            [record],
            thresholds={"doc_residual_oil_pct_max": 3.5},
        )

        self.assertNotIn(
            "HIGH DOC RESIDUAL OIL",
            results[0]["exceptions"],
        )

    def test_empty_records_are_rejected(self):
        with self.assertRaises(ValueError):
            monitor_production([])

    def test_report_contains_summary_and_date(self):
        record = self.make_record(
            date="2026-10-21",
            throughput_tonnes="22",
            solvent_used_litres="5900",
            doc_residual_oil_pct="3.4",
            doc_moisture_pct="11.5",
        )

        results = monitor_production([record])
        report = build_monitoring_report(results)

        self.assertIn(
            "# Production KPI Monitoring and Exception Report",
            report,
        )
        
        self.assertIn("Production records analysed: 1", report)
        self.assertIn("Records requiring review: 1", report)
        self.assertIn("Total exceptions detected: 4", report) 
        self.assertIn("2026-10-21", report)
        self.assertIn("HIGH DOC RESIDUAL OIL", report)
        self.assertIn("Suggested checks:", report)

    def test_report_identifies_record_without_exceptions(self):
        results = monitor_production([self.make_record()])
        report = build_monitoring_report(results)

        self.assertIn(
            "No configured exceptions detected",
            report,
        )


if __name__ == "__main__":
    unittest.main()
