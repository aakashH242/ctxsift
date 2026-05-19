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

- load_ms: `5330.96`
- cpu_rss_bytes: `null`
- gpu_peak_bytes: `null`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `275`
- accepted_count: `204`
- soft_accepted_count: `71`
- rejected_count: `5`
- exact_pass_count: `236`
- avg_inference_ms: `8373.44`
- p95_inference_ms: `29746.61`
- avg_exact_preservation_ratio: `0.910`
- avg_summary_quality_ratio: `0.805`
- avg_format_adherence_score: `0.715`
- avg_instruction_following_score: `0.672`
- avg_brevity_ratio: `0.719`
- avg_case_score: `0.743`
- p10_case_score: `0.223`
- quality_core: `0.639`
- latency_factor: `0.850`
- final_score: `54.34`
- peak_cpu_rss_bytes: `null`
- peak_gpu_bytes: `null`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `28253.19` | `0.689` | `1.000` | `0.900` | `0.500` | `0.404` | `0.358` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-02` | `summary` | `python` | `8562.19` | `0.832` | `1.000` | `0.932` | `0.500` | `0.459` | `0.727` | `accepted` | - | - | - |
| `python-03` | `recall` | `python` | `23061.00` | `0.686` | `1.000` | `0.904` | `0.500` | `0.397` | `0.311` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-04` | `recall` | `python` | `18639.87` | `0.905` | `1.000` | `0.940` | `1.000` | `0.760` | `0.200` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `21537.20` | `0.713` | `1.000` | `0.956` | `0.500` | `0.425` | `0.500` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `pytest-01` | `recall` | `pytest` | `10185.90` | `0.928` | `1.000` | `0.939` | `1.000` | `0.830` | `0.435` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `18067.43` | `0.587` | `0.488` | `0.818` | `1.000` | `0.784` | `0.279` | `soft_accepted` | missing_exact_anchors | pytest tests/integration -k billing -vv --maxfail=1, /workspace/tests/integration/test_billing_api.py:73 | - |
| `pytest-03` | `recall` | `pytest` | `36884.13` | `0.773` | `1.000` | `0.935` | `1.000` | `0.776` | `0.253` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `pytest-04` | `recall` | `pytest` | `4805.64` | `0.986` | `1.000` | `0.963` | `1.000` | `0.986` | `0.952` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `22167.35` | `0.653` | `1.000` | `0.914` | `0.500` | `0.403` | `0.353` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `mypy-01` | `recall` | `mypy` | `4979.42` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `8753.21` | `0.929` | `1.000` | `0.950` | `1.000` | `0.898` | `0.660` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `5347.46` | `0.993` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `5343.18` | `0.875` | `0.911` | `0.930` | `1.000` | `0.850` | `0.500` | `accepted` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `1307.69` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `2666.21` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `2790.80` | `0.984` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `5166.06` | `0.972` | `1.000` | `0.913` | `1.000` | `0.981` | `0.935` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `3371.72` | `0.968` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `3362.56` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `2809.86` | `0.970` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `1018.90` | `0.992` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `3677.18` | `0.978` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `15635.30` | `0.880` | `1.000` | `0.926` | `1.000` | `0.819` | `0.398` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `27434.02` | `0.737` | `0.818` | `0.941` | `1.000` | `0.871` | `0.571` | `soft_accepted` | missing_exact_anchors | src/routes/checkout/index.tsx | - |
| `pnpm-01` | `recall` | `pnpm` | `13718.66` | `0.912` | `1.000` | `0.932` | `1.000` | `0.786` | `0.286` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `17042.05` | `0.811` | `0.909` | `0.942` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 5.51.1 | - |
| `pnpm-03` | `summary` | `pnpm` | `33608.22` | `0.871` | `1.000` | `0.895` | `1.000` | `0.825` | `0.417` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `2736.92` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `11038.60` | `0.763` | `0.895` | `0.927` | `1.000` | `0.889` | `0.630` | `soft_accepted` | missing_exact_anchors | Watching for file changes | - |
| `typescript-03` | `summary` | `typescript` | `14617.67` | `0.699` | `1.000` | `0.956` | `0.500` | `0.440` | `0.603` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `eslint-01` | `recall` | `eslint` | `4655.59` | `0.963` | `1.000` | `0.937` | `1.000` | `0.936` | `0.788` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `7929.09` | `0.958` | `1.000` | `0.896` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `3703.27` | `0.988` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `13865.09` | `0.892` | `1.000` | `0.888` | `1.000` | `0.760` | `0.201` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `953.67` | `0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `14885.93` | `0.852` | `1.000` | `0.916` | `1.000` | `0.772` | `0.238` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `2160.14` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `13368.52` | `0.900` | `1.000` | `0.916` | `1.000` | `0.763` | `0.209` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `3658.50` | `0.933` | `1.000` | `0.903` | `1.000` | `0.943` | `0.811` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `4934.06` | `0.905` | `1.000` | `0.947` | `1.000` | `0.852` | `0.508` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `17921.75` | `0.909` | `1.000` | `0.947` | `1.000` | `0.767` | `0.222` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `3626.73` | `0.992` | `1.000` | `0.981` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `27359.69` | `0.691` | `1.000` | `0.926` | `0.500` | `0.396` | `0.310` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `terraform-01` | `summary` | `terraform` | `2764.68` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `6224.07` | `0.959` | `1.000` | `0.925` | `1.000` | `0.931` | `0.771` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `2349.43` | `0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `5399.77` | `0.979` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `5055.52` | `0.937` | `1.000` | `0.909` | `1.000` | `0.879` | `0.595` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `8515.89` | `0.700` | `0.676` | `0.876` | `1.000` | `0.908` | `0.694` | `soft_accepted` | missing_exact_anchors | make integration | - |
| `git-01` | `recall` | `git` | `19483.48` | `0.696` | `1.000` | `0.908` | `0.500` | `0.412` | `0.417` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `git-02` | `recall` | `git` | `5778.81` | `0.912` | `1.000` | `0.871` | `1.000` | `0.833` | `0.443` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `19998.43` | `0.911` | `1.000` | `0.947` | `1.000` | `0.774` | `0.248` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `10268.72` | `0.913` | `1.000` | `0.943` | `1.000` | `0.782` | `0.272` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `18829.49` | `0.829` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `ssh-01` | `summary` | `ssh` | `9312.84` | `0.960` | `1.000` | `0.954` | `1.000` | `0.957` | `0.857` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `6741.52` | `0.973` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `14271.02` | `0.766` | `0.774` | `0.893` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Exec format error | - |
| `systemd-02` | `summary` | `systemd` | `19515.99` | `0.843` | `1.000` | `0.882` | `1.000` | `0.781` | `0.269` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `8067.24` | `0.888` | `1.000` | `0.937` | `1.000` | `0.827` | `0.422` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `48268.11` | `0.899` | `1.000` | `0.934` | `1.000` | `0.747` | `0.155` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `11036.79` | `0.762` | `0.750` | `0.898` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | example.com/mono-app/pkg/server | - |
| `go-test-01` | `summary` | `go-test` | `15223.85` | `0.910` | `1.000` | `0.928` | `1.000` | `0.877` | `0.590` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `48420.06` | `0.699` | `0.867` | `0.913` | `1.000` | `0.780` | `0.267` | `soft_accepted` | missing_exact_anchors | cannot find symbol | - |
| `maven-01` | `summary` | `maven` | `36566.00` | `0.638` | `1.000` | `0.906` | `0.500` | `0.388` | `0.253` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `maven-02` | `summary` | `maven` | `34557.71` | `0.722` | `0.636` | `0.913` | `1.000` | `0.949` | `0.829` | `soft_accepted` | missing_exact_anchors | mvn -U -DskipTests package | - |
| `gradle-01` | `recall` | `gradle` | `12312.13` | `0.904` | `1.000` | `0.927` | `1.000` | `0.767` | `0.224` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `21030.08` | `0.964` | `1.000` | `0.910` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `21989.44` | `0.849` | `1.000` | `0.912` | `1.000` | `0.768` | `0.227` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `4256.11` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `51642.83` | `0.583` | `0.526` | `0.903` | `1.000` | `0.768` | `0.228` | `soft_accepted` | missing_exact_anchors | MODULE_NOT_FOUND, /workspace/dist/config/index.js:4:18 | - |
| `npm-04` | `summary` | `npm` | `15222.22` | `0.863` | `1.000` | `0.927` | `1.000` | `0.784` | `0.281` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `4650.71` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `16818.93` | `0.875` | `1.000` | `0.908` | `1.000` | `0.823` | `0.410` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `16219.31` | `0.684` | `1.000` | `0.941` | `0.500` | `0.429` | `0.526` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `pytest-06` | `summary` | `pytest` | `12800.94` | `0.876` | `1.000` | `0.911` | `1.000` | `0.824` | `0.412` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `5520.54` | `0.971` | `1.000` | `0.939` | `1.000` | `0.992` | `0.972` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `12064.99` | `0.929` | `1.000` | `0.933` | `1.000` | `0.912` | `0.707` | `accepted` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `9816.36` | `0.884` | `1.000` | `0.918` | `1.000` | `0.833` | `0.443` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `3859.71` | `0.975` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `43859.86` | `0.650` | `1.000` | `0.932` | `0.500` | `0.392` | `0.282` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | - | - |
| `kubectl-07` | `recall` | `kubectl` | `2928.86` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `9272.65` | `0.913` | `1.000` | `0.919` | `1.000` | `0.799` | `0.328` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `4368.66` | `0.965` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `16548.51` | `0.861` | `1.000` | `0.893` | `1.000` | `0.807` | `0.358` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `2404.43` | `0.979` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `4176.49` | `0.972` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `3147.75` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `5124.82` | `0.969` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `2140.22` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `3341.97` | `0.703` | `0.444` | `0.916` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERROR 1054 (42S22), line 1 | - |
| `redis-01` | `summary` | `redis` | `3236.11` | `0.949` | `1.000` | `0.948` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `5587.02` | `0.713` | `0.667` | `0.955` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | LOADING | - |
| `github-actions-01` | `recall` | `github-actions` | `47252.07` | `0.333` | `0.000` | `0.714` | `1.000` | `0.741` | `0.137` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | ruff check ., src/api/views.py, line=91, Ruff F821, exit code 2 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `14938.26` | `0.898` | `1.000` | `0.903` | `1.000` | `0.874` | `0.581` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `4473.96` | `0.959` | `1.000` | `0.898` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `5555.44` | `0.923` | `1.000` | `0.925` | `1.000` | `0.906` | `0.686` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `4538.99` | `0.984` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `7204.09` | `0.921` | `1.000` | `0.949` | `1.000` | `0.802` | `0.339` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `5918.22` | `0.909` | `1.000` | `0.914` | `1.000` | `0.887` | `0.625` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `15549.12` | `0.941` | `1.000` | `0.951` | `1.000` | `0.861` | `0.536` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `8400.51` | `0.534` | `0.254` | `0.856` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/router.rs:137:42, src/router.rs:128, req.into_body(), req.method(), req.clone().into_body() | - |
| `ci-log-01` | `recall` | `ci-log` | `22809.17` | `0.915` | `1.000` | `0.900` | `1.000` | `0.821` | `0.404` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `6456.25` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `15727.76` | `0.831` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `soft_accepted` | structured_output_mismatch | - | - |
| `build-log-01` | `summary` | `build-log` | `37610.04` | `0.671` | `1.000` | `0.908` | `0.500` | `0.426` | `0.506` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `docker-build-02` | `summary` | `docker-build` | `50403.79` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | Dockerfile:18, COPY apps/web ./apps/web, "/apps/web": not found | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them do not add extra structu...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them preserve exact filenames...' |
| `lint-output-01` | `instruction_following` | `lint-output` | `33231.25` | `0.355` | `1.000` | `0.684` | `0.000` | `0.000` | `0.118` | `soft_accepted` | structured_output_mismatch | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `5940.07` | `0.514` | `1.000` | `0.713` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `6633.95` | `0.463` | `1.000` | `0.721` | `0.000` | `0.000` | `0.464` | `accepted` | - | - | - |
| `structured-output-01` | `structured` | `structured-output` | `12455.34` | `0.408` | `1.000` | `0.692` | `0.000` | `0.000` | `0.725` | `soft_accepted` | structured_output_mismatch | - | - |
| `structured-output-02` | `structured` | `structured-output` | `10082.30` | `0.164` | `0.095` | `0.348` | `0.000` | `0.000` | `0.694` | `soft_accepted` | missing_exact_anchors | test / integration, port 5432 is already allocated, deploy / preview, Upload artifact, dist/preview | - |
| `structured-output-03` | `structured` | `structured-output` | `7102.68` | `0.329` | `1.000` | `0.356` | `0.000` | `0.000` | `0.220` | `accepted` | - | - | - |
| `structured-output-04` | `structured` | `structured-output` | `14357.01` | `0.225` | `1.000` | `0.210` | `0.000` | `0.000` | `0.014` | `soft_accepted` | structured_output_mismatch | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `8982.18` | `0.027` | `0.000` | `0.298` | `0.000` | `0.000` | `0.032` | `soft_accepted` | missing_exact_anchors | tests/api/test_users.py::test_create_user_requires_email, tests/api/test_users.py::test_delete_user_requires_admin, tests/jobs/test_reconcile.py::TestReconcile::test_retries_deadlock | - |
| `exact-format-02` | `exact_format` | `exact-format` | `18647.75` | `0.121` | `0.714` | `0.319` | `0.000` | `0.000` | `0.055` | `soft_accepted` | missing_exact_anchors | SearchBox debounces network query before fetch | - |
| `exact-format-03` | `exact_format` | `exact-format` | `9366.86` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `6839.47` | `0.681` | `0.778` | `0.892` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `21823.32` | `0.861` | `1.000` | `0.861` | `1.000` | `0.791` | `0.304` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `5129.92` | `0.753` | `1.000` | `0.906` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `7588.53` | `0.951` | `1.000` | `0.937` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `5075.47` | `0.981` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `10274.49` | `0.979` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `8093.75` | `0.747` | `1.000` | `0.914` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `6194.77` | `0.960` | `1.000` | `0.919` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `6896.29` | `0.967` | `1.000` | `0.917` | `1.000` | `0.962` | `0.872` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `8643.89` | `0.985` | `1.000` | `0.952` | `1.000` | `0.992` | `0.974` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `15169.81` | `0.928` | `1.000` | `0.913` | `1.000` | `0.850` | `0.500` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `4409.41` | `0.979` | `1.000` | `0.926` | `1.000` | `0.992` | `0.974` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `4223.21` | `0.982` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `4713.61` | `0.971` | `1.000` | `0.933` | `1.000` | `0.962` | `0.875` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `5024.42` | `0.972` | `1.000` | `0.936` | `1.000` | `0.966` | `0.886` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `21766.85` | `0.751` | `1.000` | `0.932` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `rails-01` | `recall` | `rails` | `6614.72` | `0.982` | `1.000` | `0.952` | `1.000` | `0.982` | `0.939` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `7935.45` | `0.958` | `1.000` | `0.932` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `3164.28` | `0.979` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `3513.17` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `4809.85` | `0.952` | `1.000` | `0.931` | `1.000` | `0.906` | `0.688` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `6419.10` | `0.983` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `5133.24` | `0.982` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `3109.37` | `0.960` | `1.000` | `0.931` | `1.000` | `0.932` | `0.775` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `3951.71` | `0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `4205.11` | `0.966` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `4681.11` | `0.970` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `2058.33` | `0.971` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `3266.45` | `0.966` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `3801.85` | `0.962` | `1.000` | `0.904` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `3926.12` | `0.951` | `1.000` | `0.941` | `1.000` | `0.949` | `0.830` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `3649.14` | `0.966` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `8335.36` | `0.740` | `1.000` | `0.926` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `3915.65` | `0.965` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `2568.52` | `0.959` | `1.000` | `0.898` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `2281.76` | `0.968` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `2844.04` | `0.966` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `4311.65` | `0.969` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `3212.16` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `12205.53` | `0.367` | `1.000` | `0.671` | `0.000` | `0.000` | `0.308` | `soft_accepted` | structured_output_mismatch | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `7588.25` | `0.451` | `1.000` | `0.768` | `0.000` | `0.000` | `1.000` | `soft_accepted` | structured_output_mismatch | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `44464.75` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | tests/test_api.py::test_create_user, tests/test_auth.py::test_refresh_token_expiry | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them do not add extra structu...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them preserve exact filenames...' |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `6531.27` | `0.388` | `1.000` | `0.708` | `0.000` | `0.000` | `0.444` | `soft_accepted` | structured_output_mismatch | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `4817.48` | `0.254` | `0.000` | `0.692` | `0.000` | `0.000` | `0.917` | `soft_accepted` | missing_exact_anchors | Warning Failed, secret "api-env" not found, Warning BackOff, Back-off restarting failed container api | - |
| `npm-06` | `instruction_following` | `npm` | `3033.08` | `0.862` | `1.000` | `0.912` | `0.833` | `0.722` | `0.556` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `4222.07` | `0.418` | `1.000` | `0.686` | `0.000` | `0.000` | `0.118` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `3983.40` | `0.422` | `1.000` | `0.622` | `0.000` | `0.000` | `0.355` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `7098.13` | `0.475` | `1.000` | `0.788` | `0.000` | `0.000` | `0.389` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `6785.03` | `0.525` | `1.000` | `0.750` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `2970.69` | `0.513` | `1.000` | `0.690` | `0.250` | `0.179` | `0.056` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `2731.35` | `0.421` | `1.000` | `0.706` | `0.000` | `0.000` | `0.095` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `6910.42` | `0.321` | `0.333` | `0.705` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/auth.rs:88, billing::tests::rounds_half_even, left: 1750, right: 1749 | - |
| `shell-01` | `instruction_following` | `shell` | `3623.29` | `0.441` | `1.000` | `0.725` | `0.000` | `0.000` | `0.237` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `6346.86` | `0.321` | `0.467` | `0.725` | `0.000` | `0.000` | `0.667` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | file, line, code, message | - |
| `terraform-10` | `structured` | `terraform` | `5962.01` | `0.312` | `0.667` | `0.569` | `0.000` | `0.000` | `0.636` | `soft_accepted` | missing_exact_anchors | resource, field | - |
| `junit-01` | `structured` | `junit` | `6796.75` | `0.211` | `0.286` | `0.329` | `0.000` | `0.000` | `0.929` | `soft_accepted` | missing_exact_anchors | Test, Error, Location, --- | - |
| `kubernetes-03` | `structured` | `kubernetes` | `5916.97` | `0.132` | `0.429` | `0.174` | `0.000` | `0.000` | `0.174` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | unhealthy_pods, name, status, restarts | - |
| `eslint-06` | `structured` | `eslint` | `3220.37` | `0.332` | `1.000` | `0.231` | `0.000` | `0.000` | `0.625` | `accepted` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `23189.16` | `0.196` | `0.444` | `0.404` | `0.000` | `0.000` | `0.200` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | stage, command, error | - |
| `go-test-04` | `structured` | `go-test` | `6702.86` | `0.303` | `0.424` | `0.703` | `0.000` | `0.000` | `0.611` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | failed_tests, name, location, message | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `4087.21` | `0.244` | `0.167` | `0.622` | `0.000` | `0.000` | `0.667` | `soft_accepted` | missing_exact_anchors | Job, Step, Exit, ---, Run | - |
| `npm-07` | `structured` | `npm` | `12148.44` | `0.226` | `0.833` | `0.303` | `0.000` | `0.000` | `0.077` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | package | - |
| `mypy-06` | `structured` | `mypy` | `44437.65` | `0.059` | `0.000` | `0.195` | `0.000` | `0.000` | `0.104` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | File, Line, Code, Message, ---, app/api.py | - |
| `gradle-03` | `structured` | `gradle` | `6593.92` | `0.255` | `0.545` | `0.457` | `0.000` | `0.000` | `0.538` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | failed, task, cause | - |
| `playwright-02` | `structured` | `playwright` | `11041.32` | `0.318` | `0.333` | `0.747` | `0.000` | `0.000` | `0.833` | `soft_accepted` | missing_exact_anchors | project, file, line, test | - |
| `postgres-04` | `structured` | `postgres` | `7416.80` | `0.318` | `0.424` | `0.764` | `0.000` | `0.000` | `0.600` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | errors, file, line, message | - |
| `vite-01` | `structured` | `vite` | `7084.03` | `0.230` | `1.000` | `0.219` | `0.000` | `0.000` | `0.048` | `soft_accepted` | structured_output_mismatch | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `6348.31` | `0.192` | `1.000` | `0.322` | `0.000` | `0.000` | `0.200` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `3118.49` | `0.188` | `1.000` | `0.305` | `0.000` | `0.000` | `0.143` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `25334.56` | `0.034` | `0.000` | `0.331` | `0.000` | `0.000` | `0.143` | `soft_accepted` | missing_exact_anchors | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | - |
| `npm-08` | `exact_format` | `npm` | `1357.43` | `0.183` | `1.000` | `0.289` | `0.000` | `0.000` | `0.083` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `1814.04` | `0.197` | `1.000` | `0.319` | `0.000` | `0.000` | `0.300` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `2142.50` | `0.189` | `1.000` | `0.290` | `0.000` | `0.000` | `0.200` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `1127.98` | `0.234` | `1.000` | `0.336` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `1430.52` | `0.179` | `1.000` | `0.242` | `0.000` | `0.000` | `0.091` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `2125.96` | `0.180` | `1.000` | `0.257` | `0.000` | `0.000` | `0.077` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `5702.43` | `0.731` | `1.000` | `0.921` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `4591.22` | `0.940` | `1.000` | `0.879` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `4911.06` | `0.754` | `1.000` | `0.908` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `2990.21` | `0.951` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `4150.88` | `0.944` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `7409.93` | `0.686` | `1.000` | `0.814` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `4194.16` | `0.715` | `0.583` | `0.848` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `3395.92` | `0.985` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `2208.81` | `0.950` | `1.000` | `0.934` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `6766.36` | `0.754` | `1.000` | `0.950` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `package-management-01` | `recall` | `package-management` | `2517.57` | `0.965` | `1.000` | `0.861` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `5092.95` | `0.715` | `0.667` | `0.965` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `1536.93` | `0.952` | `1.000` | `0.940` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `1838.76` | `0.963` | `1.000` | `0.901` | `1.000` | `0.965` | `0.882` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `1078.87` | `0.966` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `2816.57` | `0.921` | `1.000` | `0.874` | `1.000` | `0.856` | `0.520` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `2127.62` | `0.952` | `1.000` | `0.892` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `1322.53` | `0.970` | `1.000` | `0.913` | `1.000` | `0.977` | `0.923` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `2110.29` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `923.58` | `0.966` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `18944.38` | `0.869` | `1.000` | `0.852` | `1.000` | `0.716` | `0.055` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `492.44` | `0.973` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `3235.98` | `0.972` | `1.000` | `0.889` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1744.63` | `0.967` | `1.000` | `0.866` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `392.00` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `849.88` | `0.986` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `2310.75` | `0.936` | `1.000` | `0.906` | `1.000` | `0.877` | `0.591` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `3892.13` | `0.975` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `1356.90` | `0.976` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `13170.98` | `0.820` | `1.000` | `0.886` | `1.000` | `0.981` | `0.938` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `856.39` | `0.974` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `4718.52` | `0.579` | `0.286` | `0.815` | `1.000` | `0.869` | `0.562` | `soft_accepted` | missing_exact_anchors | FAILURE: Build failed with an exception | - |
| `docker-05` | `summary` | `docker` | `1014.95` | `0.903` | `1.000` | `0.850` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `418.03` | `0.961` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `2135.19` | `0.888` | `1.000` | `0.844` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `672.57` | `0.976` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `1269.61` | `0.896` | `1.000` | `0.823` | `1.000` | `0.933` | `0.778` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `8024.49` | `0.423` | `1.000` | `0.827` | `0.000` | `0.000` | `0.500` | `soft_accepted` | structured_output_mismatch | - | - |
| `testing-06` | `instruction_following` | `testing` | `3250.74` | `0.439` | `1.000` | `0.763` | `0.000` | `0.000` | `0.105` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `8780.05` | `0.379` | `1.000` | `0.777` | `0.000` | `0.000` | `0.125` | `soft_accepted` | structured_output_mismatch | - | - |
| `linting-02` | `structured` | `linting` | `1283.77` | `0.355` | `1.000` | `0.183` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `43194.19` | `0.261` | `1.000` | `0.309` | `0.000` | `0.000` | `0.138` | `soft_accepted` | structured_output_mismatch | - | - |
| `deployment-02` | `structured` | `deployment` | `1841.42` | `0.447` | `1.000` | `0.557` | `0.000` | `0.000` | `0.800` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `962.72` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `1421.80` | `0.231` | `1.000` | `0.647` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `43085.11` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | OUTPUT: | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them do not add extra structu...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them do not add extra structu...' |
| `shell-04` | `exact_format` | `shell` | `1105.96` | `0.207` | `1.000` | `0.491` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `3641.97` | `0.141` | `0.286` | `0.726` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Resources: 1 added | - |
| `build-05` | `exact_format` | `build` | `2479.14` | `0.202` | `1.000` | `0.315` | `0.000` | `0.000` | `0.400` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `937.71` | `0.582` | `1.000` | `0.658` | `0.500` | `0.400` | `0.333` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `524.64` | `0.936` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `656.19` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `665.70` | `0.959` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `609.87` | `0.943` | `1.000` | `0.885` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `1395.93` | `0.919` | `1.000` | `0.900` | `1.000` | `0.906` | `0.688` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `312.61` | `0.932` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `1454.69` | `0.936` | `1.000` | `0.873` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `485.61` | `0.933` | `1.000` | `0.866` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1386.01` | `0.913` | `1.000` | `0.826` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `525.14` | `0.950` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `402.71` | `0.938` | `1.000` | `0.875` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `1263.56` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | command not found | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary' |
| `explanation-06` | `explanation` | `explanation` | `2100.21` | `0.904` | `1.000` | `0.808` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `1721.31` | `0.932` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `515.41` | `0.926` | `1.000` | `0.853` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `2788.45` | `0.904` | `1.000` | `0.809` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `840.77` | `0.948` | `1.000` | `0.896` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `2106.73` | `0.916` | `1.000` | `0.832` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `400.68` | `0.933` | `1.000` | `0.866` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `43096.07` | `0.261` | `1.000` | `0.309` | `0.000` | `0.000` | `0.138` | `soft_accepted` | structured_output_mismatch | - | - |
| `linting-03` | `structured` | `linting` | `1801.44` | `0.447` | `1.000` | `0.557` | `0.000` | `0.000` | `0.800` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `1130.72` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `422.45` | `0.231` | `1.000` | `0.648` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `18811.27` | `0.191` | `1.000` | `0.308` | `0.014` | `0.010` | `0.007` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `3329.11` | `0.141` | `0.286` | `0.726` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Resources: 1 added | - |
| `runtime-07` | `exact_format` | `runtime` | `1098.72` | `0.207` | `1.000` | `0.319` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `2620.53` | `0.227` | `1.000` | `0.791` | `0.000` | `0.000` | `0.750` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `shell-08` | `exact_format` | `shell` | `2099.81` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `664.57` | `0.936` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `293.26` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `463.89` | `0.960` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `900.15` | `0.970` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `1416.73` | `0.936` | `1.000` | `0.873` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `530.04` | `0.963` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `1435.45` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | undefined: fmt.Println | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary' |
| `explanation-17` | `explanation` | `explanation` | `2130.66` | `0.928` | `1.000` | `0.856` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1252.11` | `0.939` | `1.000` | `0.878` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
