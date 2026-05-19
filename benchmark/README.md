# Benchmark

To find which models are actually suited for CtxSift's compression task, we built a benchmark around the thing CtxSift 
does in practice: take raw tool output and return only the information the agent asked for.

This benchmark is not a summarization benchmark. It checks whether a model can preserve exact anchors when 
needed, follow output-shape instructions, stay concise, and return something semantically useful.

The benchmark corpus currently has **280** cases. The dataset is synthetic, but curated. 
It is built from realistic CLI output, stack traces, test failures, CI logs, build output, linter output, 
deployment logs, and extraction-style asks. Some rows were seeded from real-world error material and then normalized 
into a benchmark-friendly contract.

There are broadly two kinds of benchmark rows here.

1. Error and diagnosis rows, where the model has to pick out the important failure signals from noisy output.
2. Extraction and structure rows, where the model must obey a stricter output contract such as exact lines, one value only, JSON, YAML, bullet lists, regex-constrained output, or tables.

The benchmark can be run locally on CPU, locally on GPU, or remotely through LiteLLM-compatible hosted models.
Because of that, **latency numbers are only meaningful relative to the machine and provider used for that run**. 
Quality comparisons are the main signal. Speed is still measured, but used only as a mild scoring modifier.

---

## Benchmark Rig

The local benchmark runs in this repo were run on the following machine:

- CPU: `12th Gen Intel(R) Core(TM) i7-12700F`
- Cores / threads: `12 / 20`
- RAM: `64 GiB`
- GPU: `NVIDIA GeForce RTX 3060 Ti`
- GPU memory: `8 GiB`
- NVIDIA driver: `591.86`
- OS: `Windows 11 Pro 64-bit` (`10.0.26200`)
- Python: `3.12.0`

This matters mostly for CPU and GPU latency comparisons. 
Remote-model quality comparisons are still useful from this machine, but remote latency also depends on provider routing, network path, and server-side load.

---

## What The Models Are Tested On

The dataset covers six benchmark families:

- `summary` : compact useful summaries of noisy output
- `recall` : retrieval-safe compression where exact anchors matter heavily
- `explanation` : short grounded explanation of what went wrong
- `instruction_following` : obey selection rules and output constraints
- `structured` : JSON, YAML, bullet lists, or tables
- `exact_format` : only the exact value, lines, command, id, or match requested

It also spans multiple output modes:

- `plain_text`
- `bullet_list`
- `json`
- `yaml`
- `table`
- `single_line`
- `regex_constrained`
- `exact_lines`

Current corpus shape:

- `280` total cases
- `87` summary
- `86` recall
- `38` explanation
- `26` exact-format
- `23` structured
- `20` instruction-following

The benchmark does not only reward "good sounding" prose. 
A model can be semantically on topic and still score badly if the task asked for exact lines, one value only, 
or a strict JSON shape and the model ignored that contract.

---

## Scoring Rules

The benchmark uses a **case-first** score. Each case is scored separately, and only then rolled up into a scenario score. 
This helps measure a model's reliability. A model that does great on easy summary rows but very poorly 
on exact extraction rows should not hide that weakness behind a smooth scenario average.

Each case gets these component scores:

- **Preserve** : how much of the required exact anchor material survived verbatim
- **Quality** : semantic quality against the expected target
- **Format** : how well the output matched the declared contract such as JSON, YAML, bullet shape, exact lines, one line, or regex
- **Brevity** : whether the output stayed close to the case budget
- **Instruction** : whether the output followed the requested form and task contract

Validation is also part of the benchmark. Outputs are classified as:

- `accepted`
- `soft_accepted`
- `rejected`

Rejected outputs are true benchmark failures. Soft-accepted outputs are still scored, but discounted.

The current scenario score follows this formula:

```text
case_score =
validation_factor * (
  w_anchor * anchor_score +
  w_semantic * semantic_score +
  w_format * format_score +
  w_brevity * brevity_score
)

validation_factor =
  1.00 if accepted
  0.85 if soft_accepted
  0.00 if rejected

quality_core =
0.80 * mean(case_scores) + 0.20 * p10(case_scores)

latency_factor =
clamp(0.85, 1.00, (target_ms / observed_ms)^0.15)

final_score =
100 * quality_core * latency_factor
```

The headline score is mainly a quality score, with a small penalty for being slow and an explicit penalty for weak tail behavior.

### Family-aware weighting

Not every benchmark family cares about the same thing. For example, `exact_format` should care much more about output 
shape than a `summary` row should. So the benchmark uses family-aware weights internally instead of one flat global mix.

### Semantic quality

Semantic quality is not just bag-of-words overlap. The benchmark uses the same embedding stack CtxSift already uses for 
recall, and compares model output against the scoring target semantically where that makes sense.

That especially helps:

- `summary`
- `explanation`
- part of `instruction_following`

For `structured` and `exact_format`, embeddings are only part of the story. Shape still matters more there.

---

## Matrix And Tracks

The benchmark matrix lives in [matrix.json](./matrix.json). It defines named scenarios such as CPU GGUF runs, GPU Transformers runs, and remote hosted runs.

The current tracks are:

- `cpu` : local GGUF models through embedded `llama.cpp`
- `gpu` : local Transformers models on CUDA
- `remote` : hosted models through LiteLLM-compatible endpoints

The current phases are mostly:

- `cpu-screen`
- `gpu-screen`
- `remote-screen`

This lets us do wide screening first, then a narrower second pass where needed.

---

## Layout

- `dataset.jsonl`: benchmark corpus
- `matrix.json`: model and quantization scenarios
- `loader.py`: manifest loader for dataset and matrix
- `runner.py`: async benchmark runner
- `scoring.py`: exactness, format, brevity, and final-score helpers
- `semantic_quality.py`: embedding-based semantic scoring helpers
- `schemas.py`: benchmark result types
- `report.py`: JSON and Markdown result writers
- `viewer.py`: local HTML dashboard renderer
- `results/`: generated benchmark runs and viewer output

---

## Running It Locally

> NOTE: Latency results may vary a lot based on your hardware, provider, and current system load. Treat score as the main comparison signal and latency as a secondary operational signal.

### List scenarios

```bash
uv run python -m benchmark.runner --list-scenarios
```

### Run one local scenario

```bash
uv run python -m benchmark.runner --scenario cpu-smollm2-360m-no-quant
```

### Run one phase

```bash
uv run python -m benchmark.runner --phase cpu-screen
```

### Run a subset of cases

```bash
uv run python -m benchmark.runner --scenario gpu-qwen2.5-1.5b-no-quant --max-cases 50
```

### Run one or more specific case ids

```bash
uv run python -m benchmark.runner --scenario cpu-granite-4.0-350m-no-quant --case-id pytest-01 --case-id kubectl-09
```

### Print model output while it runs

```bash
uv run python -m benchmark.runner --scenario gpu-qwen3.5-0.8b-no-quant --show-output
```

### Give the run a custom name

```bash
uv run python -m benchmark.runner --scenario gpu-qwen2.5-1.5b-no-quant --name smoke
```

When `--name` is omitted, each scenario writes into its own folder under `benchmark/results` as:

```text
<scenario>-<timestamp>/
```

When `--name` is provided, the folder becomes:

```text
<name>-<timestamp>/
```

### Run against remote models

Remote benchmark mode uses the same dataset and the same matrix, but executes scenarios against the configured LiteLLM backend instead of local inference.

```bash
uv run python -m benchmark.runner --remote --env-file .env --scenario remote-gpt-4o-mini
```

In remote mode:

- the runner loads the env file first
- resolves the normal CtxSift remote config
- uses the remote model defined by the selected remote scenario
- runs requests concurrently to speed up benchmark execution

If your `.env` contains `CTXSIFT_LLM_BASE_URL`, `CTXSIFT_LLM_API_KEY`, and related remote settings, the remote runner will use them.

---

## Viewing Results

The viewer reads one result file, one run directory, or the whole `benchmark/results` tree and generates a local HTML dashboard.

### Render and open the whole results tree

```bash
uv run python -m benchmark.viewer --open ./benchmark/results/

### Render a specific run folder

```bash
uv run python -m benchmark.viewer --open ./benchmark/results/remote-gpt-5.4-mini-20260518T065257Z
```

### Render multiple roots together

```bash
uv run python -m benchmark.viewer --open ./benchmark/results/run-a ./benchmark/results/run-b
```

The viewer currently shows:

- CPU, GPU, and remote leaderboards
- model detail tables
- per-case metrics
- failed-case hover detail
- a head-to-head compare panel

---

## Reading The Score Correctly

The final score is not a "general model intelligence" score. It is a **CtxSift suitability score**.

That means:

- strong summary quality alone is not enough
- exactness matters
- structure obedience matters
- weak tail behavior matters
- latency matters a little, but only a little

So a model can be good in a general sense and still score lower here if it keeps adding extra prose when the task asked for only a command, only a JSON object, or only exact lines.

That is intentional as the goal is to return only the task-relevant signal.

---

## Notes

- CPU runs use GGUF models and embedded `llama.cpp`
- GPU runs use Transformers on CUDA
- Remote runs use LiteLLM-compatible providers
- Small models are more likely to echo scaffold text or miss strict output contracts
- Quantization can help larger GPU models fit, but often hurts smaller models on this benchmark
- Attention backend choice such as `sdpa` vs `flash_attention_2` can change both speed and behavior on GPU

If you want to change or regenerate the dataset, the helper and research files in this folder are the place to start, especially [dataset_research_prompt.md](./dataset_research_prompt.md) and [normalize_dataset.py](./normalize_dataset.py).
