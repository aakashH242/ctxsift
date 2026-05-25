# cpu-qwen3.5-0.8b

## Scenario

- track: `cpu`
- phase: `cpu-screen`
- model: `unsloth/Qwen3.5-0.8B-GGUF`
- quantization: `none`
- device: `cpu`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `9834.62`
- cpu_rss_bytes: `null`
- gpu_peak_bytes: `null`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- recovered_final_score: `56.45`
- raw_final_score: `49.84`
- recovery_lift: `+6.61`
- case_count: `280`
- success_count: `264`
- accepted_count: `199`
- soft_accepted_count: `65`
- rejected_count: `16`
- exact_pass_count: `221`
- avg_inference_ms: `4542.82`
- p95_inference_ms: `9507.65`
- avg_exact_preservation_ratio: `0.912`
- avg_summary_quality_ratio: `0.816`
- avg_format_adherence_score: `0.834`
- avg_instruction_following_score: `0.800`
- avg_brevity_ratio: `0.885`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.762`
- p10_case_score: `0.143`
- quality_core: `0.638`
- latency_factor: `0.884`
- final_score: `56.45`
- peak_cpu_rss_bytes: `null`
- peak_gpu_bytes: `null`

### Raw View

- accepted_count: `129`
- soft_accepted_count: `134`
- rejected_count: `17`
- exact_pass_count: `221`
- avg_exact_preservation_ratio: `0.912`
- avg_summary_quality_ratio: `0.815`
- avg_format_adherence_score: `0.679`
- avg_instruction_following_score: `0.644`
- avg_brevity_ratio: `0.886`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.669`
- p10_case_score: `0.143`
- quality_core: `0.564`
- final_score: `49.84`

## Cases

| case_id | family | domain | ms | recovered_score | raw_score | lift | preserve | quality | format | instruction | recovered_thought_density | raw_thought_density | recovered_validation | raw_validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `13122.18` | `0.586` | `0.587` | `-0.001` | `1.000` | `0.899` | `0.500` | `0.404` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-02` | `summary` | `python` | `12362.20` | `0.613` | `0.613` | `-0.001` | `1.000` | `0.936` | `0.500` | `0.459` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-03` | `recall` | `python` | `3363.59` | `0.989` | `0.661` | `+0.328` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-04` | `recall` | `python` | `4129.91` | `0.989` | `0.661` | `+0.328` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-05` | `recall` | `python` | `2960.35` | `0.993` | `0.664` | `+0.329` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `3401.09` | `0.992` | `0.662` | `+0.329` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `6346.90` | `0.624` | `0.473` | `+0.151` | `0.093` | `0.903` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | pytest tests/integration -k billing -vv --maxfail=1, tests/integration/test_billing_api.py::test_invoice_webhook_uses_signature, /workspace/tests/integration/test_billing_api.py:73, 1 error in 2.31s | - |
| `pytest-03` | `recall` | `pytest` | `3788.99` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `2951.72` | `0.994` | `0.665` | `+0.329` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `5902.25` | `0.776` | `0.776` | `+0.000` | `0.765` | `0.930` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | pytest tests/unit tests/integration --disable-warnings=0 | - |
| `mypy-01` | `recall` | `mypy` | `2755.94` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.962` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `2947.22` | `0.979` | `0.653` | `+0.326` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `3862.64` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ruff-01` | `recall` | `ruff` | `5680.82` | `0.867` | `0.865` | `+0.002` | `0.911` | `0.931` | `1.000` | `0.864` | `0.000` | `0.000` | `accepted` | `accepted` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `1956.02` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `2187.17` | `0.983` | `0.656` | `+0.327` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `3845.35` | `0.985` | `0.000` | `+0.985` | `1.000` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `2933.00` | `0.982` | `0.653` | `+0.329` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `2660.31` | `0.984` | `0.655` | `+0.329` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `black-01` | `summary` | `black` | `2484.98` | `0.989` | `0.661` | `+0.328` | `1.000` | `0.971` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `black-02` | `summary` | `black` | `2529.01` | `0.979` | `0.654` | `+0.325` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `black-03` | `recall` | `black` | `1904.72` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.969` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `3460.42` | `0.978` | `0.651` | `+0.327` | `1.000` | `0.912` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `15084.87` | `0.834` | `0.834` | `+0.000` | `1.000` | `0.925` | `1.000` | `0.811` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `5222.19` | `0.783` | `0.783` | `+0.000` | `0.800` | `0.928` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Lifecycle script `build` failed, storefront@2.8.1 | - |
| `pnpm-01` | `recall` | `pnpm` | `5308.35` | `0.802` | `0.802` | `+0.000` | `0.895` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | --no-frozen-lockfile | - |
| `pnpm-02` | `summary` | `pnpm` | `8419.65` | `0.979` | `0.979` | `+0.000` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `3611.84` | `0.987` | `0.657` | `+0.329` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `3347.51` | `0.983` | `0.655` | `+0.327` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `3115.94` | `0.993` | `0.663` | `+0.330` | `1.000` | `0.971` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `14208.19` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.953` | `0.500` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | unterminated_reasoning_block | - | fallback output validation failed: model did not stop thinking before reaching the output limit. first_pass="- tsc src/index.ts src/http.ts --pretty false - src/index.ts(48,20): error TS2769: No overload matches this call. Overload 1 of 2, '(url: string, init?: Requ..." repair_pass="- tsc src/index.ts src/http.ts --pretty false - src/index.ts(48,20): error TS2769: No overload matches this call. Overload 1 of 2, '(url: string, init?: Requ..." |
| `eslint-01` | `recall` | `eslint` | `7795.26` | `0.947` | `0.946` | `+0.000` | `1.000` | `0.932` | `1.000` | `0.936` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `2251.67` | `0.980` | `0.654` | `+0.326` | `1.000` | `0.951` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `3491.10` | `0.985` | `0.986` | `-0.001` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `4684.61` | `0.985` | `0.985` | `+0.000` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `1853.94` | `0.975` | `0.975` | `+0.000` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `4126.97` | `0.977` | `0.650` | `+0.327` | `1.000` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `1388.76` | `0.975` | `0.975` | `+0.000` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `3426.70` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.949` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `7083.41` | `0.964` | `0.963` | `+0.001` | `1.000` | `0.928` | `1.000` | `0.990` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `2622.61` | `0.975` | `0.651` | `+0.324` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `4798.66` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.965` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `1917.51` | `0.995` | `0.995` | `+0.000` | `1.000` | `0.988` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `6037.54` | `0.982` | `0.652` | `+0.329` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `2141.86` | `0.984` | `0.652` | `+0.332` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `5261.43` | `0.945` | `0.945` | `-0.000` | `1.000` | `0.936` | `1.000` | `0.931` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `2755.41` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `2917.92` | `0.984` | `0.655` | `+0.328` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `5125.59` | `0.937` | `0.938` | `-0.000` | `1.000` | `0.931` | `1.000` | `0.921` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `5492.09` | `0.785` | `0.785` | `+0.000` | `0.811` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Error 2 | - |
| `git-01` | `recall` | `git` | `19796.60` | `0.592` | `0.592` | `+0.000` | `1.000` | `0.906` | `0.500` | `0.411` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `git-02` | `recall` | `git` | `7561.85` | `0.864` | `0.864` | `+0.000` | `1.000` | `0.868` | `1.000` | `0.816` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `4447.83` | `0.989` | `0.659` | `+0.330` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `3908.00` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `curl-02` | `recall` | `curl` | `3217.78` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ssh-01` | `summary` | `ssh` | `5003.74` | `0.765` | `0.765` | `+0.000` | `0.714` | `0.928` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | GIT_SSH_COMMAND="ssh -o IdentitiesOnly=yes -i ~/.ssh/deploy_key" git ls-remote git@github.com:example/mono-app.git | - |
| `ssh-02` | `summary` | `ssh` | `2385.12` | `0.980` | `0.651` | `+0.329` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `5890.13` | `0.609` | `0.467` | `+0.142` | `0.226` | `0.774` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | queue-worker.service, /opt/app/bin/worker.sh, status=203/EXEC | - |
| `systemd-02` | `summary` | `systemd` | `3283.73` | `0.962` | `0.640` | `+0.322` | `1.000` | `0.904` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `2551.29` | `0.977` | `0.649` | `+0.327` | `1.000` | `0.942` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `8936.80` | `0.911` | `0.614` | `+0.296` | `1.000` | `0.951` | `1.000` | `0.864` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `7923.16` | `0.770` | `0.599` | `+0.171` | `0.750` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | example.com/mono-app/pkg/server | - |
| `go-test-01` | `summary` | `go-test` | `6807.53` | `0.742` | `0.574` | `+0.168` | `0.600` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | go test ./... -run TestCacheTTL -count=1 | - |
| `javac-01` | `recall` | `javac` | `30674.95` | `0.678` | `0.678` | `-0.000` | `0.600` | `0.912` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | javac -d out $(find src/main/java -name '*.java') | - |
| `maven-01` | `recall` | `maven` | `9569.98` | `0.566` | `0.421` | `+0.145` | `0.304` | `0.914` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | mvn -q test, UserControllerTest.java:72, maven-surefire-plugin:3.5.5:test | - |
| `maven-02` | `summary` | `maven` | `3325.13` | `0.990` | `0.660` | `+0.330` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `3153.09` | `0.987` | `0.658` | `+0.329` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `4575.14` | `0.696` | `0.696` | `+0.000` | `0.389` | `0.930` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ./gradlew test, Execution failed for task ':test' | - |
| `cargo-01` | `recall` | `cargo` | `8996.01` | `0.983` | `0.983` | `+0.000` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `cargo-02` | `recall` | `cargo` | `3688.70` | `0.984` | `0.984` | `+0.000` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `51119.13` | `0.423` | `0.423` | `+0.000` | `0.526` | `0.928` | `0.500` | `0.380` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | node dist/server.js, MODULE_NOT_FOUND | - |
| `npm-04` | `summary` | `npm` | `20445.41` | `0.823` | `0.823` | `+0.000` | `1.000` | `0.934` | `1.000` | `0.790` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `4202.81` | `0.976` | `0.646` | `+0.330` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `2398.04` | `0.989` | `0.660` | `+0.329` | `1.000` | `0.973` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-runtime-01` | `recall` | `python-runtime` | `10210.37` | `0.609` | `0.610` | `-0.000` | `1.000` | `0.939` | `0.500` | `0.428` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `pytest-06` | `summary` | `pytest` | `6498.25` | `0.986` | `0.986` | `+0.000` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `3955.59` | `0.963` | `0.637` | `+0.327` | `1.000` | `0.908` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `8876.88` | `0.976` | `0.976` | `+0.000` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `2739.94` | `0.982` | `0.652` | `+0.330` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `2348.08` | `0.969` | `0.969` | `+0.000` | `1.000` | `0.924` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `7956.41` | `0.827` | `0.646` | `+0.182` | `1.000` | `0.934` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `2749.33` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `8110.74` | `0.993` | `0.661` | `+0.332` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `2047.84` | `0.977` | `0.649` | `+0.328` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `3317.20` | `0.979` | `0.648` | `+0.331` | `1.000` | `0.946` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `2030.56` | `0.992` | `0.992` | `+0.000` | `1.000` | `0.979` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `4366.73` | `0.974` | `0.974` | `+0.000` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `5280.36` | `0.684` | `0.684` | `+0.000` | `0.600` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | psql -h 127.0.0.1 -U app_user -d appdb -c 'select 1' | - |
| `postgres-02` | `summary` | `postgres` | `9876.01` | `0.963` | `0.963` | `+0.000` | `1.000` | `0.906` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `2723.18` | `0.989` | `0.659` | `+0.330` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `4292.84` | `0.732` | `0.732` | `+0.000` | `0.667` | `0.861` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | mysql -h db.example.net -u app -D appdb -e "SELECT id, createdAt FROM users LIMIT 5" | - |
| `redis-01` | `summary` | `redis` | `2653.68` | `0.986` | `0.655` | `+0.331` | `1.000` | `0.965` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `1990.02` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `9548.92` | `0.899` | `0.897` | `+0.002` | `1.000` | `0.895` | `1.000` | `0.868` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `6678.47` | `0.730` | `0.560` | `+0.170` | `0.579` | `0.911` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | pnpm install --frozen-lockfile, react-dom@18.3.1 | - |
| `jenkins-01` | `summary` | `jenkins` | `1859.79` | `0.967` | `0.644` | `+0.322` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `make-01` | `summary` | `make` | `2726.90` | `0.979` | `0.653` | `+0.327` | `1.000` | `0.949` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `4661.85` | `0.985` | `0.985` | `+0.000` | `1.000` | `0.962` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `2603.31` | `0.992` | `0.660` | `+0.332` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `2687.87` | `0.981` | `0.653` | `+0.328` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `4040.31` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `25728.85` | `0.540` | `0.539` | `+0.001` | `0.851` | `0.904` | `0.500` | `0.405` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | src/router.rs:128 | - |
| `ci-log-01` | `recall` | `ci-log` | `7387.73` | `0.945` | `0.633` | `+0.312` | `1.000` | `0.928` | `1.000` | `0.936` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `15154.14` | `0.859` | `0.860` | `-0.000` | `1.000` | `0.952` | `1.000` | `0.771` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `8326.29` | `0.765` | `0.765` | `+0.000` | `0.679` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | checkout_test.go:71, total = 42.00, want 37.00, test timed out after 10m0s | - |
| `build-log-01` | `summary` | `build-log` | `3516.50` | `0.961` | `0.961` | `+0.000` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `3071.50` | `0.581` | `0.494` | `+0.086` | `1.000` | `0.936` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `12375.61` | `0.000` | `0.000` | `+0.000` | `0.625` | `0.228` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | @typescript-eslint/no-misused-promises, @typescript-eslint/no-explicit-any, @typescript-eslint/no-unsafe-assignment | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass="- /repo/web/src/App.tsx 12:7 warning 'debugMode' is assigned a value but never used 27:19 error Promise returned in function argument where a void return was..." repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass="- /repo/web/src/App.tsx 12:7 warning 'debugMode' is assigned a value but never used 27:19 error Promise returned in function argument where a void return was..." |
| `git-review-01` | `instruction_following` | `git-review` | `9273.81` | `0.495` | `0.495` | `+0.000` | `1.000` | `0.657` | `0.375` | `0.375` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `25593.89` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.337` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='- exit status 22' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='search endpoint failed after 2 attempts curl: (22) exit status 22 https://staging.example.com/api/search?q=smoke curl: (22) failed endpoint: https://staging....' |
| `structured-output-01` | `structured` | `structured-output` | `7486.63` | `0.279` | `0.279` | `+0.000` | `0.611` | `0.188` | `0.375` | `0.375` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | /work/app/api/routes.py, 21 | - |
| `structured-output-02` | `structured` | `structured-output` | `9008.84` | `0.175` | `0.175` | `-0.000` | `0.905` | `0.851` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | port 5432 is already allocated | - |
| `structured-output-03` | `structured` | `structured-output` | `7834.07` | `0.143` | `0.143` | `+0.000` | `0.857` | `0.497` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | "refresh token expired", "invalid refresh token" | - |
| `structured-output-04` | `structured` | `structured-output` | `6128.71` | `0.108` | `0.108` | `+0.000` | `1.000` | `0.194` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `6633.48` | `0.453` | `0.453` | `+0.000` | `1.000` | `0.000` | `0.494` | `0.376` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `4089.73` | `0.568` | `0.568` | `+0.000` | `1.000` | `0.331` | `0.576` | `0.576` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `4138.51` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `1795.62` | `0.966` | `0.645` | `+0.321` | `1.000` | `0.914` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `2361.34` | `0.955` | `0.637` | `+0.318` | `1.000` | `0.888` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `5979.99` | `0.716` | `0.716` | `+0.000` | `1.000` | `0.704` | `0.667` | `0.651` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `9244.75` | `0.800` | `0.800` | `+0.000` | `0.905` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | app.tasks.email.send_welcome_email | - |
| `mypy-05` | `recall` | `mypy` | `6757.17` | `0.682` | `0.521` | `+0.161` | `0.600` | `0.928` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | include_meta, -> bytes, -> str | - |
| `terraform-08` | `recall` | `terraform` | `3896.58` | `0.984` | `0.658` | `+0.326` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `6197.68` | `0.748` | `0.579` | `+0.169` | `0.783` | `0.912` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | InventorySyncTest.java:132 | - |
| `kubernetes-01` | `recall` | `kubernetes` | `7076.89` | `0.945` | `0.945` | `+0.000` | `1.000` | `0.918` | `1.000` | `0.940` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `3041.89` | `0.983` | `0.655` | `+0.327` | `1.000` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `6016.79` | `0.988` | `0.987` | `+0.000` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `2609.73` | `0.987` | `0.658` | `+0.330` | `1.000` | `0.949` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `4489.51` | `0.983` | `0.983` | `+0.000` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `5418.78` | `0.711` | `0.549` | `+0.162` | `0.667` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | 20260518_add_workspace_limits.sql, packages/db/test/migrate.test.ts:44:7 | - |
| `pnpm-04` | `recall` | `pnpm` | `3127.92` | `0.988` | `0.658` | `+0.330` | `1.000` | `0.952` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `2378.49` | `0.988` | `0.662` | `+0.325` | `1.000` | `0.951` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `2760.14` | `0.982` | `0.656` | `+0.326` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `3295.29` | `0.984` | `0.654` | `+0.329` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `3339.41` | `0.992` | `0.662` | `+0.330` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `3461.82` | `0.982` | `0.982` | `+0.000` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `2308.49` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.949` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `5676.50` | `0.929` | `0.929` | `+0.000` | `1.000` | `0.929` | `1.000` | `0.906` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `3487.93` | `0.981` | `0.981` | `+0.000` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `2576.42` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `4143.75` | `0.641` | `0.641` | `+0.000` | `0.529` | `0.865` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | web@1.7.0, upload-sourcemaps dist --rewrite | - |
| `python-pytest-01` | `summary` | `python-pytest` | `2827.73` | `0.969` | `0.648` | `+0.321` | `1.000` | `0.922` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `8059.95` | `0.760` | `0.591` | `+0.170` | `0.684` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ./integration | - |
| `npm-05` | `summary` | `npm` | `4894.55` | `0.711` | `0.547` | `+0.164` | `0.533` | `0.882` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | web@1.2.0, src/pages/admin.tsx | - |
| `helm-01` | `summary` | `helm` | `2597.94` | `0.970` | `0.643` | `+0.326` | `1.000` | `0.924` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `5160.69` | `0.780` | `0.606` | `+0.174` | `0.895` | `0.859` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | typing.Optional | - |
| `k6-01` | `summary` | `k6` | `8105.13` | `0.739` | `0.575` | `+0.164` | `0.652` | `0.892` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | checks, http_req_duration | - |
| `composer-01` | `summary` | `composer` | `8306.85` | `0.939` | `0.629` | `+0.309` | `1.000` | `0.941` | `1.000` | `0.949` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `4356.78` | `0.592` | `0.442` | `+0.150` | `0.000` | `0.866` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | xcodebuild, -scheme, MobileApp, -configuration, Release | - |
| `make-02` | `summary` | `make` | `5930.26` | `0.803` | `0.629` | `+0.174` | `0.909` | `0.919` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | -Iinclude | - |
| `python-pytest-02` | `summary` | `python-pytest` | `7762.76` | `0.969` | `0.969` | `+0.000` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `3944.50` | `0.951` | `0.640` | `+0.311` | `1.000` | `0.878` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `4497.82` | `0.786` | `0.786` | `+0.000` | `0.833` | `0.916` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `5674.06` | `0.967` | `0.967` | `+0.000` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `2230.88` | `0.945` | `0.628` | `+0.317` | `1.000` | `0.863` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `2689.39` | `0.975` | `0.649` | `+0.326` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `8290.77` | `0.355` | `0.355` | `+0.000` | `0.741` | `0.628` | `0.333` | `0.333` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | 22:7, prefer-const | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `2330.98` | `0.603` | `0.603` | `+0.000` | `1.000` | `0.696` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `3845.59` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `0.617` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_lines_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- tests/test_api.py::test_create_user - tests/test_auth.py::test_refresh_token_expiry' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- tests/test_api.py::test_create_user - tests/test_auth.py::test_refresh_token_expiry' |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `3283.65` | `0.665` | `0.665` | `+0.000` | `1.000` | `0.673` | `0.667` | `0.581` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `1965.81` | `0.597` | `0.597` | `+0.000` | `1.000` | `0.675` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `6507.51` | `0.596` | `0.596` | `+0.000` | `1.000` | `0.385` | `0.533` | `0.411` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `4863.25` | `0.256` | `0.256` | `+0.000` | `0.450` | `0.325` | `0.371` | `0.349` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | [deps 4/4], pnpm install --frozen-lockfile | - |
| `terraform-09` | `instruction_following` | `terraform` | `2352.60` | `0.598` | `0.598` | `+0.000` | `1.000` | `0.680` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `7158.46` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.901` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- UserService.java:[44,17] cannot find symbol symbol: method findByEmail(java.lang.String) - UserController.java:[28,31] incompatible types: java.lang.Long c...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='[WARNING] /repo/src/main/java/App.java:[12,8] unchecked conversion [ERROR] /repo/src/main/java/UserService.java:[44,17] cannot find symbol symbol: method fin...' |
| `playwright-01` | `instruction_following` | `playwright` | `4727.54` | `0.644` | `0.644` | `+0.000` | `1.000` | `0.860` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `3853.45` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.000` | `0.380` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_lines_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- src/App.tsx - src/api/client.ts - README.md is formatted' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- src/App.tsx - src/api/client.ts - README.md is formatted' |
| `kubectl-08` | `instruction_following` | `kubectl` | `4649.86` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.000` | `0.475` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_lines_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- worker-5b8c - CrashLoopBackOff - migrator-9z1q - Error' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='worker-5b8c - CrashLoopBackOff - migrator-9z1q - Error' |
| `cargo-04` | `instruction_following` | `cargo` | `5955.37` | `0.468` | `0.468` | `+0.000` | `1.000` | `0.685` | `0.333` | `0.333` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `4935.25` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.546` | `0.336` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) exit code 23' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) exit code 23' |
| `pyright-01` | `structured` | `pyright` | `6781.50` | `0.335` | `0.335` | `+0.000` | `1.000` | `0.183` | `0.300` | `0.300` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `6165.79` | `0.088` | `0.088` | `+0.000` | `0.667` | `0.182` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | resource, field | - |
| `junit-01` | `structured` | `junit` | `2587.36` | `0.944` | `0.944` | `+0.000` | `1.000` | `0.814` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `2457.19` | `0.143` | `0.143` | `+0.000` | `1.000` | `0.190` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `8221.49` | `0.070` | `0.070` | `+0.000` | `0.667` | `0.179` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | line, column, rule | - |
| `docker-build-04` | `structured` | `docker-build` | `2806.73` | `0.713` | `0.713` | `+0.000` | `1.000` | `0.606` | `0.800` | `0.659` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `7790.69` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.779` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- failed_tests - name - TestParseAmount - location - amount_test.go:22 - message --- FAIL: TestParseAmount (0.00s) amount_test.go:22: got 10.0 want 10.00 ---...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='--- FAIL: TestParseAmount (0.00s) amount_test.go:22: got 10.0 want 10.00 --- FAIL: TestFormatCurrency (0.00s) currency_test.go:51: got USD 10 want $10.00 FAIL' |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `2832.26` | `0.827` | `0.827` | `+0.000` | `1.000` | `0.633` | `1.000` | `0.812` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `6006.80` | `0.084` | `0.084` | `-0.000` | `0.667` | `0.229` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | package, required | - |
| `mypy-06` | `structured` | `mypy` | `3664.09` | `0.211` | `0.211` | `+0.000` | `1.000` | `0.858` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `4823.99` | `0.064` | `0.064` | `+0.000` | `0.242` | `0.177` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | failed, task, :api:compileJava, cause | - |
| `playwright-02` | `structured` | `playwright` | `4807.87` | `0.148` | `0.148` | `+0.000` | `0.167` | `0.164` | `0.225` | `0.225` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | project, chromium, file, line, test | - |
| `postgres-04` | `structured` | `postgres` | `1914.87` | `0.142` | `0.142` | `+0.000` | `1.000` | `0.181` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `vite-01` | `structured` | `vite` | `3719.48` | `0.104` | `0.104` | `+0.000` | `1.000` | `0.183` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `2126.59` | `0.414` | `0.414` | `+0.000` | `1.000` | `0.000` | `0.333` | `0.250` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `6355.89` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.282` | `0.087` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass="Merge made by the 'ort' strategy. commit 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 Author: CI Bot Status: deployed to staging" repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass="Merge made by the 'ort' strategy. commit 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 Author: CI Bot Status: deployed to staging" |
| `docker-04` | `exact_format` | `docker` | `10597.15` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.331` | `0.311` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='pushed ghcr.io/acme/api:2026.05.18 digest: sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 verified ghcr.io/acme/api@sha256:aaaaaaaa1...' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='pushed ghcr.io/acme/api:2026.05.18 digest: sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 verified ghcr.io/acme/api@sha256:aaaaaaaa1...' |
| `npm-08` | `exact_format` | `npm` | `1541.95` | `0.221` | `0.221` | `+0.000` | `1.000` | `0.294` | `0.233` | `0.181` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `3289.35` | `0.403` | `0.403` | `+0.000` | `1.000` | `0.335` | `0.400` | `0.400` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `4031.34` | `0.204` | `0.204` | `+0.000` | `0.500` | `0.298` | `0.277` | `0.277` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | prod | - |
| `cargo-05` | `exact_format` | `cargo` | `1589.12` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `1233.87` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `3957.50` | `0.063` | `0.063` | `+0.000` | `0.000` | `0.248` | `0.150` | `0.110` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | 20260518133742 | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `1542.52` | `0.951` | `0.633` | `+0.318` | `1.000` | `0.878` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `3387.58` | `0.956` | `0.640` | `+0.316` | `1.000` | `0.890` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `6104.81` | `0.703` | `0.703` | `+0.000` | `0.667` | `0.647` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | orders_customer_id_fkey | - |
| `docker-build-05` | `explanation` | `docker-build` | `3045.18` | `0.966` | `0.966` | `+0.000` | `1.000` | `0.916` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `1758.77` | `0.963` | `0.642` | `+0.321` | `1.000` | `0.908` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `3143.16` | `0.725` | `0.565` | `+0.160` | `0.750` | `0.788` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | returns a reference | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `4986.64` | `0.710` | `0.713` | `-0.003` | `0.583` | `0.848` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `1581.57` | `0.989` | `0.662` | `+0.327` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `1801.35` | `0.987` | `0.663` | `+0.324` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `1885.02` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `3925.79` | `0.651` | `0.651` | `+0.000` | `0.538` | `0.893` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | npm ERR! code E404 | - |
| `runtime-02` | `recall` | `runtime` | `3032.36` | `0.691` | `0.691` | `+0.000` | `0.667` | `0.854` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | duplicate key value violates unique constraint | - |
| `compilation-01` | `recall` | `compilation` | `1958.57` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `3169.90` | `0.652` | `0.652` | `+0.000` | `0.524` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | main.rs:5:26 | - |
| `ci-01` | `recall` | `ci` | `1635.01` | `0.967` | `0.967` | `+0.000` | `1.000` | `0.867` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `3970.02` | `0.980` | `0.980` | `+0.000` | `1.000` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `2717.56` | `0.937` | `0.937` | `+0.000` | `1.000` | `0.892` | `1.000` | `0.937` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `25150.91` | `0.752` | `0.752` | `+0.000` | `0.778` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | "ami" is required | - |
| `compilation-02` | `recall` | `compilation` | `3431.63` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `3354.12` | `0.966` | `0.966` | `+0.000` | `1.000` | `0.863` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `5005.69` | `0.560` | `0.560` | `+0.000` | `0.412` | `0.857` | `1.000` | `0.918` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Execution failed for task ':test' | - |
| `container-runtime-01` | `recall` | `container-runtime` | `3475.29` | `0.934` | `0.935` | `-0.002` | `1.000` | `0.873` | `1.000` | `0.940` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `3444.99` | `0.972` | `0.978` | `-0.006` | `1.000` | `0.889` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `3033.44` | `0.595` | `0.595` | `+0.000` | `0.500` | `0.891` | `1.000` | `0.906` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | You must be logged in to the server | - |
| `runtime-03` | `recall` | `runtime` | `1052.06` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `1308.27` | `0.972` | `0.972` | `+0.000` | `1.000` | `0.887` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `4844.37` | `0.907` | `0.907` | `-0.000` | `1.000` | `0.906` | `1.000` | `0.877` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `4718.36` | `0.975` | `0.975` | `+0.000` | `1.000` | `0.899` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `3794.38` | `0.593` | `0.593` | `+0.000` | `0.500` | `0.928` | `1.000` | `0.883` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | foo.c:5:2 | - |
| `ci-03` | `recall` | `ci` | `6932.48` | `0.833` | `0.833` | `+0.000` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `1139.50` | `0.976` | `0.976` | `+0.000` | `1.000` | `0.904` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `2703.45` | `0.747` | `0.747` | `+0.000` | `0.714` | `0.875` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | failing tests | - |
| `docker-05` | `summary` | `docker` | `3339.24` | `0.886` | `0.886` | `+0.000` | `1.000` | `0.850` | `1.000` | `0.925` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `976.63` | `0.935` | `0.621` | `+0.314` | `1.000` | `0.837` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `1190.65` | `0.953` | `0.629` | `+0.324` | `1.000` | `0.884` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `1193.59` | `0.976` | `0.976` | `+0.000` | `1.000` | `0.940` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `984.29` | `0.937` | `0.937` | `+0.000` | `1.000` | `0.842` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `2072.35` | `0.659` | `0.659` | `+0.001` | `1.000` | `0.918` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `2195.82` | `0.972` | `0.972` | `+0.000` | `1.000` | `0.907` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `4161.55` | `0.479` | `0.641` | `-0.162` | `1.000` | `0.846` | `0.500` | `0.400` | `0.000` | `0.000` | `soft_accepted` | `accepted` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `3363.31` | `0.074` | `0.074` | `+0.000` | `0.333` | `0.173` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | E302 | - |
| `kubernetes-06` | `structured` | `kubernetes` | `2703.50` | `0.143` | `0.143` | `-0.000` | `1.000` | `0.194` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `3596.34` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.666` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- InstanceId: i-12345 - State: {"Name": "running"}' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- InstanceId: i-12345 - State: {"Name": "running"}' |
| `network-01` | `exact_format` | `network` | `1828.30` | `0.624` | `0.624` | `+0.000` | `1.000` | `0.332` | `0.675` | `0.574` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `2867.03` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response' |
| `shell-03` | `exact_format` | `shell` | `3290.46` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.667` | `0.475` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_lines_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- step1 - OUTPUT: value1 - step2 - OUTPUT: value2' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- step1 - OUTPUT: value1 - step2 - OUTPUT: value2' |
| `shell-04` | `exact_format` | `shell` | `1478.96` | `0.290` | `0.290` | `+0.000` | `1.000` | `0.491` | `0.311` | `0.233` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `4554.49` | `0.303` | `0.303` | `+0.000` | `0.286` | `0.600` | `0.473` | `0.473` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Resources: 1 added | - |
| `build-05` | `exact_format` | `build` | `1282.46` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `1321.57` | `0.712` | `0.712` | `+0.000` | `1.000` | `0.658` | `0.750` | `0.600` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `1084.00` | `0.949` | `0.949` | `+0.000` | `1.000` | `0.872` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `1053.89` | `0.937` | `0.937` | `+0.000` | `1.000` | `0.843` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `3686.50` | `0.967` | `0.967` | `+0.000` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `1223.90` | `0.960` | `0.960` | `+0.000` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `4420.10` | `0.874` | `0.874` | `+0.000` | `1.000` | `0.877` | `1.000` | `0.894` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `1098.39` | `0.945` | `0.945` | `+0.000` | `1.000` | `0.863` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `1518.11` | `0.889` | `0.889` | `+0.000` | `1.000` | `0.849` | `1.000` | `0.931` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `1159.52` | `0.946` | `0.946` | `+0.000` | `1.000` | `0.866` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1156.54` | `0.955` | `0.955` | `+0.000` | `1.000` | `0.888` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `1081.85` | `0.955` | `0.955` | `+0.000` | `1.000` | `0.887` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `1395.98` | `0.965` | `0.965` | `+0.000` | `1.000` | `0.914` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `2699.77` | `0.958` | `0.958` | `+0.000` | `1.000` | `0.895` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `1356.39` | `0.926` | `0.926` | `+0.000` | `1.000` | `0.816` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `1143.53` | `0.946` | `0.946` | `+0.000` | `1.000` | `0.864` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `1176.82` | `0.941` | `0.941` | `+0.000` | `1.000` | `0.853` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `2944.10` | `0.960` | `0.960` | `+0.000` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `1017.26` | `0.959` | `0.959` | `+0.000` | `1.000` | `0.896` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `1226.57` | `0.946` | `0.946` | `+0.000` | `1.000` | `0.864` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `2589.28` | `0.946` | `0.946` | `+0.000` | `1.000` | `0.866` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `2676.19` | `0.143` | `0.143` | `-0.000` | `1.000` | `0.194` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `3501.20` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.666` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- InstanceId: i-12345 - State: {"Name": "running"}' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- InstanceId: i-12345 - State: {"Name": "running"}' |
| `network-02` | `exact_format` | `network` | `1598.19` | `0.624` | `0.624` | `+0.000` | `1.000` | `0.332` | `0.675` | `0.574` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `3040.91` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.648` | `0.750` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response INFO: Retrying...' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response INFO: Retrying...' |
| `shell-07` | `exact_format` | `shell` | `2633.77` | `0.770` | `0.770` | `+0.000` | `1.000` | `0.000` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `4591.12` | `0.303` | `0.303` | `+0.000` | `0.286` | `0.600` | `0.473` | `0.473` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Resources: 1 added | - |
| `runtime-07` | `exact_format` | `runtime` | `1403.92` | `0.516` | `0.516` | `+0.000` | `1.000` | `0.319` | `0.560` | `0.476` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `1882.92` | `0.574` | `0.574` | `+0.000` | `1.000` | `0.850` | `0.560` | `0.504` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `1131.63` | `1.000` | `1.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `1084.64` | `0.949` | `0.949` | `+0.000` | `1.000` | `0.872` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `1048.78` | `0.937` | `0.937` | `+0.000` | `1.000` | `0.843` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `1143.19` | `0.968` | `0.968` | `+0.000` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `3864.56` | `0.976` | `0.976` | `+0.000` | `1.000` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `1387.67` | `0.889` | `0.889` | `+0.000` | `1.000` | `0.849` | `1.000` | `0.931` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `1065.19` | `0.971` | `0.971` | `+0.000` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `2328.67` | `0.586` | `0.586` | `+0.000` | `0.000` | `0.847` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | undefined: fmt.Println | - |
| `explanation-17` | `explanation` | `explanation` | `1018.14` | `0.969` | `0.969` | `+0.000` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `3120.44` | `0.951` | `0.951` | `+0.000` | `1.000` | `0.878` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
