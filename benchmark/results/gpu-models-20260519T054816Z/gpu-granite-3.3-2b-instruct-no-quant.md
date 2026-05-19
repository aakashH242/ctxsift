# gpu-granite-3.3-2b-instruct-no-quant

## Scenario

- track: `gpu`
- phase: `gpu-screen`
- model: `ibm-granite/granite-3.3-2b-instruct`
- quantization: `none`
- device: `cuda`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `329895.46`
- cpu_rss_bytes: `1794064384`
- gpu_peak_bytes: `5148320256`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `268`
- accepted_count: `204`
- soft_accepted_count: `64`
- rejected_count: `12`
- exact_pass_count: `210`
- avg_inference_ms: `6338.19`
- p95_inference_ms: `20323.57`
- avg_exact_preservation_ratio: `0.890`
- avg_summary_quality_ratio: `0.841`
- avg_format_adherence_score: `0.799`
- avg_instruction_following_score: `0.782`
- avg_brevity_ratio: `0.901`
- avg_case_score: `0.792`
- p10_case_score: `0.430`
- quality_core: `0.720`
- latency_factor: `0.850`
- final_score: `61.16`
- peak_cpu_rss_bytes: `1866665984`
- peak_gpu_bytes: `5494760960`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `3192.98` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-02` | `summary` | `python` | `9844.92` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='- python services/worker.py --queue emails --concurrency 4 - /workspace/services/worker.py - line 11 - ModuleNotFoundError - dramatiq_abort<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='worker boot failed $ python services/worker.py --queue emails --concurrency 4 INFO boot: reading .env.local WARNING redis retry 1/3 failed: ConnectionResetEr...' |
| `python-03` | `recall` | `python` | `2067.10` | `0.983` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `26658.90` | `0.900` | `1.000` | `0.921` | `1.000` | `0.759` | `0.196` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `2106.91` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `8603.64` | `0.797` | `0.909` | `0.951` | `1.000` | `0.973` | `0.909` | `soft_accepted` | missing_exact_anchors | 500 == 409 | - |
| `pytest-02` | `summary` | `pytest` | `3330.35` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `26618.23` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | pytest tests -q -x, tests/jobs/test_retention.py::test_archive_marks_job_deleted, teardown, psycopg.errors.ForeignKeyViolation, job_runs_job_id_fkey, 149 passed, 1 skipped, 1 error in 58.73s | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='``` - pytest tests -q -x - tests/jobs/test_retention.py::test_archive_marks_job_deleted - teardown - psycopg.errors.ForeignKeyViolation - job_runs_job_id_fke...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='149 passed, 1 skipped, 1 error in 58.73s $ pytest tests -q -x ........................................................................ [ 48%] ..................' |
| `pytest-04` | `recall` | `pytest` | `2624.28` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `3742.79` | `0.757` | `0.686` | `0.923` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/unit tests/integration --disable-warnings=0, stripe | - |
| `mypy-01` | `recall` | `mypy` | `3871.58` | `0.662` | `0.537` | `0.950` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mypy src/accounts/user_service.py --show-error-codes, Found 1 error in 1 file | - |
| `mypy-02` | `summary` | `mypy` | `8279.45` | `0.634` | `0.316` | `0.911` | `1.000` | `0.906` | `0.686` | `soft_accepted` | missing_exact_anchors | mypy src tests --pretty --show-error-codes, src/payments/retry.py:118, checked 37 source files | - |
| `mypy-03` | `recall` | `mypy` | `10259.90` | `0.966` | `1.000` | `0.958` | `1.000` | `0.931` | `0.769` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `1937.04` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-02` | `summary` | `ruff` | `1577.77` | `0.991` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `5767.04` | `0.712` | `0.463` | `0.930` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ruff check src/auth/login.py, src/auth/login.py:93:13 | - |
| `pylint-01` | `recall` | `pylint` | `4449.05` | `0.635` | `0.476` | `0.931` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pylint src/storage/path_utils.py, src/storage/path_utils.py:27:18 | - |
| `pylint-02` | `recall` | `pylint` | `14276.03` | `0.974` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `3683.31` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `6120.37` | `0.807` | `0.900` | `0.935` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 41 files would be left unchanged | - |
| `black-02` | `summary` | `black` | `3299.63` | `0.981` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `1212.68` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `12541.97` | `0.972` | `1.000` | `0.926` | `1.000` | `0.970` | `0.900` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `8635.89` | `0.782` | `0.778` | `0.940` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERESOLVE | - |
| `npm-03` | `summary` | `npm` | `7925.06` | `0.982` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `2047.63` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `23707.99` | `0.981` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `25522.82` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `17365.47` | `0.983` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `11674.69` | `0.996` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `16300.11` | `0.960` | `1.000` | `0.960` | `1.000` | `0.951` | `0.837` | `accepted` | - | - | - |
| `eslint-01` | `recall` | `eslint` | `33716.54` | `0.937` | `1.000` | `0.931` | `1.000` | `0.862` | `0.542` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `13862.05` | `0.730` | `0.500` | `0.961` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | eslint ., ESLint: 9.14.0 | - |
| `eslint-03` | `recall` | `eslint` | `6624.71` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `10744.87` | `0.984` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `3456.71` | `0.985` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `7145.93` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `7354.61` | `0.796` | `0.833` | `0.945` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | could not be found | - |
| `docker-compose-02` | `recall` | `docker-compose` | `3314.44` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `11417.16` | `0.966` | `1.000` | `0.928` | `1.000` | `0.990` | `0.968` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `14881.73` | `0.983` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `16229.63` | `0.710` | `0.684` | `0.926` | `1.000` | `0.988` | `0.960` | `soft_accepted` | missing_exact_anchors | kubectl describe pod api-7d9f7bbd8c-rx2kq -n staging | - |
| `kubectl-03` | `summary` | `kubectl` | `4552.46` | `0.815` | `0.889` | `0.966` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | timed out waiting for the condition | - |
| `kubectl-04` | `recall` | `kubectl` | `8815.53` | `0.988` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `9071.02` | `0.764` | `0.647` | `0.969` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform validate | - |
| `terraform-02` | `recall` | `terraform` | `14834.67` | `0.720` | `0.684` | `0.956` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform plan | - |
| `terraform-03` | `recall` | `terraform` | `16581.40` | `0.789` | `0.871` | `0.945` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | state snapshot | - |
| `terraform-04` | `summary` | `terraform` | `24856.22` | `0.982` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `6416.78` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `23187.52` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `10285.66` | `0.679` | `0.600` | `0.916` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | git rebase origin/main | - |
| `git-02` | `recall` | `git` | `3896.93` | `0.978` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `16576.87` | `0.700` | `0.625` | `0.969` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | curl 56 | - |
| `curl-01` | `recall` | `curl` | `19999.82` | `0.989` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `39172.18` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | curl -I https://docs.example.com/sdk/latest, HTTP/2 301, location: /sdk/v3.4/, cache-control: max-age=3600 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='- HTTP/2 301 - date: Sat, 16 May 2026 07:14:19 GMT - content-type: text/html; charset=UTF-8 - content-length: 167 - location: /sdk/v3.4/ - cache-control: max...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='HTTP/2 301 - location: /sdk/v3.4/ - cache-control: max-age=3600 $ curl -I https://docs.example.com/sdk/latest HTTP/2 301 date: Sat, 16 May 2026 07:14:19 GMT ...' |
| `ssh-01` | `summary` | `ssh` | `8150.56` | `0.984` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `8684.29` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `13993.54` | `0.767` | `0.677` | `0.958` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | status=203/EXEC | - |
| `systemd-02` | `summary` | `systemd` | `9698.40` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `34359.62` | `0.946` | `1.000` | `0.912` | `1.000` | `0.962` | `0.875` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `26905.81` | `0.671` | `0.571` | `0.928` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | sudo dnf install python3-devel postgresql-devel | - |
| `go-build-01` | `summary` | `go-build` | `20009.42` | `0.977` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `10407.37` | `0.974` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `20342.99` | `0.804` | `0.867` | `0.949` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | cannot find symbol | - |
| `maven-01` | `summary` | `maven` | `28140.49` | `0.769` | `0.913` | `0.939` | `1.000` | `0.902` | `0.673` | `soft_accepted` | missing_exact_anchors | UserControllerTest.getUser_notFound_returns404 | - |
| `maven-02` | `summary` | `maven` | `20287.53` | `0.976` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `48706.16` | `0.905` | `1.000` | `0.932` | `1.000` | `0.767` | `0.224` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `14090.90` | `0.947` | `1.000` | `0.900` | `1.000` | `0.974` | `0.912` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `31498.36` | `0.940` | `1.000` | `0.918` | `1.000` | `0.946` | `0.821` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `14603.91` | `0.730` | `0.500` | `0.959` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | cargo build | - |
| `node-runtime-01` | `recall` | `node-runtime` | `60724.90` | `0.693` | `1.000` | `0.917` | `0.500` | `0.404` | `0.359` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `npm-04` | `summary` | `npm` | `8340.57` | `0.810` | `0.895` | `0.949` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | dashboard-web@0.9.0 | - |
| `tsc-01` | `summary` | `tsc` | `8067.81` | `0.800` | `0.882` | `0.927` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | userId | - |
| `eslint-04` | `summary` | `eslint` | `1925.22` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `1700.52` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `18788.20` | `0.871` | `1.000` | `0.922` | `1.000` | `0.804` | `0.346` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `4169.65` | `0.923` | `1.000` | `0.871` | `1.000` | `0.950` | `0.833` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `7574.23` | `0.711` | `0.467` | `0.925` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund | - |
| `docker-compose-04` | `summary` | `docker-compose` | `1234.32` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `2807.26` | `0.954` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `4387.05` | `0.818` | `1.000` | `0.907` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `2550.20` | `0.995` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `4878.88` | `0.961` | `1.000` | `0.941` | `1.000` | `0.928` | `0.759` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `3592.77` | `0.666` | `0.267` | `0.918` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform validate, main.tf line 27 | - |
| `terraform-07` | `summary` | `terraform` | `18683.70` | `0.860` | `1.000` | `0.914` | `1.000` | `0.790` | `0.299` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `3681.99` | `0.734` | `0.611` | `0.903` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "server" directive is not allowed here, configuration file /etc/nginx/nginx.conf test failed | - |
| `nginx-02` | `summary` | `nginx` | `5347.86` | `0.980` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `2580.16` | `0.996` | `1.000` | `0.986` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `2505.74` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `5302.19` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `2148.42` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `9075.20` | `0.949` | `1.000` | `0.948` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `1931.25` | `0.989` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `6739.97` | `0.647` | `0.524` | `0.901` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | line=91, Ruff F821, exit code 2 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `7593.28` | `0.971` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `883.52` | `0.967` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `1820.29` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `3354.58` | `0.965` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `1615.80` | `0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `1882.42` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `8718.80` | `0.805` | `0.909` | `0.952` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ROUND_HALF_UP is deprecated for discounts; use ROUND_HALF_EVEN | - |
| `compiler-error-01` | `recall` | `compiler-error` | `11496.13` | `0.725` | `0.701` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | req.method(), req.clone().into_body() | - |
| `ci-log-01` | `recall` | `ci-log` | `8099.41` | `0.971` | `1.000` | `0.939` | `1.000` | `0.959` | `0.863` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `4878.52` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `9523.30` | `0.876` | `1.000` | `0.941` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `build-log-01` | `summary` | `build-log` | `3142.11` | `0.960` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `1279.11` | `0.774` | `1.000` | `0.935` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `4992.72` | `0.608` | `1.000` | `0.715` | `0.400` | `0.320` | `0.333` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `16022.36` | `0.437` | `1.000` | `0.703` | `0.000` | `0.000` | `0.262` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `3281.27` | `0.656` | `0.355` | `0.667` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `7182.44` | `0.843` | `1.000` | `0.825` | `0.812` | `0.741` | `0.707` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `8249.22` | `0.431` | `0.905` | `0.833` | `0.000` | `0.000` | `0.758` | `soft_accepted` | missing_exact_anchors | port 5432 is already allocated | - |
| `structured-output-03` | `structured` | `structured-output` | `7278.74` | `0.463` | `1.000` | `0.542` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-04` | `structured` | `structured-output` | `3762.63` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `4144.76` | `0.209` | `1.000` | `0.339` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `4369.60` | `0.148` | `0.714` | `0.457` | `0.000` | `0.000` | `0.429` | `soft_accepted` | missing_exact_anchors | SearchBox debounces network query before fetch | - |
| `exact-format-03` | `exact_format` | `exact-format` | `6876.36` | `0.068` | `0.000` | `0.300` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ghcr.io/acme/worker@sha256:4f8c2e0b1d9a6c7e5f3a2b1908d4c6e7f0a123456789abcdeffedcba98765432 | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `11148.24` | `0.698` | `1.000` | `0.904` | `0.500` | `0.453` | `0.687` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `12212.25` | `0.889` | `1.000` | `0.858` | `1.000` | `0.881` | `0.603` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `22001.19` | `0.694` | `1.000` | `0.909` | `0.000` | `0.000` | `0.390` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `6948.72` | `0.806` | `0.905` | `0.965` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | retries exhausted for queue emails | - |
| `mypy-05` | `recall` | `mypy` | `3670.69` | `0.979` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `7230.03` | `0.806` | `0.905` | `0.965` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | module.worker.aws_iam_policy.worker_inline | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `10678.11` | `0.748` | `1.000` | `0.919` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `3045.80` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `2444.41` | `0.983` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `2392.66` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `8111.58` | `0.981` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `9157.71` | `0.772` | `0.821` | `0.953` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | packages/api/src/index.ts:4:25 | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `9668.02` | `0.794` | `0.905` | `0.906` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | exit code 1 | - |
| `pnpm-04` | `recall` | `pnpm` | `2044.57` | `0.992` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `6016.49` | `0.986` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `6489.56` | `0.756` | `0.783` | `0.947` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | key :ttl not found | - |
| `rails-01` | `recall` | `rails` | `8447.04` | `0.725` | `0.706` | `0.943` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 20260518093012_add_index_to_events_request_id.rb:3 | - |
| `phpunit-01` | `recall` | `phpunit` | `2950.67` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `9854.84` | `0.713` | `0.750` | `0.907` | `1.000` | `0.923` | `0.744` | `soft_accepted` | missing_exact_anchors | duplicate location "/api" | - |
| `postgres-03` | `recall` | `postgres` | `3772.14` | `0.730` | `0.722` | `0.934` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | embedding vector(1536) | - |
| `ansible-02` | `recall` | `ansible` | `2209.35` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `15419.51` | `0.975` | `1.000` | `0.945` | `1.000` | `0.968` | `0.894` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `7613.40` | `0.719` | `0.688` | `0.945` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | FullyQualifiedErrorId : UnauthorizedAccess | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `7667.01` | `0.964` | `1.000` | `0.920` | `1.000` | `0.951` | `0.838` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `11834.21` | `0.972` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `2797.70` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `5541.74` | `0.971` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `1972.97` | `0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `4495.42` | `0.960` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `5008.15` | `0.704` | `0.478` | `0.896` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | checks, http_req_duration, avg | - |
| `composer-01` | `summary` | `composer` | `3738.38` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `6610.73` | `0.965` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `9914.40` | `0.739` | `1.000` | `0.925` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `4015.18` | `0.970` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `892.29` | `0.963` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `4971.49` | `0.785` | `0.833` | `0.912` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `2229.59` | `0.967` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `4817.40` | `0.972` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `2934.49` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `3538.99` | `0.532` | `1.000` | `0.691` | `0.200` | `0.167` | `0.444` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `2927.45` | `0.473` | `0.882` | `0.934` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | JWT expiry from 15m to 7d | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `1288.46` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `1746.87` | `0.945` | `1.000` | `0.818` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `4329.51` | `0.533` | `1.000` | `0.777` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `2379.28` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `3339.01` | `0.421` | `0.750` | `0.817` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | [deps 4/4] | - |
| `terraform-09` | `instruction_following` | `terraform` | `909.38` | `0.517` | `1.000` | `0.723` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `3185.92` | `0.590` | `1.000` | `0.967` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `1304.22` | `0.611` | `1.000` | `0.704` | `0.250` | `0.250` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `638.92` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `2187.01` | `0.454` | `1.000` | `0.679` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `6661.46` | `0.493` | `1.000` | `0.755` | `0.000` | `0.000` | `0.667` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `2017.22` | `0.527` | `1.000` | `0.756` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `4484.92` | `0.339` | `1.000` | `0.183` | `0.000` | `0.000` | `0.842` | `accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `6093.63` | `0.609` | `0.667` | `0.433` | `0.883` | `0.883` | `1.000` | `soft_accepted` | missing_exact_anchors | resource, field | - |
| `junit-01` | `structured` | `junit` | `2678.88` | `0.944` | `1.000` | `0.814` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `2088.28` | `0.359` | `1.000` | `0.198` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `6378.84` | `0.594` | `1.000` | `0.410` | `0.632` | `0.476` | `0.179` | `accepted` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `4333.01` | `0.579` | `1.000` | `0.448` | `0.548` | `0.426` | `0.259` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `3212.76` | `0.579` | `1.000` | `0.958` | `0.000` | `0.000` | `0.917` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `3891.62` | `0.457` | `1.000` | `0.689` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `1966.43` | `0.616` | `1.000` | `0.275` | `0.583` | `0.583` | `1.000` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `6459.16` | `0.484` | `0.867` | `0.985` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --- | - |
| `gradle-03` | `structured` | `gradle` | `4984.34` | `0.383` | `1.000` | `0.193` | `0.221` | `0.179` | `0.368` | `accepted` | - | - | - |
| `playwright-02` | `structured` | `playwright` | `10778.75` | `0.262` | `0.833` | `0.193` | `0.000` | `0.000` | `0.833` | `soft_accepted` | missing_exact_anchors | project | - |
| `postgres-04` | `structured` | `postgres` | `2281.31` | `0.569` | `1.000` | `0.916` | `0.000` | `0.000` | `0.938` | `accepted` | - | - | - |
| `vite-01` | `structured` | `vite` | `4977.18` | `0.259` | `1.000` | `0.180` | `0.000` | `0.000` | `0.053` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `2370.98` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | tests/test_a.py::test_one, tests/test_b.py::TestB::test_three | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='tests/test_a.py::test_one tests/test_b.py::TestB::test_three<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='tests/test_a.py::test_one, tests/test_b.py::TestB::test_three<|end_of_text|>' |
| `git-04` | `exact_format` | `git` | `3108.39` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='9f4c2d7a1b8e3c6d0a1234567890abcdef123456<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='9f4c2d7a1b8e3c6d0a1234567890abcdef123456<|end_of_text|>' |
| `docker-04` | `exact_format` | `docker` | `7657.61` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='- ghcr.io/acme/api:2026.05.18 - digest: sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 - verified ghcr.io/acme/api@sha256:aaaaaaaa11...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444<|end_of_text|>' |
| `npm-08` | `exact_format` | `npm` | `641.28` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 2.18.4 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='2.18.4<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='2.18.4<|end_of_text|>' |
| `go-test-05` | `exact_format` | `go-test` | `4646.11` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | github.com/acme/shop/checkout, TestCheckoutAppliesCoupon | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='--- FAIL: TestCheckoutAppliesCoupon (0.01s) checkout_test.go:77: got 120 want 100 FAIL github.com/acme/shop/checkout 0.31s<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='--- FAIL: TestCheckoutAppliesCoupon (0.01s) checkout_test.go:77: got 120 want 100 FAIL github.com/acme/shop/checkout 0.31s<|end_of_text|>' |
| `kubectl-09` | `exact_format` | `kubectl` | `1070.99` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | migrator-v2-9xk, prod | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='migrator-v2-9xk, prod<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='migrator-v2-9xk, prod<|end_of_text|>' |
| `cargo-05` | `exact_format` | `cargo` | `2949.42` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | auth::tests::rejects_expired, billing::tests::rounds_half_even | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='failures: auth::tests::rejects_expired, billing::tests::rounds_half_even test result: FAILED. 40 passed; 2 failed<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='failures: auth::tests::rejects_expired, billing::tests::rounds_half_even test result: FAILED. 40 passed; 2 failed<|end_of_text|>' |
| `curl-03` | `exact_format` | `curl` | `425.11` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 503 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='503<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='503<|end_of_text|>' |
| `rails-02` | `exact_format` | `rails` | `1365.73` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 20260518133742 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='20260518133742<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='20260518133742<|end_of_text|>' |
| `python-traceback-02` | `explanation` | `python-traceback` | `1292.53` | `0.965` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `7903.60` | `0.922` | `1.000` | `0.844` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `10345.79` | `0.692` | `1.000` | `0.857` | `0.000` | `0.000` | `0.632` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `1784.29` | `0.968` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `1181.22` | `0.960` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `4015.54` | `0.728` | `0.750` | `0.814` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | returns a reference | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `4561.06` | `0.932` | `1.000` | `0.864` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `4820.79` | `0.910` | `1.000` | `0.918` | `1.000` | `0.791` | `0.304` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `4343.54` | `0.950` | `1.000` | `0.933` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `2006.79` | `0.956` | `1.000` | `0.949` | `1.000` | `0.908` | `0.692` | `accepted` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `3180.90` | `0.973` | `1.000` | `0.894` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `4020.90` | `0.669` | `0.667` | `0.925` | `1.000` | `0.868` | `0.560` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `5179.64` | `0.931` | `1.000` | `0.934` | `1.000` | `0.843` | `0.476` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `3884.94` | `0.964` | `1.000` | `0.923` | `1.000` | `0.950` | `0.833` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `1520.44` | `0.714` | `0.714` | `0.873` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 5 tests run, 1 failure | - |
| `testing-03` | `recall` | `testing` | `2048.26` | `0.981` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `3480.80` | `0.978` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `2441.31` | `0.751` | `0.778` | `0.934` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "ami" is required | - |
| `compilation-02` | `recall` | `compilation` | `3268.66` | `0.985` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `1222.42` | `0.439` | `0.000` | `0.900` | `1.000` | `0.973` | `0.909` | `soft_accepted` | missing_exact_anchors | Installing npm modules, failed with exit code 1 | - |
| `build-01` | `recall` | `build` | `1822.18` | `0.975` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `3935.95` | `0.973` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `1060.05` | `0.979` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1907.35` | `0.962` | `1.000` | `0.848` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `1300.41` | `0.996` | `1.000` | `0.984` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `2237.07` | `0.982` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `1491.42` | `0.965` | `1.000` | `0.911` | `1.000` | `0.960` | `0.867` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `4018.38` | `0.617` | `0.417` | `0.955` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | User signs in, capybara-3.34.0/lib/capybara/node/element.rb:1008 | - |
| `build-02` | `recall` | `build` | `3869.95` | `0.601` | `0.500` | `0.898` | `1.000` | `0.874` | `0.579` | `soft_accepted` | missing_exact_anchors | error: expected ';' | - |
| `ci-03` | `recall` | `ci` | `4030.88` | `0.833` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `577.47` | `0.974` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `3474.78` | `0.840` | `1.000` | `0.864` | `1.000` | `0.790` | `0.300` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `1427.79` | `0.921` | `1.000` | `0.895` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `1493.50` | `0.884` | `1.000` | `0.924` | `1.000` | `0.829` | `0.429` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `1107.43` | `0.779` | `0.810` | `0.909` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 5 passed | - |
| `npm-09` | `summary` | `npm` | `1489.51` | `0.915` | `1.000` | `0.938` | `1.000` | `0.880` | `0.600` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `1061.87` | `0.931` | `1.000` | `0.827` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `1338.44` | `0.577` | `1.000` | `0.924` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `2973.45` | `0.438` | `1.000` | `0.757` | `0.000` | `0.000` | `0.111` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `5016.86` | `0.440` | `1.000` | `0.763` | `0.000` | `0.000` | `0.111` | `accepted` | - | - | - |
| `linting-02` | `structured` | `linting` | `4219.84` | `0.355` | `1.000` | `0.183` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `2144.95` | `0.579` | `1.000` | `0.957` | `0.000` | `0.000` | `0.923` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `1234.16` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `620.51` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `367.02` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `630.24` | `0.242` | `1.000` | `0.588` | `0.000` | `0.000` | `0.667` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `444.48` | `0.232` | `1.000` | `0.655` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `4617.84` | `0.265` | `1.000` | `0.798` | `0.000` | `0.000` | `0.700` | `accepted` | - | - | - |
| `build-05` | `exact_format` | `build` | `424.37` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `712.76` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `1129.53` | `0.933` | `1.000` | `0.893` | `1.000` | `0.960` | `0.867` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `1335.15` | `0.928` | `1.000` | `0.897` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `1801.34` | `0.967` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `1362.01` | `0.954` | `1.000` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `971.72` | `0.955` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `1334.73` | `0.931` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `2378.51` | `0.937` | `1.000` | `0.873` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `1412.35` | `0.943` | `1.000` | `0.886` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `2790.76` | `0.924` | `1.000` | `0.849` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `1227.58` | `0.949` | `1.000` | `0.919` | `1.000` | `0.967` | `0.889` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `1208.40` | `0.939` | `1.000` | `0.878` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `892.64` | `0.947` | `1.000` | `0.894` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `618.85` | `0.919` | `1.000` | `0.837` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `2858.54` | `0.909` | `1.000` | `0.843` | `1.000` | `0.962` | `0.875` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `1059.21` | `0.939` | `1.000` | `0.879` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `573.27` | `0.943` | `1.000` | `0.886` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `1503.35` | `0.948` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `1587.84` | `0.907` | `1.000` | `0.877` | `1.000` | `0.905` | `0.682` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `964.25` | `0.933` | `1.000` | `0.865` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `2167.71` | `0.579` | `1.000` | `0.957` | `0.000` | `0.000` | `0.923` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `1221.80` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `626.58` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `370.23` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `374.18` | `0.700` | `1.000` | `0.335` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `4649.26` | `0.265` | `1.000` | `0.798` | `0.000` | `0.000` | `0.700` | `accepted` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `414.37` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `300.59` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `498.80` | `0.251` | `1.000` | `0.759` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `1141.29` | `0.933` | `1.000` | `0.893` | `1.000` | `0.960` | `0.867` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `1324.19` | `0.928` | `1.000` | `0.897` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `486.37` | `0.948` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `1787.06` | `0.966` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `2390.54` | `0.937` | `1.000` | `0.873` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `1429.01` | `0.966` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `2980.33` | `0.926` | `1.000` | `0.852` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `1205.31` | `0.925` | `1.000` | `0.916` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1001.33` | `0.931` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
