# PromptTransferX

**Cross-Model Behavioral Portability of Prompt Specifications in LLM-Based Intelligent Systems**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Evaluation Window](https://img.shields.io/badge/Evaluation-Mar–Aug%202026-green)](docs/model_log.md)
[![Patterns](https://img.shields.io/badge/Patterns-24-orange)](patterns/)
[![Models](https://img.shields.io/badge/Models-6%20primary%20%2B%202%20replication-purple)](docs/model_log.md)

---

## Overview

PromptTransferX is a benchmark and measurement framework for evaluating the **cross-model behavioral portability** of structured prompt specifications across heterogeneous LLM backends. It addresses the following system-level question:

> When an LLM backend is substituted, upgraded, or diversified in a deployed intelligent system, does the same prompt specification preserve its intended behavior?

The benchmark evaluates **24 canonical prompt specifications** across **6 heterogeneous LLM backends**, **7 task categories**, and **5 standardized datasets**, using a human-calibrated composite metric (Prompt Transfer Score, PTS) and a three-judge evaluation protocol.

---

## Key Findings

| Finding | Result |
|---|---|
| Patterns achieving Transfer ≥ 0.70 | **11 of 24** |
| Mean Transfer score (all 24 patterns) | **0.581** |
| Mean PTS (all conditions) | **0.638 (SD = 0.142)** |
| Structural vs. Pragmatic portability gap | **point-biserial r = 0.62, p < 0.01** |
| Claude-family fingerprint (P11) | **Z = 6.84, p < 0.001, r = 0.87** |
| PTS human calibration | **κ = 0.84; Spearman ρ = 0.86** |

---

## Repository Structure

```
PromptTransferX/
├── README.md                        # This file
├── LICENSE
├── CITATION.cff
│
├── patterns/                        # 24 canonical prompt specifications
│   ├── README.md
│   ├── P01_meta_language_creation.md
│   ├── P02_output_automater.md
│   ├── P03_persona.md
│   ├── P04_visualization_generator.md
│   ├── P05_recipe_template.md
│   ├── P06_fact_check_list.md
│   ├── P07_reflection.md
│   ├── P08_question_refinement.md
│   ├── P09_alternative_approaches.md
│   ├── P10_cognitive_verifier.md
│   ├── P11_constraint_reframing.md
│   ├── P12_flipped_interaction.md
│   ├── P13_game_play.md
│   ├── P14_infinite_generation.md
│   ├── P15_context_manager.md
│   ├── P16_context_ignoring_resistance.md
│   ├── P17_chain_of_thought.md
│   ├── P18_auto_cot.md
│   ├── P19_self_consistency.md
│   ├── P20_react.md
│   ├── P21_self_refine.md
│   ├── P22_logic_of_thought.md
│   ├── P23_chain_of_draft.md
│   └── P24_narrative_of_thought.md
│
├── variants/                        # 72 validated paraphrastic variants (3 per pattern)
│   ├── README.md
│   └── variants_all.json            # Machine-readable; all 24 × 3 variants
│
├── datasets/                        # Dataset configuration and sample instances
│   ├── README.md
│   ├── dataset_config.json
│   ├── applicability_matrix.csv
│   └── samples/
│       ├── gsm8k_sample.json
│       ├── hellaswag_sample.json
│       ├── humaneval_sample.json
│       ├── medqa_sample.json
│       ├── truthfulqa_sample.json
│       ├── writingprompts_sample.json
│       └── ifeval_cfbench_sample.json
│
├── harness/                         # Evaluation harness pseudocode and scripts
│   ├── README.md
│   ├── evaluate.py                  # Main evaluation loop (pseudocode + structure)
│   ├── pts_scorer.py                # PTS metric computation
│   ├── judge_protocol.py            # Three-judge BehInt scoring
│   ├── portability_metrics.py       # Transfer, U(P), S(P), Π(P), PSI
│   └── statistical_analysis.py     # Friedman, Wilcoxon, bootstrap CIs
│
├── rubrics/                         # Per-class BehInt scoring rubrics
│   ├── README.md
│   ├── rubric_class_I.md
│   ├── rubric_class_II.md
│   ├── rubric_class_IIstar.md
│   ├── rubric_class_III.md
│   ├── rubric_class_IV.md
│   └── rubric_pts_weights.md
│
├── results/                         # Empirical score tables
│   ├── README.md
│   ├── primary_pts_scores.csv       # PTS per (pattern × model) with 95% CIs
│   ├── transfer_scores.csv          # Transfer, Restricted Transfer, PSI, Class
│   ├── model_level_means.csv        # Mean PTS per model
│   ├── task_category_transfer.csv   # Transfer by task category
│   └── volatility_taxonomy.csv     # Class assignments with justification
│
├── ablations/                       # Ablation study results
│   ├── README.md
│   ├── temperature_sensitivity.csv
│   ├── system_prompt_sensitivity.csv
│   ├── phrasing_variation_anova.csv
│   └── pts_weight_robustness.csv
│
├── replication/                     # Cross-generation and cross-lingual data
│   ├── README.md
│   ├── cross_generation_2026.csv    # Claude Opus 4.6 + Qwen3-14B
│   └── cross_lingual_arabic.csv    # Arabic MMLU replication
│
└── docs/                            # Supporting documentation
    ├── model_log.md                 # Exact model versions and API timestamps
    ├── taxonomy_corrections.md      # P14 and P24 classification corrections
    ├── ethics_p11.md                # Ethics statement for Constraint Reframing
    └── guidelines.md                # Seven evidence-based design guidelines
```

---

## Quick Start


### Exploring Patterns

Each pattern file in `patterns/` contains:
- Canonical specification (V-A)
- Pattern metadata (class, PSI, PromptPrism level, origin)
- Per-model PTS scores
- Design guidance

### Replicating Evaluation

See `harness/evaluate.py` for the full evaluation loop specification and `harness/pts_scorer.py` for the PTS metric implementation.

---

## Volatility Taxonomy (Revised Boundaries)

| Class | Transfer Range | Patterns | Deployment |
|---|---|---|---|
| **I — Stable** | ≥ 0.75 | P05, P15, P18, P23 | Deploy across heterogeneous backends |
| **II — Context-Sensitive** | 0.60–0.74 | P02, P03, P06, P08, P09, P17, P19, P24 | Validate per task category |
| **II\* — Claude-Divergent** | 0.60–0.74 | P07, P10, P16, P21 | Apply G4 mitigation (task-specific system prompt) |
| **III — Model-Specific** | 0.45–0.59 | P04, P12, P13, P14, P20, P22 | Model-specific calibration required |
| **IV — Brittle** | < 0.45 | P01, P11 | Avoid in multi-backend systems |

> **Taxonomy corrections:** P14 (Transfer = 0.48) is Class III, not IV. P24 (Transfer = 0.60) is Class II, not III. See `docs/taxonomy_corrections.md`.

---

## License

MIT License. See [LICENSE](LICENSE).

Raw LLM API outputs may be subject to model provider terms of service.
