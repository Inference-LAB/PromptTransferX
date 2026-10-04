# Evaluation Harness

## Files

| File | Description |
|---|---|
| `evaluate.py` | Main evaluation loop (full protocol specification) |
| `pts_scorer.py` | PTS metric: Acc, FmtAdh, BehInt, Consist, sensitivity analysis |
| `judge_protocol.py` | Three-judge BehInt scoring with self-preference bias control |
| `portability_metrics.py` | Transfer, U(P), S(P), Portability, PSI computation |
| `statistical_analysis.py` | Friedman, Wilcoxon, bootstrap CI, point-biserial, ANOVA |

## Setup

```bash
pip install openai anthropic google-generativeai scipy
```

For local vLLM inference:
```bash
pip install vllm
python -m vllm.entrypoints.openai.api_server \
    --model Meta-Llama-3-70B-Instruct \
    --dtype bfloat16 \
    --port 8000
```

## Running evaluation

```python
from harness.evaluate import run_evaluation, MODELS, TASKS, load_variants, load_applicability_matrix

variants      = load_variants("../variants/variants_all.json")
applicability = load_applicability_matrix("../datasets/applicability_matrix.csv")

def dataset_loader(task_id):
    # Return list of task instances for the given task
    # Each instance: {"TASK": "...", "answer": "...", ...}
    ...

results = run_evaluation(
    patterns=["P01", ..., "P24"],
    models=MODELS,
    tasks=TASKS,
    variants=variants,
    applicability=applicability,
    dataset_loader=dataset_loader,
    output_path="../results/primary_pts_scores.csv",
)
```

## Evaluation protocol

- **Runs:** 5 independent samples per (pattern, model, task, variant)
- **Variants:** 4 per pattern (V-A canonical + V-B, V-C, V-D)
- **Temperature:** 0.0 for deterministic tasks; 0.7 for creative writing
- **System prompt:** null for primary evaluation
- **Max tokens:** 1024
- **PTS:** mean across 4 × 5 = 20 samples per cell

## Adding new models

Add to `MODELS` dict in `evaluate.py`, implement the `query_model` branch for the
new API, and run the evaluation loop. PSI will auto-update against M5 (Mistral-7B).
If replacing M5 with a new weakest-tier model, update `OPEN_WEIGHT_TIER` in
`portability_metrics.py` and re-calibrate PSI thresholds per Guideline G7.
