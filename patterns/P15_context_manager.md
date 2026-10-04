# P15 — Context Manager

| Field | Value |
|---|---|
| **ID** | P15 |
| **Name** | Context Manager |
| **Category** | Context Control |
| **Origin** | White et al. (2023) |
| **PromptPrism Level** | Structural |
| **Volatility Class** | I — Stable |
| **Transfer** | 0.78 [.73,.82] |
| **Restricted Transfer** | 0.84 [.79,.88] |
| **PSI** | 0.14 |
| **Core Mechanism** | Explicit context scope control |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.85 | ±.03 |
| Claude 3 Opus (M2) | 0.83 | ±.03 |
| Gemini 1.5 Pro (M3) | 0.82 | ±.03 |
| LLaMA-3-70B-Instruct (M4) | 0.76 | ±.04 |
| Mistral-7B-Instruct (M5) | 0.71 | ±.05 |
| MedLLaMA-2-7B (M6) | 0.66 | ±.06 |

## Canonical Specification (V-A)

```
For this task, use ONLY the following context. Do not draw on any other knowledge or make assumptions beyond what is stated here.

CONTEXT:
[CONTEXT_TEXT]

TASK: [TASK]

If the context does not contain enough information to answer fully, say so explicitly.
```

## Deployment Guidance

Deploy with confidence. Highest Transfer for Medical QA (0.81). PSI=0.14 (fifth lowest); even MedLLaMA-2 (0.66) performs above Class III threshold. The explicit context-boundary instruction is reliably followed across all instruction-tuned models. Best choice for RAG-adjacent deployments requiring strict context scoping.
