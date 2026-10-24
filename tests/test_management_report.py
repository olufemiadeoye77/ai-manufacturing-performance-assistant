
import unittest
from pathlib import Path

from src.management_report import generate_report


REPORT_PATH = Path("reports/management_report.md")


class ManagementReportTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        generate_report()
        cls.report = REPORT_PATH.read_text(encoding="utf-8")

    def test_recommendations_section_exists(self):
        self.assertIn(
            "## 6. Structured Investigation Recommendations",
            self.report,
        )

    def test_all_four_exceptions_are_included(self):
        exceptions = [
            "HIGH DOC RESIDUAL OIL",
            "HIGH DOC MOISTURE",
            "HIGH SOLVENT CONSUMPTION",
            "LOW CAPACITY UTILIZATION",
        ]

        for exception in exceptions:
            with self.subTest(exception=exception):
                self.assertIn(exception, self.report)

    def test_priority_is_included(self):
        self.assertIn("**Priority:** High", self.report)
        self.assertIn("**Priority:** Medium", self.report)

    def test_possible_causes_are_included(self):
        self.assertIn(
            "**Possible causes to investigate:**",
            self.report,
        )

    def test_recommended_checks_are_included(self):
        self.assertIn("**Recommended checks:**", self.report)

    def test_evidence_to_collect_is_included(self):
        self.assertIn("**Evidence to collect:**", self.report)

    def test_report_includes_caution_about_diagnosis(self):
        self.assertIn(
            "not confirmed diagnoses",
            self.report,
        )


if __name__ == "__main__":
    unittest.main()
