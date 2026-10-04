# P09 — Alternative Approaches

| Field | Value |
|---|---|
| **ID** | P09 |
| **Name** | Alternative Approaches |
| **Category** | Prompt Improvement |
| **Origin** | White et al. (2023) |
| **PromptPrism Level** | Structural |
| **Volatility Class** | II — Context-Sensitive |
| **Transfer** | 0.74 [.68,.79] |
| **Restricted Transfer** | 0.83 [.78,.87] |
| **PSI** | 0.14 |
| **Core Mechanism** | Multi-solution exploration |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.81 | ±.03 |
| Claude 3 Opus (M2) | 0.79 | ±.04 |
| Gemini 1.5 Pro (M3) | 0.77 | ±.04 |
| LLaMA-3-70B-Instruct (M4) | 0.73 | ±.05 |
| Mistral-7B-Instruct (M5) | 0.67 | ±.06 |
| MedLLaMA-2-7B (M6) | 0.60 | ±.06 |

## Canonical Specification (V-A)

```
For [TASK], provide three distinct approaches. For each, clearly state: (1) the core method, (2) the key trade-off, and (3) when to prefer it. Then recommend which to use in the common case and why.
```

## Deployment Guidance

Strong cross-tier reliability. PSI=0.14 (fourth lowest in catalog). Excellent for Mathematical Reasoning and Code Generation. The explicit three-approach structure reduces model-specific interpretation variance.
