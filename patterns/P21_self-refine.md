# P21 — Self-Refine

| Field | Value |
|---|---|
| **ID** | P21 |
| **Name** | Self-Refine |
| **Category** | Self-Correction |
| **Origin** | Madaan et al. (2023) |
| **PromptPrism Level** | Semantic / Pragmatic |
| **Volatility Class** | II* — Context-Sensitive (Claude-Divergent) |
| **Transfer** | 0.66 [.59,.72] |
| **Restricted Transfer** | 0.78 [.71,.84] |
| **PSI** | 0.18 |
| **Core Mechanism** | Iterative self-generated feedback |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.80 | ±.04 |
| Claude 3 Opus (M2) | 0.83 | ±.04 |
| Gemini 1.5 Pro (M3) | 0.78 | ±.04 |
| LLaMA-3-70B-Instruct (M4) | 0.70 | ±.05 |
| Mistral-7B-Instruct (M5) | 0.62 | ±.06 |
| MedLLaMA-2-7B (M6) | 0.53 | ±.08 |

## Canonical Specification (V-A)

```
Generate your initial response to [TASK]. Then critique it: What are its weaknesses? What information is missing or imprecise? What would a domain expert object to? Then revise to produce a clearly improved final response. Label each phase: DRAFT / CRITIQUE / REVISION.
```

## Deployment Guidance

Claude 3 Opus shows highest PTS (0.83) on this pattern, consistent with its reflective alignment. Refusal-adjacent critique variants trigger Claude fingerprint. Task-specific system prompt partially mitigates (+0.05 PTS). Validate on Mistral-7B (0.62, near Class III boundary) before deployment in open-weight settings.
