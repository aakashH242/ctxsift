# gpu-qwen3.5-0.8b

## Scenario

- track: `gpu`
- phase: `gpu-screen`
- model: `Qwen/Qwen3.5-0.8B`
- quantization: `none`
- device: `cuda`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `34875.59`
- cpu_rss_bytes: `7246749696`
- gpu_peak_bytes: `2777570816`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- recovered_final_score: `59.13`
- raw_final_score: `32.43`
- recovery_lift: `+26.71`
- case_count: `280`
- success_count: `266`
- accepted_count: `201`
- soft_accepted_count: `65`
- rejected_count: `14`
- exact_pass_count: `223`
- avg_inference_ms: `3428.68`
- p95_inference_ms: `9695.35`
- avg_exact_preservation_ratio: `0.921`
- avg_summary_quality_ratio: `0.813`
- avg_format_adherence_score: `0.830`
- avg_instruction_following_score: `0.798`
- avg_brevity_ratio: `0.892`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.766`
- p10_case_score: `0.143`
- quality_core: `0.641`
- latency_factor: `0.922`
- final_score: `59.13`
- peak_cpu_rss_bytes: `7247835136`
- peak_gpu_bytes: `2986727424`

### Raw View

- accepted_count: `1`
- soft_accepted_count: `197`
- rejected_count: `82`
- exact_pass_count: `223`
- avg_exact_preservation_ratio: `0.921`
- avg_summary_quality_ratio: `0.799`
- avg_format_adherence_score: `0.464`
- avg_instruction_following_score: `0.344`
- avg_brevity_ratio: `0.876`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.439`
- p10_case_score: `0.000`
- quality_core: `0.352`
- final_score: `32.43`

## Cases

| case_id | family | domain | ms | recovered_score | raw_score | lift | preserve | quality | format | instruction | recovered_thought_density | raw_thought_density | recovered_validation | raw_validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `10370.69` | `0.586` | `0.584` | `+0.002` | `1.000` | `0.900` | `0.500` | `0.404` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-02` | `summary` | `python` | `9101.91` | `0.613` | `0.611` | `+0.002` | `1.000` | `0.936` | `0.500` | `0.459` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-03` | `recall` | `python` | `1384.34` | `0.989` | `0.660` | `+0.328` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-04` | `recall` | `python` | `1825.56` | `0.989` | `0.661` | `+0.328` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-05` | `recall` | `python` | `1708.50` | `0.993` | `0.664` | `+0.329` | `1.000` | `0.971` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `1812.14` | `0.992` | `0.662` | `+0.330` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `1571.68` | `0.626` | `0.476` | `+0.151` | `0.093` | `0.909` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | pytest tests/integration -k billing -vv --maxfail=1, tests/integration/test_billing_api.py::test_invoice_webhook_uses_signature, /workspace/tests/integration/test_billing_api.py:73, 1 error in 2.31s | - |
| `pytest-03` | `recall` | `pytest` | `2074.74` | `0.991` | `0.662` | `+0.329` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `1862.86` | `0.994` | `0.665` | `+0.329` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `1668.61` | `0.987` | `0.658` | `+0.329` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `2004.60` | `0.991` | `0.662` | `+0.329` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `1593.46` | `0.979` | `0.650` | `+0.329` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `3250.05` | `0.991` | `0.662` | `+0.329` | `1.000` | `0.965` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ruff-01` | `recall` | `ruff` | `5213.53` | `0.867` | `0.578` | `+0.289` | `0.911` | `0.932` | `1.000` | `0.864` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `1298.28` | `0.990` | `0.661` | `+0.329` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `1379.07` | `0.983` | `0.654` | `+0.330` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `3397.46` | `0.985` | `0.000` | `+0.985` | `1.000` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `2237.16` | `0.982` | `0.653` | `+0.329` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `1717.13` | `0.984` | `0.655` | `+0.329` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `black-01` | `summary` | `black` | `1546.87` | `0.989` | `0.660` | `+0.329` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `black-02` | `summary` | `black` | `1480.51` | `0.978` | `0.653` | `+0.326` | `1.000` | `0.946` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `black-03` | `recall` | `black` | `1140.67` | `0.992` | `0.663` | `+0.329` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `2522.65` | `0.978` | `0.651` | `+0.327` | `1.000` | `0.912` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `12900.29` | `0.834` | `0.559` | `+0.275` | `1.000` | `0.926` | `1.000` | `0.811` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `3851.05` | `0.783` | `0.611` | `+0.172` | `0.800` | `0.928` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Lifecycle script `build` failed, storefront@2.8.1 | - |
| `pnpm-01` | `recall` | `pnpm` | `4561.33` | `0.802` | `0.627` | `+0.175` | `0.895` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | --no-frozen-lockfile | - |
| `pnpm-02` | `summary` | `pnpm` | `8844.19` | `0.984` | `0.658` | `+0.327` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `2020.97` | `0.986` | `0.657` | `+0.329` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `2735.69` | `0.983` | `0.655` | `+0.328` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `2005.97` | `0.993` | `0.663` | `+0.330` | `1.000` | `0.971` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `13587.95` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.936` | `0.500` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | unterminated_reasoning_block | - | qwen3.5 output validation failed: model did not stop thinking before reaching the output limit. first_pass="- tsc src/index.ts src/http.ts --pretty false - src/index.ts(48,20): error TS2769: No overload matches this call. Overload 1 of 2, '(url: string, init?: Requ..." repair_pass="- tsc src/index.ts src/http.ts --pretty false - src/index.ts(48,20): error TS2769: No overload matches this call. Overload 1 of 2, '(url: string, init?: Requ..." |
| `eslint-01` | `recall` | `eslint` | `6604.77` | `0.805` | `0.627` | `+0.178` | `0.920` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Unused eslint-disable directive | - |
| `eslint-02` | `summary` | `eslint` | `1542.24` | `0.980` | `0.653` | `+0.327` | `1.000` | `0.951` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `2687.65` | `0.985` | `0.657` | `+0.328` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `14841.34` | `0.838` | `0.568` | `+0.271` | `1.000` | `0.889` | `1.000` | `0.760` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `936.22` | `0.984` | `0.655` | `+0.329` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `2023.78` | `0.977` | `0.650` | `+0.328` | `1.000` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `741.77` | `0.975` | `0.649` | `+0.326` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `1442.86` | `0.987` | `0.658` | `+0.329` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `5550.01` | `0.964` | `0.638` | `+0.326` | `1.000` | `0.928` | `1.000` | `0.990` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `1543.25` | `0.975` | `0.650` | `+0.325` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `2931.55` | `0.991` | `0.659` | `+0.332` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `1309.74` | `0.995` | `0.664` | `+0.331` | `1.000` | `0.988` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `13572.27` | `0.585` | `0.000` | `+0.585` | `1.000` | `0.920` | `0.500` | `0.396` | `0.000` | `0.000` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `terraform-01` | `summary` | `terraform` | `1367.50` | `0.984` | `0.651` | `+0.333` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `4944.73` | `0.945` | `0.630` | `+0.315` | `1.000` | `0.937` | `1.000` | `0.931` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `2192.87` | `0.989` | `0.661` | `+0.328` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `1782.22` | `0.984` | `0.655` | `+0.329` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `4412.21` | `0.937` | `0.628` | `+0.310` | `1.000` | `0.931` | `1.000` | `0.921` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `2731.96` | `0.785` | `0.613` | `+0.172` | `0.811` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Error 2 | - |
| `git-01` | `recall` | `git` | `17639.45` | `0.592` | `0.591` | `+0.001` | `1.000` | `0.906` | `0.500` | `0.411` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `git-02` | `recall` | `git` | `7162.46` | `0.864` | `0.582` | `+0.282` | `1.000` | `0.867` | `1.000` | `0.816` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `git-03` | `recall` | `git` | `1404.91` | `0.989` | `0.658` | `+0.331` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `2196.96` | `0.990` | `0.661` | `+0.329` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `curl-02` | `recall` | `curl` | `2125.15` | `0.989` | `0.661` | `+0.328` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ssh-01` | `summary` | `ssh` | `1762.62` | `0.701` | `0.535` | `+0.166` | `0.476` | `0.888` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | GIT_SSH_COMMAND="ssh -o IdentitiesOnly=yes -i ~/.ssh/deploy_key" git ls-remote git@github.com:example/mono-app.git, git@github.com:example/mono-app.git | - |
| `ssh-02` | `summary` | `ssh` | `1251.21` | `0.980` | `0.647` | `+0.332` | `1.000` | `0.949` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `2122.47` | `0.659` | `0.511` | `+0.148` | `0.355` | `0.840` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | /opt/app/bin/worker.sh, status=203/EXEC | - |
| `systemd-02` | `summary` | `systemd` | `887.60` | `0.962` | `0.638` | `+0.324` | `1.000` | `0.904` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `1299.45` | `0.977` | `0.648` | `+0.329` | `1.000` | `0.942` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `6901.06` | `0.911` | `0.612` | `+0.298` | `1.000` | `0.951` | `1.000` | `0.864` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `5685.66` | `0.770` | `0.598` | `+0.171` | `0.750` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | example.com/mono-app/pkg/server | - |
| `go-test-01` | `summary` | `go-test` | `1949.16` | `0.742` | `0.577` | `+0.165` | `0.600` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | go test ./... -run TestCacheTTL -count=1 | - |
| `javac-01` | `recall` | `javac` | `25216.01` | `0.984` | `0.655` | `+0.329` | `1.000` | `0.934` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `maven-01` | `recall` | `maven` | `4123.07` | `0.566` | `0.421` | `+0.145` | `0.304` | `0.915` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | mvn -q test, UserControllerTest.java:72, maven-surefire-plugin:3.5.5:test | - |
| `maven-02` | `summary` | `maven` | `1557.10` | `0.990` | `0.659` | `+0.331` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `1581.58` | `0.987` | `0.658` | `+0.329` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `1730.66` | `0.696` | `0.534` | `+0.162` | `0.389` | `0.930` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ./gradlew test, Execution failed for task ':test' | - |
| `cargo-01` | `recall` | `cargo` | `7016.06` | `0.983` | `0.657` | `+0.327` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `cargo-02` | `recall` | `cargo` | `3065.31` | `0.984` | `0.657` | `+0.327` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `53753.77` | `0.423` | `0.423` | `-0.000` | `0.526` | `0.927` | `0.500` | `0.381` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | node dist/server.js, MODULE_NOT_FOUND | - |
| `npm-04` | `summary` | `npm` | `1524.46` | `0.974` | `0.645` | `+0.329` | `1.000` | `0.934` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `3753.16` | `0.976` | `0.640` | `+0.337` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `1485.43` | `0.989` | `0.660` | `+0.330` | `1.000` | `0.973` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-runtime-01` | `recall` | `python-runtime` | `7613.82` | `0.609` | `0.608` | `+0.001` | `1.000` | `0.939` | `0.500` | `0.428` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `pytest-06` | `summary` | `pytest` | `2811.46` | `0.986` | `0.658` | `+0.327` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `3921.38` | `0.969` | `0.637` | `+0.333` | `1.000` | `0.939` | `1.000` | `0.992` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `3518.60` | `0.801` | `0.625` | `+0.175` | `0.911` | `0.910` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | zod@3.23.8 | - |
| `docker-compose-04` | `summary` | `docker-compose` | `1250.86` | `0.982` | `0.651` | `+0.331` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `1885.02` | `0.969` | `0.645` | `+0.324` | `1.000` | `0.924` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `2590.25` | `0.827` | `0.644` | `+0.184` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `2039.56` | `0.990` | `0.662` | `+0.328` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `4891.36` | `0.993` | `0.661` | `+0.332` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `3194.10` | `0.975` | `0.647` | `+0.328` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `1833.06` | `0.978` | `0.649` | `+0.330` | `1.000` | `0.946` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `1483.14` | `0.992` | `0.663` | `+0.329` | `1.000` | `0.979` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `3779.76` | `0.974` | `0.649` | `+0.325` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `2862.36` | `0.684` | `0.524` | `+0.160` | `0.600` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | psql -h 127.0.0.1 -U app_user -d appdb -c 'select 1' | - |
| `postgres-02` | `summary` | `postgres` | `7777.96` | `0.963` | `0.641` | `+0.322` | `1.000` | `0.908` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `2076.81` | `0.989` | `0.658` | `+0.330` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `2169.15` | `0.732` | `0.566` | `+0.166` | `0.667` | `0.861` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | mysql -h db.example.net -u app -D appdb -e "SELECT id, createdAt FROM users LIMIT 5" | - |
| `redis-01` | `summary` | `redis` | `1784.41` | `0.986` | `0.654` | `+0.332` | `1.000` | `0.965` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `1300.82` | `0.989` | `0.660` | `+0.329` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `2891.36` | `0.678` | `0.520` | `+0.159` | `0.619` | `0.878` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | line=91, Ruff F821 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `1979.36` | `0.730` | `0.560` | `+0.170` | `0.579` | `0.911` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | pnpm install --frozen-lockfile, react-dom@18.3.1 | - |
| `jenkins-01` | `summary` | `jenkins` | `850.36` | `0.967` | `0.642` | `+0.325` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `make-01` | `summary` | `make` | `1542.57` | `0.980` | `0.651` | `+0.329` | `1.000` | `0.949` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `3078.70` | `0.984` | `0.657` | `+0.327` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `1314.53` | `0.992` | `0.658` | `+0.334` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `1495.35` | `0.981` | `0.653` | `+0.328` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `1925.26` | `0.990` | `0.662` | `+0.328` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `29405.60` | `0.540` | `0.537` | `+0.002` | `0.851` | `0.904` | `0.500` | `0.405` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | src/router.rs:128 | - |
| `ci-log-01` | `recall` | `ci-log` | `8804.59` | `0.945` | `0.630` | `+0.315` | `1.000` | `0.927` | `1.000` | `0.936` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `14170.96` | `0.859` | `0.583` | `+0.276` | `1.000` | `0.952` | `1.000` | `0.771` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `4071.04` | `0.686` | `0.525` | `+0.161` | `0.321` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | github.com/acme/shop/checkout, checkout_test.go:71, total = 42.00, want 37.00, github.com/acme/shop/inventory, test timed out after 10m0s | - |
| `build-log-01` | `summary` | `build-log` | `1787.98` | `0.961` | `0.640` | `+0.321` | `1.000` | `0.902` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `931.58` | `0.581` | `0.493` | `+0.088` | `1.000` | `0.935` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `10288.89` | `0.000` | `0.000` | `+0.000` | `0.625` | `0.228` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | @typescript-eslint/no-misused-promises, @typescript-eslint/no-explicit-any, @typescript-eslint/no-unsafe-assignment | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass="- /repo/web/src/App.tsx 12:7 warning 'debugMode' is assigned a value but never used 27:19 error Promise returned in function argument where a void return was..." repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass="- /repo/web/src/App.tsx 12:7 warning 'debugMode' is assigned a value but never used 27:19 error Promise returned in function argument where a void return was..." |
| `git-review-01` | `instruction_following` | `git-review` | `6125.74` | `0.495` | `0.000` | `+0.495` | `1.000` | `0.657` | `0.375` | `0.375` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `1783.77` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.334` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='- exit status 22' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='- exit status 22 - search endpoint failed after 2 attempts - https://staging.example.com/api/search?q=smoke - curl: (22)' |
| `structured-output-01` | `structured` | `structured-output` | `5472.28` | `0.279` | `0.000` | `+0.279` | `0.611` | `0.188` | `0.375` | `0.375` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | /work/app/api/routes.py, 21 | - |
| `structured-output-02` | `structured` | `structured-output` | `6823.79` | `0.175` | `0.000` | `+0.175` | `0.905` | `0.851` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | port 5432 is already allocated | - |
| `structured-output-03` | `structured` | `structured-output` | `4839.28` | `0.143` | `0.000` | `+0.143` | `0.857` | `0.497` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | "refresh token expired", "invalid refresh token" | - |
| `structured-output-04` | `structured` | `structured-output` | `5784.90` | `0.108` | `0.000` | `+0.108` | `1.000` | `0.194` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `4203.76` | `0.453` | `0.000` | `+0.453` | `1.000` | `0.000` | `0.494` | `0.376` | `0.000` | `0.000` | `soft_accepted` | `rejected` | verbatim_alignment_weak | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `1366.28` | `0.568` | `0.000` | `+0.568` | `1.000` | `0.331` | `0.576` | `0.576` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `2661.58` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `795.07` | `0.965` | `0.645` | `+0.321` | `1.000` | `0.914` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `3359.86` | `0.759` | `0.589` | `+0.170` | `0.750` | `0.889` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `5682.98` | `0.716` | `0.000` | `+0.716` | `1.000` | `0.704` | `0.667` | `0.651` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `6996.98` | `0.800` | `0.626` | `+0.175` | `0.905` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | app.tasks.email.send_welcome_email | - |
| `mypy-05` | `recall` | `mypy` | `4069.80` | `0.682` | `0.521` | `+0.161` | `0.600` | `0.929` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | include_meta, -> bytes, -> str | - |
| `terraform-08` | `recall` | `terraform` | `2750.98` | `0.984` | `0.658` | `+0.326` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `4772.40` | `0.981` | `0.654` | `+0.327` | `1.000` | `0.924` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `7011.48` | `0.945` | `0.631` | `+0.314` | `1.000` | `0.919` | `1.000` | `0.940` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `1817.34` | `0.983` | `0.657` | `+0.326` | `1.000` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `5700.15` | `0.988` | `0.660` | `+0.328` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `1608.84` | `0.987` | `0.657` | `+0.331` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `4923.32` | `0.988` | `0.658` | `+0.330` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `26456.49` | `0.711` | `0.549` | `+0.163` | `0.667` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | 20260518_add_workspace_limits.sql, packages/db/test/migrate.test.ts:44:7 | - |
| `pnpm-04` | `recall` | `pnpm` | `2684.45` | `0.988` | `0.658` | `+0.330` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `1524.19` | `0.988` | `0.662` | `+0.326` | `1.000` | `0.951` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `1667.85` | `0.983` | `0.658` | `+0.325` | `1.000` | `0.931` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `2898.10` | `0.984` | `0.654` | `+0.330` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `2587.75` | `0.992` | `0.661` | `+0.330` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `2777.99` | `0.982` | `0.655` | `+0.327` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `1462.38` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `3368.05` | `0.984` | `0.657` | `+0.327` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `3833.16` | `0.981` | `0.655` | `+0.326` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `1934.32` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `3631.17` | `0.944` | `0.631` | `+0.313` | `1.000` | `0.931` | `1.000` | `0.932` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `2020.59` | `0.969` | `0.646` | `+0.323` | `1.000` | `0.922` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `5685.40` | `0.760` | `0.590` | `+0.170` | `0.684` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ./integration | - |
| `npm-05` | `summary` | `npm` | `2109.86` | `0.711` | `0.547` | `+0.164` | `0.533` | `0.882` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | web@1.2.0, src/pages/admin.tsx | - |
| `helm-01` | `summary` | `helm` | `1523.00` | `0.956` | `0.637` | `+0.319` | `1.000` | `0.891` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `2617.61` | `0.780` | `0.606` | `+0.174` | `0.895` | `0.860` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | typing.Optional | - |
| `k6-01` | `summary` | `k6` | `6071.22` | `0.739` | `0.574` | `+0.165` | `0.652` | `0.892` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | checks, http_req_duration | - |
| `composer-01` | `summary` | `composer` | `6171.92` | `0.939` | `0.625` | `+0.313` | `1.000` | `0.941` | `1.000` | `0.949` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `1584.00` | `0.584` | `0.436` | `+0.148` | `0.000` | `0.844` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | xcodebuild, -scheme, MobileApp, -configuration, Release | - |
| `make-02` | `summary` | `make` | `3656.65` | `0.803` | `0.628` | `+0.175` | `0.909` | `0.918` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | -Iinclude | - |
| `python-pytest-02` | `summary` | `python-pytest` | `2669.44` | `0.688` | `0.528` | `+0.160` | `0.385` | `0.908` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | auto, Not, properly, terminated | - |
| `jest-01` | `summary` | `jest` | `2741.67` | `0.951` | `0.641` | `+0.311` | `1.000` | `0.878` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `3126.13` | `0.788` | `0.613` | `+0.175` | `0.833` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `4009.06` | `0.781` | `0.607` | `+0.174` | `0.814` | `0.914` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | FAILED | - |
| `wrangler-01` | `summary` | `wrangler` | `1863.13` | `0.946` | `0.627` | `+0.319` | `1.000` | `0.864` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `3466.01` | `0.974` | `0.648` | `+0.325` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `10215.86` | `0.290` | `0.000` | `+0.290` | `0.926` | `0.629` | `0.200` | `0.200` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | prefer-const | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `2154.96` | `0.603` | `0.000` | `+0.603` | `1.000` | `0.696` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `1640.47` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `0.617` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_lines_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- tests/test_api.py::test_create_user - tests/test_auth.py::test_refresh_token_expiry' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- tests/test_api.py::test_create_user - tests/test_auth.py::test_refresh_token_expiry' |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `2468.20` | `0.665` | `0.000` | `+0.665` | `1.000` | `0.673` | `0.667` | `0.581` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `1116.28` | `0.976` | `0.000` | `+0.976` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `4486.05` | `0.596` | `0.000` | `+0.596` | `1.000` | `0.385` | `0.533` | `0.411` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `1892.20` | `0.256` | `0.000` | `+0.256` | `0.450` | `0.325` | `0.371` | `0.349` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | [deps 4/4], pnpm install --frozen-lockfile | - |
| `terraform-09` | `instruction_following` | `terraform` | `1057.25` | `0.599` | `0.000` | `+0.599` | `1.000` | `0.680` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `5356.23` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.856` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- /repo/src/main/java/App.java:[12,8] unchecked conversion - /repo/src/main/java/UserService.java:[44,17] cannot find symbol symbol: method findByEmail(java....' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- /repo/src/main/java/App.java:[12,8] unchecked conversion - /repo/src/main/java/UserService.java:[44,17] cannot find symbol symbol: method findByEmail(java....' |
| `playwright-01` | `instruction_following` | `playwright` | `1727.90` | `0.644` | `0.000` | `+0.644` | `1.000` | `0.860` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `1533.50` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.000` | `0.380` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_lines_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- src/App.tsx - src/api/client.ts - README.md is formatted' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- src/App.tsx - src/api/client.ts - README.md is formatted' |
| `kubectl-08` | `instruction_following` | `kubectl` | `1965.06` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.000` | `0.475` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_lines_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- worker-5b8c - CrashLoopBackOff - migrator-9z1q - Error' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='worker-5b8c - CrashLoopBackOff - migrator-9z1q - Error' |
| `cargo-04` | `instruction_following` | `cargo` | `2763.23` | `0.468` | `0.000` | `+0.468` | `1.000` | `0.685` | `0.333` | `0.333` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `2481.91` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.594` | `0.350` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) backup.sh failed with exit code 23' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) backup.sh failed with exit code 23' |
| `pyright-01` | `structured` | `pyright` | `4133.05` | `0.335` | `0.000` | `+0.335` | `1.000` | `0.183` | `0.300` | `0.300` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `4891.34` | `0.088` | `0.000` | `+0.088` | `0.667` | `0.182` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | resource, field | - |
| `junit-01` | `structured` | `junit` | `6300.35` | `0.101` | `0.000` | `+0.101` | `0.857` | `0.188` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | CalculatorTest | - |
| `kubernetes-03` | `structured` | `kubernetes` | `1951.24` | `0.143` | `0.000` | `+0.143` | `1.000` | `0.190` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `7490.49` | `0.070` | `0.000` | `+0.070` | `0.667` | `0.179` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | line, column, rule | - |
| `docker-build-04` | `structured` | `docker-build` | `2484.57` | `0.713` | `0.000` | `+0.713` | `1.000` | `0.606` | `0.800` | `0.659` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `1527.58` | `0.142` | `0.000` | `+0.142` | `1.000` | `0.187` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `2690.51` | `0.827` | `0.000` | `+0.827` | `1.000` | `0.633` | `1.000` | `0.812` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `npm-07` | `structured` | `npm` | `3871.39` | `0.084` | `0.000` | `+0.084` | `0.667` | `0.229` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | package, required | - |
| `mypy-06` | `structured` | `mypy` | `25159.62` | `0.124` | `0.124` | `+0.000` | `1.000` | `0.344` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `2810.81` | `0.064` | `0.000` | `+0.064` | `0.242` | `0.177` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | failed, task, :api:compileJava, cause | - |
| `playwright-02` | `structured` | `playwright` | `7500.17` | `0.149` | `0.000` | `+0.149` | `0.167` | `0.172` | `0.225` | `0.225` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | project, chromium, file, line, test | - |
| `postgres-04` | `structured` | `postgres` | `1694.08` | `0.142` | `0.000` | `+0.142` | `1.000` | `0.181` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `vite-01` | `structured` | `vite` | `4131.88` | `0.104` | `0.000` | `+0.104` | `1.000` | `0.183` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `1311.65` | `0.414` | `0.000` | `+0.414` | `1.000` | `0.000` | `0.333` | `0.250` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `git-04` | `exact_format` | `git` | `4035.36` | `0.216` | `0.000` | `+0.216` | `1.000` | `0.279` | `0.237` | `0.171` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `9893.16` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `678.77` | `0.221` | `0.000` | `+0.221` | `1.000` | `0.294` | `0.233` | `0.181` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `1008.45` | `0.403` | `0.000` | `+0.403` | `1.000` | `0.335` | `0.400` | `0.400` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `2211.32` | `0.204` | `0.000` | `+0.204` | `0.500` | `0.298` | `0.277` | `0.277` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | prod | - |
| `cargo-05` | `exact_format` | `cargo` | `899.17` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `341.89` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `1825.45` | `0.063` | `0.000` | `+0.063` | `0.000` | `0.248` | `0.150` | `0.110` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | 20260518133742 | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `3293.73` | `0.647` | `0.648` | `-0.001` | `1.000` | `0.924` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `3238.46` | `0.956` | `0.639` | `+0.317` | `1.000` | `0.890` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `3544.49` | `0.717` | `0.000` | `+0.717` | `1.000` | `0.673` | `0.667` | `0.667` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `1205.84` | `0.967` | `0.642` | `+0.325` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `849.59` | `0.963` | `0.640` | `+0.324` | `1.000` | `0.908` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `1048.47` | `0.725` | `0.567` | `+0.158` | `0.750` | `0.788` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | returns a reference | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `3158.15` | `0.710` | `0.548` | `+0.161` | `0.583` | `0.848` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `884.62` | `0.989` | `0.662` | `+0.328` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `988.00` | `0.987` | `0.657` | `+0.330` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `1103.77` | `0.991` | `0.662` | `+0.329` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `2491.33` | `0.977` | `0.651` | `+0.326` | `1.000` | `0.908` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `2246.67` | `0.719` | `0.551` | `+0.168` | `0.667` | `0.983` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `1290.47` | `0.983` | `0.655` | `+0.328` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `2835.05` | `0.952` | `0.634` | `+0.318` | `1.000` | `0.923` | `1.000` | `0.950` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `2003.91` | `0.705` | `0.544` | `+0.162` | `0.714` | `0.832` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | 5 tests run, 1 failure | - |
| `testing-03` | `recall` | `testing` | `2165.65` | `0.980` | `0.652` | `+0.328` | `1.000` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `2297.92` | `0.937` | `0.622` | `+0.314` | `1.000` | `0.892` | `1.000` | `0.937` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `27560.27` | `0.752` | `0.581` | `+0.170` | `0.778` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | "ami" is required | - |
| `compilation-02` | `recall` | `compilation` | `1750.33` | `0.990` | `0.662` | `+0.328` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `2020.83` | `0.966` | `0.644` | `+0.322` | `1.000` | `0.864` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `build-01` | `recall` | `build` | `3592.43` | `0.560` | `0.418` | `+0.142` | `0.412` | `0.858` | `1.000` | `0.918` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Execution failed for task ':test' | - |
| `container-runtime-01` | `recall` | `container-runtime` | `1783.30` | `0.974` | `0.648` | `+0.326` | `1.000` | `0.895` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `1828.98` | `0.972` | `0.652` | `+0.320` | `1.000` | `0.888` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `696.42` | `0.971` | `0.647` | `+0.324` | `1.000` | `0.883` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `417.62` | `0.991` | `0.658` | `+0.332` | `1.000` | `0.962` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `726.47` | `0.972` | `0.647` | `+0.325` | `1.000` | `0.888` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `1575.85` | `0.984` | `0.655` | `+0.329` | `1.000` | `0.934` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `3020.34` | `0.975` | `0.651` | `+0.324` | `1.000` | `0.898` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `build-02` | `recall` | `build` | `2390.94` | `0.593` | `0.445` | `+0.148` | `0.500` | `0.928` | `1.000` | `0.883` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | foo.c:5:2 | - |
| `ci-03` | `recall` | `ci` | `4290.81` | `0.833` | `0.654` | `+0.179` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `536.94` | `0.976` | `0.648` | `+0.329` | `1.000` | `0.905` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `build-03` | `summary` | `build` | `805.51` | `0.747` | `0.574` | `+0.172` | `0.714` | `0.875` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | failing tests | - |
| `docker-05` | `summary` | `docker` | `1700.72` | `0.886` | `0.577` | `+0.309` | `1.000` | `0.850` | `1.000` | `0.925` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `318.80` | `0.935` | `0.000` | `+0.935` | `1.000` | `0.837` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `ci-04` | `summary` | `ci` | `528.09` | `0.953` | `0.000` | `+0.953` | `1.000` | `0.884` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `npm-09` | `summary` | `npm` | `629.93` | `0.976` | `0.648` | `+0.329` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `271.56` | `0.936` | `0.000` | `+0.936` | `1.000` | `0.841` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `934.53` | `0.659` | `0.000` | `+0.659` | `1.000` | `0.918` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `833.81` | `0.972` | `0.000` | `+0.972` | `1.000` | `0.907` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `1437.82` | `0.479` | `0.000` | `+0.479` | `1.000` | `0.846` | `0.500` | `0.400` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `1085.57` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.198` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- E302 - found 1' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- E302 - found 1' |
| `kubernetes-06` | `structured` | `kubernetes` | `2175.70` | `0.143` | `0.000` | `+0.143` | `1.000` | `0.195` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `1807.34` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.666` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- InstanceId: i-12345 - State: {"Name": "running"}' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- InstanceId: i-12345 - State: {"Name": "running"}' |
| `network-01` | `exact_format` | `network` | `820.19` | `0.624` | `0.000` | `+0.624` | `1.000` | `0.332` | `0.675` | `0.574` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `810.76` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response' |
| `shell-03` | `exact_format` | `shell` | `1691.74` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.667` | `0.475` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_lines_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- step1 - OUTPUT: value1 - step2 - OUTPUT: value2' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- step1 - OUTPUT: value1 - step2 - OUTPUT: value2' |
| `shell-04` | `exact_format` | `shell` | `671.45` | `0.291` | `0.000` | `+0.291` | `1.000` | `0.492` | `0.311` | `0.233` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `build-04` | `exact_format` | `build` | `2768.86` | `0.303` | `0.000` | `+0.303` | `0.286` | `0.600` | `0.473` | `0.473` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | Resources: 1 added | - |
| `build-05` | `exact_format` | `build` | `425.81` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `536.26` | `0.712` | `0.000` | `+0.712` | `1.000` | `0.658` | `0.750` | `0.600` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `477.22` | `0.949` | `0.627` | `+0.322` | `1.000` | `0.872` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `455.69` | `0.937` | `0.619` | `+0.318` | `1.000` | `0.843` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `1897.09` | `0.967` | `0.644` | `+0.323` | `1.000` | `0.916` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `463.73` | `0.960` | `0.637` | `+0.323` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `2560.38` | `0.874` | `0.580` | `+0.294` | `1.000` | `0.877` | `1.000` | `0.894` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `366.49` | `0.945` | `0.000` | `+0.945` | `1.000` | `0.863` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `780.99` | `0.889` | `0.582` | `+0.307` | `1.000` | `0.849` | `1.000` | `0.931` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `417.55` | `0.947` | `0.627` | `+0.320` | `1.000` | `0.867` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `418.40` | `0.955` | `0.636` | `+0.319` | `1.000` | `0.888` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `378.80` | `0.955` | `0.635` | `+0.320` | `1.000` | `0.887` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `814.92` | `0.965` | `0.637` | `+0.328` | `1.000` | `0.913` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `1201.12` | `0.958` | `0.000` | `+0.958` | `1.000` | `0.894` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `747.58` | `0.926` | `0.611` | `+0.314` | `1.000` | `0.814` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `513.31` | `0.946` | `0.629` | `+0.316` | `1.000` | `0.864` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `548.36` | `0.941` | `0.627` | `+0.314` | `1.000` | `0.853` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `1894.02` | `0.960` | `0.633` | `+0.327` | `1.000` | `0.900` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `396.43` | `0.959` | `0.000` | `+0.959` | `1.000` | `0.897` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `627.07` | `0.945` | `0.627` | `+0.319` | `1.000` | `0.864` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `331.67` | `0.900` | `0.000` | `+0.900` | `1.000` | `0.751` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `ci-07` | `structured` | `ci` | `2069.65` | `0.143` | `0.000` | `+0.143` | `1.000` | `0.195` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `linting-03` | `structured` | `linting` | `1693.51` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.666` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- InstanceId: i-12345 - State: {"Name": "running"}' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- InstanceId: i-12345 - State: {"Name": "running"}' |
| `network-02` | `exact_format` | `network` | `789.34` | `0.624` | `0.000` | `+0.624` | `1.000` | `0.332` | `0.675` | `0.574` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `1173.06` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.648` | `0.750` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response INFO: Retrying...' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response INFO: Retrying...' |
| `shell-07` | `exact_format` | `shell` | `847.35` | `0.770` | `0.000` | `+0.770` | `1.000` | `0.000` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `build-06` | `exact_format` | `build` | `2565.06` | `0.303` | `0.000` | `+0.303` | `0.286` | `0.600` | `0.473` | `0.473` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | Resources: 1 added | - |
| `runtime-07` | `exact_format` | `runtime` | `548.87` | `0.516` | `0.000` | `+0.516` | `1.000` | `0.319` | `0.560` | `0.476` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `build-07` | `exact_format` | `build` | `1073.95` | `0.574` | `0.000` | `+0.574` | `1.000` | `0.850` | `0.560` | `0.504` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `263.21` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `476.89` | `0.949` | `0.627` | `+0.322` | `1.000` | `0.872` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `445.79` | `0.937` | `0.619` | `+0.318` | `1.000` | `0.843` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `520.10` | `0.968` | `0.641` | `+0.327` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `2246.09` | `0.976` | `0.649` | `+0.326` | `1.000` | `0.940` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `820.51` | `0.889` | `0.582` | `+0.307` | `1.000` | `0.849` | `1.000` | `0.931` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `411.98` | `0.971` | `0.645` | `+0.326` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `284.19` | `0.930` | `0.000` | `+0.930` | `1.000` | `0.825` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `382.09` | `0.969` | `0.000` | `+0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1195.57` | `0.938` | `0.625` | `+0.313` | `1.000` | `0.845` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
