# Benchmark

To find which models are actually suited for CtxSift's compression task, we built a benchmark around the thing CtxSift
does in practice: take raw tool output and return only the information the agent asked for.

This benchmark is not a summarization benchmark. It checks whether a model can preserve exact anchors when
needed, follow output-shape instructions, stay concise, and return something semantically useful.

The benchmark corpus currently has **280** cases. The dataset is synthetic, but curated.
It is built from realistic CLI output, stack traces, test failures, CI logs, build output, linter output,
deployment logs, and extraction-style asks. Some rows were seeded from real-world error material and then normalized
into a benchmark-friendly contract.

There are broadly two kinds of benchmark rows:

1. **Error and diagnosis rows** — the model must pick out the important failure signals from noisy output.
2. **Extraction and structure rows** — the model must obey a stricter output contract such as exact lines, one value only, JSON, YAML, bullet lists, regex-constrained output, or tables.

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

| Family | What it tests |
|---|---|
| `summary` | Compact, useful summaries of noisy command output |
| `recall` | Retrieval-safe compression where exact anchor tokens matter heavily |
| `explanation` | Short, grounded explanation of what went wrong |
| `instruction_following` | Obey strict selection rules and output constraints |
| `structured` | JSON, YAML, bullet lists, or markdown tables |
| `exact_format` | Return only the exact value, command, identifier, or lines requested |

It also spans multiple output modes:

| Mode | What the model must produce |
|---|---|
| `plain_text` | A concise prose summary — no headings, bullets, or code fences unless asked |
| `bullet_list` | A list where every line starts with `- ` |
| `json` | A valid JSON object or array matching the expected shape |
| `yaml` | A valid YAML document matching the expected structure |
| `table` | A markdown table with the correct header and column count |
| `single_line` | Exactly one non-empty line of output |
| `regex_constrained` | Output that matches a declared regex pattern exactly |
| `exact_lines` | Verbatim quoted or extracted lines copied from the raw input |

Current corpus shape:

- `280` total cases — `87` summary, `86` recall, `38` explanation, `26` exact-format, `23` structured, `20` instruction-following

The benchmark does not only reward "good sounding" prose.
A model can be semantically on topic and still score badly if the task asked for exact lines, one value only,
or a strict JSON shape and the model ignored that contract.

---

## Scoring Rules

The benchmark uses a **case-first** score. Each case is scored separately, and only then rolled up into a scenario score.
This helps measure a model's reliability. A model that does great on easy summary rows but very poorly
on exact extraction rows should not hide that weakness behind a smooth scenario average.

Each case gets four weighted component scores:

| Component | What it measures |
|---|---|
| **Preserve** | How much of the required exact anchor material survived verbatim |
| **Quality** | Semantic quality against the expected target output (embedding-based) |
| **Format** | How well the output matched the declared output contract |
| **Brevity** | Whether the output stayed close to the per-case token budget |

Additionally, an `instruction_following_score` is computed and stored per case. It combines format adherence with a brevity check and is surfaced in the result files and the viewer, but does not have its own weight slot in the case score formula.

Validation is also part of the benchmark. Outputs are classified as:

- `accepted` — output passes all hard validation checks
- `soft_accepted` — output passes hard checks but has minor quality flags (e.g. missing some anchors, slight format mismatch)
- `rejected` — output fails a hard validation check and scores zero

**What causes a rejection:** the validator inspects the normalized output and rejects it if it detects any of the following:

- `empty_output` — the model returned nothing after cleanup
- `control_token_leakage` — model-internal tokens like `<|im_end|>` or `<|im_start|>` leaked into the output
- `role_token_leakage` — chat-role markers like `<|system|>` or `<|user|>` leaked into the output
- `schema_echo` — the model echoed back the prompt's structured label section instead of producing output
- `prompt_scaffold_echo` — the model echoed back the prompt's instruction or output-form section
- `exact_lines_contract_breakage` — for `exact_lines` mode: the output contained obvious summarization instead of verbatim lines
- `exact_format_contract_breakage` — for `exact_format` mode: the output contained prose, bullets, or headings when only a bare value was requested
- `structured_contract_breakage` — for `structured` mode (JSON/YAML/table/bullet-list): the output contained none of the expected structure

Soft-accepted outputs are still scored, but discounted.

The current scenario score follows this formula:

```text
case_score =
  validation_factor * (
    w_anchor   * anchor_score   +
    w_semantic * semantic_score +
    w_format   * format_score   +
    w_brevity  * brevity_score
  )

validation_factor =
  1.00  if accepted
  0.85  if soft_accepted
  0.00  if rejected

quality_core =
  0.80 * mean(case_scores) + 0.20 * p10(case_scores)

latency_factor =
  clamp(0.85, 1.00, (2000ms / observed_ms)^0.15)

final_score =
  100 * quality_core * latency_factor
```

The latency target is **2000 ms**. Finishing faster than 2000 ms is fully neutral — the factor is 1.0, no bonus and no penalty. Only being *slower* than 2000 ms incurs a penalty, and that penalty is capped at 0.85, so latency can reduce the score by at most 15%.

The headline score is mainly a quality score, with a small penalty for being slow and an explicit penalty for weak tail behavior (the p10 term in `quality_core`).

### Family-aware weighting

Not every benchmark family cares about the same thing. `exact_format` rows care much more about output
shape than a `summary` row does. So the benchmark uses family-aware weights internally instead of one flat global mix.

| Family | Anchor | Semantic | Format | Brevity |
|---|:-:|:-:|:-:|:-:|
| `recall` | 0.45 | 0.25 | 0.20 | 0.10 |
| `summary` | 0.25 | 0.40 | 0.20 | 0.15 |
| `explanation` | 0.20 | 0.50 | 0.20 | 0.10 |
| `structured` | 0.20 | 0.30 | 0.40 | 0.10 |
| `instruction_following` | 0.20 | 0.30 | 0.40 | 0.10 |
| `exact_format` | 0.15 | 0.10 | 0.70 | 0.05 |

### Format checks

Some cases also carry an explicit `format_check` in the dataset. When set, this overrides the mode-inferred format scoring with a stricter check:

| format_check | What it does |
|---|---|
| `none` | Falls back to the mode-inferred format check (default) |
| `exact_match` | Output must match the expected output exactly, line by line |
| `json_shape` | Output must be valid JSON with a structure matching the expected shape |
| `yaml_shape` | Output must be valid YAML with a structure matching the expected shape |
| `table_shape` | Output must be a markdown table with the correct column header and count |
| `bullet_shape` | Every non-empty output line must start with `- ` |
| `regex` | Output must fully match the regex pattern declared in the case's `pass_rule` |

### Semantic quality

Semantic quality is not just bag-of-words overlap. The benchmark uses the same embedding stack CtxSift already uses for
recall, and compares model output against the scoring target semantically.

That especially helps:

- `summary`
- `explanation`
- part of `instruction_following`

For `structured` and `exact_format`, embeddings are only part of the story. Shape still matters more there.

---

## Matrix And Tracks

The benchmark matrix lives in [matrix.json](./matrix.json). It defines named scenarios such as CPU GGUF runs, GPU Transformers runs, and remote hosted runs.

The current tracks are:

- `cpu` — local GGUF models through embedded `llama.cpp`
- `gpu` — local Transformers models on CUDA
- `remote` — hosted models through LiteLLM-compatible endpoints

The current phases are:

- `cpu-screen` — wide CPU screening pass
- `gpu-screen` — wide GPU screening pass
- `remote-screen` — wide remote screening pass

This lets you run a wide screening pass first, then a narrower second pass where needed using `--scenario` filtering.

---

## Layout

| File | Purpose |
|---|---|
| `dataset.jsonl` | Benchmark corpus — 280 cases |
| `matrix.json` | Model and quantization scenarios |
| `loader.py` | Manifest loader for dataset and matrix |
| `runner.py` | Async benchmark runner |
| `scoring.py` | Exactness, format, brevity, and final-score helpers |
| `semantic_quality.py` | Embedding-based semantic scoring |
| `schemas.py` | Benchmark result and case types |
| `report.py` | JSON and Markdown result writers |
| `metrics.py` | Process and GPU memory measurement helpers |
| `stats.py` | Percentile helpers |
| `viewer.py` | Local HTML dashboard renderer |
| `results/` | Generated benchmark runs |

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

When `--name` is omitted, each scenario writes into its own folder under `benchmark/results` named:

```text
<scenario>-<timestamp>/
```

When `--name` is provided, all scenarios in that run share one folder:

```text
<name>-<timestamp>/
```

### Run against remote models

Remote benchmark mode uses the same dataset and the same matrix, but executes scenarios against the configured LiteLLM backend instead of local inference. Remote cases run concurrently (up to 16 at a time) to keep wall-clock time reasonable.

```bash
uv run python -m benchmark.runner --remote --env-file .env --scenario remote-gpt-4o-mini
```

In remote mode:

- the runner loads the env file first
- resolves the normal CtxSift remote config
- uses the remote model defined by the selected remote scenario
- runs requests concurrently to speed up benchmark execution

If your `.env` contains `CTXSIFT_LLM_BASE_URL`, `CTXSIFT_LLM_API_KEY`, and related remote settings, the remote runner will use them automatically.

---

## Viewing Results

The viewer reads one result file, one run directory, or the whole `benchmark/results` tree and generates a local HTML dashboard.

### Render and open the whole results tree

```bash
uv run python -m benchmark.viewer --open ./benchmark/results/
```

If you already generated results in this checkout, the latest snapshot also lives at `benchmark/results/viewer.html`. That file is just the generated static dashboard.

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
- weak tail behavior matters (the p10 term keeps a few bad cases from being hidden by the average)
- latency matters a little, but only a little — the penalty is capped at 15%

A model can be good in a general sense and still score lower here if it keeps adding extra prose when the task asked for only a command, only a JSON object, or only exact lines. That is intentional — the goal is to return only the task-relevant signal.

---

## Notes

- CPU runs use GGUF models and embedded `llama.cpp`
- GPU runs use Transformers on CUDA
- Remote runs use LiteLLM-compatible providers
- Small models are more likely to echo scaffold text or leak control tokens — this causes hard rejections
- Quantization can help larger GPU models fit in VRAM, but often hurts smaller models on this benchmark
- Attention backend choice (`sdpa` vs `flash_attention_2`) can change both speed and behavior on GPU
- If you want to change or regenerate the dataset, start with `normalize_dataset.py` in this folder
