# gpu-qwen3.5-2b

## Scenario

- track: `gpu`
- phase: `gpu-screen`
- model: `Qwen/Qwen3.5-2B`
- quantization: `none`
- device: `cuda`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `2011833.13`
- cpu_rss_bytes: `7994466304`
- gpu_peak_bytes: `5023137280`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- recovered_final_score: `61.07`
- raw_final_score: `30.23`
- recovery_lift: `+30.84`
- case_count: `280`
- success_count: `268`
- accepted_count: `237`
- soft_accepted_count: `31`
- rejected_count: `12`
- exact_pass_count: `256`
- avg_inference_ms: `16921.64`
- p95_inference_ms: `44660.05`
- avg_exact_preservation_ratio: `0.965`
- avg_summary_quality_ratio: `0.844`
- avg_format_adherence_score: `0.869`
- avg_instruction_following_score: `0.839`
- avg_brevity_ratio: `0.901`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.827`
- p10_case_score: `0.286`
- quality_core: `0.718`
- latency_factor: `0.850`
- final_score: `61.07`
- peak_cpu_rss_bytes: `8036409344`
- peak_gpu_bytes: `5135802880`

### Raw View

- accepted_count: `0`
- soft_accepted_count: `194`
- rejected_count: `86`
- exact_pass_count: `256`
- avg_exact_preservation_ratio: `0.965`
- avg_summary_quality_ratio: `0.807`
- avg_format_adherence_score: `0.492`
- avg_instruction_following_score: `0.344`
- avg_brevity_ratio: `0.883`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.445`
- p10_case_score: `0.000`
- quality_core: `0.356`
- final_score: `30.23`

## Cases

| case_id | family | domain | ms | recovered_score | raw_score | lift | preserve | quality | format | instruction | recovered_thought_density | raw_thought_density | recovered_validation | raw_validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `10341.83` | `0.991` | `0.661` | `+0.330` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-02` | `summary` | `python` | `10137.52` | `0.985` | `0.657` | `+0.328` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-03` | `recall` | `python` | `7728.01` | `0.989` | `0.660` | `+0.328` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-04` | `recall` | `python` | `10491.65` | `0.989` | `0.661` | `+0.328` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-05` | `recall` | `python` | `117096.63` | `0.609` | `0.000` | `+0.609` | `1.000` | `0.955` | `0.500` | `0.423` | `0.000` | `0.000` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `pytest-01` | `recall` | `pytest` | `9853.44` | `0.992` | `0.662` | `+0.330` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `100380.52` | `0.864` | `0.000` | `+0.864` | `1.000` | `0.939` | `1.000` | `0.846` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `12483.91` | `0.991` | `0.662` | `+0.329` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `10488.77` | `0.994` | `0.665` | `+0.329` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `10201.52` | `0.987` | `0.658` | `+0.329` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `11478.90` | `0.988` | `0.658` | `+0.330` | `1.000` | `0.952` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `9085.60` | `0.979` | `0.650` | `+0.329` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `27409.19` | `0.991` | `0.662` | `+0.330` | `1.000` | `0.965` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ruff-01` | `recall` | `ruff` | `9262.95` | `0.990` | `0.660` | `+0.330` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ruff-02` | `summary` | `ruff` | `7664.79` | `0.990` | `0.661` | `+0.329` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `21179.79` | `0.971` | `0.646` | `+0.325` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `7544.85` | `0.990` | `0.659` | `+0.331` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `16745.40` | `0.982` | `0.653` | `+0.329` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `9053.57` | `0.985` | `0.656` | `+0.329` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `black-01` | `summary` | `black` | `9305.78` | `0.989` | `0.660` | `+0.329` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `black-02` | `summary` | `black` | `8957.96` | `0.978` | `0.653` | `+0.326` | `1.000` | `0.946` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `black-03` | `recall` | `black` | `5799.28` | `0.993` | `0.663` | `+0.330` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `15653.25` | `0.978` | `0.651` | `+0.327` | `1.000` | `0.912` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `11300.92` | `0.979` | `0.651` | `+0.329` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `9031.62` | `0.981` | `0.654` | `+0.327` | `1.000` | `0.951` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `8916.38` | `0.988` | `0.657` | `+0.331` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `13209.23` | `0.987` | `0.653` | `+0.334` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `10710.89` | `0.986` | `0.657` | `+0.329` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `10101.83` | `0.988` | `0.657` | `+0.330` | `1.000` | `0.969` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `36083.27` | `0.907` | `0.608` | `+0.299` | `1.000` | `0.929` | `1.000` | `0.867` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `11116.73` | `0.972` | `0.650` | `+0.322` | `1.000` | `0.930` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-01` | `recall` | `eslint` | `16263.36` | `0.989` | `0.659` | `+0.330` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `7930.15` | `0.980` | `0.653` | `+0.327` | `1.000` | `0.951` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `16586.78` | `0.985` | `0.657` | `+0.328` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `9635.03` | `0.986` | `0.657` | `+0.329` | `1.000` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `10946.63` | `0.975` | `0.650` | `+0.325` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `11518.30` | `0.977` | `0.650` | `+0.328` | `1.000` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `3871.32` | `0.991` | `0.658` | `+0.334` | `1.000` | `0.978` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `6870.20` | `0.987` | `0.658` | `+0.329` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `24122.08` | `0.959` | `0.635` | `+0.324` | `1.000` | `0.916` | `1.000` | `0.990` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `31432.27` | `0.844` | `0.560` | `+0.284` | `1.000` | `0.941` | `1.000` | `0.816` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `28914.17` | `0.991` | `0.659` | `+0.332` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `12875.79` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.968` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `12836.63` | `0.988` | `0.659` | `+0.328` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `6671.10` | `0.984` | `0.651` | `+0.333` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `6918.63` | `0.986` | `0.657` | `+0.330` | `1.000` | `0.946` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `6423.46` | `0.986` | `0.657` | `+0.329` | `1.000` | `0.943` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `34200.92` | `0.980` | `0.652` | `+0.327` | `1.000` | `0.949` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `9431.15` | `0.990` | `0.661` | `+0.329` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `7964.85` | `0.975` | `0.654` | `+0.321` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `git-01` | `recall` | `git` | `5895.65` | `0.972` | `0.645` | `+0.327` | `1.000` | `0.887` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `git-02` | `recall` | `git` | `5274.40` | `0.984` | `0.655` | `+0.329` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `git-03` | `recall` | `git` | `8563.92` | `0.989` | `0.658` | `+0.331` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `14285.04` | `0.989` | `0.661` | `+0.328` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `curl-02` | `recall` | `curl` | `8600.58` | `0.992` | `0.662` | `+0.330` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ssh-01` | `summary` | `ssh` | `13624.92` | `0.986` | `0.657` | `+0.329` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `7516.45` | `0.980` | `0.647` | `+0.332` | `1.000` | `0.949` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `5971.88` | `0.983` | `0.654` | `+0.329` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `5342.51` | `0.962` | `0.638` | `+0.324` | `1.000` | `0.904` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `7683.60` | `0.977` | `0.648` | `+0.329` | `1.000` | `0.942` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `15255.77` | `0.990` | `0.660` | `+0.330` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `29621.51` | `0.962` | `0.641` | `+0.321` | `1.000` | `0.906` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `82024.60` | `0.882` | `0.588` | `+0.294` | `1.000` | `0.927` | `1.000` | `0.877` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `javac-01` | `recall` | `javac` | `8273.16` | `0.986` | `0.658` | `+0.328` | `1.000` | `0.945` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `maven-01` | `recall` | `maven` | `116175.34` | `0.580` | `0.578` | `+0.001` | `1.000` | `0.905` | `0.500` | `0.392` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `maven-02` | `summary` | `maven` | `8513.73` | `0.990` | `0.659` | `+0.331` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `8646.34` | `0.987` | `0.658` | `+0.329` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `40424.00` | `0.863` | `0.579` | `+0.284` | `1.000` | `0.916` | `1.000` | `0.858` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `cargo-01` | `recall` | `cargo` | `5576.54` | `0.985` | `0.657` | `+0.327` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `cargo-02` | `recall` | `cargo` | `18698.11` | `0.986` | `0.656` | `+0.330` | `1.000` | `0.945` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `177220.53` | `0.596` | `0.000` | `+0.596` | `1.000` | `0.924` | `0.500` | `0.412` | `0.000` | `0.000` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `npm-04` | `summary` | `npm` | `58131.54` | `0.823` | `0.553` | `+0.270` | `1.000` | `0.934` | `1.000` | `0.790` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `7517.13` | `0.977` | `0.651` | `+0.326` | `1.000` | `0.943` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `8650.93` | `0.989` | `0.660` | `+0.330` | `1.000` | `0.973` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-runtime-01` | `recall` | `python-runtime` | `7417.78` | `0.992` | `0.662` | `+0.329` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `13834.39` | `0.986` | `0.657` | `+0.328` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `5624.05` | `0.975` | `0.646` | `+0.329` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `13465.56` | `0.631` | `0.480` | `+0.151` | `0.089` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund, Dockerfile:8, failed to solve | - |
| `docker-compose-04` | `summary` | `docker-compose` | `55199.98` | `0.842` | `0.564` | `+0.279` | `1.000` | `0.906` | `1.000` | `0.833` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `15901.71` | `0.970` | `0.646` | `+0.324` | `1.000` | `0.925` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `17257.84` | `0.827` | `0.649` | `+0.179` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `12410.20` | `0.990` | `0.658` | `+0.332` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `14819.47` | `0.993` | `0.660` | `+0.333` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `27337.93` | `0.962` | `0.641` | `+0.322` | `1.000` | `0.906` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `14502.99` | `0.785` | `0.615` | `+0.170` | `0.867` | `0.893` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | aws_security_group_rule.web_https | - |
| `nginx-01` | `summary` | `nginx` | `7600.10` | `0.984` | `0.652` | `+0.333` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `29010.58` | `0.972` | `0.648` | `+0.324` | `1.000` | `0.929` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `11371.67` | `0.994` | `0.662` | `+0.332` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `25227.76` | `0.969` | `0.645` | `+0.323` | `1.000` | `0.922` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `20943.27` | `0.989` | `0.660` | `+0.329` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `11440.47` | `0.988` | `0.659` | `+0.329` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `27621.94` | `0.935` | `0.623` | `+0.312` | `1.000` | `0.948` | `1.000` | `0.940` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `8216.78` | `0.988` | `0.658` | `+0.330` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `37910.89` | `0.899` | `0.602` | `+0.297` | `1.000` | `0.894` | `1.000` | `0.868` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `133127.43` | `0.803` | `0.000` | `+0.803` | `1.000` | `0.906` | `1.000` | `0.777` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `4899.05` | `0.967` | `0.642` | `+0.325` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `make-01` | `summary` | `make` | `27429.87` | `0.974` | `0.650` | `+0.324` | `1.000` | `0.936` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `13767.00` | `0.981` | `0.655` | `+0.326` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `7163.07` | `0.992` | `0.658` | `+0.334` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `9016.58` | `0.981` | `0.653` | `+0.328` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `13659.05` | `0.993` | `0.664` | `+0.328` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `159338.03` | `0.983` | `0.652` | `+0.331` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-log-01` | `recall` | `ci-log` | `14053.99` | `0.985` | `0.659` | `+0.326` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `18155.72` | `0.994` | `0.663` | `+0.331` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `28825.33` | `0.981` | `0.655` | `+0.326` | `1.000` | `0.952` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `build-log-01` | `summary` | `build-log` | `7437.02` | `0.971` | `0.645` | `+0.325` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `11208.88` | `0.688` | `0.685` | `+0.002` | `0.333` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Dockerfile:18, "/apps/web": not found | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `68908.04` | `0.298` | `0.000` | `+0.298` | `0.750` | `0.628` | `0.333` | `0.260` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | 27:19, @typescript-eslint/no-misused-promises | - |
| `git-review-01` | `instruction_following` | `git-review` | `14611.31` | `0.609` | `0.000` | `+0.609` | `1.000` | `0.722` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `14322.71` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.334` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='- search endpoint failed after 2 attempts - exit status 22 - https://staging.example.com/api/search?q=smoke - curl: (22)' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='search endpoint failed after 2 attempts exit status 22 https://staging.example.com/api/search?q=smoke curl: (22)' |
| `structured-output-01` | `structured` | `structured-output` | `43694.65` | `0.244` | `0.000` | `+0.244` | `0.500` | `0.185` | `0.375` | `0.346` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | /work/app/api/routes.py, 21, reportUndefinedVariable | - |
| `structured-output-02` | `structured` | `structured-output` | `38428.61` | `0.174` | `0.000` | `+0.174` | `0.905` | `0.832` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | port 5432 is already allocated | - |
| `structured-output-03` | `structured` | `structured-output` | `114326.19` | `0.826` | `0.000` | `+0.826` | `0.929` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | "refresh token expired" | - |
| `structured-output-04` | `structured` | `structured-output` | `20429.45` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `18792.20` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `0.617` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_lines_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- tests/api/test_users.py::test_create_user_requires_email - tests/api/test_users.py::test_delete_user_requires_admin - tests/jobs/test_reconcile.py::TestRec...' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- tests/api/test_users.py::test_create_user_requires_email - tests/api/test_users.py::test_delete_user_requires_admin - tests/jobs/test_reconcile.py::TestRec...' |
| `exact-format-02` | `exact_format` | `exact-format` | `5662.26` | `0.558` | `0.000` | `+0.558` | `1.000` | `0.337` | `0.595` | `0.524` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `15502.37` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `15213.55` | `0.783` | `0.610` | `+0.173` | `0.778` | `0.943` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | has no attribute 'dumps' | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `11905.55` | `0.954` | `0.637` | `+0.316` | `1.000` | `0.884` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `23120.91` | `0.712` | `0.000` | `+0.712` | `1.000` | `0.673` | `0.667` | `0.658` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `11148.83` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `8960.05` | `0.984` | `0.655` | `+0.330` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `36693.10` | `0.982` | `0.651` | `+0.331` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `9874.63` | `0.978` | `0.652` | `+0.326` | `1.000` | `0.911` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `15658.72` | `0.985` | `0.657` | `+0.328` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `10142.43` | `0.983` | `0.657` | `+0.326` | `1.000` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `38180.48` | `0.971` | `0.646` | `+0.325` | `1.000` | `0.935` | `1.000` | `0.978` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `9531.33` | `0.987` | `0.657` | `+0.331` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `28611.85` | `0.987` | `0.657` | `+0.330` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `45179.87` | `0.977` | `0.650` | `+0.327` | `1.000` | `0.947` | `1.000` | `0.982` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `9643.76` | `0.988` | `0.660` | `+0.328` | `1.000` | `0.952` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `7303.22` | `0.988` | `0.662` | `+0.326` | `1.000` | `0.951` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `11064.10` | `0.982` | `0.658` | `+0.324` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `14631.71` | `0.987` | `0.657` | `+0.330` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `13999.17` | `0.992` | `0.661` | `+0.330` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `8275.22` | `0.987` | `0.657` | `+0.330` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `12926.04` | `0.990` | `0.661` | `+0.329` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `40908.03` | `0.928` | `0.621` | `+0.307` | `1.000` | `0.927` | `1.000` | `0.906` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `9920.85` | `0.973` | `0.650` | `+0.323` | `1.000` | `0.894` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `8047.33` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `8385.75` | `0.982` | `0.655` | `+0.327` | `1.000` | `0.929` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `13226.98` | `0.959` | `0.639` | `+0.321` | `1.000` | `0.898` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `33838.09` | `0.965` | `0.643` | `+0.322` | `1.000` | `0.913` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `35312.73` | `0.968` | `0.645` | `+0.323` | `1.000` | `0.919` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `8924.42` | `0.739` | `0.571` | `+0.167` | `0.625` | `0.907` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | template, executing, Values.image.repository | - |
| `ruff-04` | `summary` | `ruff` | `14778.00` | `0.954` | `0.633` | `+0.321` | `1.000` | `0.886` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `32085.34` | `0.961` | `0.641` | `+0.321` | `1.000` | `0.904` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `29326.31` | `0.939` | `0.625` | `+0.313` | `1.000` | `0.941` | `1.000` | `0.949` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `11040.54` | `0.953` | `0.637` | `+0.316` | `1.000` | `0.882` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `make-02` | `summary` | `make` | `10867.66` | `0.959` | `0.637` | `+0.322` | `1.000` | `0.897` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `18581.96` | `0.968` | `0.645` | `+0.323` | `1.000` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `19108.91` | `0.960` | `0.641` | `+0.319` | `1.000` | `0.899` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `10304.46` | `0.789` | `0.615` | `+0.174` | `0.833` | `0.925` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `21689.33` | `0.966` | `0.643` | `+0.323` | `1.000` | `0.915` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `13098.09` | `0.966` | `0.644` | `+0.323` | `1.000` | `0.916` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `7085.35` | `0.600` | `0.452` | `+0.147` | `0.000` | `0.889` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | tests/test_slugify.py, FAILED, tests/test_slugify.py::test_slug_is_ascii, Falsifying, example | - |
| `eslint-05` | `instruction_following` | `eslint` | `35100.25` | `0.000` | `0.000` | `+0.000` | `0.741` | `0.226` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | 22:7, prefer-const | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- src/App.tsx 10:3 warning Unexpected console statement no-console - src/api.ts 4:12 error Unexpected any. Specify a different type @typescript-eslint/no-exp...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- src/App.tsx 10:3 warning Unexpected console statement no-console - src/api.ts 4:12 error Unexpected any. Specify a different type @typescript-eslint/no-exp...' |
| `git-diff-01` | `instruction_following` | `git-diff` | `7787.15` | `0.973` | `0.000` | `+0.973` | `1.000` | `0.910` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `8779.82` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `0.617` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_lines_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- tests/test_api.py::test_create_user - tests/test_auth.py::test_refresh_token_expiry' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- tests/test_api.py::test_create_user - tests/test_auth.py::test_refresh_token_expiry' |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `9327.32` | `0.888` | `0.000` | `+0.888` | `1.000` | `0.675` | `1.000` | `0.957` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `5401.61` | `0.976` | `0.000` | `+0.976` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `7469.69` | `0.874` | `0.000` | `+0.874` | `1.000` | `0.750` | `0.800` | `0.800` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `16112.98` | `0.297` | `0.000` | `+0.297` | `1.000` | `0.396` | `0.323` | `0.249` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `6373.08` | `0.606` | `0.000` | `+0.606` | `1.000` | `0.709` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `18908.83` | `0.561` | `0.000` | `+0.561` | `1.000` | `0.850` | `0.400` | `0.400` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `15389.97` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.386` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- [firefox] › checkout.spec.ts:44:1 › pays with saved card Error: expect(locator).toBeVisible() failed Locator: text=Payment complete' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- [firefox] › checkout.spec.ts:44:1 › pays with saved card Error: expect(locator).toBeVisible() failed Locator: text=Payment complete' |
| `prettier-01` | `instruction_following` | `prettier` | `33539.92` | `0.279` | `0.000` | `+0.279` | `1.000` | `0.000` | `0.150` | `0.107` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `11816.38` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.000` | `0.475` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_lines_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- worker-5b8c - CrashLoopBackOff - migrator-9z1q - Error' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- worker-5b8c - CrashLoopBackOff - migrator-9z1q - Error' |
| `cargo-04` | `instruction_following` | `cargo` | `160706.53` | `0.660` | `0.000` | `+0.660` | `0.333` | `0.698` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | src/auth.rs:88, Option::unwrap(), left: 1750, right: 1749 | - |
| `shell-01` | `instruction_following` | `shell` | `11706.39` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.546` | `0.336` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13)' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) exit code 23' |
| `pyright-01` | `structured` | `pyright` | `13028.61` | `0.361` | `0.000` | `+0.361` | `1.000` | `0.185` | `0.338` | `0.338` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `61645.63` | `0.118` | `0.000` | `+0.118` | `1.000` | `0.188` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `junit-01` | `structured` | `junit` | `14335.43` | `0.217` | `0.000` | `+0.217` | `1.000` | `0.812` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `28847.56` | `0.115` | `0.000` | `+0.115` | `1.000` | `0.191` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `26856.81` | `0.287` | `0.000` | `+0.287` | `0.667` | `0.184` | `0.500` | `0.387` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | line, column, rule | - |
| `docker-build-04` | `structured` | `docker-build` | `11467.87` | `0.626` | `0.000` | `+0.626` | `1.000` | `0.704` | `0.548` | `0.527` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `31823.92` | `0.000` | `0.000` | `+0.000` | `0.424` | `0.753` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | failed_tests, name, location, message | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='--- FAIL: TestParseAmount (0.00s) amount_test.go:22: got 10.0 want 10.00 --- FAIL: TestFormatCurrency (0.00s) currency_test.go:51: got USD 10 want $10.00 FAIL' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='--- FAIL: TestParseAmount (0.00s) amount_test.go:22: got 10.0 want 10.00 --- FAIL: TestFormatCurrency (0.00s) currency_test.go:51: got USD 10 want $10.00 FAIL' |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `13124.03` | `0.840` | `0.000` | `+0.840` | `1.000` | `0.634` | `1.000` | `0.850` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `npm-07` | `structured` | `npm` | `37157.48` | `0.355` | `0.000` | `+0.355` | `0.667` | `0.349` | `0.562` | `0.439` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | package, required | - |
| `mypy-06` | `structured` | `mypy` | `30312.34` | `0.137` | `0.000` | `+0.137` | `0.733` | `0.595` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | Code, Message | - |
| `gradle-03` | `structured` | `gradle` | `16361.17` | `0.146` | `0.000` | `+0.146` | `0.697` | `0.183` | `0.100` | `0.100` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | :api:compileJava | - |
| `playwright-02` | `structured` | `playwright` | `40807.40` | `0.168` | `0.000` | `+0.168` | `0.333` | `0.183` | `0.250` | `0.235` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | project, chromium, file, line | - |
| `postgres-04` | `structured` | `postgres` | `35276.79` | `0.140` | `0.000` | `+0.140` | `0.636` | `0.752` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | file, line, message | - |
| `vite-01` | `structured` | `vite` | `14717.42` | `0.051` | `0.000` | `+0.051` | `0.400` | `0.181` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | /repo/apps/admin/src/client.ts, @acme/api, /repo/apps/public/src/Home.tsx | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `7061.21` | `0.414` | `0.000` | `+0.414` | `1.000` | `0.000` | `0.333` | `0.250` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `git-04` | `exact_format` | `git` | `7117.69` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `49788.82` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.331` | `0.311` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='pushed ghcr.io/acme/api:2026.05.18 digest: sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 verified ghcr.io/acme/api@sha256:aaaaaaaa1...' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='pushed ghcr.io/acme/api:2026.05.18 digest: sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 verified ghcr.io/acme/api@sha256:aaaaaaaa1...' |
| `npm-08` | `exact_format` | `npm` | `1499.71` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `9901.22` | `0.176` | `0.000` | `+0.176` | `1.000` | `0.319` | `0.165` | `0.130` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `17309.80` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.300` | `0.156` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='migrator-v2-9xk 0/1 Error 0 33m worker-123 1/1 Running 0 1h namespace: prod' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='migrator-v2-9xk 0/1 Error 0 33m worker-123 1/1 Running 0 1h namespace: prod' |
| `cargo-05` | `exact_format` | `cargo` | `8246.91` | `0.394` | `0.000` | `+0.394` | `1.000` | `0.000` | `0.308` | `0.227` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `1104.21` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `3455.04` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `18935.79` | `0.646` | `0.646` | `-0.001` | `1.000` | `0.920` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `14971.16` | `0.956` | `0.638` | `+0.318` | `1.000` | `0.890` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `2882.36` | `0.720` | `0.000` | `+0.720` | `1.000` | `0.682` | `0.667` | `0.667` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `15048.32` | `0.956` | `0.636` | `+0.320` | `1.000` | `0.914` | `1.000` | `0.987` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `4272.68` | `0.965` | `0.639` | `+0.326` | `1.000` | `0.914` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `22632.01` | `0.617` | `0.618` | `-0.001` | `1.000` | `0.825` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `28306.97` | `0.710` | `0.543` | `+0.167` | `0.583` | `0.848` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `4779.79` | `0.989` | `0.662` | `+0.328` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `4524.93` | `0.985` | `0.660` | `+0.325` | `1.000` | `0.940` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `21336.86` | `0.663` | `0.662` | `+0.001` | `1.000` | `0.964` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `package-management-01` | `recall` | `package-management` | `11631.20` | `0.976` | `0.650` | `+0.326` | `1.000` | `0.904` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `11603.52` | `0.714` | `0.547` | `+0.167` | `0.667` | `0.962` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `8685.62` | `0.929` | `0.620` | `+0.308` | `1.000` | `0.943` | `1.000` | `0.900` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `12736.07` | `0.952` | `0.634` | `+0.318` | `1.000` | `0.923` | `1.000` | `0.950` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `4309.76` | `0.962` | `0.641` | `+0.321` | `1.000` | `0.847` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `5429.49` | `0.980` | `0.652` | `+0.329` | `1.000` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `13173.34` | `0.937` | `0.622` | `+0.314` | `1.000` | `0.892` | `1.000` | `0.937` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `7774.73` | `0.981` | `0.653` | `+0.328` | `1.000` | `0.924` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `5321.97` | `0.992` | `0.665` | `+0.327` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `2596.00` | `0.974` | `0.649` | `+0.325` | `1.000` | `0.895` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `build-01` | `recall` | `build` | `11975.47` | `0.922` | `0.614` | `+0.308` | `1.000` | `0.895` | `1.000` | `0.909` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `3564.19` | `0.976` | `0.648` | `+0.329` | `1.000` | `0.905` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `5349.02` | `0.972` | `0.652` | `+0.320` | `1.000` | `0.888` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `2789.18` | `0.967` | `0.639` | `+0.327` | `1.000` | `0.867` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `1994.20` | `0.991` | `0.658` | `+0.332` | `1.000` | `0.962` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `2904.88` | `0.967` | `0.641` | `+0.327` | `1.000` | `0.870` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `2816.13` | `0.966` | `0.645` | `+0.322` | `1.000` | `0.865` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `31230.37` | `0.975` | `0.000` | `+0.975` | `1.000` | `0.898` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `build-02` | `recall` | `build` | `4358.46` | `0.976` | `0.651` | `+0.325` | `1.000` | `0.902` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `22236.88` | `0.833` | `0.650` | `+0.183` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `2538.53` | `0.976` | `0.648` | `+0.329` | `1.000` | `0.905` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `build-03` | `summary` | `build` | `8368.63` | `0.896` | `0.591` | `+0.305` | `1.000` | `0.878` | `1.000` | `0.925` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `4999.65` | `0.886` | `0.577` | `+0.309` | `1.000` | `0.850` | `1.000` | `0.925` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `1946.17` | `0.961` | `0.642` | `+0.319` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `2288.29` | `0.953` | `0.000` | `+0.953` | `1.000` | `0.884` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `npm-09` | `summary` | `npm` | `2268.84` | `0.969` | `0.640` | `+0.328` | `1.000` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `734.86` | `0.936` | `0.000` | `+0.936` | `1.000` | `0.841` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `5808.01` | `0.763` | `0.000` | `+0.763` | `0.636` | `0.901` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | index.js | - |
| `testing-06` | `instruction_following` | `testing` | `5893.64` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `7367.73` | `0.479` | `0.000` | `+0.479` | `1.000` | `0.846` | `0.500` | `0.400` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `9417.17` | `0.143` | `0.000` | `+0.143` | `1.000` | `0.192` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `11487.88` | `0.240` | `0.000` | `+0.240` | `1.000` | `0.996` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `6548.42` | `0.925` | `0.000` | `+0.925` | `1.000` | `0.817` | `1.000` | `0.940` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `network-01` | `exact_format` | `network` | `3851.67` | `0.624` | `0.000` | `+0.624` | `1.000` | `0.332` | `0.675` | `0.574` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `6333.79` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response INFO: Retrying... ERROR: Timeout while waiting for response' |
| `shell-03` | `exact_format` | `shell` | `3261.96` | `0.715` | `0.000` | `+0.715` | `1.000` | `0.667` | `0.635` | `0.540` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `607.03` | `0.191` | `0.000` | `+0.191` | `1.000` | `0.320` | `0.150` | `0.150` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `build-04` | `exact_format` | `build` | `11085.16` | `0.812` | `0.000` | `+0.812` | `1.000` | `0.824` | `0.728` | `0.663` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `build-05` | `exact_format` | `build` | `942.95` | `0.730` | `0.000` | `+0.730` | `1.000` | `0.333` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `2480.91` | `0.587` | `0.000` | `+0.587` | `1.000` | `0.657` | `0.617` | `0.493` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `7627.30` | `0.949` | `0.627` | `+0.322` | `1.000` | `0.872` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `1869.04` | `0.937` | `0.619` | `+0.318` | `1.000` | `0.843` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `4891.64` | `0.967` | `0.644` | `+0.323` | `1.000` | `0.916` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `5795.04` | `0.960` | `0.637` | `+0.323` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `12499.43` | `0.874` | `0.580` | `+0.294` | `1.000` | `0.877` | `1.000` | `0.894` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `1525.33` | `0.945` | `0.000` | `+0.945` | `1.000` | `0.863` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `3136.42` | `0.964` | `0.639` | `+0.325` | `1.000` | `0.910` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `5356.86` | `0.947` | `0.627` | `+0.320` | `1.000` | `0.867` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1974.05` | `0.955` | `0.636` | `+0.319` | `1.000` | `0.888` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `1732.72` | `0.960` | `0.638` | `+0.322` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `2633.81` | `0.950` | `0.629` | `+0.321` | `1.000` | `0.875` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `6002.67` | `0.958` | `0.000` | `+0.958` | `1.000` | `0.894` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `783.34` | `0.939` | `0.000` | `+0.939` | `1.000` | `0.847` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `2339.02` | `0.946` | `0.629` | `+0.316` | `1.000` | `0.864` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `1201.37` | `0.936` | `0.000` | `+0.936` | `1.000` | `0.841` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `2815.05` | `0.945` | `0.628` | `+0.317` | `1.000` | `0.863` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `1821.13` | `0.959` | `0.000` | `+0.959` | `1.000` | `0.897` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `3390.25` | `0.945` | `0.627` | `+0.319` | `1.000` | `0.864` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `1679.66` | `0.946` | `0.000` | `+0.946` | `1.000` | `0.865` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `ci-07` | `structured` | `ci` | `11535.36` | `0.240` | `0.000` | `+0.240` | `1.000` | `0.996` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `linting-03` | `structured` | `linting` | `6296.55` | `0.925` | `0.000` | `+0.925` | `1.000` | `0.817` | `1.000` | `0.940` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `network-02` | `exact_format` | `network` | `3803.13` | `0.624` | `0.000` | `+0.624` | `1.000` | `0.332` | `0.675` | `0.574` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `5714.40` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.648` | `0.750` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response INFO: Retrying...' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response INFO: Retrying...' |
| `shell-07` | `exact_format` | `shell` | `1699.43` | `0.770` | `0.000` | `+0.770` | `1.000` | `0.000` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `build-06` | `exact_format` | `build` | `10940.70` | `0.812` | `0.000` | `+0.812` | `1.000` | `0.824` | `0.728` | `0.663` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `1932.96` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `build-07` | `exact_format` | `build` | `5521.77` | `0.574` | `0.000` | `+0.574` | `1.000` | `0.850` | `0.560` | `0.504` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `930.02` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `7406.99` | `0.949` | `0.627` | `+0.322` | `1.000` | `0.872` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `1902.13` | `0.937` | `0.619` | `+0.318` | `1.000` | `0.843` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `2442.10` | `0.968` | `0.641` | `+0.327` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `8760.49` | `0.976` | `0.649` | `+0.326` | `1.000` | `0.940` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `3043.34` | `0.964` | `0.639` | `+0.325` | `1.000` | `0.910` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `6419.33` | `0.971` | `0.645` | `+0.326` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `1100.02` | `0.930` | `0.000` | `+0.930` | `1.000` | `0.825` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `1671.19` | `0.969` | `0.000` | `+0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `3428.29` | `0.951` | `0.633` | `+0.318` | `1.000` | `0.878` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
