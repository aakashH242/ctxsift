# remote-gpt-4o

## Scenario

- track: `remote`
- phase: `remote-screen`
- model: `gpt-4o`
- quantization: `none`
- device: `remote`
- dtype: `remote`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `1464.14`
- cpu_rss_bytes: `1958047744`
- gpu_peak_bytes: `1260272640`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- recovered_final_score: `86.28`
- raw_final_score: `82.77`
- recovery_lift: `+3.51`
- case_count: `280`
- success_count: `274`
- accepted_count: `253`
- soft_accepted_count: `21`
- rejected_count: `6`
- exact_pass_count: `266`
- avg_inference_ms: `1429.00`
- p95_inference_ms: `2379.61`
- avg_exact_preservation_ratio: `0.985`
- avg_summary_quality_ratio: `0.879`
- avg_format_adherence_score: `0.936`
- avg_instruction_following_score: `0.920`
- avg_brevity_ratio: `0.974`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.897`
- p10_case_score: `0.727`
- quality_core: `0.863`
- latency_factor: `1.000`
- final_score: `86.28`
- peak_cpu_rss_bytes: `1958047744`
- peak_gpu_bytes: `1260272640`

### Raw View

- accepted_count: `237`
- soft_accepted_count: `39`
- rejected_count: `4`
- exact_pass_count: `266`
- avg_exact_preservation_ratio: `0.985`
- avg_summary_quality_ratio: `0.883`
- avg_format_adherence_score: `0.906`
- avg_instruction_following_score: `0.890`
- avg_brevity_ratio: `0.975`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.875`
- p10_case_score: `0.640`
- quality_core: `0.828`
- final_score: `82.77`

## Cases

| case_id | family | domain | ms | recovered_score | raw_score | lift | preserve | quality | format | instruction | recovered_thought_density | raw_thought_density | recovered_validation | raw_validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `1127.00` | `0.989` | `0.990` | `-0.001` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-02` | `summary` | `python` | `2839.74` | `0.975` | `0.975` | `+0.000` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-03` | `recall` | `python` | `1893.37` | `0.785` | `0.785` | `+0.000` | `0.873` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Worker failed to boot. | - |
| `python-04` | `recall` | `python` | `919.98` | `0.998` | `0.998` | `+0.000` | `1.000` | `0.991` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `1063.79` | `0.998` | `0.998` | `+0.000` | `1.000` | `0.990` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `1132.87` | `0.983` | `0.983` | `+0.000` | `1.000` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `1058.31` | `0.984` | `0.985` | `-0.002` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `1086.59` | `0.996` | `0.996` | `+0.000` | `1.000` | `0.983` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `1715.72` | `0.998` | `0.998` | `+0.000` | `1.000` | `0.993` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `2993.08` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.968` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `851.25` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `2148.56` | `0.813` | `0.813` | `+0.000` | `0.895` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | checked 37 source files | - |
| `mypy-03` | `recall` | `mypy` | `1099.13` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ruff-01` | `recall` | `ruff` | `982.88` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.973` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ruff-02` | `summary` | `ruff` | `1621.23` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `2189.98` | `0.742` | `0.742` | `+0.000` | `0.829` | `0.917` | `1.000` | `0.929` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Found 1 error. | - |
| `pylint-01` | `recall` | `pylint` | `838.93` | `0.996` | `0.996` | `+0.000` | `1.000` | `0.983` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `883.85` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `842.21` | `0.997` | `0.997` | `+0.000` | `1.000` | `0.993` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `1805.43` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `1756.14` | `0.982` | `0.984` | `-0.002` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `942.15` | `0.996` | `0.996` | `+0.000` | `1.000` | `0.985` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `2252.79` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `2028.20` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `1987.42` | `0.973` | `0.973` | `+0.000` | `1.000` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `939.91` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `901.46` | `0.988` | `0.988` | `+0.000` | `1.000` | `0.969` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `2426.55` | `0.971` | `0.971` | `+0.000` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `2099.49` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.973` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `866.57` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.981` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `2284.84` | `0.794` | `0.794` | `+0.000` | `0.808` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | src/http.ts(9,17) | - |
| `eslint-01` | `recall` | `eslint` | `1033.47` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.974` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `3098.46` | `0.978` | `0.978` | `+0.000` | `1.000` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `917.79` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.979` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `896.70` | `0.997` | `0.997` | `+0.000` | `1.000` | `0.988` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `794.33` | `0.973` | `0.973` | `+0.000` | `1.000` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `910.14` | `0.979` | `0.980` | `-0.000` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `699.29` | `0.986` | `0.986` | `+0.000` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `788.24` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.982` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `1801.35` | `0.976` | `0.976` | `+0.000` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `858.43` | `0.986` | `0.986` | `+0.000` | `1.000` | `0.965` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `1032.51` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `684.22` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `937.66` | `0.983` | `0.983` | `+0.000` | `1.000` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `1069.93` | `0.984` | `0.984` | `+0.000` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `732.99` | `0.997` | `0.997` | `+0.000` | `1.000` | `0.990` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `2801.01` | `0.996` | `0.996` | `+0.000` | `1.000` | `0.985` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `2022.83` | `0.780` | `0.780` | `+0.000` | `0.707` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | terraform test | - |
| `mixed-01` | `recall` | `mixed` | `820.46` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `892.71` | `0.969` | `0.969` | `+0.000` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `726.93` | `0.980` | `0.980` | `+0.000` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `646.59` | `0.985` | `0.985` | `+0.000` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `812.75` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.981` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `912.64` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `curl-02` | `recall` | `curl` | `806.47` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.981` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ssh-01` | `summary` | `ssh` | `1353.06` | `0.970` | `0.970` | `+0.000` | `1.000` | `0.925` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `1853.57` | `0.795` | `0.795` | `+0.000` | `0.788` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Host key verification failed. | - |
| `systemd-01` | `summary` | `systemd` | `797.27` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.979` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `900.11` | `0.964` | `0.964` | `+0.000` | `1.000` | `0.910` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `1083.77` | `0.957` | `0.957` | `+0.000` | `1.000` | `0.891` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `822.67` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `912.15` | `0.976` | `0.976` | `+0.000` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `804.46` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.979` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `javac-01` | `recall` | `javac` | `700.36` | `0.986` | `0.986` | `+0.000` | `1.000` | `0.946` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `maven-01` | `recall` | `maven` | `789.15` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.982` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `maven-02` | `summary` | `maven` | `2033.64` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `830.14` | `0.999` | `0.999` | `+0.000` | `1.000` | `0.995` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `769.77` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.980` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `cargo-01` | `recall` | `cargo` | `711.47` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `cargo-02` | `recall` | `cargo` | `6641.80` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `688.37` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-04` | `summary` | `npm` | `2319.38` | `0.977` | `0.977` | `+0.000` | `1.000` | `0.942` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `741.91` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.988` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `1094.43` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.981` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-runtime-01` | `recall` | `python-runtime` | `827.92` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `1101.58` | `0.996` | `0.996` | `+0.000` | `1.000` | `0.990` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `940.50` | `0.981` | `0.654` | `+0.327` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `1933.75` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.983` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `729.96` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.968` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `747.39` | `0.982` | `0.982` | `+0.000` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `1676.13` | `0.839` | `0.989` | `-0.150` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `851.82` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.981` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `1194.89` | `0.986` | `0.986` | `+0.000` | `1.000` | `0.945` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `788.86` | `0.978` | `0.978` | `+0.000` | `1.000` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `2874.47` | `0.970` | `0.970` | `+0.000` | `1.000` | `0.925` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `839.09` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.982` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `2050.65` | `0.999` | `0.999` | `+0.000` | `1.000` | `0.996` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `822.76` | `0.998` | `0.998` | `+0.000` | `1.000` | `0.991` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `1769.34` | `0.997` | `0.997` | `+0.000` | `1.000` | `0.993` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `805.62` | `0.970` | `0.970` | `+0.000` | `1.000` | `0.925` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `1801.38` | `0.982` | `0.982` | `+0.000` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `881.27` | `0.970` | `0.970` | `+0.000` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `728.81` | `0.998` | `0.998` | `+0.000` | `1.000` | `0.990` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `757.68` | `0.986` | `0.986` | `+0.000` | `1.000` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `815.57` | `0.981` | `0.981` | `+0.000` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `1039.54` | `0.976` | `0.976` | `+0.000` | `1.000` | `0.940` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `802.02` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.979` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `996.64` | `0.968` | `0.968` | `+0.000` | `1.000` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `736.19` | `0.997` | `0.997` | `+0.000` | `1.000` | `0.987` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `1890.96` | `0.979` | `0.979` | `+0.000` | `1.000` | `0.946` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `2142.09` | `0.999` | `0.999` | `+0.000` | `1.000` | `0.995` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `776.13` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-log-01` | `recall` | `ci-log` | `2158.84` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `2360.25` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.981` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `2856.55` | `0.828` | `0.828` | `+0.000` | `0.929` | `0.981` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | test timed out after 10m0s | - |
| `build-log-01` | `summary` | `build-log` | `19635.68` | `0.957` | `0.957` | `+0.000` | `1.000` | `0.893` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `1709.19` | `0.982` | `0.982` | `+0.000` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `1078.93` | `0.754` | `0.754` | `+0.000` | `1.000` | `0.804` | `0.667` | `0.667` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `1078.42` | `0.951` | `0.951` | `+0.000` | `1.000` | `0.837` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `1520.81` | `0.692` | `0.692` | `+0.000` | `0.226` | `0.300` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | exit status 22, https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `1049.18` | `1.000` | `0.201` | `+0.799` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `2611.98` | `0.000` | `0.172` | `-0.172` | `1.000` | `0.684` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `soft_accepted` | structured_contract_breakage | - | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml failed_jobs: - job: test / integration step: Start docker compose exit_code: 1 cause: port 5432 is already allocated - job: deploy / preview step: Up...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml failed_jobs: - job: test / integration step: Start docker compose exit_code: 1 cause: port 5432 is already allocated - job: deploy / preview step: Up...' |
| `structured-output-03` | `structured` | `structured-output` | `1909.69` | `0.824` | `0.824` | `+0.000` | `0.929` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | "invalid refresh token" | - |
| `structured-output-04` | `structured` | `structured-output` | `1266.27` | `1.000` | `0.125` | `+0.875` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `17559.86` | `0.850` | `0.850` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `738.82` | `0.780` | `0.780` | `+0.000` | `1.000` | `0.858` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `807.47` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `1634.21` | `0.983` | `0.983` | `+0.000` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `868.84` | `0.941` | `0.941` | `+0.000` | `1.000` | `0.853` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `1228.76` | `0.715` | `0.715` | `+0.000` | `1.000` | `0.666` | `0.667` | `0.667` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `822.65` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `2351.95` | `0.986` | `0.986` | `+0.000` | `1.000` | `0.943` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `827.02` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `1487.46` | `0.984` | `0.984` | `+0.000` | `1.000` | `0.936` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `1015.30` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `728.90` | `0.986` | `0.986` | `+0.000` | `1.000` | `0.943` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `861.94` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `963.24` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `879.24` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `1915.87` | `0.806` | `0.806` | `+0.000` | `0.905` | `0.962` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | 20260518_add_workspace_limits.sql | - |
| `pnpm-04` | `recall` | `pnpm` | `949.14` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.980` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `2587.23` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `931.64` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `883.47` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `861.71` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.978` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `831.14` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.965` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `803.45` | `0.993` | `0.993` | `+0.000` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `819.73` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `2016.73` | `0.982` | `0.982` | `+0.000` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `868.45` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.968` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `746.26` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `1689.02` | `0.780` | `0.780` | `+0.000` | `0.783` | `0.929` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | tests/refunds | - |
| `go-test-03` | `summary` | `go-test` | `793.20` | `0.974` | `0.974` | `+0.000` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `1825.39` | `0.970` | `0.970` | `+0.000` | `1.000` | `0.925` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `778.66` | `0.972` | `0.972` | `+0.000` | `1.000` | `0.930` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `857.60` | `0.971` | `0.971` | `+0.000` | `1.000` | `0.928` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `1697.06` | `0.780` | `0.780` | `+0.000` | `0.826` | `0.902` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | checks | - |
| `composer-01` | `summary` | `composer` | `1778.60` | `0.974` | `0.974` | `+0.000` | `1.000` | `0.934` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `1531.23` | `0.979` | `0.979` | `+0.000` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `1728.98` | `0.967` | `0.967` | `+0.000` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `1776.65` | `0.972` | `0.972` | `+0.000` | `1.000` | `0.929` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `2182.11` | `0.971` | `0.971` | `+0.000` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `1625.21` | `0.973` | `0.973` | `-0.000` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `943.40` | `0.973` | `0.973` | `+0.000` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `2114.77` | `0.977` | `0.977` | `+0.000` | `1.000` | `0.943` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `974.15` | `0.984` | `0.984` | `+0.000` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `696.37` | `0.964` | `0.964` | `+0.000` | `1.000` | `0.879` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `755.62` | `0.956` | `0.956` | `+0.000` | `1.000` | `0.855` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `1594.02` | `0.450` | `0.450` | `+0.000` | `1.000` | `0.000` | `0.383` | `0.287` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `691.72` | `0.908` | `0.908` | `+0.000` | `1.000` | `0.694` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `683.40` | `0.962` | `0.962` | `+0.000` | `1.000` | `0.875` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `1728.12` | `0.874` | `0.874` | `+0.000` | `1.000` | `0.750` | `0.800` | `0.800` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `726.79` | `0.756` | `0.756` | `+0.000` | `1.000` | `0.608` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `694.50` | `0.926` | `0.926` | `+0.000` | `1.000` | `0.754` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `2252.62` | `0.977` | `0.977` | `+0.000` | `1.000` | `0.924` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `1476.78` | `0.644` | `0.644` | `+0.000` | `1.000` | `0.860` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `1458.70` | `0.643` | `0.643` | `+0.000` | `1.000` | `0.000` | `0.617` | `0.524` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `1649.97` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.667` | `0.725` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_lines_contract_breakage | - | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='``` worker-5b8c 0/1 CrashLoopBackOff 6 migrator-9z1q 0/1 Error 0 ```' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='``` worker-5b8c 0/1 CrashLoopBackOff 6 migrator-9z1q 0/1 Error 0 ```' |
| `cargo-04` | `instruction_following` | `cargo` | `1011.81` | `0.919` | `0.919` | `+0.000` | `1.000` | `0.729` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `2021.62` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.552` | `0.486` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) exit code 23' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) exit code 23' |
| `pyright-01` | `structured` | `pyright` | `1117.78` | `0.388` | `0.168` | `+0.219` | `1.000` | `0.188` | `0.375` | `0.375` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `977.32` | `0.839` | `0.184` | `+0.655` | `1.000` | `0.861` | `0.771` | `0.771` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `junit-01` | `structured` | `junit` | `1986.73` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.589` | `1.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```markdown | Test | Error | Location | |-------------------|---------------------------------------|----------------------| | CalculatorTest | java.lang.Ari...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```markdown | Test | Error | Location | |-------------------|---------------------------------------|----------------------| | CalculatorTest > dividesByZero...' |
| `kubernetes-03` | `structured` | `kubernetes` | `838.39` | `0.389` | `0.151` | `+0.237` | `1.000` | `0.323` | `0.333` | `0.333` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `1971.10` | `0.132` | `0.125` | `+0.007` | `1.000` | `0.194` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `1334.88` | `0.881` | `0.185` | `+0.696` | `1.000` | `0.798` | `0.875` | `0.875` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `886.89` | `0.389` | `0.164` | `+0.225` | `1.000` | `0.326` | `0.333` | `0.333` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `792.98` | `0.975` | `0.975` | `+0.000` | `1.000` | `1.000` | `1.000` | `0.925` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `774.88` | `0.781` | `0.126` | `+0.655` | `1.000` | `0.601` | `0.800` | `0.800` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `1007.32` | `0.952` | `0.809` | `+0.143` | `1.000` | `0.902` | `1.000` | `0.945` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `772.77` | `0.644` | `0.142` | `+0.501` | `1.000` | `0.509` | `0.625` | `0.625` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `playwright-02` | `structured` | `playwright` | `787.20` | `0.361` | `0.138` | `+0.223` | `1.000` | `0.182` | `0.338` | `0.338` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `2371.51` | `0.000` | `0.155` | `-0.155` | `1.000` | `0.518` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `soft_accepted` | structured_contract_breakage | - | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml errors: - file: migrations/004.sql line: 12 message: column "tenant_id" contains null values - file: migrations/004.sql line: 20 message: current tra...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml errors: - file: migrations/004.sql line: 12 message: column "tenant_id" contains null values - file: migrations/004.sql line: 20 message: current tra...' |
| `vite-01` | `structured` | `vite` | `1269.21` | `0.110` | `0.096` | `+0.013` | `1.000` | `0.194` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `1465.63` | `0.850` | `0.850` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `git-04` | `exact_format` | `git` | `737.94` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `706.17` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `957.32` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `1830.17` | `0.204` | `0.204` | `+0.000` | `0.286` | `0.309` | `0.306` | `0.306` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | github.com/acme/shop/checkout | - |
| `kubectl-09` | `exact_format` | `kubectl` | `723.13` | `0.355` | `0.355` | `+0.000` | `1.000` | `0.305` | `0.350` | `0.350` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `691.93` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `643.16` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `1421.60` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `2026.42` | `0.963` | `0.963` | `+0.000` | `1.000` | `0.909` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `1811.83` | `0.970` | `0.970` | `+0.000` | `1.000` | `0.925` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `1130.75` | `0.894` | `0.894` | `+0.000` | `1.000` | `0.647` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `1584.54` | `0.975` | `0.975` | `+0.000` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `838.50` | `0.971` | `0.971` | `+0.000` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `1908.45` | `0.904` | `0.904` | `+0.000` | `1.000` | `0.761` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `1475.32` | `0.947` | `0.947` | `+0.000` | `1.000` | `0.868` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `747.21` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `808.50` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `742.62` | `0.987` | `0.987` | `+0.000` | `1.000` | `0.946` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `775.19` | `0.980` | `0.980` | `+0.000` | `1.000` | `0.922` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `7654.87` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `634.80` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.962` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `726.75` | `0.986` | `0.986` | `+0.000` | `1.000` | `0.945` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `838.64` | `0.976` | `0.976` | `+0.000` | `1.000` | `0.904` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `650.34` | `0.981` | `0.981` | `+0.000` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `932.85` | `0.976` | `0.976` | `+0.000` | `1.000` | `0.904` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `725.97` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `1068.91` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `576.19` | `0.975` | `0.975` | `+0.000` | `1.000` | `0.900` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `667.19` | `0.984` | `0.984` | `+0.000` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `837.92` | `0.969` | `0.969` | `+0.000` | `1.000` | `0.875` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `729.15` | `0.977` | `0.977` | `+0.000` | `1.000` | `0.907` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `651.87` | `0.970` | `0.970` | `+0.000` | `1.000` | `0.881` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `650.22` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.981` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `790.38` | `0.979` | `0.979` | `+0.000` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `729.62` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `908.05` | `0.988` | `0.988` | `+0.000` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `1545.76` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `2415.56` | `0.839` | `0.839` | `+0.000` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `711.87` | `0.979` | `0.979` | `+0.000` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `706.00` | `0.969` | `0.969` | `+0.000` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `1441.81` | `0.945` | `0.945` | `+0.000` | `1.000` | `0.862` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `644.67` | `0.926` | `0.926` | `+0.000` | `1.000` | `0.953` | `1.000` | `0.925` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `597.70` | `0.953` | `0.953` | `+0.000` | `1.000` | `0.884` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `1750.24` | `0.984` | `0.984` | `+0.000` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `1422.52` | `0.948` | `0.948` | `+0.000` | `1.000` | `0.871` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `1902.49` | `0.973` | `0.973` | `+0.000` | `1.000` | `0.909` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `880.62` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `1459.24` | `0.479` | `0.641` | `-0.162` | `1.000` | `0.846` | `0.500` | `0.400` | `0.000` | `0.000` | `soft_accepted` | `accepted` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `1086.94` | `0.870` | `0.179` | `+0.691` | `1.000` | `0.839` | `0.833` | `0.833` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `1078.47` | `0.404` | `0.197` | `+0.207` | `1.000` | `0.325` | `0.354` | `0.354` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `1553.27` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```markdown | InstanceId | State | |------------|---------| | i-12345 | running | ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```markdown | InstanceId | State | |------------|---------| | i-12345 | running | ```' |
| `network-01` | `exact_format` | `network` | `1613.81` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `703.55` | `0.729` | `0.729` | `+0.000` | `1.000` | `0.319` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `732.15` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `592.19` | `0.191` | `0.191` | `+0.000` | `1.000` | `0.320` | `0.150` | `0.150` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `1629.19` | `0.640` | `0.640` | `+0.000` | `1.000` | `0.250` | `0.688` | `0.688` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `build-05` | `exact_format` | `build` | `663.91` | `0.730` | `0.730` | `+0.000` | `1.000` | `0.333` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `666.92` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `1419.06` | `0.949` | `0.949` | `+0.000` | `1.000` | `0.872` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `1700.92` | `0.956` | `0.956` | `+0.000` | `1.000` | `0.891` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `1768.56` | `0.953` | `0.953` | `+0.000` | `1.000` | `0.883` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `11322.26` | `0.940` | `0.940` | `+0.000` | `1.000` | `0.911` | `1.000` | `0.967` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `1754.17` | `0.963` | `0.963` | `+0.000` | `1.000` | `0.907` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `1568.30` | `0.979` | `0.979` | `+0.000` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `1773.03` | `0.944` | `0.944` | `+0.000` | `1.000` | `0.860` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `758.70` | `0.965` | `0.965` | `+0.000` | `1.000` | `0.912` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `2295.20` | `0.967` | `0.967` | `+0.000` | `1.000` | `0.918` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `1833.57` | `0.959` | `0.959` | `+0.000` | `1.000` | `0.899` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `1476.43` | `0.950` | `0.950` | `+0.000` | `1.000` | `0.875` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `966.06` | `0.854` | `0.854` | `+0.000` | `1.000` | `0.886` | `1.000` | `0.861` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `1473.08` | `0.822` | `0.822` | `+0.000` | `1.000` | `0.823` | `1.000` | `0.850` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `1647.56` | `0.954` | `0.954` | `+0.000` | `1.000` | `0.885` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `775.96` | `0.894` | `0.894` | `+0.000` | `1.000` | `0.871` | `1.000` | `0.925` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `1474.28` | `0.955` | `0.955` | `+0.000` | `1.000` | `0.886` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `667.56` | `0.950` | `0.950` | `+0.000` | `1.000` | `0.875` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `879.49` | `0.904` | `0.904` | `+0.000` | `1.000` | `0.897` | `1.000` | `0.925` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `851.87` | `0.941` | `0.941` | `+0.000` | `1.000` | `0.889` | `1.000` | `0.980` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `757.14` | `0.404` | `0.197` | `+0.207` | `1.000` | `0.325` | `0.354` | `0.354` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `739.95` | `1.000` | `0.850` | `+0.150` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `646.31` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `819.86` | `0.729` | `0.729` | `+0.000` | `1.000` | `0.319` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `632.94` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `1443.57` | `0.640` | `0.640` | `+0.000` | `1.000` | `0.250` | `0.688` | `0.688` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `runtime-07` | `exact_format` | `runtime` | `591.29` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `995.84` | `0.191` | `0.191` | `+0.000` | `1.000` | `0.319` | `0.150` | `0.150` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `1347.09` | `0.448` | `0.448` | `+0.000` | `0.000` | `0.960` | `0.617` | `0.617` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | HOME | - |
| `deployment-05` | `explanation` | `deployment` | `1752.72` | `0.947` | `0.947` | `+0.000` | `1.000` | `0.906` | `1.000` | `0.979` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `1600.79` | `0.949` | `0.949` | `+0.000` | `1.000` | `0.874` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `1286.90` | `0.968` | `0.968` | `+0.000` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `2177.45` | `0.967` | `0.967` | `+0.000` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `1507.66` | `0.880` | `0.880` | `+0.000` | `1.000` | `0.857` | `1.000` | `0.914` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `1038.77` | `0.916` | `0.916` | `+0.000` | `1.000` | `0.920` | `1.000` | `0.929` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `1288.21` | `0.930` | `0.930` | `+0.000` | `1.000` | `0.825` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `2144.50` | `0.894` | `0.894` | `+0.000` | `1.000` | `0.891` | `1.000` | `0.914` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1663.53` | `0.933` | `0.933` | `+0.000` | `1.000` | `0.875` | `1.000` | `0.977` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
