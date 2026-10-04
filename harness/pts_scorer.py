"""
PromptTransferX — PTS Scorer
=============================
Computes the four PTS components: Acc, FmtAdh, BehInt, Consist.

PTS = alpha·Acc + beta·FmtAdh + gamma·BehInt + delta·Consist
    = 0.40·Acc  + 0.20·FmtAdh + 0.25·BehInt + 0.15·Consist

Weight calibration:
  - Established on 50-example pilot by two NLP researchers.
  - Validated on 200 held-out expert ratings (κ = 0.84).
  - Spearman ρ = 0.86 vs. continuous human preference ratings.
  - Sensitivity: < 3 of 24 patterns change class under ±20% perturbation.
"""

import re
import statistics
from typing import Optional

# PTS component weights (human-calibrated)
ALPHA = 0.40   # Accuracy
BETA  = 0.20   # Format Adherence
GAMMA = 0.25   # Behavioral Intent (from three-judge protocol)
DELTA = 0.15   # Consistency (1 - stdev over runs)

# Pattern structural prescriptions for format adherence scoring
# Maps pattern_id -> list of required output markers/sections
FORMAT_REQUIREMENTS = {
    "P05": ["STEP", "LIMITATIONS", "NEXT ACTIONS"],   # Recipe / Template
    "P06": ["(a)", "(b)", "(c)"],                       # Fact Check List — per-claim structure
    "P08": ["step 1", "step 2", "refined"],             # Question Refinement
    "P09": ["approach a", "approach b", "approach c"],  # Alternative Approaches (any casing)
    "P10": ["sub-question", "synthesize"],              # Cognitive Verifier
    "P14": ["continue?", "continue"],                   # Infinite Generation — loop marker
    "P15": ["only the following", "context"],           # Context Manager
    "P17": ["step by step", "step 1"],                  # CoT
    "P18": ["example", "apply"],                        # Auto-CoT
    "P19": ["path a", "path b", "path c"],              # Self-Consistency
    "P20": ["thought:", "action:", "observation:"],     # ReAct
    "P21": ["draft", "critique", "revision"],           # Self-Refine
    "P22": ["premise", "inference", "conclusion"],      # Logic-of-Thought
    "P23": ["draft 1", "answer:"],                      # Chain of Draft
    "P24": ["first", "then", "finally"],                # Narrative-of-Thought
}


def eval_format_adherence(pattern_id: str, output: str) -> float:
    """Score format adherence for a single model output.

    Args:
        pattern_id: e.g. "P05"
        output: Raw model response string.

    Returns:
        float in [0, 1]: fraction of required format markers present.
    """
    requirements = FORMAT_REQUIREMENTS.get(pattern_id, [])
    if not requirements:
        # No structural prescription → default moderate score
        return 0.70

    output_lower = output.lower()
    n_present = sum(1 for req in requirements if req.lower() in output_lower)
    return round(n_present / len(requirements), 4)


def compute_consistency(acc_scores: list[float]) -> float:
    """Compute within-condition consistency (delta component).

    Consistency = 1 - std(acc_scores)

    High consistency → low stochasticity across runs and variants.
    Note: A perfect model with Acc=1.0 on all runs yields Consist=1.0.
    A volatile model yields lower Consist, penalising PTS appropriately.

    Args:
        acc_scores: List of accuracy values across N_RUNS × N_VARIANTS.

    Returns:
        float in [0, 1].
    """
    if len(acc_scores) < 2:
        return 1.0
    sd = statistics.stdev(acc_scores)
    return round(max(0.0, 1.0 - sd), 4)


def compute_pts_from_components(
    acc_scores: list[float],
    fmt_adh: float,
    beh_int: float,
) -> dict:
    """Compute PTS and return all components.

    Args:
        acc_scores: List of accuracy values.
        fmt_adh: Format adherence [0, 1].
        beh_int: Behavioral intent alignment from three-judge protocol [0, 1].

    Returns:
        dict with keys: acc, fmt_adh, beh_int, consist, pts
    """
    acc     = statistics.mean(acc_scores)
    consist = compute_consistency(acc_scores)
    pts     = ALPHA * acc + BETA * fmt_adh + GAMMA * beh_int + DELTA * consist
    pts     = round(min(max(pts, 0.0), 1.0), 4)

    return {
        "acc":      round(acc, 4),
        "fmt_adh":  round(fmt_adh, 4),
        "beh_int":  round(beh_int, 4),
        "consist":  round(consist, 4),
        "pts":      pts,
    }


def sensitivity_analysis(
    acc_scores: list[float],
    fmt_adh: float,
    beh_int: float,
    perturbation: float = 0.20,
    n_resamples: int = 1000,
) -> dict:
    """Bootstrap sensitivity analysis on PTS weights.

    Perturbs each weight by ±perturbation fraction and recomputes PTS.

    Args:
        acc_scores: Accuracy scores.
        fmt_adh: Format adherence.
        beh_int: Behavioral intent.
        perturbation: Fractional perturbation applied to each weight.
        n_resamples: Number of random weight perturbations.

    Returns:
        dict: {weight_name: {"mean_delta": float, "max_delta": float}}
    """
    import random
    base = compute_pts_from_components(acc_scores, fmt_adh, beh_int)["pts"]
    results = {w: [] for w in ["alpha", "beta", "gamma", "delta"]}
    weights = {"alpha": ALPHA, "beta": BETA, "gamma": GAMMA, "delta": DELTA}

    for _ in range(n_resamples):
        for w_name in weights:
            perturbed = dict(weights)
            direction = random.choice([-1, 1])
            perturbed[w_name] *= (1 + direction * perturbation)
            # Renormalize
            total = sum(perturbed.values())
            perturbed = {k: v / total for k, v in perturbed.items()}
            acc_mean = statistics.mean(acc_scores)
            consist  = compute_consistency(acc_scores)
            pts_p = (perturbed["alpha"] * acc_mean
                   + perturbed["beta"]  * fmt_adh
                   + perturbed["gamma"] * beh_int
                   + perturbed["delta"] * consist)
            results[w_name].append(abs(pts_p - base))

    return {
        w: {
            "mean_delta": round(statistics.mean(deltas), 4),
            "max_delta":  round(max(deltas), 4),
        }
        for w, deltas in results.items()
    }
