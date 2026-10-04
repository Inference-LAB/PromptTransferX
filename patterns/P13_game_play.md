# P13 — Game Play

| Field | Value |
|---|---|
| **ID** | P13 |
| **Name** | Game Play |
| **Category** | Interaction |
| **Origin** | White et al. (2023) |
| **PromptPrism Level** | Pragmatic |
| **Volatility Class** | III — Model-Specific |
| **Transfer** | 0.51 [.44,.59] |
| **Restricted Transfer** | 0.68 [.61,.75] |
| **PSI** | 0.24 |
| **Core Mechanism** | Gamified structured interaction |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.74 | ±.04 |
| Claude 3 Opus (M2) | 0.72 | ±.05 |
| Gemini 1.5 Pro (M3) | 0.70 | ±.04 |
| LLaMA-3-70B-Instruct (M4) | 0.61 | ±.06 |
| Mistral-7B-Instruct (M5) | 0.50 | ±.07 |
| MedLLaMA-2-7B (M6) | 0.38 | ±.09 |

## Canonical Specification (V-A)

```
Let's play a structured learning game about [TOPIC]. Rules: (1) You present a scenario or question. (2) I answer. (3) You score my answer (correct/partially correct/incorrect) and explain. (4) Track my score. (5) After 5 rounds, summarize what I've learned. Begin round 1.
```

## Deployment Guidance

High model-specificity. Worst pattern for Commonsense Inference (0.48). Gamified schemas require emergent interaction conventions not reliably present in 7B open-weight models (Mistral: 0.50; MedLLaMA-2: 0.38). Use only on frontier-model backends with task-specific validation.
