# remote-gpt-4o

## Scenario

- track: `remote`
- phase: `remote-screen`
- model: `gpt-4o`
- quantization: `none`
- device: `remote`
- dtype: `remote`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `1639.58`
- cpu_rss_bytes: `1949057024`
- gpu_peak_bytes: `1234713600`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `256`
- accepted_count: `246`
- soft_accepted_count: `10`
- rejected_count: `24`
- exact_pass_count: `250`
- avg_inference_ms: `1651.79`
- p95_inference_ms: `3377.53`
- avg_exact_preservation_ratio: `0.908`
- avg_summary_quality_ratio: `0.839`
- avg_format_adherence_score: `0.867`
- avg_instruction_following_score: `0.860`
- avg_brevity_ratio: `0.969`
- avg_case_score: `0.856`
- p10_case_score: `0.232`
- quality_core: `0.731`
- latency_factor: `1.000`
- final_score: `73.11`
- peak_cpu_rss_bytes: `1949290496`
- peak_gpu_bytes: `1234713600`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `1286.26` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-02` | `summary` | `python` | `2298.65` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass="``` $ python services/worker.py --queue emails --concurrency 4 ModuleNotFoundError: No module named 'dramatiq_abort' ```" repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='``` File "/workspace/services/worker.py", line 11, in <module> ModuleNotFoundError: No module named \'dramatiq_abort\' worker boot failed ```' |
| `python-03` | `recall` | `python` | `1689.65` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `1345.49` | `0.998` | `1.000` | `0.991` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `1605.36` | `0.992` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `1074.46` | `0.999` | `1.000` | `0.996` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `2835.32` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `1429.37` | `0.995` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `2258.48` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `3763.17` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `1187.46` | `0.996` | `1.000` | `0.984` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `3668.86` | `0.986` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `1301.64` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `1900.37` | `0.957` | `0.911` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `1492.76` | `0.995` | `1.000` | `0.987` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `940.58` | `0.997` | `1.000` | `0.992` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `2083.81` | `0.996` | `1.000` | `0.984` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `2741.20` | `0.983` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `1032.91` | `0.997` | `1.000` | `0.992` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `1171.34` | `0.996` | `1.000` | `0.990` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `837.37` | `0.990` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `999.01` | `0.996` | `1.000` | `0.985` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `1428.92` | `0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `1381.67` | `0.992` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `4216.21` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `1303.13` | `0.994` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `4132.50` | `0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `1317.13` | `0.994` | `1.000` | `0.986` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `1268.24` | `0.987` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `1117.76` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `5030.14` | `0.988` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-01` | `recall` | `eslint` | `1355.10` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `2355.16` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `2002.58` | `0.985` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `1577.35` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `933.67` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `7424.29` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `933.17` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `887.22` | `0.996` | `1.000` | `0.983` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `1158.97` | `0.995` | `1.000` | `0.988` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `1404.97` | `0.990` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `1708.31` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `959.07` | `0.996` | `1.000` | `0.989` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `1717.37` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `1067.15` | `0.994` | `1.000` | `0.985` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `1110.89` | `0.997` | `1.000` | `0.989` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `1035.30` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `1053.59` | `0.987` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `939.40` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `1994.48` | `0.987` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `901.37` | `0.981` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `2516.01` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `1121.60` | `0.998` | `1.000` | `0.990` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `1543.58` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `1087.64` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-01` | `summary` | `ssh` | `1291.08` | `0.991` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `1562.20` | `0.990` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `871.26` | `0.991` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `1003.85` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `1163.74` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `1284.02` | `0.997` | `1.000` | `0.988` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `1778.33` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `887.72` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `1157.22` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `1207.14` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-02` | `summary` | `maven` | `1239.07` | `0.995` | `1.000` | `0.987` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `1047.00` | `0.997` | `1.000` | `0.987` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `948.01` | `0.978` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `1013.83` | `0.992` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `1348.06` | `0.992` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `1101.56` | `0.993` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-04` | `summary` | `npm` | `1877.56` | `0.988` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `984.62` | `0.991` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `945.76` | `0.991` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `1228.10` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `1037.32` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `3362.03` | `0.976` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `1187.16` | `0.973` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `1014.72` | `0.982` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `892.55` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `2747.66` | `0.832` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `5927.57` | `0.993` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `1293.61` | `0.997` | `1.000` | `0.987` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `1259.47` | `0.977` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `1625.52` | `0.986` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `1368.70` | `0.991` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `1249.64` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `1136.87` | `0.998` | `1.000` | `0.991` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `988.20` | `0.992` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `1055.88` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `1005.19` | `0.986` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `1475.27` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `838.17` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `5140.19` | `0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `1034.91` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `2063.91` | `0.972` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `971.34` | `0.985` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `2433.35` | `0.956` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `926.62` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `1468.94` | `0.963` | `1.000` | `0.907` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `1010.77` | `0.998` | `1.000` | `0.993` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `1417.17` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-log-01` | `recall` | `ci-log` | `1044.45` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `1832.38` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `3617.32` | `0.991` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-log-01` | `summary` | `build-log` | `2599.27` | `0.956` | `1.000` | `0.891` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `1094.26` | `0.774` | `1.000` | `0.935` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `1414.18` | `0.866` | `1.000` | `0.998` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `1276.57` | `0.839` | `1.000` | `0.795` | `0.750` | `0.750` | `1.000` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `2092.23` | `0.627` | `0.226` | `0.643` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | exit status 22, https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `3598.68` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | /work/app/services/payments.py, 42, reportArgumentType, /work/app/api/routes.py, 21, reportUndefinedVariable | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json [ { "file": "/work/app/services/payments.py", "line": 42, "code": "reportArgumentType", "message": "Argument of type \\"str | None\\" cannot be assigne...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json [ { "file": "/work/app/services/payments.py", "line": 42, "code": "reportArgumentType", "message": "Argument of type \\"str | None\\" cannot be assigne...' |
| `structured-output-02` | `structured` | `structured-output` | `3604.34` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | test / integration, Start docker compose, port 5432 is already allocated, deploy / preview, Upload artifact, dist/preview | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml failed_jobs: - job: test / integration step: Start docker compose exit_code: 1 cause: port 5432 is already allocated - job: deploy / preview step: Up...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml failed_jobs: - job: test / integration step: Start docker compose exit_code: 1 cause: port 5432 is already allocated - job: deploy / preview step: Up...' |
| `structured-output-03` | `structured` | `structured-output` | `2434.62` | `0.824` | `0.929` | `0.944` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "invalid refresh token" | - |
| `structured-output-04` | `structured` | `structured-output` | `3685.58` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | /repo/apps/web/src/main.tsx, @sentry/browser, /repo/packages/time/src/format.ts, date-fns-tz, /repo/packages/time/src/parse.ts, /repo/apps/web/src/features/flags.ts, @acme/flags | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "/repo/apps/web/src/main.tsx": [ "@sentry/browser" ], "/repo/packages/time/src/format.ts": [ "date-fns-tz" ], "/repo/packages/time/src/parse.ts": [...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "/repo/apps/web/src/main.tsx": [ { "import": "@sentry/browser", "issue": "Rollup failed to resolve import" } ], "/repo/packages/time/src/format.ts"...' |
| `exact-format-01` | `exact_format` | `exact-format` | `2059.10` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | tests/api/test_users.py::test_create_user_requires_email, tests/api/test_users.py::test_delete_user_requires_admin, tests/jobs/test_reconcile.py::TestReconcile::test_retries_deadlock | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='``` tests/api/test_users.py::test_create_user_requires_email tests/api/test_users.py::test_delete_user_requires_admin tests/jobs/test_reconcile.py::TestRecon...' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='``` FAILED tests/api/test_users.py::test_create_user_requires_email - AssertionError: 201 != 422 FAILED tests/api/test_users.py::test_delete_user_requires_ad...' |
| `exact-format-02` | `exact_format` | `exact-format` | `2289.05` | `0.156` | `0.714` | `0.576` | `0.000` | `0.000` | `0.375` | `soft_accepted` | missing_exact_anchors | SearchBox debounces network query before fetch | - |
| `exact-format-03` | `exact_format` | `exact-format` | `1202.35` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `2828.47` | `0.966` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `1408.98` | `0.943` | `1.000` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `1264.97` | `0.976` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `1926.49` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `2053.79` | `0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `1146.72` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `941.32` | `0.985` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `1062.06` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `1736.03` | `0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `2539.90` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `850.72` | `0.997` | `1.000` | `0.987` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `1485.29` | `0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `2321.38` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `1337.12` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `1506.40` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `1604.17` | `0.986` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `1463.57` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `2599.24` | `0.993` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `1255.99` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `1026.81` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `1027.68` | `0.992` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `2391.17` | `0.984` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `2083.49` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `2214.78` | `0.995` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `1377.75` | `0.972` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `2016.76` | `0.978` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `1682.31` | `0.968` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `1396.00` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `1669.89` | `0.950` | `1.000` | `0.875` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `2736.83` | `0.965` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `3424.05` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `2818.32` | `0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `6300.36` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `2615.62` | `0.974` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `3067.26` | `0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `2521.09` | `0.974` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `1888.75` | `0.967` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `1543.96` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `1714.11` | `0.979` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `2307.17` | `1.000` | `1.000` | `0.998` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `1283.45` | `0.919` | `1.000` | `0.729` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `5319.37` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | tests/test_api.py::test_create_user, tests/test_auth.py::test_refresh_token_expiry | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='``` tests/test_api.py::test_create_user tests/test_auth.py::test_refresh_token_expiry ```' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='``` FAILED tests/test_api.py::test_create_user - assert 201 == 422 FAILED tests/test_auth.py::test_refresh_token_expiry - AssertionError ```' |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `1106.46` | `0.938` | `1.000` | `0.795` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `1071.79` | `0.919` | `1.000` | `0.730` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `6150.77` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | npm ERR! code ENOTEMPTY, npm ERR! syscall rename, /repo/node_modules/esbuild, /repo/node_modules/.esbuild.DELETE | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='``` npm ERR! code ENOTEMPTY npm ERR! syscall rename ```' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='``` npm ERR! code ENOTEMPTY npm ERR! syscall rename npm ERR! path /repo/node_modules/esbuild npm ERR! dest /repo/node_modules/.esbuild.DELETE ```' |
| `docker-build-03` | `instruction_following` | `docker-build` | `892.39` | `0.523` | `1.000` | `0.742` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `2210.66` | `0.918` | `1.000` | `0.728` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `1203.67` | `0.996` | `1.000` | `0.988` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `1951.23` | `0.714` | `1.000` | `0.715` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `2537.12` | `0.850` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `1914.82` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | worker-5b8c, CrashLoopBackOff, migrator-9z1q, Error | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='``` worker-5b8c 0/1 CrashLoopBackOff 6 migrator-9z1q 0/1 Error 0 ```' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='``` worker-5b8c 0/1 CrashLoopBackOff 6 migrator-9z1q 0/1 Error 0 ```' |
| `cargo-04` | `instruction_following` | `cargo` | `2542.81` | `0.963` | `1.000` | `0.875` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `2097.24` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | rsync, /var/backups/uploads, Permission denied (13), exit code 23 | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13)' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) backup.sh failed with exit code 23' |
| `pyright-01` | `structured` | `pyright` | `2655.14` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | file, /repo/app/user.py, line, code, reportOptionalMemberAccess, message | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "file": "/repo/app/user.py", "line": 31, "code": "reportOptionalMemberAccess", "message": "\\"email\\" is not a known attribute of \\"None\\"" } ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "file": "/repo/app/user.py", "line": 31, "code": "reportOptionalMemberAccess", "message": "\\"email\\" is not a known attribute of \\"None\\"" } ```' |
| `terraform-10` | `structured` | `terraform` | `2330.00` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | add, aws_iam_role.app, change, resource, aws_lambda_function.api, field | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "add": ["aws_iam_role.app"], "change": { "resource": "aws_lambda_function.api", "field": "memory_size", "from": 512, "to": 1024 } } ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "add": ["aws_iam_role.app"], "change": { "resource": "aws_lambda_function.api", "field": "memory_size" } } ```' |
| `junit-01` | `structured` | `junit` | `2204.62` | `0.713` | `0.857` | `0.559` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | dividesByZero | - |
| `kubernetes-03` | `structured` | `kubernetes` | `2443.18` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | unhealthy_pods, name, api-77df, status, CrashLoopBackOff, restarts | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml unhealthy_pods: - name: api-77df status: CrashLoopBackOff restarts: 5 ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml unhealthy_pods: - name: api-77df status: CrashLoopBackOff restarts: 5 - name: search-0 status: ImagePullBackOff restarts: 0 ```' |
| `eslint-06` | `structured` | `eslint` | `2613.84` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | src/a.ts, line, column, rule, no-unused-vars, src/b.ts | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json [ { "file": "src/a.ts", "line": 1, "column": 7, "rule": "no-unused-vars" } ] ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json [ { "file": "src/a.ts", "line": 1, "column": 7, "rule": "no-unused-vars" }, { "file": "src/b.ts", "line": 8, "column": 10, "rule": "no-console" }, { ...' |
| `docker-build-04` | `structured` | `docker-build` | `2703.61` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | stage, builder, command, pnpm, build, error | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "stage": "builder", "command": "pnpm build", "error": "Cannot find module \'@acme/config\'" } ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "stage": "builder", "command": "pnpm build", "error": "Cannot find module \'@acme/config\'" } ```' |
| `go-test-04` | `structured` | `go-test` | `2290.73` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | failed_tests, name, TestParseAmount, location, amount_test.go:22, message | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml failed_tests: - name: TestParseAmount location: amount_test.go:22 message: got 10.0 want 10.00 ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml failed_tests: - name: TestParseAmount location: amount_test.go:22 message: got 10.0 want 10.00 ```' |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `1540.32` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `2671.80` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | package, legacy-widget@2.4.0, peer, react, required, 18.0.0 | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "package": "legacy-widget@2.4.0", "conflicting_dependency": { "peer": "react", "required": "^18.0.0", "found": "react@19.0.0", "conflict": "react@1...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "package": "legacy-widget@2.4.0", "peer": "react", "required": "^18.0.0", "found": "react@19.0.0" } ```' |
| `mypy-06` | `structured` | `mypy` | `1817.53` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `3138.21` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | failed, task, :api:compileJava, cause, cannot, find | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "task": ":api:compileJava", "result": "FAILED", "error": { "file": "/repo/api/src/main/java/App.java", "line": 19, "cause": "cannot find symbol" } ...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "task": ":api:compileJava", "result": "failed", "cause": "cannot find symbol" } ```' |
| `playwright-02` | `structured` | `playwright` | `3185.54` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | project, chromium, file, checkout.spec.ts, line, test | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json [ { "project": "chromium", "file": "checkout.spec.ts", "line": 42, "test": "checkout › submits card" } ] ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json [ { "project": "chromium", "file": "checkout.spec.ts", "line": 42, "test": "checkout › submits card" } ] ```' |
| `postgres-04` | `structured` | `postgres` | `2625.60` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | errors, file, migrations/004.sql, line, message, column | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml errors: - file: migrations/004.sql line: 12 error: ERROR: column "tenant_id" contains null values - file: migrations/004.sql line: 20 error: ERROR: c...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml errors: - file: migrations/004.sql line: 12 message: ERROR: column "tenant_id" contains null values - file: migrations/004.sql line: 20 message: ERRO...' |
| `vite-01` | `structured` | `vite` | `2684.86` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | /repo/apps/admin/src/App.tsx, @acme/ui/Button, /repo/apps/admin/src/client.ts, @acme/api, /repo/apps/public/src/Home.tsx | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "errors": [ { "file": "/repo/apps/admin/src/App.tsx", "import": "@acme/ui/Button", "reason": "Rollup failed to resolve import" }, { "file": "/repo/...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "errors": [ { "file": "/repo/apps/admin/src/App.tsx", "import": "@acme/ui/Button", "reason": "Rollup failed to resolve import" }, { "file": "/repo/...' |
| `python-pytest-06` | `exact_format` | `python-pytest` | `961.11` | `0.195` | `1.000` | `0.320` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `855.33` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `2419.60` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `729.60` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `1607.72` | `0.212` | `1.000` | `0.319` | `0.000` | `0.000` | `0.600` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `822.94` | `0.230` | `1.000` | `0.305` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `1095.35` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `736.78` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `819.99` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `1224.68` | `0.937` | `1.000` | `0.875` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `2905.78` | `0.907` | `1.000` | `0.841` | `1.000` | `0.960` | `0.868` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `2265.35` | `0.965` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `897.15` | `0.965` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `1154.77` | `0.964` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `2413.61` | `0.901` | `1.000` | `0.802` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `1225.39` | `0.948` | `1.000` | `0.896` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `781.25` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `1510.54` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `1103.30` | `0.984` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `1356.81` | `0.973` | `1.000` | `0.894` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `1161.56` | `0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `1145.59` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `1506.00` | `0.986` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `854.88` | `0.975` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `869.35` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `1166.10` | `0.980` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `1615.14` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `1199.82` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `748.45` | `0.975` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `1168.08` | `0.985` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `993.79` | `0.974` | `1.000` | `0.896` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `915.54` | `0.975` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1195.97` | `0.969` | `1.000` | `0.875` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `980.28` | `0.996` | `1.000` | `0.984` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `977.47` | `0.972` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `1055.23` | `0.981` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `1364.86` | `0.981` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `1942.97` | `0.994` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `2343.63` | `0.837` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `715.57` | `0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `1158.93` | `0.920` | `1.000` | `0.869` | `1.000` | `0.945` | `0.818` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `1877.28` | `0.910` | `1.000` | `0.868` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `835.03` | `0.961` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `772.35` | `0.953` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `1998.51` | `0.669` | `0.667` | `0.910` | `1.000` | `0.812` | `0.375` | `soft_accepted` | missing_exact_anchors | unable to resolve dependency tree | - |
| `rust-02` | `summary` | `rust` | `2014.92` | `0.926` | `1.000` | `0.862` | `1.000` | `0.962` | `0.875` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `2123.56` | `0.986` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `920.44` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `2946.33` | `0.545` | `1.000` | `0.769` | `0.500` | `0.365` | `0.100` | `soft_accepted` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `2883.90` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | E302, found 1 | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "file": "/app/main.py", "line": 10, "column": 1, "error_code": "E302", "message": "expected 2 blank lines, found 1" } ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "file": "/app/main.py", "line": 10, "column": 1, "error_code": "E302", "raw_output": "/app/main.py:10:1: E302 expected 2 blank lines, found 1", "re...' |
| `kubernetes-06` | `structured` | `kubernetes` | `2682.38` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | kind, metadata, spec | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml kind: Service metadata: name: my-service namespace: default spec: clusterIP: 10.0.0.1 ports: - port: 80 protocol: TCP ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml kind: Service metadata: name: my-service namespace: default spec: clusterIP: 10.0.0.1 ports: - port: 80 protocol: TCP ```' |
| `deployment-02` | `structured` | `deployment` | `792.34` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `1580.85` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `997.14` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `1724.96` | `1.000` | `1.000` | `0.999` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `869.18` | `0.232` | `1.000` | `0.320` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `2054.20` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | Resources: 1 added, instance_id | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- Resources: 1 added - instance_id = "i-0abcd1234efgh"' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- Resources: 1 added - instance_id = "i-0abcd1234efgh"' |
| `build-05` | `exact_format` | `build` | `805.16` | `0.233` | `1.000` | `0.333` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `710.17` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `2060.54` | `0.934` | `1.000` | `0.895` | `1.000` | `0.960` | `0.867` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `1896.33` | `0.927` | `1.000` | `0.887` | `1.000` | `0.950` | `0.833` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `5755.63` | `0.950` | `1.000` | `0.933` | `1.000` | `0.950` | `0.833` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `880.88` | `0.927` | `1.000` | `0.886` | `1.000` | `0.953` | `0.842` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `2142.77` | `0.912` | `1.000` | `0.894` | `1.000` | `0.894` | `0.647` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `2471.45` | `0.966` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `1554.47` | `0.887` | `1.000` | `0.856` | `1.000` | `0.876` | `0.588` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `1215.35` | `0.956` | `1.000` | `0.911` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `2487.68` | `0.940` | `1.000` | `0.910` | `1.000` | `0.954` | `0.846` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `993.63` | `0.960` | `1.000` | `0.932` | `1.000` | `0.982` | `0.941` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `1315.34` | `0.946` | `1.000` | `0.903` | `1.000` | `0.983` | `0.944` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `1057.47` | `0.912` | `1.000` | `0.893` | `1.000` | `0.896` | `0.652` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `1917.15` | `0.898` | `1.000` | `0.837` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `2033.42` | `0.953` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `2498.38` | `0.922` | `1.000` | `0.885` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `4293.31` | `0.965` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `963.08` | `0.911` | `1.000` | `0.885` | `1.000` | `0.906` | `0.688` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `1225.98` | `0.914` | `1.000` | `0.897` | `1.000` | `0.896` | `0.652` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `903.29` | `0.953` | `1.000` | `0.907` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `2577.90` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | kind, metadata, spec | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml kind: Service metadata: name: my-service namespace: default spec: clusterIP: 10.0.0.1 ports: - port: 80 protocol: TCP ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml kind: Service metadata: name: my-service namespace: default spec: clusterIP: 10.0.0.1 ports: - port: 80 protocol: TCP ```' |
| `linting-03` | `structured` | `linting` | `1038.43` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `1800.75` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `1024.25` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `692.39` | `1.000` | `1.000` | `0.999` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `2124.00` | `0.411` | `1.000` | `0.497` | `0.333` | `0.333` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `runtime-07` | `exact_format` | `runtime` | `1348.10` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `838.49` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `2040.94` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `1378.36` | `0.936` | `1.000` | `0.898` | `1.000` | `0.960` | `0.867` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `1058.03` | `0.942` | `1.000` | `0.897` | `1.000` | `0.981` | `0.938` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `1809.84` | `0.960` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `2466.94` | `0.969` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `1092.82` | `0.877` | `1.000` | `0.870` | `1.000` | `0.825` | `0.417` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `2730.22` | `0.928` | `1.000` | `0.928` | `1.000` | `0.892` | `0.640` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `912.28` | `0.957` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `1032.66` | `0.912` | `1.000` | `0.900` | `1.000` | `0.887` | `0.625` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1953.00` | `0.951` | `1.000` | `0.902` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
