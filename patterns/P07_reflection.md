# P07 — Reflection

| Field | Value |
|---|---|
| **ID** | P07 |
| **Name** | Reflection |
| **Category** | Error Identification |
| **Origin** | White et al. (2023) |
| **PromptPrism Level** | Semantic / Pragmatic |
| **Volatility Class** | II* — Context-Sensitive (Claude-Divergent) |
| **Transfer** | 0.66 [.59,.72] |
| **Restricted Transfer** | 0.75 [.68,.81] |
| **PSI** | 0.20 |
| **Core Mechanism** | Self-introspective error detection |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.79 | ±.04 |
| Claude 3 Opus (M2) | 0.82 | ±.04 |
| Gemini 1.5 Pro (M3) | 0.77 | ±.04 |
| LLaMA-3-70B-Instruct (M4) | 0.68 | ±.05 |
| Mistral-7B-Instruct (M5) | 0.59 | ±.07 |
| MedLLaMA-2-7B (M6) | 0.52 | ±.08 |

## Canonical Specification (V-A)

```
Answer [TASK]. Then reflect critically on your own response: What assumptions did you make? Where might you be wrong? What additional information would change your answer? Present this reflection clearly separated from your main response.
```

## Deployment Guidance

Claude 3 Opus shows anomalously HIGH PTS (0.82) on this pattern—above GPT-4o (0.79)—due to the reflective mechanism aligning with its alignment training. However, refusal-adjacent variants trigger divergence. Apply G4 mitigation: task-specific system prompt improves Mistral-7B by +0.09. Temperature-sensitive on open-weight models (Δ=0.18 at T=1.0 vs T=0.0 on Mistral-7B).
