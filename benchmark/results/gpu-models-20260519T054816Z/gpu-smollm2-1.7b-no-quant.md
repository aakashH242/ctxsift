# gpu-smollm2-1.7b-no-quant

## Scenario

- track: `gpu`
- phase: `gpu-screen`
- model: `HuggingFaceTB/SmolLM2-1.7B-Instruct`
- quantization: `none`
- device: `cuda`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `12017.24`
- cpu_rss_bytes: `2729971712`
- gpu_peak_bytes: `4726266880`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `269`
- accepted_count: `206`
- soft_accepted_count: `63`
- rejected_count: `11`
- exact_pass_count: `220`
- avg_inference_ms: `4796.28`
- p95_inference_ms: `15262.56`
- avg_exact_preservation_ratio: `0.881`
- avg_summary_quality_ratio: `0.810`
- avg_format_adherence_score: `0.758`
- avg_instruction_following_score: `0.716`
- avg_brevity_ratio: `0.749`
- avg_case_score: `0.752`
- p10_case_score: `0.274`
- quality_core: `0.656`
- latency_factor: `0.877`
- final_score: `57.57`
- peak_cpu_rss_bytes: `2729992192`
- peak_gpu_bytes: `5023862784`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `21402.47` | `0.683` | `1.000` | `0.900` | `0.500` | `0.393` | `0.286` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-02` | `summary` | `python` | `5274.19` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass="python services/worker.py --queue emails --concurrency 4 INFO boot: reading .env.local WARNING redis retry 1/3 failed: ConnectionResetError(104, 'Connection ..." repair_status=rejected repair_flags=['control_token_leakage'] repair_pass="python services/worker.py --queue emails --concurrency 4 INFO boot: reading .env.local WARNING redis retry 1/3 failed: ConnectionResetError(104, 'Connection ..." |
| `python-03` | `recall` | `python` | `8979.37` | `0.687` | `1.000` | `0.909` | `0.500` | `0.397` | `0.311` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-04` | `recall` | `python` | `16189.52` | `0.625` | `0.583` | `0.852` | `1.000` | `0.880` | `0.600` | `soft_accepted` | missing_exact_anchors | python -m jobs.refresh_catalog --region us-east-1, catalog?page=2, us-east-1 | - |
| `python-05` | `recall` | `python` | `4232.61` | `0.518` | `0.222` | `0.836` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | python tools/export_report.py --input data/may.csv --format parquet, /workspace/src/reports/export.py, line 131, data/may.csv | - |
| `pytest-01` | `recall` | `pytest` | `3595.53` | `0.539` | `0.273` | `0.846` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/api/test_users.py -q, tests/api/test_users.py::test_create_user_rejects_duplicate[email], tests/api/test_users.py:47 | - |
| `pytest-02` | `summary` | `pytest` | `11964.36` | `0.890` | `1.000` | `0.946` | `1.000` | `0.823` | `0.409` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `3777.37` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | pytest tests -q -x, tests/jobs/test_retention.py::test_archive_marks_job_deleted, teardown, psycopg.errors.ForeignKeyViolation, job_runs_job_id_fkey, 149 passed, 1 skipped, 1 error in 58.73s | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='psycopg.errors.ForeignKeyViolation: update or delete on table "jobs" violates foreign key constraint "job_runs_job_id_fkey" on table "job_runs"<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='psycopg.errors.ForeignKeyViolation: update or delete on table "jobs" violates foreign key constraint "job_runs_job_id_fkey" on table "job_runs" DETAIL: Key (...' |
| `pytest-04` | `recall` | `pytest` | `3004.84` | `0.625` | `0.450` | `0.929` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/cli/test_export.py -q, /workspace/tests/cli/test_export.py:12 | - |
| `pytest-05` | `summary` | `pytest` | `21168.01` | `0.667` | `1.000` | `0.927` | `0.500` | `0.413` | `0.423` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `mypy-01` | `recall` | `mypy` | `1580.76` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `1525.21` | `0.989` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `917.10` | `0.988` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `6648.50` | `0.856` | `1.000` | `0.898` | `1.000` | `0.794` | `0.312` | `accepted` | - | - | - |
| `ruff-02` | `summary` | `ruff` | `680.12` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `845.21` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `4174.81` | `0.984` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `7649.54` | `0.969` | `1.000` | `0.901` | `1.000` | `0.981` | `0.935` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `1007.62` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `4324.30` | `0.985` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `1279.42` | `0.763` | `0.766` | `0.892` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 1 file failed to reformat, 1 file reformatted | - |
| `black-03` | `recall` | `black` | `672.35` | `0.993` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `1494.80` | `0.978` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `9719.25` | `0.673` | `0.667` | `0.922` | `1.000` | `0.813` | `0.376` | `soft_accepted` | missing_exact_anchors | npm install | - |
| `npm-03` | `summary` | `npm` | `10500.24` | `0.887` | `1.000` | `0.929` | `1.000` | `0.832` | `0.439` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `4788.26` | `0.798` | `0.895` | `0.943` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --no-frozen-lockfile | - |
| `pnpm-02` | `summary` | `pnpm` | `4886.07` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `11035.61` | `0.873` | `1.000` | `0.901` | `1.000` | `0.825` | `0.417` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `4908.55` | `0.705` | `0.467` | `0.905` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tsc -p tsconfig.json --noEmit, src/server/index.ts(3,18), src/server/index.ts(4,18) | - |
| `typescript-02` | `recall` | `typescript` | `4659.13` | `0.939` | `1.000` | `0.931` | `1.000` | `0.867` | `0.558` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `9461.14` | `0.699` | `1.000` | `0.956` | `0.500` | `0.440` | `0.603` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `eslint-01` | `recall` | `eslint` | `2793.31` | `0.977` | `1.000` | `0.938` | `1.000` | `0.979` | `0.929` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `5231.90` | `0.772` | `0.727` | `0.941` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | eslint . | - |
| `eslint-03` | `recall` | `eslint` | `2554.00` | `0.988` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `1900.51` | `0.986` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `475.04` | `0.992` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `1220.41` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `384.10` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `9266.93` | `0.904` | `1.000` | `0.932` | `1.000` | `0.762` | `0.207` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `2007.57` | `0.966` | `1.000` | `0.928` | `1.000` | `0.990` | `0.968` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `5873.77` | `0.873` | `1.000` | `0.912` | `1.000` | `0.816` | `0.388` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `15348.31` | `0.907` | `1.000` | `0.940` | `1.000` | `0.765` | `0.216` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `1019.84` | `0.987` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `14051.71` | `0.981` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `4895.20` | `0.976` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `5307.12` | `0.956` | `1.000` | `0.924` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `2256.73` | `0.696` | `0.613` | `0.974` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform apply | - |
| `terraform-04` | `summary` | `terraform` | `14258.24` | `0.916` | `1.000` | `0.948` | `1.000` | `0.874` | `0.581` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `5150.76` | `0.937` | `1.000` | `0.910` | `1.000` | `0.879` | `0.595` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `7070.96` | `0.909` | `1.000` | `0.886` | `1.000` | `0.908` | `0.694` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `19527.66` | `0.678` | `1.000` | `0.901` | `0.500` | `0.384` | `0.229` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `git-02` | `recall` | `git` | `6210.09` | `0.905` | `1.000` | `0.867` | `1.000` | `0.816` | `0.386` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `14827.83` | `0.722` | `0.875` | `0.922` | `1.000` | `0.776` | `0.254` | `soft_accepted` | missing_exact_anchors | invalid index-pack output | - |
| `curl-01` | `recall` | `curl` | `11227.21` | `0.899` | `1.000` | `0.944` | `1.000` | `0.739` | `0.131` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `5384.34` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | curl -I https://docs.example.com/sdk/latest, HTTP/2 301, location: /sdk/v3.4/, cache-control: max-age=3600 | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='curl -I https://docs.example.com/sdk/latest<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='HTTP/2 301 location: /sdk/v3.4/ cache-control: max-age=3600 HTTP/2 301 location: /sdk/v3.4/ cache-control: max-age=3600 $ curl -I https://docs.example.com/sd...' |
| `ssh-01` | `summary` | `ssh` | `2489.74` | `0.967` | `1.000` | `0.940` | `1.000` | `0.981` | `0.938` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `3612.29` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `1589.80` | `0.975` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `535.99` | `0.962` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `2581.21` | `0.699` | `0.429` | `0.913` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | sudo apt-get install libpq-dev postgresql-client, held broken packages | - |
| `dnf-01` | `recall` | `dnf` | `14386.46` | `0.903` | `1.000` | `0.943` | `1.000` | `0.752` | `0.173` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `6379.03` | `0.752` | `0.700` | `0.901` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | go build ./cmd/api | - |
| `go-test-01` | `summary` | `go-test` | `14189.81` | `0.884` | `1.000` | `0.939` | `1.000` | `0.817` | `0.391` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `5415.44` | `0.974` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `16112.11` | `0.658` | `1.000` | `0.923` | `0.500` | `0.405` | `0.366` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `maven-02` | `summary` | `maven` | `14864.65` | `0.887` | `1.000` | `0.933` | `1.000` | `0.827` | `0.425` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `7505.82` | `0.904` | `1.000` | `0.927` | `1.000` | `0.767` | `0.224` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `8142.06` | `0.638` | `0.389` | `0.896` | `1.000` | `0.890` | `0.633` | `soft_accepted` | missing_exact_anchors | ./gradlew test, Execution failed for task ':test' | - |
| `cargo-01` | `summary` | `cargo` | `8939.78` | `0.920` | `1.000` | `0.920` | `1.000` | `0.904` | `0.681` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `4662.58` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `14815.74` | `0.693` | `1.000` | `0.919` | `0.500` | `0.404` | `0.359` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `npm-04` | `summary` | `npm` | `13969.08` | `0.662` | `0.684` | `0.922` | `1.000` | `0.778` | `0.262` | `soft_accepted` | missing_exact_anchors | npm install | - |
| `tsc-01` | `summary` | `tsc` | `2179.62` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `5860.54` | `0.953` | `1.000` | `0.925` | `1.000` | `0.967` | `0.889` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `7512.53` | `0.690` | `1.000` | `0.943` | `0.500` | `0.435` | `0.566` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `pytest-06` | `summary` | `pytest` | `11855.60` | `0.857` | `1.000` | `0.890` | `1.000` | `0.802` | `0.341` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `3295.59` | `0.968` | `1.000` | `0.929` | `1.000` | `0.992` | `0.972` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `16413.51` | `0.861` | `1.000` | `0.935` | `1.000` | `0.773` | `0.244` | `accepted` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `11451.94` | `0.852` | `1.000` | `0.923` | `1.000` | `0.766` | `0.220` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `4031.95` | `0.788` | `0.833` | `0.923` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | field is immutable | - |
| `kubectl-06` | `summary` | `kubectl` | `16636.35` | `0.647` | `1.000` | `0.914` | `0.500` | `0.396` | `0.308` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | - | - |
| `kubectl-07` | `recall` | `kubectl` | `3176.63` | `0.985` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `6441.08` | `0.912` | `1.000` | `0.918` | `1.000` | `0.799` | `0.328` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `3665.36` | `0.932` | `1.000` | `0.913` | `1.000` | `0.934` | `0.780` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `6088.59` | `0.872` | `1.000` | `0.899` | `1.000` | `0.824` | `0.414` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `1997.76` | `0.764` | `0.667` | `0.954` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | sudo nginx -t | - |
| `nginx-02` | `summary` | `nginx` | `6609.23` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `5784.85` | `0.992` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `4449.35` | `0.967` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `1130.92` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `1142.88` | `0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `6843.81` | `0.949` | `1.000` | `0.948` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `473.17` | `0.505` | `0.167` | `0.879` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | redis-cli -u redis://127.0.0.1:6379 PING, LOADING | - |
| `github-actions-01` | `recall` | `github-actions` | `4953.19` | `0.640` | `0.524` | `0.870` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ruff check ., line=91, exit code 2 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `10005.02` | `0.853` | `1.000` | `0.911` | `1.000` | `0.777` | `0.255` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `449.35` | `0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `962.40` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `1977.22` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `5362.95` | `0.916` | `1.000` | `0.942` | `1.000` | `0.790` | `0.300` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `3671.88` | `0.910` | `1.000` | `0.915` | `1.000` | `0.887` | `0.625` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `8380.49` | `0.748` | `0.773` | `0.930` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/unit/test_invoice_totals.py:88 | - |
| `compiler-error-01` | `recall` | `compiler-error` | `17363.62` | `0.427` | `0.299` | `0.826` | `0.500` | `0.443` | `0.621` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | error[E0382], src/router.rs:137:42, borrow of moved value: `req`, src/router.rs:128, req.clone().into_body() | - |
| `ci-log-01` | `recall` | `ci-log` | `8629.28` | `0.926` | `1.000` | `0.931` | `1.000` | `0.829` | `0.431` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `8008.15` | `0.923` | `1.000` | `0.963` | `1.000` | `0.797` | `0.324` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `14488.29` | `0.831` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `soft_accepted` | structured_output_mismatch | - | - |
| `build-log-01` | `summary` | `build-log` | `15099.02` | `0.651` | `1.000` | `0.898` | `0.500` | `0.406` | `0.376` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `docker-build-02` | `summary` | `docker-build` | `15316.58` | `0.646` | `1.000` | `0.907` | `0.000` | `0.000` | `0.217` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `4304.55` | `0.523` | `1.000` | `0.690` | `0.250` | `0.187` | `0.157` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `15595.40` | `0.309` | `0.810` | `0.654` | `0.000` | `0.000` | `0.050` | `soft_accepted` | missing_exact_anchors | DROP COLUMN refresh_token_expires_at, session cookie maxAge changed from 86400 to 604800 | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `1611.45` | `0.513` | `1.000` | `0.709` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-01` | `structured` | `structured-output` | `5322.22` | `0.435` | `1.000` | `0.656` | `0.000` | `0.000` | `0.387` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `13893.28` | `0.283` | `0.905` | `0.420` | `0.000` | `0.000` | `0.263` | `soft_accepted` | missing_exact_anchors | port 5432 is already allocated | - |
| `structured-output-03` | `structured` | `structured-output` | `4959.61` | `0.329` | `1.000` | `0.357` | `0.000` | `0.000` | `0.220` | `accepted` | - | - | - |
| `structured-output-04` | `structured` | `structured-output` | `1989.83` | `0.357` | `1.000` | `0.192` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `2602.85` | `0.187` | `1.000` | `0.335` | `0.000` | `0.000` | `0.071` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `12137.71` | `0.121` | `0.714` | `0.319` | `0.000` | `0.000` | `0.055` | `soft_accepted` | missing_exact_anchors | SearchBox debounces network query before fetch | - |
| `exact-format-03` | `exact_format` | `exact-format` | `4180.14` | `0.185` | `1.000` | `0.314` | `0.000` | `0.000` | `0.062` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `3965.07` | `0.703` | `0.556` | `0.899` | `1.000` | `0.900` | `0.667` | `soft_accepted` | missing_exact_anchors | has no attribute 'dumps', shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `15181.52` | `0.665` | `0.750` | `0.821` | `1.000` | `0.765` | `0.218` | `soft_accepted` | missing_exact_anchors | AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `4388.69` | `0.790` | `1.000` | `0.907` | `0.182` | `0.182` | `1.000` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `3824.66` | `0.985` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `3716.05` | `0.980` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `13604.80` | `0.977` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `28563.60` | `0.460` | `0.217` | `0.896` | `1.000` | `0.759` | `0.198` | `soft_accepted` | missing_exact_anchors | BACKORDER_CREATED, STOCK_RESERVED, InventorySyncTest.java:132, OrderServiceTest > calculatesDiscountForGoldCustomer() PASSED | - |
| `kubernetes-01` | `recall` | `kubernetes` | `1394.59` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `6279.90` | `0.932` | `1.000` | `0.922` | `1.000` | `0.855` | `0.515` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `3488.06` | `0.983` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `14177.85` | `0.930` | `1.000` | `0.939` | `1.000` | `0.836` | `0.452` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `3002.01` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `3320.09` | `0.988` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `3037.15` | `0.970` | `1.000` | `0.931` | `1.000` | `0.962` | `0.875` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `3143.93` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `15018.98` | `0.704` | `1.000` | `0.922` | `0.500` | `0.422` | `0.478` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `rails-01` | `recall` | `rails` | `4823.66` | `0.931` | `1.000` | `0.922` | `1.000` | `0.852` | `0.508` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `4025.66` | `0.993` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `1445.42` | `0.978` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `2290.41` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `6841.15` | `0.952` | `1.000` | `0.931` | `1.000` | `0.906` | `0.688` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `4712.06` | `0.982` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `26746.41` | `0.918` | `1.000` | `0.923` | `1.000` | `0.811` | `0.369` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `5794.66` | `0.960` | `1.000` | `0.931` | `1.000` | `0.932` | `0.775` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `5070.80` | `0.904` | `1.000` | `0.875` | `1.000` | `0.908` | `0.694` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `6894.98` | `0.514` | `0.211` | `0.766` | `1.000` | `0.790` | `0.301` | `soft_accepted` | missing_exact_anchors | ./integration, TestWebhookReplay, github.com/acme/api/internal/webhook, dispatch | - |
| `npm-05` | `summary` | `npm` | `13000.49` | `0.886` | `1.000` | `0.921` | `1.000` | `0.836` | `0.454` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `976.61` | `0.929` | `0.875` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | template | - |
| `ruff-04` | `summary` | `ruff` | `15478.30` | `0.901` | `1.000` | `0.913` | `1.000` | `0.872` | `0.573` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `3306.00` | `0.961` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `2115.24` | `0.946` | `1.000` | `0.945` | `1.000` | `0.936` | `0.786` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `1538.32` | `0.940` | `1.000` | `0.851` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `2574.71` | `0.678` | `0.545` | `0.874` | `1.000` | `0.924` | `0.745` | `soft_accepted` | missing_exact_anchors | build/server.o, src/server.c:14:10 | - |
| `python-pytest-02` | `summary` | `python-pytest` | `6578.87` | `0.965` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `1952.85` | `0.956` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `4923.76` | `0.967` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `2192.17` | `0.672` | `0.349` | `0.885` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/test_signup.py, FAILED, tests/test_signup.py::test_signup_is_idempotent | - |
| `wrangler-01` | `summary` | `wrangler` | `11283.49` | `0.913` | `1.000` | `0.935` | `1.000` | `0.878` | `0.595` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `2993.88` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `13983.16` | `0.432` | `1.000` | `0.660` | `0.074` | `0.053` | `0.045` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `1009.41` | `0.949` | `1.000` | `0.829` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `3689.59` | `0.416` | `1.000` | `0.694` | `0.000` | `0.000` | `0.077` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `1686.43` | `0.673` | `1.000` | `0.735` | `0.500` | `0.428` | `0.522` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `3691.92` | `0.417` | `1.000` | `0.651` | `0.000` | `0.000` | `0.220` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `1457.19` | `0.863` | `1.000` | `0.912` | `0.833` | `0.722` | `0.556` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `3309.42` | `0.429` | `1.000` | `0.713` | `0.000` | `0.000` | `0.154` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `6167.66` | `0.407` | `1.000` | `0.634` | `0.000` | `0.000` | `0.169` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `2277.69` | `0.554` | `1.000` | `0.899` | `0.000` | `0.000` | `0.840` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `3781.32` | `0.542` | `1.000` | `0.695` | `0.083` | `0.083` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `313.77` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `2937.27` | `0.421` | `1.000` | `0.706` | `0.000` | `0.000` | `0.087` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `14396.59` | `0.422` | `1.000` | `0.707` | `0.000` | `0.000` | `0.097` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `625.90` | `0.540` | `1.000` | `0.801` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `4810.12` | `0.277` | `1.000` | `0.191` | `0.000` | `0.000` | `0.195` | `accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `2358.68` | `0.306` | `1.000` | `0.188` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `junit-01` | `structured` | `junit` | `4963.56` | `0.404` | `0.857` | `0.805` | `0.000` | `0.000` | `0.619` | `soft_accepted` | missing_exact_anchors | --- | - |
| `kubernetes-03` | `structured` | `kubernetes` | `3150.10` | `0.274` | `1.000` | `0.190` | `0.000` | `0.000` | `0.174` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `4042.07` | `0.279` | `0.667` | `0.188` | `0.250` | `0.204` | `0.385` | `soft_accepted` | missing_exact_anchors | line, column, rule | - |
| `docker-build-04` | `structured` | `docker-build` | `833.14` | `0.788` | `0.852` | `0.659` | `0.800` | `0.800` | `1.000` | `accepted` | - | build | - |
| `go-test-04` | `structured` | `go-test` | `9910.91` | `0.320` | `1.000` | `0.364` | `0.000` | `0.000` | `0.103` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `5863.33` | `0.233` | `0.833` | `0.331` | `0.000` | `0.000` | `0.085` | `soft_accepted` | missing_exact_anchors | --- | - |
| `npm-07` | `structured` | `npm` | `1622.20` | `0.724` | `1.000` | `0.460` | `0.714` | `0.714` | `1.000` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `4179.76` | `0.267` | `0.333` | `0.665` | `0.000` | `0.000` | `0.474` | `soft_accepted` | missing_exact_anchors | File, Line, Code, Message, --- | - |
| `gradle-03` | `structured` | `gradle` | `2348.53` | `0.265` | `0.697` | `0.187` | `0.071` | `0.069` | `0.875` | `soft_accepted` | missing_exact_anchors | :api:compileJava | - |
| `playwright-02` | `structured` | `playwright` | `2174.71` | `0.357` | `1.000` | `0.189` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `7605.66` | `0.231` | `0.545` | `0.471` | `0.000` | `0.000` | `0.208` | `soft_accepted` | missing_exact_anchors | errors, file, line | - |
| `vite-01` | `structured` | `vite` | `4687.32` | `0.254` | `1.000` | `0.174` | `0.000` | `0.000` | `0.023` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `2500.79` | `0.192` | `1.000` | `0.322` | `0.000` | `0.000` | `0.200` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `1498.63` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='9f4c2d7a1b8e3c6d0a1234567890abcdef123456<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='9f4c2d7a1b8e3c6d0a1234567890abcdef123456<|im_end|>' |
| `docker-04` | `exact_format` | `docker` | `4095.48` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='pushed ghcr.io/acme/api:2026.05.18 digest: sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='pushed ghcr.io/acme/api:2026.05.18 digest: sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 verified ghcr.io/acme/api@sha256:aaaaaaaa1...' |
| `npm-08` | `exact_format` | `npm` | `1149.60` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 2.18.4 | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='$ npm view @acme/sdk version 2.18.4 npm notice New major version of npm available<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='$ npm view @acme/sdk version 2.18.4 npm notice New major version of npm available<|im_end|>' |
| `go-test-05` | `exact_format` | `go-test` | `220.07` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | github.com/acme/shop/checkout, TestCheckoutAppliesCoupon | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='77<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='77<|im_end|>' |
| `kubectl-09` | `exact_format` | `kubectl` | `1888.35` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | migrator-v2-9xk, prod | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='api-7d9f migrator-v2-9xk worker-123 namespace: prod<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='NAME READY STATUS RESTARTS AGE api-7d9f 1/1 Running 0 1h migrator-v2-9xk 0/1 Error 0 33m worker-123 1/1 Running 0 1h namespace: prod<|im_end|>' |
| `cargo-05` | `exact_format` | `cargo` | `1513.26` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | auth::tests::rejects_expired, billing::tests::rounds_half_even | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='auth::tests::rejects_expired billing::tests::rounds_half_even test result: FAILED. 40 passed; 2 failed<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='auth::tests::rejects_expired billing::tests::rounds_half_even test result: FAILED. 40 passed; 2 failed<|im_end|>' |
| `curl-03` | `exact_format` | `curl` | `216.33` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 503 | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='503<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='503<|im_end|>' |
| `rails-02` | `exact_format` | `rails` | `2722.71` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 20260518133742 | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='20260518133742 AddTenantIdToUsers: migrating ===================== -- add_column(:users, :tenant_id, :uuid) rails aborted! PG::DuplicateColumn: ERROR: column...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='20260518133742 AddTenantIdToUsers: migrating ===================== -- add_column(:users, :tenant_id, :uuid) rails aborted! PG::DuplicateColumn: ERROR: column...' |
| `python-traceback-02` | `explanation` | `python-traceback` | `2029.99` | `0.710` | `0.444` | `0.892` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /repo/scripts/email.py | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `1044.59` | `0.937` | `1.000` | `0.873` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `6254.61` | `0.745` | `1.000` | `0.890` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `2929.06` | `0.960` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `514.14` | `0.954` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `3892.01` | `0.695` | `1.000` | `0.835` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `3508.48` | `0.933` | `1.000` | `0.866` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `3513.12` | `0.984` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `3594.10` | `0.893` | `1.000` | `0.898` | `1.000` | `0.755` | `0.182` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `2584.09` | `0.754` | `1.000` | `0.948` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `package-management-01` | `recall` | `package-management` | `7163.80` | `0.924` | `1.000` | `0.872` | `1.000` | `0.870` | `0.565` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `895.65` | `0.715` | `0.667` | `0.965` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `2444.53` | `0.664` | `0.545` | `0.945` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Program.cs(15,10) | - |
| `package-management-02` | `recall` | `package-management` | `1740.63` | `0.521` | `0.190` | `0.910` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | error[E0277], main.rs:5:26 | - |
| `ci-01` | `recall` | `ci` | `851.77` | `0.962` | `1.000` | `0.846` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `3824.92` | `0.973` | `1.000` | `0.893` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `1011.95` | `0.978` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `3788.47` | `0.742` | `0.778` | `0.892` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "ami" is required | - |
| `compilation-02` | `recall` | `compilation` | `6299.05` | `0.983` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `265.99` | `0.975` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `453.15` | `0.975` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `383.87` | `0.977` | `1.000` | `0.907` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `2728.70` | `0.972` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `2172.88` | `0.962` | `1.000` | `0.846` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `236.85` | `0.996` | `1.000` | `0.984` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `385.96` | `0.969` | `1.000` | `0.876` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `3133.36` | `0.936` | `1.000` | `0.906` | `1.000` | `0.877` | `0.591` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `1432.40` | `0.952` | `1.000` | `0.901` | `1.000` | `0.931` | `0.769` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `1444.38` | `0.404` | `0.000` | `0.891` | `1.000` | `0.857` | `0.524` | `soft_accepted` | missing_exact_anchors | foo.c:5:2, error: expected ';' | - |
| `ci-03` | `recall` | `ci` | `6778.27` | `0.833` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `282.03` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `909.27` | `0.591` | `0.286` | `0.871` | `1.000` | `0.850` | `0.500` | `soft_accepted` | missing_exact_anchors | FAILURE: Build failed with an exception | - |
| `docker-05` | `summary` | `docker` | `2958.56` | `0.820` | `1.000` | `0.823` | `1.000` | `0.782` | `0.273` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `218.05` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `753.87` | `0.689` | `0.524` | `0.865` | `1.000` | `0.967` | `0.889` | `soft_accepted` | missing_exact_anchors | Success: | - |
| `npm-09` | `summary` | `npm` | `1852.21` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `2829.92` | `0.942` | `1.000` | `0.856` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `3382.61` | `0.482` | `1.000` | `0.802` | `0.000` | `0.000` | `0.417` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `1727.11` | `0.439` | `1.000` | `0.760` | `0.000` | `0.000` | `0.105` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `381.54` | `0.688` | `1.000` | `0.628` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `linting-02` | `structured` | `linting` | `1378.98` | `0.433` | `0.667` | `0.365` | `0.417` | `0.417` | `1.000` | `soft_accepted` | missing_exact_anchors | found 1 | - |
| `kubernetes-06` | `structured` | `kubernetes` | `1913.04` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `694.58` | `0.447` | `1.000` | `0.558` | `0.000` | `0.000` | `0.800` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `441.14` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `185.42` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `334.43` | `0.252` | `1.000` | `0.765` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `177.56` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `1213.49` | `0.272` | `1.000` | `0.874` | `0.000` | `0.000` | `0.700` | `accepted` | - | - | - |
| `build-05` | `exact_format` | `build` | `266.81` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `355.84` | `0.582` | `1.000` | `0.657` | `0.500` | `0.400` | `0.333` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `630.80` | `0.908` | `1.000` | `0.892` | `1.000` | `0.886` | `0.619` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `786.10` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `507.52` | `0.958` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `355.35` | `0.950` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `2606.66` | `0.903` | `1.000` | `0.877` | `1.000` | `0.894` | `0.647` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `156.25` | `0.931` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `213.80` | `0.605` | `0.000` | `0.823` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | password authentication failed | - |
| `explanation-01` | `explanation` | `explanation` | `237.17` | `0.934` | `1.000` | `0.867` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `831.11` | `0.889` | `1.000` | `0.879` | `1.000` | `0.850` | `0.500` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `196.32` | `0.950` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `278.42` | `0.937` | `1.000` | `0.875` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `266.42` | `0.950` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `210.62` | `0.903` | `1.000` | `0.807` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `468.35` | `0.954` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `120.31` | `0.920` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `363.83` | `0.950` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `188.23` | `0.948` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `138.34` | `0.916` | `1.000` | `0.833` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `168.43` | `0.933` | `1.000` | `0.865` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `2064.03` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `702.80` | `0.447` | `1.000` | `0.558` | `0.000` | `0.000` | `0.800` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `458.86` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `219.41` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `136.19` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `1196.96` | `0.272` | `1.000` | `0.874` | `0.000` | `0.000` | `0.700` | `accepted` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `238.89` | `0.207` | `1.000` | `0.325` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `4433.61` | `0.227` | `1.000` | `0.791` | `0.000` | `0.000` | `0.750` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `shell-08` | `exact_format` | `shell` | `200.01` | `0.231` | `1.000` | `0.646` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `655.47` | `0.908` | `1.000` | `0.892` | `1.000` | `0.886` | `0.619` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `812.87` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `254.16` | `0.958` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `588.30` | `0.970` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `213.23` | `0.605` | `0.000` | `0.823` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | password authentication failed | - |
| `explanation-15` | `explanation` | `explanation` | `283.07` | `0.963` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `168.23` | `0.913` | `1.000` | `0.825` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `206.34` | `0.961` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `388.61` | `0.939` | `1.000` | `0.878` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
