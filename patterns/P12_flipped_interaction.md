# P12 — Flipped Interaction

| Field | Value |
|---|---|
| **ID** | P12 |
| **Name** | Flipped Interaction |
| **Category** | Interaction |
| **Origin** | White et al. (2023) |
| **PromptPrism Level** | Pragmatic |
| **Volatility Class** | III — Model-Specific |
| **Transfer** | 0.54 [.47,.61] |
| **Restricted Transfer** | 0.72 [.65,.78] |
| **PSI** | 0.21 |
| **Core Mechanism** | Role reversal—LLM asks user |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.76 | ±.04 |
| Claude 3 Opus (M2) | 0.78 | ±.04 |
| Gemini 1.5 Pro (M3) | 0.74 | ±.04 |
| LLaMA-3-70B-Instruct (M4) | 0.64 | ±.06 |
| Mistral-7B-Instruct (M5) | 0.55 | ±.07 |
| MedLLaMA-2-7B (M6) | 0.41 | ±.08 |

## Canonical Specification (V-A)

```
Instead of me asking you questions, I want you to interview me to gather the information needed to [GOAL]. Ask me one question at a time. Wait for my answer before proceeding. Do not attempt to answer on my behalf. Begin.
```

## Deployment Guidance

Model-specific calibration required. Role-reversal schema depends on pragmatic conventions that vary across model families; MedLLaMA-2 (0.41) approaches Class IV. Restricted Transfer (0.72) is acceptable on general-purpose models. Not recommended for 7B open-weight models without calibration.
