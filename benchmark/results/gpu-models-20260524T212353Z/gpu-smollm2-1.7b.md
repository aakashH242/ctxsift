# gpu-smollm2-1.7b

## Scenario

- track: `gpu`
- phase: `gpu-screen`
- model: `HuggingFaceTB/SmolLM2-1.7B-Instruct`
- quantization: `none`
- device: `cuda`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `1345091.43`
- cpu_rss_bytes: `7170678784`
- gpu_peak_bytes: `4725004288`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- recovered_final_score: `53.00`
- raw_final_score: `19.49`
- recovery_lift: `+33.51`
- case_count: `280`
- success_count: `267`
- accepted_count: `172`
- soft_accepted_count: `95`
- rejected_count: `13`
- exact_pass_count: `189`
- avg_inference_ms: `17674.62`
- p95_inference_ms: `68518.91`
- avg_exact_preservation_ratio: `0.809`
- avg_summary_quality_ratio: `0.819`
- avg_format_adherence_score: `0.848`
- avg_instruction_following_score: `0.805`
- avg_brevity_ratio: `0.836`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.725`
- p10_case_score: `0.218`
- quality_core: `0.624`
- latency_factor: `0.850`
- final_score: `53.00`
- peak_cpu_rss_bytes: `7168409600`
- peak_gpu_bytes: `5134195712`

### Raw View

- accepted_count: `1`
- soft_accepted_count: `138`
- rejected_count: `141`
- exact_pass_count: `189`
- avg_exact_preservation_ratio: `0.809`
- avg_summary_quality_ratio: `0.787`
- avg_format_adherence_score: `0.476`
- avg_instruction_following_score: `0.246`
- avg_brevity_ratio: `0.772`
- avg_thought_leakage_density: `0.000`
- avg_thought_marker_count: `0.00`
- avg_case_score: `0.287`
- p10_case_score: `0.000`
- quality_core: `0.229`
- final_score: `19.49`

## Cases

| case_id | family | domain | ms | recovered_score | raw_score | lift | preserve | quality | format | instruction | recovered_thought_density | raw_thought_density | recovered_validation | raw_validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `60048.73` | `0.586` | `0.584` | `+0.002` | `1.000` | `0.899` | `0.500` | `0.404` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-02` | `summary` | `python` | `6861.63` | `0.987` | `0.661` | `+0.326` | `1.000` | `0.969` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-03` | `recall` | `python` | `2762.16` | `0.470` | `0.000` | `+0.470` | `0.127` | `0.784` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | ./scripts/run-local-api.sh, /workspace/src/api/app.py, line 58, KeyError, JWT_PRIVATE_KEY | - |
| `python-04` | `recall` | `python` | `9478.71` | `0.988` | `0.660` | `+0.328` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-05` | `recall` | `python` | `7702.94` | `0.992` | `0.664` | `+0.329` | `1.000` | `0.969` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `27689.48` | `0.888` | `0.000` | `+0.888` | `1.000` | `0.935` | `1.000` | `0.830` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `65010.08` | `0.837` | `0.000` | `+0.837` | `1.000` | `0.933` | `1.000` | `0.810` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `10055.94` | `0.538` | `0.396` | `+0.142` | `0.250` | `0.882` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | pytest tests -q -x, tests/jobs/test_retention.py::test_archive_marks_job_deleted, teardown, 149 passed, 1 skipped, 1 error in 58.73s | - |
| `pytest-04` | `recall` | `pytest` | `9135.03` | `0.994` | `0.664` | `+0.330` | `1.000` | `0.975` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `5103.38` | `0.987` | `0.658` | `+0.329` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `5418.11` | `0.988` | `0.660` | `+0.328` | `1.000` | `0.952` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `35015.80` | `0.880` | `0.000` | `+0.880` | `1.000` | `0.951` | `1.000` | `0.862` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `7030.79` | `0.988` | `0.662` | `+0.327` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ruff-01` | `recall` | `ruff` | `6205.40` | `0.530` | `0.391` | `+0.140` | `0.267` | `0.815` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ruff check src --output-format=full, src/payments/init.py:1:20, all, Found 1 error. | - |
| `ruff-02` | `summary` | `ruff` | `2076.84` | `0.690` | `0.000` | `+0.690` | `0.400` | `0.905` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | src/api/serializers.py, 1 file would be reformatted, 52 files already formatted | - |
| `ruff-03` | `summary` | `ruff` | `7420.72` | `0.971` | `0.646` | `+0.325` | `1.000` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `2240.25` | `0.510` | `0.000` | `+0.510` | `0.190` | `0.858` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | pylint src/storage/path_utils.py, src/storage/path_utils.py:27:18, E1101, no-member | - |
| `pylint-02` | `recall` | `pylint` | `5856.33` | `0.987` | `0.657` | `+0.330` | `1.000` | `0.947` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `25315.02` | `0.964` | `0.000` | `+0.964` | `1.000` | `0.911` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `black-01` | `summary` | `black` | `3883.00` | `0.632` | `0.479` | `+0.153` | `0.200` | `0.858` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | black --check src tests, /workspace/src/api/routes.py, /workspace/tests/test_routes.py | - |
| `black-02` | `summary` | `black` | `7796.11` | `0.977` | `0.653` | `+0.324` | `1.000` | `0.943` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `black-03` | `recall` | `black` | `2922.12` | `0.685` | `0.524` | `+0.161` | `0.600` | `0.943` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | All done!, 2 files would be left unchanged | - |
| `npm-01` | `recall` | `npm` | `7036.34` | `0.978` | `0.653` | `+0.325` | `1.000` | `0.912` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `41047.56` | `0.640` | `0.498` | `+0.142` | `0.667` | `0.922` | `1.000` | `0.811` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | npm install | - |
| `npm-03` | `summary` | `npm` | `84776.16` | `0.802` | `0.000` | `+0.802` | `1.000` | `0.936` | `1.000` | `0.758` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `4645.38` | `0.657` | `0.500` | `+0.157` | `0.526` | `0.942` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | pnpm-lock.yaml, packages/web/package.json, --no-frozen-lockfile | - |
| `pnpm-02` | `summary` | `pnpm` | `8267.51` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `51623.77` | `0.834` | `0.000` | `+0.834` | `1.000` | `0.892` | `1.000` | `0.830` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `7692.80` | `0.705` | `0.541` | `+0.164` | `0.467` | `0.905` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | tsc -p tsconfig.json --noEmit, src/server/index.ts(3,18), src/server/index.ts(4,18) | - |
| `typescript-02` | `recall` | `typescript` | `19182.50` | `0.907` | `0.608` | `+0.299` | `1.000` | `0.928` | `1.000` | `0.867` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `23208.69` | `0.000` | `0.000` | `+0.000` | `0.615` | `0.954` | `0.500` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | unterminated_reasoning_block | src/index.ts(48,20), src/http.ts(9,17) | smollm2 output validation failed: model did not stop thinking before reaching the output limit. first_pass="TS2769: No overload matches this call. Overload 1 of 2, '(url: string, init?: RequestInit | undefined): Promise<Response>', gave the following error. Argumen..." repair_pass="$ tsc src/index.ts src/http.ts --pretty false Error TS2769: No overload matches this call. Overload 1 of 2, '(url: string, init?: RequestInit | undefined): P..." |
| `eslint-01` | `recall` | `eslint` | `13896.53` | `0.972` | `0.000` | `+0.972` | `1.000` | `0.938` | `1.000` | `0.979` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `9698.99` | `0.783` | `0.609` | `+0.173` | `0.773` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ESLint: 9.14.0 | - |
| `eslint-03` | `recall` | `eslint` | `9109.27` | `0.520` | `0.381` | `+0.138` | `0.192` | `0.899` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | eslint src --max-warnings=0, /workspace/src/hooks/useCart.ts, react-hooks/exhaustive-deps, maximum: 0 | - |
| `docker-01` | `recall` | `docker` | `68521.62` | `0.683` | `0.522` | `+0.161` | `0.592` | `0.949` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | COPY docker/entrypoint.sh /entrypoint.sh, /docker/entrypoint.sh | - |
| `docker-02` | `summary` | `docker` | `2006.76` | `0.987` | `0.657` | `+0.330` | `1.000` | `0.967` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `13052.12` | `0.977` | `0.652` | `+0.325` | `1.000` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `3557.73` | `0.975` | `0.649` | `+0.326` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `34423.90` | `0.846` | `0.574` | `+0.272` | `1.000` | `0.916` | `1.000` | `0.763` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `9203.47` | `0.964` | `0.638` | `+0.326` | `1.000` | `0.928` | `1.000` | `0.990` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `15112.39` | `0.844` | `0.564` | `+0.280` | `1.000` | `0.941` | `1.000` | `0.816` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `48494.91` | `0.853` | `0.579` | `+0.275` | `1.000` | `0.936` | `1.000` | `0.767` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `4683.29` | `0.987` | `0.659` | `+0.328` | `1.000` | `0.968` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `132940.34` | `0.524` | `0.523` | `+0.001` | `0.524` | `0.862` | `1.000` | `0.730` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | kubectl logs payments-worker-6f8f7d4df5-z5vsm -c worker --previous -n payments, payments-worker-6f8f7d4df5-z5vsm, invalid worker.concurrency | - |
| `terraform-01` | `summary` | `terraform` | `16937.00` | `0.978` | `0.652` | `+0.326` | `1.000` | `0.944` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `59924.01` | `0.873` | `0.000` | `+0.873` | `1.000` | `0.918` | `1.000` | `0.811` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `11481.48` | `0.988` | `0.000` | `+0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `43555.09` | `0.953` | `0.000` | `+0.953` | `1.000` | `0.939` | `1.000` | `0.970` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `4895.56` | `0.990` | `0.661` | `+0.329` | `1.000` | `0.961` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `19941.13` | `0.888` | `0.591` | `+0.296` | `1.000` | `0.886` | `1.000` | `0.908` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `git-01` | `recall` | `git` | `54746.04` | `0.589` | `0.000` | `+0.589` | `1.000` | `0.902` | `0.500` | `0.407` | `0.000` | `0.000` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `git-02` | `recall` | `git` | `28285.52` | `0.864` | `0.000` | `+0.864` | `1.000` | `0.867` | `1.000` | `0.816` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `git-03` | `recall` | `git` | `4651.79` | `0.989` | `0.659` | `+0.329` | `1.000` | `0.955` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `10689.31` | `0.990` | `0.000` | `+0.990` | `1.000` | `0.958` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `curl-02` | `recall` | `curl` | `3499.25` | `0.557` | `0.412` | `+0.145` | `0.286` | `0.908` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | HTTP/2 301, location: /sdk/v3.4/, cache-control: max-age=3600 | - |
| `ssh-01` | `summary` | `ssh` | `29944.78` | `0.967` | `0.000` | `+0.967` | `1.000` | `0.953` | `1.000` | `0.981` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `17429.48` | `0.973` | `0.648` | `+0.326` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `43240.96` | `0.842` | `0.000` | `+0.842` | `1.000` | `0.915` | `1.000` | `0.828` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `3015.34` | `0.962` | `0.639` | `+0.322` | `1.000` | `0.904` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `39834.03` | `0.848` | `0.000` | `+0.848` | `1.000` | `0.932` | `1.000` | `0.827` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `71181.25` | `0.491` | `0.356` | `+0.136` | `0.143` | `0.856` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | sudo dnf install python3-devel postgresql-devel, conflicting requests, python3.12-3.12.0-1.el9.x86_64, python3.12-3.12.2-2.el9.x86_64 | - |
| `go-build-01` | `summary` | `go-build` | `29195.65` | `0.752` | `0.584` | `+0.168` | `0.700` | `0.901` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | go build ./cmd/api | - |
| `go-test-01` | `summary` | `go-test` | `48378.06` | `0.882` | `0.000` | `+0.882` | `1.000` | `0.928` | `1.000` | `0.877` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `javac-01` | `recall` | `javac` | `29249.02` | `0.984` | `0.000` | `+0.984` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `maven-01` | `recall` | `maven` | `10660.33` | `0.478` | `0.344` | `+0.134` | `0.087` | `0.891` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | mvn -q test, UserControllerTest.java:72, maven-surefire-plugin:3.5.5:test, /workspace/webapp/target/surefire-reports | - |
| `maven-02` | `summary` | `maven` | `59784.57` | `0.842` | `0.000` | `+0.842` | `1.000` | `0.928` | `1.000` | `0.821` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `23605.23` | `0.856` | `0.579` | `+0.277` | `1.000` | `0.932` | `1.000` | `0.773` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `34381.30` | `0.629` | `0.489` | `+0.141` | `0.667` | `0.901` | `1.000` | `0.803` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ./gradlew test | - |
| `cargo-01` | `recall` | `cargo` | `10079.10` | `0.985` | `0.658` | `+0.327` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `cargo-02` | `recall` | `cargo` | `22644.82` | `0.773` | `0.602` | `+0.172` | `0.833` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | crates.io index | - |
| `node-runtime-01` | `recall` | `node-runtime` | `74817.95` | `0.591` | `0.000` | `+0.591` | `1.000` | `0.924` | `0.500` | `0.404` | `0.000` | `0.000` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `npm-04` | `summary` | `npm` | `62497.19` | `0.626` | `0.487` | `+0.138` | `0.684` | `0.919` | `1.000` | `0.780` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | npm install | - |
| `tsc-01` | `summary` | `tsc` | `9913.39` | `0.976` | `0.647` | `+0.329` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `30798.90` | `0.916` | `0.000` | `+0.916` | `1.000` | `0.921` | `1.000` | `0.929` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `python-runtime-01` | `recall` | `python-runtime` | `43588.20` | `0.615` | `0.613` | `+0.002` | `1.000` | `0.943` | `0.500` | `0.435` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `pytest-06` | `summary` | `pytest` | `34409.05` | `0.838` | `0.000` | `+0.838` | `1.000` | `0.912` | `1.000` | `0.824` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `25972.56` | `0.966` | `0.000` | `+0.966` | `1.000` | `0.929` | `1.000` | `0.992` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `74528.09` | `0.810` | `0.000` | `+0.810` | `1.000` | `0.932` | `1.000` | `0.772` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `33391.57` | `0.842` | `0.000` | `+0.842` | `1.000` | `0.906` | `1.000` | `0.833` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `4063.98` | `0.676` | `0.519` | `+0.157` | `0.333` | `0.905` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | kubectl apply -f k8s/, field is immutable | - |
| `kubectl-06` | `summary` | `kubectl` | `142404.50` | `0.556` | `0.556` | `+0.000` | `0.000` | `0.760` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | kubectl describe pod web-7f6f6d9d7b-kj4t2 -n dev, migrate, CrashLoopBackOff, Exit Code:    1 | - |
| `kubectl-07` | `recall` | `kubectl` | `6394.85` | `0.988` | `0.660` | `+0.328` | `1.000` | `0.954` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `12771.97` | `0.702` | `0.540` | `+0.163` | `0.636` | `0.960` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | terraform plan -lock-timeout=5s -out=tfplan | - |
| `terraform-06` | `summary` | `terraform` | `18076.37` | `0.917` | `0.608` | `+0.308` | `1.000` | `0.913` | `1.000` | `0.934` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `28534.64` | `0.837` | `0.558` | `+0.279` | `1.000` | `0.895` | `1.000` | `0.832` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `6087.11` | `0.696` | `0.535` | `+0.161` | `0.389` | `0.929` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | sudo nginx -t, configuration file /etc/nginx/nginx.conf test failed | - |
| `nginx-02` | `summary` | `nginx` | `12673.12` | `0.975` | `0.649` | `+0.325` | `1.000` | `0.937` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `12909.68` | `0.988` | `0.660` | `+0.328` | `1.000` | `0.952` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `15913.77` | `0.969` | `0.000` | `+0.969` | `1.000` | `0.922` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `5386.36` | `0.989` | `0.660` | `+0.329` | `1.000` | `0.972` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `5162.47` | `0.988` | `0.660` | `+0.328` | `1.000` | `0.970` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `9571.69` | `0.621` | `0.468` | `+0.152` | `0.189` | `0.889` | `1.000` | `0.967` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | redis-cli -u redis://127.0.0.1:6379 SET sync:cursor 90210, MISCONF, sync:cursor | - |
| `redis-02` | `recall` | `redis` | `2449.82` | `0.505` | `0.370` | `+0.136` | `0.167` | `0.879` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | redis-cli -u redis://127.0.0.1:6379 PING, LOADING | - |
| `github-actions-01` | `recall` | `github-actions` | `64844.84` | `0.622` | `0.622` | `-0.001` | `0.714` | `0.905` | `1.000` | `0.779` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ruff check . | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `73496.51` | `0.804` | `0.000` | `+0.804` | `1.000` | `0.912` | `1.000` | `0.774` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `2196.26` | `0.967` | `0.642` | `+0.325` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `make-01` | `summary` | `make` | `31138.41` | `0.901` | `0.000` | `+0.901` | `1.000` | `0.924` | `1.000` | `0.906` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `tar-01` | `summary` | `tar` | `7454.83` | `0.984` | `0.657` | `+0.326` | `1.000` | `0.959` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `4234.33` | `0.645` | `0.489` | `+0.155` | `0.500` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | proxy-2, UNREACHABLE!, Connection timed out | - |
| `rsync-01` | `summary` | `rsync` | `3944.52` | `0.981` | `0.654` | `+0.327` | `1.000` | `0.953` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `19902.47` | `0.992` | `0.663` | `+0.329` | `1.000` | `0.968` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `70784.12` | `0.520` | `0.519` | `+0.001` | `0.851` | `0.878` | `0.500` | `0.381` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | src/router.rs:128 | - |
| `ci-log-01` | `recall` | `ci-log` | `38010.70` | `0.896` | `0.604` | `+0.292` | `1.000` | `0.930` | `1.000` | `0.847` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `79274.12` | `0.867` | `0.000` | `+0.867` | `1.000` | `0.942` | `1.000` | `0.789` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `7248.40` | `0.617` | `0.467` | `+0.150` | `0.071` | `0.894` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | github.com/acme/shop/checkout, TestCheckoutAppliesStoreCredit, checkout_test.go:71, github.com/acme/shop/inventory, TestReconcileInventory, test timed out after 10m0s, worker.go:144 | - |
| `build-log-01` | `summary` | `build-log` | `67556.00` | `0.552` | `0.000` | `+0.552` | `1.000` | `0.891` | `0.500` | `0.406` | `0.000` | `0.000` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `docker-build-02` | `summary` | `docker-build` | `3932.82` | `0.582` | `0.000` | `+0.582` | `0.000` | `0.836` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | Dockerfile:18, COPY apps/web ./apps/web, "/apps/web": not found | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `18683.05` | `0.319` | `0.000` | `+0.319` | `1.000` | `0.627` | `0.250` | `0.187` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `58076.04` | `0.528` | `0.000` | `+0.528` | `0.286` | `0.628` | `0.750` | `0.750` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | packages/api/src/auth/session.ts, packages/api/src/schema/openapi.yaml, migrations/202605171200_add_refresh_ttl.sql | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `17429.97` | `0.692` | `0.000` | `+0.692` | `0.226` | `0.300` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | exit status 22, https://staging.example.com/api/search?q=smoke, curl: (22) | - |
| `structured-output-01` | `structured` | `structured-output` | `18443.77` | `0.215` | `0.000` | `+0.215` | `1.000` | `0.879` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `60595.99` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.388` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='test / integration failed in 4m02s Step: Start docker compose Command: docker compose up -d postgres redis Error: service "postgres" failed to start: Bind fo...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='port 5432 is already allocated - deploy / preview - upload artifact - dist/preview Step: Start docker compose Command: docker compose up -d postgres redis Er...' |
| `structured-output-03` | `structured` | `structured-output` | `55545.79` | `0.662` | `0.000` | `+0.662` | `0.500` | `0.629` | `1.000` | `0.970` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | createSession › rejects expired refresh token, calculateTax › uses EU VAT for DE customer, Expected: 19, Received: 0 | - |
| `structured-output-04` | `structured` | `structured-output` | `8404.72` | `0.143` | `0.000` | `+0.143` | `1.000` | `0.195` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `135078.11` | `0.000` | `0.000` | `+0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors, verbatim_alignment_weak | tests/api/test_users.py::test_create_user_requires_email, tests/api/test_users.py::test_delete_user_requires_admin, tests/jobs/test_reconcile.py::TestReconcile::test_retries_deadlock | - |
| `exact-format-02` | `exact_format` | `exact-format` | `8027.41` | `0.218` | `0.000` | `+0.218` | `0.714` | `0.425` | `0.297` | `0.242` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | SearchBox debounces network query before fetch | - |
| `exact-format-03` | `exact_format` | `exact-format` | `50983.31` | `0.497` | `0.000` | `+0.497` | `1.000` | `0.335` | `0.550` | `0.440` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `9926.81` | `0.648` | `0.491` | `+0.157` | `0.222` | `0.893` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | /repo/tools/json.py, shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `7652.76` | `0.606` | `0.460` | `+0.146` | `0.250` | `0.752` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | TS2322, AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `24906.62` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.420` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- customer_id - 00000000-0000-0000-0000-000000000000 - customers Explanation: - The migration failed because the customer_id column was not added to the orde...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='Applying migration 202605181045_add_order_customer_fk.sql BEGIN; ALTER TABLE orders ADD COLUMN customer_id uuid; ALTER TABLE orders ADD CONSTRAINT orders_cus...' |
| `python-traceback-01` | `recall` | `python-traceback` | `70246.11` | `0.887` | `0.000` | `+0.887` | `1.000` | `0.926` | `1.000` | `0.832` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `4327.84` | `0.986` | `0.658` | `+0.327` | `1.000` | `0.942` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `26406.00` | `0.979` | `0.000` | `+0.979` | `1.000` | `0.917` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `11862.45` | `0.985` | `0.658` | `+0.327` | `1.000` | `0.940` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `6292.10` | `0.985` | `0.657` | `+0.328` | `1.000` | `0.941` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `85165.86` | `0.869` | `0.000` | `+0.869` | `1.000` | `0.924` | `1.000` | `0.800` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `66151.69` | `0.886` | `0.000` | `+0.886` | `1.000` | `0.927` | `1.000` | `0.830` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `26787.73` | `0.930` | `0.000` | `+0.930` | `1.000` | `0.923` | `1.000` | `0.911` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `32509.46` | `0.983` | `0.000` | `+0.983` | `1.000` | `0.933` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `7257.37` | `0.989` | `0.661` | `+0.328` | `1.000` | `0.957` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `132600.35` | `0.520` | `0.520` | `+0.000` | `0.211` | `0.868` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | --frozen-lockfile, pnpm-lock.yaml, packages/api/package.json, fastify, ^5.1.0, ^5.2.1 | - |
| `swift-01` | `recall` | `swift` | `27294.05` | `0.964` | `0.000` | `+0.964` | `1.000` | `0.935` | `1.000` | `0.966` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `68512.59` | `0.801` | `0.625` | `+0.176` | `0.913` | `0.927` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | refreshes expired keys | - |
| `rails-01` | `recall` | `rails` | `19725.66` | `0.966` | `0.645` | `+0.321` | `1.000` | `0.943` | `1.000` | `0.966` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `29058.63` | `0.962` | `0.000` | `+0.962` | `1.000` | `0.937` | `1.000` | `0.961` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `12734.26` | `0.979` | `0.651` | `+0.328` | `1.000` | `0.918` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `12656.72` | `0.982` | `0.657` | `+0.325` | `1.000` | `0.926` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `28859.34` | `0.929` | `0.000` | `+0.929` | `1.000` | `0.931` | `1.000` | `0.906` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `37240.29` | `0.983` | `0.000` | `+0.983` | `1.000` | `0.934` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `17205.77` | `0.983` | `0.655` | `+0.327` | `1.000` | `0.932` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `6128.12` | `0.793` | `0.620` | `+0.174` | `0.882` | `0.945` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | exit code 1 | - |
| `python-pytest-01` | `summary` | `python-pytest` | `35544.83` | `0.963` | `0.000` | `+0.963` | `1.000` | `0.908` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `2233.86` | `0.616` | `0.000` | `+0.616` | `0.105` | `0.871` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | ./integration, runtime, github.com/acme/api/internal/webhook, Dispatcher, dispatch | - |
| `npm-05` | `summary` | `npm` | `5233.47` | `0.698` | `0.534` | `+0.164` | `0.467` | `0.886` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | TS2339, Property, roleName | - |
| `helm-01` | `summary` | `helm` | `2221.41` | `0.930` | `0.617` | `+0.312` | `0.875` | `0.902` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | template | - |
| `ruff-04` | `summary` | `ruff` | `13848.24` | `0.619` | `0.465` | `+0.154` | `0.211` | `0.815` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | app/api/routes.py:3:1, app/services/user.py:88:89, tests/test_user.py:12:1 | - |
| `k6-01` | `summary` | `k6` | `3802.12` | `0.606` | `0.456` | `+0.150` | `0.174` | `0.798` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | smoke.js, http_req_failed, http_req_duration, avg | - |
| `composer-01` | `summary` | `composer` | `3101.88` | `0.636` | `0.483` | `+0.154` | `0.200` | `0.871` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | composer, --no-dev, Loading, composer | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `4920.74` | `0.944` | `0.627` | `+0.317` | `1.000` | `0.859` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `make-02` | `summary` | `make` | `5547.80` | `0.959` | `0.637` | `+0.322` | `1.000` | `0.897` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `13312.68` | `0.969` | `0.646` | `+0.323` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `8125.66` | `0.964` | `0.644` | `+0.320` | `1.000` | `0.909` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `15072.22` | `0.954` | `0.000` | `+0.954` | `1.000` | `0.885` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `4983.07` | `0.627` | `0.474` | `+0.153` | `0.186` | `0.853` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | tests/test_signup.py, FAILED, tests/test_signup.py::test_signup_is_idempotent, psycopg.errors.UniqueViolation | - |
| `wrangler-01` | `summary` | `wrangler` | `2568.07` | `0.579` | `0.436` | `+0.142` | `0.000` | `0.828` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | wrangler, deploy, Total, Upload, 183.22 | - |
| `python-pytest-04` | `summary` | `python-pytest` | `65540.82` | `0.816` | `0.817` | `-0.000` | `1.000` | `0.913` | `1.000` | `0.792` | `0.000` | `0.000` | `accepted` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `17520.44` | `0.358` | `0.000` | `+0.358` | `0.630` | `0.718` | `0.333` | `0.333` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | src/App.tsx, src/api.ts | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `9125.94` | `0.480` | `0.000` | `+0.480` | `0.882` | `0.625` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | JWT expiry from 15m to 7d | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `17522.59` | `0.316` | `0.000` | `+0.316` | `1.000` | `0.000` | `0.202` | `0.146` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `7388.90` | `0.530` | `0.000` | `+0.530` | `1.000` | `0.626` | `0.500` | `0.428` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `2758.94` | `0.597` | `0.000` | `+0.597` | `1.000` | `0.675` | `0.500` | `0.500` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `6085.35` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `31732.53` | `0.178` | `0.000` | `+0.178` | `0.200` | `0.312` | `0.277` | `0.277` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | [deps 4/4], pnpm install --frozen-lockfile, exit code: 1 | - |
| `terraform-09` | `instruction_following` | `terraform` | `11207.93` | `0.344` | `0.000` | `+0.344` | `0.667` | `0.615` | `0.333` | `0.333` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | identifier = "prod-main" | - |
| `maven-03` | `instruction_following` | `maven` | `74756.25` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.917` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='- UserService.java:[44,17] - findByEmail - UserController.java:[28,31] - java.lang.Long - java.util.UUID [ERROR] /repo/src/main/java/UserService.java:[44,17]...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='[ERROR] /repo/src/main/java/UserService.java:[44,17] - UserService.java:[44,17] cannot find symbol - UserService.java:[44,17] - UserService.java:[44,17] - Us...' |
| `playwright-01` | `instruction_following` | `playwright` | `2760.39` | `0.401` | `0.000` | `+0.401` | `1.000` | `0.682` | `0.250` | `0.250` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `3202.46` | `0.850` | `0.000` | `+0.850` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | verbatim_alignment_weak | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `6162.08` | `0.484` | `0.000` | `+0.484` | `1.000` | `0.000` | `0.467` | `0.467` | `0.000` | `0.000` | `soft_accepted` | `rejected` | verbatim_alignment_weak | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `7985.89` | `0.668` | `0.000` | `+0.668` | `0.333` | `0.730` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | src/auth.rs:88, Option::unwrap(), left: 1750, right: 1749 | - |
| `shell-01` | `instruction_following` | `shell` | `3898.87` | `0.328` | `0.000` | `+0.328` | `1.000` | `0.327` | `0.318` | `0.318` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `7887.45` | `0.341` | `0.000` | `+0.341` | `1.000` | `0.192` | `0.338` | `0.313` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `10956.14` | `0.123` | `0.000` | `+0.123` | `1.000` | `0.189` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `junit-01` | `structured` | `junit` | `8001.39` | `0.000` | `0.000` | `+0.000` | `0.571` | `0.394` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | Error, Location | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```markdown | Test | Result | | --- | --- | | CalculatorTest | dividesByZero FAILED | | UserServiceTest | rejectsDuplicateEmail FAILED | ```' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='```markdown | Test | Result | | --- | --- | | CalculatorTest | dividesByZero FAILED | | UserServiceTest | rejectsDuplicateEmail FAILED | ```' |
| `kubernetes-03` | `structured` | `kubernetes` | `11346.26` | `0.163` | `0.000` | `+0.163` | `1.000` | `0.186` | `0.100` | `0.079` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `16575.87` | `0.287` | `0.000` | `+0.287` | `0.667` | `0.185` | `0.500` | `0.387` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | line, column, rule | - |
| `docker-build-04` | `structured` | `docker-build` | `4248.21` | `0.769` | `0.000` | `+0.769` | `0.852` | `0.659` | `0.800` | `0.800` | `0.000` | `0.000` | `accepted` | `rejected` | - | build | - |
| `go-test-04` | `structured` | `go-test` | `75628.65` | `0.000` | `0.000` | `+0.000` | `0.424` | `0.569` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | failed_tests, name, location, message | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='TestParseAmount (0.00s) amount_test.go:22: got 10.0 want 10.00 --- FAIL: TestFormatCurrency (0.00s) currency_test.go:51: got USD 10 want $10.00 FAIL --- FAIL...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='--- FAIL: TestParseAmount (0.00s) amount_test.go:22: got 10.0 want 10.00 --- FAIL: TestFormatCurrency (0.00s) currency_test.go:51: got USD 10 want $10.00 FAI...' |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `10329.29` | `0.000` | `0.000` | `+0.000` | `0.833` | `0.587` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | --- | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```markdown Job: lint Step: success Time: 22s Job: test Step: failed Reason: Run unit tests Exit: 1 Job: build Step: success Time: 49s Job: deploy Step: fail...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='job lint success 22s job test failed step="Run unit tests" exit=1 job build success 49s job deploy failed step="Upload artifact" exit=1' |
| `npm-07` | `structured` | `npm` | `4156.25` | `0.760` | `0.000` | `+0.760` | `1.000` | `0.530` | `0.800` | `0.800` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `13245.96` | `0.000` | `0.000` | `+0.000` | `0.733` | `0.833` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | Message, --- | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='```markdown File: app/api.py Line: 10 Code: Module has no attribute "Router" Error: [attr-defined] File: app/auth.py Line: 44 Code: Incompatible return value...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='app/api.py:10: error: Module has no attribute "Router" [attr-defined] app/auth.py:44: error: Incompatible return value type (got "None", expected "User") [re...' |
| `gradle-03` | `structured` | `gradle` | `9098.29` | `0.072` | `0.000` | `+0.072` | `0.424` | `0.187` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | failed, cause, cannot, find | - |
| `playwright-02` | `structured` | `playwright` | `4931.09` | `0.361` | `0.000` | `+0.361` | `1.000` | `0.185` | `0.338` | `0.338` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `74395.10` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.752` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='errors - file - migrations/004.sql - line - message - column psql:migrations/004.sql:12: ERROR: column "tenant_id" contains null values psql:migrations/004.s...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='- file: migrations/004.sql - line: 12 - message: ERROR: column "tenant_id" contains null values - column: tenant_id - column: null - column: values - column:...' |
| `vite-01` | `structured` | `vite` | `18414.67` | `0.061` | `0.000` | `+0.061` | `0.600` | `0.187` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | /repo/apps/admin/src/client.ts, /repo/apps/public/src/Home.tsx | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `5373.30` | `0.850` | `0.000` | `+0.850` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | verbatim_alignment_weak | - | - |
| `git-04` | `exact_format` | `git` | `3299.27` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `5421.98` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `974.18` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `1701.82` | `0.086` | `0.000` | `+0.086` | `0.000` | `0.233` | `0.150` | `0.150` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | github.com/acme/shop/checkout, TestCheckoutAppliesCoupon | - |
| `kubectl-09` | `exact_format` | `kubectl` | `21045.23` | `0.088` | `0.000` | `+0.088` | `0.000` | `0.270` | `0.150` | `0.150` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | migrator-v2-9xk, prod | - |
| `cargo-05` | `exact_format` | `cargo` | `2433.72` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `794.69` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `1757.02` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `2204.21` | `0.660` | `0.000` | `+0.660` | `0.444` | `0.789` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | /repo/scripts/email.py | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `3247.95` | `0.567` | `0.421` | `+0.146` | `0.000` | `0.794` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | string | null, url: string, user.photoUrl | - |
| `postgres-05` | `explanation` | `postgres` | `6408.45` | `0.719` | `0.000` | `+0.719` | `0.667` | `0.708` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | orders_customer_id_fkey | - |
| `docker-build-05` | `explanation` | `docker-build` | `3254.99` | `0.738` | `0.567` | `+0.170` | `0.636` | `0.897` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | COPY | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `9412.40` | `0.962` | `0.641` | `+0.321` | `1.000` | `0.906` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `3701.12` | `0.725` | `0.561` | `+0.164` | `0.750` | `0.788` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | returns a reference | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `5847.97` | `0.714` | `0.553` | `+0.161` | `0.583` | `0.862` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `19230.40` | `0.984` | `0.000` | `+0.984` | `1.000` | `0.938` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `testing-01` | `recall` | `testing` | `2677.22` | `0.988` | `0.659` | `+0.329` | `1.000` | `0.952` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `18864.44` | `0.660` | `0.000` | `+0.660` | `1.000` | `0.950` | `0.500` | `0.500` | `0.000` | `0.000` | `soft_accepted` | `rejected` | plain_text_style_mismatch | - | - |
| `package-management-01` | `recall` | `package-management` | `3523.93` | `0.455` | `0.319` | `+0.135` | `0.000` | `0.940` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | npm ERR! code E404, 404 Not Found, GET https://registry.npmjs.org/foo | - |
| `runtime-02` | `recall` | `runtime` | `4230.81` | `0.715` | `0.548` | `+0.167` | `0.667` | `0.965` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `5893.48` | `0.633` | `0.478` | `+0.155` | `0.545` | `0.940` | `1.000` | `0.931` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Program.cs(15,10) | - |
| `package-management-02` | `recall` | `package-management` | `9600.24` | `0.614` | `0.612` | `+0.002` | `1.000` | `0.894` | `0.500` | `0.448` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-01` | `recall` | `ci` | `10077.94` | `0.839` | `0.000` | `+0.839` | `1.000` | `0.813` | `1.000` | `0.793` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `testing-03` | `recall` | `testing` | `6069.64` | `0.590` | `0.440` | `+0.150` | `0.364` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | COPY failed | - |
| `deployment-01` | `recall` | `deployment` | `5268.42` | `0.978` | `0.652` | `+0.327` | `1.000` | `0.913` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `5412.49` | `0.742` | `0.574` | `+0.168` | `0.778` | `0.892` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | "ami" is required | - |
| `compilation-02` | `recall` | `compilation` | `66254.09` | `0.864` | `0.000` | `+0.864` | `1.000` | `0.924` | `1.000` | `0.792` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `ci-02` | `recall` | `ci` | `1393.89` | `0.975` | `0.649` | `+0.326` | `1.000` | `0.900` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `build-01` | `recall` | `build` | `2269.12` | `0.975` | `0.649` | `+0.326` | `1.000` | `0.900` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `768.74` | `0.982` | `0.654` | `+0.328` | `1.000` | `0.929` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `2553.52` | `0.449` | `0.318` | `+0.131` | `0.000` | `0.913` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | package com.google.common does not exist, 1 error | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1337.73` | `0.969` | `0.643` | `+0.327` | `1.000` | `0.878` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `921.67` | `0.996` | `0.659` | `+0.337` | `1.000` | `0.984` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `9389.49` | `0.986` | `0.000` | `+0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `4462.90` | `0.594` | `0.444` | `+0.149` | `0.364` | `0.939` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | COPY failed | - |
| `testing-04` | `recall` | `testing` | `6223.39` | `0.762` | `0.593` | `+0.170` | `0.833` | `0.888` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | User signs in | - |
| `build-02` | `recall` | `build` | `3032.41` | `0.976` | `0.650` | `+0.326` | `1.000` | `0.906` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `12549.99` | `0.833` | `0.654` | `+0.179` | `1.000` | `0.920` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `1000.69` | `0.980` | `0.649` | `+0.331` | `1.000` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `build-03` | `summary` | `build` | `4723.91` | `0.896` | `0.591` | `+0.305` | `1.000` | `0.878` | `1.000` | `0.925` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `1522.04` | `0.945` | `0.000` | `+0.945` | `1.000` | `0.862` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `935.51` | `0.980` | `0.611` | `+0.370` | `1.000` | `0.951` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `1433.76` | `0.952` | `0.632` | `+0.320` | `1.000` | `0.880` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `1878.32` | `0.534` | `0.387` | `+0.147` | `0.000` | `0.894` | `1.000` | `0.880` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | ERESOLVE, unable to resolve dependency tree | - |
| `rust-02` | `summary` | `rust` | `6117.51` | `0.527` | `0.383` | `+0.144` | `0.000` | `0.856` | `1.000` | `0.891` | `0.000` | `0.000` | `soft_accepted` | `soft_accepted` | missing_exact_anchors | Finished dev | - |
| `linting-01` | `instruction_following` | `linting` | `5947.58` | `0.422` | `0.000` | `+0.422` | `0.636` | `0.623` | `0.500` | `0.465` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | index.js | - |
| `testing-06` | `instruction_following` | `testing` | `3911.23` | `0.092` | `0.000` | `+0.092` | `0.500` | `0.240` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | ERROR: | - |
| `ci-05` | `instruction_following` | `ci` | `26690.01` | `0.620` | `0.000` | `+0.620` | `0.286` | `0.797` | `1.000` | `0.800` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | ERROR: failed to fetch | - |
| `linting-02` | `structured` | `linting` | `9360.44` | `0.098` | `0.000` | `+0.098` | `0.667` | `0.182` | `0.000` | `0.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | found 1 | - |
| `kubernetes-06` | `structured` | `kubernetes` | `12407.53` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.462` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='| kind | metadata | spec | |------|----------|------| | Service | Service | Service | | name | my-service | name | | namespace | default | namespace | | clus...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='{"kind":"Service","metadata":{"name":"my-service","namespace":"default"},"spec":{"clusterIP":"10.0.0.1","ports":[{"port":80,"protocol":"TCP"}]}}' |
| `deployment-02` | `structured` | `deployment` | `1071.67` | `0.148` | `0.000` | `+0.148` | `1.000` | `0.233` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `network-01` | `exact_format` | `network` | `3714.20` | `0.624` | `0.000` | `+0.624` | `1.000` | `0.332` | `0.675` | `0.574` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `2328.47` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response' |
| `shell-03` | `exact_format` | `shell` | `1711.47` | `0.715` | `0.000` | `+0.715` | `1.000` | `0.667` | `0.635` | `0.540` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `969.83` | `0.191` | `0.000` | `+0.191` | `1.000` | `0.320` | `0.150` | `0.150` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `build-04` | `exact_format` | `build` | `7465.97` | `0.303` | `0.000` | `+0.303` | `0.286` | `0.600` | `0.473` | `0.473` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | Resources: 1 added | - |
| `build-05` | `exact_format` | `build` | `996.63` | `0.730` | `0.000` | `+0.730` | `1.000` | `0.333` | `0.750` | `0.750` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `1221.21` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `2853.20` | `0.878` | `0.582` | `+0.296` | `1.000` | `0.885` | `1.000` | `0.895` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `849.27` | `0.937` | `0.619` | `+0.318` | `1.000` | `0.843` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `2468.91` | `0.967` | `0.644` | `+0.323` | `1.000` | `0.916` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `854.99` | `0.960` | `0.000` | `+0.960` | `1.000` | `0.900` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `ci-06` | `explanation` | `ci` | `1782.45` | `0.650` | `0.000` | `+0.650` | `0.333` | `0.829` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | SIGSEGV | - |
| `runtime-06` | `explanation` | `runtime` | `659.96` | `0.945` | `0.000` | `+0.945` | `1.000` | `0.863` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `1117.84` | `0.577` | `0.000` | `+0.577` | `0.000` | `0.823` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | password authentication failed | - |
| `explanation-01` | `explanation` | `explanation` | `841.54` | `0.944` | `0.000` | `+0.944` | `1.000` | `0.861` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `1845.16` | `0.930` | `0.000` | `+0.930` | `1.000` | `0.825` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `823.72` | `0.960` | `0.638` | `+0.322` | `1.000` | `0.901` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `1287.94` | `0.950` | `0.629` | `+0.321` | `1.000` | `0.875` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `1639.09` | `0.958` | `0.000` | `+0.958` | `1.000` | `0.894` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `928.26` | `0.923` | `0.608` | `+0.314` | `1.000` | `0.807` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `2411.22` | `0.963` | `0.637` | `+0.326` | `1.000` | `0.908` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `489.29` | `0.936` | `0.000` | `+0.936` | `1.000` | `0.841` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `1441.25` | `0.948` | `0.627` | `+0.321` | `1.000` | `0.870` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `852.70` | `0.959` | `0.000` | `+0.959` | `1.000` | `0.897` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `507.33` | `0.933` | `0.000` | `+0.933` | `1.000` | `0.833` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `501.03` | `0.900` | `0.000` | `+0.900` | `1.000` | `0.751` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `ci-07` | `structured` | `ci` | `12073.16` | `0.000` | `0.000` | `+0.000` | `1.000` | `0.462` | `0.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | structured_contract_breakage | - | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['structured_contract_breakage'] first_pass='| kind | metadata | spec | |------|----------|------| | Service | Service | Service | | name | my-service | name | | namespace | default | namespace | | clus...' repair_status=rejected repair_flags=['structured_contract_breakage'] repair_pass='{"kind":"Service","metadata":{"name":"my-service","namespace":"default"},"spec":{"clusterIP":"10.0.0.1","ports":[{"port":80,"protocol":"TCP"}]}}' |
| `linting-03` | `structured` | `linting` | `1027.11` | `0.148` | `0.000` | `+0.148` | `1.000` | `0.233` | `0.000` | `0.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `network-02` | `exact_format` | `network` | `3403.87` | `0.624` | `0.000` | `+0.624` | `1.000` | `0.332` | `0.675` | `0.574` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `2296.13` | `0.000` | `0.000` | `+0.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `0.000` | `rejected` | `rejected` | exact_format_contract_breakage | - | smollm2 output validation failed. first_pass_status=rejected first_pass_flags=['exact_format_contract_breakage'] first_pass='ERROR: Timeout while waiting for response' repair_status=rejected repair_flags=['exact_format_contract_breakage'] repair_pass='ERROR: Timeout while waiting for response' |
| `shell-07` | `exact_format` | `shell` | `807.11` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `build-06` | `exact_format` | `build` | `7323.35` | `0.303` | `0.000` | `+0.303` | `0.286` | `0.600` | `0.473` | `0.473` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | Resources: 1 added | - |
| `runtime-07` | `exact_format` | `runtime` | `1260.82` | `1.000` | `0.000` | `+1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `build-07` | `exact_format` | `build` | `2926.60` | `0.574` | `0.000` | `+0.574` | `1.000` | `0.850` | `0.560` | `0.504` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `1906.83` | `0.446` | `0.000` | `+0.446` | `1.000` | `0.646` | `0.467` | `0.373` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `2696.00` | `0.878` | `0.582` | `+0.296` | `1.000` | `0.885` | `1.000` | `0.895` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `730.73` | `0.937` | `0.619` | `+0.318` | `1.000` | `0.843` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `893.78` | `0.972` | `0.642` | `+0.330` | `1.000` | `0.931` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `3772.04` | `0.935` | `0.000` | `+0.935` | `1.000` | `0.838` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `1123.70` | `0.577` | `0.000` | `+0.577` | `0.000` | `0.823` | `1.000` | `1.000` | `0.000` | `0.000` | `soft_accepted` | `rejected` | missing_exact_anchors | password authentication failed | - |
| `explanation-15` | `explanation` | `explanation` | `945.92` | `0.968` | `0.000` | `+0.968` | `1.000` | `0.921` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `2107.94` | `0.930` | `0.000` | `+0.930` | `1.000` | `0.825` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `913.19` | `0.969` | `0.000` | `+0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `rejected` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `3709.12` | `0.951` | `0.633` | `+0.318` | `1.000` | `0.878` | `1.000` | `1.000` | `0.000` | `0.000` | `accepted` | `soft_accepted` | - | - | - |
