# P18 — Auto-CoT

| Field | Value |
|---|---|
| **ID** | P18 |
| **Name** | Auto-CoT |
| **Category** | Reasoning Augmentation |
| **Origin** | Zhang et al. (2022) |
| **PromptPrism Level** | Structural |
| **Volatility Class** | I — Stable |
| **Transfer** | 0.77 [.72,.82] |
| **Restricted Transfer** | 0.87 [.83,.91] |
| **PSI** | 0.11 |
| **Core Mechanism** | Automated rationale generation |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.84 | ±.03 |
| Claude 3 Opus (M2) | 0.82 | ±.03 |
| Gemini 1.5 Pro (M3) | 0.81 | ±.03 |
| LLaMA-3-70B-Instruct (M4) | 0.79 | ±.04 |
| Mistral-7B-Instruct (M5) | 0.73 | ±.05 |
| MedLLaMA-2-7B (M6) | 0.65 | ±.06 |

## Canonical Specification (V-A)

```
Before answering [TASK], automatically generate a worked example of a similar but simpler problem, showing step-by-step reasoning. Then apply the same reasoning pattern to the actual problem. Show both the example rationale and the main solution.
```

## Deployment Guidance

Deploy with confidence. Lowest PSI in the catalog (0.11, tied with P05). Excellent stability on Mathematical Reasoning and Instruction Following. The self-exemplification mechanism is reliably triggered across all instruction-tuned model families. Robust to temperature variation (PTS range 0.80–0.83 at T=0.0–1.0).
