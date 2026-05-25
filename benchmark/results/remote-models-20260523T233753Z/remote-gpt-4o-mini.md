# remote-gpt-4o-mini

## Scenario

- track: `remote`
- phase: `remote-screen`
- model: `gpt-4o-mini`
- quantization: `none`
- device: `remote`
- dtype: `remote`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `2515.49`
- cpu_rss_bytes: `1950507008`
- gpu_peak_bytes: `1260272640`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- recovered_final_score: `84.61`
- raw_final_score: `84.30`
- recovery_lift: `+0.31`
- case_count: `280`
- success_count: `279`
- accepted_count: `262`
- soft_accepted_count: `17`
- rejected_count: `1`
- exact_pass_count: `274`
- avg_inference_ms: `1519.84`
- p95_inference_ms: `2974.37`
- avg_exact_preservation_ratio: `0.990`
- avg_summary_quality_ratio: `0.863`
- avg_format_adherence_score: `0.919`
- avg_instruction_following_score: `0.912`
- avg_brevity_ratio: `0.962`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.896`
- p10_case_score: `0.648`
- quality_core: `0.846`
- latency_factor: `1.000`
- final_score: `84.61`
- peak_cpu_rss_bytes: `1950584832`
- peak_gpu_bytes: `1260272640`

### Raw View

- accepted_count: `257`
- soft_accepted_count: `23`
- rejected_count: `0`
- exact_pass_count: `274`
- avg_exact_preservation_ratio: `0.990`
- avg_summary_quality_ratio: `0.870`
- avg_format_adherence_score: `0.910`
- avg_instruction_following_score: `0.902`
- avg_brevity_ratio: `0.965`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.892`
- p10_case_score: `0.648`
- quality_core: `0.843`
- final_score: `84.30`

## Cases

| case_id | family | domain | ms | recovered_score | raw_score | lift | preserve | quality | format | instruction | recovered_thought_density | raw_thought_density | recovered_validation | raw_validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `5894.63` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.973` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-02` | `summary` | `python` | `2722.62` | `0.988` | `0.988` | `+0.000` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-03` | `recall` | `python` | `1032.02` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `1164.00` | `0.989` | `0.990` | `-0.000` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `987.45` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.971` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `2281.77` | `0.992` | `0.991` | `+0.000` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `3092.95` | `0.981` | `0.981` | `-0.000` | `1.000` | `0.952` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `3107.19` | `0.991` | `0.990` | `+0.000` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `1249.57` | `0.997` | `0.997` | `+0.000` | `1.000` | `0.987` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `2262.02` | `0.981` | `0.981` | `+0.000` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `1121.04` | `0.998` | `0.997` | `+0.000` | `1.000` | `0.990` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `3060.09` | `0.984` | `0.984` | `-0.000` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `1603.84` | `0.997` | `0.996` | `+0.001` | `1.000` | `0.987` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ruff-01` | `recall` | `ruff` | `1036.89` | `0.990` | `0.991` | `-0.001` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ruff-02` | `summary` | `ruff` | `1875.92` | `0.994` | `0.994` | `-0.000` | `1.000` | `0.986` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `2704.61` | `0.972` | `0.971` | `+0.001` | `1.000` | `0.930` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `913.05` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `1068.11` | `0.982` | `0.982` | `+0.000` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `853.93` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.983` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `930.83` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `1832.90` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `959.37` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `3171.23` | `0.985` | `0.984` | `+0.000` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `1378.69` | `0.980` | `0.979` | `+0.001` | `1.000` | `0.949` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `2187.14` | `0.986` | `0.986` | `+0.000` | `1.000` | `0.965` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `1311.48` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.969` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `1347.51` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `3224.78` | `0.807` | `0.807` | `+0.000` | `0.905` | `0.934` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Exit status 1 | - |
| `typescript-01` | `summary` | `typescript` | `1148.94` | `0.981` | `0.982` | `-0.001` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `803.39` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.968` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `2941.75` | `0.983` | `0.983` | `+0.000` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-01` | `recall` | `eslint` | `1377.23` | `0.985` | `0.986` | `-0.001` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `8575.04` | `0.980` | `0.980` | `+0.000` | `1.000` | `0.951` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `1303.69` | `0.985` | `0.985` | `+0.000` | `1.000` | `0.940` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `962.70` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `1054.52` | `0.977` | `0.977` | `+0.000` | `1.000` | `0.943` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `1057.65` | `0.977` | `0.979` | `-0.001` | `1.000` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `759.78` | `0.996` | `0.996` | `+0.000` | `1.000` | `0.990` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `1199.79` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.974` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `1273.64` | `0.978` | `0.978` | `+0.000` | `1.000` | `0.945` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `1100.43` | `0.979` | `0.979` | `+0.000` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `2747.79` | `0.990` | `0.989` | `+0.001` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `1745.89` | `0.988` | `0.988` | `+0.000` | `1.000` | `0.971` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `1865.83` | `0.948` | `0.948` | `+0.000` | `1.000` | `0.937` | `1.000` | `0.936` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `973.13` | `0.988` | `0.988` | `+0.000` | `1.000` | `0.969` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `1886.22` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `1429.46` | `0.989` | `0.989` | `-0.001` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `2234.14` | `0.978` | `0.977` | `+0.001` | `1.000` | `0.945` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `2322.89` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `870.84` | `0.975` | `0.975` | `+0.000` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `777.55` | `0.971` | `0.971` | `+0.000` | `1.000` | `0.885` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `1793.84` | `0.985` | `0.985` | `+0.000` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `942.26` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `6660.93` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `curl-02` | `recall` | `curl` | `981.49` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ssh-01` | `summary` | `ssh` | `1439.27` | `0.983` | `0.982` | `+0.001` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `910.69` | `0.983` | `0.983` | `+0.000` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `728.58` | `0.982` | `0.982` | `+0.000` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `976.42` | `0.966` | `0.966` | `+0.000` | `1.000` | `0.916` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `1219.80` | `0.975` | `0.648` | `+0.327` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `1156.64` | `0.990` | `0.989` | `+0.001` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `865.35` | `0.976` | `0.976` | `-0.000` | `1.000` | `0.940` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `2162.97` | `0.979` | `0.980` | `-0.000` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `javac-01` | `recall` | `javac` | `1183.04` | `0.986` | `0.986` | `+0.000` | `1.000` | `0.946` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `maven-01` | `recall` | `maven` | `1469.48` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.969` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `maven-02` | `summary` | `maven` | `2964.85` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.988` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `1520.43` | `0.988` | `0.661` | `+0.327` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `2019.65` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `cargo-01` | `recall` | `cargo` | `1184.34` | `0.985` | `0.985` | `+0.000` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `cargo-02` | `recall` | `cargo` | `962.27` | `0.999` | `0.999` | `+0.000` | `1.000` | `0.995` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `1075.36` | `0.991` | `0.992` | `-0.001` | `1.000` | `0.962` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-04` | `summary` | `npm` | `2358.21` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `726.37` | `0.985` | `0.985` | `+0.000` | `1.000` | `0.962` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `880.00` | `0.989` | `0.988` | `+0.001` | `1.000` | `0.973` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-runtime-01` | `recall` | `python-runtime` | `766.18` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.978` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `944.06` | `0.986` | `0.985` | `+0.001` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `2093.76` | `0.981` | `0.983` | `-0.002` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `2416.97` | `0.976` | `0.978` | `-0.002` | `1.000` | `0.940` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `2234.18` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.979` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `2238.44` | `0.977` | `0.977` | `+0.000` | `1.000` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `1938.73` | `0.830` | `0.980` | `-0.150` | `1.000` | `0.942` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `1210.97` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.974` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `1396.86` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `849.89` | `0.976` | `0.976` | `+0.000` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `1301.05` | `0.960` | `0.955` | `+0.005` | `1.000` | `0.899` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `2483.17` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.980` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `836.44` | `0.987` | `0.987` | `-0.000` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `1165.58` | `0.998` | `0.998` | `+0.000` | `1.000` | `0.991` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `1213.91` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `1015.29` | `0.981` | `0.983` | `-0.002` | `1.000` | `0.952` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `1162.65` | `0.985` | `0.986` | `-0.001` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `1627.31` | `0.971` | `0.646` | `+0.325` | `1.000` | `0.929` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `793.62` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `869.41` | `0.983` | `0.983` | `+0.000` | `1.000` | `0.931` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `1344.06` | `0.983` | `0.983` | `+0.000` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `632.85` | `0.967` | `0.968` | `-0.002` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `1133.09` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `1024.06` | `0.979` | `0.654` | `+0.325` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `848.80` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.978` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `1021.16` | `0.981` | `0.982` | `-0.001` | `1.000` | `0.952` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `1034.26` | `0.990` | `0.991` | `-0.000` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `984.56` | `0.986` | `0.988` | `-0.002` | `1.000` | `0.945` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-log-01` | `recall` | `ci-log` | `1148.57` | `0.985` | `0.987` | `-0.001` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `1218.89` | `0.994` | `0.993` | `+0.001` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `1467.09` | `0.985` | `0.985` | `+0.000` | `1.000` | `0.962` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-log-01` | `summary` | `build-log` | `975.91` | `0.978` | `0.978` | `+0.000` | `1.000` | `0.946` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `651.65` | `0.975` | `0.975` | `+0.000` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `2191.40` | `0.440` | `0.440` | `+0.000` | `1.000` | `0.632` | `0.400` | `0.320` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `1233.74` | `0.953` | `0.953` | `+0.000` | `1.000` | `0.842` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `1598.28` | `0.692` | `0.692` | `+0.000` | `0.226` | `0.300` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | exit status 22, https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `1594.32` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `2079.87` | `0.227` | `0.227` | `-0.000` | `1.000` | `0.894` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `structured-output-03` | `structured` | `structured-output` | `3768.21` | `0.936` | `0.936` | `+0.000` | `1.000` | `0.787` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `structured-output-04` | `structured` | `structured-output` | `1608.48` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `2283.75` | `0.850` | `0.850` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `1942.50` | `0.568` | `0.568` | `-0.000` | `1.000` | `0.331` | `0.576` | `0.576` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `1083.27` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `1133.63` | `0.973` | `0.973` | `+0.000` | `1.000` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `3364.86` | `0.948` | `0.948` | `+0.000` | `1.000` | `0.870` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `1464.83` | `0.713` | `0.713` | `+0.000` | `1.000` | `0.658` | `0.667` | `0.667` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `985.09` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `912.02` | `0.988` | `0.988` | `+0.001` | `1.000` | `0.952` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `1317.38` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.968` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `1086.30` | `0.978` | `0.977` | `+0.001` | `1.000` | `0.911` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `1307.91` | `0.988` | `0.988` | `+0.000` | `1.000` | `0.951` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `1713.53` | `0.983` | `0.984` | `-0.001` | `1.000` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `1119.10` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.965` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `885.29` | `0.987` | `0.988` | `-0.000` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `1337.82` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `2505.69` | `0.991` | `0.990` | `+0.001` | `1.000` | `0.962` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `3254.22` | `0.988` | `0.988` | `+0.000` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `975.23` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `1119.89` | `0.984` | `0.984` | `+0.000` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `911.51` | `0.984` | `0.984` | `+0.000` | `1.000` | `0.934` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `1393.95` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `937.09` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `1280.07` | `0.989` | `0.989` | `-0.001` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `866.90` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `879.64` | `0.968` | `0.968` | `+0.000` | `1.000` | `0.872` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `920.69` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `2520.91` | `0.996` | `0.996` | `+0.000` | `1.000` | `0.985` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `2239.50` | `0.769` | `0.769` | `+0.000` | `0.783` | `0.897` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | tests/refunds | - |
| `go-test-03` | `summary` | `go-test` | `3195.66` | `0.969` | `0.966` | `+0.003` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `2162.06` | `0.953` | `0.953` | `+0.000` | `1.000` | `0.883` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `956.65` | `0.971` | `0.971` | `+0.000` | `1.000` | `0.928` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `2773.57` | `0.960` | `0.961` | `-0.000` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `2570.49` | `0.775` | `0.775` | `+0.000` | `0.826` | `0.888` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | smoke.js | - |
| `composer-01` | `summary` | `composer` | `1925.76` | `0.945` | `0.942` | `+0.003` | `1.000` | `0.862` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `1769.99` | `0.943` | `0.943` | `+0.000` | `1.000` | `0.856` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `2766.89` | `0.649` | `0.649` | `+0.000` | `1.000` | `0.931` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `2368.73` | `0.969` | `0.970` | `-0.000` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `705.83` | `0.953` | `0.958` | `-0.005` | `1.000` | `0.882` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `2132.43` | `0.972` | `0.972` | `+0.001` | `1.000` | `0.930` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `1052.92` | `0.967` | `0.967` | `+0.000` | `1.000` | `0.918` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `4058.91` | `0.972` | `0.979` | `-0.006` | `1.000` | `0.931` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `1080.35` | `0.974` | `0.974` | `-0.001` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `1025.65` | `0.935` | `0.935` | `+0.000` | `1.000` | `0.782` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `1077.41` | `0.603` | `0.603` | `+0.000` | `1.000` | `0.696` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `2081.14` | `0.546` | `0.546` | `+0.000` | `1.000` | `0.000` | `0.617` | `0.524` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `1109.57` | `0.907` | `0.907` | `+0.000` | `1.000` | `0.691` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `826.23` | `0.962` | `0.962` | `+0.000` | `1.000` | `0.875` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `936.41` | `0.874` | `0.874` | `+0.000` | `1.000` | `0.750` | `0.800` | `0.800` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `1048.48` | `0.731` | `0.731` | `+0.000` | `1.000` | `0.346` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `656.89` | `0.483` | `0.483` | `+0.000` | `1.000` | `0.752` | `0.333` | `0.333` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `1012.93` | `0.724` | `0.724` | `+0.000` | `1.000` | `0.698` | `0.667` | `0.667` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `2472.61` | `0.401` | `0.401` | `+0.000` | `1.000` | `0.682` | `0.250` | `0.250` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `1639.95` | `0.850` | `0.850` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `958.61` | `0.751` | `0.751` | `+0.000` | `1.000` | `0.500` | `0.725` | `0.580` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `1250.86` | `0.923` | `0.923` | `+0.000` | `1.000` | `0.743` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `1875.48` | `0.261` | `0.261` | `+0.000` | `0.500` | `0.294` | `0.360` | `0.360` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | rsync, /var/backups/uploads | - |
| `pyright-01` | `structured` | `pyright` | `2102.32` | `0.479` | `0.165` | `+0.314` | `1.000` | `0.545` | `0.388` | `0.388` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `1897.43` | `0.128` | `0.128` | `+0.000` | `1.000` | `0.188` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `junit-01` | `structured` | `junit` | `1579.63` | `0.928` | `0.928` | `+0.000` | `1.000` | `0.760` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `1470.83` | `0.389` | `0.151` | `+0.237` | `1.000` | `0.323` | `0.333` | `0.333` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `1292.63` | `0.701` | `0.701` | `+0.000` | `1.000` | `0.194` | `0.875` | `0.875` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `1560.74` | `0.653` | `0.653` | `+0.000` | `1.000` | `0.595` | `0.714` | `0.583` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `1578.70` | `0.389` | `0.164` | `+0.225` | `1.000` | `0.326` | `0.333` | `0.333` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `1349.26` | `0.986` | `0.986` | `+0.000` | `1.000` | `1.000` | `1.000` | `0.957` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `2112.77` | `0.781` | `0.781` | `+0.000` | `1.000` | `0.601` | `0.800` | `0.800` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `2158.29` | `0.911` | `0.911` | `+0.000` | `1.000` | `0.815` | `1.000` | `0.900` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `993.56` | `0.219` | `0.219` | `+0.000` | `1.000` | `0.183` | `0.125` | `0.125` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `playwright-02` | `structured` | `playwright` | `1460.32` | `0.345` | `0.345` | `+0.000` | `1.000` | `0.187` | `0.312` | `0.312` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `2832.41` | `0.000` | `0.157` | `-0.157` | `1.000` | `0.538` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `soft_accepted` | structured_contract_breakage | - | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml errors: - file: "migrations/004.sql" line: 12 message: "ERROR: column \\"tenant_id\\" contains null values" column: "tenant_id" - file: "migrations/004...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml errors: - file: "migrations/004.sql" line: 12 message: "ERROR: column \\"tenant_id\\" contains null values" column: "tenant_id" - file: "migrations/004...' |
| `vite-01` | `structured` | `vite` | `1569.22` | `0.103` | `0.103` | `+0.000` | `1.000` | `0.178` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `1566.28` | `0.850` | `0.850` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `git-04` | `exact_format` | `git` | `788.09` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `1085.42` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `589.39` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `1081.64` | `0.176` | `0.176` | `-0.000` | `1.000` | `0.319` | `0.165` | `0.130` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `721.49` | `0.355` | `0.355` | `+0.000` | `1.000` | `0.305` | `0.350` | `0.350` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `827.25` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `714.77` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `1021.87` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `1067.76` | `0.973` | `0.973` | `+0.000` | `1.000` | `0.931` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `2003.46` | `0.958` | `0.958` | `+0.000` | `1.000` | `0.895` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `1086.90` | `0.888` | `0.888` | `+0.000` | `1.000` | `0.628` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `2751.25` | `0.970` | `0.970` | `+0.000` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `930.69` | `0.971` | `0.971` | `+0.000` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `1136.20` | `0.933` | `0.933` | `+0.000` | `1.000` | `0.833` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `1882.77` | `0.949` | `0.952` | `-0.003` | `1.000` | `0.872` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `742.58` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `1087.09` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `2131.13` | `0.661` | `0.661` | `+0.000` | `1.000` | `0.955` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `package-management-01` | `recall` | `package-management` | `840.37` | `0.974` | `0.974` | `+0.000` | `1.000` | `0.898` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `972.89` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `932.07` | `0.939` | `0.939` | `+0.000` | `1.000` | `0.955` | `1.000` | `0.914` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `1042.90` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `779.90` | `0.976` | `0.976` | `+0.000` | `1.000` | `0.904` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `1772.97` | `0.960` | `0.960` | `+0.000` | `1.000` | `0.841` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `1040.94` | `0.981` | `0.981` | `+0.000` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `1892.08` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `1044.80` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `853.56` | `0.975` | `0.975` | `+0.000` | `1.000` | `0.900` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `793.22` | `0.982` | `0.982` | `+0.000` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `1058.76` | `0.982` | `0.982` | `+0.000` | `1.000` | `0.929` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `759.81` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `961.84` | `0.969` | `0.969` | `+0.000` | `1.000` | `0.874` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `782.98` | `0.996` | `0.996` | `+0.000` | `1.000` | `0.984` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `851.57` | `0.972` | `0.972` | `+0.000` | `1.000` | `0.888` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `638.65` | `0.958` | `0.958` | `+0.000` | `1.000` | `0.831` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `1035.40` | `0.978` | `0.978` | `+0.000` | `1.000` | `0.913` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `1111.87` | `0.983` | `0.983` | `+0.000` | `1.000` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `2963.96` | `0.833` | `0.978` | `-0.145` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `672.92` | `0.974` | `0.974` | `+0.000` | `1.000` | `0.895` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `1084.24` | `0.969` | `0.969` | `+0.000` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `585.39` | `0.945` | `0.945` | `+0.000` | `1.000` | `0.862` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `801.01` | `0.935` | `0.935` | `+0.000` | `1.000` | `0.837` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `834.77` | `0.953` | `0.953` | `+0.000` | `1.000` | `0.884` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `631.27` | `0.976` | `0.976` | `+0.000` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `1192.38` | `0.936` | `0.936` | `+0.000` | `1.000` | `0.841` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `755.56` | `0.581` | `0.581` | `+0.000` | `1.000` | `0.610` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `1599.64` | `0.972` | `0.972` | `+0.000` | `1.000` | `0.907` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `2239.86` | `0.359` | `0.504` | `-0.144` | `1.000` | `0.845` | `0.333` | `0.250` | `0.000` | `0.000` | `soft_accepted` | `accepted` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `1100.78` | `0.143` | `0.143` | `+0.000` | `1.000` | `0.188` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `978.66` | `0.404` | `1.000` | `-0.596` | `1.000` | `0.325` | `0.354` | `0.354` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `995.47` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `1105.87` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `1475.85` | `0.729` | `0.729` | `+0.000` | `1.000` | `0.319` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `701.09` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `1294.45` | `0.191` | `0.191` | `+0.000` | `1.000` | `0.320` | `0.150` | `0.150` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `2181.76` | `0.583` | `0.583` | `+0.000` | `1.000` | `0.000` | `0.623` | `0.623` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `build-05` | `exact_format` | `build` | `596.04` | `0.730` | `0.730` | `+0.000` | `1.000` | `0.333` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `634.40` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `1853.87` | `0.935` | `0.935` | `+0.000` | `1.000` | `0.911` | `1.000` | `0.960` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `964.45` | `0.954` | `0.954` | `+0.000` | `1.000` | `0.884` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `2007.38` | `0.911` | `0.911` | `+0.000` | `1.000` | `0.894` | `1.000` | `0.937` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `1679.70` | `0.910` | `0.910` | `+0.000` | `1.000` | `0.905` | `1.000` | `0.929` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `937.03` | `0.903` | `0.903` | `+0.000` | `1.000` | `0.904` | `1.000` | `0.920` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `1819.00` | `0.945` | `0.945` | `+0.000` | `1.000` | `0.863` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `1772.04` | `0.897` | `0.897` | `+0.000` | `1.000` | `0.869` | `1.000` | `0.931` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `1745.58` | `0.965` | `0.965` | `+0.000` | `1.000` | `0.913` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1853.90` | `0.867` | `0.867` | `+0.000` | `1.000` | `0.895` | `1.000` | `0.874` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `1680.46` | `0.960` | `0.960` | `+0.000` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `1819.16` | `0.950` | `0.950` | `+0.000` | `1.000` | `0.875` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `2226.95` | `0.881` | `0.881` | `+0.000` | `1.000` | `0.922` | `1.000` | `0.880` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `1506.28` | `0.939` | `0.939` | `+0.000` | `1.000` | `0.847` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `4433.73` | `0.886` | `0.886` | `+0.000` | `1.000` | `0.896` | `1.000` | `0.900` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `2286.91` | `0.912` | `0.912` | `+0.000` | `1.000` | `0.890` | `1.000` | `0.940` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `2022.84` | `0.955` | `0.955` | `+0.000` | `1.000` | `0.886` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `1773.80` | `0.876` | `0.876` | `+0.000` | `1.000` | `0.883` | `1.000` | `0.894` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `1985.52` | `0.898` | `0.898` | `+0.000` | `1.000` | `0.935` | `1.000` | `0.896` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `806.59` | `0.922` | `0.922` | `+0.000` | `1.000` | `0.901` | `1.000` | `0.947` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `1189.21` | `0.404` | `0.197` | `+0.207` | `1.000` | `0.325` | `0.354` | `0.354` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `1169.74` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `757.88` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `1369.24` | `0.729` | `0.729` | `+0.000` | `1.000` | `0.319` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `622.73` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `1569.49` | `0.640` | `0.640` | `+0.000` | `1.000` | `0.250` | `0.688` | `0.688` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `runtime-07` | `exact_format` | `runtime` | `777.59` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `669.88` | `0.191` | `0.191` | `+0.000` | `1.000` | `0.319` | `0.150` | `0.150` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `1385.20` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `1365.24` | `0.948` | `0.948` | `+0.000` | `1.000` | `0.870` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `852.89` | `0.924` | `0.924` | `+0.000` | `1.000` | `0.876` | `1.000` | `0.965` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `1649.51` | `0.972` | `0.972` | `+0.000` | `1.000` | `0.929` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `2223.34` | `0.928` | `0.928` | `+0.000` | `1.000` | `0.892` | `1.000` | `0.960` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `2003.14` | `0.893` | `0.893` | `+0.000` | `1.000` | `0.859` | `1.000` | `0.931` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `1876.56` | `0.931` | `0.931` | `+0.000` | `1.000` | `0.914` | `1.000` | `0.953` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `1651.12` | `0.606` | `0.606` | `+0.000` | `0.000` | `0.906` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | undefined: fmt.Println | - |
| `explanation-17` | `explanation` | `explanation` | `1796.99` | `0.886` | `0.886` | `+0.000` | `1.000` | `0.920` | `1.000` | `0.887` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1675.01` | `0.942` | `0.942` | `+0.000` | `1.000` | `0.856` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
