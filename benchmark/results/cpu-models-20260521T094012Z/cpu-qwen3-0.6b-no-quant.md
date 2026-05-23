# cpu-qwen3-0.6b-no-quant

## Scenario

- track: `cpu`
- phase: `cpu-screen`
- model: `unsloth/Qwen3-0.6B-GGUF`
- quantization: `none`
- device: `cpu`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `27546.28`
- cpu_rss_bytes: `null`
- gpu_peak_bytes: `null`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `243`
- accepted_count: `203`
- soft_accepted_count: `40`
- rejected_count: `37`
- exact_pass_count: `210`
- avg_inference_ms: `15931.51`
- p95_inference_ms: `34562.81`
- avg_exact_preservation_ratio: `0.825`
- avg_summary_quality_ratio: `0.763`
- avg_format_adherence_score: `0.760`
- avg_instruction_following_score: `0.742`
- avg_brevity_ratio: `0.897`
- avg_case_score: `0.748`
- p10_case_score: `0.000`
- quality_core: `0.598`
- latency_factor: `0.850`
- final_score: `50.86`
- peak_cpu_rss_bytes: `null`
- peak_gpu_bytes: `null`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `30577.73` | `0.689` | `1.000` | `0.899` | `0.500` | `0.404` | `0.358` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-02` | `summary` | `python` | `21219.89` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='$ python services/worker.py --queue emails --concurrency 4 - /workspace/services/worker.py - line 11 - ModuleNotFoundError - dramatiq_abort - worker boot failed' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='python services/worker.py --queue emails --concurrency 4 - /workspace/services/worker.py - line 11 - ModuleNotFoundError - dramatiq_abort - worker boot failed' |
| `python-03` | `recall` | `python` | `28266.15` | `0.989` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `55439.21` | `0.565` | `0.417` | `0.904` | `1.000` | `0.854` | `0.512` | `soft_accepted` | missing_exact_anchors | /workspace/src/jobs/refresh_catalog.py, line 119, httpx.ReadTimeout | - |
| `python-05` | `recall` | `python` | `22470.45` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `11257.51` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `11069.40` | `0.985` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `12605.52` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `9862.70` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `33096.70` | `0.671` | `1.000` | `0.928` | `0.500` | `0.418` | `0.455` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `mypy-01` | `recall` | `mypy` | `6863.47` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `8839.86` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `20813.19` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `31845.22` | `0.908` | `0.911` | `0.932` | `1.000` | `0.914` | `0.714` | `accepted` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `15027.39` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `7127.35` | `0.971` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `9616.30` | `0.987` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `19763.45` | `0.979` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `8648.00` | `0.966` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `19865.58` | `0.794` | `0.800` | `0.961` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 2 files would be reformatted, 41 files would be left unchanged | - |
| `black-02` | `summary` | `black` | `19448.07` | `0.971` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `6383.88` | `0.992` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `9956.17` | `0.947` | `1.000` | `0.919` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `15030.10` | `0.874` | `1.000` | `0.918` | `1.000` | `0.814` | `0.380` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `8368.96` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `9864.35` | `0.941` | `1.000` | `0.922` | `1.000` | `0.883` | `0.609` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `11384.39` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `17681.62` | `0.874` | `1.000` | `0.891` | `1.000` | `0.835` | `0.449` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `9588.21` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `13048.58` | `0.995` | `1.000` | `0.981` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `37088.67` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | tsc src/index.ts src/http.ts --pretty false, src/index.ts(48,20), TS2769, URL, RequestInit, src/http.ts(9,17) | fallback output validation failed: model did not stop thinking before reaching the output limit. first_pass="<think> Okay, let's see. The user provided a command to compile TypeScript files, and there's an error in the output. The error message says that the overloa..." repair_pass="<think> Okay, let's see. The user provided a TypeScript error message and wants me to fix the recall-oriented compression. The previous answer was invalid be..." |
| `eslint-01` | `recall` | `eslint` | `23121.70` | `0.963` | `1.000` | `0.937` | `1.000` | `0.936` | `0.788` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `8139.69` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `20623.62` | `0.982` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `56132.80` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | docker build -t api:dev ., COPY docker/entrypoint.sh /entrypoint.sh, /docker/entrypoint.sh, Dockerfile:14, failed to solve | fallback output validation failed: model did not stop thinking before reaching the output limit. first_pass="<think> Okay, let's see. The user wants me to compress the Docker build command for later recall. They provided the exact command, but there's a problem with..." repair_pass="<think> Okay, let's see. The user provided a Dockerfile and mentioned that the previous answer was invalid for recall-oriented compression. The previous answ..." |
| `docker-02` | `summary` | `docker` | `7786.45` | `0.984` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `25764.62` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `7847.89` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `19648.09` | `0.900` | `1.000` | `0.915` | `1.000` | `0.765` | `0.216` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `10514.24` | `0.968` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `10709.67` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `31987.09` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `7071.85` | `0.987` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `44322.92` | `0.691` | `1.000` | `0.926` | `0.500` | `0.396` | `0.310` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `terraform-01` | `summary` | `terraform` | `10710.20` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `11696.70` | `0.989` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `8010.06` | `0.990` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `20462.53` | `0.816` | `0.902` | `0.960` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | expected t3.small default | - |
| `mixed-01` | `recall` | `mixed` | `7767.17` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `9675.20` | `0.963` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `8584.70` | `0.976` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `24208.74` | `0.924` | `1.000` | `0.860` | `1.000` | `0.876` | `0.587` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `14796.54` | `0.947` | `1.000` | `0.950` | `1.000` | `0.879` | `0.596` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `12455.43` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `17081.83` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo, exact_lines_contract_breakage | curl -I https://docs.example.com/sdk/latest, HTTP/2 301, location: /sdk/v3.4/, cache-control: max-age=3600 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo', 'exact_lines_contract_breakage'] first_pass='- return the exact requested lines or quoted excerpts only - copy quoted or extracted lines exactly from the raw output - do not summarize unless the instruc...' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- curl -I https://docs.example.com/sdk/latest - HTTP/2 301 - location: /sdk/v3.4/ - cache-control: max-age=3600' |
| `ssh-01` | `summary` | `ssh` | `7739.81` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `9037.78` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `15144.69` | `0.913` | `1.000` | `0.911` | `1.000` | `0.897` | `0.655` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `33549.61` | `0.786` | `0.857` | `0.901` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | api.service | - |
| `apt-01` | `summary` | `apt` | `20710.82` | `0.977` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `25752.36` | `0.904` | `1.000` | `0.939` | `1.000` | `0.759` | `0.198` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `18191.75` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `37007.61` | `0.618` | `0.133` | `0.859` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | go test ./... -run TestCacheTTL -count=1, cache_test.go:47, invalid memory address or nil pointer dereference | - |
| `javac-01` | `summary` | `javac` | `10504.63` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `24479.65` | `0.672` | `0.304` | `0.912` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mvn -q test, UserControllerTest.java:72, maven-surefire-plugin:3.5.5:test | - |
| `maven-02` | `summary` | `maven` | `23050.20` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `16801.13` | `0.909` | `1.000` | `0.931` | `1.000` | `0.780` | `0.265` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `12319.81` | `0.977` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `19861.28` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `34370.03` | `0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `42643.94` | `0.619` | `0.789` | `0.914` | `0.500` | `0.416` | `0.442` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | MODULE_NOT_FOUND | - |
| `npm-04` | `summary` | `npm` | `38080.25` | `0.857` | `1.000` | `0.918` | `1.000` | `0.779` | `0.264` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `11256.84` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `25591.68` | `0.760` | `0.727` | `0.905` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ESLint found too many warnings | - |
| `python-runtime-01` | `summary` | `python-runtime` | `37109.58` | `0.704` | `1.000` | `0.947` | `0.500` | `0.450` | `0.667` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `pytest-06` | `summary` | `pytest` | `24552.70` | `0.889` | `1.000` | `0.913` | `1.000` | `0.847` | `0.491` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `16708.62` | `0.882` | `1.000` | `0.919` | `1.000` | `0.828` | `0.427` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `43377.42` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund, Dockerfile:8, zod@3.23.8, failed to solve | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='$ docker build -t example/web:dev . [+] Building 38.7s (10/14) => [internal] load build definition from Dockerfile 0.0s => => transferring dockerfile: 1.07kB...' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='docker build -t example/web:dev . [+] Building 38.7s (10/14) => [internal] load build definition from Dockerfile 0.0s => [1/8] FROM docker.io/library/node:20...' |
| `docker-compose-04` | `summary` | `docker-compose` | `14568.34` | `0.879` | `1.000` | `0.907` | `1.000` | `0.833` | `0.443` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `10518.46` | `0.975` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `20586.69` | `0.823` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `21914.70` | `0.870` | `1.000` | `0.856` | `1.000` | `0.719` | `0.063` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `31008.46` | `0.991` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `8582.86` | `0.962` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `23390.08` | `0.981` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `8632.25` | `0.979` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `9994.63` | `0.974` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `8790.10` | `0.992` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `12468.05` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `9674.24` | `0.983` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `10982.31` | `0.986` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `12060.01` | `0.949` | `1.000` | `0.948` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `7828.32` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `19641.18` | `0.928` | `1.000` | `0.890` | `1.000` | `0.868` | `0.560` | `accepted` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `19155.86` | `0.898` | `1.000` | `0.907` | `1.000` | `0.871` | `0.571` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `10706.85` | `0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `15641.12` | `0.923` | `1.000` | `0.925` | `1.000` | `0.906` | `0.686` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `8737.50` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `8907.85` | `0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `25760.98` | `0.784` | `0.833` | `0.909` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | runtime-1a2b3c.js | - |
| `test-failure-01` | `recall` | `test-failure` | `28441.89` | `0.971` | `1.000` | `0.950` | `1.000` | `0.950` | `0.833` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `34567.20` | `0.979` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-log-01` | `recall` | `ci-log` | `11300.32` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `17314.73` | `0.950` | `1.000` | `0.958` | `1.000` | `0.882` | `0.607` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `34523.35` | `0.794` | `0.821` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | worker.go:144 | - |
| `build-log-01` | `summary` | `build-log` | `27840.38` | `0.970` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `36276.21` | `0.568` | `0.667` | `0.878` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Dockerfile:18 | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `28013.66` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | /repo/web/src/App.tsx, 27:19, @typescript-eslint/no-misused-promises, /repo/web/src/api/client.ts, 8:10, @typescript-eslint/no-explicit-any, 33:11, @typescript-eslint/no-unsafe-assignment | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- /repo/web/src/App.tsx 12:7 error Promise returned in function argument where a void return was expected - /repo/web/src/api/client.ts 8:10 error Unexpected...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- /repo/web/src/App.tsx 27:19 @typescript-eslint/no-misused-promises - /repo/web/src/api/client.ts 8:10 @typescript-eslint/no-explicit-any - 33:11 @typescrip...' |
| `git-review-01` | `instruction_following` | `git-review` | `21555.69` | `0.589` | `1.000` | `0.760` | `0.250` | `0.221` | `0.607` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `38926.92` | `0.523` | `1.000` | `0.745` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-01` | `structured` | `structured-output` | `15056.70` | `0.529` | `1.000` | `0.861` | `0.000` | `0.000` | `0.707` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `29546.31` | `0.314` | `0.905` | `0.490` | `0.000` | `0.000` | `0.410` | `soft_accepted` | missing_exact_anchors | port 5432 is already allocated | - |
| `structured-output-03` | `structured` | `structured-output` | `21014.25` | `0.763` | `0.643` | `0.898` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Expected: 19, Received: 0 | - |
| `structured-output-04` | `structured` | `structured-output` | `33970.63` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | /repo/apps/web/src/main.tsx, @sentry/browser, /repo/packages/time/src/format.ts, date-fns-tz, /repo/packages/time/src/parse.ts, /repo/apps/web/src/features/flags.ts, @acme/flags | fallback output validation failed: model did not stop thinking before reaching the output limit. first_pass='```json { "@sentry/browser": ["@sentry/browser"], "/repo/apps/web/src/main.tsx": ["@sentry/browser"], "/repo/packages/time/src/format.ts": ["date-fns-tz"], "...' repair_pass="<think> Okay, let's see. The user mentioned that their previous answer was invalid for recall-oriented compression. They provided a JSON structure that inclu..." |
| `exact-format-01` | `exact_format` | `exact-format` | `24744.24` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | tests/api/test_users.py::test_create_user_requires_email, tests/api/test_users.py::test_delete_user_requires_admin, tests/jobs/test_reconcile.py::TestReconcile::test_retries_deadlock | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='FAILED tests/api/test_users.py::test_create_user_requires_email - AssertionError: 201 != 422 - FAILED tests/api/test_users.py::test_delete_user_requires_admi...' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- FAILED tests/api/test_users.py::test_create_user_requires_email - AssertionError: 201 != 422 - FAILED tests/api/test_users.py::test_delete_user_requires_ad...' |
| `exact-format-02` | `exact_format` | `exact-format` | `27773.77` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | packages/web/src/search/searchBox.test.tsx, SearchBox debounces network query before fetch | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='packages/web/src/search/searchBox.test.tsx SearchBox ✓ opens suggestions on focus (31 ms) ✕ debounces network query before fetch (1015 ms) ✓ clears query on ...' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='packages/web/src/search/searchBox.test.tsx - SearchBox debounces network query before fetch' |
| `exact-format-03` | `exact_format` | `exact-format` | `20242.59` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `17698.93` | `0.685` | `0.778` | `0.900` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `18382.02` | `0.767` | `0.750` | `0.906` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `25225.63` | `0.699` | `0.750` | `0.904` | `0.667` | `0.640` | `0.868` | `soft_accepted` | missing_exact_anchors | 00000000-0000-0000-0000-000000000000 | - |
| `python-traceback-01` | `recall` | `python-traceback` | `24991.74` | `0.654` | `0.524` | `0.935` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /srv/app/app/tasks/email.py, line 92 | - |
| `mypy-05` | `recall` | `mypy` | `10672.25` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `25494.78` | `0.978` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `27990.68` | `0.983` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `12608.68` | `0.982` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `12402.44` | `0.978` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `23850.10` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `16800.59` | `0.718` | `0.700` | `0.917` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker compose up --wait api worker | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `10673.70` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `8892.30` | `0.984` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `31033.56` | `0.804` | `0.895` | `0.975` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --frozen-lockfile | - |
| `swift-01` | `recall` | `swift` | `21775.40` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `22866.34` | `0.749` | `0.783` | `0.914` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | test/my_app/cache_worker_test.exs:29 | - |
| `rails-01` | `recall` | `rails` | `22860.38` | `0.749` | `0.765` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ArgumentError | - |
| `phpunit-01` | `recall` | `phpunit` | `14091.83` | `0.957` | `1.000` | `0.927` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `15655.10` | `0.979` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `9572.75` | `0.982` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `10035.38` | `0.951` | `1.000` | `0.929` | `1.000` | `0.906` | `0.688` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `14743.66` | `0.983` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `14308.14` | `0.984` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `10120.43` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `10261.14` | `0.963` | `1.000` | `0.907` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `6300.40` | `0.960` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `10338.88` | `0.970` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `15061.18` | `0.932` | `0.875` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | template | - |
| `ruff-04` | `summary` | `ruff` | `12722.70` | `0.960` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `26535.66` | `0.943` | `1.000` | `0.858` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `10390.93` | `0.951` | `1.000` | `0.941` | `1.000` | `0.949` | `0.830` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `14327.48` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | xcodebuild, -scheme, MobileApp, -configuration, Release | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them **Summary:** The command...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them **Summary:** The command...' |
| `make-02` | `summary` | `make` | `18589.35` | `0.742` | `1.000` | `0.933` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `24471.39` | `0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `13713.08` | `0.956` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `16488.41` | `0.962` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `20900.36` | `0.970` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `38319.08` | `0.917` | `1.000` | `0.793` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `10310.34` | `0.964` | `1.000` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `22878.98` | `0.728` | `1.000` | `0.982` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `10265.25` | `0.961` | `1.000` | `0.871` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `16141.88` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | tests/test_api.py::test_create_user, tests/test_auth.py::test_refresh_token_expiry | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- FAILED tests/test_api.py::test_create_user - assert 201 == 422 - FAILED tests/test_auth.py::test_refresh_token_expiry - AssertionError' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- FAILED tests/test_api.py::test_create_user - assert 201 == 422 - FAILED tests/test_auth.py::test_refresh_token_expiry - AssertionError' |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `12262.07` | `0.656` | `1.000` | `0.705` | `0.500` | `0.417` | `0.444` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `33475.51` | `0.686` | `0.577` | `0.638` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | secret "api-env" not found, Back-off restarting failed container api | - |
| `npm-06` | `instruction_following` | `npm` | `19918.48` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | npm ERR! code ENOTEMPTY, npm ERR! syscall rename, /repo/node_modules/esbuild, /repo/node_modules/.esbuild.DELETE | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='npm ERR! code ENOTEMPTY - npm ERR! syscall rename' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='npm ERR! code ENOTEMPTY - npm ERR! syscall rename - /repo/node_modules/esbuild - /repo/node_modules/.esbuild.DELETE' |
| `docker-build-03` | `instruction_following` | `docker-build` | `16709.17` | `0.429` | `1.000` | `0.708` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `22633.33` | `0.475` | `0.333` | `0.641` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors | aws_db_instance.main, destroyed | - |
| `maven-03` | `instruction_following` | `maven` | `14626.57` | `0.839` | `1.000` | `0.924` | `0.667` | `0.658` | `0.955` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `16129.24` | `0.714` | `1.000` | `0.713` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `18339.56` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | src/App.tsx, src/api/client.ts | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- src/App.tsx - src/api/client.ts' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- src/App.tsx - src/api/client.ts' |
| `kubectl-08` | `instruction_following` | `kubectl` | `17739.57` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | worker-5b8c, CrashLoopBackOff, migrator-9z1q, Error | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- worker-5b8c 0/1 CrashLoopBackOff 6 9m - migrator-9z1q 0/1 Error 0 4m' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- worker-5b8c 0/1 CrashLoopBackOff 6 9m - migrator-9z1q 0/1 Error 0 4m' |
| `cargo-04` | `instruction_following` | `cargo` | `24722.24` | `0.659` | `0.333` | `0.695` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/auth.rs:88, Option::unwrap(), left: 1750, right: 1749 | - |
| `shell-01` | `instruction_following` | `shell` | `28116.13` | `0.310` | `0.500` | `0.681` | `0.000` | `0.000` | `0.600` | `soft_accepted` | missing_exact_anchors | /var/backups/uploads, exit code 23 | - |
| `pyright-01` | `structured` | `pyright` | `21543.13` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | file, /repo/app/user.py, line, code, reportOptionalMemberAccess, message | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- repo/app/user.py:31:12 - error: "email" is not a known attribute of "None" (reportOptionalMemberAccess) - repo/app/user.py:45:5 - warning: Type is partiall...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- repo/app/user.py:31:12 - error: "email" is not a known attribute of "None" (reportOptionalMemberAccess) - repo/app/user.py:45:5 - warning: Type is partiall...' |
| `terraform-10` | `structured` | `terraform` | `25608.94` | `0.203` | `0.667` | `0.186` | `0.000` | `0.000` | `0.500` | `soft_accepted` | missing_exact_anchors | resource, field | - |
| `junit-01` | `structured` | `junit` | `32030.79` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | Test, Error, Location, ---, CalculatorTest, dividesByZero | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- Test - Error - CalculatorTest > dividesByZero FAILED java.lang.ArithmeticException: / by zero at Calculator.java:42 UserServiceTest > rejectsDuplicateEmail...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- Test - Error - Location - CalculatorTest > dividesByZero FAILED java.lang.ArithmeticException: / by zero at Calculator.java:42 UserServiceTest > rejectsDup...' |
| `kubernetes-03` | `structured` | `kubernetes` | `43924.30` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | unhealthy_pods, name, api-77df, status, CrashLoopBackOff, restarts | fallback output validation failed: model did not stop thinking before reaching the output limit. first_pass='- NAME READY STATUS RESTARTS AGE api-77df 0/1 CrashLoopBackOff 5 12m worker-884b 1/1 Running 0 12m search-0 0/1 ImagePullBackOff 0 4m redis-0 1/1 Running 0 2h' repair_pass="<think> Okay, let's see. The user mentioned that the previous answer was invalid for recall-oriented compression. They provided the previous answer and want ..." |
| `eslint-06` | `structured` | `eslint` | `20168.36` | `0.485` | `1.000` | `0.190` | `0.500` | `0.392` | `0.278` | `accepted` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `25502.47` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | stage, builder, command, pnpm, build, error | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- stage: builder - builder: 5/6 - command: pnpm build - pnpm: - build: 2.4 Error: Cannot find module \'@acme/config\' - error: process "/bin/sh -c pnpm build" ...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "stage": "builder", "builder": "5/6", "command": "pnpm build", "pnpm": "pnpm", "build": "2.4 Error: Cannot find module \'@acme/config\'", "error": "p...' |
| `go-test-04` | `structured` | `go-test` | `30176.09` | `0.351` | `1.000` | `0.196` | `0.000` | `0.000` | `0.917` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `43271.36` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | Job, Step, Exit, ---, test, Run | fallback output validation failed: model did not stop thinking before reaching the output limit. first_pass='- job lint success 22s - job test failed step="Run unit tests" exit=1 - job build success 49s - job deploy failed step="Upload artifact" exit=1' repair_pass="<think> Okay, let's see. The user mentioned that the previous answer was invalid for recall-oriented compression. They provided the previous answer and want ..." |
| `npm-07` | `structured` | `npm` | `45889.38` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | package, legacy-widget@2.4.0, peer, react, required, 18.0.0 | fallback output validation failed: model did not stop thinking before reaching the output limit. first_pass='- package: legacy-widget@2.4.0 - peer: react@"^18.0.0" - react: 18.0.0 - required: 18.0.0' repair_pass="<think> Okay, let's see. The user provided an invalid compression summary and wants me to fix it. The previous answer had some package, peer, required, and v..." |
| `mypy-06` | `structured` | `mypy` | `47862.04` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | File, Line, Code, Message, ---, app/api.py | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='app/api.py:10: error: Module has no attribute "Router" app/auth.py:44: error: Incompatible return value type (got "None", expected "User") --- ```python | Us...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```markdown | File | Line | Code | Message | |------------|--------|--------------|----------| | app/api.py | 10 | `| User ID | Email | Password | Role |` | ...' |
| `gradle-03` | `structured` | `gradle` | `71637.85` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | failed, task, :api:compileJava, cause, cannot, find | fallback output validation failed: model did not stop thinking before reaching the output limit. first_pass='- Task :core:test PASSED - Task :api:compileJava FAILED > Task :api:compileJava FAILED > Task :api:compileJava FAILED > Task :api:compileJava FAILED > Task :...' repair_pass="<think> Okay, let's see. The user provided a previous answer that was invalid for recall-oriented compression. The previous answer had multiple tasks with er..." |
| `playwright-02` | `structured` | `playwright` | `30428.58` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | project, chromium, file, checkout.spec.ts, line, test | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='project": "chromium", "chromium": { "checkout.spec.ts": { "line": 42, "error": "expect(page).toHaveURL(/success/) failed", "reason": "page should have URL \'/...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='project": "chromium", "chromium": { "checkout.spec.ts": { "line": 42, "test": "checkout", "file": "checkout.spec.ts" } } }, { "project": "webkit", "webkit": ...' |
| `postgres-04` | `structured` | `postgres` | `23035.69` | `0.312` | `0.424` | `0.750` | `0.000` | `0.000` | `0.577` | `soft_accepted` | missing_exact_anchors | errors, file, line, message | - |
| `vite-01` | `structured` | `vite` | `24301.96` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | /repo/apps/admin/src/App.tsx, @acme/ui/Button, /repo/apps/admin/src/client.ts, @acme/api, /repo/apps/public/src/Home.tsx | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json [vite]: Rollup failed to resolve import "@acme/ui/Button" from "/repo/apps/admin/src/App.tsx". [vite]: Rollup failed to resolve import "@acme/api" fr...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json [vite]: Rollup failed to resolve import "@acme/ui/Button" from "/repo/apps/admin/src/App.tsx". [vite]: Rollup failed to resolve import "@acme/api" fr...' |
| `python-pytest-06` | `exact_format` | `python-pytest` | `20086.02` | `0.170` | `1.000` | `0.332` | `0.000` | `0.000` | `0.333` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `git-04` | `exact_format` | `git` | `20878.80` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | schema_echo, prompt_scaffold_echo, exact_format_contract_breakage | 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['schema_echo', 'prompt_scaffold_echo', 'exact_format_contract_breakage'] first_pass='- return only the requested value, command, identifier, or lines - no prose, labels, bullets, headings, code fences, or surrounding context - if the instruct...' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='9f4c2d7a1b8e3c6d0a1234567890abcdef123456 Author: CI Bot Status: deployed to staging' |
| `docker-04` | `exact_format` | `docker` | `21592.43` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='pushed ghcr.io/acme/api:2026.05.18 digest: sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='pushed ghcr.io/acme/api:2026.05.18 digest: sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444' |
| `npm-08` | `exact_format` | `npm` | `33578.32` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `10197.30` | `0.197` | `1.000` | `0.319` | `0.000` | `0.000` | `0.300` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `22165.66` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | migrator-v2-9xk, prod | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='migrator-v2-9xk 0/1 Error 0 33m worker-123 1/1 Running 0 1h namespace: prod' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='- migrator-v2-9xk 0/1 Error 0 33m - prod' |
| `cargo-05` | `exact_format` | `cargo` | `17822.68` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | auth::tests::rejects_expired, billing::tests::rounds_half_even | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- return the exact requested lines only' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='auth::tests::rejects_expired - billing::tests::rounds_half_even' |
| `curl-03` | `exact_format` | `curl` | `8056.11` | `0.190` | `1.000` | `0.273` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `7888.24` | `0.182` | `1.000` | `0.253` | `0.000` | `0.000` | `0.143` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `16070.95` | `0.943` | `1.000` | `0.885` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `22912.52` | `0.945` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `6690.38` | `0.956` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `18618.69` | `0.960` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `8983.79` | `0.944` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `26649.90` | `0.685` | `1.000` | `0.812` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `17633.52` | `0.620` | `0.167` | `0.791` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | contents: read, contents: write | - |
| `runtime-01` | `recall` | `runtime` | `9238.99` | `0.983` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `8351.74` | `0.984` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `10973.32` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `24175.79` | `0.974` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `17323.64` | `0.714` | `0.667` | `0.959` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `11319.36` | `0.964` | `1.000` | `0.950` | `1.000` | `0.931` | `0.769` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `11033.89` | `0.979` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `7973.16` | `0.966` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `7222.54` | `0.960` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `12222.97` | `0.977` | `1.000` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `10279.52` | `0.982` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `8214.65` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `6480.35` | `0.975` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `35434.72` | `0.943` | `1.000` | `0.892` | `1.000` | `0.909` | `0.696` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `9414.64` | `0.979` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `7547.10` | `0.980` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `8998.97` | `0.962` | `1.000` | `0.847` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `7659.49` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `7202.28` | `0.967` | `1.000` | `0.870` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `6850.38` | `0.958` | `1.000` | `0.832` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `18971.85` | `0.984` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `13044.27` | `0.976` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `31158.87` | `0.746` | `0.778` | `0.913` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 404  Not Found | - |
| `testing-05` | `recall` | `testing` | `5761.28` | `0.948` | `1.000` | `0.792` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `16926.86` | `0.957` | `1.000` | `0.892` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `9800.67` | `0.882` | `1.000` | `0.875` | `1.000` | `0.864` | `0.545` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `5560.83` | `0.961` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `6987.09` | `0.954` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `15043.85` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `18053.40` | `0.900` | `1.000` | `0.833` | `1.000` | `0.933` | `0.778` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `21848.57` | `0.660` | `1.000` | `0.852` | `0.333` | `0.305` | `0.714` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `22519.46` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | ERROR:, * rerun pytest test_auth.py::TestAuth::test_login | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='ERROR: test_login (__main__.TestAuth) Traceback (most recent call last): File "test_auth.py", line 10, in test_login assert login("user", "pass") AssertionError' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='ERROR: test_login (__main__.TestAuth) Traceback (most recent call last): File "test_auth.py", line 10, in test_login assert login("user", "pass") AssertionEr...' |
| `ci-05` | `instruction_following` | `ci` | `36703.17` | `0.539` | `1.000` | `0.758` | `0.500` | `0.360` | `0.067` | `soft_accepted` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `21300.06` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | E302, found 1 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- E302 - found 1' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json - E302 - found 1 ```' |
| `kubernetes-06` | `structured` | `kubernetes` | `5606.29` | `0.599` | `1.000` | `0.996` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `59245.01` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | InstanceId, State | fallback output validation failed: model did not stop thinking before reaching the output limit. first_pass='<think> Okay, let\'s see. The user wants to convert the given JSON into a Markdown table. The input is a JSON object with a "Reservations" array containing a ...' repair_pass='<think> Okay, let\'s see. The user wants to convert a JSON object into a Markdown table. The input is a JSON with a "Reservations" array containing a single r...' |
| `network-01` | `exact_format` | `network` | `9927.60` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `13885.06` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | Timeout while waiting for response | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='Timeout while waiting for response INFO: Retrying... ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response' |
| `shell-03` | `exact_format` | `shell` | `35507.42` | `0.085` | `0.000` | `0.747` | `0.000` | `0.000` | `0.500` | `soft_accepted` | missing_exact_anchors, verbatim_alignment_weak | OUTPUT: | - |
| `shell-04` | `exact_format` | `shell` | `7974.02` | `0.208` | `1.000` | `0.492` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `31770.92` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | Resources: 1 added, instance_id | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- instance_id = "i-0abcd1234efgh" - instance_public_ip = "35.153.12.34"' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='instance_id = "i-0abcd1234efgh" - instance_public_ip = "35.153.12.34" Apply complete! Resources: 1 added, 0 changed, 0 destroyed.' |
| `build-05` | `exact_format` | `build` | `14669.17` | `0.225` | `1.000` | `0.609` | `0.000` | `0.000` | `0.286` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `7491.38` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `5662.66` | `0.935` | `1.000` | `0.870` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `3561.96` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `7105.12` | `0.959` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `8327.65` | `0.943` | `1.000` | `0.885` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `7865.23` | `0.903` | `1.000` | `0.877` | `1.000` | `0.894` | `0.647` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `3782.81` | `0.932` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `6431.33` | `0.954` | `1.000` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `11448.30` | `0.930` | `1.000` | `0.860` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `6080.92` | `0.944` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `4455.61` | `0.950` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `5806.59` | `0.867` | `1.000` | `0.734` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `4687.24` | `0.947` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `5858.48` | `0.901` | `1.000` | `0.802` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `4357.62` | `0.932` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `17874.81` | `0.920` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `5343.98` | `0.950` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `3642.07` | `0.948` | `1.000` | `0.896` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `5585.87` | `0.916` | `1.000` | `0.832` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `4438.20` | `0.933` | `1.000` | `0.866` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `7698.95` | `0.599` | `1.000` | `0.996` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `61108.67` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | InstanceId, State | fallback output validation failed: model did not stop thinking before reaching the output limit. first_pass='<think> Okay, let\'s see. The user wants to convert the given JSON into a Markdown table. The input is a JSON object with a "Reservations" array containing a ...' repair_pass='<think> Okay, let\'s see. The user wants to convert a JSON object into a Markdown table. The input is a JSON with a "Reservations" array containing a single r...' |
| `network-02` | `exact_format` | `network` | `10530.40` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `13622.86` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | Timeout while waiting for response | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response INFO: Retrying...' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response INFO: Retrying...' |
| `shell-07` | `exact_format` | `shell` | `13526.30` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | value1, value2 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- value1 - value2' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='value1 - value2' |
| `build-06` | `exact_format` | `build` | `31607.90` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | Resources: 1 added, instance_id | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- instance_id = "i-0abcd1234efgh" - instance_public_ip = "35.153.12.34"' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='instance_id = "i-0abcd1234efgh" - instance_public_ip = "35.153.12.34" Apply complete! Resources: 1 added, 0 changed, 0 destroyed.' |
| `runtime-07` | `exact_format` | `runtime` | `7376.35` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `9456.48` | `0.292` | `1.000` | `0.924` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `9398.41` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `5442.00` | `0.935` | `1.000` | `0.870` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `3322.89` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `3657.73` | `0.960` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `10498.08` | `0.918` | `1.000` | `0.836` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `5953.31` | `0.954` | `1.000` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `4902.03` | `0.963` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `6859.21` | `0.913` | `1.000` | `0.826` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `4588.26` | `0.928` | `1.000` | `0.856` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `4743.27` | `0.939` | `1.000` | `0.878` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
