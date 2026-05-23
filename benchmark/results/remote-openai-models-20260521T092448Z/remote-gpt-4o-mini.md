# remote-gpt-4o-mini

## Scenario

- track: `remote`
- phase: `remote-screen`
- model: `gpt-4o-mini`
- quantization: `none`
- device: `remote`
- dtype: `remote`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `2522.69`
- cpu_rss_bytes: `1939992576`
- gpu_peak_bytes: `1226193920`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `265`
- accepted_count: `250`
- soft_accepted_count: `15`
- rejected_count: `15`
- exact_pass_count: `259`
- avg_inference_ms: `2087.44`
- p95_inference_ms: `4557.84`
- avg_exact_preservation_ratio: `0.941`
- avg_summary_quality_ratio: `0.854`
- avg_format_adherence_score: `0.867`
- avg_instruction_following_score: `0.860`
- avg_brevity_ratio: `0.967`
- avg_case_score: `0.868`
- p10_case_score: `0.427`
- quality_core: `0.780`
- latency_factor: `0.994`
- final_score: `77.46`
- peak_cpu_rss_bytes: `1940221952`
- peak_gpu_bytes: `1226193920`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `2052.43` | `0.997` | `1.000` | `0.988` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-02` | `summary` | `python` | `4376.18` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_lines_contract_breakage | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='```plaintext python services/worker.py --queue emails --concurrency 4 /workspace/services/worker.py line 11 ModuleNotFoundError dramatiq_abort worker boot fa...' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='```plaintext python services/worker.py --queue emails --concurrency 4 /workspace/services/worker.py line 11 ModuleNotFoundError dramatiq_abort worker boot fa...' |
| `python-03` | `recall` | `python` | `2051.18` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `1998.68` | `0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `2137.08` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `4029.86` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `2311.72` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `4733.02` | `0.996` | `1.000` | `0.986` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `2318.02` | `0.997` | `1.000` | `0.989` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `2045.21` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `2047.77` | `0.998` | `1.000` | `0.990` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `2155.66` | `0.994` | `1.000` | `0.986` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `2500.67` | `0.993` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `2102.51` | `0.954` | `0.911` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `1996.35` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `1667.19` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `1741.26` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `1548.52` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `1407.46` | `0.994` | `1.000` | `0.984` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `1893.57` | `0.990` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `2584.08` | `0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `1208.01` | `0.996` | `1.000` | `0.985` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `2695.93` | `0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `2116.71` | `0.985` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `1488.38` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `4939.07` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `1961.38` | `0.996` | `1.000` | `0.991` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `2496.98` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `1861.15` | `0.984` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `1755.58` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `5663.62` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | empty_output | tsc src/index.ts src/http.ts --pretty false, src/index.ts(48,20), TS2769, URL, RequestInit, src/http.ts(9,17) | litellm output validation failed: model did not stop thinking before reaching the output limit. first_pass="tsc src/index.ts src/http.ts --pretty false src/index.ts(48,20): error TS2769: No overload matches this call. Overload 1 of 2, '(url: string, init?: RequestI..." repair_pass="tsc src/index.ts src/http.ts --pretty false src/index.ts(48,20): error TS2769: No overload matches this call. Argument of type 'URL' is not assignable to par..." |
| `eslint-01` | `recall` | `eslint` | `2435.54` | `0.985` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `3481.83` | `0.976` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `2093.42` | `0.988` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `1629.13` | `0.986` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `3588.97` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `1679.08` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `1479.42` | `0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `2607.38` | `0.997` | `1.000` | `0.988` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `1204.44` | `0.983` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `2795.76` | `0.987` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `1968.25` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `1628.17` | `0.996` | `1.000` | `0.989` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `2786.55` | `0.956` | `1.000` | `0.926` | `1.000` | `0.923` | `0.743` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `1525.52` | `0.992` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `1683.02` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `1668.48` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `3249.15` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `1352.59` | `0.992` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `1305.06` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `1849.92` | `0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `1365.03` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `1347.69` | `0.995` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `1875.39` | `0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `3108.37` | `0.839` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `ssh-01` | `summary` | `ssh` | `1799.35` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `1457.32` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `1089.53` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `1633.64` | `0.970` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `1592.68` | `0.977` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `2127.63` | `0.995` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `1058.14` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `3885.93` | `0.984` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `1564.71` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `3081.87` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-02` | `summary` | `maven` | `2026.87` | `0.963` | `1.000` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `1917.47` | `0.997` | `1.000` | `0.990` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `2437.21` | `0.985` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `1801.74` | `0.983` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `4257.29` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `1606.03` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-04` | `summary` | `npm` | `3009.51` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `2471.27` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `1694.40` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `1851.20` | `0.988` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `3169.12` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `5224.62` | `0.972` | `1.000` | `0.939` | `1.000` | `0.992` | `0.972` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `3251.86` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `1345.91` | `0.994` | `1.000` | `0.984` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `1758.48` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `2744.06` | `0.830` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `2060.73` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `2170.85` | `0.997` | `1.000` | `0.989` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `4070.43` | `0.962` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `1393.93` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `1542.34` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `1687.45` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `1692.35` | `0.998` | `1.000` | `0.991` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `1644.87` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `2155.39` | `0.994` | `1.000` | `0.985` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `1849.66` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `2029.46` | `0.930` | `1.000` | `0.945` | `1.000` | `0.904` | `0.681` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `1305.15` | `0.994` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `1414.90` | `0.986` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `3373.21` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `941.74` | `0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `1609.59` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `2638.74` | `0.939` | `1.000` | `0.881` | `1.000` | `0.973` | `0.909` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `1423.28` | `0.994` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `1549.28` | `0.992` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `4559.57` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `1431.22` | `0.986` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-log-01` | `recall` | `ci-log` | `1826.90` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `2697.22` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `4676.46` | `0.991` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-log-01` | `summary` | `build-log` | `3739.42` | `0.962` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `1086.87` | `0.775` | `1.000` | `0.938` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `2573.96` | `0.866` | `1.000` | `0.998` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `1638.81` | `0.946` | `1.000` | `0.821` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `3147.12` | `0.627` | `0.226` | `0.643` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | exit status 22, https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `6362.23` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | /work/app/services/payments.py, 42, reportArgumentType, /work/app/api/routes.py, 21, reportUndefinedVariable | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json [ { "file": "/work/app/services/payments.py", "line": 42, "code": "reportArgumentType", "message": "Argument of type \\"str | None\\" cannot be assigne...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json [ { "file": "/work/app/services/payments.py", "line": 42, "code": "reportArgumentType", "message": "Argument of type \\"str | None\\" cannot be assigne...' |
| `structured-output-02` | `structured` | `structured-output` | `2224.01` | `0.568` | `1.000` | `0.894` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-03` | `structured` | `structured-output` | `4580.10` | `0.826` | `0.929` | `0.954` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "refresh token expired" | - |
| `structured-output-04` | `structured` | `structured-output` | `2386.29` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `2772.77` | `0.850` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `2133.54` | `0.233` | `1.000` | `0.331` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `2486.93` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `1745.76` | `0.960` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `4105.01` | `0.744` | `0.750` | `0.850` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `1806.19` | `0.903` | `1.000` | `0.940` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `4087.55` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `2131.12` | `0.981` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `2735.19` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `1982.73` | `0.984` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `1954.89` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `1573.83` | `0.983` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `1775.26` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `1489.13` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `5824.64` | `0.989` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `2143.21` | `0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `2783.50` | `0.985` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `1680.31` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `1455.30` | `0.984` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `1487.29` | `0.983` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `1792.25` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `1528.65` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `1759.29` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `1586.92` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `4621.97` | `0.749` | `0.792` | `0.901` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | //services/reporting:report_parser_test | - |
| `powershell-01` | `recall` | `powershell` | `1348.55` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `1669.69` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `2107.82` | `0.769` | `0.783` | `0.897` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/refunds | - |
| `go-test-03` | `summary` | `go-test` | `1172.43` | `0.976` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `4754.92` | `0.953` | `1.000` | `0.883` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `1049.22` | `0.971` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `6579.97` | `0.954` | `1.000` | `0.886` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `3785.23` | `0.963` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `4617.44` | `0.967` | `1.000` | `0.948` | `1.000` | `0.975` | `0.917` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `3747.42` | `0.966` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `2580.79` | `0.968` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `3424.93` | `0.970` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `870.30` | `0.954` | `1.000` | `0.885` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `3590.00` | `0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `1366.14` | `0.967` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `4550.89` | `0.971` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `1769.97` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `2128.54` | `0.998` | `1.000` | `0.994` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `1431.94` | `0.919` | `1.000` | `0.729` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `1519.82` | `0.429` | `1.000` | `0.708` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `1368.39` | `0.940` | `1.000` | `0.799` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `1248.40` | `0.919` | `1.000` | `0.730` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `1855.62` | `0.899` | `1.000` | `0.931` | `0.800` | `0.800` | `1.000` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `1097.69` | `0.523` | `1.000` | `0.742` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `1065.74` | `0.650` | `1.000` | `0.722` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `2778.80` | `0.852` | `1.000` | `0.952` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `2963.16` | `0.646` | `1.000` | `0.708` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `1670.72` | `0.849` | `1.000` | `0.997` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `1235.92` | `0.489` | `1.000` | `0.854` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `4727.18` | `0.720` | `1.000` | `0.867` | `0.400` | `0.400` | `1.000` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `2119.59` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | rsync, /var/backups/uploads, Permission denied (13), exit code 23 | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) exit code 23' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='rsync: [sender] change_dir "/var/backups/uploads" failed: Permission denied (13) exit code 23' |
| `pyright-01` | `structured` | `pyright` | `3241.17` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | file, /repo/app/user.py, line, code, reportOptionalMemberAccess, message | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "file": "/repo/app/user.py", "line": "31:12", "code": "error", "reportOptionalMemberAccess": "email", "message": "\\"email\\" is not a known attribut...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "file": "/repo/app/user.py", "line": "31:12", "code": "error", "reportOptionalMemberAccess": "email", "message": "\\"email\\" is not a known attribut...' |
| `terraform-10` | `structured` | `terraform` | `2643.59` | `0.387` | `1.000` | `0.191` | `0.200` | `0.170` | `0.500` | `accepted` | - | - | - |
| `junit-01` | `structured` | `junit` | `1349.98` | `0.928` | `1.000` | `0.760` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `2968.51` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | unhealthy_pods, name, api-77df, status, CrashLoopBackOff, restarts | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml unhealthy_pods: - name: api-77df status: CrashLoopBackOff restarts: 5 ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml unhealthy_pods: - name: api-77df status: CrashLoopBackOff restarts: 5 ```' |
| `eslint-06` | `structured` | `eslint` | `3832.96` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | src/a.ts, line, column, rule, no-unused-vars, src/b.ts | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "errors": [ { "file": "src/a.ts", "line": 1, "column": 7, "rule": "no-unused-vars" } ] } ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "errors": [ { "file": "src/a.ts", "line": 1, "column": 7, "rule": "no-unused-vars" }, { "file": "src/b.ts", "line": 9, "column": 3, "rule": "@types...' |
| `docker-build-04` | `structured` | `docker-build` | `3813.53` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | stage, builder, command, pnpm, build, error | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "stage": "#8", "builder": "[builder 5/6]", "command": "RUN pnpm build", "pnpm": "pnpm build", "build": "Error: Cannot find module \'@acme/config\'", ...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "stage": "#8", "builder": "[builder 5/6]", "command": "RUN pnpm build", "pnpm": "pnpm build", "build": "Error: Cannot find module \'@acme/config\'", ...' |
| `go-test-04` | `structured` | `go-test` | `3786.19` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | failed_tests, name, TestParseAmount, location, amount_test.go:22, message | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml failed_tests: - name: TestParseAmount location: amount_test.go:22 message: got 10.0 want 10.00 ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml failed_tests: - name: TestParseAmount location: amount_test.go:22 message: got 10.0 want 10.00 ```' |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `1289.13` | `0.986` | `1.000` | `1.000` | `1.000` | `0.957` | `0.857` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `1642.87` | `0.800` | `1.000` | `0.601` | `0.800` | `0.800` | `1.000` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `2047.73` | `0.935` | `1.000` | `0.817` | `1.000` | `0.970` | `0.900` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `1132.29` | `0.405` | `1.000` | `0.183` | `0.125` | `0.125` | `1.000` | `accepted` | - | - | - |
| `playwright-02` | `structured` | `playwright` | `3505.92` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | project, chromium, file, checkout.spec.ts, line, test | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "project": "chromium", "file": "checkout.spec.ts", "line": "42:3", "test": "checkout › submits card", "error": "expect(page).toHaveURL(/success/) f...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "project": "chromium", "file": "checkout.spec.ts", "line": "42:3", "test": "checkout › submits card", "error": "expect(page).toHaveURL(/success/) f...' |
| `postgres-04` | `structured` | `postgres` | `3769.77` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | errors, file, migrations/004.sql, line, message, column | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml - file: migrations/004.sql line: 12 error: "ERROR: column \\"tenant_id\\" contains null values" message: "column \\"tenant_id\\" contains null values" co...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml - errors: - file: migrations/004.sql line: 12 error: "ERROR: column \\"tenant_id\\" contains null values" message: "column \\"tenant_id\\" contains null ...' |
| `vite-01` | `structured` | `vite` | `5861.29` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | /repo/apps/admin/src/App.tsx, @acme/ui/Button, /repo/apps/admin/src/client.ts, @acme/api, /repo/apps/public/src/Home.tsx | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```json { "errors": [ { "file": "/repo/apps/admin/src/App.tsx", "import": "@acme/ui/Button" }, { "file": "/repo/apps/admin/src/client.ts", "import": "@acme/a...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "errors": [ { "file": "/repo/apps/admin/src/App.tsx", "import": "@acme/ui/Button" }, { "file": "/repo/apps/admin/src/client.ts", "import": "@acme/a...' |
| `python-pytest-06` | `exact_format` | `python-pytest` | `1002.22` | `0.195` | `1.000` | `0.320` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `1569.92` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `1318.64` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `869.65` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `965.08` | `0.233` | `1.000` | `0.334` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `5544.64` | `0.230` | `1.000` | `0.305` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `1316.69` | `1.000` | `1.000` | `0.998` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `789.36` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `945.66` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `1502.96` | `0.946` | `1.000` | `0.892` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `1891.96` | `0.936` | `1.000` | `0.871` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `2448.59` | `0.956` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `3242.85` | `0.960` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `1672.44` | `0.969` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `4354.81` | `0.691` | `1.000` | `0.826` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `1891.87` | `0.911` | `1.000` | `0.823` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `961.00` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `1086.59` | `0.986` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `3714.35` | `0.755` | `1.000` | `0.955` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `package-management-01` | `recall` | `package-management` | `1597.78` | `0.975` | `1.000` | `0.898` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `1055.32` | `0.990` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `1283.08` | `0.960` | `1.000` | `0.953` | `1.000` | `0.914` | `0.714` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `1803.44` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `868.87` | `0.976` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `1393.37` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `1175.82` | `0.976` | `1.000` | `0.903` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `1663.10` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `1960.00` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `810.11` | `0.974` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `928.78` | `0.982` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `919.94` | `0.980` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `1049.70` | `0.989` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1262.88` | `0.969` | `1.000` | `0.874` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `1650.01` | `0.991` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `1368.25` | `0.972` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `989.78` | `0.966` | `1.000` | `0.865` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `2165.69` | `0.978` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `1214.10` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `3068.50` | `0.833` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `893.98` | `0.976` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `917.62` | `0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `794.08` | `0.945` | `1.000` | `0.862` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `843.22` | `0.961` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `838.00` | `0.953` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `2270.08` | `0.890` | `1.000` | `0.938` | `1.000` | `0.829` | `0.429` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `975.52` | `0.942` | `1.000` | `0.856` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `2648.04` | `0.778` | `1.000` | `0.928` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `1540.32` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `1863.68` | `0.529` | `1.000` | `0.629` | `0.500` | `0.400` | `0.333` | `soft_accepted` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `2000.89` | `0.349` | `1.000` | `0.189` | `0.000` | `0.000` | `0.923` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `3323.59` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | kind, metadata, spec | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml kind: Service metadata: name: my-service namespace: default spec: clusterIP: 10.0.0.1 ports: - port: 80 protocol: TCP ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml kind: Service metadata: name: my-service namespace: default spec: clusterIP: 10.0.0.1 ports: - port: 80 protocol: TCP ```' |
| `deployment-02` | `structured` | `deployment` | `1966.59` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `939.46` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `1942.71` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `898.64` | `1.000` | `1.000` | `0.999` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `1843.80` | `0.232` | `1.000` | `0.320` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `1996.47` | `0.411` | `1.000` | `0.497` | `0.333` | `0.333` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `build-05` | `exact_format` | `build` | `709.84` | `0.233` | `1.000` | `0.333` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `1778.58` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `1541.07` | `0.935` | `1.000` | `0.897` | `1.000` | `0.960` | `0.867` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `1344.89` | `0.912` | `1.000` | `0.866` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `3911.33` | `0.954` | `1.000` | `0.907` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `1081.99` | `0.940` | `1.000` | `0.902` | `1.000` | `0.967` | `0.889` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `1485.00` | `0.915` | `1.000` | `0.900` | `1.000` | `0.894` | `0.647` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `1170.92` | `0.965` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `2593.60` | `0.922` | `1.000` | `0.844` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `1164.02` | `0.932` | `1.000` | `0.910` | `1.000` | `0.932` | `0.773` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1512.95` | `0.879` | `1.000` | `0.863` | `1.000` | `0.843` | `0.478` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `1946.19` | `0.969` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `1069.61` | `0.956` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `1354.83` | `0.936` | `1.000` | `0.914` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `1199.47` | `0.868` | `1.000` | `0.866` | `1.000` | `0.804` | `0.348` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `1244.26` | `0.955` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `1120.98` | `0.925` | `1.000` | `0.878` | `1.000` | `0.957` | `0.857` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `2320.29` | `0.960` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `2616.61` | `0.881` | `1.000` | `0.862` | `1.000` | `0.850` | `0.500` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `1671.92` | `0.927` | `1.000` | `0.896` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `1287.47` | `0.945` | `1.000` | `0.904` | `1.000` | `0.980` | `0.933` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `3250.35` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | structured_contract_breakage | kind, metadata, spec | litellm output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml kind: Service metadata: name: my-service namespace: default spec: clusterIP: 10.0.0.1 ports: - port: 80 protocol: TCP ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml kind: Service metadata: name: my-service namespace: default spec: clusterIP: 10.0.0.1 ports: - port: 80 protocol: TCP ```' |
| `linting-03` | `structured` | `linting` | `1002.08` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `1416.91` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `1751.03` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | exact_format_contract_breakage | Timeout while waiting for response | litellm output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response' |
| `shell-07` | `exact_format` | `shell` | `796.96` | `1.000` | `1.000` | `0.999` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `1918.30` | `0.411` | `1.000` | `0.497` | `0.333` | `0.333` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `runtime-07` | `exact_format` | `runtime` | `825.83` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `810.89` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `1796.39` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `2513.99` | `0.927` | `1.000` | `0.901` | `1.000` | `0.929` | `0.765` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `3750.91` | `0.937` | `1.000` | `0.874` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `2143.50` | `0.960` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `10704.92` | `0.969` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `3001.38` | `0.928` | `1.000` | `0.856` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `1209.91` | `0.921` | `1.000` | `0.914` | `1.000` | `0.892` | `0.640` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `1245.81` | `0.951` | `1.000` | `0.915` | `1.000` | `0.981` | `0.938` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `2047.09` | `0.961` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1211.63` | `0.942` | `1.000` | `0.885` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
