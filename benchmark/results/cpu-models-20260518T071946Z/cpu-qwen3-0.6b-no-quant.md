# cpu-qwen3-0.6b-no-quant

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

- load_ms: `26597.49`
- cpu_rss_bytes: `null`
- gpu_peak_bytes: `null`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `268`
- accepted_count: `225`
- soft_accepted_count: `43`
- rejected_count: `12`
- exact_pass_count: `235`
- avg_inference_ms: `19741.62`
- p95_inference_ms: `41018.24`
- avg_exact_preservation_ratio: `0.922`
- avg_summary_quality_ratio: `0.808`
- avg_format_adherence_score: `0.757`
- avg_instruction_following_score: `0.735`
- avg_brevity_ratio: `0.849`
- avg_case_score: `0.781`
- p10_case_score: `0.276`
- quality_core: `0.680`
- latency_factor: `0.850`
- final_score: `57.77`
- peak_cpu_rss_bytes: `null`
- peak_gpu_bytes: `null`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `36239.79` | `0.689` | `1.000` | `0.899` | `0.500` | `0.404` | `0.358` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-02` | `summary` | `python` | `21315.38` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass="worker boot failed. I need to make sure I don't add any extra information. The actionable failure here is the ModuleNotFoundError because the script can't fi..." repair_status=rejected repair_flags=['control_token_leakage'] repair_pass="<think> Okay, let's see. The user mentioned that their previous answer was invalid for recall-oriented compression. The previous answer included some lines b..." |
| `python-03` | `recall` | `python` | `40784.63` | `0.686` | `1.000` | `0.905` | `0.500` | `0.397` | `0.311` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-04` | `recall` | `python` | `47723.45` | `0.678` | `0.583` | `0.940` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /workspace/src/jobs/refresh_catalog.py, line 119 | - |
| `python-05` | `recall` | `python` | `34352.61` | `0.712` | `1.000` | `0.954` | `0.500` | `0.423` | `0.489` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `pytest-01` | `recall` | `pytest` | `26129.84` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `12399.48` | `0.985` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `32258.91` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | pytest tests -q -x, tests/jobs/test_retention.py::test_archive_marks_job_deleted, teardown, psycopg.errors.ForeignKeyViolation, job_runs_job_id_fkey, 149 passed, 1 skipped, 1 error in 58.73s | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass="149 passed, 1 skipped, 1 error in 58.73s I need to check if all the required elements are included and that there are no extra parts. The user's instruction ..." repair_status=rejected repair_flags=['control_token_leakage'] repair_pass="<think> Okay, let's see. The user mentioned that their previous answer was invalid for recall-oriented compression. They provided a previous answer with some..." |
| `pytest-04` | `recall` | `pytest` | `12668.18` | `0.993` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `39767.36` | `0.671` | `1.000` | `0.928` | `0.500` | `0.418` | `0.455` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `mypy-01` | `recall` | `mypy` | `9163.65` | `0.991` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `10703.83` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `36753.88` | `0.887` | `1.000` | `0.902` | `1.000` | `0.733` | `0.111` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `15964.42` | `0.954` | `0.911` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | all | - |
| `ruff-02` | `summary` | `ruff` | `17965.40` | `0.990` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `8627.12` | `0.971` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `13406.46` | `0.986` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `23166.46` | `0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `12116.51` | `0.966` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `26202.63` | `0.794` | `0.800` | `0.961` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 2 files would be reformatted, 41 files would be left unchanged | - |
| `black-02` | `summary` | `black` | `24958.30` | `0.971` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `8416.58` | `0.992` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `12436.36` | `0.947` | `1.000` | `0.919` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `18630.29` | `0.874` | `1.000` | `0.918` | `1.000` | `0.814` | `0.380` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `10455.22` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `12767.39` | `0.944` | `1.000` | `0.926` | `1.000` | `0.887` | `0.622` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `14165.92` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `21823.48` | `0.874` | `1.000` | `0.891` | `1.000` | `0.835` | `0.449` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `11705.86` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `26898.38` | `0.940` | `1.000` | `0.931` | `1.000` | `0.871` | `0.569` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `42195.60` | `0.699` | `1.000` | `0.953` | `0.500` | `0.440` | `0.603` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `eslint-01` | `recall` | `eslint` | `33904.78` | `0.983` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `10507.68` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `39428.89` | `0.760` | `0.808` | `0.923` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | maximum: 0 | - |
| `docker-01` | `recall` | `docker` | `27671.53` | `0.986` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `9997.72` | `0.984` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `29612.63` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `9273.77` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `22238.84` | `0.900` | `1.000` | `0.915` | `1.000` | `0.765` | `0.216` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `12773.92` | `0.968` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `12803.99` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `47959.68` | `0.854` | `1.000` | `0.797` | `1.000` | `0.714` | `0.047` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `8410.78` | `0.987` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `18398.33` | `0.927` | `1.000` | `0.924` | `1.000` | `0.839` | `0.464` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `10326.83` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `16451.67` | `0.981` | `1.000` | `0.938` | `1.000` | `0.989` | `0.964` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `11973.55` | `0.990` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `22803.17` | `0.816` | `0.902` | `0.960` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | expected t3.small default | - |
| `mixed-01` | `recall` | `mixed` | `10396.41` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `12403.66` | `0.963` | `1.000` | `0.908` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `14316.20` | `0.979` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `15860.66` | `0.983` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `13666.05` | `0.972` | `1.000` | `0.952` | `1.000` | `0.951` | `0.838` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `19908.73` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `30848.37` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | curl -I https://docs.example.com/sdk/latest, HTTP/2 301, location: /sdk/v3.4/, cache-control: max-age=3600 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='curl -I https://docs.example.com/sdk/latest. The redirect is to /sdk/v3.4/ with a 301 status code. The headers include the HTTP/2 status, date, content type,...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass="<think> Okay, let's see. The user mentioned that their previous answer was invalid for recall-oriented compression. The previous answer was a curl command wi..." |
| `ssh-01` | `summary` | `ssh` | `9181.22` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `10788.09` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `17714.60` | `0.913` | `1.000` | `0.911` | `1.000` | `0.897` | `0.655` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `37621.80` | `0.786` | `0.857` | `0.901` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | api.service | - |
| `apt-01` | `summary` | `apt` | `24730.56` | `0.977` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `30851.41` | `0.868` | `1.000` | `0.847` | `1.000` | `0.720` | `0.067` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `23385.44` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `44069.74` | `0.810` | `1.000` | `0.858` | `1.000` | `0.733` | `0.110` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `25247.66` | `0.978` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `28558.91` | `0.672` | `0.304` | `0.912` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | mvn -q test, UserControllerTest.java:72, maven-surefire-plugin:3.5.5:test | - |
| `maven-02` | `summary` | `maven` | `27671.45` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `14698.47` | `0.918` | `1.000` | `0.940` | `1.000` | `0.800` | `0.333` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `14181.61` | `0.977` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `12541.93` | `0.976` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `12207.46` | `0.975` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `31646.65` | `0.754` | `0.789` | `0.929` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | MODULE_NOT_FOUND | - |
| `npm-04` | `summary` | `npm` | `47542.17` | `0.857` | `1.000` | `0.918` | `1.000` | `0.779` | `0.264` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `14548.12` | `0.973` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `32489.25` | `0.760` | `0.727` | `0.905` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ESLint found too many warnings | - |
| `python-runtime-01` | `summary` | `python-runtime` | `27679.75` | `0.693` | `1.000` | `0.947` | `0.500` | `0.437` | `0.577` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `pytest-06` | `summary` | `pytest` | `28080.52` | `0.889` | `1.000` | `0.913` | `1.000` | `0.847` | `0.491` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `20435.16` | `0.882` | `1.000` | `0.919` | `1.000` | `0.828` | `0.427` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `29237.64` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `17838.33` | `0.879` | `1.000` | `0.907` | `1.000` | `0.833` | `0.443` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `12720.00` | `0.975` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `24113.77` | `0.823` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `11462.89` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `12354.16` | `0.993` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `9793.29` | `0.962` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `26952.41` | `0.981` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `11095.52` | `0.979` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `11839.64` | `0.974` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `16088.94` | `0.992` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `15235.13` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `11732.95` | `0.983` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `14334.46` | `0.986` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `14628.69` | `0.949` | `1.000` | `0.948` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `17878.29` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `44185.15` | `0.614` | `0.524` | `0.846` | `1.000` | `0.927` | `0.757` | `soft_accepted` | missing_exact_anchors | ruff check ., line=91, exit code 2 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `23990.56` | `0.898` | `1.000` | `0.907` | `1.000` | `0.871` | `0.571` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `12872.15` | `0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `19958.40` | `0.923` | `1.000` | `0.925` | `1.000` | `0.906` | `0.686` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `10485.35` | `0.984` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `8630.69` | `0.990` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `30680.64` | `0.784` | `0.833` | `0.909` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | runtime-1a2b3c.js | - |
| `test-failure-01` | `recall` | `test-failure` | `37507.47` | `0.957` | `1.000` | `0.950` | `1.000` | `0.909` | `0.698` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `39977.36` | `0.774` | `0.851` | `0.910` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/router.rs:137:42 | - |
| `ci-log-01` | `recall` | `ci-log` | `17482.28` | `0.986` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `21495.17` | `0.927` | `1.000` | `0.959` | `1.000` | `0.811` | `0.370` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `37813.27` | `0.787` | `0.821` | `0.927` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | worker.go:144 | - |
| `build-log-01` | `summary` | `build-log` | `34048.89` | `0.970` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `34288.74` | `0.974` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `46334.09` | `0.423` | `1.000` | `0.692` | `0.000` | `0.000` | `0.157` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `30316.68` | `0.720` | `1.000` | `0.734` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `28050.94` | `0.391` | `1.000` | `0.621` | `0.000` | `0.000` | `0.050` | `accepted` | - | - | - |
| `structured-output-01` | `structured` | `structured-output` | `40561.57` | `0.550` | `1.000` | `0.834` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `33403.93` | `0.355` | `1.000` | `0.183` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-03` | `structured` | `structured-output` | `29491.14` | `0.278` | `0.786` | `0.235` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | createSession › rejects expired refresh token, "refresh token expired", calculateTax › uses EU VAT for DE customer | - |
| `structured-output-04` | `structured` | `structured-output` | `43427.37` | `0.220` | `1.000` | `0.197` | `0.000` | `0.000` | `0.002` | `soft_accepted` | structured_output_mismatch | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `14467.16` | `0.187` | `1.000` | `0.334` | `0.000` | `0.000` | `0.062` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `33964.96` | `0.121` | `0.714` | `0.319` | `0.000` | `0.000` | `0.075` | `soft_accepted` | missing_exact_anchors | SearchBox debounces network query before fetch | - |
| `exact-format-03` | `exact_format` | `exact-format` | `29515.26` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `21804.50` | `0.685` | `0.778` | `0.900` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `22912.25` | `0.767` | `0.750` | `0.906` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `35008.84` | `0.743` | `1.000` | `0.885` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `33996.30` | `0.654` | `0.524` | `0.934` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /srv/app/app/tasks/email.py, line 92 | - |
| `mypy-05` | `recall` | `mypy` | `16223.01` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `15445.21` | `0.979` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `31514.58` | `0.665` | `0.783` | `0.921` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | OrderServiceTest > calculatesDiscountForGoldCustomer() PASSED | - |
| `kubernetes-01` | `recall` | `kubernetes` | `16120.86` | `0.968` | `1.000` | `0.922` | `1.000` | `0.963` | `0.878` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `14925.50` | `0.978` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `17833.42` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-05` | `recall` | `docker-compose` | `11786.36` | `0.980` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `16707.35` | `0.984` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `14521.28` | `0.982` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `41184.40` | `0.979` | `1.000` | `0.939` | `1.000` | `0.984` | `0.946` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `12584.62` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `38972.88` | `0.713` | `0.696` | `0.901` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | test/my_app/cache_worker_test.exs:29, refreshes expired keys | - |
| `rails-01` | `recall` | `rails` | `41144.03` | `0.749` | `0.765` | `0.948` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ArgumentError | - |
| `phpunit-01` | `recall` | `phpunit` | `16206.50` | `0.956` | `1.000` | `0.925` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `15774.81` | `0.979` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `14639.25` | `0.982` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `22317.81` | `0.639` | `0.500` | `0.907` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | UNREACHABLE, 10.0.4.22 port 22, Connection timed out | - |
| `bazel-01` | `recall` | `bazel` | `15452.86` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `26974.40` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `31451.62` | `0.960` | `1.000` | `0.931` | `1.000` | `0.932` | `0.775` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `13667.09` | `0.963` | `1.000` | `0.907` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `8579.74` | `0.960` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `12743.42` | `0.970` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `19418.23` | `0.932` | `0.875` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | template | - |
| `ruff-04` | `summary` | `ruff` | `15848.34` | `0.960` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `34443.69` | `0.943` | `1.000` | `0.858` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `13875.42` | `0.951` | `1.000` | `0.941` | `1.000` | `0.949` | `0.830` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `18354.71` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | xcodebuild, -scheme, MobileApp, -configuration, Release | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them **Summary:** The command...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them **Summary:** The command...' |
| `make-02` | `summary` | `make` | `23647.12` | `0.742` | `1.000` | `0.933` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `29908.36` | `0.969` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `16067.88` | `0.956` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `19209.06` | `0.962` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `23492.12` | `0.970` | `1.000` | `0.924` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `26295.95` | `0.775` | `1.000` | `0.780` | `1.000` | `0.726` | `0.086` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `11376.36` | `0.964` | `1.000` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `25945.67` | `0.366` | `1.000` | `0.673` | `0.000` | `0.000` | `0.286` | `soft_accepted` | structured_output_mismatch | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `15107.76` | `0.962` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `10257.67` | `0.429` | `1.000` | `0.709` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `13112.72` | `0.656` | `1.000` | `0.705` | `0.500` | `0.417` | `0.444` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `27947.79` | `0.446` | `1.000` | `0.685` | `0.000` | `0.000` | `0.407` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `13389.35` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `19207.06` | `0.549` | `1.000` | `0.831` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `30936.99` | `0.327` | `0.667` | `0.646` | `0.000` | `0.000` | `0.579` | `soft_accepted` | missing_exact_anchors | identifier = "prod-main" | - |
| `maven-03` | `instruction_following` | `maven` | `26924.74` | `0.697` | `1.000` | `0.880` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `15241.70` | `0.526` | `1.000` | `0.754` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `9307.73` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `25504.00` | `0.453` | `1.000` | `0.782` | `0.000` | `0.000` | `0.182` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `25802.60` | `0.427` | `0.833` | `0.810` | `0.000` | `0.000` | `0.933` | `soft_accepted` | missing_exact_anchors | src/auth.rs:88 | - |
| `shell-01` | `instruction_following` | `shell` | `33019.36` | `0.452` | `1.000` | `0.742` | `0.000` | `0.000` | `0.300` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `50034.22` | `0.355` | `0.733` | `0.698` | `0.000` | `0.000` | `0.615` | `soft_accepted` | missing_exact_anchors | file, code | - |
| `terraform-10` | `structured` | `terraform` | `27568.94` | `0.434` | `1.000` | `0.569` | `0.000` | `0.000` | `0.636` | `accepted` | - | - | - |
| `junit-01` | `structured` | `junit` | `28845.63` | `0.539` | `0.857` | `0.937` | `0.000` | `0.000` | `0.867` | `accepted` | - | Test | - |
| `kubernetes-03` | `structured` | `kubernetes` | `63138.75` | `0.151` | `0.571` | `0.209` | `0.000` | `0.000` | `0.008` | `soft_accepted` | missing_exact_anchors | name, status, restarts | - |
| `eslint-06` | `structured` | `eslint` | `44431.89` | `0.325` | `1.000` | `0.232` | `0.000` | `0.000` | `0.556` | `accepted` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `15527.49` | `0.434` | `1.000` | `0.567` | `0.000` | `0.000` | `0.636` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `10702.07` | `0.499` | `1.000` | `0.779` | `0.000` | `0.000` | `0.647` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `25905.42` | `0.276` | `0.667` | `0.548` | `0.000` | `0.000` | `0.273` | `soft_accepted` | missing_exact_anchors | Job, Step | - |
| `npm-07` | `structured` | `npm` | `15592.39` | `0.370` | `1.000` | `0.234` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `39350.11` | `0.243` | `0.333` | `0.594` | `0.000` | `0.000` | `0.409` | `soft_accepted` | missing_exact_anchors | File, Line, Code, Message, --- | - |
| `gradle-03` | `structured` | `gradle` | `35644.35` | `0.312` | `0.697` | `0.425` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | :api:compileJava | - |
| `playwright-02` | `structured` | `playwright` | `14712.48` | `0.531` | `1.000` | `0.769` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `14814.24` | `0.358` | `1.000` | `0.192` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `vite-01` | `structured` | `vite` | `14364.83` | `0.269` | `1.000` | `0.214` | `0.000` | `0.000` | `0.045` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `38346.99` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | tests/test_a.py::test_one, tests/test_b.py::TestB::test_three | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='FAILED tests/test_a.py::test_one - AssertionError PASSED tests/test_a.py::test_two FAILED tests/test_b.py::TestB::test_three - TimeoutError So each failing t...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass="<think> Okay, let's see. The user mentioned that their previous answer was invalid for recall-oriented compression. They provided a test failure message with..." |
| `git-04` | `exact_format` | `git` | `35081.48` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `27837.11` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass="<think> Okay, let's see. The user wants me to output exactly the requested value or lines. The instruction mentions preserving exact filenames, symbols, erro..." repair_status=rejected repair_flags=['control_token_leakage'] repair_pass="<think> Okay, let's see. The user provided an invalid compression summary and mentioned that the previous answer was invalid for recall-oriented compression...." |
| `npm-08` | `exact_format` | `npm` | `23603.33` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 2.18.4 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='2.18.4 npm notice New major version of npm available So, the exact output they want is the lines between the two commands. The first line is the command, the...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='$ npm view @acme/sdk version. The second line is the output line: 2.18.4. The user wants only that span. They also specified not to add extra structure or ex...' |
| `go-test-05` | `exact_format` | `go-test` | `27199.14` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | github.com/acme/shop/checkout, TestCheckoutAppliesCoupon | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass="<think> Okay, let's see. The user wants me to output exactly the requested value or lines from the given test. The test is TestCheckoutAppliesCoupon, and the..." repair_status=rejected repair_flags=['control_token_leakage'] repair_pass="<think> Okay, let's see. The user provided a test case where the expected value is 100 but the actual is 120. The task is to output the span from line 77 to ..." |
| `kubectl-09` | `exact_format` | `kubectl` | `32369.82` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | migrator-v2-9xk, prod | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='migrator-v2-9xk" and "prod" as the exact names. The output shows that the migrator is in the prod namespace. The command is "migrator-v2-9xk" and the status ...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass='migrator-v2-9xk 0/1 Error 0 33m". The user wants to preserve the exact tokens, so I need to make sure that the output only includes that exact line. The othe...' |
| `cargo-05` | `exact_format` | `cargo` | `23498.22` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | auth::tests::rejects_expired, billing::tests::rounds_half_even | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass='<think> Okay, let\'s see. The user wants me to output exactly the requested value or lines based on the given instruction. The instruction mentions "auth::tes...' repair_status=rejected repair_flags=['control_token_leakage'] repair_pass="<think> Okay, let's see. The user provided a previous answer that was invalid for recall-oriented compression. The previous answer included the test names an..." |
| `curl-03` | `exact_format` | `curl` | `25220.21` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 503 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass="<think> Okay, let's see. The user wants me to output exactly the requested value or lines. The instruction says to preserve exact filenames, symbols, error c..." repair_status=rejected repair_flags=['control_token_leakage'] repair_pass="<think> Okay, let's see. The user provided an example output and mentioned that the previous answer was invalid for recall-oriented compression. The example ..." |
| `rails-02` | `exact_format` | `rails` | `54944.06` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | control_token_leakage | 20260518133742 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['control_token_leakage'] first_pass="<think> Okay, let's see. The user wants me to output exactly the requested value or lines. The instruction says to preserve the exact filename, symbols, erro..." repair_status=rejected repair_flags=['control_token_leakage'] repair_pass="<think> Okay, let's see. The user provided a previous answer that was invalid for recall-oriented compression. Now they want me to output the command and the..." |
| `python-traceback-02` | `explanation` | `python-traceback` | `16107.34` | `0.943` | `1.000` | `0.885` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `26592.81` | `0.945` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `14335.55` | `0.931` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `21616.84` | `0.960` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `10721.66` | `0.944` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `32527.10` | `0.685` | `1.000` | `0.812` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `20881.73` | `0.620` | `0.167` | `0.791` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | contents: read, contents: write | - |
| `runtime-01` | `recall` | `runtime` | `15092.59` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `23076.68` | `0.985` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `16239.86` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `10509.25` | `0.975` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `17125.53` | `0.714` | `0.667` | `0.959` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `14830.01` | `0.954` | `1.000` | `0.948` | `1.000` | `0.900` | `0.667` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `39514.35` | `0.964` | `1.000` | `0.924` | `1.000` | `0.950` | `0.833` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `11513.46` | `0.966` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `13754.99` | `0.961` | `1.000` | `0.842` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `13623.27` | `0.976` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `9895.27` | `0.982` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `15431.61` | `0.958` | `1.000` | `0.938` | `1.000` | `0.920` | `0.733` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `9570.01` | `0.975` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `24841.31` | `0.981` | `1.000` | `0.922` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `25668.74` | `0.843` | `1.000` | `0.761` | `1.000` | `0.709` | `0.029` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `11938.46` | `0.985` | `1.000` | `0.938` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `11615.03` | `0.967` | `1.000` | `0.867` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `13077.21` | `0.967` | `1.000` | `0.866` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `12109.89` | `0.972` | `1.000` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `11557.97` | `0.958` | `1.000` | `0.832` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `27357.55` | `0.984` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `26933.75` | `0.976` | `1.000` | `0.902` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `44834.54` | `0.833` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `7131.74` | `0.974` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `21053.06` | `0.957` | `1.000` | `0.892` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `13456.44` | `0.882` | `1.000` | `0.875` | `1.000` | `0.864` | `0.545` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `7074.49` | `0.961` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `8884.54` | `0.954` | `1.000` | `0.884` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `18655.40` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `22171.46` | `0.900` | `1.000` | `0.833` | `1.000` | `0.933` | `0.778` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `32321.95` | `0.464` | `1.000` | `0.734` | `0.000` | `0.000` | `0.435` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `22713.29` | `0.922` | `1.000` | `0.738` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `18586.44` | `0.644` | `1.000` | `0.775` | `0.500` | `0.367` | `0.111` | `accepted` | - | - | - |
| `linting-02` | `structured` | `linting` | `10047.83` | `0.468` | `1.000` | `0.560` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `6120.93` | `0.359` | `1.000` | `0.196` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `22682.84` | `0.422` | `1.000` | `0.518` | `0.000` | `0.000` | `0.667` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `11881.96` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `10605.91` | `0.231` | `1.000` | `0.648` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `21377.38` | `0.502` | `1.000` | `0.856` | `0.333` | `0.300` | `0.667` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `8714.74` | `0.207` | `1.000` | `0.491` | `0.000` | `0.000` | `0.167` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `22273.87` | `0.249` | `1.000` | `0.492` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `build-05` | `exact_format` | `build` | `14403.97` | `0.225` | `1.000` | `0.609` | `0.000` | `0.000` | `0.286` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `7509.12` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `6463.90` | `0.935` | `1.000` | `0.870` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `4412.58` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `7620.32` | `0.959` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `9494.97` | `0.943` | `1.000` | `0.885` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `9127.20` | `0.903` | `1.000` | `0.877` | `1.000` | `0.894` | `0.647` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `4307.80` | `0.932` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `7041.37` | `0.954` | `1.000` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `12585.00` | `0.930` | `1.000` | `0.860` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `6199.30` | `0.944` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `4076.68` | `0.950` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `6351.36` | `0.867` | `1.000` | `0.734` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `5127.18` | `0.947` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `6382.20` | `0.901` | `1.000` | `0.802` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `5227.88` | `0.932` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `21803.78` | `0.920` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `5981.83` | `0.950` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `4078.23` | `0.948` | `1.000` | `0.896` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `5365.28` | `0.916` | `1.000` | `0.832` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `4902.71` | `0.933` | `1.000` | `0.866` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `5743.05` | `0.359` | `1.000` | `0.196` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `21834.91` | `0.422` | `1.000` | `0.518` | `0.000` | `0.000` | `0.667` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `11360.63` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `8504.41` | `0.231` | `1.000` | `0.648` | `0.000` | `0.000` | `0.333` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `13184.30` | `0.700` | `1.000` | `0.335` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `20947.92` | `0.249` | `1.000` | `0.492` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `10043.54` | `0.207` | `1.000` | `0.319` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `21821.99` | `0.242` | `1.000` | `0.851` | `0.000` | `0.000` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `shell-08` | `exact_format` | `shell` | `13192.54` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `6645.80` | `0.935` | `1.000` | `0.870` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `4199.75` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `5367.27` | `0.960` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `12094.71` | `0.918` | `1.000` | `0.836` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `7508.44` | `0.954` | `1.000` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `5455.75` | `0.963` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `7737.84` | `0.913` | `1.000` | `0.826` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `5237.40` | `0.928` | `1.000` | `0.856` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `5461.40` | `0.939` | `1.000` | `0.878` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
