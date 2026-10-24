
"""
Stage 6: Manufacturing What-If Scenario Analysis

Estimates potential solvent savings using production data.
This educational module does not predict or guarantee actual savings.
"""


def calculate_scenario(
    throughput_tonnes,
    solvent_used_litres,
    target_litres_per_tonne,
    cost_per_litre=None,
):
    """Compare recorded solvent use with a proposed target."""

    if throughput_tonnes <= 0:
        raise ValueError("Throughput must be greater than zero.")

    if solvent_used_litres < 0:
        raise ValueError("Solvent used cannot be negative.")

    if target_litres_per_tonne <= 0:
        raise ValueError("Target consumption must be greater than zero.")

    if cost_per_litre is not None and cost_per_litre < 0:
        raise ValueError("Cost per litre cannot be negative.")

    current_litres_per_tonne = (
        solvent_used_litres / throughput_tonnes
    )

    target_solvent_litres = (
        throughput_tonnes * target_litres_per_tonne
    )

    potential_litres_saved = (
        solvent_used_litres - target_solvent_litres
    )

    if solvent_used_litres > 0:
        reduction_percent = (
            potential_litres_saved / solvent_used_litres
        ) * 100
    else:
        reduction_percent = 0.0

    estimated_cost_savings = None

    if cost_per_litre is not None:
        estimated_cost_savings = (
            potential_litres_saved * cost_per_litre
        )

    return {
        "throughput_tonnes": throughput_tonnes,
        "current_solvent_litres": solvent_used_litres,
        "current_litres_per_tonne": current_litres_per_tonne,
        "target_litres_per_tonne": target_litres_per_tonne,
        "target_solvent_litres": target_solvent_litres,
        "potential_litres_saved": potential_litres_saved,
        "reduction_percent": reduction_percent,
        "estimated_cost_savings": estimated_cost_savings,
    }


if __name__ == "__main__":
    result = calculate_scenario(
        throughput_tonnes=25,
        solvent_used_litres=5000,
        target_litres_per_tonne=180,
    )

    print("MANUFACTURING WHAT-IF SCENARIO")
    print("------------------------------")
    print(f"Throughput: {result['throughput_tonnes']} tonnes")
    print(f"Current consumption: {result['current_litres_per_tonne']:.2f} L/t")
    print(f"Target consumption: {result['target_litres_per_tonne']:.2f} L/t")
    print(f"Potential solvent savings: {result['potential_litres_saved']:.2f} litres")
    print(f"Potential reduction: {result['reduction_percent']:.2f}%")
