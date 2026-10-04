# Taxonomy Boundary Corrections

## Summary

The volatility taxonomy boundaries were revised after the primary evaluation,
based on the empirical distribution of Transfer scores across all 24 patterns.

## Original (pilot-based) boundaries

| Class | Transfer range |
|---|---|
| I — Stable | ≥ 0.80 |
| II — Context-Sensitive | 0.65 – 0.79 |
| III — Model-Specific | 0.45 – 0.64 |
| IV — Brittle | < 0.45 |

## Revised (final) boundaries

| Class | Transfer range |
|---|---|
| I — Stable | ≥ 0.75 |
| II — Context-Sensitive | 0.60 – 0.74 |
| III — Model-Specific | 0.45 – 0.59 |
| IV — Brittle | < 0.45 |

## Pattern-level corrections

### P14 — Infinite Generation

- **Reported Transfer:** 0.48
- **Pilot boundary:** would have placed P14 in Class IV (< 0.45 pilot threshold was 0.45)
- **Revised boundary:** 0.48 ≥ 0.45 → **Class III** (correct)
- **Previous error:** Some earlier draft text referred to P14 as Class IV. This is incorrect under both boundary sets since 0.48 ≥ 0.45.
- **Cross-generation confirmation:** P14 retains Class III on Claude Opus 4.6 and Qwen3-14B (Aug 2026 replication).

### P24 — Narrative-of-Thought

- **Reported Transfer:** 0.60
- **Pilot boundary:** 0.60 < 0.65 → would have placed P24 in Class III
- **Revised boundary:** 0.60 = lower bound of Class II (0.60–0.74) → **Class II** (correct)
- **Previous error:** Some earlier draft text referred to P24 as Class III.

## Stable designations

- Class IV contains **only P01 (Transfer = 0.40) and P11 (Transfer = 0.35)**
  under all boundary revisions.
- Class IV designations are stable in **99.2% of bootstrap resamples** (N = 1,000)
  under ±20% weight perturbation.
- The Class IV designation for P01 and P11 is confirmed by all three judges
  independently (max disagreement: ±0.04).
