# P04 — Visualization Generator

| Field | Value |
|---|---|
| **ID** | P04 |
| **Name** | Visualization Generator |
| **Category** | Output Customization |
| **Origin** | White et al. (2023) |
| **PromptPrism Level** | Structural / Semantic |
| **Volatility Class** | III — Model-Specific |
| **Transfer** | 0.57 [.51,.63] |
| **Restricted Transfer** | 0.70 [.64,.76] |
| **PSI** | 0.23 |
| **Core Mechanism** | Structured visual output elicitation |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.77 | ±.04 |
| Claude 3 Opus (M2) | 0.73 | ±.05 |
| Gemini 1.5 Pro (M3) | 0.71 | ±.04 |
| LLaMA-3-70B-Instruct (M4) | 0.62 | ±.06 |
| Mistral-7B-Instruct (M5) | 0.54 | ±.07 |
| MedLLaMA-2-7B (M6) | 0.44 | ±.08 |

## Canonical Specification (V-A)

```
Generate a text-based visualization of [TOPIC/DATA]. Use ASCII art, tables, tree structures, or diagrams as appropriate. The visualization should make the structure or relationships immediately apparent without any additional explanation. Topic: [TASK]
```

## Deployment Guidance

Model-specific calibration required. Large variance across tiers; MedLLaMA-2 (0.44) near Class IV. Reliable only on frontier models. Prefer P05 Recipe/Template as a structural alternative for code/generation tasks.
