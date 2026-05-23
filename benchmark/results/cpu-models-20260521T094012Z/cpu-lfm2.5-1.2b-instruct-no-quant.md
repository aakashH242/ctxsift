# cpu-lfm2.5-1.2b-instruct-no-quant

## Scenario

- track: `cpu`
- phase: `cpu-screen`
- model: `LiquidAI/LFM2.5-1.2B-Instruct-GGUF`
- quantization: `none`
- device: `cpu`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `5934.67`
- cpu_rss_bytes: `null`
- gpu_peak_bytes: `null`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `267`
- accepted_count: `126`
- soft_accepted_count: `141`
- rejected_count: `13`
- exact_pass_count: `131`
- avg_inference_ms: `7401.04`
- p95_inference_ms: `14813.77`
- avg_exact_preservation_ratio: `0.729`
- avg_summary_quality_ratio: `0.816`
- avg_format_adherence_score: `0.825`
- avg_instruction_following_score: `0.820`
- avg_brevity_ratio: `0.942`
- avg_case_score: `0.715`
- p10_case_score: `0.240`
- quality_core: `0.620`
- latency_factor: `0.850`
- final_score: `52.69`
- peak_cpu_rss_bytes: `null`
- peak_gpu_bytes: `null`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `3958.53` | `0.992` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-02` | `summary` | `python` | `6570.09` | `0.839` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `python-03` | `recall` | `python` | `10415.35` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `10981.65` | `0.994` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `8647.86` | `0.593` | `0.407` | `0.859` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | python tools/export_report.py --input data/may.csv --format parquet, /workspace/src/reports/export.py, data/may.csv | - |
| `pytest-01` | `recall` | `pytest` | `9052.96` | `0.486` | `0.091` | `0.924` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/api/test_users.py -q, tests/api/test_users.py::test_create_user_rejects_duplicate[email], tests/api/test_users.py:47, AssertionError | - |
| `pytest-02` | `summary` | `pytest` | `13036.87` | `0.699` | `0.372` | `0.950` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/integration/test_billing_api.py::test_invoice_webhook_uses_signature, /workspace/tests/integration/test_billing_api.py:73, 1 error in 2.31s | - |
| `pytest-03` | `recall` | `pytest` | `12983.38` | `0.581` | `0.341` | `0.923` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests -q -x, tests/jobs/test_retention.py::test_archive_marks_job_deleted, psycopg.errors.ForeignKeyViolation | - |
| `pytest-04` | `recall` | `pytest` | `8247.51` | `0.710` | `0.650` | `0.973` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /workspace/tests/cli/test_export.py:12, pytest.mark.slowdb | - |
| `pytest-05` | `summary` | `pytest` | `8848.75` | `0.702` | `0.431` | `0.920` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/unit tests/integration --disable-warnings=0, src/billing/client.py:9, 1 error during collection | - |
| `mypy-01` | `recall` | `mypy` | `7194.91` | `0.749` | `0.756` | `0.964` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/accounts/user_service.py:84 | - |
| `mypy-02` | `summary` | `mypy` | `10385.93` | `0.720` | `0.579` | `0.909` | `1.000` | `0.976` | `0.921` | `soft_accepted` | missing_exact_anchors | mypy src tests --pretty --show-error-codes, arg-type | - |
| `mypy-03` | `recall` | `mypy` | `4582.78` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `7867.98` | `0.763` | `0.667` | `0.954` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Client, all, Found 1 error. | - |
| `ruff-02` | `summary` | `ruff` | `4855.64` | `0.743` | `0.600` | `0.936` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ruff format --check src tests | - |
| `ruff-03` | `summary` | `ruff` | `7592.41` | `0.813` | `0.902` | `0.952` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | except | - |
| `pylint-01` | `recall` | `pylint` | `3231.43` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `7922.97` | `0.787` | `0.877` | `0.926` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | parse-error | - |
| `pylint-03` | `summary` | `pylint` | `4441.38` | `0.987` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `6927.69` | `0.767` | `0.700` | `0.945` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | black --check src tests | - |
| `black-02` | `summary` | `black` | `6850.41` | `0.778` | `0.745` | `0.949` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | black src | - |
| `black-03` | `recall` | `black` | `5702.16` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `11590.04` | `0.804` | `0.905` | `0.954` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | package-lock.json | - |
| `npm-02` | `summary` | `npm` | `9766.59` | `0.809` | `0.889` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | peer react@"^17.0.0" | - |
| `npm-03` | `summary` | `npm` | `4708.41` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `5556.10` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `8707.16` | `0.793` | `0.818` | `0.946` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERR_PNPM_NO_MATCHING_VERSION | - |
| `pnpm-03` | `summary` | `pnpm` | `10638.28` | `0.992` | `1.000` | `0.981` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `7881.42` | `0.706` | `0.467` | `0.911` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tsc -p tsconfig.json --noEmit, src/server/index.ts(3,18), src/server/index.ts(4,18) | - |
| `typescript-02` | `recall` | `typescript` | `9164.90` | `0.800` | `0.895` | `0.955` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | string | undefined | - |
| `typescript-03` | `summary` | `typescript` | `10045.85` | `0.714` | `0.577` | `0.864` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tsc src/index.ts src/http.ts --pretty false, src/index.ts(48,20) | - |
| `eslint-01` | `recall` | `eslint` | `9667.75` | `0.682` | `0.600` | `0.929` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /workspace/src/server.js, 3 problems (2 errors, 1 warning) | - |
| `eslint-02` | `summary` | `eslint` | `7052.62` | `0.788` | `0.773` | `0.960` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ESLint: 9.14.0 | - |
| `eslint-03` | `recall` | `eslint` | `9030.44` | `0.992` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `10891.16` | `0.449` | `0.000` | `0.913` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker build -t api:dev ., COPY docker/entrypoint.sh /entrypoint.sh, /docker/entrypoint.sh, Dockerfile:14, failed to solve | - |
| `docker-02` | `summary` | `docker` | `2212.28` | `0.990` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `10621.62` | `0.572` | `0.000` | `0.807` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker build -f docker/web.Dockerfile -t web:ci ., RUN npm ci, ERESOLVE, react-dates@21.8.0, react@18.2.0, exit code: 1 | - |
| `docker-compose-01` | `summary` | `docker-compose` | `2204.50` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `12471.16` | `0.787` | `0.875` | `0.927` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | app-1 exited with code 1 | - |
| `docker-compose-03` | `summary` | `docker-compose` | `3234.42` | `0.985` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `8520.85` | `0.812` | `0.882` | `0.962` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | kubectl-edit | - |
| `kubectl-02` | `recall` | `kubectl` | `13761.78` | `0.738` | `0.737` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ghcr.io/acme/api:2026.05.15-3 | - |
| `kubectl-03` | `summary` | `kubectl` | `6318.35` | `0.819` | `0.889` | `0.979` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | timed out waiting for the condition | - |
| `kubectl-04` | `recall` | `kubectl` | `13435.95` | `0.743` | `0.762` | `0.923` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /app/config.yaml | - |
| `terraform-01` | `summary` | `terraform` | `4886.10` | `0.985` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `8420.90` | `0.700` | `0.684` | `0.945` | `1.000` | `0.938` | `0.794` | `soft_accepted` | missing_exact_anchors | terraform plan | - |
| `terraform-03` | `recall` | `terraform` | `6398.53` | `0.995` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `7074.45` | `0.655` | `0.195` | `0.929` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform test, tests/aws.tftest.hcl line 18, Test assertion failed, aws_instance.web.instance_type | - |
| `mixed-01` | `recall` | `mixed` | `7713.75` | `0.780` | `0.837` | `0.964` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | rsync warning | - |
| `mixed-02` | `summary` | `mixed` | `6719.36` | `0.695` | `0.378` | `0.934` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | make integration, Error 2, integration | - |
| `git-01` | `recall` | `git` | `4358.51` | `0.972` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `7139.49` | `0.679` | `0.593` | `0.927` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | main -> main, failed to push some refs | - |
| `git-03` | `recall` | `git` | `12630.32` | `0.597` | `0.375` | `0.936` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | curl 56, Connection reset by peer, invalid index-pack output | - |
| `curl-01` | `recall` | `curl` | `15586.13` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `8407.13` | `0.842` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `ssh-01` | `summary` | `ssh` | `8572.01` | `0.646` | `0.238` | `0.876` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | GIT_SSH_COMMAND="ssh -o IdentitiesOnly=yes -i ~/.ssh/deploy_key" git ls-remote git@github.com:example/mono-app.git, fatal: Could not read from remote repository., git@github.com:example/mono-app.git | - |
| `ssh-02` | `summary` | `ssh` | `4217.70` | `0.980` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `10769.82` | `0.766` | `0.677` | `0.955` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | status=203/EXEC | - |
| `systemd-02` | `summary` | `systemd` | `12353.15` | `0.748` | `0.643` | `0.923` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /etc/api/config.yaml | - |
| `apt-01` | `summary` | `apt` | `4907.21` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `15266.91` | `0.615` | `0.429` | `0.924` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | sudo dnf install python3-devel postgresql-devel, conflicting requests | - |
| `go-build-01` | `summary` | `go-build` | `3739.98` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `10775.67` | `0.669` | `0.267` | `0.925` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | go test ./... -run TestCacheTTL -count=1, cache_test.go:47 | - |
| `javac-01` | `summary` | `javac` | `9445.49` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `14046.59` | `0.806` | `0.913` | `0.925` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | UserControllerTest.getUser_notFound_returns404 | - |
| `maven-02` | `summary` | `maven` | `11700.37` | `0.599` | `0.000` | `0.886` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mvn -U -DskipTests package, org.postgresql:postgresql:jar:42.7.3, Failed to execute goal on project ingest-service, Could not resolve dependencies | - |
| `gradle-01` | `recall` | `gradle` | `10615.09` | `0.751` | `0.762` | `0.961` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | :service:compileClasspath | - |
| `gradle-02` | `summary` | `gradle` | `7329.77` | `0.768` | `0.722` | `0.933` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Execution failed for task ':test' | - |
| `cargo-01` | `summary` | `cargo` | `8212.01` | `0.789` | `0.788` | `0.952` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | error[E0308] | - |
| `cargo-02` | `summary` | `cargo` | `6302.62` | `0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `5029.40` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-04` | `summary` | `npm` | `6611.66` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `4977.71` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `8345.09` | `0.985` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `9486.13` | `0.990` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `9753.82` | `0.637` | `0.133` | `0.915` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/api/test_auth.py -k login -q, tests/api/test_auth.py:88, assert 200 == 429 | - |
| `mypy-04` | `summary` | `mypy` | `7906.80` | `0.979` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `14514.17` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund, Dockerfile:8, zod@3.23.8, failed to solve | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='- failed to solve: npm ci command mismatch - lockfile missing: zod@3.23.8, undici-types@6.19.8' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='- failed to solve: npm ci command mismatch - zod@3.23.8, undici-types@6.19.8 missing' |
| `docker-compose-04` | `summary` | `docker-compose` | `10401.26` | `0.767` | `0.733` | `0.921` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mono-api-1, port is already allocated | - |
| `kubectl-05` | `summary` | `kubectl` | `2645.16` | `0.982` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `14858.92` | `0.805` | `0.882` | `0.941` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | migrate | - |
| `kubectl-07` | `recall` | `kubectl` | `4021.81` | `0.988` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `15246.29` | `0.696` | `0.636` | `0.928` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform plan -lock-timeout=5s -out=tfplan | - |
| `terraform-06` | `summary` | `terraform` | `8563.57` | `0.803` | `0.867` | `0.944` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Reference to undeclared resource | - |
| `terraform-07` | `summary` | `terraform` | `10620.27` | `0.593` | `0.000` | `0.868` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform plan -detailed-exitcode -no-color, Plan: 1 to add, 1 to change, 0 to destroy., 2, aws_security_group_rule.web_https | - |
| `nginx-01` | `summary` | `nginx` | `6541.56` | `0.750` | `0.611` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "server" directive is not allowed here, configuration file /etc/nginx/nginx.conf test failed | - |
| `nginx-02` | `summary` | `nginx` | `4227.00` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `24733.50` | `0.688` | `0.600` | `0.958` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | psql -h 127.0.0.1 -U app_user -d appdb -c 'select 1' | - |
| `postgres-02` | `summary` | `postgres` | `3797.01` | `0.987` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `6848.42` | `0.741` | `0.600` | `0.928` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mysql -h db.example.net -u reporting -p reporting_db | - |
| `mysql-02` | `summary` | `mysql` | `4284.54` | `0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `8721.48` | `0.987` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `5779.28` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `10337.86` | `0.643` | `0.524` | `0.881` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | line=91, Ruff F821, exit code 2 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `13042.35` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `5781.39` | `0.633` | `0.250` | `0.830` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm run build, webpack --mode production | - |
| `make-01` | `summary` | `make` | `10059.44` | `0.678` | `0.395` | `0.871` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | make CFLAGS='-O2 -Wall -Werror' all, src/parser.c:214:12, parse_config | - |
| `tar-01` | `summary` | `tar` | `6981.94` | `0.810` | `0.857` | `0.972` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | unexpected end of file | - |
| `ansible-01` | `recall` | `ansible` | `5122.23` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `8066.46` | `0.805` | `0.833` | `0.972` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | some files vanished before they could be transferred | - |
| `test-failure-01` | `recall` | `test-failure` | `14779.81` | `0.449` | `0.000` | `0.914` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/unit/test_invoice_totals.py::test_discount_rounding, tests/unit/test_invoice_totals.py:88, Decimal('17.50'), Decimal('17.49'), ROUND_HALF_UP is deprecated for discounts; use ROUND_HALF_EVEN | - |
| `compiler-error-01` | `recall` | `compiler-error` | `16490.05` | `0.619` | `0.448` | `0.905` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | error[E0382], borrow of moved value: `req`, req.into_body(), req.clone().into_body() | - |
| `ci-log-01` | `recall` | `ci-log` | `12651.28` | `0.458` | `0.000` | `0.953` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | helm upgrade --install payments-api charts/payments-api --namespace prod-payments, Deployment.apps "payments-api" is invalid, spec.template.spec.containers[0].env[3].valueFrom.secretKeyRef.name, Invalid value: "", deployments.apps "payments-api" not found | - |
| `package-manager-01` | `recall` | `package-manager` | `14828.33` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `11313.03` | `0.583` | `0.000` | `0.840` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | github.com/acme/shop/checkout, TestCheckoutAppliesStoreCredit, checkout_test.go:71, total = 42.00, want 37.00, github.com/acme/shop/inventory, TestReconcileInventory, test timed out after 10m0s, worker.go:144 | - |
| `build-log-01` | `summary` | `build-log` | `13323.99` | `0.687` | `0.375` | `0.911` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | InvoiceMapper.java:[58,29], setTaxCode(java.lang.String) | - |
| `docker-build-02` | `summary` | `docker-build` | `14208.58` | `0.679` | `0.333` | `0.913` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | COPY apps/web ./apps/web, "/apps/web": not found | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `35175.41` | `0.472` | `0.625` | `0.687` | `0.500` | `0.386` | `0.242` | `soft_accepted` | missing_exact_anchors | @typescript-eslint/no-misused-promises, @typescript-eslint/no-explicit-any, @typescript-eslint/no-unsafe-assignment | - |
| `git-review-01` | `instruction_following` | `git-review` | `25328.31` | `0.704` | `1.000` | `0.776` | `0.429` | `0.429` | `1.000` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `14688.56` | `0.581` | `0.000` | `0.614` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | search endpoint failed after 2 attempts, exit status 22, https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `12657.40` | `0.408` | `0.778` | `0.814` | `0.000` | `0.000` | `0.806` | `soft_accepted` | missing_exact_anchors | reportArgumentType, reportUndefinedVariable | - |
| `structured-output-02` | `structured` | `structured-output` | `21173.24` | `0.372` | `0.905` | `0.545` | `0.000` | `0.000` | `0.926` | `soft_accepted` | missing_exact_anchors | Start docker compose | - |
| `structured-output-03` | `structured` | `structured-output` | `11534.78` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | createSession › rejects expired refresh token, src/auth/session.test.ts, "refresh token expired", "invalid refresh token", calculateTax › uses EU VAT for DE customer, src/billing/tax.test.ts, Expected: 19, Received: 0 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- Test: src/auth/session.test.ts File: src/auth/session.test.ts Error: refresh token expired' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='PASS src/auth/session.test.ts Error: refresh token expired "refresh token expired" "invalid refresh token" calculateTax › uses EU VAT for DE customer src/bil...' |
| `structured-output-04` | `structured` | `structured-output` | `15884.29` | `0.278` | `0.844` | `0.196` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /repo/apps/web/src/features/flags.ts | - |
| `exact-format-01` | `exact_format` | `exact-format` | `8082.01` | `0.185` | `1.000` | `0.332` | `0.000` | `0.000` | `0.043` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `8058.58` | `0.107` | `0.286` | `0.328` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | packages/web/src/search/searchBox.test.tsx | - |
| `exact-format-03` | `exact_format` | `exact-format` | `11222.66` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `5570.84` | `0.782` | `0.778` | `0.930` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `5825.98` | `0.735` | `0.750` | `0.830` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | string | undefined | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `6934.63` | `0.578` | `0.000` | `0.894` | `0.667` | `0.667` | `1.000` | `soft_accepted` | missing_exact_anchors | orders_customer_id_fkey, customer_id, 00000000-0000-0000-0000-000000000000, customers | - |
| `python-traceback-01` | `recall` | `python-traceback` | `9898.52` | `0.667` | `0.571` | `0.909` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | app.tasks.email.send_welcome_email, [bad@example.test](mailto:bad@example.test), retries exhausted for queue emails | - |
| `mypy-05` | `recall` | `mypy` | `8105.45` | `0.633` | `0.467` | `0.939` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Signature of "serialize" incompatible with supertype "BaseExporter", include_meta, -> bytes, -> str | - |
| `terraform-08` | `recall` | `terraform` | `12830.56` | `0.784` | `0.905` | `0.861` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | module.worker.aws_iam_policy.worker_inline | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `7922.10` | `0.586` | `0.348` | `0.933` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | InventorySyncTest > publishesBackorderEvent() FAILED, InventorySyncTest.java:132, OrderServiceTest > calculatesDiscountForGoldCustomer() PASSED | - |
| `kubernetes-01` | `recall` | `kubernetes` | `10622.29` | `0.655` | `0.520` | `0.946` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | api-7d9f8c8b99-mx2kq, Exit Code: 78, FATAL config: required env STRIPE_KEY is empty | - |
| `go-test-02` | `recall` | `go-test` | `9677.17` | `0.739` | `0.741` | `0.944` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | (*Store).Get(), TestConcurrentSetGet | - |
| `cargo-03` | `recall` | `cargo` | `9027.05` | `0.592` | `0.359` | `0.939` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | error[E0432], crates/storage/src/events.rs:7:5, gated behind the `sync` feature, could not compile `storage` | - |
| `docker-compose-05` | `recall` | `docker-compose` | `7810.79` | `0.547` | `0.250` | `0.924` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | container app-api-1 is unhealthy, dependency failed to start, migration failed; exiting, docker compose up --wait api worker | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `7361.56` | `0.629` | `0.464` | `0.924` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | packages/api/src/index.ts:4:25, /repo/packages/contracts/dist/index.d.ts, packages/contracts/src/index.ts | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `8313.16` | `0.539` | `0.238` | `0.906` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 20260518_add_workspace_limits.sql, relation "workspace_limits" already exists, packages/db/src/migrate.ts:77:13, packages/db/test/migrate.test.ts:44:7, exit code 1 | - |
| `pnpm-04` | `recall` | `pnpm` | `8539.44` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `8169.35` | `0.618` | `0.419` | `0.955` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Tests/UserDecoderTests.swift:47, XCTAssertEqual failed, fatalError | - |
| `elixir-01` | `recall` | `elixir` | `8407.29` | `0.722` | `0.696` | `0.945` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | key :ttl not found, refreshes expired keys | - |
| `rails-01` | `recall` | `rails` | `7469.20` | `0.537` | `0.235` | `0.904` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | index_events_on_request_id, already exists, 20260518093012_add_index_to_events_request_id.rb:3, ArgumentError | - |
| `phpunit-01` | `recall` | `phpunit` | `20980.77` | `0.503` | `0.213` | `0.783` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Tests\Billing\InvoiceTotalTest::testAppliesCreditBeforeTax, Failed asserting that '88.00' is identical to '86.40', /tests/Billing/InvoiceTotalTest.php:52, Failures: 1 | - |
| `nginx-03` | `recall` | `nginx` | `10223.10` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `8944.38` | `0.759` | `0.778` | `0.974` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | type "vector" does not exist, current transaction is aborted | - |
| `ansible-02` | `recall` | `ansible` | `20113.76` | `0.793` | `0.875` | `0.956` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Connection timed out | - |
| `bazel-01` | `recall` | `bazel` | `34757.96` | `0.502` | `0.167` | `0.862` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | //services/reporting:report_parser_test, Opening and ending tag mismatch: total line 18 and totals, services/reporting/parser.py", line 141, etree.fromstring(xml_bytes) | - |
| `powershell-01` | `recall` | `powershell` | `8591.95` | `0.671` | `0.562` | `0.945` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | cannot be loaded because running scripts is disabled, FullyQualifiedErrorId : UnauthorizedAccess | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `8774.14` | `0.794` | `0.882` | `0.950` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | web@1.7.0 | - |
| `python-pytest-01` | `summary` | `python-pytest` | `8176.44` | `0.771` | `0.783` | `0.902` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/refunds | - |
| `go-test-03` | `summary` | `go-test` | `7263.84` | `0.771` | `0.737` | `0.932` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | github.com/acme/api/internal/webhook | - |
| `npm-05` | `summary` | `npm` | `7611.97` | `0.957` | `1.000` | `0.892` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `5861.03` | `0.624` | `0.125` | `0.883` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | api/templates/deployment.yaml:42:29, executing, api/templates/deployment.yaml, Values.image.repository | - |
| `ruff-04` | `summary` | `ruff` | `10426.48` | `0.656` | `0.211` | `0.923` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | app/api/routes.py:3:1, app/services/user.py:88:89, tests/test_user.py:12:1 | - |
| `k6-01` | `summary` | `k6` | `6901.42` | `0.784` | `0.826` | `0.913` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | http_req_duration | - |
| `composer-01` | `summary` | `composer` | `5782.67` | `0.893` | `0.800` | `0.857` | `1.000` | `1.000` | `1.000` | `accepted` | - | install | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `6346.22` | `0.584` | `0.000` | `0.843` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | xcodebuild, -scheme, MobileApp, -configuration, Release | - |
| `make-02` | `summary` | `make` | `5753.91` | `0.752` | `0.682` | `0.912` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | -Iinclude, build/server.o | - |
| `python-pytest-02` | `summary` | `python-pytest` | `5571.04` | `0.693` | `0.462` | `0.874` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | auto, tests/e2e | - |
| `jest-01` | `summary` | `jest` | `6341.96` | `0.766` | `0.889` | `0.822` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | matches | - |
| `dbt-01` | `summary` | `dbt` | `6991.86` | `0.785` | `0.833` | `0.914` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `6948.70` | `0.650` | `0.186` | `0.920` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/test_signup.py, tests/test_signup.py::test_signup_is_idempotent, sqlalchemy.exc.IntegrityError, psycopg.errors.UniqueViolation | - |
| `wrangler-01` | `summary` | `wrangler` | `7977.02` | `0.955` | `1.000` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `6286.01` | `0.778` | `0.778` | `0.927` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Falsifying, example | - |
| `eslint-05` | `instruction_following` | `eslint` | `10285.68` | `0.518` | `0.815` | `0.700` | `0.500` | `0.405` | `0.364` | `soft_accepted` | missing_exact_anchors | 22:7 | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `8100.27` | `0.819` | `1.000` | `0.841` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `3574.76` | `0.430` | `1.000` | `0.709` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `7347.27` | `0.557` | `0.900` | `0.719` | `0.400` | `0.400` | `1.000` | `soft_accepted` | missing_exact_anchors | ubuntu-latest | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `2956.73` | `0.916` | `1.000` | `0.719` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `4779.20` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `7666.33` | `0.430` | `0.800` | `0.820` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERR_PNPM_LOCKFILE_CONFIG_MISMATCH | - |
| `terraform-09` | `instruction_following` | `terraform` | `8568.49` | `0.313` | `0.000` | `0.665` | `0.250` | `0.227` | `0.688` | `soft_accepted` | missing_exact_anchors | aws_db_instance.main, destroyed, identifier = "prod-main" | - |
| `maven-03` | `instruction_following` | `maven` | `7370.13` | `0.530` | `0.125` | `0.772` | `0.667` | `0.667` | `1.000` | `soft_accepted` | missing_exact_anchors | UserService.java:[44,17], UserController.java:[28,31], java.lang.Long, java.util.UUID | - |
| `playwright-01` | `instruction_following` | `playwright` | `7038.23` | `0.614` | `1.000` | `0.712` | `0.250` | `0.250` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `4595.88` | `0.850` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `6868.58` | `0.399` | `1.000` | `0.816` | `0.000` | `0.000` | `0.250` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `9057.91` | `0.541` | `0.500` | `0.831` | `0.500` | `0.481` | `0.875` | `soft_accepted` | missing_exact_anchors | Option::unwrap(), left: 1750, right: 1749 | - |
| `shell-01` | `instruction_following` | `shell` | `6292.22` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | rsync, /var/backups/uploads, Permission denied (13), exit code 23 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='rsync: Permission denied (13)' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='rsync: Permission denied (13)' |
| `pyright-01` | `structured` | `pyright` | `8323.50` | `0.245` | `0.667` | `0.184` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /repo/app/user.py | - |
| `terraform-10` | `structured` | `terraform` | `6565.58` | `0.245` | `0.167` | `0.185` | `0.250` | `0.250` | `1.000` | `soft_accepted` | missing_exact_anchors | add, aws_iam_role.app, resource, aws_lambda_function.api, field | - |
| `junit-01` | `structured` | `junit` | `11529.46` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | Test, Error, Location, ---, CalculatorTest, dividesByZero | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='| Test | Error | Location | --- |--------------|------------------------------|----------| | CalculatorTest| dividesByZero FAILED | java.lang.ArithmeticExcep...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='CalculatorTest > dividesByZero FAILED java.lang.ArithmeticException: / by zero at Calculator.java:42 UserServiceTest > rejectsDuplicateEmail FAILED expected:...' |
| `kubernetes-03` | `structured` | `kubernetes` | `9133.42` | `0.262` | `0.857` | `0.191` | `0.000` | `0.000` | `0.800` | `soft_accepted` | missing_exact_anchors | name | - |
| `eslint-06` | `structured` | `eslint` | `11965.60` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | src/a.ts, line, column, rule, no-unused-vars, src/b.ts | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='src/a.ts { "line": 7, "column": "1", "rule": "error", "message": "x is assigned a value but never used" } src/b.ts { "line": 10, "column": "8", "rule": "warn...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass="- src/a.ts 1:7 error 'x' is assigned a value but never used no-unused-vars - src/b.ts 8:10 warning console.log is not allowed no-console 9:3 error Unexpected..." |
| `docker-build-04` | `structured` | `docker-build` | `4066.51` | `0.782` | `1.000` | `0.695` | `0.714` | `0.688` | `0.875` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `4681.20` | `0.350` | `1.000` | `0.196` | `0.000` | `0.000` | `0.917` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `10000.32` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | Job, Step, Exit, ---, test, Run | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='| Job | Step | Exit | --- |-----------|--------|------| | job | lint | success | | job | test | failed | Step: Run unit tests; exit=1 | | job | build | succe...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='job lint success 22s job test failed step="Run unit tests" exit=1 job build success 49s job deploy failed step="Upload artifact" exit=1' |
| `npm-07` | `structured` | `npm` | `10273.26` | `0.615` | `1.000` | `0.528` | `0.500` | `0.436` | `0.571` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `10966.37` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | File, Line, Code, Message, ---, app/api.py | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='| File | Line | Code | Message | |------|------|------|---------| | app/api.py | 10 | error: Module has no attribute "Router" [attr-defined] | Error in API m...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='app/api.py:10: error: Module has no attribute "Router" [attr-defined] app/auth.py:44: error: Incompatible return value type (got "None", expected "User") [re...' |
| `gradle-03` | `structured` | `gradle` | `11978.65` | `0.176` | `0.485` | `0.186` | `0.000` | `0.000` | `0.538` | `soft_accepted` | missing_exact_anchors | failed, :api:compileJava | - |
| `playwright-02` | `structured` | `playwright` | `5551.23` | `0.357` | `1.000` | `0.189` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `8681.57` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | errors, file, migrations/004.sql, line, message, column | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='psql:migrations/004.sql ERROR: column "tenant_id" contains null values STATEMENT: ALTER TABLE users ALTER COLUMN tenant_id SET NOT NULL ERROR: current transa...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='psql:migrations/004.sql errors file migrations/004.sql line 12: ERROR: column "tenant_id" contains null values line 13: STATEMENT: ALTER TABLE users ALTER CO...' |
| `vite-01` | `structured` | `vite` | `8384.81` | `0.050` | `0.000` | `0.170` | `0.000` | `0.000` | `0.071` | `soft_accepted` | missing_exact_anchors | /repo/apps/admin/src/App.tsx, @acme/ui/Button, /repo/apps/admin/src/client.ts, @acme/api, /repo/apps/public/src/Home.tsx | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `3787.79` | `0.190` | `1.000` | `0.318` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `2918.84` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `3456.09` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `1852.63` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `3211.64` | `0.232` | `1.000` | `0.317` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `6210.25` | `0.231` | `1.000` | `0.306` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `4293.91` | `0.190` | `1.000` | `0.334` | `0.000` | `0.000` | `0.125` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `2230.00` | `0.191` | `1.000` | `0.281` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `2629.52` | `0.202` | `1.000` | `0.275` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `2366.99` | `0.950` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `7483.46` | `0.660` | `0.222` | `0.864` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | string | null, url: string | - |
| `postgres-05` | `explanation` | `postgres` | `5512.34` | `0.875` | `1.000` | `0.883` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `4200.25` | `0.940` | `1.000` | `0.880` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `5657.46` | `0.963` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `5653.90` | `0.691` | `0.750` | `0.726` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | returns a reference | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `5155.66` | `0.922` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `4871.89` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `6119.22` | `0.648` | `0.643` | `0.908` | `1.000` | `0.836` | `0.455` | `soft_accepted` | missing_exact_anchors | TestCalculator::testDivideByZero | - |
| `testing-02` | `recall` | `testing` | `5654.19` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `5747.27` | `0.656` | `0.538` | `0.919` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm ERR! code E404 | - |
| `runtime-02` | `recall` | `runtime` | `4949.04` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `5278.03` | `0.663` | `0.545` | `0.937` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Program.cs(15,10) | - |
| `package-management-02` | `recall` | `package-management` | `5319.38` | `0.678` | `0.667` | `0.929` | `1.000` | `0.896` | `0.652` | `soft_accepted` | missing_exact_anchors | error[E0277] | - |
| `ci-01` | `recall` | `ci` | `4085.67` | `0.967` | `1.000` | `0.868` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `4479.87` | `0.954` | `1.000` | `0.814` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `6472.71` | `0.952` | `1.000` | `0.892` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `6040.34` | `0.751` | `0.778` | `0.934` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "ami" is required | - |
| `compilation-02` | `recall` | `compilation` | `5262.25` | `0.768` | `0.810` | `0.957` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Cannot find module 'lodash' | - |
| `ci-02` | `recall` | `ci` | `1748.30` | `0.975` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `5612.41` | `0.941` | `1.000` | `0.858` | `1.000` | `0.929` | `0.762` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `3296.83` | `0.979` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `3839.05` | `0.981` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `4945.72` | `0.965` | `1.000` | `0.858` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `4095.46` | `0.930` | `1.000` | `0.862` | `1.000` | `0.893` | `0.643` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `4074.80` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `4886.58` | `0.950` | `1.000` | `0.801` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `10843.74` | `0.773` | `0.833` | `0.937` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | User signs in | - |
| `build-02` | `recall` | `build` | `4690.13` | `0.641` | `0.500` | `0.918` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | error: expected ';' | - |
| `ci-03` | `recall` | `ci` | `10283.42` | `0.837` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `1815.28` | `0.974` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `6129.50` | `0.914` | `1.000` | `0.878` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `4093.85` | `0.903` | `1.000` | `0.850` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `1908.28` | `0.955` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `4230.68` | `0.941` | `1.000` | `0.853` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `5453.04` | `0.665` | `0.667` | `0.900` | `1.000` | `0.812` | `0.375` | `soft_accepted` | missing_exact_anchors | unable to resolve dependency tree | - |
| `rust-02` | `summary` | `rust` | `5915.86` | `0.942` | `1.000` | `0.855` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `8491.64` | `0.565` | `0.636` | `0.870` | `0.500` | `0.465` | `0.769` | `soft_accepted` | missing_exact_anchors | index.js | - |
| `testing-06` | `instruction_following` | `testing` | `7272.77` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `8892.46` | `0.551` | `1.000` | `0.785` | `0.500` | `0.369` | `0.125` | `soft_accepted` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `4442.46` | `0.241` | `0.667` | `0.168` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | found 1 | - |
| `kubernetes-06` | `structured` | `kubernetes` | `7697.76` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage, prompt_scaffold_echo | kind, metadata, spec | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='{"kind": "Service", "metadata": {"name": "my-service", "namespace": "default"}, "spec": {"clusterIP": "10.0.0.1", "ports": [{"port": 80, "protocol": "TCP"}]}}' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='- follow the requested structure exactly - include only items that satisfy the instruction - omit related but out-of-scope items' |
| `deployment-02` | `structured` | `deployment` | `2331.85` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `2102.97` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `6229.81` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | Timeout while waiting for response | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response INFO: Retrying... ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response INFO: Retrying... ERROR: Timeout while waiting for response' |
| `shell-03` | `exact_format` | `shell` | `2012.90` | `0.252` | `1.000` | `0.765` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `5291.69` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | NullPointerException | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='NullPointerException: null' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='NullPointerException: null' |
| `build-04` | `exact_format` | `build` | `7491.05` | `0.192` | `0.714` | `0.693` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | instance_id | - |
| `build-05` | `exact_format` | `build` | `2173.80` | `0.216` | `1.000` | `0.325` | `0.000` | `0.000` | `0.667` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `2099.10` | `0.232` | `1.000` | `0.658` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `3099.24` | `0.947` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `3485.96` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `5151.32` | `0.722` | `0.500` | `0.899` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pull access denied | - |
| `runtime-05` | `explanation` | `runtime` | `3730.76` | `0.943` | `1.000` | `0.885` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `4246.68` | `0.957` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `1589.93` | `0.927` | `1.000` | `0.854` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `2778.83` | `0.910` | `1.000` | `0.820` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `3006.72` | `0.933` | `1.000` | `0.866` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `4283.60` | `0.913` | `1.000` | `0.826` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `3821.42` | `0.631` | `0.000` | `0.886` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | no configured push destination | - |
| `explanation-04` | `explanation` | `explanation` | `4043.71` | `0.625` | `0.000` | `0.870` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | exited with 1 | - |
| `explanation-05` | `explanation` | `explanation` | `3127.15` | `0.901` | `1.000` | `0.802` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `1448.67` | `0.944` | `1.000` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `4974.53` | `0.954` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `3552.46` | `0.919` | `1.000` | `0.838` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `5086.63` | `0.625` | `0.000` | `0.870` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | would be overwritten by merge | - |
| `explanation-10` | `explanation` | `explanation` | `1754.58` | `0.952` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `3582.13` | `0.916` | `1.000` | `0.832` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `1445.87` | `0.933` | `1.000` | `0.866` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `8025.44` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage, prompt_scaffold_echo | kind, metadata, spec | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='{"kind": "Service", "metadata": {"name": "my-service", "namespace": "default"}, "spec": {"clusterIP": "10.0.0.1", "ports": [{"port": 80, "protocol": "TCP"}]}}' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='- follow the requested structure exactly - include only items that satisfy the instruction - omit related but out-of-scope items' |
| `linting-03` | `structured` | `linting` | `2362.85` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `1908.47` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `4502.77` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | Timeout while waiting for response | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response INFO: Retrying...' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response INFO: Retrying...' |
| `shell-07` | `exact_format` | `shell` | `1754.21` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `6618.90` | `0.192` | `0.714` | `0.693` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | instance_id | - |
| `runtime-07` | `exact_format` | `runtime` | `2279.80` | `0.207` | `1.000` | `0.324` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `2878.82` | `0.268` | `1.000` | `0.850` | `0.000` | `0.000` | `0.667` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `1972.21` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `4364.77` | `0.947` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `3282.89` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `1720.15` | `0.964` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `5387.23` | `0.970` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `3046.74` | `0.910` | `1.000` | `0.820` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `3966.36` | `0.934` | `1.000` | `0.869` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `3010.33` | `0.913` | `1.000` | `0.826` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `2983.35` | `0.928` | `1.000` | `0.856` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `3948.56` | `0.938` | `1.000` | `0.875` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
