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

- load_ms: `3677.13`
- cpu_rss_bytes: `null`
- gpu_peak_bytes: `null`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `277`
- accepted_count: `93`
- soft_accepted_count: `184`
- rejected_count: `3`
- exact_pass_count: `116`
- avg_inference_ms: `5155.39`
- p95_inference_ms: `11298.66`
- avg_exact_preservation_ratio: `0.628`
- avg_summary_quality_ratio: `0.173`
- avg_format_adherence_score: `0.728`
- avg_instruction_following_score: `0.699`
- avg_brevity_ratio: `0.806`
- avg_case_score: `0.432`
- p10_case_score: `0.170`
- quality_core: `0.380`
- latency_factor: `0.868`
- final_score: `32.97`
- peak_cpu_rss_bytes: `null`
- peak_gpu_bytes: `null`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `4361.71` | `0.574` | `0.833` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | line 18 column 3 | - |
| `python-02` | `summary` | `python` | `9150.58` | `0.459` | `1.000` | `0.000` | `0.500` | `0.459` | `0.727` | `accepted` | - | - | - |
| `python-03` | `recall` | `python` | `12288.60` | `0.376` | `0.655` | `0.000` | `0.500` | `0.422` | `0.479` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | ./scripts/run-local-api.sh, Worker failed to boot. | - |
| `python-04` | `recall` | `python` | `23161.80` | `0.572` | `0.917` | `0.043` | `1.000` | `0.850` | `0.500` | `soft_accepted` | missing_exact_anchors | catalog?page=2 | - |
| `python-05` | `recall` | `python` | `9783.35` | `0.713` | `1.000` | `0.073` | `1.000` | `0.835` | `0.449` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `6104.50` | `0.292` | `0.182` | `0.078` | `1.000` | `0.828` | `0.426` | `soft_accepted` | missing_exact_anchors | pytest tests/api/test_users.py -q, tests/api/test_users.py::test_create_user_rejects_duplicate[email], tests/api/test_users.py:47, 500 == 409 | - |
| `pytest-02` | `summary` | `pytest` | `5619.95` | `0.475` | `0.837` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 1 error in 2.31s | - |
| `pytest-03` | `recall` | `pytest` | `6009.36` | `0.457` | `0.750` | `0.000` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors, verbatim_alignment_weak | job_runs_job_id_fkey, 149 passed, 1 skipped, 1 error in 58.73s | - |
| `pytest-04` | `recall` | `pytest` | `7324.92` | `0.530` | `0.825` | `0.000` | `1.000` | `0.858` | `0.526` | `soft_accepted` | missing_exact_anchors | 4 passed, 1 warning in 0.18s | - |
| `pytest-05` | `summary` | `pytest` | `8431.95` | `0.283` | `0.431` | `0.000` | `0.500` | `0.475` | `0.833` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | pytest tests/unit tests/integration --disable-warnings=0, src/billing/client.py:9, 1 error during collection | - |
| `mypy-01` | `recall` | `mypy` | `1840.13` | `0.356` | `0.195` | `0.125` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mypy src/accounts/user_service.py --show-error-codes, src/accounts/user_service.py:84, attr-defined, Found 1 error in 1 file | - |
| `mypy-02` | `summary` | `mypy` | `6451.29` | `0.438` | `0.211` | `0.320` | `1.000` | `0.969` | `0.897` | `soft_accepted` | missing_exact_anchors | mypy src tests --pretty --show-error-codes, src/payments/retry.py:118, arg-type, checked 37 source files | - |
| `mypy-03` | `recall` | `mypy` | `7426.54` | `0.872` | `1.000` | `0.488` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `2259.88` | `0.354` | `0.000` | `0.167` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ruff check src --output-format=full, src/payments/init.py:1:20, F401, Client, all, Found 1 error. | - |
| `ruff-02` | `summary` | `ruff` | `4536.11` | `0.561` | `0.600` | `0.400` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ruff format --check src tests | - |
| `ruff-03` | `summary` | `ruff` | `4033.10` | `0.518` | `0.829` | `0.129` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Found 1 error. | - |
| `pylint-01` | `recall` | `pylint` | `3855.19` | `0.827` | `1.000` | `0.308` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `8814.54` | `0.778` | `1.000` | `0.170` | `1.000` | `0.956` | `0.853` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `5834.14` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `3888.38` | `0.449` | `0.500` | `0.133` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | black --check src tests, 2 files would be reformatted, 41 files would be left unchanged | - |
| `black-02` | `summary` | `black` | `1578.91` | `0.388` | `0.000` | `0.267` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | black src, /workspace/src/config/schema.py, Cannot parse, 58:12, 1 file failed to reformat, 1 file reformatted | - |
| `black-03` | `recall` | `black` | `2455.83` | `0.332` | `0.200` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | python -m black --check app.py cli.py, 2 files would be left unchanged | - |
| `npm-01` | `recall` | `npm` | `8128.57` | `0.727` | `1.000` | `0.147` | `1.000` | `0.821` | `0.404` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `3310.06` | `0.454` | `0.444` | `0.182` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm install, peer react@"^17.0.0", --legacy-peer-deps | - |
| `npm-03` | `summary` | `npm` | `3108.44` | `0.456` | `0.745` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | storefront@2.8.1, /workspace | - |
| `pnpm-01` | `recall` | `pnpm` | `6050.13` | `0.609` | `0.895` | `0.246` | `1.000` | `0.858` | `0.528` | `soft_accepted` | missing_exact_anchors | --no-frozen-lockfile | - |
| `pnpm-02` | `summary` | `pnpm` | `4410.15` | `0.738` | `1.000` | `0.345` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `3811.70` | `0.477` | `0.429` | `0.261` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pnpm -r test --stream, health route > returns build metadata when git sha is present, api@1.6.0, Exit status 1 | - |
| `typescript-01` | `summary` | `typescript` | `6393.49` | `0.461` | `0.667` | `0.065` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/server/index.ts(4,18), node:path | - |
| `typescript-02` | `recall` | `typescript` | `4732.79` | `0.682` | `0.895` | `0.400` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Watching for file changes | - |
| `typescript-03` | `summary` | `typescript` | `11369.17` | `0.398` | `1.000` | `0.071` | `0.500` | `0.440` | `0.603` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `eslint-01` | `recall` | `eslint` | `5989.76` | `0.755` | `1.000` | `0.185` | `1.000` | `0.877` | `0.591` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `4019.30` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `4448.43` | `0.869` | `1.000` | `0.476` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `5815.15` | `0.255` | `0.000` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker build -t api:dev ., COPY docker/entrypoint.sh /entrypoint.sh, /docker/entrypoint.sh, Dockerfile:14, failed to solve | - |
| `docker-02` | `summary` | `docker` | `2174.61` | `0.673` | `1.000` | `0.182` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `4157.21` | `0.386` | `0.000` | `0.261` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker build -f docker/web.Dockerfile -t web:ci ., RUN npm ci, ERESOLVE, react-dates@21.8.0, react@18.2.0, exit code: 1 | - |
| `docker-compose-01` | `summary` | `docker-compose` | `4231.43` | `0.714` | `1.000` | `0.286` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `18597.62` | `0.686` | `1.000` | `0.062` | `1.000` | `0.760` | `0.200` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `2575.61` | `0.694` | `1.000` | `0.235` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `5456.41` | `0.414` | `0.529` | `0.111` | `1.000` | `0.920` | `0.733` | `soft_accepted` | missing_exact_anchors | kubectl apply -f k8s/deployment.yaml --server-side, --force-conflicts | - |
| `kubectl-02` | `recall` | `kubectl` | `6946.76` | `0.597` | `0.895` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ErrImagePull | - |
| `kubectl-03` | `summary` | `kubectl` | `3479.73` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `51454.11` | `0.173` | `0.000` | `0.000` | `1.000` | `0.712` | `0.038` | `soft_accepted` | missing_exact_anchors | kubectl logs payments-worker-6f8f7d4df5-z5vsm -c worker --previous -n payments, payments-worker-6f8f7d4df5-z5vsm, /app/config.yaml, ValueError, invalid worker.concurrency, worker | - |
| `terraform-01` | `summary` | `terraform` | `3780.61` | `0.445` | `0.235` | `0.286` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform validate, main.tf line 23, Unsupported argument | - |
| `terraform-02` | `recall` | `terraform` | `3685.46` | `0.804` | `1.000` | `0.214` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `2533.41` | `0.868` | `1.000` | `0.471` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `5957.04` | `0.426` | `0.098` | `0.316` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform test, run "plan_defaults", tests/aws.tftest.hcl line 18, Test assertion failed, aws_instance.web.instance_type | - |
| `mixed-01` | `recall` | `mixed` | `3960.37` | `0.549` | `0.767` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | main.c(1338) | - |
| `mixed-02` | `summary` | `mixed` | `2971.45` | `0.297` | `0.000` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | make integration, migrations/202605121045_add_login_audit.sql, psql, Error 2, integration | - |
| `git-01` | `recall` | `git` | `15195.80` | `0.536` | `1.000` | `0.169` | `0.500` | `0.407` | `0.377` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `git-02` | `recall` | `git` | `4106.05` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `7302.56` | `0.490` | `0.500` | `0.207` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | curl 56, Connection reset by peer | - |
| `curl-01` | `recall` | `curl` | `2455.67` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `6185.06` | `0.425` | `1.000` | `0.000` | `0.500` | `0.500` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `ssh-01` | `summary` | `ssh` | `2541.29` | `0.377` | `0.000` | `0.235` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | GIT_SSH_COMMAND="ssh -o IdentitiesOnly=yes -i ~/.ssh/deploy_key" git ls-remote git@github.com:example/mono-app.git, Permission denied (publickey), fatal: Could not read from remote repository., git@github.com:example/mono-app.git | - |
| `ssh-02` | `summary` | `ssh` | `3092.19` | `0.465` | `0.788` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Host key verification failed. | - |
| `systemd-01` | `summary` | `systemd` | `2921.41` | `0.416` | `0.000` | `0.348` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | queue-worker.service, /opt/app/bin/worker.sh, status=203/EXEC, Exec format error | - |
| `systemd-02` | `summary` | `systemd` | `8384.84` | `0.531` | `0.643` | `0.286` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | line 17 | - |
| `apt-01` | `summary` | `apt` | `5772.88` | `0.313` | `0.286` | `0.000` | `1.000` | `0.894` | `0.648` | `soft_accepted` | missing_exact_anchors | sudo apt-get install libpq-dev postgresql-client, postgresql-client-16, held broken packages | - |
| `dnf-01` | `recall` | `dnf` | `27637.44` | `0.722` | `1.000` | `0.143` | `1.000` | `0.810` | `0.365` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `2173.31` | `0.457` | `0.750` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | example.com/mono-app/pkg/server | - |
| `go-test-01` | `summary` | `go-test` | `2742.21` | `0.343` | `0.000` | `0.133` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | go test ./... -run TestCacheTTL -count=1, TestCacheTTL, cache_test.go:47, invalid memory address or nil pointer dereference | - |
| `javac-01` | `summary` | `javac` | `4897.28` | `0.367` | `0.133` | `0.122` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | javac -d out $(find src/main/java -name '*.java'), src/main/java/com/example/app/cli/RunCommand.java:18, cannot find symbol | - |
| `maven-01` | `summary` | `maven` | `5700.71` | `0.418` | `0.565` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | UserControllerTest.java:72, /workspace/webapp/target/surefire-reports | - |
| `maven-02` | `summary` | `maven` | `3693.62` | `0.297` | `0.000` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mvn -U -DskipTests package, org.postgresql:postgresql:jar:42.7.3, Failed to execute goal on project ingest-service, Could not resolve dependencies | - |
| `gradle-01` | `recall` | `gradle` | `5343.07` | `0.438` | `0.476` | `0.111` | `1.000` | `0.920` | `0.733` | `soft_accepted` | missing_exact_anchors | ./gradlew :service:build --warning-mode=all, :service:compileClasspath | - |
| `gradle-02` | `summary` | `gradle` | `11166.04` | `0.555` | `1.000` | `0.083` | `1.000` | `0.843` | `0.477` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `11281.03` | `0.554` | `1.000` | `0.112` | `1.000` | `0.819` | `0.395` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `3877.35` | `0.567` | `0.667` | `0.375` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | crates.io index, guessing_game v0.1.0 | - |
| `node-runtime-01` | `recall` | `node-runtime` | `16636.17` | `0.498` | `1.000` | `0.024` | `0.500` | `0.394` | `0.295` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `npm-04` | `summary` | `npm` | `4776.83` | `0.412` | `0.368` | `0.105` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm install, ERESOLVE, dashboard-web@0.9.0 | - |
| `tsc-01` | `summary` | `tsc` | `2360.35` | `0.297` | `0.000` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npx tsc -p tsconfig.build.json, src/routes/user.ts(14,21), TS2339, userId | - |
| `eslint-04` | `summary` | `eslint` | `2239.68` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `6739.02` | `0.468` | `0.800` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | rules/staging.json | - |
| `pytest-06` | `summary` | `pytest` | `2523.37` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `3930.17` | `0.485` | `0.882` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | id | - |
| `docker-build-01` | `summary` | `docker-build` | `20999.06` | `0.405` | `0.844` | `0.068` | `1.000` | `0.777` | `0.256` | `soft_accepted` | missing_exact_anchors | failed to solve | - |
| `docker-compose-04` | `summary` | `docker-compose` | `7078.29` | `0.568` | `1.000` | `0.130` | `1.000` | `0.833` | `0.443` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `6161.38` | `0.686` | `1.000` | `0.214` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `5179.89` | `0.297` | `0.000` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | kubectl describe pod web-7f6f6d9d7b-kj4t2 -n dev, migrate, CrashLoopBackOff, Exit Code:    1 | - |
| `kubectl-07` | `recall` | `kubectl` | `1846.48` | `0.833` | `1.000` | `0.333` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `5464.99` | `0.248` | `0.000` | `0.136` | `1.000` | `0.874` | `0.579` | `soft_accepted` | missing_exact_anchors | terraform plan -lock-timeout=5s -out=tfplan, Error acquiring the state lock, 9c4fd2f2-8b24-42c1-93b5-65f0e2d83f63, prod/network/terraform.tfstate | - |
| `terraform-06` | `summary` | `terraform` | `3725.98` | `0.616` | `1.000` | `0.122` | `1.000` | `0.934` | `0.780` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `3621.75` | `0.368` | `0.333` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform plan -detailed-exitcode -no-color, 2, aws_security_group_rule.web_https | - |
| `nginx-01` | `summary` | `nginx` | `1750.53` | `0.657` | `1.000` | `0.143` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `6951.36` | `0.667` | `1.000` | `0.167` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `3991.85` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `3863.94` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `4700.23` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `2003.09` | `0.714` | `1.000` | `0.286` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `4084.83` | `0.361` | `0.000` | `0.188` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | redis-cli -u redis://127.0.0.1:6379 SET sync:cursor 90210, MISCONF, stop-writes-on-bgsave-error, sync:cursor | - |
| `redis-02` | `recall` | `redis` | `3952.99` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `6719.89` | `0.361` | `0.524` | `0.077` | `0.500` | `0.455` | `0.700` | `soft_accepted` | missing_exact_anchors | line=91, Ruff F821, exit code 2 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `7464.08` | `0.426` | `0.316` | `0.182` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pnpm install --frozen-lockfile, react-dom@18.3.1, ERROR: Job failed: exit status 1 | - |
| `jenkins-01` | `summary` | `jenkins` | `3194.35` | `0.649` | `1.000` | `0.151` | `1.000` | `0.978` | `0.925` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `4543.77` | `0.475` | `0.837` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Error 1 | - |
| `tar-01` | `summary` | `tar` | `3753.15` | `0.445` | `0.500` | `0.121` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tar -xzf cache/node_modules.tgz -C /tmp/restore, Unexpected EOF in archive | - |
| `ansible-01` | `recall` | `ansible` | `3808.04` | `0.510` | `0.667` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | UNREACHABLE!, Connection timed out | - |
| `rsync-01` | `summary` | `rsync` | `5408.60` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `28079.06` | `0.603` | `0.909` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ROUND_HALF_UP is deprecated for discounts; use ROUND_HALF_EVEN | - |
| `compiler-error-01` | `recall` | `compiler-error` | `34732.51` | `0.253` | `0.403` | `0.007` | `0.500` | `0.372` | `0.144` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | src/router.rs:128, req.into_body(), req.method(), req.clone().into_body() | - |
| `ci-log-01` | `recall` | `ci-log` | `8803.20` | `0.720` | `1.000` | `0.078` | `1.000` | `0.850` | `0.500` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `8295.27` | `0.547` | `0.704` | `0.105` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | peer vite@"^4.0.0 || ^5.0.0", --force or --legacy-peer-deps | - |
| `test-summary-01` | `summary` | `test-summary` | `5361.35` | `0.415` | `0.179` | `0.235` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | github.com/acme/shop/checkout, TestCheckoutAppliesStoreCredit, total = 42.00, want 37.00, github.com/acme/shop/inventory, TestReconcileInventory, test timed out after 10m0s, worker.go:144 | - |
| `build-log-01` | `summary` | `build-log` | `5159.79` | `0.377` | `0.000` | `0.235` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | billing-service, InvoiceMapper.java:[58,29], cannot find symbol, setTaxCode(java.lang.String), InvoiceDto | - |
| `docker-build-02` | `summary` | `docker-build` | `7520.35` | `0.293` | `0.000` | `0.041` | `1.000` | `0.957` | `0.857` | `soft_accepted` | missing_exact_anchors | Dockerfile:18, COPY apps/web ./apps/web, "/apps/web": not found | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `9492.40` | `0.160` | `0.875` | `0.000` | `0.000` | `0.000` | `0.138` | `soft_accepted` | missing_exact_anchors | /repo/web/src/App.tsx | - |
| `git-review-01` | `instruction_following` | `git-review` | `7200.77` | `0.223` | `0.810` | `0.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | DROP COLUMN refresh_token_expires_at, session cookie maxAge changed from 86400 to 604800 | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `4146.87` | `0.145` | `0.355` | `0.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `9088.71` | `0.413` | `1.000` | `0.667` | `0.000` | `0.000` | `0.853` | `soft_accepted` | structured_output_mismatch | - | - |
| `structured-output-02` | `structured` | `structured-output` | `31205.30` | `0.282` | `0.905` | `0.368` | `0.000` | `0.000` | `0.403` | `soft_accepted` | missing_exact_anchors | port 5432 is already allocated | - |
| `structured-output-03` | `structured` | `structured-output` | `7749.37` | `0.170` | `0.500` | `0.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | "refresh token expired", "invalid refresh token", Expected: 19, Received: 0 | - |
| `structured-output-04` | `structured` | `structured-output` | `6708.71` | `0.430` | `0.531` | `1.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /repo/packages/time/src/parse.ts, /repo/apps/web/src/features/flags.ts, @acme/flags | - |
| `exact-format-01` | `exact_format` | `exact-format` | `26544.06` | `0.161` | `1.000` | `0.000` | `0.015` | `0.011` | `0.016` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `5717.22` | `0.155` | `1.000` | `0.000` | `0.000` | `0.000` | `0.100` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `3335.04` | `0.014` | `0.000` | `0.000` | `0.000` | `0.000` | `0.333` | `soft_accepted` | missing_exact_anchors | ghcr.io/acme/worker@sha256:4f8c2e0b1d9a6c7e5f3a2b1908d4c6e7f0a123456789abcdeffedcba98765432 | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `4289.90` | `0.406` | `0.000` | `0.356` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /repo/tools/json.py, has no attribute 'dumps', shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `3142.16` | `0.380` | `0.500` | `0.093` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | string | undefined, AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `6084.93` | `0.429` | `1.000` | `0.257` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `3518.95` | `0.270` | `0.000` | `0.069` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | app.tasks.email.send_welcome_email, SMTPRecipientsRefused, /srv/app/app/tasks/email.py, line 92, [bad@example.test](mailto:bad@example.test), retries exhausted for queue emails | - |
| `mypy-05` | `recall` | `mypy` | `5741.53` | `0.264` | `0.000` | `0.043` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/services/exporter.py:118, Signature of "serialize" incompatible with supertype "BaseExporter", [override], include_meta, -> bytes, -> str | - |
| `terraform-08` | `recall` | `terraform` | `6301.53` | `0.469` | `0.524` | `0.065` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | request id: 0f3e2b11-9ac9-4fd2-a3bb-6c07a3c6a90d, modules/worker/iam.tf line 27 | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `3831.35` | `0.515` | `0.565` | `0.207` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | InventorySyncTest > publishesBackorderEvent() FAILED, OrderServiceTest > calculatesDiscountForGoldCustomer() PASSED | - |
| `kubernetes-01` | `recall` | `kubernetes` | `5329.63` | `0.327` | `0.160` | `0.049` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | api-7d9f8c8b99-mx2kq, registry.example.com/api:2026.05.18-1, CrashLoopBackOff, Exit Code: 78, FATAL config: required env STRIPE_KEY is empty | - |
| `go-test-02` | `recall` | `go-test` | `4132.27` | `0.255` | `0.000` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | WARNING: DATA RACE, (*Store).Set(), /work/internal/cache/store.go:88, (*Store).Get(), /work/internal/cache/store.go:54, TestConcurrentSetGet | - |
| `cargo-03` | `recall` | `cargo` | `62440.74` | `0.177` | `0.000` | `0.007` | `1.000` | `0.720` | `0.068` | `soft_accepted` | missing_exact_anchors | error[E0432], BroadcastStream, crates/storage/src/events.rs:7:5, tokio_stream::wrappers, gated behind the `sync` feature, could not compile `storage` | - |
| `docker-compose-05` | `recall` | `docker-compose` | `2737.08` | `0.283` | `0.000` | `0.133` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | container app-api-1 is unhealthy, dependency failed to start, FATAL: password authentication failed for user "app", migration failed; exiting, docker compose up --wait api worker | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `5234.87` | `0.794` | `1.000` | `0.258` | `1.000` | `0.938` | `0.792` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `7002.84` | `0.616` | `0.905` | `0.069` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | exit code 1 | - |
| `pnpm-04` | `recall` | `pnpm` | `4331.43` | `0.517` | `0.684` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | fastify, ^5.1.0, ^5.2.1 | - |
| `swift-01` | `recall` | `swift` | `3097.15` | `0.786` | `1.000` | `0.190` | `1.000` | `0.966` | `0.886` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `4811.23` | `0.521` | `0.696` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | test/my_app/cache_worker_test.exs:29, refreshes expired keys | - |
| `rails-01` | `recall` | `rails` | `4892.75` | `0.798` | `1.000` | `0.194` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `3538.97` | `0.336` | `0.213` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Failed asserting that '88.00' is identical to '86.40', /tests/Billing/InvoiceTotalTest.php:52, Failures: 1, Deprecations: 2 | - |
| `nginx-03` | `recall` | `nginx` | `3144.77` | `0.792` | `1.000` | `0.167` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `4317.72` | `0.590` | `0.722` | `0.276` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | psql:dump.sql:418 | - |
| `ansible-02` | `recall` | `ansible` | `3285.47` | `0.255` | `0.000` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | web-02, UNREACHABLE, 10.0.4.22 port 22, Connection timed out, ansible-playbook deploy.yml -i inventory/prod.ini | - |
| `bazel-01` | `recall` | `bazel` | `9237.83` | `0.611` | `0.792` | `0.319` | `1.000` | `0.947` | `0.824` | `soft_accepted` | missing_exact_anchors | etree.fromstring(xml_bytes) | - |
| `powershell-01` | `recall` | `powershell` | `2500.45` | `0.290` | `0.000` | `0.167` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | .\scripts\release.ps1 -Version 1.4.2, cannot be loaded because running scripts is disabled, PSSecurityException, FullyQualifiedErrorId : UnauthorizedAccess | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `5759.97` | `0.708` | `0.882` | `0.545` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | exit code 1 | - |
| `python-pytest-01` | `summary` | `python-pytest` | `3332.87` | `0.400` | `0.348` | `0.083` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/payments, tests/refunds, tests/payments/test_webhook.py::test_replays_duplicate_event | - |
| `go-test-03` | `summary` | `go-test` | `3877.37` | `0.328` | `0.000` | `0.089` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ./integration, TestWebhookReplay, runtime, github.com/acme/api/internal/webhook, Dispatcher, dispatch | - |
| `npm-05` | `summary` | `npm` | `8532.70` | `0.667` | `1.000` | `0.283` | `1.000` | `0.907` | `0.690` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `3834.42` | `0.464` | `0.562` | `0.138` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | api/templates/deployment.yaml:42:29, Values.image.repository | - |
| `ruff-04` | `summary` | `ruff` | `6495.10` | `0.403` | `0.211` | `0.222` | `1.000` | `0.966` | `0.887` | `soft_accepted` | missing_exact_anchors | app/api/routes.py:3:1, app/services/user.py:88:89, tests/test_user.py:12:1 | - |
| `k6-01` | `summary` | `k6` | `5356.56` | `0.496` | `0.826` | `0.067` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | avg | - |
| `composer-01` | `summary` | `composer` | `1838.90` | `0.468` | `0.800` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Loading | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `4896.19` | `0.347` | `0.000` | `0.146` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | xcodebuild, -scheme, MobileApp, -configuration, Release | - |
| `make-02` | `summary` | `make` | `2775.27` | `0.377` | `0.227` | `0.091` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | -Iinclude, src/server.c, build/server.o, src/server.c:14:10 | - |
| `python-pytest-02` | `summary` | `python-pytest` | `3000.21` | `0.350` | `0.000` | `0.154` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | auto, tests/e2e, Not, properly, terminated | - |
| `jest-01` | `summary` | `jest` | `978.11` | `0.633` | `1.000` | `0.083` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `4647.27` | `0.419` | `0.333` | `0.150` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --select, Compilation, Error | - |
| `python-pytest-03` | `summary` | `python-pytest` | `6770.52` | `0.733` | `1.000` | `0.333` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `10245.00` | `0.740` | `1.000` | `0.351` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `4333.23` | `0.486` | `0.889` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | example | - |
| `eslint-05` | `instruction_following` | `eslint` | `6346.50` | `0.447` | `0.630` | `1.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 4:12, @typescript-eslint/no-explicit-any | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `3144.31` | `0.386` | `1.000` | `0.286` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `1511.73` | `0.207` | `1.000` | `0.000` | `0.000` | `0.000` | `0.071` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `6390.37` | `0.241` | `1.000` | `0.129` | `0.000` | `0.000` | `0.444` | `soft_accepted` | structured_output_mismatch | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `1023.15` | `0.400` | `1.000` | `0.333` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `1735.30` | `0.803` | `1.000` | `0.714` | `0.833` | `0.722` | `0.556` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `3763.12` | `0.252` | `1.000` | `0.095` | `0.000` | `0.000` | `0.235` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `3446.89` | `0.235` | `1.000` | `0.000` | `0.000` | `0.000` | `0.355` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `55495.24` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | UserService.java:[44,17], findByEmail, UserController.java:[28,31], java.lang.Long, java.util.UUID | granite output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='- follow the requested structure exactly - bullets, headings, markdown, or code blocks are allowed only because the instruction asked for them - do not add e...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='- follow the requested structure exactly - bullets, headings, markdown, or code blocks are allowed only because the instruction asked for them - do not add e...' |
| `playwright-01` | `instruction_following` | `playwright` | `4329.23` | `0.290` | `1.000` | `0.095` | `0.000` | `0.000` | `0.611` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `1778.82` | `0.204` | `1.000` | `0.000` | `0.000` | `0.000` | `0.043` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `1810.63` | `0.099` | `0.333` | `0.000` | `0.000` | `0.000` | `0.500` | `soft_accepted` | missing_exact_anchors | CrashLoopBackOff, Error | - |
| `cargo-04` | `instruction_following` | `cargo` | `3022.50` | `0.142` | `0.333` | `0.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/auth.rs:88, Option::unwrap(), left: 1750, right: 1749 | - |
| `shell-01` | `instruction_following` | `shell` | `2936.84` | `0.275` | `1.000` | `0.170` | `0.000` | `0.000` | `0.237` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `7411.07` | `0.370` | `0.867` | `0.650` | `0.000` | `0.000` | `0.667` | `soft_accepted` | missing_exact_anchors | message | - |
| `terraform-10` | `structured` | `terraform` | `6702.14` | `0.253` | `0.667` | `0.381` | `0.000` | `0.000` | `0.500` | `soft_accepted` | missing_exact_anchors | resource, field | - |
| `junit-01` | `structured` | `junit` | `2985.70` | `0.335` | `0.286` | `0.867` | `0.000` | `0.000` | `0.765` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | Test, Error, Location, --- | - |
| `kubernetes-03` | `structured` | `kubernetes` | `4177.56` | `0.182` | `0.571` | `0.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | CrashLoopBackOff, restarts | - |
| `eslint-06` | `structured` | `eslint` | `3834.66` | `0.155` | `0.667` | `0.080` | `0.000` | `0.000` | `0.250` | `soft_accepted` | missing_exact_anchors | line, column, rule | - |
| `docker-build-04` | `structured` | `docker-build` | `4131.39` | `0.267` | `0.741` | `0.417` | `0.000` | `0.000` | `0.412` | `soft_accepted` | missing_exact_anchors | error | - |
| `go-test-04` | `structured` | `go-test` | `4820.38` | `0.387` | `0.879` | `0.714` | `0.000` | `0.000` | `0.647` | `soft_accepted` | missing_exact_anchors | message | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `2749.21` | `0.189` | `0.333` | `0.429` | `0.000` | `0.000` | `0.273` | `soft_accepted` | missing_exact_anchors | Job, Step, Exit, --- | - |
| `npm-07` | `structured` | `npm` | `5596.91` | `0.210` | `0.833` | `0.214` | `0.000` | `0.000` | `0.167` | `soft_accepted` | missing_exact_anchors | required | - |
| `mypy-06` | `structured` | `mypy` | `3775.05` | `0.145` | `0.333` | `0.095` | `0.000` | `0.000` | `0.750` | `soft_accepted` | missing_exact_anchors | File, Line, Code, Message, --- | - |
| `gradle-03` | `structured` | `gradle` | `2227.82` | `0.350` | `1.000` | `0.167` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `playwright-02` | `structured` | `playwright` | `3357.59` | `0.198` | `0.667` | `0.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | line, test | - |
| `postgres-04` | `structured` | `postgres` | `5226.24` | `0.295` | `0.424` | `0.683` | `0.000` | `0.000` | `0.577` | `soft_accepted` | missing_exact_anchors | errors, file, line, message | - |
| `vite-01` | `structured` | `vite` | `3237.36` | `0.114` | `0.600` | `0.000` | `0.000` | `0.000` | `0.143` | `soft_accepted` | missing_exact_anchors | /repo/apps/admin/src/App.tsx, /repo/apps/public/src/Home.tsx | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `2262.16` | `0.167` | `1.000` | `0.000` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `5130.71` | `0.157` | `1.000` | `0.000` | `0.000` | `0.000` | `0.143` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `4261.42` | `0.011` | `0.000` | `0.000` | `0.000` | `0.000` | `0.250` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | - |
| `npm-08` | `exact_format` | `npm` | `2553.84` | `0.163` | `1.000` | `0.000` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `5399.23` | `0.143` | `1.000` | `0.000` | `0.000` | `0.000` | `0.375` | `soft_accepted` | structured_output_mismatch | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `5089.28` | `0.136` | `1.000` | `0.000` | `0.000` | `0.000` | `0.200` | `soft_accepted` | structured_output_mismatch | - | - |
| `cargo-05` | `exact_format` | `cargo` | `4505.67` | `0.133` | `1.000` | `0.000` | `0.000` | `0.000` | `0.125` | `soft_accepted` | structured_output_mismatch | - | - |
| `curl-03` | `exact_format` | `curl` | `2607.59` | `0.131` | `1.000` | `0.000` | `0.000` | `0.000` | `0.091` | `soft_accepted` | structured_output_mismatch | - | - |
| `rails-02` | `exact_format` | `rails` | `5493.19` | `0.130` | `1.000` | `0.000` | `0.000` | `0.000` | `0.056` | `soft_accepted` | structured_output_mismatch | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `3451.72` | `0.482` | `1.000` | `0.333` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `1428.61` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `1533.14` | `0.351` | `1.000` | `0.103` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `1729.92` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `1759.55` | `0.561` | `1.000` | `0.122` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `10155.47` | `0.429` | `1.000` | `0.211` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `2347.69` | `0.445` | `0.583` | `0.213` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `1924.57` | `0.250` | `0.000` | `0.143` | `1.000` | `0.875` | `0.583` | `soft_accepted` | missing_exact_anchors | main.cpp:10:5, error: 'cout' was not declared in this scope | - |
| `testing-01` | `recall` | `testing` | `2950.11` | `0.466` | `0.643` | `0.000` | `1.000` | `0.876` | `0.588` | `soft_accepted` | missing_exact_anchors | TestCalculator::testDivideByZero | - |
| `testing-02` | `recall` | `testing` | `2545.79` | `0.374` | `0.364` | `0.095` | `1.000` | `0.859` | `0.529` | `soft_accepted` | missing_exact_anchors | Cannot read property 'foo' of undefined, /usr/src/app/index.js:12:15 | - |
| `package-management-01` | `recall` | `package-management` | `3276.03` | `0.535` | `0.615` | `0.211` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | GET https://registry.npmjs.org/foo | - |
| `runtime-02` | `recall` | `runtime` | `3449.31` | `0.720` | `1.000` | `0.130` | `1.000` | `0.814` | `0.378` | `accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `2842.07` | `0.712` | `1.000` | `0.114` | `1.000` | `0.800` | `0.333` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `1762.82` | `0.363` | `0.190` | `0.167` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | error[E0277], main.rs:5:26 | - |
| `ci-01` | `recall` | `ci` | `1722.60` | `0.305` | `0.000` | `0.235` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Error: Tests failed, 5 tests run, 1 failure | - |
| `testing-03` | `recall` | `testing` | `829.84` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `3083.54` | `0.555` | `0.778` | `0.171` | `1.000` | `0.880` | `0.600` | `soft_accepted` | missing_exact_anchors | BadRequest | - |
| `infrastructure-01` | `recall` | `infrastructure` | `3080.64` | `0.807` | `1.000` | `0.286` | `1.000` | `0.957` | `0.857` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `3982.50` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `2070.25` | `0.253` | `0.000` | `0.105` | `1.000` | `0.914` | `0.714` | `soft_accepted` | missing_exact_anchors | Installing npm modules, failed with exit code 1 | - |
| `build-01` | `recall` | `build` | `1568.24` | `0.508` | `0.588` | `0.133` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | BUILD FAILED | - |
| `container-runtime-01` | `recall` | `container-runtime` | `524.74` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `1836.46` | `0.263` | `0.000` | `0.095` | `1.000` | `0.957` | `0.857` | `soft_accepted` | missing_exact_anchors | package com.google.common does not exist, 1 error | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1745.02` | `0.479` | `0.500` | `0.154` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Unauthorized | - |
| `runtime-03` | `recall` | `runtime` | `1497.79` | `0.575` | `0.667` | `0.308` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | maximum recursion depth exceeded | - |
| `package-management-03` | `recall` | `package-management` | `4217.42` | `0.248` | `0.000` | `0.100` | `1.000` | `0.900` | `0.667` | `soft_accepted` | missing_exact_anchors | No matching distribution found, requests==3.0.0 | - |
| `infrastructure-03` | `recall` | `infrastructure` | `2213.21` | `0.531` | `0.636` | `0.182` | `1.000` | `0.979` | `0.929` | `soft_accepted` | missing_exact_anchors | no such file or directory | - |
| `testing-04` | `recall` | `testing` | `2468.72` | `0.319` | `0.167` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Failure/Error, capybara-3.34.0/lib/capybara/node/element.rb:1008 | - |
| `build-02` | `recall` | `build` | `2145.79` | `0.262` | `0.000` | `0.174` | `1.000` | `0.894` | `0.647` | `soft_accepted` | missing_exact_anchors | foo.c:5:2, error: expected ';' | - |
| `ci-03` | `recall` | `ci` | `2153.00` | `0.425` | `0.222` | `0.400` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERROR: failed to fetch, libssl1.0.0_1.0.2g-1ubuntu4.0_amd64.deb | - |
| `testing-05` | `recall` | `testing` | `415.36` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `1884.71` | `0.528` | `0.286` | `0.500` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | FAILURE: Build failed with an exception | - |
| `docker-05` | `summary` | `docker` | `2176.22` | `0.314` | `0.000` | `0.143` | `1.000` | `0.925` | `0.750` | `soft_accepted` | missing_exact_anchors | healthcheck status: unhealthy | - |
| `kubernetes-05` | `summary` | `kubernetes` | `875.20` | `0.332` | `0.000` | `0.250` | `1.000` | `0.880` | `0.600` | `soft_accepted` | missing_exact_anchors | rolled out successfully | - |
| `ci-04` | `summary` | `ci` | `1612.31` | `0.366` | `0.524` | `0.000` | `1.000` | `0.900` | `0.667` | `soft_accepted` | missing_exact_anchors | Success: | - |
| `npm-09` | `summary` | `npm` | `2952.08` | `0.227` | `0.000` | `0.100` | `1.000` | `0.753` | `0.176` | `soft_accepted` | missing_exact_anchors | ERESOLVE, unable to resolve dependency tree | - |
| `rust-02` | `summary` | `rust` | `1966.35` | `0.567` | `1.000` | `0.000` | `1.000` | `0.933` | `0.778` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `5885.16` | `0.300` | `1.000` | `0.000` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `4189.72` | `0.600` | `1.000` | `1.000` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `4985.75` | `0.174` | `1.000` | `0.000` | `0.000` | `0.000` | `0.048` | `soft_accepted` | structured_output_mismatch | - | - |
| `linting-02` | `structured` | `linting` | `759.49` | `0.433` | `1.000` | `0.444` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `2774.18` | `0.450` | `1.000` | `0.500` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `1582.32` | `0.295` | `1.000` | `0.222` | `0.000` | `0.000` | `0.286` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `3049.38` | `0.255` | `1.000` | `1.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `shell-02` | `exact_format` | `shell` | `5463.32` | `0.170` | `1.000` | `0.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `shell-03` | `exact_format` | `shell` | `3390.63` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | OUTPUT: | granite output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Raw output: step1 value1 step2' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='OUTPUT: - keep the response concise - if the instruction requires exact quoted material or a longer structured answer, prioritize correctness instead' |
| `shell-04` | `exact_format` | `shell` | `3935.39` | `0.170` | `1.000` | `0.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `build-04` | `exact_format` | `build` | `3442.98` | `0.079` | `0.286` | `0.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors, verbatim_alignment_weak | Resources: 1 added | - |
| `build-05` | `exact_format` | `build` | `1792.66` | `0.170` | `1.000` | `0.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `shell-05` | `exact_format` | `shell` | `3033.83` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | PATH | granite output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='- return the exact requested lines or quoted excerpts only - copy quoted or extracted lines exactly from the raw output - do not summarize unless the instruc...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='- return the exact requested lines or quoted excerpts only - copy quoted or extracted lines exactly from the raw output - do not summarize unless the instruc...' |
| `deployment-03` | `explanation` | `deployment` | `1587.12` | `0.395` | `0.000` | `0.357` | `1.000` | `0.960` | `0.867` | `soft_accepted` | missing_exact_anchors | No module named 'requests' | - |
| `runtime-04` | `explanation` | `runtime` | `2303.56` | `0.342` | `0.000` | `0.320` | `1.000` | `0.829` | `0.429` | `soft_accepted` | missing_exact_anchors | IndexError: list index out of range | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `1917.07` | `0.615` | `1.000` | `0.231` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `983.15` | `0.656` | `1.000` | `0.312` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `1556.08` | `0.389` | `0.333` | `0.182` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | SIGSEGV | - |
| `runtime-06` | `explanation` | `runtime` | `1144.09` | `0.402` | `0.000` | `0.345` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | KeyError: 'username' | - |
| `deployment-04` | `explanation` | `deployment` | `4014.35` | `0.310` | `0.000` | `0.242` | `1.000` | `0.830` | `0.435` | `soft_accepted` | missing_exact_anchors | password authentication failed | - |
| `explanation-01` | `explanation` | `explanation` | `1817.71` | `0.625` | `1.000` | `0.250` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1306.42` | `0.373` | `0.000` | `0.320` | `1.000` | `0.936` | `0.786` | `soft_accepted` | missing_exact_anchors | toUpperCase is not a function | - |
| `explanation-03` | `explanation` | `explanation` | `1998.27` | `0.446` | `0.000` | `0.471` | `1.000` | `0.967` | `0.889` | `soft_accepted` | missing_exact_anchors | no configured push destination | - |
| `explanation-04` | `explanation` | `explanation` | `1559.96` | `0.384` | `0.000` | `0.303` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | exited with 1 | - |
| `explanation-05` | `explanation` | `explanation` | `1340.60` | `0.733` | `1.000` | `0.467` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `932.69` | `0.717` | `1.000` | `0.500` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `1851.70` | `0.386` | `0.000` | `0.333` | `1.000` | `0.962` | `0.875` | `soft_accepted` | missing_exact_anchors | SECRET_KEY setting must not be empty | - |
| `explanation-08` | `explanation` | `explanation` | `2372.54` | `0.276` | `0.000` | `0.077` | `1.000` | `0.957` | `0.857` | `soft_accepted` | missing_exact_anchors | Unable to locate credentials | - |
| `explanation-09` | `explanation` | `explanation` | `1477.73` | `0.625` | `1.000` | `0.250` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `1682.50` | `0.346` | `0.000` | `0.286` | `1.000` | `0.894` | `0.647` | `soft_accepted` | missing_exact_anchors | KeyError: 'API_KEY' | - |
| `explanation-11` | `explanation` | `explanation` | `2214.61` | `0.391` | `0.000` | `0.400` | `1.000` | `0.880` | `0.600` | `soft_accepted` | missing_exact_anchors | Address already in use | - |
| `explanation-12` | `explanation` | `explanation` | `1533.02` | `0.449` | `0.000` | `0.500` | `1.000` | `0.933` | `0.778` | `soft_accepted` | missing_exact_anchors | OOMKilled | - |
| `ci-07` | `structured` | `ci` | `2258.57` | `0.450` | `1.000` | `0.500` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `1730.57` | `0.295` | `1.000` | `0.222` | `0.000` | `0.000` | `0.286` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `1999.48` | `0.255` | `1.000` | `1.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `shell-06` | `exact_format` | `shell` | `6041.11` | `0.170` | `1.000` | `0.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `shell-07` | `exact_format` | `shell` | `3343.43` | `0.170` | `1.000` | `0.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `build-06` | `exact_format` | `build` | `3243.92` | `0.079` | `0.286` | `0.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors, verbatim_alignment_weak | Resources: 1 added | - |
| `runtime-07` | `exact_format` | `runtime` | `2607.43` | `0.255` | `1.000` | `1.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `build-07` | `exact_format` | `build` | `4889.41` | `0.263` | `1.000` | `0.800` | `0.000` | `0.000` | `0.667` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `2595.98` | `0.170` | `1.000` | `0.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `deployment-05` | `explanation` | `deployment` | `1408.03` | `0.395` | `0.000` | `0.357` | `1.000` | `0.960` | `0.867` | `soft_accepted` | missing_exact_anchors | No module named 'requests' | - |
| `deployment-06` | `explanation` | `deployment` | `2562.76` | `0.342` | `0.000` | `0.320` | `1.000` | `0.829` | `0.429` | `soft_accepted` | missing_exact_anchors | IndexError: list index out of range | - |
| `deployment-07` | `explanation` | `deployment` | `1543.07` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `1719.99` | `0.591` | `1.000` | `0.182` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `2209.76` | `0.310` | `0.000` | `0.242` | `1.000` | `0.830` | `0.435` | `soft_accepted` | missing_exact_anchors | password authentication failed | - |
| `explanation-15` | `explanation` | `explanation` | `3535.35` | `0.611` | `1.000` | `0.270` | `1.000` | `0.929` | `0.762` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `912.29` | `0.561` | `1.000` | `0.171` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `1852.33` | `0.303` | `0.000` | `0.207` | `1.000` | `0.858` | `0.526` | `soft_accepted` | missing_exact_anchors | missing script: start | - |
| `package-management-04` | `explanation` | `package-management` | `1719.96` | `0.471` | `0.444` | `0.370` | `1.000` | `0.940` | `0.800` | `soft_accepted` | missing_exact_anchors | nonexistent (invalid) version of flask | - |
