# Variants Directory

This directory contains all 72 validated paraphrastic variants (3 per pattern × 24 patterns).

## File

- `variants_all.json` — All 72 variants in machine-readable JSON format

## Variant naming

Each pattern has four phrasings:
- **V-A** — Canonical specification (also in `patterns/` directory)
- **V-B** — Paraphrastic variant B
- **V-C** — Paraphrastic variant C  
- **V-D** — Paraphrastic variant D

## Construction protocol

Variants were constructed by two NLP researchers and cross-validated for intent fidelity (inter-rater κ = 0.84). Rules:
1. Preserve the core behavioral mechanism of the canonical specification
2. Rephrase surface form using different syntactic structures
3. Do not add or remove behavioral constraints relative to V-A
4. Verify that the intended PTS components (Acc, FmtAdh, BehInt, Consist) remain evaluable

## Usage in evaluation

PTS is computed as the **mean across all four phrasings** (V-A, V-B, V-C, V-D). Reporting only the best-performing phrasing inflates transferability claims by up to 22.7% (phrasing variation partial η² = 0.227).

## Placeholder conventions

| Placeholder | Meaning |
|---|---|
| `[TASK]` | The specific task or problem to solve |
| `[TOPIC]` | Subject matter domain |
| `[INPUT]` | Raw input to process |
| `[CONTEXT_TEXT]` | Provided context/document |
| `[GOAL]` | Target objective |
| `[PERSONA_NAME]` | Named persona |
| `[ROLE]` | Professional role description |
| `[DOMAIN]` | Knowledge domain |
| `[BACKGROUND]` | Persona background description |
| `[STYLE]` | Communication style specification |
| `[EXPERTISE]` | Area of expertise |
| `[OUTPUT_FORMAT]` | Desired output format |
