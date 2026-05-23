# remote-gpt-5.4-nano

## Scenario

- track: `remote`
- phase: `remote-screen`
- model: `gpt-5.4-nano`
- quantization: `none`
- device: `remote`
- dtype: `remote`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `897.24`
- cpu_rss_bytes: `1934458880`
- gpu_peak_bytes: `1217674240`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `277`
- accepted_count: `269`
- soft_accepted_count: `8`
- rejected_count: `3`
- exact_pass_count: `274`
- avg_inference_ms: `1510.74`
- p95_inference_ms: `3127.78`
- avg_exact_preservation_ratio: `0.985`
- avg_summary_quality_ratio: `0.880`
- avg_format_adherence_score: `0.888`
- avg_instruction_following_score: `0.880`
- avg_brevity_ratio: `0.957`
- avg_case_score: `0.896`
- p10_case_score: `0.582`
- quality_core: `0.833`
- latency_factor: `1.000`
- final_score: `83.32`
- peak_cpu_rss_bytes: `1934598144`
- peak_gpu_bytes: `1217674240`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `1551.86` | `0.990` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-02` | `summary` | `python` | `2472.66` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- python services/worker.py --queue emails --concurrency 4 - /workspace/services/worker.py - line 11 - ModuleNotFoundError - dramatiq_abort - worker boot failed' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- python services/worker.py --queue emails --concurrency 4 - /workspace/services/worker.py - line 11 - ModuleNotFoundError - worker boot failed' |
| `python-03` | `recall` | `python` | `1238.42` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `1333.96` | `0.995` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `1529.22` | `0.995` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `1172.37` | `0.995` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `1338.65` | `0.992` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `1358.14` | `0.995` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `1071.26` | `0.994` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `1037.46` | `0.992` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `2006.14` | `0.996` | `1.000` | `0.983` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `3119.01` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `1566.11` | `0.996` | `1.000` | `0.984` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `1111.69` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-02` | `summary` | `ruff` | `3300.58` | `0.997` | `1.000` | `0.993` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `2547.12` | `0.988` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `790.90` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `1376.80` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `1343.08` | `0.993` | `1.000` | `0.983` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `1031.02` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `1230.74` | `0.986` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `905.84` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `1747.98` | `0.989` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `1329.02` | `0.981` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `1254.09` | `0.985` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `1592.39` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `1394.78` | `0.995` | `1.000` | `0.988` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `1303.56` | `0.985` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `1184.33` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `1451.33` | `0.994` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `1504.58` | `0.994` | `1.000` | `0.985` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-01` | `recall` | `eslint` | `1433.85` | `0.984` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `1190.92` | `0.988` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `1482.60` | `0.986` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `1404.98` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `1255.51` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `2520.77` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `1016.41` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `1434.61` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `1499.94` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `1370.61` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `2408.66` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `958.78` | `0.992` | `1.000` | `0.981` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `1555.68` | `0.990` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `1108.31` | `0.991` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `1289.16` | `0.991` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `1076.86` | `0.992` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `977.33` | `0.992` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `1252.99` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `1218.23` | `0.974` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `3456.87` | `0.977` | `1.000` | `0.907` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `986.04` | `0.986` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `946.80` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `1479.90` | `0.993` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `1838.93` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | curl -I https://docs.example.com/sdk/latest, HTTP/2 301, location: /sdk/v3.4/, cache-control: max-age=3600 | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- curl -I https://docs.example.com/sdk/latest - HTTP/2 301 - location: /sdk/v3.4/ - cache-control: max-age=3600' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- curl -I https://docs.example.com/sdk/latest - HTTP/2 301 - location: /sdk/v3.4/ - cache-control: max-age=3600' |
| `ssh-01` | `summary` | `ssh` | `1420.02` | `0.994` | `1.000` | `0.985` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `1354.26` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `1105.21` | `0.988` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `963.89` | `0.967` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `980.23` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `1345.10` | `0.996` | `1.000` | `0.983` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `899.02` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `1169.64` | `0.990` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `1026.88` | `0.977` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `1549.54` | `0.987` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-02` | `summary` | `maven` | `1926.47` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `1365.23` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `1327.63` | `0.979` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `1134.88` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `1130.20` | `0.988` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `1189.88` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-04` | `summary` | `npm` | `1632.75` | `0.987` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `1701.58` | `0.976` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `8755.22` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `1592.76` | `0.992` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `2442.68` | `0.994` | `1.000` | `0.985` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `1241.75` | `0.985` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `3151.62` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund, Dockerfile:8, zod@3.23.8, failed to solve | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='RUN npm ci --no-audit --no-fund Missing: zod@3.23.8 from lock file Missing: undici-types@6.19.8 from lock file Dockerfile:8 failed to solve' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='RUN npm ci --no-audit --no-fund Missing: zod@3.23.8 from lock file Missing: undici-types@6.19.8 from lock file Dockerfile:8 failed to solve' |
| `docker-compose-04` | `summary` | `docker-compose` | `1079.90` | `0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `1452.39` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `2143.60` | `0.830` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `1677.23` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `1330.04` | `0.992` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `1477.50` | `0.970` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `2152.68` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `1086.31` | `0.991` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `1288.62` | `0.991` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `1155.02` | `0.997` | `1.000` | `0.988` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `1724.04` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `1333.99` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `1096.44` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `1415.52` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `886.81` | `0.994` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `2442.66` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `1819.25` | `0.980` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `898.78` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `2037.58` | `0.986` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `1302.36` | `0.992` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `1283.34` | `0.971` | `1.000` | `0.974` | `1.000` | `0.933` | `0.778` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `1405.83` | `0.985` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `1780.65` | `0.998` | `1.000` | `0.991` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `1306.03` | `0.989` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-log-01` | `recall` | `ci-log` | `1653.57` | `0.984` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `1458.52` | `0.993` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `3533.55` | `0.992` | `1.000` | `0.981` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-log-01` | `summary` | `build-log` | `1173.35` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `975.94` | `0.975` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `8054.14` | `0.758` | `1.000` | `0.995` | `0.400` | `0.400` | `1.000` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `1647.84` | `0.855` | `1.000` | `0.849` | `0.750` | `0.750` | `1.000` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `1504.10` | `0.655` | `0.355` | `0.666` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `5882.03` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `3320.78` | `0.511` | `1.000` | `0.703` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-03` | `structured` | `structured-output` | `1210.17` | `0.983` | `1.000` | `0.975` | `1.000` | `0.970` | `0.900` | `accepted` | - | - | - |
| `structured-output-04` | `structured` | `structured-output` | `1151.46` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `2213.21` | `0.189` | `1.000` | `0.336` | `0.000` | `0.000` | `0.100` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `1141.90` | `0.278` | `1.000` | `0.776` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `1331.56` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `1406.43` | `0.978` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `1209.61` | `0.961` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `1880.53` | `0.902` | `1.000` | `0.936` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `1411.78` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `1270.02` | `0.984` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `1423.48` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `2492.10` | `0.984` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `1450.48` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `1373.90` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `1363.93` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `1069.79` | `0.995` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `1278.46` | `0.983` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `1363.66` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `1503.64` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `1127.83` | `0.996` | `1.000` | `0.986` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `1184.71` | `0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `1555.90` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `1250.61` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `1529.91` | `0.986` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `1181.46` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `1088.48` | `0.992` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `1197.89` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `1212.47` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `1346.69` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `1085.50` | `0.972` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `1224.69` | `0.973` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `2555.74` | `0.965` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `1864.23` | `0.978` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `2800.73` | `0.962` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `1406.91` | `0.962` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `2471.49` | `0.974` | `1.000` | `0.958` | `1.000` | `0.981` | `0.936` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `2308.79` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `2821.98` | `0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `2571.16` | `0.977` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `945.20` | `0.970` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `2194.26` | `0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `2012.63` | `0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `1044.38` | `0.982` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `1524.74` | `0.980` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `1108.72` | `1.000` | `1.000` | `0.998` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `1809.22` | `0.962` | `1.000` | `0.873` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `970.18` | `0.429` | `1.000` | `0.708` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `937.01` | `0.940` | `1.000` | `0.799` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `1190.87` | `0.919` | `1.000` | `0.730` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `960.09` | `0.900` | `1.000` | `0.932` | `0.800` | `0.800` | `1.000` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `933.33` | `0.523` | `1.000` | `0.742` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `893.02` | `0.918` | `1.000` | `0.726` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `1452.77` | `0.984` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `1119.10` | `0.919` | `1.000` | `0.730` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `2219.49` | `0.850` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `2018.23` | `0.444` | `1.000` | `0.907` | `0.000` | `0.000` | `0.500` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `1152.24` | `0.968` | `1.000` | `0.892` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `1859.47` | `0.512` | `1.000` | `0.706` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `1092.06` | `0.816` | `1.000` | `0.587` | `0.850` | `0.850` | `1.000` | `accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `1376.72` | `0.608` | `1.000` | `0.326` | `0.525` | `0.525` | `1.000` | `accepted` | - | - | - |
| `junit-01` | `structured` | `junit` | `3213.37` | `0.809` | `0.857` | `0.933` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | dividesByZero | - |
| `kubernetes-03` | `structured` | `kubernetes` | `986.38` | `0.587` | `1.000` | `0.323` | `0.475` | `0.475` | `1.000` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `3634.81` | `0.254` | `0.722` | `0.181` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/b.ts | - |
| `docker-build-04` | `structured` | `docker-build` | `2212.13` | `0.806` | `1.000` | `0.736` | `0.714` | `0.714` | `1.000` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `1096.08` | `0.588` | `1.000` | `0.326` | `0.475` | `0.475` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `1186.71` | `0.869` | `1.000` | `0.696` | `1.000` | `0.880` | `0.600` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `1087.94` | `0.638` | `1.000` | `0.347` | `0.583` | `0.583` | `1.000` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `1677.53` | `0.917` | `1.000` | `0.894` | `1.000` | `0.846` | `0.486` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `942.32` | `0.713` | `1.000` | `0.493` | `0.662` | `0.662` | `1.000` | `accepted` | - | - | - |
| `playwright-02` | `structured` | `playwright` | `940.40` | `0.354` | `1.000` | `0.182` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `1095.61` | `0.475` | `1.000` | `0.584` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `vite-01` | `structured` | `vite` | `2028.11` | `0.256` | `1.000` | `0.179` | `0.000` | `0.000` | `0.027` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `1191.43` | `0.195` | `1.000` | `0.320` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `1104.48` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `875.64` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `836.39` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `1265.82` | `0.204` | `1.000` | `0.323` | `0.000` | `0.000` | `0.429` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `1699.14` | `0.231` | `1.000` | `0.306` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `2594.00` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `1275.80` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `1949.66` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `1004.89` | `0.968` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `1142.05` | `0.945` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `1407.53` | `0.962` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `935.80` | `0.958` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `1143.93` | `0.959` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `1164.41` | `0.904` | `1.000` | `0.809` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `1039.48` | `0.952` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `888.85` | `0.991` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `985.51` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `1031.34` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `927.68` | `0.980` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `814.37` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `1171.77` | `0.985` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `843.37` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `1021.60` | `0.974` | `1.000` | `0.894` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `1079.93` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `1288.23` | `0.981` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `1697.83` | `0.989` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `989.12` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `938.21` | `0.973` | `1.000` | `0.891` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `880.71` | `0.982` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `1058.87` | `0.977` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `1389.06` | `0.981` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1186.98` | `0.973` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `900.20` | `0.991` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `822.57` | `0.986` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `896.44` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `1218.59` | `0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `904.85` | `0.984` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `3162.89` | `0.837` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `1002.50` | `0.976` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `972.75` | `0.964` | `1.000` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `731.04` | `0.952` | `1.000` | `0.881` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `687.89` | `0.961` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `1239.54` | `0.952` | `1.000` | `0.880` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `752.78` | `0.923` | `1.000` | `0.956` | `1.000` | `0.880` | `0.600` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `970.10` | `0.936` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `1795.82` | `0.778` | `1.000` | `0.928` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `1402.71` | `0.922` | `1.000` | `0.739` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `1608.94` | `0.529` | `1.000` | `0.629` | `0.500` | `0.400` | `0.333` | `soft_accepted` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `1125.30` | `0.787` | `1.000` | `0.671` | `0.714` | `0.714` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `1450.32` | `0.539` | `1.000` | `0.325` | `0.354` | `0.354` | `1.000` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `706.62` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `854.24` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `646.32` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `1775.81` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `600.31` | `0.232` | `1.000` | `0.320` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `1581.11` | `0.513` | `1.000` | `0.797` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `build-05` | `exact_format` | `build` | `752.02` | `0.233` | `1.000` | `0.333` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `856.12` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `2156.05` | `0.891` | `1.000` | `0.895` | `1.000` | `0.830` | `0.433` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `1244.89` | `0.891` | `1.000` | `0.870` | `1.000` | `0.867` | `0.556` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `1541.95` | `0.940` | `1.000` | `0.931` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `3582.48` | `0.950` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `1289.78` | `0.924` | `1.000` | `0.925` | `1.000` | `0.883` | `0.611` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `846.24` | `0.967` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `1877.48` | `0.955` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `2191.61` | `0.931` | `1.000` | `0.861` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `2101.76` | `0.944` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `3625.54` | `0.938` | `1.000` | `0.923` | `1.000` | `0.929` | `0.762` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `953.01` | `0.951` | `1.000` | `0.902` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `974.02` | `0.936` | `1.000` | `0.936` | `1.000` | `0.905` | `0.682` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `691.03` | `0.887` | `1.000` | `0.851` | `1.000` | `0.885` | `0.615` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `1829.43` | `0.954` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `2090.12` | `0.927` | `1.000` | `0.853` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `1734.93` | `0.971` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `1162.18` | `0.910` | `1.000` | `0.873` | `1.000` | `0.920` | `0.733` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `2018.84` | `0.932` | `1.000` | `0.864` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `782.96` | `0.947` | `1.000` | `0.907` | `1.000` | `0.980` | `0.933` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `941.09` | `0.539` | `1.000` | `0.325` | `0.354` | `0.354` | `1.000` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `709.63` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `1545.96` | `0.299` | `1.000` | `0.991` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `621.20` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `950.04` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `1660.08` | `0.279` | `1.000` | `0.789` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `1124.47` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `644.40` | `0.253` | `1.000` | `0.525` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `794.33` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `2072.71` | `0.912` | `1.000` | `0.911` | `1.000` | `0.870` | `0.565` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `876.27` | `0.896` | `1.000` | `0.871` | `1.000` | `0.880` | `0.600` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `3309.22` | `0.879` | `1.000` | `0.842` | `1.000` | `0.874` | `0.579` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `2296.53` | `0.933` | `1.000` | `0.929` | `1.000` | `0.905` | `0.684` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `1039.56` | `0.948` | `1.000` | `0.914` | `1.000` | `0.973` | `0.909` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `3254.51` | `0.963` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `2623.10` | `0.952` | `1.000` | `0.916` | `1.000` | `0.981` | `0.938` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `1882.29` | `0.919` | `1.000` | `0.919` | `1.000` | `0.876` | `0.588` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `862.94` | `0.947` | `1.000` | `0.894` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
