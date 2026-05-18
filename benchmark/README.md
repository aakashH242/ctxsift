# Benchmark

This folder contains the local-model benchmark harness for `ctxsift` compression.

## Layout

- `dataset.jsonl`: benchmark corpus
- `matrix.json`: model and quantization scenarios
- `runner.py`: async benchmark runner
- `report.py`: JSON and Markdown result writers
- `dataset_research_prompt.md`: prompt used to generate corpus

## Run

```powershell
uv run python -m benchmark.runner --phase cpu-screen
uv run python -m benchmark.runner --phase gpu-screen
uv run python -m benchmark.runner --scenario gpu-qwen2.5-1.5b-bnb8
uv run python -m benchmark.runner --phase cpu-screen --name cpu-smoke
```

Results are written to:

```text
benchmark/results/<scenario>-<timestamp>/<scenario>.json
benchmark/results/<scenario>-<timestamp>/<scenario>.md
```

With `--name`, results are written under:

```text
benchmark/results/<name>-<timestamp>/<scenario>.json
benchmark/results/<name>-<timestamp>/<scenario>.md
```

Render a self-contained HTML viewer from one result file or a results directory:

```powershell
uv run python -m benchmark.viewer benchmark/results/gpu-qwen2.5-1.5b-no-quant-20260515T234740Z --open
uv run python -m benchmark.viewer benchmark/results --open
uv run python -m benchmark.viewer benchmark/results/gpu-qwen2.5-1.5b-no-quant-20260515T234740Z benchmark/results/cpu-smollm2-360m-no-quant-20260516T012829Z --open
uv run python -m benchmark.viewer benchmark/results/gpu-qwen2.5-1.5b-no-quant-20260515T234740Z/gpu-qwen2.5-1.5b-no-quant.json
```

## Notes

- One backend instance is created per scenario and reused across all dataset cases.
- Warmup is separated from measured case runs so the model is loaded only once per scenario.
- Default concurrency is `1` for memory safety with local transformer inference.
