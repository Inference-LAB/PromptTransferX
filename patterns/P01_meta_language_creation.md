# P01 — Meta Language Creation

| Field | Value |
|---|---|
| **ID** | P01 |
| **Name** | Meta Language Creation |
| **Category** | Input Semantics |
| **Origin** | White et al. (2023) |
| **PromptPrism Level** | Semantic / Pragmatic |
| **Volatility Class** | IV — Brittle |
| **Transfer** | 0.40 [95% CI: .34, .47] |
| **Restricted Transfer** | 0.60 [.53, .67] |
| **PSI** | 0.43 |
| **Core Mechanism** | Custom symbolic language injection |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.72 | ±.04 |
| Claude 3 Opus (M2) | 0.68 | ±.05 |
| Gemini 1.5 Pro (M3) | 0.65 | ±.04 |
| LLaMA-3-70B-Instruct (M4) | 0.51 | ±.06 |
| Mistral-7B-Instruct (M5) | 0.43 | ±.07 |
| MedLLaMA-2-7B (M6) | 0.29 | ±.08 |

## Canonical Specification (V-A)

```
For the rest of this conversation, treat each line beginning with ► as a command
to execute. ► [COMMAND] means: [DEFINITION]. Acknowledge with "Meta-language
active." Then execute: ► [TASK]
```

## Deployment Guidance

**Do not deploy in multi-backend systems without per-model calibration.**
PSI = 0.43 indicates a large proprietary-to-open-weight performance gap.
MedLLaMA-2 (0.29) is the primary driver of low full-panel Transfer; even
excluding it, Restricted Transfer (0.60) remains below the Class II threshold.
Custom symbolic language injection depends on implicit capability conventions
that vary substantially across model families.
