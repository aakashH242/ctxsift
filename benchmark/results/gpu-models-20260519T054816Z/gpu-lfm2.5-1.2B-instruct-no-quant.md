# gpu-lfm2.5-1.2B-instruct-no-quant

## Scenario

- track: `gpu`
- phase: `gpu-screen`
- model: `LiquidAI/LFM2.5-1.2B-Instruct`
- quantization: `none`
- device: `cuda`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `237300.02`
- cpu_rss_bytes: `1778069504`
- gpu_peak_bytes: `2399064576`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `268`
- accepted_count: `120`
- soft_accepted_count: `148`
- rejected_count: `12`
- exact_pass_count: `123`
- avg_inference_ms: `1940.67`
- p95_inference_ms: `5185.39`
- avg_exact_preservation_ratio: `0.675`
- avg_summary_quality_ratio: `0.821`
- avg_format_adherence_score: `0.792`
- avg_instruction_following_score: `0.786`
- avg_brevity_ratio: `0.933`
- avg_case_score: `0.684`
- p10_case_score: `0.337`
- quality_core: `0.614`
- latency_factor: `1.000`
- final_score: `61.45`
- peak_cpu_rss_bytes: `1781047296`
- peak_gpu_bytes: `2677278720`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `6713.13` | `0.704` | `0.667` | `0.911` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /workspace/app/config.py, line 18 column 3 | - |
| `python-02` | `summary` | `python` | `3581.83` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass="- ModuleNotFoundError: No module named 'dramatiq_abort' - worker boot failed<|im_end|>" repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='python services/worker.py --queue emails --concurrency 4 /workspace/services/worker.py line 11 ModuleNotFoundError dramatiq_abort worker boot failed<|im_end|>' |
| `python-03` | `recall` | `python` | `4713.95` | `0.702` | `0.655` | `0.927` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ./scripts/run-local-api.sh, Worker failed to boot. | - |
| `python-04` | `recall` | `python` | `3989.35` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `2981.43` | `0.595` | `0.407` | `0.868` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | python tools/export_report.py --input data/may.csv --format parquet, /workspace/src/reports/export.py, data/may.csv | - |
| `pytest-01` | `recall` | `pytest` | `4969.53` | `0.450` | `0.000` | `0.919` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/api/test_users.py -q, tests/api/test_users.py::test_create_user_rejects_duplicate[email], tests/api/test_users.py:47, AssertionError, 500 == 409 | - |
| `pytest-02` | `summary` | `pytest` | `6040.72` | `0.749` | `0.605` | `0.951` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /workspace/tests/integration/test_billing_api.py:73, 1 error in 2.31s | - |
| `pytest-03` | `recall` | `pytest` | `6905.28` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | pytest tests -q -x, tests/jobs/test_retention.py::test_archive_marks_job_deleted, teardown, psycopg.errors.ForeignKeyViolation, job_runs_job_id_fkey, 149 passed, 1 skipped, 1 error in 58.73s | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='149 passed, 1 skipped, 1 error in 58.73s ERROR: ForeignKeyViolation – update or delete on table "jobs" violates foreign key constraint "job_runs_job_id_fkey"...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='pytest tests -q -x tests/jobs/test_retention.py::test_archive_marks_job_deleted teardown psycopg.errors.ForeignKeyViolation job_runs_job_id_fkey 149 passed 1...' |
| `pytest-04` | `recall` | `pytest` | `4432.14` | `0.710` | `0.650` | `0.971` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /workspace/tests/cli/test_export.py:12, pytest.mark.slowdb | - |
| `pytest-05` | `summary` | `pytest` | `2244.36` | `0.636` | `0.235` | `0.849` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/unit tests/integration --disable-warnings=0, tests/unit/test_stripe_client.py, src/billing/client.py:9, 1 error during collection | - |
| `mypy-01` | `recall` | `mypy` | `5016.79` | `0.596` | `0.366` | `0.947` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mypy src/accounts/user_service.py --show-error-codes, src/accounts/user_service.py:84, attr-defined | - |
| `mypy-02` | `summary` | `mypy` | `6352.06` | `0.723` | `0.579` | `0.909` | `1.000` | `0.984` | `0.946` | `soft_accepted` | missing_exact_anchors | mypy src tests --pretty --show-error-codes, arg-type | - |
| `mypy-03` | `recall` | `mypy` | `5462.61` | `0.519` | `0.182` | `0.914` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mypy src/orders/normalize.py --show-error-codes --strict, src/orders/normalize.py:41, union-attr, type: ignore | - |
| `ruff-01` | `summary` | `ruff` | `6266.36` | `0.763` | `0.667` | `0.951` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Client, all, Found 1 error. | - |
| `ruff-02` | `summary` | `ruff` | `3171.15` | `0.813` | `0.867` | `0.975` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 52 files already formatted | - |
| `ruff-03` | `summary` | `ruff` | `5128.28` | `0.813` | `0.902` | `0.952` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | except | - |
| `pylint-01` | `recall` | `pylint` | `2223.95` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `4378.32` | `0.683` | `0.614` | `0.910` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pylint src/config/runtime.py src/api/server.py, expected ":" | - |
| `pylint-03` | `summary` | `pylint` | `3488.20` | `0.987` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `4124.71` | `0.788` | `0.800` | `0.942` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 2 files would be reformatted, 41 files would be left unchanged | - |
| `black-02` | `summary` | `black` | `3324.31` | `0.715` | `0.532` | `0.895` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | black src, /workspace/src/config/schema.py | - |
| `black-03` | `recall` | `black` | `2661.24` | `0.997` | `1.000` | `0.986` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `6456.21` | `0.803` | `0.905` | `0.950` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | package-lock.json | - |
| `npm-02` | `summary` | `npm` | `2596.32` | `0.810` | `0.889` | `0.953` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | peer react@"^17.0.0" | - |
| `npm-03` | `summary` | `npm` | `4446.90` | `0.763` | `0.691` | `0.938` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Lifecycle script `build` failed, /workspace | - |
| `pnpm-01` | `recall` | `pnpm` | `1087.71` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `877.60` | `0.991` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `1290.64` | `0.823` | `0.905` | `0.980` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | health route > returns build metadata when git sha is present | - |
| `typescript-01` | `summary` | `typescript` | `1488.09` | `0.713` | `0.467` | `0.930` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tsc -p tsconfig.json --noEmit, src/server/index.ts(3,18), src/server/index.ts(4,18) | - |
| `typescript-02` | `recall` | `typescript` | `1356.89` | `0.798` | `0.895` | `0.947` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Watching for file changes | - |
| `typescript-03` | `summary` | `typescript` | `996.47` | `0.637` | `0.308` | `0.806` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tsc src/index.ts src/http.ts --pretty false, src/index.ts(48,20), RequestInit, src/http.ts(9,17) | - |
| `eslint-01` | `recall` | `eslint` | `1081.47` | `0.731` | `0.720` | `0.943` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Unused eslint-disable directive, 3 problems (2 errors, 1 warning) | - |
| `eslint-02` | `summary` | `eslint` | `1327.25` | `0.787` | `0.773` | `0.956` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ESLint: 9.14.0 | - |
| `eslint-03` | `recall` | `eslint` | `1623.65` | `0.761` | `0.808` | `0.929` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | react-hooks/exhaustive-deps | - |
| `docker-01` | `recall` | `docker` | `683.27` | `0.442` | `0.000` | `0.881` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker build -t api:dev ., COPY docker/entrypoint.sh /entrypoint.sh, /docker/entrypoint.sh, Dockerfile:14, failed to solve | - |
| `docker-02` | `summary` | `docker` | `341.15` | `0.990` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `844.93` | `0.572` | `0.000` | `0.806` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker build -f docker/web.Dockerfile -t web:ci ., RUN npm ci, ERESOLVE, react-dates@21.8.0, react@18.2.0, exit code: 1 | - |
| `docker-compose-01` | `summary` | `docker-compose` | `286.98` | `0.977` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `952.26` | `0.506` | `0.125` | `0.955` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker compose up --build, demo-app-1, sqlalchemy.exc.ProgrammingError, app-1 exited with code 1 | - |
| `docker-compose-03` | `summary` | `docker-compose` | `591.80` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `1298.68` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `1572.07` | `0.997` | `1.000` | `0.987` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `769.59` | `0.721` | `0.556` | `0.898` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | kubectl wait --for=condition=Available deployment/worker -n jobs --timeout=90s, timed out waiting for the condition | - |
| `kubectl-04` | `recall` | `kubectl` | `1546.00` | `0.682` | `0.619` | `0.896` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | kubectl logs payments-worker-6f8f7d4df5-z5vsm -c worker --previous -n payments, payments-worker-6f8f7d4df5-z5vsm | - |
| `terraform-01` | `summary` | `terraform` | `1266.18` | `0.761` | `0.647` | `0.957` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform validate | - |
| `terraform-02` | `recall` | `terraform` | `986.16` | `0.630` | `0.474` | `0.942` | `1.000` | `0.979` | `0.931` | `soft_accepted` | missing_exact_anchors | terraform plan, aws_security_group.db.id, Reference to undeclared resource | - |
| `terraform-03` | `recall` | `terraform` | `1143.52` | `0.995` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `1238.04` | `0.641` | `0.098` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform test, run "plan_defaults", tests/aws.tftest.hcl line 18, Test assertion failed, aws_instance.web.instance_type | - |
| `mixed-01` | `recall` | `mixed` | `1285.01` | `0.782` | `0.837` | `0.972` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | rsync warning | - |
| `mixed-02` | `summary` | `mixed` | `1065.35` | `0.718` | `0.486` | `0.932` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | make integration, Error 2 | - |
| `git-01` | `recall` | `git` | `1244.24` | `0.976` | `1.000` | `0.902` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `727.62` | `0.663` | `0.556` | `0.922` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | git push origin main | - |
| `git-03` | `recall` | `git` | `969.43` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `1766.74` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `1124.98` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | curl -I https://docs.example.com/sdk/latest, HTTP/2 301, location: /sdk/v3.4/, cache-control: max-age=3600 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='curl -I https://docs.example.com/sdk/latest HTTP/2 301 location: /sdk/v3.4/ cache-control: max-age=3600<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='curl -I https://docs.example.com/sdk/latest HTTP/2 301 location: /sdk/v3.4/ cache-control: max-age=3600<|im_end|>' |
| `ssh-01` | `summary` | `ssh` | `1063.79` | `0.646` | `0.238` | `0.876` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | GIT_SSH_COMMAND="ssh -o IdentitiesOnly=yes -i ~/.ssh/deploy_key" git ls-remote git@github.com:example/mono-app.git, fatal: Could not read from remote repository., git@github.com:example/mono-app.git | - |
| `ssh-02` | `summary` | `ssh` | `1615.84` | `0.787` | `0.788` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Host key verification failed. | - |
| `systemd-01` | `summary` | `systemd` | `741.04` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `679.15` | `0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `844.54` | `0.614` | `0.143` | `0.841` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | sudo apt-get install libpq-dev postgresql-client, libpq-dev, libpq5, postgresql-client-16 | - |
| `dnf-01` | `recall` | `dnf` | `886.24` | `0.420` | `0.000` | `0.778` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | sudo dnf install python3-devel postgresql-devel, conflicting requests, python3.12-devel, python3.12-3.12.0-1.el9.x86_64, python3.12-3.12.2-2.el9.x86_64 | - |
| `go-build-01` | `summary` | `go-build` | `964.41` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `947.44` | `0.745` | `0.600` | `0.943` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | go test ./... -run TestCacheTTL -count=1 | - |
| `javac-01` | `summary` | `javac` | `1025.55` | `0.618` | `0.133` | `0.858` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | javac -d out $(find src/main/java -name '*.java'), src/main/java/com/example/app/cli/RunCommand.java:18, cannot find symbol | - |
| `maven-01` | `summary` | `maven` | `1327.67` | `0.686` | `0.348` | `0.925` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | UserControllerTest.java:72, maven-surefire-plugin:3.5.5:test, /workspace/webapp/target/surefire-reports | - |
| `maven-02` | `summary` | `maven` | `1297.04` | `0.592` | `0.000` | `0.867` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mvn -U -DskipTests package, org.postgresql:postgresql:jar:42.7.3, Failed to execute goal on project ingest-service, Could not resolve dependencies | - |
| `gradle-01` | `recall` | `gradle` | `1280.69` | `0.660` | `0.524` | `0.961` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | :service:compileJava, :service:compileClasspath | - |
| `gradle-02` | `summary` | `gradle` | `910.13` | `0.748` | `0.667` | `0.910` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ./gradlew test | - |
| `cargo-01` | `summary` | `cargo` | `1423.45` | `0.699` | `0.424` | `0.914` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | cargo build, error[E0308] | - |
| `cargo-02` | `summary` | `cargo` | `836.24` | `0.802` | `0.833` | `0.962` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | rand = "^0.9.0" | - |
| `node-runtime-01` | `recall` | `node-runtime` | `1112.83` | `0.662` | `0.526` | `0.967` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Cannot find module './env/schema', MODULE_NOT_FOUND | - |
| `npm-04` | `summary` | `npm` | `1043.67` | `0.984` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `1014.22` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `1496.92` | `0.976` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `1207.19` | `0.743` | `0.600` | `0.934` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /workspace/app/loader.py, line 52 | - |
| `pytest-06` | `summary` | `pytest` | `899.57` | `0.637` | `0.133` | `0.915` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/api/test_auth.py -k login -q, tests/api/test_auth.py:88, assert 200 == 429 | - |
| `mypy-04` | `summary` | `mypy` | `1412.78` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `903.95` | `0.624` | `0.089` | `0.906` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund, Dockerfile:8, failed to solve | - |
| `docker-compose-04` | `summary` | `docker-compose` | `2509.93` | `0.805` | `0.867` | `0.951` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | port is already allocated | - |
| `kubectl-05` | `summary` | `kubectl` | `2066.27` | `0.982` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `4249.38` | `0.708` | `0.529` | `0.876` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | kubectl describe pod web-7f6f6d9d7b-kj4t2 -n dev, migrate | - |
| `kubectl-07` | `recall` | `kubectl` | `2816.45` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `6126.46` | `0.616` | `0.424` | `0.933` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform plan -lock-timeout=5s -out=tfplan, Error acquiring the state lock | - |
| `terraform-06` | `summary` | `terraform` | `5216.15` | `0.802` | `0.867` | `0.941` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Reference to undeclared resource | - |
| `terraform-07` | `summary` | `terraform` | `3258.28` | `0.598` | `0.000` | `0.884` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform plan -detailed-exitcode -no-color, Plan: 1 to add, 1 to change, 0 to destroy., 2, aws_security_group_rule.web_https | - |
| `nginx-01` | `summary` | `nginx` | `2616.00` | `0.752` | `0.611` | `0.955` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "server" directive is not allowed here, configuration file /etc/nginx/nginx.conf test failed | - |
| `nginx-02` | `summary` | `nginx` | `3883.65` | `0.749` | `0.611` | `0.946` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | cannot load certificate, configuration file /etc/nginx/nginx.conf test failed | - |
| `postgres-01` | `recall` | `postgres` | `2328.57` | `0.471` | `0.133` | `0.921` | `1.000` | `0.893` | `0.643` | `soft_accepted` | missing_exact_anchors | psql -h 127.0.0.1 -U app_user -d appdb -c 'select 1', FATAL:, role "app_user" does not exist | - |
| `postgres-02` | `summary` | `postgres` | `2570.77` | `0.772` | `0.706` | `0.956` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | migrations/202605160830_add_users.sql:42 | - |
| `mysql-01` | `summary` | `mysql` | `3193.14` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `3367.04` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `3352.88` | `0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `1863.02` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `4784.31` | `0.593` | `0.619` | `0.878` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors | line=91, Ruff F821 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `1295.26` | `0.979` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `253.33` | `0.966` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `1125.74` | `0.690` | `0.326` | `0.950` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | make CFLAGS='-O2 -Wall -Werror' all, Makefile:22, Error 1 | - |
| `tar-01` | `summary` | `tar` | `1359.08` | `0.977` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `1178.71` | `0.494` | `0.167` | `0.824` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ansible-playbook -i inventories/prod/hosts.ini deploy.yml --limit proxy, UNREACHABLE!, Connection timed out | - |
| `rsync-01` | `summary` | `rsync` | `926.98` | `0.762` | `0.667` | `0.949` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | runtime-1a2b3c.js, some files vanished before they could be transferred | - |
| `test-failure-01` | `recall` | `test-failure` | `745.97` | `0.399` | `0.000` | `0.676` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/unit/test_invoice_totals.py::test_discount_rounding, tests/unit/test_invoice_totals.py:88, Decimal('17.50'), Decimal('17.49'), ROUND_HALF_UP is deprecated for discounts; use ROUND_HALF_EVEN | - |
| `compiler-error-01` | `recall` | `compiler-error` | `1655.62` | `0.555` | `0.299` | `0.875` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | error[E0382], src/router.rs:128, req.into_body(), req.method(), req.clone().into_body() | - |
| `ci-log-01` | `recall` | `ci-log` | `1959.70` | `0.440` | `0.000` | `0.869` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | helm upgrade --install payments-api charts/payments-api --namespace prod-payments, Deployment.apps "payments-api" is invalid, spec.template.spec.containers[0].env[3].valueFrom.secretKeyRef.name, Invalid value: "", deployments.apps "payments-api" not found | - |
| `package-manager-01` | `recall` | `package-manager` | `5602.17` | `0.728` | `0.704` | `0.960` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm ERR! code ERESOLVE, peer vite@"^4.0.0 || ^5.0.0" | - |
| `test-summary-01` | `summary` | `test-summary` | `2201.63` | `0.585` | `0.000` | `0.845` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | github.com/acme/shop/checkout, TestCheckoutAppliesStoreCredit, checkout_test.go:71, total = 42.00, want 37.00, github.com/acme/shop/inventory, TestReconcileInventory, test timed out after 10m0s, worker.go:144 | - |
| `build-log-01` | `summary` | `build-log` | `3728.43` | `0.637` | `0.125` | `0.920` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | billing-service, InvoiceMapper.java:[58,29], setTaxCode(java.lang.String), InvoiceDto | - |
| `docker-build-02` | `summary` | `docker-build` | `1258.87` | `0.570` | `0.000` | `0.802` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Dockerfile:18, COPY apps/web ./apps/web, "/apps/web": not found | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `8494.37` | `0.379` | `1.000` | `0.708` | `0.000` | `0.000` | `0.333` | `soft_accepted` | structured_output_mismatch | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `4417.07` | `0.721` | `1.000` | `0.736` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `3341.85` | `0.287` | `0.129` | `0.705` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | search endpoint failed after 2 attempts, https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `6477.27` | `0.408` | `0.778` | `0.813` | `0.000` | `0.000` | `0.806` | `soft_accepted` | missing_exact_anchors | reportArgumentType, reportUndefinedVariable | - |
| `structured-output-02` | `structured` | `structured-output` | `7120.05` | `0.356` | `1.000` | `0.186` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-03` | `structured` | `structured-output` | `5108.62` | `0.285` | `0.821` | `0.236` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/auth/session.test.ts | - |
| `structured-output-04` | `structured` | `structured-output` | `8132.20` | `0.594` | `1.000` | `0.979` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `3012.09` | `0.200` | `1.000` | `0.338` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `4584.51` | `0.081` | `0.286` | `0.310` | `0.000` | `0.000` | `0.429` | `soft_accepted` | missing_exact_anchors | packages/web/src/search/searchBox.test.tsx | - |
| `exact-format-03` | `exact_format` | `exact-format` | `4182.06` | `0.190` | `1.000` | `0.333` | `0.000` | `0.000` | `0.125` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `2400.34` | `0.715` | `0.556` | `0.861` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | has no attribute 'dumps', shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `1994.43` | `0.915` | `1.000` | `0.831` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `4162.58` | `0.578` | `0.750` | `0.861` | `0.000` | `0.000` | `1.000` | `soft_accepted` | structured_output_mismatch | customer_id | - |
| `python-traceback-01` | `recall` | `python-traceback` | `2772.02` | `0.569` | `0.333` | `0.889` | `1.000` | `0.990` | `0.968` | `soft_accepted` | missing_exact_anchors | app.tasks.email.send_welcome_email, line 92, [bad@example.test](mailto:bad@example.test), retries exhausted for queue emails | - |
| `mypy-05` | `recall` | `mypy` | `4171.76` | `0.786` | `0.867` | `0.939` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Signature of "serialize" incompatible with supertype "BaseExporter" | - |
| `terraform-08` | `recall` | `terraform` | `5664.99` | `0.584` | `0.333` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | module.worker.aws_iam_policy.worker_inline, EntityAlreadyExists, status code: 409, request id: 0f3e2b11-9ac9-4fd2-a3bb-6c07a3c6a90d | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `3199.31` | `0.583` | `0.348` | `0.916` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | InventorySyncTest > publishesBackorderEvent() FAILED, InventorySyncTest.java:132, OrderServiceTest > calculatesDiscountForGoldCustomer() PASSED | - |
| `kubernetes-01` | `recall` | `kubernetes` | `2641.19` | `0.570` | `0.320` | `0.908` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | api-7d9f8c8b99-mx2kq, registry.example.com/api:2026.05.18-1, Exit Code: 78, FATAL config: required env STRIPE_KEY is empty | - |
| `go-test-02` | `recall` | `go-test` | `3580.58` | `0.546` | `0.259` | `0.904` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | (*Store).Set(), /work/internal/cache/store.go:88, (*Store).Get(), /work/internal/cache/store.go:54 | - |
| `cargo-03` | `recall` | `cargo` | `2166.76` | `0.469` | `0.103` | `0.824` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | error[E0432], crates/storage/src/events.rs:7:5, tokio_stream::wrappers, gated behind the `sync` feature, could not compile `storage` | - |
| `docker-compose-05` | `recall` | `docker-compose` | `2885.51` | `0.668` | `0.550` | `0.956` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | container app-api-1 is unhealthy, dependency failed to start, migration failed; exiting | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `2194.34` | `0.629` | `0.464` | `0.923` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | packages/api/src/index.ts:4:25, /repo/packages/contracts/dist/index.d.ts, packages/contracts/src/index.ts | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `1783.54` | `0.478` | `0.095` | `0.878` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | packages/db migrate.test.ts, 20260518_add_workspace_limits.sql, relation "workspace_limits" already exists, packages/db/src/migrate.ts:77:13, packages/db/test/migrate.test.ts:44:7 | - |
| `pnpm-04` | `recall` | `pnpm` | `2668.76` | `0.763` | `0.789` | `0.967` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERR_PNPM_OUTDATED_LOCKFILE | - |
| `swift-01` | `recall` | `swift` | `3135.06` | `0.528` | `0.256` | `0.822` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | UserDecoderTests testMissingAvatarUsesPlaceholder, Tests/UserDecoderTests.swift:47, Optional(placeholder.png), fatalError | - |
| `elixir-01` | `recall` | `elixir` | `2946.44` | `0.633` | `0.478` | `0.920` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | lib/my_app/cache_worker.ex:63, test/my_app/cache_worker_test.exs:29, refreshes expired keys | - |
| `rails-01` | `recall` | `rails` | `1477.85` | `0.533` | `0.235` | `0.885` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 20260518093012 AddIndexToEventsRequestId, index_events_on_request_id, 20260518093012_add_index_to_events_request_id.rb:3, ArgumentError | - |
| `phpunit-01` | `recall` | `phpunit` | `2460.16` | `0.501` | `0.213` | `0.775` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Tests\Billing\InvoiceTotalTest::testAppliesCreditBeforeTax, Failed asserting that '88.00' is identical to '86.40', /tests/Billing/InvoiceTotalTest.php:52, Failures: 1 | - |
| `nginx-03` | `recall` | `nginx` | `2228.23` | `0.456` | `0.000` | `0.944` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | nginx -t -c /etc/nginx/nginx.conf, duplicate location "/api", /etc/nginx/conf.d/api.conf:22, configuration file /etc/nginx/nginx.conf test failed | - |
| `postgres-03` | `recall` | `postgres` | `1780.74` | `0.438` | `0.000` | `0.862` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | psql:dump.sql:418, type "vector" does not exist, embedding vector(1536), current transaction is aborted, ROLLBACK | - |
| `ansible-02` | `recall` | `ansible` | `3055.45` | `0.986` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `3768.24` | `0.499` | `0.167` | `0.850` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | //services/reporting:report_parser_test, Opening and ending tag mismatch: total line 18 and totals, services/reporting/parser.py", line 141, etree.fromstring(xml_bytes) | - |
| `powershell-01` | `recall` | `powershell` | `2897.64` | `0.719` | `0.688` | `0.945` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | FullyQualifiedErrorId : UnauthorizedAccess | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `2067.13` | `0.637` | `0.471` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Authentication credentials were not provided, http status: 401, exit code 1 | - |
| `python-pytest-01` | `summary` | `python-pytest` | `2274.60` | `0.770` | `0.783` | `0.901` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/refunds | - |
| `go-test-03` | `summary` | `go-test` | `1567.01` | `0.610` | `0.105` | `0.854` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ./integration, TestWebhookReplay, github.com/acme/api/internal/webhook, Dispatcher, dispatch | - |
| `npm-05` | `summary` | `npm` | `1821.64` | `0.611` | `0.133` | `0.838` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | web@1.2.0, src/pages/admin.tsx, TS2339, Property | - |
| `helm-01` | `summary` | `helm` | `873.24` | `0.624` | `0.125` | `0.883` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | api/templates/deployment.yaml:42:29, executing, api/templates/deployment.yaml, Values.image.repository | - |
| `ruff-04` | `summary` | `ruff` | `4029.98` | `0.653` | `0.211` | `0.913` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | app/api/routes.py:3:1, app/services/user.py:88:89, tests/test_user.py:12:1 | - |
| `k6-01` | `summary` | `k6` | `2372.11` | `0.960` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `1371.43` | `0.579` | `0.000` | `0.828` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | composer, install, --no-dev, Loading, composer | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `2231.99` | `0.584` | `0.000` | `0.843` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | xcodebuild, -scheme, MobileApp, -configuration, Release | - |
| `make-02` | `summary` | `make` | `761.05` | `0.641` | `0.227` | `0.867` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | -Iinclude, src/server.c, build/server.o, src/server.c:14:10 | - |
| `python-pytest-02` | `summary` | `python-pytest` | `431.31` | `0.592` | `0.000` | `0.866` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | auto, tests/e2e, Not, properly, terminated | - |
| `jest-01` | `summary` | `jest` | `580.62` | `0.766` | `0.889` | `0.822` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | matches | - |
| `dbt-01` | `summary` | `dbt` | `614.66` | `0.778` | `0.833` | `0.892` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `578.40` | `0.650` | `0.186` | `0.920` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/test_signup.py, tests/test_signup.py::test_signup_is_idempotent, sqlalchemy.exc.IntegrityError, psycopg.errors.UniqueViolation | - |
| `wrangler-01` | `summary` | `wrangler` | `958.75` | `0.954` | `1.000` | `0.886` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `506.37` | `0.778` | `0.778` | `0.927` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Falsifying, example | - |
| `eslint-05` | `instruction_following` | `eslint` | `2707.24` | `0.342` | `0.815` | `0.672` | `0.000` | `0.000` | `0.381` | `soft_accepted` | missing_exact_anchors | src/App.tsx | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `952.78` | `0.642` | `0.706` | `0.825` | `0.667` | `0.667` | `1.000` | `soft_accepted` | missing_exact_anchors | infra/terraform/iam.tf | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `592.91` | `0.429` | `1.000` | `0.708` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `1325.64` | `0.642` | `1.000` | `0.694` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `430.56` | `0.916` | `1.000` | `0.719` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `925.87` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `1282.78` | `0.430` | `0.800` | `0.820` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERR_PNPM_LOCKFILE_CONFIG_MISMATCH | - |
| `terraform-09` | `instruction_following` | `terraform` | `1277.19` | `0.641` | `1.000` | `0.692` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `1256.02` | `0.823` | `1.000` | `0.855` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `421.23` | `0.715` | `1.000` | `0.715` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `210.29` | `0.596` | `1.000` | `0.985` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `570.09` | `0.435` | `1.000` | `0.708` | `0.000` | `0.000` | `0.222` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `1327.78` | `0.599` | `0.833` | `0.792` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors | Option::unwrap() | - |
| `shell-01` | `instruction_following` | `shell` | `489.06` | `0.378` | `0.643` | `0.719` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Permission denied (13) | - |
| `pyright-01` | `structured` | `pyright` | `2045.53` | `0.245` | `0.667` | `0.185` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /repo/app/user.py | - |
| `terraform-10` | `structured` | `terraform` | `1409.28` | `0.404` | `0.833` | `0.738` | `0.000` | `0.000` | `0.875` | `soft_accepted` | missing_exact_anchors | field | - |
| `junit-01` | `structured` | `junit` | `2571.07` | `0.428` | `0.857` | `0.925` | `0.000` | `0.000` | `0.542` | `soft_accepted` | missing_exact_anchors | CalculatorTest | - |
| `kubernetes-03` | `structured` | `kubernetes` | `1443.57` | `0.282` | `1.000` | `0.188` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `2826.95` | `0.406` | `0.889` | `0.409` | `0.391` | `0.298` | `0.208` | `soft_accepted` | missing_exact_anchors | no-unused-vars | - |
| `docker-build-04` | `structured` | `docker-build` | `910.16` | `0.702` | `1.000` | `0.684` | `0.548` | `0.511` | `0.778` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `1243.10` | `0.550` | `1.000` | `0.905` | `0.000` | `0.000` | `0.786` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `1163.50` | `0.570` | `1.000` | `0.466` | `0.500` | `0.395` | `0.300` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `1563.45` | `0.486` | `0.833` | `0.433` | `0.611` | `0.484` | `0.308` | `soft_accepted` | missing_exact_anchors | required | - |
| `mypy-06` | `structured` | `mypy` | `1229.09` | `0.526` | `1.000` | `0.857` | `0.000` | `0.000` | `0.692` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `1578.33` | `0.254` | `0.697` | `0.189` | `0.083` | `0.076` | `0.700` | `soft_accepted` | missing_exact_anchors | :api:compileJava | - |
| `playwright-02` | `structured` | `playwright` | `935.81` | `0.353` | `1.000` | `0.177` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `994.82` | `0.550` | `1.000` | `0.905` | `0.000` | `0.000` | `0.789` | `accepted` | - | - | - |
| `vite-01` | `structured` | `vite` | `1793.40` | `0.595` | `1.000` | `0.982` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `1379.56` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | tests/test_a.py::test_one, tests/test_b.py::TestB::test_three | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='FAILED tests/test_a.py::test_one - AssertionError; PASSED tests/test_a.py::test_two; FAILED tests/test_b.py::TestB::test_three - TimeoutError<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='FAILED tests/test_a.py::test_one - AssertionError; PASSED tests/test_a.py::test_two; FAILED tests/test_b.py::TestB::test_three - TimeoutError<|im_end|>' |
| `git-04` | `exact_format` | `git` | `1158.52` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass="Merge made by the 'ort' strategy commit 9f4c2d7a1b8e3c6d0a1234567890abcdef123456<|im_end|>" repair_status=rejected repair_flags=['control_token_leakage'] repair_pass="Merge made by the 'ort' strategy commit 9f4c2d7a1b8e3c6d0a1234567890abcdef123456<|im_end|>" |
| `docker-04` | `exact_format` | `docker` | `2529.64` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='pushed ghcr.io/acme/api:2026.05.18 digest sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 verified ghcr.io/acme/api@sha256:aaaaaaaa11...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='pushed ghcr.io/acme/api:2026.05.18 digest sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 verified ghcr.io/acme/api@sha256:aaaaaaaa11...' |
| `npm-08` | `exact_format` | `npm` | `191.16` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 2.18.4 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='2.18.4<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='2.18.4<|im_end|>' |
| `go-test-05` | `exact_format` | `go-test` | `667.56` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | github.com/acme/shop/checkout, TestCheckoutAppliesCoupon | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='github.com/acme/shop/checkout TestCheckoutAppliesCoupon 0.31s<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='github.com/acme/shop/checkout TestCheckoutAppliesCoupon<|im_end|>' |
| `kubectl-09` | `exact_format` | `kubectl` | `503.81` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | migrator-v2-9xk, prod | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='migrator-v2-9xk 0/1 Error 0 33m<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='migrator-v2-9xk prod<|im_end|>' |
| `cargo-05` | `exact_format` | `cargo` | `1089.26` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | auth::tests::rejects_expired, billing::tests::rounds_half_even | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='failures: auth::tests::rejects_expired billing::tests::rounds_half_even test result: FAILED. 40 passed; 2 failed<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='failures: auth::tests::rejects_expired billing::tests::rounds_half_even<|im_end|>' |
| `curl-03` | `exact_format` | `curl` | `201.58` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 503 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='503 curl exit code: 0<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='503 Raw output<|im_end|>' |
| `rails-02` | `exact_format` | `rails` | `901.06` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 20260518133742 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='20260518133742 AddTenantIdToUsers: migrating PG::DuplicateColumn: ERROR: column "tenant_id" of relation "users" already exists<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='20260518133742 AddTenantIdToUsers: migrating ===================== -- column already exists<|im_end|>' |
| `python-traceback-02` | `explanation` | `python-traceback` | `305.71` | `0.950` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `994.45` | `0.624` | `0.000` | `0.869` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | string | null, url: string, user.photoUrl | - |
| `postgres-05` | `explanation` | `postgres` | `798.04` | `0.619` | `1.000` | `0.857` | `0.000` | `0.000` | `1.000` | `soft_accepted` | structured_output_mismatch | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `372.09` | `0.949` | `1.000` | `0.898` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `875.09` | `0.965` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `591.00` | `0.688` | `0.750` | `0.719` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | returns a reference | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `887.00` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `860.25` | `0.431` | `0.000` | `0.918` | `1.000` | `0.933` | `0.778` | `soft_accepted` | missing_exact_anchors | main.cpp:10:5, error: 'cout' was not declared in this scope | - |
| `testing-01` | `recall` | `testing` | `2723.14` | `0.649` | `0.643` | `0.908` | `1.000` | `0.843` | `0.476` | `soft_accepted` | missing_exact_anchors | TestCalculator::testDivideByZero | - |
| `testing-02` | `recall` | `testing` | `2251.23` | `0.715` | `0.818` | `0.882` | `1.000` | `0.859` | `0.529` | `soft_accepted` | missing_exact_anchors | Cannot read property 'foo' of undefined | - |
| `package-management-01` | `recall` | `package-management` | `1959.97` | `0.656` | `0.538` | `0.919` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm ERR! code E404 | - |
| `runtime-02` | `recall` | `runtime` | `1703.25` | `0.715` | `0.667` | `0.965` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `2101.07` | `0.974` | `1.000` | `0.932` | `1.000` | `0.973` | `0.909` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `1867.18` | `0.477` | `0.190` | `0.864` | `1.000` | `0.880` | `0.600` | `soft_accepted` | missing_exact_anchors | error[E0277], main.rs:5:26 | - |
| `ci-01` | `recall` | `ci` | `1006.17` | `0.967` | `1.000` | `0.868` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `1054.49` | `0.669` | `0.636` | `0.801` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | no such file or directory | - |
| `deployment-01` | `recall` | `deployment` | `2823.44` | `0.732` | `0.778` | `0.869` | `1.000` | `0.981` | `0.938` | `soft_accepted` | missing_exact_anchors | BadRequest | - |
| `infrastructure-01` | `recall` | `infrastructure` | `2541.37` | `0.751` | `0.778` | `0.934` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "ami" is required | - |
| `compilation-02` | `recall` | `compilation` | `1764.62` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `841.54` | `0.974` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `2854.07` | `0.943` | `1.000` | `0.893` | `1.000` | `0.909` | `0.696` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `622.49` | `0.979` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `832.45` | `0.980` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1200.66` | `0.965` | `1.000` | `0.858` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `1527.87` | `0.930` | `1.000` | `0.862` | `1.000` | `0.893` | `0.643` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `2376.57` | `0.652` | `0.500` | `0.967` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | No matching distribution found | - |
| `infrastructure-03` | `recall` | `infrastructure` | `1667.53` | `0.950` | `1.000` | `0.800` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `1544.77` | `0.775` | `0.833` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | User signs in | - |
| `build-02` | `recall` | `build` | `1887.25` | `0.624` | `0.500` | `0.942` | `1.000` | `0.920` | `0.733` | `soft_accepted` | missing_exact_anchors | error: expected ';' | - |
| `ci-03` | `recall` | `ci` | `3741.22` | `0.837` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `505.88` | `0.976` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `1861.03` | `0.914` | `1.000` | `0.878` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `798.86` | `0.945` | `1.000` | `0.862` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `321.65` | `0.955` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `872.03` | `0.953` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `1165.91` | `0.676` | `0.667` | `0.884` | `1.000` | `0.850` | `0.500` | `soft_accepted` | missing_exact_anchors | unable to resolve dependency tree | - |
| `rust-02` | `summary` | `rust` | `596.75` | `0.936` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `2547.25` | `0.514` | `1.000` | `0.825` | `0.000` | `0.000` | `0.667` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `2649.73` | `0.546` | `1.000` | `0.931` | `0.000` | `0.000` | `0.667` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `3293.93` | `0.674` | `1.000` | `0.829` | `0.500` | `0.387` | `0.250` | `accepted` | - | - | - |
| `linting-02` | `structured` | `linting` | `944.55` | `0.354` | `1.000` | `0.181` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `1972.04` | `0.579` | `1.000` | `0.957` | `0.000` | `0.000` | `0.923` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `1033.17` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `375.95` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `938.33` | `0.220` | `1.000` | `0.579` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `592.62` | `0.252` | `1.000` | `0.765` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `204.19` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `3299.75` | `0.086` | `0.000` | `0.515` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Resources: 1 added, instance_id | - |
| `build-05` | `exact_format` | `build` | `727.16` | `0.198` | `1.000` | `0.309` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `678.06` | `0.232` | `1.000` | `0.658` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `843.46` | `0.947` | `1.000` | `0.894` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `699.95` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `1287.96` | `0.722` | `0.500` | `0.899` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pull access denied | - |
| `runtime-05` | `explanation` | `runtime` | `865.77` | `0.950` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `963.46` | `0.956` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `619.36` | `0.927` | `1.000` | `0.855` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `438.58` | `0.910` | `1.000` | `0.821` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `821.13` | `0.934` | `1.000` | `0.867` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1174.26` | `0.944` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `1162.01` | `0.632` | `0.000` | `0.886` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | no configured push destination | - |
| `explanation-04` | `explanation` | `explanation` | `1101.85` | `0.617` | `0.000` | `0.851` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | exited with 1 | - |
| `explanation-05` | `explanation` | `explanation` | `457.78` | `0.901` | `1.000` | `0.802` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `323.03` | `0.943` | `1.000` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `958.99` | `0.932` | `1.000` | `0.864` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `781.96` | `0.920` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `1987.69` | `0.614` | `0.000` | `0.845` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | would be overwritten by merge | - |
| `explanation-10` | `explanation` | `explanation` | `652.34` | `0.953` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `816.29` | `0.916` | `1.000` | `0.833` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `357.61` | `0.941` | `1.000` | `0.883` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `2056.74` | `0.579` | `1.000` | `0.957` | `0.000` | `0.000` | `0.923` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `902.71` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `537.95` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `575.46` | `0.231` | `1.000` | `0.648` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `255.85` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `2080.58` | `0.086` | `0.000` | `0.515` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Resources: 1 added, instance_id | - |
| `runtime-07` | `exact_format` | `runtime` | `289.03` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `1366.96` | `0.106` | `0.000` | `0.749` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | testError:34 | - |
| `shell-08` | `exact_format` | `shell` | `196.88` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `935.43` | `0.947` | `1.000` | `0.894` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `708.69` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `974.99` | `0.959` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `2052.26` | `0.970` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `541.73` | `0.910` | `1.000` | `0.821` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `808.81` | `0.963` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `674.03` | `0.913` | `1.000` | `0.825` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `775.15` | `0.928` | `1.000` | `0.855` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1354.01` | `0.938` | `1.000` | `0.875` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
