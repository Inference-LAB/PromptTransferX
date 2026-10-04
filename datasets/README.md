# Datasets Directory

## Files

| File | Description |
|---|---|
| `applicability_matrix.csv` | Pattern–task applicability (P=Primary, S=Secondary, -=Not applicable) |
| `dataset_config.json` | Dataset configurations, HuggingFace paths, splits, metrics |
| `samples/` | 3 sample instances per dataset for harness testing |

## Datasets used

| Task | Dataset | HuggingFace path | License |
|---|---|---|---|
| Mathematical Reasoning | GSM8K | `gsm8k` | MIT |
| Commonsense Inference | HellaSwag | `Rowan/hellaswag` | MIT |
| Code Generation | HumanEval | `openai_humaneval` | MIT |
| Medical QA | MedQA-USMLE | `bigbio/med_qa` | MIT |
| Creative Writing | WritingPrompts | `euclaise/writingprompts` | — |
| Hallucination Resistance | TruthfulQA | `truthful_qa` | Apache 2.0 |
| Instruction Following | IFEval + CFBench | `google/IFEval`, `opencompass/CFBench` | Apache 2.0 |

## Applicability matrix

The applicability matrix specifies which patterns are evaluated on which tasks.
Portability scores are computed **only on applicable pairings** (P or S).
Non-applicable pairings (—) are excluded from all aggregate statistics.

Applicability judgments were derived from:
1. The specification's stated mechanism (from White et al. and source papers)
2. The PromptPrism linguistic level (Jeoung et al., 2025)
3. The task's evaluation objective and output format

Inter-rater reliability: Two NLP researchers, κ = 0.81.

## Loading datasets

```python
from datasets import load_dataset

gsm8k     = load_dataset("gsm8k", "main", split="test")
hellaswag = load_dataset("Rowan/hellaswag", split="validation")
humaneval = load_dataset("openai_humaneval", split="test")
medqa     = load_dataset("bigbio/med_qa", "med_qa_en_source", split="test")
truthfulqa = load_dataset("truthful_qa", "generation", split="validation")
ifeval    = load_dataset("google/IFEval", split="train")
```
