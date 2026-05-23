# cpu-qwen3.5-0.8b-no-quant

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

- load_ms: `12632.04`
- cpu_rss_bytes: `null`
- gpu_peak_bytes: `null`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `261`
- accepted_count: `208`
- soft_accepted_count: `53`
- rejected_count: `19`
- exact_pass_count: `217`
- avg_inference_ms: `5552.22`
- p95_inference_ms: `16880.53`
- avg_exact_preservation_ratio: `0.871`
- avg_summary_quality_ratio: `0.781`
- avg_format_adherence_score: `0.780`
- avg_instruction_following_score: `0.765`
- avg_brevity_ratio: `0.890`
- avg_case_score: `0.767`
- p10_case_score: `0.204`
- quality_core: `0.654`
- latency_factor: `0.858`
- final_score: `56.14`
- peak_cpu_rss_bytes: `null`
- peak_gpu_bytes: `null`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `16434.28` | `0.681` | `0.633` | `0.865` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | python -m app.cli sync --config config/settings.json, config/settings.json | - |
| `python-02` | `summary` | `python` | `10772.16` | `0.833` | `1.000` | `0.936` | `0.500` | `0.459` | `0.727` | `accepted` | - | - | - |
| `python-03` | `recall` | `python` | `3744.53` | `0.989` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `4976.98` | `0.989` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `3516.68` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `3436.59` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `7506.29` | `0.685` | `0.326` | `0.937` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/integration -k billing -vv --maxfail=1, tests/integration/test_billing_api.py::test_invoice_webhook_uses_signature, 1 error in 2.31s | - |
| `pytest-03` | `recall` | `pytest` | `4823.81` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `2998.20` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `3439.69` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `2735.61` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `3158.05` | `0.979` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `4193.59` | `0.991` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `2799.95` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-02` | `summary` | `ruff` | `1979.71` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `2244.85` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `2346.99` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `3858.20` | `0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `2996.62` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `2764.32` | `0.989` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `2520.18` | `0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `1902.27` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `6418.07` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `9625.48` | `0.982` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `5900.37` | `0.785` | `0.800` | `0.934` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Lifecycle script `build` failed, storefront@2.8.1 | - |
| `pnpm-01` | `recall` | `pnpm` | `2333.62` | `0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `9143.05` | `0.979` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `6242.88` | `0.978` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `6489.00` | `0.980` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `3488.04` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `15684.53` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | tsc src/index.ts src/http.ts --pretty false, src/index.ts(48,20), TS2769, URL, RequestInit, src/http.ts(9,17) | fallback output validation failed: model did not stop thinking before reaching the output limit. first_pass="- tsc src/index.ts src/http.ts --pretty false - src/index.ts(48,20): error TS2769: No overload matches this call. Overload 1 of 2, '(url: string, init?: Requ..." repair_pass="- tsc src/index.ts src/http.ts --pretty false - src/index.ts(48,20): error TS2769: No overload matches this call. Overload 1 of 2, '(url: string, init?: Requ..." |
| `eslint-01` | `recall` | `eslint` | `7724.61` | `0.809` | `0.920` | `0.950` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Unused eslint-disable directive | - |
| `eslint-02` | `summary` | `eslint` | `2396.81` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `3699.52` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `17539.26` | `0.888` | `1.000` | `0.873` | `1.000` | `0.759` | `0.197` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `1899.59` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `4502.20` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `1360.79` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `7615.08` | `0.795` | `0.875` | `0.968` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | demo-app-1 | - |
| `docker-compose-03` | `summary` | `docker-compose` | `6699.28` | `0.737` | `0.600` | `0.919` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker compose up api | - |
| `kubectl-01` | `summary` | `kubectl` | `3126.46` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `18861.65` | `0.909` | `1.000` | `0.947` | `1.000` | `0.767` | `0.222` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `1992.66` | `0.995` | `1.000` | `0.988` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `19049.88` | `0.916` | `1.000` | `0.926` | `1.000` | `0.803` | `0.342` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `4491.01` | `0.760` | `0.647` | `0.956` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform validate | - |
| `terraform-02` | `recall` | `terraform` | `11110.29` | `0.958` | `1.000` | `0.925` | `1.000` | `0.931` | `0.771` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `6385.59` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `2835.15` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `5417.84` | `0.956` | `1.000` | `0.931` | `1.000` | `0.921` | `0.735` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `9353.51` | `0.911` | `1.000` | `0.893` | `1.000` | `0.908` | `0.694` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `20658.14` | `0.694` | `1.000` | `0.907` | `0.500` | `0.411` | `0.404` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `git-02` | `recall` | `git` | `4811.93` | `0.709` | `0.704` | `0.869` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | main -> main, non-fast-forward | - |
| `git-03` | `recall` | `git` | `4827.67` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `4505.25` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `7062.40` | `0.836` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `ssh-01` | `summary` | `ssh` | `3984.92` | `0.987` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `2476.78` | `0.980` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `6322.66` | `0.765` | `0.677` | `0.953` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | status=203/EXEC | - |
| `systemd-02` | `summary` | `systemd` | `3756.77` | `0.962` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `2724.58` | `0.977` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `10648.55` | `0.943` | `1.000` | `0.951` | `1.000` | `0.864` | `0.548` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `8580.60` | `0.770` | `0.750` | `0.921` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | example.com/mono-app/pkg/server | - |
| `go-test-01` | `summary` | `go-test` | `19186.18` | `0.914` | `1.000` | `0.936` | `1.000` | `0.880` | `0.600` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `35935.30` | `0.737` | `0.600` | `0.917` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | javac -d out $(find src/main/java -name '*.java') | - |
| `maven-01` | `summary` | `maven` | `11783.78` | `0.594` | `0.304` | `0.931` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | mvn -q test, UserControllerTest.java:72, /workspace/webapp/target/surefire-reports | - |
| `maven-02` | `summary` | `maven` | `3752.76` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `6834.15` | `0.959` | `1.000` | `0.960` | `1.000` | `0.906` | `0.688` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `5729.86` | `0.696` | `0.389` | `0.930` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ./gradlew test, Execution failed for task ':test' | - |
| `cargo-01` | `summary` | `cargo` | `10301.68` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `2144.53` | `0.966` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `14602.94` | `0.656` | `0.526` | `0.942` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | node dist/server.js, MODULE_NOT_FOUND | - |
| `npm-04` | `summary` | `npm` | `3737.04` | `0.974` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `5034.67` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `2905.04` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `4336.24` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `7087.12` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `5001.98` | `0.971` | `1.000` | `0.939` | `1.000` | `0.992` | `0.972` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `11014.36` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund, Dockerfile:8, zod@3.23.8, failed to solve | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='- failed to solve: process "/bin/sh -c npm ci --no-audit --no-fund" did not complete successfully: exit code: 1' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='$ docker build -t example/web:dev . RUN npm ci --no-audit --no-fund Dockerfile:8 ERROR: failed to solve: process "/bin/sh -c npm ci --no-audit --no-fund" did...' |
| `docker-compose-04` | `summary` | `docker-compose` | `7316.61` | `0.739` | `0.600` | `0.922` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker compose up --build | - |
| `kubectl-05` | `summary` | `kubectl` | `1922.77` | `0.982` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `29091.07` | `0.827` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `3207.50` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `5104.75` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `5800.04` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `4753.07` | `0.979` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `5562.62` | `0.979` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `6740.35` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `7375.14` | `0.684` | `0.600` | `0.939` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | psql -h 127.0.0.1 -U app_user -d appdb -c 'select 1' | - |
| `postgres-02` | `summary` | `postgres` | `12866.76` | `0.963` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `3311.83` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `4820.47` | `0.732` | `0.667` | `0.861` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mysql -h db.example.net -u app -D appdb -e "SELECT id, createdAt FROM users LIMIT 5" | - |
| `redis-01` | `summary` | `redis` | `3027.07` | `0.986` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `2297.23` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `8562.78` | `0.679` | `0.619` | `0.879` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | line=91, Ruff F821 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `25529.73` | `0.861` | `1.000` | `0.933` | `1.000` | `0.775` | `0.250` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `2132.97` | `0.968` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `2938.96` | `0.979` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `5400.74` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `3414.60` | `0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `2891.61` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `10235.09` | `0.664` | `0.545` | `0.945` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/unit/test_invoice_totals.py::test_discount_rounding, tests/unit/test_invoice_totals.py:88 | - |
| `compiler-error-01` | `recall` | `compiler-error` | `36451.85` | `0.634` | `0.851` | `0.904` | `0.500` | `0.405` | `0.369` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | src/router.rs:128 | - |
| `ci-log-01` | `recall` | `ci-log` | `8389.39` | `0.961` | `1.000` | `0.928` | `1.000` | `0.936` | `0.786` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `16880.53` | `0.912` | `1.000` | `0.955` | `1.000` | `0.771` | `0.236` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `19321.60` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-log-01` | `summary` | `build-log` | `19755.89` | `0.662` | `1.000` | `0.895` | `0.500` | `0.422` | `0.477` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `docker-build-02` | `summary` | `docker-build` | `19042.21` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | Dockerfile:18, COPY apps/web ./apps/web, "/apps/web": not found | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='- Dockerfile:18 - "/apps/web": not found' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='#0 building with "default" instance using docker driver #1 [internal] load build definition from Dockerfile #1 transferring dockerfile: 1.16kB done #1 DONE 0...' |
| `lint-output-01` | `instruction_following` | `lint-output` | `15143.28` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | /repo/web/src/App.tsx, 27:19, @typescript-eslint/no-misused-promises, /repo/web/src/api/client.ts, 8:10, @typescript-eslint/no-explicit-any, 33:11, @typescript-eslint/no-unsafe-assignment | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass="- /repo/web/src/App.tsx 12:7 warning 'debugMode' is assigned a value but never used 27:19 error Promise returned in function argument where a void return was..." repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass="- /repo/web/src/App.tsx 12:7 warning 'debugMode' is assigned a value but never used 27:19 error Promise returned in function argument where a void return was..." |
| `git-review-01` | `instruction_following` | `git-review` | `10599.02` | `0.693` | `1.000` | `0.737` | `0.429` | `0.429` | `1.000` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `6846.97` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | search endpoint failed after 2 attempts, exit status 22, https://staging.example.com/api/search?q=smoke, curl: (22) | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='- exit status 22' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='search endpoint failed after 2 attempts curl: (22) exit status 22 https://staging.example.com/api/search?q=smoke curl: (22) search endpoint failed after 2 at...' |
| `structured-output-01` | `structured` | `structured-output` | `10559.86` | `0.355` | `1.000` | `0.184` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `11567.34` | `0.289` | `0.333` | `0.578` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | port 5432 is already allocated, deploy / preview, Upload artifact, dist/preview | - |
| `structured-output-03` | `structured` | `structured-output` | `9091.92` | `0.358` | `0.857` | `0.497` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "refresh token expired", "invalid refresh token" | - |
| `structured-output-04` | `structured` | `structured-output` | `7684.34` | `0.270` | `1.000` | `0.192` | `0.000` | `0.000` | `0.125` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `7592.09` | `0.162` | `1.000` | `0.336` | `0.000` | `0.000` | `0.143` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `5308.78` | `0.124` | `0.714` | `0.321` | `0.000` | `0.000` | `0.143` | `soft_accepted` | missing_exact_anchors | SearchBox debounces network query before fetch | - |
| `exact-format-03` | `exact_format` | `exact-format` | `4657.20` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `1939.97` | `0.957` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `2766.76` | `0.945` | `1.000` | `0.891` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `5991.44` | `0.877` | `1.000` | `0.914` | `0.667` | `0.640` | `0.868` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `10321.51` | `0.800` | `0.905` | `0.937` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | app.tasks.email.send_welcome_email | - |
| `mypy-05` | `recall` | `mypy` | `7033.38` | `0.682` | `0.600` | `0.928` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | include_meta, -> bytes, -> str | - |
| `terraform-08` | `recall` | `terraform` | `7656.80` | `0.985` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `6637.18` | `0.748` | `0.783` | `0.912` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | InventorySyncTest.java:132 | - |
| `kubernetes-01` | `recall` | `kubernetes` | `13865.85` | `0.960` | `1.000` | `0.918` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `3630.61` | `0.984` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `3666.58` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `2909.43` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `8017.79` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `6271.23` | `0.983` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `3957.86` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `2594.17` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `3413.72` | `0.985` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `5441.52` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `7449.35` | `0.787` | `0.851` | `0.970` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Failed asserting that '88.00' is identical to '86.40' | - |
| `nginx-03` | `recall` | `nginx` | `2488.84` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `3308.20` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `3027.74` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `8366.49` | `0.754` | `0.792` | `0.925` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | services/reporting/parser.py", line 141 | - |
| `powershell-01` | `recall` | `powershell` | `6795.31` | `0.718` | `0.688` | `0.939` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | .\scripts\release.ps1 -Version 1.4.2 | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `2788.56` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `3164.17` | `0.969` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `11975.73` | `0.753` | `0.684` | `0.911` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ./integration | - |
| `npm-05` | `summary` | `npm` | `8568.31` | `0.968` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `27746.42` | `0.853` | `1.000` | `0.904` | `1.000` | `0.782` | `0.274` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `4123.35` | `0.951` | `1.000` | `0.877` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `11360.21` | `0.966` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `5551.93` | `0.951` | `1.000` | `0.941` | `1.000` | `0.949` | `0.830` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `7489.24` | `0.965` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `6340.55` | `0.807` | `0.909` | `0.931` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | -Iinclude | - |
| `python-pytest-02` | `summary` | `python-pytest` | `4075.53` | `0.969` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `3487.63` | `0.962` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `6583.83` | `0.784` | `0.833` | `0.910` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `6862.09` | `0.785` | `0.814` | `0.926` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | FAILED | - |
| `wrangler-01` | `summary` | `wrangler` | `6498.86` | `0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `2988.59` | `0.970` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `7719.34` | `0.605` | `1.000` | `0.721` | `0.222` | `0.222` | `1.000` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `2584.31` | `0.962` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `3913.94` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | tests/test_api.py::test_create_user, tests/test_auth.py::test_refresh_token_expiry | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- tests/test_api.py::test_create_user - tests/test_auth.py::test_refresh_token_expiry' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- tests/test_api.py::test_create_user - tests/test_auth.py::test_refresh_token_expiry' |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `4424.71` | `0.657` | `1.000` | `0.708` | `0.500` | `0.417` | `0.444` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `2220.87` | `0.940` | `1.000` | `0.799` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `6993.88` | `0.467` | `1.000` | `0.812` | `0.000` | `0.000` | `0.238` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `4380.52` | `0.333` | `0.450` | `0.671` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | [deps 4/4], pnpm install --frozen-lockfile | - |
| `terraform-09` | `instruction_following` | `terraform` | `2369.05` | `0.709` | `1.000` | `0.696` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `8335.23` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | UserService.java:[44,17], findByEmail, UserController.java:[28,31], java.lang.Long, java.util.UUID | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- /repo/src/main/java/App.java:[12,8] unchecked conversion - /repo/src/main/java/UserService.java:[44,17] cannot find symbol symbol: method findByEmail(java....' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='[WARNING] /repo/src/main/java/App.java:[12,8] unchecked conversion [ERROR] /repo/src/main/java/UserService.java:[44,17] cannot find symbol symbol: method fin...' |
| `playwright-01` | `instruction_following` | `playwright` | `6635.59` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | firefox, checkout.spec.ts:44:1, pays with saved card, Payment complete | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- [firefox] › checkout.spec.ts:44:1 › pays with saved card Error: expect(locator).toBeVisible() failed Locator: text=Payment complete' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- [firefox] › checkout.spec.ts:44:1 › pays with saved card Error: expect(locator).toBeVisible() failed Locator: text=Payment complete - [webkit] › checkout.s...' |
| `prettier-01` | `instruction_following` | `prettier` | `3450.70` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | src/App.tsx, src/api/client.ts | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- src/App.tsx - src/api/client.ts - README.md is formatted' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- src/App.tsx - src/api/client.ts - README.md is formatted' |
| `kubectl-08` | `instruction_following` | `kubectl` | `4358.49` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | worker-5b8c, CrashLoopBackOff, migrator-9z1q, Error | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- worker-5b8c - migrator-9z1q - Error' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- worker-5b8c - CrashLoopBackOff - migrator-9z1q - Error' |
| `cargo-04` | `instruction_following` | `cargo` | `5676.89` | `0.653` | `1.000` | `0.734` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `4824.33` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | rsync, /var/backups/uploads, Permission denied (13), exit code 23 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13)' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) exit code 23' |
| `pyright-01` | `structured` | `pyright` | `6536.54` | `0.502` | `1.000` | `0.776` | `0.000` | `0.000` | `0.696` | `accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `5984.32` | `0.293` | `1.000` | `0.188` | `0.000` | `0.000` | `0.368` | `accepted` | - | - | - |
| `junit-01` | `structured` | `junit` | `2703.57` | `0.944` | `1.000` | `0.814` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `6476.78` | `0.280` | `1.000` | `0.191` | `0.000` | `0.000` | `0.222` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `10016.34` | `0.174` | `0.667` | `0.179` | `0.000` | `0.000` | `0.179` | `soft_accepted` | missing_exact_anchors | line, column, rule | - |
| `docker-build-04` | `structured` | `docker-build` | `3628.27` | `0.796` | `1.000` | `0.702` | `0.714` | `0.714` | `1.000` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `2005.37` | `0.356` | `1.000` | `0.187` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `3329.05` | `0.817` | `1.000` | `0.633` | `1.000` | `0.782` | `0.273` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `6981.21` | `0.206` | `0.667` | `0.229` | `0.000` | `0.000` | `0.400` | `soft_accepted` | missing_exact_anchors | package, required | - |
| `mypy-06` | `structured` | `mypy` | `7101.42` | `0.299` | `1.000` | `0.189` | `0.000` | `0.000` | `0.429` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `10691.36` | `0.161` | `0.242` | `0.177` | `0.000` | `0.000` | `0.875` | `soft_accepted` | missing_exact_anchors | failed, task, :api:compileJava, cause | - |
| `playwright-02` | `structured` | `playwright` | `7156.50` | `0.156` | `0.167` | `0.167` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | project, chromium, file, line, test | - |
| `postgres-04` | `structured` | `postgres` | `2249.76` | `0.354` | `1.000` | `0.181` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `vite-01` | `structured` | `vite` | `4458.66` | `0.259` | `1.000` | `0.181` | `0.000` | `0.000` | `0.048` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `4898.63` | `0.190` | `1.000` | `0.318` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `5497.76` | `0.028` | `0.000` | `0.245` | `0.000` | `0.000` | `0.167` | `soft_accepted` | missing_exact_anchors | 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 | - |
| `docker-04` | `exact_format` | `docker` | `3336.77` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `1285.65` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `3321.49` | `0.233` | `1.000` | `0.334` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `4139.40` | `0.230` | `1.000` | `0.302` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `2502.09` | `0.190` | `1.000` | `0.334` | `0.000` | `0.000` | `0.125` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `1241.35` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `4369.24` | `0.026` | `0.000` | `0.248` | `0.000` | `0.000` | `0.111` | `soft_accepted` | missing_exact_anchors | 20260518133742 | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `1607.29` | `0.939` | `1.000` | `0.878` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `3737.27` | `0.945` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `6537.36` | `0.752` | `0.667` | `0.902` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | orders_customer_id_fkey | - |
| `docker-build-05` | `explanation` | `docker-build` | `2802.74` | `0.958` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `2272.92` | `0.954` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `6726.87` | `0.691` | `1.000` | `0.826` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `4861.93` | `0.715` | `0.583` | `0.848` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `1963.10` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `1982.05` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `6241.40` | `0.753` | `1.000` | `0.945` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `package-management-01` | `recall` | `package-management` | `4874.18` | `0.976` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `3523.07` | `0.719` | `0.667` | `0.983` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `4597.74` | `0.952` | `1.000` | `0.940` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `5487.13` | `0.964` | `1.000` | `0.924` | `1.000` | `0.950` | `0.833` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `2982.19` | `0.967` | `1.000` | `0.866` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `3776.99` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `2884.68` | `0.952` | `1.000` | `0.892` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `28698.98` | `0.887` | `1.000` | `0.886` | `1.000` | `0.747` | `0.156` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `3387.27` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `3464.14` | `0.966` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `5915.63` | `0.886` | `1.000` | `0.814` | `1.000` | `0.798` | `0.327` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `2886.56` | `0.973` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `3568.01` | `0.972` | `1.000` | `0.889` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1159.61` | `0.967` | `1.000` | `0.867` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `1066.13` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `3088.37` | `0.972` | `1.000` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `4937.36` | `0.936` | `1.000` | `0.906` | `1.000` | `0.877` | `0.591` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `9902.45` | `0.948` | `1.000` | `0.906` | `1.000` | `0.914` | `0.714` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `4285.47` | `0.610` | `0.500` | `0.928` | `1.000` | `0.883` | `0.611` | `soft_accepted` | missing_exact_anchors | foo.c:5:2 | - |
| `ci-03` | `recall` | `ci` | `8410.78` | `0.831` | `1.000` | `0.911` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `1189.75` | `0.976` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `2718.64` | `0.943` | `1.000` | `0.859` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `983.76` | `0.945` | `1.000` | `0.862` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `859.34` | `0.935` | `1.000` | `0.837` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `1138.58` | `0.953` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `1205.96` | `0.976` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `966.65` | `0.937` | `1.000` | `0.842` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `2575.36` | `0.658` | `1.000` | `0.859` | `0.333` | `0.300` | `0.667` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `1818.75` | `0.922` | `1.000` | `0.738` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `4049.70` | `0.529` | `1.000` | `0.628` | `0.500` | `0.400` | `0.333` | `soft_accepted` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `2211.74` | `0.633` | `1.000` | `0.347` | `0.571` | `0.571` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `3234.61` | `0.358` | `1.000` | `0.194` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `3770.86` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | InstanceId, State | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- InstanceId: i-12345 - State: {"Name": "running"}' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- InstanceId: i-12345 - State: {"Name": "running"}' |
| `network-01` | `exact_format` | `network` | `1692.07` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `2837.68` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | Timeout while waiting for response | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response' |
| `shell-03` | `exact_format` | `shell` | `3442.52` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | OUTPUT: | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- OUTPUT: step1 OUTPUT: value1 step2 OUTPUT: value2' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- OUTPUT: step1 OUTPUT: value1 step2 OUTPUT: value2' |
| `shell-04` | `exact_format` | `shell` | `1598.39` | `0.207` | `1.000` | `0.491` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `4820.47` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | Resources: 1 added, instance_id | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- Resources: 1 added - instance_id - instance_public_ip = "35.153.12.34"' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- Resources: 1 added - instance_id - instance_public_ip = "35.153.12.34"' |
| `build-05` | `exact_format` | `build` | `1433.75` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `1397.45` | `0.232` | `1.000` | `0.658` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `1021.38` | `0.935` | `1.000` | `0.870` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `967.19` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `1683.52` | `0.946` | `1.000` | `0.893` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `1040.67` | `0.950` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `3914.60` | `0.903` | `1.000` | `0.877` | `1.000` | `0.894` | `0.647` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `964.49` | `0.932` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `1194.88` | `0.931` | `1.000` | `0.861` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `953.68` | `0.930` | `1.000` | `0.860` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `991.02` | `0.913` | `1.000` | `0.826` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `925.60` | `0.943` | `1.000` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `1092.62` | `0.938` | `1.000` | `0.875` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `2316.30` | `0.947` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `1380.11` | `0.908` | `1.000` | `0.816` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `1141.00` | `0.932` | `1.000` | `0.864` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `942.96` | `0.920` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `983.84` | `0.902` | `1.000` | `0.805` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `990.72` | `0.948` | `1.000` | `0.896` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `953.50` | `0.916` | `1.000` | `0.832` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `980.63` | `0.875` | `1.000` | `0.750` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `2940.76` | `0.358` | `1.000` | `0.194` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `4370.69` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | InstanceId, State | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- InstanceId: i-12345 - State: {"Name": "running"}' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- InstanceId: i-12345 - State: {"Name": "running"}' |
| `network-02` | `exact_format` | `network` | `1662.37` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `2962.29` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | Timeout while waiting for response | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response INFO: Retrying...' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response INFO: Retrying...' |
| `shell-07` | `exact_format` | `shell` | `2466.68` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | value1, value2 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- value1 - value2' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- value1 - value2' |
| `build-06` | `exact_format` | `build` | `4596.86` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | Resources: 1 added, instance_id | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- Resources: 1 added - instance_id - instance_public_ip = "35.153.12.34"' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- Resources: 1 added - instance_id - instance_public_ip = "35.153.12.34"' |
| `runtime-07` | `exact_format` | `runtime` | `1417.20` | `0.207` | `1.000` | `0.319` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `2130.34` | `0.268` | `1.000` | `0.850` | `0.000` | `0.000` | `0.667` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `1234.67` | `0.231` | `1.000` | `0.646` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `1033.86` | `0.935` | `1.000` | `0.870` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `1009.15` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `1095.20` | `0.959` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `4239.27` | `0.970` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `1278.37` | `0.931` | `1.000` | `0.861` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `1058.05` | `0.960` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `1276.94` | `0.913` | `1.000` | `0.826` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `1045.09` | `0.928` | `1.000` | `0.856` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1378.63` | `0.932` | `1.000` | `0.864` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
