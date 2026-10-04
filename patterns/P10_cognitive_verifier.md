# P10 — Cognitive Verifier

| Field | Value |
|---|---|
| **ID** | P10 |
| **Name** | Cognitive Verifier |
| **Category** | Prompt Improvement |
| **Origin** | White et al. (2023) |
| **PromptPrism Level** | Structural |
| **Volatility Class** | II* — Context-Sensitive (Claude-Divergent) |
| **Transfer** | 0.66 [.60,.72] |
| **Restricted Transfer** | 0.79 [.74,.84] |
| **PSI** | 0.17 |
| **Core Mechanism** | Sub-question decomposition |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.83 | ±.03 |
| Claude 3 Opus (M2) | 0.81 | ±.04 |
| Gemini 1.5 Pro (M3) | 0.78 | ±.04 |
| LLaMA-3-70B-Instruct (M4) | 0.72 | ±.05 |
| Mistral-7B-Instruct (M5) | 0.66 | ±.06 |
| MedLLaMA-2-7B (M6) | 0.55 | ±.07 |

## Canonical Specification (V-A)

```
Before answering [TASK], generate 3–5 sub-questions whose answers would allow you to answer the main question more accurately and completely. Answer each sub-question explicitly. Then synthesize a final answer.
```

## Deployment Guidance

Claude-divergent on refusal-adjacent sub-question formulations. Core structural mechanism (explicit decomposition + synthesis) is reliable for Medical QA and Mathematical Reasoning. Validate on refusal-adjacent task variants when deploying on Claude-family backends.
