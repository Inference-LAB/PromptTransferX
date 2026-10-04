"""
PromptTransferX — Portability Metrics
======================================
Computes Transfer, U(P), S(P), Portability, and PSI from per-model PTS scores.

Metrics:
    Transfer(P)    = min_M[PTS(P,M)] / max_M[PTS(P,M)]
    U(P)           = (1/M) Σ_m PTS(P, m)
    S(P)           = 1 - σ_M[PTS] / (μ_M[PTS] + ε)
    Portability(P) = U(P) × S(P)
    PSI(P)         = PTS(P, M1_GPT4o) − PTS(P, M5_Mistral7B)

Volatility taxonomy (revised post-pilot):
    Class I   Transfer ≥ 0.75   Stable
    Class II  0.60–0.74          Context-Sensitive
    Class III 0.45–0.59          Model-Specific
    Class IV  < 0.45             Brittle

Note: Class II* (Claude-Divergent) is assigned post-hoc via model-conditional
analysis, not the Transfer score alone.

PSI thresholds:
    < 0.15   Stable cross-tier
    0.15–0.25 Context-sensitive
    0.25–0.35 Model-specific
    > 0.35   Brittle
    Negative  Open-weight outperforms proprietary (P11 only: −0.38)
"""

import statistics
from typing import Optional

EPSILON = 0.01          # stability denominator guard
PROPRIETARY_TIER  = "M1"   # GPT-4o
OPEN_WEIGHT_TIER  = "M5"   # Mistral-7B-Instruct (weakest general-purpose)
MEDLLAMA_ID       = "M6"   # Excluded in Restricted Transfer


def transfer_score(pts_per_model: dict[str, float]) -> float:
    """Compute legacy Transfer score.

    Transfer(P) = min_M[PTS(P,M)] / max_M[PTS(P,M)]

    Note: A prompt scoring poorly on all models can still achieve a high
    Transfer ratio. This is why Transfer alone is insufficient — U(P) and
    S(P) must also be reported. See portability() for the composite measure.
    """
    scores = list(pts_per_model.values())
    if not scores or max(scores) == 0:
        return 0.0
    return round(min(scores) / max(scores), 4)


def restricted_transfer_score(pts_per_model: dict[str, float]) -> float:
    """Transfer excluding MedLLaMA-2 (domain fine-tune).

    Isolates the portability gap attributable to general-purpose model
    variance, removing the domain-mismatch component of MedLLaMA-2.
    """
    filtered = {k: v for k, v in pts_per_model.items() if k != MEDLLAMA_ID}
    return transfer_score(filtered)


def behavioral_utility(pts_per_model: dict[str, float]) -> float:
    """Mean behavioral utility U(P) = (1/M) Σ_m PTS(P, m)."""
    scores = list(pts_per_model.values())
    return round(statistics.mean(scores), 4) if scores else 0.0


def cross_model_stability(pts_per_model: dict[str, float]) -> float:
    """Cross-model stability S(P) = 1 - σ / (μ + ε).

    A specification with uniformly low PTS scores has high stability
    but low utility; the portability composite U(P) × S(P) correctly
    penalises this case.
    """
    scores = list(pts_per_model.values())
    if len(scores) < 2:
        return 1.0
    mu = statistics.mean(scores)
    sigma = statistics.stdev(scores)
    return round(1.0 - sigma / (mu + EPSILON), 4)


def portability(pts_per_model: dict[str, float]) -> float:
    """Composite portability Π(P) = U(P) × S(P).

    Requires both sufficient utility AND sufficient stability.
    A specification with U=0.9 but S=0.3 has Π=0.27 — low portability
    despite high absolute performance on the best model.
    """
    u = behavioral_utility(pts_per_model)
    s = cross_model_stability(pts_per_model)
    return round(u * s, 4)


def pattern_stability_index(pts_per_model: dict[str, float]) -> Optional[float]:
    """PSI(P) = PTS(P, GPT-4o) − PTS(P, Mistral-7B).

    Quantifies the proprietary-to-open-weight tier gap.
    Negative PSI (P11) indicates open-weight outperforms proprietary.
    """
    if PROPRIETARY_TIER in pts_per_model and OPEN_WEIGHT_TIER in pts_per_model:
        return round(pts_per_model[PROPRIETARY_TIER] - pts_per_model[OPEN_WEIGHT_TIER], 3)
    return None


def psi_category(psi: Optional[float]) -> str:
    """Categorise PSI value.

    Returns:
        str: "stable" | "context-sensitive" | "model-specific" | "brittle" | "inverted"
    """
    if psi is None:
        return "unknown"
    if psi < 0:
        return "inverted"
    elif psi < 0.15:
        return "stable"
    elif psi < 0.25:
        return "context-sensitive"
    elif psi < 0.35:
        return "model-specific"
    else:
        return "brittle"


def volatility_class(transfer: float) -> str:
    """Assign volatility class based on Transfer score.

    Revised taxonomy (post-pilot):
        I   >= 0.75
        II  0.60–0.74
        III 0.45–0.59
        IV  < 0.45

    P14 correction: Transfer = 0.48 → Class III (not IV).
    P24 correction: Transfer = 0.60 → Class II (not III).
    """
    if transfer >= 0.75:
        return "I"
    elif transfer >= 0.60:
        return "II"
    elif transfer >= 0.45:
        return "III"
    else:
        return "IV"


def full_portability_report(pts_per_model: dict[str, float]) -> dict:
    """Compute all portability metrics for one pattern.

    Args:
        pts_per_model: {model_id: mean_pts}

    Returns:
        dict with all portability metrics.
    """
    tr   = transfer_score(pts_per_model)
    rtr  = restricted_transfer_score(pts_per_model)
    u    = behavioral_utility(pts_per_model)
    s    = cross_model_stability(pts_per_model)
    pi   = portability(pts_per_model)
    psi  = pattern_stability_index(pts_per_model)
    cls  = volatility_class(tr)
    psi_cat = psi_category(psi)

    return {
        "transfer":            tr,
        "restricted_transfer": rtr,
        "utility":             u,
        "stability":           s,
        "portability":         pi,
        "psi":                 psi,
        "psi_category":        psi_cat,
        "volatility_class":    cls,
    }
