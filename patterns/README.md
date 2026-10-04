# Patterns Directory

This directory contains the 24 canonical prompt specifications evaluated in PromptTransferX.

## File naming

`P{ID}_{snake_case_name}.md`

## Pattern metadata fields

Each file contains:

| Field | Description |
|---|---|
| `ID` | Pattern identifier (P01–P24) |
| `Name` | Full pattern name |
| `Category` | Functional category (White et al. taxonomy) |
| `Origin` | Source paper/catalog |
| `PromptPrism Level` | Structural / Semantic / Pragmatic (Jeoung et al., 2025) |
| `Volatility Class` | I / II / II* / III / IV |
| `Transfer` | min/max PTS ratio with 95% bootstrapped CI |
| `Restricted Transfer` | Transfer excluding MedLLaMA-2 |
| `PSI` | Pattern Stability Index = PTS(GPT-4o) − PTS(Mistral-7B) |
| `Core Mechanism` | One-sentence mechanism description |
| `Canonical Specification` | The V-A (primary) instantiation |
| `Per-model PTS` | Mean PTS per model with ±CI |
| `Deployment Guidance` | Practitioner recommendation |

## Volatility Class boundaries (revised post-pilot)

- **Class I — Stable:** Transfer ≥ 0.75
- **Class II — Context-Sensitive:** 0.60–0.74
- **Class II\* — Claude-Divergent:** 0.60–0.74, with Claude-family fingerprint
- **Class III — Model-Specific:** 0.45–0.59
- **Class IV — Brittle:** < 0.45

> Taxonomy correction: P14 (Transfer = 0.48) → Class III. P24 (Transfer = 0.60) → Class II. See `docs/taxonomy_corrections.md`.

## PSI thresholds

| PSI | Tier gap interpretation |
|---|---|
| < 0.15 | Stable cross-tier |
| 0.15–0.25 | Context-sensitive |
| 0.25–0.35 | Model-specific |
| > 0.35 | Brittle |
| Negative | Open-weight outperforms proprietary (P11 only) |
