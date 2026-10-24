
"""
AI Manufacturing Performance Assistant
Stage 5: Investigation Recommendation Engine

Provides rule-based investigation guidance for detected exceptions.
Recommendations are suggestions, not confirmed diagnoses.

This educational prototype uses synthetic data and provisional thresholds.
Validate all recommendations against approved plant procedures.
"""


RECOMMENDATIONS = {
    "HIGH DOC RESIDUAL OIL": {
        "priority": "High",
        "possible_causes": [
            "Insufficient extraction time or ineffective contact",
            "Inappropriate solvent-to-solid ratio",
            "Poor material preparation or uneven percolation",
            "Unstable operating conditions",
        ],
        "recommended_checks": [
            "Review extraction time and solvent circulation records",
            "Check solvent distribution and percolation conditions",
            "Inspect material preparation and bed uniformity",
            "Confirm the DOC residual oil result using the approved laboratory method",
        ],
        "evidence_to_collect": [
            "DOC laboratory results",
            "Extraction operating log",
            "Solvent circulation records",
            "Material preparation and feed records",
        ],
    },
    "HIGH DOC MOISTURE": {
        "priority": "High",
        "possible_causes": [
            "Insufficient drying or desolventising",
            "Excess moisture in incoming material",
            "Unstable process temperature or residence time",
            "Sampling or measurement variation",
        ],
        "recommended_checks": [
            "Review desolventiser-toaster operating conditions",
            "Check incoming cake moisture and process records",
            "Review residence time and approved operating temperatures",
            "Repeat moisture testing if required by the laboratory procedure",
        ],
        "evidence_to_collect": [
            "DOC moisture laboratory results",
            "Incoming cake moisture records",
            "Desolventiser-toaster operating log",
            "Sampling and test records",
        ],
    },
    "HIGH SOLVENT CONSUMPTION": {
        "priority": "High",
        "possible_causes": [
            "Solvent losses from leaks or vapour escape",
            "Inefficient solvent recovery",
            "Inventory, measurement, or recording discrepancies",
            "Changes in production throughput or operating conditions",
        ],
        "recommended_checks": [
            "Reconcile solvent opening stock, additions, usage, and closing stock",
            "Inspect the plant for leaks using approved site procedures",
            "Review solvent recovery equipment performance and operating logs",
            "Verify the production tonnage and solvent volume measurements",
        ],
        "evidence_to_collect": [
            "Solvent inventory and reconciliation records",
            "Solvent recovery operating logs",
            "Leak inspection records",
            "Production and solvent measurement records",
        ],
    },
    "LOW CAPACITY UTILIZATION": {
        "priority": "Medium",
        "possible_causes": [
            "Equipment downtime or frequent stoppages",
            "Feedstock supply or preparation constraints",
            "Reduced operating hours",
            "Process bottlenecks or unstable operation",
        ],
        "recommended_checks": [
            "Compare actual throughput with rated daily capacity",
            "Review operating hours, stoppages, and maintenance records",
            "Check feedstock availability and feeding consistency",
            "Identify bottlenecks using production and downtime logs",
        ],
        "evidence_to_collect": [
            "Daily production report",
            "Equipment downtime and maintenance log",
            "Feedstock supply records",
            "Shift operating hours and stoppage records",
        ],
    },
}


def generate_recommendations(exceptions):
    """
    Generate investigation guidance for a list of exception messages.

    Returns a list of recommendation dictionaries.
    Unknown exception names are rejected to avoid misleading guidance.
    """
    if not isinstance(exceptions, list):
        raise TypeError("exceptions must be a list.")

    recommendations = []

    for exception in exceptions:
        if exception not in RECOMMENDATIONS:
            raise ValueError(
                f"Unknown exception: {exception}"
            )

        recommendation = RECOMMENDATIONS[exception]

        recommendations.append({
            "exception": exception,
            "priority": recommendation["priority"],
            "possible_causes": recommendation["possible_causes"].copy(),
            "recommended_checks": recommendation["recommended_checks"].copy(),
            "evidence_to_collect": recommendation["evidence_to_collect"].copy(),
        })

    return recommendations


if __name__ == "__main__":
    sample_exceptions = [
        "HIGH DOC RESIDUAL OIL",
        "HIGH SOLVENT CONSUMPTION",
    ]

    for item in generate_recommendations(sample_exceptions):
        print(f"\nException: {item['exception']}")
        print(f"Priority: {item['priority']}")

        print("Possible causes to investigate:")
        for cause in item["possible_causes"]:
            print(f"  - {cause}")

        print("Recommended checks:")
        for check in item["recommended_checks"]:
            print(f"  - {check}")

        print("Evidence to collect:")
        for evidence in item["evidence_to_collect"]:
            print(f"  - {evidence}")
