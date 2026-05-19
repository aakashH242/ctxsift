# gpu-qwen2.5-1.5b-no-quant

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

- load_ms: `228804.23`
- cpu_rss_bytes: `2193457152`
- gpu_peak_bytes: `4312901120`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `267`
- accepted_count: `144`
- soft_accepted_count: `123`
- rejected_count: `13`
- exact_pass_count: `146`
- avg_inference_ms: `3782.86`
- p95_inference_ms: `10126.17`
- avg_exact_preservation_ratio: `0.697`
- avg_summary_quality_ratio: `0.803`
- avg_format_adherence_score: `0.754`
- avg_instruction_following_score: `0.723`
- avg_brevity_ratio: `0.842`
- avg_case_score: `0.677`
- p10_case_score: `0.284`
- quality_core: `0.598`
- latency_factor: `0.909`
- final_score: `54.38`
- peak_cpu_rss_bytes: `2193547264`
- peak_gpu_bytes: `4502294528`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `5219.42` | `0.741` | `0.833` | `0.904` | `1.000` | `0.912` | `0.706` | `soft_accepted` | missing_exact_anchors | line 18 column 3 | - |
| `python-02` | `summary` | `python` | `7591.73` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass="python services/worker.py --queue emails --concurrency 4 INFO boot: reading .env.local WARNING redis retry 1/3 failed: ConnectionResetError(104, 'Connection ..." repair_status=rejected repair_flags=['control_token_leakage'] repair_pass="python services/worker.py --queue emails --concurrency 4 INFO boot: reading .env.local WARNING redis retry 1/3 failed: ConnectionResetError(104, 'Connection ..." |
| `python-03` | `recall` | `python` | `5131.60` | `0.932` | `1.000` | `0.906` | `1.000` | `0.868` | `0.561` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `27880.24` | `0.890` | `1.000` | `0.901` | `1.000` | `0.744` | `0.147` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `8151.24` | `0.700` | `0.630` | `0.962` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /workspace/src/reports/export.py, line 131 | - |
| `pytest-01` | `recall` | `pytest` | `1032.57` | `0.429` | `0.000` | `0.820` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/api/test_users.py -q, tests/api/test_users.py::test_create_user_rejects_duplicate[email], tests/api/test_users.py:47, AssertionError, 500 == 409 | - |
| `pytest-02` | `summary` | `pytest` | `20811.52` | `0.879` | `1.000` | `0.939` | `1.000` | `0.808` | `0.360` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `18201.98` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | pytest tests -q -x, tests/jobs/test_retention.py::test_archive_marks_job_deleted, teardown, psycopg.errors.ForeignKeyViolation, job_runs_job_id_fkey, 149 passed, 1 skipped, 1 error in 58.73s | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='```python $ pytest tests -q -x ........................................................................ [ 48%] ..............................s..................' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='```python $ pytest tests -q -x ........................................................................ [ 48%] ..............................s..................' |
| `pytest-04` | `recall` | `pytest` | `1777.27` | `0.627` | `0.475` | `0.895` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /workspace/tests/cli/test_export.py:12, PytestUnknownMarkWarning, pytest.mark.slowdb | - |
| `pytest-05` | `summary` | `pytest` | `3700.81` | `0.661` | `0.275` | `0.911` | `1.000` | `0.990` | `0.968` | `soft_accepted` | missing_exact_anchors | pytest tests/unit tests/integration --disable-warnings=0, src/billing/client.py:9, ModuleNotFoundError, 1 error during collection | - |
| `mypy-01` | `recall` | `mypy` | `2127.76` | `0.525` | `0.195` | `0.919` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mypy src/accounts/user_service.py --show-error-codes, src/accounts/user_service.py:84, attr-defined, Found 1 error in 1 file | - |
| `mypy-02` | `summary` | `mypy` | `5210.56` | `0.591` | `0.211` | `0.864` | `1.000` | `0.894` | `0.648` | `soft_accepted` | missing_exact_anchors | mypy src tests --pretty --show-error-codes, src/payments/retry.py:118, arg-type, checked 37 source files | - |
| `mypy-03` | `recall` | `mypy` | `5775.27` | `0.574` | `0.455` | `0.883` | `1.000` | `0.850` | `0.500` | `soft_accepted` | missing_exact_anchors | src/orders/normalize.py:41, union-attr, type: ignore | - |
| `ruff-01` | `summary` | `ruff` | `3043.65` | `0.953` | `0.911` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `937.48` | `0.995` | `1.000` | `0.988` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `8198.30` | `0.970` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `8781.01` | `0.981` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `9394.96` | `0.585` | `0.439` | `0.893` | `1.000` | `0.902` | `0.674` | `soft_accepted` | missing_exact_anchors | pylint src/config/runtime.py src/api/server.py, src/config/runtime.py:44:0, expected ":" | - |
| `pylint-03` | `summary` | `pylint` | `4380.83` | `0.584` | `0.267` | `0.880` | `1.000` | `0.837` | `0.456` | `soft_accepted` | missing_exact_anchors | pylint src/notifications/push.py --jobs=0, src/notifications/push.py:6:0, import-error, --jobs=0 | - |
| `black-01` | `summary` | `black` | `1367.73` | `0.987` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `1562.15` | `0.971` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `929.80` | `0.997` | `1.000` | `0.989` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `4201.04` | `0.427` | `0.000` | `0.888` | `1.000` | `0.940` | `0.800` | `soft_accepted` | missing_exact_anchors | npm ci, EUSAGE, react@18.3.1, scheduler@0.23.2, package-lock.json, /home/dev/.npm/_logs/2026-05-15T09_20_11_449Z-debug-0.log | - |
| `npm-02` | `summary` | `npm` | `6662.04` | `0.868` | `1.000` | `0.909` | `1.000` | `0.809` | `0.365` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `24906.55` | `0.690` | `0.927` | `0.920` | `1.000` | `0.724` | `0.081` | `soft_accepted` | missing_exact_anchors | storefront@2.8.1 | - |
| `pnpm-01` | `recall` | `pnpm` | `3517.09` | `0.755` | `0.789` | `0.931` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERR_PNPM_OUTDATED_LOCKFILE | - |
| `pnpm-02` | `summary` | `pnpm` | `5424.73` | `0.950` | `1.000` | `0.936` | `1.000` | `0.951` | `0.837` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `6053.60` | `0.567` | `0.286` | `0.857` | `1.000` | `0.806` | `0.354` | `soft_accepted` | missing_exact_anchors | packages/api, health route > returns build metadata when git sha is present, ERR_PNPM_RECURSIVE_RUN_FIRST_FAIL, api@1.6.0, Exit status 1 | - |
| `typescript-01` | `summary` | `typescript` | `2129.35` | `0.661` | `0.333` | `0.861` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tsc -p tsconfig.json --noEmit, src/server/index.ts(3,18), TS2307, src/server/index.ts(4,18) | - |
| `typescript-02` | `recall` | `typescript` | `5146.40` | `0.471` | `0.105` | `0.912` | `1.000` | `0.935` | `0.784` | `soft_accepted` | missing_exact_anchors | tsc -b packages/, packages/web/src/components/Price.tsx(22,9), TS2322, Watching for file changes | - |
| `typescript-03` | `summary` | `typescript` | `12042.53` | `0.631` | `0.769` | `0.902` | `0.500` | `0.439` | `0.594` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | tsc src/index.ts src/http.ts --pretty false | - |
| `eslint-01` | `recall` | `eslint` | `3507.81` | `0.957` | `1.000` | `0.923` | `1.000` | `0.929` | `0.765` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `5039.67` | `0.685` | `0.500` | `0.885` | `1.000` | `0.954` | `0.846` | `soft_accepted` | missing_exact_anchors | eslint ., ESLint: 9.14.0 | - |
| `eslint-03` | `recall` | `eslint` | `4131.59` | `0.760` | `0.808` | `0.923` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | maximum: 0 | - |
| `docker-01` | `recall` | `docker` | `11222.81` | `0.627` | `0.653` | `0.868` | `1.000` | `0.780` | `0.267` | `soft_accepted` | missing_exact_anchors | Dockerfile:14, failed to solve | - |
| `docker-02` | `summary` | `docker` | `1499.33` | `0.761` | `0.667` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker run --rm api:dev | - |
| `docker-03` | `summary` | `docker` | `6230.31` | `0.521` | `0.000` | `0.833` | `1.000` | `0.859` | `0.529` | `soft_accepted` | missing_exact_anchors | docker build -f docker/web.Dockerfile -t web:ci ., RUN npm ci, ERESOLVE, react-dates@21.8.0, react@18.2.0, exit code: 1 | - |
| `docker-compose-01` | `summary` | `docker-compose` | `1355.92` | `0.673` | `0.333` | `0.897` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker compose up, could not be found | - |
| `docker-compose-02` | `recall` | `docker-compose` | `1426.13` | `0.532` | `0.250` | `0.855` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker compose up --build, tenant_settings, sqlalchemy.exc.ProgrammingError | - |
| `docker-compose-03` | `summary` | `docker-compose` | `4700.49` | `0.735` | `0.600` | `0.911` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker compose up api | - |
| `kubectl-01` | `summary` | `kubectl` | `3283.62` | `0.740` | `0.647` | `0.907` | `1.000` | `0.991` | `0.971` | `soft_accepted` | missing_exact_anchors | kubectl apply -f k8s/deployment.yaml --server-side | - |
| `kubectl-02` | `recall` | `kubectl` | `3758.35` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `1954.84` | `0.990` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `6934.75` | `0.924` | `1.000` | `0.919` | `1.000` | `0.832` | `0.441` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `2350.64` | `0.648` | `0.118` | `0.958` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform validate, main.tf line 23, resource "aws_vpc" "main", Unsupported argument | - |
| `terraform-02` | `recall` | `terraform` | `2598.82` | `0.560` | `0.316` | `0.905` | `1.000` | `0.970` | `0.900` | `soft_accepted` | missing_exact_anchors | terraform plan, outputs.tf line 14, Reference to undeclared resource | - |
| `terraform-03` | `recall` | `terraform` | `1997.94` | `0.984` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `4464.37` | `0.616` | `0.098` | `0.945` | `1.000` | `0.945` | `0.818` | `soft_accepted` | missing_exact_anchors | terraform test, run "plan_defaults", tests/aws.tftest.hcl line 18, Test assertion failed, expected t3.small default | - |
| `mixed-01` | `recall` | `mixed` | `4320.85` | `0.931` | `1.000` | `0.892` | `1.000` | `0.874` | `0.581` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `3511.50` | `0.652` | `0.270` | `0.873` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | make integration, psql, Error 2, integration | - |
| `git-01` | `recall` | `git` | `13652.14` | `0.695` | `1.000` | `0.892` | `0.500` | `0.417` | `0.444` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `git-02` | `recall` | `git` | `1295.57` | `0.713` | `0.704` | `0.888` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | main -> main, non-fast-forward | - |
| `git-03` | `recall` | `git` | `2194.47` | `0.480` | `0.125` | `0.834` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | git clone --progress https://github.com/example/very-large-repo.git, curl 56, Connection reset by peer | - |
| `curl-01` | `recall` | `curl` | `1238.09` | `0.503` | `0.200` | `0.806` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | curl -fL --retry 3 --retry-all-errors -o dist/tool-linux-amd64.tar.gz https://downloads.example.com/tool/releases/v1.8.4/tool-linux-amd64.tar.gz, curl: (22), dist/tool-linux-amd64.tar.gz | - |
| `curl-02` | `summary` | `curl` | `6147.62` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | curl -I https://docs.example.com/sdk/latest, HTTP/2 301, location: /sdk/v3.4/, cache-control: max-age=3600 | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='```plaintext HTTP/2 301 date: Sat, 16 May 2026 07:14:19 GMT content-type: text/html; charset=UTF-8 content-length: 167 location: /sdk/v3.4/ cache-control: ma...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='curl -I https://docs.example.com/sdk/latest HTTP/2 301 date: Sat, 16 May 2026 07:14:19 GMT content-type: text/html; charset=UTF-8 content-length: 167 locatio...' |
| `ssh-01` | `summary` | `ssh` | `3422.29` | `0.731` | `0.762` | `0.900` | `1.000` | `0.920` | `0.732` | `soft_accepted` | missing_exact_anchors | fatal: Could not read from remote repository. | - |
| `ssh-02` | `summary` | `ssh` | `4551.63` | `0.632` | `0.121` | `0.909` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ssh deploy@staging.example.net, /home/dev/.ssh/known_hosts:42, Host key verification failed. | - |
| `systemd-01` | `summary` | `systemd` | `1590.87` | `0.742` | `0.548` | `0.964` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | queue-worker.service, status=203/EXEC | - |
| `systemd-02` | `summary` | `systemd` | `4239.56` | `0.787` | `0.857` | `0.904` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | api.service | - |
| `apt-01` | `summary` | `apt` | `1075.45` | `0.966` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `4241.78` | `0.967` | `1.000` | `0.916` | `1.000` | `0.965` | `0.885` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `3919.12` | `0.766` | `0.750` | `0.909` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | example.com/mono-app/pkg/server | - |
| `go-test-01` | `summary` | `go-test` | `2801.70` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `3375.36` | `0.966` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `3182.73` | `0.718` | `0.522` | `0.911` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mvn -q test, maven-surefire-plugin:3.5.5:test | - |
| `maven-02` | `summary` | `maven` | `3782.53` | `0.647` | `0.303` | `0.840` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mvn -U -DskipTests package, Failed to execute goal on project ingest-service, Could not resolve dependencies | - |
| `gradle-01` | `recall` | `gradle` | `6814.36` | `0.902` | `1.000` | `0.878` | `1.000` | `0.797` | `0.324` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `827.06` | `0.970` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `10439.54` | `0.882` | `1.000` | `0.899` | `1.000` | `0.845` | `0.485` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `1609.68` | `0.793` | `0.833` | `0.937` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | guessing_game v0.1.0 | - |
| `node-runtime-01` | `recall` | `node-runtime` | `16308.22` | `0.593` | `0.789` | `0.896` | `0.500` | `0.377` | `0.180` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | MODULE_NOT_FOUND | - |
| `npm-04` | `summary` | `npm` | `9062.68` | `0.855` | `1.000` | `0.916` | `1.000` | `0.778` | `0.260` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `3256.42` | `0.958` | `1.000` | `0.934` | `1.000` | `0.969` | `0.897` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `3685.50` | `0.715` | `0.500` | `0.914` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | react-hooks/exhaustive-deps, ESLint found too many warnings | - |
| `python-runtime-01` | `summary` | `python-runtime` | `11625.14` | `0.685` | `1.000` | `0.942` | `0.500` | `0.429` | `0.526` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `pytest-06` | `summary` | `pytest` | `1621.79` | `0.982` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `3398.52` | `0.950` | `1.000` | `0.896` | `1.000` | `0.984` | `0.946` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `5691.61` | `0.680` | `0.378` | `0.889` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund, zod@3.23.8 | - |
| `docker-compose-04` | `summary` | `docker-compose` | `1754.01` | `0.606` | `0.000` | `0.907` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker compose up --build, mono-api-1, 0.0.0.0:8080, port is already allocated | - |
| `kubectl-05` | `summary` | `kubectl` | `1927.29` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `8518.52` | `0.668` | `0.706` | `0.863` | `1.000` | `0.828` | `0.426` | `soft_accepted` | missing_exact_anchors | Exit Code:    1 | - |
| `kubectl-07` | `recall` | `kubectl` | `1796.17` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `11721.23` | `0.548` | `0.424` | `0.862` | `1.000` | `0.814` | `0.379` | `soft_accepted` | missing_exact_anchors | terraform plan -lock-timeout=5s -out=tfplan, Error acquiring the state lock | - |
| `terraform-06` | `summary` | `terraform` | `4821.82` | `0.642` | `0.133` | `0.928` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform validate, main.tf line 27, aws_vpc.core.id | - |
| `terraform-07` | `summary` | `terraform` | `4047.64` | `0.593` | `0.133` | `0.868` | `1.000` | `0.935` | `0.784` | `soft_accepted` | missing_exact_anchors | terraform plan -detailed-exitcode -no-color, Plan: 1 to add, 1 to change, 0 to destroy., aws_security_group_rule.web_https | - |
| `nginx-01` | `summary` | `nginx` | `1421.12` | `0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `3199.92` | `0.966` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `1807.34` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `5805.78` | `0.783` | `0.882` | `0.909` | `1.000` | `0.974` | `0.914` | `soft_accepted` | missing_exact_anchors | relation "users" already exists | - |
| `mysql-01` | `summary` | `mysql` | `1555.22` | `0.650` | `0.267` | `0.869` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mysql -h db.example.net -u reporting -p reporting_db, ERROR 1045 (28000) | - |
| `mysql-02` | `summary` | `mysql` | `2103.28` | `0.610` | `0.111` | `0.851` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mysql -h db.example.net -u app -D appdb -e "SELECT id, createdAt FROM users LIMIT 5", ERROR 1054 (42S22), line 1 | - |
| `redis-01` | `summary` | `redis` | `7095.06` | `0.942` | `1.000` | `0.922` | `1.000` | `0.946` | `0.821` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `1815.63` | `0.993` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `2741.60` | `0.567` | `0.333` | `0.866` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ruff check ., line=91, Ruff F821 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `18205.34` | `0.853` | `1.000` | `0.911` | `1.000` | `0.777` | `0.255` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `731.38` | `0.963` | `1.000` | `0.907` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `6393.86` | `0.971` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `4671.56` | `0.879` | `1.000` | `0.897` | `1.000` | `0.841` | `0.469` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `2917.95` | `0.958` | `1.000` | `0.959` | `1.000` | `0.903` | `0.677` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `4050.99` | `0.644` | `0.167` | `0.915` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | rsync -av --delete build/ artifact-store/build/, code 24, some files vanished before they could be transferred | - |
| `test-failure-01` | `recall` | `test-failure` | `5600.09` | `0.481` | `0.091` | `0.902` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/unit/test_invoice_totals.py::test_discount_rounding, tests/unit/test_invoice_totals.py:88, Decimal('17.50'), Decimal('17.49') | - |
| `compiler-error-01` | `recall` | `compiler-error` | `17036.75` | `0.575` | `0.701` | `0.875` | `0.500` | `0.413` | `0.423` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | src/router.rs:128, req.clone().into_body() | - |
| `ci-log-01` | `recall` | `ci-log` | `8692.81` | `0.963` | `1.000` | `0.928` | `1.000` | `0.944` | `0.815` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `8043.40` | `0.606` | `0.481` | `0.924` | `1.000` | `0.896` | `0.654` | `soft_accepted` | missing_exact_anchors | npm ERR! code ERESOLVE, peer vite@"^4.0.0 || ^5.0.0", --force or --legacy-peer-deps | - |
| `test-summary-01` | `summary` | `test-summary` | `6251.81` | `0.741` | `0.643` | `0.903` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | checkout_test.go:71, worker.go:144 | - |
| `build-log-01` | `summary` | `build-log` | `5492.89` | `0.687` | `0.438` | `0.873` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | cannot find symbol, setTaxCode(java.lang.String), InvoiceDto | - |
| `docker-build-02` | `summary` | `docker-build` | `13029.37` | `0.637` | `1.000` | `0.875` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `8503.59` | `0.466` | `1.000` | `0.682` | `0.000` | `0.000` | `0.615` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `5717.57` | `0.512` | `1.000` | `0.706` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `2186.02` | `0.538` | `1.000` | `0.792` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-01` | `structured` | `structured-output` | `5203.16` | `0.511` | `1.000` | `0.823` | `0.000` | `0.000` | `0.644` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `4501.24` | `0.334` | `0.429` | `0.737` | `0.000` | `0.000` | `0.862` | `soft_accepted` | missing_exact_anchors | test / integration, port 5432 is already allocated, deploy / preview | - |
| `structured-output-03` | `structured` | `structured-output` | `6031.77` | `0.340` | `0.750` | `0.500` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "invalid refresh token", Received: 0 | - |
| `structured-output-04` | `structured` | `structured-output` | `2702.80` | `0.369` | `1.000` | `0.229` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `1497.07` | `0.234` | `1.000` | `0.337` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `2245.70` | `0.222` | `1.000` | `0.475` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `2193.05` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `8177.02` | `0.593` | `0.000` | `0.848` | `1.000` | `0.919` | `0.730` | `soft_accepted` | missing_exact_anchors | /repo/tools/json.py, has no attribute 'dumps', shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `4480.30` | `0.758` | `0.750` | `0.884` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `3538.71` | `0.736` | `1.000` | `0.871` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `1579.90` | `0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `4982.95` | `0.978` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `5523.39` | `0.524` | `0.190` | `0.924` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | module.worker.aws_iam_policy.worker_inline, status code: 409, request id: 0f3e2b11-9ac9-4fd2-a3bb-6c07a3c6a90d, modules/worker/iam.tf line 27 | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `2186.43` | `0.981` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `5872.81` | `0.957` | `1.000` | `0.914` | `1.000` | `0.935` | `0.783` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `6067.21` | `0.616` | `0.444` | `0.919` | `1.000` | `0.983` | `0.944` | `soft_accepted` | missing_exact_anchors | WARNING: DATA RACE, (*Store).Set(), (*Store).Get() | - |
| `cargo-03` | `recall` | `cargo` | `4822.59` | `0.725` | `0.718` | `0.921` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | error[E0432], could not compile `storage` | - |
| `docker-compose-05` | `recall` | `docker-compose` | `6895.65` | `0.953` | `1.000` | `0.937` | `1.000` | `0.907` | `0.691` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `6139.70` | `0.767` | `0.821` | `0.940` | `1.000` | `0.992` | `0.974` | `soft_accepted` | missing_exact_anchors | packages/api/src/index.ts:4:25 | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `3876.89` | `0.981` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `6202.36` | `0.652` | `0.579` | `0.924` | `1.000` | `0.928` | `0.761` | `soft_accepted` | missing_exact_anchors | ERR_PNPM_OUTDATED_LOCKFILE, --frozen-lockfile, fastify | - |
| `swift-01` | `recall` | `swift` | `4070.88` | `0.570` | `0.326` | `0.895` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | UserDecoderTests testMissingAvatarUsesPlaceholder, Tests/UserDecoderTests.swift:47, XCTAssertEqual failed, fatalError | - |
| `elixir-01` | `recall` | `elixir` | `4170.42` | `0.672` | `0.565` | `0.947` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | lib/my_app/cache_worker.ex:63, test/my_app/cache_worker_test.exs:29 | - |
| `rails-01` | `recall` | `rails` | `4791.46` | `0.943` | `1.000` | `0.915` | `1.000` | `0.894` | `0.646` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `11024.98` | `0.527` | `0.362` | `0.896` | `1.000` | `0.800` | `0.333` | `soft_accepted` | missing_exact_anchors | Tests\Billing\InvoiceTotalTest::testAppliesCreditBeforeTax, Failures: 1, Deprecations: 2 | - |
| `nginx-03` | `recall` | `nginx` | `4699.04` | `0.538` | `0.250` | `0.884` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | nginx -t -c /etc/nginx/nginx.conf, /etc/nginx/conf.d/api.conf:22, configuration file /etc/nginx/nginx.conf test failed | - |
| `postgres-03` | `recall` | `postgres` | `4041.23` | `0.446` | `0.000` | `0.926` | `1.000` | `0.978` | `0.927` | `soft_accepted` | missing_exact_anchors | psql:dump.sql:418, type "vector" does not exist, embedding vector(1536), current transaction is aborted, ROLLBACK | - |
| `ansible-02` | `recall` | `ansible` | `5598.64` | `0.979` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `2799.98` | `0.592` | `0.375` | `0.910` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | //services/reporting:report_parser_test, services/reporting/parser.py", line 141, etree.fromstring(xml_bytes) | - |
| `powershell-01` | `recall` | `powershell` | `2073.36` | `0.497` | `0.125` | `0.915` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | .\scripts\release.ps1 -Version 1.4.2, PSSecurityException, FullyQualifiedErrorId : UnauthorizedAccess | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `4722.34` | `0.679` | `0.588` | `0.936` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | http status: 401, exit code 1 | - |
| `python-pytest-01` | `summary` | `python-pytest` | `3269.71` | `0.964` | `1.000` | `0.911` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `5759.18` | `0.961` | `1.000` | `0.903` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `1075.07` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | web@1.2.0, src/pages/admin.tsx, TS2339, Property, roleName | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary return a concise plain-text recall summary' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary return a concise plain-text recall summary' |
| `helm-01` | `summary` | `helm` | `3930.83` | `0.624` | `0.125` | `0.882` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | template, api/templates/deployment.yaml:42:29, executing, api/templates/deployment.yaml | - |
| `ruff-04` | `summary` | `ruff` | `8778.03` | `0.620` | `0.211` | `0.818` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | app/api/routes.py:3:1, app/services/user.py:88:89, tests/test_user.py:12:1 | - |
| `k6-01` | `summary` | `k6` | `6064.99` | `0.685` | `0.478` | `0.862` | `1.000` | `0.983` | `0.942` | `soft_accepted` | missing_exact_anchors | checks, http_req_duration, avg | - |
| `composer-01` | `summary` | `composer` | `2443.86` | `0.749` | `0.800` | `0.827` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Loading | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `3192.62` | `0.952` | `1.000` | `0.880` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `4209.52` | `0.707` | `0.545` | `0.880` | `1.000` | `0.986` | `0.953` | `soft_accepted` | missing_exact_anchors | build/server.o, src/server.c:14:10 | - |
| `python-pytest-02` | `summary` | `python-pytest` | `4530.55` | `0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `4626.45` | `0.961` | `1.000` | `0.902` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `2486.16` | `0.790` | `0.833` | `0.929` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `2225.23` | `0.960` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `3221.46` | `0.637` | `0.200` | `0.872` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | deploy, Total, Upload, 183.22 | - |
| `python-pytest-04` | `summary` | `python-pytest` | `2060.17` | `0.962` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `5699.33` | `0.335` | `0.630` | `0.671` | `0.000` | `0.000` | `0.667` | `soft_accepted` | missing_exact_anchors | 22:7, 4:12 | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `2705.04` | `0.667` | `0.412` | `0.676` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | infra/terraform/iam.tf, iam:PassRole | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `2801.80` | `0.404` | `1.000` | `0.659` | `0.000` | `0.000` | `0.067` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `5506.37` | `0.355` | `0.800` | `0.692` | `0.000` | `0.000` | `0.500` | `soft_accepted` | missing_exact_anchors | node=22, node=20 | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `3388.21` | `0.362` | `0.577` | `0.730` | `0.000` | `0.000` | `0.917` | `soft_accepted` | missing_exact_anchors | Warning Failed, secret "api-env" not found | - |
| `npm-06` | `instruction_following` | `npm` | `4061.76` | `0.330` | `0.455` | `0.733` | `0.000` | `0.000` | `0.769` | `soft_accepted` | missing_exact_anchors | npm ERR! code ENOTEMPTY, npm ERR! syscall rename | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `1302.17` | `0.543` | `1.000` | `0.811` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `894.80` | `0.713` | `1.000` | `0.710` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `8684.80` | `0.314` | `0.375` | `0.757` | `0.000` | `0.000` | `0.677` | `soft_accepted` | missing_exact_anchors | UserService.java:[44,17], UserController.java:[28,31] | - |
| `playwright-01` | `instruction_following` | `playwright` | `2668.11` | `0.390` | `0.818` | `0.651` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Payment complete | - |
| `prettier-01` | `instruction_following` | `prettier` | `321.08` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `3030.04` | `0.421` | `1.000` | `0.706` | `0.000` | `0.000` | `0.095` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `4625.21` | `0.352` | `0.500` | `0.787` | `0.000` | `0.000` | `0.778` | `soft_accepted` | missing_exact_anchors | src/auth.rs:88, left: 1750, right: 1749 | - |
| `shell-01` | `instruction_following` | `shell` | `1121.29` | `0.537` | `1.000` | `0.789` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `4201.82` | `0.482` | `1.000` | `0.736` | `0.000` | `0.000` | `0.615` | `accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `6588.17` | `0.473` | `1.000` | `0.676` | `0.000` | `0.000` | `0.700` | `accepted` | - | - | - |
| `junit-01` | `structured` | `junit` | `1922.98` | `0.914` | `1.000` | `0.714` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `8127.60` | `0.284` | `0.857` | `0.461` | `0.000` | `0.000` | `0.250` | `soft_accepted` | missing_exact_anchors | unhealthy_pods | - |
| `eslint-06` | `structured` | `eslint` | `4330.49` | `0.303` | `1.000` | `0.276` | `0.000` | `0.000` | `0.200` | `accepted` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `1332.88` | `0.448` | `0.852` | `0.634` | `0.000` | `0.000` | `0.875` | `accepted` | - | build | - |
| `go-test-04` | `structured` | `go-test` | `2346.27` | `0.579` | `1.000` | `0.958` | `0.000` | `0.000` | `0.917` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `1986.12` | `0.822` | `1.000` | `0.633` | `1.000` | `0.795` | `0.316` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `2383.00` | `0.258` | `0.667` | `0.233` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | legacy-widget@2.4.0, required | - |
| `mypy-06` | `structured` | `mypy` | `5580.14` | `0.389` | `0.867` | `0.661` | `0.000` | `0.000` | `0.857` | `soft_accepted` | missing_exact_anchors | Message | - |
| `gradle-03` | `structured` | `gradle` | `977.65` | `0.413` | `1.000` | `0.378` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `playwright-02` | `structured` | `playwright` | `1407.25` | `0.401` | `1.000` | `0.338` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `4056.62` | `0.426` | `1.000` | `0.562` | `0.000` | `0.000` | `0.577` | `accepted` | - | - | - |
| `vite-01` | `structured` | `vite` | `2909.59` | `0.278` | `1.000` | `0.226` | `0.000` | `0.000` | `0.100` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `2558.81` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | tests/test_a.py::test_one, tests/test_b.py::TestB::test_three | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='```python tests/test_a.py::test_one - AssertionError PASSED tests/test_a.py::test_two FAILED tests/test_b.py::TestB::test_three - TimeoutError ```<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='```python tests/test_a.py::test_one - AssertionError PASSED tests/test_a.py::test_two FAILED tests/test_b.py::TestB::test_three - TimeoutError ```<|im_end|>' |
| `git-04` | `exact_format` | `git` | `2916.73` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='9f4c2d7a1b8e3c6d0a1234567890abcdef123456<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass="Merge made by the 'ort' strategy. commit 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 Author: CI Bot Status: deployed to staging<|im_end|>" |
| `docker-04` | `exact_format` | `docker` | `3319.42` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='```plaintext sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 ```<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='```plaintext ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 ```<|im_end|>' |
| `npm-08` | `exact_format` | `npm` | `451.41` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 2.18.4 | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='2.18.4<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='2.18.4<|im_end|>' |
| `go-test-05` | `exact_format` | `go-test` | `1099.80` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | github.com/acme/shop/checkout, TestCheckoutAppliesCoupon | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='```go got 120 want 100 ```<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='```go github.com/acme/shop/checkout TestCheckoutAppliesCoupon ```<|im_end|>' |
| `kubectl-09` | `exact_format` | `kubectl` | `1065.32` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | migrator-v2-9xk, prod | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='```plaintext migrator-v2-9xk prod ```<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='```plaintext migrator-v2-9xk prod ```<|im_end|>' |
| `cargo-05` | `exact_format` | `cargo` | `2450.15` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | auth::tests::rejects_expired, billing::tests::rounds_half_even | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='```plaintext - failures: - auth::tests::rejects_expired - billing::tests::rounds_half_even - test result: FAILED. 40 passed; 2 failed ```<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='failures: auth::tests::rejects_expired billing::tests::rounds_half_even test result: FAILED. 40 passed; 2 failed<|im_end|>' |
| `curl-03` | `exact_format` | `curl` | `268.14` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 503 | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='503<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='503<|im_end|>' |
| `rails-02` | `exact_format` | `rails` | `2501.60` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 20260518133742 | qwen2.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='PG::DuplicateColumn: ERROR: column "tenant_id" of relation "users" already exists<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='== 20260518133742 AddTenantIdToUsers: migrating ===================== -- add_column(:users, :tenant_id, :uuid) rails aborted! PG::DuplicateColumn: ERROR: col...' |
| `python-traceback-02` | `explanation` | `python-traceback` | `7230.67` | `0.731` | `1.000` | `0.920` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `6744.51` | `0.892` | `1.000` | `0.852` | `1.000` | `0.897` | `0.657` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `5695.88` | `0.739` | `1.000` | `0.878` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `1515.55` | `0.963` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `1995.11` | `0.949` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `3495.68` | `0.633` | `0.250` | `0.790` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | E0515, returns a reference | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `2425.05` | `0.643` | `0.167` | `0.846` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | contents: read, contents: write | - |
| `runtime-01` | `recall` | `runtime` | `1562.06` | `0.984` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `1814.12` | `0.953` | `1.000` | `0.945` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `2763.14` | `0.747` | `1.000` | `0.914` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `package-management-01` | `recall` | `package-management` | `1884.73` | `0.968` | `1.000` | `0.873` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `1692.97` | `0.715` | `0.667` | `0.965` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `5017.72` | `0.952` | `1.000` | `0.940` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `3690.47` | `0.905` | `1.000` | `0.872` | `1.000` | `0.812` | `0.375` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `1139.38` | `0.967` | `1.000` | `0.868` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `2252.69` | `0.523` | `0.364` | `0.873` | `1.000` | `0.800` | `0.333` | `soft_accepted` | missing_exact_anchors | COPY failed | - |
| `deployment-01` | `recall` | `deployment` | `1866.40` | `0.480` | `0.222` | `0.864` | `1.000` | `0.845` | `0.484` | `soft_accepted` | missing_exact_anchors | cannot be handled as a Pod, Name: name not present | - |
| `infrastructure-01` | `recall` | `infrastructure` | `1761.37` | `0.948` | `1.000` | `0.909` | `1.000` | `0.912` | `0.706` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `1407.56` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `861.96` | `0.975` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `953.53` | `0.607` | `0.412` | `0.918` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Execution failed for task ':test' | - |
| `container-runtime-01` | `recall` | `container-runtime` | `441.82` | `0.979` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `2103.97` | `0.428` | `0.000` | `0.872` | `1.000` | `0.957` | `0.857` | `soft_accepted` | missing_exact_anchors | package com.google.common does not exist, 1 error | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1057.69` | `0.967` | `1.000` | `0.868` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `271.75` | `0.991` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `1588.60` | `0.975` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `2946.47` | `0.400` | `0.000` | `0.908` | `1.000` | `0.830` | `0.433` | `soft_accepted` | missing_exact_anchors | COPY failed, no such file or directory | - |
| `testing-04` | `recall` | `testing` | `1943.80` | `0.512` | `0.167` | `0.910` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Failure/Error, capybara-3.34.0/lib/capybara/node/element.rb:1008 | - |
| `build-02` | `recall` | `build` | `2749.36` | `0.896` | `1.000` | `0.847` | `1.000` | `0.803` | `0.344` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `1161.38` | `0.432` | `0.000` | `0.833` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERROR: failed to fetch, 404  Not Found, libssl1.0.0_1.0.2g-1ubuntu4.0_amd64.deb | - |
| `testing-05` | `recall` | `testing` | `315.01` | `0.974` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `1404.09` | `0.581` | `0.286` | `0.831` | `1.000` | `0.859` | `0.529` | `soft_accepted` | missing_exact_anchors | FAILURE: Build failed with an exception | - |
| `docker-05` | `summary` | `docker` | `1000.01` | `0.903` | `1.000` | `0.850` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `549.19` | `0.961` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `974.81` | `0.779` | `0.810` | `0.909` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 5 passed | - |
| `npm-09` | `summary` | `npm` | `1157.35` | `0.854` | `1.000` | `0.908` | `1.000` | `0.782` | `0.273` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `1435.57` | `0.523` | `0.000` | `0.836` | `1.000` | `0.862` | `0.538` | `soft_accepted` | missing_exact_anchors | Finished dev | - |
| `linting-01` | `instruction_following` | `linting` | `1594.59` | `0.552` | `1.000` | `0.840` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `4623.19` | `0.424` | `0.500` | `0.758` | `0.400` | `0.293` | `0.111` | `soft_accepted` | missing_exact_anchors | * rerun pytest test_auth.py::TestAuth::test_login | - |
| `ci-05` | `instruction_following` | `ci` | `527.90` | `0.688` | `1.000` | `0.628` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `linting-02` | `structured` | `linting` | `1194.75` | `0.503` | `1.000` | `0.678` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `1862.39` | `0.550` | `1.000` | `0.900` | `0.000` | `0.000` | `0.800` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `641.84` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `1140.04` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `285.71` | `0.250` | `1.000` | `0.754` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `757.25` | `0.125` | `0.000` | `0.975` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | OUTPUT: | - |
| `shell-04` | `exact_format` | `shell` | `260.71` | `0.199` | `1.000` | `0.322` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `3955.60` | `0.119` | `0.286` | `0.474` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Resources: 1 added | - |
| `build-05` | `exact_format` | `build` | `131.14` | `0.233` | `1.000` | `0.333` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `599.96` | `0.582` | `1.000` | `0.657` | `0.500` | `0.400` | `0.333` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `1034.87` | `0.935` | `1.000` | `0.870` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `1227.52` | `0.931` | `1.000` | `0.862` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `1438.43` | `0.964` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `736.09` | `0.959` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `583.56` | `0.967` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `699.14` | `0.931` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `1290.01` | `0.955` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `554.69` | `0.939` | `1.000` | `0.878` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `776.69` | `0.944` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `921.34` | `0.653` | `0.000` | `0.936` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | no configured push destination | - |
| `explanation-04` | `explanation` | `explanation` | `935.55` | `0.631` | `0.000` | `0.886` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | exited with 1 | - |
| `explanation-05` | `explanation` | `explanation` | `853.17` | `0.652` | `0.000` | `0.933` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | command not found | - |
| `explanation-06` | `explanation` | `explanation` | `1226.37` | `0.907` | `1.000` | `0.814` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `1239.02` | `0.954` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `718.02` | `0.920` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `1189.59` | `0.645` | `0.000` | `0.918` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | would be overwritten by merge | - |
| `explanation-10` | `explanation` | `explanation` | `1259.28` | `0.614` | `0.000` | `0.876` | `1.000` | `0.954` | `0.846` | `soft_accepted` | missing_exact_anchors | KeyError: 'API_KEY' | - |
| `explanation-11` | `explanation` | `explanation` | `900.30` | `0.932` | `1.000` | `0.864` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `763.73` | `0.933` | `1.000` | `0.865` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `1840.74` | `0.550` | `1.000` | `0.900` | `0.000` | `0.000` | `0.800` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `652.81` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `1149.85` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `264.92` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `1096.85` | `0.700` | `1.000` | `0.335` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `3899.87` | `0.119` | `0.286` | `0.474` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Resources: 1 added | - |
| `runtime-07` | `exact_format` | `runtime` | `406.10` | `0.198` | `1.000` | `0.314` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `2801.90` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `264.43` | `0.220` | `1.000` | `0.578` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `1007.98` | `0.935` | `1.000` | `0.870` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `1214.58` | `0.931` | `1.000` | `0.862` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `838.71` | `0.958` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `1390.68` | `0.625` | `0.000` | `0.935` | `1.000` | `0.905` | `0.684` | `soft_accepted` | missing_exact_anchors | cannot list resource "pods" | - |
| `explanation-14` | `explanation` | `explanation` | `1382.33` | `0.955` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `584.71` | `0.963` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `958.26` | `0.649` | `0.000` | `0.928` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | undefined: fmt.Println | - |
| `explanation-17` | `explanation` | `explanation` | `1487.15` | `0.894` | `1.000` | `0.883` | `1.000` | `0.858` | `0.526` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1167.91` | `0.707` | `0.444` | `0.901` | `1.000` | `0.977` | `0.923` | `soft_accepted` | missing_exact_anchors | nonexistent (invalid) version of flask | - |
