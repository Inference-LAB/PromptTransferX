# P03 — Persona

| Field | Value |
|---|---|
| **ID** | P03 |
| **Name** | Persona |
| **Category** | Output Customization |
| **Origin** | White et al. (2023) |
| **PromptPrism Level** | Semantic |
| **Volatility Class** | II — Context-Sensitive |
| **Transfer** | 0.74 [.69,.79] |
| **Restricted Transfer** | 0.83 [.78,.87] |
| **PSI** | 0.15 |
| **Core Mechanism** | Role identity assignment |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.88 | ±.03 |
| Claude 3 Opus (M2) | 0.84 | ±.04 |
| Gemini 1.5 Pro (M3) | 0.86 | ±.03 |
| LLaMA-3-70B-Instruct (M4) | 0.79 | ±.04 |
| Mistral-7B-Instruct (M5) | 0.73 | ±.05 |
| MedLLaMA-2-7B (M6) | 0.65 | ±.06 |

## Canonical Specification (V-A)

```
From this point, you are Dr. Maya Chen, a senior clinical pharmacologist with 20 years of experience in drug interaction research. Respond only as Dr. Chen would—with her depth of expertise, her communication style, and her professional vocabulary. [TASK]
```

## Deployment Guidance

Good general-purpose transferability. Strongest on creative and domain-specific tasks (Persona achieves Transfer=0.83 on Creative Writing). Validate on Mistral-7B for formal domains.
