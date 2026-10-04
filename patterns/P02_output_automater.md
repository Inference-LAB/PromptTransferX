# P02 — Output Automater

| Field | Value |
|---|---|
| **ID** | P02 |
| **Name** | Output Automater |
| **Category** | Output Customization |
| **Origin** | White et al. (2023) |
| **PromptPrism Level** | Structural |
| **Volatility Class** | II — Context-Sensitive |
| **Transfer** | 0.74 [.68,.79] |
| **Restricted Transfer** | 0.82 [.77,.86] |
| **PSI** | 0.15 |
| **Core Mechanism** | Automate multi-step output generation |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.83 | ±.03 |
| Claude 3 Opus (M2) | 0.81 | ±.04 |
| Gemini 1.5 Pro (M3) | 0.79 | ±.03 |
| LLaMA-3-70B-Instruct (M4) | 0.74 | ±.05 |
| Mistral-7B-Instruct (M5) | 0.68 | ±.06 |
| MedLLaMA-2-7B (M6) | 0.61 | ±.06 |

## Canonical Specification (V-A)

```
Whenever I describe a multi-step task, automatically generate a complete, executable script or structured plan that accomplishes all steps without requiring additional input from me. The output should be fully self-contained. Task: [TASK]
```

## Deployment Guidance

Safe for multi-backend deployment with task-category validation. PSI=0.15 indicates a small cross-tier gap. Re-validate after backend changes.
