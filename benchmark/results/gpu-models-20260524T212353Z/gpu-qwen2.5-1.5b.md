# gpu-qwen2.5-1.5b

## Scenario

- track: `gpu`
- phase: `gpu-screen`
- model: `Qwen/Qwen2.5-1.5B-Instruct`
- quantization: `none`
- device: `cuda`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `223822.89`
- cpu_rss_bytes: `5162647552`
- gpu_peak_bytes: `4324306944`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- recovered_final_score: `59.28`
- raw_final_score: `27.28`
- recovery_lift: `+31.99`
- case_count: `280`
- success_count: `271`
- accepted_count: `171`
- soft_accepted_count: `100`
- rejected_count: `9`
- exact_pass_count: `191`
- avg_inference_ms: `7804.11`
- p95_inference_ms: `20437.97`
- avg_exact_preservation_ratio: `0.814`
- avg_summary_quality_ratio: `0.844`
- avg_format_adherence_score: `0.870`
- avg_instruction_following_score: `0.845`
- avg_brevity_ratio: `0.911`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.761`
- p10_case_score: `0.444`
- quality_core: `0.697`
- latency_factor: `0.850`
- final_score: `59.28`
- peak_cpu_rss_bytes: `5163134976`
- peak_gpu_bytes: `4464932352`

### Raw View

- accepted_count: `0`
- soft_accepted_count: `192`
- rejected_count: `88`
- exact_pass_count: `194`
- avg_exact_preservation_ratio: `0.822`
- avg_summary_quality_ratio: `0.798`
- avg_format_adherence_score: `0.484`
- avg_instruction_following_score: `0.332`
- avg_brevity_ratio: `0.883`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.401`
- p10_case_score: `0.000`
- quality_core: `0.321`
- final_score: `27.28`

## Cases

| case_id | family | domain | ms | recovered_score | raw_score | lift | preserve | quality | format | instruction | recovered_thought_density | raw_thought_density | recovered_validation | raw_validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `55409.63` | `0.576` | `0.573` | `+0.003` | `1.000` | `0.896` | `0.500` | `0.389` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-02` | `summary` | `python` | `13997.63` | `0.985` | `0.657` | `+0.328` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-03` | `recall` | `python` | `2900.02` | `0.990` | `0.659` | `+0.331` | `1.000` | `0.962` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-04` | `recall` | `python` | `37019.32` | `0.851` | `0.578` | `+0.274` | `1.000` | `0.943` | `1.000` | `0.760` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-05` | `recall` | `python` | `17419.86` | `0.773` | `0.602` | `+0.171` | `0.815` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | /workspace/src/reports/export.py | - |
| `pytest-01` | `recall` | `pytest` | `7760.55` | `0.411` | `0.411` | `-0.000` | `0.273` | `0.917` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | tests/api/test_users.py::test_create_user_rejects_duplicate[email], tests/api/test_users.py:47, AssertionError, 500 == 409 | - |
| `pytest-02` | `summary` | `pytest` | `11234.86` | `0.560` | `0.420` | `+0.141` | `0.093` | `0.888` | `1.000` | `0.896` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | pytest tests/integration -k billing -vv --maxfail=1, tests/integration/test_billing_api.py::test_invoice_webhook_uses_signature, /workspace/tests/integration/test_billing_api.py:73, 1 error in 2.31s | - |
| `pytest-03` | `recall` | `pytest` | `23087.46` | `0.859` | `0.581` | `+0.277` | `1.000` | `0.938` | `1.000` | `0.776` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `9831.16` | `0.982` | `0.648` | `+0.334` | `1.000` | `0.960` | `1.000` | `0.986` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `7059.27` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `7814.06` | `0.992` | `0.660` | `+0.331` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `10644.50` | `0.595` | `0.450` | `+0.145` | `0.211` | `0.873` | `1.000` | `0.923` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | mypy src tests --pretty --show-error-codes, src/payments/retry.py:118, arg-type, checked 37 source files | - |
| `mypy-03` | `recall` | `mypy` | `6399.09` | `0.993` | `0.661` | `+0.332` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ruff-01` | `recall` | `ruff` | `5909.49` | `0.945` | `0.626` | `+0.319` | `0.911` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `2160.49` | `0.994` | `0.664` | `+0.330` | `1.000` | `0.985` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `5973.83` | `0.650` | `0.494` | `+0.156` | `0.293` | `0.854` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ruff check src/auth/login.py, src/auth/login.py:93:13, Found 1 error. | - |
| `pylint-01` | `recall` | `pylint` | `8992.99` | `0.984` | `0.657` | `+0.327` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `15192.47` | `0.975` | `0.651` | `+0.324` | `1.000` | `0.902` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `8295.10` | `0.966` | `0.643` | `+0.323` | `1.000` | `0.915` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `black-01` | `summary` | `black` | `5606.31` | `0.989` | `0.660` | `+0.329` | `1.000` | `0.973` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `black-02` | `summary` | `black` | `2316.02` | `0.642` | `0.488` | `+0.154` | `0.234` | `0.866` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | black src, /workspace/src/config/schema.py, Cannot parse, 58:12 | - |
| `black-03` | `recall` | `black` | `1935.48` | `0.993` | `0.664` | `+0.329` | `1.000` | `0.973` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `14444.03` | `0.620` | `0.621` | `-0.001` | `0.905` | `0.903` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, fenced_output_wrapper | package-lock.json | - |
| `npm-02` | `summary` | `npm` | `17720.74` | `0.831` | `0.554` | `+0.278` | `1.000` | `0.919` | `1.000` | `0.811` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `15849.22` | `0.747` | `0.579` | `+0.168` | `0.709` | `0.879` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | npm run build, storefront@2.8.1 | - |
| `pnpm-01` | `recall` | `pnpm` | `3720.68` | `0.987` | `0.657` | `+0.330` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `9694.54` | `0.986` | `0.659` | `+0.327` | `1.000` | `0.965` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `12284.57` | `0.986` | `0.659` | `+0.327` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `9321.77` | `0.983` | `0.656` | `+0.327` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `4373.09` | `0.993` | `0.662` | `+0.331` | `1.000` | `0.971` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `15776.20` | `0.646` | `0.492` | `+0.154` | `0.385` | `0.861` | `1.000` | `0.956` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | tsc src/index.ts src/http.ts --pretty false, src/index.ts(48,20), src/http.ts(9,17) | - |
| `eslint-01` | `recall` | `eslint` | `6419.89` | `0.983` | `0.656` | `+0.327` | `1.000` | `0.931` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `6013.21` | `0.674` | `0.520` | `+0.154` | `0.318` | `0.908` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | eslint ., ERR_MODULE_NOT_FOUND, ESLint: 9.14.0 | - |
| `eslint-03` | `recall` | `eslint` | `9651.72` | `0.985` | `0.659` | `+0.327` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `21592.25` | `0.707` | `0.539` | `+0.168` | `0.653` | `0.951` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Dockerfile:14, failed to solve | - |
| `docker-02` | `summary` | `docker` | `2369.12` | `0.992` | `0.652` | `+0.340` | `1.000` | `0.980` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `14632.67` | `0.568` | `0.422` | `+0.146` | `0.000` | `0.833` | `1.000` | `0.977` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | docker build -f docker/web.Dockerfile -t web:ci ., RUN npm ci, ERESOLVE, react-dates@21.8.0, react@18.2.0, exit code: 1 | - |
| `docker-compose-01` | `summary` | `docker-compose` | `2578.82` | `0.638` | `0.484` | `+0.154` | `0.167` | `0.897` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | docker compose up, external, could not be found | - |
| `docker-compose-02` | `recall` | `docker-compose` | `5719.62` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `9304.92` | `0.615` | `0.612` | `+0.003` | `1.000` | `0.906` | `0.500` | `0.472` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `kubectl-01` | `summary` | `kubectl` | `16164.23` | `0.549` | `0.545` | `+0.004` | `1.000` | `0.920` | `0.500` | `0.394` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `kubectl-02` | `recall` | `kubectl` | `13820.82` | `0.991` | `0.662` | `+0.329` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `4928.11` | `0.990` | `0.661` | `+0.329` | `1.000` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `15083.36` | `0.988` | `0.660` | `+0.327` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `3624.89` | `0.654` | `0.496` | `+0.158` | `0.235` | `0.902` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | terraform validate, main.tf line 23, resource "aws_vpc" "main" | - |
| `terraform-02` | `recall` | `terraform` | `12273.51` | `0.720` | `0.552` | `+0.168` | `0.684` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | terraform plan | - |
| `terraform-03` | `recall` | `terraform` | `9463.79` | `0.789` | `0.616` | `+0.173` | `0.871` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | state snapshot | - |
| `terraform-04` | `summary` | `terraform` | `16075.75` | `0.647` | `0.000` | `+0.647` | `0.195` | `0.907` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | terraform test, run "plan_defaults", tests/aws.tftest.hcl line 18, Test assertion failed | - |
| `mixed-01` | `recall` | `mixed` | `4932.45` | `0.989` | `0.658` | `+0.331` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `12610.32` | `0.560` | `0.422` | `+0.138` | `0.270` | `0.817` | `1.000` | `0.873` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | make integration, psql, Error 2, integration | - |
| `git-01` | `recall` | `git` | `2117.48` | `0.972` | `0.647` | `+0.325` | `1.000` | `0.887` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `git-02` | `recall` | `git` | `3146.05` | `0.984` | `0.656` | `+0.329` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `git-03` | `recall` | `git` | `63145.93` | `0.859` | `0.580` | `+0.278` | `1.000` | `0.945` | `1.000` | `0.773` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `7500.75` | `0.990` | `0.661` | `+0.328` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `curl-02` | `recall` | `curl` | `7850.92` | `0.984` | `0.656` | `+0.328` | `1.000` | `0.934` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ssh-01` | `summary` | `ssh` | `12339.37` | `0.488` | `0.487` | `+0.001` | `0.524` | `0.892` | `0.500` | `0.432` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | Permission denied (publickey), fatal: Could not read from remote repository. | - |
| `ssh-02` | `summary` | `ssh` | `5182.70` | `0.965` | `0.640` | `+0.325` | `1.000` | `0.913` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `7231.28` | `0.972` | `0.647` | `+0.325` | `1.000` | `0.930` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `13680.01` | `0.780` | `0.610` | `+0.171` | `0.857` | `0.884` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | api.service | - |
| `apt-01` | `summary` | `apt` | `5441.61` | `0.977` | `0.643` | `+0.334` | `1.000` | `0.942` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `7773.93` | `0.990` | `0.658` | `+0.332` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `10727.92` | `0.971` | `0.646` | `+0.325` | `1.000` | `0.928` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `6648.65` | `0.984` | `0.656` | `+0.327` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `javac-01` | `recall` | `javac` | `9353.10` | `0.984` | `0.655` | `+0.329` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `maven-01` | `recall` | `maven` | `10822.08` | `0.988` | `0.656` | `+0.333` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `maven-02` | `summary` | `maven` | `12003.05` | `0.990` | `0.661` | `+0.329` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `6428.66` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `5537.36` | `0.672` | `0.514` | `+0.158` | `0.389` | `0.858` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ./gradlew test, Execution failed for task ':test' | - |
| `cargo-01` | `recall` | `cargo` | `10031.72` | `0.971` | `0.638` | `+0.333` | `1.000` | `0.923` | `1.000` | `0.982` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `cargo-02` | `recall` | `cargo` | `9967.36` | `0.984` | `0.655` | `+0.329` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `33667.98` | `0.589` | `0.589` | `+0.000` | `1.000` | `0.892` | `0.500` | `0.411` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `npm-04` | `summary` | `npm` | `25885.35` | `0.670` | `0.519` | `+0.151` | `0.684` | `0.906` | `1.000` | `0.865` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ERESOLVE, dashboard-web@0.9.0 | - |
| `tsc-01` | `summary` | `tsc` | `14961.64` | `0.976` | `0.646` | `+0.330` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `9880.24` | `0.985` | `0.658` | `+0.327` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-runtime-01` | `recall` | `python-runtime` | `2165.92` | `0.993` | `0.664` | `+0.329` | `1.000` | `0.971` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `6101.55` | `0.986` | `0.658` | `+0.327` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `7423.22` | `0.969` | `0.631` | `+0.339` | `1.000` | `0.939` | `1.000` | `0.992` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `17708.06` | `0.660` | `0.503` | `+0.157` | `0.311` | `0.872` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund, failed to solve | - |
| `docker-compose-04` | `summary` | `docker-compose` | `19428.19` | `0.557` | `0.417` | `+0.140` | `0.133` | `0.883` | `1.000` | `0.879` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | docker compose up --build, 0.0.0.0:8080, port is already allocated | - |
| `kubectl-05` | `summary` | `kubectl` | `3911.15` | `0.983` | `0.655` | `+0.328` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `10702.38` | `0.827` | `0.649` | `+0.179` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `3949.60` | `0.990` | `0.662` | `+0.328` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `25000.71` | `0.514` | `0.387` | `+0.127` | `0.424` | `0.866` | `1.000` | `0.792` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | terraform plan -lock-timeout=5s -out=tfplan, Error acquiring the state lock | - |
| `terraform-06` | `summary` | `terraform` | `7366.40` | `0.794` | `0.620` | `+0.174` | `0.867` | `0.918` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Reference to undeclared resource | - |
| `terraform-07` | `summary` | `terraform` | `11159.30` | `0.600` | `0.452` | `+0.148` | `0.267` | `0.896` | `1.000` | `0.898` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | terraform plan -detailed-exitcode -no-color, Plan: 1 to add, 1 to change, 0 to destroy. | - |
| `nginx-01` | `summary` | `nginx` | `6446.75` | `0.986` | `0.649` | `+0.337` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `4982.05` | `0.987` | `0.657` | `+0.330` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `2819.84` | `0.674` | `0.515` | `+0.159` | `0.600` | `0.891` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | psql -h 127.0.0.1 -U app_user -d appdb -c 'select 1' | - |
| `postgres-02` | `summary` | `postgres` | `7147.05` | `0.514` | `0.514` | `-0.000` | `0.353` | `0.883` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | migrations/202605160830_add_users.sql:42, relation "users" already exists, ROLLBACK | - |
| `mysql-01` | `summary` | `mysql` | `11549.93` | `0.989` | `0.651` | `+0.338` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `9706.98` | `0.985` | `0.658` | `+0.327` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `17802.72` | `0.935` | `0.614` | `+0.321` | `1.000` | `0.948` | `1.000` | `0.940` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `3349.90` | `0.990` | `0.660` | `+0.329` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `7898.02` | `0.916` | `0.611` | `+0.304` | `1.000` | `0.890` | `1.000` | `0.900` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `47001.10` | `0.804` | `0.540` | `+0.264` | `1.000` | `0.909` | `1.000` | `0.777` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `3183.41` | `0.967` | `0.640` | `+0.326` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `make-01` | `summary` | `make` | `8281.31` | `0.611` | `0.000` | `+0.611` | `0.093` | `0.864` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | make CFLAGS='-O2 -Wall -Werror' all, src/parser.c:214:12, Makefile:22, Error 1 | - |
| `tar-01` | `summary` | `tar` | `5957.59` | `0.984` | `0.652` | `+0.331` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `5240.59` | `0.991` | `0.662` | `+0.329` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `4028.56` | `0.628` | `0.476` | `+0.152` | `0.167` | `0.869` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | rsync -av --delete build/ artifact-store/build/, code 24, some files vanished before they could be transferred | - |
| `test-failure-01` | `recall` | `test-failure` | `5102.23` | `0.990` | `0.663` | `+0.327` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `33964.90` | `0.650` | `0.651` | `-0.001` | `1.000` | `0.895` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | fenced_output_wrapper | - | - |
| `ci-log-01` | `recall` | `ci-log` | `15939.89` | `0.726` | `0.557` | `+0.168` | `0.706` | `0.946` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Invalid value: "" | - |
| `package-manager-01` | `recall` | `package-manager` | `23389.83` | `0.725` | `0.558` | `+0.167` | `0.704` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | npm ERR! code ERESOLVE, peer vite@"^4.0.0 || ^5.0.0" | - |
| `test-summary-01` | `summary` | `test-summary` | `14150.09` | `0.982` | `0.655` | `+0.327` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `build-log-01` | `summary` | `build-log` | `8002.78` | `0.956` | `0.638` | `+0.318` | `1.000` | `0.890` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `13203.65` | `0.572` | `0.485` | `+0.087` | `1.000` | `0.906` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `5139.28` | `0.510` | `0.000` | `+0.510` | `1.000` | `0.637` | `0.400` | `0.400` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `6120.48` | `0.609` | `0.000` | `+0.609` | `1.000` | `0.722` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `4748.88` | `0.679` | `0.000` | `+0.679` | `0.129` | `0.291` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | search endpoint failed after 2 attempts, https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `19445.87` | `0.705` | `0.000` | `+0.705` | `0.500` | `0.803` | `1.000` | `0.964` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | /work/app/api/routes.py, 21, reportUndefinedVariable | - |
| `structured-output-02` | `structured` | `structured-output` | `12260.61` | `0.000` | `0.000` | `+0.000` | `0.905` | `0.756` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | port 5432 is already allocated | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml - job: test / integration step: Start docker compose exit_code: 1 cause: Bind for 0.0.0.0:5432 failed: port is already allocated - job: deploy / prev...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml - job: test / integration step: Start docker compose exit_code: 1 cause: Bind for 0.0.0.0:5432 failed: port is already allocated - job: deploy / prev...' |
| `structured-output-03` | `structured` | `structured-output` | `10329.34` | `0.824` | `0.000` | `+0.824` | `0.929` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | "invalid refresh token" | - |
| `structured-output-04` | `structured` | `structured-output` | `6053.50` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `5557.03` | `0.850` | `0.000` | `+0.850` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | verbatim_alignment_weak | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `7922.33` | `0.499` | `0.000` | `+0.499` | `0.714` | `0.429` | `0.683` | `0.540` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | SearchBox debounces network query before fetch | - |
| `exact-format-03` | `exact_format` | `exact-format` | `6248.39` | `0.570` | `0.000` | `+0.570` | `1.000` | `0.335` | `0.617` | `0.524` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `20266.95` | `0.713` | `0.000` | `+0.713` | `0.556` | `0.875` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | has no attribute 'dumps', shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `10249.23` | `0.757` | `0.589` | `+0.169` | `0.750` | `0.884` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `7718.72` | `0.582` | `0.000` | `+0.582` | `1.000` | `0.617` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `3648.04` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `13319.87` | `0.984` | `0.652` | `+0.332` | `1.000` | `0.936` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `14566.42` | `0.522` | `0.382` | `+0.140` | `0.190` | `0.914` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | module.worker.aws_iam_policy.worker_inline, status code: 409, request id: 0f3e2b11-9ac9-4fd2-a3bb-6c07a3c6a90d, modules/worker/iam.tf line 27 | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `9100.81` | `0.980` | `0.654` | `+0.327` | `1.000` | `0.922` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `11564.04` | `0.684` | `0.523` | `+0.160` | `0.600` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | registry.example.com/api:2026.05.18-1, Exit Code: 78 | - |
| `go-test-02` | `recall` | `go-test` | `8021.95` | `0.694` | `0.529` | `+0.165` | `0.630` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | (*Store).Set(), (*Store).Get() | - |
| `cargo-03` | `recall` | `cargo` | `20608.98` | `0.603` | `0.600` | `+0.003` | `0.897` | `0.900` | `0.500` | `0.480` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | could not compile `storage` | - |
| `docker-compose-05` | `recall` | `docker-compose` | `7399.00` | `0.988` | `0.659` | `+0.328` | `1.000` | `0.951` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `6148.48` | `0.988` | `0.660` | `+0.328` | `1.000` | `0.951` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `12435.06` | `0.428` | `0.300` | `+0.128` | `0.000` | `0.890` | `1.000` | `0.959` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | packages/db migrate.test.ts, 20260518_add_workspace_limits.sql, relation "workspace_limits" already exists, packages/db/src/migrate.ts:77:13, packages/db/test/migrate.test.ts:44:7, exit code 1 | - |
| `pnpm-04` | `recall` | `pnpm` | `7418.11` | `0.988` | `0.657` | `+0.331` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `9116.91` | `0.962` | `0.639` | `+0.323` | `1.000` | `0.889` | `1.000` | `0.982` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `7996.55` | `0.982` | `0.655` | `+0.327` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `9617.03` | `0.544` | `0.397` | `+0.147` | `0.235` | `0.936` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | events, already exists, 20260518093012_add_index_to_events_request_id.rb:3, ArgumentError | - |
| `phpunit-01` | `recall` | `phpunit` | `13754.93` | `0.993` | `0.000` | `+0.993` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `6085.69` | `0.989` | `0.656` | `+0.333` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `13902.38` | `0.462` | `0.462` | `+0.001` | `0.500` | `0.901` | `0.500` | `0.466` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | psql:dump.sql:418, ROLLBACK | - |
| `ansible-02` | `recall` | `ansible` | `13215.95` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.949` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `5568.18` | `0.976` | `0.653` | `+0.322` | `1.000` | `0.902` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `10469.05` | `0.446` | `0.313` | `+0.133` | `0.000` | `0.897` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | .\scripts\release.ps1 -Version 1.4.2, cannot be loaded because running scripts is disabled, PSSecurityException, FullyQualifiedErrorId : UnauthorizedAccess | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `8494.45` | `0.960` | `0.636` | `+0.324` | `1.000` | `0.937` | `1.000` | `0.958` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `6540.88` | `0.642` | `0.486` | `+0.156` | `0.174` | `0.903` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | tests/payments, tests/refunds, tests/payments/test_webhook.py::test_replays_duplicate_event, RuntimeError | - |
| `go-test-03` | `summary` | `go-test` | `34830.53` | `0.923` | `0.000` | `+0.923` | `1.000` | `0.909` | `1.000` | `0.944` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `npm-05` | `summary` | `npm` | `11466.78` | `0.968` | `0.645` | `+0.323` | `1.000` | `0.919` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `8783.51` | `0.591` | `0.446` | `+0.146` | `0.125` | `0.867` | `1.000` | `0.952` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | template, api/templates/deployment.yaml:42:29, executing, api/templates/deployment.yaml | - |
| `ruff-04` | `summary` | `ruff` | `5875.49` | `0.958` | `0.637` | `+0.321` | `1.000` | `0.894` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `10885.23` | `0.688` | `0.529` | `+0.159` | `0.478` | `0.850` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | checks, http_req_duration, avg | - |
| `composer-01` | `summary` | `composer` | `3630.38` | `0.755` | `0.590` | `+0.165` | `0.800` | `0.847` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Loading | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `3735.01` | `0.944` | `0.619` | `+0.325` | `1.000` | `0.859` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `make-02` | `summary` | `make` | `7444.89` | `0.600` | `0.600` | `-0.000` | `0.773` | `0.910` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | build/server.o | - |
| `python-pytest-02` | `summary` | `python-pytest` | `9059.02` | `0.969` | `0.646` | `+0.323` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `9008.13` | `0.631` | `0.632` | `-0.000` | `1.000` | `0.873` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `dbt-01` | `summary` | `dbt` | `6990.63` | `0.790` | `0.616` | `+0.175` | `0.833` | `0.929` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `8490.40` | `0.965` | `0.642` | `+0.323` | `1.000` | `0.912` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `8136.61` | `0.643` | `0.488` | `+0.155` | `0.200` | `0.892` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | deploy, Total, Upload, 183.22 | - |
| `python-pytest-04` | `summary` | `python-pytest` | `6822.39` | `0.973` | `0.643` | `+0.330` | `1.000` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `8998.32` | `0.248` | `0.000` | `+0.248` | `1.000` | `0.630` | `0.118` | `0.096` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `5351.32` | `0.973` | `0.000` | `+0.973` | `1.000` | `0.911` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `3647.59` | `0.850` | `0.000` | `+0.850` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | verbatim_alignment_weak | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `4182.57` | `0.888` | `0.000` | `+0.888` | `1.000` | `0.675` | `1.000` | `0.957` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `2520.99` | `0.597` | `0.000` | `+0.597` | `1.000` | `0.675` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `4377.79` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `6024.26` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.336` | `0.487` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='- pnpm install --frozen-lockfile - ERR_PNPM_LOCKFILE_CONFIG_MISMATCH - exit code: 1' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='- pnpm install --frozen-lockfile - ERR_PNPM_LOCKFILE_CONFIG_MISMATCH - exit code: 1 - [deps 4/4]' |
| `terraform-09` | `instruction_following` | `terraform` | `2896.72` | `0.483` | `0.000` | `+0.483` | `1.000` | `0.752` | `0.333` | `0.333` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `3424.04` | `0.966` | `0.000` | `+0.966` | `1.000` | `0.888` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `3338.02` | `0.401` | `0.000` | `+0.401` | `1.000` | `0.682` | `0.250` | `0.250` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `1748.85` | `0.850` | `0.000` | `+0.850` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | verbatim_alignment_weak | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `3527.39` | `0.646` | `0.000` | `+0.646` | `1.000` | `0.000` | `0.735` | `0.735` | `0.000` | `0.000` | `soft_accepted` | `rejected` | verbatim_alignment_weak | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `6906.74` | `0.468` | `0.000` | `+0.468` | `1.000` | `0.685` | `0.333` | `0.333` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `1674.04` | `0.273` | `0.000` | `+0.273` | `0.357` | `0.287` | `0.397` | `0.397` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | rsync, /var/backups/uploads, exit code 23 | - |
| `pyright-01` | `structured` | `pyright` | `20701.78` | `0.687` | `0.000` | `+0.687` | `1.000` | `0.725` | `0.667` | `0.595` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `6109.11` | `0.000` | `0.000` | `+0.000` | `0.167` | `0.470` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | add, aws_iam_role.app, change, aws_lambda_function.api, field | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "aws_iam_role": { "app" }, "resource": { "memory_size": 1024 } } ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "aws_iam_role": { "app" }, "resource": { "memory_size": 1024 } } ```' |
| `junit-01` | `structured` | `junit` | `3653.72` | `0.944` | `0.000` | `+0.944` | `1.000` | `0.814` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `18551.79` | `0.000` | `0.000` | `+0.000` | `0.571` | `0.368` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | name, status, restarts | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml - healthy_pods: - NAME: worker-884b READY: 1/1 STATUS: Running RESTARTS: 0 AGE: 12m - unhealthy_pods: - NAME: api-77df READY: 0/1 STATUS: CrashLoopBa...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml unhealthy_pods: - NAME: api-77df READY: 0/1 STATUS: CrashLoopBackOff RESTARTS: 5 - NAME: search-0 READY: 0/1 STATUS: ImagePullBackOff RESTARTS: 0 ```' |
| `eslint-06` | `structured` | `eslint` | `4803.32` | `0.702` | `0.000` | `+0.702` | `1.000` | `0.196` | `0.875` | `0.875` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `5131.71` | `0.664` | `0.000` | `+0.664` | `0.704` | `0.658` | `0.875` | `0.875` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | builder, build | - |
| `go-test-04` | `structured` | `go-test` | `11725.39` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.867` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml - failed_tests: - TestParseAmount - TestFormatCurrency name: TestParseAmount TestParseAmount: location: amount_test.go:22 message: got 10.0 want 10.0...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml - failed_tests: - TestParseAmount - TestFormatCurrency name: TestParseAmount location: amount_test.go:22 message: got 10.0 want 10.00 - name: TestFor...' |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `5087.70` | `0.823` | `0.000` | `+0.823` | `1.000` | `0.633` | `1.000` | `0.800` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `npm-07` | `structured` | `npm` | `6780.38` | `0.630` | `0.000` | `+0.630` | `1.000` | `0.362` | `0.667` | `0.667` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `11261.21` | `0.231` | `0.000` | `+0.231` | `1.000` | `0.957` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `4010.63` | `0.099` | `0.000` | `+0.099` | `0.697` | `0.177` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | :api:compileJava | - |
| `playwright-02` | `structured` | `playwright` | `3840.38` | `0.311` | `0.000` | `+0.311` | `1.000` | `0.179` | `0.266` | `0.266` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `5099.69` | `0.540` | `0.000` | `+0.540` | `1.000` | `0.391` | `0.521` | `0.521` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `vite-01` | `structured` | `vite` | `8196.99` | `0.104` | `0.000` | `+0.104` | `1.000` | `0.181` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `8998.61` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.000` | `0.635` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_lines_contract_breakage | - | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo', 'exact_lines_contract_breakage'] first_pass='- return the exact requested lines or quoted excerpts only - copy quoted or extracted lines exactly from the raw output - do not summarize unless the instruc...' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='```python tests/test_a.py::test_one tests/test_b.py::TestB::test_three ```' |
| `git-04` | `exact_format` | `git` | `2646.28` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `7415.41` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `643.45` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `1754.21` | `0.596` | `0.000` | `+0.596` | `1.000` | `0.664` | `0.575` | `0.575` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `1893.06` | `0.254` | `0.000` | `+0.254` | `0.500` | `0.304` | `0.350` | `0.350` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | prod | - |
| `cargo-05` | `exact_format` | `cargo` | `1980.56` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `486.24` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `5198.75` | `0.201` | `0.000` | `+0.201` | `1.000` | `0.258` | `0.220` | `0.158` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `6470.17` | `0.677` | `0.518` | `+0.159` | `0.444` | `0.839` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | /repo/scripts/email.py | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `8073.10` | `0.639` | `0.486` | `+0.153` | `0.222` | `0.865` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | string | null, url: string | - |
| `postgres-05` | `explanation` | `postgres` | `11244.64` | `0.706` | `0.000` | `+0.706` | `0.667` | `0.658` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | orders_customer_id_fkey | - |
| `docker-build-05` | `explanation` | `docker-build` | `7258.22` | `0.744` | `0.578` | `+0.167` | `0.636` | `0.916` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | COPY | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `3427.20` | `0.967` | `0.646` | `+0.321` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `10076.21` | `0.642` | `0.492` | `+0.150` | `0.250` | `0.856` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | E0515, returns a reference | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `6597.02` | `0.714` | `0.553` | `+0.161` | `0.583` | `0.860` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `4473.18` | `0.984` | `0.656` | `+0.328` | `1.000` | `0.936` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `8807.87` | `0.928` | `0.620` | `+0.308` | `1.000` | `0.940` | `1.000` | `0.900` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `6881.94` | `0.596` | `0.454` | `+0.142` | `0.545` | `0.933` | `1.000` | `0.850` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | /usr/src/app/index.js:12:15 | - |
| `package-management-01` | `recall` | `package-management` | `4769.54` | `0.974` | `0.644` | `+0.330` | `1.000` | `0.898` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `2748.45` | `0.979` | `0.652` | `+0.327` | `1.000` | `0.916` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `7241.88` | `0.865` | `0.584` | `+0.281` | `1.000` | `0.908` | `1.000` | `0.800` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `5884.22` | `0.952` | `0.634` | `+0.318` | `1.000` | `0.923` | `1.000` | `0.950` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `1839.59` | `0.967` | `0.644` | `+0.323` | `1.000` | `0.868` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `5030.21` | `0.375` | `0.260` | `+0.115` | `0.000` | `0.879` | `1.000` | `0.826` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | COPY failed, no such file or directory | - |
| `deployment-01` | `recall` | `deployment` | `3172.83` | `0.516` | `0.371` | `+0.145` | `0.222` | `0.897` | `1.000` | `0.965` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | cannot be handled as a Pod, Name: name not present | - |
| `infrastructure-01` | `recall` | `infrastructure` | `4317.30` | `0.927` | `0.616` | `+0.310` | `1.000` | `0.909` | `1.000` | `0.912` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `2628.29` | `0.656` | `0.498` | `+0.157` | `0.524` | `0.942` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | src/app.ts:10:3 | - |
| `ci-02` | `recall` | `ci` | `2361.47` | `0.973` | `0.648` | `+0.325` | `1.000` | `0.892` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `build-01` | `recall` | `build` | `7162.56` | `0.921` | `0.614` | `+0.307` | `1.000` | `0.891` | `1.000` | `0.909` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `881.43` | `0.981` | `0.653` | `+0.328` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `4889.92` | `0.655` | `0.499` | `+0.157` | `0.636` | `0.866` | `1.000` | `0.940` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | package com.google.common does not exist | - |
| `infrastructure-02` | `recall` | `infrastructure` | `2214.05` | `0.970` | `0.643` | `+0.327` | `1.000` | `0.881` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `2304.79` | `0.991` | `0.658` | `+0.332` | `1.000` | `0.962` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `1177.88` | `0.969` | `0.644` | `+0.325` | `1.000` | `0.876` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `5597.77` | `0.539` | `0.402` | `+0.137` | `0.364` | `0.927` | `1.000` | `0.877` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | COPY failed | - |
| `testing-04` | `recall` | `testing` | `3985.38` | `0.763` | `0.593` | `+0.170` | `0.833` | `0.889` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | User signs in | - |
| `build-02` | `recall` | `build` | `4129.11` | `0.901` | `0.603` | `+0.299` | `1.000` | `0.891` | `1.000` | `0.874` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `5581.93` | `0.833` | `0.653` | `+0.180` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `732.29` | `0.980` | `0.649` | `+0.331` | `1.000` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `build-03` | `summary` | `build` | `2752.70` | `0.906` | `0.594` | `+0.312` | `1.000` | `0.902` | `1.000` | `0.925` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `1153.64` | `0.945` | `0.000` | `+0.945` | `1.000` | `0.862` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `1244.26` | `0.961` | `0.637` | `+0.324` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `1548.22` | `0.952` | `0.632` | `+0.320` | `1.000` | `0.880` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `2294.48` | `0.889` | `0.561` | `+0.328` | `1.000` | `0.941` | `1.000` | `0.880` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `4386.78` | `0.881` | `0.574` | `+0.307` | `1.000` | `0.823` | `1.000` | `0.933` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `3663.49` | `0.547` | `0.000` | `+0.547` | `1.000` | `0.627` | `0.500` | `0.450` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `3050.23` | `0.379` | `0.000` | `+0.379` | `0.500` | `0.413` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | ERROR: | - |
| `ci-05` | `instruction_following` | `ci` | `3344.08` | `0.479` | `0.000` | `+0.479` | `1.000` | `0.846` | `0.500` | `0.400` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `4641.05` | `0.142` | `0.000` | `+0.142` | `1.000` | `0.185` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `9479.12` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.957` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml - kind: Service metadata: name: my-service namespace: default spec: clusterIP: 10.0.0.1 ports: - port: 80 protocol: TCP ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml - kind: Service metadata: name: my-service namespace: default spec: clusterIP: 10.0.0.1 ports: - port: 80 protocol: TCP ```' |
| `deployment-02` | `structured` | `deployment` | `1503.13` | `0.209` | `0.000` | `+0.209` | `1.000` | `0.741` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `network-01` | `exact_format` | `network` | `1321.53` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `2813.03` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.579` | `0.570` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response INFO: Retrying... ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response' |
| `shell-03` | `exact_format` | `shell` | `1149.16` | `0.307` | `0.000` | `+0.307` | `0.000` | `1.000` | `0.617` | `0.617` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors, verbatim_alignment_weak | OUTPUT: | - |
| `shell-04` | `exact_format` | `shell` | `324.13` | `0.191` | `0.000` | `+0.191` | `1.000` | `0.320` | `0.150` | `0.150` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `build-04` | `exact_format` | `build` | `4054.98` | `0.640` | `0.000` | `+0.640` | `1.000` | `0.250` | `0.688` | `0.688` | `0.000` | `0.000` | `soft_accepted` | `rejected` | verbatim_alignment_weak | - | - |
| `build-05` | `exact_format` | `build` | `455.57` | `0.730` | `0.000` | `+0.730` | `1.000` | `0.333` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `1205.33` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `2266.72` | `0.948` | `0.000` | `+0.948` | `1.000` | `0.870` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `2040.94` | `0.937` | `0.619` | `+0.318` | `1.000` | `0.843` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `2056.32` | `0.715` | `0.547` | `+0.168` | `0.500` | `0.915` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | pull access denied | - |
| `runtime-05` | `explanation` | `runtime` | `2419.01` | `0.963` | `0.000` | `+0.963` | `1.000` | `0.908` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `ci-06` | `explanation` | `ci` | `1348.02` | `0.650` | `0.000` | `+0.650` | `0.333` | `0.829` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | SIGSEGV | - |
| `runtime-06` | `explanation` | `runtime` | `1723.27` | `0.945` | `0.000` | `+0.945` | `1.000` | `0.863` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `1940.69` | `0.598` | `0.446` | `+0.152` | `0.000` | `0.884` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | password authentication failed | - |
| `explanation-01` | `explanation` | `explanation` | `2464.42` | `0.944` | `0.000` | `+0.944` | `1.000` | `0.861` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `2006.51` | `0.955` | `0.636` | `+0.319` | `1.000` | `0.888` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `2207.28` | `0.617` | `0.463` | `+0.154` | `0.000` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | no configured push destination | - |
| `explanation-04` | `explanation` | `explanation` | `2038.59` | `0.950` | `0.629` | `+0.321` | `1.000` | `0.875` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `2489.64` | `0.615` | `0.461` | `+0.154` | `0.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | command not found | - |
| `explanation-06` | `explanation` | `explanation` | `2063.57` | `0.939` | `0.000` | `+0.939` | `1.000` | `0.847` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `2431.75` | `0.591` | `0.443` | `+0.148` | `0.000` | `0.862` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | SECRET_KEY setting must not be empty | - |
| `explanation-08` | `explanation` | `explanation` | `1526.83` | `0.936` | `0.000` | `+0.936` | `1.000` | `0.841` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `4423.67` | `0.596` | `0.440` | `+0.156` | `0.000` | `0.878` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | would be overwritten by merge | - |
| `explanation-10` | `explanation` | `explanation` | `2358.56` | `0.605` | `0.438` | `+0.167` | `0.000` | `0.905` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | KeyError: 'API_KEY' | - |
| `explanation-11` | `explanation` | `explanation` | `2013.47` | `0.933` | `0.000` | `+0.933` | `1.000` | `0.833` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `2099.97` | `0.946` | `0.000` | `+0.946` | `1.000` | `0.865` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `ci-07` | `structured` | `ci` | `9645.19` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.957` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml - kind: Service metadata: name: my-service namespace: default spec: clusterIP: 10.0.0.1 ports: - port: 80 protocol: TCP ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml - kind: Service metadata: name: my-service namespace: default spec: clusterIP: 10.0.0.1 ports: - port: 80 protocol: TCP ```' |
| `linting-03` | `structured` | `linting` | `1424.69` | `0.209` | `0.000` | `+0.209` | `1.000` | `0.741` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `network-02` | `exact_format` | `network` | `1066.60` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `1292.24` | `0.729` | `0.000` | `+0.729` | `1.000` | `0.319` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `542.28` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `build-06` | `exact_format` | `build` | `4059.29` | `0.640` | `0.000` | `+0.640` | `1.000` | `0.250` | `0.688` | `0.688` | `0.000` | `0.000` | `soft_accepted` | `rejected` | verbatim_alignment_weak | - | - |
| `runtime-07` | `exact_format` | `runtime` | `944.42` | `0.516` | `0.000` | `+0.516` | `1.000` | `0.319` | `0.560` | `0.476` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `build-07` | `exact_format` | `build` | `2010.00` | `0.314` | `0.000` | `+0.314` | `1.000` | `0.475` | `0.290` | `0.290` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `414.12` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `2204.07` | `0.948` | `0.000` | `+0.948` | `1.000` | `0.870` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `2045.14` | `0.937` | `0.619` | `+0.318` | `1.000` | `0.843` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `1973.88` | `0.966` | `0.641` | `+0.325` | `1.000` | `0.915` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `4769.25` | `0.569` | `0.422` | `+0.147` | `0.000` | `0.938` | `1.000` | `0.917` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | cannot list resource "pods" | - |
| `explanation-14` | `explanation` | `explanation` | `1915.10` | `0.598` | `0.446` | `+0.152` | `0.000` | `0.884` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | password authentication failed | - |
| `explanation-15` | `explanation` | `explanation` | `1783.04` | `0.971` | `0.645` | `+0.326` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `1702.06` | `0.930` | `0.000` | `+0.930` | `1.000` | `0.825` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `2286.06` | `0.606` | `0.443` | `+0.163` | `0.000` | `0.908` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | missing script: start | - |
| `package-management-04` | `explanation` | `package-management` | `2584.00` | `0.695` | `0.528` | `+0.167` | `0.444` | `0.890` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | nonexistent (invalid) version of flask | - |
