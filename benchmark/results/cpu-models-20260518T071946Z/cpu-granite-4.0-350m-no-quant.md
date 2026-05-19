# cpu-granite-4.0-350m-no-quant

## Scenario

- track: `cpu`
- phase: `cpu-screen`
- model: `ibm-granite/granite-4.0-350m-GGUF`
- quantization: `none`
- device: `cpu`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `3675.20`
- cpu_rss_bytes: `null`
- gpu_peak_bytes: `null`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `278`
- accepted_count: `103`
- soft_accepted_count: `175`
- rejected_count: `2`
- exact_pass_count: `117`
- avg_inference_ms: `4173.44`
- p95_inference_ms: `10097.56`
- avg_exact_preservation_ratio: `0.616`
- avg_summary_quality_ratio: `0.791`
- avg_format_adherence_score: `0.746`
- avg_instruction_following_score: `0.717`
- avg_brevity_ratio: `0.803`
- avg_case_score: `0.629`
- p10_case_score: `0.225`
- quality_core: `0.549`
- latency_factor: `0.896`
- final_score: `49.12`
- peak_cpu_rss_bytes: `null`
- peak_gpu_bytes: `null`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `3761.59` | `0.776` | `0.833` | `0.953` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | line 18 column 3 | - |
| `python-02` | `summary` | `python` | `10301.55` | `0.833` | `1.000` | `0.936` | `0.500` | `0.459` | `0.727` | `accepted` | - | - | - |
| `python-03` | `recall` | `python` | `10115.55` | `0.566` | `0.655` | `0.894` | `0.500` | `0.422` | `0.479` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | ./scripts/run-local-api.sh, Worker failed to boot. | - |
| `python-04` | `recall` | `python` | `7861.54` | `0.744` | `0.917` | `0.852` | `1.000` | `0.850` | `0.500` | `soft_accepted` | missing_exact_anchors | catalog?page=2 | - |
| `python-05` | `recall` | `python` | `4564.44` | `0.443` | `0.148` | `0.819` | `1.000` | `0.850` | `0.500` | `soft_accepted` | missing_exact_anchors | python tools/export_report.py --input data/may.csv --format parquet, /workspace/src/reports/export.py, line 131, writer, data/may.csv | - |
| `pytest-01` | `recall` | `pytest` | `5175.95` | `0.462` | `0.182` | `0.876` | `1.000` | `0.828` | `0.426` | `soft_accepted` | missing_exact_anchors | pytest tests/api/test_users.py -q, tests/api/test_users.py::test_create_user_rejects_duplicate[email], tests/api/test_users.py:47, 500 == 409 | - |
| `pytest-02` | `summary` | `pytest` | `5129.20` | `0.798` | `0.837` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 1 error in 2.31s | - |
| `pytest-03` | `recall` | `pytest` | `5470.45` | `0.659` | `0.750` | `0.949` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors, verbatim_alignment_weak | job_runs_job_id_fkey, 149 passed, 1 skipped, 1 error in 58.73s | - |
| `pytest-04` | `recall` | `pytest` | `6526.52` | `0.730` | `0.825` | `0.939` | `1.000` | `0.858` | `0.526` | `soft_accepted` | missing_exact_anchors | 4 passed, 1 warning in 0.18s | - |
| `pytest-05` | `summary` | `pytest` | `7326.81` | `0.592` | `0.431` | `0.909` | `0.500` | `0.475` | `0.833` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | pytest tests/unit tests/integration --disable-warnings=0, src/billing/client.py:9, 1 error during collection | - |
| `mypy-01` | `recall` | `mypy` | `1985.47` | `0.522` | `0.195` | `0.904` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mypy src/accounts/user_service.py --show-error-codes, src/accounts/user_service.py:84, attr-defined, Found 1 error in 1 file | - |
| `mypy-02` | `summary` | `mypy` | `4633.51` | `0.621` | `0.211` | `0.859` | `1.000` | `0.969` | `0.897` | `soft_accepted` | missing_exact_anchors | mypy src tests --pretty --show-error-codes, src/payments/retry.py:118, arg-type, checked 37 source files | - |
| `mypy-03` | `recall` | `mypy` | `5566.59` | `0.982` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `1951.52` | `0.545` | `0.000` | `0.727` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ruff check src --output-format=full, src/payments/init.py:1:20, F401, Client, all, Found 1 error. | - |
| `ruff-02` | `summary` | `ruff` | `1838.31` | `0.745` | `0.600` | `0.940` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ruff format --check src tests | - |
| `ruff-03` | `summary` | `ruff` | `3367.30` | `0.787` | `0.829` | `0.922` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Found 1 error. | - |
| `pylint-01` | `recall` | `pylint` | `3560.22` | `0.984` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `5284.65` | `0.960` | `1.000` | `0.898` | `1.000` | `0.956` | `0.853` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `3985.56` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `4023.21` | `0.718` | `0.500` | `0.923` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | black --check src tests, 2 files would be reformatted, 41 files would be left unchanged | - |
| `black-02` | `summary` | `black` | `1343.87` | `0.546` | `0.000` | `0.730` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | black src, /workspace/src/config/schema.py, Cannot parse, 58:12, 1 file failed to reformat, 1 file reformatted | - |
| `black-03` | `recall` | `black` | `1643.68` | `0.534` | `0.200` | `0.953` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | python -m black --check app.py cli.py, 2 files would be left unchanged | - |
| `npm-01` | `recall` | `npm` | `8296.87` | `0.919` | `1.000` | `0.913` | `1.000` | `0.821` | `0.404` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `3194.55` | `0.704` | `0.444` | `0.917` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm install, peer react@"^17.0.0", --legacy-peer-deps | - |
| `npm-03` | `summary` | `npm` | `3263.08` | `0.754` | `0.745` | `0.877` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | storefront@2.8.1, /workspace | - |
| `pnpm-01` | `recall` | `pnpm` | `5687.17` | `0.753` | `0.895` | `0.921` | `1.000` | `0.858` | `0.528` | `soft_accepted` | missing_exact_anchors | --no-frozen-lockfile | - |
| `pnpm-02` | `summary` | `pnpm` | `4436.39` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `3551.91` | `0.694` | `0.429` | `0.898` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pnpm -r test --stream, health route > returns build metadata when git sha is present, api@1.6.0, Exit status 1 | - |
| `typescript-01` | `summary` | `typescript` | `4262.34` | `0.751` | `0.667` | `0.917` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/server/index.ts(4,18), node:path | - |
| `typescript-02` | `recall` | `typescript` | `4316.85` | `0.798` | `0.895` | `0.944` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Watching for file changes | - |
| `typescript-03` | `summary` | `typescript` | `10094.39` | `0.699` | `1.000` | `0.953` | `0.500` | `0.440` | `0.603` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `eslint-01` | `recall` | `eslint` | `5644.22` | `0.938` | `1.000` | `0.917` | `1.000` | `0.877` | `0.591` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `4026.06` | `0.976` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `3138.57` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `5262.73` | `0.418` | `0.000` | `0.768` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker build -t api:dev ., COPY docker/entrypoint.sh /entrypoint.sh, /docker/entrypoint.sh, Dockerfile:14, failed to solve | - |
| `docker-02` | `summary` | `docker` | `1692.17` | `0.984` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `3899.55` | `0.559` | `0.000` | `0.769` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker build -f docker/web.Dockerfile -t web:ci ., RUN npm ci, ERESOLVE, react-dates@21.8.0, react@18.2.0, exit code: 1 | - |
| `docker-compose-01` | `summary` | `docker-compose` | `1530.53` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `12461.66` | `0.900` | `1.000` | `0.919` | `1.000` | `0.760` | `0.200` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `2419.12` | `0.968` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `5085.61` | `0.671` | `0.529` | `0.866` | `1.000` | `0.920` | `0.733` | `soft_accepted` | missing_exact_anchors | kubectl apply -f k8s/deployment.yaml --server-side, --force-conflicts | - |
| `kubectl-02` | `recall` | `kubectl` | `6479.58` | `0.801` | `0.895` | `0.957` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ErrImagePull | - |
| `kubectl-03` | `summary` | `kubectl` | `3422.29` | `0.981` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `44166.35` | `0.332` | `0.000` | `0.747` | `1.000` | `0.712` | `0.038` | `soft_accepted` | missing_exact_anchors | kubectl logs payments-worker-6f8f7d4df5-z5vsm -c worker --previous -n payments, payments-worker-6f8f7d4df5-z5vsm, /app/config.yaml, ValueError, invalid worker.concurrency, worker | - |
| `terraform-01` | `summary` | `terraform` | `2905.88` | `0.668` | `0.235` | `0.944` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform validate, main.tf line 23, Unsupported argument | - |
| `terraform-02` | `recall` | `terraform` | `3352.88` | `0.979` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `1708.61` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `3522.98` | `0.625` | `0.098` | `0.903` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform test, run "plan_defaults", tests/aws.tftest.hcl line 18, Test assertion failed, aws_instance.web.instance_type | - |
| `mixed-01` | `recall` | `mixed` | `2710.13` | `0.751` | `0.767` | `0.953` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | main.c(1338) | - |
| `mixed-02` | `summary` | `mixed` | `2524.17` | `0.594` | `0.000` | `0.872` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | make integration, migrations/202605121045_add_login_audit.sql, psql, Error 2, integration | - |
| `git-01` | `recall` | `git` | `10916.25` | `0.691` | `1.000` | `0.902` | `0.500` | `0.407` | `0.377` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `git-02` | `recall` | `git` | `3025.88` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `5317.87` | `0.640` | `0.500` | `0.913` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | curl 56, Connection reset by peer | - |
| `curl-01` | `recall` | `curl` | `2336.09` | `0.990` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `4539.11` | `0.740` | `1.000` | `0.926` | `0.500` | `0.500` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `ssh-01` | `summary` | `ssh` | `2118.56` | `0.556` | `0.000` | `0.759` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | GIT_SSH_COMMAND="ssh -o IdentitiesOnly=yes -i ~/.ssh/deploy_key" git ls-remote git@github.com:example/mono-app.git, Permission denied (publickey), fatal: Could not read from remote repository., git@github.com:example/mono-app.git | - |
| `ssh-02` | `summary` | `ssh` | `2652.57` | `0.771` | `0.788` | `0.901` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Host key verification failed. | - |
| `systemd-01` | `summary` | `systemd` | `2756.86` | `0.532` | `0.000` | `0.689` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | queue-worker.service, /opt/app/bin/worker.sh, status=203/EXEC, Exec format error | - |
| `systemd-02` | `summary` | `systemd` | `6180.52` | `0.728` | `0.643` | `0.865` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | line 17 | - |
| `apt-01` | `summary` | `apt` | `5069.37` | `0.619` | `0.286` | `0.898` | `1.000` | `0.894` | `0.648` | `soft_accepted` | missing_exact_anchors | sudo apt-get install libpq-dev postgresql-client, postgresql-client-16, held broken packages | - |
| `dnf-01` | `recall` | `dnf` | `19765.46` | `0.921` | `1.000` | `0.937` | `1.000` | `0.810` | `0.365` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `2136.32` | `0.767` | `0.750` | `0.913` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | example.com/mono-app/pkg/server | - |
| `go-test-01` | `summary` | `go-test` | `2867.79` | `0.574` | `0.000` | `0.813` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | go test ./... -run TestCacheTTL -count=1, TestCacheTTL, cache_test.go:47, invalid memory address or nil pointer dereference | - |
| `javac-01` | `summary` | `javac` | `4146.44` | `0.613` | `0.133` | `0.844` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | javac -d out $(find src/main/java -name '*.java'), src/main/java/com/example/app/cli/RunCommand.java:18, cannot find symbol | - |
| `maven-01` | `summary` | `maven` | `4848.30` | `0.734` | `0.565` | `0.931` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | UserControllerTest.java:72, /workspace/webapp/target/surefire-reports | - |
| `maven-02` | `summary` | `maven` | `3236.03` | `0.548` | `0.000` | `0.737` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mvn -U -DskipTests package, org.postgresql:postgresql:jar:42.7.3, Failed to execute goal on project ingest-service, Could not resolve dependencies | - |
| `gradle-01` | `recall` | `gradle` | `4530.28` | `0.595` | `0.476` | `0.850` | `1.000` | `0.920` | `0.733` | `soft_accepted` | missing_exact_anchors | ./gradlew :service:build --warning-mode=all, :service:compileClasspath | - |
| `gradle-02` | `summary` | `gradle` | `7765.65` | `0.889` | `1.000` | `0.918` | `1.000` | `0.843` | `0.477` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `8095.23` | `0.857` | `1.000` | `0.868` | `1.000` | `0.819` | `0.395` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `2749.94` | `0.747` | `0.667` | `0.907` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | crates.io index, guessing_game v0.1.0 | - |
| `node-runtime-01` | `recall` | `node-runtime` | `13693.93` | `0.676` | `1.000` | `0.864` | `0.500` | `0.394` | `0.295` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `npm-04` | `summary` | `npm` | `3634.11` | `0.683` | `0.368` | `0.902` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm install, ERESOLVE, dashboard-web@0.9.0 | - |
| `tsc-01` | `summary` | `tsc` | `1859.65` | `0.534` | `0.000` | `0.696` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npx tsc -p tsconfig.build.json, src/routes/user.ts(14,21), TS2339, userId | - |
| `eslint-04` | `summary` | `eslint` | `1696.40` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `5087.48` | `0.776` | `0.800` | `0.906` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | rules/staging.json | - |
| `pytest-06` | `summary` | `pytest` | `1862.12` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `3154.15` | `0.801` | `0.882` | `0.930` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | id | - |
| `docker-build-01` | `summary` | `docker-build` | `5795.91` | `0.569` | `0.000` | `0.798` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund, Dockerfile:8, zod@3.23.8, failed to solve | - |
| `docker-compose-04` | `summary` | `docker-compose` | `5285.19` | `0.872` | `1.000` | `0.889` | `1.000` | `0.833` | `0.443` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `3780.91` | `0.969` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `4481.95` | `0.537` | `0.000` | `0.704` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | kubectl describe pod web-7f6f6d9d7b-kj4t2 -n dev, migrate, CrashLoopBackOff, Exit Code:    1 | - |
| `kubectl-07` | `recall` | `kubectl` | `1488.48` | `0.979` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `4157.90` | `0.400` | `0.000` | `0.851` | `1.000` | `0.874` | `0.579` | `soft_accepted` | missing_exact_anchors | terraform plan -lock-timeout=5s -out=tfplan, Error acquiring the state lock, 9c4fd2f2-8b24-42c1-93b5-65f0e2d83f63, prod/network/terraform.tfstate | - |
| `terraform-06` | `summary` | `terraform` | `3132.04` | `0.932` | `1.000` | `0.912` | `1.000` | `0.934` | `0.780` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `3876.15` | `0.666` | `0.333` | `0.875` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform plan -detailed-exitcode -no-color, 2, aws_security_group_rule.web_https | - |
| `nginx-01` | `summary` | `nginx` | `1320.44` | `0.966` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `4968.26` | `0.976` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `3434.33` | `0.991` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `2384.70` | `0.967` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `5273.25` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `1352.81` | `0.988` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `2486.95` | `0.593` | `0.000` | `0.870` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | redis-cli -u redis://127.0.0.1:6379 SET sync:cursor 90210, MISCONF, stop-writes-on-bgsave-error, sync:cursor | - |
| `redis-02` | `recall` | `redis` | `3268.80` | `0.979` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `5854.85` | `0.539` | `0.286` | `0.824` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | src/api/views.py, line=91, Ruff F821, exit code 2 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `4895.37` | `0.653` | `0.316` | `0.849` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pnpm install --frozen-lockfile, react-dom@18.3.1, ERROR: Job failed: exit status 1 | - |
| `jenkins-01` | `summary` | `jenkins` | `2903.89` | `0.947` | `1.000` | `0.896` | `1.000` | `0.978` | `0.925` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `3488.07` | `0.795` | `0.837` | `0.939` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Error 1 | - |
| `tar-01` | `summary` | `tar` | `3108.73` | `0.708` | `0.500` | `0.896` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tar -xzf cache/node_modules.tgz -C /tmp/restore, Unexpected EOF in archive | - |
| `ansible-01` | `recall` | `ansible` | `3295.83` | `0.700` | `0.667` | `0.895` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | UNREACHABLE!, Connection timed out | - |
| `rsync-01` | `summary` | `rsync` | `4570.27` | `0.956` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `22331.98` | `0.801` | `0.909` | `0.932` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ROUND_HALF_UP is deprecated for discounts; use ROUND_HALF_EVEN | - |
| `compiler-error-01` | `recall` | `compiler-error` | `29155.11` | `0.445` | `0.403` | `0.909` | `0.500` | `0.372` | `0.144` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | src/router.rs:128, req.into_body(), req.method(), req.clone().into_body() | - |
| `ci-log-01` | `recall` | `ci-log` | `7400.13` | `0.928` | `1.000` | `0.914` | `1.000` | `0.850` | `0.500` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `6985.22` | `0.718` | `0.704` | `0.911` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | peer vite@"^4.0.0 || ^5.0.0", --force or --legacy-peer-deps | - |
| `test-summary-01` | `summary` | `test-summary` | `4664.75` | `0.557` | `0.250` | `0.858` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors | github.com/acme/shop/checkout, TestCheckoutAppliesStoreCredit, github.com/acme/shop/inventory, TestReconcileInventory, test timed out after 10m0s, worker.go:144 | - |
| `build-log-01` | `summary` | `build-log` | `4711.73` | `0.582` | `0.000` | `0.836` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | billing-service, InvoiceMapper.java:[58,29], cannot find symbol, setTaxCode(java.lang.String), InvoiceDto | - |
| `docker-build-02` | `summary` | `docker-build` | `7616.92` | `0.676` | `0.333` | `0.904` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Dockerfile:18, "/apps/web": not found | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `7795.73` | `0.360` | `1.000` | `0.693` | `0.000` | `0.000` | `0.157` | `soft_accepted` | structured_output_mismatch | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `6087.92` | `0.384` | `0.714` | `0.695` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | User.lastLoginIp, DROP COLUMN refresh_token_expires_at, session cookie maxAge changed from 86400 to 604800 | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `2461.01` | `0.564` | `0.000` | `0.545` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | search endpoint failed after 2 attempts, exit status 22, https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `6863.53` | `0.430` | `1.000` | `0.735` | `0.000` | `0.000` | `0.853` | `soft_accepted` | structured_output_mismatch | - | - |
| `structured-output-02` | `structured` | `structured-output` | `8304.02` | `0.190` | `0.476` | `0.230` | `0.000` | `0.000` | `0.595` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | Start docker compose, port 5432 is already allocated, Upload artifact, dist/preview | - |
| `structured-output-03` | `structured` | `structured-output` | `8287.67` | `0.337` | `1.000` | `0.353` | `0.000` | `0.000` | `0.310` | `accepted` | - | - | - |
| `structured-output-04` | `structured` | `structured-output` | `5449.64` | `0.424` | `0.531` | `0.976` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /repo/packages/time/src/parse.ts, /repo/apps/web/src/features/flags.ts, @acme/flags | - |
| `exact-format-01` | `exact_format` | `exact-format` | `4514.71` | `0.185` | `1.000` | `0.331` | `0.000` | `0.000` | `0.034` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `3953.46` | `0.187` | `1.000` | `0.324` | `0.000` | `0.000` | `0.100` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `5580.68` | `0.183` | `1.000` | `0.306` | `0.000` | `0.000` | `0.040` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `2517.50` | `0.631` | `0.000` | `0.886` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /repo/tools/json.py, has no attribute 'dumps', shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `2991.43` | `0.695` | `0.500` | `0.834` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | string | undefined, AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `5286.36` | `0.803` | `1.000` | `0.906` | `0.250` | `0.250` | `1.000` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `3594.37` | `0.404` | `0.000` | `0.699` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | app.tasks.email.send_welcome_email, SMTPRecipientsRefused, /srv/app/app/tasks/email.py, line 92, [bad@example.test](mailto:bad@example.test), retries exhausted for queue emails | - |
| `mypy-05` | `recall` | `mypy` | `3223.36` | `0.429` | `0.000` | `0.821` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/services/exporter.py:118, Signature of "serialize" incompatible with supertype "BaseExporter", [override], include_meta, -> bytes, -> str | - |
| `terraform-08` | `recall` | `terraform` | `5048.40` | `0.651` | `0.524` | `0.923` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | request id: 0f3e2b11-9ac9-4fd2-a3bb-6c07a3c6a90d, modules/worker/iam.tf line 27 | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `3065.48` | `0.665` | `0.565` | `0.914` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | InventorySyncTest > publishesBackorderEvent() FAILED, OrderServiceTest > calculatesDiscountForGoldCustomer() PASSED | - |
| `kubernetes-01` | `recall` | `kubernetes` | `3396.16` | `0.487` | `0.160` | `0.806` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | api-7d9f8c8b99-mx2kq, registry.example.com/api:2026.05.18-1, CrashLoopBackOff, Exit Code: 78, FATAL config: required env STRIPE_KEY is empty | - |
| `go-test-02` | `recall` | `go-test` | `2799.93` | `0.407` | `0.000` | `0.714` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | WARNING: DATA RACE, (*Store).Set(), /work/internal/cache/store.go:88, (*Store).Get(), /work/internal/cache/store.go:54, TestConcurrentSetGet | - |
| `cargo-03` | `recall` | `cargo` | `40712.59` | `0.350` | `0.000` | `0.822` | `1.000` | `0.720` | `0.068` | `soft_accepted` | missing_exact_anchors | error[E0432], BroadcastStream, crates/storage/src/events.rs:7:5, tokio_stream::wrappers, gated behind the `sync` feature, could not compile `storage` | - |
| `docker-compose-05` | `recall` | `docker-compose` | `3098.85` | `0.406` | `0.000` | `0.709` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | container app-api-1 is unhealthy, dependency failed to start, FATAL: password authentication failed for user "app", migration failed; exiting, docker compose up --wait api worker | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `2678.24` | `0.952` | `1.000` | `0.892` | `1.000` | `0.938` | `0.792` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `5116.01` | `0.801` | `0.905` | `0.939` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | exit code 1 | - |
| `pnpm-04` | `recall` | `pnpm` | `3349.33` | `0.712` | `0.684` | `0.917` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | fastify, ^5.1.0, ^5.2.1 | - |
| `swift-01` | `recall` | `swift` | `2840.65` | `0.972` | `1.000` | `0.936` | `1.000` | `0.966` | `0.886` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `3577.30` | `0.707` | `0.696` | `0.877` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | test/my_app/cache_worker_test.exs:29, refreshes expired keys | - |
| `rails-01` | `recall` | `rails` | `2775.69` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `2762.70` | `0.527` | `0.213` | `0.897` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Failed asserting that '88.00' is identical to '86.40', /tests/Billing/InvoiceTotalTest.php:52, Failures: 1, Deprecations: 2 | - |
| `nginx-03` | `recall` | `nginx` | `2730.56` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `3662.41` | `0.728` | `0.722` | `0.928` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | psql:dump.sql:418 | - |
| `ansible-02` | `recall` | `ansible` | `2275.42` | `0.401` | `0.000` | `0.687` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | web-02, UNREACHABLE, 10.0.4.22 port 22, Connection timed out, ansible-playbook deploy.yml -i inventory/prod.ini | - |
| `bazel-01` | `recall` | `bazel` | `7446.65` | `0.725` | `0.792` | `0.856` | `1.000` | `0.947` | `0.824` | `soft_accepted` | missing_exact_anchors | etree.fromstring(xml_bytes) | - |
| `powershell-01` | `recall` | `powershell` | `2427.03` | `0.401` | `0.000` | `0.685` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | .\scripts\release.ps1 -Version 1.4.2, cannot be loaded because running scripts is disabled, PSSecurityException, FullyQualifiedErrorId : UnauthorizedAccess | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `3002.90` | `0.797` | `0.882` | `0.964` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | exit code 1 | - |
| `python-pytest-01` | `summary` | `python-pytest` | `6159.44` | `0.938` | `1.000` | `0.874` | `1.000` | `0.978` | `0.926` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `4654.82` | `0.607` | `0.211` | `0.803` | `1.000` | `0.981` | `0.936` | `soft_accepted` | missing_exact_anchors | ./integration, github.com/acme/api/internal/webhook, Dispatcher, dispatch | - |
| `npm-05` | `summary` | `npm` | `8024.63` | `0.907` | `1.000` | `0.897` | `1.000` | `0.896` | `0.653` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `1121.38` | `0.972` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `6559.15` | `0.749` | `0.737` | `0.882` | `1.000` | `0.988` | `0.959` | `soft_accepted` | missing_exact_anchors | app/services/user.py:88:89 | - |
| `k6-01` | `summary` | `k6` | `3257.71` | `0.957` | `1.000` | `0.892` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `6323.30` | `0.924` | `1.000` | `0.936` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `2238.40` | `0.558` | `0.000` | `0.767` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | xcodebuild, -scheme, MobileApp, -configuration, Release | - |
| `make-02` | `summary` | `make` | `2079.82` | `0.648` | `0.227` | `0.888` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | -Iinclude, src/server.c, build/server.o, src/server.c:14:10 | - |
| `python-pytest-02` | `summary` | `python-pytest` | `2068.07` | `0.534` | `0.000` | `0.695` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | auto, tests/e2e, Not, properly, terminated | - |
| `jest-01` | `summary` | `jest` | `2209.98` | `0.945` | `1.000` | `0.861` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `3947.48` | `0.674` | `0.333` | `0.899` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --select, Compilation, Error | - |
| `python-pytest-03` | `summary` | `python-pytest` | `3907.08` | `0.962` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `4371.07` | `0.913` | `1.000` | `0.843` | `1.000` | `0.952` | `0.839` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `3920.95` | `0.785` | `0.889` | `0.878` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | example | - |
| `eslint-05` | `instruction_following` | `eslint` | `5944.19` | `0.270` | `0.370` | `0.654` | `0.000` | `0.000` | `0.471` | `soft_accepted` | missing_exact_anchors | prefer-const, src/api.ts, 4:12, @typescript-eslint/no-explicit-any | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `3327.45` | `0.554` | `1.000` | `0.848` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `1713.75` | `0.414` | `1.000` | `0.688` | `0.000` | `0.000` | `0.071` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `5426.96` | `0.388` | `1.000` | `0.708` | `0.000` | `0.000` | `0.444` | `soft_accepted` | structured_output_mismatch | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `10571.66` | `0.455` | `1.000` | `0.783` | `0.000` | `0.000` | `1.000` | `soft_accepted` | structured_output_mismatch | - | - |
| `npm-06` | `instruction_following` | `npm` | `2006.57` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `2421.67` | `0.447` | `1.000` | `0.740` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `5120.41` | `0.415` | `1.000` | `0.627` | `0.000` | `0.000` | `0.268` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `11684.18` | `0.217` | `0.000` | `0.519` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | UserService.java:[44,17], findByEmail, UserController.java:[28,31], java.lang.Long, java.util.UUID | - |
| `playwright-01` | `instruction_following` | `playwright` | `9435.31` | `0.201` | `0.000` | `0.528` | `0.000` | `0.000` | `0.786` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | firefox, checkout.spec.ts:44:1, pays with saved card, Payment complete | - |
| `prettier-01` | `instruction_following` | `prettier` | `679.21` | `0.462` | `1.000` | `0.707` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `2463.36` | `0.316` | `0.333` | `0.685` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | CrashLoopBackOff, Error | - |
| `cargo-04` | `instruction_following` | `cargo` | `5178.70` | `0.485` | `1.000` | `0.778` | `0.000` | `0.000` | `0.519` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `2472.16` | `0.446` | `1.000` | `0.732` | `0.000` | `0.000` | `0.265` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `6715.40` | `0.264` | `0.133` | `0.725` | `0.000` | `0.000` | `0.667` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | file, /repo/app/user.py, line, code, message | - |
| `terraform-10` | `structured` | `terraform` | `5914.93` | `0.312` | `0.667` | `0.569` | `0.000` | `0.000` | `0.636` | `soft_accepted` | missing_exact_anchors | resource, field | - |
| `junit-01` | `structured` | `junit` | `6618.61` | `0.215` | `0.286` | `0.557` | `0.000` | `0.000` | `0.283` | `soft_accepted` | missing_exact_anchors | Test, Error, Location, --- | - |
| `kubernetes-03` | `structured` | `kubernetes` | `22688.49` | `0.145` | `0.571` | `0.181` | `0.000` | `0.000` | `0.016` | `soft_accepted` | missing_exact_anchors | CrashLoopBackOff, restarts | - |
| `eslint-06` | `structured` | `eslint` | `4041.81` | `0.209` | `0.667` | `0.291` | `0.000` | `0.000` | `0.250` | `soft_accepted` | missing_exact_anchors | line, column, rule | - |
| `docker-build-04` | `structured` | `docker-build` | `2689.30` | `0.243` | `0.593` | `0.223` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | stage, error | - |
| `go-test-04` | `structured` | `go-test` | `4673.72` | `0.192` | `0.364` | `0.176` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | failed_tests, amount_test.go:22, message | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `1922.82` | `0.631` | `1.000` | `0.626` | `0.500` | `0.414` | `0.429` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `2636.53` | `0.490` | `0.500` | `0.365` | `0.667` | `0.667` | `1.000` | `soft_accepted` | missing_exact_anchors | legacy-widget@2.4.0, required, 18.0.0 | - |
| `mypy-06` | `structured` | `mypy` | `4115.79` | `0.265` | `0.600` | `0.304` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Line, Code, Message | - |
| `gradle-03` | `structured` | `gradle` | `2013.06` | `0.287` | `0.667` | `0.346` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | failed, task | - |
| `playwright-02` | `structured` | `playwright` | `4359.14` | `0.323` | `0.500` | `0.598` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | file, line, test | - |
| `postgres-04` | `structured` | `postgres` | `3199.98` | `0.258` | `0.758` | `0.175` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | message, column | - |
| `vite-01` | `structured` | `vite` | `6768.53` | `0.471` | `0.800` | `0.982` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /repo/apps/public/src/Home.tsx | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `6776.05` | `0.153` | `1.000` | `0.286` | `0.000` | `0.000` | `0.023` | `soft_accepted` | exact_format_style_mismatch | - | - |
| `git-04` | `exact_format` | `git` | `1781.60` | `0.182` | `1.000` | `0.282` | `0.000` | `0.000` | `0.071` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `2501.23` | `0.039` | `0.000` | `0.331` | `0.000` | `0.000` | `0.250` | `soft_accepted` | missing_exact_anchors | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | - |
| `npm-08` | `exact_format` | `npm` | `4279.94` | `0.192` | `1.000` | `0.294` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `1228.98` | `0.065` | `0.000` | `0.262` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors, exact_format_style_mismatch | github.com/acme/shop/checkout, TestCheckoutAppliesCoupon | - |
| `kubectl-09` | `exact_format` | `kubectl` | `3670.96` | `0.097` | `0.500` | `0.283` | `0.000` | `0.000` | `0.211` | `soft_accepted` | missing_exact_anchors | prod | - |
| `cargo-05` | `exact_format` | `cargo` | `1363.68` | `0.189` | `1.000` | `0.329` | `0.000` | `0.000` | `0.125` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `3396.27` | `0.149` | `1.000` | `0.235` | `0.000` | `0.000` | `0.029` | `soft_accepted` | exact_format_style_mismatch | - | - |
| `rails-02` | `exact_format` | `rails` | `3771.63` | `0.026` | `0.000` | `0.248` | `0.000` | `0.000` | `0.111` | `soft_accepted` | missing_exact_anchors | 20260518133742 | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `3241.52` | `0.731` | `1.000` | `0.920` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `922.85` | `0.924` | `1.000` | `0.848` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `24903.08` | `0.629` | `1.000` | `0.880` | `0.000` | `0.000` | `1.000` | `soft_accepted` | structured_output_mismatch | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `1656.77` | `0.921` | `1.000` | `0.842` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `1511.76` | `0.952` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `7913.96` | `0.691` | `1.000` | `0.826` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `2280.08` | `0.721` | `0.583` | `0.862` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `1627.59` | `0.416` | `0.000` | `0.923` | `1.000` | `0.875` | `0.583` | `soft_accepted` | missing_exact_anchors | main.cpp:10:5, error: 'cout' was not declared in this scope | - |
| `testing-01` | `recall` | `testing` | `2257.63` | `0.655` | `0.643` | `0.892` | `1.000` | `0.876` | `0.588` | `soft_accepted` | missing_exact_anchors | TestCalculator::testDivideByZero | - |
| `testing-02` | `recall` | `testing` | `2277.36` | `0.537` | `0.364` | `0.860` | `1.000` | `0.859` | `0.529` | `soft_accepted` | missing_exact_anchors | Cannot read property 'foo' of undefined, /usr/src/app/index.js:12:15 | - |
| `package-management-01` | `recall` | `package-management` | `1944.99` | `0.691` | `0.615` | `0.942` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | GET https://registry.npmjs.org/foo | - |
| `runtime-02` | `recall` | `runtime` | `2664.44` | `0.914` | `1.000` | `0.905` | `1.000` | `0.814` | `0.378` | `accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `2874.48` | `0.895` | `1.000` | `0.846` | `1.000` | `0.800` | `0.333` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `1789.07` | `0.508` | `0.190` | `0.850` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | error[E0277], main.rs:5:26 | - |
| `ci-01` | `recall` | `ci` | `1263.22` | `0.436` | `0.000` | `0.851` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Error: Tests failed, 5 tests run, 1 failure | - |
| `testing-03` | `recall` | `testing` | `771.81` | `0.981` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `2617.68` | `0.706` | `0.778` | `0.883` | `1.000` | `0.880` | `0.600` | `soft_accepted` | missing_exact_anchors | BadRequest | - |
| `infrastructure-01` | `recall` | `infrastructure` | `1241.89` | `0.968` | `1.000` | `0.929` | `1.000` | `0.957` | `0.857` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `2976.00` | `0.982` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `1420.26` | `0.413` | `0.000` | `0.860` | `1.000` | `0.914` | `0.714` | `soft_accepted` | missing_exact_anchors | Installing npm modules, failed with exit code 1 | - |
| `build-01` | `recall` | `build` | `1428.39` | `0.677` | `0.588` | `0.929` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | BUILD FAILED | - |
| `container-runtime-01` | `recall` | `container-runtime` | `507.62` | `0.985` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `1395.72` | `0.432` | `0.000` | `0.891` | `1.000` | `0.957` | `0.857` | `soft_accepted` | missing_exact_anchors | package com.google.common does not exist, 1 error | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1872.01` | `0.625` | `0.500` | `0.840` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Unauthorized | - |
| `runtime-03` | `recall` | `runtime` | `2024.98` | `0.712` | `0.667` | `0.950` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | maximum recursion depth exceeded | - |
| `package-management-03` | `recall` | `package-management` | `1851.23` | `0.420` | `0.000` | `0.909` | `1.000` | `0.900` | `0.667` | `soft_accepted` | missing_exact_anchors | No matching distribution found, requests==3.0.0 | - |
| `infrastructure-03` | `recall` | `infrastructure` | `1765.29` | `0.681` | `0.636` | `0.886` | `1.000` | `0.979` | `0.929` | `soft_accepted` | missing_exact_anchors | no such file or directory | - |
| `testing-04` | `recall` | `testing` | `1610.79` | `0.504` | `0.167` | `0.871` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Failure/Error, capybara-3.34.0/lib/capybara/node/element.rb:1008 | - |
| `build-02` | `recall` | `build` | `1742.53` | `0.418` | `0.000` | `0.908` | `1.000` | `0.894` | `0.647` | `soft_accepted` | missing_exact_anchors | foo.c:5:2, error: expected ';' | - |
| `ci-03` | `recall` | `ci` | `2602.46` | `0.526` | `0.222` | `0.875` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERROR: failed to fetch, libssl1.0.0_1.0.2g-1ubuntu4.0_amd64.deb | - |
| `testing-05` | `recall` | `testing` | `534.89` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `1140.09` | `0.673` | `0.286` | `0.926` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | FAILURE: Build failed with an exception | - |
| `docker-05` | `summary` | `docker` | `1287.66` | `0.548` | `0.000` | `0.831` | `1.000` | `0.925` | `0.750` | `soft_accepted` | missing_exact_anchors | healthcheck status: unhealthy | - |
| `kubernetes-05` | `summary` | `kubernetes` | `890.50` | `0.552` | `0.000` | `0.898` | `1.000` | `0.880` | `0.600` | `soft_accepted` | missing_exact_anchors | rolled out successfully | - |
| `ci-04` | `summary` | `ci` | `1716.16` | `0.653` | `0.524` | `0.843` | `1.000` | `0.900` | `0.667` | `soft_accepted` | missing_exact_anchors | Success: | - |
| `npm-09` | `summary` | `npm` | `1559.27` | `0.488` | `0.000` | `0.870` | `1.000` | `0.753` | `0.176` | `soft_accepted` | missing_exact_anchors | ERESOLVE, unable to resolve dependency tree | - |
| `rust-02` | `summary` | `rust` | `2111.58` | `0.896` | `1.000` | `0.823` | `1.000` | `0.933` | `0.778` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `3800.01` | `0.310` | `0.364` | `0.638` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | error | - |
| `testing-06` | `instruction_following` | `testing` | `5222.93` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | ERROR:, * rerun pytest test_auth.py::TestAuth::test_login | granite output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='- follow the requested structure exactly - return only the requested json, yaml, table, or bullet structure - do not add prose before or after the structured...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='- follow the requested structure exactly - return only the requested json, yaml, table, or bullet structure - do not add prose before or after the structured...' |
| `ci-05` | `instruction_following` | `ci` | `3559.16` | `0.434` | `1.000` | `0.751` | `0.000` | `0.000` | `0.091` | `accepted` | - | - | - |
| `linting-02` | `structured` | `linting` | `6430.67` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | schema_echo, prompt_scaffold_echo | E302, found 1 | granite output validation failed. first_pass_status=rejected first_pass_flags=['schema_echo', 'prompt_scaffold_echo'] first_pass='E302 - found 1 Raw output: - follow the requested structure exactly - return only the requested json, yaml, table, or bullet structure - do not add prose bef...' repair_status=rejected repair_flags=['schema_echo', 'prompt_scaffold_echo'] repair_pass='E302 - found 1 Raw output: - follow the requested structure exactly - return only the requested json, yaml, table, or bullet structure - do not add prose bef...' |
| `kubernetes-06` | `structured` | `kubernetes` | `1638.14` | `0.358` | `1.000` | `0.195` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `2669.59` | `0.366` | `1.000` | `0.220` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `1167.82` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `1269.12` | `0.220` | `1.000` | `0.579` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `423.85` | `0.265` | `1.000` | `0.651` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `1828.13` | `0.207` | `1.000` | `0.491` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `3116.87` | `0.192` | `0.714` | `0.693` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | instance_id | - |
| `build-05` | `exact_format` | `build` | `758.64` | `0.225` | `1.000` | `0.609` | `0.000` | `0.000` | `0.286` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `532.90` | `0.582` | `1.000` | `0.658` | `0.500` | `0.400` | `0.333` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `1374.94` | `0.634` | `0.000` | `0.918` | `1.000` | `0.960` | `0.867` | `soft_accepted` | missing_exact_anchors | No module named 'requests' | - |
| `runtime-04` | `explanation` | `runtime` | `2586.77` | `0.597` | `0.000` | `0.918` | `1.000` | `0.829` | `0.429` | `soft_accepted` | missing_exact_anchors | IndexError: list index out of range | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `1662.60` | `0.964` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `911.90` | `0.943` | `1.000` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `1630.40` | `0.685` | `0.333` | `0.878` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | SIGSEGV | - |
| `runtime-06` | `explanation` | `runtime` | `1374.24` | `0.653` | `0.000` | `0.937` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | KeyError: 'username' | - |
| `deployment-04` | `explanation` | `deployment` | `1827.18` | `0.562` | `0.000` | `0.835` | `1.000` | `0.830` | `0.435` | `soft_accepted` | missing_exact_anchors | password authentication failed | - |
| `explanation-01` | `explanation` | `explanation` | `1357.29` | `0.943` | `1.000` | `0.886` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1433.87` | `0.578` | `0.000` | `0.803` | `1.000` | `0.936` | `0.786` | `soft_accepted` | missing_exact_anchors | toUpperCase is not a function | - |
| `explanation-03` | `explanation` | `explanation` | `1453.58` | `0.618` | `0.000` | `0.877` | `1.000` | `0.967` | `0.889` | `soft_accepted` | missing_exact_anchors | no configured push destination | - |
| `explanation-04` | `explanation` | `explanation` | `1988.59` | `0.630` | `0.000` | `0.882` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | exited with 1 | - |
| `explanation-05` | `explanation` | `explanation` | `924.07` | `0.945` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `999.36` | `0.902` | `1.000` | `0.870` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `1435.84` | `0.620` | `0.000` | `0.884` | `1.000` | `0.962` | `0.875` | `soft_accepted` | missing_exact_anchors | SECRET_KEY setting must not be empty | - |
| `explanation-08` | `explanation` | `explanation` | `1717.85` | `0.615` | `0.000` | `0.876` | `1.000` | `0.957` | `0.857` | `soft_accepted` | missing_exact_anchors | Unable to locate credentials | - |
| `explanation-09` | `explanation` | `explanation` | `1622.00` | `0.963` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `1597.02` | `0.595` | `0.000` | `0.870` | `1.000` | `0.894` | `0.647` | `soft_accepted` | missing_exact_anchors | KeyError: 'API_KEY' | - |
| `explanation-11` | `explanation` | `explanation` | `1775.68` | `0.572` | `0.000` | `0.826` | `1.000` | `0.880` | `0.600` | `soft_accepted` | missing_exact_anchors | Address already in use | - |
| `explanation-12` | `explanation` | `explanation` | `1577.52` | `0.625` | `0.000` | `0.914` | `1.000` | `0.933` | `0.778` | `soft_accepted` | missing_exact_anchors | OOMKilled | - |
| `ci-07` | `structured` | `ci` | `1556.94` | `0.358` | `1.000` | `0.195` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `3489.02` | `0.366` | `1.000` | `0.220` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `780.81` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `284.05` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `413.58` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `2188.53` | `0.192` | `0.714` | `0.693` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | instance_id | - |
| `runtime-07` | `exact_format` | `runtime` | `1129.21` | `0.046` | `0.000` | `0.287` | `0.000` | `0.000` | `0.500` | `soft_accepted` | missing_exact_anchors | Listening on port 8080 | - |
| `build-07` | `exact_format` | `build` | `2535.39` | `0.227` | `1.000` | `0.791` | `0.000` | `0.000` | `0.750` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `shell-08` | `exact_format` | `shell` | `472.88` | `0.231` | `1.000` | `0.646` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `1366.51` | `0.634` | `0.000` | `0.918` | `1.000` | `0.960` | `0.867` | `soft_accepted` | missing_exact_anchors | No module named 'requests' | - |
| `deployment-06` | `explanation` | `deployment` | `2150.87` | `0.597` | `0.000` | `0.918` | `1.000` | `0.829` | `0.429` | `soft_accepted` | missing_exact_anchors | IndexError: list index out of range | - |
| `deployment-07` | `explanation` | `deployment` | `1438.72` | `0.960` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `2030.00` | `0.972` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `1995.05` | `0.562` | `0.000` | `0.835` | `1.000` | `0.830` | `0.435` | `soft_accepted` | missing_exact_anchors | password authentication failed | - |
| `explanation-15` | `explanation` | `explanation` | `1893.43` | `0.917` | `1.000` | `0.882` | `1.000` | `0.929` | `0.762` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `991.50` | `0.905` | `1.000` | `0.860` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `1533.15` | `0.568` | `0.000` | `0.830` | `1.000` | `0.858` | `0.526` | `soft_accepted` | missing_exact_anchors | missing script: start | - |
| `package-management-04` | `explanation` | `package-management` | `1671.76` | `0.669` | `0.444` | `0.836` | `1.000` | `0.940` | `0.800` | `soft_accepted` | missing_exact_anchors | nonexistent (invalid) version of flask | - |
