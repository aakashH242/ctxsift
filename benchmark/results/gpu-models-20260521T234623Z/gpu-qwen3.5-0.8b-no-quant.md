# gpu-qwen3.5-0.8b-no-quant

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

- load_ms: `36909.98`
- cpu_rss_bytes: `3056939008`
- gpu_peak_bytes: `2771878912`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `235`
- accepted_count: `193`
- soft_accepted_count: `42`
- rejected_count: `45`
- exact_pass_count: `200`
- avg_inference_ms: `5506.16`
- p95_inference_ms: `21720.19`
- avg_exact_preservation_ratio: `0.798`
- avg_summary_quality_ratio: `0.726`
- avg_format_adherence_score: `0.752`
- avg_instruction_following_score: `0.736`
- avg_brevity_ratio: `0.917`
- avg_case_score: `0.731`
- p10_case_score: `0.000`
- quality_core: `0.584`
- latency_factor: `0.859`
- final_score: `50.21`
- peak_cpu_rss_bytes: `3057496064`
- peak_gpu_bytes: `2911623680`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `34068.79` | `0.689` | `1.000` | `0.898` | `0.500` | `0.404` | `0.358` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-02` | `summary` | `python` | `9939.01` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- python services/worker.py --queue emails --concurrency 4 - /workspace/services/worker.py - line 11 - ModuleNotFoundError - dramatiq_abort - worker boot fai...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass="$ python services/worker.py --queue emails --concurrency 4 INFO boot: reading .env.local WARNING redis retry 1/3 failed: ConnectionResetError(104, 'Connectio..." |
| `python-03` | `recall` | `python` | `2054.75` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `2761.49` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `2582.03` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `2817.22` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `3370.12` | `0.681` | `0.326` | `0.924` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/integration -k billing -vv --maxfail=1, tests/integration/test_billing_api.py::test_invoice_webhook_uses_signature, 1 error in 2.31s | - |
| `pytest-03` | `recall` | `pytest` | `3502.98` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `2546.45` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `2167.17` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `2155.91` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `2080.51` | `0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `4205.12` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `1972.79` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-02` | `summary` | `ruff` | `1748.24` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `1758.12` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `1791.63` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `2866.58` | `0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `2188.77` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `1978.63` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `1897.83` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `1532.57` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `6246.46` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `2375.03` | `0.979` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `3524.01` | `0.785` | `0.800` | `0.934` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Lifecycle script `build` failed, storefront@2.8.1 | - |
| `pnpm-01` | `recall` | `pnpm` | `1887.23` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `8193.81` | `0.979` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `2538.31` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `3544.36` | `0.983` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `2652.74` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `16214.44` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | tsc src/index.ts src/http.ts --pretty false, src/index.ts(48,20), TS2769, URL, RequestInit, src/http.ts(9,17) | qwen3.5 output validation failed: model did not stop thinking before reaching the output limit. first_pass="- tsc src/index.ts src/http.ts --pretty false - src/index.ts(48,20): error TS2769: No overload matches this call. Overload 1 of 2, '(url: string, init?: Requ..." repair_pass="- tsc src/index.ts src/http.ts --pretty false - src/index.ts(48,20): error TS2769: No overload matches this call. Overload 1 of 2, '(url: string, init?: Requ..." |
| `eslint-01` | `recall` | `eslint` | `6720.79` | `0.809` | `0.920` | `0.949` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Unused eslint-disable directive | - |
| `eslint-02` | `summary` | `eslint` | `1707.89` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `3497.53` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `22401.02` | `0.888` | `1.000` | `0.872` | `1.000` | `0.759` | `0.197` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `1745.29` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `3169.80` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `1307.02` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `3587.10` | `0.795` | `0.875` | `0.968` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | demo-app-1 | - |
| `docker-compose-03` | `summary` | `docker-compose` | `5386.88` | `0.737` | `0.600` | `0.919` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker compose up api | - |
| `kubectl-01` | `summary` | `kubectl` | `1887.54` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `24072.17` | `0.905` | `1.000` | `0.947` | `1.000` | `0.756` | `0.186` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `1570.52` | `0.995` | `1.000` | `0.988` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `19524.44` | `0.916` | `1.000` | `0.925` | `1.000` | `0.803` | `0.342` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `1623.70` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `7843.03` | `0.958` | `1.000` | `0.924` | `1.000` | `0.931` | `0.771` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `5173.71` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `2094.88` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `5569.40` | `0.956` | `1.000` | `0.931` | `1.000` | `0.921` | `0.735` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `6068.50` | `0.963` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `25686.08` | `0.694` | `1.000` | `0.906` | `0.500` | `0.411` | `0.404` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `git-02` | `recall` | `git` | `11500.09` | `0.905` | `1.000` | `0.867` | `1.000` | `0.816` | `0.386` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `2693.87` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `3289.44` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `7067.03` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | curl -I https://docs.example.com/sdk/latest, HTTP/2 301, location: /sdk/v3.4/, cache-control: max-age=3600 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='curl -I https://docs.example.com/sdk/latest HTTP/2 301 location: /sdk/v3.4/ cache-control: max-age=3600 server: envoy via: 1.1 edge x-request-id: 7e9f7a4d<|i...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='curl -I https://docs.example.com/sdk/latest HTTP/2 301 location: /sdk/v3.4/ cache-control: max-age=3600 server: envoy via: 1.1 edge x-request-id: 7e9f7a4d<|i...' |
| `ssh-01` | `summary` | `ssh` | `4562.03` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `1955.27` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `2334.49` | `0.760` | `0.677` | `0.936` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | status=203/EXEC | - |
| `systemd-02` | `summary` | `systemd` | `1526.62` | `0.962` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `1847.29` | `0.977` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `11109.14` | `0.943` | `1.000` | `0.951` | `1.000` | `0.864` | `0.548` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `12463.88` | `0.962` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `22483.48` | `0.914` | `1.000` | `0.936` | `1.000` | `0.880` | `0.600` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `41432.92` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `8389.55` | `0.594` | `0.304` | `0.931` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | mvn -q test, UserControllerTest.java:72, /workspace/webapp/target/surefire-reports | - |
| `maven-02` | `summary` | `maven` | `2130.83` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `2068.61` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `9045.48` | `0.895` | `1.000` | `0.916` | `1.000` | `0.858` | `0.525` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `9529.58` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `1468.31` | `0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `14916.69` | `0.612` | `0.737` | `0.936` | `0.500` | `0.432` | `0.548` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | node dist/server.js | - |
| `npm-04` | `summary` | `npm` | `2006.32` | `0.974` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `4908.76` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `1906.95` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `3341.20` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `3200.50` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `5183.50` | `0.972` | `1.000` | `0.939` | `1.000` | `0.992` | `0.972` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `5226.68` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund, Dockerfile:8, zod@3.23.8, failed to solve | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='- failed to solve: process "/bin/sh -c npm ci --no-audit --no-fund" did not complete successfully: exit code: 1 - Missing: zod@3.23.8 from lock file - Missin...' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='- docker build -t example/web:dev . - RUN npm ci --no-audit --no-fund - Dockerfile:8 - zod@3.23.8 - failed to solve<|im_end|>' |
| `docker-compose-04` | `summary` | `docker-compose` | `1630.39` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `1329.82` | `0.982` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `29359.17` | `0.827` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `2745.57` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `3184.90` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `3494.74` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `3429.56` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `2421.19` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `5856.04` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `4090.99` | `0.684` | `0.600` | `0.939` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | psql -h 127.0.0.1 -U app_user -d appdb -c 'select 1' | - |
| `postgres-02` | `summary` | `postgres` | `10571.28` | `0.963` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `2734.44` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `2854.22` | `0.732` | `0.667` | `0.861` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mysql -h db.example.net -u app -D appdb -e "SELECT id, createdAt FROM users LIMIT 5" | - |
| `redis-01` | `summary` | `redis` | `4361.24` | `0.951` | `1.000` | `0.952` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `1719.13` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `6437.58` | `0.679` | `0.619` | `0.879` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | line=91, Ruff F821 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `21428.41` | `0.859` | `1.000` | `0.927` | `1.000` | `0.777` | `0.255` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `1328.75` | `0.968` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `2033.59` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `4107.50` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `1717.56` | `0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `1947.86` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `2773.36` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `34860.63` | `0.634` | `0.851` | `0.904` | `0.500` | `0.405` | `0.369` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | src/router.rs:128 | - |
| `ci-log-01` | `recall` | `ci-log` | `10835.50` | `0.960` | `1.000` | `0.927` | `1.000` | `0.936` | `0.786` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `18046.41` | `0.917` | `1.000` | `0.949` | `1.000` | `0.790` | `0.301` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `23246.77` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-log-01` | `summary` | `build-log` | `6236.92` | `0.739` | `0.562` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | InvoiceMapper.java:[58,29], cannot find symbol | - |
| `docker-build-02` | `summary` | `docker-build` | `21427.68` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | Dockerfile:18, COPY apps/web ./apps/web, "/apps/web": not found | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='- Dockerfile:18 - "/apps/web": not found<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='#0 building with "default" instance using docker driver #1 [internal] load build definition from Dockerfile #1 transferring dockerfile: 1.16kB done #1 DONE 0...' |
| `lint-output-01` | `instruction_following` | `lint-output` | `15594.42` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | /repo/web/src/App.tsx, 27:19, @typescript-eslint/no-misused-promises, /repo/web/src/api/client.ts, 8:10, @typescript-eslint/no-explicit-any, 33:11, @typescript-eslint/no-unsafe-assignment | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass="- /repo/web/src/App.tsx 12:7 warning 'debugMode' is assigned a value but never used 27:19 error Promise returned in function argument where a void return was..." repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass="- /repo/web/src/App.tsx 12:7 warning 'debugMode' is assigned a value but never used 27:19 error Promise returned in function argument where a void return was..." |
| `git-review-01` | `instruction_following` | `git-review` | `12235.03` | `0.670` | `1.000` | `0.734` | `0.375` | `0.375` | `1.000` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `2861.61` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | search endpoint failed after 2 attempts, exit status 22, https://staging.example.com/api/search?q=smoke, curl: (22) | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='- exit status 22<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='search endpoint failed after 2 attempts curl: (22) https://staging.example.com/api/search?q=smoke curl: (22) exit status 22<|im_end|>' |
| `structured-output-01` | `structured` | `structured-output` | `8685.71` | `0.355` | `1.000` | `0.184` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `13273.10` | `0.437` | `0.905` | `0.851` | `0.000` | `0.000` | `0.781` | `soft_accepted` | missing_exact_anchors | port 5432 is already allocated | - |
| `structured-output-03` | `structured` | `structured-output` | `6937.87` | `0.358` | `0.857` | `0.497` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "refresh token expired", "invalid refresh token" | - |
| `structured-output-04` | `structured` | `structured-output` | `7444.57` | `0.270` | `1.000` | `0.192` | `0.000` | `0.000` | `0.125` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `4895.69` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | tests/api/test_users.py::test_create_user_requires_email, tests/api/test_users.py::test_delete_user_requires_admin, tests/jobs/test_reconcile.py::TestReconcile::test_retries_deadlock | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- tests/api/test_users.py::test_create_user_requires_email - tests/api/test_users.py::test_delete_user_requires_admin - tests/jobs/test_reconcile.py::TestRec...' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- tests/api/test_users.py::test_create_user_requires_email - tests/api/test_users.py::test_delete_user_requires_admin - tests/jobs/test_reconcile.py::TestRec...' |
| `exact-format-02` | `exact_format` | `exact-format` | `2990.84` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | packages/web/src/search/searchBox.test.tsx, SearchBox debounces network query before fetch | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='npm run test:searchBox<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='FAIL packages/web/src/search/searchBox.test.tsx SearchBox ✓ opens suggestions on focus (31 ms) ✕ debounces network query before fetch (1015 ms) ✓ clears quer...' |
| `exact-format-03` | `exact_format` | `exact-format` | `6569.89` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | ghcr.io/acme/worker@sha256:4f8c2e0b1d9a6c7e5f3a2b1908d4c6e7f0a123456789abcdeffedcba98765432 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='ghcr.io/acme/worker@sha256:4f8c2e0b1d9a6c7e5f3a2b1908d4c6e7f0a123456789abcdeffedcba98765432<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='ghcr.io/acme/worker@sha256:4f8c2e0b1d9a6c7e5f3a2b1908d4c6e7f0a123456789abcdeffedcba98765432<|im_end|>' |
| `diagnosis-01` | `explanation` | `diagnosis` | `1022.36` | `0.957` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `5302.84` | `0.752` | `0.750` | `0.868` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `6327.68` | `0.869` | `1.000` | `0.913` | `0.667` | `0.625` | `0.793` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `8723.75` | `0.800` | `0.905` | `0.937` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | app.tasks.email.send_welcome_email | - |
| `mypy-05` | `recall` | `mypy` | `9240.50` | `0.980` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `3663.08` | `0.984` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `4925.49` | `0.748` | `0.783` | `0.913` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | InventorySyncTest.java:132 | - |
| `kubernetes-01` | `recall` | `kubernetes` | `11820.96` | `0.960` | `1.000` | `0.919` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `2637.33` | `0.984` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `2618.32` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `2045.86` | `0.987` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `4865.21` | `0.772` | `0.821` | `0.954` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | packages/api/src/index.ts:4:25 | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `6248.19` | `0.983` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `3845.65` | `0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `2034.13` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `3932.10` | `0.983` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `6166.10` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `3511.04` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `2247.33` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `3211.85` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `11295.70` | `0.952` | `1.000` | `0.931` | `1.000` | `0.906` | `0.688` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `11578.06` | `0.983` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `7504.25` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `2022.18` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `2472.08` | `0.969` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `10904.93` | `0.752` | `0.684` | `0.910` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ./integration | - |
| `npm-05` | `summary` | `npm` | `5149.59` | `0.715` | `0.533` | `0.896` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | web@1.2.0, src/pages/admin.tsx | - |
| `helm-01` | `summary` | `helm` | `33814.26` | `0.853` | `1.000` | `0.904` | `1.000` | `0.782` | `0.274` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `3786.71` | `0.951` | `1.000` | `0.877` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `12514.77` | `0.966` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `6898.78` | `0.951` | `1.000` | `0.941` | `1.000` | `0.949` | `0.830` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `8062.31` | `0.965` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `6195.78` | `0.807` | `0.909` | `0.931` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | -Iinclude | - |
| `python-pytest-02` | `summary` | `python-pytest` | `9374.60` | `0.965` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `6899.77` | `0.960` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `6561.09` | `0.784` | `0.833` | `0.910` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `6632.47` | `0.785` | `0.814` | `0.926` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | FAILED | - |
| `wrangler-01` | `summary` | `wrangler` | `7441.47` | `0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `2695.42` | `0.970` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `6408.04` | `0.619` | `1.000` | `0.729` | `0.250` | `0.250` | `1.000` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `2065.74` | `0.962` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `2702.95` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | tests/test_api.py::test_create_user, tests/test_auth.py::test_refresh_token_expiry | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- tests/test_api.py::test_create_user - tests/test_auth.py::test_refresh_token_expiry<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- tests/test_api.py::test_create_user - tests/test_auth.py::test_refresh_token_expiry<|im_end|>' |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `4316.39` | `0.657` | `1.000` | `0.708` | `0.500` | `0.417` | `0.444` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `1874.78` | `0.940` | `1.000` | `0.799` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `6909.38` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | npm ERR! code ENOTEMPTY, npm ERR! syscall rename, /repo/node_modules/esbuild, /repo/node_modules/.esbuild.DELETE | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- npm ERR! code ENOTEMPTY - npm ERR! syscall rename - /repo/node_modules/esbuild - /repo/node_modules/.esbuild.DELETE<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='npm WARN deprecated request@2.88.2: request has been deprecated npm WARN old lockfile The package-lock.json file was created with an old version of npm npm E...' |
| `docker-build-03` | `instruction_following` | `docker-build` | `1730.52` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | [deps 4/4], pnpm install --frozen-lockfile, ERR_PNPM_LOCKFILE_CONFIG_MISMATCH, exit code: 1 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='#16 ERR_PNPM_LOCKFILE_CONFIG_MISMATCH<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='#16 ERR_PNPM_LOCKFILE_CONFIG_MISMATCH<|im_end|>' |
| `terraform-09` | `instruction_following` | `terraform` | `2197.55` | `0.546` | `0.667` | `0.696` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors | aws_db_instance.main | - |
| `maven-03` | `instruction_following` | `maven` | `8889.11` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | UserService.java:[44,17], findByEmail, UserController.java:[28,31], java.lang.Long, java.util.UUID | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- /repo/src/main/java/App.java:[12,8] unchecked conversion - /repo/src/main/java/UserService.java:[44,17] cannot find symbol symbol: method findByEmail(java....' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='[WARNING] /repo/src/main/java/App.java:[12,8] unchecked conversion [ERROR] /repo/src/main/java/UserService.java:[44,17] cannot find symbol symbol: method fin...' |
| `playwright-01` | `instruction_following` | `playwright` | `6623.59` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | firefox, checkout.spec.ts:44:1, pays with saved card, Payment complete | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- [firefox] › checkout.spec.ts:44:1 › pays with saved card Error: expect(locator).toBeVisible() failed Locator: text=Payment complete' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- [firefox] › checkout.spec.ts:44:1 › pays with saved card Error: expect(locator).toBeVisible() failed Locator: text=Payment complete - [webkit] › checkout.s...' |
| `prettier-01` | `instruction_following` | `prettier` | `1920.54` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | src/App.tsx, src/api/client.ts | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- src/App.tsx - src/api/client.ts - README.md is formatted<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- src/App.tsx - src/api/client.ts - README.md is formatted<|im_end|>' |
| `kubectl-08` | `instruction_following` | `kubectl` | `2532.14` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | worker-5b8c, CrashLoopBackOff, migrator-9z1q, Error | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- worker-5b8c - migrator-9z1q - Error<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- worker-5b8c - CrashLoopBackOff - migrator-9z1q - Error<|im_end|>' |
| `cargo-04` | `instruction_following` | `cargo` | `5562.60` | `0.463` | `0.667` | `0.705` | `0.250` | `0.250` | `1.000` | `soft_accepted` | missing_exact_anchors | src/auth.rs:88, Option::unwrap() | - |
| `shell-01` | `instruction_following` | `shell` | `3285.83` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | rsync, /var/backups/uploads, Permission denied (13), exit code 23 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13)<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) exit code 23<|im_end|>' |
| `pyright-01` | `structured` | `pyright` | `11102.14` | `0.199` | `0.533` | `0.183` | `0.000` | `0.000` | `0.727` | `soft_accepted` | missing_exact_anchors | file, /repo/app/user.py | - |
| `terraform-10` | `structured` | `terraform` | `7213.42` | `0.293` | `1.000` | `0.188` | `0.000` | `0.000` | `0.368` | `accepted` | - | - | - |
| `junit-01` | `structured` | `junit` | `2255.90` | `0.944` | `1.000` | `0.814` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `7273.24` | `0.279` | `1.000` | `0.190` | `0.000` | `0.000` | `0.222` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `9290.48` | `0.174` | `0.667` | `0.179` | `0.000` | `0.000` | `0.179` | `soft_accepted` | missing_exact_anchors | line, column, rule | - |
| `docker-build-04` | `structured` | `docker-build` | `3174.78` | `0.796` | `1.000` | `0.702` | `0.714` | `0.714` | `1.000` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `1277.35` | `0.356` | `1.000` | `0.187` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `3370.15` | `0.817` | `1.000` | `0.633` | `1.000` | `0.782` | `0.273` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `19208.12` | `0.174` | `0.667` | `0.183` | `0.000` | `0.000` | `0.160` | `soft_accepted` | missing_exact_anchors | package, required | - |
| `mypy-06` | `structured` | `mypy` | `34100.96` | `0.308` | `1.000` | `0.337` | `0.000` | `0.000` | `0.067` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `10767.79` | `0.161` | `0.242` | `0.177` | `0.000` | `0.000` | `0.875` | `soft_accepted` | missing_exact_anchors | failed, task, :api:compileJava, cause | - |
| `playwright-02` | `structured` | `playwright` | `72071.29` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | project, chromium, file, checkout.spec.ts, line, test | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='{ "error": "checkout.spec.ts:42:3 › checkout › submits card", "error": "login.spec.ts:12:1 › login › remembers session", "error": "login.spec.ts:12:1 › login...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='{ "error": "checkout.spec.ts:42:3 › checkout › submits card", "error": "login.spec.ts:12:1 › login › remembers session", "error": "login.spec.ts:12:1 › login...' |
| `postgres-04` | `structured` | `postgres` | `1145.50` | `0.354` | `1.000` | `0.181` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `vite-01` | `structured` | `vite` | `3780.83` | `0.260` | `1.000` | `0.183` | `0.000` | `0.000` | `0.053` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `3450.44` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | tests/test_a.py::test_one, tests/test_b.py::TestB::test_three | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='FAILED tests/test_a.py::test_one - AssertionError PASSED tests/test_a.py::test_two FAILED tests/test_b.py::TestB::test_three - TimeoutError<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='FAILED tests/test_a.py::test_one - AssertionError PASSED tests/test_a.py::test_two FAILED tests/test_b.py::TestB::test_three - TimeoutError<|im_end|>' |
| `git-04` | `exact_format` | `git` | `3332.44` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass="Merge made by the 'ort' strategy.<|im_end|>" repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass="Merge made by the 'ort' strategy. commit 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 Author: CI Bot Status: deployed to staging<|im_end|>" |
| `docker-04` | `exact_format` | `docker` | `4851.98` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444<|im_end|>' |
| `npm-08` | `exact_format` | `npm` | `884.00` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 2.18.4 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='2.18.4<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='2.18.4<|im_end|>' |
| `go-test-05` | `exact_format` | `go-test` | `1468.26` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | github.com/acme/shop/checkout, TestCheckoutAppliesCoupon | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='github.com/acme/shop/checkout 0.31s<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='github.com/acme/shop/checkout TestCheckoutAppliesCoupon<|im_end|>' |
| `kubectl-09` | `exact_format` | `kubectl` | `2205.84` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | migrator-v2-9xk, prod | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='migrator-v2-9xk 0/1 Error 0 33m<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='migrator-v2-9xk 0/1 Error 0 33m prod<|im_end|>' |
| `cargo-05` | `exact_format` | `cargo` | `3543.24` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | auth::tests::rejects_expired, billing::tests::rounds_half_even | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='failures: auth::tests::rejects_expired billing::tests::rounds_half_even test result: FAILED. 40 passed; 2 failed<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='failures: auth::tests::rejects_expired billing::tests::rounds_half_even test result: FAILED. 40 passed; 2 failed<|im_end|>' |
| `curl-03` | `exact_format` | `curl` | `621.97` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 503 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='503<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='503<|im_end|>' |
| `rails-02` | `exact_format` | `rails` | `2020.25` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 20260518133742 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='PG::DuplicateColumn: ERROR: column "tenant_id" of relation "users" already exists<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='PG::DuplicateColumn: ERROR: column "tenant_id" of relation "users" already exists<|im_end|>' |
| `python-traceback-02` | `explanation` | `python-traceback` | `2241.97` | `0.962` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `3732.41` | `0.945` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `4408.51` | `0.880` | `1.000` | `0.893` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `1358.76` | `0.783` | `0.818` | `0.914` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | outside the build context | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `1412.29` | `0.960` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `5015.61` | `0.691` | `1.000` | `0.826` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `3607.34` | `0.715` | `0.583` | `0.848` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `1061.36` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `1276.85` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `7710.61` | `0.732` | `1.000` | `0.944` | `0.500` | `0.462` | `0.750` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `package-management-01` | `recall` | `package-management` | `4437.57` | `0.976` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `3033.02` | `0.719` | `0.667` | `0.983` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `2348.87` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `6165.01` | `0.964` | `1.000` | `0.923` | `1.000` | `0.950` | `0.833` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `2791.02` | `0.966` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `4000.05` | `0.426` | `0.000` | `0.917` | `1.000` | `0.917` | `0.722` | `soft_accepted` | missing_exact_anchors | COPY failed, no such file or directory | - |
| `deployment-01` | `recall` | `deployment` | `3465.58` | `0.952` | `1.000` | `0.892` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `40995.60` | `0.887` | `1.000` | `0.885` | `1.000` | `0.747` | `0.156` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `2467.21` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `2523.24` | `0.965` | `1.000` | `0.860` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `10363.84` | `0.883` | `1.000` | `0.846` | `1.000` | `0.763` | `0.211` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `2499.25` | `0.973` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `2875.89` | `0.972` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `926.63` | `0.967` | `1.000` | `0.867` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `762.18` | `0.991` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `2279.32` | `0.972` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `4395.23` | `0.936` | `1.000` | `0.906` | `1.000` | `0.877` | `0.591` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `11346.16` | `0.948` | `1.000` | `0.906` | `1.000` | `0.914` | `0.714` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `3531.28` | `0.614` | `0.500` | `0.930` | `1.000` | `0.894` | `0.647` | `soft_accepted` | missing_exact_anchors | foo.c:5:2 | - |
| `ci-03` | `recall` | `ci` | `8290.18` | `0.800` | `1.000` | `0.892` | `1.000` | `0.905` | `0.682` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `709.69` | `0.976` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `1681.26` | `0.943` | `1.000` | `0.858` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `451.86` | `0.945` | `1.000` | `0.862` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `349.31` | `0.935` | `1.000` | `0.837` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `715.61` | `0.953` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `612.26` | `0.969` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `368.68` | `0.936` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `6390.12` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | error, index.js | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass="- 5:10 warning Unexpected console statement no-console - 7:5 error 'apiKey' is assigned a value but never used no-unused-vars ✖ 1 problem (0 errors, 1 warning)" repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass="/home/user/project/src/index.js 5:10 warning Unexpected console statement no-console 7:5 error 'apiKey' is assigned a value but never used no-unused-vars ✖ 1..." |
| `testing-06` | `instruction_following` | `testing` | `1054.81` | `0.922` | `1.000` | `0.739` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `1773.67` | `0.529` | `1.000` | `0.629` | `0.500` | `0.400` | `0.333` | `soft_accepted` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `2126.51` | `0.633` | `1.000` | `0.347` | `0.571` | `0.571` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `3456.00` | `0.358` | `1.000` | `0.195` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `2354.16` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | InstanceId, State | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- InstanceId: i-12345 - State: {"Name": "running"}' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- InstanceId: i-12345 - State: {"Name": "running"}' |
| `network-01` | `exact_format` | `network` | `2261.77` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | CVE-2021-1234, Critical | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='Vulnerability found: CVE-2021-1234 - Critical<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='Vulnerability found: CVE-2021-1234 - Critical<|im_end|>' |
| `shell-02` | `exact_format` | `shell` | `980.26` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | Timeout while waiting for response | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response<|im_end|>' |
| `shell-03` | `exact_format` | `shell` | `2015.46` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | OUTPUT: | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- OUTPUT: step1 OUTPUT: value1 step2 OUTPUT: value2<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- OUTPUT: step1 OUTPUT: value1 step2 OUTPUT: value2<|im_end|>' |
| `shell-04` | `exact_format` | `shell` | `1675.57` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | NullPointerException | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='[ERROR] Build failure Line 102: NullPointerException: null<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='[ERROR] Build failure Line 102: NullPointerException: null<|im_end|>' |
| `build-04` | `exact_format` | `build` | `3752.06` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, prompt_scaffold_echo, exact_lines_contract_breakage | Resources: 1 added, instance_id | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'prompt_scaffold_echo', 'exact_lines_contract_breakage'] first_pass='- return the exact requested lines or quoted excerpts only - copy quoted or extracted lines exactly from the raw output - do not summarize unless the instruc...' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- Resources: 1 added - instance_id = "i-0abcd1234efgh" - instance_public_ip = "35.153.12.34"<|im_end|>' |
| `build-05` | `exact_format` | `build` | `1054.43` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | BUILD SUCCESSFUL | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='BUILD SUCCESSFUL in 10s<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='BUILD SUCCESSFUL in 10s<|im_end|>' |
| `shell-05` | `exact_format` | `shell` | `1221.25` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | PATH | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='PATH=/usr/bin:/bin HOME=/home/user<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='PATH=/usr/bin:/bin HOME=/home/user<|im_end|>' |
| `deployment-03` | `explanation` | `deployment` | `477.54` | `0.935` | `1.000` | `0.870` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `513.15` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `2282.63` | `0.958` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `477.42` | `0.950` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `2641.58` | `0.903` | `1.000` | `0.877` | `1.000` | `0.894` | `0.647` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `433.92` | `0.931` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `566.88` | `0.937` | `1.000` | `0.873` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `473.63` | `0.931` | `1.000` | `0.861` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `482.74` | `0.913` | `1.000` | `0.825` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `429.67` | `0.944` | `1.000` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `650.72` | `0.937` | `1.000` | `0.875` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `1343.08` | `0.947` | `1.000` | `0.894` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `996.93` | `0.907` | `1.000` | `0.814` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `564.51` | `0.932` | `1.000` | `0.864` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `385.50` | `0.920` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `431.38` | `0.902` | `1.000` | `0.805` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `460.25` | `0.948` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `392.80` | `0.916` | `1.000` | `0.833` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `386.93` | `0.875` | `1.000` | `0.751` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `2748.04` | `0.358` | `1.000` | `0.195` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `2190.72` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | InstanceId, State | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- InstanceId: i-12345 - State: {"Name": "running"}' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- InstanceId: i-12345 - State: {"Name": "running"}' |
| `network-02` | `exact_format` | `network` | `1943.77` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | CVE-2021-1234, Critical | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='Vulnerability found: CVE-2021-1234 - Critical<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='Vulnerability found: CVE-2021-1234 - Critical<|im_end|>' |
| `shell-06` | `exact_format` | `shell` | `957.28` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | Timeout while waiting for response | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response<|im_end|>' |
| `shell-07` | `exact_format` | `shell` | `961.42` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | value1, value2 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- value1 - value2<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- value1 - value2<|im_end|>' |
| `build-06` | `exact_format` | `build` | `3718.30` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, prompt_scaffold_echo, exact_lines_contract_breakage | Resources: 1 added, instance_id | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'prompt_scaffold_echo', 'exact_lines_contract_breakage'] first_pass='- return the exact requested lines or quoted excerpts only - copy quoted or extracted lines exactly from the raw output - do not summarize unless the instruc...' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- Resources: 1 added - instance_id = "i-0abcd1234efgh" - instance_public_ip = "35.153.12.34"<|im_end|>' |
| `runtime-07` | `exact_format` | `runtime` | `1398.98` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | Listening on port 8080 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='Starting server... Listening on port 8080<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='Starting server... Listening on port 8080<|im_end|>' |
| `build-07` | `exact_format` | `build` | `2729.82` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | testError:34 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='[ERROR] Failures: [ERROR] MyTest.testError:34 expected:<1> but was:<2><|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='[ERROR] Failures: [ERROR] MyTest.testError:34 expected:<1> but was:<2><|im_end|>' |
| `shell-08` | `exact_format` | `shell` | `865.57` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | HOME | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='USER=root HOME=/root<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='USER=root HOME=/root<|im_end|>' |
| `deployment-05` | `explanation` | `deployment` | `474.72` | `0.935` | `1.000` | `0.870` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `519.34` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `522.00` | `0.959` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `3125.55` | `0.970` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `568.41` | `0.937` | `1.000` | `0.873` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `475.79` | `0.960` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `396.51` | `0.913` | `1.000` | `0.825` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `388.05` | `0.928` | `1.000` | `0.855` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `833.36` | `0.932` | `1.000` | `0.864` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
