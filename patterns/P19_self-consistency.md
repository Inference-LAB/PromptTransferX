# P19 — Self-Consistency

| Field | Value |
|---|---|
| **ID** | P19 |
| **Name** | Self-Consistency |
| **Category** | Reasoning Augmentation |
| **Origin** | Wang et al. (2022) |
| **PromptPrism Level** | Structural |
| **Volatility Class** | II — Context-Sensitive |
| **Transfer** | 0.71 [.65,.77] |
| **Restricted Transfer** | 0.85 [.81,.89] |
| **PSI** | 0.13 |
| **Core Mechanism** | Multi-path majority voting |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.87 | ±.03 |
| Claude 3 Opus (M2) | 0.85 | ±.03 |
| Gemini 1.5 Pro (M3) | 0.84 | ±.03 |
| LLaMA-3-70B-Instruct (M4) | 0.80 | ±.04 |
| Mistral-7B-Instruct (M5) | 0.74 | ±.05 |
| MedLLaMA-2-7B (M6) | 0.62 | ±.07 |

## Canonical Specification (V-A)

```
Solve [TASK] using three independent reasoning paths. Do not let one path influence another. Label them Path A, Path B, Path C. After completing all three independently, identify the answer that appears in the majority of paths and state it as your final answer.
```

## Deployment Guidance

Best pattern for Mathematical Reasoning (Transfer=0.84). Near-Class-I when excluding MedLLaMA-2. The majority-voting mechanism is robustly implemented across frontier and large open-weight models. MedLLaMA-2 (0.62) is the main cross-model gap driver.
