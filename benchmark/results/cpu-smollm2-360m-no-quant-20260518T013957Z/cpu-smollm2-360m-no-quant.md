# cpu-smollm2-360m-no-quant

## Scenario

- track: `cpu`
- phase: `cpu-screen`
- model: `unsloth/SmolLM2-360M-Instruct-GGUF`
- quantization: `none`
- device: `cpu`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `6990.09`
- cpu_rss_bytes: `null`
- gpu_peak_bytes: `null`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `275`
- accepted_count: `209`
- soft_accepted_count: `66`
- rejected_count: `5`
- exact_pass_count: `242`
- avg_inference_ms: `9722.50`
- p95_inference_ms: `31449.01`
- avg_exact_preservation_ratio: `0.932`
- avg_summary_quality_ratio: `0.164`
- avg_format_adherence_score: `0.708`
- avg_instruction_following_score: `0.666`
- avg_brevity_ratio: `0.715`
- avg_case_score: `0.531`
- p10_case_score: `0.205`
- quality_core: `0.466`
- latency_factor: `0.850`
- final_score: `39.61`
- peak_cpu_rss_bytes: `null`
- peak_gpu_bytes: `null`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `33945.74` | `0.504` | `1.000` | `0.027` | `0.500` | `0.404` | `0.358` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-02` | `summary` | `python` | `14906.61` | `0.459` | `1.000` | `0.000` | `0.500` | `0.459` | `0.727` | `accepted` | - | - | - |
| `python-03` | `recall` | `python` | `31291.66` | `0.499` | `1.000` | `0.025` | `0.500` | `0.397` | `0.311` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-04` | `recall` | `python` | `24771.70` | `0.670` | `1.000` | `0.000` | `1.000` | `0.760` | `0.200` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `23955.99` | `0.517` | `1.000` | `0.039` | `0.500` | `0.423` | `0.489` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `pytest-01` | `recall` | `pytest` | `14542.84` | `0.713` | `1.000` | `0.080` | `1.000` | `0.830` | `0.435` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `20925.74` | `0.319` | `0.488` | `0.028` | `1.000` | `0.784` | `0.279` | `soft_accepted` | missing_exact_anchors | pytest tests/integration -k billing -vv --maxfail=1, /workspace/tests/integration/test_billing_api.py:73 | - |
| `pytest-03` | `recall` | `pytest` | `44047.81` | `0.583` | `1.000` | `0.041` | `1.000` | `0.776` | `0.253` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `pytest-04` | `recall` | `pytest` | `5970.76` | `0.745` | `1.000` | `0.000` | `1.000` | `0.986` | `0.952` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `24537.79` | `0.342` | `1.000` | `0.000` | `0.500` | `0.403` | `0.353` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `mypy-01` | `recall` | `mypy` | `6210.48` | `0.875` | `1.000` | `0.500` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `9764.31` | `0.687` | `1.000` | `0.344` | `1.000` | `0.898` | `0.660` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `6836.35` | `0.868` | `1.000` | `0.474` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `6279.14` | `0.539` | `0.911` | `0.091` | `1.000` | `0.850` | `0.500` | `accepted` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `1210.79` | `0.760` | `1.000` | `0.400` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `3598.77` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `3916.09` | `0.825` | `1.000` | `0.300` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `5359.31` | `0.744` | `1.000` | `0.000` | `1.000` | `0.981` | `0.935` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `7168.92` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `3138.83` | `0.760` | `1.000` | `0.400` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `5794.52` | `0.647` | `1.000` | `0.118` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `2012.95` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `7710.55` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `21489.03` | `0.550` | `1.000` | `0.101` | `1.000` | `0.819` | `0.398` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `39129.77` | `0.507` | `0.818` | `0.267` | `1.000` | `0.871` | `0.571` | `soft_accepted` | missing_exact_anchors | src/routes/checkout/index.tsx | - |
| `pnpm-01` | `recall` | `pnpm` | `20927.69` | `0.710` | `1.000` | `0.127` | `1.000` | `0.786` | `0.286` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `21997.32` | `0.491` | `0.909` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 5.51.1 | - |
| `pnpm-03` | `summary` | `pnpm` | `45180.55` | `0.529` | `1.000` | `0.042` | `1.000` | `0.825` | `0.417` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `3600.36` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `12703.34` | `0.609` | `0.895` | `0.203` | `1.000` | `0.889` | `0.630` | `soft_accepted` | missing_exact_anchors | Watching for file changes | - |
| `typescript-03` | `summary` | `typescript` | `17983.69` | `0.398` | `1.000` | `0.071` | `0.500` | `0.440` | `0.603` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `eslint-01` | `recall` | `eslint` | `5499.14` | `0.787` | `1.000` | `0.233` | `1.000` | `0.936` | `0.788` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `11180.62` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `5275.70` | `0.847` | `1.000` | `0.389` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `19237.51` | `0.684` | `1.000` | `0.055` | `1.000` | `0.760` | `0.201` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `1237.04` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `17814.89` | `0.500` | `1.000` | `0.037` | `1.000` | `0.772` | `0.238` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `2492.43` | `0.714` | `1.000` | `0.286` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `16864.20` | `0.687` | `1.000` | `0.065` | `1.000` | `0.763` | `0.209` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `4468.91` | `0.646` | `1.000` | `0.186` | `1.000` | `0.943` | `0.811` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `5994.15` | `0.569` | `1.000` | `0.108` | `1.000` | `0.852` | `0.508` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `58425.03` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | multimodal_leakage | kubectl describe pod api-7d9f7bbd8c-rx2kq -n staging, api-7d9f7bbd8c-rx2kq, ghcr.io/acme/api:2026.05.15-3, ImagePullBackOff, ErrImagePull | fallback output validation failed. first_pass_status=rejected first_pass_flags=['multimodal_leakage'] first_pass='kubectl describe pod api-7d9f7bbd8c-rx2kq -n staging Name: api-7d9f7bbd8c-rx2kq Namespace: staging Priority: 0 Service Account: default Node: worker-2/10.0.3...' repair_status=rejected repair_flags=['multimodal_leakage'] repair_pass='kubectl describe pod api-7d9f7bbd8c-rx2kq -n staging Name: api-7d9f7bbd8c-rx2kq Namespace: staging Priority: 0 Service Account: default Node: worker-2/10.0.3...' |
| `kubectl-03` | `summary` | `kubectl` | `4778.97` | `0.867` | `1.000` | `0.667` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `31816.16` | `0.512` | `1.000` | `0.085` | `0.500` | `0.396` | `0.310` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `terraform-01` | `summary` | `terraform` | `4180.32` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `6865.71` | `0.792` | `1.000` | `0.261` | `1.000` | `0.931` | `0.771` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `3461.29` | `0.872` | `1.000` | `0.486` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `5964.13` | `0.642` | `1.000` | `0.105` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `5412.68` | `0.729` | `1.000` | `0.078` | `1.000` | `0.879` | `0.595` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `11655.18` | `0.425` | `0.676` | `0.068` | `1.000` | `0.908` | `0.694` | `soft_accepted` | missing_exact_anchors | make integration | - |
| `git-01` | `recall` | `git` | `25493.09` | `0.542` | `1.000` | `0.183` | `0.500` | `0.412` | `0.417` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `git-02` | `recall` | `git` | `6301.40` | `0.708` | `1.000` | `0.056` | `1.000` | `0.833` | `0.443` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `23606.59` | `0.696` | `1.000` | `0.086` | `1.000` | `0.774` | `0.248` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `11050.88` | `0.682` | `1.000` | `0.020` | `1.000` | `0.782` | `0.272` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `18876.80` | `0.550` | `1.000` | `0.118` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `ssh-01` | `summary` | `ssh` | `9757.03` | `0.618` | `1.000` | `0.098` | `1.000` | `0.957` | `0.857` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `7753.27` | `0.708` | `1.000` | `0.269` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `18446.00` | `0.501` | `0.774` | `0.115` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Exec format error | - |
| `systemd-02` | `summary` | `systemd` | `23793.15` | `0.536` | `1.000` | `0.114` | `1.000` | `0.781` | `0.269` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `10045.16` | `0.539` | `1.000` | `0.064` | `1.000` | `0.827` | `0.422` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `57001.32` | `0.678` | `1.000` | `0.052` | `1.000` | `0.747` | `0.155` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `12514.72` | `0.494` | `0.750` | `0.108` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | example.com/mono-app/pkg/server | - |
| `go-test-01` | `summary` | `go-test` | `18381.98` | `0.560` | `1.000` | `0.055` | `1.000` | `0.877` | `0.590` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `55485.47` | `0.396` | `0.867` | `0.022` | `1.000` | `0.780` | `0.267` | `soft_accepted` | missing_exact_anchors | cannot find symbol | - |
| `maven-01` | `summary` | `maven` | `44977.75` | `0.355` | `1.000` | `0.075` | `0.500` | `0.388` | `0.253` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `maven-02` | `summary` | `maven` | `41182.10` | `0.451` | `0.636` | `0.118` | `1.000` | `0.949` | `0.829` | `soft_accepted` | missing_exact_anchors | mvn -U -DskipTests package | - |
| `gradle-01` | `recall` | `gradle` | `13906.37` | `0.692` | `1.000` | `0.077` | `1.000` | `0.767` | `0.224` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `26685.00` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `27221.31` | `0.484` | `1.000` | `0.000` | `1.000` | `0.768` | `0.227` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `5736.77` | `0.673` | `1.000` | `0.182` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `69091.37` | `0.391` | `0.526` | `0.000` | `1.000` | `0.768` | `0.228` | `soft_accepted` | missing_exact_anchors | MODULE_NOT_FOUND, /workspace/dist/config/index.js:4:18 | - |
| `npm-04` | `summary` | `npm` | `18100.24` | `0.517` | `1.000` | `0.061` | `1.000` | `0.784` | `0.281` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `5495.68` | `0.687` | `1.000` | `0.217` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `20715.69` | `0.539` | `1.000` | `0.070` | `1.000` | `0.823` | `0.410` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `19807.97` | `0.386` | `1.000` | `0.063` | `0.500` | `0.429` | `0.526` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `pytest-06` | `summary` | `pytest` | `16078.17` | `0.545` | `1.000` | `0.083` | `1.000` | `0.824` | `0.412` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `7595.31` | `0.698` | `1.000` | `0.255` | `1.000` | `0.992` | `0.972` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `48249.05` | `0.509` | `1.000` | `0.047` | `1.000` | `0.780` | `0.266` | `accepted` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `12367.53` | `0.568` | `1.000` | `0.130` | `1.000` | `0.833` | `0.443` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `4439.40` | `0.720` | `1.000` | `0.300` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `53391.28` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | multimodal_leakage | kubectl describe pod web-7f6f6d9d7b-kj4t2 -n dev, migrate, CrashLoopBackOff, Exit Code:    1 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['multimodal_leakage'] first_pass='kubectl describe pod web-7f6f6d9d7b-kj4t2 -n dev Name: web-7f6f6d9d7b-kj4t2 Namespace: dev Priority: 0 Service Account: default Node: worker-01/10.0.0.21 Sta...' repair_status=rejected repair_flags=['multimodal_leakage'] repair_pass='kubectl describe pod web-7f6f6d9d7b-kj4t2 -n dev Name: web-7f6f6d9d7b-kj4t2 Namespace: dev Priority: 0 Service Account: default Node: worker-01/10.0.0.21 Sta...' |
| `kubectl-07` | `recall` | `kubectl` | `3589.59` | `0.776` | `1.000` | `0.105` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `9627.95` | `0.697` | `1.000` | `0.055` | `1.000` | `0.799` | `0.328` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `5469.66` | `0.629` | `1.000` | `0.071` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `21337.98` | `0.504` | `1.000` | `0.000` | `1.000` | `0.807` | `0.358` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `3279.14` | `0.700` | `1.000` | `0.250` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `4738.93` | `0.662` | `1.000` | `0.154` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `3710.56` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `7050.48` | `0.623` | `1.000` | `0.057` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `2729.53` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `4385.76` | `0.392` | `0.444` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERROR 1054 (42S22), line 1 | - |
| `redis-01` | `summary` | `redis` | `3832.59` | `0.637` | `1.000` | `0.167` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `8930.03` | `0.510` | `0.667` | `0.000` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | LOADING | - |
| `github-actions-01` | `recall` | `github-actions` | `7271.21` | `0.730` | `1.000` | `0.097` | `1.000` | `0.868` | `0.560` | `accepted` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `21630.78` | `0.548` | `1.000` | `0.027` | `1.000` | `0.874` | `0.581` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `7568.19` | `0.623` | `1.000` | `0.057` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `7511.62` | `0.579` | `1.000` | `0.065` | `1.000` | `0.906` | `0.686` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `7196.45` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `8430.09` | `0.684` | `1.000` | `0.000` | `1.000` | `0.802` | `0.339` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `8704.41` | `0.559` | `1.000` | `0.037` | `1.000` | `0.887` | `0.625` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `22452.54` | `0.712` | `1.000` | `0.032` | `1.000` | `0.861` | `0.536` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `11096.73` | `0.388` | `0.254` | `0.171` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/router.rs:137:42, src/router.rs:128, req.into_body(), req.method(), req.clone().into_body() | - |
| `ci-log-01` | `recall` | `ci-log` | `32026.87` | `0.707` | `1.000` | `0.065` | `1.000` | `0.821` | `0.404` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `7387.94` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `14552.32` | `0.514` | `1.000` | `0.035` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `build-log-01` | `summary` | `build-log` | `46850.53` | `0.397` | `1.000` | `0.102` | `0.500` | `0.426` | `0.506` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `docker-build-02` | `summary` | `docker-build` | `19998.92` | `0.326` | `1.000` | `0.101` | `0.000` | `0.000` | `0.240` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `10803.64` | `0.212` | `1.000` | `0.000` | `0.000` | `0.000` | `0.118` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `15646.81` | `0.273` | `1.000` | `0.093` | `0.000` | `0.000` | `0.447` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `8960.05` | `0.297` | `1.000` | `0.089` | `0.000` | `0.000` | `0.703` | `accepted` | - | - | - |
| `structured-output-01` | `structured` | `structured-output` | `15612.72` | `0.387` | `1.000` | `0.609` | `0.000` | `0.000` | `0.725` | `soft_accepted` | structured_output_mismatch | - | - |
| `structured-output-02` | `structured` | `structured-output` | `18769.39` | `0.279` | `0.905` | `0.360` | `0.000` | `0.000` | `0.391` | `soft_accepted` | missing_exact_anchors | port 5432 is already allocated | - |
| `structured-output-03` | `structured` | `structured-output` | `12279.84` | `0.270` | `1.000` | `0.160` | `0.000` | `0.000` | `0.220` | `accepted` | - | - | - |
| `structured-output-04` | `structured` | `structured-output` | `19898.28` | `0.171` | `1.000` | `0.000` | `0.000` | `0.000` | `0.014` | `soft_accepted` | structured_output_mismatch | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `21239.70` | `0.129` | `1.000` | `0.000` | `0.000` | `0.000` | `0.045` | `soft_accepted` | structured_output_mismatch | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `26192.28` | `0.093` | `0.714` | `0.000` | `0.000` | `0.000` | `0.055` | `soft_accepted` | missing_exact_anchors | SearchBox debounces network query before fetch | - |
| `exact-format-03` | `exact_format` | `exact-format` | `11906.23` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `8618.15` | `0.432` | `0.778` | `0.305` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `24804.96` | `0.430` | `1.000` | `0.000` | `1.000` | `0.791` | `0.304` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `6745.58` | `0.429` | `1.000` | `0.257` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `9308.76` | `0.746` | `1.000` | `0.118` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `6518.38` | `0.780` | `1.000` | `0.120` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `12992.94` | `0.801` | `1.000` | `0.205` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `10314.21` | `0.627` | `1.000` | `0.353` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `18329.08` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | multimodal_leakage | api-7d9f8c8b99-mx2kq, registry.example.com/api:2026.05.18-1, CrashLoopBackOff, Exit Code: 78, STRIPE_KEY, FATAL config: required env STRIPE_KEY is empty | fallback output validation failed. first_pass_status=rejected first_pass_flags=['multimodal_leakage'] first_pass='$ kubectl describe pod api-7d9f8c8b99-mx2kq -n prod Containers: api: Image: registry.example.com/api:2026.05.18-1 State: Waiting Reason: CrashLoopBackOff Las...' repair_status=rejected repair_flags=['multimodal_leakage'] repair_pass='$ kubectl describe pod api-7d9f8c8b99-mx2kq -n prod Containers: api: Image: registry.example.com/api:2026.05.18-1 State: Waiting Reason: CrashLoopBackOff Las...' |
| `go-test-02` | `recall` | `go-test` | `9568.04` | `0.778` | `1.000` | `0.163` | `1.000` | `0.962` | `0.872` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `10801.02` | `0.785` | `1.000` | `0.151` | `1.000` | `0.992` | `0.974` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `19035.17` | `0.722` | `1.000` | `0.089` | `1.000` | `0.850` | `0.500` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `5592.54` | `0.804` | `1.000` | `0.226` | `1.000` | `0.992` | `0.974` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `5269.88` | `0.788` | `1.000` | `0.154` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `5795.97` | `0.796` | `1.000` | `0.235` | `1.000` | `0.962` | `0.875` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `4797.81` | `0.786` | `1.000` | `0.190` | `1.000` | `0.966` | `0.886` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `28684.51` | `0.581` | `1.000` | `0.133` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `rails-01` | `recall` | `rails` | `8285.94` | `0.769` | `1.000` | `0.100` | `1.000` | `0.982` | `0.939` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `11550.50` | `0.738` | `1.000` | `0.051` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `4099.90` | `0.768` | `1.000` | `0.071` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `3636.33` | `0.808` | `1.000` | `0.231` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `7288.45` | `0.745` | `1.000` | `0.105` | `1.000` | `0.906` | `0.688` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `8069.42` | `0.803` | `1.000` | `0.213` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `7508.30` | `0.789` | `1.000` | `0.158` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `4567.73` | `0.759` | `1.000` | `0.128` | `1.000` | `0.932` | `0.775` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `4511.35` | `0.698` | `1.000` | `0.244` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `5448.52` | `0.680` | `1.000` | `0.200` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `12021.57` | `0.709` | `1.000` | `0.273` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `3248.12` | `0.683` | `1.000` | `0.207` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `3351.29` | `0.683` | `1.000` | `0.208` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `4987.21` | `0.698` | `1.000` | `0.246` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `4708.89` | `0.679` | `1.000` | `0.261` | `1.000` | `0.949` | `0.830` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `4785.37` | `0.747` | `1.000` | `0.367` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `13461.76` | `0.465` | `1.000` | `0.118` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `4546.28` | `0.733` | `1.000` | `0.333` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `3202.87` | `0.733` | `1.000` | `0.333` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `3098.70` | `0.697` | `1.000` | `0.242` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `3929.22` | `0.741` | `1.000` | `0.353` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `5348.99` | `0.763` | `1.000` | `0.407` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `3425.40` | `0.686` | `1.000` | `0.214` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `13724.28` | `0.196` | `1.000` | `0.000` | `0.000` | `0.000` | `0.308` | `soft_accepted` | structured_output_mismatch | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `9924.48` | `0.386` | `1.000` | `0.286` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `3979.64` | `0.210` | `1.000` | `0.000` | `0.000` | `0.000` | `0.100` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `7462.66` | `0.241` | `1.000` | `0.129` | `0.000` | `0.000` | `0.444` | `soft_accepted` | structured_output_mismatch | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `4953.01` | `0.386` | `1.000` | `0.286` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `3603.71` | `0.803` | `1.000` | `0.714` | `0.833` | `0.722` | `0.556` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `4962.50` | `0.226` | `1.000` | `0.050` | `0.000` | `0.000` | `0.111` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `5397.77` | `0.235` | `1.000` | `0.000` | `0.000` | `0.000` | `0.355` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `10924.05` | `0.459` | `1.000` | `0.800` | `0.000` | `0.000` | `1.000` | `soft_accepted` | structured_output_mismatch | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `5000.73` | `0.355` | `1.000` | `0.182` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `3041.85` | `0.306` | `1.000` | `0.000` | `0.250` | `0.179` | `0.056` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `3344.61` | `0.262` | `1.000` | `0.174` | `0.000` | `0.000` | `0.095` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `5077.49` | `0.321` | `1.000` | `0.235` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `3859.76` | `0.275` | `1.000` | `0.170` | `0.000` | `0.000` | `0.237` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `8198.92` | `0.302` | `0.467` | `0.650` | `0.000` | `0.000` | `0.667` | `soft_accepted` | missing_exact_anchors | file, line, code, message | - |
| `terraform-10` | `structured` | `terraform` | `8451.39` | `0.253` | `0.667` | `0.381` | `0.000` | `0.000` | `0.500` | `soft_accepted` | missing_exact_anchors | resource, field | - |
| `junit-01` | `structured` | `junit` | `7256.74` | `0.288` | `0.286` | `0.743` | `0.000` | `0.000` | `0.591` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | Test, Error, Location, --- | - |
| `kubernetes-03` | `structured` | `kubernetes` | `7643.10` | `0.163` | `0.429` | `0.296` | `0.000` | `0.000` | `0.174` | `soft_accepted` | missing_exact_anchors | unhealthy_pods, name, status, restarts | - |
| `eslint-06` | `structured` | `eslint` | `14353.01` | `0.226` | `1.000` | `0.044` | `0.000` | `0.000` | `0.125` | `accepted` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `7676.48` | `0.179` | `0.444` | `0.312` | `0.000` | `0.000` | `0.280` | `soft_accepted` | missing_exact_anchors | stage, command, error | - |
| `go-test-04` | `structured` | `go-test` | `7741.13` | `0.309` | `0.424` | `0.714` | `0.000` | `0.000` | `0.647` | `soft_accepted` | missing_exact_anchors | failed_tests, name, location, message | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `4481.03` | `0.189` | `0.333` | `0.429` | `0.000` | `0.000` | `0.273` | `soft_accepted` | missing_exact_anchors | Job, Step, Exit, --- | - |
| `npm-07` | `structured` | `npm` | `14454.17` | `0.176` | `0.833` | `0.107` | `0.000` | `0.000` | `0.077` | `soft_accepted` | missing_exact_anchors | package | - |
| `mypy-06` | `structured` | `mypy` | `7693.01` | `0.296` | `0.333` | `0.698` | `0.000` | `0.000` | `0.720` | `soft_accepted` | missing_exact_anchors | File, Line, Code, Message, --- | - |
| `gradle-03` | `structured` | `gradle` | `5862.40` | `0.215` | `0.545` | `0.300` | `0.000` | `0.000` | `0.538` | `soft_accepted` | missing_exact_anchors | failed, task, cause | - |
| `playwright-02` | `structured` | `playwright` | `13323.50` | `0.301` | `0.333` | `0.682` | `0.000` | `0.000` | `0.833` | `soft_accepted` | missing_exact_anchors | project, file, line, test | - |
| `postgres-04` | `structured` | `postgres` | `7595.51` | `0.295` | `0.424` | `0.683` | `0.000` | `0.000` | `0.577` | `soft_accepted` | missing_exact_anchors | errors, file, line, message | - |
| `vite-01` | `structured` | `vite` | `3973.51` | `0.205` | `1.000` | `0.000` | `0.000` | `0.000` | `0.048` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `3259.08` | `0.175` | `1.000` | `0.000` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `2753.73` | `0.157` | `1.000` | `0.000` | `0.000` | `0.000` | `0.143` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `11758.66` | `0.006` | `0.000` | `0.000` | `0.000` | `0.000` | `0.143` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | - |
| `npm-08` | `exact_format` | `npm` | `3774.97` | `0.131` | `1.000` | `0.000` | `0.000` | `0.000` | `0.083` | `soft_accepted` | structured_output_mismatch | - | - |
| `go-test-05` | `exact_format` | `go-test` | `5587.38` | `0.140` | `1.000` | `0.000` | `0.000` | `0.000` | `0.300` | `soft_accepted` | structured_output_mismatch | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `6949.41` | `0.136` | `1.000` | `0.000` | `0.000` | `0.000` | `0.200` | `soft_accepted` | structured_output_mismatch | - | - |
| `cargo-05` | `exact_format` | `cargo` | `4570.50` | `0.170` | `1.000` | `0.000` | `0.000` | `0.000` | `1.000` | `soft_accepted` | structured_output_mismatch | - | - |
| `curl-03` | `exact_format` | `curl` | `5500.55` | `0.131` | `1.000` | `0.000` | `0.000` | `0.000` | `0.091` | `soft_accepted` | structured_output_mismatch | - | - |
| `rails-02` | `exact_format` | `rails` | `9293.71` | `0.131` | `1.000` | `0.000` | `0.000` | `0.000` | `0.071` | `soft_accepted` | structured_output_mismatch | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `7007.26` | `0.476` | `1.000` | `0.320` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `5287.20` | `0.573` | `1.000` | `0.146` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `2670.42` | `0.300` | `1.000` | `0.000` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `2746.86` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `5051.16` | `0.543` | `1.000` | `0.087` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `9007.28` | `0.434` | `1.000` | `0.222` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `5318.07` | `0.396` | `0.583` | `0.098` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `3960.97` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `2802.39` | `0.767` | `1.000` | `0.200` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `7919.03` | `0.585` | `1.000` | `0.154` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `package-management-01` | `recall` | `package-management` | `3428.60` | `0.833` | `1.000` | `0.333` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `6488.25` | `0.616` | `0.667` | `0.500` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `1899.57` | `0.717` | `1.000` | `0.000` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `3465.60` | `0.812` | `1.000` | `0.296` | `1.000` | `0.965` | `0.882` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `1381.33` | `0.776` | `1.000` | `0.105` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `3740.47` | `0.778` | `1.000` | `0.303` | `1.000` | `0.856` | `0.520` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `2860.94` | `0.746` | `1.000` | `0.069` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `1607.73` | `0.792` | `1.000` | `0.200` | `1.000` | `0.977` | `0.923` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `3023.91` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `1280.54` | `0.821` | `1.000` | `0.286` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `23992.48` | `0.659` | `1.000` | `0.013` | `1.000` | `0.716` | `0.055` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `704.17` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `3727.77` | `0.800` | `1.000` | `0.200` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1882.63` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `618.95` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `699.91` | `0.861` | `1.000` | `0.444` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `2943.57` | `0.792` | `1.000` | `0.333` | `1.000` | `0.877` | `0.591` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `5074.00` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `1481.76` | `0.788` | `1.000` | `0.154` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `16513.20` | `0.681` | `1.000` | `0.231` | `1.000` | `0.981` | `0.938` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `912.41` | `0.750` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `6241.63` | `0.357` | `0.286` | `0.160` | `1.000` | `0.869` | `0.562` | `soft_accepted` | missing_exact_anchors | FAILURE: Build failed with an exception | - |
| `docker-05` | `summary` | `docker` | `1201.12` | `0.620` | `1.000` | `0.143` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `387.52` | `0.600` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `2756.35` | `0.550` | `1.000` | `0.000` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `679.76` | `0.733` | `1.000` | `0.333` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `1370.50` | `0.567` | `1.000` | `0.000` | `1.000` | `0.933` | `0.778` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `8185.56` | `0.359` | `1.000` | `0.581` | `0.000` | `0.000` | `0.476` | `soft_accepted` | structured_output_mismatch | - | - |
| `testing-06` | `instruction_following` | `testing` | `3620.42` | `0.268` | `1.000` | `0.190` | `0.000` | `0.000` | `0.105` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `5560.10` | `0.229` | `1.000` | `0.083` | `0.000` | `0.000` | `0.043` | `accepted` | - | - | - |
| `linting-02` | `structured` | `linting` | `1679.88` | `0.450` | `1.000` | `0.500` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `2867.09` | `0.680` | `1.000` | `0.323` | `0.800` | `0.712` | `0.632` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `1045.49` | `0.413` | `1.000` | `0.444` | `0.000` | `0.000` | `0.800` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `2951.00` | `0.175` | `1.000` | `0.000` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `3453.24` | `0.203` | `1.000` | `0.400` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `2512.83` | `0.497` | `1.000` | `0.800` | `0.333` | `0.300` | `0.667` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `4798.90` | `0.187` | `1.000` | `0.286` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `3176.26` | `0.267` | `1.000` | `0.824` | `0.000` | `0.000` | `0.700` | `accepted` | - | - | - |
| `build-05` | `exact_format` | `build` | `3461.47` | `0.209` | `1.000` | `0.444` | `0.000` | `0.000` | `0.286` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `2456.52` | `0.567` | `1.000` | `0.500` | `0.500` | `0.400` | `0.333` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `856.25` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `514.94` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `980.98` | `0.615` | `1.000` | `0.231` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `860.66` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `1562.30` | `0.469` | `1.000` | `0.000` | `1.000` | `0.906` | `0.688` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `328.75` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `1674.36` | `0.731` | `1.000` | `0.462` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `598.92` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1763.48` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `417.21` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `425.24` | `0.690` | `1.000` | `0.381` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `1205.59` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | command not found | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary' |
| `explanation-06` | `explanation` | `explanation` | `3055.74` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `2263.53` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `676.75` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `3687.07` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `775.64` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `3027.17` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `544.70` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `2241.52` | `0.680` | `1.000` | `0.323` | `0.800` | `0.712` | `0.632` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `962.90` | `0.413` | `1.000` | `0.444` | `0.000` | `0.000` | `0.800` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `3857.06` | `0.175` | `1.000` | `0.000` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `2518.35` | `0.217` | `1.000` | `0.500` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `4919.42` | `0.289` | `1.000` | `0.000` | `0.200` | `0.200` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `build-06` | `exact_format` | `build` | `4208.25` | `0.267` | `1.000` | `0.824` | `0.000` | `0.000` | `0.700` | `accepted` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `2736.61` | `0.175` | `1.000` | `0.000` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `3521.00` | `0.263` | `1.000` | `0.800` | `0.000` | `0.000` | `0.667` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `55068.52` | `0.128` | `1.000` | `0.003` | `0.000` | `0.000` | `0.002` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `deployment-05` | `explanation` | `deployment` | `1408.95` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `420.81` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `606.59` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `1336.96` | `0.591` | `1.000` | `0.182` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `1893.30` | `0.731` | `1.000` | `0.462` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `516.10` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `1687.76` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | undefined: fmt.Println | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary' |
| `explanation-17` | `explanation` | `explanation` | `4591.53` | `0.500` | `1.000` | `0.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1688.13` | `0.562` | `1.000` | `0.125` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
