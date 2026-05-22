# remote-gpt-5-mini

## Scenario

- track: `remote`
- phase: `remote-screen`
- model: `gpt-5-mini`
- quantization: `none`
- device: `remote`
- dtype: `remote`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `5840.63`
- cpu_rss_bytes: `1937350656`
- gpu_peak_bytes: `1217674240`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `148`
- accepted_count: `146`
- soft_accepted_count: `2`
- rejected_count: `132`
- exact_pass_count: `148`
- avg_inference_ms: `6560.27`
- p95_inference_ms: `13069.84`
- avg_exact_preservation_ratio: `0.529`
- avg_summary_quality_ratio: `0.451`
- avg_format_adherence_score: `0.451`
- avg_instruction_following_score: `0.444`
- avg_brevity_ratio: `0.965`
- avg_case_score: `0.462`
- p10_case_score: `0.000`
- quality_core: `0.369`
- latency_factor: `0.850`
- final_score: `31.40`
- peak_cpu_rss_bytes: `1937391616`
- peak_gpu_bytes: `1217674240`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `6540.96` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | python -m app.cli sync --config config/settings.json, /workspace/app/config.py, line 27, JSONDecodeError, line 18 column 3, config/settings.json | LiteLLM backend returned empty output. |
| `python-02` | `summary` | `python` | `6366.32` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | LiteLLM backend returned empty output. |
| `python-03` | `recall` | `python` | `8436.77` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `9245.20` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | python -m jobs.refresh_catalog --region us-east-1, /workspace/src/jobs/refresh_catalog.py, line 119, httpx.ReadTimeout, catalog?page=2, us-east-1 | LiteLLM backend returned empty output. |
| `python-05` | `recall` | `python` | `8527.34` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | python tools/export_report.py --input data/may.csv --format parquet, /workspace/src/reports/export.py, line 131, UnboundLocalError, writer, data/may.csv | LiteLLM backend returned empty output. |
| `pytest-01` | `recall` | `pytest` | `5660.74` | `0.995` | `1.000` | `0.981` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `7470.63` | `0.987` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `7230.16` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | pytest tests -q -x, tests/jobs/test_retention.py::test_archive_marks_job_deleted, teardown, psycopg.errors.ForeignKeyViolation, job_runs_job_id_fkey, 149 passed, 1 skipped, 1 error in 58.73s | LiteLLM backend returned empty output. |
| `pytest-04` | `recall` | `pytest` | `5511.85` | `0.996` | `1.000` | `0.983` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `6484.76` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | pytest tests/unit tests/integration --disable-warnings=0, tests/unit/test_stripe_client.py, src/billing/client.py:9, ModuleNotFoundError, stripe, 1 error during collection | LiteLLM backend returned empty output. |
| `mypy-01` | `recall` | `mypy` | `5508.58` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `6716.24` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | mypy src tests --pretty --show-error-codes, src/payments/retry.py:118, arg-type, RetryEvent, append, checked 37 source files | LiteLLM backend returned empty output. |
| `mypy-03` | `recall` | `mypy` | `6171.09` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | mypy src/orders/normalize.py --show-error-codes --strict, src/orders/normalize.py:41, union-attr, currency, Order | None, type: ignore | LiteLLM backend returned empty output. |
| `ruff-01` | `summary` | `ruff` | `6826.43` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ruff check src --output-format=full, src/payments/init.py:1:20, F401, Client, all, Found 1 error. | LiteLLM backend returned empty output. |
| `ruff-02` | `summary` | `ruff` | `6489.24` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ruff format --check src tests, src/api/serializers.py, 1 file would be reformatted, 52 files already formatted | LiteLLM backend returned empty output. |
| `ruff-03` | `summary` | `ruff` | `6788.95` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ruff check src/auth/login.py, src/auth/login.py:93:13, B904, except, Found 1 error. | LiteLLM backend returned empty output. |
| `pylint-01` | `recall` | `pylint` | `9135.41` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | pylint src/storage/path_utils.py, src/storage/path_utils.py:27:18, E1101, no-member, mothers, Path | LiteLLM backend returned empty output. |
| `pylint-02` | `recall` | `pylint` | `8849.40` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | pylint src/config/runtime.py src/api/server.py, src/config/runtime.py:44:0, F0010, parse-error, expected ":", src/api/server.py | LiteLLM backend returned empty output. |
| `pylint-03` | `summary` | `pylint` | `5023.02` | `0.997` | `1.000` | `0.992` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `6936.18` | `0.992` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `6804.32` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | black src, /workspace/src/config/schema.py, Cannot parse, 58:12, 1 file failed to reformat, 1 file reformatted | LiteLLM backend returned empty output. |
| `black-03` | `recall` | `black` | `4645.12` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `7438.06` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | npm ci, EUSAGE, react@18.3.1, scheduler@0.23.2, package-lock.json, /home/dev/.npm/_logs/2026-05-15T09_20_11_449Z-debug-0.log | LiteLLM backend returned empty output. |
| `npm-02` | `summary` | `npm` | `6572.79` | `0.992` | `1.000` | `0.981` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `7327.89` | `0.990` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `8105.80` | `0.941` | `1.000` | `0.937` | `1.000` | `0.871` | `0.571` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `7490.26` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | pnpm add @tanstack/react-query-devtools@5.52.0 -F packages/admin, ERR_PNPM_NO_MATCHING_VERSION, @tanstack/react-query-devtools@5.52.0, packages/admin, 5.51.1 | LiteLLM backend returned empty output. |
| `pnpm-03` | `summary` | `pnpm` | `6634.46` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `4390.41` | `0.983` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `5753.65` | `0.995` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `6415.16` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | tsc src/index.ts src/http.ts --pretty false, src/index.ts(48,20), TS2769, URL, RequestInit, src/http.ts(9,17) | LiteLLM backend returned empty output. |
| `eslint-01` | `recall` | `eslint` | `7301.09` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | eslint src --format stylish, /workspace/src/logger.js, no-console, Unused eslint-disable directive, /workspace/src/server.js, 3 problems (2 errors, 1 warning) | LiteLLM backend returned empty output. |
| `eslint-02` | `summary` | `eslint` | `6891.10` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `7370.99` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | eslint src --max-warnings=0, /workspace/src/hooks/useCart.ts, react-hooks/exhaustive-deps, 1 problem (0 errors, 1 warning), maximum: 0 | LiteLLM backend returned empty output. |
| `docker-01` | `recall` | `docker` | `6169.66` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | docker build -t api:dev ., COPY docker/entrypoint.sh /entrypoint.sh, /docker/entrypoint.sh, Dockerfile:14, failed to solve | LiteLLM backend returned empty output. |
| `docker-02` | `summary` | `docker` | `4195.81` | `0.987` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `6083.90` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | docker build -f docker/web.Dockerfile -t web:ci ., RUN npm ci, ERESOLVE, react-dates@21.8.0, react@18.2.0, exit code: 1 | LiteLLM backend returned empty output. |
| `docker-compose-01` | `summary` | `docker-compose` | `4381.53` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `7840.38` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | docker compose up --build, demo-app-1, tenant_settings, sqlalchemy.exc.ProgrammingError, app-1 exited with code 1 | LiteLLM backend returned empty output. |
| `docker-compose-03` | `summary` | `docker-compose` | `6489.24` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | docker compose up api, preview-api-1, 0.0.0.0:8080, port is already allocated | LiteLLM backend returned empty output. |
| `kubectl-01` | `summary` | `kubectl` | `6875.41` | `0.990` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `6545.28` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | kubectl describe pod api-7d9f7bbd8c-rx2kq -n staging, api-7d9f7bbd8c-rx2kq, ghcr.io/acme/api:2026.05.15-3, ImagePullBackOff, ErrImagePull | LiteLLM backend returned empty output. |
| `kubectl-03` | `summary` | `kubectl` | `7555.25` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | kubectl wait --for=condition=Available deployment/worker -n jobs --timeout=90s, deployment/worker, timed out waiting for the condition, deployments/worker | LiteLLM backend returned empty output. |
| `kubectl-04` | `recall` | `kubectl` | `6080.18` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | kubectl logs payments-worker-6f8f7d4df5-z5vsm -c worker --previous -n payments, payments-worker-6f8f7d4df5-z5vsm, /app/config.yaml, ValueError, invalid worker.concurrency, worker | LiteLLM backend returned empty output. |
| `terraform-01` | `summary` | `terraform` | `4615.85` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `6766.49` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | terraform plan, outputs.tf line 14, aws_security_group.db.id, Reference to undeclared resource, aws_security_group, db | LiteLLM backend returned empty output. |
| `terraform-03` | `recall` | `terraform` | `6780.09` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | terraform apply, Error acquiring the state lock, v1.7.5, v1.5.7, state snapshot | LiteLLM backend returned empty output. |
| `terraform-04` | `summary` | `terraform` | `7192.18` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | terraform test, run "plan_defaults", tests/aws.tftest.hcl line 18, Test assertion failed, aws_instance.web.instance_type, expected t3.small default | LiteLLM backend returned empty output. |
| `mixed-01` | `recall` | `mixed` | `7479.32` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | rsync -av --delete build/ backup/build/, /workspace/build/.cache/tmp-93f1.json, code 24, rsync warning, main.c(1338) | LiteLLM remote backend request failed: litellm.BadRequestError: OpenAIException - Could not finish the message because max_tokens or model output limit was reached. Please try again with higher max_tokens. LiteLLM Retried: 1 times |
| `mixed-02` | `summary` | `mixed` | `8159.04` | `0.982` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `7783.72` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | git rebase origin/main, src/api/client.py, a1c9f42, OrdersClient | LiteLLM backend returned empty output. |
| `git-02` | `recall` | `git` | `6729.05` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | git push origin main, main -> main, non-fast-forward, failed to push some refs | LiteLLM backend returned empty output. |
| `git-03` | `recall` | `git` | `7559.28` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | git clone --progress https://github.com/example/very-large-repo.git, curl 56, Connection reset by peer, invalid index-pack output | LiteLLM backend returned empty output. |
| `curl-01` | `recall` | `curl` | `7881.63` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | curl -fL --retry 3 --retry-all-errors -o dist/tool-linux-amd64.tar.gz https://downloads.example.com/tool/releases/v1.8.4/tool-linux-amd64.tar.gz, curl: (22), 404, dist/tool-linux-amd64.tar.gz | LiteLLM backend returned empty output. |
| `curl-02` | `summary` | `curl` | `6305.29` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | curl -I https://docs.example.com/sdk/latest, HTTP/2 301, location: /sdk/v3.4/, cache-control: max-age=3600 | LiteLLM backend returned empty output. |
| `ssh-01` | `summary` | `ssh` | `7234.22` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | GIT_SSH_COMMAND="ssh -o IdentitiesOnly=yes -i ~/.ssh/deploy_key" git ls-remote git@github.com:example/mono-app.git, Permission denied (publickey), fatal: Could not read from remote repository., git@github.com:example/mono-app.git | LiteLLM backend returned empty output. |
| `ssh-02` | `summary` | `ssh` | `6896.29` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ssh deploy@staging.example.net, /home/dev/.ssh/known_hosts:42, staging.example.net, Host key verification failed. | LiteLLM backend returned empty output. |
| `systemd-01` | `summary` | `systemd` | `6746.96` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `5177.45` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `11539.39` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | sudo apt-get install libpq-dev postgresql-client, libpq-dev, libpq5, postgresql-client-16, held broken packages | LiteLLM backend returned empty output. |
| `dnf-01` | `recall` | `dnf` | `10919.73` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | sudo dnf install python3-devel postgresql-devel, conflicting requests, python3.12-devel, python3.12-3.12.0-1.el9.x86_64, python3.12-3.12.2-2.el9.x86_64 | LiteLLM backend returned empty output. |
| `go-build-01` | `summary` | `go-build` | `5517.35` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `8296.91` | `0.991` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `6530.45` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | javac -d out $(find src/main/java -name '*.java'), src/main/java/com/example/app/cli/RunCommand.java:18, OrderService, cannot find symbol | LiteLLM backend returned empty output. |
| `maven-01` | `summary` | `maven` | `5652.66` | `0.988` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-02` | `summary` | `maven` | `6524.58` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `10046.56` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `10418.73` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ./gradlew test, InventoryServiceTest, InventoryServiceTest.java:118, Execution failed for task ':test' | LiteLLM backend returned empty output. |
| `cargo-01` | `summary` | `cargo` | `10363.43` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | cargo build, error[E0308], src/config.rs:27:18, ingest-cli | LiteLLM backend returned empty output. |
| `cargo-02` | `summary` | `cargo` | `10767.86` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | cargo build, rand = "^0.9.0", crates.io index, guessing_game v0.1.0 | LiteLLM backend returned empty output. |
| `node-runtime-01` | `recall` | `node-runtime` | `17819.90` | `0.993` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-04` | `summary` | `npm` | `7023.84` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | npm install, ERESOLVE, react@18.3.1, @testing-library/react-hooks@8.0.1, dashboard-web@0.9.0 | LiteLLM backend returned empty output. |
| `tsc-01` | `summary` | `tsc` | `7788.61` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | npx tsc -p tsconfig.build.json, src/routes/user.ts(14,21), TS2339, userId | LiteLLM backend returned empty output. |
| `eslint-04` | `summary` | `eslint` | `7724.79` | `0.993` | `1.000` | `0.983` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `7697.19` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | python -m tools.sync_rules --env staging, /workspace/app/loader.py, line 52, FileNotFoundError, rules/staging.json | LiteLLM backend returned empty output. |
| `pytest-06` | `summary` | `pytest` | `4840.13` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `23145.40` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | mypy app, app/models/session.py:44, union-attr, User | None, id | LiteLLM backend returned empty output. |
| `docker-build-01` | `summary` | `docker-build` | `8180.71` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund, Dockerfile:8, zod@3.23.8, failed to solve | LiteLLM backend returned empty output. |
| `docker-compose-04` | `summary` | `docker-compose` | `6992.44` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | docker compose up --build, mono-api-1, 0.0.0.0:8080, port is already allocated | LiteLLM backend returned empty output. |
| `kubectl-05` | `summary` | `kubectl` | `5705.88` | `0.975` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `7806.77` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | kubectl describe pod web-7f6f6d9d7b-kj4t2 -n dev, migrate, CrashLoopBackOff, Exit Code:    1 | LiteLLM backend returned empty output. |
| `kubectl-07` | `recall` | `kubectl` | `6868.04` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `7200.69` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | terraform plan -lock-timeout=5s -out=tfplan, Error acquiring the state lock, 9c4fd2f2-8b24-42c1-93b5-65f0e2d83f63, prod/network/terraform.tfstate | LiteLLM backend returned empty output. |
| `terraform-06` | `summary` | `terraform` | `6734.36` | `0.976` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `8177.48` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | terraform plan -detailed-exitcode -no-color, Plan: 1 to add, 1 to change, 0 to destroy., 2, aws_security_group_rule.web_https | LiteLLM backend returned empty output. |
| `nginx-01` | `summary` | `nginx` | `7321.03` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `7731.44` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | sudo service nginx reload, /etc/letsencrypt/live/example.com/fullchain.pem, cannot load certificate, configuration file /etc/nginx/nginx.conf test failed | LiteLLM backend returned empty output. |
| `postgres-01` | `recall` | `postgres` | `8820.00` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | psql -h 127.0.0.1 -U app_user -d appdb -c 'select 1', FATAL:, role "app_user" does not exist, 127.0.0.1 | LiteLLM backend returned empty output. |
| `postgres-02` | `summary` | `postgres` | `7978.88` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | psql -v ON_ERROR_STOP=1 -f migrations/all.sql appdb, migrations/202605160830_add_users.sql:42, relation "users" already exists, ROLLBACK | LiteLLM backend returned empty output. |
| `mysql-01` | `summary` | `mysql` | `7528.08` | `0.995` | `1.000` | `0.989` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `3550.33` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `7191.25` | `0.948` | `1.000` | `0.946` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `7365.67` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `7631.07` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ruff check ., src/api/views.py, line=91, Ruff F821, exit code 2 | LiteLLM backend returned empty output. |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `8348.55` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | pnpm install --frozen-lockfile, ERR_PNPM_ENOSPC, no space left on device, react-dom@18.3.1, ERROR: Job failed: exit status 1 | LiteLLM backend returned empty output. |
| `jenkins-01` | `summary` | `jenkins` | `6479.62` | `0.967` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `7373.44` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | make CFLAGS='-O2 -Wall -Werror' all, src/parser.c:214:12, parse_config, Makefile:22, Error 1 | LiteLLM backend returned empty output. |
| `tar-01` | `summary` | `tar` | `7413.85` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | tar -xzf cache/node_modules.tgz -C /tmp/restore, unexpected end of file, Unexpected EOF in archive, cache/node_modules.tgz | LiteLLM backend returned empty output. |
| `ansible-01` | `recall` | `ansible` | `6163.45` | `0.995` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `7318.15` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | rsync -av --delete build/ artifact-store/build/, runtime-1a2b3c.js, code 24, some files vanished before they could be transferred | LiteLLM backend returned empty output. |
| `test-failure-01` | `recall` | `test-failure` | `7335.23` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | tests/unit/test_invoice_totals.py::test_discount_rounding, tests/unit/test_invoice_totals.py:88, Decimal('17.50'), Decimal('17.49'), ROUND_HALF_UP is deprecated for discounts; use ROUND_HALF_EVEN | LiteLLM backend returned empty output. |
| `compiler-error-01` | `recall` | `compiler-error` | `6782.61` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-log-01` | `recall` | `ci-log` | `11628.28` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | helm upgrade --install payments-api charts/payments-api --namespace prod-payments, Deployment.apps "payments-api" is invalid, spec.template.spec.containers[0].env[3].valueFrom.secretKeyRef.name, Invalid value: "", deployments.apps "payments-api" not found | LiteLLM backend returned empty output. |
| `package-manager-01` | `recall` | `package-manager` | `8056.32` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | npm install @storybook/react-vite@8.2.0 vite@6.0.1, npm ERR! code ERESOLVE, @storybook/react-vite@8.2.0, vite@6.0.1, peer vite@"^4.0.0 || ^5.0.0", --force or --legacy-peer-deps | LiteLLM backend returned empty output. |
| `test-summary-01` | `summary` | `test-summary` | `7197.28` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | github.com/acme/shop/checkout, TestCheckoutAppliesStoreCredit, checkout_test.go:71, total = 42.00, want 37.00, github.com/acme/shop/inventory, TestReconcileInventory, test timed out after 10m0s, worker.go:144 | LiteLLM backend returned empty output. |
| `build-log-01` | `summary` | `build-log` | `7988.99` | `0.985` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `5914.56` | `0.774` | `1.000` | `0.935` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `7214.68` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | /repo/web/src/App.tsx, 27:19, @typescript-eslint/no-misused-promises, /repo/web/src/api/client.ts, 8:10, @typescript-eslint/no-explicit-any, 33:11, @typescript-eslint/no-unsafe-assignment | LiteLLM backend returned empty output. |
| `git-review-01` | `instruction_following` | `git-review` | `9417.82` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | packages/api/src/auth/session.ts, packages/api/src/schema/openapi.yaml, migrations/202605171200_add_refresh_ttl.sql, User.lastLoginIp, DROP COLUMN refresh_token_expires_at, session cookie maxAge changed from 86400 to 604800 | LiteLLM backend returned empty output. |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `9721.04` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | search endpoint failed after 2 attempts, exit status 22, https://staging.example.com/api/search?q=smoke, curl: (22) | LiteLLM backend returned empty output. |
| `structured-output-01` | `structured` | `structured-output` | `9817.50` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | /work/app/services/payments.py, 42, reportArgumentType, /work/app/api/routes.py, 21, reportUndefinedVariable | LiteLLM backend returned empty output. |
| `structured-output-02` | `structured` | `structured-output` | `13670.70` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | test / integration, Start docker compose, port 5432 is already allocated, deploy / preview, Upload artifact, dist/preview | LiteLLM backend returned empty output. |
| `structured-output-03` | `structured` | `structured-output` | `7046.64` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | createSession › rejects expired refresh token, src/auth/session.test.ts, "refresh token expired", "invalid refresh token", calculateTax › uses EU VAT for DE customer, src/billing/tax.test.ts, Expected: 19, Received: 0 | LiteLLM backend returned empty output. |
| `structured-output-04` | `structured` | `structured-output` | `5167.79` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `10069.80` | `0.189` | `1.000` | `0.336` | `0.000` | `0.000` | `0.100` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `5215.97` | `0.278` | `1.000` | `0.776` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `6326.30` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `7790.45` | `0.989` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `6839.83` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | TS2322, string | undefined, AvatarProps.url | LiteLLM backend returned empty output. |
| `diagnosis-03` | `explanation` | `diagnosis` | `7107.83` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | orders_customer_id_fkey, customer_id, 00000000-0000-0000-0000-000000000000, customers | LiteLLM backend returned empty output. |
| `python-traceback-01` | `recall` | `python-traceback` | `7129.66` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | app.tasks.email.send_welcome_email, SMTPRecipientsRefused, /srv/app/app/tasks/email.py, line 92, [bad@example.test](mailto:bad@example.test), retries exhausted for queue emails | LiteLLM backend returned empty output. |
| `mypy-05` | `recall` | `mypy` | `6383.21` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | src/services/exporter.py:118, Signature of "serialize" incompatible with supertype "BaseExporter", [override], include_meta, -> bytes, -> str | LiteLLM backend returned empty output. |
| `terraform-08` | `recall` | `terraform` | `11013.90` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | module.worker.aws_iam_policy.worker_inline, worker-prod-inline, EntityAlreadyExists, status code: 409, request id: 0f3e2b11-9ac9-4fd2-a3bb-6c07a3c6a90d, modules/worker/iam.tf line 27 | LiteLLM backend returned empty output. |
| `gradle-junit-01` | `recall` | `gradle-junit` | `6403.43` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | InventorySyncTest > publishesBackorderEvent() FAILED, BACKORDER_CREATED, STOCK_RESERVED, InventorySyncTest.java:132, OrderServiceTest > calculatesDiscountForGoldCustomer() PASSED | LiteLLM backend returned empty output. |
| `kubernetes-01` | `recall` | `kubernetes` | `6666.62` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | api-7d9f8c8b99-mx2kq, registry.example.com/api:2026.05.18-1, CrashLoopBackOff, Exit Code: 78, STRIPE_KEY, FATAL config: required env STRIPE_KEY is empty | LiteLLM backend returned empty output. |
| `go-test-02` | `recall` | `go-test` | `7332.04` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | WARNING: DATA RACE, (*Store).Set(), /work/internal/cache/store.go:88, (*Store).Get(), /work/internal/cache/store.go:54, TestConcurrentSetGet | LiteLLM backend returned empty output. |
| `cargo-03` | `recall` | `cargo` | `7052.87` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | error[E0432], BroadcastStream, crates/storage/src/events.rs:7:5, tokio_stream::wrappers, gated behind the `sync` feature, could not compile `storage` | LiteLLM backend returned empty output. |
| `docker-compose-05` | `recall` | `docker-compose` | `7286.26` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | container app-api-1 is unhealthy, dependency failed to start, FATAL: password authentication failed for user "app", migration failed; exiting, docker compose up --wait api worker | LiteLLM backend returned empty output. |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `9734.60` | `0.983` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `8587.24` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | packages/db migrate.test.ts, 20260518_add_workspace_limits.sql, relation "workspace_limits" already exists, packages/db/src/migrate.ts:77:13, packages/db/test/migrate.test.ts:44:7, exit code 1 | LiteLLM backend returned empty output. |
| `pnpm-04` | `recall` | `pnpm` | `6772.74` | `0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `6791.68` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | UserDecoderTests testMissingAvatarUsesPlaceholder, Tests/UserDecoderTests.swift:47, XCTAssertEqual failed, nil, Optional(placeholder.png), fatalError | LiteLLM backend returned empty output. |
| `elixir-01` | `recall` | `elixir` | `6630.93` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | MyApp.CacheWorker, KeyError, key :ttl not found, lib/my_app/cache_worker.ex:63, test/my_app/cache_worker_test.exs:29, refreshes expired keys | LiteLLM backend returned empty output. |
| `rails-01` | `recall` | `rails` | `6541.09` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | 20260518093012 AddIndexToEventsRequestId, index_events_on_request_id, events, already exists, 20260518093012_add_index_to_events_request_id.rb:3, ArgumentError | LiteLLM backend returned empty output. |
| `phpunit-01` | `recall` | `phpunit` | `7898.43` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | Tests\Billing\InvoiceTotalTest::testAppliesCreditBeforeTax, Failed asserting that '88.00' is identical to '86.40', /tests/Billing/InvoiceTotalTest.php:52, Failures: 1, Deprecations: 2 | LiteLLM backend returned empty output. |
| `nginx-03` | `recall` | `nginx` | `6848.23` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | nginx -t -c /etc/nginx/nginx.conf, duplicate location "/api", /etc/nginx/conf.d/api.conf:22, configuration file /etc/nginx/nginx.conf test failed | LiteLLM backend returned empty output. |
| `postgres-03` | `recall` | `postgres` | `11564.10` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | psql:dump.sql:418, type "vector" does not exist, embedding vector(1536), current transaction is aborted, ROLLBACK | LiteLLM backend returned empty output. |
| `ansible-02` | `recall` | `ansible` | `11524.85` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | web-02, UNREACHABLE, 10.0.4.22 port 22, Connection timed out, ansible-playbook deploy.yml -i inventory/prod.ini | LiteLLM backend returned empty output. |
| `bazel-01` | `recall` | `bazel` | `7071.77` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | //services/reporting:report_parser_test, XMLSyntaxError, Opening and ending tag mismatch: total line 18 and totals, services/reporting/parser.py", line 141, etree.fromstring(xml_bytes) | LiteLLM backend returned empty output. |
| `powershell-01` | `recall` | `powershell` | `6899.53` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | .\scripts\release.ps1 -Version 1.4.2, cannot be loaded because running scripts is disabled, PSSecurityException, FullyQualifiedErrorId : UnauthorizedAccess | LiteLLM backend returned empty output. |
| `sentry-cli-01` | `recall` | `sentry-cli` | `8067.44` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | web@1.7.0, upload-sourcemaps dist --rewrite, Authentication credentials were not provided, http status: 401, exit code 1 | LiteLLM remote backend request failed: litellm.BadRequestError: OpenAIException - Could not finish the message because max_tokens or model output limit was reached. Please try again with higher max_tokens. LiteLLM Retried: 1 times |
| `python-pytest-01` | `summary` | `python-pytest` | `7358.97` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | tests/payments, tests/refunds, tests/payments/test_webhook.py::test_replays_duplicate_event, RuntimeError, STRIPE_WEBHOOK_SECRET | LiteLLM backend returned empty output. |
| `go-test-03` | `summary` | `go-test` | `6267.56` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `9411.44` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | web@1.2.0, src/pages/admin.tsx, TS2339, Property, roleName | LiteLLM backend returned empty output. |
| `helm-01` | `summary` | `helm` | `9611.93` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | template, api/templates/deployment.yaml:42:29, executing, api/templates/deployment.yaml, Values.image.repository | LiteLLM backend returned empty output. |
| `ruff-04` | `summary` | `ruff` | `7083.64` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | app/api/routes.py:3:1, typing.Optional, app/services/user.py:88:89, tests/test_user.py:12:1, un-formatted | LiteLLM backend returned empty output. |
| `k6-01` | `summary` | `k6` | `7508.98` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | smoke.js, checks, http_req_failed, http_req_duration, avg | LiteLLM backend returned empty output. |
| `composer-01` | `summary` | `composer` | `6622.80` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | composer, install, --no-dev, Loading, composer | LiteLLM backend returned empty output. |
| `xcodebuild-01` | `summary` | `xcodebuild` | `7026.15` | `0.972` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `6591.41` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | -Iinclude, src/server.c, build/server.o, src/server.c:14:10, openssl/ssl.h | LiteLLM backend returned empty output. |
| `python-pytest-02` | `summary` | `python-pytest` | `6653.49` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | auto, tests/e2e, Not, properly, terminated | LiteLLM backend returned empty output. |
| `jest-01` | `summary` | `jest` | `6142.30` | `0.963` | `1.000` | `0.907` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `13193.95` | `0.970` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `16265.73` | `0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `10458.57` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | wrangler, deploy, Total, Upload, 183.22 | LiteLLM backend returned empty output. |
| `python-pytest-04` | `summary` | `python-pytest` | `5987.14` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `15688.13` | `1.000` | `1.000` | `0.998` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `6533.79` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | src/auth/token.ts, JWT expiry from 15m to 7d, infra/terraform/iam.tf, iam:PassRole | LiteLLM backend returned empty output. |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `13882.30` | `0.429` | `1.000` | `0.708` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `8211.22` | `0.940` | `1.000` | `0.799` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `8966.01` | `0.919` | `1.000` | `0.730` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `6148.02` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | npm ERR! code ENOTEMPTY, npm ERR! syscall rename, /repo/node_modules/esbuild, /repo/node_modules/.esbuild.DELETE | LiteLLM backend returned empty output. |
| `docker-build-03` | `instruction_following` | `docker-build` | `12391.95` | `0.523` | `1.000` | `0.742` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `13980.52` | `0.918` | `1.000` | `0.726` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `8695.83` | `0.986` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `7782.12` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | firefox, checkout.spec.ts:44:1, pays with saved card, Payment complete | LiteLLM backend returned empty output. |
| `prettier-01` | `instruction_following` | `prettier` | `13154.86` | `0.465` | `1.000` | `0.717` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `7056.77` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | worker-5b8c, CrashLoopBackOff, migrator-9z1q, Error | LiteLLM backend returned empty output. |
| `cargo-04` | `instruction_following` | `cargo` | `8414.71` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | auth::tests::parses_expired_token, src/auth.rs:88, Option::unwrap(), billing::tests::rounds_half_even, left: 1750, right: 1749 | LiteLLM backend returned empty output. |
| `shell-01` | `instruction_following` | `shell` | `13015.73` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | rsync, /var/backups/uploads, Permission denied (13), exit code 23 | LiteLLM backend returned empty output. |
| `pyright-01` | `structured` | `pyright` | `9276.74` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | file, /repo/app/user.py, line, code, reportOptionalMemberAccess, message | LiteLLM backend returned empty output. |
| `terraform-10` | `structured` | `terraform` | `8521.23` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | add, aws_iam_role.app, change, resource, aws_lambda_function.api, field | LiteLLM backend returned empty output. |
| `junit-01` | `structured` | `junit` | `7659.06` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | Test, Error, Location, ---, CalculatorTest, dividesByZero | LiteLLM backend returned empty output. |
| `kubernetes-03` | `structured` | `kubernetes` | `2730.97` | `0.587` | `1.000` | `0.323` | `0.475` | `0.475` | `1.000` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `7265.43` | `0.269` | `1.000` | `0.183` | `0.000` | `0.000` | `0.147` | `accepted` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `8151.58` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | stage, builder, command, pnpm, build, error | LiteLLM backend returned empty output. |
| `go-test-04` | `structured` | `go-test` | `8192.71` | `0.397` | `1.000` | `0.191` | `0.100` | `0.100` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `7028.57` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | Job, Step, Exit, ---, test, Run | LiteLLM backend returned empty output. |
| `npm-07` | `structured` | `npm` | `5003.47` | `0.800` | `1.000` | `0.601` | `0.800` | `0.800` | `1.000` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `7528.88` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | File, Line, Code, Message, ---, app/api.py | LiteLLM backend returned empty output. |
| `gradle-03` | `structured` | `gradle` | `8832.47` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | failed, task, :api:compileJava, cause, cannot, find | LiteLLM backend returned empty output. |
| `playwright-02` | `structured` | `playwright` | `6833.92` | `0.355` | `1.000` | `0.183` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `8166.20` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | errors, file, migrations/004.sql, line, message, column | LiteLLM backend returned empty output. |
| `vite-01` | `structured` | `vite` | `6415.99` | `0.560` | `1.000` | `0.198` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `3455.00` | `0.195` | `1.000` | `0.320` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `3729.74` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `3492.14` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `2259.10` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `6072.70` | `0.234` | `1.000` | `0.335` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `8175.47` | `0.231` | `1.000` | `0.306` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `5003.65` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `2182.85` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `3324.27` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `14205.91` | `0.962` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `9645.24` | `0.951` | `1.000` | `0.902` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `13622.49` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | orders_customer_id_fkey, customer_id, customers | LiteLLM backend returned empty output. |
| `docker-build-05` | `explanation` | `docker-build` | `7280.86` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ../shared, outside the build context, COPY | LiteLLM backend returned empty output. |
| `kubernetes-04` | `explanation` | `kubernetes` | `6821.52` | `0.956` | `1.000` | `0.911` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `6381.89` | `0.900` | `1.000` | `0.799` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `6612.09` | `0.968` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `5150.74` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `5363.75` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `10775.56` | `0.757` | `1.000` | `0.960` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `package-management-01` | `recall` | `package-management` | `8733.53` | `0.978` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `8183.82` | `0.984` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `9988.20` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | CS0234, Program.cs(15,10), JsonConvert | LiteLLM backend returned empty output. |
| `package-management-02` | `recall` | `package-management` | `8106.77` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | error[E0277], main.rs:5:26, Display | LiteLLM backend returned empty output. |
| `ci-01` | `recall` | `ci` | `8005.19` | `0.968` | `1.000` | `0.871` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `10293.61` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | COPY failed, no such file or directory | LiteLLM backend returned empty output. |
| `deployment-01` | `recall` | `deployment` | `7391.60` | `0.975` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `3945.10` | `0.988` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `3735.20` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `10278.84` | `0.971` | `1.000` | `0.882` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `11491.97` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | BUILD FAILED, Execution failed for task ':test' | LiteLLM backend returned empty output. |
| `container-runtime-01` | `recall` | `container-runtime` | `9300.22` | `0.977` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `8194.76` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | package com.google.common does not exist, 1 error | LiteLLM backend returned empty output. |
| `infrastructure-02` | `recall` | `infrastructure` | `4148.88` | `0.970` | `1.000` | `0.879` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `3395.96` | `0.991` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `7875.47` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | No matching distribution found, requests==3.0.0 | LiteLLM backend returned empty output. |
| `infrastructure-03` | `recall` | `infrastructure` | `4480.48` | `0.985` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `10386.54` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | Failure/Error, User signs in, capybara-3.34.0/lib/capybara/node/element.rb:1008 | LiteLLM backend returned empty output. |
| `build-02` | `recall` | `build` | `6232.93` | `0.985` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `7850.51` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ERROR: failed to fetch, 404  Not Found, libssl1.0.0_1.0.2g-1ubuntu4.0_amd64.deb | LiteLLM backend returned empty output. |
| `testing-05` | `recall` | `testing` | `6868.31` | `0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `4044.53` | `0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `3204.47` | `0.938` | `1.000` | `0.845` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `4522.74` | `0.961` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `3966.27` | `0.950` | `1.000` | `0.875` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `5232.37` | `0.983` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `7153.62` | `0.949` | `1.000` | `0.874` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `7826.00` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | error, index.js | LiteLLM backend returned empty output. |
| `testing-06` | `instruction_following` | `testing` | `5585.82` | `0.817` | `1.000` | `0.945` | `0.667` | `0.600` | `0.667` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `6369.51` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ERROR: failed to fetch, 404  Not Found | LiteLLM backend returned empty output. |
| `linting-02` | `structured` | `linting` | `6678.19` | `0.832` | `1.000` | `0.837` | `0.786` | `0.707` | `0.667` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `6603.42` | `0.539` | `1.000` | `0.325` | `0.354` | `0.354` | `1.000` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `4896.57` | `0.925` | `1.000` | `0.817` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `6268.93` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `2879.71` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `2980.20` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `2611.28` | `0.232` | `1.000` | `0.320` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `5221.53` | `0.513` | `1.000` | `0.798` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `build-05` | `exact_format` | `build` | `2751.21` | `0.233` | `1.000` | `0.333` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `5303.65` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `7213.17` | `0.921` | `1.000` | `0.898` | `1.000` | `0.917` | `0.722` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `4864.61` | `0.904` | `1.000` | `0.888` | `1.000` | `0.880` | `0.600` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `7650.28` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | pull access denied, repository does not exist | LiteLLM backend returned empty output. |
| `runtime-05` | `explanation` | `runtime` | `7684.03` | `0.929` | `1.000` | `0.905` | `1.000` | `0.929` | `0.762` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `8176.50` | `0.963` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `4223.90` | `0.930` | `1.000` | `0.891` | `1.000` | `0.955` | `0.850` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `6892.65` | `0.916` | `1.000` | `0.899` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `7022.27` | `0.925` | `1.000` | `0.902` | `1.000` | `0.922` | `0.739` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `6537.47` | `0.909` | `1.000` | `0.908` | `1.000` | `0.865` | `0.550` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `9509.68` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | no configured push destination | LiteLLM backend returned empty output. |
| `explanation-04` | `explanation` | `explanation` | `7777.96` | `0.949` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `6553.88` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | command not found | LiteLLM backend returned empty output. |
| `explanation-06` | `explanation` | `explanation` | `6678.06` | `0.870` | `1.000` | `0.833` | `1.000` | `0.860` | `0.533` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `5269.30` | `0.956` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `5342.39` | `0.888` | `1.000` | `0.883` | `1.000` | `0.838` | `0.462` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `4946.65` | `0.967` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `6238.42` | `0.909` | `1.000` | `0.903` | `1.000` | `0.874` | `0.579` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `5098.83` | `0.934` | `1.000` | `0.918` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `3484.92` | `0.933` | `1.000` | `0.879` | `1.000` | `0.980` | `0.933` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `4110.89` | `0.539` | `1.000` | `0.325` | `0.354` | `0.354` | `1.000` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `4201.00` | `0.925` | `1.000` | `0.817` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `5473.90` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `2549.12` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `2232.93` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `12911.93` | `0.411` | `1.000` | `0.497` | `0.333` | `0.333` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `runtime-07` | `exact_format` | `runtime` | `3245.18` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `2692.57` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `5102.21` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `8851.52` | `0.945` | `1.000` | `0.905` | `1.000` | `0.979` | `0.929` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `6144.34` | `0.932` | `1.000` | `0.865` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `7054.18` | `0.924` | `1.000` | `0.892` | `1.000` | `0.936` | `0.786` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `7333.37` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | cannot list resource "pods" | LiteLLM backend returned empty output. |
| `explanation-14` | `explanation` | `explanation` | `9574.10` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | password authentication failed | LiteLLM backend returned empty output. |
| `explanation-15` | `explanation` | `explanation` | `5513.98` | `0.975` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `7918.37` | `0.917` | `1.000` | `0.877` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `6885.35` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | missing script: start | LiteLLM backend returned empty output. |
| `package-management-04` | `explanation` | `package-management` | `3798.56` | `0.940` | `1.000` | `0.881` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
