# P08 — Question Refinement

| Field | Value |
|---|---|
| **ID** | P08 |
| **Name** | Question Refinement |
| **Category** | Prompt Improvement |
| **Origin** | White et al. (2023) |
| **PromptPrism Level** | Structural |
| **Volatility Class** | II — Context-Sensitive |
| **Transfer** | 0.70 [.64,.75] |
| **Restricted Transfer** | 0.79 [.74,.84] |
| **PSI** | 0.17 |
| **Core Mechanism** | Iterative question reformulation |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.82 | ±.03 |
| Claude 3 Opus (M2) | 0.80 | ±.04 |
| Gemini 1.5 Pro (M3) | 0.78 | ±.03 |
| LLaMA-3-70B-Instruct (M4) | 0.71 | ±.05 |
| Mistral-7B-Instruct (M5) | 0.65 | ±.06 |
| MedLLaMA-2-7B (M6) | 0.57 | ±.07 |

## Canonical Specification (V-A)

```
Before answering, suggest a better, more specific version of my question that would produce a more useful answer. State the improved question explicitly, then answer it. My question: [TASK]
```

## Deployment Guidance

Good for Medical QA and instructional tasks. Structural mechanism (explicit reformulation step) provides stable cross-tier behavior. PSI=0.17 is moderate; validate on Mistral-7B for deployment sets including 7B models.
