# cpu-LFM2-700M

## Scenario

- track: `cpu`
- phase: `cpu-screen`
- model: `LiquidAI/LFM2-700M-GGUF`
- quantization: `none`
- device: `cpu`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `64685.86`
- cpu_rss_bytes: `null`
- gpu_peak_bytes: `null`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- recovered_final_score: `49.15`
- raw_final_score: `33.75`
- recovery_lift: `+15.40`
- case_count: `280`
- success_count: `263`
- accepted_count: `154`
- soft_accepted_count: `109`
- rejected_count: `17`
- exact_pass_count: `177`
- avg_inference_ms: `6758.19`
- p95_inference_ms: `22141.91`
- avg_exact_preservation_ratio: `0.823`
- avg_summary_quality_ratio: `0.801`
- avg_format_adherence_score: `0.799`
- avg_instruction_following_score: `0.747`
- avg_brevity_ratio: `0.789`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.691`
- p10_case_score: `0.126`
- quality_core: `0.578`
- latency_factor: `0.850`
- final_score: `49.15`
- peak_cpu_rss_bytes: `null`
- peak_gpu_bytes: `null`

### Raw View

- accepted_count: `50`
- soft_accepted_count: `188`
- rejected_count: `42`
- exact_pass_count: `177`
- avg_exact_preservation_ratio: `0.823`
- avg_summary_quality_ratio: `0.807`
- avg_format_adherence_score: `0.538`
- avg_instruction_following_score: `0.455`
- avg_brevity_ratio: `0.774`
- avg_thought_leakage_density: `0.002`
- avg_thought_marker_count: `0.02`
- avg_case_score: `0.496`
- p10_case_score: `0.000`
- quality_core: `0.397`
- final_score: `33.75`

## Cases

| case_id | family | domain | ms | recovered_score | raw_score | lift | preserve | quality | format | instruction | recovered_thought_density | raw_thought_density | recovered_validation | raw_validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `6297.50` | `0.711` | `0.546` | `+0.165` | `0.667` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | /workspace/app/config.py, line 27 | - |
| `python-02` | `summary` | `python` | `6395.07` | `0.613` | `0.613` | `-0.001` | `1.000` | `0.936` | `0.500` | `0.459` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-03` | `recall` | `python` | `16032.77` | `0.582` | `0.000` | `+0.582` | `1.000` | `0.935` | `0.500` | `0.387` | `0.000` | `0.000` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `python-04` | `recall` | `python` | `13058.84` | `0.609` | `0.610` | `-0.000` | `1.000` | `0.949` | `0.500` | `0.425` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-05` | `recall` | `python` | `7976.68` | `0.518` | `0.518` | `-0.000` | `0.778` | `0.915` | `0.500` | `0.405` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | python tools/export_report.py --input data/may.csv --format parquet | - |
| `pytest-01` | `recall` | `pytest` | `14534.58` | `0.827` | `0.563` | `+0.264` | `1.000` | `0.898` | `1.000` | `0.734` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `4543.66` | `0.984` | `0.657` | `+0.327` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `4842.44` | `0.992` | `0.662` | `+0.330` | `1.000` | `0.968` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-04` | `recall` | `pytest` | `10293.68` | `0.918` | `0.618` | `+0.301` | `1.000` | `0.955` | `1.000` | `0.876` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `22945.41` | `0.562` | `0.561` | `+0.001` | `0.510` | `0.895` | `1.000` | `0.743` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | src/billing/client.py:9, ModuleNotFoundError, 1 error during collection | - |
| `mypy-01` | `recall` | `mypy` | `6726.27` | `0.605` | `0.563` | `+0.042` | `1.000` | `0.901` | `0.500` | `0.431` | `0.000` | `0.093` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `mypy-02` | `summary` | `mypy` | `6680.59` | `0.705` | `0.705` | `+0.000` | `0.474` | `0.902` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | mypy src tests --pretty --show-error-codes, arg-type, checked 37 source files | - |
| `mypy-03` | `recall` | `mypy` | `6179.77` | `0.736` | `0.736` | `+0.000` | `0.727` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | mypy src/orders/normalize.py --show-error-codes --strict | - |
| `ruff-01` | `recall` | `ruff` | `4114.24` | `0.889` | `0.591` | `+0.298` | `0.911` | `0.929` | `1.000` | `0.905` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `3968.96` | `0.758` | `0.583` | `+0.175` | `0.667` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | src/api/serializers.py | - |
| `ruff-03` | `summary` | `ruff` | `20692.05` | `0.970` | `0.649` | `+0.321` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `3201.25` | `0.987` | `0.000` | `+0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `6697.90` | `0.973` | `0.973` | `-0.000` | `1.000` | `0.914` | `1.000` | `0.990` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `2420.21` | `0.984` | `0.655` | `+0.329` | `1.000` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `black-01` | `summary` | `black` | `6592.57` | `0.816` | `0.639` | `+0.177` | `0.900` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | 2 files would be reformatted | - |
| `black-02` | `summary` | `black` | `4789.77` | `0.968` | `0.971` | `-0.003` | `1.000` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `1837.08` | `0.993` | `0.664` | `+0.329` | `1.000` | `0.973` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `4543.95` | `0.949` | `0.636` | `+0.313` | `1.000` | `0.935` | `1.000` | `0.940` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `6860.00` | `0.756` | `0.585` | `+0.170` | `0.667` | `0.931` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ERESOLVE, react@18.2.0 | - |
| `npm-03` | `summary` | `npm` | `18114.81` | `0.808` | `0.000` | `+0.808` | `1.000` | `0.914` | `1.000` | `0.779` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `3939.22` | `0.992` | `0.663` | `+0.329` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `7642.56` | `0.777` | `0.602` | `+0.174` | `0.727` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | pnpm add @tanstack/react-query-devtools@5.52.0 -F packages/admin | - |
| `pnpm-03` | `summary` | `pnpm` | `23293.32` | `0.784` | `0.610` | `+0.174` | `0.762` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | packages/api | - |
| `typescript-01` | `summary` | `typescript` | `8445.97` | `0.709` | `0.543` | `+0.167` | `0.467` | `0.919` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | tsc -p tsconfig.json --noEmit, src/server/index.ts(3,18), src/server/index.ts(4,18) | - |
| `typescript-02` | `recall` | `typescript` | `7383.59` | `0.665` | `0.511` | `+0.153` | `0.632` | `0.943` | `1.000` | `0.929` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | packages/web/src/components/Price.tsx(22,9), Watching for file changes | - |
| `typescript-03` | `summary` | `typescript` | `11267.17` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.895` | `0.500` | `0.000` | `0.084` | `0.084` | `rejected` | `rejected` | unterminated_reasoning_block | - | fallback output validation failed: model did not stop thinking before reaching the output limit. first_pass="- Error: TS2769: No overload matches this call. - Argument of type 'URL' is not assignable to parameter of type 'string'. - Overload 1 of 2, '(url: string, i..." repair_pass="Here's the corrected answer: Error: TS2769: No overload matches this call. Argument of type 'URL' is not assignable to parameter of type 'string'. Overload 1..." |
| `eslint-01` | `recall` | `eslint` | `6905.86` | `0.760` | `0.760` | `+0.000` | `0.800` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | /workspace/src/server.js | - |
| `eslint-02` | `summary` | `eslint` | `8344.24` | `0.778` | `0.778` | `+0.000` | `0.773` | `0.930` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ESLint: 9.14.0 | - |
| `eslint-03` | `recall` | `eslint` | `5529.06` | `0.579` | `0.429` | `+0.150` | `0.385` | `0.885` | `1.000` | `0.973` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | eslint src --max-warnings=0, 1 problem (0 errors, 1 warning), maximum: 0 | - |
| `docker-01` | `recall` | `docker` | `4533.16` | `0.983` | `0.656` | `+0.327` | `1.000` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `1444.73` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.979` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `26341.71` | `0.790` | `0.000` | `+0.790` | `1.000` | `0.936` | `1.000` | `0.741` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `2949.22` | `0.770` | `0.596` | `+0.173` | `0.667` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | external, could not be found | - |
| `docker-compose-02` | `recall` | `docker-compose` | `9922.82` | `0.703` | `0.554` | `+0.149` | `0.875` | `0.905` | `1.000` | `0.831` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | app-1 exited with code 1 | - |
| `docker-compose-03` | `summary` | `docker-compose` | `5602.63` | `0.971` | `0.643` | `+0.328` | `1.000` | `0.929` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `6369.03` | `0.730` | `0.730` | `+0.000` | `0.529` | `0.940` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | kubectl apply -f k8s/deployment.yaml --server-side, containers[name="api"].image | - |
| `kubectl-02` | `recall` | `kubectl` | `10125.00` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `4204.17` | `0.991` | `0.991` | `+0.000` | `1.000` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `7500.57` | `0.553` | `0.553` | `-0.000` | `0.429` | `0.867` | `1.000` | `0.881` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | kubectl logs payments-worker-6f8f7d4df5-z5vsm -c worker --previous -n payments, payments-worker-6f8f7d4df5-z5vsm, ValueError | - |
| `terraform-01` | `summary` | `terraform` | `4788.29` | `0.776` | `0.776` | `+0.000` | `0.706` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | main.tf line 23 | - |
| `terraform-02` | `recall` | `terraform` | `6607.09` | `0.719` | `0.553` | `+0.165` | `0.684` | `0.950` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | terraform plan | - |
| `terraform-03` | `recall` | `terraform` | `5700.14` | `0.604` | `0.000` | `+0.604` | `0.387` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | terraform apply, Error acquiring the state lock | - |
| `terraform-04` | `summary` | `terraform` | `9687.39` | `0.718` | `0.552` | `+0.166` | `0.463` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | terraform test, tests/aws.tftest.hcl line 18 | - |
| `mixed-01` | `recall` | `mixed` | `3374.77` | `0.988` | `0.000` | `+0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `3022.73` | `0.975` | `0.650` | `+0.325` | `1.000` | `0.936` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `git-01` | `recall` | `git` | `23913.56` | `0.643` | `0.642` | `+0.001` | `1.000` | `0.908` | `0.500` | `0.486` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `git-02` | `recall` | `git` | `7194.84` | `0.974` | `0.651` | `+0.323` | `1.000` | `0.898` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `git-03` | `recall` | `git` | `7257.56` | `0.487` | `0.354` | `+0.133` | `0.125` | `0.867` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | git clone --progress https://github.com/example/very-large-repo.git, curl 56, Connection reset by peer | - |
| `curl-01` | `recall` | `curl` | `3924.87` | `0.989` | `0.989` | `+0.000` | `1.000` | `0.956` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `curl-02` | `recall` | `curl` | `2365.32` | `0.994` | `0.994` | `+0.000` | `1.000` | `0.976` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ssh-01` | `summary` | `ssh` | `5390.14` | `0.977` | `0.000` | `+0.977` | `1.000` | `0.942` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `6373.47` | `0.746` | `0.578` | `+0.168` | `0.636` | `0.922` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ssh deploy@staging.example.net | - |
| `systemd-01` | `summary` | `systemd` | `6945.62` | `0.768` | `0.768` | `+0.000` | `0.677` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | status=203/EXEC | - |
| `systemd-02` | `summary` | `systemd` | `7155.32` | `0.740` | `0.740` | `+0.000` | `0.643` | `0.900` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | /etc/api/config.yaml | - |
| `apt-01` | `summary` | `apt` | `22087.77` | `0.797` | `0.538` | `+0.259` | `1.000` | `0.937` | `1.000` | `0.751` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `5743.69` | `0.992` | `0.661` | `+0.331` | `1.000` | `0.968` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `11254.51` | `0.717` | `0.000` | `+0.717` | `0.750` | `0.892` | `1.000` | `0.928` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | example.com/mono-app/pkg/server | - |
| `go-test-01` | `summary` | `go-test` | `29358.19` | `0.838` | `0.000` | `+0.838` | `1.000` | `0.925` | `1.000` | `0.817` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `javac-01` | `recall` | `javac` | `7805.19` | `0.548` | `0.404` | `+0.143` | `0.267` | `0.897` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | javac -d out $(find src/main/java -name '*.java'), src/main/java/com/example/app/cli/RunCommand.java:18 | - |
| `maven-01` | `recall` | `maven` | `9978.34` | `0.344` | `0.343` | `+0.000` | `0.087` | `0.893` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | mvn -q test, UserControllerTest.java:72, maven-surefire-plugin:3.5.5:test, /workspace/webapp/target/surefire-reports | - |
| `maven-02` | `summary` | `maven` | `10477.22` | `0.914` | `0.610` | `+0.303` | `1.000` | `0.918` | `1.000` | `0.927` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `10508.86` | `0.598` | `0.454` | `+0.144` | `0.476` | `0.922` | `1.000` | `0.920` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ./gradlew :service:build --warning-mode=all, :service:compileClasspath | - |
| `gradle-02` | `summary` | `gradle` | `9607.59` | `0.739` | `0.569` | `+0.170` | `0.667` | `0.882` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ./gradlew test | - |
| `cargo-01` | `recall` | `cargo` | `5882.87` | `0.613` | `0.461` | `+0.153` | `0.424` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | cargo build, error[E0308] | - |
| `cargo-02` | `recall` | `cargo` | `3334.51` | `0.984` | `0.983` | `+0.001` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `6467.10` | `0.630` | `0.474` | `+0.156` | `0.474` | `0.914` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | node dist/server.js, /workspace/dist/config/index.js:4:18 | - |
| `npm-04` | `summary` | `npm` | `3808.39` | `0.976` | `0.650` | `+0.326` | `1.000` | `0.940` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `4806.09` | `0.515` | `0.515` | `+0.000` | `0.353` | `0.884` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, fenced_output_wrapper | npx tsc -p tsconfig.build.json, src/routes/user.ts(14,21) | - |
| `eslint-04` | `summary` | `eslint` | `4479.08` | `0.962` | `0.637` | `+0.324` | `1.000` | `0.937` | `1.000` | `0.982` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-runtime-01` | `recall` | `python-runtime` | `22142.91` | `0.853` | `0.000` | `+0.853` | `1.000` | `0.947` | `1.000` | `0.761` | `0.000` | `0.050` | `accepted` | `rejected` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `23193.25` | `0.787` | `0.787` | `-0.000` | `1.000` | `0.898` | `1.000` | `0.757` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `4123.74` | `0.967` | `0.640` | `+0.327` | `1.000` | `0.932` | `1.000` | `0.992` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `9944.84` | `0.708` | `0.542` | `+0.166` | `0.467` | `0.916` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | docker build -t example/web:dev ., RUN npm ci --no-audit --no-fund | - |
| `docker-compose-04` | `summary` | `docker-compose` | `3378.83` | `0.982` | `0.651` | `+0.331` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `2240.80` | `0.975` | `0.648` | `+0.327` | `1.000` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `22902.57` | `0.544` | `0.546` | `-0.002` | `1.000` | `0.926` | `0.500` | `0.386` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | - | - |
| `kubectl-07` | `recall` | `kubectl` | `4934.19` | `0.990` | `0.990` | `+0.000` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `10754.05` | `0.541` | `0.541` | `+0.000` | `0.424` | `0.937` | `1.000` | `0.822` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | terraform plan -lock-timeout=5s -out=tfplan, Error acquiring the state lock | - |
| `terraform-06` | `summary` | `terraform` | `1967.51` | `0.977` | `0.649` | `+0.328` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `7860.00` | `0.507` | `0.507` | `+0.000` | `0.000` | `0.805` | `1.000` | `0.885` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | terraform plan -detailed-exitcode -no-color, Plan: 1 to add, 1 to change, 0 to destroy., 2, aws_security_group_rule.web_https | - |
| `nginx-01` | `summary` | `nginx` | `5781.26` | `0.734` | `0.567` | `+0.167` | `0.556` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | sudo nginx -t, "server" directive is not allowed here | - |
| `nginx-02` | `summary` | `nginx` | `10662.76` | `0.754` | `0.585` | `+0.169` | `0.667` | `0.925` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | sudo service nginx reload | - |
| `postgres-01` | `recall` | `postgres` | `2252.72` | `0.994` | `0.663` | `+0.331` | `1.000` | `0.977` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `3481.39` | `0.971` | `0.645` | `+0.326` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `7948.99` | `0.556` | `0.557` | `-0.000` | `1.000` | `0.883` | `0.500` | `0.414` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `mysql-02` | `summary` | `mysql` | `5216.17` | `0.658` | `0.657` | `+0.001` | `1.000` | `0.963` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | fenced_output_wrapper | - | - |
| `redis-01` | `summary` | `redis` | `2461.08` | `0.982` | `0.653` | `+0.328` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `3575.45` | `0.983` | `0.657` | `+0.326` | `1.000` | `0.931` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `7909.17` | `0.674` | `0.514` | `+0.161` | `0.619` | `0.880` | `1.000` | `0.990` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ruff check ., line=91 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `9130.48` | `0.625` | `0.625` | `+0.000` | `0.105` | `0.896` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | pnpm install --frozen-lockfile, ERR_PNPM_ENOSPC, react-dom@18.3.1, ERROR: Job failed: exit status 1 | - |
| `jenkins-01` | `summary` | `jenkins` | `3420.71` | `0.961` | `0.959` | `+0.002` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `11578.77` | `0.875` | `0.000` | `+0.875` | `1.000` | `0.929` | `1.000` | `0.867` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `tar-01` | `summary` | `tar` | `2599.98` | `0.984` | `0.652` | `+0.332` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `4341.12` | `0.926` | `0.622` | `+0.304` | `1.000` | `0.966` | `1.000` | `0.885` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `5348.23` | `0.794` | `0.794` | `+0.000` | `0.833` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | runtime-1a2b3c.js | - |
| `test-failure-01` | `recall` | `test-failure` | `31315.39` | `0.550` | `0.551` | `-0.000` | `0.545` | `0.907` | `1.000` | `0.754` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | tests/unit/test_invoice_totals.py::test_discount_rounding, tests/unit/test_invoice_totals.py:88 | - |
| `compiler-error-01` | `recall` | `compiler-error` | `34991.48` | `0.540` | `0.000` | `+0.540` | `0.851` | `0.902` | `0.500` | `0.406` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors, plain_text_style_mismatch | src/router.rs:128 | - |
| `ci-log-01` | `recall` | `ci-log` | `29055.06` | `0.592` | `0.460` | `+0.132` | `0.647` | `0.919` | `1.000` | `0.761` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | helm upgrade --install payments-api charts/payments-api --namespace prod-payments | - |
| `package-manager-01` | `recall` | `package-manager` | `16431.04` | `0.678` | `0.000` | `+0.678` | `0.778` | `0.948` | `1.000` | `0.834` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | npm install @storybook/react-vite@8.2.0 vite@6.0.1 | - |
| `test-summary-01` | `summary` | `test-summary` | `42546.63` | `0.738` | `0.737` | `+0.001` | `0.571` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | github.com/acme/shop/checkout, TestReconcileInventory, worker.go:144 | - |
| `build-log-01` | `summary` | `build-log` | `26539.43` | `0.721` | `0.721` | `+0.000` | `0.688` | `0.913` | `1.000` | `0.946` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | InvoiceMapper.java:[58,29] | - |
| `docker-build-02` | `summary` | `docker-build` | `7303.10` | `0.378` | `0.376` | `+0.002` | `0.333` | `0.899` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | COPY apps/web ./apps/web, "/apps/web": not found | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `10655.56` | `0.321` | `0.321` | `+0.000` | `0.250` | `0.636` | `0.500` | `0.383` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | /repo/web/src/App.tsx, @typescript-eslint/no-misused-promises, /repo/web/src/api/client.ts, 8:10, @typescript-eslint/no-explicit-any, @typescript-eslint/no-unsafe-assignment | - |
| `git-review-01` | `instruction_following` | `git-review` | `10073.32` | `0.398` | `0.398` | `+0.000` | `0.286` | `0.648` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | packages/api/src/auth/session.ts, packages/api/src/schema/openapi.yaml, migrations/202605171200_add_refresh_ttl.sql | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `11023.73` | `0.063` | `0.063` | `+0.000` | `0.677` | `0.330` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `9706.23` | `0.744` | `0.160` | `+0.584` | `0.778` | `0.841` | `1.000` | `0.902` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | reportArgumentType, reportUndefinedVariable | - |
| `structured-output-02` | `structured` | `structured-output` | `8034.05` | `0.000` | `0.000` | `+0.000` | `0.429` | `0.455` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | test / integration, port 5432 is already allocated, deploy / preview | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml - job: failed_jobs step: Start docker compose command: docker compose up -d postgres redis error: service "postgres" failed to start: Bind for 0.0.0....' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml - job: failed_jobs step: Start docker compose command: docker compose up -d postgres redis error: service "postgres" failed to start: Bind for 0.0.0....' |
| `structured-output-03` | `structured` | `structured-output` | `7627.08` | `0.110` | `0.110` | `+0.000` | `0.214` | `0.638` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | src/auth/session.test.ts, "invalid refresh token", src/billing/tax.test.ts, Expected: 19, Received: 0 | - |
| `structured-output-04` | `structured` | `structured-output` | `5250.79` | `0.060` | `0.048` | `+0.013` | `0.156` | `0.154` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | /repo/apps/web/src/main.tsx, @sentry/browser, /repo/packages/time/src/format.ts, date-fns-tz, /repo/packages/time/src/parse.ts, /repo/apps/web/src/features/flags.ts | - |
| `exact-format-01` | `exact_format` | `exact-format` | `9587.22` | `0.199` | `0.199` | `+0.000` | `0.667` | `0.000` | `0.216` | `0.155` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, verbatim_alignment_weak | tests/jobs/test_reconcile.py::TestReconcile::test_retries_deadlock | - |
| `exact-format-02` | `exact_format` | `exact-format` | `6824.43` | `0.392` | `0.392` | `+0.000` | `0.714` | `0.330` | `0.544` | `0.451` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | SearchBox debounces network query before fetch | - |
| `exact-format-03` | `exact_format` | `exact-format` | `11785.71` | `0.067` | `0.067` | `+0.000` | `0.000` | `0.306` | `0.156` | `0.112` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ghcr.io/acme/worker@sha256:4f8c2e0b1d9a6c7e5f3a2b1908d4c6e7f0a123456789abcdeffedcba98765432 | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `6877.90` | `0.488` | `0.486` | `+0.001` | `0.222` | `0.875` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | /repo/tools/json.py, shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `6490.75` | `0.652` | `0.495` | `+0.157` | `0.250` | `0.887` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | TS2322, AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `5785.80` | `0.433` | `0.433` | `+0.000` | `0.500` | `0.662` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | orders_customer_id_fkey, 00000000-0000-0000-0000-000000000000 | - |
| `python-traceback-01` | `recall` | `python-traceback` | `41162.98` | `0.403` | `0.288` | `+0.115` | `0.190` | `0.877` | `1.000` | `0.716` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | /srv/app/app/tasks/email.py, line 92, [bad@example.test](mailto:bad@example.test), retries exhausted for queue emails | - |
| `mypy-05` | `recall` | `mypy` | `3799.12` | `0.980` | `0.651` | `+0.329` | `1.000` | `0.922` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `13485.56` | `0.985` | `0.658` | `+0.327` | `1.000` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `21734.63` | `0.585` | `0.584` | `+0.001` | `1.000` | `0.896` | `0.500` | `0.402` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `10087.39` | `0.980` | `0.000` | `+0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `16416.70` | `0.879` | `0.000` | `+0.879` | `1.000` | `0.930` | `1.000` | `0.817` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `9323.55` | `0.651` | `0.600` | `+0.051` | `1.000` | `0.899` | `0.500` | `0.500` | `0.000` | `0.095` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `8599.01` | `0.770` | `0.770` | `+0.000` | `0.825` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | dependency failed to start | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `9222.78` | `0.953` | `0.639` | `+0.314` | `1.000` | `0.921` | `1.000` | `0.953` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `8733.31` | `0.983` | `0.982` | `+0.001` | `1.000` | `0.931` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `11601.96` | `0.871` | `0.589` | `+0.282` | `1.000` | `0.898` | `1.000` | `0.815` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `7548.36` | `0.746` | `0.579` | `+0.168` | `0.767` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Tests/UserDecoderTests.swift:47 | - |
| `elixir-01` | `recall` | `elixir` | `9197.94` | `0.981` | `0.656` | `+0.325` | `1.000` | `0.925` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `7279.52` | `0.987` | `0.987` | `-0.000` | `1.000` | `0.946` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `11422.87` | `0.780` | `0.608` | `+0.172` | `0.851` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Failed asserting that '88.00' is identical to '86.40' | - |
| `nginx-03` | `recall` | `nginx` | `8510.55` | `0.982` | `0.656` | `+0.326` | `1.000` | `0.929` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `2024.39` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.949` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `6153.23` | `0.787` | `0.506` | `+0.281` | `0.875` | `0.929` | `1.000` | `1.000` | `0.000` | `0.275` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | 10.0.4.22 port 22 | - |
| `bazel-01` | `recall` | `bazel` | `9710.63` | `0.951` | `0.000` | `+0.951` | `1.000` | `0.877` | `1.000` | `0.968` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `13757.56` | `0.885` | `0.000` | `+0.885` | `1.000` | `0.897` | `1.000` | `0.842` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `2198.63` | `0.993` | `0.662` | `+0.331` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `7543.14` | `0.773` | `0.773` | `+0.000` | `0.783` | `0.910` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | tests/payments/test_webhook.py::test_replays_duplicate_event | - |
| `go-test-03` | `summary` | `go-test` | `7775.67` | `0.943` | `0.627` | `+0.316` | `1.000` | `0.857` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `7092.33` | `0.776` | `0.776` | `+0.000` | `0.867` | `0.865` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | web@1.2.0 | - |
| `helm-01` | `summary` | `helm` | `2487.76` | `0.970` | `0.643` | `+0.326` | `1.000` | `0.924` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `21492.45` | `0.642` | `0.506` | `+0.136` | `0.895` | `0.894` | `1.000` | `0.749` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | typing.Optional | - |
| `k6-01` | `summary` | `k6` | `6048.42` | `0.741` | `0.574` | `+0.167` | `0.652` | `0.896` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | http_req_duration, avg | - |
| `composer-01` | `summary` | `composer` | `5147.56` | `0.698` | `0.525` | `+0.173` | `0.400` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | install, --no-dev, Loading | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `5335.98` | `0.963` | `0.963` | `+0.000` | `1.000` | `0.908` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `10886.58` | `0.647` | `0.000` | `+0.647` | `1.000` | `0.924` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `6131.55` | `0.765` | `0.765` | `+0.000` | `0.692` | `0.943` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Not, properly | - |
| `jest-01` | `summary` | `jest` | `7459.77` | `0.958` | `0.000` | `+0.958` | `1.000` | `0.896` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `4401.67` | `0.788` | `0.788` | `+0.000` | `0.833` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | --select | - |
| `python-pytest-03` | `summary` | `python-pytest` | `8366.95` | `0.962` | `0.000` | `+0.962` | `1.000` | `0.905` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `7141.66` | `0.967` | `0.967` | `+0.000` | `1.000` | `0.916` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `5444.77` | `0.727` | `0.563` | `+0.164` | `0.556` | `0.915` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | FAILED, Falsifying, example | - |
| `eslint-05` | `instruction_following` | `eslint` | `22132.97` | `0.123` | `0.123` | `+0.000` | `0.556` | `0.610` | `0.054` | `0.038` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | src/App.tsx, prefer-const, src/api.ts | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `2352.94` | `0.603` | `0.603` | `+0.000` | `1.000` | `0.696` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `6517.40` | `0.146` | `0.146` | `+0.000` | `0.500` | `0.000` | `0.178` | `0.129` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, verbatim_alignment_weak | tests/test_auth.py::test_refresh_token_expiry | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `3164.88` | `0.520` | `0.520` | `+0.000` | `1.000` | `0.621` | `0.500` | `0.417` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `4918.25` | `0.736` | `0.736` | `+0.000` | `0.423` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Warning Failed, Warning BackOff | - |
| `npm-06` | `instruction_following` | `npm` | `7426.63` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.640` | `0.619` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_lines_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- npm ERR! code ENOTEMPTY - npm ERR! syscall rename - /repo/node_modules/esbuild - npm ERR! dest /repo/node_modules/.esbuild.DELETE - npm ERR! errno -39 - np...' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- npm WARN deprecated request@2.88.2: request has been deprecated - npm WARN old lockfile The package-lock.json file was created with an old version of npm -...' |
| `docker-build-03` | `instruction_following` | `docker-build` | `4827.32` | `0.000` | `0.000` | `+0.000` | `0.450` | `0.312` | `0.262` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | [deps 4/4], pnpm install --frozen-lockfile | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='- ERR_PNPM_LOCKFILE_CONFIG_MISMATCH - exit code: 1' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: pnpm install --frozen-lockfile failed: Cannot proceed with frozen-lockfile due to mismatch in pnpm config exit code: 1' |
| `terraform-09` | `instruction_following` | `terraform` | `4147.55` | `0.372` | `0.372` | `+0.000` | `1.000` | `0.748` | `0.200` | `0.200` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `5448.19` | `0.412` | `0.412` | `+0.000` | `0.375` | `0.649` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | UserService.java:[44,17], UserController.java:[28,31] | - |
| `playwright-01` | `instruction_following` | `playwright` | `7367.77` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.282` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- Error: expect(locator).toBeVisible() failed - Locator: text=Payment complete - [webkit] › checkout.spec.ts:44:1 › pays with saved card Error: locator not f...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='Running 36 tests using 4 workers ✓ [chromium] › login.spec.ts:12:1 › logs in ✘ [firefox] › checkout.spec.ts:44:1 › pays with saved card Error: expect(locator...' |
| `prettier-01` | `instruction_following` | `prettier` | `4143.08` | `0.850` | `0.850` | `+0.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `5232.89` | `0.000` | `0.000` | `+0.000` | `0.500` | `0.500` | `0.382` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_lines_contract_breakage | worker-5b8c, CrashLoopBackOff | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_lines_contract_breakage'] first_pass='- migrator-9z1q Error 0 4m' repair_status=rejected repair_flags=['exact_lines_contract_breakage'] repair_pass='- NAME READY STATUS RESTARTS AGE API: 7d9f 1/1 Running 0 10m WORKER: 5b8c 0/1 CrashLoopBackOff 6 9m REDIS: 0 1/1 Running 0 2h MIGRATOR: 9z1q 0/1 Error 0 4m' |
| `cargo-04` | `instruction_following` | `cargo` | `2826.13` | `0.466` | `0.466` | `+0.000` | `1.000` | `0.674` | `0.333` | `0.333` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `4372.19` | `0.338` | `0.338` | `+0.000` | `0.714` | `0.505` | `0.438` | `0.398` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | rsync, exit code 23 | - |
| `pyright-01` | `structured` | `pyright` | `7041.45` | `0.000` | `0.000` | `+0.000` | `0.267` | `0.312` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | file, /repo/app/user.py, line, code | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```python from typing import Optional from django.db import errors def reportOptionalMemberAccess(email: Optional[str] = None): if email is None: return try:...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass="```python from typing import Optional from django.db import errors def reportOptionalMemberAccess(email: Optional[str] = None): if email is None: return if '..." |
| `terraform-10` | `structured` | `terraform` | `9410.90` | `0.109` | `0.109` | `+0.000` | `0.833` | `0.414` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | aws_lambda_function.api | - |
| `junit-01` | `structured` | `junit` | `37850.20` | `0.000` | `0.000` | `+0.000` | `0.571` | `0.337` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | Test, Location, CalculatorTest | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='| Error | Code | |----------------------------------------------------------------------|--------------------------------------------------------------------...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='| Error | Code' |
| `kubernetes-03` | `structured` | `kubernetes` | `7025.11` | `0.134` | `0.134` | `+0.000` | `1.000` | `0.183` | `0.056` | `0.042` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `5078.57` | `0.037` | `0.047` | `-0.011` | `0.111` | `0.174` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | src/a.ts, line, column, rule, src/b.ts | - |
| `docker-build-04` | `structured` | `docker-build` | `4291.64` | `0.403` | `0.121` | `+0.281` | `0.407` | `0.380` | `0.583` | `0.583` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | stage, builder, command, pnpm | - |
| `go-test-04` | `structured` | `go-test` | `5659.34` | `0.000` | `0.000` | `+0.000` | `0.697` | `0.863` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | amount_test.go:22 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```yaml - fail_tests: FAIL amount_test.go:22: got 10.0 want 10.00 - fail_tests: FAIL currency_test.go:51: got USD 10 want $10.00 ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```yaml - failed_tests name: TestParseAmount location: 0.00s message: got 10.0 want 10.00 - failed_tests name: TestFormatCurrency location: 51s message: got ...' |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `2099.39` | `0.183` | `0.183` | `+0.000` | `1.000` | `0.679` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `6931.42` | `0.386` | `0.110` | `+0.277` | `0.500` | `0.274` | `0.571` | `0.571` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | package, legacy-widget@2.4.0, required | - |
| `mypy-06` | `structured` | `mypy` | `22026.33` | `0.000` | `0.000` | `+0.000` | `0.000` | `0.267` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | File, Line, Code, Message, ---, app/api.py | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='| Module Name | Error Description' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='Found 2 errors in 2 files' |
| `gradle-03` | `structured` | `gradle` | `7086.48` | `0.054` | `0.064` | `-0.010` | `0.242` | `0.185` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | failed, task, :api:compileJava, cause | - |
| `playwright-02` | `structured` | `playwright` | `7033.86` | `0.070` | `0.124` | `-0.054` | `0.333` | `0.191` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | project, file, line, test | - |
| `postgres-04` | `structured` | `postgres` | `6215.59` | `0.000` | `0.000` | `+0.000` | `0.424` | `0.735` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | errors, file, line, message | fallback output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```sql psql:migrations/004.sql:12: ERROR: column "tenant_id" contains null values psql:migrations/004.sql:13: STATEMENT: ALTER TABLE users ALTER COLUMN tenan...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```sql psql:migrations/004.sql:12: ERROR: column "tenant_id" contains null values psql:migrations/004.sql:13: STATEMENT: ALTER TABLE users ALTER COLUMN tenan...' |
| `vite-01` | `structured` | `vite` | `9041.11` | `0.108` | `0.109` | `-0.000` | `1.000` | `0.225` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `2161.16` | `0.414` | `0.414` | `+0.000` | `1.000` | `0.000` | `0.333` | `0.250` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `4967.65` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.275` | `0.070` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass="- Merge made by the 'ort' strategy. - commit 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 - Author: CI Bot - Status: deployed to staging" repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass="Merge made by the 'ort' strategy. commit 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 Author: CI Bot Status: deployed to staging" |
| `docker-04` | `exact_format` | `docker` | `6212.79` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.331` | `0.311` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='pushed ghcr.io/acme/api:2026.05.18 digest: sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='pushed ghcr.io/acme/api:2026.05.18 digest: sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 verified ghcr.io/acme/api@sha256:aaaaaaaa1...' |
| `npm-08` | `exact_format` | `npm` | `1680.47` | `0.126` | `0.126` | `+0.000` | `1.000` | `0.286` | `0.100` | `0.072` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `4250.49` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.321` | `0.175` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='FAIL: TestCheckoutAppliesCoupon (0.01s) checkout_test.go:77: got 120 want 100' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='- github.com/acme/shop/checkout - TestCheckoutAppliesCoupon - 0.01s - got 120 want 100' |
| `kubectl-09` | `exact_format` | `kubectl` | `1957.54` | `0.310` | `0.310` | `+0.000` | `1.000` | `0.303` | `0.325` | `0.283` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `2153.23` | `0.394` | `0.394` | `+0.000` | `1.000` | `0.000` | `0.308` | `0.227` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `3461.65` | `0.121` | `0.121` | `+0.000` | `1.000` | `0.247` | `0.093` | `0.068` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `4629.60` | `0.201` | `0.171` | `+0.030` | `1.000` | `0.249` | `0.220` | `0.158` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `5486.81` | `0.693` | `0.533` | `+0.161` | `0.444` | `0.886` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | /repo/scripts/email.py | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `6323.74` | `0.934` | `0.623` | `+0.311` | `1.000` | `0.869` | `1.000` | `0.982` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `4664.81` | `0.581` | `0.581` | `+0.000` | `0.000` | `0.612` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | orders_customer_id_fkey, customer_id, customers | - |
| `docker-build-05` | `explanation` | `docker-build` | `6207.09` | `0.960` | `0.000` | `+0.960` | `1.000` | `0.899` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `2009.00` | `0.969` | `0.646` | `+0.323` | `1.000` | `0.922` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `1730.84` | `0.935` | `0.624` | `+0.311` | `1.000` | `0.838` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `4714.41` | `0.628` | `0.473` | `+0.156` | `0.167` | `0.869` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | contents: read, contents: write | - |
| `runtime-01` | `recall` | `runtime` | `6124.10` | `0.572` | `0.000` | `+0.572` | `1.000` | `0.914` | `0.500` | `0.377` | `0.000` | `0.000` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `testing-01` | `recall` | `testing` | `5383.77` | `0.985` | `0.656` | `+0.328` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `1595.71` | `0.988` | `0.988` | `+0.000` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `1568.77` | `0.974` | `0.645` | `+0.329` | `1.000` | `0.897` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `5110.30` | `0.914` | `0.616` | `+0.298` | `1.000` | `0.925` | `1.000` | `0.883` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `4414.21` | `0.861` | `0.862` | `-0.001` | `1.000` | `0.906` | `1.000` | `0.794` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `4043.90` | `0.910` | `0.910` | `+0.000` | `1.000` | `0.928` | `1.000` | `0.873` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `1523.39` | `0.964` | `0.964` | `+0.000` | `1.000` | `0.858` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `1607.89` | `0.980` | `0.980` | `+0.000` | `1.000` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `2319.31` | `0.976` | `0.976` | `+0.000` | `1.000` | `0.906` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `4302.69` | `0.940` | `0.000` | `+0.940` | `1.000` | `0.933` | `1.000` | `0.925` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `3789.64` | `0.987` | `0.660` | `+0.327` | `1.000` | `0.946` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `1162.94` | `0.973` | `0.650` | `+0.323` | `1.000` | `0.894` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `build-01` | `recall` | `build` | `4205.58` | `0.592` | `0.592` | `+0.000` | `0.412` | `0.882` | `1.000` | `0.982` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Execution failed for task ':test' | - |
| `container-runtime-01` | `recall` | `container-runtime` | `1144.51` | `0.981` | `0.981` | `+0.000` | `1.000` | `0.925` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `2658.85` | `0.975` | `0.975` | `+0.000` | `1.000` | `0.899` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1572.70` | `0.970` | `0.645` | `+0.325` | `1.000` | `0.879` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `1027.65` | `0.991` | `0.662` | `+0.328` | `1.000` | `0.963` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `2783.14` | `0.986` | `0.986` | `+0.000` | `1.000` | `0.942` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `1246.31` | `0.958` | `0.958` | `+0.000` | `1.000` | `0.832` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `2044.85` | `0.977` | `0.651` | `+0.326` | `1.000` | `0.906` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `build-02` | `recall` | `build` | `1550.27` | `0.947` | `0.947` | `+0.000` | `1.000` | `0.892` | `1.000` | `0.954` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `8367.00` | `0.762` | `0.618` | `+0.144` | `1.000` | `0.912` | `1.000` | `0.855` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `3310.46` | `0.966` | `0.645` | `+0.321` | `1.000` | `0.865` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `build-03` | `summary` | `build` | `1750.22` | `0.925` | `0.613` | `+0.311` | `1.000` | `0.912` | `1.000` | `0.945` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `1381.17` | `0.886` | `0.591` | `+0.294` | `1.000` | `0.850` | `1.000` | `0.925` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `880.20` | `0.935` | `0.621` | `+0.314` | `1.000` | `0.837` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `1264.46` | `0.950` | `0.627` | `+0.323` | `1.000` | `0.875` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `1225.93` | `0.976` | `0.651` | `+0.325` | `1.000` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `1386.22` | `0.942` | `0.621` | `+0.321` | `1.000` | `0.855` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `4828.37` | `0.305` | `0.305` | `+0.000` | `1.000` | `0.624` | `0.200` | `0.165` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `1764.90` | `0.150` | `0.149` | `+0.000` | `1.000` | `0.246` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `6951.64` | `0.470` | `0.470` | `+0.000` | `1.000` | `0.929` | `0.500` | `0.359` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | - | - |
| `linting-02` | `structured` | `linting` | `1433.77` | `0.142` | `0.161` | `-0.020` | `1.000` | `0.180` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `2191.76` | `0.404` | `0.197` | `+0.207` | `1.000` | `0.325` | `0.354` | `0.354` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `3574.42` | `0.386` | `0.386` | `+0.000` | `0.500` | `0.589` | `0.500` | `0.450` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | InstanceId | - |
| `network-01` | `exact_format` | `network` | `1703.20` | `0.624` | `0.624` | `+0.000` | `1.000` | `0.332` | `0.675` | `0.574` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `3151.42` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.648` | `0.750` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response INFO: Retrying...' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response INFO: Retrying... ERROR: Timeout while waiting for response' |
| `shell-03` | `exact_format` | `shell` | `3857.78` | `0.173` | `0.173` | `+0.000` | `0.000` | `0.667` | `0.425` | `0.361` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, verbatim_alignment_weak | OUTPUT: | - |
| `shell-04` | `exact_format` | `shell` | `1452.22` | `0.290` | `0.290` | `+0.000` | `1.000` | `0.491` | `0.311` | `0.233` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `2211.02` | `0.837` | `0.837` | `+0.000` | `1.000` | `0.875` | `0.750` | `0.700` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-05` | `exact_format` | `build` | `3783.69` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.471` | `0.405` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='BUILD SUCCESSFUL in 10s - Verify input format - Review output for accuracy - Ensure no unnecessary processing' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='BUILD SUCCESSFUL in 10s - Verify input format - Ensure no unnecessary processing - Output: 2 actionable tasks: 2 up-to-date' |
| `shell-05` | `exact_format` | `shell` | `1423.27` | `0.587` | `0.587` | `+0.000` | `1.000` | `0.658` | `0.617` | `0.493` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `1604.73` | `0.880` | `0.589` | `+0.290` | `1.000` | `0.890` | `1.000` | `0.895` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `1641.67` | `0.874` | `0.587` | `+0.287` | `1.000` | `0.874` | `1.000` | `0.896` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `1390.80` | `0.967` | `0.644` | `+0.323` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `1388.25` | `0.962` | `0.642` | `+0.320` | `1.000` | `0.906` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `1252.02` | `0.953` | `0.635` | `+0.318` | `1.000` | `0.882` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `1260.15` | `0.961` | `0.637` | `+0.324` | `1.000` | `0.903` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `1007.34` | `0.949` | `0.634` | `+0.315` | `1.000` | `0.873` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `1113.26` | `0.946` | `0.630` | `+0.316` | `1.000` | `0.866` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1437.95` | `0.921` | `0.615` | `+0.306` | `1.000` | `0.887` | `1.000` | `0.954` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `979.54` | `0.960` | `0.630` | `+0.330` | `1.000` | `0.900` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `1232.38` | `0.965` | `0.639` | `+0.325` | `1.000` | `0.912` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `893.42` | `0.921` | `0.615` | `+0.306` | `1.000` | `0.802` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `1064.67` | `0.923` | `0.611` | `+0.312` | `1.000` | `0.808` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `1084.68` | `0.946` | `0.629` | `+0.317` | `1.000` | `0.864` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `1191.58` | `0.941` | `0.625` | `+0.316` | `1.000` | `0.853` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `1390.58` | `0.924` | `0.000` | `+0.924` | `1.000` | `0.809` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `1468.85` | `0.859` | `0.577` | `+0.281` | `1.000` | `0.874` | `1.000` | `0.874` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `1106.15` | `0.946` | `0.630` | `+0.315` | `1.000` | `0.864` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `1149.54` | `0.968` | `0.637` | `+0.331` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `2208.05` | `0.404` | `0.197` | `+0.207` | `1.000` | `0.325` | `0.354` | `0.354` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `3581.79` | `0.386` | `0.386` | `+0.000` | `0.500` | `0.589` | `0.500` | `0.450` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | InstanceId | - |
| `network-02` | `exact_format` | `network` | `1425.50` | `0.624` | `0.624` | `+0.000` | `1.000` | `0.332` | `0.675` | `0.574` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `2725.82` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | fallback output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response INFO: Retrying...' |
| `shell-07` | `exact_format` | `shell` | `2409.35` | `0.770` | `0.770` | `+0.000` | `1.000` | `0.000` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `2144.55` | `0.837` | `0.837` | `+0.000` | `1.000` | `0.875` | `0.750` | `0.700` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `1246.95` | `0.516` | `0.516` | `+0.000` | `1.000` | `0.319` | `0.560` | `0.476` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `1675.10` | `0.574` | `0.574` | `+0.000` | `1.000` | `0.850` | `0.560` | `0.504` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `1229.89` | `0.446` | `0.446` | `+0.000` | `1.000` | `0.646` | `0.467` | `0.373` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `1609.03` | `0.880` | `0.589` | `+0.290` | `1.000` | `0.890` | `1.000` | `0.895` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `1641.43` | `0.874` | `0.587` | `+0.287` | `1.000` | `0.874` | `1.000` | `0.896` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `1177.02` | `0.968` | `0.644` | `+0.324` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `1551.56` | `0.976` | `0.648` | `+0.328` | `1.000` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `1042.08` | `0.949` | `0.634` | `+0.315` | `1.000` | `0.873` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `1552.60` | `0.968` | `0.000` | `+0.968` | `1.000` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `5091.41` | `0.551` | `0.413` | `+0.139` | `0.000` | `0.889` | `1.000` | `0.914` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | undefined: fmt.Println | - |
| `explanation-17` | `explanation` | `explanation` | `1585.59` | `0.849` | `0.567` | `+0.282` | `1.000` | `0.892` | `1.000` | `0.850` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `1368.48` | `0.955` | `0.630` | `+0.324` | `1.000` | `0.886` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
