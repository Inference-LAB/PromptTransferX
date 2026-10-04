# P14 — Infinite Generation

| Field | Value |
|---|---|
| **ID** | P14 |
| **Name** | Infinite Generation |
| **Category** | Interaction |
| **Origin** | White et al. (2023) |
| **PromptPrism Level** | Structural / Pragmatic |
| **Volatility Class** | III — Model-Specific |
| **Transfer** | 0.48 [.40,.56] |
| **Restricted Transfer** | 0.64 [.56,.72] |
| **PSI** | 0.25 |
| **Core Mechanism** | Continuous bounded output loop |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.69 | ±.05 |
| Claude 3 Opus (M2) | 0.65 | ±.05 |
| Gemini 1.5 Pro (M3) | 0.62 | ±.05 |
| LLaMA-3-70B-Instruct (M4) | 0.51 | ±.07 |
| Mistral-7B-Instruct (M5) | 0.44 | ±.08 |
| MedLLaMA-2-7B (M6) | 0.33 | ±.09 |

## Canonical Specification (V-A)

```
Generate a continuous list of [ITEMS] related to [TOPIC]. After each batch of 10, print "CONTINUE?" and wait. When I say "continue," generate the next 10 without repeating any previous items. Track the total count. Begin with items 1–10.
```

## Deployment Guidance

**TAXONOMY CORRECTION:** Transfer=0.48 ≥ 0.45; correctly Class III (not Class IV as stated in earlier drafts). See docs/taxonomy_corrections.md. Loop-maintenance requires stateful behavior not reliably sustained across model families at the 7B scale. Creative Writing shows the worst task-specific result (0.39). Not recommended for open-weight models below 70B without explicit calibration.
