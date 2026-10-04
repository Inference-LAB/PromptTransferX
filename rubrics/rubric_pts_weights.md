# PTS Component Weights and Calibration

## Weights

| Component | Symbol | Weight | Description |
|---|---|---|---|
| Accuracy | Acc | **α = 0.40** | Task-specific accuracy normalised to [0, 1] |
| Behavioral Intent | BehInt | **γ = 0.25** | Three-judge rubric score, normalised |
| Format Adherence | FmtAdh | **β = 0.20** | Proportion of required format elements present |
| Consistency | Consist | **δ = 0.15** | 1 − std(Acc) across N_RUNS × N_VARIANTS |

**PTS = 0.40·Acc + 0.20·FmtAdh + 0.25·BehInt + 0.15·Consist**

## Calibration procedure

1. **Pilot:** Two NLP researchers independently rated 50 (pattern, model, output) triples
   on a continuous preference scale (1–10).
2. **Weight derivation:** Weights minimising mean squared error between PTS and
   human preference ratings on the 50-item pilot.
3. **Validation:** Weights fixed and applied to 200 held-out expert ratings.
   - Inter-rater reliability on held-out set: κ = 0.84
   - Convergent validity: Spearman ρ = 0.86 (p < 0.001, N = 200) vs. continuous ratings

## Sensitivity analysis results

| Perturbed weight | Mean rank change | Patterns changing class |
|---|---|---|
| α ± 20% | 0.31 | 2 of 24 |
| β ± 20% | 0.18 | 1 of 24 |
| γ ± 20% | 0.27 | 2 of 24 |
| δ ± 20% | 0.12 | 0 of 24 |
| All simultaneously | 0.44 | 3 of 24 |
| Equal weights (0.25 each) | 0.38 | 3 of 24 |

Class IV designations stable in 99.2% of all bootstrap resamples (N=1,000).

## Important note

These weights are an **expert-calibrated composite**, not a universally optimal
specification. Task-adaptive weighting (higher α for accuracy-critical tasks,
higher β for format-critical tasks) may improve per-category measurement granularity.
