# gpu-qwen3.5-0.8b-no-quant

## Scenario

- track: `gpu`
- phase: `gpu-screen`
- model: `Qwen/Qwen3.5-0.8B`
- quantization: `none`
- device: `cuda`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `12516.82`
- cpu_rss_bytes: `2808651776`
- gpu_peak_bytes: `2763202560`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `268`
- accepted_count: `224`
- soft_accepted_count: `44`
- rejected_count: `12`
- exact_pass_count: `231`
- avg_inference_ms: `12708.46`
- p95_inference_ms: `46749.62`
- avg_exact_preservation_ratio: `0.916`
- avg_summary_quality_ratio: `0.809`
- avg_format_adherence_score: `0.772`
- avg_instruction_following_score: `0.759`
- avg_brevity_ratio: `0.890`
- avg_case_score: `0.786`
- p10_case_score: `0.277`
- quality_core: `0.685`
- latency_factor: `0.850`
- final_score: `58.19`
- peak_cpu_rss_bytes: `2812207104`
- peak_gpu_bytes: `2899504128`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `70826.91` | `0.689` | `1.000` | `0.898` | `0.500` | `0.404` | `0.358` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-02` | `summary` | `python` | `20908.74` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='- python services/worker.py --queue emails --concurrency 4 - /workspace/services/worker.py - line 11 - ModuleNotFoundError - dramatiq_abort - worker boot fai...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass="$ python services/worker.py --queue emails --concurrency 4 INFO boot: reading .env.local WARNING redis retry 1/3 failed: ConnectionResetError(104, 'Connectio..." |
| `python-03` | `recall` | `python` | `4502.49` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `6136.01` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `5613.66` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `6032.50` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `6635.72` | `0.681` | `0.326` | `0.924` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/integration -k billing -vv --maxfail=1, tests/integration/test_billing_api.py::test_invoice_webhook_uses_signature, 1 error in 2.31s | - |
| `pytest-03` | `recall` | `pytest` | `25839.24` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | pytest tests -q -x, tests/jobs/test_retention.py::test_archive_marks_job_deleted, teardown, psycopg.errors.ForeignKeyViolation, job_runs_job_id_fkey, 149 passed, 1 skipped, 1 error in 58.73s | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='- pytest tests -q -x - tests/jobs/test_retention.py::test_archive_marks_job_deleted - teardown - psycopg.errors.ForeignKeyViolation - job_runs_job_id_fkey - ...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='ERROR at teardown of test_archive_marks_job_deleted self = <sqlalchemy.engine.base.Connection object at 0x7ff2d0184890> def exec_single_context(self, dialect...' |
| `pytest-04` | `recall` | `pytest` | `6659.15` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `5856.66` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `5759.87` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `5492.59` | `0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `11364.73` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `5292.46` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-02` | `summary` | `ruff` | `4634.23` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `4676.50` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `4806.14` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `7726.47` | `0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `5808.74` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `5240.82` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `5037.64` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `3936.46` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `8432.99` | `0.978` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `6200.92` | `0.979` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `9025.73` | `0.785` | `0.800` | `0.934` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Lifecycle script `build` failed, storefront@2.8.1 | - |
| `pnpm-01` | `recall` | `pnpm` | `10400.34` | `0.802` | `0.895` | `0.963` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --no-frozen-lockfile | - |
| `pnpm-02` | `summary` | `pnpm` | `21861.65` | `0.979` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `6442.98` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `9106.20` | `0.983` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `6829.38` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `42721.62` | `0.699` | `1.000` | `0.956` | `0.500` | `0.440` | `0.603` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `eslint-01` | `recall` | `eslint` | `17393.08` | `0.809` | `0.920` | `0.949` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Unused eslint-disable directive | - |
| `eslint-02` | `summary` | `eslint` | `4361.18` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `9243.93` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `10337.75` | `0.984` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `3872.47` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `6804.56` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `2235.06` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `8142.85` | `0.795` | `0.875` | `0.968` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | demo-app-1 | - |
| `docker-compose-03` | `summary` | `docker-compose` | `13882.98` | `0.737` | `0.600` | `0.919` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker compose up api | - |
| `kubectl-01` | `summary` | `kubectl` | `4824.36` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `56395.27` | `0.909` | `1.000` | `0.947` | `1.000` | `0.767` | `0.222` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `3995.06` | `0.995` | `1.000` | `0.988` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `9382.33` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `4284.89` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `38100.63` | `0.716` | `0.789` | `0.925` | `1.000` | `0.869` | `0.562` | `soft_accepted` | missing_exact_anchors | aws_security_group.db.id, Reference to undeclared resource | - |
| `terraform-03` | `recall` | `terraform` | `14163.41` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `5517.46` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `5964.00` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `16239.48` | `0.963` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `3372.96` | `0.972` | `1.000` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `23288.30` | `0.905` | `1.000` | `0.867` | `1.000` | `0.816` | `0.386` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `4257.90` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `7409.95` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `14312.75` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | curl -I https://docs.example.com/sdk/latest, HTTP/2 301, location: /sdk/v3.4/, cache-control: max-age=3600 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='curl -I https://docs.example.com/sdk/latest HTTP/2 301 location: /sdk/v3.4/ cache-control: max-age=3600 server: envoy via: 1.1 edge x-request-id: 7e9f7a4d<|i...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='curl -I https://docs.example.com/sdk/latest HTTP/2 301 location: /sdk/v3.4/ cache-control: max-age=3600 server: envoy via: 1.1 edge x-request-id: 7e9f7a4d<|i...' |
| `ssh-01` | `summary` | `ssh` | `9949.90` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `4100.51` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `5414.31` | `0.760` | `0.677` | `0.936` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | status=203/EXEC | - |
| `systemd-02` | `summary` | `systemd` | `2743.64` | `0.962` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `4195.76` | `0.977` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `24375.77` | `0.943` | `1.000` | `0.951` | `1.000` | `0.864` | `0.548` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `27216.50` | `0.962` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `48994.36` | `0.914` | `1.000` | `0.936` | `1.000` | `0.880` | `0.600` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `90230.08` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `18638.25` | `0.594` | `0.304` | `0.931` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | mvn -q test, UserControllerTest.java:72, /workspace/webapp/target/surefire-reports | - |
| `maven-02` | `summary` | `maven` | `5479.13` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `5619.97` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `24760.46` | `0.895` | `1.000` | `0.916` | `1.000` | `0.858` | `0.525` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `22577.27` | `0.974` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `3721.41` | `0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `9152.28` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-04` | `summary` | `npm` | `5204.76` | `0.974` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `12761.91` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `4778.75` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `26714.39` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `8020.70` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `13506.49` | `0.972` | `1.000` | `0.939` | `1.000` | `0.992` | `0.972` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `11512.85` | `0.801` | `0.911` | `0.910` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | zod@3.23.8 | - |
| `docker-compose-04` | `summary` | `docker-compose` | `4171.94` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `3365.12` | `0.982` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `75857.73` | `0.827` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `7173.77` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `8460.17` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `9093.13` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `7103.46` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `4507.13` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `13386.41` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `9717.41` | `0.684` | `0.600` | `0.939` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | psql -h 127.0.0.1 -U app_user -d appdb -c 'select 1' | - |
| `postgres-02` | `summary` | `postgres` | `27837.51` | `0.963` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `7149.07` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `7202.59` | `0.732` | `0.667` | `0.861` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mysql -h db.example.net -u app -D appdb -e "SELECT id, createdAt FROM users LIMIT 5" | - |
| `redis-01` | `summary` | `redis` | `11632.69` | `0.951` | `1.000` | `0.952` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `4438.42` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `10787.15` | `0.643` | `0.524` | `0.883` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | line=91, Ruff F821, exit code 2 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `58845.16` | `0.859` | `1.000` | `0.927` | `1.000` | `0.777` | `0.255` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `3445.48` | `0.968` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `5357.52` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `10552.40` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `4427.76` | `0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `5001.75` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `11803.59` | `0.664` | `0.545` | `0.944` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/unit/test_invoice_totals.py::test_discount_rounding, tests/unit/test_invoice_totals.py:88 | - |
| `compiler-error-01` | `recall` | `compiler-error` | `85206.55` | `0.634` | `0.851` | `0.904` | `0.500` | `0.405` | `0.369` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | src/router.rs:128 | - |
| `ci-log-01` | `recall` | `ci-log` | `21405.16` | `0.960` | `1.000` | `0.927` | `1.000` | `0.936` | `0.786` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `47890.09` | `0.912` | `1.000` | `0.955` | `1.000` | `0.771` | `0.236` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `19792.55` | `0.880` | `1.000` | `0.951` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `build-log-01` | `summary` | `build-log` | `13459.47` | `0.739` | `0.562` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | InvoiceMapper.java:[58,29], cannot find symbol | - |
| `docker-build-02` | `summary` | `docker-build` | `49007.54` | `0.639` | `1.000` | `0.883` | `0.000` | `0.000` | `0.240` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `37018.46` | `0.294` | `0.625` | `0.680` | `0.000` | `0.000` | `0.167` | `soft_accepted` | missing_exact_anchors | @typescript-eslint/no-misused-promises, @typescript-eslint/no-explicit-any, @typescript-eslint/no-unsafe-assignment | - |
| `git-review-01` | `instruction_following` | `git-review` | `29074.19` | `0.672` | `1.000` | `0.732` | `0.429` | `0.404` | `0.810` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `6321.62` | `0.515` | `1.000` | `0.717` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-01` | `structured` | `structured-output` | `22050.64` | `0.355` | `1.000` | `0.184` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `23240.06` | `0.438` | `0.905` | `0.853` | `0.000` | `0.000` | `0.781` | `soft_accepted` | missing_exact_anchors | port 5432 is already allocated | - |
| `structured-output-03` | `structured` | `structured-output` | `24885.55` | `0.375` | `0.929` | `0.518` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "refresh token expired" | - |
| `structured-output-04` | `structured` | `structured-output` | `15244.55` | `0.256` | `1.000` | `0.175` | `0.000` | `0.000` | `0.036` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `6918.50` | `0.234` | `1.000` | `0.343` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `12631.41` | `0.160` | `0.714` | `0.315` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | SearchBox debounces network query before fetch | - |
| `exact-format-03` | `exact_format` | `exact-format` | `8676.83` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `2520.10` | `0.957` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `13755.28` | `0.752` | `0.750` | `0.868` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `23539.79` | `0.850` | `1.000` | `0.900` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `36845.53` | `0.963` | `1.000` | `0.945` | `1.000` | `0.931` | `0.769` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `25565.26` | `0.980` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `9690.04` | `0.984` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `12744.75` | `0.748` | `0.783` | `0.913` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | InventorySyncTest.java:132 | - |
| `kubernetes-01` | `recall` | `kubernetes` | `44631.61` | `0.960` | `1.000` | `0.919` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `5971.47` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `7016.41` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `5413.31` | `0.987` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `14519.54` | `0.770` | `0.821` | `0.944` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | packages/api/src/index.ts:4:25 | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `97791.41` | `0.711` | `0.667` | `0.947` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 20260518_add_workspace_limits.sql, packages/db/test/migrate.test.ts:44:7 | - |
| `pnpm-04` | `recall` | `pnpm` | `7727.72` | `0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `4520.60` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `6552.56` | `0.983` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `15866.59` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `8063.19` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `4977.36` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `8008.09` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `5581.81` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `30761.16` | `0.983` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `7828.26` | `0.716` | `0.688` | `0.931` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | .\scripts\release.ps1 -Version 1.4.2 | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `5223.69` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `6494.98` | `0.969` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `29231.19` | `0.752` | `0.684` | `0.910` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ./integration | - |
| `npm-05` | `summary` | `npm` | `13400.89` | `0.715` | `0.533` | `0.896` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | web@1.2.0, src/pages/admin.tsx | - |
| `helm-01` | `summary` | `helm` | `91789.46` | `0.853` | `1.000` | `0.904` | `1.000` | `0.782` | `0.274` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `10743.74` | `0.951` | `1.000` | `0.877` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `29230.18` | `0.966` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `14107.27` | `0.951` | `1.000` | `0.941` | `1.000` | `0.949` | `0.830` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `15911.80` | `0.965` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `12518.83` | `0.807` | `0.909` | `0.931` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | -Iinclude | - |
| `python-pytest-02` | `summary` | `python-pytest` | `20428.82` | `0.965` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `15243.52` | `0.960` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `13846.23` | `0.784` | `0.833` | `0.910` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `15025.63` | `0.785` | `0.814` | `0.926` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | FAILED | - |
| `wrangler-01` | `summary` | `wrangler` | `16762.79` | `0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `6390.61` | `0.970` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `21225.65` | `0.431` | `1.000` | `0.673` | `0.000` | `0.000` | `0.286` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `4390.62` | `0.962` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `2619.31` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `8300.85` | `0.739` | `1.000` | `0.716` | `0.667` | `0.581` | `0.571` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `3426.34` | `0.940` | `1.000` | `0.799` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `4293.24` | `0.682` | `1.000` | `0.739` | `0.400` | `0.400` | `1.000` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `25165.67` | `0.417` | `1.000` | `0.685` | `0.000` | `0.000` | `0.111` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `5143.06` | `0.546` | `0.667` | `0.696` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors | aws_db_instance.main | - |
| `maven-03` | `instruction_following` | `maven` | `9294.84` | `0.582` | `1.000` | `0.942` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `4765.89` | `0.526` | `1.000` | `0.754` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `2284.41` | `0.719` | `1.000` | `0.729` | `0.667` | `0.533` | `0.333` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `6280.88` | `0.512` | `1.000` | `0.707` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `8779.86` | `0.653` | `1.000` | `0.733` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `10220.80` | `0.487` | `1.000` | `0.780` | `0.000` | `0.000` | `0.529` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `19431.68` | `0.503` | `1.000` | `0.779` | `0.000` | `0.000` | `0.696` | `accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `17104.95` | `0.293` | `1.000` | `0.186` | `0.000` | `0.000` | `0.368` | `accepted` | - | - | - |
| `junit-01` | `structured` | `junit` | `15682.76` | `0.354` | `1.000` | `0.180` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `19039.48` | `0.280` | `1.000` | `0.193` | `0.000` | `0.000` | `0.222` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `49598.17` | `0.132` | `0.444` | `0.171` | `0.000` | `0.000` | `0.152` | `soft_accepted` | missing_exact_anchors | src/a.ts, src/b.ts | - |
| `docker-build-04` | `structured` | `docker-build` | `8528.44` | `0.796` | `1.000` | `0.702` | `0.714` | `0.714` | `1.000` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `10748.79` | `0.562` | `1.000` | `0.900` | `0.000` | `0.000` | `0.917` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `9010.03` | `0.817` | `1.000` | `0.633` | `1.000` | `0.782` | `0.273` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `16300.73` | `0.679` | `1.000` | `0.594` | `0.714` | `0.533` | `0.154` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `10984.57` | `0.329` | `1.000` | `0.190` | `0.000` | `0.000` | `0.720` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `13606.87` | `0.310` | `1.000` | `0.317` | `0.000` | `0.000` | `0.700` | `soft_accepted` | structured_output_mismatch | - | - |
| `playwright-02` | `structured` | `playwright` | `182052.88` | `0.108` | `0.167` | `0.279` | `0.000` | `0.000` | `0.104` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | project, chromium, file, line, test | - |
| `postgres-04` | `structured` | `postgres` | `21300.78` | `0.403` | `1.000` | `0.578` | `0.000` | `0.000` | `0.294` | `accepted` | - | - | - |
| `vite-01` | `structured` | `vite` | `9821.66` | `0.260` | `1.000` | `0.183` | `0.000` | `0.000` | `0.053` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `8660.57` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | tests/test_a.py::test_one, tests/test_b.py::TestB::test_three | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='FAILED tests/test_a.py::test_one - AssertionError PASSED tests/test_a.py::test_two FAILED tests/test_b.py::TestB::test_three - TimeoutError<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='FAILED tests/test_a.py::test_one - AssertionError PASSED tests/test_a.py::test_two FAILED tests/test_b.py::TestB::test_three - TimeoutError<|im_end|>' |
| `git-04` | `exact_format` | `git` | `14423.09` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass="Merge made by the 'ort' strategy. commit 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 Author: CI Bot Status: deployed to staging<|im_end|>" repair_status=rejected repair_flags=['control_token_leakage'] repair_pass="Merge made by the 'ort' strategy. commit 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 Author: CI Bot Status: deployed to staging<|im_end|>" |
| `docker-04` | `exact_format` | `docker` | `13389.67` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444<|im_end|>' |
| `npm-08` | `exact_format` | `npm` | `2015.18` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 2.18.4 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='2.18.4<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='2.18.4<|im_end|>' |
| `go-test-05` | `exact_format` | `go-test` | `3810.02` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | github.com/acme/shop/checkout, TestCheckoutAppliesCoupon | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='github.com/acme/shop/checkout 0.31s<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='github.com/acme/shop/checkout 0.31s<|im_end|>' |
| `kubectl-09` | `exact_format` | `kubectl` | `5986.11` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | migrator-v2-9xk, prod | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='migrator-v2-9xk 0/1 Error 0 33m<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='migrator-v2-9xk 0/1 Error 0 33m namespace: prod<|im_end|>' |
| `cargo-05` | `exact_format` | `cargo` | `9441.51` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | auth::tests::rejects_expired, billing::tests::rounds_half_even | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='failures: auth::tests::rejects_expired billing::tests::rounds_half_even test result: FAILED. 40 passed; 2 failed<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='failures: auth::tests::rejects_expired billing::tests::rounds_half_even test result: FAILED. 40 passed; 2 failed<|im_end|>' |
| `curl-03` | `exact_format` | `curl` | `1224.89` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 503 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='503<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='503<|im_end|>' |
| `rails-02` | `exact_format` | `rails` | `5205.38` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 20260518133742 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='PG::DuplicateColumn: ERROR: column "tenant_id" of relation "users" already exists<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='PG::DuplicateColumn: ERROR: column "tenant_id" of relation "users" already exists<|im_end|>' |
| `python-traceback-02` | `explanation` | `python-traceback` | `5895.99` | `0.962` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `10035.85` | `0.945` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `4191.39` | `0.951` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `3392.72` | `0.783` | `0.818` | `0.914` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | outside the build context | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `3789.77` | `0.960` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `13471.42` | `0.691` | `1.000` | `0.826` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `9389.97` | `0.715` | `0.583` | `0.848` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `2587.98` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `3128.37` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `18665.71` | `0.711` | `1.000` | `0.944` | `0.500` | `0.425` | `0.500` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `package-management-01` | `recall` | `package-management` | `8257.35` | `0.976` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `6460.99` | `0.719` | `0.667` | `0.983` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `4042.15` | `0.983` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `9327.37` | `0.964` | `1.000` | `0.923` | `1.000` | `0.950` | `0.833` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `3455.98` | `0.964` | `1.000` | `0.855` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `6312.27` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `7127.37` | `0.952` | `1.000` | `0.892` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `94508.86` | `0.891` | `1.000` | `0.903` | `1.000` | `0.747` | `0.158` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `2988.93` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `5769.37` | `0.965` | `1.000` | `0.860` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `9267.56` | `0.963` | `1.000` | `0.896` | `1.000` | `0.967` | `0.889` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `4793.60` | `0.973` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `5603.54` | `0.972` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1676.02` | `0.967` | `1.000` | `0.867` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `1333.60` | `0.991` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `4986.38` | `0.972` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `10845.91` | `0.936` | `1.000` | `0.906` | `1.000` | `0.877` | `0.591` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `25514.09` | `0.948` | `1.000` | `0.906` | `1.000` | `0.914` | `0.714` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `7715.36` | `0.614` | `0.500` | `0.930` | `1.000` | `0.894` | `0.647` | `soft_accepted` | missing_exact_anchors | foo.c:5:2 | - |
| `ci-03` | `recall` | `ci` | `17408.37` | `0.800` | `1.000` | `0.892` | `1.000` | `0.905` | `0.682` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `3638.90` | `0.976` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `3968.48` | `0.943` | `1.000` | `0.858` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `992.85` | `0.945` | `1.000` | `0.862` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `715.83` | `0.935` | `1.000` | `0.837` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `1543.73` | `0.953` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `1380.32` | `0.969` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `626.10` | `0.936` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `5576.14` | `0.526` | `1.000` | `0.863` | `0.000` | `0.000` | `0.667` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `2424.04` | `0.922` | `1.000` | `0.739` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `2314.31` | `0.688` | `1.000` | `0.628` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `linting-02` | `structured` | `linting` | `5469.84` | `0.721` | `1.000` | `0.513` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `7830.29` | `0.358` | `1.000` | `0.195` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `2792.38` | `0.500` | `1.000` | `0.666` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `3750.07` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `971.39` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `2580.86` | `0.252` | `1.000` | `0.765` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `2089.03` | `0.208` | `1.000` | `0.492` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `9747.74` | `0.279` | `1.000` | `0.905` | `0.000` | `0.000` | `0.778` | `accepted` | - | - | - |
| `build-05` | `exact_format` | `build` | `2825.58` | `0.225` | `1.000` | `0.609` | `0.000` | `0.000` | `0.286` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `1483.60` | `0.232` | `1.000` | `0.658` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `1089.83` | `0.935` | `1.000` | `0.870` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `1217.64` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `5856.56` | `0.958` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `1038.28` | `0.950` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `6735.57` | `0.903` | `1.000` | `0.877` | `1.000` | `0.894` | `0.647` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `968.94` | `0.931` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `1381.51` | `0.937` | `1.000` | `0.873` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `1106.18` | `0.931` | `1.000` | `0.861` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1139.84` | `0.913` | `1.000` | `0.825` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `1037.41` | `0.944` | `1.000` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `1584.90` | `0.937` | `1.000` | `0.875` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `3339.89` | `0.947` | `1.000` | `0.894` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `2562.99` | `0.907` | `1.000` | `0.814` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `1349.95` | `0.932` | `1.000` | `0.864` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `851.17` | `0.920` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `997.91` | `0.902` | `1.000` | `0.805` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `1095.85` | `0.948` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `817.33` | `0.916` | `1.000` | `0.833` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `834.84` | `0.875` | `1.000` | `0.751` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `7097.94` | `0.358` | `1.000` | `0.195` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `2699.33` | `0.500` | `1.000` | `0.666` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `3543.31` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `1065.24` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `15456.60` | `0.700` | `1.000` | `0.335` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `9383.65` | `0.279` | `1.000` | `0.905` | `0.000` | `0.000` | `0.778` | `accepted` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `1570.00` | `0.207` | `1.000` | `0.325` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `950.61` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `863.99` | `0.232` | `1.000` | `0.653` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `1097.30` | `0.935` | `1.000` | `0.870` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `1206.70` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `1209.55` | `0.959` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `7913.86` | `0.970` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `1303.34` | `0.937` | `1.000` | `0.873` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `1139.96` | `0.960` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `877.80` | `0.913` | `1.000` | `0.825` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `834.00` | `0.928` | `1.000` | `0.855` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1995.37` | `0.932` | `1.000` | `0.864` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
