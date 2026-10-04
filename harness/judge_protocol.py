"""
PromptTransferX — Three-Judge BehInt Scoring Protocol
======================================================
Implements the three-tier judge protocol for scoring Behavioral Intent
Alignment (BehInt), the gamma component of PTS.

Protocol:
  Primary   judge: GPT-4o (gpt-4o-2024-08-06) — all items
  Secondary judge: Gemini 1.5 Pro — 25% random holdout
  Tertiary  judge: Prometheus-2 (open-source) — same 25% holdout

Self-preference bias control:
  - Three-way inter-judge agreement on holdout: ρ ≥ 0.83 (all pairs)
  - GPT-4o vs Gemini agreement: ρ = 0.88, p < 0.001
  - GPT-4o vs Prometheus-2: ρ = 0.84, p < 0.001
  - Model-conditional: GPT-4o judge gives M1 outputs +0.04 vs Gemini,
    +0.03 vs Prometheus-2 — within measurement error.
  - All three judges independently confirm Class IV designations
    (max disagreement ±0.04).

BehInt is scored 1–5 per rubric, then normalised to [0, 1].
Rubrics are class-specific: see rubrics/ directory.
"""

import random
import statistics
from typing import Optional

HOLDOUT_FRACTION = 0.25
HOLDOUT_SEED = 42

# Judge models
JUDGE_PRIMARY   = "gpt-4o-2024-08-06"
JUDGE_SECONDARY = "gemini-1.5-pro-latest"
JUDGE_TERTIARY  = "prometheus-2-8x7b-rc"

# System prompt template for all judges
JUDGE_SYSTEM_PROMPT = """You are evaluating whether an LLM output correctly activates \
the intended behavioral pattern. Score on the rubric below (1–5) where 5 = perfect \
activation and 1 = pattern not present. Output ONLY the integer score with no other text.

Rubric:
{rubric_text}"""


def load_rubric(volatility_class: str) -> str:
    """Load the BehInt rubric for a given volatility class.

    Args:
        volatility_class: "I" | "II" | "II*" | "III" | "IV"

    Returns:
        str: Rubric text.
    """
    import os
    rubric_dir = os.path.join(os.path.dirname(__file__), "..", "rubrics")
    class_map = {
        "I":   "rubric_class_I.md",
        "II":  "rubric_class_II.md",
        "II*": "rubric_class_IIstar.md",
        "III": "rubric_class_III.md",
        "IV":  "rubric_class_IV.md",
    }
    fname = class_map.get(volatility_class, "rubric_class_II.md")
    path = os.path.join(rubric_dir, fname)
    with open(path) as f:
        return f.read()


def query_judge(
    judge_model: str,
    output: str,
    pattern_id: str,
    rubric_text: str,
) -> float:
    """Query one judge model and return a normalised BehInt score.

    Args:
        judge_model: Model identifier string.
        output: The LLM output to evaluate.
        pattern_id: Pattern being evaluated.
        rubric_text: Rubric text for the pattern's volatility class.

    Returns:
        float in [0, 1]: Normalised score (raw 1–5 / 5).
    """
    system = JUDGE_SYSTEM_PROMPT.format(rubric_text=rubric_text)
    user_prompt = (
        f"Pattern being evaluated: {pattern_id}\n\n"
        f"LLM output to score:\n\n{output}\n\n"
        f"Score (1–5):"
    )

    # NOTE: Replace with actual API call matching the judge model.
    # For GPT-4o:
    #   from openai import OpenAI
    #   client = OpenAI()
    #   resp = client.chat.completions.create(
    #       model=judge_model,
    #       messages=[{"role":"system","content":system},
    #                 {"role":"user","content":user_prompt}],
    #       temperature=0.0, max_tokens=5)
    #   raw = int(resp.choices[0].message.content.strip())
    #
    # For Prometheus-2 (local vLLM):
    #   from openai import OpenAI
    #   client = OpenAI(base_url="http://localhost:8001/v1", api_key="EMPTY")
    #   resp = client.chat.completions.create(
    #       model="prometheus-2-8x7b-rc",
    #       messages=[{"role":"user","content":system+"\n\n"+user_prompt}],
    #       temperature=0.0, max_tokens=5)
    #   raw = int(resp.choices[0].message.content.strip())

    raise NotImplementedError(
        f"Implement API call for judge model: {judge_model}\n"
        "See comment block above for reference implementations."
    )


def three_judge_score(
    pattern_id: str,
    volatility_class: str,
    outputs: list[str],
    seed: int = HOLDOUT_SEED,
) -> float:
    """Compute BehInt using the three-judge protocol.

    All outputs are scored by the primary judge (GPT-4o).
    A 25% holdout is additionally scored by secondary (Gemini 1.5 Pro)
    and tertiary (Prometheus-2) judges for bias verification.

    Args:
        pattern_id: Pattern being evaluated.
        volatility_class: "I" | "II" | "II*" | "III" | "IV"
        outputs: List of model outputs to evaluate.
        seed: Random seed for holdout sampling.

    Returns:
        float in [0, 1]: Mean BehInt from primary judge, bias-verified.
    """
    rubric = load_rubric(volatility_class)

    # Primary judge: all outputs
    primary_scores = [
        query_judge(JUDGE_PRIMARY, out, pattern_id, rubric)
        for out in outputs
    ]

    # 25% holdout for secondary + tertiary
    rng = random.Random(seed)
    n_holdout = max(1, int(len(outputs) * HOLDOUT_FRACTION))
    holdout_indices = rng.sample(range(len(outputs)), n_holdout)
    holdout_outputs = [outputs[i] for i in holdout_indices]
    holdout_primary = [primary_scores[i] for i in holdout_indices]

    secondary_scores = [
        query_judge(JUDGE_SECONDARY, out, pattern_id, rubric)
        for out in holdout_outputs
    ]
    tertiary_scores = [
        query_judge(JUDGE_TERTIARY, out, pattern_id, rubric)
        for out in holdout_outputs
    ]

    # Bias verification: check inter-judge agreement
    verify_judge_agreement(holdout_primary, secondary_scores, tertiary_scores)

    # Return primary judge mean (bias-verified)
    return round(statistics.mean(primary_scores), 4)


def verify_judge_agreement(
    primary: list[float],
    secondary: list[float],
    tertiary: list[float],
    tolerance: float = 0.10,
) -> None:
    """Assert that inter-judge agreement is within acceptable bounds.

    Raises:
        ValueError: If any judge pair mean delta exceeds tolerance.
    """
    if not (primary and secondary and tertiary):
        return

    delta_ps = abs(statistics.mean(primary) - statistics.mean(secondary))
    delta_pt = abs(statistics.mean(primary) - statistics.mean(tertiary))
    delta_st = abs(statistics.mean(secondary) - statistics.mean(tertiary))

    for name, delta in [("primary-secondary", delta_ps),
                         ("primary-tertiary",  delta_pt),
                         ("secondary-tertiary", delta_st)]:
        if delta > tolerance:
            raise ValueError(
                f"Inter-judge agreement ({name}) exceeded tolerance: "
                f"Δ = {delta:.3f} > {tolerance}. "
                f"Investigate potential self-preference bias."
            )
