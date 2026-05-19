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

- load_ms: `11373.43`
- cpu_rss_bytes: `1930207232`
- gpu_peak_bytes: `1226193920`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `150`
- accepted_count: `149`
- soft_accepted_count: `1`
- rejected_count: `130`
- exact_pass_count: `150`
- avg_inference_ms: `10331.80`
- p95_inference_ms: `18791.80`
- avg_exact_preservation_ratio: `0.536`
- avg_summary_quality_ratio: `0.467`
- avg_format_adherence_score: `0.472`
- avg_instruction_following_score: `0.466`
- avg_brevity_ratio: `0.968`
- avg_case_score: `0.477`
- p10_case_score: `0.000`
- quality_core: `0.382`
- latency_factor: `0.850`
- final_score: `32.45`
- peak_cpu_rss_bytes: `1930276864`
- peak_gpu_bytes: `1226193920`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `11603.66` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | python -m app.cli sync --config config/settings.json, /workspace/app/config.py, line 27, JSONDecodeError, line 18 column 3, config/settings.json | LiteLLM backend returned empty output. |
| `python-02` | `summary` | `python` | `11677.21` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | LiteLLM backend returned empty output. |
| `python-03` | `recall` | `python` | `12008.67` | `0.993` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `11674.34` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | python -m jobs.refresh_catalog --region us-east-1, /workspace/src/jobs/refresh_catalog.py, line 119, httpx.ReadTimeout, catalog?page=2, us-east-1 | LiteLLM backend returned empty output. |
| `python-05` | `recall` | `python` | `10356.28` | `0.995` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `7695.53` | `0.998` | `1.000` | `0.991` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `11487.05` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | pytest tests/integration -k billing -vv --maxfail=1, tests/integration/test_billing_api.py::test_invoice_webhook_uses_signature, signed_payload, /workspace/tests/integration/test_billing_api.py:73, 1 error in 2.31s | LiteLLM backend returned empty output. |
| `pytest-03` | `recall` | `pytest` | `12443.58` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | pytest tests -q -x, tests/jobs/test_retention.py::test_archive_marks_job_deleted, teardown, psycopg.errors.ForeignKeyViolation, job_runs_job_id_fkey, 149 passed, 1 skipped, 1 error in 58.73s | LiteLLM backend returned empty output. |
| `pytest-04` | `recall` | `pytest` | `10279.89` | `0.996` | `1.000` | `0.985` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `11505.82` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | pytest tests/unit tests/integration --disable-warnings=0, tests/unit/test_stripe_client.py, src/billing/client.py:9, ModuleNotFoundError, stripe, 1 error during collection | LiteLLM backend returned empty output. |
| `mypy-01` | `recall` | `mypy` | `11497.80` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | mypy src/accounts/user_service.py --show-error-codes, src/accounts/user_service.py:84, attr-defined, UserRecord, is_staff, Found 1 error in 1 file | LiteLLM backend returned empty output. |
| `mypy-02` | `summary` | `mypy` | `11471.96` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | mypy src tests --pretty --show-error-codes, src/payments/retry.py:118, arg-type, RetryEvent, append, checked 37 source files | LiteLLM backend returned empty output. |
| `mypy-03` | `recall` | `mypy` | `11427.14` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | mypy src/orders/normalize.py --show-error-codes --strict, src/orders/normalize.py:41, union-attr, currency, Order | None, type: ignore | LiteLLM backend returned empty output. |
| `ruff-01` | `summary` | `ruff` | `11694.67` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ruff check src --output-format=full, src/payments/init.py:1:20, F401, Client, all, Found 1 error. | LiteLLM backend returned empty output. |
| `ruff-02` | `summary` | `ruff` | `11670.38` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ruff format --check src tests, src/api/serializers.py, 1 file would be reformatted, 52 files already formatted | LiteLLM backend returned empty output. |
| `ruff-03` | `summary` | `ruff` | `11427.43` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ruff check src/auth/login.py, src/auth/login.py:93:13, B904, except, Found 1 error. | LiteLLM backend returned empty output. |
| `pylint-01` | `recall` | `pylint` | `13564.23` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | pylint src/storage/path_utils.py, src/storage/path_utils.py:27:18, E1101, no-member, mothers, Path | LiteLLM backend returned empty output. |
| `pylint-02` | `recall` | `pylint` | `12107.55` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | pylint src/config/runtime.py src/api/server.py, src/config/runtime.py:44:0, F0010, parse-error, expected ":", src/api/server.py | LiteLLM backend returned empty output. |
| `pylint-03` | `summary` | `pylint` | `8138.51` | `0.998` | `1.000` | `0.995` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `11308.38` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | black --check src tests, /workspace/src/api/routes.py, /workspace/tests/test_routes.py, 2 files would be reformatted, 41 files would be left unchanged | LiteLLM backend returned empty output. |
| `black-02` | `summary` | `black` | `11148.01` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | black src, /workspace/src/config/schema.py, Cannot parse, 58:12, 1 file failed to reformat, 1 file reformatted | LiteLLM backend returned empty output. |
| `black-03` | `recall` | `black` | `6308.59` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `11000.89` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | npm ci, EUSAGE, react@18.3.1, scheduler@0.23.2, package-lock.json, /home/dev/.npm/_logs/2026-05-15T09_20_11_449Z-debug-0.log | LiteLLM backend returned empty output. |
| `npm-02` | `summary` | `npm` | `10995.59` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | npm install, ERESOLVE, react@18.2.0, react-dates@21.8.0, peer react@"^17.0.0", --legacy-peer-deps | LiteLLM backend returned empty output. |
| `npm-03` | `summary` | `npm` | `14478.89` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | npm run build, ./CheckoutButton, src/routes/checkout/index.tsx, Lifecycle script `build` failed, storefront@2.8.1, /workspace | LiteLLM backend returned empty output. |
| `pnpm-01` | `recall` | `pnpm` | `13925.73` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | pnpm install --frozen-lockfile, ERR_PNPM_OUTDATED_LOCKFILE, pnpm-lock.yaml, packages/web/package.json, --no-frozen-lockfile | LiteLLM backend returned empty output. |
| `pnpm-02` | `summary` | `pnpm` | `11220.22` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | pnpm add @tanstack/react-query-devtools@5.52.0 -F packages/admin, ERR_PNPM_NO_MATCHING_VERSION, @tanstack/react-query-devtools@5.52.0, packages/admin, 5.51.1 | LiteLLM backend returned empty output. |
| `pnpm-03` | `summary` | `pnpm` | `16831.32` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `6451.46` | `0.983` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `11666.23` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `11352.93` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | tsc src/index.ts src/http.ts --pretty false, src/index.ts(48,20), TS2769, URL, RequestInit, src/http.ts(9,17) | LiteLLM backend returned empty output. |
| `eslint-01` | `recall` | `eslint` | `11696.31` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | eslint src --format stylish, /workspace/src/logger.js, no-console, Unused eslint-disable directive, /workspace/src/server.js, 3 problems (2 errors, 1 warning) | LiteLLM backend returned empty output. |
| `eslint-02` | `summary` | `eslint` | `7369.77` | `0.985` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `11575.56` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | eslint src --max-warnings=0, /workspace/src/hooks/useCart.ts, react-hooks/exhaustive-deps, 1 problem (0 errors, 1 warning), maximum: 0 | LiteLLM backend returned empty output. |
| `docker-01` | `recall` | `docker` | `12042.96` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | docker build -t api:dev ., COPY docker/entrypoint.sh /entrypoint.sh, /docker/entrypoint.sh, Dockerfile:14, failed to solve | LiteLLM backend returned empty output. |
| `docker-02` | `summary` | `docker` | `10185.64` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | docker run --rm api:dev, api:dev, /entrypoint.sh, no such file or directory | LiteLLM backend returned empty output. |
| `docker-03` | `summary` | `docker` | `10717.99` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | docker build -f docker/web.Dockerfile -t web:ci ., RUN npm ci, ERESOLVE, react-dates@21.8.0, react@18.2.0, exit code: 1 | LiteLLM backend returned empty output. |
| `docker-compose-01` | `summary` | `docker-compose` | `6466.65` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `10230.11` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | docker compose up --build, demo-app-1, tenant_settings, sqlalchemy.exc.ProgrammingError, app-1 exited with code 1 | LiteLLM backend returned empty output. |
| `docker-compose-03` | `summary` | `docker-compose` | `84781.97` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `10596.46` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | kubectl apply -f k8s/deployment.yaml --server-side, apps/v1, containers[name="api"].image, kubectl-edit, --force-conflicts | LiteLLM backend returned empty output. |
| `kubectl-02` | `recall` | `kubectl` | `10724.97` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `8877.55` | `0.992` | `1.000` | `0.981` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `10878.28` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | kubectl logs payments-worker-6f8f7d4df5-z5vsm -c worker --previous -n payments, payments-worker-6f8f7d4df5-z5vsm, /app/config.yaml, ValueError, invalid worker.concurrency, worker | LiteLLM backend returned empty output. |
| `terraform-01` | `summary` | `terraform` | `9059.72` | `0.991` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `12831.38` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | terraform plan, outputs.tf line 14, aws_security_group.db.id, Reference to undeclared resource, aws_security_group, db | LiteLLM backend returned empty output. |
| `terraform-03` | `recall` | `terraform` | `10916.87` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `12254.46` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | terraform test, run "plan_defaults", tests/aws.tftest.hcl line 18, Test assertion failed, aws_instance.web.instance_type, expected t3.small default | LiteLLM backend returned empty output. |
| `mixed-01` | `recall` | `mixed` | `11988.63` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `8000.51` | `0.987` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `12389.32` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | git rebase origin/main, src/api/client.py, a1c9f42, OrdersClient | LiteLLM backend returned empty output. |
| `git-02` | `recall` | `git` | `14438.42` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | git push origin main, main -> main, non-fast-forward, failed to push some refs | LiteLLM backend returned empty output. |
| `git-03` | `recall` | `git` | `11649.24` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `81672.32` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | curl -fL --retry 3 --retry-all-errors -o dist/tool-linux-amd64.tar.gz https://downloads.example.com/tool/releases/v1.8.4/tool-linux-amd64.tar.gz, curl: (22), 404, dist/tool-linux-amd64.tar.gz | LiteLLM backend returned empty output. |
| `curl-02` | `summary` | `curl` | `25461.31` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | curl -I https://docs.example.com/sdk/latest, HTTP/2 301, location: /sdk/v3.4/, cache-control: max-age=3600 | LiteLLM backend returned empty output. |
| `ssh-01` | `summary` | `ssh` | `13514.46` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | GIT_SSH_COMMAND="ssh -o IdentitiesOnly=yes -i ~/.ssh/deploy_key" git ls-remote git@github.com:example/mono-app.git, Permission denied (publickey), fatal: Could not read from remote repository., git@github.com:example/mono-app.git | LiteLLM backend returned empty output. |
| `ssh-02` | `summary` | `ssh` | `11478.56` | `0.981` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `13537.49` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | queue-worker.service, /opt/app/bin/worker.sh, status=203/EXEC, Exec format error | LiteLLM backend returned empty output. |
| `systemd-02` | `summary` | `systemd` | `12932.73` | `0.971` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `12253.96` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | sudo apt-get install libpq-dev postgresql-client, libpq-dev, libpq5, postgresql-client-16, held broken packages | LiteLLM backend returned empty output. |
| `dnf-01` | `recall` | `dnf` | `11651.16` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | sudo dnf install python3-devel postgresql-devel, conflicting requests, python3.12-devel, python3.12-3.12.0-1.el9.x86_64, python3.12-3.12.2-2.el9.x86_64 | LiteLLM backend returned empty output. |
| `go-build-01` | `summary` | `go-build` | `6661.16` | `0.978` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `10071.68` | `0.991` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `11390.45` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | javac -d out $(find src/main/java -name '*.java'), src/main/java/com/example/app/cli/RunCommand.java:18, OrderService, cannot find symbol | LiteLLM backend returned empty output. |
| `maven-01` | `summary` | `maven` | `8655.49` | `0.987` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-02` | `summary` | `maven` | `12437.50` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | mvn -U -DskipTests package, org.postgresql:postgresql:jar:42.7.3, Failed to execute goal on project ingest-service, Could not resolve dependencies | LiteLLM backend returned empty output. |
| `gradle-01` | `recall` | `gradle` | `11379.94` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ./gradlew :service:build --warning-mode=all, :service:compileJava, :service:compileClasspath, org.mapstruct:mapstruct:1.5.5.Final | LiteLLM backend returned empty output. |
| `gradle-02` | `summary` | `gradle` | `7405.66` | `0.990` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `10741.02` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | cargo build, error[E0308], src/config.rs:27:18, ingest-cli | LiteLLM backend returned empty output. |
| `cargo-02` | `summary` | `cargo` | `10733.93` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | cargo build, rand = "^0.9.0", crates.io index, guessing_game v0.1.0 | LiteLLM backend returned empty output. |
| `node-runtime-01` | `recall` | `node-runtime` | `11040.93` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | node dist/server.js, Cannot find module './env/schema', MODULE_NOT_FOUND, /workspace/dist/config/index.js:4:18 | LiteLLM backend returned empty output. |
| `npm-04` | `summary` | `npm` | `11151.90` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | npm install, ERESOLVE, react@18.3.1, @testing-library/react-hooks@8.0.1, dashboard-web@0.9.0 | LiteLLM backend returned empty output. |
| `tsc-01` | `summary` | `tsc` | `10507.00` | `0.992` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `12022.11` | `0.987` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `11017.37` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | python -m tools.sync_rules --env staging, /workspace/app/loader.py, line 52, FileNotFoundError, rules/staging.json | LiteLLM backend returned empty output. |
| `pytest-06` | `summary` | `pytest` | `7909.98` | `0.990` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `12553.27` | `0.991` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `13137.43` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund, Dockerfile:8, zod@3.23.8, failed to solve | LiteLLM backend returned empty output. |
| `docker-compose-04` | `summary` | `docker-compose` | `12334.35` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | docker compose up --build, mono-api-1, 0.0.0.0:8080, port is already allocated | LiteLLM backend returned empty output. |
| `kubectl-05` | `summary` | `kubectl` | `11544.46` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | kubectl apply -f k8s/, Service "api", spec.clusterIP, field is immutable | LiteLLM backend returned empty output. |
| `kubectl-06` | `summary` | `kubectl` | `11337.12` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | kubectl describe pod web-7f6f6d9d7b-kj4t2 -n dev, migrate, CrashLoopBackOff, Exit Code:    1 | LiteLLM backend returned empty output. |
| `kubectl-07` | `recall` | `kubectl` | `11429.63` | `0.994` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `9208.83` | `0.997` | `1.000` | `0.987` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `10817.65` | `0.970` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `10230.71` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | terraform plan -detailed-exitcode -no-color, Plan: 1 to add, 1 to change, 0 to destroy., 2, aws_security_group_rule.web_https | LiteLLM backend returned empty output. |
| `nginx-01` | `summary` | `nginx` | `12081.62` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | sudo nginx -t, "server" directive is not allowed here, /etc/nginx/sites-enabled/api.conf:1, configuration file /etc/nginx/nginx.conf test failed | LiteLLM backend returned empty output. |
| `nginx-02` | `summary` | `nginx` | `12645.26` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | sudo service nginx reload, /etc/letsencrypt/live/example.com/fullchain.pem, cannot load certificate, configuration file /etc/nginx/nginx.conf test failed | LiteLLM backend returned empty output. |
| `postgres-01` | `recall` | `postgres` | `10765.85` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | psql -h 127.0.0.1 -U app_user -d appdb -c 'select 1', FATAL:, role "app_user" does not exist, 127.0.0.1 | LiteLLM backend returned empty output. |
| `postgres-02` | `summary` | `postgres` | `13298.27` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | psql -v ON_ERROR_STOP=1 -f migrations/all.sql appdb, migrations/202605160830_add_users.sql:42, relation "users" already exists, ROLLBACK | LiteLLM backend returned empty output. |
| `mysql-01` | `summary` | `mysql` | `14854.93` | `0.994` | `1.000` | `0.985` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `8050.12` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `12048.93` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | redis-cli -u redis://127.0.0.1:6379 SET sync:cursor 90210, MISCONF, stop-writes-on-bgsave-error, sync:cursor | LiteLLM backend returned empty output. |
| `redis-02` | `recall` | `redis` | `8434.32` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `11636.09` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ruff check ., src/api/views.py, line=91, Ruff F821, exit code 2 | LiteLLM backend returned empty output. |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `10897.02` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | pnpm install --frozen-lockfile, ERR_PNPM_ENOSPC, no space left on device, react-dom@18.3.1, ERROR: Job failed: exit status 1 | LiteLLM backend returned empty output. |
| `jenkins-01` | `summary` | `jenkins` | `15061.65` | `0.974` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `10927.15` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | make CFLAGS='-O2 -Wall -Werror' all, src/parser.c:214:12, parse_config, Makefile:22, Error 1 | LiteLLM backend returned empty output. |
| `tar-01` | `summary` | `tar` | `10778.88` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | tar -xzf cache/node_modules.tgz -C /tmp/restore, unexpected end of file, Unexpected EOF in archive, cache/node_modules.tgz | LiteLLM backend returned empty output. |
| `ansible-01` | `recall` | `ansible` | `11011.41` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ansible-playbook -i inventories/prod/hosts.ini deploy.yml --limit proxy, proxy-2, UNREACHABLE!, Connection timed out | LiteLLM backend returned empty output. |
| `rsync-01` | `summary` | `rsync` | `13790.81` | `0.976` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `14505.53` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | tests/unit/test_invoice_totals.py::test_discount_rounding, tests/unit/test_invoice_totals.py:88, Decimal('17.50'), Decimal('17.49'), ROUND_HALF_UP is deprecated for discounts; use ROUND_HALF_EVEN | LiteLLM backend returned empty output. |
| `compiler-error-01` | `recall` | `compiler-error` | `14724.49` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | error[E0382], src/router.rs:137:42, borrow of moved value: `req`, src/router.rs:128, req.into_body(), req.method(), req.clone().into_body() | LiteLLM backend returned empty output. |
| `ci-log-01` | `recall` | `ci-log` | `20554.94` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | helm upgrade --install payments-api charts/payments-api --namespace prod-payments, Deployment.apps "payments-api" is invalid, spec.template.spec.containers[0].env[3].valueFrom.secretKeyRef.name, Invalid value: "", deployments.apps "payments-api" not found | LiteLLM backend returned empty output. |
| `package-manager-01` | `recall` | `package-manager` | `11616.78` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | npm install @storybook/react-vite@8.2.0 vite@6.0.1, npm ERR! code ERESOLVE, @storybook/react-vite@8.2.0, vite@6.0.1, peer vite@"^4.0.0 || ^5.0.0", --force or --legacy-peer-deps | LiteLLM backend returned empty output. |
| `test-summary-01` | `summary` | `test-summary` | `10811.51` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | github.com/acme/shop/checkout, TestCheckoutAppliesStoreCredit, checkout_test.go:71, total = 42.00, want 37.00, github.com/acme/shop/inventory, TestReconcileInventory, test timed out after 10m0s, worker.go:144 | LiteLLM backend returned empty output. |
| `build-log-01` | `summary` | `build-log` | `11968.10` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | billing-service, InvoiceMapper.java:[58,29], cannot find symbol, setTaxCode(java.lang.String), InvoiceDto | LiteLLM backend returned empty output. |
| `docker-build-02` | `summary` | `docker-build` | `6130.25` | `0.978` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `8272.41` | `0.866` | `1.000` | `0.998` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `12365.49` | `0.952` | `1.000` | `0.840` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `13598.74` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | search endpoint failed after 2 attempts, exit status 22, https://staging.example.com/api/search?q=smoke, curl: (22) | LiteLLM backend returned empty output. |
| `structured-output-01` | `structured` | `structured-output` | `13740.67` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | /work/app/services/payments.py, 42, reportArgumentType, /work/app/api/routes.py, 21, reportUndefinedVariable | LiteLLM backend returned empty output. |
| `structured-output-02` | `structured` | `structured-output` | `11804.67` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | test / integration, Start docker compose, port 5432 is already allocated, deploy / preview, Upload artifact, dist/preview | LiteLLM backend returned empty output. |
| `structured-output-03` | `structured` | `structured-output` | `10353.91` | `0.988` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-04` | `structured` | `structured-output` | `6013.45` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `17178.64` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | tests/api/test_users.py::test_create_user_requires_email, tests/api/test_users.py::test_delete_user_requires_admin, tests/jobs/test_reconcile.py::TestReconcile::test_retries_deadlock | LiteLLM backend returned empty output. |
| `exact-format-02` | `exact_format` | `exact-format` | `7138.95` | `0.278` | `1.000` | `0.775` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `7005.03` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `10989.05` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | /repo/tools/json.py, has no attribute 'dumps', shadowing | LiteLLM backend returned empty output. |
| `diagnosis-02` | `explanation` | `diagnosis` | `11296.44` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | TS2322, string | undefined, AvatarProps.url | LiteLLM backend returned empty output. |
| `diagnosis-03` | `explanation` | `diagnosis` | `11200.72` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | orders_customer_id_fkey, customer_id, 00000000-0000-0000-0000-000000000000, customers | LiteLLM remote backend request failed: litellm.BadRequestError: OpenAIException - Could not finish the message because max_tokens or model output limit was reached. Please try again with higher max_tokens. LiteLLM Retried: 1 times |
| `python-traceback-01` | `recall` | `python-traceback` | `11073.02` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | app.tasks.email.send_welcome_email, SMTPRecipientsRefused, /srv/app/app/tasks/email.py, line 92, [bad@example.test](mailto:bad@example.test), retries exhausted for queue emails | LiteLLM backend returned empty output. |
| `mypy-05` | `recall` | `mypy` | `13519.95` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | src/services/exporter.py:118, Signature of "serialize" incompatible with supertype "BaseExporter", [override], include_meta, -> bytes, -> str | LiteLLM backend returned empty output. |
| `terraform-08` | `recall` | `terraform` | `14309.71` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | module.worker.aws_iam_policy.worker_inline, worker-prod-inline, EntityAlreadyExists, status code: 409, request id: 0f3e2b11-9ac9-4fd2-a3bb-6c07a3c6a90d, modules/worker/iam.tf line 27 | LiteLLM backend returned empty output. |
| `gradle-junit-01` | `recall` | `gradle-junit` | `11978.27` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | InventorySyncTest > publishesBackorderEvent() FAILED, BACKORDER_CREATED, STOCK_RESERVED, InventorySyncTest.java:132, OrderServiceTest > calculatesDiscountForGoldCustomer() PASSED | LiteLLM backend returned empty output. |
| `kubernetes-01` | `recall` | `kubernetes` | `12028.40` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | api-7d9f8c8b99-mx2kq, registry.example.com/api:2026.05.18-1, CrashLoopBackOff, Exit Code: 78, STRIPE_KEY, FATAL config: required env STRIPE_KEY is empty | LiteLLM backend returned empty output. |
| `go-test-02` | `recall` | `go-test` | `12006.00` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | WARNING: DATA RACE, (*Store).Set(), /work/internal/cache/store.go:88, (*Store).Get(), /work/internal/cache/store.go:54, TestConcurrentSetGet | LiteLLM backend returned empty output. |
| `cargo-03` | `recall` | `cargo` | `11479.47` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | error[E0432], BroadcastStream, crates/storage/src/events.rs:7:5, tokio_stream::wrappers, gated behind the `sync` feature, could not compile `storage` | LiteLLM backend returned empty output. |
| `docker-compose-05` | `recall` | `docker-compose` | `11903.20` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | container app-api-1 is unhealthy, dependency failed to start, FATAL: password authentication failed for user "app", migration failed; exiting, docker compose up --wait api worker | LiteLLM backend returned empty output. |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `12826.33` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | TS2307, @acme/contracts, packages/api/src/index.ts:4:25, TS6305, /repo/packages/contracts/dist/index.d.ts, packages/contracts/src/index.ts | LiteLLM backend returned empty output. |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `10136.95` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `100839.34` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ERR_PNPM_OUTDATED_LOCKFILE, --frozen-lockfile, pnpm-lock.yaml, packages/api/package.json, fastify, ^5.1.0, ^5.2.1 | LiteLLM backend returned empty output. |
| `swift-01` | `recall` | `swift` | `11692.04` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | UserDecoderTests testMissingAvatarUsesPlaceholder, Tests/UserDecoderTests.swift:47, XCTAssertEqual failed, nil, Optional(placeholder.png), fatalError | LiteLLM backend returned empty output. |
| `elixir-01` | `recall` | `elixir` | `19309.34` | `0.986` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `12723.30` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | 20260518093012 AddIndexToEventsRequestId, index_events_on_request_id, events, already exists, 20260518093012_add_index_to_events_request_id.rb:3, ArgumentError | LiteLLM backend returned empty output. |
| `phpunit-01` | `recall` | `phpunit` | `7375.48` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `10706.74` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | nginx -t -c /etc/nginx/nginx.conf, duplicate location "/api", /etc/nginx/conf.d/api.conf:22, configuration file /etc/nginx/nginx.conf test failed | LiteLLM backend returned empty output. |
| `postgres-03` | `recall` | `postgres` | `14805.24` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | psql:dump.sql:418, type "vector" does not exist, embedding vector(1536), current transaction is aborted, ROLLBACK | LiteLLM backend returned empty output. |
| `ansible-02` | `recall` | `ansible` | `12259.78` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | web-02, UNREACHABLE, 10.0.4.22 port 22, Connection timed out, ansible-playbook deploy.yml -i inventory/prod.ini | LiteLLM backend returned empty output. |
| `bazel-01` | `recall` | `bazel` | `11302.68` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | //services/reporting:report_parser_test, XMLSyntaxError, Opening and ending tag mismatch: total line 18 and totals, services/reporting/parser.py", line 141, etree.fromstring(xml_bytes) | LiteLLM backend returned empty output. |
| `powershell-01` | `recall` | `powershell` | `11743.91` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | .\scripts\release.ps1 -Version 1.4.2, cannot be loaded because running scripts is disabled, PSSecurityException, FullyQualifiedErrorId : UnauthorizedAccess | LiteLLM backend returned empty output. |
| `sentry-cli-01` | `recall` | `sentry-cli` | `10648.15` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | web@1.7.0, upload-sourcemaps dist --rewrite, Authentication credentials were not provided, http status: 401, exit code 1 | LiteLLM remote backend request failed: litellm.BadRequestError: OpenAIException - Could not finish the message because max_tokens or model output limit was reached. Please try again with higher max_tokens. LiteLLM Retried: 1 times |
| `python-pytest-01` | `summary` | `python-pytest` | `6638.46` | `0.972` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `8224.92` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ./integration, TestWebhookReplay, runtime, github.com/acme/api/internal/webhook, Dispatcher, dispatch | LiteLLM backend returned empty output. |
| `npm-05` | `summary` | `npm` | `13278.02` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | web@1.2.0, src/pages/admin.tsx, TS2339, Property, roleName | LiteLLM backend returned empty output. |
| `helm-01` | `summary` | `helm` | `11898.23` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | template, api/templates/deployment.yaml:42:29, executing, api/templates/deployment.yaml, Values.image.repository | LiteLLM backend returned empty output. |
| `ruff-04` | `summary` | `ruff` | `13065.30` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | app/api/routes.py:3:1, typing.Optional, app/services/user.py:88:89, tests/test_user.py:12:1, un-formatted | LiteLLM backend returned empty output. |
| `k6-01` | `summary` | `k6` | `12027.43` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | smoke.js, checks, http_req_failed, http_req_duration, avg | LiteLLM backend returned empty output. |
| `composer-01` | `summary` | `composer` | `9311.20` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | composer, install, --no-dev, Loading, composer | LiteLLM backend returned empty output. |
| `xcodebuild-01` | `summary` | `xcodebuild` | `9431.15` | `0.970` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `9422.95` | `0.974` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `11782.47` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | auto, tests/e2e, Not, properly, terminated | LiteLLM backend returned empty output. |
| `jest-01` | `summary` | `jest` | `9519.35` | `0.961` | `1.000` | `0.902` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `15396.81` | `0.971` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `9475.50` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | tests/test_signup.py, FAILED, tests/test_signup.py::test_signup_is_idempotent, sqlalchemy.exc.IntegrityError, psycopg.errors.UniqueViolation | LiteLLM backend returned empty output. |
| `wrangler-01` | `summary` | `wrangler` | `11785.16` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | wrangler, deploy, Total, Upload, 183.22 | LiteLLM backend returned empty output. |
| `python-pytest-04` | `summary` | `python-pytest` | `9853.81` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `9221.20` | `1.000` | `1.000` | `0.998` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `17848.08` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | src/auth/token.ts, JWT expiry from 15m to 7d, infra/terraform/iam.tf, iam:PassRole | LiteLLM backend returned empty output. |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `4239.08` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `7343.90` | `0.940` | `1.000` | `0.799` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `12905.96` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | Warning Failed, secret "api-env" not found, Warning BackOff, Back-off restarting failed container api | LiteLLM backend returned empty output. |
| `npm-06` | `instruction_following` | `npm` | `12742.68` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | npm ERR! code ENOTEMPTY, npm ERR! syscall rename, /repo/node_modules/esbuild, /repo/node_modules/.esbuild.DELETE | LiteLLM backend returned empty output. |
| `docker-build-03` | `instruction_following` | `docker-build` | `5911.15` | `0.523` | `1.000` | `0.742` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `9216.71` | `0.918` | `1.000` | `0.726` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `12418.27` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | UserService.java:[44,17], findByEmail, UserController.java:[28,31], java.lang.Long, java.util.UUID | LiteLLM backend returned empty output. |
| `playwright-01` | `instruction_following` | `playwright` | `11239.82` | `0.920` | `1.000` | `0.732` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `2186.02` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `6970.12` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `14552.15` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | auth::tests::parses_expired_token, src/auth.rs:88, Option::unwrap(), billing::tests::rounds_half_even, left: 1750, right: 1749 | LiteLLM backend returned empty output. |
| `shell-01` | `instruction_following` | `shell` | `11326.92` | `0.541` | `1.000` | `0.802` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `12952.09` | `0.356` | `1.000` | `0.188` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `14914.50` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | add, aws_iam_role.app, change, resource, aws_lambda_function.api, field | LiteLLM backend returned empty output. |
| `junit-01` | `structured` | `junit` | `9799.53` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | Test, Error, Location, ---, CalculatorTest, dividesByZero | LiteLLM backend returned empty output. |
| `kubernetes-03` | `structured` | `kubernetes` | `5306.68` | `0.849` | `1.000` | `0.596` | `0.925` | `0.925` | `1.000` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `11617.72` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | src/a.ts, line, column, rule, no-unused-vars, src/b.ts | LiteLLM backend returned empty output. |
| `docker-build-04` | `structured` | `docker-build` | `13211.00` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | stage, builder, command, pnpm, build, error | LiteLLM backend returned empty output. |
| `go-test-04` | `structured` | `go-test` | `7253.51` | `0.849` | `1.000` | `0.596` | `0.925` | `0.925` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `11462.29` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | Job, Step, Exit, ---, test, Run | LiteLLM backend returned empty output. |
| `npm-07` | `structured` | `npm` | `7426.07` | `0.800` | `1.000` | `0.601` | `0.800` | `0.800` | `1.000` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `19999.30` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | File, Line, Code, Message, ---, app/api.py | LiteLLM backend returned empty output. |
| `gradle-03` | `structured` | `gradle` | `11776.97` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | failed, task, :api:compileJava, cause, cannot, find | LiteLLM backend returned empty output. |
| `playwright-02` | `structured` | `playwright` | `7806.84` | `0.355` | `1.000` | `0.183` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `12355.65` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | errors, file, migrations/004.sql, line, message, column | LiteLLM backend returned empty output. |
| `vite-01` | `structured` | `vite` | `15687.88` | `0.257` | `1.000` | `0.179` | `0.000` | `0.000` | `0.032` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `16944.53` | `0.195` | `1.000` | `0.320` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `4533.05` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `5678.00` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `3194.07` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `7890.81` | `0.211` | `1.000` | `0.314` | `0.000` | `0.000` | `0.600` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `5871.98` | `0.231` | `1.000` | `0.306` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `3946.31` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `4576.91` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `4969.27` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `33285.76` | `0.731` | `1.000` | `0.920` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `34415.21` | `0.947` | `1.000` | `0.894` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `33726.17` | `0.956` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `10133.13` | `0.970` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `9841.99` | `0.962` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `13264.55` | `0.903` | `1.000` | `0.806` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `44221.64` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | HTTP 403, contents: read, contents: write | LiteLLM backend returned empty output. |
| `runtime-01` | `recall` | `runtime` | `21728.50` | `0.999` | `1.000` | `0.996` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `7087.85` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `8655.13` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `7594.15` | `0.975` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `5776.98` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `8266.58` | `0.952` | `1.000` | `0.942` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `17725.08` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `10054.29` | `0.967` | `1.000` | `0.868` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `12826.76` | `0.979` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `13448.84` | `0.952` | `1.000` | `0.892` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `13262.79` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `8928.60` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `18232.86` | `0.971` | `1.000` | `0.882` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `5396.95` | `0.983` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `7740.86` | `0.977` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `16623.57` | `0.981` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `10356.76` | `0.970` | `1.000` | `0.879` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `5280.61` | `0.991` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `18766.53` | `0.986` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `11779.49` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `16462.44` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | Failure/Error, User signs in, capybara-3.34.0/lib/capybara/node/element.rb:1008 | LiteLLM backend returned empty output. |
| `build-02` | `recall` | `build` | `9772.42` | `0.983` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `16458.60` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ERROR: failed to fetch, 404  Not Found, libssl1.0.0_1.0.2g-1ubuntu4.0_amd64.deb | LiteLLM backend returned empty output. |
| `testing-05` | `recall` | `testing` | `5093.85` | `0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `7676.37` | `0.977` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `10671.09` | `0.942` | `1.000` | `0.856` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `5116.88` | `0.961` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `9084.11` | `0.954` | `1.000` | `0.885` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `7284.25` | `0.985` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `11000.68` | `0.906` | `1.000` | `0.848` | `1.000` | `0.933` | `0.778` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `12281.54` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | error, index.js | LiteLLM backend returned empty output. |
| `testing-06` | `instruction_following` | `testing` | `18828.90` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ERROR:, * rerun pytest test_auth.py::TestAuth::test_login | LiteLLM backend returned empty output. |
| `ci-05` | `instruction_following` | `ci` | `12650.09` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | ERROR: failed to fetch, 404  Not Found | LiteLLM backend returned empty output. |
| `linting-02` | `structured` | `linting` | `9663.92` | `0.832` | `1.000` | `0.837` | `0.786` | `0.707` | `0.667` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `9590.89` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `12089.42` | `0.870` | `1.000` | `0.635` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `5001.78` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `3418.81` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `3795.95` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `2985.80` | `0.232` | `1.000` | `0.320` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `7121.15` | `0.483` | `1.000` | `0.497` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `build-05` | `exact_format` | `build` | `10122.55` | `0.233` | `1.000` | `0.333` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `8643.94` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `12098.02` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | No module named 'requests' | LiteLLM backend returned empty output. |
| `runtime-04` | `explanation` | `runtime` | `10380.45` | `0.939` | `1.000` | `0.890` | `1.000` | `0.981` | `0.938` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `10676.64` | `0.948` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `7471.23` | `0.970` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `10871.36` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | nil pointer dereference, SIGSEGV | LiteLLM backend returned empty output. |
| `runtime-06` | `explanation` | `runtime` | `5730.86` | `0.943` | `1.000` | `0.908` | `1.000` | `0.968` | `0.895` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `14334.72` | `0.914` | `1.000` | `0.895` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `11997.44` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | Cannot find module 'react' | LiteLLM backend returned empty output. |
| `explanation-02` | `explanation` | `explanation` | `10247.81` | `0.899` | `1.000` | `0.876` | `1.000` | `0.883` | `0.611` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `13129.77` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | no configured push destination | LiteLLM backend returned empty output. |
| `explanation-04` | `explanation` | `explanation` | `11657.43` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | exited with 1 | LiteLLM backend returned empty output. |
| `explanation-05` | `explanation` | `explanation` | `11436.71` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | command not found | LiteLLM backend returned empty output. |
| `explanation-06` | `explanation` | `explanation` | `8196.88` | `0.867` | `1.000` | `0.845` | `1.000` | `0.833` | `0.444` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `11362.45` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | SECRET_KEY setting must not be empty | LiteLLM backend returned empty output. |
| `explanation-08` | `explanation` | `explanation` | `17116.47` | `0.901` | `1.000` | `0.893` | `1.000` | `0.864` | `0.545` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `21407.35` | `0.920` | `1.000` | `0.921` | `1.000` | `0.878` | `0.593` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `6108.58` | `0.902` | `1.000` | `0.900` | `1.000` | `0.857` | `0.524` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `8001.54` | `0.929` | `1.000` | `0.915` | `1.000` | `0.914` | `0.714` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `5525.58` | `0.946` | `1.000` | `0.906` | `1.000` | `0.980` | `0.933` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `9915.65` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `6625.40` | `0.925` | `1.000` | `0.817` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `9584.90` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `4889.15` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `4723.82` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `5380.07` | `0.483` | `1.000` | `0.497` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `4443.58` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `2763.40` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `8565.16` | `0.231` | `1.000` | `0.646` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `8907.81` | `0.933` | `1.000` | `0.904` | `1.000` | `0.944` | `0.812` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `18812.48` | `0.932` | `1.000` | `0.887` | `1.000` | `0.965` | `0.882` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `9751.30` | `0.905` | `1.000` | `0.881` | `1.000` | `0.894` | `0.647` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `10025.00` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | cannot list resource "pods" | LiteLLM backend returned empty output. |
| `explanation-14` | `explanation` | `explanation` | `8885.21` | `0.897` | `1.000` | `0.915` | `1.000` | `0.820` | `0.400` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `8278.85` | `0.974` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `7185.85` | `0.920` | `1.000` | `0.883` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `9629.00` | `0.978` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `6421.99` | `0.915` | `1.000` | `0.870` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
