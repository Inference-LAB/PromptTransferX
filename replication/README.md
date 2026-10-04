# Replication Directory

Secondary analyses extending the primary evaluation.

| File | Study |
|---|---|
| `cross_generation_2026.csv` | All 24 patterns on Claude Opus 4.6 (M7) and Qwen3-14B (M8) — Math + IF tasks, Aug 2026 |
| `cross_lingual_arabic.csv` | 7 patterns (4 Class I + 3 Class IV) on Arabic MMLU — GPT-4o and LLaMA-3-70B, N=200 |

## Cross-generation findings

- Class I designations stable on both new models
- Claude fingerprint intensifies: P11 PTS 0.12 (Opus 3) → 0.09 (Opus 4.6)
- Qwen3-14B mean PTS 0.681 vs. Mistral-7B 0.627 — proprietary-open gap narrowing

## Cross-lingual findings

- Class I Arabic Transfer = 0.76 vs. Class IV = 0.42
- P05 Arabic PTS within 0.05 of English PTS on both models
- Results are preliminary: N=7 patterns, 2 models; directionally consistent only
