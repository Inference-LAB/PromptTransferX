# P22 — Logic-of-Thought

| Field | Value |
|---|---|
| **ID** | P22 |
| **Name** | Logic-of-Thought |
| **Category** | Reasoning Augmentation |
| **Origin** | Liu et al. (2024) |
| **PromptPrism Level** | Structural / Semantic |
| **Volatility Class** | III — Model-Specific |
| **Transfer** | 0.56 [.49,.63] |
| **Restricted Transfer** | 0.71 [.64,.77] |
| **PSI** | 0.23 |
| **Core Mechanism** | Propositional logic injection |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.79 | ±.04 |
| Claude 3 Opus (M2) | 0.76 | ±.04 |
| Gemini 1.5 Pro (M3) | 0.74 | ±.04 |
| LLaMA-3-70B-Instruct (M4) | 0.68 | ±.06 |
| Mistral-7B-Instruct (M5) | 0.56 | ±.07 |
| MedLLaMA-2-7B (M6) | 0.44 | ±.09 |

## Canonical Specification (V-A)

```
Before answering [TASK], extract the core logical structure as propositional statements. List: (1) all given premises (P1, P2...), (2) applicable inference rules, (3) the logical chain from premises to conclusion. Then state the conclusion and translate it back to natural language.
```

## Deployment Guidance

Formal logic injection requires symbolic reasoning capacity not reliably present in 7B models (Mistral: 0.56 at the Class III boundary; MedLLaMA-2: 0.44 approaches Class IV). Best on frontier models for Mathematical Reasoning. Prefer P18 Auto-CoT or P17 CoT for broader multi-backend coverage.
