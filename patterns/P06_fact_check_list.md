# P06 — Fact Check List

| Field | Value |
|---|---|
| **ID** | P06 |
| **Name** | Fact Check List |
| **Category** | Error Identification |
| **Origin** | White et al. (2023) |
| **PromptPrism Level** | Structural |
| **Volatility Class** | II — Context-Sensitive |
| **Transfer** | 0.73 [.67,.78] |
| **Restricted Transfer** | 0.80 [.75,.85] |
| **PSI** | 0.16 |
| **Core Mechanism** | Self-generated verifiability claims |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.80 | ±.03 |
| Claude 3 Opus (M2) | 0.78 | ±.04 |
| Gemini 1.5 Pro (M3) | 0.75 | ±.04 |
| LLaMA-3-70B-Instruct (M4) | 0.70 | ±.05 |
| Mistral-7B-Instruct (M5) | 0.64 | ±.06 |
| MedLLaMA-2-7B (M6) | 0.58 | ±.07 |

## Canonical Specification (V-A)

```
After providing your answer to [TASK], generate a numbered list of specific factual claims in your response that could be independently verified. For each claim, state: (a) the claim, (b) how it could be verified, and (c) your confidence level (High / Medium / Low).
```

## Deployment Guidance

Reliable for Hallucination Resistance and Medical QA tasks. Best-performing pattern for Hallucination Resistance (0.79). Validate per task category; Creative Writing shows lower utility for this pattern.
