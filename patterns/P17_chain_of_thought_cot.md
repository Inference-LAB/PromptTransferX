# P17 — Chain of Thought (CoT)

| Field | Value |
|---|---|
| **ID** | P17 |
| **Name** | Chain of Thought (CoT) |
| **Category** | Reasoning Augmentation |
| **Origin** | Wei et al. (2022) |
| **PromptPrism Level** | Structural |
| **Volatility Class** | II — Context-Sensitive |
| **Transfer** | 0.73 [.67,.78] |
| **Restricted Transfer** | 0.86 [.82,.90] |
| **PSI** | 0.12 |
| **Core Mechanism** | Intermediate step verbalization |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.88 | ±.03 |
| Claude 3 Opus (M2) | 0.86 | ±.03 |
| Gemini 1.5 Pro (M3) | 0.85 | ±.03 |
| LLaMA-3-70B-Instruct (M4) | 0.82 | ±.04 |
| Mistral-7B-Instruct (M5) | 0.76 | ±.05 |
| MedLLaMA-2-7B (M6) | 0.64 | ±.07 |

## Canonical Specification (V-A)

```
Let's work through this step by step. First, identify the key constraints and given information. Then, consider each relevant factor in turn. Show your intermediate reasoning clearly. Finally, synthesize a conclusion. Problem: [TASK]
```

## Deployment Guidance

Best pattern for Commonsense Inference (0.82). Near-Class-I when excluding MedLLaMA-2 (Restricted Transfer=0.86). PSI=0.12 is among the lowest in the catalog. Note for 2026 evaluation: Qwen3-14B achieves CoT PTS=0.84, near LLaMA-3-70B (0.82)—proprietary-open gap narrowing for reasoning tasks.
