# Ablations Directory

Results from ablation studies supplementing the primary evaluation.

| File | Study |
|---|---|
| `temperature_sensitivity.csv` | PTS at T=0.0/0.3/0.7/1.0 for P05/P07/P11 × 3 models × 2 tasks |
| `system_prompt_sensitivity.csv` | PTS under null / generic / task-specific system prompts |
| `phrasing_variation_anova.csv` | Two-way mixed ANOVA: pattern identity vs. phrasing variation |
| `pts_weight_robustness.csv` | PTS sensitivity to ±20% weight perturbation (N=1,000 resamples) |

## Key findings

- **Temperature:** Class I patterns (P05) are robust across T=0.0–1.0 (PTS range 0.80–0.83). Class IV (P11) shows amplified variance at higher temperatures.
- **System prompt:** Claude fingerprint on P11 persists regardless of system prompt condition (rules out null-SP artifact). Task-specific SP improves Mistral-7B on P07 by +0.09.
- **Phrasing:** Pattern identity explains 61.3% of PTS variance; phrasing variation explains 22.7%. Reporting only best phrasing inflates claims.
- **Weights:** <3 of 24 patterns change class under ±20% weight perturbation; Class IV stable in 99.2% of bootstrap resamples.
