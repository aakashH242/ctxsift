# cpu-qwen2.5-coder-0.5b-instruct-128k-no-quant

## Scenario

- track: `cpu`
- phase: `cpu-screen`
- model: `unsloth/Qwen2.5-Coder-0.5B-Instruct-128K-GGUF`
- quantization: `none`
- device: `cpu`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `1886.16`
- cpu_rss_bytes: `null`
- gpu_peak_bytes: `null`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `279`
- accepted_count: `170`
- soft_accepted_count: `109`
- rejected_count: `1`
- exact_pass_count: `177`
- avg_inference_ms: `6276.12`
- p95_inference_ms: `16248.57`
- avg_exact_preservation_ratio: `0.805`
- avg_summary_quality_ratio: `0.820`
- avg_format_adherence_score: `0.762`
- avg_instruction_following_score: `0.739`
- avg_brevity_ratio: `0.828`
- avg_case_score: `0.724`
- p10_case_score: `0.290`
- quality_core: `0.637`
- latency_factor: `0.850`
- final_score: `54.18`
- peak_cpu_rss_bytes: `null`
- peak_gpu_bytes: `null`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `18761.17` | `0.410` | `0.300` | `0.833` | `0.500` | `0.408` | `0.387` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | python -m app.cli sync --config config/settings.json, /workspace/app/config.py, line 27, config/settings.json | - |
| `python-02` | `summary` | `python` | `7756.16` | `0.614` | `0.627` | `0.890` | `0.500` | `0.459` | `0.727` | `soft_accepted` | missing_exact_anchors, verbatim_alignment_weak | python services/worker.py --queue emails --concurrency 4, worker boot failed | - |
| `python-03` | `recall` | `python` | `16739.12` | `0.534` | `0.636` | `0.880` | `0.500` | `0.383` | `0.217` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | /workspace/src/api/app.py, line 58 | - |
| `python-04` | `recall` | `python` | `10580.14` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `13902.54` | `0.541` | `0.407` | `0.873` | `1.000` | `0.805` | `0.349` | `soft_accepted` | missing_exact_anchors | python tools/export_report.py --input data/may.csv --format parquet, /workspace/src/reports/export.py, data/may.csv | - |
| `pytest-01` | `recall` | `pytest` | `9958.08` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `10591.76` | `0.777` | `0.767` | `0.931` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/integration/test_billing_api.py::test_invoice_webhook_uses_signature | - |
| `pytest-03` | `recall` | `pytest` | `7431.53` | `0.757` | `1.000` | `0.961` | `0.500` | `0.500` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `pytest-04` | `recall` | `pytest` | `6123.25` | `0.777` | `0.825` | `0.970` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | PytestUnknownMarkWarning | - |
| `pytest-05` | `summary` | `pytest` | `2724.39` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `5100.19` | `0.619` | `0.439` | `0.924` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mypy src/accounts/user_service.py --show-error-codes, attr-defined, Found 1 error in 1 file | - |
| `mypy-02` | `summary` | `mypy` | `14481.76` | `0.668` | `0.579` | `0.881` | `1.000` | `0.878` | `0.593` | `soft_accepted` | missing_exact_anchors | mypy src tests --pretty --show-error-codes, arg-type | - |
| `mypy-03` | `recall` | `mypy` | `3220.59` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `6861.23` | `0.715` | `0.644` | `0.887` | `1.000` | `0.950` | `0.833` | `soft_accepted` | missing_exact_anchors | ruff check src --output-format=full, all | - |
| `ruff-02` | `summary` | `ruff` | `2365.00` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `7160.31` | `0.888` | `1.000` | `0.874` | `1.000` | `0.878` | `0.592` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `5563.90` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `16194.07` | `0.724` | `0.789` | `0.895` | `1.000` | `0.917` | `0.725` | `soft_accepted` | missing_exact_anchors | pylint src/config/runtime.py src/api/server.py | - |
| `pylint-03` | `summary` | `pylint` | `2847.32` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `2647.84` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `4127.15` | `0.979` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `1414.68` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `4011.79` | `0.984` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `6234.27` | `0.697` | `0.444` | `0.898` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm install, ERESOLVE | - |
| `npm-03` | `summary` | `npm` | `7186.03` | `0.729` | `0.564` | `0.916` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm run build, ./CheckoutButton | - |
| `pnpm-01` | `recall` | `pnpm` | `3013.55` | `0.983` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `6393.79` | `0.810` | `0.909` | `0.938` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 5.51.1 | - |
| `pnpm-03` | `summary` | `pnpm` | `16841.07` | `0.927` | `1.000` | `0.920` | `1.000` | `0.919` | `0.729` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `4291.73` | `0.648` | `0.333` | `0.822` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tsc -p tsconfig.json --noEmit, src/server/index.ts(3,18), TS2307, src/server/index.ts(4,18) | - |
| `typescript-02` | `recall` | `typescript` | `9350.20` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `3329.66` | `0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-01` | `recall` | `eslint` | `7650.24` | `0.985` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `4811.72` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `3729.03` | `0.610` | `0.423` | `0.908` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /workspace/src/hooks/useCart.ts, react-hooks/exhaustive-deps, 1 problem (0 errors, 1 warning) | - |
| `docker-01` | `recall` | `docker` | `9071.66` | `0.714` | `0.755` | `0.875` | `1.000` | `0.945` | `0.818` | `soft_accepted` | missing_exact_anchors | docker build -t api:dev . | - |
| `docker-02` | `summary` | `docker` | `3159.25` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `6660.14` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `1926.75` | `0.637` | `0.167` | `0.895` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker compose up, external, could not be found | - |
| `docker-compose-02` | `recall` | `docker-compose` | `4692.90` | `0.984` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `2352.86` | `0.983` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `5428.16` | `0.644` | `0.529` | `0.874` | `1.000` | `0.852` | `0.508` | `soft_accepted` | missing_exact_anchors | kubectl apply -f k8s/deployment.yaml --server-side, containers[name="api"].image | - |
| `kubectl-02` | `recall` | `kubectl` | `13835.60` | `0.656` | `0.684` | `0.905` | `1.000` | `0.812` | `0.375` | `soft_accepted` | missing_exact_anchors | kubectl describe pod api-7d9f7bbd8c-rx2kq -n staging | - |
| `kubectl-03` | `summary` | `kubectl` | `2659.90` | `0.684` | `0.389` | `0.893` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | kubectl wait --for=condition=Available deployment/worker -n jobs --timeout=90s, deployments/worker | - |
| `kubectl-04` | `recall` | `kubectl` | `16830.07` | `0.535` | `0.619` | `0.869` | `0.500` | `0.401` | `0.342` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | kubectl logs payments-worker-6f8f7d4df5-z5vsm -c worker --previous -n payments, payments-worker-6f8f7d4df5-z5vsm | - |
| `terraform-01` | `summary` | `terraform` | `8383.96` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `4891.94` | `0.983` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `5171.10` | `0.689` | `0.613` | `0.940` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform apply | - |
| `terraform-04` | `summary` | `terraform` | `5536.22` | `0.682` | `0.390` | `0.888` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/aws.tftest.hcl line 18, Test assertion failed, aws_instance.web.instance_type, expected t3.small default | - |
| `mixed-01` | `recall` | `mixed` | `48687.45` | `0.488` | `0.326` | `0.884` | `1.000` | `0.720` | `0.068` | `soft_accepted` | missing_exact_anchors | rsync -av --delete build/ backup/build/, rsync warning, main.c(1338) | - |
| `mixed-02` | `summary` | `mixed` | `4983.45` | `0.718` | `0.622` | `0.847` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | migrations/202605121045_add_login_audit.sql, psql | - |
| `git-01` | `recall` | `git` | `13376.53` | `0.974` | `1.000` | `0.896` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `5367.13` | `0.924` | `1.000` | `0.860` | `1.000` | `0.876` | `0.587` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `9602.46` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `9234.71` | `0.990` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `3781.75` | `0.973` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-01` | `summary` | `ssh` | `10175.77` | `0.853` | `1.000` | `0.923` | `1.000` | `0.769` | `0.229` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `4972.45` | `0.745` | `0.636` | `0.919` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ssh deploy@staging.example.net | - |
| `systemd-01` | `summary` | `systemd` | `7657.03` | `0.763` | `0.677` | `0.946` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | status=203/EXEC | - |
| `systemd-02` | `summary` | `systemd` | `6423.19` | `0.912` | `1.000` | `0.872` | `1.000` | `0.926` | `0.754` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `4670.10` | `0.964` | `1.000` | `0.911` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `13082.98` | `0.910` | `1.000` | `0.926` | `1.000` | `0.786` | `0.287` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `10299.12` | `0.957` | `1.000` | `0.893` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `5519.63` | `0.742` | `0.600` | `0.932` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | go test ./... -run TestCacheTTL -count=1 | - |
| `javac-01` | `summary` | `javac` | `3462.06` | `0.969` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `23874.10` | `0.553` | `0.565` | `0.879` | `0.500` | `0.407` | `0.381` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | maven-surefire-plugin:3.5.5:test, /workspace/webapp/target/surefire-reports | - |
| `maven-02` | `summary` | `maven` | `7548.75` | `0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `13724.84` | `0.662` | `0.714` | `0.892` | `1.000` | `0.805` | `0.349` | `soft_accepted` | missing_exact_anchors | ./gradlew :service:build --warning-mode=all | - |
| `gradle-02` | `summary` | `gradle` | `6087.58` | `0.721` | `0.667` | `0.913` | `1.000` | `0.932` | `0.775` | `soft_accepted` | missing_exact_anchors | ./gradlew test | - |
| `cargo-01` | `summary` | `cargo` | `6241.71` | `0.709` | `0.515` | `0.887` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | cargo build, ingest-cli | - |
| `cargo-02` | `summary` | `cargo` | `4571.89` | `0.968` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `5107.78` | `0.544` | `0.263` | `0.887` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | node dist/server.js, MODULE_NOT_FOUND, /workspace/dist/config/index.js:4:18 | - |
| `npm-04` | `summary` | `npm` | `8206.49` | `0.709` | `0.474` | `0.915` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm install, ERESOLVE | - |
| `tsc-01` | `summary` | `tsc` | `4925.42` | `0.963` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `5654.17` | `0.716` | `0.500` | `0.917` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npx eslint src --max-warnings=0, react-hooks/exhaustive-deps | - |
| `python-runtime-01` | `summary` | `python-runtime` | `46032.89` | `0.514` | `0.560` | `0.869` | `0.500` | `0.367` | `0.114` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | python -m tools.sync_rules --env staging, rules/staging.json | - |
| `pytest-06` | `summary` | `pytest` | `5688.03` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `5353.96` | `0.964` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `9791.60` | `0.773` | `0.733` | `0.941` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker build -t example/web:dev . | - |
| `docker-compose-04` | `summary` | `docker-compose` | `4814.68` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `8238.27` | `0.854` | `1.000` | `0.848` | `1.000` | `0.830` | `0.434` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `13429.51` | `0.629` | `0.118` | `0.901` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | kubectl describe pod web-7f6f6d9d7b-kj4t2 -n dev, CrashLoopBackOff, Exit Code:    1 | - |
| `kubectl-07` | `recall` | `kubectl` | `2358.36` | `0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `12661.25` | `0.638` | `0.636` | `0.889` | `1.000` | `0.827` | `0.423` | `soft_accepted` | missing_exact_anchors | terraform plan -lock-timeout=5s -out=tfplan | - |
| `terraform-06` | `summary` | `terraform` | `4394.05` | `0.729` | `0.600` | `0.893` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform validate | - |
| `terraform-07` | `summary` | `terraform` | `5426.62` | `0.612` | `0.133` | `0.842` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform plan -detailed-exitcode -no-color, Plan: 1 to add, 1 to change, 0 to destroy., aws_security_group_rule.web_https | - |
| `nginx-01` | `summary` | `nginx` | `3151.90` | `0.984` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `8267.75` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `4273.75` | `0.674` | `0.600` | `0.891` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | psql -h 127.0.0.1 -U app_user -d appdb -c 'select 1' | - |
| `postgres-02` | `summary` | `postgres` | `5547.25` | `0.971` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `3491.24` | `0.761` | `0.667` | `0.947` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERROR 1045 (28000) | - |
| `mysql-02` | `summary` | `mysql` | `2743.38` | `0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `6914.87` | `0.735` | `0.676` | `0.907` | `1.000` | `0.967` | `0.889` | `soft_accepted` | missing_exact_anchors | redis-cli -u redis://127.0.0.1:6379 SET sync:cursor 90210 | - |
| `redis-02` | `recall` | `redis` | `3997.54` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `13279.39` | `0.596` | `0.524` | `0.866` | `1.000` | `0.847` | `0.491` | `soft_accepted` | missing_exact_anchors | ruff check ., line=91, exit code 2 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `23245.87` | `0.852` | `1.000` | `0.910` | `1.000` | `0.777` | `0.255` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `6246.60` | `0.948` | `1.000` | `0.897` | `1.000` | `0.978` | `0.925` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `4527.07` | `0.642` | `0.256` | `0.853` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | make CFLAGS='-O2 -Wall -Werror' all, src/parser.c:214:12, Makefile:22 | - |
| `tar-01` | `summary` | `tar` | `8431.49` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `4916.53` | `0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `7460.05` | `0.960` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `9256.71` | `0.411` | `0.000` | `0.783` | `1.000` | `0.965` | `0.882` | `soft_accepted` | missing_exact_anchors | tests/unit/test_invoice_totals.py::test_discount_rounding, tests/unit/test_invoice_totals.py:88, Decimal('17.50'), Decimal('17.49'), ROUND_HALF_UP is deprecated for discounts; use ROUND_HALF_EVEN | - |
| `compiler-error-01` | `recall` | `compiler-error` | `20068.09` | `0.518` | `0.552` | `0.867` | `0.500` | `0.417` | `0.446` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | src/router.rs:128, req.into_body(), req.method() | - |
| `ci-log-01` | `recall` | `ci-log` | `11888.23` | `0.786` | `0.882` | `0.911` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | deployments.apps "payments-api" not found | - |
| `package-manager-01` | `recall` | `package-manager` | `4595.66` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `50747.84` | `0.656` | `0.500` | `0.903` | `1.000` | `0.870` | `0.567` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | github.com/acme/shop/inventory, TestReconcileInventory, test timed out after 10m0s, worker.go:144 | - |
| `build-log-01` | `summary` | `build-log` | `5261.35` | `0.748` | `0.688` | `0.897` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | InvoiceMapper.java:[58,29] | - |
| `docker-build-02` | `summary` | `docker-build` | `5202.10` | `0.751` | `1.000` | `0.922` | `0.000` | `0.000` | `0.882` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `13943.25` | `0.292` | `0.625` | `0.681` | `0.000` | `0.000` | `0.145` | `soft_accepted` | missing_exact_anchors | @typescript-eslint/no-misused-promises, @typescript-eslint/no-explicit-any, @typescript-eslint/no-unsafe-assignment | - |
| `git-review-01` | `instruction_following` | `git-review` | `4572.58` | `0.692` | `1.000` | `0.735` | `0.429` | `0.429` | `1.000` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `7665.54` | `0.393` | `0.645` | `0.778` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | search endpoint failed after 2 attempts, exit status 22 | - |
| `structured-output-01` | `structured` | `structured-output` | `5663.16` | `0.382` | `0.500` | `0.830` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /work/app/api/routes.py, 21, reportUndefinedVariable | - |
| `structured-output-02` | `structured` | `structured-output` | `12845.08` | `0.333` | `0.905` | `0.542` | `0.000` | `0.000` | `0.481` | `soft_accepted` | missing_exact_anchors | port 5432 is already allocated | - |
| `structured-output-03` | `structured` | `structured-output` | `7374.59` | `0.679` | `0.500` | `0.661` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | createSession › rejects expired refresh token, calculateTax › uses EU VAT for DE customer, Expected: 19, Received: 0 | - |
| `structured-output-04` | `structured` | `structured-output` | `7365.44` | `0.125` | `0.219` | `0.178` | `0.000` | `0.000` | `0.500` | `soft_accepted` | missing_exact_anchors | /repo/apps/web/src/main.tsx, /repo/packages/time/src/format.ts, /repo/packages/time/src/parse.ts, /repo/apps/web/src/features/flags.ts, @acme/flags | - |
| `exact-format-01` | `exact_format` | `exact-format` | `29272.50` | `0.186` | `1.000` | `0.327` | `0.000` | `0.000` | `0.056` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `24184.66` | `0.238` | `1.000` | `0.509` | `0.000` | `0.000` | `0.750` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `5869.46` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | ghcr.io/acme/worker@sha256:4f8c2e0b1d9a6c7e5f3a2b1908d4c6e7f0a123456789abcdeffedcba98765432 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them if one short reason is r...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `diagnosis-01` | `explanation` | `diagnosis` | `8419.18` | `0.725` | `0.778` | `0.811` | `1.000` | `0.976` | `0.920` | `soft_accepted` | missing_exact_anchors | shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `3093.82` | `0.613` | `0.000` | `0.843` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | TS2322, string | undefined, AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `14376.82` | `0.695` | `1.000` | `0.897` | `0.000` | `0.000` | `0.465` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `11298.03` | `0.614` | `0.429` | `0.918` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /srv/app/app/tasks/email.py, line 92, retries exhausted for queue emails | - |
| `mypy-05` | `recall` | `mypy` | `7456.94` | `0.975` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `7993.71` | `0.944` | `1.000` | `0.910` | `1.000` | `0.898` | `0.661` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `6651.94` | `0.664` | `0.565` | `0.908` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | InventorySyncTest > publishesBackorderEvent() FAILED, OrderServiceTest > calculatesDiscountForGoldCustomer() PASSED | - |
| `kubernetes-01` | `recall` | `kubernetes` | `5772.45` | `0.584` | `0.360` | `0.902` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | api-7d9f8c8b99-mx2kq, registry.example.com/api:2026.05.18-1, CrashLoopBackOff, Exit Code: 78 | - |
| `go-test-02` | `recall` | `go-test` | `5276.89` | `0.970` | `1.000` | `0.880` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `12906.04` | `0.944` | `1.000` | `0.900` | `1.000` | `0.907` | `0.691` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `5207.10` | `0.979` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `2712.12` | `0.981` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `7495.57` | `0.983` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `5942.39` | `0.705` | `0.684` | `0.888` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | fastify, ^5.1.0, ^5.2.1 | - |
| `swift-01` | `recall` | `swift` | `6338.40` | `0.705` | `0.651` | `0.944` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | XCTAssertEqual failed, fatalError | - |
| `elixir-01` | `recall` | `elixir` | `4983.82` | `0.624` | `0.478` | `0.875` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | lib/my_app/cache_worker.ex:63, test/my_app/cache_worker_test.exs:29, refreshes expired keys | - |
| `rails-01` | `recall` | `rails` | `6245.13` | `0.584` | `0.353` | `0.915` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 20260518093012 AddIndexToEventsRequestId, 20260518093012_add_index_to_events_request_id.rb:3, ArgumentError | - |
| `phpunit-01` | `recall` | `phpunit` | `5099.70` | `0.937` | `1.000` | `0.902` | `1.000` | `0.884` | `0.614` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `2512.61` | `0.988` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `2202.62` | `0.983` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `6103.65` | `0.974` | `1.000` | `0.896` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `9455.19` | `0.951` | `1.000` | `0.908` | `1.000` | `0.921` | `0.737` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `5448.42` | `0.492` | `0.125` | `0.892` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | .\scripts\release.ps1 -Version 1.4.2, PSSecurityException, FullyQualifiedErrorId : UnauthorizedAccess | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `6654.21` | `0.966` | `1.000` | `0.928` | `1.000` | `0.951` | `0.838` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `13535.52` | `0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `10343.91` | `0.861` | `1.000` | `0.878` | `1.000` | `0.819` | `0.396` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `6524.98` | `0.730` | `0.733` | `0.887` | `1.000` | `0.941` | `0.803` | `soft_accepted` | missing_exact_anchors | web@1.2.0, Property | - |
| `helm-01` | `summary` | `helm` | `2435.44` | `0.964` | `1.000` | `0.911` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `12703.47` | `0.946` | `1.000` | `0.865` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `30424.99` | `0.943` | `1.000` | `0.858` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `8099.04` | `0.712` | `0.600` | `0.918` | `1.000` | `0.940` | `0.800` | `soft_accepted` | missing_exact_anchors | install, --no-dev | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `4530.75` | `0.745` | `0.800` | `0.816` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | xcodebuild | - |
| `make-02` | `summary` | `make` | `8647.02` | `0.959` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `9533.96` | `0.961` | `1.000` | `0.902` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `8483.14` | `0.609` | `0.222` | `0.777` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/components/Header.test.tsx, FAIL, src/components/Header.test.tsx | - |
| `dbt-01` | `summary` | `dbt` | `3264.52` | `0.778` | `0.833` | `0.891` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `6652.44` | `0.778` | `0.814` | `0.905` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | FAILED | - |
| `wrangler-01` | `summary` | `wrangler` | `4503.47` | `0.969` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `10888.77` | `0.959` | `1.000` | `0.898` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `5641.02` | `0.428` | `1.000` | `0.681` | `0.000` | `0.000` | `0.235` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `4750.34` | `0.512` | `1.000` | `0.708` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `5532.52` | `0.414` | `1.000` | `0.688` | `0.000` | `0.000` | `0.071` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `3745.42` | `0.654` | `1.000` | `0.705` | `0.500` | `0.414` | `0.429` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `2485.75` | `0.697` | `0.538` | `0.708` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | secret "api-env" not found, Warning BackOff | - |
| `npm-06` | `instruction_following` | `npm` | `2497.17` | `0.682` | `1.000` | `0.739` | `0.400` | `0.400` | `1.000` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `3241.53` | `0.293` | `0.200` | `0.681` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | [deps 4/4], pnpm install --frozen-lockfile, exit code: 1 | - |
| `terraform-09` | `instruction_following` | `terraform` | `10303.05` | `0.479` | `1.000` | `0.668` | `0.000` | `0.000` | `0.786` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `3281.59` | `0.577` | `1.000` | `0.922` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `8347.41` | `0.460` | `1.000` | `0.674` | `0.000` | `0.000` | `0.579` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `1100.35` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `4345.28` | `0.519` | `1.000` | `0.730` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `5405.21` | `0.521` | `1.000` | `0.809` | `0.000` | `0.000` | `0.778` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `3433.39` | `0.452` | `1.000` | `0.742` | `0.000` | `0.000` | `0.290` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `2920.30` | `0.470` | `1.000` | `0.566` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `5177.18` | `0.255` | `0.833` | `0.289` | `0.000` | `0.000` | `0.467` | `soft_accepted` | missing_exact_anchors | aws_lambda_function.api | - |
| `junit-01` | `structured` | `junit` | `3870.66` | `0.477` | `1.000` | `0.654` | `0.000` | `0.000` | `0.812` | `accepted` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `2640.91` | `0.380` | `1.000` | `0.378` | `0.000` | `0.000` | `0.667` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `9614.31` | `0.158` | `0.444` | `0.269` | `0.000` | `0.000` | `0.156` | `soft_accepted` | missing_exact_anchors | src/a.ts, src/b.ts | - |
| `docker-build-04` | `structured` | `docker-build` | `3917.00` | `0.398` | `1.000` | `0.504` | `0.000` | `0.000` | `0.467` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `4452.80` | `0.317` | `0.879` | `0.325` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | message | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `3667.56` | `0.388` | `1.000` | `0.541` | `0.000` | `0.000` | `0.261` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `2748.09` | `0.449` | `1.000` | `0.564` | `0.000` | `0.000` | `0.800` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `2538.81` | `0.574` | `1.000` | `0.931` | `0.000` | `0.000` | `0.947` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `4508.20` | `0.270` | `0.576` | `0.341` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | :api:compileJava, cause | - |
| `playwright-02` | `structured` | `playwright` | `7785.24` | `0.325` | `0.833` | `0.386` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | file | - |
| `postgres-04` | `structured` | `postgres` | `2999.47` | `0.502` | `1.000` | `0.788` | `0.000` | `0.000` | `0.652` | `accepted` | - | - | - |
| `vite-01` | `structured` | `vite` | `2859.94` | `0.271` | `1.000` | `0.219` | `0.000` | `0.000` | `0.050` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `4470.73` | `0.022` | `0.000` | `0.248` | `0.000` | `0.000` | `0.030` | `soft_accepted` | missing_exact_anchors, exact_format_style_mismatch | tests/test_a.py::test_one, tests/test_b.py::TestB::test_three | - |
| `git-04` | `exact_format` | `git` | `5265.80` | `0.154` | `1.000` | `0.275` | `0.000` | `0.000` | `0.071` | `soft_accepted` | exact_format_style_mismatch | - | - |
| `docker-04` | `exact_format` | `docker` | `9778.53` | `0.035` | `0.000` | `0.326` | `0.000` | `0.000` | `0.167` | `soft_accepted` | missing_exact_anchors, exact_format_style_mismatch | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | - |
| `npm-08` | `exact_format` | `npm` | `4062.07` | `0.023` | `0.000` | `0.251` | `0.000` | `0.000` | `0.030` | `soft_accepted` | missing_exact_anchors, exact_format_style_mismatch | 2.18.4 | - |
| `go-test-05` | `exact_format` | `go-test` | `4555.70` | `0.157` | `1.000` | `0.305` | `0.000` | `0.000` | `0.091` | `soft_accepted` | exact_format_style_mismatch | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `4045.29` | `0.196` | `1.000` | `0.305` | `0.000` | `0.000` | `1.000` | `soft_accepted` | exact_format_style_mismatch | - | - |
| `cargo-05` | `exact_format` | `cargo` | `2499.22` | `0.255` | `1.000` | `0.994` | `0.000` | `0.000` | `1.000` | `soft_accepted` | exact_format_style_mismatch | - | - |
| `curl-03` | `exact_format` | `curl` | `4923.05` | `0.149` | `1.000` | `0.243` | `0.000` | `0.000` | `0.027` | `soft_accepted` | exact_format_style_mismatch | - | - |
| `rails-02` | `exact_format` | `rails` | `4345.98` | `0.020` | `0.000` | `0.222` | `0.000` | `0.000` | `0.030` | `soft_accepted` | missing_exact_anchors, exact_format_style_mismatch | 20260518133742 | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `3996.71` | `0.929` | `1.000` | `0.859` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `3568.35` | `0.577` | `0.000` | `0.758` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | string | null, url: string, user.photoUrl | - |
| `postgres-05` | `explanation` | `postgres` | `3181.29` | `0.437` | `0.000` | `0.828` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | orders_customer_id_fkey, customer_id, customers | - |
| `docker-build-05` | `explanation` | `docker-build` | `1345.16` | `0.966` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `1834.19` | `0.966` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `3796.25` | `0.636` | `0.250` | `0.796` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | E0515, returns a reference | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `4150.23` | `0.721` | `0.583` | `0.862` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `3922.55` | `0.587` | `0.500` | `0.930` | `1.000` | `0.800` | `0.333` | `soft_accepted` | missing_exact_anchors | error: 'cout' was not declared in this scope | - |
| `testing-01` | `recall` | `testing` | `2517.77` | `0.977` | `1.000` | `0.944` | `1.000` | `0.973` | `0.909` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `4490.30` | `0.648` | `0.545` | `0.866` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /usr/src/app/index.js:12:15 | - |
| `package-management-01` | `recall` | `package-management` | `4857.50` | `0.969` | `1.000` | `0.876` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `2745.16` | `0.979` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `4344.41` | `0.946` | `1.000` | `0.900` | `1.000` | `0.914` | `0.714` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `8997.91` | `0.443` | `0.190` | `0.840` | `1.000` | `0.776` | `0.254` | `soft_accepted` | missing_exact_anchors | error[E0277], main.rs:5:26 | - |
| `ci-01` | `recall` | `ci` | `3260.74` | `0.543` | `0.286` | `0.840` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Error: Tests failed | - |
| `testing-03` | `recall` | `testing` | `2369.14` | `0.976` | `1.000` | `0.903` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `1803.31` | `0.976` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `31952.42` | `0.706` | `0.778` | `0.868` | `1.000` | `0.889` | `0.632` | `soft_accepted` | missing_exact_anchors | "ami" is required | - |
| `compilation-02` | `recall` | `compilation` | `1880.19` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `3649.62` | `0.565` | `0.364` | `0.802` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | failed with exit code 1 | - |
| `build-01` | `recall` | `build` | `2459.40` | `0.978` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `1031.10` | `0.971` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `3252.10` | `0.976` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `989.05` | `0.967` | `1.000` | `0.867` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `1316.82` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `1379.50` | `0.986` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `1770.67` | `0.592` | `0.364` | `0.931` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | COPY failed | - |
| `testing-04` | `recall` | `testing` | `2247.71` | `0.974` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `1018.66` | `0.976` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `3182.05` | `0.615` | `0.444` | `0.896` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERROR: failed to fetch | - |
| `testing-05` | `recall` | `testing` | `934.51` | `0.976` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `2396.14` | `0.914` | `1.000` | `0.879` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `4059.61` | `0.905` | `1.000` | `0.856` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `803.42` | `0.976` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `712.53` | `0.952` | `1.000` | `0.880` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `592.75` | `0.976` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `2527.27` | `0.879` | `1.000` | `0.811` | `1.000` | `0.910` | `0.700` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `2499.13` | `0.497` | `1.000` | `0.830` | `0.000` | `0.000` | `0.476` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `1145.57` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `2587.67` | `0.417` | `1.000` | `0.692` | `0.000` | `0.000` | `0.091` | `accepted` | - | - | - |
| `linting-02` | `structured` | `linting` | `1154.70` | `0.463` | `1.000` | `0.544` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `2669.93` | `0.471` | `1.000` | `0.594` | `0.000` | `0.000` | `0.923` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `1233.43` | `0.980` | `1.000` | `1.000` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `1081.30` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `1775.99` | `0.207` | `1.000` | `0.320` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `4310.72` | `0.085` | `0.000` | `0.747` | `0.000` | `0.000` | `0.500` | `soft_accepted` | missing_exact_anchors | OUTPUT: | - |
| `shell-04` | `exact_format` | `shell` | `806.91` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `3556.68` | `0.141` | `0.286` | `0.726` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Resources: 1 added | - |
| `build-05` | `exact_format` | `build` | `3297.51` | `0.233` | `1.000` | `0.333` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `818.52` | `0.582` | `1.000` | `0.658` | `0.500` | `0.400` | `0.333` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `1901.25` | `0.936` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `3576.51` | `0.921` | `1.000` | `0.842` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `1939.91` | `0.888` | `1.000` | `0.885` | `1.000` | `0.836` | `0.455` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `2507.84` | `0.936` | `1.000` | `0.873` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `4741.25` | `0.847` | `1.000` | `0.837` | `1.000` | `0.785` | `0.282` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `3245.10` | `0.931` | `1.000` | `0.861` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `872.46` | `0.946` | `1.000` | `0.891` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `1950.33` | `0.940` | `1.000` | `0.879` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `5680.39` | `0.939` | `1.000` | `0.879` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `3149.92` | `0.851` | `1.000` | `0.830` | `1.000` | `0.809` | `0.364` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `1169.25` | `0.944` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `861.52` | `0.964` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `2625.27` | `0.908` | `1.000` | `0.816` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `817.11` | `0.932` | `1.000` | `0.864` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `437.21` | `0.920` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `646.14` | `0.943` | `1.000` | `0.886` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `1759.91` | `0.947` | `1.000` | `0.894` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `4317.46` | `0.868` | `1.000` | `0.844` | `1.000` | `0.836` | `0.455` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `3894.98` | `0.933` | `1.000` | `0.866` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `4117.53` | `0.471` | `1.000` | `0.594` | `0.000` | `0.000` | `0.923` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `1409.08` | `0.980` | `1.000` | `1.000` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `1212.51` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `1418.25` | `0.207` | `1.000` | `0.320` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `3417.13` | `0.700` | `1.000` | `0.335` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `4827.85` | `0.141` | `0.286` | `0.726` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Resources: 1 added | - |
| `runtime-07` | `exact_format` | `runtime` | `955.37` | `0.207` | `1.000` | `0.319` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `2384.39` | `0.227` | `1.000` | `0.791` | `0.000` | `0.000` | `0.750` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `shell-08` | `exact_format` | `shell` | `912.57` | `0.231` | `1.000` | `0.646` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `1803.61` | `0.936` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `4254.13` | `0.921` | `1.000` | `0.842` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `2771.13` | `0.642` | `0.000` | `0.909` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Could not locate 'config.yaml' | - |
| `explanation-13` | `explanation` | `explanation` | `2258.23` | `0.618` | `0.000` | `0.853` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | cannot list resource "pods" | - |
| `explanation-14` | `explanation` | `explanation` | `1064.38` | `0.946` | `1.000` | `0.891` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `2215.66` | `0.636` | `0.000` | `0.897` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Cannot find module 'lodash' | - |
| `explanation-16` | `explanation` | `explanation` | `3062.97` | `0.913` | `1.000` | `0.826` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `5602.60` | `0.928` | `1.000` | `0.856` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1182.33` | `0.948` | `1.000` | `0.896` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
