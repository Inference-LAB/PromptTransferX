# Model Versions and API Query Log

All primary evaluations were conducted March–July 2026.
Partial replication conducted August 2026.

## Primary models (M1–M6)

| Model ID | Model name | API/inference string | Query window | Endpoint | Decoding |
|---|---|---|---|---|---|
| M1 | GPT-4o | `gpt-4o-2024-08-06` | Mar–Jul 2026 | OpenAI Chat Completions API | T=0.0/0.7, max_tokens=1024 |
| M2 | Claude 3 Opus | `claude-3-opus-20240229` | Mar–Jul 2026 | Anthropic Messages API | T=0.0/0.7, max_tokens=1024 |
| M3 | Gemini 1.5 Pro | `gemini-1.5-pro-latest` | Mar–Jul 2026 | Google AI Studio API | T=0.0/0.7, max_tokens=1024 |
| M4 | LLaMA-3-70B-Instruct | `Meta-Llama-3-70B-Instruct` | Mar–Jul 2026 | vLLM local, bf16 | T=0.0/0.7, max_tokens=1024 |
| M5 | Mistral-7B-Instruct-v0.3 | `Mistral-7B-Instruct-v0.3` | Mar–Jul 2026 | vLLM local, bf16 | T=0.0/0.7, max_tokens=1024 |
| M6 | MedLLaMA-2-7B | `medllama2_7b` (HuggingFace Hub) | Mar–Jul 2026 | vLLM local, bf16 | T=0.0/0.7, max_tokens=1024 |

## Replication models (M7–M8, partial)

| Model ID | Model name | API/inference string | Query window | Scope |
|---|---|---|---|---|
| M7 | Claude Opus 4.6 | `claude-opus-4-6` | Aug 2026 | All 24 patterns × Math + IF tasks |
| M8 | Qwen3-14B-Instruct | `Qwen3-14B-Instruct` (HuggingFace Hub) | Aug 2026 | All 24 patterns × Math + IF tasks |

## Evaluation judges

| Role | Model | API string | Applied to |
|---|---|---|---|
| Primary judge | GPT-4o | `gpt-4o-2024-08-06` | All items |
| Secondary judge | Gemini 1.5 Pro | `gemini-1.5-pro-latest` | 25% holdout (N=1,260) |
| Tertiary judge | Prometheus-2 | `prometheus-2-8x7b-rc` | 25% holdout (N=1,260) |

## Global settings

- System prompt: `null` (empty) for primary evaluation
- Ablation conditions: `null` / `"You are a helpful assistant."` / task-specific
- Seed: Provider-specific where supported; not available for all proprietary APIs
- Number of independent runs per cell: 5
- Number of paraphrastic variants per pattern: 4 (V-A, V-B, V-C, V-D)
- Bootstrap CI resamples: 10,000

## Provider notes

API-accessed proprietary models (M1, M2, M3) may change without notice.
Results are reproducible only with the exact version strings listed above.
vLLM local deployments are reproducible given the same model checkpoint
and vLLM version (≥0.4.0 for all tested checkpoints).
