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

- load_ms: `104640.72`
- cpu_rss_bytes: `1749520384`
- gpu_peak_bytes: `5151123968`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `238`
- accepted_count: `169`
- soft_accepted_count: `69`
- rejected_count: `42`
- exact_pass_count: `176`
- avg_inference_ms: `4657.43`
- p95_inference_ms: `10703.16`
- avg_exact_preservation_ratio: `0.770`
- avg_summary_quality_ratio: `0.760`
- avg_format_adherence_score: `0.795`
- avg_instruction_following_score: `0.779`
- avg_brevity_ratio: `0.929`
- avg_case_score: `0.731`
- p10_case_score: `0.000`
- quality_core: `0.585`
- latency_factor: `0.881`
- final_score: `51.54`
- peak_cpu_rss_bytes: `1751486464`
- peak_gpu_bytes: `5510016000`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `5142.06` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-02` | `summary` | `python` | `9249.75` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass="- python services/worker.py --queue emails --concurrency 4 - ModuleNotFoundError: No module named 'dramatiq_abort' - worker boot failed<|end_of_text|>" repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass="ModuleNotFoundError: No module named 'dramatiq_abort' - worker boot failed ``` ``` $ python services/worker.py --queue emails --concurrency 4 INFO boot: read..." |
| `python-03` | `recall` | `python` | `2345.57` | `0.985` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `6780.97` | `0.761` | `0.792` | `0.956` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | line 119 | - |
| `python-05` | `recall` | `python` | `2262.97` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `7270.24` | `0.984` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `4313.98` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `10535.19` | `0.939` | `1.000` | `0.947` | `1.000` | `0.857` | `0.523` | `accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `3165.80` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `3550.61` | `0.757` | `0.686` | `0.923` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/unit tests/integration --disable-warnings=0, stripe | - |
| `mypy-01` | `recall` | `mypy` | `5385.13` | `0.731` | `0.707` | `0.968` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mypy src/accounts/user_service.py --show-error-codes | - |
| `mypy-02` | `summary` | `mypy` | `9098.04` | `0.634` | `0.316` | `0.911` | `1.000` | `0.906` | `0.686` | `soft_accepted` | missing_exact_anchors | mypy src tests --pretty --show-error-codes, src/payments/retry.py:118, checked 37 source files | - |
| `mypy-03` | `recall` | `mypy` | `8802.84` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `1836.64` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-02` | `summary` | `ruff` | `1501.57` | `0.991` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `5507.67` | `0.712` | `0.463` | `0.930` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ruff check src/auth/login.py, src/auth/login.py:93:13 | - |
| `pylint-01` | `recall` | `pylint` | `5555.24` | `0.638` | `0.476` | `0.945` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pylint src/storage/path_utils.py, src/storage/path_utils.py:27:18 | - |
| `pylint-02` | `recall` | `pylint` | `7498.11` | `0.754` | `0.789` | `0.929` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pylint src/config/runtime.py src/api/server.py | - |
| `pylint-03` | `summary` | `pylint` | `3591.05` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `6492.76` | `0.807` | `0.900` | `0.935` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 41 files would be left unchanged | - |
| `black-02` | `summary` | `black` | `3516.82` | `0.981` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `1334.38` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `4973.32` | `0.981` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `9688.53` | `0.782` | `0.778` | `0.940` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERESOLVE | - |
| `npm-03` | `summary` | `npm` | `7841.67` | `0.982` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `2225.58` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `9446.31` | `0.981` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `8932.47` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `6168.91` | `0.983` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `2340.88` | `0.992` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `5181.95` | `0.960` | `1.000` | `0.960` | `1.000` | `0.951` | `0.837` | `accepted` | - | - | - |
| `eslint-01` | `recall` | `eslint` | `7890.86` | `0.640` | `0.560` | `0.928` | `1.000` | `0.905` | `0.684` | `soft_accepted` | missing_exact_anchors | eslint src --format stylish, 3 problems (2 errors, 1 warning) | - |
| `eslint-02` | `summary` | `eslint` | `4722.76` | `0.730` | `0.500` | `0.961` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | eslint ., ESLint: 9.14.0 | - |
| `eslint-03` | `recall` | `eslint` | `2466.58` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `2894.73` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `1203.20` | `0.985` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `2431.62` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `2567.75` | `0.796` | `0.833` | `0.945` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | could not be found | - |
| `docker-compose-02` | `recall` | `docker-compose` | `1316.57` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `4005.02` | `0.966` | `1.000` | `0.928` | `1.000` | `0.990` | `0.968` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `5121.79` | `0.983` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `24676.73` | `0.906` | `1.000` | `0.936` | `1.000` | `0.767` | `0.222` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `3214.19` | `0.815` | `0.889` | `0.966` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | timed out waiting for the condition | - |
| `kubectl-04` | `recall` | `kubectl` | `2883.78` | `0.988` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `3108.39` | `0.764` | `0.647` | `0.969` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform validate | - |
| `terraform-02` | `recall` | `terraform` | `4692.52` | `0.680` | `0.579` | `0.958` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform plan, aws_security_group.db.id | - |
| `terraform-03` | `recall` | `terraform` | `3847.39` | `0.793` | `0.871` | `0.962` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | v1.5.7 | - |
| `terraform-04` | `summary` | `terraform` | `8243.83` | `0.982` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `6064.97` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `7728.93` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `2931.18` | `0.979` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `3491.72` | `0.678` | `0.593` | `0.924` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | main -> main, failed to push some refs | - |
| `git-03` | `recall` | `git` | `5499.28` | `0.992` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `7146.63` | `0.989` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `7219.12` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | curl -I https://docs.example.com/sdk/latest, HTTP/2 301, location: /sdk/v3.4/, cache-control: max-age=3600 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- HTTP/2 301 - location: /sdk/v3.4/ - cache-control: max-age=3600<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='$ curl -I https://docs.example.com/sdk/latest HTTP/2 301 date: Sat, 16 May 2026 07:14:19 GMT content-type: text/html; charset=UTF-8 content-length: 167 locat...' |
| `ssh-01` | `summary` | `ssh` | `2733.59` | `0.984` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `2762.42` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `5000.02` | `0.767` | `0.677` | `0.958` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | status=203/EXEC | - |
| `systemd-02` | `summary` | `systemd` | `3640.03` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `10972.61` | `0.946` | `1.000` | `0.912` | `1.000` | `0.962` | `0.875` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `28351.20` | `0.905` | `1.000` | `0.940` | `1.000` | `0.760` | `0.200` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `6463.11` | `0.977` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `5021.61` | `0.974` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `4209.93` | `0.715` | `0.467` | `0.937` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | javac -d out $(find src/main/java -name '*.java'), cannot find symbol | - |
| `maven-01` | `summary` | `maven` | `9710.79` | `0.769` | `0.913` | `0.939` | `1.000` | `0.902` | `0.673` | `soft_accepted` | missing_exact_anchors | UserControllerTest.getUser_notFound_returns404 | - |
| `maven-02` | `summary` | `maven` | `6937.82` | `0.976` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `6964.56` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `4753.26` | `0.947` | `1.000` | `0.900` | `1.000` | `0.974` | `0.912` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `5774.79` | `0.599` | `0.000` | `0.888` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | cargo build, error[E0308], src/config.rs:27:18, ingest-cli | - |
| `cargo-02` | `summary` | `cargo` | `6886.47` | `0.730` | `0.500` | `0.959` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | cargo build | - |
| `node-runtime-01` | `recall` | `node-runtime` | `21632.00` | `0.693` | `1.000` | `0.922` | `0.500` | `0.403` | `0.354` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `npm-04` | `summary` | `npm` | `9238.35` | `0.810` | `0.895` | `0.949` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | dashboard-web@0.9.0 | - |
| `tsc-01` | `summary` | `tsc` | `8614.95` | `0.800` | `0.882` | `0.927` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | userId | - |
| `eslint-04` | `summary` | `eslint` | `2572.17` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `2354.77` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `18846.76` | `0.871` | `1.000` | `0.922` | `1.000` | `0.804` | `0.346` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `4261.42` | `0.923` | `1.000` | `0.871` | `1.000` | `0.950` | `0.833` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `5981.78` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund, Dockerfile:8, zod@3.23.8, failed to solve | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='Dockerfile:8 > 8 | >>> RUN npm ci --no-audit --no-fund > > ERROR: failed to solve: process "/bin/sh -c npm ci --no-audit --no-fund" did not complete successf...' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='docker build -t example/web:dev . Dockerfile:8 > RUN npm ci --no-audit --no-fund ERROR: failed to solve: process "/bin/sh -c npm ci --no-audit --no-fund" did...' |
| `docker-compose-04` | `summary` | `docker-compose` | `1340.61` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `2811.70` | `0.954` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `4402.78` | `0.818` | `1.000` | `0.907` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `2441.71` | `0.995` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `5073.64` | `0.943` | `1.000` | `0.928` | `1.000` | `0.883` | `0.611` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `3582.96` | `0.666` | `0.267` | `0.918` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform validate, main.tf line 27 | - |
| `terraform-07` | `summary` | `terraform` | `18560.94` | `0.860` | `1.000` | `0.914` | `1.000` | `0.790` | `0.299` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `3776.27` | `0.734` | `0.611` | `0.903` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "server" directive is not allowed here, configuration file /etc/nginx/nginx.conf test failed | - |
| `nginx-02` | `summary` | `nginx` | `5356.04` | `0.980` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `6019.53` | `0.977` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `2495.83` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `5313.82` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `2177.89` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `8903.65` | `0.949` | `1.000` | `0.948` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `1569.65` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `9178.24` | `0.941` | `1.000` | `0.908` | `1.000` | `0.891` | `0.636` | `accepted` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `7412.10` | `0.971` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `840.20` | `0.967` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `1724.85` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `3478.46` | `0.965` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `1674.04` | `0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `2031.42` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `3801.15` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `9769.76` | `0.756` | `1.000` | `0.956` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-log-01` | `recall` | `ci-log` | `9346.79` | `0.964` | `1.000` | `0.935` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `4534.46` | `0.994` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `6282.86` | `0.800` | `0.857` | `0.943` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | total = 42.00, want 37.00, test timed out after 10m0s | - |
| `build-log-01` | `summary` | `build-log` | `2974.55` | `0.960` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `2916.03` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | Dockerfile:18, COPY apps/web ./apps/web, "/apps/web": not found | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='Dockerfile:18 ERROR: failed to calculate checksum of ref 91cf823e-4d44-4fc6-9a85::h2x: "/apps/web": not found<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='Dockerfile:18 COPY apps/web ./apps/web<|end_of_text|>' |
| `lint-output-01` | `instruction_following` | `lint-output` | `4836.03` | `0.608` | `1.000` | `0.715` | `0.400` | `0.320` | `0.333` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `19144.18` | `0.664` | `0.810` | `0.731` | `0.750` | `0.750` | `1.000` | `soft_accepted` | missing_exact_anchors | User.lastLoginIp, DROP COLUMN refresh_token_expires_at | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `6576.11` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | search endpoint failed after 2 attempts, exit status 22, https://staging.example.com/api/search?q=smoke, curl: (22) | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='exit status 22, search endpoint failed after 2 attempts<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='$ ./scripts/smoke.sh --env staging [stderr] smoke.sh: search endpoint failed after 2 attempts [stderr] exit status 22 [stderr] curl: (22) The requested URL r...' |
| `structured-output-01` | `structured` | `structured-output` | `6545.16` | `0.847` | `1.000` | `0.820` | `0.812` | `0.755` | `0.763` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `7370.14` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | test / integration, Start docker compose, port 5432 is already allocated, deploy / preview, Upload artifact, dist/preview | granite output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml - failed_jobs: - job: deploy / preview step: Upload artifact exit_code: 1 cause: No files were found with the provided path: dist/preview - job: test...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml - test / integration step: Start docker compose cause: service "postgres" failed to start: Bind for 0.0.0.0:5432 failed: port is already allocated ex...' |
| `structured-output-03` | `structured` | `structured-output` | `7037.98` | `0.826` | `0.929` | `0.954` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "refresh token expired" | - |
| `structured-output-04` | `structured` | `structured-output` | `3579.74` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `5961.41` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | tests/api/test_users.py::test_create_user_requires_email, tests/api/test_users.py::test_delete_user_requires_admin, tests/jobs/test_reconcile.py::TestReconcile::test_retries_deadlock | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- tests/api/test_users.py::test_create_user_requires_email - tests/api/test_users.py::test_delete_user_requires_admin - tests/jobs/test_reconcile.py::TestRec...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='tests/api/test_users.py::test_create_user_requires_email tests/api/test_users.py::test_delete_user_requires_admin tests/jobs/test_reconcile.py::TestReconcile...' |
| `exact-format-02` | `exact_format` | `exact-format` | `3359.54` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | packages/web/src/search/searchBox.test.tsx, SearchBox debounces network query before fetch | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='``` jest packages/web/src/search/searchBox.test.tsx --findTestsFor=SearchBox.debounces network query before fetch ```<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='``` return only the requested value, command, identifier, or lines: packages/web/src/search/searchBox.test.tsx SearchBox debounces network query before fetch...' |
| `exact-format-03` | `exact_format` | `exact-format` | `5362.19` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | ghcr.io/acme/worker@sha256:4f8c2e0b1d9a6c7e5f3a2b1908d4c6e7f0a123456789abcdeffedcba98765432 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='4f8c2e0b1d9a6c7e5f3a2b1908d4c6e7f0a123456789abcdeffedcba98765432<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='ghcr.io/acme/worker@sha256:4f8c2e0b1d9a6c7e5f3a2b1908d4c6e7f0a123456789abcdeffedcba98765432<|end_of_text|>' |
| `diagnosis-01` | `explanation` | `diagnosis` | `10699.54` | `0.698` | `1.000` | `0.904` | `0.500` | `0.453` | `0.687` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `11918.63` | `0.889` | `1.000` | `0.858` | `1.000` | `0.881` | `0.603` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `10545.66` | `0.854` | `1.000` | `0.908` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `7408.14` | `0.745` | `0.762` | `0.936` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | line 92 | - |
| `mypy-05` | `recall` | `mypy` | `3461.28` | `0.979` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `10512.06` | `0.528` | `0.190` | `0.943` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | module.worker.aws_iam_policy.worker_inline, status code: 409, request id: 0f3e2b11-9ac9-4fd2-a3bb-6c07a3c6a90d, modules/worker/iam.tf line 27 | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `5958.65` | `0.668` | `0.565` | `0.925` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | InventorySyncTest > publishesBackorderEvent() FAILED, OrderServiceTest > calculatesDiscountForGoldCustomer() PASSED | - |
| `kubernetes-01` | `recall` | `kubernetes` | `2951.56` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `2492.61` | `0.983` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `8145.29` | `0.769` | `0.821` | `0.944` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | error[E0432] | - |
| `docker-compose-05` | `recall` | `docker-compose` | `10436.64` | `0.638` | `0.525` | `0.946` | `1.000` | `0.933` | `0.776` | `soft_accepted` | missing_exact_anchors | migration failed; exiting, docker compose up --wait api worker | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `10061.38` | `0.772` | `0.821` | `0.953` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | packages/api/src/index.ts:4:25 | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `10723.65` | `0.658` | `0.524` | `0.955` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | packages/db/src/migrate.ts:77:13, packages/db/test/migrate.test.ts:44:7 | - |
| `pnpm-04` | `recall` | `pnpm` | `2815.17` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `7759.32` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `6269.18` | `0.752` | `0.783` | `0.931` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | test/my_app/cache_worker_test.exs:29 | - |
| `rails-01` | `recall` | `rails` | `7374.88` | `0.725` | `0.706` | `0.943` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 20260518093012_add_index_to_events_request_id.rb:3 | - |
| `phpunit-01` | `recall` | `phpunit` | `3071.30` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `5873.25` | `0.553` | `0.250` | `0.953` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | nginx -t -c /etc/nginx/nginx.conf, duplicate location "/api", configuration file /etc/nginx/nginx.conf test failed | - |
| `postgres-03` | `recall` | `postgres` | `4306.23` | `0.692` | `0.611` | `0.956` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | psql:dump.sql:418, type "vector" does not exist | - |
| `ansible-02` | `recall` | `ansible` | `1834.21` | `0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `11867.57` | `0.754` | `0.792` | `0.924` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | services/reporting/parser.py", line 141 | - |
| `powershell-01` | `recall` | `powershell` | `4346.36` | `0.672` | `0.562` | `0.952` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | cannot be loaded because running scripts is disabled, FullyQualifiedErrorId : UnauthorizedAccess | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `4189.17` | `0.640` | `0.471` | `0.964` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Authentication credentials were not provided, http status: 401, exit code 1 | - |
| `python-pytest-01` | `summary` | `python-pytest` | `11470.67` | `0.972` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `2652.84` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `5337.52` | `0.971` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `1906.90` | `0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `4383.79` | `0.960` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `4938.66` | `0.704` | `0.478` | `0.896` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | checks, http_req_duration, avg | - |
| `composer-01` | `summary` | `composer` | `3633.89` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `6411.32` | `0.965` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `9540.75` | `0.739` | `1.000` | `0.925` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `3858.98` | `0.970` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `854.36` | `0.963` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `4717.63` | `0.785` | `0.833` | `0.912` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `2121.36` | `0.967` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `4519.08` | `0.972` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `2768.32` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `2089.17` | `0.619` | `1.000` | `0.731` | `0.250` | `0.250` | `1.000` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `2476.76` | `0.817` | `0.882` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | JWT expiry from 15m to 7d | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `1964.18` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | tests/test_api.py::test_create_user, tests/test_auth.py::test_refresh_token_expiry | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='tests/test_api.py::test_create_user<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- tests/test_api.py::test_create_user - tests/test_auth.py::test_refresh_token_expiry<|end_of_text|>' |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `1550.87` | `0.946` | `1.000` | `0.818` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `1209.36` | `0.958` | `1.000` | `0.860` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `7769.54` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | npm ERR! code ENOTEMPTY, npm ERR! syscall rename, /repo/node_modules/esbuild, /repo/node_modules/.esbuild.DELETE | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- npm ERR! code ENOTEMPTY - npm ERR! syscall rename - /repo/node_modules/esbuild - npm ERR! dest /repo/node_modules/.esbuild.DELETE - npm ERR! errno -39<|end...' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='npm ERR! code ENOTEMPTY - npm ERR! syscall rename - /repo/node_modules/esbuild - /repo/node_modules/.esbuild.DELETE ``` npm WARN deprecated request@2.88.2: r...' |
| `docker-build-03` | `instruction_following` | `docker-build` | `5288.88` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | [deps 4/4], pnpm install --frozen-lockfile, ERR_PNPM_LOCKFILE_CONFIG_MISMATCH, exit code: 1 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='#16 [deps 4/4] RUN pnpm install --frozen-lockfile 1.22 ERR_PNPM_LOCKFILE_CONFIG_MISMATCH ERROR: process "/bin/sh -c pnpm install --frozen-lockfile" did not c...' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='#16 [deps 4/4] RUN pnpm install --frozen-lockfile 1.22 ERR_PNPM_LOCKFILE_CONFIG_MISMATCH ERROR: process "/bin/sh -c pnpm install --frozen-lockfile" did not c...' |
| `terraform-09` | `instruction_following` | `terraform` | `1504.46` | `0.537` | `0.667` | `0.661` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors | aws_db_instance.main | - |
| `maven-03` | `instruction_following` | `maven` | `2674.78` | `0.993` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `1822.74` | `0.661` | `1.000` | `0.758` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `2204.73` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | src/App.tsx, src/api/client.ts | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='src/App.tsx src/api/client.ts<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='``` src/App.tsx: [warn] Code style issues found. src/api/client.ts: [warn] Code style issues found. ```<|end_of_text|>' |
| `kubectl-08` | `instruction_following` | `kubectl` | `1705.54` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | worker-5b8c, CrashLoopBackOff, migrator-9z1q, Error | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='worker-5b8c migrator-9z1q<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- worker-5b8c: CrashLoopBackOff - migrator-9z1q: Error<|end_of_text|>' |
| `cargo-04` | `instruction_following` | `cargo` | `7007.57` | `0.569` | `0.500` | `0.674` | `0.667` | `0.667` | `1.000` | `soft_accepted` | missing_exact_anchors | billing::tests::rounds_half_even, left: 1750, right: 1749 | - |
| `shell-01` | `instruction_following` | `shell` | `2065.92` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | rsync, /var/backups/uploads, Permission denied (13), exit code 23 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) exit code 23<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='rsync error: Permission denied (13), exit code 23<|end_of_text|>' |
| `pyright-01` | `structured` | `pyright` | `10394.64` | `0.404` | `0.867` | `0.777` | `0.000` | `0.000` | `0.696` | `soft_accepted` | missing_exact_anchors | message | - |
| `terraform-10` | `structured` | `terraform` | `6448.69` | `0.752` | `1.000` | `0.402` | `0.883` | `0.824` | `0.778` | `accepted` | - | - | - |
| `junit-01` | `structured` | `junit` | `2417.48` | `0.944` | `1.000` | `0.814` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `1496.60` | `0.436` | `1.000` | `0.454` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `6038.42` | `0.478` | `1.000` | `0.191` | `0.500` | `0.381` | `0.208` | `accepted` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `4353.90` | `0.680` | `1.000` | `0.567` | `0.714` | `0.552` | `0.241` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `7330.71` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | failed_tests, name, TestParseAmount, location, amount_test.go:22, message | granite output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='--- failed_tests: - TestParseAmount - TestFormatCurrency name: TestParseAmount: FAIL TestFormatCurrency: FAIL location: - amount_test.go:22 - currency_test.g...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml failed_tests: - TestParseAmount location: - amount_test.go:22 message: TestParseAmount: got 10.0 want 10.00 - TestFormatCurrency location: - currency...' |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `3795.50` | `0.448` | `1.000` | `0.693` | `0.000` | `0.000` | `0.400` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `1921.94` | `0.616` | `1.000` | `0.275` | `0.583` | `0.583` | `1.000` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `3295.27` | `0.958` | `1.000` | `0.908` | `1.000` | `0.957` | `0.857` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `5449.25` | `0.386` | `1.000` | `0.191` | `0.071` | `0.071` | `1.000` | `accepted` | - | - | - |
| `playwright-02` | `structured` | `playwright` | `11496.40` | `0.260` | `0.833` | `0.195` | `0.000` | `0.000` | `0.800` | `soft_accepted` | missing_exact_anchors | project | - |
| `postgres-04` | `structured` | `postgres` | `7463.22` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | errors, file, migrations/004.sql, line, message, column | granite output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml migrations: - file: migrations/004.sql line: 12 message: column "tenant_id" contains null values error: ERROR: column "tenant_id" contains null value...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml migrations: - file: migrations/004.sql line: 12 message: "ERROR: column \'tenant_id\' contains null values" error: "ERROR: column \'tenant_id\' contains ...' |
| `vite-01` | `structured` | `vite` | `4714.89` | `0.259` | `1.000` | `0.180` | `0.000` | `0.000` | `0.053` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `2418.06` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | tests/test_a.py::test_one, tests/test_b.py::TestB::test_three | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- tests/test_a.py::test_one - tests/test_b.py::TestB::test_three<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- tests/test_a.py::test_one - tests/test_b.py::TestB::test_three<|end_of_text|>' |
| `git-04` | `exact_format` | `git` | `2963.83` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='9f4c2d7a1b8e3c6d0a1234567890abcdef123456<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='9f4c2d7a1b8e3c6d0a1234567890abcdef123456<|end_of_text|>' |
| `docker-04` | `exact_format` | `docker` | `7206.59` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='- ghcr.io/acme/api:2026.05.18 - digest: sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 - verified ghcr.io/acme/api@sha256:aaaaaaaa11...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444<|end_of_text|>' |
| `npm-08` | `exact_format` | `npm` | `704.66` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 2.18.4 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='2.18.4<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='2.18.4<|end_of_text|>' |
| `go-test-05` | `exact_format` | `go-test` | `4447.42` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | github.com/acme/shop/checkout, TestCheckoutAppliesCoupon | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='--- FAIL: TestCheckoutAppliesCoupon (0.01s) checkout_test.go:77: got 120 want 100 FAIL github.com/acme/shop/checkout 0.31s<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='--- FAIL: TestCheckoutAppliesCoupon (0.01s) checkout_test.go:77: got 120 want 100 FAIL github.com/acme/shop/checkout 0.31s<|end_of_text|>' |
| `kubectl-09` | `exact_format` | `kubectl` | `1148.79` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | migrator-v2-9xk, prod | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='migrator-v2-9xk prod<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='migrator-v2-9xk namespace: prod<|end_of_text|>' |
| `cargo-05` | `exact_format` | `cargo` | `1798.09` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | auth::tests::rejects_expired, billing::tests::rounds_half_even | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- auth::tests::rejects_expired - billing::tests::rounds_half_even<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- auth::tests::rejects_expired - billing::tests::rounds_half_even<|end_of_text|>' |
| `curl-03` | `exact_format` | `curl` | `495.35` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 503 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='503<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='503<|end_of_text|>' |
| `rails-02` | `exact_format` | `rails` | `1340.22` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 20260518133742 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='20260518133742<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='20260518133742<|end_of_text|>' |
| `python-traceback-02` | `explanation` | `python-traceback` | `1259.31` | `0.965` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `7584.89` | `0.922` | `1.000` | `0.844` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `5031.97` | `0.937` | `1.000` | `0.891` | `1.000` | `0.974` | `0.915` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `1677.23` | `0.968` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `1122.06` | `0.960` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `3785.55` | `0.728` | `0.750` | `0.814` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | returns a reference | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `4333.38` | `0.932` | `1.000` | `0.864` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `4245.38` | `0.915` | `1.000` | `0.920` | `1.000` | `0.805` | `0.350` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `3015.14` | `0.983` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `3829.43` | `0.979` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `2285.32` | `0.974` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `2398.23` | `0.701` | `0.667` | `0.926` | `1.000` | `0.980` | `0.933` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `3549.78` | `0.635` | `0.545` | `0.956` | `1.000` | `0.887` | `0.625` | `soft_accepted` | missing_exact_anchors | Program.cs(15,10) | - |
| `package-management-02` | `recall` | `package-management` | `6979.14` | `0.642` | `0.667` | `0.895` | `1.000` | `0.796` | `0.319` | `soft_accepted` | missing_exact_anchors | error[E0277] | - |
| `ci-01` | `recall` | `ci` | `2200.64` | `0.714` | `0.714` | `0.874` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 5 tests run, 1 failure | - |
| `testing-03` | `recall` | `testing` | `2253.47` | `0.981` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `4630.35` | `0.978` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `3080.24` | `0.752` | `0.778` | `0.937` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "ami" is required | - |
| `compilation-02` | `recall` | `compilation` | `3909.68` | `0.985` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `1627.81` | `0.688` | `0.636` | `0.890` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Installing npm modules | - |
| `build-01` | `recall` | `build` | `2695.73` | `0.977` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `2425.85` | `0.450` | `0.000` | `0.916` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Could not locate 'config.yaml' | - |
| `compilation-03` | `recall` | `compilation` | `1310.15` | `0.979` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1287.50` | `0.967` | `1.000` | `0.867` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `937.94` | `0.978` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `1885.56` | `0.642` | `0.500` | `0.923` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | No matching distribution found | - |
| `infrastructure-03` | `recall` | `infrastructure` | `1416.24` | `0.972` | `1.000` | `0.917` | `1.000` | `0.979` | `0.929` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `4561.07` | `0.617` | `0.417` | `0.955` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | User signs in, capybara-3.34.0/lib/capybara/node/element.rb:1008 | - |
| `build-02` | `recall` | `build` | `2564.15` | `0.639` | `0.500` | `0.906` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | error: expected ';' | - |
| `ci-03` | `recall` | `ci` | `3989.41` | `0.833` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `555.42` | `0.974` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `3269.54` | `0.840` | `1.000` | `0.864` | `1.000` | `0.790` | `0.300` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `1378.41` | `0.921` | `1.000` | `0.895` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `1418.15` | `0.884` | `1.000` | `0.924` | `1.000` | `0.829` | `0.429` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `1050.92` | `0.779` | `0.810` | `0.909` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 5 passed | - |
| `npm-09` | `summary` | `npm` | `1444.27` | `0.915` | `1.000` | `0.938` | `1.000` | `0.880` | `0.600` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `1019.87` | `0.931` | `1.000` | `0.827` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `853.59` | `0.627` | `1.000` | `0.647` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `2871.46` | `0.613` | `1.000` | `0.793` | `0.400` | `0.298` | `0.154` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `6811.94` | `0.439` | `1.000` | `0.696` | `0.250` | `0.180` | `0.071` | `soft_accepted` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `2559.93` | `0.611` | `1.000` | `0.352` | `0.550` | `0.526` | `0.857` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `4180.18` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | kind, metadata, spec | granite output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml kind: Service metadata: name: my-service namespace: default spec: clusterIP: 10.0.0.1 ports: - port: 80 protocol: TCP ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='{"kind":"Service","metadata":{"name":"my-service","namespace":"default"},"spec":{"clusterIP":"10.0.0.1","ports":[{"port":80,"protocol":"TCP"}]}}' |
| `deployment-02` | `structured` | `deployment` | `1030.01` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `1694.34` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | CVE-2021-1234, Critical | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='CVE-2021-1234<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='Vulnerability found: CVE-2021-1234 - Critical<|end_of_text|>' |
| `shell-02` | `exact_format` | `shell` | `799.82` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | Timeout while waiting for response | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response<|end_of_text|>' |
| `shell-03` | `exact_format` | `shell` | `1749.62` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | OUTPUT: | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='OUTPUT: step1 step2 OUTPUT: value1 OUTPUT: value2<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='OUTPUT: step1 OUTPUT: value1 step2 OUTPUT: value2<|end_of_text|>' |
| `shell-04` | `exact_format` | `shell` | `1240.24` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | NullPointerException | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='NullPointerException: null Line 102<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='[ERROR] Build failure Line 102: NullPointerException: null<|end_of_text|>' |
| `build-04` | `exact_format` | `build` | `4524.42` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | Resources: 1 added, instance_id | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='1. Apply complete! 2. Resources: 1 added, 0 changed, 0 destroyed. 3. instance_id = "i-0abcd1234efgh" 4. instance_public_ip = "35.153.12.34"<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- Resources: 1 added - instance_id: "i-0abcd1234efgh"<|end_of_text|>' |
| `build-05` | `exact_format` | `build` | `503.04` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | BUILD SUCCESSFUL | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='BUILD SUCCESSFUL<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='BUILD SUCCESSFUL<|end_of_text|>' |
| `shell-05` | `exact_format` | `shell` | `723.54` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | PATH | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='/usr/bin:/bin<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='PATH=/usr/bin:/bin<|end_of_text|>' |
| `deployment-03` | `explanation` | `deployment` | `1119.06` | `0.933` | `1.000` | `0.893` | `1.000` | `0.960` | `0.867` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `1263.93` | `0.928` | `1.000` | `0.897` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `1734.82` | `0.967` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `1295.19` | `0.954` | `1.000` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `957.88` | `0.955` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `1247.20` | `0.931` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `2246.70` | `0.937` | `1.000` | `0.873` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `1297.08` | `0.943` | `1.000` | `0.886` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `2697.11` | `0.924` | `1.000` | `0.849` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `1189.22` | `0.949` | `1.000` | `0.919` | `1.000` | `0.967` | `0.889` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `1142.58` | `0.939` | `1.000` | `0.878` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `887.34` | `0.947` | `1.000` | `0.894` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `585.49` | `0.919` | `1.000` | `0.837` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `2707.32` | `0.909` | `1.000` | `0.843` | `1.000` | `0.962` | `0.875` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `1038.69` | `0.939` | `1.000` | `0.879` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `557.31` | `0.943` | `1.000` | `0.886` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `1463.86` | `0.948` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `1525.55` | `0.907` | `1.000` | `0.877` | `1.000` | `0.905` | `0.682` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `917.13` | `0.933` | `1.000` | `0.865` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `3902.00` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | kind, metadata, spec | granite output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml kind: Service metadata: name: my-service namespace: default spec: clusterIP: 10.0.0.1 ports: - port: 80 protocol: TCP ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='{"kind":"Service","metadata":{"name":"my-service","namespace":"default"},"spec":{"clusterIP":"10.0.0.1","ports":[{"port":80,"protocol":"TCP"}]}}' |
| `linting-03` | `structured` | `linting` | `1016.32` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `1365.06` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | CVE-2021-1234, Critical | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='CVE-2021-1234<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='Vulnerability found: CVE-2021-1234 - Critical<|end_of_text|>' |
| `shell-06` | `exact_format` | `shell` | `773.19` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | Timeout while waiting for response | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response<|end_of_text|>' |
| `shell-07` | `exact_format` | `shell` | `643.38` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | value1, value2 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='value1 value2<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='value1 value2 END<|end_of_text|>' |
| `build-06` | `exact_format` | `build` | `3696.88` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | Resources: 1 added, instance_id | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='1. Apply complete! 2. Resources: 1 added, 0 changed, 0 destroyed. 3. instance_id = "i-0abcd1234efgh" 4. instance_public_ip = "35.153.12.34"<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- Resources: 1 added - instance_id: "i-0abcd1234efgh"<|end_of_text|>' |
| `runtime-07` | `exact_format` | `runtime` | `857.11` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | Listening on port 8080 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='Listening on port 8080<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='Listening on port 8080<|end_of_text|>' |
| `build-07` | `exact_format` | `build` | `1532.67` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | testError:34 | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='testError:34<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='[ERROR] Failures: [ERROR] MyTest.testError:34 expected:<1> but was:<2><|end_of_text|>' |
| `shell-08` | `exact_format` | `shell` | `837.50` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | HOME | granite output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='/root<|end_of_text|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='/root PRESERVED TOKENS: HOME=/root<|end_of_text|>' |
| `deployment-05` | `explanation` | `deployment` | `1085.14` | `0.933` | `1.000` | `0.893` | `1.000` | `0.960` | `0.867` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `1229.53` | `0.928` | `1.000` | `0.897` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `461.51` | `0.948` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `1716.60` | `0.966` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `2239.90` | `0.937` | `1.000` | `0.873` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `1363.03` | `0.966` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `2794.24` | `0.926` | `1.000` | `0.852` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `1165.55` | `0.925` | `1.000` | `0.916` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `932.18` | `0.931` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
