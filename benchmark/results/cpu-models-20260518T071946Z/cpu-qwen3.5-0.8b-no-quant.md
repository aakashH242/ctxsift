# cpu-qwen3.5-0.8b-no-quant

## Scenario

- track: `cpu`
- phase: `cpu-screen`
- model: `unsloth/Qwen3.5-0.8B-GGUF`
- quantization: `none`
- device: `cpu`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `65419.70`
- cpu_rss_bytes: `null`
- gpu_peak_bytes: `null`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `280`
- accepted_count: `230`
- soft_accepted_count: `50`
- rejected_count: `0`
- exact_pass_count: `242`
- avg_inference_ms: `8263.89`
- p95_inference_ms: `30541.39`
- avg_exact_preservation_ratio: `0.954`
- avg_summary_quality_ratio: `0.838`
- avg_format_adherence_score: `0.782`
- avg_instruction_following_score: `0.764`
- avg_brevity_ratio: `0.857`
- avg_case_score: `0.805`
- p10_case_score: `0.319`
- quality_core: `0.708`
- latency_factor: `0.850`
- final_score: `60.20`
- peak_cpu_rss_bytes: `null`
- peak_gpu_bytes: `null`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `36140.79` | `0.689` | `1.000` | `0.898` | `0.500` | `0.404` | `0.358` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-02` | `summary` | `python` | `9862.06` | `0.834` | `1.000` | `0.938` | `0.500` | `0.459` | `0.727` | `accepted` | - | - | - |
| `python-03` | `recall` | `python` | `4517.65` | `0.989` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `5634.19` | `0.989` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `3741.96` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `4001.60` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `9567.33` | `0.685` | `0.326` | `0.937` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/integration -k billing -vv --maxfail=1, tests/integration/test_billing_api.py::test_invoice_webhook_uses_signature, 1 error in 2.31s | - |
| `pytest-03` | `recall` | `pytest` | `20331.21` | `0.757` | `1.000` | `0.961` | `0.500` | `0.500` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `pytest-04` | `recall` | `pytest` | `4334.09` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `4170.96` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `3221.48` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `3740.19` | `0.979` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `6462.31` | `0.991` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `3600.22` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-02` | `summary` | `ruff` | `2311.68` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `2758.02` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `2796.30` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `3942.12` | `0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `3915.63` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `2916.31` | `0.989` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `3378.60` | `0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `2352.42` | `0.992` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `14215.96` | `0.940` | `1.000` | `0.923` | `1.000` | `0.877` | `0.590` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `16384.00` | `0.982` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `8525.99` | `0.785` | `0.800` | `0.934` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Lifecycle script `build` failed, storefront@2.8.1 | - |
| `pnpm-01` | `recall` | `pnpm` | `2683.45` | `0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `13450.02` | `0.979` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `11802.16` | `0.978` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `11141.08` | `0.980` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `4713.60` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `22511.65` | `0.699` | `1.000` | `0.956` | `0.500` | `0.440` | `0.603` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `eslint-01` | `recall` | `eslint` | `9804.67` | `0.809` | `0.920` | `0.950` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Unused eslint-disable directive | - |
| `eslint-02` | `summary` | `eslint` | `2965.79` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `4942.08` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `6879.66` | `0.984` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `3145.55` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `5232.66` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `1982.15` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `9774.22` | `0.795` | `0.875` | `0.968` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | demo-app-1 | - |
| `docker-compose-03` | `summary` | `docker-compose` | `8203.21` | `0.737` | `0.600` | `0.919` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker compose up api | - |
| `kubectl-01` | `summary` | `kubectl` | `3433.45` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `27209.26` | `0.909` | `1.000` | `0.947` | `1.000` | `0.767` | `0.222` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `2671.03` | `0.995` | `1.000` | `0.988` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `32597.63` | `0.916` | `1.000` | `0.926` | `1.000` | `0.803` | `0.342` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `9234.87` | `0.760` | `0.647` | `0.956` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform validate | - |
| `terraform-02` | `recall` | `terraform` | `19105.45` | `0.958` | `1.000` | `0.925` | `1.000` | `0.931` | `0.771` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `8760.96` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `5056.79` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `10467.47` | `0.956` | `1.000` | `0.931` | `1.000` | `0.921` | `0.735` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `12761.97` | `0.911` | `1.000` | `0.893` | `1.000` | `0.908` | `0.694` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `25320.53` | `0.694` | `1.000` | `0.907` | `0.500` | `0.411` | `0.404` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `git-02` | `recall` | `git` | `9657.34` | `0.906` | `1.000` | `0.868` | `1.000` | `0.816` | `0.386` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `5156.91` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `4827.27` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `9053.69` | `0.836` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `ssh-01` | `summary` | `ssh` | `4668.75` | `0.987` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `3108.14` | `0.980` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `8316.52` | `0.765` | `0.677` | `0.953` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | status=203/EXEC | - |
| `systemd-02` | `summary` | `systemd` | `4887.17` | `0.962` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `2957.61` | `0.977` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `12716.47` | `0.943` | `1.000` | `0.951` | `1.000` | `0.864` | `0.548` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `12114.64` | `0.770` | `0.750` | `0.921` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | example.com/mono-app/pkg/server | - |
| `go-test-01` | `summary` | `go-test` | `25030.43` | `0.914` | `1.000` | `0.936` | `1.000` | `0.880` | `0.600` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `48501.69` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `18921.99` | `0.594` | `0.304` | `0.931` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | mvn -q test, UserControllerTest.java:72, /workspace/webapp/target/surefire-reports | - |
| `maven-02` | `summary` | `maven` | `5092.05` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `5081.16` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `6295.24` | `0.696` | `0.389` | `0.930` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ./gradlew test, Execution failed for task ':test' | - |
| `cargo-01` | `summary` | `cargo` | `17969.02` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `4673.39` | `0.966` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `29683.75` | `0.612` | `0.737` | `0.936` | `0.500` | `0.432` | `0.548` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | node dist/server.js | - |
| `npm-04` | `summary` | `npm` | `7374.58` | `0.974` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `11606.48` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `6747.80` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `23505.70` | `0.675` | `1.000` | `0.940` | `0.500` | `0.418` | `0.455` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `pytest-06` | `summary` | `pytest` | `9677.56` | `0.986` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `6150.50` | `0.971` | `1.000` | `0.939` | `1.000` | `0.992` | `0.972` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `13878.94` | `0.800` | `0.911` | `0.910` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | zod@3.23.8 | - |
| `docker-compose-04` | `summary` | `docker-compose` | `8840.24` | `0.739` | `0.600` | `0.922` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker compose up --build | - |
| `kubectl-05` | `summary` | `kubectl` | `2356.57` | `0.982` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `37626.77` | `0.827` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `4630.01` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `6698.21` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `5101.24` | `0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `5773.45` | `0.979` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `6186.43` | `0.979` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `6558.09` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `6829.62` | `0.684` | `0.600` | `0.939` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | psql -h 127.0.0.1 -U app_user -d appdb -c 'select 1' | - |
| `postgres-02` | `summary` | `postgres` | `15844.51` | `0.963` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `3935.94` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `5978.97` | `0.732` | `0.667` | `0.861` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mysql -h db.example.net -u app -D appdb -e "SELECT id, createdAt FROM users LIMIT 5" | - |
| `redis-01` | `summary` | `redis` | `4593.24` | `0.986` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `2487.64` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `7403.97` | `0.643` | `0.524` | `0.883` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | line=91, Ruff F821, exit code 2 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `31068.79` | `0.861` | `1.000` | `0.933` | `1.000` | `0.775` | `0.250` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `2690.31` | `0.968` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `3802.26` | `0.979` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `7247.73` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `3573.12` | `0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `4196.73` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `15180.43` | `0.669` | `0.545` | `0.967` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | tests/unit/test_invoice_totals.py::test_discount_rounding, tests/unit/test_invoice_totals.py:88 | - |
| `compiler-error-01` | `recall` | `compiler-error` | `49401.81` | `0.634` | `0.851` | `0.904` | `0.500` | `0.405` | `0.369` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | src/router.rs:128 | - |
| `ci-log-01` | `recall` | `ci-log` | `14171.88` | `0.961` | `1.000` | `0.928` | `1.000` | `0.936` | `0.786` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `23439.03` | `0.912` | `1.000` | `0.955` | `1.000` | `0.771` | `0.236` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `23621.72` | `0.829` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `soft_accepted` | structured_output_mismatch | - | - |
| `build-log-01` | `summary` | `build-log` | `31565.06` | `0.662` | `1.000` | `0.895` | `0.500` | `0.422` | `0.477` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `docker-build-02` | `summary` | `docker-build` | `31789.90` | `0.639` | `1.000` | `0.883` | `0.000` | `0.000` | `0.240` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `23828.95` | `0.294` | `0.625` | `0.680` | `0.000` | `0.000` | `0.167` | `soft_accepted` | missing_exact_anchors | @typescript-eslint/no-misused-promises, @typescript-eslint/no-explicit-any, @typescript-eslint/no-unsafe-assignment | - |
| `git-review-01` | `instruction_following` | `git-review` | `18499.81` | `0.672` | `1.000` | `0.732` | `0.429` | `0.404` | `0.810` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `6314.91` | `0.515` | `1.000` | `0.717` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-01` | `structured` | `structured-output` | `13789.36` | `0.355` | `1.000` | `0.184` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `14225.09` | `0.438` | `0.905` | `0.853` | `0.000` | `0.000` | `0.781` | `soft_accepted` | missing_exact_anchors | port 5432 is already allocated | - |
| `structured-output-03` | `structured` | `structured-output` | `15153.76` | `0.375` | `0.929` | `0.518` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "refresh token expired" | - |
| `structured-output-04` | `structured` | `structured-output` | `8377.96` | `0.256` | `1.000` | `0.175` | `0.000` | `0.000` | `0.036` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `4416.02` | `0.234` | `1.000` | `0.343` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `5990.21` | `0.196` | `1.000` | `0.328` | `0.000` | `0.000` | `0.273` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `5806.77` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `3276.37` | `0.957` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `3223.41` | `0.945` | `1.000` | `0.891` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `7218.26` | `0.830` | `0.750` | `0.917` | `0.667` | `0.644` | `0.885` | `accepted` | - | customer_id | - |
| `python-traceback-01` | `recall` | `python-traceback` | `11867.62` | `0.980` | `1.000` | `0.943` | `1.000` | `0.981` | `0.938` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `14567.60` | `0.980` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `5876.60` | `0.984` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `9897.47` | `0.748` | `0.783` | `0.912` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | InventorySyncTest.java:132 | - |
| `kubernetes-01` | `recall` | `kubernetes` | `30513.63` | `0.742` | `0.800` | `0.910` | `1.000` | `0.957` | `0.857` | `soft_accepted` | missing_exact_anchors | registry.example.com/api:2026.05.18-1 | - |
| `go-test-02` | `recall` | `go-test` | `4274.49` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `4197.63` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `4973.50` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `10496.53` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `83272.81` | `0.608` | `0.571` | `0.945` | `1.000` | `0.764` | `0.213` | `soft_accepted` | missing_exact_anchors | packages/db migrate.test.ts, 20260518_add_workspace_limits.sql, exit code 1 | - |
| `pnpm-04` | `recall` | `pnpm` | `4667.89` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `3664.29` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `6471.92` | `0.982` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `7682.64` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `5726.19` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `3295.25` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `5044.24` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `15500.04` | `0.951` | `1.000` | `0.929` | `1.000` | `0.906` | `0.688` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `5370.34` | `0.975` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `3972.08` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `3606.19` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `4616.52` | `0.969` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `18120.37` | `0.753` | `0.684` | `0.911` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ./integration | - |
| `npm-05` | `summary` | `npm` | `13203.97` | `0.968` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `41213.34` | `0.853` | `1.000` | `0.904` | `1.000` | `0.782` | `0.274` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `6102.93` | `0.951` | `1.000` | `0.877` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `18774.79` | `0.966` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `6867.24` | `0.951` | `1.000` | `0.941` | `1.000` | `0.949` | `0.830` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `9836.73` | `0.965` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `8195.47` | `0.807` | `0.909` | `0.931` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | -Iinclude | - |
| `python-pytest-02` | `summary` | `python-pytest` | `6384.53` | `0.969` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `4557.45` | `0.962` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `8333.30` | `0.784` | `0.833` | `0.910` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `9151.98` | `0.785` | `0.814` | `0.926` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | FAILED | - |
| `wrangler-01` | `summary` | `wrangler` | `8071.58` | `0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `4680.05` | `0.970` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `11901.43` | `0.431` | `1.000` | `0.673` | `0.000` | `0.000` | `0.286` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `36891.44` | `0.584` | `1.000` | `0.919` | `0.022` | `0.022` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `2421.56` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `4105.36` | `0.739` | `1.000` | `0.716` | `0.667` | `0.581` | `0.571` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `2669.64` | `0.940` | `1.000` | `0.799` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `2961.79` | `0.682` | `1.000` | `0.739` | `0.400` | `0.400` | `1.000` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `5426.25` | `0.322` | `0.450` | `0.696` | `0.000` | `0.000` | `0.800` | `soft_accepted` | missing_exact_anchors | [deps 4/4], pnpm install --frozen-lockfile | - |
| `terraform-09` | `instruction_following` | `terraform` | `6101.17` | `0.546` | `0.667` | `0.696` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors | aws_db_instance.main | - |
| `maven-03` | `instruction_following` | `maven` | `4791.56` | `0.583` | `1.000` | `0.942` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `3261.46` | `0.526` | `1.000` | `0.754` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `2308.63` | `0.719` | `1.000` | `0.729` | `0.667` | `0.533` | `0.333` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `5080.27` | `0.399` | `0.833` | `0.677` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | migrator-9z1q | - |
| `cargo-04` | `instruction_following` | `cargo` | `7129.74` | `0.653` | `1.000` | `0.734` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `8101.22` | `0.487` | `1.000` | `0.780` | `0.000` | `0.000` | `0.529` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `9231.15` | `0.503` | `1.000` | `0.779` | `0.000` | `0.000` | `0.696` | `accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `16890.47` | `0.217` | `0.833` | `0.185` | `0.000` | `0.000` | `0.333` | `soft_accepted` | missing_exact_anchors | field | - |
| `junit-01` | `structured` | `junit` | `4764.38` | `0.354` | `1.000` | `0.180` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `7553.77` | `0.280` | `1.000` | `0.193` | `0.000` | `0.000` | `0.222` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `11406.46` | `0.268` | `1.000` | `0.182` | `0.000` | `0.000` | `0.135` | `accepted` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `4209.78` | `0.796` | `1.000` | `0.702` | `0.714` | `0.714` | `1.000` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `4873.35` | `0.562` | `1.000` | `0.900` | `0.000` | `0.000` | `0.917` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `4144.05` | `0.817` | `1.000` | `0.633` | `1.000` | `0.782` | `0.273` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `6819.90` | `0.679` | `1.000` | `0.594` | `0.714` | `0.533` | `0.154` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `34548.62` | `0.267` | `1.000` | `0.190` | `0.000` | `0.000` | `0.099` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `7487.26` | `0.288` | `1.000` | `0.298` | `0.000` | `0.000` | `0.500` | `soft_accepted` | structured_output_mismatch | - | - |
| `playwright-02` | `structured` | `playwright` | `78845.12` | `0.108` | `0.167` | `0.279` | `0.000` | `0.000` | `0.104` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | project, chromium, file, line, test | - |
| `postgres-04` | `structured` | `postgres` | `9088.20` | `0.403` | `1.000` | `0.578` | `0.000` | `0.000` | `0.294` | `accepted` | - | - | - |
| `vite-01` | `structured` | `vite` | `5306.82` | `0.258` | `1.000` | `0.182` | `0.000` | `0.000` | `0.034` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `2674.05` | `0.190` | `1.000` | `0.318` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `4150.41` | `0.182` | `1.000` | `0.282` | `0.000` | `0.000` | `0.071` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `3796.64` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `2088.76` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `3755.08` | `0.232` | `1.000` | `0.323` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `4529.88` | `0.220` | `1.000` | `0.303` | `0.000` | `0.000` | `0.800` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `2450.50` | `0.189` | `1.000` | `0.329` | `0.000` | `0.000` | `0.125` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `1256.11` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `4494.50` | `0.026` | `0.000` | `0.248` | `0.000` | `0.000` | `0.111` | `soft_accepted` | missing_exact_anchors | 20260518133742 | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `1832.58` | `0.939` | `1.000` | `0.878` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `4621.33` | `0.945` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `7256.13` | `0.745` | `1.000` | `0.890` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `3309.03` | `0.958` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `2085.25` | `0.954` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `7417.04` | `0.691` | `1.000` | `0.826` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `6327.74` | `0.715` | `0.583` | `0.848` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `1998.68` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `2206.78` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `6283.58` | `0.755` | `1.000` | `0.951` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `package-management-01` | `recall` | `package-management` | `5125.21` | `0.976` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `4512.28` | `0.719` | `0.667` | `0.983` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `6503.83` | `0.952` | `1.000` | `0.940` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `6227.82` | `0.964` | `1.000` | `0.924` | `1.000` | `0.950` | `0.833` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `3260.46` | `0.964` | `1.000` | `0.855` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `4546.37` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `4955.23` | `0.952` | `1.000` | `0.892` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `35843.25` | `0.892` | `1.000` | `0.903` | `1.000` | `0.747` | `0.158` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `1862.57` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `3988.65` | `0.966` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `6991.47` | `0.891` | `1.000` | `0.822` | `1.000` | `0.807` | `0.356` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `1326.71` | `0.979` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `3894.95` | `0.972` | `1.000` | `0.889` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1432.56` | `0.967` | `1.000` | `0.867` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `1257.92` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `1628.01` | `0.972` | `1.000` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `6101.05` | `0.936` | `1.000` | `0.906` | `1.000` | `0.877` | `0.591` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `10818.82` | `0.948` | `1.000` | `0.906` | `1.000` | `0.914` | `0.714` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `4467.05` | `0.614` | `0.500` | `0.930` | `1.000` | `0.894` | `0.647` | `soft_accepted` | missing_exact_anchors | foo.c:5:2 | - |
| `ci-03` | `recall` | `ci` | `9570.45` | `0.800` | `1.000` | `0.892` | `1.000` | `0.905` | `0.682` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `1325.10` | `0.976` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `3213.46` | `0.943` | `1.000` | `0.859` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `1204.07` | `0.945` | `1.000` | `0.862` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `1138.20` | `0.935` | `1.000` | `0.837` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `1468.33` | `0.953` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `1503.81` | `0.976` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `1172.10` | `0.937` | `1.000` | `0.842` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `2763.68` | `0.526` | `1.000` | `0.864` | `0.000` | `0.000` | `0.667` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `2026.76` | `0.922` | `1.000` | `0.738` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `2201.05` | `0.688` | `1.000` | `0.627` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `linting-02` | `structured` | `linting` | `2174.77` | `0.638` | `1.000` | `0.349` | `0.583` | `0.583` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `3406.50` | `0.358` | `1.000` | `0.195` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `1762.70` | `0.500` | `1.000` | `0.666` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `3392.61` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `2135.95` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `1909.90` | `0.252` | `1.000` | `0.765` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `1673.36` | `0.207` | `1.000` | `0.491` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `5665.85` | `0.279` | `1.000` | `0.905` | `0.000` | `0.000` | `0.778` | `accepted` | - | - | - |
| `build-05` | `exact_format` | `build` | `1896.66` | `0.225` | `1.000` | `0.609` | `0.000` | `0.000` | `0.286` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `1479.40` | `0.232` | `1.000` | `0.658` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `1282.83` | `0.935` | `1.000` | `0.870` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `1269.03` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `2226.09` | `0.946` | `1.000` | `0.893` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `1260.14` | `0.950` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `4784.04` | `0.903` | `1.000` | `0.877` | `1.000` | `0.894` | `0.647` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `1157.91` | `0.932` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `1522.03` | `0.931` | `1.000` | `0.861` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `1256.69` | `0.930` | `1.000` | `0.860` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1081.82` | `0.913` | `1.000` | `0.826` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `1197.47` | `0.943` | `1.000` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `1344.56` | `0.938` | `1.000` | `0.875` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `2904.77` | `0.947` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `1669.27` | `0.908` | `1.000` | `0.816` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `1322.09` | `0.932` | `1.000` | `0.864` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `1181.64` | `0.920` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `1043.13` | `0.902` | `1.000` | `0.805` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `1160.92` | `0.948` | `1.000` | `0.896` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `1158.72` | `0.916` | `1.000` | `0.832` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `1122.62` | `0.875` | `1.000` | `0.750` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `3585.11` | `0.358` | `1.000` | `0.195` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `1805.95` | `0.500` | `1.000` | `0.666` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `3459.26` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `1473.99` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `7637.85` | `0.700` | `1.000` | `0.335` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `6535.29` | `0.279` | `1.000` | `0.905` | `0.000` | `0.000` | `0.778` | `accepted` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `1590.83` | `0.207` | `1.000` | `0.324` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `1420.13` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `1190.72` | `0.232` | `1.000` | `0.653` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `1072.05` | `0.935` | `1.000` | `0.870` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `1250.10` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `1225.27` | `0.959` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `4622.87` | `0.970` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `1392.85` | `0.931` | `1.000` | `0.861` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `1196.70` | `0.960` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `1069.54` | `0.913` | `1.000` | `0.826` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `1191.61` | `0.928` | `1.000` | `0.856` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1447.42` | `0.932` | `1.000` | `0.864` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
