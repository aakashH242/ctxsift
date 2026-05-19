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

- load_ms: `1658.32`
- cpu_rss_bytes: `1932234752`
- gpu_peak_bytes: `1234713600`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `280`
- accepted_count: `269`
- soft_accepted_count: `11`
- rejected_count: `0`
- exact_pass_count: `274`
- avg_inference_ms: `1783.42`
- p95_inference_ms: `3729.25`
- avg_exact_preservation_ratio: `0.997`
- avg_summary_quality_ratio: `0.898`
- avg_format_adherence_score: `0.878`
- avg_instruction_following_score: `0.872`
- avg_brevity_ratio: `0.958`
- avg_case_score: `0.902`
- p10_case_score: `0.576`
- quality_core: `0.837`
- latency_factor: `1.000`
- final_score: `83.67`
- peak_cpu_rss_bytes: `1932345344`
- peak_gpu_bytes: `1234713600`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `1486.58` | `0.997` | `1.000` | `0.987` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-02` | `summary` | `python` | `2820.06` | `0.750` | `1.000` | `0.957` | `0.500` | `0.500` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `python-03` | `recall` | `python` | `2750.20` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `1310.11` | `0.998` | `1.000` | `0.990` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `1199.45` | `0.997` | `1.000` | `0.987` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `1995.07` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `1575.13` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `4142.02` | `0.824` | `1.000` | `0.951` | `1.000` | `0.946` | `0.821` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `pytest-04` | `recall` | `pytest` | `1143.76` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `1153.24` | `0.990` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `1297.41` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `2463.86` | `0.820` | `0.895` | `0.979` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | checked 37 source files | - |
| `mypy-03` | `recall` | `mypy` | `1480.23` | `0.993` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `1252.76` | `0.981` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-02` | `summary` | `ruff` | `1184.70` | `0.997` | `1.000` | `0.993` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `915.92` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `1176.36` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `1226.62` | `0.981` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `1414.84` | `0.989` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `1352.75` | `0.995` | `1.000` | `0.988` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `1015.43` | `0.985` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `1202.84` | `0.994` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `1718.14` | `0.993` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `811.71` | `0.993` | `1.000` | `0.983` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `1688.27` | `0.980` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `1792.82` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `2125.54` | `0.997` | `1.000` | `0.993` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `1214.37` | `0.994` | `1.000` | `0.985` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `1294.77` | `0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `1440.44` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `3258.51` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-01` | `recall` | `eslint` | `1763.73` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `2631.04` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `1596.78` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `1841.13` | `0.996` | `1.000` | `0.983` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `1119.63` | `0.982` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `1326.11` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `884.07` | `0.995` | `1.000` | `0.988` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `1027.30` | `0.996` | `1.000` | `0.985` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `3253.23` | `0.963` | `1.000` | `0.952` | `1.000` | `0.965` | `0.882` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `1220.92` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `1260.91` | `0.994` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `3099.93` | `0.980` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `1670.50` | `0.978` | `1.000` | `0.913` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `1588.50` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `1721.57` | `0.997` | `1.000` | `0.990` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `1152.05` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `4108.81` | `0.819` | `0.902` | `0.970` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | expected t3.small default | - |
| `mixed-01` | `recall` | `mixed` | `1077.07` | `0.995` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `1201.18` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `884.52` | `0.979` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `1304.29` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `1264.25` | `0.995` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `2179.97` | `0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `2195.57` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-01` | `summary` | `ssh` | `1737.96` | `0.996` | `1.000` | `0.991` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `1696.63` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `1120.14` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `2896.90` | `0.972` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `3579.91` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `4418.21` | `0.953` | `1.000` | `0.914` | `1.000` | `0.923` | `0.742` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `1460.78` | `0.982` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `2677.44` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `1112.07` | `0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `1193.25` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-02` | `summary` | `maven` | `4057.03` | `0.986` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `1869.16` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `1766.35` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `1629.96` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `2701.43` | `0.990` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `1724.61` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-04` | `summary` | `npm` | `1841.50` | `0.991` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `3524.10` | `0.992` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `1439.98` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `2508.73` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `1379.91` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `3299.90` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `1427.68` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `1056.52` | `0.987` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `1318.26` | `0.987` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `6468.25` | `0.827` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `1460.60` | `0.996` | `1.000` | `0.985` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `3155.62` | `0.996` | `1.000` | `0.983` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `1106.64` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `1137.25` | `0.991` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `1626.08` | `0.990` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `830.66` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `1186.86` | `0.998` | `1.000` | `0.990` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `842.36` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `1668.90` | `0.992` | `1.000` | `0.980` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `2092.12` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `1722.64` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `2061.39` | `0.998` | `1.000` | `0.991` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `4806.48` | `0.879` | `1.000` | `0.916` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `3803.35` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `1423.78` | `0.967` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `1178.65` | `0.986` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `2126.83` | `0.964` | `1.000` | `0.911` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `1003.21` | `0.995` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `1317.73` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `3233.18` | `0.999` | `1.000` | `0.995` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `1266.68` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-log-01` | `recall` | `ci-log` | `1281.91` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `1898.17` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `2048.32` | `0.874` | `1.000` | `0.934` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `build-log-01` | `summary` | `build-log` | `2722.75` | `0.960` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `921.95` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `1278.30` | `0.758` | `1.000` | `0.993` | `0.400` | `0.400` | `1.000` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `1341.82` | `0.946` | `1.000` | `0.821` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `1620.75` | `0.915` | `1.000` | `0.717` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-01` | `structured` | `structured-output` | `2633.85` | `0.590` | `1.000` | `0.977` | `0.000` | `0.000` | `0.967` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `1440.66` | `0.505` | `1.000` | `0.684` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-03` | `structured` | `structured-output` | `3003.04` | `0.989` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-04` | `structured` | `structured-output` | `3570.67` | `0.369` | `1.000` | `0.229` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `2077.92` | `0.189` | `1.000` | `0.336` | `0.000` | `0.000` | `0.100` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `2534.82` | `0.187` | `1.000` | `0.320` | `0.000` | `0.000` | `0.107` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `1333.77` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `2864.77` | `0.958` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `2306.76` | `0.942` | `1.000` | `0.883` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `1345.76` | `0.905` | `1.000` | `0.943` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `2561.35` | `0.807` | `0.905` | `0.967` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | retries exhausted for queue emails | - |
| `mypy-05` | `recall` | `mypy` | `1037.48` | `0.986` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `4620.66` | `0.751` | `0.762` | `0.961` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | status code: 409 | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `1204.61` | `0.981` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `1482.98` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `1606.52` | `0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `2411.52` | `0.803` | `0.897` | `0.962` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | could not compile `storage` | - |
| `docker-compose-05` | `recall` | `docker-compose` | `2079.16` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `3965.41` | `0.984` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `1282.00` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `1442.82` | `0.997` | `1.000` | `0.987` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `1164.83` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `1114.90` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `1319.80` | `0.993` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `1498.28` | `0.994` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `1083.96` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `1324.42` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `1073.57` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `2737.88` | `0.985` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `1434.99` | `0.990` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `1068.63` | `0.996` | `1.000` | `0.983` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `1805.82` | `0.972` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `3246.61` | `0.968` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `2911.27` | `0.963` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `1715.41` | `0.972` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `1968.44` | `0.950` | `1.000` | `0.875` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `4377.62` | `0.965` | `1.000` | `0.911` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `3015.15` | `0.982` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `3690.52` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `2358.13` | `0.976` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `3483.48` | `0.958` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `1843.08` | `0.956` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `3283.35` | `0.977` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `2716.46` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `3027.61` | `0.967` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `2996.94` | `0.982` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `882.02` | `1.000` | `1.000` | `0.998` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `893.78` | `0.919` | `1.000` | `0.729` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `935.68` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `1134.07` | `0.938` | `1.000` | `0.795` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `967.37` | `0.919` | `1.000` | `0.730` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `2524.00` | `0.810` | `1.000` | `0.901` | `0.600` | `0.600` | `1.000` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `1134.31` | `0.523` | `1.000` | `0.742` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `2046.43` | `0.917` | `1.000` | `0.725` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `2384.01` | `0.986` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `2034.62` | `0.713` | `1.000` | `0.711` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `895.55` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `1128.28` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `2714.33` | `0.952` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `1193.14` | `0.541` | `1.000` | `0.802` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `1565.74` | `0.546` | `1.000` | `0.856` | `0.000` | `0.000` | `0.889` | `accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `3273.40` | `0.427` | `1.000` | `0.634` | `0.000` | `0.000` | `0.368` | `accepted` | - | - | - |
| `junit-01` | `structured` | `junit` | `3106.25` | `0.877` | `1.000` | `0.589` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `1007.68` | `0.446` | `1.000` | `0.485` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `1489.46` | `0.358` | `1.000` | `0.340` | `0.000` | `0.000` | `0.556` | `accepted` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `1136.83` | `0.510` | `1.000` | `0.699` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `1013.66` | `0.483` | `1.000` | `0.611` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `1321.21` | `0.986` | `1.000` | `1.000` | `1.000` | `0.957` | `0.857` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `1331.68` | `0.371` | `1.000` | `0.236` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `1601.20` | `0.968` | `1.000` | `0.910` | `1.000` | `0.984` | `0.947` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `1257.63` | `0.409` | `1.000` | `0.363` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `playwright-02` | `structured` | `playwright` | `6313.51` | `0.493` | `1.000` | `0.762` | `0.000` | `0.000` | `0.645` | `accepted` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `1606.91` | `0.449` | `1.000` | `0.497` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `vite-01` | `structured` | `vite` | `1918.14` | `0.269` | `1.000` | `0.216` | `0.000` | `0.000` | `0.043` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `1024.78` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `935.79` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `879.36` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `836.09` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `1893.43` | `0.197` | `1.000` | `0.322` | `0.000` | `0.000` | `0.300` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `866.56` | `0.230` | `1.000` | `0.304` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `815.93` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `1025.47` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `709.14` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `966.37` | `0.949` | `1.000` | `0.898` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `2540.73` | `0.930` | `1.000` | `0.860` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `1150.14` | `0.942` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `1010.22` | `0.961` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `896.13` | `0.969` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `1868.53` | `0.738` | `0.750` | `0.837` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | returns a reference | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `1888.17` | `0.948` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `831.15` | `0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `923.89` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `1870.00` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `862.19` | `0.980` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `1275.78` | `0.982` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `1011.10` | `0.991` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `1387.14` | `0.986` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `768.96` | `0.976` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `969.42` | `0.960` | `1.000` | `0.840` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `939.30` | `0.982` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `675.96` | `0.994` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `927.44` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `678.56` | `0.975` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `1372.22` | `0.984` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `1116.75` | `0.978` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `1507.26` | `0.984` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1241.59` | `0.970` | `1.000` | `0.880` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `761.95` | `0.995` | `1.000` | `0.981` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `792.00` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `926.31` | `0.981` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `1062.69` | `0.986` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `1134.86` | `0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `2068.29` | `0.839` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `930.77` | `0.981` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `1328.01` | `0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `1896.98` | `0.945` | `1.000` | `0.862` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `1033.87` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `734.89` | `0.954` | `1.000` | `0.885` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `1815.26` | `0.879` | `1.000` | `0.933` | `1.000` | `0.812` | `0.375` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `3726.32` | `0.951` | `1.000` | `0.877` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `3784.93` | `0.478` | `1.000` | `0.811` | `0.000` | `0.000` | `0.345` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `919.82` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `1497.81` | `0.674` | `1.000` | `0.829` | `0.500` | `0.387` | `0.250` | `accepted` | - | - | - |
| `linting-02` | `structured` | `linting` | `2411.75` | `0.508` | `1.000` | `0.718` | `0.000` | `0.000` | `0.923` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `1773.06` | `0.579` | `1.000` | `0.957` | `0.000` | `0.000` | `0.923` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `793.09` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `789.61` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `841.36` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `816.70` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `889.62` | `0.232` | `1.000` | `0.320` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `7011.67` | `0.483` | `1.000` | `0.497` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `build-05` | `exact_format` | `build` | `624.87` | `0.233` | `1.000` | `0.333` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `870.13` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `896.37` | `0.934` | `1.000` | `0.895` | `1.000` | `0.960` | `0.867` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `2485.42` | `0.944` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `2077.65` | `0.957` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `2717.09` | `0.957` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `7832.56` | `0.970` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `1670.20` | `0.952` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `2300.26` | `0.955` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `1233.60` | `0.958` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1986.52` | `0.920` | `1.000` | `0.912` | `1.000` | `0.894` | `0.647` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `2198.20` | `0.975` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `1943.88` | `0.952` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `954.54` | `0.921` | `1.000` | `0.906` | `1.000` | `0.905` | `0.682` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `1677.48` | `0.875` | `1.000` | `0.836` | `1.000` | `0.871` | `0.571` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `2902.26` | `0.937` | `1.000` | `0.899` | `1.000` | `0.962` | `0.875` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `1265.48` | `0.896` | `1.000` | `0.867` | `1.000` | `0.889` | `0.632` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `1836.93` | `0.953` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `1717.07` | `0.955` | `1.000` | `0.911` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `901.30` | `0.916` | `1.000` | `0.908` | `1.000` | `0.887` | `0.625` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `1126.41` | `0.932` | `1.000` | `0.899` | `1.000` | `0.947` | `0.824` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `1171.94` | `0.579` | `1.000` | `0.957` | `0.000` | `0.000` | `0.923` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `935.60` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `676.05` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `625.21` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `640.99` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `1833.97` | `0.483` | `1.000` | `0.497` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `1058.67` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `2246.55` | `0.250` | `1.000` | `0.938` | `0.000` | `0.000` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `shell-08` | `exact_format` | `shell` | `962.14` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `1689.72` | `0.934` | `1.000` | `0.895` | `1.000` | `0.960` | `0.867` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `1751.46` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `1709.08` | `0.960` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `2575.79` | `0.972` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `989.10` | `0.899` | `1.000` | `0.880` | `1.000` | `0.876` | `0.588` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `1660.21` | `0.913` | `1.000` | `0.897` | `1.000` | `0.892` | `0.640` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `844.91` | `0.965` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `828.20` | `0.897` | `1.000` | `0.882` | `1.000` | `0.867` | `0.556` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `2306.30` | `0.948` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
