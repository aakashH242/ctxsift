# remote-gpt-4.1-mini

## Scenario

- track: `remote`
- phase: `remote-screen`
- model: `gpt-4.1-mini`
- quantization: `none`
- device: `remote`
- dtype: `remote`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `6669.78`
- cpu_rss_bytes: `694587392`
- gpu_peak_bytes: `0`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `259`
- accepted_count: `247`
- soft_accepted_count: `12`
- rejected_count: `21`
- exact_pass_count: `254`
- avg_inference_ms: `1836.30`
- p95_inference_ms: `3902.78`
- avg_exact_preservation_ratio: `0.918`
- avg_summary_quality_ratio: `0.850`
- avg_format_adherence_score: `0.852`
- avg_instruction_following_score: `0.845`
- avg_brevity_ratio: `0.959`
- avg_case_score: `0.850`
- p10_case_score: `0.274`
- quality_core: `0.735`
- latency_factor: `1.000`
- final_score: `73.46`
- peak_cpu_rss_bytes: `704884736`
- peak_gpu_bytes: `0`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `1445.12` | `0.993` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-02` | `summary` | `python` | `2073.95` | `0.886` | `1.000` | `0.965` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `python-03` | `recall` | `python` | `3025.37` | `0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `1855.47` | `0.994` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `2607.76` | `0.997` | `1.000` | `0.986` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `2410.76` | `0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `1961.12` | `0.994` | `1.000` | `0.984` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `3146.80` | `0.968` | `1.000` | `0.976` | `1.000` | `0.923` | `0.742` | `accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `1435.22` | `0.996` | `1.000` | `0.985` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `1729.04` | `0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `2337.50` | `0.996` | `1.000` | `0.984` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `3692.54` | `0.993` | `1.000` | `0.983` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `1505.94` | `0.996` | `1.000` | `0.984` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `1305.48` | `0.982` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-02` | `summary` | `ruff` | `2387.85` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `2379.46` | `0.987` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `1162.94` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `2379.63` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `1410.57` | `0.998` | `1.000` | `0.995` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `1331.66` | `0.995` | `1.000` | `0.988` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `1522.25` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `1219.47` | `0.993` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `1548.73` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `1296.51` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `988.69` | `0.988` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `1355.41` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `2498.02` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `1635.02` | `0.991` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `2969.87` | `0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `1828.73` | `0.995` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `4489.17` | `0.991` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-01` | `recall` | `eslint` | `1618.88` | `0.990` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `1132.79` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `1271.64` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `1131.84` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `1164.14` | `0.987` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `3556.34` | `0.993` | `1.000` | `0.983` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `988.66` | `0.996` | `1.000` | `0.991` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `4004.45` | `0.995` | `1.000` | `0.981` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `1225.55` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `2858.12` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `1625.99` | `0.993` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `1257.07` | `0.991` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `1762.72` | `0.976` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `1017.98` | `0.996` | `1.000` | `0.990` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `2423.66` | `0.993` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `1273.00` | `0.997` | `1.000` | `0.986` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `2115.39` | `0.994` | `1.000` | `0.986` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `1453.37` | `0.995` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `1216.98` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `1383.37` | `0.979` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `1289.18` | `0.981` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `1245.25` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `1722.88` | `0.994` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `2003.68` | `0.839` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `ssh-01` | `summary` | `ssh` | `3302.56` | `0.998` | `1.000` | `0.995` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `1131.59` | `0.992` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `991.24` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `1032.51` | `0.976` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `3891.48` | `0.988` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `3353.28` | `0.995` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `2848.12` | `0.982` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `1065.77` | `0.991` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `1191.79` | `0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `1296.47` | `0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-02` | `summary` | `maven` | `1524.59` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `1856.90` | `0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `993.47` | `0.991` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `1131.01` | `0.991` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `1288.07` | `0.984` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `1063.57` | `0.995` | `1.000` | `0.981` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-04` | `summary` | `npm` | `1871.67` | `0.978` | `1.000` | `0.956` | `1.000` | `0.991` | `0.971` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `1019.89` | `0.994` | `1.000` | `0.986` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `1263.97` | `0.994` | `1.000` | `0.986` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `2967.34` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `2952.57` | `0.996` | `1.000` | `0.990` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `2035.21` | `0.989` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `4256.73` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund, Dockerfile:8, zod@3.23.8, failed to solve | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='=> [4/8] RUN npm ci --no-audit --no-fund 29.7s 29.12 npm ERR! Missing: zod@3.23.8 from lock file Dockerfile:8 ERROR: failed to solve: process "/bin/sh -c npm...' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='$ docker build -t example/web:dev . => [4/8] RUN npm ci --no-audit --no-fund Dockerfile:8 npm ERR! Missing: zod@3.23.8 from lock file ERROR: failed to solve:...' |
| `docker-compose-04` | `summary` | `docker-compose` | `1308.91` | `0.992` | `1.000` | `0.981` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `1162.09` | `0.992` | `1.000` | `0.981` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `2720.70` | `0.832` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `1470.42` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `1435.85` | `0.994` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `1483.74` | `0.979` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `1204.49` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `1319.55` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `2806.02` | `0.999` | `1.000` | `0.997` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `1344.99` | `0.999` | `1.000` | `0.994` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `1121.16` | `0.997` | `1.000` | `0.992` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `1395.23` | `0.991` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `2779.03` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `1799.14` | `0.980` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `924.16` | `0.995` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `2184.85` | `0.797` | `0.905` | `0.920` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | exit code 2 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `1607.92` | `0.968` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `2131.21` | `0.795` | `0.875` | `0.916` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | exit code 137 | - |
| `make-01` | `summary` | `make` | `1243.60` | `0.995` | `1.000` | `0.987` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `1581.09` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `1410.33` | `0.995` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `1738.02` | `0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `2750.69` | `0.998` | `1.000` | `0.990` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `7786.80` | `0.991` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-log-01` | `recall` | `ci-log` | `1586.17` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `12021.46` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `5116.32` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-log-01` | `summary` | `build-log` | `4616.57` | `0.980` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `946.25` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `1606.45` | `0.758` | `1.000` | `0.995` | `0.400` | `0.400` | `1.000` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `1642.70` | `0.968` | `1.000` | `0.893` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `9710.42` | `0.654` | `0.355` | `0.663` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `7419.68` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | /work/app/services/payments.py, 42, reportArgumentType, /work/app/api/routes.py, 21, reportUndefinedVariable | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json [ { "file": "/work/app/services/payments.py", "line": 42, "code": "reportArgumentType", "message": "Argument of type \\"str | None\\" cannot be assigne...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json [ { "file": "/work/app/services/payments.py", "line": 42, "code": "reportArgumentType", "message": "Argument of type \\"str | None\\" cannot be assigne...' |
| `structured-output-02` | `structured` | `structured-output` | `1944.77` | `0.511` | `1.000` | `0.703` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-03` | `structured` | `structured-output` | `3086.43` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | createSession › rejects expired refresh token, src/auth/session.test.ts, "refresh token expired", "invalid refresh token", calculateTax › uses EU VAT for DE customer, src/billing/tax.test.ts, Expected: 19, Received: 0 | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```markdown | Test | File | Error | |-------------------------------------------|--------------------------|---------------------------| | createSession › re...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```markdown | Test | File | Error | |---------------------------------------|--------------------------|---------------------------------------------| | crea...' |
| `structured-output-04` | `structured` | `structured-output` | `3743.96` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | /repo/apps/web/src/main.tsx, @sentry/browser, /repo/packages/time/src/format.ts, date-fns-tz, /repo/packages/time/src/parse.ts, /repo/apps/web/src/features/flags.ts, @acme/flags | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "/repo/apps/web/src/main.tsx": [ "@sentry/browser" ], "/repo/packages/time/src/format.ts": [ "date-fns-tz" ], "/repo/packages/time/src/parse.ts": [...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "/repo/apps/web/src/main.tsx": [ "@sentry/browser" ], "/repo/packages/time/src/format.ts": [ "date-fns-tz" ], "/repo/packages/time/src/parse.ts": [...' |
| `exact-format-01` | `exact_format` | `exact-format` | `2156.75` | `0.850` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `1331.80` | `0.286` | `1.000` | `0.858` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `1092.04` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `2534.50` | `0.975` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `1337.20` | `0.964` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `1893.04` | `0.875` | `1.000` | `0.928` | `0.667` | `0.623` | `0.780` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `3567.31` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `1638.37` | `0.981` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `1786.27` | `0.993` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `1083.51` | `0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `2359.27` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `2238.37` | `0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `3389.03` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `1676.25` | `0.989` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `1597.54` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `3025.59` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `1647.21` | `0.996` | `1.000` | `0.983` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `962.22` | `0.990` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `1226.38` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `7413.39` | `0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `8381.94` | `0.787` | `0.851` | `0.974` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Failed asserting that '88.00' is identical to '86.40' | - |
| `nginx-03` | `recall` | `nginx` | `1225.64` | `0.992` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `2727.98` | `0.993` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `2040.28` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `4555.69` | `0.984` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `1400.76` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `1170.33` | `0.997` | `1.000` | `0.989` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `1124.25` | `0.972` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `998.10` | `0.978` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `1041.00` | `0.968` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `1987.73` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `2290.37` | `0.952` | `1.000` | `0.879` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `3140.16` | `0.969` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `2537.49` | `0.969` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `1221.93` | `0.977` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `1179.87` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `2879.34` | `0.968` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `1119.07` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `1008.46` | `0.977` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `1038.81` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `1675.65` | `0.978` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `1135.40` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `1091.21` | `0.998` | `1.000` | `0.994` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `1318.29` | `0.919` | `1.000` | `0.729` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `2145.97` | `0.429` | `1.000` | `0.708` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `2847.13` | `0.943` | `1.000` | `0.811` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `1267.24` | `0.919` | `1.000` | `0.730` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `1120.56` | `0.900` | `1.000` | `0.932` | `0.800` | `0.800` | `1.000` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `2013.27` | `0.523` | `1.000` | `0.742` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `1005.21` | `0.918` | `1.000` | `0.726` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `2900.67` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | UserService.java:[44,17], findByEmail, UserController.java:[28,31], java.lang.Long, java.util.UUID | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- UserService.java:[44,17] cannot find symbol symbol: method findByEmail(java.lang.String) - UserController.java:[28,31] incompatible types: java.lang.Long c...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- UserService.java:[44,17] cannot find symbol symbol: method findByEmail(java.lang.String) - UserController.java:[28,31] incompatible types: java.lang.Long c...' |
| `playwright-01` | `instruction_following` | `playwright` | `1151.34` | `0.915` | `1.000` | `0.715` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `1956.86` | `0.850` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `6722.42` | `0.444` | `1.000` | `0.907` | `0.000` | `0.000` | `0.500` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `1707.16` | `0.952` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `2625.75` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | rsync, /var/backups/uploads, Permission denied (13), exit code 23 | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) rsync error: some files/attrs were not transferred (code 23) at main.c(1338)...' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) backup.sh failed with exit code 23' |
| `pyright-01` | `structured` | `pyright` | `2777.25` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | file, /repo/app/user.py, line, code, reportOptionalMemberAccess, message | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json [ { "file": "/repo/app/user.py", "line": 31, "code": "\\"email\\" is not a known attribute of \\"None\\"", "reportOptionalMemberAccess": "error", "messag...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json [ { "file": "/repo/app/user.py", "line": 31, "code": "\\"email\\" is not a known attribute of \\"None\\"", "reportOptionalMemberAccess": "error", "messag...' |
| `terraform-10` | `structured` | `terraform` | `3212.94` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | add, aws_iam_role.app, change, resource, aws_lambda_function.api, field | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "add": [ "aws_iam_role.app" ], "change": [ { "resource": "aws_lambda_function.api", "field": "memory_size" } ] } ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "add": [ "aws_iam_role.app" ], "change": [ { "resource": "aws_lambda_function.api", "field": "memory_size" } ] } ```' |
| `junit-01` | `structured` | `junit` | `4661.38` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | Test, Error, Location, ---, CalculatorTest, dividesByZero | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```markdown | Test | Error | Location | |-----------------|------------------------------|-------------------| | CalculatorTest | java.lang.ArithmeticExcepti...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```markdown | Test | Error | Location | |----------------|---------------------------------|------------------| | CalculatorTest | dividesByZero | Calculator...' |
| `kubernetes-03` | `structured` | `kubernetes` | `1245.06` | `0.587` | `1.000` | `0.323` | `0.475` | `0.475` | `1.000` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `2530.63` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | src/a.ts, line, column, rule, no-unused-vars, src/b.ts | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "src/a.ts": [ { "line": 1, "column": 7, "rule": "no-unused-vars" } ] } ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "src/a.ts": [ { "line": 1, "column": 7, "rule": "no-unused-vars" } ], "src/b.ts": [] } ```' |
| `docker-build-04` | `structured` | `docker-build` | `2607.58` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | stage, builder, command, pnpm, build, error | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "stage": "builder", "builder": "5/6", "command": "pnpm build", "pnpm": "build", "error": "Error: Cannot find module \'@acme/config\'" } ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "stage": "builder", "builder": "5/6", "command": "pnpm build", "pnpm": "build", "error": "Error: Cannot find module \'@acme/config\'" } ```' |
| `go-test-04` | `structured` | `go-test` | `3918.82` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | failed_tests, name, TestParseAmount, location, amount_test.go:22, message | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml failed_tests: - name: TestParseAmount location: amount_test.go:22 message: got 10.0 want 10.00 ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml failed_tests: - name: TestParseAmount location: amount_test.go:22 message: got 10.0 want 10.00 ```' |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `976.58` | `0.986` | `1.000` | `1.000` | `1.000` | `0.957` | `0.857` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `2671.44` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | package, legacy-widget@2.4.0, peer, react, required, 18.0.0 | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "package": "legacy-widget@2.4.0", "peer": "react", "required": "18.0.0" } ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "package": "legacy-widget@2.4.0", "peer": "react", "required": "18.0.0" } ```' |
| `mypy-06` | `structured` | `mypy` | `2607.22` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | File, Line, Code, Message, ---, app/api.py | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```markdown | File | Line | Code | Message | |------------|------|---------------------|------------------------------------| | app/api.py | 10 | Module has ...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```markdown | File | Line | Code | Message | |------------|------|--------------------------|--------------------------------------| | app/api.py | 10 | Modu...' |
| `gradle-03` | `structured` | `gradle` | `2539.40` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | failed, task, :api:compileJava, cause, cannot, find | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "task": ":api:compileJava", "failed": true, "cause": "cannot find symbol" } ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "task": ":api:compileJava", "failed": true, "cause": "cannot find symbol" } ```' |
| `playwright-02` | `structured` | `playwright` | `3353.70` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | project, chromium, file, checkout.spec.ts, line, test | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "project": "chromium", "file": "checkout.spec.ts", "line": 42, "test": "checkout › submits card", "reason": "expect(page).toHaveURL(/success/) fail...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "project": "chromium", "file": "checkout.spec.ts", "line": 42, "test": "checkout › submits card", "reason": "expect(page).toHaveURL(/success/) fail...' |
| `postgres-04` | `structured` | `postgres` | `3963.57` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | errors, file, migrations/004.sql, line, message, column | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml - file: migrations/004.sql line: 12 message: column "tenant_id" contains null values column: tenant_id errors: true - file: migrations/004.sql line: ...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml - file: migrations/004.sql line: 12 message: column "tenant_id" contains null values column: tenant_id errors: true - file: migrations/004.sql line: ...' |
| `vite-01` | `structured` | `vite` | `2971.50` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | /repo/apps/admin/src/App.tsx, @acme/ui/Button, /repo/apps/admin/src/client.ts, @acme/api, /repo/apps/public/src/Home.tsx | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "/repo/apps/admin/src/App.tsx": [ "@acme/ui/Button" ], "/repo/apps/admin/src/client.ts": [ "@acme/api" ], "/repo/apps/public/src/Home.tsx": [ "@acm...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "/repo/apps/admin/src/App.tsx": [ "@acme/ui/Button" ], "/repo/apps/admin/src/client.ts": [ "@acme/api" ], "/repo/apps/public/src/Home.tsx": [ "@acm...' |
| `python-pytest-06` | `exact_format` | `python-pytest` | `900.80` | `0.195` | `1.000` | `0.320` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `1340.93` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `976.28` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `745.16` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `1072.64` | `0.197` | `1.000` | `0.319` | `0.000` | `0.000` | `0.300` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `909.84` | `0.231` | `1.000` | `0.306` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `820.49` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `743.90` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `2236.55` | `0.179` | `1.000` | `0.255` | `0.000` | `0.000` | `0.077` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `1273.62` | `0.961` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `5425.77` | `0.944` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `1160.25` | `0.958` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `1053.30` | `0.959` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `1080.89` | `0.967` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `2173.25` | `0.907` | `1.000` | `0.814` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `1304.66` | `0.955` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `887.66` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `1022.92` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `880.60` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `917.58` | `0.976` | `1.000` | `0.903` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `1098.57` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `1116.74` | `0.965` | `1.000` | `0.952` | `1.000` | `0.931` | `0.769` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `1157.99` | `0.984` | `1.000` | `0.959` | `1.000` | `0.981` | `0.938` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `1234.58` | `0.968` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `1050.82` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `1172.76` | `0.981` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `1000.95` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `899.43` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `728.48` | `0.975` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `1318.08` | `0.979` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `912.57` | `0.977` | `1.000` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `1130.10` | `0.981` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1235.89` | `0.971` | `1.000` | `0.883` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `792.54` | `0.996` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `948.03` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `871.18` | `0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `1082.45` | `0.978` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `806.79` | `0.984` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `3492.38` | `0.833` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `1052.66` | `0.976` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `1750.58` | `0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `1098.94` | `0.884` | `1.000` | `0.880` | `1.000` | `0.864` | `0.545` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `715.84` | `0.961` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `787.65` | `0.953` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `1050.23` | `0.907` | `1.000` | `0.955` | `1.000` | `0.850` | `0.500` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `956.04` | `0.942` | `1.000` | `0.856` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `1828.38` | `0.980` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `984.16` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `3457.45` | `0.545` | `1.000` | `0.769` | `0.500` | `0.365` | `0.100` | `soft_accepted` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `4781.55` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | E302, found 1 | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "file": "/app/main.py", "line": 10, "column": 1, "code": "E302", "message": "expected 2 blank lines, found 1" } ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json [ { "code": "E302", "message": "found 1" } ] ```' |
| `kubernetes-06` | `structured` | `kubernetes` | `2917.80` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | kind, metadata, spec | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml kind: Service metadata: name: my-service namespace: default spec: clusterIP: 10.0.0.1 ports: - port: 80 protocol: TCP ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml kind: Service metadata: name: my-service namespace: default spec: clusterIP: 10.0.0.1 ports: - port: 80 protocol: TCP ```' |
| `deployment-02` | `structured` | `deployment` | `1069.41` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `2129.44` | `0.299` | `1.000` | `0.990` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `4050.77` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | Timeout while waiting for response | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response ERROR: Timeout while waiting for response' |
| `shell-03` | `exact_format` | `shell` | `728.60` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `1492.25` | `0.232` | `1.000` | `0.320` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `1730.41` | `0.279` | `1.000` | `0.789` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `build-05` | `exact_format` | `build` | `806.87` | `0.233` | `1.000` | `0.333` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `1879.44` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `1847.61` | `0.933` | `1.000` | `0.903` | `1.000` | `0.944` | `0.812` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `1060.93` | `0.932` | `1.000` | `0.887` | `1.000` | `0.965` | `0.882` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `1074.05` | `0.898` | `1.000` | `0.886` | `1.000` | `0.867` | `0.556` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `1028.53` | `0.942` | `1.000` | `0.896` | `1.000` | `0.982` | `0.941` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `2031.96` | `0.965` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `932.70` | `0.966` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `2842.12` | `0.875` | `1.000` | `0.839` | `1.000` | `0.867` | `0.556` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `1280.22` | `0.951` | `1.000` | `0.913` | `1.000` | `0.983` | `0.944` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1931.36` | `0.938` | `1.000` | `0.877` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `2028.56` | `0.972` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `1330.71` | `0.945` | `1.000` | `0.891` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `2237.25` | `0.920` | `1.000` | `0.897` | `1.000` | `0.914` | `0.714` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `1162.57` | `0.872` | `1.000` | `0.851` | `1.000` | `0.841` | `0.471` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `4035.06` | `0.954` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `2020.82` | `0.912` | `1.000` | `0.898` | `1.000` | `0.889` | `0.632` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `2152.81` | `0.944` | `1.000` | `0.920` | `1.000` | `0.953` | `0.842` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `963.55` | `0.899` | `1.000` | `0.876` | `1.000` | `0.883` | `0.611` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `1175.60` | `0.906` | `1.000` | `0.888` | `1.000` | `0.887` | `0.625` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `1070.40` | `0.957` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `1533.80` | `0.539` | `1.000` | `0.325` | `0.354` | `0.354` | `1.000` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `1014.84` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `770.62` | `0.299` | `1.000` | `0.991` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `696.48` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `735.86` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `1854.70` | `0.279` | `1.000` | `0.789` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `739.23` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `794.39` | `0.287` | `1.000` | `0.945` | `0.000` | `0.000` | `0.857` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `1787.78` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `1985.68` | `0.915` | `1.000` | `0.900` | `1.000` | `0.895` | `0.650` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `1137.19` | `0.932` | `1.000` | `0.887` | `1.000` | `0.965` | `0.882` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `1801.25` | `0.609` | `0.000` | `0.876` | `1.000` | `0.936` | `0.786` | `soft_accepted` | missing_exact_anchors | Could not locate 'config.yaml' | - |
| `explanation-13` | `explanation` | `explanation` | `2239.32` | `0.959` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `2239.70` | `0.906` | `1.000` | `0.888` | `1.000` | `0.887` | `0.625` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `1347.08` | `0.976` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `1131.56` | `0.937` | `1.000` | `0.917` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `2136.27` | `0.940` | `1.000` | `0.937` | `1.000` | `0.914` | `0.714` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `896.34` | `0.944` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
