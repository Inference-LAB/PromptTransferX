# P23 — Chain of Draft (CoD)

| Field | Value |
|---|---|
| **ID** | P23 |
| **Name** | Chain of Draft (CoD) |
| **Category** | Reasoning Augmentation |
| **Origin** | Xu et al. (2025) |
| **PromptPrism Level** | Structural |
| **Volatility Class** | I — Stable |
| **Transfer** | 0.75 [.69,.80] |
| **Restricted Transfer** | 0.86 [.82,.90] |
| **PSI** | 0.12 |
| **Core Mechanism** | Minimal draft reasoning trace |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.84 | ±.03 |
| Claude 3 Opus (M2) | 0.82 | ±.03 |
| Gemini 1.5 Pro (M3) | 0.81 | ±.03 |
| LLaMA-3-70B-Instruct (M4) | 0.78 | ±.04 |
| Mistral-7B-Instruct (M5) | 0.72 | ±.05 |
| MedLLaMA-2-7B (M6) | 0.63 | ±.07 |

## Canonical Specification (V-A)

```
Solve [TASK] using minimal draft reasoning traces. Keep each reasoning step to 5 words or fewer. Show 3–7 draft steps, then give the final answer. Format:
Draft 1: [≤5 words]
Draft 2: [≤5 words]
...
Answer: [full answer]
```

## Deployment Guidance

Deploy with confidence. PSI=0.12 (third lowest). The word-count constraint on draft steps is a structural prescription reliably followed across all tested model families. Cross-generationally stable (Class I retained on Claude Opus 4.6 and Qwen3-14B). Cross-lingually stable (Arabic PTS within 0.05 of English values).
