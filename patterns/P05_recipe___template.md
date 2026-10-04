# P05 — Recipe / Template

| Field | Value |
|---|---|
| **ID** | P05 |
| **Name** | Recipe / Template |
| **Category** | Output Customization |
| **Origin** | White et al. (2023) |
| **PromptPrism Level** | Structural |
| **Volatility Class** | I — Stable |
| **Transfer** | 0.82 [.78,.86] |
| **Restricted Transfer** | 0.87 [.83,.91] |
| **PSI** | 0.11 |
| **Core Mechanism** | Constrained sequential output structure |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.84 | ±.03 |
| Claude 3 Opus (M2) | 0.82 | ±.03 |
| Gemini 1.5 Pro (M3) | 0.80 | ±.03 |
| LLaMA-3-70B-Instruct (M4) | 0.78 | ±.04 |
| Mistral-7B-Instruct (M5) | 0.73 | ±.05 |
| MedLLaMA-2-7B (M6) | 0.69 | ±.05 |

## Canonical Specification (V-A)

```
Provide the solution in exactly the following structure:
[STEP 1:]
[STEP 2:]
[STEP 3:]
[LIMITATIONS:]
[NEXT ACTIONS:]

Do not deviate from this format. Fill each section completely. Task: [TASK]
```

## Deployment Guidance

Deploy with confidence across heterogeneous backends. Highest Transfer in the benchmark (0.82); best pattern for Instruction Following (0.91) and Code Generation (0.88). PSI=0.11 is the second-lowest in the catalog. Validate on weakest target model as standard pre-deployment check.
