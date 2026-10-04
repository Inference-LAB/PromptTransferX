# P20 — ReAct

| Field | Value |
|---|---|
| **ID** | P20 |
| **Name** | ReAct |
| **Category** | Reasoning Augmentation |
| **Origin** | Yao et al. (2022) |
| **PromptPrism Level** | Structural / Semantic |
| **Volatility Class** | III — Model-Specific |
| **Transfer** | 0.59 [.53,.66] |
| **Restricted Transfer** | 0.74 [.67,.80] |
| **PSI** | 0.21 |
| **Core Mechanism** | Interleaved reasoning and action |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.81 | ±.03 |
| Claude 3 Opus (M2) | 0.79 | ±.04 |
| Gemini 1.5 Pro (M3) | 0.77 | ±.04 |
| LLaMA-3-70B-Instruct (M4) | 0.69 | ±.05 |
| Mistral-7B-Instruct (M5) | 0.60 | ±.07 |
| MedLLaMA-2-7B (M6) | 0.48 | ±.08 |

## Canonical Specification (V-A)

```
Solve [TASK] using the ReAct format. Alternate between Thought and Action steps:
Thought: [reason about current state]
Action: [specify what you would do or look up]
Observation: [what the action yields]
...repeat until...
Final Answer: [conclusion]
```

## Deployment Guidance

The Thought-Action-Observation loop requires schema maintenance that degrades significantly in 7B models (Mistral: 0.60, near Class III boundary). MedLLaMA-2 approaches Class IV (0.48). Reliable only on frontier and 70B+ models. Best suited for agentic task categories not included in this evaluation set.
