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

- load_ms: `2575.00`
- cpu_rss_bytes: `1929846784`
- gpu_peak_bytes: `1234713600`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `280`
- accepted_count: `267`
- soft_accepted_count: `13`
- rejected_count: `0`
- exact_pass_count: `273`
- avg_inference_ms: `2002.58`
- p95_inference_ms: `4453.60`
- avg_exact_preservation_ratio: `0.992`
- avg_summary_quality_ratio: `0.893`
- avg_format_adherence_score: `0.873`
- avg_instruction_following_score: `0.866`
- avg_brevity_ratio: `0.952`
- avg_case_score: `0.894`
- p10_case_score: `0.589`
- quality_core: `0.833`
- latency_factor: `1.000`
- final_score: `83.29`
- peak_cpu_rss_bytes: `1929846784`
- peak_gpu_bytes: `1234713600`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `1820.63` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-02` | `summary` | `python` | `1779.21` | `0.888` | `1.000` | `0.969` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `python-03` | `recall` | `python` | `1607.47` | `0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `1638.64` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `1953.78` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `3774.73` | `0.995` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `3653.48` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `4918.45` | `0.751` | `0.773` | `0.944` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors, verbatim_alignment_weak | tests/jobs/test_retention.py::test_archive_marks_job_deleted | - |
| `pytest-04` | `recall` | `pytest` | `1721.15` | `0.997` | `1.000` | `0.989` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `2456.14` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `1668.88` | `0.998` | `1.000` | `0.992` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `2094.83` | `0.995` | `1.000` | `0.988` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `1848.82` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `2062.62` | `0.954` | `0.911` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `1057.56` | `0.997` | `1.000` | `0.991` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `2403.54` | `0.985` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `1480.84` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `1738.60` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `1838.03` | `0.995` | `1.000` | `0.986` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `1338.12` | `0.996` | `1.000` | `0.990` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `2439.25` | `0.981` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `1009.25` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `4511.35` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `2010.43` | `0.988` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `4328.21` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `1597.86` | `0.992` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `1589.85` | `0.997` | `1.000` | `0.992` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `2097.68` | `0.988` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `1572.51` | `0.983` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `1552.47` | `0.995` | `1.000` | `0.981` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `5636.02` | `0.747` | `1.000` | `0.946` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `eslint-01` | `recall` | `eslint` | `3210.52` | `0.985` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `1290.81` | `0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `4925.06` | `0.988` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `1197.82` | `0.994` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `2415.22` | `0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `2539.81` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `1037.64` | `0.996` | `1.000` | `0.991` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `4036.54` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `2161.60` | `0.983` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `2207.42` | `0.988` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `4450.56` | `0.993` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `1730.42` | `0.996` | `1.000` | `0.989` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `2205.04` | `0.976` | `1.000` | `0.920` | `1.000` | `0.989` | `0.963` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `1572.62` | `0.992` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `1495.50` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `2667.85` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `4511.89` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `3093.54` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `2332.91` | `0.961` | `1.000` | `0.903` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `1608.40` | `0.984` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `1197.63` | `0.977` | `1.000` | `0.907` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `1334.46` | `0.995` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `2900.67` | `0.995` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `2955.33` | `0.840` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `ssh-01` | `summary` | `ssh` | `1420.32` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `1303.02` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `1460.96` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `1580.67` | `0.968` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `1212.99` | `0.977` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `2931.82` | `0.972` | `1.000` | `0.970` | `1.000` | `0.938` | `0.793` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `1212.38` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `2559.59` | `0.974` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `1636.76` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `3287.11` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-02` | `summary` | `maven` | `1883.38` | `0.980` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `5114.52` | `0.977` | `1.000` | `0.958` | `1.000` | `0.964` | `0.880` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `2277.17` | `0.763` | `0.667` | `0.954` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ./gradlew test | - |
| `cargo-01` | `summary` | `cargo` | `1789.58` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `1418.28` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `1153.52` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-04` | `summary` | `npm` | `1620.97` | `0.974` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `2128.29` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `1755.63` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `1553.76` | `0.992` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `3579.38` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `4938.95` | `0.972` | `1.000` | `0.939` | `1.000` | `0.992` | `0.972` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `1782.53` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `1306.63` | `0.995` | `1.000` | `0.987` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `1668.01` | `0.976` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `2973.00` | `0.830` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `1608.29` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `1929.75` | `0.993` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `4969.00` | `0.962` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `1291.82` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `1385.69` | `0.984` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `1387.91` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `2208.60` | `0.998` | `1.000` | `0.991` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `1471.31` | `0.986` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `1231.42` | `0.994` | `1.000` | `0.985` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `1441.13` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `1359.75` | `0.991` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `952.23` | `0.998` | `1.000` | `0.992` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `3197.39` | `0.756` | `0.810` | `0.899` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | line=91, exit code 2 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `1858.53` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `2151.47` | `0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `1531.70` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `1254.34` | `0.992` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `1123.95` | `0.997` | `1.000` | `0.987` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `1441.90` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `1556.54` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `2235.65` | `0.988` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-log-01` | `recall` | `ci-log` | `2051.76` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `2910.24` | `0.991` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `1911.58` | `0.882` | `1.000` | `0.955` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `build-log-01` | `summary` | `build-log` | `2466.95` | `0.969` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `1097.25` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `1512.77` | `0.866` | `1.000` | `0.998` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `1896.16` | `0.946` | `1.000` | `0.821` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `1229.91` | `0.916` | `1.000` | `0.721` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-01` | `structured` | `structured-output` | `2035.58` | `0.590` | `1.000` | `0.977` | `0.000` | `0.000` | `0.967` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `1649.56` | `0.568` | `1.000` | `0.895` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-03` | `structured` | `structured-output` | `4110.65` | `0.933` | `1.000` | `0.778` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-04` | `structured` | `structured-output` | `1717.22` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `3182.18` | `0.300` | `1.000` | `0.997` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `4689.97` | `0.188` | `1.000` | `0.322` | `0.000` | `0.000` | `0.115` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `1703.85` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `1951.68` | `0.956` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `4790.97` | `0.933` | `1.000` | `0.866` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `2144.98` | `0.906` | `1.000` | `0.946` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `3177.22` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `2106.48` | `0.981` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `2364.21` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `1199.74` | `0.985` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `1370.21` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `1173.71` | `0.983` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `2535.56` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `1311.73` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `1815.20` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `1500.43` | `0.993` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `2902.38` | `0.986` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `1153.62` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `1155.73` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `3519.85` | `0.982` | `1.000` | `0.951` | `1.000` | `0.982` | `0.939` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `1232.67` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `2926.21` | `0.987` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `1481.94` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `1178.70` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `3672.90` | `0.984` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `1266.56` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `1646.07` | `0.992` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `2274.90` | `0.769` | `0.783` | `0.897` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/refunds | - |
| `go-test-03` | `summary` | `go-test` | `4093.90` | `0.751` | `0.684` | `0.905` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ./integration | - |
| `npm-05` | `summary` | `npm` | `1205.47` | `0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `1107.25` | `0.971` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `1768.75` | `0.954` | `1.000` | `0.886` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `3509.97` | `0.966` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `4121.40` | `0.962` | `1.000` | `0.936` | `1.000` | `0.975` | `0.917` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `3436.70` | `0.966` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `3145.17` | `0.972` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `3192.59` | `0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `1132.50` | `0.957` | `1.000` | `0.893` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `2722.95` | `0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `1429.83` | `0.967` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `3566.97` | `0.971` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `1216.51` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `1449.60` | `0.998` | `1.000` | `0.994` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `1154.74` | `0.919` | `1.000` | `0.729` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `1009.72` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `1423.84` | `0.940` | `1.000` | `0.799` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `1035.44` | `0.919` | `1.000` | `0.730` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `1322.89` | `0.900` | `1.000` | `0.932` | `0.800` | `0.800` | `1.000` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `1161.89` | `0.523` | `1.000` | `0.742` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `937.67` | `0.650` | `1.000` | `0.722` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `3270.58` | `0.595` | `1.000` | `0.985` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `2022.71` | `0.713` | `1.000` | `0.711` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `894.73` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `1297.66` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `3417.70` | `0.720` | `1.000` | `0.867` | `0.400` | `0.400` | `1.000` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `1019.95` | `0.540` | `1.000` | `0.802` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `3007.94` | `0.465` | `1.000` | `0.686` | `0.000` | `0.000` | `0.593` | `accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `1174.72` | `0.436` | `1.000` | `0.186` | `0.200` | `0.200` | `1.000` | `accepted` | - | - | - |
| `junit-01` | `structured` | `junit` | `1503.99` | `0.928` | `1.000` | `0.760` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `1236.43` | `0.446` | `1.000` | `0.485` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `2564.56` | `0.332` | `1.000` | `0.312` | `0.000` | `0.000` | `0.385` | `accepted` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `2156.72` | `0.524` | `1.000` | `0.394` | `0.381` | `0.328` | `0.538` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `1411.24` | `0.483` | `1.000` | `0.611` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `1651.15` | `0.986` | `1.000` | `1.000` | `1.000` | `0.957` | `0.857` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `1192.52` | `0.800` | `1.000` | `0.601` | `0.800` | `0.800` | `1.000` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `2169.45` | `0.945` | `1.000` | `0.817` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `1030.73` | `0.405` | `1.000` | `0.183` | `0.125` | `0.125` | `1.000` | `accepted` | - | - | - |
| `playwright-02` | `structured` | `playwright` | `1754.31` | `0.357` | `1.000` | `0.190` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `1632.74` | `0.449` | `1.000` | `0.497` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `vite-01` | `structured` | `vite` | `2003.60` | `0.270` | `1.000` | `0.184` | `0.000` | `0.000` | `0.143` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `1021.71` | `1.000` | `1.000` | `0.998` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `1076.32` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `1366.15` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `816.93` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `911.47` | `0.234` | `1.000` | `0.335` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `906.44` | `0.230` | `1.000` | `0.304` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `1128.04` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `761.58` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `1032.60` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `978.89` | `0.966` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `1429.45` | `0.945` | `1.000` | `0.889` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `2036.67` | `0.956` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `2248.65` | `0.960` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `1317.83` | `0.968` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `4064.88` | `0.691` | `1.000` | `0.826` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `1035.88` | `0.911` | `1.000` | `0.822` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `890.85` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `982.31` | `0.986` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `11706.66` | `0.755` | `1.000` | `0.955` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `package-management-01` | `recall` | `package-management` | `1346.95` | `0.978` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `3763.92` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `1366.85` | `0.960` | `1.000` | `0.953` | `1.000` | `0.914` | `0.714` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `1184.98` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `1000.38` | `0.976` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `956.29` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `1264.05` | `0.981` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `1411.24` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `1128.27` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `1155.20` | `0.975` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `967.02` | `0.982` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `980.94` | `0.980` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `6119.98` | `0.989` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1161.18` | `0.969` | `1.000` | `0.874` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `851.87` | `0.991` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `1161.25` | `0.987` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `1009.10` | `0.966` | `1.000` | `0.865` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `1790.87` | `0.979` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `849.62` | `0.986` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `3635.09` | `0.833` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `981.61` | `0.976` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `1082.45` | `0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `840.39` | `0.945` | `1.000` | `0.862` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `1050.32` | `0.961` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `877.53` | `0.953` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `1082.17` | `0.881` | `1.000` | `0.953` | `1.000` | `0.800` | `0.333` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `1006.73` | `0.942` | `1.000` | `0.856` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `5435.06` | `0.781` | `1.000` | `0.936` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `1127.81` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `875.91` | `0.688` | `1.000` | `0.628` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `linting-02` | `structured` | `linting` | `1443.29` | `0.789` | `1.000` | `0.677` | `0.714` | `0.714` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `2300.85` | `0.579` | `1.000` | `0.957` | `0.000` | `0.000` | `0.923` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `1980.16` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `1077.58` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `1135.81` | `0.220` | `1.000` | `0.579` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `1136.15` | `0.252` | `1.000` | `0.765` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `1076.45` | `0.231` | `1.000` | `0.643` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `1448.15` | `0.483` | `1.000` | `0.497` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `build-05` | `exact_format` | `build` | `949.64` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `956.17` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `2264.33` | `0.953` | `1.000` | `0.919` | `1.000` | `0.979` | `0.929` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `4232.32` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `2431.17` | `0.974` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `2308.73` | `0.950` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `1950.92` | `0.908` | `1.000` | `0.893` | `1.000` | `0.883` | `0.611` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `1059.68` | `0.972` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `1215.91` | `0.939` | `1.000` | `0.877` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `2326.08` | `0.952` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1116.77` | `0.950` | `1.000` | `0.917` | `1.000` | `0.975` | `0.917` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `1805.35` | `0.943` | `1.000` | `0.925` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `1047.51` | `0.954` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `2660.93` | `0.912` | `1.000` | `0.913` | `1.000` | `0.867` | `0.556` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `1448.95` | `0.851` | `1.000` | `0.823` | `1.000` | `0.820` | `0.400` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `1003.67` | `0.949` | `1.000` | `0.898` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `4824.25` | `0.885` | `1.000` | `0.828` | `1.000` | `0.912` | `0.706` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `2124.31` | `0.960` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `2307.12` | `0.920` | `1.000` | `0.911` | `1.000` | `0.894` | `0.647` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `1803.68` | `0.930` | `1.000` | `0.917` | `1.000` | `0.914` | `0.714` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `1528.91` | `0.945` | `1.000` | `0.904` | `1.000` | `0.980` | `0.933` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `2447.73` | `0.579` | `1.000` | `0.957` | `0.000` | `0.000` | `0.923` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `1926.30` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `1654.47` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `1715.65` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `947.35` | `0.700` | `1.000` | `0.335` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `1091.59` | `0.483` | `1.000` | `0.497` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `1480.59` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `3352.15` | `0.250` | `1.000` | `0.938` | `0.000` | `0.000` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `shell-08` | `exact_format` | `shell` | `1594.46` | `0.232` | `1.000` | `0.653` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `2799.11` | `0.912` | `1.000` | `0.901` | `1.000` | `0.886` | `0.619` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `1045.77` | `0.936` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `2075.18` | `0.960` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `2418.79` | `0.638` | `0.000` | `0.901` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | cannot list resource "pods" | - |
| `explanation-14` | `explanation` | `explanation` | `2018.29` | `0.893` | `1.000` | `0.842` | `1.000` | `0.914` | `0.714` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `1232.68` | `0.915` | `1.000` | `0.906` | `1.000` | `0.885` | `0.615` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `1558.67` | `0.907` | `1.000` | `0.894` | `1.000` | `0.880` | `0.600` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `2295.49` | `0.893` | `1.000` | `0.907` | `1.000` | `0.820` | `0.400` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1929.58` | `0.942` | `1.000` | `0.885` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
