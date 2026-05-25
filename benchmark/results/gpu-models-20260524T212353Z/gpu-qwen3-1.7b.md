# gpu-qwen3-1.7b

## Scenario

- track: `gpu`
- phase: `gpu-screen`
- model: `Qwen/Qwen3-1.7B`
- quantization: `none`
- device: `cuda`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `87404.43`
- cpu_rss_bytes: `6847631360`
- gpu_peak_bytes: `4716511744`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- recovered_final_score: `58.05`
- raw_final_score: `0.00`
- recovery_lift: `+58.05`
- case_count: `280`
- success_count: `267`
- accepted_count: `216`
- soft_accepted_count: `51`
- rejected_count: `13`
- exact_pass_count: `239`
- avg_inference_ms: `33799.40`
- p95_inference_ms: `107948.43`
- avg_exact_preservation_ratio: `0.936`
- avg_summary_quality_ratio: `0.844`
- avg_format_adherence_score: `0.869`
- avg_instruction_following_score: `0.824`
- avg_brevity_ratio: `0.891`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.796`
- p10_case_score: `0.230`
- quality_core: `0.683`
- latency_factor: `0.850`
- final_score: `58.05`
- peak_cpu_rss_bytes: `6860521472`
- peak_gpu_bytes: `5169350144`

### Raw View

- accepted_count: `0`
- soft_accepted_count: `0`
- rejected_count: `280`
- exact_pass_count: `243`
- avg_exact_preservation_ratio: `0.944`
- avg_summary_quality_ratio: `0.759`
- avg_format_adherence_score: `0.418`
- avg_instruction_following_score: `0.000`
- avg_brevity_ratio: `0.622`
- avg_thought_leakage_density: `0.370`
- avg_thought_marker_count: `2.82`
- avg_case_score: `0.000`
- p10_case_score: `0.000`
- quality_core: `0.000`
- final_score: `0.00`

## Cases

| case_id | family | domain | ms | recovered_score | raw_score | lift | preserve | quality | format | instruction | recovered_thought_density | raw_thought_density | recovered_validation | raw_validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `72237.40` | `0.586` | `0.000` | `+0.586` | `1.000` | `0.899` | `0.500` | `0.404` | `0.000` | `0.133` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `python-02` | `summary` | `python` | `35018.10` | `0.613` | `0.000` | `+0.613` | `1.000` | `0.939` | `0.500` | `0.459` | `0.000` | `0.151` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `python-03` | `recall` | `python` | `5685.15` | `0.990` | `0.000` | `+0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.245` | `accepted` | `rejected` | - | - | - |
| `python-04` | `recall` | `python` | `52995.37` | `0.988` | `0.000` | `+0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `0.000` | `0.557` | `accepted` | `rejected` | - | - | - |
| `python-05` | `recall` | `python` | `43529.40` | `0.756` | `0.000` | `+0.756` | `0.778` | `0.958` | `1.000` | `1.000` | `0.000` | `0.731` | `soft_accepted` | `rejected` | missing_exact_anchors | python tools/export_report.py --input data/may.csv --format parquet | - |
| `pytest-01` | `recall` | `pytest` | `61869.52` | `0.888` | `0.000` | `+0.888` | `1.000` | `0.935` | `1.000` | `0.830` | `0.000` | `0.131` | `accepted` | `rejected` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `75362.85` | `0.979` | `0.000` | `+0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.562` | `accepted` | `rejected` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `43573.49` | `0.859` | `0.000` | `+0.859` | `1.000` | `0.937` | `1.000` | `0.776` | `0.000` | `0.116` | `accepted` | `rejected` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `65346.15` | `0.992` | `0.000` | `+0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.627` | `accepted` | `rejected` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `63831.40` | `0.570` | `0.000` | `+0.570` | `1.000` | `0.930` | `0.500` | `0.413` | `0.000` | `0.115` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `mypy-01` | `recall` | `mypy` | `7849.44` | `0.991` | `0.000` | `+0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.250` | `accepted` | `rejected` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `79764.12` | `0.880` | `0.000` | `+0.880` | `1.000` | `0.951` | `1.000` | `0.862` | `0.000` | `0.152` | `accepted` | `rejected` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `13403.23` | `0.991` | `0.000` | `+0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `0.000` | `0.217` | `accepted` | `rejected` | - | - | - |
| `ruff-01` | `recall` | `ruff` | `16665.12` | `0.895` | `0.000` | `+0.895` | `0.911` | `0.932` | `1.000` | `0.914` | `0.000` | `0.158` | `accepted` | `rejected` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `4918.91` | `0.990` | `0.000` | `+0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.264` | `accepted` | `rejected` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `11467.97` | `0.985` | `0.000` | `+0.985` | `1.000` | `0.962` | `1.000` | `1.000` | `0.000` | `0.281` | `accepted` | `rejected` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `6058.07` | `0.992` | `0.000` | `+0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.299` | `accepted` | `rejected` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `18205.75` | `0.982` | `0.000` | `+0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.245` | `accepted` | `rejected` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `11130.01` | `0.966` | `0.000` | `+0.966` | `1.000` | `0.915` | `1.000` | `1.000` | `0.000` | `0.218` | `accepted` | `rejected` | - | - | - |
| `black-01` | `summary` | `black` | `42052.02` | `0.989` | `0.000` | `+0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `0.000` | `0.229` | `accepted` | `rejected` | - | - | - |
| `black-02` | `summary` | `black` | `9645.19` | `0.970` | `0.000` | `+0.970` | `1.000` | `0.925` | `1.000` | `1.000` | `0.000` | `0.209` | `accepted` | `rejected` | - | - | - |
| `black-03` | `recall` | `black` | `54951.82` | `0.992` | `0.000` | `+0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.768` | `accepted` | `rejected` | - | - | - |
| `npm-01` | `recall` | `npm` | `22883.35` | `0.977` | `0.000` | `+0.977` | `1.000` | `0.908` | `1.000` | `1.000` | `0.000` | `0.213` | `accepted` | `rejected` | - | - | - |
| `npm-02` | `summary` | `npm` | `31784.30` | `0.831` | `0.000` | `+0.831` | `1.000` | `0.919` | `1.000` | `0.811` | `0.000` | `0.126` | `accepted` | `rejected` | - | - | - |
| `npm-03` | `summary` | `npm` | `44072.13` | `0.981` | `0.000` | `+0.981` | `1.000` | `0.951` | `1.000` | `1.000` | `0.000` | `0.745` | `accepted` | `rejected` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `9533.37` | `0.986` | `0.000` | `+0.986` | `1.000` | `0.944` | `1.000` | `1.000` | `0.000` | `0.202` | `accepted` | `rejected` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `52007.91` | `0.772` | `0.000` | `+0.772` | `0.727` | `0.940` | `1.000` | `1.000` | `0.000` | `0.255` | `soft_accepted` | `rejected` | missing_exact_anchors | pnpm add @tanstack/react-query-devtools@5.52.0 -F packages/admin | - |
| `pnpm-03` | `summary` | `pnpm` | `53196.55` | `0.687` | `0.000` | `+0.687` | `0.381` | `0.907` | `1.000` | `1.000` | `0.000` | `0.319` | `soft_accepted` | `rejected` | missing_exact_anchors | pnpm -r test --stream, packages/api, health route > returns build metadata when git sha is present | - |
| `typescript-01` | `summary` | `typescript` | `10001.94` | `0.981` | `0.000` | `+0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.244` | `accepted` | `rejected` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `6386.73` | `0.993` | `0.000` | `+0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.256` | `accepted` | `rejected` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `48731.25` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.942` | `0.500` | `0.000` | `0.000` | `0.168` | `rejected` | `rejected` | unterminated_reasoning_block | - | qwen3 output validation failed: model did not stop thinking before reaching the output limit. first_pass="$ tsc src/index.ts src/http.ts --pretty false src/index.ts(48,20): error TS2769: No overload matches this call. Overload 1 of 2, '(url: string, init?: Reques..." repair_pass="$ tsc src/index.ts src/http.ts --pretty false src/index.ts(48,20): error TS2769: No overload matches this call. Overload 1 of 2, '(url: string, init?: Reques..." |
| `eslint-01` | `recall` | `eslint` | `14416.65` | `0.984` | `0.000` | `+0.984` | `1.000` | `0.934` | `1.000` | `1.000` | `0.000` | `0.175` | `accepted` | `rejected` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `5998.54` | `0.983` | `0.000` | `+0.983` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.353` | `accepted` | `rejected` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `6459.06` | `0.989` | `0.000` | `+0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.222` | `accepted` | `rejected` | - | - | - |
| `docker-01` | `recall` | `docker` | `6194.73` | `0.537` | `0.000` | `+0.537` | `0.245` | `0.887` | `1.000` | `1.000` | `0.000` | `0.436` | `soft_accepted` | `rejected` | missing_exact_anchors | COPY docker/entrypoint.sh /entrypoint.sh, /docker/entrypoint.sh, Dockerfile:14, failed to solve | - |
| `docker-02` | `summary` | `docker` | `3787.05` | `0.988` | `0.000` | `+0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.264` | `accepted` | `rejected` | - | - | - |
| `docker-03` | `summary` | `docker` | `12575.38` | `0.975` | `0.000` | `+0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.214` | `accepted` | `rejected` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `2782.30` | `0.982` | `0.000` | `+0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.316` | `accepted` | `rejected` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `54952.01` | `0.844` | `0.000` | `+0.844` | `1.000` | `0.907` | `1.000` | `0.763` | `0.000` | `0.111` | `accepted` | `rejected` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `67257.28` | `0.959` | `0.000` | `+0.959` | `1.000` | `0.916` | `1.000` | `0.990` | `0.000` | `0.821` | `accepted` | `rejected` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `65944.78` | `0.757` | `0.000` | `+0.757` | `0.647` | `0.948` | `1.000` | `1.000` | `0.000` | `0.866` | `soft_accepted` | `rejected` | missing_exact_anchors | kubectl apply -f k8s/deployment.yaml --server-side | - |
| `kubectl-02` | `recall` | `kubectl` | `113834.38` | `0.753` | `0.000` | `+0.753` | `0.789` | `0.925` | `1.000` | `1.000` | `0.000` | `0.275` | `soft_accepted` | `rejected` | missing_exact_anchors | ImagePullBackOff | - |
| `kubectl-03` | `summary` | `kubectl` | `47526.26` | `0.987` | `0.000` | `+0.987` | `1.000` | `0.968` | `1.000` | `1.000` | `0.000` | `0.640` | `accepted` | `rejected` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `88866.93` | `0.585` | `0.000` | `+0.585` | `1.000` | `0.920` | `0.500` | `0.396` | `0.000` | `0.122` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `terraform-01` | `summary` | `terraform` | `110634.35` | `0.750` | `0.000` | `+0.750` | `0.647` | `0.928` | `1.000` | `1.000` | `0.000` | `0.232` | `soft_accepted` | `rejected` | missing_exact_anchors | terraform validate | - |
| `terraform-02` | `recall` | `terraform` | `62351.57` | `0.944` | `0.000` | `+0.944` | `1.000` | `0.932` | `1.000` | `0.931` | `0.000` | `0.569` | `accepted` | `rejected` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `8449.05` | `0.989` | `0.000` | `+0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.282` | `accepted` | `rejected` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `14051.71` | `0.784` | `0.000` | `+0.784` | `0.732` | `0.974` | `1.000` | `1.000` | `0.000` | `0.341` | `soft_accepted` | `rejected` | missing_exact_anchors | Test assertion failed, expected t3.small default | - |
| `mixed-01` | `recall` | `mixed` | `7957.35` | `0.988` | `0.000` | `+0.988` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.229` | `accepted` | `rejected` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `26552.66` | `0.888` | `0.000` | `+0.888` | `1.000` | `0.886` | `1.000` | `0.908` | `0.000` | `0.143` | `accepted` | `rejected` | - | - | - |
| `git-01` | `recall` | `git` | `10503.83` | `0.974` | `0.000` | `+0.974` | `1.000` | `0.894` | `1.000` | `1.000` | `0.000` | `0.183` | `accepted` | `rejected` | - | - | - |
| `git-02` | `recall` | `git` | `27052.90` | `0.864` | `0.000` | `+0.864` | `1.000` | `0.867` | `1.000` | `0.816` | `0.000` | `0.140` | `accepted` | `rejected` | - | - | - |
| `git-03` | `recall` | `git` | `93899.30` | `0.855` | `0.000` | `+0.855` | `1.000` | `0.937` | `1.000` | `0.770` | `0.000` | `0.112` | `accepted` | `rejected` | - | - | - |
| `curl-01` | `recall` | `curl` | `10109.61` | `0.989` | `0.000` | `+0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.228` | `accepted` | `rejected` | - | - | - |
| `curl-02` | `recall` | `curl` | `14829.26` | `0.983` | `0.000` | `+0.983` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.163` | `accepted` | `rejected` | - | - | - |
| `ssh-01` | `summary` | `ssh` | `11172.47` | `0.978` | `0.000` | `+0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `0.000` | `0.199` | `accepted` | `rejected` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `21344.79` | `0.970` | `0.000` | `+0.970` | `1.000` | `0.925` | `1.000` | `1.000` | `0.000` | `0.151` | `accepted` | `rejected` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `52641.01` | `0.842` | `0.000` | `+0.842` | `1.000` | `0.915` | `1.000` | `0.828` | `0.000` | `0.137` | `accepted` | `rejected` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `4093.70` | `0.962` | `0.000` | `+0.962` | `1.000` | `0.904` | `1.000` | `1.000` | `0.000` | `0.285` | `accepted` | `rejected` | - | - | - |
| `apt-01` | `summary` | `apt` | `24600.93` | `0.848` | `0.000` | `+0.848` | `1.000` | `0.932` | `1.000` | `0.827` | `0.000` | `0.140` | `accepted` | `rejected` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `23976.80` | `0.990` | `0.000` | `+0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.219` | `accepted` | `rejected` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `22361.45` | `0.963` | `0.000` | `+0.963` | `1.000` | `0.907` | `1.000` | `1.000` | `0.000` | `0.159` | `accepted` | `rejected` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `56857.19` | `0.882` | `0.000` | `+0.882` | `1.000` | `0.927` | `1.000` | `0.877` | `0.000` | `0.115` | `accepted` | `rejected` | - | - | - |
| `javac-01` | `recall` | `javac` | `21524.18` | `0.984` | `0.000` | `+0.984` | `1.000` | `0.934` | `1.000` | `1.000` | `0.000` | `0.131` | `accepted` | `rejected` | - | - | - |
| `maven-01` | `recall` | `maven` | `49851.77` | `0.890` | `0.000` | `+0.890` | `1.000` | `0.881` | `1.000` | `0.859` | `0.000` | `0.136` | `accepted` | `rejected` | - | - | - |
| `maven-02` | `summary` | `maven` | `68616.66` | `0.941` | `0.000` | `+0.941` | `1.000` | `0.946` | `1.000` | `0.949` | `0.000` | `0.508` | `accepted` | `rejected` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `32649.71` | `0.853` | `0.000` | `+0.853` | `1.000` | `0.932` | `1.000` | `0.767` | `0.000` | `0.117` | `accepted` | `rejected` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `29573.90` | `0.863` | `0.000` | `+0.863` | `1.000` | `0.916` | `1.000` | `0.858` | `0.000` | `0.127` | `accepted` | `rejected` | - | - | - |
| `cargo-01` | `recall` | `cargo` | `22319.96` | `0.949` | `0.000` | `+0.949` | `1.000` | `0.919` | `1.000` | `0.946` | `0.000` | `0.149` | `accepted` | `rejected` | - | - | - |
| `cargo-02` | `recall` | `cargo` | `90992.15` | `0.984` | `0.000` | `+0.984` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.675` | `accepted` | `rejected` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `96736.51` | `0.596` | `0.000` | `+0.596` | `1.000` | `0.923` | `0.500` | `0.412` | `0.000` | `0.113` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `npm-04` | `summary` | `npm` | `31178.34` | `0.830` | `0.000` | `+0.830` | `1.000` | `0.924` | `1.000` | `0.805` | `0.000` | `0.130` | `accepted` | `rejected` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `13895.26` | `0.973` | `0.000` | `+0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.217` | `accepted` | `rejected` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `55900.24` | `0.766` | `0.000` | `+0.766` | `0.727` | `0.923` | `1.000` | `1.000` | `0.000` | `0.246` | `soft_accepted` | `rejected` | missing_exact_anchors | ESLint found too many warnings | - |
| `python-runtime-01` | `recall` | `python-runtime` | `50716.87` | `0.610` | `0.000` | `+0.610` | `1.000` | `0.937` | `0.500` | `0.429` | `0.000` | `0.137` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `pytest-06` | `summary` | `pytest` | `41870.76` | `0.838` | `0.000` | `+0.838` | `1.000` | `0.912` | `1.000` | `0.824` | `0.000` | `0.119` | `accepted` | `rejected` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `25157.28` | `0.972` | `0.000` | `+0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `0.000` | `0.217` | `accepted` | `rejected` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `12437.39` | `0.974` | `0.000` | `+0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.230` | `accepted` | `rejected` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `36272.10` | `0.842` | `0.000` | `+0.842` | `1.000` | `0.906` | `1.000` | `0.833` | `0.000` | `0.129` | `accepted` | `rejected` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `4007.58` | `0.983` | `0.000` | `+0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.308` | `accepted` | `rejected` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `15488.86` | `0.821` | `0.000` | `+0.821` | `1.000` | `0.915` | `1.000` | `1.000` | `0.000` | `0.256` | `soft_accepted` | `rejected` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `8303.55` | `0.991` | `0.000` | `+0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.251` | `accepted` | `rejected` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `10325.65` | `0.993` | `0.000` | `+0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.236` | `accepted` | `rejected` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `22016.41` | `0.917` | `0.000` | `+0.917` | `1.000` | `0.913` | `1.000` | `0.934` | `0.000` | `0.139` | `accepted` | `rejected` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `33716.85` | `0.834` | `0.000` | `+0.834` | `1.000` | `0.887` | `1.000` | `0.832` | `0.000` | `0.119` | `accepted` | `rejected` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `6949.05` | `0.985` | `0.000` | `+0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.255` | `accepted` | `rejected` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `5272.12` | `0.987` | `0.000` | `+0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.235` | `accepted` | `rejected` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `10206.31` | `0.992` | `0.000` | `+0.992` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.291` | `accepted` | `rejected` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `16726.94` | `0.968` | `0.000` | `+0.968` | `1.000` | `0.919` | `1.000` | `1.000` | `0.000` | `0.165` | `accepted` | `rejected` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `8566.63` | `0.983` | `0.000` | `+0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.256` | `accepted` | `rejected` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `9956.94` | `0.984` | `0.000` | `+0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.230` | `accepted` | `rejected` | - | - | - |
| `redis-01` | `summary` | `redis` | `28169.49` | `0.935` | `0.000` | `+0.935` | `1.000` | `0.948` | `1.000` | `0.940` | `0.000` | `0.273` | `accepted` | `rejected` | - | - | - |
| `redis-02` | `recall` | `redis` | `5141.42` | `0.989` | `0.000` | `+0.989` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.309` | `accepted` | `rejected` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `135746.20` | `0.899` | `0.000` | `+0.899` | `1.000` | `0.894` | `1.000` | `0.868` | `0.000` | `0.148` | `accepted` | `rejected` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `13455.05` | `0.975` | `0.000` | `+0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.226` | `accepted` | `rejected` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `33939.90` | `0.967` | `0.000` | `+0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.920` | `accepted` | `rejected` | - | - | - |
| `make-01` | `summary` | `make` | `24361.86` | `0.901` | `0.000` | `+0.901` | `1.000` | `0.925` | `1.000` | `0.906` | `0.000` | `0.150` | `accepted` | `rejected` | - | - | - |
| `tar-01` | `summary` | `tar` | `9188.67` | `0.982` | `0.000` | `+0.982` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.196` | `accepted` | `rejected` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `27110.69` | `0.868` | `0.000` | `+0.868` | `1.000` | `0.942` | `1.000` | `0.790` | `0.000` | `0.137` | `accepted` | `rejected` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `11130.11` | `0.975` | `0.000` | `+0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.243` | `accepted` | `rejected` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `49213.31` | `0.994` | `0.000` | `+0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.747` | `accepted` | `rejected` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `8493.62` | `0.986` | `0.000` | `+0.986` | `1.000` | `0.945` | `1.000` | `1.000` | `0.000` | `0.200` | `accepted` | `rejected` | - | - | - |
| `ci-log-01` | `recall` | `ci-log` | `20071.18` | `0.700` | `0.000` | `+0.700` | `0.647` | `0.930` | `1.000` | `1.000` | `0.000` | `0.208` | `soft_accepted` | `rejected` | missing_exact_anchors | helm upgrade --install payments-api charts/payments-api --namespace prod-payments | - |
| `package-manager-01` | `recall` | `package-manager` | `52164.19` | `0.872` | `0.000` | `+0.872` | `1.000` | `0.958` | `1.000` | `0.792` | `0.000` | `0.112` | `accepted` | `rejected` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `17345.65` | `0.979` | `0.000` | `+0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.179` | `accepted` | `rejected` | - | - | - |
| `build-log-01` | `summary` | `build-log` | `10906.86` | `0.956` | `0.000` | `+0.956` | `1.000` | `0.890` | `1.000` | `1.000` | `0.000` | `0.232` | `accepted` | `rejected` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `4945.89` | `0.586` | `0.000` | `+0.586` | `0.000` | `0.849` | `1.000` | `1.000` | `0.000` | `0.454` | `soft_accepted` | `rejected` | missing_exact_anchors | Dockerfile:18, COPY apps/web ./apps/web, "/apps/web": not found | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `50644.24` | `0.319` | `0.000` | `+0.319` | `1.000` | `0.627` | `0.250` | `0.187` | `0.000` | `0.161` | `accepted` | `rejected` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `171999.87` | `0.958` | `0.000` | `+0.958` | `1.000` | `0.859` | `1.000` | `1.000` | `0.000` | `0.749` | `accepted` | `rejected` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `4141.91` | `0.679` | `0.000` | `+0.679` | `0.129` | `0.291` | `1.000` | `1.000` | `0.000` | `0.474` | `soft_accepted` | `rejected` | missing_exact_anchors | search endpoint failed after 2 attempts, https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `23792.89` | `0.130` | `0.000` | `+0.130` | `1.000` | `0.191` | `0.000` | `0.000` | `0.000` | `0.119` | `accepted` | `rejected` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `77094.65` | `0.191` | `0.000` | `+0.191` | `1.000` | `0.685` | `0.000` | `0.000` | `0.000` | `0.378` | `accepted` | `rejected` | - | - | - |
| `structured-output-03` | `structured` | `structured-output` | `70883.18` | `0.000` | `0.000` | `+0.000` | `0.929` | `0.238` | `0.000` | `0.000` | `0.000` | `0.696` | `rejected` | `rejected` | structured_contract_breakage | createSession › rejects expired refresh token | qwen3 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- createSession › rejects expired refresh token - "refresh token expired" - calculateTax › uses EU VAT for DE customer - "Expected: 19\\nReceived: 0"' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- src/auth/session.test.ts - "refresh token expired" - src/billing/tax.test.ts - "invalid refresh token" - calculateTax › uses EU VAT for DE customer - Expec...' |
| `structured-output-04` | `structured` | `structured-output` | `12681.23` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.147` | `accepted` | `rejected` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `12733.69` | `0.850` | `0.000` | `+0.850` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.252` | `soft_accepted` | `rejected` | verbatim_alignment_weak | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `118221.96` | `0.216` | `0.000` | `+0.216` | `0.714` | `0.311` | `0.267` | `0.267` | `0.000` | `0.402` | `soft_accepted` | `rejected` | missing_exact_anchors | SearchBox debounces network query before fetch | - |
| `exact-format-03` | `exact_format` | `exact-format` | `122788.50` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.370` | `accepted` | `rejected` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `25836.28` | `0.598` | `0.000` | `+0.598` | `0.778` | `0.898` | `0.500` | `0.500` | `0.000` | `0.176` | `soft_accepted` | `rejected` | missing_exact_anchors, plain_text_style_mismatch | shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `35352.11` | `0.761` | `0.000` | `+0.761` | `0.750` | `0.896` | `1.000` | `1.000` | `0.000` | `0.186` | `soft_accepted` | `rejected` | missing_exact_anchors | AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `56432.74` | `0.682` | `0.000` | `+0.682` | `1.000` | `0.686` | `0.667` | `0.604` | `0.000` | `0.499` | `accepted` | `rejected` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `30295.90` | `0.927` | `0.000` | `+0.927` | `1.000` | `0.937` | `1.000` | `0.900` | `0.000` | `0.147` | `accepted` | `rejected` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `84457.44` | `0.980` | `0.000` | `+0.980` | `1.000` | `0.919` | `1.000` | `1.000` | `0.000` | `0.569` | `accepted` | `rejected` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `80531.68` | `0.977` | `0.000` | `+0.977` | `1.000` | `0.909` | `1.000` | `1.000` | `0.000` | `0.547` | `accepted` | `rejected` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `36949.36` | `0.655` | `0.000` | `+0.655` | `1.000` | `0.924` | `0.500` | `0.500` | `0.000` | `0.172` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `73440.61` | `0.945` | `0.000` | `+0.945` | `1.000` | `0.919` | `1.000` | `0.940` | `0.000` | `0.553` | `accepted` | `rejected` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `5793.03` | `0.983` | `0.000` | `+0.983` | `1.000` | `0.932` | `1.000` | `1.000` | `0.000` | `0.209` | `accepted` | `rejected` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `6889.19` | `0.987` | `0.000` | `+0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.207` | `accepted` | `rejected` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `7726.15` | `0.988` | `0.000` | `+0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.208` | `accepted` | `rejected` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `20081.87` | `0.983` | `0.000` | `+0.983` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.182` | `accepted` | `rejected` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `8116.72` | `0.989` | `0.000` | `+0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.199` | `accepted` | `rejected` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `6509.53` | `0.762` | `0.000` | `+0.762` | `0.789` | `0.966` | `1.000` | `1.000` | `0.000` | `0.369` | `soft_accepted` | `rejected` | missing_exact_anchors | ERR_PNPM_OUTDATED_LOCKFILE | - |
| `swift-01` | `recall` | `swift` | `3918.56` | `0.623` | `0.000` | `+0.623` | `0.512` | `0.809` | `1.000` | `1.000` | `0.000` | `0.319` | `soft_accepted` | `rejected` | missing_exact_anchors | UserDecoderTests testMissingAvatarUsesPlaceholder, Tests/UserDecoderTests.swift:47, XCTAssertEqual failed | - |
| `elixir-01` | `recall` | `elixir` | `6021.10` | `0.985` | `0.000` | `+0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.209` | `accepted` | `rejected` | - | - | - |
| `rails-01` | `recall` | `rails` | `22137.55` | `0.793` | `0.000` | `+0.793` | `0.882` | `0.943` | `1.000` | `1.000` | `0.000` | `0.280` | `soft_accepted` | `rejected` | missing_exact_anchors | 20260518093012 AddIndexToEventsRequestId | - |
| `phpunit-01` | `recall` | `phpunit` | `14268.05` | `0.692` | `0.000` | `+0.692` | `0.638` | `0.906` | `1.000` | `1.000` | `0.000` | `0.244` | `soft_accepted` | `rejected` | missing_exact_anchors | Tests\Billing\InvoiceTotalTest::testAppliesCreditBeforeTax, Failed asserting that '88.00' is identical to '86.40' | - |
| `nginx-03` | `recall` | `nginx` | `10937.17` | `0.979` | `0.000` | `+0.979` | `1.000` | `0.916` | `1.000` | `1.000` | `0.000` | `0.217` | `accepted` | `rejected` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `11478.11` | `0.982` | `0.000` | `+0.982` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.164` | `accepted` | `rejected` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `65851.29` | `0.929` | `0.000` | `+0.929` | `1.000` | `0.931` | `1.000` | `0.906` | `0.000` | `0.487` | `accepted` | `rejected` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `33635.93` | `0.982` | `0.000` | `+0.982` | `1.000` | `0.928` | `1.000` | `1.000` | `0.000` | `0.152` | `accepted` | `rejected` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `17714.16` | `0.984` | `0.000` | `+0.984` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.163` | `accepted` | `rejected` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `15285.72` | `0.944` | `0.000` | `+0.944` | `1.000` | `0.931` | `1.000` | `0.932` | `0.000` | `0.166` | `accepted` | `rejected` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `17356.23` | `0.972` | `0.000` | `+0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `0.000` | `0.198` | `accepted` | `rejected` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `6858.15` | `0.963` | `0.000` | `+0.963` | `1.000` | `0.907` | `1.000` | `1.000` | `0.000` | `0.234` | `accepted` | `rejected` | - | - | - |
| `npm-05` | `summary` | `npm` | `84191.82` | `0.949` | `0.000` | `+0.949` | `1.000` | `0.871` | `1.000` | `1.000` | `0.000` | `0.595` | `accepted` | `rejected` | - | - | - |
| `helm-01` | `summary` | `helm` | `24034.78` | `0.971` | `0.000` | `+0.971` | `1.000` | `0.928` | `1.000` | `1.000` | `0.000` | `0.756` | `accepted` | `rejected` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `125523.45` | `0.951` | `0.000` | `+0.951` | `1.000` | `0.877` | `1.000` | `1.000` | `0.000` | `0.251` | `accepted` | `rejected` | - | - | - |
| `k6-01` | `summary` | `k6` | `50082.60` | `0.652` | `0.000` | `+0.652` | `0.304` | `0.854` | `1.000` | `1.000` | `0.000` | `0.387` | `soft_accepted` | `rejected` | missing_exact_anchors | smoke.js, checks, http_req_duration, avg | - |
| `composer-01` | `summary` | `composer` | `45485.60` | `0.938` | `0.000` | `+0.938` | `1.000` | `0.939` | `1.000` | `0.949` | `0.000` | `0.296` | `accepted` | `rejected` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `65743.16` | `0.945` | `0.000` | `+0.945` | `1.000` | `0.862` | `1.000` | `1.000` | `0.000` | `0.931` | `accepted` | `rejected` | - | - | - |
| `make-02` | `summary` | `make` | `16808.23` | `0.644` | `0.000` | `+0.644` | `1.000` | `0.914` | `0.500` | `0.500` | `0.000` | `0.195` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `15145.52` | `0.969` | `0.000` | `+0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.189` | `accepted` | `rejected` | - | - | - |
| `jest-01` | `summary` | `jest` | `113327.62` | `0.953` | `0.000` | `+0.953` | `1.000` | `0.882` | `1.000` | `1.000` | `0.000` | `0.287` | `accepted` | `rejected` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `7744.69` | `0.949` | `0.000` | `+0.949` | `1.000` | `0.872` | `1.000` | `1.000` | `0.000` | `0.274` | `accepted` | `rejected` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `7426.00` | `0.973` | `0.000` | `+0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `0.000` | `0.339` | `accepted` | `rejected` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `98646.29` | `0.969` | `0.000` | `+0.969` | `1.000` | `0.922` | `1.000` | `1.000` | `0.000` | `0.563` | `accepted` | `rejected` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `53017.15` | `0.778` | `0.000` | `+0.778` | `0.778` | `0.927` | `1.000` | `1.000` | `0.000` | `0.402` | `soft_accepted` | `rejected` | missing_exact_anchors | Falsifying, example | - |
| `eslint-05` | `instruction_following` | `eslint` | `13551.05` | `0.413` | `0.000` | `+0.413` | `0.815` | `0.623` | `0.400` | `0.324` | `0.000` | `0.200` | `accepted` | `rejected` | - | src/api.ts | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `48623.99` | `0.943` | `0.000` | `+0.943` | `1.000` | `0.810` | `1.000` | `1.000` | `0.000` | `0.662` | `accepted` | `rejected` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `7700.22` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `0.617` | `0.000` | `0.000` | `0.315` | `rejected` | `rejected` | exact_lines_contract_breakage | - | qwen3 output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- tests/test_api.py::test_create_user - tests/test_auth.py::test_refresh_token_expiry' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- tests/test_api.py::test_create_user - tests/test_auth.py::test_refresh_token_expiry' |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `9249.26` | `0.654` | `0.000` | `+0.654` | `1.000` | `0.622` | `0.667` | `0.587` | `0.000` | `0.248` | `accepted` | `rejected` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `4135.66` | `0.976` | `0.000` | `+0.976` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.299` | `accepted` | `rejected` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `88223.67` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `0.750` | `0.000` | `0.000` | `0.602` | `rejected` | `rejected` | exact_lines_contract_breakage | - | qwen3 output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- npm ERR! code ENOTEMPTY - npm ERR! syscall rename - npm ERR! path /repo/node_modules/esbuild - npm ERR! dest /repo/node_modules/.esbuild.DELETE - npm ERR! ...' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- npm ERR! code ENOTEMPTY - npm ERR! syscall rename - npm ERR! path /repo/node_modules/esbuild - npm ERR! dest /repo/node_modules/.esbuild.DELETE' |
| `docker-build-03` | `instruction_following` | `docker-build` | `20776.73` | `0.178` | `0.000` | `+0.178` | `0.200` | `0.312` | `0.277` | `0.277` | `0.000` | `0.424` | `soft_accepted` | `rejected` | missing_exact_anchors | [deps 4/4], pnpm install --frozen-lockfile, exit code: 1 | - |
| `terraform-09` | `instruction_following` | `terraform` | `74252.81` | `0.607` | `0.000` | `+0.607` | `1.000` | `0.712` | `0.500` | `0.500` | `0.000` | `0.943` | `accepted` | `rejected` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `17187.83` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.971` | `0.000` | `0.000` | `0.000` | `0.246` | `rejected` | `rejected` | structured_contract_breakage | - | qwen3 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- /repo/src/main/java/UserService.java:[44,17] cannot find symbol symbol: method findByEmail(java.lang.String) - /repo/src/main/java/UserController.java:[28,...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- /repo/src/main/java/UserService.java:[44,17] cannot find symbol symbol: method findByEmail(java.lang.String) - /repo/src/main/java/UserController.java:[28,...' |
| `playwright-01` | `instruction_following` | `playwright` | `58953.43` | `0.644` | `0.000` | `+0.644` | `1.000` | `0.860` | `0.500` | `0.500` | `0.000` | `0.318` | `accepted` | `rejected` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `5064.78` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `0.617` | `0.000` | `0.000` | `0.366` | `rejected` | `rejected` | exact_lines_contract_breakage | - | qwen3 output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- src/App.tsx - src/api/client.ts' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- src/App.tsx - src/api/client.ts' |
| `kubectl-08` | `instruction_following` | `kubectl` | `53695.48` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.000` | `0.361` | `0.000` | `0.000` | `0.652` | `rejected` | `rejected` | exact_lines_contract_breakage | - | qwen3 output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- api-7d9f - redis-0' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- api-7d9f - redis-0 - worker-5b8c - CrashLoopBackOff - migrator-9z1q - Error' |
| `cargo-04` | `instruction_following` | `cargo` | `23173.59` | `0.365` | `0.000` | `+0.365` | `0.833` | `0.672` | `0.333` | `0.321` | `0.000` | `0.194` | `soft_accepted` | `rejected` | missing_exact_anchors | src/auth.rs:88 | - |
| `shell-01` | `instruction_following` | `shell` | `4479.58` | `0.231` | `0.000` | `+0.231` | `0.643` | `0.320` | `0.297` | `0.297` | `0.000` | `0.414` | `soft_accepted` | `rejected` | missing_exact_anchors | Permission denied (13) | - |
| `pyright-01` | `structured` | `pyright` | `18822.21` | `0.170` | `0.000` | `+0.170` | `0.867` | `0.759` | `0.000` | `0.000` | `0.000` | `0.281` | `soft_accepted` | `rejected` | missing_exact_anchors | code | - |
| `terraform-10` | `structured` | `terraform` | `87085.70` | `0.702` | `0.000` | `+0.702` | `1.000` | `0.432` | `0.750` | `0.750` | `0.000` | `0.532` | `accepted` | `rejected` | - | - | - |
| `junit-01` | `structured` | `junit` | `17160.86` | `0.806` | `0.000` | `+0.806` | `0.857` | `0.922` | `1.000` | `1.000` | `0.000` | `0.229` | `soft_accepted` | `rejected` | missing_exact_anchors | dividesByZero | - |
| `kubernetes-03` | `structured` | `kubernetes` | `19256.52` | `0.176` | `0.000` | `+0.176` | `1.000` | `0.667` | `0.000` | `0.000` | `0.000` | `0.129` | `accepted` | `rejected` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `17968.03` | `0.611` | `0.000` | `+0.611` | `1.000` | `0.197` | `0.828` | `0.683` | `0.000` | `0.130` | `accepted` | `rejected` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `6396.38` | `0.758` | `0.000` | `+0.758` | `1.000` | `0.704` | `0.714` | `0.714` | `0.000` | `0.356` | `accepted` | `rejected` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `124655.38` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.710` | `0.000` | `0.000` | `0.000` | `0.156` | `rejected` | `rejected` | structured_contract_breakage | - | qwen3 output validation failed: model did not stop thinking before reaching the output limit. first_pass='--- - failed_tests: TestParseAmount, TestFormatCurrency - name: TestParseAmount - location: amount_test.go:22 - amount_test.go:22: got 10.0 want 10.00 - mess...' repair_pass="<think> Okay, let's see. The user wants me to correct the compression answer. The previous answer had some issues with the structure and the tokens. The raw ..." |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `98511.23` | `0.000` | `0.000` | `+0.000` | `0.500` | `0.550` | `0.000` | `0.000` | `0.000` | `0.772` | `rejected` | `rejected` | structured_contract_breakage | Job, Step, Exit | qwen3 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='job|lint|success|22s job|test|failed|step="Run unit tests"|exit=1 job|build|success|49s job|deploy|failed|step="Upload artifact"|exit=1' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='job|lint|success|22s job|test|failed|step="Run unit tests"|exit=1 job|build|success|49s job|deploy|failed|step="Upload artifact"|exit=1 ---' |
| `npm-07` | `structured` | `npm` | `10971.59` | `0.572` | `0.000` | `+0.572` | `1.000` | `0.350` | `0.583` | `0.583` | `0.000` | `0.188` | `accepted` | `rejected` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `13101.26` | `0.940` | `0.000` | `+0.940` | `1.000` | `0.818` | `1.000` | `0.984` | `0.000` | `0.206` | `accepted` | `rejected` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `9580.50` | `0.217` | `0.000` | `+0.217` | `1.000` | `0.172` | `0.125` | `0.125` | `0.000` | `0.177` | `accepted` | `rejected` | - | - | - |
| `playwright-02` | `structured` | `playwright` | `49318.51` | `0.313` | `0.000` | `+0.313` | `1.000` | `0.189` | `0.266` | `0.266` | `0.000` | `0.847` | `accepted` | `rejected` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `12428.14` | `0.177` | `0.000` | `+0.177` | `1.000` | `0.546` | `0.000` | `0.000` | `0.000` | `0.191` | `accepted` | `rejected` | - | - | - |
| `vite-01` | `structured` | `vite` | `17707.51` | `0.108` | `0.000` | `+0.108` | `1.000` | `0.219` | `0.000` | `0.000` | `0.000` | `0.233` | `accepted` | `rejected` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `4663.40` | `0.850` | `0.000` | `+0.850` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.332` | `soft_accepted` | `rejected` | verbatim_alignment_weak | - | - |
| `git-04` | `exact_format` | `git` | `5788.11` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.413` | `accepted` | `rejected` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `101681.28` | `0.398` | `0.000` | `+0.398` | `0.000` | `0.313` | `0.617` | `0.617` | `0.000` | `0.964` | `soft_accepted` | `rejected` | missing_exact_anchors | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | - |
| `npm-08` | `exact_format` | `npm` | `1498.94` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.512` | `accepted` | `rejected` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `79646.79` | `0.086` | `0.000` | `+0.086` | `0.000` | `0.233` | `0.150` | `0.150` | `0.000` | `0.531` | `soft_accepted` | `rejected` | missing_exact_anchors | github.com/acme/shop/checkout, TestCheckoutAppliesCoupon | - |
| `kubectl-09` | `exact_format` | `kubectl` | `58546.21` | `0.494` | `0.000` | `+0.494` | `1.000` | `0.306` | `0.500` | `0.500` | `0.000` | `0.798` | `accepted` | `rejected` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `3980.66` | `0.711` | `0.000` | `+0.711` | `1.000` | `0.000` | `0.660` | `0.660` | `0.000` | `0.283` | `accepted` | `rejected` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `1296.02` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.531` | `accepted` | `rejected` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `163288.45` | `0.065` | `0.000` | `+0.065` | `0.000` | `0.237` | `0.150` | `0.114` | `0.000` | `0.410` | `soft_accepted` | `rejected` | missing_exact_anchors | 20260518133742 | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `71406.41` | `0.660` | `0.000` | `+0.660` | `0.444` | `0.789` | `1.000` | `1.000` | `0.000` | `0.434` | `soft_accepted` | `rejected` | missing_exact_anchors | /repo/scripts/email.py | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `18744.69` | `0.695` | `0.000` | `+0.695` | `0.444` | `0.892` | `1.000` | `1.000` | `0.000` | `0.253` | `soft_accepted` | `rejected` | missing_exact_anchors | url: string | - |
| `postgres-05` | `explanation` | `postgres` | `8587.92` | `0.895` | `0.000` | `+0.895` | `1.000` | `0.650` | `1.000` | `1.000` | `0.000` | `0.299` | `accepted` | `rejected` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `2712.06` | `0.768` | `0.000` | `+0.768` | `0.818` | `0.874` | `1.000` | `1.000` | `0.000` | `0.446` | `soft_accepted` | `rejected` | missing_exact_anchors | outside the build context | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `37990.61` | `0.974` | `0.000` | `+0.974` | `1.000` | `0.934` | `1.000` | `1.000` | `0.000` | `0.709` | `accepted` | `rejected` | - | - | - |
| `rust-01` | `explanation` | `rust` | `16700.26` | `0.617` | `0.000` | `+0.617` | `1.000` | `0.825` | `0.500` | `0.500` | `0.000` | `0.179` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `59343.46` | `0.936` | `0.000` | `+0.936` | `1.000` | `0.841` | `1.000` | `1.000` | `0.000` | `0.636` | `accepted` | `rejected` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `5651.87` | `0.601` | `0.000` | `+0.601` | `0.500` | `0.952` | `1.000` | `0.891` | `0.000` | `0.377` | `soft_accepted` | `rejected` | missing_exact_anchors | error: 'cout' was not declared in this scope | - |
| `testing-01` | `recall` | `testing` | `4419.80` | `0.986` | `0.000` | `+0.986` | `1.000` | `0.946` | `1.000` | `1.000` | `0.000` | `0.360` | `accepted` | `rejected` | - | - | - |
| `testing-02` | `recall` | `testing` | `4066.84` | `0.988` | `0.000` | `+0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `0.000` | `0.370` | `accepted` | `rejected` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `43615.44` | `0.976` | `0.000` | `+0.976` | `1.000` | `0.904` | `1.000` | `1.000` | `0.000` | `0.272` | `accepted` | `rejected` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `30175.82` | `0.989` | `0.000` | `+0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.723` | `accepted` | `rejected` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `60861.50` | `0.991` | `0.000` | `+0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `0.000` | `0.821` | `accepted` | `rejected` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `2656.94` | `0.978` | `0.000` | `+0.978` | `1.000` | `0.912` | `1.000` | `1.000` | `0.000` | `0.424` | `accepted` | `rejected` | - | - | - |
| `ci-01` | `recall` | `ci` | `57245.03` | `0.966` | `0.000` | `+0.966` | `1.000` | `0.865` | `1.000` | `1.000` | `0.000` | `0.739` | `accepted` | `rejected` | - | - | - |
| `testing-03` | `recall` | `testing` | `97849.37` | `0.980` | `0.000` | `+0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `0.000` | `0.642` | `accepted` | `rejected` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `50328.32` | `0.976` | `0.000` | `+0.976` | `1.000` | `0.906` | `1.000` | `1.000` | `0.000` | `0.813` | `accepted` | `rejected` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `41669.75` | `0.977` | `0.000` | `+0.977` | `1.000` | `0.907` | `1.000` | `1.000` | `0.000` | `0.234` | `accepted` | `rejected` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `4202.23` | `0.990` | `0.000` | `+0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.391` | `accepted` | `rejected` | - | - | - |
| `ci-02` | `recall` | `ci` | `55264.79` | `0.975` | `0.000` | `+0.975` | `1.000` | `0.900` | `1.000` | `1.000` | `0.000` | `0.712` | `accepted` | `rejected` | - | - | - |
| `build-01` | `recall` | `build` | `71085.43` | `0.974` | `0.000` | `+0.974` | `1.000` | `0.896` | `1.000` | `1.000` | `0.000` | `0.416` | `accepted` | `rejected` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `39556.23` | `0.976` | `0.000` | `+0.976` | `1.000` | `0.905` | `1.000` | `1.000` | `0.000` | `0.776` | `accepted` | `rejected` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `28663.92` | `0.985` | `0.000` | `+0.985` | `1.000` | `0.939` | `1.000` | `1.000` | `0.000` | `0.904` | `accepted` | `rejected` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `111626.49` | `0.971` | `0.000` | `+0.971` | `1.000` | `0.883` | `1.000` | `1.000` | `0.000` | `0.380` | `accepted` | `rejected` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `47817.25` | `0.991` | `0.000` | `+0.991` | `1.000` | `0.962` | `1.000` | `1.000` | `0.000` | `0.790` | `accepted` | `rejected` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `79026.64` | `0.972` | `0.000` | `+0.972` | `1.000` | `0.888` | `1.000` | `1.000` | `0.000` | `0.968` | `accepted` | `rejected` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `90135.07` | `0.966` | `0.000` | `+0.966` | `1.000` | `0.865` | `1.000` | `1.000` | `0.000` | `0.977` | `accepted` | `rejected` | - | - | - |
| `testing-04` | `recall` | `testing` | `153953.39` | `0.640` | `0.000` | `+0.640` | `0.583` | `0.941` | `1.000` | `0.914` | `0.000` | `0.759` | `soft_accepted` | `rejected` | missing_exact_anchors | Failure/Error | - |
| `build-02` | `recall` | `build` | `54594.15` | `0.976` | `0.000` | `+0.976` | `1.000` | `0.906` | `1.000` | `1.000` | `0.000` | `0.287` | `accepted` | `rejected` | - | - | - |
| `ci-03` | `recall` | `ci` | `174659.87` | `0.832` | `0.000` | `+0.832` | `1.000` | `0.916` | `1.000` | `1.000` | `0.000` | `0.720` | `soft_accepted` | `rejected` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `31730.50` | `0.976` | `0.000` | `+0.976` | `1.000` | `0.905` | `1.000` | `1.000` | `0.000` | `0.948` | `accepted` | `rejected` | - | - | - |
| `build-03` | `summary` | `build` | `4235.14` | `0.896` | `0.000` | `+0.896` | `1.000` | `0.878` | `1.000` | `0.925` | `0.000` | `0.221` | `accepted` | `rejected` | - | - | - |
| `docker-05` | `summary` | `docker` | `3506.69` | `0.886` | `0.000` | `+0.886` | `1.000` | `0.850` | `1.000` | `0.925` | `0.000` | `0.312` | `accepted` | `rejected` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `1664.89` | `0.961` | `0.000` | `+0.961` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.402` | `accepted` | `rejected` | - | - | - |
| `ci-04` | `summary` | `ci` | `2044.13` | `0.953` | `0.000` | `+0.953` | `1.000` | `0.884` | `1.000` | `1.000` | `0.000` | `0.436` | `accepted` | `rejected` | - | - | - |
| `npm-09` | `summary` | `npm` | `34673.62` | `0.969` | `0.000` | `+0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.680` | `accepted` | `rejected` | - | - | - |
| `rust-02` | `summary` | `rust` | `1058.82` | `0.936` | `0.000` | `+0.936` | `1.000` | `0.841` | `1.000` | `1.000` | `0.000` | `0.482` | `accepted` | `rejected` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `5334.05` | `0.662` | `0.000` | `+0.662` | `1.000` | `0.930` | `0.500` | `0.500` | `0.000` | `0.329` | `accepted` | `rejected` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `49064.15` | `0.417` | `0.000` | `+0.417` | `0.500` | `0.590` | `0.500` | `0.500` | `0.000` | `0.414` | `soft_accepted` | `rejected` | missing_exact_anchors | * rerun pytest test_auth.py::TestAuth::test_login | - |
| `ci-05` | `instruction_following` | `ci` | `23448.23` | `0.486` | `0.000` | `+0.486` | `1.000` | `0.995` | `0.500` | `0.362` | `0.000` | `0.280` | `soft_accepted` | `rejected` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `6299.03` | `0.097` | `0.000` | `+0.097` | `0.667` | `0.174` | `0.000` | `0.000` | `0.000` | `0.417` | `soft_accepted` | `rejected` | missing_exact_anchors | found 1 | - |
| `kubernetes-06` | `structured` | `kubernetes` | `9375.71` | `0.143` | `0.000` | `+0.143` | `1.000` | `0.195` | `0.000` | `0.000` | `0.000` | `0.181` | `accepted` | `rejected` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `9128.47` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.175` | `accepted` | `rejected` | - | - | - |
| `network-01` | `exact_format` | `network` | `2828.07` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.443` | `accepted` | `rejected` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `95554.65` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `0.411` | `rejected` | `rejected` | exact_format_contract_breakage | - | qwen3 output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response' |
| `shell-03` | `exact_format` | `shell` | `45401.05` | `0.715` | `0.000` | `+0.715` | `1.000` | `0.667` | `0.635` | `0.540` | `0.000` | `0.294` | `accepted` | `rejected` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `1727.65` | `0.191` | `0.000` | `+0.191` | `1.000` | `0.320` | `0.150` | `0.150` | `0.000` | `0.454` | `accepted` | `rejected` | - | - | - |
| `build-04` | `exact_format` | `build` | `87937.85` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.600` | `0.617` | `0.000` | `0.000` | `0.276` | `rejected` | `rejected` | exact_lines_contract_breakage | - | qwen3 output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- Resources: 1 added - instance_id = "i-0abcd1234efgh" - instance_public_ip = "35.153.12.34"' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- Apply complete! Resources: 1 added, 0 changed, 0 destroyed. - instance_id = "i-0abcd1234efgh" - instance_public_ip = "35.153.12.34"' |
| `build-05` | `exact_format` | `build` | `1268.32` | `0.730` | `0.000` | `+0.730` | `1.000` | `0.333` | `0.750` | `0.750` | `0.000` | `0.467` | `accepted` | `rejected` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `1743.35` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.460` | `accepted` | `rejected` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `23917.35` | `0.949` | `0.000` | `+0.949` | `1.000` | `0.872` | `1.000` | `1.000` | `0.000` | `0.403` | `accepted` | `rejected` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `4838.26` | `0.903` | `0.000` | `+0.903` | `1.000` | `0.872` | `1.000` | `0.937` | `0.000` | `0.352` | `accepted` | `rejected` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `130100.33` | `0.586` | `0.000` | `+0.586` | `0.000` | `0.880` | `1.000` | `0.981` | `0.000` | `0.443` | `soft_accepted` | `rejected` | missing_exact_anchors | pull access denied, repository does not exist | - |
| `runtime-05` | `explanation` | `runtime` | `43073.45` | `0.955` | `0.000` | `+0.955` | `1.000` | `0.887` | `1.000` | `1.000` | `0.000` | `0.858` | `accepted` | `rejected` | - | - | - |
| `ci-06` | `explanation` | `ci` | `2752.47` | `0.977` | `0.000` | `+0.977` | `1.000` | `0.942` | `1.000` | `1.000` | `0.000` | `0.378` | `accepted` | `rejected` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `18439.83` | `0.945` | `0.000` | `+0.945` | `1.000` | `0.863` | `1.000` | `1.000` | `0.000` | `0.952` | `accepted` | `rejected` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `1265.03` | `0.928` | `0.000` | `+0.928` | `1.000` | `0.821` | `1.000` | `1.000` | `0.000` | `0.426` | `accepted` | `rejected` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `27298.60` | `0.963` | `0.000` | `+0.963` | `1.000` | `0.907` | `1.000` | `1.000` | `0.000` | `0.854` | `accepted` | `rejected` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1824.00` | `0.930` | `0.000` | `+0.930` | `1.000` | `0.825` | `1.000` | `1.000` | `0.000` | `0.428` | `accepted` | `rejected` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `22001.77` | `0.960` | `0.000` | `+0.960` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.416` | `accepted` | `rejected` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `26087.87` | `0.950` | `0.000` | `+0.950` | `1.000` | `0.875` | `1.000` | `1.000` | `0.000` | `0.936` | `accepted` | `rejected` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `27125.17` | `0.915` | `0.000` | `+0.915` | `1.000` | `0.878` | `1.000` | `0.950` | `0.000` | `0.734` | `accepted` | `rejected` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `1820.19` | `0.923` | `0.000` | `+0.923` | `1.000` | `0.807` | `1.000` | `1.000` | `0.000` | `0.422` | `accepted` | `rejected` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `1941.74` | `0.946` | `0.000` | `+0.946` | `1.000` | `0.864` | `1.000` | `1.000` | `0.000` | `0.411` | `accepted` | `rejected` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `50612.70` | `0.941` | `0.000` | `+0.941` | `1.000` | `0.853` | `1.000` | `1.000` | `0.000` | `0.413` | `accepted` | `rejected` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `95649.87` | `0.957` | `0.000` | `+0.957` | `1.000` | `0.894` | `1.000` | `1.000` | `0.000` | `0.668` | `accepted` | `rejected` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `18248.23` | `0.920` | `0.000` | `+0.920` | `1.000` | `0.917` | `1.000` | `0.936` | `0.000` | `0.800` | `accepted` | `rejected` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `3826.40` | `0.953` | `0.000` | `+0.953` | `1.000` | `0.918` | `1.000` | `0.981` | `0.000` | `0.361` | `accepted` | `rejected` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `111818.10` | `0.946` | `0.000` | `+0.946` | `1.000` | `0.865` | `1.000` | `1.000` | `0.000` | `0.454` | `accepted` | `rejected` | - | - | - |
| `ci-07` | `structured` | `ci` | `7999.46` | `0.143` | `0.000` | `+0.143` | `1.000` | `0.195` | `0.000` | `0.000` | `0.000` | `0.181` | `accepted` | `rejected` | - | - | - |
| `linting-03` | `structured` | `linting` | `7858.92` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.175` | `accepted` | `rejected` | - | - | - |
| `network-02` | `exact_format` | `network` | `2429.68` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.443` | `accepted` | `rejected` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `4043.03` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `0.411` | `rejected` | `rejected` | exact_format_contract_breakage | - | qwen3 output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response INFO: Retrying...' |
| `shell-07` | `exact_format` | `shell` | `54684.47` | `0.770` | `0.000` | `+0.770` | `1.000` | `0.000` | `0.750` | `0.750` | `0.000` | `0.798` | `accepted` | `rejected` | - | - | - |
| `build-06` | `exact_format` | `build` | `91523.00` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.600` | `0.617` | `0.000` | `0.000` | `0.276` | `rejected` | `rejected` | exact_lines_contract_breakage | - | qwen3 output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- Resources: 1 added - instance_id = "i-0abcd1234efgh" - instance_public_ip = "35.153.12.34"' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- Apply complete! Resources: 1 added, 0 changed, 0 destroyed. - instance_id = "i-0abcd1234efgh" - instance_public_ip = "35.153.12.34"' |
| `runtime-07` | `exact_format` | `runtime` | `2029.36` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.448` | `accepted` | `rejected` | - | - | - |
| `build-07` | `exact_format` | `build` | `52652.26` | `0.574` | `0.000` | `+0.574` | `1.000` | `0.850` | `0.560` | `0.504` | `0.000` | `0.702` | `accepted` | `rejected` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `1935.23` | `0.359` | `0.000` | `+0.359` | `1.000` | `0.304` | `0.355` | `0.355` | `0.000` | `0.487` | `accepted` | `rejected` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `25630.64` | `0.949` | `0.000` | `+0.949` | `1.000` | `0.872` | `1.000` | `1.000` | `0.000` | `0.403` | `accepted` | `rejected` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `4873.57` | `0.903` | `0.000` | `+0.903` | `1.000` | `0.872` | `1.000` | `0.937` | `0.000` | `0.352` | `accepted` | `rejected` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `2094.84` | `0.968` | `0.000` | `+0.968` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.403` | `accepted` | `rejected` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `43543.58` | `0.976` | `0.000` | `+0.976` | `1.000` | `0.940` | `1.000` | `1.000` | `0.000` | `0.358` | `accepted` | `rejected` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `1237.53` | `0.928` | `0.000` | `+0.928` | `1.000` | `0.821` | `1.000` | `1.000` | `0.000` | `0.426` | `accepted` | `rejected` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `20209.14` | `0.892` | `0.000` | `+0.892` | `1.000` | `0.896` | `1.000` | `0.909` | `0.000` | `0.736` | `accepted` | `rejected` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `1323.54` | `0.930` | `0.000` | `+0.930` | `1.000` | `0.825` | `1.000` | `1.000` | `0.000` | `0.443` | `accepted` | `rejected` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `26233.82` | `0.969` | `0.000` | `+0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.430` | `accepted` | `rejected` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `33308.87` | `0.950` | `0.000` | `+0.950` | `1.000` | `0.875` | `1.000` | `1.000` | `0.000` | `0.315` | `accepted` | `rejected` | - | - | - |
