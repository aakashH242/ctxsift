# gpu-qwen3.5-2b-no-quant

## Scenario

- track: `gpu`
- phase: `gpu-screen`
- model: `Qwen/Qwen3.5-2B`
- quantization: `none`
- device: `cuda`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `86420.01`
- cpu_rss_bytes: `3034210304`
- gpu_peak_bytes: `5015575552`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `241`
- accepted_count: `215`
- soft_accepted_count: `26`
- rejected_count: `39`
- exact_pass_count: `219`
- avg_inference_ms: `9748.44`
- p95_inference_ms: `28478.27`
- avg_exact_preservation_ratio: `0.834`
- avg_summary_quality_ratio: `0.764`
- avg_format_adherence_score: `0.797`
- avg_instruction_following_score: `0.788`
- avg_brevity_ratio: `0.951`
- avg_case_score: `0.779`
- p10_case_score: `0.000`
- quality_core: `0.623`
- latency_factor: `0.850`
- final_score: `52.99`
- peak_cpu_rss_bytes: `3041411072`
- peak_gpu_bytes: `5150310400`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `60865.94` | `0.689` | `1.000` | `0.900` | `0.500` | `0.404` | `0.358` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-02` | `summary` | `python` | `9227.44` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass="- ModuleNotFoundError: No module named 'dramatiq_abort'<|im_end|>" repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- python services/worker.py --queue emails --concurrency 4 - /workspace/services/worker.py - line 11 - ModuleNotFoundError - dramatiq_abort - worker boot fai...' |
| `python-03` | `recall` | `python` | `5484.11` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `7374.56` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `9107.68` | `0.672` | `0.593` | `0.896` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | python tools/export_report.py --input data/may.csv --format parquet, data/may.csv | - |
| `pytest-01` | `recall` | `pytest` | `7337.03` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `15061.90` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `9279.04` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `7641.09` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `6828.16` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `7811.52` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `11671.04` | `0.989` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `23483.65` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `17558.91` | `0.927` | `0.911` | `0.935` | `1.000` | `0.950` | `0.833` | `accepted` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `5209.64` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `5827.35` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `5952.17` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `6837.56` | `0.986` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `6571.65` | `0.985` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `6516.83` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `6426.03` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `4149.41` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `19752.53` | `0.749` | `0.762` | `0.951` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /home/dev/.npm/_logs/2026-05-15T09_20_11_449Z-debug-0.log | - |
| `npm-02` | `summary` | `npm` | `32613.32` | `0.873` | `1.000` | `0.919` | `1.000` | `0.811` | `0.368` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `6176.24` | `0.981` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `5963.27` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `9109.26` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `7982.90` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `11052.04` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `6261.81` | `0.990` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `7415.32` | `0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-01` | `recall` | `eslint` | `19065.52` | `0.804` | `0.920` | `0.926` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Unused eslint-disable directive | - |
| `eslint-02` | `summary` | `eslint` | `5372.17` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `11282.33` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `6336.17` | `0.986` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `4351.87` | `0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `8903.70` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `3280.17` | `0.991` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `5638.37` | `0.987` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `5222.61` | `0.983` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `6112.95` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `11073.70` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `5454.06` | `0.992` | `1.000` | `0.981` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `9599.63` | `0.988` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `5059.61` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `5244.08` | `0.986` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `4825.63` | `0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `6541.76` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `7162.97` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `4936.43` | `0.976` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `7274.10` | `0.972` | `1.000` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `5834.78` | `0.782` | `0.852` | `0.947` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | main -> main | - |
| `git-03` | `recall` | `git` | `5250.13` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `10867.30` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `14898.76` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | curl -I https://docs.example.com/sdk/latest, HTTP/2 301, location: /sdk/v3.4/, cache-control: max-age=3600 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- curl -I https://docs.example.com/sdk/latest - HTTP/2 301 - location: /sdk/v3.4/ - cache-control: max-age=3600<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- curl -I https://docs.example.com/sdk/latest - HTTP/2 301 - location: /sdk/v3.4/ - cache-control: max-age=3600<|im_end|>' |
| `ssh-01` | `summary` | `ssh` | `10976.89` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `5605.04` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `4370.96` | `0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `3574.72` | `0.962` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `5521.20` | `0.977` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `11391.81` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `5567.04` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `64615.12` | `0.910` | `1.000` | `0.927` | `1.000` | `0.877` | `0.590` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `6939.15` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `15552.30` | `0.979` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-02` | `summary` | `maven` | `6378.90` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `6511.36` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `6095.30` | `0.977` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `4189.00` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `4470.65` | `0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `4944.45` | `0.991` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-04` | `summary` | `npm` | `6233.22` | `0.974` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `5211.92` | `0.977` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `5809.50` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `11772.31` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `11810.77` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `4044.48` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `14028.16` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund, Dockerfile:8, zod@3.23.8, failed to solve | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='- docker build -t example/web:dev . - RUN npm ci --no-audit --no-fund - Dockerfile:8 - zod@3.23.8 - failed to solve<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='- docker build -t example/web:dev . - RUN npm ci --no-audit --no-fund - Dockerfile:8 - zod@3.23.8 - failed to solve<|im_end|>' |
| `docker-compose-04` | `summary` | `docker-compose` | `5524.21` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `4542.31` | `0.982` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `11628.26` | `0.827` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `9609.42` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `10157.53` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `4045.51` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `6669.81` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `5595.68` | `0.984` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `5117.85` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `6570.22` | `0.996` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `18123.78` | `0.971` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `5804.18` | `0.987` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `7539.96` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `7531.07` | `0.986` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `5520.22` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `29945.16` | `0.930` | `1.000` | `0.894` | `1.000` | `0.868` | `0.560` | `accepted` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `7762.14` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `3590.31` | `0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `6744.64` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `5632.14` | `0.990` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `5724.98` | `0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `6757.60` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `9802.14` | `0.993` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `102184.82` | `0.641` | `0.851` | `0.902` | `0.500` | `0.419` | `0.461` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | src/router.rs:128 | - |
| `ci-log-01` | `recall` | `ci-log` | `9318.07` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `59069.71` | `0.912` | `1.000` | `0.952` | `1.000` | `0.771` | `0.236` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `24051.42` | `0.781` | `0.750` | `0.954` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | checkout_test.go:71, total = 42.00, want 37.00 | - |
| `build-log-01` | `summary` | `build-log` | `6832.91` | `0.968` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `6482.19` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | Dockerfile:18, COPY apps/web ./apps/web, "/apps/web": not found | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='Dockerfile:18 COPY apps/web ./apps/web "/apps/web": not found<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='Dockerfile:18 COPY apps/web ./apps/web "/apps/web": not found<|im_end|>' |
| `lint-output-01` | `instruction_following` | `lint-output` | `32456.54` | `0.569` | `1.000` | `0.707` | `0.333` | `0.257` | `0.235` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `28478.27` | `0.522` | `0.905` | `0.761` | `0.375` | `0.324` | `0.548` | `soft_accepted` | missing_exact_anchors | session cookie maxAge changed from 86400 to 604800 | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `11391.85` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | search endpoint failed after 2 attempts, exit status 22, https://staging.example.com/api/search?q=smoke, curl: (22) | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='- search endpoint failed after 2 attempts - exit status 22 - https://staging.example.com/api/search?q=smoke - curl: (22)<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='- search endpoint failed after 2 attempts - exit status 22 - https://staging.example.com/api/search?q=smoke - curl: (22)<|im_end|>' |
| `structured-output-01` | `structured` | `structured-output` | `22195.27` | `0.218` | `0.500` | `0.187` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /work/app/api/routes.py, 21, reportUndefinedVariable | - |
| `structured-output-02` | `structured` | `structured-output` | `30296.91` | `0.435` | `0.905` | `0.833` | `0.000` | `0.000` | `0.806` | `soft_accepted` | missing_exact_anchors | port 5432 is already allocated | - |
| `structured-output-03` | `structured` | `structured-output` | `31454.04` | `0.826` | `0.929` | `0.954` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "refresh token expired" | - |
| `structured-output-04` | `structured` | `structured-output` | `15084.38` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `13940.22` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | tests/api/test_users.py::test_create_user_requires_email, tests/api/test_users.py::test_delete_user_requires_admin, tests/jobs/test_reconcile.py::TestReconcile::test_retries_deadlock | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- tests/api/test_users.py::test_create_user_requires_email - tests/api/test_users.py::test_delete_user_requires_admin - tests/jobs/test_reconcile.py::TestRec...' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- tests/api/test_users.py::test_create_user_requires_email - tests/api/test_users.py::test_delete_user_requires_admin - tests/jobs/test_reconcile.py::TestRec...' |
| `exact-format-02` | `exact_format` | `exact-format` | `5810.61` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | packages/web/src/search/searchBox.test.tsx, SearchBox debounces network query before fetch | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='npm run test packages/web/src/search/searchBox.test.tsx -- --testNamePattern="SearchBox › debounces network query before fetch"<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='SearchBox debounces network query before fetch<|im_end|>' |
| `exact-format-03` | `exact_format` | `exact-format` | `22388.21` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | ghcr.io/acme/worker@sha256:4f8c2e0b1d9a6c7e5f3a2b1908d4c6e7f0a123456789abcdeffedcba98765432 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='ghcr.io/acme/worker@sha256:4f8c2e0b1d9a6c7e5f3a2b1908d4c6e7f0a123456789abcdeffedcba98765432<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='ghcr.io/acme/worker@sha256:4f8c2e0b1d9a6c7e5f3a2b1908d4c6e7f0a123456789abcdeffedcba98765432<|im_end|>' |
| `diagnosis-01` | `explanation` | `diagnosis` | `5236.27` | `0.968` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `10713.43` | `0.925` | `1.000` | `0.850` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `17761.06` | `0.901` | `1.000` | `0.936` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `7548.17` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `5951.62` | `0.984` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `27423.81` | `0.982` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `12067.33` | `0.983` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `10605.11` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `27943.81` | `0.977` | `1.000` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `29178.63` | `0.976` | `1.000` | `0.935` | `1.000` | `0.978` | `0.927` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `6464.80` | `0.987` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `15456.55` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `40567.44` | `0.982` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `19243.89` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `21808.58` | `0.973` | `1.000` | `0.937` | `1.000` | `0.966` | `0.886` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `11127.21` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `10008.78` | `0.984` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `10674.20` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `7025.27` | `0.987` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `11127.35` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `29112.19` | `0.951` | `1.000` | `0.927` | `1.000` | `0.906` | `0.688` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `7545.03` | `0.973` | `1.000` | `0.894` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `6053.81` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `5921.13` | `0.982` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `8834.19` | `0.959` | `1.000` | `0.898` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `17345.88` | `0.960` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `25168.68` | `0.968` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `7355.13` | `0.970` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `11155.58` | `0.954` | `1.000` | `0.886` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `6642.04` | `0.943` | `1.000` | `0.858` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `25333.12` | `0.951` | `1.000` | `0.941` | `1.000` | `0.949` | `0.830` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `19231.76` | `0.966` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `10837.86` | `0.958` | `1.000` | `0.894` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `8669.45` | `0.791` | `0.846` | `0.924` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | auto | - |
| `jest-01` | `summary` | `jest` | `6930.78` | `0.662` | `0.222` | `0.932` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/components/Header.test.tsx, FAIL, src/components/Header.test.tsx | - |
| `dbt-01` | `summary` | `dbt` | `9065.48` | `0.791` | `0.833` | `0.932` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `9385.85` | `0.954` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `7493.30` | `0.922` | `1.000` | `0.804` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `6208.19` | `0.600` | `0.000` | `0.890` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/test_slugify.py, FAILED, tests/test_slugify.py::test_slug_is_ascii, Falsifying, example | - |
| `eslint-05` | `instruction_following` | `eslint` | `15000.67` | `0.676` | `1.000` | `0.697` | `0.500` | `0.450` | `0.667` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `5380.40` | `0.962` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `10694.17` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | tests/test_api.py::test_create_user, tests/test_auth.py::test_refresh_token_expiry | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- FAILED tests/test_api.py::test_create_user - assert 201 == 422 - FAILED tests/test_auth.py::test_refresh_token_expiry - AssertionError<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- FAILED tests/test_api.py::test_create_user - assert 201 == 422 - FAILED tests/test_auth.py::test_refresh_token_expiry - AssertionError<|im_end|>' |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `7110.39` | `0.908` | `1.000` | `0.741` | `1.000` | `0.957` | `0.857` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `4177.54` | `0.940` | `1.000` | `0.799` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `13278.20` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | npm ERR! code ENOTEMPTY, npm ERR! syscall rename, /repo/node_modules/esbuild, /repo/node_modules/.esbuild.DELETE | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- npm ERR! code ENOTEMPTY - npm ERR! syscall rename - npm ERR! path /repo/node_modules/esbuild - npm ERR! dest /repo/node_modules/.esbuild.DELETE<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- npm ERR! code ENOTEMPTY - npm ERR! syscall rename - npm ERR! path /repo/node_modules/esbuild - npm ERR! dest /repo/node_modules/.esbuild.DELETE<|im_end|>' |
| `docker-build-03` | `instruction_following` | `docker-build` | `11883.05` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | [deps 4/4], pnpm install --frozen-lockfile, ERR_PNPM_LOCKFILE_CONFIG_MISMATCH, exit code: 1 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='- [deps 4/4] RUN pnpm install --frozen-lockfile, ERR_PNPM_LOCKFILE_CONFIG_MISMATCH, exit code: 1<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='- [deps 4/4] RUN pnpm install --frozen-lockfile - ERR_PNPM_LOCKFILE_CONFIG_MISMATCH - exit code: 1<|im_end|>' |
| `terraform-09` | `instruction_following` | `terraform` | `2751.80` | `0.918` | `1.000` | `0.726` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `14712.34` | `0.731` | `1.000` | `0.905` | `0.400` | `0.400` | `1.000` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `12543.44` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | firefox, checkout.spec.ts:44:1, pays with saved card, Payment complete | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- firefox › checkout.spec.ts:44:1 › pays with saved card Error: expect(locator).toBeVisible() failed Locator: text=Payment complete' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- firefox › checkout.spec.ts:44:1 › pays with saved card Error: expect(locator).toBeVisible() failed Locator: text=Payment complete' |
| `prettier-01` | `instruction_following` | `prettier` | `3990.81` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | src/App.tsx, src/api/client.ts | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- src/App.tsx - src/api/client.ts<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- src/App.tsx - src/api/client.ts<|im_end|>' |
| `kubectl-08` | `instruction_following` | `kubectl` | `8546.12` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | worker-5b8c, CrashLoopBackOff, migrator-9z1q, Error | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- worker-5b8c - CrashLoopBackOff - migrator-9z1q - Error<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- worker-5b8c - CrashLoopBackOff - migrator-9z1q - Error<|im_end|>' |
| `cargo-04` | `instruction_following` | `cargo` | `13186.01` | `0.657` | `1.000` | `0.804` | `0.333` | `0.316` | `0.824` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `4640.95` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | rsync, /var/backups/uploads, Permission denied (13), exit code 23 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='- Permission denied (13)<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='- rsync - /var/backups/uploads - exit code 23<|im_end|>' |
| `pyright-01` | `structured` | `pyright` | `27765.49` | `0.312` | `1.000` | `0.188` | `0.000` | `0.000` | `0.552` | `accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `15342.14` | `0.873` | `1.000` | `0.701` | `0.961` | `0.897` | `0.778` | `accepted` | - | - | - |
| `junit-01` | `structured` | `junit` | `10349.71` | `0.944` | `1.000` | `0.813` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `21713.31` | `0.288` | `1.000` | `0.191` | `0.000` | `0.000` | `0.308` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `22903.77` | `0.479` | `1.000` | `0.191` | `0.500` | `0.383` | `0.217` | `accepted` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `9269.54` | `0.784` | `1.000` | `0.704` | `0.714` | `0.688` | `0.875` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `17855.24` | `0.357` | `1.000` | `0.191` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `11588.83` | `0.820` | `1.000` | `0.632` | `1.000` | `0.790` | `0.300` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `11727.98` | `0.202` | `0.667` | `0.181` | `0.000` | `0.000` | `0.500` | `soft_accepted` | missing_exact_anchors | package, required | - |
| `mypy-06` | `structured` | `mypy` | `13604.09` | `0.944` | `1.000` | `0.906` | `1.000` | `0.916` | `0.720` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `15632.85` | `0.391` | `1.000` | `0.191` | `0.083` | `0.083` | `1.000` | `accepted` | - | - | - |
| `playwright-02` | `structured` | `playwright` | `20663.23` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | project, chromium, file, checkout.spec.ts, line, test | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "test": "submits card", "project": "chromium", "file": "checkout.spec.ts", "line": 42, "error": "expect(page).toHaveURL(/success/) failed", "status...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "test": "submits card", "project": "chromium", "file": "checkout.spec.ts", "line": 42, "error": "expect(page).toHaveURL(/success/) failed", "status...' |
| `postgres-04` | `structured` | `postgres` | `15228.52` | `0.477` | `1.000` | `0.740` | `0.000` | `0.000` | `0.556` | `accepted` | - | - | - |
| `vite-01` | `structured` | `vite` | `10324.50` | `0.126` | `0.400` | `0.181` | `0.000` | `0.000` | `0.143` | `soft_accepted` | missing_exact_anchors | /repo/apps/admin/src/client.ts, @acme/api, /repo/apps/public/src/Home.tsx | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `6343.85` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | tests/test_a.py::test_one, tests/test_b.py::TestB::test_three | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- tests/test_a.py::test_one - tests/test_b.py::TestB::test_three<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- tests/test_a.py::test_one - tests/test_b.py::TestB::test_three<|im_end|>' |
| `git-04` | `exact_format` | `git` | `14054.20` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='9f4c2d7a1b8e3c6d0a1234567890abcdef123456<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass="Merge made by the 'ort' strategy. commit 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 Author: CI Bot Status: deployed to staging<|im_end|>" |
| `docker-04` | `exact_format` | `docker` | `35070.96` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='pushed ghcr.io/acme/api:2026.05.18 digest: sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 verified ghcr.io/acme/api@sha256:aaaaaaaa1...' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='pushed ghcr.io/acme/api:2026.05.18 digest: sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 verified ghcr.io/acme/api@sha256:aaaaaaaa1...' |
| `npm-08` | `exact_format` | `npm` | `2541.07` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 2.18.4 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='2.18.4<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='2.18.4<|im_end|>' |
| `go-test-05` | `exact_format` | `go-test` | `16793.83` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | github.com/acme/shop/checkout, TestCheckoutAppliesCoupon | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='--- FAIL: TestCheckoutAppliesCoupon (0.01s) checkout_test.go:77: got 120 want 100 FAIL github.com/acme/shop/checkout 0.31s<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='--- FAIL: TestCheckoutAppliesCoupon (0.01s) checkout_test.go:77: got 120 want 100 FAIL github.com/acme/shop/checkout 0.31s<|im_end|>' |
| `kubectl-09` | `exact_format` | `kubectl` | `4254.43` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | migrator-v2-9xk, prod | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='migrator-v2-9xk 0/1 Error 0 33m<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='prod<|im_end|>' |
| `cargo-05` | `exact_format` | `cargo` | `8834.94` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | auth::tests::rejects_expired, billing::tests::rounds_half_even | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- auth::tests::rejects_expired - billing::tests::rounds_half_even test result: FAILED. 40 passed; 2 failed<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- auth::tests::rejects_expired - billing::tests::rounds_half_even<|im_end|>' |
| `curl-03` | `exact_format` | `curl` | `1621.30` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 503 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='503<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='503<|im_end|>' |
| `rails-02` | `exact_format` | `rails` | `12240.47` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 20260518133742 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='20260518133742<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='20260518133742 AddTenantIdToUsers: migrating ===================== -- add_column(:users, :tenant_id, :uuid) rails aborted! PG::DuplicateColumn: ERROR: column...' |
| `python-traceback-02` | `explanation` | `python-traceback` | `2405.44` | `0.933` | `1.000` | `0.865` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `12398.19` | `0.945` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `2424.19` | `0.877` | `1.000` | `0.887` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `3071.96` | `0.934` | `1.000` | `0.868` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `3921.96` | `0.954` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `2502.47` | `0.896` | `1.000` | `0.792` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `13366.60` | `0.715` | `0.583` | `0.848` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `3455.73` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `4041.21` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `11096.30` | `0.755` | `1.000` | `0.954` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `package-management-01` | `recall` | `package-management` | `8197.90` | `0.437` | `0.000` | `0.933` | `1.000` | `0.944` | `0.812` | `soft_accepted` | missing_exact_anchors | npm ERR! code E404, 404 Not Found, GET https://registry.npmjs.org/foo | - |
| `runtime-02` | `recall` | `runtime` | `10700.24` | `0.714` | `0.667` | `0.959` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `5042.48` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `4458.47` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `2881.16` | `0.962` | `1.000` | `0.847` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `3629.31` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `8395.67` | `0.965` | `1.000` | `0.887` | `1.000` | `0.981` | `0.938` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `7656.07` | `0.750` | `0.778` | `0.927` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "ami" is required | - |
| `compilation-02` | `recall` | `compilation` | `3673.53` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `1729.29` | `0.974` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `8388.82` | `0.943` | `1.000` | `0.895` | `1.000` | `0.909` | `0.696` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `2587.87` | `0.976` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `5492.15` | `0.972` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `2015.04` | `0.967` | `1.000` | `0.867` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `1566.84` | `0.991` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `3737.76` | `0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `2144.62` | `0.966` | `1.000` | `0.865` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `5902.42` | `0.979` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `3907.46` | `0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `16816.73` | `0.833` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `2014.09` | `0.976` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `2161.90` | `0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `3767.67` | `0.903` | `1.000` | `0.850` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `1428.57` | `0.961` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `1752.25` | `0.953` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `2024.64` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `727.86` | `0.936` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `4186.71` | `0.767` | `0.636` | `0.917` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | index.js | - |
| `testing-06` | `instruction_following` | `testing` | `4013.86` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `4911.74` | `0.529` | `1.000` | `0.629` | `0.500` | `0.400` | `0.333` | `soft_accepted` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `8190.54` | `0.703` | `1.000` | `0.510` | `0.625` | `0.625` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `8063.26` | `0.599` | `1.000` | `0.996` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `4945.25` | `0.925` | `1.000` | `0.817` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `4786.55` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | CVE-2021-1234, Critical | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='CVE-2021-1234 - Critical<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='CVE-2021-1234 - Critical<|im_end|>' |
| `shell-02` | `exact_format` | `shell` | `4911.20` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | Timeout while waiting for response | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response INFO: Retrying... ERROR: Timeout while waiting for response<|im_end|>' |
| `shell-03` | `exact_format` | `shell` | `3723.82` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | OUTPUT: | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_lines_contract_breakage'] first_pass='- OUTPUT: value1 - OUTPUT: value2<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- OUTPUT: value1 - OUTPUT: value2<|im_end|>' |
| `shell-04` | `exact_format` | `shell` | `829.04` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | NullPointerException | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='NullPointerException<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='NullPointerException<|im_end|>' |
| `build-04` | `exact_format` | `build` | `12171.51` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | Resources: 1 added, instance_id | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='Resources: 1 added instance_id = "i-0abcd1234efgh" instance_public_ip = "35.153.12.34"<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='Resources: 1 added instance_id = "i-0abcd1234efgh" instance_public_ip = "35.153.12.34"<|im_end|>' |
| `build-05` | `exact_format` | `build` | `3754.82` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | BUILD SUCCESSFUL | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='BUILD SUCCESSFUL<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='BUILD SUCCESSFUL in 10s 2 actionable tasks: 2 up-to-date<|im_end|>' |
| `shell-05` | `exact_format` | `shell` | `3874.94` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | PATH | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='PATH=/usr/bin:/bin HOME=/home/user<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='PATH=/usr/bin:/bin HOME=/home/user<|im_end|>' |
| `deployment-03` | `explanation` | `deployment` | `1730.05` | `0.936` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `1419.87` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `2027.65` | `0.929` | `1.000` | `0.859` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `1297.71` | `0.950` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `8136.82` | `0.903` | `1.000` | `0.877` | `1.000` | `0.894` | `0.647` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `1145.60` | `0.931` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `868.87` | `0.910` | `1.000` | `0.821` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `1335.03` | `0.931` | `1.000` | `0.861` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1494.81` | `0.944` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `1462.13` | `0.950` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `990.45` | `0.864` | `1.000` | `0.727` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `1291.42` | `0.939` | `1.000` | `0.878` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `701.61` | `0.923` | `1.000` | `0.847` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `1436.05` | `0.922` | `1.000` | `0.845` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `992.02` | `0.920` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `2147.56` | `0.932` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `1279.09` | `0.948` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `2283.67` | `0.932` | `1.000` | `0.864` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `986.51` | `0.875` | `1.000` | `0.751` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `8081.26` | `0.599` | `1.000` | `0.996` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `4777.86` | `0.925` | `1.000` | `0.817` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `4335.65` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | CVE-2021-1234, Critical | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='CVE-2021-1234 - Critical<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='CVE-2021-1234 - Critical<|im_end|>' |
| `shell-06` | `exact_format` | `shell` | `3442.83` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_format_contract_breakage | Timeout while waiting for response | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage', 'exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response INFO: Retrying...<|im_end|>' |
| `shell-07` | `exact_format` | `shell` | `2276.19` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage, exact_lines_contract_breakage | value1, value2 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='value1 value2<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage', 'exact_lines_contract_breakage'] repair_pass='- value1 - value2<|im_end|>' |
| `build-06` | `exact_format` | `build` | `12401.24` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | Resources: 1 added, instance_id | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='Resources: 1 added instance_id = "i-0abcd1234efgh" instance_public_ip = "35.153.12.34"<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='Resources: 1 added instance_id = "i-0abcd1234efgh" instance_public_ip = "35.153.12.34"<|im_end|>' |
| `runtime-07` | `exact_format` | `runtime` | `3352.46` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | Listening on port 8080 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='Listening on port 8080<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='Listening on port 8080<|im_end|>' |
| `build-07` | `exact_format` | `build` | `9411.43` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | testError:34 | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='[ERROR] Failures: [ERROR] MyTest.testError:34 expected:<1> but was:<2><|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='[ERROR] Failures: [ERROR] MyTest.testError:34 expected:<1> but was:<2><|im_end|>' |
| `shell-08` | `exact_format` | `shell` | `1730.18` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | HOME | qwen3.5 output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='HOME<|im_end|>' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='USER=root HOME=/root<|im_end|>' |
| `deployment-05` | `explanation` | `deployment` | `1800.87` | `0.936` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `1514.34` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `1618.00` | `0.959` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `1538.37` | `0.919` | `1.000` | `0.838` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `998.51` | `0.910` | `1.000` | `0.821` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `1446.96` | `0.960` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `971.82` | `0.913` | `1.000` | `0.825` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `1729.05` | `0.961` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `3266.17` | `0.939` | `1.000` | `0.878` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
