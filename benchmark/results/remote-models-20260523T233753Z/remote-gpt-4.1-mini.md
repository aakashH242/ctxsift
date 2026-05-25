# remote-gpt-4.1-mini

## Scenario

- track: `remote`
- phase: `remote-screen`
- model: `gpt-4.1-mini`
- quantization: `none`
- device: `remote`
- dtype: `remote`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `3927.47`
- cpu_rss_bytes: `695410688`
- gpu_peak_bytes: `0`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- recovered_final_score: `86.99`
- raw_final_score: `86.71`
- recovery_lift: `+0.28`
- case_count: `280`
- success_count: `276`
- accepted_count: `263`
- soft_accepted_count: `13`
- rejected_count: `4`
- exact_pass_count: `273`
- avg_inference_ms: `1588.35`
- p95_inference_ms: `2965.85`
- avg_exact_preservation_ratio: `0.993`
- avg_summary_quality_ratio: `0.880`
- avg_format_adherence_score: `0.932`
- avg_instruction_following_score: `0.921`
- avg_brevity_ratio: `0.969`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.905`
- p10_case_score: `0.730`
- quality_core: `0.870`
- latency_factor: `1.000`
- final_score: `86.99`
- peak_cpu_rss_bytes: `707776512`
- peak_gpu_bytes: `0`

### Raw View

- accepted_count: `257`
- soft_accepted_count: `20`
- rejected_count: `3`
- exact_pass_count: `273`
- avg_exact_preservation_ratio: `0.993`
- avg_summary_quality_ratio: `0.887`
- avg_format_adherence_score: `0.924`
- avg_instruction_following_score: `0.913`
- avg_brevity_ratio: `0.969`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.901`
- p10_case_score: `0.730`
- quality_core: `0.867`
- final_score: `86.71`

## Cases

| case_id | family | domain | ms | recovered_score | raw_score | lift | preserve | quality | format | instruction | recovered_thought_density | raw_thought_density | recovered_validation | raw_validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `1270.93` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-02` | `summary` | `python` | `1989.74` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.986` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-03` | `recall` | `python` | `1078.72` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `1236.51` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.965` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `1472.39` | `0.996` | `0.996` | `+0.000` | `1.000` | `0.984` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `1374.72` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `1947.31` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.981` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `1698.49` | `0.968` | `0.968` | `+0.000` | `1.000` | `0.974` | `1.000` | `0.956` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `1245.09` | `0.996` | `0.996` | `+0.000` | `1.000` | `0.983` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `1112.43` | `0.984` | `0.984` | `+0.000` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `1469.69` | `0.996` | `0.995` | `+0.001` | `1.000` | `0.983` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `3381.78` | `0.985` | `0.987` | `-0.001` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `1041.88` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.971` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ruff-01` | `recall` | `ruff` | `876.19` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.973` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ruff-02` | `summary` | `ruff` | `1077.01` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.982` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `2645.19` | `0.972` | `0.972` | `+0.000` | `1.000` | `0.929` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `2288.47` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.969` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `1245.97` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `1319.36` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.983` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `1108.70` | `0.996` | `0.996` | `+0.000` | `1.000` | `0.989` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `2285.55` | `0.983` | `0.983` | `+0.000` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `902.65` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `1456.18` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.974` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `1428.30` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `1192.85` | `0.960` | `0.960` | `+0.000` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `1182.78` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `1389.40` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.981` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `3142.96` | `0.980` | `0.980` | `+0.000` | `1.000` | `0.949` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `3900.54` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.978` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `1502.06` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `3140.36` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.968` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-01` | `recall` | `eslint` | `1563.30` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.969` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `1224.50` | `0.982` | `0.982` | `+0.000` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `1070.04` | `0.988` | `0.988` | `+0.000` | `1.000` | `0.952` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `899.89` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.968` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `1023.54` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.974` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `1115.83` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `1100.92` | `0.996` | `0.996` | `+0.000` | `1.000` | `0.991` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `1019.70` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.979` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `1020.85` | `0.998` | `0.998` | `+0.000` | `1.000` | `0.995` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `1334.10` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `1447.38` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `1107.79` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.988` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `1514.81` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `1044.37` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.982` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `824.99` | `0.997` | `0.997` | `+0.000` | `1.000` | `0.988` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `1106.86` | `0.998` | `0.998` | `+0.000` | `1.000` | `0.992` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `1000.01` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.983` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `1863.47` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.969` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `4594.61` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `1263.58` | `0.983` | `0.983` | `+0.000` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `824.46` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `1130.78` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `1627.02` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `curl-02` | `recall` | `curl` | `834.36` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.980` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ssh-01` | `summary` | `ssh` | `1313.83` | `0.986` | `0.989` | `-0.003` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `1145.19` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `857.95` | `0.985` | `0.985` | `+0.000` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `963.01` | `0.975` | `0.975` | `+0.000` | `1.000` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `1587.55` | `0.966` | `0.966` | `+0.000` | `1.000` | `0.960` | `1.000` | `0.976` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `1808.03` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `2888.01` | `0.977` | `0.977` | `+0.000` | `1.000` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `914.83` | `0.984` | `0.984` | `+0.000` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `javac-01` | `recall` | `javac` | `866.54` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `maven-01` | `recall` | `maven` | `1031.04` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.969` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `maven-02` | `summary` | `maven` | `1451.77` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.984` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `1048.95` | `0.998` | `0.998` | `+0.000` | `1.000` | `0.992` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `944.25` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `cargo-01` | `recall` | `cargo` | `925.98` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.968` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `cargo-02` | `recall` | `cargo` | `958.44` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.971` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `793.44` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.973` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-04` | `summary` | `npm` | `1337.61` | `0.988` | `0.988` | `+0.000` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `1266.49` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.984` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `1528.91` | `0.988` | `0.988` | `+0.000` | `1.000` | `0.971` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-runtime-01` | `recall` | `python-runtime` | `1039.91` | `0.996` | `0.996` | `+0.000` | `1.000` | `0.985` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `2158.74` | `0.997` | `0.997` | `+0.000` | `1.000` | `0.991` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `4474.16` | `0.989` | `0.988` | `+0.000` | `1.000` | `0.971` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `3902.16` | `0.983` | `0.984` | `-0.001` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `1668.89` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.982` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `978.60` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.981` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `2907.66` | `0.839` | `0.989` | `-0.149` | `1.000` | `0.968` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `4450.32` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.971` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `1257.31` | `0.998` | `0.998` | `+0.000` | `1.000` | `0.992` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `1011.23` | `0.978` | `0.978` | `+0.000` | `1.000` | `0.946` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `1041.29` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `871.68` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `1165.40` | `0.999` | `0.999` | `+0.000` | `1.000` | `0.998` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `1183.00` | `0.998` | `0.998` | `+0.000` | `1.000` | `0.991` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `1518.42` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.986` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `1184.92` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `945.47` | `0.988` | `0.988` | `+0.000` | `1.000` | `0.971` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `1210.67` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.974` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `1290.37` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.980` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `1383.88` | `0.978` | `0.978` | `+0.000` | `1.000` | `0.912` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `1257.31` | `0.982` | `0.982` | `+0.000` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `1121.59` | `0.971` | `0.971` | `+0.000` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `825.32` | `0.988` | `0.988` | `+0.000` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `1417.61` | `0.965` | `0.965` | `+0.000` | `1.000` | `0.914` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `1242.76` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.981` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `1276.67` | `0.988` | `0.988` | `+0.000` | `1.000` | `0.969` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `2605.17` | `0.996` | `0.996` | `+0.000` | `1.000` | `0.986` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `1380.18` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-log-01` | `recall` | `ci-log` | `1728.68` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `1589.78` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.971` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `2763.61` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.979` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-log-01` | `summary` | `build-log` | `2527.69` | `0.980` | `0.980` | `+0.000` | `1.000` | `0.949` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `1952.13` | `0.975` | `0.975` | `+0.000` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `2982.90` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.997` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='/repo/web/src/App.tsx - 27:19 @typescript-eslint/no-misused-promises /repo/web/src/api/client.ts - 8:10 @typescript-eslint/no-explicit-any - 33:11 @typescrip...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='/repo/web/src/App.tsx - 27:19 @typescript-eslint/no-misused-promises /repo/web/src/api/client.ts - 8:10 @typescript-eslint/no-explicit-any - 33:11 @typescrip...' |
| `git-review-01` | `instruction_following` | `git-review` | `2636.12` | `0.957` | `0.957` | `+0.000` | `1.000` | `0.856` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `1936.13` | `0.709` | `0.709` | `+0.000` | `0.355` | `0.310` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `4113.48` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `1277.39` | `0.204` | `0.983` | `-0.779` | `1.000` | `0.703` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `structured-output-03` | `structured` | `structured-output` | `2907.67` | `0.823` | `0.823` | `+0.000` | `0.929` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | "invalid refresh token" | - |
| `structured-output-04` | `structured` | `structured-output` | `1612.40` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `2570.27` | `0.437` | `0.437` | `+0.000` | `1.000` | `0.000` | `0.371` | `0.271` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `832.94` | `0.772` | `0.772` | `+0.000` | `1.000` | `0.776` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `2097.50` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `2757.81` | `0.977` | `0.977` | `+0.000` | `1.000` | `0.942` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `1045.08` | `0.967` | `0.967` | `+0.000` | `1.000` | `0.918` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `2513.11` | `0.725` | `0.725` | `+0.000` | `1.000` | `0.702` | `0.667` | `0.667` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `1196.18` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `1463.12` | `0.981` | `0.981` | `-0.000` | `1.000` | `0.924` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `1553.59` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.968` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `1494.01` | `0.984` | `0.984` | `+0.000` | `1.000` | `0.936` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `1832.70` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `1599.38` | `0.982` | `0.982` | `+0.000` | `1.000` | `0.930` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `1491.07` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `1143.57` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `2352.02` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `1370.62` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `1358.92` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `1156.78` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `1078.03` | `0.984` | `0.984` | `+0.000` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `1516.72` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `2808.04` | `0.788` | `0.788` | `+0.000` | `0.851` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Failed asserting that '88.00' is identical to '86.40' | - |
| `nginx-03` | `recall` | `nginx` | `1097.27` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.962` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `1390.49` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `1208.88` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.969` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `1169.43` | `0.970` | `0.970` | `+0.000` | `1.000` | `0.881` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `1263.40` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `2431.93` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `2133.98` | `0.767` | `0.767` | `+0.000` | `0.783` | `0.892` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | tests/refunds | - |
| `go-test-03` | `summary` | `go-test` | `2081.43` | `0.980` | `0.980` | `+0.000` | `1.000` | `0.949` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `2056.85` | `0.961` | `0.961` | `+0.000` | `1.000` | `0.903` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `1070.68` | `0.969` | `0.969` | `+0.000` | `1.000` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `2294.00` | `0.950` | `0.950` | `+0.000` | `1.000` | `0.875` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `1875.08` | `0.960` | `0.960` | `+0.000` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `2638.62` | `0.976` | `0.976` | `+0.000` | `1.000` | `0.940` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `1225.33` | `0.977` | `0.977` | `+0.000` | `1.000` | `0.942` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `2077.50` | `0.972` | `0.972` | `+0.000` | `1.000` | `0.931` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `2480.81` | `0.970` | `0.970` | `+0.001` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `1245.48` | `0.973` | `0.973` | `+0.000` | `1.000` | `0.931` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `2471.83` | `0.977` | `0.977` | `+0.000` | `1.000` | `0.942` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `1085.16` | `0.969` | `0.969` | `+0.000` | `1.000` | `0.922` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `2314.77` | `0.974` | `0.974` | `+0.000` | `1.000` | `0.936` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `1175.46` | `0.978` | `0.978` | `+0.000` | `1.000` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `1035.94` | `0.927` | `0.927` | `+0.000` | `1.000` | `0.757` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `992.07` | `0.943` | `0.943` | `+0.000` | `1.000` | `0.810` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `1748.80` | `0.450` | `0.450` | `+0.000` | `1.000` | `0.000` | `0.383` | `0.287` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `1249.99` | `0.907` | `0.907` | `+0.000` | `1.000` | `0.691` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `865.70` | `0.962` | `0.962` | `+0.000` | `1.000` | `0.875` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `934.78` | `0.874` | `0.874` | `+0.000` | `1.000` | `0.750` | `0.800` | `0.800` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `1025.56` | `0.731` | `0.731` | `+0.000` | `1.000` | `0.346` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `746.06` | `0.908` | `0.908` | `+0.000` | `1.000` | `0.694` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `1195.26` | `0.974` | `0.974` | `+0.000` | `1.000` | `0.914` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `1726.70` | `0.783` | `0.783` | `+0.000` | `0.818` | `0.859` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Payment complete | - |
| `prettier-01` | `instruction_following` | `prettier` | `1492.54` | `0.850` | `0.850` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `1679.39` | `0.850` | `0.850` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `1066.31` | `0.925` | `0.925` | `+0.000` | `1.000` | `0.750` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `1909.85` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.546` | `0.336` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) exit code 23' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) exit code 23' |
| `pyright-01` | `structured` | `pyright` | `1350.65` | `0.527` | `0.156` | `+0.371` | `1.000` | `0.545` | `0.450` | `0.450` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `1128.31` | `0.761` | `0.142` | `+0.619` | `1.000` | `0.593` | `0.771` | `0.771` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `junit-01` | `structured` | `junit` | `2083.17` | `0.713` | `0.713` | `+0.000` | `0.857` | `0.559` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | dividesByZero | - |
| `kubernetes-03` | `structured` | `kubernetes` | `1045.78` | `0.389` | `0.151` | `+0.237` | `1.000` | `0.323` | `0.333` | `0.333` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `2583.42` | `0.132` | `0.132` | `+0.000` | `1.000` | `0.194` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `1151.02` | `0.830` | `0.177` | `+0.652` | `1.000` | `0.766` | `0.800` | `0.800` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `899.81` | `0.389` | `0.749` | `-0.360` | `1.000` | `0.326` | `0.333` | `0.333` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `1101.11` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `1240.92` | `0.781` | `0.126` | `+0.655` | `1.000` | `0.601` | `0.800` | `0.800` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `1275.72` | `0.850` | `0.850` | `+0.000` | `1.000` | `0.500` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `823.96` | `0.219` | `0.140` | `+0.079` | `1.000` | `0.184` | `0.125` | `0.125` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `playwright-02` | `structured` | `playwright` | `892.47` | `0.361` | `0.143` | `+0.217` | `1.000` | `0.182` | `0.338` | `0.338` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `2648.27` | `0.000` | `0.158` | `-0.158` | `1.000` | `0.551` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `soft_accepted` | structured_contract_breakage | - | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml errors: - file: migrations/004.sql line: 12 column: null message: \'column "tenant_id" contains null values\' - file: migrations/004.sql line: 20 colum...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml errors: - file: migrations/004.sql line: 12 column: null message: \'column "tenant_id" contains null values\' - file: migrations/004.sql line: 20 colum...' |
| `vite-01` | `structured` | `vite` | `1087.03` | `0.476` | `0.126` | `+0.350` | `1.000` | `0.198` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `881.50` | `0.490` | `0.490` | `+0.000` | `1.000` | `0.000` | `0.430` | `0.333` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `836.52` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `883.02` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `590.49` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `1774.39` | `0.238` | `0.238` | `+0.000` | `1.000` | `0.322` | `0.233` | `0.205` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `1867.82` | `0.204` | `0.204` | `+0.000` | `0.500` | `0.298` | `0.277` | `0.277` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | prod | - |
| `cargo-05` | `exact_format` | `cargo` | `651.90` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `571.93` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `1462.71` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `1075.98` | `0.962` | `0.962` | `+0.000` | `1.000` | `0.906` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `1695.42` | `0.969` | `0.969` | `+0.000` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `1293.79` | `0.903` | `0.903` | `+0.000` | `1.000` | `0.678` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `838.99` | `0.971` | `0.971` | `+0.000` | `1.000` | `0.928` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `888.06` | `0.984` | `0.984` | `+0.000` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `3179.37` | `0.933` | `0.933` | `+0.000` | `1.000` | `0.832` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `1135.62` | `0.945` | `0.945` | `+0.000` | `1.000` | `0.862` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `715.87` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `747.76` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `856.86` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `841.37` | `0.977` | `0.977` | `+0.000` | `1.000` | `0.907` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `810.62` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.962` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `868.95` | `0.948` | `0.948` | `+0.000` | `1.000` | `0.952` | `1.000` | `0.931` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `3204.69` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `715.46` | `0.963` | `0.963` | `+0.000` | `1.000` | `0.853` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `800.79` | `0.980` | `0.980` | `+0.000` | `1.000` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `898.85` | `0.981` | `0.981` | `+0.000` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `775.66` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `776.58` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `621.02` | `0.974` | `0.974` | `+0.000` | `1.000` | `0.895` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `787.23` | `0.976` | `0.976` | `+0.000` | `1.000` | `0.905` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `603.80` | `0.980` | `0.980` | `+0.000` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `684.35` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.965` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `729.53` | `0.969` | `0.969` | `+0.000` | `1.000` | `0.874` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `1275.65` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.981` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `4274.45` | `0.972` | `0.972` | `+0.000` | `1.000` | `0.888` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `777.42` | `0.983` | `0.983` | `+0.000` | `1.000` | `0.934` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `951.45` | `0.978` | `0.978` | `+0.000` | `1.000` | `0.912` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `1405.78` | `0.984` | `0.984` | `+0.000` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `23587.94` | `0.833` | `0.978` | `-0.145` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `621.95` | `0.976` | `0.976` | `+0.000` | `1.000` | `0.905` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `991.60` | `0.969` | `0.969` | `+0.000` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `1384.00` | `0.945` | `0.945` | `+0.000` | `1.000` | `0.862` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `966.96` | `0.891` | `0.891` | `+0.000` | `1.000` | `0.947` | `1.000` | `0.880` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `1886.32` | `0.953` | `0.953` | `+0.000` | `1.000` | `0.884` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `1274.68` | `0.832` | `0.832` | `+0.000` | `1.000` | `0.958` | `1.000` | `0.790` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `967.48` | `0.940` | `0.940` | `+0.000` | `1.000` | `0.850` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `1709.34` | `0.968` | `0.968` | `+0.000` | `1.000` | `0.893` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `1085.20` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `4165.58` | `0.487` | `0.590` | `-0.103` | `1.000` | `0.993` | `0.500` | `0.365` | `0.000` | `0.000` | `soft_accepted` | `accepted` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `929.65` | `0.870` | `0.179` | `+0.691` | `1.000` | `0.839` | `0.833` | `0.833` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `839.52` | `0.404` | `1.000` | `-0.596` | `1.000` | `0.325` | `0.354` | `0.354` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `695.39` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `744.20` | `0.684` | `0.684` | `+0.000` | `1.000` | `0.991` | `0.635` | `0.635` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `1550.90` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response' |
| `shell-03` | `exact_format` | `shell` | `773.50` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `1415.67` | `0.191` | `0.191` | `+0.000` | `1.000` | `0.320` | `0.150` | `0.150` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `2227.71` | `0.513` | `0.513` | `+0.000` | `1.000` | `0.200` | `0.489` | `0.489` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `build-05` | `exact_format` | `build` | `670.36` | `0.730` | `0.730` | `+0.000` | `1.000` | `0.333` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `1489.69` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `1755.21` | `0.931` | `0.931` | `+0.000` | `1.000` | `0.900` | `1.000` | `0.960` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `1631.68` | `0.969` | `0.969` | `+0.000` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `1757.15` | `0.912` | `0.912` | `+0.000` | `1.000` | `0.896` | `1.000` | `0.937` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `2246.75` | `0.945` | `0.945` | `+0.000` | `1.000` | `0.894` | `1.000` | `0.982` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `1672.20` | `0.972` | `0.972` | `+0.000` | `1.000` | `0.929` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `1627.49` | `0.980` | `0.980` | `+0.000` | `1.000` | `0.951` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `2661.89` | `0.846` | `0.846` | `+0.000` | `1.000` | `0.838` | `1.000` | `0.876` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `1989.84` | `0.966` | `0.966` | `+0.000` | `1.000` | `0.916` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `2478.94` | `0.964` | `0.964` | `+0.000` | `1.000` | `0.911` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `2133.76` | `0.963` | `0.963` | `+0.000` | `1.000` | `0.907` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `759.08` | `0.960` | `0.960` | `+0.000` | `1.000` | `0.899` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `1700.54` | `0.958` | `0.958` | `+0.000` | `1.000` | `0.929` | `1.000` | `0.981` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `2229.79` | `0.814` | `0.814` | `+0.000` | `1.000` | `0.831` | `1.000` | `0.833` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `2104.84` | `0.959` | `0.959` | `+0.000` | `1.000` | `0.898` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `2060.44` | `0.916` | `0.916` | `+0.000` | `1.000` | `0.868` | `1.000` | `0.957` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `2120.21` | `0.961` | `0.961` | `+0.000` | `1.000` | `0.902` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `2121.84` | `0.888` | `0.888` | `+0.000` | `1.000` | `0.891` | `1.000` | `0.906` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `2030.24` | `0.915` | `0.915` | `+0.000` | `1.000` | `0.903` | `1.000` | `0.937` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `1421.63` | `0.962` | `0.962` | `+0.000` | `1.000` | `0.906` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `1019.70` | `0.404` | `1.000` | `-0.596` | `1.000` | `0.325` | `0.354` | `0.354` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `747.46` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `1268.78` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `723.49` | `0.729` | `0.729` | `+0.000` | `1.000` | `0.319` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `724.74` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `1718.70` | `0.787` | `0.787` | `+0.000` | `1.000` | `0.714` | `0.673` | `0.673` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `682.29` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `1277.03` | `0.191` | `0.191` | `+0.000` | `1.000` | `0.319` | `0.150` | `0.150` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `1494.68` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `1740.83` | `0.946` | `0.946` | `+0.000` | `1.000` | `0.905` | `1.000` | `0.979` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `2032.23` | `0.944` | `0.944` | `+0.000` | `1.000` | `0.925` | `1.000` | `0.965` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `1489.18` | `0.968` | `0.968` | `+0.000` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `1788.06` | `0.902` | `0.902` | `+0.000` | `1.000` | `0.906` | `1.000` | `0.917` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `1708.30` | `0.833` | `0.833` | `+0.000` | `1.000` | `0.836` | `1.000` | `0.858` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `2003.08` | `0.937` | `0.937` | `+0.000` | `1.000` | `0.904` | `1.000` | `0.967` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `1864.38` | `0.965` | `0.965` | `+0.000` | `1.000` | `0.912` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `1627.48` | `0.980` | `0.980` | `+0.000` | `1.000` | `0.951` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1941.82` | `0.952` | `0.952` | `+0.000` | `1.000` | `0.880` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
