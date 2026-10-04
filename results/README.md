# Results Directory

Empirical score tables from the PromptTransferX primary evaluation (Mar–Jul 2026).

| File | Contents |
|---|---|
| `primary_pts_scores.csv` | PTS per (pattern × model) with 95% bootstrapped CIs |
| `transfer_scores.csv` | Transfer, Restricted Transfer, PSI, Volatility Class per pattern |
| `model_level_means.csv` | Mean PTS per model with CIs and Friedman ranking |
| `task_category_transfer.csv` | Mean Transfer per task category |
| `volatility_taxonomy.csv` | Final class assignments with taxonomy correction notes |

## Key aggregate statistics

- Mean Transfer (all 24 patterns): **0.581**
- Mean PTS (all conditions): **0.638** (SD = 0.142)
- Patterns achieving Transfer ≥ 0.70: **11 of 24**
- Class I patterns: P05, P15, P18, P23
- Class IV patterns: P01, P11

## Taxonomy corrections applied

- P14 (Transfer = 0.48) → **Class III** (not IV)
- P24 (Transfer = 0.60) → **Class II** (not III)

See `docs/taxonomy_corrections.md` for full explanation.
