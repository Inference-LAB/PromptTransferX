# P24 — Narrative-of-Thought

| Field | Value |
|---|---|
| **ID** | P24 |
| **Name** | Narrative-of-Thought |
| **Category** | Reasoning Augmentation |
| **Origin** | Zhang et al. (2024) |
| **PromptPrism Level** | Semantic / Structural |
| **Volatility Class** | II — Context-Sensitive |
| **Transfer** | 0.60 [.53,.67] |
| **Restricted Transfer** | 0.74 [.67,.80] |
| **PSI** | 0.22 |
| **Core Mechanism** | Narrative-form temporal reasoning |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.77 | ±.04 |
| Claude 3 Opus (M2) | 0.75 | ±.04 |
| Gemini 1.5 Pro (M3) | 0.73 | ±.04 |
| LLaMA-3-70B-Instruct (M4) | 0.64 | ±.06 |
| Mistral-7B-Instruct (M5) | 0.55 | ±.07 |
| MedLLaMA-2-7B (M6) | 0.46 | ±.09 |

## Canonical Specification (V-A)

```
Reason through [TASK] by constructing a narrative: tell the story of how you move from the problem to the solution. Use temporal connectives (first, then, next, finally). The narrative structure should make the reasoning flow clear. Conclude with the explicit answer.
```

## Deployment Guidance

**TAXONOMY CORRECTION:** Transfer=0.60 equals the Class II lower bound; correctly Class II (not Class III as stated in earlier drafts). See docs/taxonomy_corrections.md. Large open-weight gap (Mistral: 0.55, MedLLaMA-2: 0.46). Strongest on Creative Writing and Commonsense Inference. Validate per task category before deployment.
