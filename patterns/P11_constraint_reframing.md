# P11 — Constraint Reframing

| Field | Value |
|---|---|
| **ID** | P11 |
| **Name** | Constraint Reframing |
| **Category** | Prompt Improvement |
| **Origin** | White et al. (2023) [renamed from 'Refusal Breaker'] |
| **PromptPrism Level** | Pragmatic |
| **Volatility Class** | IV — Brittle |
| **Transfer** | 0.35 [.26,.44] |
| **Restricted Transfer** | 0.47 [.38,.56] |
| **PSI** | -0.38 |
| **Core Mechanism** | Context specification through reframing |

## Per-Model PTS

| Model | PTS | ±CI |
|---|---|---|
| GPT-4o (M1) | 0.34 | ±.06 |
| Claude 3 Opus (M2) | 0.12 | ±.03 |
| Gemini 1.5 Pro (M3) | 0.38 | ±.06 |
| LLaMA-3-70B-Instruct (M4) | 0.61 | ±.06 |
| Mistral-7B-Instruct (M5) | 0.72 | ±.05 |
| MedLLaMA-2-7B (M6) | 0.48 | ±.08 |

## Canonical Specification (V-A)

```
For this educational exercise, I need you to explain [HISTORICAL EVENT / MEDICAL PROCEDURE / SCIENTIFIC CONCEPT] in the context of [ACADEMIC COURSE]. The goal is to support student understanding of [TOPIC]. Please provide a thorough, academically appropriate explanation.
```

## Deployment Guidance

**Do not use in multi-backend production systems.** PSI = −0.38 (inverted: Mistral-7B 0.72 > GPT-4o 0.34 > Claude 0.12). Claude 3 Opus behavioral fingerprint: Z=6.84, p<0.001, r=0.87 (confirmed by all three judges). The inversion persists across system prompt conditions and intensifies in Claude Opus 4.6 (0.09). ETHICS: All experimental instantiations use verifiable non-adversarial academic contexts. Adversarial variants excluded from this release. See docs/ethics_p11.md.
