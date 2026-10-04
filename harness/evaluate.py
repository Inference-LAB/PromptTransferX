"""
PromptTransferX — Main Evaluation Loop
=======================================
This module implements the primary evaluation loop for computing PTS
(Prompt Transfer Score) for each (pattern, model, task) tuple.

Protocol:
  - 24 patterns × 6 primary models × 7 tasks (applicability-filtered)
  - 4 paraphrastic variants per pattern (V-A canonical + V-B, V-C, V-D)
  - 5 independent runs per (pattern, model, task, variant) tuple
  - Temperature: 0.0 for deterministic tasks; 0.7 for creative writing
  - System prompt: null (primary evaluation)
  - Max tokens: 1024

PTS = 0.40·Acc + 0.20·FmtAdh + 0.25·BehInt + 0.15·Consist

Transfer(P)     = min_M[PTS(P,M)] / max_M[PTS(P,M)]
U(P)            = mean_M[PTS(P,M)]
S(P)            = 1 - std_M[PTS(P,M)] / (mean_M[PTS(P,M)] + 0.01)
Portability(P)  = U(P) × S(P)
PSI(P)          = PTS(P, GPT-4o) - PTS(P, Mistral-7B)
"""

import json
import statistics
from pathlib import Path
from typing import Optional


# ── Configuration ─────────────────────────────────────────────────────────────

MODELS = {
    "M1": {"name": "GPT-4o",                  "api": "openai",     "model_id": "gpt-4o-2024-08-06"},
    "M2": {"name": "Claude 3 Opus",            "api": "anthropic",  "model_id": "claude-3-opus-20240229"},
    "M3": {"name": "Gemini 1.5 Pro",           "api": "google",     "model_id": "gemini-1.5-pro-latest"},
    "M4": {"name": "LLaMA-3-70B-Instruct",     "api": "local_vllm", "model_id": "Meta-Llama-3-70B-Instruct"},
    "M5": {"name": "Mistral-7B-Instruct-v0.3", "api": "local_vllm", "model_id": "Mistral-7B-Instruct-v0.3"},
    "M6": {"name": "MedLLaMA-2-7B",            "api": "local_vllm", "model_id": "medllama2_7b"},
}

TASKS = {
    "MATH":   {"name": "Mathematical Reasoning",   "dataset": "gsm8k",       "metric": "exact_match", "temperature": 0.0},
    "COMMON": {"name": "Commonsense Inference",    "dataset": "hellaswag",   "metric": "accuracy_mc",  "temperature": 0.0},
    "CODE":   {"name": "Code Generation",          "dataset": "humaneval",   "metric": "pass_at_1",    "temperature": 0.0},
    "MED":    {"name": "Medical QA",               "dataset": "medqa_usmle", "metric": "accuracy_mc",  "temperature": 0.0},
    "CW":     {"name": "Creative Writing",         "dataset": "writingprompts", "metric": "judge_score", "temperature": 0.7},
    "HALL":   {"name": "Hallucination Resistance", "dataset": "truthfulqa",  "metric": "truthful_pct", "temperature": 0.0},
    "IF":     {"name": "Instruction Following",    "dataset": "ifeval+cfbench", "metric": "prompt_acc", "temperature": 0.0},
}

N_RUNS     = 5      # independent samples per (pattern, model, task, variant)
N_VARIANTS = 4      # V-A (canonical) + V-B, V-C, V-D
MAX_TOKENS = 1024
EPSILON    = 0.01   # stability denominator guard


# ── Applicability check ───────────────────────────────────────────────────────

def load_applicability_matrix(path: str = "../datasets/applicability_matrix.csv") -> dict:
    """Load the pattern-task applicability matrix.

    Returns:
        dict: {pattern_id: {task_id: "P"|"S"|"-"}}
    """
    import csv
    matrix = {}
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            pid = row["pattern_id"]
            matrix[pid] = {k: v for k, v in row.items() if k != "pattern_id"}
    return matrix


def is_applicable(pattern_id: str, task_id: str, matrix: dict) -> bool:
    """Return True if pattern is applicable (Primary or Secondary) to task."""
    return matrix.get(pattern_id, {}).get(task_id, "-") in ("P", "S")


# ── Model query ───────────────────────────────────────────────────────────────

def query_model(
    model_cfg: dict,
    prompt: str,
    temperature: float = 0.0,
    max_tokens: int = MAX_TOKENS,
    system_prompt: Optional[str] = None,
    seed: Optional[int] = None,
) -> str:
    """Query an LLM backend and return the raw text response.

    NOTE: This function is a structural specification. Replace the body
    with API calls to the appropriate provider SDK.

    Args:
        model_cfg: Model configuration dict from MODELS.
        prompt: Fully instantiated prompt string.
        temperature: Sampling temperature.
        max_tokens: Maximum output tokens.
        system_prompt: Optional system message (None = null for primary eval).
        seed: Random seed if supported by provider.

    Returns:
        str: Raw model output text.
    """
    api = model_cfg["api"]

    if api == "openai":
        # from openai import OpenAI
        # client = OpenAI()
        # messages = []
        # if system_prompt:
        #     messages.append({"role": "system", "content": system_prompt})
        # messages.append({"role": "user", "content": prompt})
        # resp = client.chat.completions.create(
        #     model=model_cfg["model_id"],
        #     messages=messages,
        #     temperature=temperature,
        #     max_tokens=max_tokens,
        #     seed=seed,
        # )
        # return resp.choices[0].message.content
        raise NotImplementedError("Install openai SDK and uncomment implementation")

    elif api == "anthropic":
        # import anthropic
        # client = anthropic.Anthropic()
        # kwargs = dict(model=model_cfg["model_id"], max_tokens=max_tokens,
        #               messages=[{"role": "user", "content": prompt}])
        # if system_prompt:
        #     kwargs["system"] = system_prompt
        # resp = client.messages.create(**kwargs)
        # return resp.content[0].text
        raise NotImplementedError("Install anthropic SDK and uncomment implementation")

    elif api == "google":
        # import google.generativeai as genai
        # model = genai.GenerativeModel(model_cfg["model_id"])
        # resp = model.generate_content(prompt,
        #     generation_config={"temperature": temperature, "max_output_tokens": max_tokens})
        # return resp.text
        raise NotImplementedError("Install google-generativeai SDK and uncomment implementation")

    elif api == "local_vllm":
        # from openai import OpenAI
        # client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
        # messages = [{"role": "user", "content": prompt}]
        # resp = client.chat.completions.create(
        #     model=model_cfg["model_id"], messages=messages,
        #     temperature=temperature, max_tokens=max_tokens)
        # return resp.choices[0].message.content
        raise NotImplementedError("Start vLLM server and uncomment implementation")

    raise ValueError(f"Unknown API type: {api}")


# ── Prompt instantiation ──────────────────────────────────────────────────────

def load_variants(variants_path: str = "../variants/variants_all.json") -> dict:
    """Load all 72 paraphrastic variants."""
    with open(variants_path) as f:
        return json.load(f)["patterns"]


def instantiate_prompt(
    pattern_id: str,
    variant: str,
    task_instance: dict,
    variants: dict,
    canonical_path: str = "../patterns/",
) -> str:
    """Build a fully instantiated prompt string.

    Args:
        pattern_id: e.g. "P05"
        variant: "VA" | "VB" | "VC" | "VD"
        task_instance: Dict with keys like "task", "topic", "input", etc.
        variants: Loaded variants dict.

    Returns:
        str: Filled-in prompt with [TASK], [TOPIC], etc. replaced.
    """
    if variant == "VA":
        # Load canonical from pattern markdown file
        import re
        pattern_files = list(Path(canonical_path).glob(f"{pattern_id}_*.md"))
        if not pattern_files:
            raise FileNotFoundError(f"No pattern file found for {pattern_id}")
        content = pattern_files[0].read_text()
        match = re.search(r"```\n(.*?)```", content, re.DOTALL)
        if not match:
            raise ValueError(f"No canonical specification block found in {pattern_files[0]}")
        template = match.group(1).strip()
    else:
        template = variants.get(pattern_id, {}).get(variant, "")
        if not template:
            raise ValueError(f"Variant {variant} not found for {pattern_id}")

    # Replace placeholders
    result = template
    for key, val in task_instance.items():
        result = result.replace(f"[{key.upper()}]", str(val))

    return result


# ── Accuracy evaluation ───────────────────────────────────────────────────────

def eval_accuracy(output: str, task_id: str, ground_truth: dict) -> float:
    """Compute task-specific accuracy for one model output.

    Args:
        output: Raw model output string.
        task_id: Task identifier from TASKS keys.
        ground_truth: Dict with expected answer/label.

    Returns:
        float: Accuracy score in [0, 1].
    """
    metric = TASKS[task_id]["metric"]

    if metric == "exact_match":
        # Extract final numeric answer from CoT output
        import re
        nums = re.findall(r"[-+]?\d*\.?\d+", output.replace(",", ""))
        predicted = nums[-1] if nums else ""
        return float(predicted == str(ground_truth.get("answer", "")))

    elif metric == "accuracy_mc":
        # Multiple-choice: check if correct letter appears in output
        correct = ground_truth.get("answer", "")
        return float(correct.upper() in output.upper()[:50])

    elif metric == "pass_at_1":
        # Code: run in sandbox and check test cases
        # Placeholder — replace with actual execution harness
        raise NotImplementedError("Connect to code execution sandbox")

    elif metric == "judge_score":
        # Creative writing: judge score handled in three_judge_score
        return 0.0  # placeholder; BehInt carries the creative score

    elif metric == "truthful_pct":
        # TruthfulQA: use GPT-4o judge for truthfulness classification
        raise NotImplementedError("Connect to TruthfulQA judge classifier")

    elif metric == "prompt_acc":
        # IFEval: check format constraints programmatically
        raise NotImplementedError("Connect to IFEval constraint checker")

    return 0.0


# ── PTS computation ───────────────────────────────────────────────────────────

def compute_pts(
    acc_scores: list[float],
    fmt_adh: float,
    beh_int: float,
) -> float:
    """Compute the Prompt Transfer Score for one (pattern, model, task) cell.

    PTS = 0.40·Acc + 0.20·FmtAdh + 0.25·BehInt + 0.15·Consist

    Args:
        acc_scores: List of N_RUNS × N_VARIANTS accuracy values.
        fmt_adh: Format adherence score [0, 1].
        beh_int: Behavioral intent score from three-judge protocol [0, 1].

    Returns:
        float: PTS in [0, 1].
    """
    acc_mean  = statistics.mean(acc_scores)
    consist   = 1.0 - statistics.stdev(acc_scores) if len(acc_scores) > 1 else 1.0

    pts = (0.40 * acc_mean
         + 0.20 * fmt_adh
         + 0.25 * beh_int
         + 0.15 * consist)
    return round(min(max(pts, 0.0), 1.0), 4)


# ── Portability metrics ───────────────────────────────────────────────────────

def compute_portability_metrics(pts_per_model: dict[str, float]) -> dict:
    """Compute Transfer, U(P), S(P), Portability, PSI from PTS per model.

    Args:
        pts_per_model: {model_id: pts_mean}

    Returns:
        dict with keys: transfer, utility, stability, portability, psi
    """
    scores = list(pts_per_model.values())
    utility    = statistics.mean(scores)
    stability  = 1.0 - statistics.stdev(scores) / (utility + EPSILON)
    transfer   = min(scores) / max(scores) if max(scores) > 0 else 0.0
    portability = utility * stability

    psi = None
    if "M1" in pts_per_model and "M5" in pts_per_model:
        psi = round(pts_per_model["M1"] - pts_per_model["M5"], 3)

    return {
        "transfer":    round(transfer, 3),
        "utility":     round(utility, 3),
        "stability":   round(stability, 3),
        "portability": round(portability, 3),
        "psi":         psi,
    }


def assign_volatility_class(transfer: float) -> str:
    """Assign a volatility class based on Transfer score.

    Revised taxonomy boundaries (post-pilot):
        I   >= 0.75   Stable
        II  0.60–0.74  Context-Sensitive
        III 0.45–0.59  Model-Specific
        IV  < 0.45     Brittle

    Note: Class II* (Claude-Divergent) is assigned post-hoc
    based on model-conditional analysis, not the Transfer score alone.
    """
    if transfer >= 0.75:
        return "I"
    elif transfer >= 0.60:
        return "II"
    elif transfer >= 0.45:
        return "III"
    else:
        return "IV"


# ── Main loop ─────────────────────────────────────────────────────────────────

def run_evaluation(
    patterns: list[str],
    models: dict,
    tasks: dict,
    variants: dict,
    applicability: dict,
    dataset_loader,
    output_path: str = "../results/primary_pts_scores.csv",
    n_runs: int = N_RUNS,
) -> dict:
    """Run the full PromptTransferX evaluation.

    Args:
        patterns: List of pattern IDs (e.g. ["P01", ..., "P24"]).
        models: MODELS dict.
        tasks: TASKS dict.
        variants: Loaded variants dict.
        applicability: Applicability matrix dict.
        dataset_loader: Callable(task_id) -> list[dict] of instances.
        output_path: Where to write the CSV results.
        n_runs: Number of independent runs per cell.

    Returns:
        dict: Nested results {pattern_id: {model_id: {task_id: pts}}}
    """
    from pts_scorer import eval_format_adherence
    from judge_protocol import three_judge_score

    all_results = {}

    for pid in patterns:
        all_results[pid] = {}

        for mid, model_cfg in models.items():
            pts_by_task = {}

            for tid, task_cfg in tasks.items():
                if not is_applicable(pid, tid, applicability):
                    continue

                instances = dataset_loader(tid)
                acc_scores = []

                for instance in instances:
                    for variant_key in ["VA", "VB", "VC", "VD"]:
                        prompt = instantiate_prompt(pid, variant_key, instance, variants)

                        for run in range(n_runs):
                            output = query_model(
                                model_cfg,
                                prompt,
                                temperature=task_cfg["temperature"],
                                system_prompt=None,  # null for primary eval
                            )
                            acc = eval_accuracy(output, tid, instance)
                            acc_scores.append(acc)

                # Aggregate PTS components
                fmt_adh = eval_format_adherence(pid, acc_scores)
                beh_int = three_judge_score(pid, acc_scores)

                pts = compute_pts(acc_scores, fmt_adh, beh_int)
                pts_by_task[tid] = pts

            all_results[pid][mid] = pts_by_task

    # Write output CSV
    import csv
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "pattern_id", "model_id", "task_id", "pts",
            "transfer", "utility", "stability", "portability", "psi", "class"
        ])
        writer.writeheader()
        for pid, model_data in all_results.items():
            pts_per_model = {
                mid: statistics.mean(task_data.values())
                for mid, task_data in model_data.items()
                if task_data
            }
            metrics = compute_portability_metrics(pts_per_model)
            vol_class = assign_volatility_class(metrics["transfer"])
            for mid, task_data in model_data.items():
                for tid, pts in task_data.items():
                    writer.writerow({
                        "pattern_id": pid, "model_id": mid, "task_id": tid,
                        "pts": pts, **metrics, "class": vol_class
                    })

    return all_results


if __name__ == "__main__":
    print("PromptTransferX Evaluation Harness")
    print("Implement dataset_loader and provider SDK connections, then call run_evaluation().")
    print("See harness/README.md for setup instructions.")
