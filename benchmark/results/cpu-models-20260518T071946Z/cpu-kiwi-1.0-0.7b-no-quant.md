# cpu-kiwi-1.0-0.7b-no-quant

## Scenario

- track: `cpu`
- phase: `cpu-screen`
- model: `mradermacher/Kiwi-1.0-0.7B-32k-Instruct-GGUF`
- quantization: `none`
- device: `cpu`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `103453.88`
- cpu_rss_bytes: `null`
- gpu_peak_bytes: `null`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `280`
- accepted_count: `81`
- soft_accepted_count: `199`
- rejected_count: `0`
- exact_pass_count: `89`
- avg_inference_ms: `29103.64`
- p95_inference_ms: `64456.12`
- avg_exact_preservation_ratio: `0.442`
- avg_summary_quality_ratio: `0.714`
- avg_format_adherence_score: `0.736`
- avg_instruction_following_score: `0.688`
- avg_brevity_ratio: `0.636`
- avg_case_score: `0.537`
- p10_case_score: `0.132`
- quality_core: `0.456`
- latency_factor: `0.850`
- final_score: `38.73`
- peak_cpu_rss_bytes: `null`
- peak_gpu_bytes: `null`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `40206.35` | `0.416` | `0.000` | `0.758` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | python -m app.cli sync --config config/settings.json, /workspace/app/config.py, line 27, JSONDecodeError, line 18 column 3, config/settings.json | - |
| `python-02` | `summary` | `python` | `38627.79` | `0.643` | `1.000` | `0.905` | `0.500` | `0.394` | `0.294` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `python-03` | `recall` | `python` | `51387.16` | `0.413` | `0.000` | `0.742` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ./scripts/run-local-api.sh, /workspace/src/api/app.py, line 58, KeyError, JWT_PRIVATE_KEY, Worker failed to boot. | - |
| `python-04` | `recall` | `python` | `22103.09` | `0.403` | `0.000` | `0.694` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | python -m jobs.refresh_catalog --region us-east-1, /workspace/src/jobs/refresh_catalog.py, line 119, httpx.ReadTimeout, catalog?page=2, us-east-1 | - |
| `python-05` | `recall` | `python` | `40462.54` | `0.416` | `0.000` | `0.759` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | python tools/export_report.py --input data/may.csv --format parquet, /workspace/src/reports/export.py, line 131, UnboundLocalError, writer, data/may.csv | - |
| `pytest-01` | `recall` | `pytest` | `25204.26` | `0.522` | `0.364` | `0.916` | `1.000` | `0.763` | `0.211` | `soft_accepted` | missing_exact_anchors | tests/api/test_users.py::test_create_user_rejects_duplicate[email], tests/api/test_users.py:47, AssertionError | - |
| `pytest-02` | `summary` | `pytest` | `79177.51` | `0.882` | `1.000` | `0.929` | `1.000` | `0.821` | `0.404` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `73944.51` | `0.407` | `0.000` | `0.714` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors, verbatim_alignment_weak | pytest tests -q -x, tests/jobs/test_retention.py::test_archive_marks_job_deleted, teardown, psycopg.errors.ForeignKeyViolation, job_runs_job_id_fkey, 149 passed, 1 skipped, 1 error in 58.73s | - |
| `pytest-04` | `recall` | `pytest` | `17250.67` | `0.986` | `1.000` | `0.962` | `1.000` | `0.986` | `0.952` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `16656.80` | `0.541` | `0.000` | `0.717` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/unit tests/integration --disable-warnings=0, tests/unit/test_stripe_client.py, src/billing/client.py:9, ModuleNotFoundError, stripe, 1 error during collection | - |
| `mypy-01` | `recall` | `mypy` | `45873.32` | `0.418` | `0.000` | `0.765` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mypy src/accounts/user_service.py --show-error-codes, src/accounts/user_service.py:84, attr-defined, UserRecord, is_staff, Found 1 error in 1 file | - |
| `mypy-02` | `summary` | `mypy` | `46559.59` | `0.753` | `0.895` | `0.950` | `1.000` | `0.864` | `0.547` | `soft_accepted` | missing_exact_anchors | RetryEvent | - |
| `mypy-03` | `recall` | `mypy` | `45804.92` | `0.683` | `0.773` | `0.943` | `1.000` | `0.759` | `0.197` | `soft_accepted` | missing_exact_anchors | type: ignore | - |
| `ruff-01` | `summary` | `ruff` | `10943.97` | `0.883` | `0.911` | `0.933` | `1.000` | `0.864` | `0.545` | `accepted` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `12260.95` | `0.507` | `0.000` | `0.760` | `1.000` | `0.884` | `0.614` | `soft_accepted` | missing_exact_anchors | ruff format --check src tests, src/api/serializers.py, 1 file would be reformatted, 52 files already formatted | - |
| `ruff-03` | `summary` | `ruff` | `31385.18` | `0.697` | `0.707` | `0.894` | `1.000` | `0.871` | `0.569` | `soft_accepted` | missing_exact_anchors | ruff check src/auth/login.py | - |
| `pylint-01` | `recall` | `pylint` | `8066.47` | `0.409` | `0.000` | `0.724` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pylint src/storage/path_utils.py, src/storage/path_utils.py:27:18, E1101, no-member, mothers, Path | - |
| `pylint-02` | `recall` | `pylint` | `53122.53` | `0.745` | `0.877` | `0.907` | `1.000` | `0.864` | `0.547` | `soft_accepted` | missing_exact_anchors | parse-error | - |
| `pylint-03` | `summary` | `pylint` | `8837.53` | `0.546` | `0.000` | `0.730` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pylint src/notifications/push.py --jobs=0, src/notifications/push.py:6:0, E0401, pywebpush, import-error, --jobs=0 | - |
| `black-01` | `summary` | `black` | `19259.98` | `0.556` | `0.000` | `0.762` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | black --check src tests, /workspace/src/api/routes.py, /workspace/tests/test_routes.py, 2 files would be reformatted, 41 files would be left unchanged | - |
| `black-02` | `summary` | `black` | `17466.29` | `0.569` | `0.000` | `0.798` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | black src, /workspace/src/config/schema.py, Cannot parse, 58:12, 1 file failed to reformat, 1 file reformatted | - |
| `black-03` | `recall` | `black` | `17924.75` | `0.415` | `0.000` | `0.752` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | python -m black --check app.py cli.py, All done!, 2 files would be left unchanged | - |
| `npm-01` | `recall` | `npm` | `27967.42` | `0.689` | `0.714` | `0.914` | `1.000` | `0.880` | `0.600` | `soft_accepted` | missing_exact_anchors | npm ci | - |
| `npm-02` | `summary` | `npm` | `20588.79` | `0.547` | `0.000` | `0.734` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm install, ERESOLVE, react@18.2.0, react-dates@21.8.0, peer react@"^17.0.0", --legacy-peer-deps | - |
| `npm-03` | `summary` | `npm` | `9211.19` | `0.550` | `0.000` | `0.742` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm run build, ./CheckoutButton, src/routes/checkout/index.tsx, Lifecycle script `build` failed, storefront@2.8.1, /workspace | - |
| `pnpm-01` | `recall` | `pnpm` | `8748.41` | `0.413` | `0.000` | `0.742` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pnpm install --frozen-lockfile, ERR_PNPM_OUTDATED_LOCKFILE, pnpm-lock.yaml, packages/web/package.json, --no-frozen-lockfile | - |
| `pnpm-02` | `summary` | `pnpm` | `37458.97` | `0.818` | `0.909` | `0.964` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 5.51.1 | - |
| `pnpm-03` | `summary` | `pnpm` | `24754.17` | `0.581` | `0.095` | `0.773` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pnpm -r test --stream, packages/api, health route > returns build metadata when git sha is present, ERR_PNPM_RECURSIVE_RUN_FIRST_FAIL, api@1.6.0 | - |
| `typescript-01` | `summary` | `typescript` | `13922.79` | `0.749` | `0.667` | `0.912` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tsc -p tsconfig.json --noEmit, TS2307 | - |
| `typescript-02` | `recall` | `typescript` | `30747.48` | `0.899` | `1.000` | `0.916` | `1.000` | `0.760` | `0.199` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `38000.70` | `0.506` | `0.154` | `0.819` | `1.000` | `0.758` | `0.193` | `soft_accepted` | missing_exact_anchors | tsc src/index.ts src/http.ts --pretty false, src/index.ts(48,20), TS2769, RequestInit, src/http.ts(9,17) | - |
| `eslint-01` | `recall` | `eslint` | `26849.91` | `0.938` | `1.000` | `0.933` | `1.000` | `0.862` | `0.542` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `26783.28` | `0.531` | `0.000` | `0.687` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | eslint ., ERR_MODULE_NOT_FOUND, eslint-plugin-react-hooks, /workspace/eslint.config.js, ESLint: 9.14.0 | - |
| `eslint-03` | `recall` | `eslint` | `9482.41` | `0.411` | `0.000` | `0.733` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | eslint src --max-warnings=0, /workspace/src/hooks/useCart.ts, react-hooks/exhaustive-deps, 1 problem (0 errors, 1 warning), maximum: 0 | - |
| `docker-01` | `recall` | `docker` | `27137.17` | `0.414` | `0.000` | `0.748` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker build -t api:dev ., COPY docker/entrypoint.sh /entrypoint.sh, /docker/entrypoint.sh, Dockerfile:14, failed to solve | - |
| `docker-02` | `summary` | `docker` | `7825.22` | `0.984` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `20768.13` | `0.500` | `0.000` | `0.733` | `1.000` | `0.889` | `0.632` | `soft_accepted` | missing_exact_anchors | docker build -f docker/web.Dockerfile -t web:ci ., RUN npm ci, ERESOLVE, react-dates@21.8.0, react@18.2.0, exit code: 1 | - |
| `docker-compose-01` | `summary` | `docker-compose` | `17608.64` | `0.958` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `76638.86` | `0.708` | `0.875` | `0.910` | `1.000` | `0.733` | `0.112` | `soft_accepted` | missing_exact_anchors | demo-app-1 | - |
| `docker-compose-03` | `summary` | `docker-compose` | `24835.45` | `0.862` | `1.000` | `0.904` | `1.000` | `0.801` | `0.337` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `47010.37` | `0.550` | `0.000` | `0.744` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | kubectl apply -f k8s/deployment.yaml --server-side, apps/v1, containers[name="api"].image, kubectl-edit, --force-conflicts | - |
| `kubectl-02` | `recall` | `kubectl` | `33210.20` | `0.909` | `1.000` | `0.947` | `1.000` | `0.767` | `0.224` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `12941.44` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `49016.76` | `0.417` | `0.000` | `0.762` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | kubectl logs payments-worker-6f8f7d4df5-z5vsm -c worker --previous -n payments, payments-worker-6f8f7d4df5-z5vsm, /app/config.yaml, ValueError, invalid worker.concurrency, worker | - |
| `terraform-01` | `summary` | `terraform` | `37460.23` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `19548.80` | `0.730` | `0.737` | `0.908` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | outputs.tf line 14 | - |
| `terraform-03` | `recall` | `terraform` | `9594.19` | `0.409` | `0.000` | `0.727` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform apply, Error acquiring the state lock, v1.7.5, v1.5.7, state snapshot | - |
| `terraform-04` | `summary` | `terraform` | `19964.56` | `0.721` | `0.488` | `0.942` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | run "plan_defaults", tests/aws.tftest.hcl line 18, Test assertion failed | - |
| `mixed-01` | `recall` | `mixed` | `12023.65` | `0.420` | `0.000` | `0.778` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | rsync -av --delete build/ backup/build/, /workspace/build/.cache/tmp-93f1.json, code 24, rsync warning, main.c(1338) | - |
| `mixed-02` | `summary` | `mixed` | `53126.72` | `0.588` | `0.486` | `0.879` | `1.000` | `0.737` | `0.123` | `soft_accepted` | missing_exact_anchors | make integration, Error 2 | - |
| `git-01` | `recall` | `git` | `11012.34` | `0.413` | `0.000` | `0.743` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | git rebase origin/main, src/api/client.py, a1c9f42, OrdersClient | - |
| `git-02` | `recall` | `git` | `43847.51` | `0.883` | `1.000` | `0.871` | `1.000` | `0.745` | `0.151` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `45729.96` | `0.751` | `0.875` | `0.950` | `1.000` | `0.855` | `0.517` | `soft_accepted` | missing_exact_anchors | invalid index-pack output | - |
| `curl-01` | `recall` | `curl` | `46231.28` | `0.411` | `0.000` | `0.736` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | curl -fL --retry 3 --retry-all-errors -o dist/tool-linux-amd64.tar.gz https://downloads.example.com/tool/releases/v1.8.4/tool-linux-amd64.tar.gz, curl: (22), 404, dist/tool-linux-amd64.tar.gz | - |
| `curl-02` | `summary` | `curl` | `46152.67` | `0.641` | `1.000` | `0.906` | `0.500` | `0.391` | `0.276` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `ssh-01` | `summary` | `ssh` | `26439.16` | `0.924` | `1.000` | `0.940` | `1.000` | `0.896` | `0.652` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `19801.33` | `0.682` | `0.788` | `0.884` | `1.000` | `0.804` | `0.348` | `soft_accepted` | missing_exact_anchors | Host key verification failed. | - |
| `systemd-01` | `summary` | `systemd` | `35173.26` | `0.967` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `35480.77` | `0.833` | `1.000` | `0.873` | `1.000` | `0.767` | `0.224` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `18373.32` | `0.549` | `0.000` | `0.739` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | sudo apt-get install libpq-dev postgresql-client, libpq-dev, libpq5, postgresql-client-16, held broken packages | - |
| `dnf-01` | `recall` | `dnf` | `51972.91` | `0.603` | `0.429` | `0.865` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | conflicting requests, python3.12-devel, python3.12-3.12.0-1.el9.x86_64, python3.12-3.12.2-2.el9.x86_64 | - |
| `go-build-01` | `summary` | `go-build` | `21446.66` | `0.557` | `0.000` | `0.764` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | go build ./cmd/api, pkg/server/handler.go:87:24, ErrNotFound, example.com/mono-app/pkg/server | - |
| `go-test-01` | `summary` | `go-test` | `74740.04` | `0.700` | `0.667` | `0.929` | `1.000` | `0.871` | `0.571` | `soft_accepted` | missing_exact_anchors | cache_test.go:47 | - |
| `javac-01` | `summary` | `javac` | `22559.65` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `22555.58` | `0.520` | `0.261` | `0.864` | `0.500` | `0.451` | `0.673` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | UserControllerTest.getUser_notFound_returns404, UserControllerTest.java:72, maven-surefire-plugin:3.5.5:test, /workspace/webapp/target/surefire-reports | - |
| `maven-02` | `summary` | `maven` | `60531.60` | `0.553` | `0.000` | `0.751` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mvn -U -DskipTests package, org.postgresql:postgresql:jar:42.7.3, Failed to execute goal on project ingest-service, Could not resolve dependencies | - |
| `gradle-01` | `recall` | `gradle` | `48486.50` | `0.563` | `0.476` | `0.912` | `1.000` | `0.759` | `0.198` | `soft_accepted` | missing_exact_anchors | ./gradlew :service:build --warning-mode=all, :service:compileJava | - |
| `gradle-02` | `summary` | `gradle` | `13162.05` | `0.533` | `0.000` | `0.692` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ./gradlew test, InventoryServiceTest, InventoryServiceTest.java:118, Execution failed for task ':test' | - |
| `cargo-01` | `summary` | `cargo` | `28185.93` | `0.881` | `1.000` | `0.901` | `1.000` | `0.841` | `0.471` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `13141.56` | `0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `45088.87` | `0.412` | `0.000` | `0.740` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | node dist/server.js, Cannot find module './env/schema', MODULE_NOT_FOUND, /workspace/dist/config/index.js:4:18 | - |
| `npm-04` | `summary` | `npm` | `42245.58` | `0.547` | `0.000` | `0.733` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm install, ERESOLVE, react@18.3.1, @testing-library/react-hooks@8.0.1, dashboard-web@0.9.0 | - |
| `tsc-01` | `summary` | `tsc` | `37933.90` | `0.551` | `0.000` | `0.746` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npx tsc -p tsconfig.build.json, src/routes/user.ts(14,21), TS2339, userId | - |
| `eslint-04` | `summary` | `eslint` | `29912.69` | `0.777` | `0.773` | `0.927` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | react-hooks/exhaustive-deps | - |
| `python-runtime-01` | `summary` | `python-runtime` | `23445.67` | `0.659` | `1.000` | `0.909` | `0.500` | `0.412` | `0.411` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `pytest-06` | `summary` | `pytest` | `44452.57` | `0.458` | `0.000` | `0.740` | `1.000` | `0.787` | `0.289` | `soft_accepted` | missing_exact_anchors | pytest tests/api/test_auth.py -k login -q, test_login_rate_limit_after_5_failures, tests/api/test_auth.py:88, assert 200 == 429 | - |
| `mypy-04` | `summary` | `mypy` | `35915.64` | `0.905` | `1.000` | `0.890` | `1.000` | `0.898` | `0.660` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `62757.19` | `0.426` | `0.000` | `0.727` | `1.000` | `0.721` | `0.069` | `soft_accepted` | missing_exact_anchors | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund, Dockerfile:8, zod@3.23.8, failed to solve | - |
| `docker-compose-04` | `summary` | `docker-compose` | `46799.74` | `0.549` | `0.000` | `0.741` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker compose up --build, mono-api-1, 0.0.0.0:8080, port is already allocated | - |
| `kubectl-05` | `summary` | `kubectl` | `14379.43` | `0.968` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `69142.60` | `0.623` | `0.353` | `0.849` | `1.000` | `0.911` | `0.702` | `soft_accepted` | missing_exact_anchors | migrate, CrashLoopBackOff, Exit Code:    1 | - |
| `kubectl-07` | `recall` | `kubectl` | `18609.88` | `0.735` | `0.722` | `0.960` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ingress.networking.k8s.io/web configured | - |
| `terraform-05` | `recall` | `terraform` | `15569.05` | `0.708` | `0.667` | `0.931` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Error acquiring the state lock, 9c4fd2f2-8b24-42c1-93b5-65f0e2d83f63 | - |
| `terraform-06` | `summary` | `terraform` | `34216.52` | `0.863` | `1.000` | `0.908` | `1.000` | `0.800` | `0.333` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `42086.89` | `0.553` | `0.400` | `0.862` | `0.500` | `0.456` | `0.707` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | Plan: 1 to add, 1 to change, 0 to destroy., 2, aws_security_group_rule.web_https | - |
| `nginx-01` | `summary` | `nginx` | `36780.68` | `0.556` | `0.000` | `0.761` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | sudo nginx -t, "server" directive is not allowed here, /etc/nginx/sites-enabled/api.conf:1, configuration file /etc/nginx/nginx.conf test failed | - |
| `nginx-02` | `summary` | `nginx` | `13628.70` | `0.470` | `0.000` | `0.681` | `1.000` | `0.862` | `0.538` | `soft_accepted` | missing_exact_anchors | sudo service nginx reload, /etc/letsencrypt/live/example.com/fullchain.pem, cannot load certificate, configuration file /etc/nginx/nginx.conf test failed | - |
| `postgres-01` | `recall` | `postgres` | `47162.23` | `0.928` | `1.000` | `0.887` | `1.000` | `0.869` | `0.562` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `53658.42` | `0.862` | `1.000` | `0.902` | `1.000` | `0.802` | `0.340` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `31350.54` | `0.627` | `0.533` | `0.826` | `1.000` | `0.847` | `0.491` | `soft_accepted` | missing_exact_anchors | ERROR 1045 (28000), Access denied for user | - |
| `mysql-02` | `summary` | `mysql` | `11673.87` | `0.545` | `0.000` | `0.729` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mysql -h db.example.net -u app -D appdb -e "SELECT id, createdAt FROM users LIMIT 5", ERROR 1054 (42S22), createdAt, line 1 | - |
| `redis-01` | `summary` | `redis` | `46141.14` | `0.559` | `0.000` | `0.769` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | redis-cli -u redis://127.0.0.1:6379 SET sync:cursor 90210, MISCONF, stop-writes-on-bgsave-error, sync:cursor | - |
| `redis-02` | `recall` | `redis` | `16875.82` | `0.413` | `0.000` | `0.742` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | redis-cli -u redis://127.0.0.1:6379 PING, LOADING, Redis is loading the dataset in memory | - |
| `github-actions-01` | `recall` | `github-actions` | `11874.30` | `0.415` | `0.000` | `0.753` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | ruff check ., src/api/views.py, line=91, Ruff F821, exit code 2 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `53930.47` | `0.551` | `0.000` | `0.747` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pnpm install --frozen-lockfile, ERR_PNPM_ENOSPC, no space left on device, react-dom@18.3.1, ERROR: Job failed: exit status 1 | - |
| `jenkins-01` | `summary` | `jenkins` | `42565.02` | `0.692` | `0.625` | `0.871` | `1.000` | `0.918` | `0.725` | `soft_accepted` | missing_exact_anchors | webpack --mode production | - |
| `make-01` | `summary` | `make` | `67796.21` | `0.853` | `1.000` | `0.924` | `1.000` | `0.768` | `0.226` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `14918.11` | `0.798` | `0.857` | `0.936` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | unexpected end of file | - |
| `ansible-01` | `recall` | `ansible` | `42099.15` | `0.404` | `0.000` | `0.701` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ansible-playbook -i inventories/prod/hosts.ini deploy.yml --limit proxy, proxy-2, UNREACHABLE!, Connection timed out | - |
| `rsync-01` | `summary` | `rsync` | `20257.99` | `0.699` | `0.667` | `0.900` | `1.000` | `0.891` | `0.638` | `soft_accepted` | missing_exact_anchors | code 24, some files vanished before they could be transferred | - |
| `test-failure-01` | `recall` | `test-failure` | `49240.11` | `0.701` | `0.773` | `0.953` | `1.000` | `0.815` | `0.385` | `soft_accepted` | missing_exact_anchors | tests/unit/test_invoice_totals.py:88 | - |
| `compiler-error-01` | `recall` | `compiler-error` | `64294.85` | `0.597` | `0.403` | `0.885` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/router.rs:128, req.into_body(), req.method(), req.clone().into_body() | - |
| `ci-log-01` | `recall` | `ci-log` | `40333.80` | `0.417` | `0.000` | `0.761` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | helm upgrade --install payments-api charts/payments-api --namespace prod-payments, Deployment.apps "payments-api" is invalid, spec.template.spec.containers[0].env[3].valueFrom.secretKeyRef.name, Invalid value: "", deployments.apps "payments-api" not found | - |
| `package-manager-01` | `recall` | `package-manager` | `24529.93` | `0.361` | `0.000` | `0.728` | `1.000` | `0.829` | `0.430` | `soft_accepted` | missing_exact_anchors | npm install @storybook/react-vite@8.2.0 vite@6.0.1, npm ERR! code ERESOLVE, @storybook/react-vite@8.2.0, vite@6.0.1, peer vite@"^4.0.0 || ^5.0.0", --force or --legacy-peer-deps | - |
| `test-summary-01` | `summary` | `test-summary` | `75931.38` | `0.725` | `0.821` | `0.930` | `1.000` | `0.851` | `0.505` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | checkout_test.go:71 | - |
| `build-log-01` | `summary` | `build-log` | `43101.55` | `0.541` | `0.000` | `0.716` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | billing-service, InvoiceMapper.java:[58,29], cannot find symbol, setTaxCode(java.lang.String), InvoiceDto | - |
| `docker-build-02` | `summary` | `docker-build` | `52886.62` | `0.468` | `0.667` | `0.884` | `0.000` | `0.000` | `0.205` | `soft_accepted` | missing_exact_anchors | Dockerfile:18 | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `19655.77` | `0.141` | `0.000` | `0.513` | `0.000` | `0.000` | `0.121` | `soft_accepted` | missing_exact_anchors | /repo/web/src/App.tsx, 27:19, @typescript-eslint/no-misused-promises, /repo/web/src/api/client.ts, 8:10, @typescript-eslint/no-explicit-any, 33:11, @typescript-eslint/no-unsafe-assignment | - |
| `git-review-01` | `instruction_following` | `git-review` | `31515.61` | `0.281` | `0.524` | `0.673` | `0.000` | `0.000` | `0.236` | `soft_accepted` | missing_exact_anchors | packages/api/src/schema/openapi.yaml, migrations/202605171200_add_refresh_ttl.sql | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `40329.86` | `0.574` | `0.000` | `0.582` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | search endpoint failed after 2 attempts, exit status 22, https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `29870.19` | `0.281` | `1.000` | `0.224` | `0.000` | `0.000` | `0.135` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `23491.76` | `0.072` | `0.000` | `0.219` | `0.000` | `0.000` | `0.188` | `soft_accepted` | missing_exact_anchors | test / integration, Start docker compose, port 5432 is already allocated, deploy / preview, Upload artifact, dist/preview | - |
| `structured-output-03` | `structured` | `structured-output` | `14631.46` | `0.060` | `0.000` | `0.176` | `0.000` | `0.000` | `0.184` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | createSession › rejects expired refresh token, src/auth/session.test.ts, "refresh token expired", "invalid refresh token", calculateTax › uses EU VAT for DE customer, src/billing/tax.test.ts, Expected: 19, Received: 0 | - |
| `structured-output-04` | `structured` | `structured-output` | `19756.63` | `0.594` | `1.000` | `0.979` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `16888.67` | `0.024` | `0.000` | `0.277` | `0.000` | `0.000` | `0.011` | `soft_accepted` | missing_exact_anchors | tests/api/test_users.py::test_create_user_requires_email, tests/api/test_users.py::test_delete_user_requires_admin, tests/jobs/test_reconcile.py::TestReconcile::test_retries_deadlock | - |
| `exact-format-02` | `exact_format` | `exact-format` | `73416.22` | `0.021` | `0.000` | `0.250` | `0.000` | `0.000` | `0.006` | `soft_accepted` | missing_exact_anchors | packages/web/src/search/searchBox.test.tsx, SearchBox debounces network query before fetch | - |
| `exact-format-03` | `exact_format` | `exact-format` | `41596.72` | `0.183` | `1.000` | `0.318` | `0.000` | `0.000` | `0.026` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `43029.32` | `0.578` | `0.000` | `0.761` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /repo/tools/json.py, has no attribute 'dumps', shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `15445.45` | `0.496` | `0.000` | `0.630` | `1.000` | `0.905` | `0.683` | `soft_accepted` | missing_exact_anchors | TS2322, string | undefined, AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `28800.14` | `0.674` | `1.000` | `0.897` | `0.000` | `0.000` | `0.256` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `16247.01` | `0.412` | `0.000` | `0.737` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | app.tasks.email.send_welcome_email, SMTPRecipientsRefused, /srv/app/app/tasks/email.py, line 92, [bad@example.test](mailto:bad@example.test), retries exhausted for queue emails | - |
| `mypy-05` | `recall` | `mypy` | `50874.08` | `0.759` | `0.867` | `0.895` | `1.000` | `0.937` | `0.788` | `soft_accepted` | missing_exact_anchors | -> str | - |
| `terraform-08` | `recall` | `terraform` | `42029.85` | `0.699` | `0.810` | `0.902` | `1.000` | `0.797` | `0.325` | `soft_accepted` | missing_exact_anchors | worker-prod-inline, EntityAlreadyExists | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `46028.81` | `0.589` | `0.565` | `0.901` | `1.000` | `0.739` | `0.129` | `soft_accepted` | missing_exact_anchors | InventorySyncTest > publishesBackorderEvent() FAILED, OrderServiceTest > calculatesDiscountForGoldCustomer() PASSED | - |
| `kubernetes-01` | `recall` | `kubernetes` | `18325.49` | `0.613` | `0.440` | `0.892` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | CrashLoopBackOff, Exit Code: 78, FATAL config: required env STRIPE_KEY is empty | - |
| `go-test-02` | `recall` | `go-test` | `56156.57` | `0.874` | `1.000` | `0.819` | `1.000` | `0.757` | `0.189` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `52113.04` | `0.977` | `1.000` | `0.927` | `1.000` | `0.985` | `0.950` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `11071.96` | `0.983` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `9285.24` | `0.404` | `0.000` | `0.702` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | TS2307, @acme/contracts, packages/api/src/index.ts:4:25, TS6305, /repo/packages/contracts/dist/index.d.ts, packages/contracts/src/index.ts | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `44971.37` | `0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `39858.63` | `0.532` | `0.316` | `0.802` | `1.000` | `0.950` | `0.833` | `soft_accepted` | missing_exact_anchors | ERR_PNPM_OUTDATED_LOCKFILE, --frozen-lockfile, pnpm-lock.yaml, packages/api/package.json | - |
| `swift-01` | `recall` | `swift` | `40481.52` | `0.640` | `0.674` | `0.849` | `1.000` | `0.811` | `0.369` | `soft_accepted` | missing_exact_anchors | UserDecoderTests testMissingAvatarUsesPlaceholder, Tests/UserDecoderTests.swift:47 | - |
| `elixir-01` | `recall` | `elixir` | `10253.34` | `0.401` | `0.000` | `0.689` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | MyApp.CacheWorker, KeyError, key :ttl not found, lib/my_app/cache_worker.ex:63, test/my_app/cache_worker_test.exs:29, refreshes expired keys | - |
| `rails-01` | `recall` | `rails` | `25413.81` | `0.637` | `0.471` | `0.951` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 20260518093012 AddIndexToEventsRequestId, index_events_on_request_id, 20260518093012_add_index_to_events_request_id.rb:3 | - |
| `phpunit-01` | `recall` | `phpunit` | `20864.58` | `0.403` | `0.000` | `0.695` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Tests\Billing\InvoiceTotalTest::testAppliesCreditBeforeTax, Failed asserting that '88.00' is identical to '86.40', /tests/Billing/InvoiceTotalTest.php:52, Failures: 1, Deprecations: 2 | - |
| `nginx-03` | `recall` | `nginx` | `11376.92` | `0.417` | `0.000` | `0.761` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | nginx -t -c /etc/nginx/nginx.conf, duplicate location "/api", /etc/nginx/conf.d/api.conf:22, configuration file /etc/nginx/nginx.conf test failed | - |
| `postgres-03` | `recall` | `postgres` | `21912.21` | `0.980` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `19227.83` | `0.403` | `0.000` | `0.695` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | web-02, UNREACHABLE, 10.0.4.22 port 22, Connection timed out, ansible-playbook deploy.yml -i inventory/prod.ini | - |
| `bazel-01` | `recall` | `bazel` | `44831.39` | `0.408` | `0.000` | `0.718` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | //services/reporting:report_parser_test, XMLSyntaxError, Opening and ending tag mismatch: total line 18 and totals, services/reporting/parser.py", line 141, etree.fromstring(xml_bytes) | - |
| `powershell-01` | `recall` | `powershell` | `24278.04` | `0.703` | `0.688` | `0.869` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | .\scripts\release.ps1 -Version 1.4.2 | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `26593.90` | `0.411` | `0.000` | `0.734` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | web@1.7.0, upload-sourcemaps dist --rewrite, Authentication credentials were not provided, http status: 401, exit code 1 | - |
| `python-pytest-01` | `summary` | `python-pytest` | `13730.63` | `0.688` | `0.435` | `0.877` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/payments/test_webhook.py::test_replays_duplicate_event, RuntimeError, STRIPE_WEBHOOK_SECRET | - |
| `go-test-03` | `summary` | `go-test` | `25049.01` | `0.549` | `0.000` | `0.739` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ./integration, TestWebhookReplay, runtime, github.com/acme/api/internal/webhook, Dispatcher, dispatch | - |
| `npm-05` | `summary` | `npm` | `46206.65` | `0.900` | `1.000` | `0.881` | `1.000` | `0.896` | `0.653` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `26924.40` | `0.924` | `0.875` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | template | - |
| `ruff-04` | `summary` | `ruff` | `36822.09` | `0.761` | `0.737` | `0.904` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | app/services/user.py:88:89 | - |
| `k6-01` | `summary` | `k6` | `29108.78` | `0.697` | `0.652` | `0.863` | `1.000` | `0.923` | `0.742` | `soft_accepted` | missing_exact_anchors | smoke.js, checks | - |
| `composer-01` | `summary` | `composer` | `42834.78` | `0.936` | `1.000` | `0.840` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `33774.62` | `0.538` | `0.000` | `0.707` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | xcodebuild, -scheme, MobileApp, -configuration, Release | - |
| `make-02` | `summary` | `make` | `17835.42` | `0.739` | `1.000` | `0.922` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `30786.86` | `0.658` | `0.462` | `0.850` | `1.000` | `0.937` | `0.789` | `soft_accepted` | missing_exact_anchors | auto, tests/e2e | - |
| `jest-01` | `summary` | `jest` | `44086.04` | `0.543` | `0.222` | `0.755` | `1.000` | `0.863` | `0.543` | `soft_accepted` | missing_exact_anchors | src/components/Header.test.tsx, FAIL, src/components/Header.test.tsx | - |
| `dbt-01` | `summary` | `dbt` | `31061.73` | `0.876` | `1.000` | `0.902` | `1.000` | `0.830` | `0.433` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `28037.82` | `0.662` | `0.419` | `0.811` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/test_signup.py::test_signup_is_idempotent, sqlalchemy.exc.IntegrityError, psycopg.errors.UniqueViolation | - |
| `wrangler-01` | `summary` | `wrangler` | `33385.65` | `0.855` | `1.000` | `0.917` | `1.000` | `0.777` | `0.257` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `23921.85` | `0.956` | `1.000` | `0.889` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `46710.38` | `0.150` | `0.000` | `0.560` | `0.000` | `0.000` | `0.081` | `soft_accepted` | missing_exact_anchors | src/App.tsx, 22:7, prefer-const, src/api.ts, 4:12, @typescript-eslint/no-explicit-any | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `16948.62` | `0.180` | `0.000` | `0.581` | `0.000` | `0.000` | `0.373` | `soft_accepted` | missing_exact_anchors | src/auth/token.ts, JWT expiry from 15m to 7d, infra/terraform/iam.tf, iam:PassRole | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `14180.83` | `0.144` | `0.000` | `0.526` | `0.000` | `0.000` | `0.111` | `soft_accepted` | missing_exact_anchors | tests/test_api.py::test_create_user, tests/test_auth.py::test_refresh_token_expiry | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `39356.47` | `0.156` | `0.000` | `0.544` | `0.000` | `0.000` | `0.203` | `soft_accepted` | missing_exact_anchors | ubuntu-latest, node=22, pnpm test, windows-latest, node=20, pnpm install | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `20163.25` | `0.253` | `0.462` | `0.609` | `0.000` | `0.000` | `0.229` | `soft_accepted` | missing_exact_anchors | Warning Failed, Back-off restarting failed container api | - |
| `npm-06` | `instruction_following` | `npm` | `10864.03` | `0.295` | `0.227` | `0.673` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm ERR! code ENOTEMPTY, npm ERR! syscall rename, /repo/node_modules/esbuild | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `25852.28` | `0.281` | `0.750` | `0.593` | `0.000` | `0.000` | `0.028` | `soft_accepted` | missing_exact_anchors | [deps 4/4] | - |
| `terraform-09` | `instruction_following` | `terraform` | `21256.67` | `0.153` | `0.000` | `0.568` | `0.000` | `0.000` | `0.095` | `soft_accepted` | missing_exact_anchors | aws_db_instance.main, destroyed, identifier = "prod-main" | - |
| `maven-03` | `instruction_following` | `maven` | `18916.81` | `0.170` | `0.000` | `0.568` | `0.000` | `0.000` | `0.292` | `soft_accepted` | missing_exact_anchors | UserService.java:[44,17], findByEmail, UserController.java:[28,31], java.lang.Long, java.util.UUID | - |
| `playwright-01` | `instruction_following` | `playwright` | `31244.88` | `0.410` | `1.000` | `0.655` | `0.000` | `0.000` | `0.141` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `24810.47` | `0.164` | `0.000` | `0.587` | `0.000` | `0.000` | `0.167` | `soft_accepted` | missing_exact_anchors | src/App.tsx, src/api/client.ts | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `9944.49` | `0.132` | `0.000` | `0.507` | `0.000` | `0.000` | `0.034` | `soft_accepted` | missing_exact_anchors | worker-5b8c, CrashLoopBackOff, migrator-9z1q, Error | - |
| `cargo-04` | `instruction_following` | `cargo` | `46515.14` | `0.407` | `0.833` | `0.706` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | auth::tests::parses_expired_token | - |
| `shell-01` | `instruction_following` | `shell` | `10444.19` | `0.465` | `1.000` | `0.759` | `0.000` | `0.000` | `0.375` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `43019.11` | `0.277` | `1.000` | `0.235` | `0.000` | `0.000` | `0.061` | `accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `21016.13` | `0.055` | `0.000` | `0.195` | `0.000` | `0.000` | `0.064` | `soft_accepted` | missing_exact_anchors | add, aws_iam_role.app, change, resource, aws_lambda_function.api, field | - |
| `junit-01` | `structured` | `junit` | `22766.22` | `0.363` | `1.000` | `0.453` | `0.000` | `0.000` | `0.277` | `accepted` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `27209.43` | `0.078` | `0.143` | `0.192` | `0.000` | `0.000` | `0.051` | `soft_accepted` | missing_exact_anchors | unhealthy_pods, api-77df, status, CrashLoopBackOff, restarts | - |
| `eslint-06` | `structured` | `eslint` | `11464.46` | `0.070` | `0.111` | `0.187` | `0.000` | `0.000` | `0.040` | `soft_accepted` | missing_exact_anchors | src/a.ts, line, column, rule, src/b.ts | - |
| `docker-build-04` | `structured` | `docker-build` | `9355.03` | `0.093` | `0.148` | `0.187` | `0.000` | `0.000` | `0.233` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | stage, builder, command, pnpm, error | - |
| `go-test-04` | `structured` | `go-test` | `7953.73` | `0.403` | `1.000` | `0.568` | `0.000` | `0.000` | `0.324` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `13050.37` | `0.086` | `0.167` | `0.188` | `0.000` | `0.000` | `0.118` | `soft_accepted` | missing_exact_anchors | Job, Step, Exit, test, Run | - |
| `npm-07` | `structured` | `npm` | `50776.41` | `0.275` | `1.000` | `0.240` | `0.000` | `0.000` | `0.028` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `17018.20` | `0.130` | `0.000` | `0.177` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | File, Line, Code, Message, ---, app/api.py | - |
| `gradle-03` | `structured` | `gradle` | `11821.50` | `0.065` | `0.000` | `0.187` | `0.000` | `0.000` | `0.206` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | failed, task, :api:compileJava, cause, cannot, find | - |
| `playwright-02` | `structured` | `playwright` | `30427.11` | `0.287` | `1.000` | `0.206` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `13266.42` | `0.064` | `0.000` | `0.170` | `0.000` | `0.000` | `0.246` | `soft_accepted` | missing_exact_anchors | errors, file, migrations/004.sql, line, message, column | - |
| `vite-01` | `structured` | `vite` | `21097.39` | `0.270` | `1.000` | `0.220` | `0.000` | `0.000` | `0.043` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `59126.56` | `0.023` | `0.000` | `0.265` | `0.000` | `0.000` | `0.003` | `soft_accepted` | missing_exact_anchors, exact_format_style_mismatch | tests/test_a.py::test_one, tests/test_b.py::TestB::test_three | - |
| `git-04` | `exact_format` | `git` | `40995.02` | `0.151` | `1.000` | `0.272` | `0.000` | `0.000` | `0.007` | `soft_accepted` | exact_format_style_mismatch | - | - |
| `docker-04` | `exact_format` | `docker` | `33251.41` | `0.153` | `1.000` | `0.297` | `0.000` | `0.000` | `0.014` | `soft_accepted` | exact_format_style_mismatch | - | - |
| `npm-08` | `exact_format` | `npm` | `13070.66` | `0.028` | `0.000` | `0.272` | `0.000` | `0.000` | `0.111` | `soft_accepted` | missing_exact_anchors | 2.18.4 | - |
| `go-test-05` | `exact_format` | `go-test` | `70291.09` | `0.023` | `0.000` | `0.269` | `0.000` | `0.000` | `0.007` | `soft_accepted` | missing_exact_anchors, exact_format_style_mismatch | github.com/acme/shop/checkout, TestCheckoutAppliesCoupon | - |
| `kubectl-09` | `exact_format` | `kubectl` | `14120.50` | `0.200` | `1.000` | `0.300` | `0.000` | `0.000` | `0.400` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `10737.48` | `0.552` | `1.000` | `0.997` | `0.500` | `0.500` | `1.000` | `soft_accepted` | exact_format_style_mismatch | - | - |
| `curl-03` | `exact_format` | `curl` | `30107.55` | `0.148` | `1.000` | `0.241` | `0.000` | `0.000` | `0.010` | `soft_accepted` | exact_format_style_mismatch | - | - |
| `rails-02` | `exact_format` | `rails` | `69649.35` | `0.020` | `0.000` | `0.236` | `0.000` | `0.000` | `0.003` | `soft_accepted` | missing_exact_anchors, exact_format_style_mismatch | 20260518133742 | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `38182.54` | `0.731` | `1.000` | `0.920` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `40005.05` | `0.878` | `1.000` | `0.760` | `1.000` | `0.994` | `0.979` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `14647.94` | `0.346` | `0.000` | `0.729` | `0.000` | `0.000` | `0.426` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | orders_customer_id_fkey, customer_id, customers | - |
| `docker-build-05` | `explanation` | `docker-build` | `12249.49` | `0.562` | `0.000` | `0.723` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ../shared, outside the build context, COPY | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `19863.63` | `0.581` | `0.000` | `0.767` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ImagePullBackOff, registry.example.com/worker:9c1d, manifest unknown | - |
| `rust-01` | `explanation` | `rust` | `7479.74` | `0.541` | `0.000` | `0.674` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | E0515, buf, returns a reference | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `39047.23` | `0.920` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `11630.36` | `0.405` | `0.000` | `0.756` | `1.000` | `0.962` | `0.875` | `soft_accepted` | missing_exact_anchors | main.cpp:10:5, error: 'cout' was not declared in this scope | - |
| `testing-01` | `recall` | `testing` | `11705.16` | `0.967` | `1.000` | `0.935` | `1.000` | `0.950` | `0.833` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `14028.59` | `0.700` | `0.818` | `0.881` | `1.000` | `0.804` | `0.346` | `soft_accepted` | missing_exact_anchors | Cannot read property 'foo' of undefined | - |
| `package-management-01` | `recall` | `package-management` | `8892.82` | `0.404` | `0.000` | `0.702` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm ERR! code E404, 404 Not Found, GET https://registry.npmjs.org/foo | - |
| `runtime-02` | `recall` | `runtime` | `11363.06` | `0.396` | `0.000` | `0.661` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | duplicate key value violates unique constraint, test@example.com, INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `26050.28` | `0.909` | `1.000` | `0.886` | `1.000` | `0.811` | `0.370` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `15285.12` | `0.416` | `0.000` | `0.759` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | error[E0277], main.rs:5:26, Display | - |
| `ci-01` | `recall` | `ci` | `19715.99` | `0.899` | `1.000` | `0.830` | `1.000` | `0.824` | `0.412` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `7873.93` | `0.975` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `10863.30` | `0.417` | `0.000` | `0.761` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | BadRequest, cannot be handled as a Pod, Name: name not present | - |
| `infrastructure-01` | `recall` | `infrastructure` | `7032.47` | `0.405` | `0.000` | `0.704` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Missing required argument, main.tf line 12, "ami" is required | - |
| `compilation-02` | `recall` | `compilation` | `7270.79` | `0.402` | `0.000` | `0.694` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | error TS2307, src/app.ts:10:3, Cannot find module 'lodash' | - |
| `ci-02` | `recall` | `ci` | `12128.22` | `0.409` | `0.000` | `0.727` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Installing npm modules, failed with exit code 1 | - |
| `build-01` | `recall` | `build` | `14810.33` | `0.895` | `1.000` | `0.846` | `1.000` | `0.800` | `0.333` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `11956.98` | `0.970` | `1.000` | `0.878` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `66934.94` | `0.418` | `0.000` | `0.765` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | package com.google.common does not exist, 1 error | - |
| `infrastructure-02` | `recall` | `infrastructure` | `14636.47` | `0.327` | `0.000` | `0.681` | `1.000` | `0.743` | `0.143` | `soft_accepted` | missing_exact_anchors | You must be logged in to the server, Unauthorized | - |
| `runtime-03` | `recall` | `runtime` | `6097.25` | `0.342` | `0.000` | `0.711` | `1.000` | `0.775` | `0.250` | `soft_accepted` | missing_exact_anchors | RecursionError, maximum recursion depth exceeded | - |
| `package-management-03` | `recall` | `package-management` | `14713.78` | `0.415` | `0.000` | `0.753` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | No matching distribution found, requests==3.0.0 | - |
| `infrastructure-03` | `recall` | `infrastructure` | `41831.47` | `0.411` | `0.000` | `0.735` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | COPY failed, no such file or directory | - |
| `testing-04` | `recall` | `testing` | `17647.09` | `0.414` | `0.000` | `0.747` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Failure/Error, User signs in, capybara-3.34.0/lib/capybara/node/element.rb:1008 | - |
| `build-02` | `recall` | `build` | `20871.53` | `0.946` | `1.000` | `0.869` | `1.000` | `0.936` | `0.786` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `13743.56` | `0.416` | `0.000` | `0.758` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERROR: failed to fetch, 404  Not Found, libssl1.0.0_1.0.2g-1ubuntu4.0_amd64.deb | - |
| `testing-05` | `recall` | `testing` | `8383.76` | `0.884` | `1.000` | `0.803` | `1.000` | `0.800` | `0.333` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `17186.14` | `0.842` | `1.000` | `0.849` | `1.000` | `0.804` | `0.346` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `33034.82` | `0.798` | `1.000` | `0.835` | `1.000` | `0.728` | `0.094` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `7515.06` | `0.461` | `0.000` | `0.715` | `1.000` | `0.812` | `0.375` | `soft_accepted` | missing_exact_anchors | rolled out successfully | - |
| `ci-04` | `summary` | `ci` | `5769.57` | `0.952` | `1.000` | `0.880` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `10967.74` | `0.821` | `1.000` | `0.871` | `1.000` | `0.745` | `0.150` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `11505.16` | `0.557` | `0.000` | `0.764` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Finished dev | - |
| `linting-01` | `instruction_following` | `linting` | `18680.34` | `0.262` | `0.636` | `0.568` | `0.000` | `0.000` | `0.105` | `soft_accepted` | missing_exact_anchors | index.js | - |
| `testing-06` | `instruction_following` | `testing` | `68230.61` | `0.397` | `1.000` | `0.653` | `0.000` | `0.000` | `0.010` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `19727.79` | `0.141` | `0.000` | `0.549` | `0.000` | `0.000` | `0.012` | `soft_accepted` | missing_exact_anchors | ERROR: failed to fetch, 404  Not Found | - |
| `linting-02` | `structured` | `linting` | `11414.68` | `0.406` | `1.000` | `0.593` | `0.000` | `0.000` | `1.000` | `soft_accepted` | structured_output_mismatch | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `17891.45` | `0.274` | `1.000` | `0.198` | `0.000` | `0.000` | `0.143` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `41999.11` | `0.047` | `0.000` | `0.176` | `0.000` | `0.000` | `0.020` | `soft_accepted` | missing_exact_anchors | InstanceId, State | - |
| `network-01` | `exact_format` | `network` | `53968.85` | `0.025` | `0.000` | `0.274` | `0.000` | `0.000` | `0.042` | `soft_accepted` | missing_exact_anchors | CVE-2021-1234, Critical | - |
| `shell-02` | `exact_format` | `shell` | `62115.98` | `0.023` | `0.000` | `0.257` | `0.000` | `0.000` | `0.036` | `soft_accepted` | missing_exact_anchors | Timeout while waiting for response | - |
| `shell-03` | `exact_format` | `shell` | `17941.99` | `0.024` | `0.000` | `0.254` | `0.000` | `0.000` | `0.062` | `soft_accepted` | missing_exact_anchors | OUTPUT: | - |
| `shell-04` | `exact_format` | `shell` | `42339.08` | `0.025` | `0.000` | `0.264` | `0.000` | `0.000` | `0.062` | `soft_accepted` | missing_exact_anchors | NullPointerException | - |
| `build-04` | `exact_format` | `build` | `18244.10` | `0.222` | `1.000` | `0.592` | `0.000` | `0.000` | `0.259` | `accepted` | - | - | - |
| `build-05` | `exact_format` | `build` | `72839.90` | `0.034` | `0.000` | `0.262` | `0.000` | `0.000` | `0.286` | `soft_accepted` | missing_exact_anchors | BUILD SUCCESSFUL | - |
| `shell-05` | `exact_format` | `shell` | `4214.36` | `0.582` | `1.000` | `0.658` | `0.500` | `0.400` | `0.333` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `14511.16` | `0.849` | `1.000` | `0.829` | `1.000` | `0.803` | `0.342` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `38415.91` | `0.588` | `0.000` | `0.783` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | IndexError: list index out of range | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `9730.15` | `0.949` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `6082.61` | `0.917` | `1.000` | `0.834` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `73191.88` | `0.475` | `0.000` | `0.713` | `1.000` | `0.708` | `0.027` | `soft_accepted` | missing_exact_anchors | nil pointer dereference, SIGSEGV | - |
| `runtime-06` | `explanation` | `runtime` | `9174.93` | `0.568` | `0.000` | `0.737` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | KeyError: 'username' | - |
| `deployment-04` | `explanation` | `deployment` | `38233.12` | `0.561` | `0.000` | `0.719` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | password authentication failed | - |
| `explanation-01` | `explanation` | `explanation` | `7196.15` | `0.930` | `1.000` | `0.860` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `6617.69` | `0.913` | `1.000` | `0.826` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `39669.91` | `0.922` | `1.000` | `0.844` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `12000.53` | `0.529` | `0.000` | `0.724` | `1.000` | `0.882` | `0.607` | `soft_accepted` | missing_exact_anchors | exited with 1 | - |
| `explanation-05` | `explanation` | `explanation` | `30197.39` | `0.789` | `1.000` | `0.770` | `1.000` | `0.711` | `0.038` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `47931.42` | `0.592` | `0.000` | `0.793` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Permission denied | - |
| `explanation-07` | `explanation` | `explanation` | `13193.25` | `0.566` | `0.000` | `0.731` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | SECRET_KEY setting must not be empty | - |
| `explanation-08` | `explanation` | `explanation` | `45321.08` | `0.559` | `0.000` | `0.715` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Unable to locate credentials | - |
| `explanation-09` | `explanation` | `explanation` | `6842.37` | `0.572` | `0.000` | `0.746` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | would be overwritten by merge | - |
| `explanation-10` | `explanation` | `explanation` | `25716.91` | `0.580` | `0.000` | `0.765` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | KeyError: 'API_KEY' | - |
| `explanation-11` | `explanation` | `explanation` | `36346.04` | `0.564` | `0.000` | `0.726` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Address already in use | - |
| `explanation-12` | `explanation` | `explanation` | `64325.66` | `0.422` | `0.000` | `0.739` | `0.500` | `0.390` | `0.264` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | OOMKilled | - |
| `ci-07` | `structured` | `ci` | `18183.29` | `0.274` | `1.000` | `0.198` | `0.000` | `0.000` | `0.143` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `39526.60` | `0.047` | `0.000` | `0.176` | `0.000` | `0.000` | `0.020` | `soft_accepted` | missing_exact_anchors | InstanceId, State | - |
| `network-02` | `exact_format` | `network` | `51721.45` | `0.025` | `0.000` | `0.274` | `0.000` | `0.000` | `0.042` | `soft_accepted` | missing_exact_anchors | CVE-2021-1234, Critical | - |
| `shell-06` | `exact_format` | `shell` | `16181.56` | `0.025` | `0.000` | `0.257` | `0.000` | `0.000` | `0.083` | `soft_accepted` | missing_exact_anchors | Timeout while waiting for response | - |
| `shell-07` | `exact_format` | `shell` | `37290.63` | `0.282` | `1.000` | `0.303` | `0.143` | `0.101` | `0.034` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `18819.05` | `0.222` | `1.000` | `0.592` | `0.000` | `0.000` | `0.259` | `accepted` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `23389.83` | `0.024` | `0.000` | `0.243` | `0.000` | `0.000` | `0.083` | `soft_accepted` | missing_exact_anchors | Listening on port 8080 | - |
| `build-07` | `exact_format` | `build` | `34384.97` | `0.048` | `0.000` | `0.260` | `0.000` | `0.000` | `0.600` | `soft_accepted` | missing_exact_anchors | testError:34 | - |
| `shell-08` | `exact_format` | `shell` | `19486.70` | `0.028` | `0.000` | `0.262` | `0.000` | `0.000` | `0.143` | `soft_accepted` | missing_exact_anchors | HOME | - |
| `deployment-05` | `explanation` | `deployment` | `13979.42` | `0.849` | `1.000` | `0.829` | `1.000` | `0.803` | `0.342` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `34584.47` | `0.588` | `0.000` | `0.783` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | IndexError: list index out of range | - |
| `deployment-07` | `explanation` | `deployment` | `16775.57` | `0.959` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `29908.28` | `0.856` | `1.000` | `0.835` | `1.000` | `0.815` | `0.382` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `38302.12` | `0.561` | `0.000` | `0.719` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | password authentication failed | - |
| `explanation-15` | `explanation` | `explanation` | `31056.21` | `0.960` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `24245.81` | `0.571` | `0.000` | `0.744` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | undefined: fmt.Println | - |
| `explanation-17` | `explanation` | `explanation` | `16587.94` | `0.563` | `0.000` | `0.724` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | missing script: start | - |
| `package-management-04` | `explanation` | `package-management` | `10014.10` | `0.880` | `1.000` | `0.840` | `1.000` | `0.880` | `0.600` | `accepted` | - | - | - |
