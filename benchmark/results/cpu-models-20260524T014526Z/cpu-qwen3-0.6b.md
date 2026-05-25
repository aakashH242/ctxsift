# cpu-qwen3-0.6b

## Scenario

- track: `cpu`
- phase: `cpu-screen`
- model: `unsloth/Qwen3-0.6B-GGUF`
- quantization: `none`
- device: `cpu`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `20417.37`
- cpu_rss_bytes: `null`
- gpu_peak_bytes: `null`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- recovered_final_score: `53.10`
- raw_final_score: `0.00`
- recovery_lift: `+53.10`
- case_count: `280`
- success_count: `260`
- accepted_count: `193`
- soft_accepted_count: `67`
- rejected_count: `20`
- exact_pass_count: `221`
- avg_inference_ms: `13910.10`
- p95_inference_ms: `30442.86`
- avg_exact_preservation_ratio: `0.907`
- avg_summary_quality_ratio: `0.809`
- avg_format_adherence_score: `0.821`
- avg_instruction_following_score: `0.781`
- avg_brevity_ratio: `0.859`
- avg_thought_leakage_density: `0.005`
- avg_thought_marker_count: `0.04`
- avg_case_score: `0.745`
- p10_case_score: `0.143`
- quality_core: `0.625`
- latency_factor: `0.850`
- final_score: `53.10`
- peak_cpu_rss_bytes: `null`
- peak_gpu_bytes: `null`

### Raw View

- accepted_count: `0`
- soft_accepted_count: `0`
- rejected_count: `280`
- exact_pass_count: `246`
- avg_exact_preservation_ratio: `0.955`
- avg_summary_quality_ratio: `0.695`
- avg_format_adherence_score: `0.379`
- avg_instruction_following_score: `0.000`
- avg_brevity_ratio: `0.123`
- avg_thought_leakage_density: `0.617`
- avg_thought_marker_count: `4.38`
- avg_case_score: `0.000`
- p10_case_score: `0.000`
- quality_core: `0.000`
- final_score: `0.00`

## Cases

| case_id | family | domain | ms | recovered_score | raw_score | lift | preserve | quality | format | instruction | recovered_thought_density | raw_thought_density | recovered_validation | raw_validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `26342.92` | `0.591` | `0.000` | `+0.591` | `1.000` | `0.897` | `0.500` | `0.411` | `0.000` | `0.409` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `python-02` | `summary` | `python` | `20351.60` | `0.613` | `0.000` | `+0.613` | `1.000` | `0.936` | `0.500` | `0.459` | `0.000` | `0.670` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `python-03` | `recall` | `python` | `19155.50` | `0.989` | `0.000` | `+0.989` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.460` | `accepted` | `rejected` | - | - | - |
| `python-04` | `recall` | `python` | `30441.22` | `0.897` | `0.000` | `+0.897` | `1.000` | `0.943` | `1.000` | `0.843` | `0.000` | `0.410` | `accepted` | `rejected` | - | - | - |
| `python-05` | `recall` | `python` | `17031.90` | `0.609` | `0.000` | `+0.609` | `1.000` | `0.953` | `0.500` | `0.423` | `0.000` | `0.488` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `pytest-01` | `recall` | `pytest` | `13698.49` | `0.888` | `0.000` | `+0.888` | `1.000` | `0.935` | `1.000` | `0.830` | `0.000` | `0.501` | `accepted` | `rejected` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `10553.49` | `0.984` | `0.000` | `+0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.856` | `accepted` | `rejected` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `21732.64` | `0.991` | `0.000` | `+0.991` | `1.000` | `0.964` | `1.000` | `1.000` | `0.000` | `0.521` | `accepted` | `rejected` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `8886.35` | `0.991` | `0.000` | `+0.991` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.342` | `accepted` | `rejected` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `25613.06` | `0.573` | `0.000` | `+0.573` | `1.000` | `0.928` | `0.500` | `0.418` | `0.000` | `0.227` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `mypy-01` | `recall` | `mypy` | `14615.87` | `0.989` | `0.000` | `+0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.457` | `accepted` | `rejected` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `10779.22` | `0.879` | `0.000` | `+0.879` | `1.000` | `0.950` | `1.000` | `0.862` | `0.000` | `0.573` | `accepted` | `rejected` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `20962.61` | `0.991` | `0.000` | `+0.991` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.535` | `accepted` | `rejected` | - | - | - |
| `ruff-01` | `recall` | `ruff` | `10787.62` | `0.944` | `0.000` | `+0.944` | `0.911` | `0.938` | `1.000` | `1.000` | `0.000` | `0.488` | `accepted` | `rejected` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `5879.48` | `0.990` | `0.000` | `+0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.530` | `accepted` | `rejected` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `7093.24` | `0.971` | `0.000` | `+0.971` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.546` | `accepted` | `rejected` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `9863.77` | `0.989` | `0.000` | `+0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.671` | `accepted` | `rejected` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `14413.23` | `0.986` | `0.000` | `+0.986` | `1.000` | `0.942` | `1.000` | `1.000` | `0.000` | `0.469` | `accepted` | `rejected` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `12942.63` | `0.682` | `0.000` | `+0.682` | `0.356` | `0.909` | `1.000` | `1.000` | `0.000` | `0.392` | `soft_accepted` | `rejected` | missing_exact_anchors | src/notifications/push.py:6:0, E0401, pywebpush, import-error | - |
| `black-01` | `summary` | `black` | `20346.30` | `0.792` | `0.000` | `+0.792` | `0.800` | `0.956` | `1.000` | `1.000` | `0.000` | `0.882` | `soft_accepted` | `rejected` | missing_exact_anchors | 2 files would be reformatted, 41 files would be left unchanged | - |
| `black-02` | `summary` | `black` | `18063.86` | `0.979` | `0.000` | `+0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.535` | `accepted` | `rejected` | - | - | - |
| `black-03` | `recall` | `black` | `13621.23` | `0.992` | `0.000` | `+0.992` | `1.000` | `0.969` | `1.000` | `1.000` | `0.000` | `0.730` | `accepted` | `rejected` | - | - | - |
| `npm-01` | `recall` | `npm` | `19832.42` | `0.978` | `0.000` | `+0.978` | `1.000` | `0.912` | `1.000` | `1.000` | `0.000` | `0.781` | `accepted` | `rejected` | - | - | - |
| `npm-02` | `summary` | `npm` | `29351.49` | `0.637` | `0.000` | `+0.637` | `0.333` | `0.791` | `1.000` | `1.000` | `0.000` | `0.645` | `soft_accepted` | `rejected` | missing_exact_anchors | ERESOLVE, react@18.2.0, react-dates@21.8.0, peer react@"^17.0.0", --legacy-peer-deps | - |
| `npm-03` | `summary` | `npm` | `11340.12` | `0.887` | `0.000` | `+0.887` | `1.000` | `0.942` | `1.000` | `0.877` | `0.000` | `0.465` | `accepted` | `rejected` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `13813.51` | `0.717` | `0.000` | `+0.717` | `0.684` | `0.945` | `1.000` | `1.000` | `0.000` | `0.892` | `soft_accepted` | `rejected` | missing_exact_anchors | pnpm install --frozen-lockfile | - |
| `pnpm-02` | `summary` | `pnpm` | `8338.57` | `0.982` | `0.000` | `+0.982` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.570` | `accepted` | `rejected` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `9270.73` | `0.983` | `0.000` | `+0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.714` | `accepted` | `rejected` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `9217.94` | `0.981` | `0.000` | `+0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.827` | `accepted` | `rejected` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `10015.32` | `0.946` | `0.000` | `+0.946` | `1.000` | `0.931` | `1.000` | `0.935` | `0.000` | `0.620` | `accepted` | `rejected` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `24877.44` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.870` | `0.500` | `0.000` | `0.645` | `0.645` | `rejected` | `rejected` | unterminated_reasoning_block, control_token_leakage, thought_leakage | - | fallback output validation failed: model did not stop thinking before reaching the output limit. first_pass="<think> Okay, let's see. The user provided a command to compile TypeScript files with specific parameters. The output includes the failing call site, error c..." repair_pass="<think> Okay, let's see. The user provided a previous answer that was invalid. The previous answer was a TypeScript compilation command with some error messa..." |
| `eslint-01` | `recall` | `eslint` | `8639.38` | `0.983` | `0.000` | `+0.983` | `1.000` | `0.931` | `1.000` | `1.000` | `0.000` | `0.727` | `accepted` | `rejected` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `8551.65` | `0.981` | `0.000` | `+0.981` | `1.000` | `0.952` | `1.000` | `1.000` | `0.000` | `0.426` | `accepted` | `rejected` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `33937.26` | `0.525` | `0.000` | `+0.525` | `0.231` | `0.854` | `1.000` | `1.000` | `0.000` | `0.836` | `soft_accepted` | `rejected` | missing_exact_anchors | /workspace/src/hooks/useCart.ts, react-hooks/exhaustive-deps, 1 problem (0 errors, 1 warning), maximum: 0 | - |
| `docker-01` | `recall` | `docker` | `19422.86` | `0.761` | `0.000` | `+0.761` | `0.796` | `0.949` | `1.000` | `1.000` | `0.000` | `0.681` | `soft_accepted` | `rejected` | missing_exact_anchors | /docker/entrypoint.sh | - |
| `docker-02` | `summary` | `docker` | `5828.74` | `0.975` | `0.000` | `+0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.865` | `accepted` | `rejected` | - | - | - |
| `docker-03` | `summary` | `docker` | `18898.82` | `0.977` | `0.000` | `+0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `0.000` | `0.335` | `accepted` | `rejected` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `5275.65` | `0.975` | `0.000` | `+0.975` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.910` | `accepted` | `rejected` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `15110.19` | `0.846` | `0.000` | `+0.846` | `1.000` | `0.908` | `1.000` | `0.765` | `0.000` | `0.226` | `accepted` | `rejected` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `8815.24` | `0.959` | `0.000` | `+0.959` | `1.000` | `0.916` | `1.000` | `0.990` | `0.000` | `0.615` | `accepted` | `rejected` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `12623.61` | `0.840` | `0.000` | `+0.840` | `1.000` | `0.930` | `1.000` | `0.816` | `0.000` | `0.723` | `accepted` | `rejected` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `32229.68` | `0.867` | `0.000` | `+0.867` | `1.000` | `0.941` | `1.000` | `0.790` | `0.000` | `0.314` | `accepted` | `rejected` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `13417.11` | `0.992` | `0.000` | `+0.992` | `1.000` | `0.981` | `1.000` | `1.000` | `0.000` | `0.346` | `accepted` | `rejected` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `17342.16` | `0.905` | `0.000` | `+0.905` | `1.000` | `0.926` | `1.000` | `0.866` | `0.000` | `0.529` | `accepted` | `rejected` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `5129.61` | `0.976` | `0.000` | `+0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.322` | `accepted` | `rejected` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `10277.40` | `0.981` | `0.000` | `+0.981` | `1.000` | `0.924` | `1.000` | `1.000` | `0.000` | `0.663` | `accepted` | `rejected` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `7516.86` | `0.990` | `0.000` | `+0.990` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.568` | `accepted` | `rejected` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `8724.71` | `0.979` | `0.000` | `+0.979` | `1.000` | `0.949` | `1.000` | `1.000` | `0.000` | `0.438` | `accepted` | `rejected` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `17878.10` | `0.715` | `0.000` | `+0.715` | `0.767` | `0.894` | `1.000` | `0.950` | `0.000` | `0.808` | `soft_accepted` | `rejected` | missing_exact_anchors | /workspace/build/.cache/tmp-93f1.json | - |
| `mixed-02` | `summary` | `mixed` | `21250.59` | `0.976` | `0.000` | `+0.976` | `1.000` | `0.939` | `1.000` | `1.000` | `0.000` | `0.315` | `accepted` | `rejected` | - | - | - |
| `git-01` | `recall` | `git` | `8433.69` | `0.980` | `0.000` | `+0.980` | `1.000` | `0.919` | `1.000` | `1.000` | `0.000` | `0.533` | `accepted` | `rejected` | - | - | - |
| `git-02` | `recall` | `git` | `13967.20` | `0.984` | `0.000` | `+0.984` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.573` | `accepted` | `rejected` | - | - | - |
| `git-03` | `recall` | `git` | `13205.65` | `0.918` | `0.000` | `+0.918` | `1.000` | `0.950` | `1.000` | `0.879` | `0.000` | `0.617` | `accepted` | `rejected` | - | - | - |
| `curl-01` | `recall` | `curl` | `11213.96` | `0.892` | `0.000` | `+0.892` | `1.000` | `0.944` | `1.000` | `0.834` | `0.000` | `0.471` | `accepted` | `rejected` | - | - | - |
| `curl-02` | `recall` | `curl` | `18035.72` | `0.983` | `0.000` | `+0.983` | `1.000` | `0.934` | `1.000` | `1.000` | `0.000` | `0.265` | `accepted` | `rejected` | - | - | - |
| `ssh-01` | `summary` | `ssh` | `8450.61` | `0.978` | `0.000` | `+0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `0.000` | `0.422` | `accepted` | `rejected` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `11299.16` | `0.970` | `0.000` | `+0.970` | `1.000` | `0.925` | `1.000` | `1.000` | `0.000` | `0.609` | `accepted` | `rejected` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `21335.69` | `0.972` | `0.000` | `+0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `0.000` | `0.593` | `accepted` | `rejected` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `20873.08` | `0.818` | `0.000` | `+0.818` | `1.000` | `0.884` | `1.000` | `0.810` | `0.000` | `0.466` | `accepted` | `rejected` | - | - | - |
| `apt-01` | `summary` | `apt` | `16130.45` | `0.764` | `0.000` | `+0.764` | `0.714` | `0.927` | `1.000` | `1.000` | `0.000` | `0.586` | `soft_accepted` | `rejected` | missing_exact_anchors | libpq5, postgresql-client-16 | - |
| `dnf-01` | `recall` | `dnf` | `22053.58` | `0.849` | `0.000` | `+0.849` | `1.000` | `0.940` | `1.000` | `0.756` | `0.000` | `0.331` | `accepted` | `rejected` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `9243.93` | `0.962` | `0.000` | `+0.962` | `1.000` | `0.906` | `1.000` | `1.000` | `0.000` | `0.544` | `accepted` | `rejected` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `22288.67` | `0.756` | `0.000` | `+0.756` | `0.667` | `0.931` | `1.000` | `1.000` | `0.000` | `0.260` | `soft_accepted` | `rejected` | missing_exact_anchors | cache_test.go:47 | - |
| `javac-01` | `recall` | `javac` | `10351.90` | `0.984` | `0.000` | `+0.984` | `1.000` | `0.934` | `1.000` | `1.000` | `0.000` | `0.655` | `accepted` | `rejected` | - | - | - |
| `maven-01` | `recall` | `maven` | `23623.16` | `0.988` | `0.000` | `+0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.769` | `accepted` | `rejected` | - | - | - |
| `maven-02` | `summary` | `maven` | `17306.74` | `0.863` | `0.000` | `+0.863` | `1.000` | `0.932` | `1.000` | `0.848` | `0.000` | `0.444` | `accepted` | `rejected` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `9518.98` | `0.872` | `0.000` | `+0.872` | `1.000` | `0.940` | `1.000` | `0.800` | `0.000` | `0.516` | `accepted` | `rejected` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `13827.09` | `0.977` | `0.000` | `+0.977` | `1.000` | `0.943` | `1.000` | `1.000` | `0.000` | `0.341` | `accepted` | `rejected` | - | - | - |
| `cargo-01` | `recall` | `cargo` | `9429.42` | `0.988` | `0.000` | `+0.988` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.429` | `accepted` | `rejected` | - | - | - |
| `cargo-02` | `recall` | `cargo` | `38980.78` | `0.985` | `0.000` | `+0.985` | `1.000` | `0.939` | `1.000` | `1.000` | `0.000` | `0.691` | `accepted` | `rejected` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `23780.81` | `0.991` | `0.000` | `+0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.330` | `accepted` | `rejected` | - | - | - |
| `npm-04` | `summary` | `npm` | `11160.36` | `0.824` | `0.000` | `+0.824` | `1.000` | `0.921` | `1.000` | `0.798` | `0.000` | `0.464` | `accepted` | `rejected` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `11631.39` | `0.973` | `0.000` | `+0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.838` | `accepted` | `rejected` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `14441.85` | `0.766` | `0.000` | `+0.766` | `0.727` | `0.922` | `1.000` | `1.000` | `0.000` | `0.808` | `soft_accepted` | `rejected` | missing_exact_anchors | ESLint found too many warnings | - |
| `python-runtime-01` | `recall` | `python-runtime` | `34297.29` | `0.610` | `0.000` | `+0.610` | `1.000` | `0.941` | `0.500` | `0.429` | `0.000` | `0.462` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `pytest-06` | `summary` | `pytest` | `15632.31` | `0.859` | `0.000` | `+0.859` | `1.000` | `0.923` | `1.000` | `0.847` | `0.000` | `0.496` | `accepted` | `rejected` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `7672.47` | `0.973` | `0.000` | `+0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.551` | `accepted` | `rejected` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `40806.74` | `0.674` | `0.000` | `+0.674` | `0.911` | `0.890` | `1.000` | `0.801` | `0.000` | `0.204` | `soft_accepted` | `rejected` | missing_exact_anchors | zod@3.23.8 | - |
| `docker-compose-04` | `summary` | `docker-compose` | `14879.13` | `0.842` | `0.000` | `+0.842` | `1.000` | `0.907` | `1.000` | `0.833` | `0.000` | `0.535` | `accepted` | `rejected` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `8925.12` | `0.970` | `0.000` | `+0.970` | `1.000` | `0.925` | `1.000` | `1.000` | `0.000` | `0.714` | `accepted` | `rejected` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `35186.73` | `0.671` | `0.000` | `+0.671` | `0.353` | `0.878` | `1.000` | `1.000` | `0.000` | `0.619` | `soft_accepted` | `rejected` | missing_exact_anchors | migrate, CrashLoopBackOff, Exit Code:    1 | - |
| `kubectl-07` | `recall` | `kubectl` | `8596.11` | `0.987` | `0.000` | `+0.987` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.723` | `accepted` | `rejected` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `28458.96` | `0.691` | `0.000` | `+0.691` | `0.636` | `0.909` | `1.000` | `1.000` | `0.000` | `0.403` | `soft_accepted` | `rejected` | missing_exact_anchors | terraform plan -lock-timeout=5s -out=tfplan | - |
| `terraform-06` | `summary` | `terraform` | `6685.26` | `0.962` | `0.000` | `+0.962` | `1.000` | `0.906` | `1.000` | `1.000` | `0.000` | `0.309` | `accepted` | `rejected` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `12044.62` | `0.899` | `0.000` | `+0.899` | `1.000` | `0.888` | `1.000` | `0.923` | `0.000` | `0.716` | `accepted` | `rejected` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `6682.64` | `0.979` | `0.000` | `+0.979` | `1.000` | `0.949` | `1.000` | `1.000` | `0.000` | `0.697` | `accepted` | `rejected` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `26770.96` | `0.557` | `0.000` | `+0.557` | `0.000` | `0.765` | `1.000` | `1.000` | `0.000` | `0.510` | `soft_accepted` | `rejected` | missing_exact_anchors | sudo service nginx reload, /etc/letsencrypt/live/example.com/fullchain.pem, cannot load certificate, configuration file /etc/nginx/nginx.conf test failed | - |
| `postgres-01` | `recall` | `postgres` | `5895.92` | `0.992` | `0.000` | `+0.992` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.812` | `accepted` | `rejected` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `14863.78` | `0.986` | `0.000` | `+0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `0.000` | `0.568` | `accepted` | `rejected` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `5992.78` | `0.983` | `0.000` | `+0.983` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.827` | `accepted` | `rejected` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `14915.88` | `0.986` | `0.000` | `+0.986` | `1.000` | `0.965` | `1.000` | `1.000` | `0.000` | `0.383` | `accepted` | `rejected` | - | - | - |
| `redis-01` | `summary` | `redis` | `9374.90` | `0.940` | `0.000` | `+0.940` | `1.000` | `0.949` | `1.000` | `0.946` | `0.000` | `0.726` | `accepted` | `rejected` | - | - | - |
| `redis-02` | `recall` | `redis` | `4807.45` | `0.989` | `0.000` | `+0.989` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.434` | `accepted` | `rejected` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `10002.16` | `0.899` | `0.000` | `+0.899` | `1.000` | `0.895` | `1.000` | `0.868` | `0.000` | `0.479` | `accepted` | `rejected` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `32904.79` | `0.758` | `0.000` | `+0.758` | `0.684` | `0.928` | `1.000` | `1.000` | `0.000` | `0.445` | `soft_accepted` | `rejected` | missing_exact_anchors | pnpm install --frozen-lockfile | - |
| `jenkins-01` | `summary` | `jenkins` | `14886.35` | `0.967` | `0.000` | `+0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.306` | `accepted` | `rejected` | - | - | - |
| `make-01` | `summary` | `make` | `11657.68` | `0.902` | `0.000` | `+0.902` | `1.000` | `0.927` | `1.000` | `0.906` | `0.000` | `0.418` | `accepted` | `rejected` | - | - | - |
| `tar-01` | `summary` | `tar` | `8482.02` | `0.984` | `0.000` | `+0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.664` | `accepted` | `rejected` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `16073.71` | `0.993` | `0.000` | `+0.993` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.627` | `accepted` | `rejected` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `9707.86` | `0.884` | `0.000` | `+0.884` | `1.000` | `0.914` | `1.000` | `0.887` | `0.000` | `0.451` | `accepted` | `rejected` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `19969.88` | `0.758` | `0.000` | `+0.758` | `0.773` | `0.975` | `1.000` | `1.000` | `0.000` | `0.651` | `soft_accepted` | `rejected` | missing_exact_anchors | tests/unit/test_invoice_totals.py:88 | - |
| `compiler-error-01` | `recall` | `compiler-error` | `24368.47` | `0.774` | `0.000` | `+0.774` | `0.851` | `0.910` | `1.000` | `1.000` | `0.000` | `0.510` | `soft_accepted` | `rejected` | missing_exact_anchors | src/router.rs:137:42 | - |
| `ci-log-01` | `recall` | `ci-log` | `20129.42` | `0.793` | `0.000` | `+0.793` | `0.882` | `0.943` | `1.000` | `1.000` | `0.000` | `0.442` | `soft_accepted` | `rejected` | missing_exact_anchors | Deployment.apps "payments-api" is invalid | - |
| `package-manager-01` | `recall` | `package-manager` | `18502.55` | `0.754` | `0.000` | `+0.754` | `0.778` | `0.950` | `1.000` | `1.000` | `0.000` | `0.416` | `soft_accepted` | `rejected` | missing_exact_anchors | --force or --legacy-peer-deps | - |
| `test-summary-01` | `summary` | `test-summary` | `17193.17` | `0.656` | `0.000` | `+0.656` | `0.214` | `0.921` | `1.000` | `1.000` | `0.000` | `0.725` | `soft_accepted` | `rejected` | missing_exact_anchors | github.com/acme/shop/checkout, checkout_test.go:71, total = 42.00, want 37.00, github.com/acme/shop/inventory, worker.go:144 | - |
| `build-log-01` | `summary` | `build-log` | `15750.69` | `0.752` | `0.000` | `+0.752` | `0.750` | `0.867` | `1.000` | `1.000` | `0.000` | `0.810` | `soft_accepted` | `rejected` | missing_exact_anchors | billing-service, cannot find symbol | - |
| `docker-build-02` | `summary` | `docker-build` | `30913.33` | `0.426` | `0.000` | `+0.426` | `0.667` | `0.878` | `0.000` | `0.000` | `0.000` | `0.362` | `soft_accepted` | `rejected` | missing_exact_anchors | Dockerfile:18 | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `28016.23` | `0.407` | `0.000` | `+0.407` | `0.375` | `0.626` | `0.500` | `0.500` | `0.000` | `0.600` | `soft_accepted` | `rejected` | missing_exact_anchors | /repo/web/src/App.tsx, 27:19, /repo/web/src/api/client.ts, 8:10, 33:11 | - |
| `git-review-01` | `instruction_following` | `git-review` | `22132.03` | `0.609` | `0.000` | `+0.609` | `1.000` | `0.722` | `0.500` | `0.500` | `0.000` | `0.349` | `accepted` | `rejected` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `34190.20` | `0.046` | `0.000` | `+0.046` | `0.355` | `0.333` | `0.000` | `0.000` | `0.000` | `0.399` | `soft_accepted` | `rejected` | missing_exact_anchors | https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `32595.85` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.284` | `0.000` | `0.000` | `0.170` | `0.416` | `rejected` | `rejected` | thought_leakage, structured_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['thought_leakage', 'structured_contract_breakage'] first_pass='/work/app/services/payments.py at line 42. The error message says "Argument of type \'str | None\' cannot be assigned to parameter \'customer_id\' of type \'str\' ...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json { "/work/app/services/payments.py": { "line": 42, "error": "Argument of type \'str | None\' cannot be assigned to parameter \'customer_id\' of type \'str\'...' |
| `structured-output-02` | `structured` | `structured-output` | `19469.73` | `0.099` | `0.000` | `+0.099` | `0.095` | `0.570` | `0.000` | `0.000` | `0.000` | `0.499` | `soft_accepted` | `rejected` | missing_exact_anchors | test / integration, port 5432 is already allocated, deploy / preview, Upload artifact, dist/preview | - |
| `structured-output-03` | `structured` | `structured-output` | `22408.16` | `0.168` | `0.000` | `+0.168` | `0.821` | `0.908` | `0.000` | `0.000` | `0.000` | `0.620` | `soft_accepted` | `rejected` | missing_exact_anchors | Received: 0 | - |
| `structured-output-04` | `structured` | `structured-output` | `17639.42` | `0.072` | `0.000` | `+0.072` | `0.312` | `0.164` | `0.000` | `0.000` | `0.000` | `0.651` | `soft_accepted` | `rejected` | missing_exact_anchors | /repo/apps/web/src/main.tsx, /repo/packages/time/src/format.ts, date-fns-tz, /repo/packages/time/src/parse.ts, /repo/apps/web/src/features/flags.ts | - |
| `exact-format-01` | `exact_format` | `exact-format` | `9783.36` | `0.437` | `0.000` | `+0.437` | `1.000` | `0.000` | `0.371` | `0.271` | `0.000` | `0.564` | `accepted` | `rejected` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `22433.39` | `0.000` | `0.000` | `+0.000` | `0.714` | `0.318` | `0.188` | `0.000` | `0.000` | `0.288` | `rejected` | `rejected` | exact_format_contract_breakage | SearchBox debounces network query before fetch | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='FAIL packages/web/src/search/searchBox.test.tsx SearchBox ✓ opens suggestions on focus (31 ms) ✕ debounces network query before fetch (1015 ms) ✓ clears quer...' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='packages/web/src/search/searchBox.test.tsx SearchBox ✓ opens suggestions on focus (31 ms) ✕ debounces network query before fetch (1015 ms) ✓ clears query on ...' |
| `exact-format-03` | `exact_format` | `exact-format` | `15904.80` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.409` | `accepted` | `rejected` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `15020.41` | `0.715` | `0.000` | `+0.715` | `0.556` | `0.880` | `1.000` | `1.000` | `0.000` | `0.607` | `soft_accepted` | `rejected` | missing_exact_anchors | has no attribute 'dumps', shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `13073.12` | `0.763` | `0.000` | `+0.763` | `0.750` | `0.900` | `1.000` | `1.000` | `0.000` | `0.624` | `soft_accepted` | `rejected` | missing_exact_anchors | AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `23742.22` | `0.547` | `0.000` | `+0.547` | `0.750` | `0.701` | `0.667` | `0.608` | `0.000` | `0.685` | `soft_accepted` | `rejected` | missing_exact_anchors | 00000000-0000-0000-0000-000000000000 | - |
| `python-traceback-01` | `recall` | `python-traceback` | `17566.44` | `0.618` | `0.000` | `+0.618` | `0.429` | `0.938` | `1.000` | `1.000` | `0.000` | `0.850` | `soft_accepted` | `rejected` | missing_exact_anchors | /srv/app/app/tasks/email.py, line 92, retries exhausted for queue emails | - |
| `mypy-05` | `recall` | `mypy` | `9982.57` | `0.982` | `0.000` | `+0.982` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.493` | `accepted` | `rejected` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `20778.77` | `0.984` | `0.000` | `+0.984` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.439` | `accepted` | `rejected` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `17876.49` | `0.655` | `0.000` | `+0.655` | `1.000` | `0.922` | `0.500` | `0.500` | `0.000` | `0.437` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `11389.75` | `0.945` | `0.000` | `+0.945` | `1.000` | `0.919` | `1.000` | `0.940` | `0.000` | `0.632` | `accepted` | `rejected` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `10418.57` | `0.957` | `0.000` | `+0.957` | `1.000` | `0.916` | `1.000` | `0.962` | `0.000` | `0.628` | `accepted` | `rejected` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `28612.03` | `0.987` | `0.000` | `+0.987` | `1.000` | `0.950` | `1.000` | `1.000` | `0.000` | `0.460` | `accepted` | `rejected` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `11750.28` | `0.980` | `0.000` | `+0.980` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.592` | `accepted` | `rejected` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `9444.39` | `0.984` | `0.000` | `+0.984` | `1.000` | `0.936` | `1.000` | `1.000` | `0.000` | `0.460` | `accepted` | `rejected` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `9541.84` | `0.982` | `0.000` | `+0.982` | `1.000` | `0.929` | `1.000` | `1.000` | `0.000` | `0.738` | `accepted` | `rejected` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `28206.59` | `0.993` | `0.000` | `+0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `0.000` | `0.328` | `accepted` | `rejected` | - | - | - |
| `swift-01` | `recall` | `swift` | `10283.33` | `0.438` | `0.000` | `+0.438` | `0.093` | `0.693` | `1.000` | `1.000` | `0.000` | `0.987` | `soft_accepted` | `rejected` | missing_exact_anchors | UserDecoderTests testMissingAvatarUsesPlaceholder, Tests/UserDecoderTests.swift:47, XCTAssertEqual failed, Optional(placeholder.png), fatalError | - |
| `elixir-01` | `recall` | `elixir` | `14005.61` | `0.982` | `0.000` | `+0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.522` | `accepted` | `rejected` | - | - | - |
| `rails-01` | `recall` | `rails` | `20742.29` | `0.984` | `0.000` | `+0.984` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.257` | `accepted` | `rejected` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `9603.37` | `0.943` | `0.000` | `+0.943` | `1.000` | `0.928` | `1.000` | `0.931` | `0.000` | `0.417` | `accepted` | `rejected` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `8026.84` | `0.979` | `0.000` | `+0.979` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.657` | `accepted` | `rejected` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `12314.59` | `0.990` | `0.000` | `+0.990` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.632` | `accepted` | `rejected` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `13803.32` | `0.581` | `0.000` | `+0.581` | `0.375` | `0.858` | `1.000` | `1.000` | `0.000` | `0.778` | `soft_accepted` | `rejected` | missing_exact_anchors | web-02, UNREACHABLE, 10.0.4.22 port 22, Connection timed out | - |
| `bazel-01` | `recall` | `bazel` | `11337.52` | `0.984` | `0.000` | `+0.984` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.464` | `accepted` | `rejected` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `9275.22` | `0.984` | `0.000` | `+0.984` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.698` | `accepted` | `rejected` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `6738.04` | `0.944` | `0.000` | `+0.944` | `1.000` | `0.931` | `1.000` | `0.932` | `0.000` | `0.682` | `accepted` | `rejected` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `10018.52` | `0.972` | `0.000` | `+0.972` | `1.000` | `0.930` | `1.000` | `1.000` | `0.000` | `0.545` | `accepted` | `rejected` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `13233.18` | `0.750` | `0.000` | `+0.750` | `0.632` | `0.937` | `1.000` | `1.000` | `0.000` | `0.595` | `soft_accepted` | `rejected` | missing_exact_anchors | github.com/acme/api/internal/webhook, dispatch | - |
| `npm-05` | `summary` | `npm` | `23947.74` | `0.943` | `0.000` | `+0.943` | `1.000` | `0.858` | `1.000` | `1.000` | `0.000` | `0.514` | `accepted` | `rejected` | - | - | - |
| `helm-01` | `summary` | `helm` | `8031.06` | `0.969` | `0.000` | `+0.969` | `1.000` | `0.924` | `1.000` | `1.000` | `0.000` | `0.649` | `accepted` | `rejected` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `17789.26` | `0.962` | `0.000` | `+0.962` | `1.000` | `0.904` | `1.000` | `1.000` | `0.000` | `0.580` | `accepted` | `rejected` | - | - | - |
| `k6-01` | `summary` | `k6` | `9394.65` | `0.960` | `0.000` | `+0.960` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.304` | `accepted` | `rejected` | - | - | - |
| `composer-01` | `summary` | `composer` | `34954.13` | `0.661` | `0.000` | `+0.661` | `0.400` | `0.819` | `1.000` | `1.000` | `0.000` | `0.785` | `soft_accepted` | `rejected` | missing_exact_anchors | install, --no-dev, Loading | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `13086.85` | `0.945` | `0.000` | `+0.945` | `1.000` | `0.862` | `1.000` | `1.000` | `0.000` | `0.929` | `accepted` | `rejected` | - | - | - |
| `make-02` | `summary` | `make` | `29009.22` | `0.648` | `0.000` | `+0.648` | `1.000` | `0.928` | `0.500` | `0.500` | `0.000` | `0.803` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `11533.46` | `0.965` | `0.000` | `+0.965` | `1.000` | `0.913` | `1.000` | `1.000` | `0.000` | `0.238` | `accepted` | `rejected` | - | - | - |
| `jest-01` | `summary` | `jest` | `7450.91` | `0.954` | `0.000` | `+0.954` | `1.000` | `0.885` | `1.000` | `1.000` | `0.000` | `0.839` | `accepted` | `rejected` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `13378.14` | `0.788` | `0.000` | `+0.788` | `0.833` | `0.922` | `1.000` | `1.000` | `0.000` | `0.639` | `soft_accepted` | `rejected` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `5522.77` | `0.973` | `0.000` | `+0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `0.000` | `0.462` | `accepted` | `rejected` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `15507.99` | `0.933` | `0.000` | `+0.933` | `1.000` | `0.834` | `1.000` | `1.000` | `0.000` | `0.904` | `accepted` | `rejected` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `7462.63` | `0.974` | `0.000` | `+0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `0.000` | `0.619` | `accepted` | `rejected` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `24226.81` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.229` | `0.000` | `0.000` | `0.000` | `0.545` | `rejected` | `rejected` | structured_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='src/App.tsx - 22:7 - prefer-const - src/api.ts - 4:12 - @typescript-eslint/no-explicit-any - include only items that satisfy the instruction - omit related b...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='src/App.tsx - 22:7 - prefer-const - src/api.ts - 4:12 - @typescript-eslint/no-explicit-any $ eslint src src/App.tsx 10:3 warning Unexpected console statement...' |
| `git-diff-01` | `instruction_following` | `git-diff` | `20234.87` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.578` | `0.000` | `0.000` | `0.000` | `0.471` | `rejected` | `rejected` | structured_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='src/auth/token.ts changes JWT expiry from 15m to 7d Review bot: infra/terraform/iam.tf adds iam:PassRole to deployer policy' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='src/auth/token.ts changes JWT expiry from 15m to 7d Review bot: infra/terraform/iam.tf adds iam:PassRole to deployer policy' |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `20722.05` | `0.178` | `0.000` | `+0.178` | `0.500` | `0.000` | `0.250` | `0.183` | `0.000` | `0.762` | `soft_accepted` | `rejected` | missing_exact_anchors | tests/test_auth.py::test_refresh_token_expiry | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `30474.07` | `0.746` | `0.000` | `+0.746` | `0.900` | `0.657` | `1.000` | `1.000` | `0.000` | `0.857` | `soft_accepted` | `rejected` | missing_exact_anchors | node=22 | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `7985.61` | `0.976` | `0.000` | `+0.976` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.641` | `accepted` | `rejected` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `14583.28` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.000` | `0.694` | `0.000` | `0.000` | `0.272` | `rejected` | `rejected` | exact_lines_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- npm ERR! code ENOTEMPTY - npm ERR! syscall rename' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='npm ERR! code ENOTEMPTY - npm ERR! syscall rename - /repo/node_modules/esbuild - /repo/node_modules/.esbuild.DELETE' |
| `docker-build-03` | `instruction_following` | `docker-build` | `46053.86` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.280` | `0.024` | `0.000` | `0.509` | `0.509` | `rejected` | `rejected` | unterminated_reasoning_block, control_token_leakage, thought_leakage, exact_format_contract_breakage | - | fallback output validation failed: model did not stop thinking before reaching the output limit. first_pass="<think> Okay, let's see. The user wants me to return only the failing Docker stage, command, error code, and exit code. They also want the output in a specif..." repair_pass="<think> Okay, let's see. The user provided their previous answer and said it was invalid. The previous answer had lines like #12 [base 3/5] RUN apk add curl,..." |
| `terraform-09` | `instruction_following` | `terraform` | `20066.85` | `0.294` | `0.000` | `+0.294` | `0.333` | `0.663` | `0.333` | `0.312` | `0.000` | `0.683` | `soft_accepted` | `rejected` | missing_exact_anchors | aws_db_instance.main, destroyed | - |
| `maven-03` | `instruction_following` | `maven` | `16349.44` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.855` | `0.000` | `0.000` | `0.000` | `0.640` | `rejected` | `rejected` | structured_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- /repo/src/main/java/App.java:[12,8] unchecked conversion - /repo/src/main/java/UserService.java:[44,17] cannot find symbol symbol: method findByEmail(java....' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='UserService.java:[44,17] cannot find symbol symbol: method findByEmail(java.lang.String) [ERROR] /repo/src/main/java/UserController.java:[28,31] incompatible...' |
| `playwright-01` | `instruction_following` | `playwright` | `18544.87` | `0.489` | `0.000` | `+0.489` | `0.818` | `0.708` | `0.500` | `0.500` | `0.000` | `0.792` | `soft_accepted` | `rejected` | missing_exact_anchors | pays with saved card | - |
| `prettier-01` | `instruction_following` | `prettier` | `24641.04` | `0.051` | `0.000` | `+0.051` | `0.000` | `1.000` | `0.000` | `0.000` | `0.000` | `0.995` | `soft_accepted` | `rejected` | missing_exact_anchors, verbatim_alignment_weak | src/App.tsx, src/api/client.ts | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `16329.57` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.000` | `0.475` | `0.000` | `0.000` | `0.365` | `rejected` | `rejected` | exact_lines_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- worker-5b8c - migrator-9z1q' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- worker-5b8c - migrator-9z1q - CrashLoopBackOff - Error' |
| `cargo-04` | `instruction_following` | `cargo` | `21123.17` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.556` | `0.000` | `0.000` | `0.000` | `0.587` | `rejected` | `rejected` | structured_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- auth::tests::parses_expired_token FAILED thread panicked at src/auth.rs:88: called `Option::unwrap()`on a`None`value - billing::tests::rounds_half_even FAI...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- auth::tests::parses_expired_token ... FAILED - billing::tests::rounds_half_even ... FAILED failures: ---- auth::tests::parses_expired_token stdout ---- thr...' |
| `shell-01` | `instruction_following` | `shell` | `9939.96` | `0.381` | `0.000` | `+0.381` | `0.857` | `0.490` | `0.408` | `0.359` | `0.000` | `0.889` | `accepted` | `rejected` | - | exit code 23 | - |
| `pyright-01` | `structured` | `pyright` | `9163.72` | `0.387` | `0.000` | `+0.387` | `1.000` | `0.187` | `0.375` | `0.375` | `0.000` | `0.495` | `accepted` | `rejected` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `19235.77` | `0.094` | `0.000` | `+0.094` | `0.833` | `0.191` | `0.000` | `0.000` | `0.000` | `0.647` | `soft_accepted` | `rejected` | missing_exact_anchors | field | - |
| `junit-01` | `structured` | `junit` | `19909.77` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.799` | `0.500` | `0.000` | `0.000` | `0.449` | `rejected` | `rejected` | structured_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- CalculatorTest > dividesByZero FAILED java.lang.ArithmeticException: / by zero at Calculator.java:42 UserServiceTest > rejectsDuplicateEmail FAILED expecte...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='Test | Error | Location | |------|-------|----------| | CalculatorTest > dividesByZero FAILED | java.lang.ArithmeticException: / by zero | at Calculator.java...' |
| `kubernetes-03` | `structured` | `kubernetes` | `21957.73` | `0.174` | `0.000` | `+0.174` | `1.000` | `0.453` | `0.000` | `0.000` | `0.000` | `0.480` | `accepted` | `rejected` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `21595.58` | `0.564` | `0.000` | `+0.564` | `1.000` | `0.193` | `0.708` | `0.629` | `0.000` | `0.727` | `accepted` | `rejected` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `22431.20` | `0.670` | `0.000` | `+0.670` | `1.000` | `0.608` | `0.714` | `0.607` | `0.000` | `0.683` | `accepted` | `rejected` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `18651.63` | `0.148` | `0.000` | `+0.148` | `1.000` | `0.232` | `0.000` | `0.000` | `0.000` | `0.742` | `accepted` | `rejected` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `19001.55` | `0.000` | `0.000` | `+0.000` | `0.333` | `0.547` | `0.000` | `0.000` | `0.000` | `0.878` | `rejected` | `rejected` | structured_contract_breakage | Job, Step, Exit, --- | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- job lint success 22s - job test failed step="Run unit tests" exit=1 - job build success 49s - job deploy failed step="Upload artifact" exit=1' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- job lint success 22s - job test failed step="Run unit tests" exit=1 - job build success 49s - job deploy failed step="Upload artifact" exit=1' |
| `npm-07` | `structured` | `npm` | `22890.41` | `0.437` | `0.000` | `+0.437` | `0.833` | `0.274` | `0.571` | `0.571` | `0.000` | `0.351` | `soft_accepted` | `rejected` | missing_exact_anchors | package | - |
| `mypy-06` | `structured` | `mypy` | `21751.82` | `0.000` | `0.000` | `+0.000` | `0.467` | `0.633` | `0.000` | `0.000` | `0.000` | `0.666` | `rejected` | `rejected` | structured_contract_breakage | File, Line, Code, Message | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='app/api.py:10: error: Module has no attribute "Router" [attr-defined] app/auth.py:44: error: Incompatible return value type (got "None", expected "User") [re...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- app/api.py:10: error: Module has no attribute "Router" [attr-defined] - app/api.py:44: error: Incompatible return value type (got "None", expected "User") ...' |
| `gradle-03` | `structured` | `gradle` | `28734.05` | `0.193` | `0.000` | `+0.193` | `1.000` | `0.188` | `0.083` | `0.083` | `0.000` | `0.836` | `accepted` | `rejected` | - | - | - |
| `playwright-02` | `structured` | `playwright` | `21999.40` | `0.755` | `0.000` | `+0.755` | `1.000` | `0.708` | `0.708` | `0.708` | `0.000` | `0.528` | `accepted` | `rejected` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `19408.88` | `0.112` | `0.000` | `+0.112` | `0.879` | `0.180` | `0.000` | `0.000` | `0.000` | `0.769` | `soft_accepted` | `rejected` | missing_exact_anchors | column | - |
| `vite-01` | `structured` | `vite` | `19425.03` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.219` | `0.000` | `0.000` | `0.000` | `0.354` | `rejected` | `rejected` | structured_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='[vite]: Rollup failed to resolve import "@acme/ui/Button" from "/repo/apps/admin/src/App.tsx". [vite]: Rollup failed to resolve import "@acme/api" from "/rep...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```json [vite]: Rollup failed to resolve import "@acme/ui/Button" from "/repo/apps/admin/src/App.tsx". [vite]: Rollup failed to resolve import "@acme/api" fr...' |
| `python-pytest-06` | `exact_format` | `python-pytest` | `15550.92` | `0.736` | `0.000` | `+0.736` | `1.000` | `1.000` | `0.750` | `0.750` | `0.000` | `0.534` | `soft_accepted` | `rejected` | verbatim_alignment_weak | - | - |
| `git-04` | `exact_format` | `git` | `20233.59` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.970` | `accepted` | `rejected` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `22613.35` | `0.694` | `0.000` | `+0.694` | `1.000` | `0.341` | `0.710` | `0.710` | `0.000` | `0.560` | `accepted` | `rejected` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `8247.62` | `0.221` | `0.000` | `+0.221` | `1.000` | `0.294` | `0.233` | `0.181` | `0.000` | `0.777` | `accepted` | `rejected` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `13796.47` | `0.194` | `0.000` | `+0.194` | `1.000` | `0.319` | `0.187` | `0.152` | `0.000` | `0.729` | `accepted` | `rejected` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `10726.10` | `0.000` | `0.000` | `+0.000` | `0.500` | `0.283` | `0.047` | `0.000` | `0.000` | `0.823` | `rejected` | `rejected` | exact_format_contract_breakage | prod | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='- NAME READY STATUS RESTARTS AGE - api-7d9f 1/1 Running 0 1h - migrator-v2-9xk 0/1 Error 0 33m - worker-123 1/1 Running 0 1h' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='namespace: prod' |
| `cargo-05` | `exact_format` | `cargo` | `5638.56` | `0.394` | `0.000` | `+0.394` | `1.000` | `0.000` | `0.308` | `0.227` | `0.000` | `0.838` | `accepted` | `rejected` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `8400.87` | `0.379` | `0.000` | `+0.379` | `1.000` | `0.245` | `0.440` | `0.327` | `0.000` | `0.540` | `accepted` | `rejected` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `7237.95` | `0.316` | `0.000` | `+0.316` | `1.000` | `0.253` | `0.370` | `0.265` | `0.000` | `0.681` | `accepted` | `rejected` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `28657.91` | `0.646` | `0.000` | `+0.646` | `1.000` | `0.921` | `0.500` | `0.500` | `0.000` | `0.617` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `18103.35` | `0.952` | `0.000` | `+0.952` | `1.000` | `0.880` | `1.000` | `1.000` | `0.000` | `0.629` | `accepted` | `rejected` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `5991.24` | `0.892` | `0.000` | `+0.892` | `1.000` | `0.640` | `1.000` | `1.000` | `0.000` | `0.827` | `accepted` | `rejected` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `15570.31` | `0.968` | `0.000` | `+0.968` | `1.000` | `0.919` | `1.000` | `1.000` | `0.000` | `0.310` | `accepted` | `rejected` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `6949.80` | `0.962` | `0.000` | `+0.962` | `1.000` | `0.905` | `1.000` | `1.000` | `0.000` | `0.739` | `accepted` | `rejected` | - | - | - |
| `rust-01` | `explanation` | `rust` | `25607.83` | `0.617` | `0.000` | `+0.617` | `1.000` | `0.825` | `0.500` | `0.500` | `0.000` | `0.697` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `13677.99` | `0.711` | `0.000` | `+0.711` | `0.583` | `0.851` | `1.000` | `1.000` | `0.000` | `0.852` | `soft_accepted` | `rejected` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `15853.36` | `0.438` | `0.000` | `+0.438` | `0.000` | `0.861` | `1.000` | `1.000` | `0.000` | `0.826` | `soft_accepted` | `rejected` | missing_exact_anchors | main.cpp:10:5, error: 'cout' was not declared in this scope | - |
| `testing-01` | `recall` | `testing` | `6560.76` | `0.986` | `0.000` | `+0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `0.000` | `0.651` | `accepted` | `rejected` | - | - | - |
| `testing-02` | `recall` | `testing` | `15380.51` | `0.985` | `0.000` | `+0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.682` | `accepted` | `rejected` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `15449.57` | `0.977` | `0.000` | `+0.977` | `1.000` | `0.908` | `1.000` | `1.000` | `0.000` | `0.588` | `accepted` | `rejected` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `18537.50` | `0.985` | `0.000` | `+0.985` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.575` | `accepted` | `rejected` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `8184.92` | `0.930` | `0.000` | `+0.930` | `1.000` | `0.948` | `1.000` | `0.900` | `0.000` | `0.790` | `accepted` | `rejected` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `10318.26` | `0.952` | `0.000` | `+0.952` | `1.000` | `0.924` | `1.000` | `0.950` | `0.000` | `0.887` | `accepted` | `rejected` | - | - | - |
| `ci-01` | `recall` | `ci` | `35079.84` | `0.436` | `0.000` | `+0.436` | `0.000` | `0.851` | `1.000` | `1.000` | `0.000` | `0.806` | `soft_accepted` | `rejected` | missing_exact_anchors | Error: Tests failed, 5 tests run, 1 failure | - |
| `testing-03` | `recall` | `testing` | `33431.47` | `0.934` | `0.000` | `+0.934` | `1.000` | `0.897` | `1.000` | `0.929` | `0.000` | `0.797` | `accepted` | `rejected` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `10938.76` | `0.936` | `0.000` | `+0.936` | `1.000` | `0.889` | `1.000` | `0.937` | `0.000` | `0.786` | `accepted` | `rejected` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `10860.20` | `0.752` | `0.000` | `+0.752` | `0.778` | `0.940` | `1.000` | `1.000` | `0.000` | `0.888` | `soft_accepted` | `rejected` | missing_exact_anchors | "ami" is required | - |
| `compilation-02` | `recall` | `compilation` | `7517.02` | `0.990` | `0.000` | `+0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.608` | `accepted` | `rejected` | - | - | - |
| `ci-02` | `recall` | `ci` | `5079.74` | `0.975` | `0.000` | `+0.975` | `1.000` | `0.899` | `1.000` | `1.000` | `0.000` | `0.759` | `accepted` | `rejected` | - | - | - |
| `build-01` | `recall` | `build` | `14434.88` | `0.921` | `0.000` | `+0.921` | `1.000` | `0.892` | `1.000` | `0.909` | `0.000` | `0.545` | `accepted` | `rejected` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `5545.23` | `0.980` | `0.000` | `+0.980` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.739` | `accepted` | `rejected` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `5704.56` | `0.989` | `0.000` | `+0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.562` | `accepted` | `rejected` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `5595.55` | `0.970` | `0.000` | `+0.970` | `1.000` | `0.879` | `1.000` | `1.000` | `0.000` | `0.930` | `accepted` | `rejected` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `7406.46` | `0.991` | `0.000` | `+0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.870` | `accepted` | `rejected` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `22801.72` | `0.967` | `0.000` | `+0.967` | `1.000` | `0.870` | `1.000` | `1.000` | `0.000` | `0.954` | `accepted` | `rejected` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `7266.18` | `0.987` | `0.000` | `+0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.774` | `accepted` | `rejected` | - | - | - |
| `testing-04` | `recall` | `testing` | `6268.87` | `0.974` | `0.000` | `+0.974` | `1.000` | `0.896` | `1.000` | `1.000` | `0.000` | `0.710` | `accepted` | `rejected` | - | - | - |
| `build-02` | `recall` | `build` | `14821.73` | `0.976` | `0.000` | `+0.976` | `1.000` | `0.906` | `1.000` | `1.000` | `0.000` | `0.710` | `accepted` | `rejected` | - | - | - |
| `ci-03` | `recall` | `ci` | `24263.34` | `0.833` | `0.000` | `+0.833` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.336` | `soft_accepted` | `rejected` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `6052.44` | `0.976` | `0.000` | `+0.976` | `1.000` | `0.904` | `1.000` | `1.000` | `0.000` | `0.959` | `accepted` | `rejected` | - | - | - |
| `build-03` | `summary` | `build` | `13566.22` | `0.747` | `0.000` | `+0.747` | `0.714` | `0.875` | `1.000` | `1.000` | `0.000` | `0.485` | `soft_accepted` | `rejected` | missing_exact_anchors | failing tests | - |
| `docker-05` | `summary` | `docker` | `5223.98` | `0.886` | `0.000` | `+0.886` | `1.000` | `0.850` | `1.000` | `0.925` | `0.000` | `0.435` | `accepted` | `rejected` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `4521.58` | `0.961` | `0.000` | `+0.961` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.473` | `accepted` | `rejected` | - | - | - |
| `ci-04` | `summary` | `ci` | `4810.04` | `0.950` | `0.000` | `+0.950` | `1.000` | `0.875` | `1.000` | `1.000` | `0.000` | `0.937` | `accepted` | `rejected` | - | - | - |
| `npm-09` | `summary` | `npm` | `6042.40` | `0.889` | `0.000` | `+0.889` | `1.000` | `0.941` | `1.000` | `0.880` | `0.000` | `0.754` | `accepted` | `rejected` | - | - | - |
| `rust-02` | `summary` | `rust` | `4099.81` | `0.885` | `0.000` | `+0.885` | `1.000` | `0.833` | `1.000` | `0.933` | `0.000` | `0.860` | `accepted` | `rejected` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `26483.15` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.216` | `0.000` | `0.000` | `0.000` | `0.701` | `rejected` | `rejected` | structured_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='error - index.js' repair_status=rejected repair_flags=['thought_leakage', 'structured_contract_breakage'] repair_pass="error message from their code, and they want me to fix it. The previous answer had an error in index.js. The error messages are about 'apiKey' being used but..." |
| `testing-06` | `instruction_following` | `testing` | `12331.15` | `0.379` | `0.000` | `+0.379` | `0.500` | `0.413` | `0.500` | `0.500` | `0.000` | `0.664` | `soft_accepted` | `rejected` | missing_exact_anchors | ERROR: | - |
| `ci-05` | `instruction_following` | `ci` | `17071.18` | `0.786` | `0.000` | `+0.786` | `1.000` | `0.999` | `1.000` | `0.775` | `0.000` | `0.579` | `soft_accepted` | `rejected` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `17298.44` | `0.140` | `0.000` | `+0.140` | `1.000` | `0.167` | `0.000` | `0.000` | `0.000` | `0.742` | `accepted` | `rejected` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `14082.30` | `0.143` | `0.000` | `+0.143` | `1.000` | `0.196` | `0.000` | `0.000` | `0.000` | `0.394` | `accepted` | `rejected` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `18327.45` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.741` | `0.000` | `0.000` | `0.000` | `0.776` | `rejected` | `rejected` | structured_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- InstanceId: i-12345 State: running' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```markdown - InstanceId: i-12345 - State: running ```' |
| `network-01` | `exact_format` | `network` | `6944.56` | `0.624` | `0.000` | `+0.624` | `1.000` | `0.332` | `0.675` | `0.574` | `0.000` | `0.950` | `accepted` | `rejected` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `9351.58` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `0.521` | `rejected` | `rejected` | exact_format_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response' |
| `shell-03` | `exact_format` | `shell` | `20871.94` | `0.708` | `0.000` | `+0.708` | `1.000` | `1.000` | `0.700` | `0.700` | `0.000` | `0.676` | `soft_accepted` | `rejected` | verbatim_alignment_weak | - | - |
| `shell-04` | `exact_format` | `shell` | `4354.75` | `0.291` | `0.000` | `+0.291` | `1.000` | `0.492` | `0.311` | `0.233` | `0.000` | `0.480` | `accepted` | `rejected` | - | - | - |
| `build-04` | `exact_format` | `build` | `13182.99` | `0.155` | `0.000` | `+0.155` | `0.286` | `0.250` | `0.215` | `0.215` | `0.000` | `0.494` | `soft_accepted` | `rejected` | missing_exact_anchors | Resources: 1 added | - |
| `build-05` | `exact_format` | `build` | `5079.97` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.553` | `accepted` | `rejected` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `5158.97` | `0.587` | `0.000` | `+0.587` | `1.000` | `0.658` | `0.617` | `0.493` | `0.000` | `0.959` | `accepted` | `rejected` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `3225.22` | `0.949` | `0.000` | `+0.949` | `1.000` | `0.872` | `1.000` | `1.000` | `0.000` | `0.925` | `accepted` | `rejected` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `3081.66` | `0.937` | `0.000` | `+0.937` | `1.000` | `0.843` | `1.000` | `1.000` | `0.000` | `0.519` | `accepted` | `rejected` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `3512.23` | `0.967` | `0.000` | `+0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.845` | `accepted` | `rejected` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `2633.70` | `0.948` | `0.000` | `+0.948` | `1.000` | `0.871` | `1.000` | `1.000` | `0.000` | `0.526` | `accepted` | `rejected` | - | - | - |
| `ci-06` | `explanation` | `ci` | `13540.89` | `0.874` | `0.000` | `+0.874` | `1.000` | `0.877` | `1.000` | `0.894` | `0.000` | `0.445` | `accepted` | `rejected` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `2681.69` | `0.945` | `0.000` | `+0.945` | `1.000` | `0.863` | `1.000` | `1.000` | `0.000` | `0.948` | `accepted` | `rejected` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `3538.11` | `0.964` | `0.000` | `+0.964` | `1.000` | `0.909` | `1.000` | `1.000` | `0.000` | `0.491` | `accepted` | `rejected` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `3026.80` | `0.946` | `0.000` | `+0.946` | `1.000` | `0.866` | `1.000` | `1.000` | `0.000` | `0.945` | `accepted` | `rejected` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `4172.01` | `0.955` | `0.000` | `+0.955` | `1.000` | `0.888` | `1.000` | `1.000` | `0.000` | `0.681` | `accepted` | `rejected` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `2935.87` | `0.960` | `0.000` | `+0.960` | `1.000` | `0.900` | `1.000` | `1.000` | `0.000` | `0.934` | `accepted` | `rejected` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `4863.46` | `0.950` | `0.000` | `+0.950` | `1.000` | `0.875` | `1.000` | `1.000` | `0.000` | `0.451` | `accepted` | `rejected` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `3340.79` | `0.958` | `0.000` | `+0.958` | `1.000` | `0.895` | `1.000` | `1.000` | `0.000` | `0.953` | `accepted` | `rejected` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `3681.79` | `0.926` | `0.000` | `+0.926` | `1.000` | `0.816` | `1.000` | `1.000` | `0.000` | `0.913` | `accepted` | `rejected` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `4860.49` | `0.963` | `0.000` | `+0.963` | `1.000` | `0.908` | `1.000` | `1.000` | `0.000` | `0.673` | `accepted` | `rejected` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `3551.43` | `0.941` | `0.000` | `+0.941` | `1.000` | `0.853` | `1.000` | `1.000` | `0.000` | `0.488` | `accepted` | `rejected` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `3811.55` | `0.958` | `0.000` | `+0.958` | `1.000` | `0.895` | `1.000` | `1.000` | `0.000` | `0.501` | `accepted` | `rejected` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `2917.82` | `0.959` | `0.000` | `+0.959` | `1.000` | `0.896` | `1.000` | `1.000` | `0.000` | `0.961` | `accepted` | `rejected` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `3158.00` | `0.946` | `0.000` | `+0.946` | `1.000` | `0.864` | `1.000` | `1.000` | `0.000` | `0.927` | `accepted` | `rejected` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `2575.25` | `0.946` | `0.000` | `+0.946` | `1.000` | `0.866` | `1.000` | `1.000` | `0.000` | `0.953` | `accepted` | `rejected` | - | - | - |
| `ci-07` | `structured` | `ci` | `14095.20` | `0.143` | `0.000` | `+0.143` | `1.000` | `0.196` | `0.000` | `0.000` | `0.000` | `0.394` | `accepted` | `rejected` | - | - | - |
| `linting-03` | `structured` | `linting` | `18148.01` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.741` | `0.000` | `0.000` | `0.000` | `0.776` | `rejected` | `rejected` | structured_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- InstanceId: i-12345 State: running' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```markdown - InstanceId: i-12345 - State: running ```' |
| `network-02` | `exact_format` | `network` | `6717.86` | `0.624` | `0.000` | `+0.624` | `1.000` | `0.332` | `0.675` | `0.574` | `0.000` | `0.950` | `accepted` | `rejected` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `10494.10` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `0.554` | `rejected` | `rejected` | exact_format_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response' |
| `shell-07` | `exact_format` | `shell` | `11466.44` | `0.736` | `0.000` | `+0.736` | `1.000` | `1.000` | `0.750` | `0.750` | `0.000` | `0.760` | `soft_accepted` | `rejected` | verbatim_alignment_weak | - | - |
| `build-06` | `exact_format` | `build` | `13959.21` | `0.155` | `0.000` | `+0.155` | `0.286` | `0.250` | `0.215` | `0.215` | `0.000` | `0.494` | `soft_accepted` | `rejected` | missing_exact_anchors | Resources: 1 added | - |
| `runtime-07` | `exact_format` | `runtime` | `6075.16` | `0.656` | `0.000` | `+0.656` | `1.000` | `0.324` | `0.710` | `0.603` | `0.000` | `0.949` | `accepted` | `rejected` | - | - | - |
| `build-07` | `exact_format` | `build` | `5574.98` | `0.574` | `0.000` | `+0.574` | `1.000` | `0.850` | `0.560` | `0.504` | `0.000` | `0.432` | `accepted` | `rejected` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `8262.69` | `0.446` | `0.000` | `+0.446` | `1.000` | `0.644` | `0.467` | `0.373` | `0.000` | `0.984` | `accepted` | `rejected` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `3243.77` | `0.949` | `0.000` | `+0.949` | `1.000` | `0.872` | `1.000` | `1.000` | `0.000` | `0.925` | `accepted` | `rejected` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `3059.31` | `0.937` | `0.000` | `+0.937` | `1.000` | `0.843` | `1.000` | `1.000` | `0.000` | `0.519` | `accepted` | `rejected` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `3578.90` | `0.968` | `0.000` | `+0.968` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.488` | `accepted` | `rejected` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `5290.33` | `0.976` | `0.000` | `+0.976` | `1.000` | `0.939` | `1.000` | `1.000` | `0.000` | `0.778` | `accepted` | `rejected` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `3551.21` | `0.964` | `0.000` | `+0.964` | `1.000` | `0.909` | `1.000` | `1.000` | `0.000` | `0.491` | `accepted` | `rejected` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `3327.50` | `0.971` | `0.000` | `+0.971` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.514` | `accepted` | `rejected` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `2546.37` | `0.930` | `0.000` | `+0.930` | `1.000` | `0.826` | `1.000` | `1.000` | `0.000` | `0.953` | `accepted` | `rejected` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `3608.06` | `0.969` | `0.000` | `+0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.950` | `accepted` | `rejected` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `22207.00` | `0.646` | `0.000` | `+0.646` | `0.444` | `0.747` | `1.000` | `1.000` | `0.000` | `0.533` | `soft_accepted` | `rejected` | missing_exact_anchors | nonexistent (invalid) version of flask | - |
