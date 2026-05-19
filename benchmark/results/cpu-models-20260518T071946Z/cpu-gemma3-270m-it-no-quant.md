# cpu-gemma3-270m-it-no-quant

## Scenario

- track: `cpu`
- phase: `cpu-screen`
- model: `unsloth/gemma-3-270m-it-GGUF`
- quantization: `none`
- device: `cpu`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `5003.43`
- cpu_rss_bytes: `null`
- gpu_peak_bytes: `null`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `269`
- accepted_count: `162`
- soft_accepted_count: `107`
- rejected_count: `11`
- exact_pass_count: `180`
- avg_inference_ms: `4781.92`
- p95_inference_ms: `15778.63`
- avg_exact_preservation_ratio: `0.752`
- avg_summary_quality_ratio: `0.752`
- avg_format_adherence_score: `0.709`
- avg_instruction_following_score: `0.658`
- avg_brevity_ratio: `0.686`
- avg_case_score: `0.658`
- p10_case_score: `0.183`
- quality_core: `0.563`
- latency_factor: `0.877`
- final_score: `49.43`
- peak_cpu_rss_bytes: `null`
- peak_gpu_bytes: `null`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `5316.95` | `0.369` | `0.000` | `0.697` | `1.000` | `0.880` | `0.600` | `soft_accepted` | missing_exact_anchors | python -m app.cli sync --config config/settings.json, /workspace/app/config.py, line 27, JSONDecodeError, line 18 column 3, config/settings.json | - |
| `python-02` | `summary` | `python` | `1968.11` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='- return the exact requested lines or quoted excerpts only - copy quoted or extracted lines exactly from the raw output - do not summarize unless the instruc...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='- return the exact requested lines or quoted excerpts only - copy quoted or extracted lines exactly from the raw output - do not summarize unless the instruc...' |
| `python-03` | `recall` | `python` | `17232.24` | `0.687` | `1.000` | `0.911` | `0.500` | `0.397` | `0.311` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-04` | `recall` | `python` | `5347.22` | `0.385` | `0.000` | `0.783` | `1.000` | `0.870` | `0.568` | `soft_accepted` | missing_exact_anchors | python -m jobs.refresh_catalog --region us-east-1, /workspace/src/jobs/refresh_catalog.py, line 119, httpx.ReadTimeout, catalog?page=2, us-east-1 | - |
| `python-05` | `recall` | `python` | `7388.20` | `0.514` | `0.407` | `0.794` | `1.000` | `0.769` | `0.232` | `soft_accepted` | missing_exact_anchors | python tools/export_report.py --input data/may.csv --format parquet, /workspace/src/reports/export.py, line 131 | - |
| `pytest-01` | `recall` | `pytest` | `4379.79` | `0.449` | `0.091` | `0.874` | `1.000` | `0.907` | `0.690` | `soft_accepted` | missing_exact_anchors | pytest tests/api/test_users.py -q, tests/api/test_users.py::test_create_user_rejects_duplicate[email], tests/api/test_users.py:47, AssertionError | - |
| `pytest-02` | `summary` | `pytest` | `16213.58` | `0.547` | `0.000` | `0.732` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/integration -k billing -vv --maxfail=1, tests/integration/test_billing_api.py::test_invoice_webhook_uses_signature, signed_payload, /workspace/tests/integration/test_billing_api.py:73, 1 error in 2.31s | - |
| `pytest-03` | `recall` | `pytest` | `29602.52` | `0.437` | `0.182` | `0.889` | `1.000` | `0.731` | `0.103` | `soft_accepted` | missing_exact_anchors, verbatim_alignment_weak | pytest tests -q -x, tests/jobs/test_retention.py::test_archive_marks_job_deleted, psycopg.errors.ForeignKeyViolation, 149 passed, 1 skipped, 1 error in 58.73s | - |
| `pytest-04` | `recall` | `pytest` | `15050.52` | `0.414` | `0.100` | `0.854` | `1.000` | `0.785` | `0.282` | `soft_accepted` | missing_exact_anchors | pytest tests/cli/test_export.py -q, /workspace/tests/cli/test_export.py:12, PytestUnknownMarkWarning, 4 passed, 1 warning in 0.18s | - |
| `pytest-05` | `summary` | `pytest` | `20725.93` | `0.667` | `1.000` | `0.928` | `0.500` | `0.413` | `0.423` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `mypy-01` | `recall` | `mypy` | `1559.09` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `4079.15` | `0.905` | `1.000` | `0.935` | `1.000` | `0.862` | `0.538` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `2227.54` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `2865.22` | `0.880` | `0.911` | `0.927` | `1.000` | `0.864` | `0.545` | `accepted` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `719.64` | `0.977` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `1581.23` | `0.968` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `3405.10` | `0.373` | `0.000` | `0.690` | `1.000` | `0.900` | `0.667` | `soft_accepted` | missing_exact_anchors | pylint src/storage/path_utils.py, src/storage/path_utils.py:27:18, E1101, no-member, mothers, Path | - |
| `pylint-02` | `recall` | `pylint` | `4403.83` | `0.388` | `0.000` | `0.703` | `1.000` | `0.942` | `0.806` | `soft_accepted` | missing_exact_anchors | pylint src/config/runtime.py src/api/server.py, src/config/runtime.py:44:0, F0010, parse-error, expected ":", src/api/server.py | - |
| `pylint-03` | `summary` | `pylint` | `1802.87` | `0.970` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `1792.83` | `0.789` | `0.800` | `0.945` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 2 files would be reformatted, 41 files would be left unchanged | - |
| `black-02` | `summary` | `black` | `2088.87` | `0.768` | `0.766` | `0.905` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 1 file failed to reformat, 1 file reformatted | - |
| `black-03` | `recall` | `black` | `804.01` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `6992.00` | `0.725` | `0.810` | `0.909` | `1.000` | `0.886` | `0.621` | `soft_accepted` | missing_exact_anchors | EUSAGE | - |
| `npm-02` | `summary` | `npm` | `4937.83` | `0.872` | `1.000` | `0.916` | `1.000` | `0.811` | `0.368` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `3870.21` | `0.941` | `1.000` | `0.947` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `3083.20` | `0.797` | `0.895` | `0.939` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --no-frozen-lockfile | - |
| `pnpm-02` | `summary` | `pnpm` | `3911.44` | `0.810` | `0.909` | `0.940` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 5.51.1 | - |
| `pnpm-03` | `summary` | `pnpm` | `7461.43` | `0.874` | `1.000` | `0.898` | `1.000` | `0.830` | `0.432` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `1725.83` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `3782.03` | `0.956` | `1.000` | `0.936` | `1.000` | `0.917` | `0.725` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `7681.88` | `0.695` | `1.000` | `0.942` | `0.500` | `0.440` | `0.603` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `eslint-01` | `recall` | `eslint` | `3188.36` | `0.960` | `1.000` | `0.925` | `1.000` | `0.936` | `0.788` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `1125.43` | `0.642` | `0.273` | `0.841` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERR_MODULE_NOT_FOUND, eslint-plugin-react-hooks, /workspace/eslint.config.js, ESLint: 9.14.0 | - |
| `eslint-03` | `recall` | `eslint` | `1901.21` | `0.985` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `8851.34` | `0.623` | `0.653` | `0.864` | `1.000` | `0.771` | `0.237` | `soft_accepted` | missing_exact_anchors | Dockerfile:14, failed to solve | - |
| `docker-02` | `summary` | `docker` | `1569.96` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `9300.32` | `0.857` | `1.000` | `0.918` | `1.000` | `0.780` | `0.267` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `642.56` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `9373.83` | `0.900` | `1.000` | `0.918` | `1.000` | `0.763` | `0.209` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `1932.86` | `0.959` | `1.000` | `0.909` | `1.000` | `0.990` | `0.968` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `2848.83` | `0.878` | `1.000` | `0.925` | `1.000` | `0.816` | `0.388` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `9440.53` | `0.909` | `1.000` | `0.947` | `1.000` | `0.767` | `0.222` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `1398.18` | `0.751` | `0.611` | `0.953` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | timed out waiting for the condition, deployments/worker | - |
| `kubectl-04` | `recall` | `kubectl` | `8769.00` | `0.759` | `0.905` | `0.916` | `1.000` | `0.870` | `0.565` | `soft_accepted` | missing_exact_anchors | invalid worker.concurrency | - |
| `terraform-01` | `summary` | `terraform` | `1042.85` | `0.656` | `0.353` | `0.834` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | main.tf line 23, resource "aws_vpc" "main", Unsupported argument, enable_classic_link | - |
| `terraform-02` | `recall` | `terraform` | `4092.96` | `0.552` | `0.316` | `0.827` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | outputs.tf line 14, aws_security_group.db.id, Reference to undeclared resource, aws_security_group, db | - |
| `terraform-03` | `recall` | `terraform` | `1134.77` | `0.985` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `2724.90` | `0.682` | `0.390` | `0.888` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/aws.tftest.hcl line 18, Test assertion failed, aws_instance.web.instance_type, expected t3.small default | - |
| `mixed-01` | `recall` | `mixed` | `5013.79` | `0.937` | `1.000` | `0.910` | `1.000` | `0.879` | `0.595` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `3396.89` | `0.911` | `1.000` | `0.892` | `1.000` | `0.908` | `0.694` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `15563.50` | `0.666` | `1.000` | `0.890` | `0.500` | `0.367` | `0.112` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `git-02` | `recall` | `git` | `1041.97` | `0.984` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `13413.85` | `0.909` | `1.000` | `0.944` | `1.000` | `0.770` | `0.233` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `6159.11` | `0.913` | `1.000` | `0.942` | `1.000` | `0.782` | `0.272` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `2592.03` | `0.754` | `1.000` | `0.967` | `0.500` | `0.500` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `ssh-01` | `summary` | `ssh` | `2038.52` | `0.977` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `4523.46` | `0.970` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `7541.68` | `0.880` | `1.000` | `0.915` | `1.000` | `0.828` | `0.427` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `12986.33` | `0.835` | `1.000` | `0.869` | `1.000` | `0.774` | `0.246` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `3473.75` | `0.881` | `1.000` | `0.920` | `1.000` | `0.827` | `0.422` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `13037.03` | `0.904` | `1.000` | `0.944` | `1.000` | `0.754` | `0.180` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `4338.99` | `0.963` | `1.000` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `4881.76` | `0.756` | `0.667` | `0.930` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | cache_test.go:47 | - |
| `javac-01` | `summary` | `javac` | `4234.68` | `0.969` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `15147.07` | `0.643` | `1.000` | `0.911` | `0.500` | `0.392` | `0.280` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `maven-02` | `summary` | `maven` | `7316.49` | `0.889` | `1.000` | `0.915` | `1.000` | `0.846` | `0.486` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `2358.60` | `0.547` | `0.286` | `0.861` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | :service:compileJava, :service:compileClasspath, org.mapstruct:mapstruct:1.5.5.Final | - |
| `gradle-02` | `summary` | `gradle` | `1632.84` | `0.558` | `0.000` | `0.766` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ./gradlew test, InventoryServiceTest, InventoryServiceTest.java:118, Execution failed for task ':test' | - |
| `cargo-01` | `summary` | `cargo` | `4878.99` | `0.744` | `0.636` | `0.916` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | cargo build | - |
| `cargo-02` | `summary` | `cargo` | `4922.63` | `0.722` | `0.500` | `0.935` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | cargo build | - |
| `node-runtime-01` | `recall` | `node-runtime` | `4845.36` | `0.536` | `0.263` | `0.846` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Cannot find module './env/schema', MODULE_NOT_FOUND, /workspace/dist/config/index.js:4:18 | - |
| `npm-04` | `summary` | `npm` | `7061.76` | `0.850` | `1.000` | `0.905` | `1.000` | `0.776` | `0.254` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `2287.04` | `0.963` | `1.000` | `0.907` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `2639.40` | `0.763` | `0.727` | `0.914` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ESLint found too many warnings | - |
| `python-runtime-01` | `summary` | `python-runtime` | `5413.17` | `0.514` | `0.000` | `0.689` | `1.000` | `0.957` | `0.857` | `soft_accepted` | missing_exact_anchors | python -m tools.sync_rules --env staging, /workspace/app/loader.py, line 52, FileNotFoundError, rules/staging.json | - |
| `pytest-06` | `summary` | `pytest` | `33001.87` | `0.535` | `0.267` | `0.860` | `1.000` | `0.737` | `0.123` | `soft_accepted` | missing_exact_anchors | pytest tests/api/test_auth.py -k login -q, tests/api/test_auth.py:88 | - |
| `mypy-04` | `summary` | `mypy` | `3003.19` | `0.959` | `1.000` | `0.909` | `1.000` | `0.992` | `0.972` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `19316.93` | `0.842` | `1.000` | `0.918` | `1.000` | `0.750` | `0.167` | `accepted` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `5263.18` | `0.884` | `1.000` | `0.918` | `1.000` | `0.833` | `0.443` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `1039.03` | `0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `30980.36` | `0.651` | `1.000` | `0.932` | `0.500` | `0.393` | `0.284` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | - | - |
| `kubectl-07` | `recall` | `kubectl` | `2316.89` | `0.988` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `10908.01` | `0.775` | `1.000` | `0.925` | `1.000` | `0.790` | `0.301` | `soft_accepted` | missing_exact_anchors | - | - |
| `terraform-06` | `summary` | `terraform` | `1293.42` | `0.660` | `0.400` | `0.816` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | main.tf line 27, aws_vpc.core.id, Reference to undeclared resource | - |
| `terraform-07` | `summary` | `terraform` | `6768.86` | `0.874` | `1.000` | `0.895` | `1.000` | `0.832` | `0.439` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `1870.79` | `0.974` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `2781.06` | `0.970` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `1513.98` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `2575.42` | `0.969` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `1408.52` | `0.978` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `2550.17` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `1977.92` | `0.943` | `1.000` | `0.933` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `654.53` | `0.986` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `3010.62` | `0.649` | `0.524` | `0.910` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | line=91, Ruff F821, exit code 2 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `2861.11` | `0.545` | `0.000` | `0.729` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pnpm install --frozen-lockfile, ERR_PNPM_ENOSPC, no space left on device, react-dom@18.3.1, ERROR: Job failed: exit status 1 | - |
| `jenkins-01` | `summary` | `jenkins` | `3691.32` | `0.945` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `3584.56` | `0.922` | `1.000` | `0.928` | `1.000` | `0.902` | `0.673` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `1200.50` | `0.980` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `1997.76` | `0.640` | `0.500` | `0.913` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | proxy-2, UNREACHABLE!, Connection timed out | - |
| `rsync-01` | `summary` | `rsync` | `5880.68` | `0.876` | `1.000` | `0.916` | `1.000` | `0.818` | `0.395` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `24367.98` | `0.751` | `0.773` | `0.942` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/unit/test_invoice_totals.py:88 | - |
| `compiler-error-01` | `recall` | `compiler-error` | `30689.08` | `0.268` | `0.000` | `0.758` | `0.500` | `0.388` | `0.253` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | error[E0382], src/router.rs:137:42, borrow of moved value: `req`, src/router.rs:128, req.into_body(), req.method(), req.clone().into_body() | - |
| `ci-log-01` | `recall` | `ci-log` | `8441.92` | `0.929` | `1.000` | `0.917` | `1.000` | `0.850` | `0.500` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `9090.39` | `0.693` | `0.778` | `0.941` | `1.000` | `0.789` | `0.296` | `soft_accepted` | missing_exact_anchors | npm ERR! code ERESOLVE | - |
| `test-summary-01` | `summary` | `test-summary` | `11243.93` | `0.821` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `soft_accepted` | structured_output_mismatch | - | - |
| `build-log-01` | `summary` | `build-log` | `15571.91` | `0.659` | `1.000` | `0.886` | `0.500` | `0.422` | `0.477` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `docker-build-02` | `summary` | `docker-build` | `11190.10` | `0.631` | `1.000` | `0.871` | `0.000` | `0.000` | `0.216` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `3573.93` | `0.176` | `0.000` | `0.581` | `0.000` | `0.000` | `0.333` | `soft_accepted` | missing_exact_anchors | /repo/web/src/App.tsx, 27:19, @typescript-eslint/no-misused-promises, /repo/web/src/api/client.ts, 8:10, @typescript-eslint/no-explicit-any, 33:11, @typescript-eslint/no-unsafe-assignment | - |
| `git-review-01` | `instruction_following` | `git-review` | `3457.39` | `0.219` | `0.000` | `0.590` | `0.000` | `0.000` | `0.810` | `soft_accepted` | missing_exact_anchors | packages/api/src/auth/session.ts, packages/api/src/schema/openapi.yaml, migrations/202605171200_add_refresh_ttl.sql, User.lastLoginIp, DROP COLUMN refresh_token_expires_at, session cookie maxAge changed from 86400 to 604800 | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `4662.09` | `0.461` | `1.000` | `0.714` | `0.000` | `0.000` | `0.464` | `accepted` | - | - | - |
| `structured-output-01` | `structured` | `structured-output` | `5394.43` | `0.268` | `0.222` | `0.672` | `0.000` | `0.000` | `0.690` | `soft_accepted` | missing_exact_anchors | /work/app/services/payments.py, /work/app/api/routes.py, 21, reportUndefinedVariable | - |
| `structured-output-02` | `structured` | `structured-output` | `18332.89` | `0.333` | `0.905` | `0.542` | `0.000` | `0.000` | `0.481` | `soft_accepted` | missing_exact_anchors | port 5432 is already allocated | - |
| `structured-output-03` | `structured` | `structured-output` | `10755.46` | `0.304` | `1.000` | `0.306` | `0.000` | `0.000` | `0.123` | `accepted` | - | - | - |
| `structured-output-04` | `structured` | `structured-output` | `8265.98` | `0.091` | `0.219` | `0.205` | `0.000` | `0.000` | `0.021` | `soft_accepted` | missing_exact_anchors | @sentry/browser, /repo/packages/time/src/format.ts, /repo/packages/time/src/parse.ts, /repo/apps/web/src/features/flags.ts, @acme/flags | - |
| `exact-format-01` | `exact_format` | `exact-format` | `21043.40` | `0.025` | `0.000` | `0.291` | `0.000` | `0.000` | `0.008` | `soft_accepted` | missing_exact_anchors | tests/api/test_users.py::test_create_user_requires_email, tests/api/test_users.py::test_delete_user_requires_admin, tests/jobs/test_reconcile.py::TestReconcile::test_retries_deadlock | - |
| `exact-format-02` | `exact_format` | `exact-format` | `4553.67` | `0.064` | `0.286` | `0.294` | `0.000` | `0.000` | `0.067` | `soft_accepted` | missing_exact_anchors | packages/web/src/search/searchBox.test.tsx | - |
| `exact-format-03` | `exact_format` | `exact-format` | `2666.58` | `0.065` | `0.000` | `0.268` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ghcr.io/acme/worker@sha256:4f8c2e0b1d9a6c7e5f3a2b1908d4c6e7f0a123456789abcdeffedcba98765432 | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `1507.47` | `0.576` | `0.000` | `0.756` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /repo/tools/json.py, has no attribute 'dumps', shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `8529.84` | `0.456` | `0.000` | `0.804` | `0.500` | `0.402` | `0.347` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | TS2322, string | undefined, AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `7158.24` | `0.569` | `0.750` | `0.838` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | customers | - |
| `python-traceback-01` | `recall` | `python-traceback` | `3476.40` | `0.454` | `0.095` | `0.801` | `1.000` | `0.973` | `0.909` | `soft_accepted` | missing_exact_anchors | SMTPRecipientsRefused, /srv/app/app/tasks/email.py, line 92, [bad@example.test](mailto:bad@example.test), retries exhausted for queue emails | - |
| `mypy-05` | `recall` | `mypy` | `3333.04` | `0.976` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `7369.65` | `0.691` | `0.762` | `0.816` | `1.000` | `0.898` | `0.661` | `soft_accepted` | missing_exact_anchors | modules/worker/iam.tf line 27 | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `2068.80` | `0.416` | `0.000` | `0.757` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | InventorySyncTest > publishesBackorderEvent() FAILED, BACKORDER_CREATED, STOCK_RESERVED, InventorySyncTest.java:132, OrderServiceTest > calculatesDiscountForGoldCustomer() PASSED | - |
| `kubernetes-01` | `recall` | `kubernetes` | `4255.04` | `0.961` | `1.000` | `0.923` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `4893.92` | `0.966` | `1.000` | `0.914` | `1.000` | `0.962` | `0.872` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `4528.10` | `0.972` | `1.000` | `0.917` | `1.000` | `0.978` | `0.927` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `4067.80` | `0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `2916.09` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `15916.44` | `0.451` | `0.238` | `0.839` | `1.000` | `0.740` | `0.133` | `soft_accepted` | missing_exact_anchors | 20260518_add_workspace_limits.sql, relation "workspace_limits" already exists, packages/db/src/migrate.ts:77:13, packages/db/test/migrate.test.ts:44:7, exit code 1 | - |
| `pnpm-04` | `recall` | `pnpm` | `3404.17` | `0.970` | `1.000` | `0.930` | `1.000` | `0.962` | `0.875` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `29008.23` | `0.431` | `0.000` | `0.829` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | UserDecoderTests testMissingAvatarUsesPlaceholder, Tests/UserDecoderTests.swift:47, XCTAssertEqual failed, nil, Optional(placeholder.png), fatalError | - |
| `elixir-01` | `recall` | `elixir` | `2532.79` | `0.476` | `0.087` | `0.882` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | KeyError, key :ttl not found, lib/my_app/cache_worker.ex:63, test/my_app/cache_worker_test.exs:29, refreshes expired keys | - |
| `rails-01` | `recall` | `rails` | `14661.68` | `0.855` | `1.000` | `0.792` | `1.000` | `0.721` | `0.070` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `2856.22` | `0.951` | `1.000` | `0.905` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `2600.08` | `0.977` | `1.000` | `0.907` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `2223.54` | `0.983` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `4319.89` | `0.952` | `1.000` | `0.932` | `1.000` | `0.906` | `0.688` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `5023.66` | `0.982` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `1666.14` | `0.407` | `0.000` | `0.713` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | .\scripts\release.ps1 -Version 1.4.2, cannot be loaded because running scripts is disabled, PSSecurityException, FullyQualifiedErrorId : UnauthorizedAccess | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `2180.51` | `0.960` | `1.000` | `0.930` | `1.000` | `0.932` | `0.775` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `4249.57` | `0.967` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `4834.88` | `0.962` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `3300.42` | `0.966` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `2522.09` | `0.966` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `3275.27` | `0.965` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `2788.16` | `0.960` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `2961.32` | `0.943` | `1.000` | `0.922` | `1.000` | `0.949` | `0.830` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `2255.45` | `0.965` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `3428.12` | `0.739` | `1.000` | `0.923` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `3209.15` | `0.966` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `7942.60` | `0.956` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `1640.71` | `0.964` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `7944.98` | `0.541` | `0.000` | `0.716` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/test_signup.py, FAILED, tests/test_signup.py::test_signup_is_idempotent, sqlalchemy.exc.IntegrityError, psycopg.errors.UniqueViolation | - |
| `wrangler-01` | `summary` | `wrangler` | `3179.44` | `0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `4961.25` | `0.815` | `1.000` | `0.757` | `1.000` | `0.824` | `0.414` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `5954.79` | `0.268` | `0.556` | `0.612` | `0.000` | `0.000` | `0.205` | `soft_accepted` | missing_exact_anchors | 22:7, prefer-const, @typescript-eslint/no-explicit-any | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `28768.44` | `0.313` | `0.706` | `0.678` | `0.000` | `0.000` | `0.237` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | iam:PassRole | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `374.08` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | tests/test_api.py::test_create_user, tests/test_auth.py::test_refresh_token_expiry | llama.cpp backend returned empty output. |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `2111.46` | `0.449` | `1.000` | `0.688` | `0.000` | `0.000` | `0.429` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `2866.14` | `0.261` | `0.269` | `0.678` | `0.000` | `0.000` | `0.500` | `soft_accepted` | missing_exact_anchors | secret "api-env" not found, Warning BackOff, Back-off restarting failed container api | - |
| `npm-06` | `instruction_following` | `npm` | `986.93` | `0.682` | `1.000` | `0.739` | `0.400` | `0.400` | `1.000` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `7782.29` | `0.381` | `1.000` | `0.590` | `0.000` | `0.000` | `0.037` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `3208.20` | `0.363` | `0.667` | `0.737` | `0.000` | `0.000` | `0.733` | `soft_accepted` | missing_exact_anchors | identifier = "prod-main" | - |
| `maven-03` | `instruction_following` | `maven` | `1937.26` | `0.574` | `1.000` | `0.912` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `3954.08` | `0.415` | `1.000` | `0.639` | `0.000` | `0.000` | `0.234` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `2193.33` | `0.145` | `0.000` | `0.537` | `0.000` | `0.000` | `0.091` | `soft_accepted` | missing_exact_anchors | src/App.tsx, src/api/client.ts | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `2629.50` | `0.411` | `1.000` | `0.673` | `0.000` | `0.000` | `0.095` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `2614.35` | `0.328` | `0.333` | `0.731` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/auth.rs:88, billing::tests::rounds_half_even, left: 1750, right: 1749 | - |
| `shell-01` | `instruction_following` | `shell` | `3721.32` | `0.441` | `1.000` | `0.724` | `0.000` | `0.000` | `0.237` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `3652.07` | `0.333` | `0.533` | `0.618` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /repo/app/user.py, message | - |
| `terraform-10` | `structured` | `terraform` | `2329.40` | `0.282` | `0.667` | `0.505` | `0.000` | `0.000` | `0.467` | `soft_accepted` | missing_exact_anchors | resource, field | - |
| `junit-01` | `structured` | `junit` | `4784.65` | `0.205` | `0.286` | `0.528` | `0.000` | `0.000` | `0.250` | `soft_accepted` | missing_exact_anchors | Test, Error, Location, --- | - |
| `kubernetes-03` | `structured` | `kubernetes` | `925.32` | `0.357` | `1.000` | `0.190` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `3573.98` | `0.204` | `0.667` | `0.281` | `0.000` | `0.000` | `0.227` | `soft_accepted` | missing_exact_anchors | line, column, rule | - |
| `docker-build-04` | `structured` | `docker-build` | `1418.50` | `0.521` | `1.000` | `0.736` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `1783.61` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | failed_tests, name, TestParseAmount, location, amount_test.go:22, message | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='- follow the requested structure exactly - return only the requested json, yaml, table, or bullet structure - do not add prose before or after the structured...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='- follow the requested structure exactly - return only the requested json, yaml, table, or bullet structure - do not add prose before or after the structured...' |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `3455.61` | `0.214` | `0.333` | `0.531` | `0.000` | `0.000` | `0.261` | `soft_accepted` | missing_exact_anchors | Job, Step, Exit, --- | - |
| `npm-07` | `structured` | `npm` | `3820.63` | `0.232` | `0.833` | `0.284` | `0.000` | `0.000` | `0.211` | `soft_accepted` | missing_exact_anchors | required | - |
| `mypy-06` | `structured` | `mypy` | `5790.33` | `0.224` | `0.467` | `0.481` | `0.000` | `0.000` | `0.265` | `soft_accepted` | missing_exact_anchors | File, Line, Code, Message | - |
| `gradle-03` | `structured` | `gradle` | `3583.56` | `0.078` | `0.000` | `0.232` | `0.000` | `0.000` | `0.219` | `soft_accepted` | missing_exact_anchors | failed, task, :api:compileJava, cause, cannot, find | - |
| `playwright-02` | `structured` | `playwright` | `3267.69` | `0.318` | `0.333` | `0.747` | `0.000` | `0.000` | `0.833` | `soft_accepted` | missing_exact_anchors | project, file, line, test | - |
| `postgres-04` | `structured` | `postgres` | `5618.37` | `0.117` | `0.303` | `0.199` | `0.000` | `0.000` | `0.170` | `soft_accepted` | missing_exact_anchors | errors, file, line, message, column | - |
| `vite-01` | `structured` | `vite` | `3459.59` | `0.268` | `1.000` | `0.217` | `0.000` | `0.000` | `0.023` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `246.66` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | tests/test_a.py::test_one, tests/test_b.py::TestB::test_three | llama.cpp backend returned empty output. |
| `git-04` | `exact_format` | `git` | `3897.67` | `0.188` | `1.000` | `0.305` | `0.000` | `0.000` | `0.143` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `3728.63` | `0.039` | `0.000` | `0.331` | `0.000` | `0.000` | `0.250` | `soft_accepted` | missing_exact_anchors | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | - |
| `npm-08` | `exact_format` | `npm` | `1754.82` | `0.155` | `1.000` | `0.279` | `0.000` | `0.000` | `0.083` | `soft_accepted` | exact_format_style_mismatch | - | - |
| `go-test-05` | `exact_format` | `go-test` | `3293.31` | `0.200` | `1.000` | `0.316` | `0.000` | `0.000` | `0.375` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `2451.86` | `0.154` | `1.000` | `0.253` | `0.000` | `0.000` | `0.114` | `soft_accepted` | exact_format_style_mismatch | - | - |
| `cargo-05` | `exact_format` | `cargo` | `3348.99` | `0.261` | `1.000` | `0.337` | `0.167` | `0.123` | `0.125` | `soft_accepted` | exact_format_style_mismatch | - | - |
| `curl-03` | `exact_format` | `curl` | `1929.59` | `0.154` | `1.000` | `0.246` | `0.000` | `0.000` | `0.143` | `soft_accepted` | exact_format_style_mismatch | - | - |
| `rails-02` | `exact_format` | `rails` | `1859.23` | `0.178` | `1.000` | `0.249` | `0.000` | `0.000` | `0.056` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `3421.94` | `0.713` | `1.000` | `0.877` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `3787.70` | `0.644` | `0.222` | `0.825` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | url: string, user.photoUrl | - |
| `postgres-05` | `explanation` | `postgres` | `4434.92` | `0.556` | `0.667` | `0.843` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | customers | - |
| `docker-build-05` | `explanation` | `docker-build` | `1900.72` | `0.955` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `2732.13` | `0.952` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `4255.83` | `0.690` | `1.000` | `0.825` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `3423.76` | `0.853` | `1.000` | `0.733` | `1.000` | `0.958` | `0.860` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `14727.10` | `0.457` | `0.500` | `0.839` | `0.500` | `0.355` | `0.033` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | main.cpp:10:5 | - |
| `testing-01` | `recall` | `testing` | `1417.85` | `0.583` | `0.357` | `0.903` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Calculator.java:50, ArithmeticException | - |
| `testing-02` | `recall` | `testing` | `3119.15` | `0.741` | `1.000` | `0.926` | `0.500` | `0.485` | `0.900` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `package-management-01` | `recall` | `package-management` | `796.86` | `0.972` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `2635.15` | `0.658` | `0.667` | `0.829` | `1.000` | `0.900` | `0.667` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `2503.97` | `0.374` | `0.000` | `0.709` | `1.000` | `0.887` | `0.625` | `soft_accepted` | missing_exact_anchors | CS0234, Program.cs(15,10), JsonConvert | - |
| `package-management-02` | `recall` | `package-management` | `2122.13` | `0.964` | `1.000` | `0.924` | `1.000` | `0.950` | `0.833` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `1948.44` | `0.536` | `0.286` | `0.834` | `1.000` | `0.980` | `0.933` | `soft_accepted` | missing_exact_anchors | Error: Tests failed | - |
| `testing-03` | `recall` | `testing` | `2380.38` | `0.938` | `1.000` | `0.879` | `1.000` | `0.905` | `0.684` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `2341.25` | `0.947` | `1.000` | `0.872` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `3046.06` | `0.908` | `1.000` | `0.873` | `1.000` | `0.820` | `0.400` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `3900.71` | `0.876` | `1.000` | `0.778` | `1.000` | `0.794` | `0.314` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `1075.89` | `0.963` | `1.000` | `0.853` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `1821.97` | `0.593` | `0.412` | `0.850` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Execution failed for task ':test' | - |
| `container-runtime-01` | `recall` | `container-runtime` | `2349.64` | `0.903` | `1.000` | `0.754` | `1.000` | `0.892` | `0.640` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `1465.35` | `0.972` | `1.000` | `0.889` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `699.90` | `0.419` | `0.000` | `0.772` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | You must be logged in to the server, Unauthorized | - |
| `runtime-03` | `recall` | `runtime` | `190.13` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | RecursionError, maximum recursion depth exceeded | llama.cpp backend returned empty output. |
| `package-management-03` | `recall` | `package-management` | `3751.73` | `0.641` | `0.500` | `0.918` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | No matching distribution found | - |
| `infrastructure-03` | `recall` | `infrastructure` | `2554.55` | `0.933` | `1.000` | `0.894` | `1.000` | `0.877` | `0.591` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `4372.25` | `0.874` | `1.000` | `0.809` | `1.000` | `0.764` | `0.213` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `1163.57` | `0.415` | `0.000` | `0.754` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | foo.c:5:2, error: expected ';' | - |
| `ci-03` | `recall` | `ci` | `2866.92` | `0.800` | `1.000` | `0.892` | `1.000` | `0.905` | `0.682` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `391.07` | `0.971` | `1.000` | `0.883` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `1008.67` | `0.747` | `0.714` | `0.875` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | failing tests | - |
| `docker-05` | `summary` | `docker` | `374.93` | `0.946` | `1.000` | `0.865` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `2478.35` | `0.786` | `1.000` | `0.801` | `1.000` | `0.731` | `0.103` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `2454.34` | `0.776` | `1.000` | `0.737` | `1.000` | `0.762` | `0.205` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `470.46` | `0.972` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `1451.37` | `0.891` | `1.000` | `0.811` | `1.000` | `0.933` | `0.778` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `1518.63` | `0.472` | `1.000` | `0.768` | `0.000` | `0.000` | `0.417` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `2153.53` | `0.202` | `0.000` | `0.740` | `0.000` | `0.000` | `0.154` | `soft_accepted` | missing_exact_anchors | ERROR:, * rerun pytest test_auth.py::TestAuth::test_login | - |
| `ci-05` | `instruction_following` | `ci` | `2017.57` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | ERROR: failed to fetch, 404  Not Found | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='- follow the requested structure exactly - return only the requested json, yaml, table, or bullet structure - do not add prose before or after the structured...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='- follow the requested structure exactly - return only the requested json, yaml, table, or bullet structure - do not add prose before or after the structured...' |
| `linting-02` | `structured` | `linting` | `1211.28` | `0.433` | `1.000` | `0.468` | `0.000` | `0.000` | `0.923` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `941.36` | `0.453` | `1.000` | `0.534` | `0.000` | `0.000` | `0.923` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `1000.47` | `0.445` | `1.000` | `0.551` | `0.000` | `0.000` | `0.800` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `431.07` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `3624.67` | `0.179` | `1.000` | `0.279` | `0.000` | `0.000` | `0.017` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `2956.51` | `0.021` | `0.000` | `0.225` | `0.000` | `0.000` | `0.047` | `soft_accepted` | missing_exact_anchors | OUTPUT: | - |
| `shell-04` | `exact_format` | `shell` | `2072.36` | `0.184` | `1.000` | `0.314` | `0.000` | `0.000` | `0.050` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `2137.26` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | Resources: 1 added, instance_id | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `build-05` | `exact_format` | `build` | `552.28` | `0.225` | `1.000` | `0.609` | `0.000` | `0.000` | `0.286` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `351.74` | `0.582` | `1.000` | `0.658` | `0.500` | `0.400` | `0.333` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `1113.43` | `0.936` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `2824.78` | `0.822` | `1.000` | `0.761` | `1.000` | `0.825` | `0.417` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `726.23` | `0.959` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `283.82` | `0.943` | `1.000` | `0.885` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `3275.11` | `0.807` | `1.000` | `0.764` | `1.000` | `0.775` | `0.250` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `315.82` | `0.949` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `3049.59` | `0.763` | `1.000` | `0.679` | `1.000` | `0.770` | `0.233` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `340.27` | `0.933` | `1.000` | `0.866` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `265.08` | `0.935` | `1.000` | `0.870` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `2820.85` | `0.814` | `1.000` | `0.764` | `1.000` | `0.796` | `0.320` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `13685.91` | `0.789` | `1.000` | `0.767` | `1.000` | `0.715` | `0.050` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `2112.24` | `0.798` | `1.000` | `0.677` | `1.000` | `0.880` | `0.600` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `2882.64` | `0.792` | `1.000` | `0.746` | `1.000` | `0.757` | `0.190` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `788.62` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | SECRET_KEY setting must not be empty | llama.cpp backend returned empty output. |
| `explanation-08` | `explanation` | `explanation` | `1821.80` | `0.838` | `1.000` | `0.735` | `1.000` | `0.912` | `0.706` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `1891.67` | `0.874` | `1.000` | `0.748` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `426.23` | `0.950` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `1849.52` | `0.840` | `1.000` | `0.738` | `1.000` | `0.914` | `0.714` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `3158.18` | `0.789` | `1.000` | `0.726` | `1.000` | `0.776` | `0.255` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `1106.97` | `0.453` | `1.000` | `0.534` | `0.000` | `0.000` | `0.923` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `1157.67` | `0.445` | `1.000` | `0.551` | `0.000` | `0.000` | `0.800` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `529.54` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `3146.96` | `0.179` | `1.000` | `0.279` | `0.000` | `0.000` | `0.018` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `1794.20` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | value1, value2 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `build-06` | `exact_format` | `build` | `2512.29` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | Resources: 1 added, instance_id | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `runtime-07` | `exact_format` | `runtime` | `1532.83` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | Listening on port 8080 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `build-07` | `exact_format` | `build` | `2712.16` | `0.029` | `0.000` | `0.259` | `0.000` | `0.000` | `0.176` | `soft_accepted` | missing_exact_anchors | testError:34 | - |
| `shell-08` | `exact_format` | `shell` | `250.95` | `0.230` | `1.000` | `0.298` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `992.06` | `0.936` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `2772.07` | `0.822` | `1.000` | `0.761` | `1.000` | `0.825` | `0.417` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `1020.36` | `0.960` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `1390.95` | `0.970` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `2755.27` | `0.763` | `1.000` | `0.679` | `1.000` | `0.770` | `0.233` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `578.62` | `0.963` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `3104.34` | `0.801` | `1.000` | `0.751` | `1.000` | `0.776` | `0.254` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `2772.88` | `0.789` | `1.000` | `0.737` | `1.000` | `0.761` | `0.204` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `2216.79` | `0.852` | `1.000` | `0.771` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
