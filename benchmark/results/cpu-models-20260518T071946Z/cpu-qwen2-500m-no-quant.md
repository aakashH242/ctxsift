# cpu-qwen2-500m-no-quant

## Scenario

- track: `cpu`
- phase: `cpu-screen`
- model: `lmstudio-community/Qwen2-500M-Instruct-GGUF`
- quantization: `none`
- device: `cpu`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `3004.40`
- cpu_rss_bytes: `null`
- gpu_peak_bytes: `null`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `256`
- accepted_count: `149`
- soft_accepted_count: `107`
- rejected_count: `24`
- exact_pass_count: `158`
- avg_inference_ms: `7810.18`
- p95_inference_ms: `24439.18`
- avg_exact_preservation_ratio: `0.693`
- avg_summary_quality_ratio: `0.732`
- avg_format_adherence_score: `0.675`
- avg_instruction_following_score: `0.648`
- avg_brevity_ratio: `0.796`
- avg_case_score: `0.634`
- p10_case_score: `0.028`
- quality_core: `0.513`
- latency_factor: `0.850`
- final_score: `43.60`
- peak_cpu_rss_bytes: `null`
- peak_gpu_bytes: `null`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `36369.13` | `0.682` | `0.633` | `0.871` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | python -m app.cli sync --config config/settings.json, config/settings.json | - |
| `python-02` | `summary` | `python` | `3935.43` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | python services/worker.py --queue emails --concurrency 4, /workspace/services/worker.py, line 11, ModuleNotFoundError, dramatiq_abort, worker boot failed | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='- return the exact requested lines or quoted excerpts only - copy quoted or extracted lines exactly from the raw output - do not summarize unless the instruc...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='- return the exact requested lines or quoted excerpts only - copy quoted or extracted lines exactly from the raw output - do not summarize unless the instruc...' |
| `python-03` | `recall` | `python` | `32138.60` | `0.600` | `0.782` | `0.894` | `0.500` | `0.397` | `0.311` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | ./scripts/run-local-api.sh | - |
| `python-04` | `recall` | `python` | `4786.27` | `0.408` | `0.000` | `0.721` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | python -m jobs.refresh_catalog --region us-east-1, /workspace/src/jobs/refresh_catalog.py, line 119, httpx.ReadTimeout, catalog?page=2, us-east-1 | - |
| `python-05` | `recall` | `python` | `4799.75` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `13914.54` | `0.928` | `1.000` | `0.932` | `1.000` | `0.833` | `0.444` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `19597.47` | `0.784` | `0.907` | `0.926` | `1.000` | `0.951` | `0.837` | `soft_accepted` | missing_exact_anchors | signed_payload | - |
| `pytest-03` | `recall` | `pytest` | `5854.18` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | pytest tests -q -x, tests/jobs/test_retention.py::test_archive_marks_job_deleted, teardown, psycopg.errors.ForeignKeyViolation, job_runs_job_id_fkey, 149 passed, 1 skipped, 1 error in 58.73s | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='- return the exact requested lines or quoted excerpts only - copy quoted or extracted lines exactly from the raw output - do not summarize unless the instruc...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='- return the exact requested lines or quoted excerpts only - copy quoted or extracted lines exactly from the raw output - do not summarize unless the instruc...' |
| `pytest-04` | `recall` | `pytest` | `11493.86` | `0.624` | `0.575` | `0.935` | `1.000` | `0.825` | `0.417` | `soft_accepted` | missing_exact_anchors | /workspace/tests/cli/test_export.py:12, PytestUnknownMarkWarning | - |
| `pytest-05` | `summary` | `pytest` | `5448.82` | `0.636` | `0.235` | `0.847` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/unit tests/integration --disable-warnings=0, tests/unit/test_stripe_client.py, src/billing/client.py:9, 1 error during collection | - |
| `mypy-01` | `recall` | `mypy` | `5591.07` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `15679.20` | `0.911` | `1.000` | `0.950` | `1.000` | `0.862` | `0.538` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `4073.17` | `0.993` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `11553.86` | `0.719` | `0.644` | `0.900` | `1.000` | `0.950` | `0.833` | `soft_accepted` | missing_exact_anchors | ruff check src --output-format=full, all | - |
| `ruff-02` | `summary` | `ruff` | `2021.60` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `4227.97` | `0.753` | `0.707` | `0.898` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ruff check src/auth/login.py | - |
| `pylint-01` | `recall` | `pylint` | `3323.70` | `0.985` | `1.000` | `0.939` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `19224.12` | `0.969` | `1.000` | `0.901` | `1.000` | `0.981` | `0.935` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `9786.13` | `0.968` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `2939.00` | `0.989` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `3554.27` | `0.703` | `0.511` | `0.873` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | black src, 1 file failed to reformat, 1 file reformatted | - |
| `black-03` | `recall` | `black` | `6360.67` | `0.988` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `12748.08` | `0.941` | `1.000` | `0.927` | `1.000` | `0.877` | `0.590` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `6721.53` | `0.873` | `1.000` | `0.918` | `1.000` | `0.811` | `0.368` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `4995.89` | `0.638` | `0.182` | `0.899` | `1.000` | `0.992` | `0.973` | `soft_accepted` | missing_exact_anchors | npm run build, ./CheckoutButton, Lifecycle script `build` failed, storefront@2.8.1, /workspace | - |
| `pnpm-01` | `recall` | `pnpm` | `3301.45` | `0.939` | `1.000` | `0.926` | `1.000` | `0.871` | `0.571` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `6158.40` | `0.985` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `20634.57` | `0.676` | `0.714` | `0.889` | `1.000` | `0.822` | `0.407` | `soft_accepted` | missing_exact_anchors | pnpm -r test --stream | - |
| `typescript-01` | `summary` | `typescript` | `4613.37` | `0.983` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `6102.79` | `0.516` | `0.263` | `0.856` | `1.000` | `0.923` | `0.744` | `soft_accepted` | missing_exact_anchors | tsc -b packages/, TS2322, string | undefined, Watching for file changes | - |
| `typescript-03` | `summary` | `typescript` | `14464.82` | `0.640` | `0.769` | `0.925` | `0.500` | `0.440` | `0.603` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | tsc src/index.ts src/http.ts --pretty false | - |
| `eslint-01` | `recall` | `eslint` | `42818.52` | `0.937` | `1.000` | `0.928` | `1.000` | `0.866` | `0.553` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `4730.26` | `0.953` | `1.000` | `0.883` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `2730.96` | `0.527` | `0.231` | `0.867` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /workspace/src/hooks/useCart.ts, react-hooks/exhaustive-deps, 1 problem (0 errors, 1 warning), maximum: 0 | - |
| `docker-01` | `recall` | `docker` | `22553.56` | `0.888` | `1.000` | `0.878` | `1.000` | `0.754` | `0.180` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `4323.17` | `0.679` | `0.389` | `0.880` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker run --rm api:dev, api:dev | - |
| `docker-03` | `summary` | `docker` | `29543.81` | `0.973` | `1.000` | `0.932` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `1870.60` | `0.976` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `3925.31` | `0.408` | `0.000` | `0.721` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker compose up --build, demo-app-1, tenant_settings, sqlalchemy.exc.ProgrammingError, app-1 exited with code 1 | - |
| `docker-compose-03` | `summary` | `docker-compose` | `7882.87` | `0.732` | `0.600` | `0.902` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | docker compose up api | - |
| `kubectl-01` | `summary` | `kubectl` | `4748.15` | `0.884` | `1.000` | `0.940` | `1.000` | `0.816` | `0.388` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `19644.41` | `0.907` | `1.000` | `0.937` | `1.000` | `0.767` | `0.222` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `3866.55` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | kubectl wait --for=condition=Available deployment/worker -n jobs --timeout=90s, deployment/worker, timed out waiting for the condition, deployments/worker | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them Summarize only the key o...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them Summarize only the key o...' |
| `kubectl-04` | `recall` | `kubectl` | `4153.71` | `0.412` | `0.000` | `0.739` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | kubectl logs payments-worker-6f8f7d4df5-z5vsm -c worker --previous -n payments, payments-worker-6f8f7d4df5-z5vsm, /app/config.yaml, ValueError, invalid worker.concurrency, worker | - |
| `terraform-01` | `summary` | `terraform` | `5408.24` | `0.741` | `0.647` | `0.901` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | terraform validate | - |
| `terraform-02` | `recall` | `terraform` | `12331.59` | `0.691` | `0.684` | `0.926` | `1.000` | `0.919` | `0.730` | `soft_accepted` | missing_exact_anchors | terraform plan | - |
| `terraform-03` | `recall` | `terraform` | `2911.51` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `4386.25` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `2165.04` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `3453.41` | `0.671` | `0.405` | `0.845` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | make integration, migrations/202605121045_add_login_audit.sql | - |
| `git-01` | `recall` | `git` | `12495.18` | `0.564` | `0.600` | `0.912` | `0.500` | `0.448` | `0.656` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | git rebase origin/main | - |
| `git-02` | `recall` | `git` | `3032.35` | `0.539` | `0.259` | `0.871` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | git push origin main, main -> main, non-fast-forward | - |
| `git-03` | `recall` | `git` | `44767.95` | `0.683` | `0.625` | `0.889` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | git clone --progress https://github.com/example/very-large-repo.git | - |
| `curl-01` | `recall` | `curl` | `8841.48` | `0.913` | `1.000` | `0.942` | `1.000` | `0.782` | `0.272` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `5233.11` | `0.828` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `ssh-01` | `summary` | `ssh` | `22066.46` | `0.697` | `0.476` | `0.877` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | GIT_SSH_COMMAND="ssh -o IdentitiesOnly=yes -i ~/.ssh/deploy_key" git ls-remote git@github.com:example/mono-app.git, git@github.com:example/mono-app.git | - |
| `ssh-02` | `summary` | `ssh` | `4115.82` | `0.559` | `0.000` | `0.768` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ssh deploy@staging.example.net, /home/dev/.ssh/known_hosts:42, staging.example.net, Host key verification failed. | - |
| `systemd-01` | `summary` | `systemd` | `7296.30` | `0.793` | `0.871` | `0.913` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | queue-worker.service | - |
| `systemd-02` | `summary` | `systemd` | `10642.85` | `0.556` | `0.143` | `0.797` | `1.000` | `0.900` | `0.667` | `soft_accepted` | missing_exact_anchors | /etc/api/config.yaml, line 17, timeuot | - |
| `apt-01` | `summary` | `apt` | `3481.47` | `0.977` | `1.000` | `0.942` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `20139.59` | `0.904` | `1.000` | `0.942` | `1.000` | `0.754` | `0.181` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `5887.95` | `0.963` | `1.000` | `0.907` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `14151.22` | `0.910` | `1.000` | `0.929` | `1.000` | `0.877` | `0.590` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `10601.01` | `0.964` | `1.000` | `0.911` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `4433.72` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-02` | `summary` | `maven` | `20961.52` | `0.896` | `1.000` | `0.930` | `1.000` | `0.848` | `0.493` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `50087.41` | `0.452` | `0.238` | `0.874` | `1.000` | `0.718` | `0.061` | `soft_accepted` | missing_exact_anchors | ./gradlew :service:build --warning-mode=all, :service:compileClasspath, org.mapstruct:mapstruct:1.5.5.Final | - |
| `gradle-02` | `summary` | `gradle` | `8828.04` | `0.768` | `0.722` | `0.933` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Execution failed for task ':test' | - |
| `cargo-01` | `summary` | `cargo` | `5150.19` | `0.942` | `1.000` | `0.921` | `1.000` | `0.946` | `0.821` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `2202.86` | `0.549` | `0.000` | `0.738` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | cargo build, rand = "^0.9.0", crates.io index, guessing_game v0.1.0 | - |
| `node-runtime-01` | `recall` | `node-runtime` | `21868.39` | `0.614` | `0.737` | `0.934` | `0.500` | `0.436` | `0.575` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | node dist/server.js | - |
| `npm-04` | `summary` | `npm` | `5528.43` | `0.695` | `0.474` | `0.874` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | npm install, ERESOLVE | - |
| `tsc-01` | `summary` | `tsc` | `11278.93` | `0.917` | `1.000` | `0.898` | `1.000` | `0.914` | `0.714` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `5338.31` | `0.957` | `1.000` | `0.915` | `1.000` | `0.982` | `0.941` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `2580.22` | `0.545` | `0.000` | `0.729` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | python -m tools.sync_rules --env staging, /workspace/app/loader.py, line 52, FileNotFoundError, rules/staging.json | - |
| `pytest-06` | `summary` | `pytest` | `5651.50` | `0.548` | `0.000` | `0.735` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pytest tests/api/test_auth.py -k login -q, test_login_rate_limit_after_5_failures, tests/api/test_auth.py:88, assert 200 == 429 | - |
| `mypy-04` | `summary` | `mypy` | `5501.06` | `0.971` | `1.000` | `0.939` | `1.000` | `0.992` | `0.972` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `5252.92` | `0.976` | `1.000` | `0.941` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `8538.86` | `0.550` | `0.133` | `0.827` | `1.000` | `0.866` | `0.554` | `soft_accepted` | missing_exact_anchors | docker compose up --build, 0.0.0.0:8080, port is already allocated | - |
| `kubectl-05` | `summary` | `kubectl` | `2234.46` | `0.705` | `0.500` | `0.885` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Service "api", spec.clusterIP, field is immutable | - |
| `kubectl-06` | `summary` | `kubectl` | `46394.69` | `0.649` | `1.000` | `0.927` | `0.500` | `0.392` | `0.282` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | - | - |
| `kubectl-07` | `recall` | `kubectl` | `2202.83` | `0.990` | `1.000` | `0.959` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `49126.00` | `0.332` | `0.000` | `0.727` | `1.000` | `0.726` | `0.086` | `soft_accepted` | missing_exact_anchors | terraform plan -lock-timeout=5s -out=tfplan, Error acquiring the state lock, 9c4fd2f2-8b24-42c1-93b5-65f0e2d83f63, prod/network/terraform.tfstate | - |
| `terraform-06` | `summary` | `terraform` | `2022.81` | `0.974` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `7969.17` | `0.974` | `1.000` | `0.936` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `3203.48` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `11502.66` | `0.972` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `3092.00` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `23992.92` | `0.844` | `1.000` | `0.910` | `1.000` | `0.759` | `0.196` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `2566.68` | `0.987` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `6969.34` | `0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `6976.84` | `0.946` | `1.000` | `0.939` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `3062.72` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `5082.54` | `0.423` | `0.000` | `0.790` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ruff check ., src/api/views.py, line=91, Ruff F821, exit code 2 | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `8583.68` | `0.533` | `0.000` | `0.808` | `1.000` | `0.908` | `0.692` | `soft_accepted` | missing_exact_anchors | pnpm install --frozen-lockfile, ERR_PNPM_ENOSPC, no space left on device, react-dom@18.3.1, ERROR: Job failed: exit status 1 | - |
| `jenkins-01` | `summary` | `jenkins` | `20732.56` | `0.820` | `1.000` | `0.864` | `1.000` | `0.748` | `0.159` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `5343.30` | `0.510` | `0.000` | `0.714` | `1.000` | `0.928` | `0.761` | `soft_accepted` | missing_exact_anchors | make CFLAGS='-O2 -Wall -Werror' all, src/parser.c:214:12, parse_config, Makefile:22, Error 1 | - |
| `tar-01` | `summary` | `tar` | `2430.44` | `0.990` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `11019.90` | `0.914` | `1.000` | `0.937` | `1.000` | `0.790` | `0.300` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `11130.88` | `0.896` | `1.000` | `0.911` | `1.000` | `0.864` | `0.545` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `22784.19` | `0.913` | `1.000` | `0.918` | `1.000` | `0.799` | `0.330` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `5374.41` | `0.410` | `0.000` | `0.728` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | error[E0382], src/router.rs:137:42, borrow of moved value: `req`, src/router.rs:128, req.into_body(), req.method(), req.clone().into_body() | - |
| `ci-log-01` | `recall` | `ci-log` | `10668.75` | `0.928` | `1.000` | `0.914` | `1.000` | `0.850` | `0.500` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `3814.30` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `13045.71` | `0.659` | `0.357` | `0.840` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | TestCheckoutAppliesStoreCredit, checkout_test.go:71, total = 42.00, want 37.00, TestReconcileInventory, test timed out after 10m0s, worker.go:144 | - |
| `build-log-01` | `summary` | `build-log` | `22686.05` | `0.663` | `1.000` | `0.895` | `0.500` | `0.422` | `0.482` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `docker-build-02` | `summary` | `docker-build` | `14745.84` | `0.709` | `1.000` | `0.907` | `0.000` | `0.000` | `0.638` | `accepted` | - | - | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `8378.94` | `0.226` | `0.250` | `0.625` | `0.000` | `0.000` | `0.286` | `soft_accepted` | missing_exact_anchors | /repo/web/src/App.tsx, /repo/web/src/api/client.ts, 8:10, @typescript-eslint/no-explicit-any, 33:11, @typescript-eslint/no-unsafe-assignment | - |
| `git-review-01` | `instruction_following` | `git-review` | `14062.61` | `0.324` | `0.714` | `0.685` | `0.000` | `0.000` | `0.333` | `soft_accepted` | missing_exact_anchors | User.lastLoginIp, DROP COLUMN refresh_token_expires_at, session cookie maxAge changed from 86400 to 604800 | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `6853.85` | `0.401` | `0.774` | `0.724` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | search endpoint failed after 2 attempts | - |
| `structured-output-01` | `structured` | `structured-output` | `6086.11` | `0.333` | `0.222` | `0.824` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /work/app/services/payments.py, /work/app/api/routes.py, 21, reportUndefinedVariable | - |
| `structured-output-02` | `structured` | `structured-output` | `14692.03` | `0.146` | `0.429` | `0.189` | `0.000` | `0.000` | `0.294` | `soft_accepted` | missing_exact_anchors | test / integration, port 5432 is already allocated, deploy / preview | - |
| `structured-output-03` | `structured` | `structured-output` | `7333.69` | `0.199` | `0.143` | `0.435` | `0.000` | `0.000` | `0.750` | `soft_accepted` | missing_exact_anchors | createSession › rejects expired refresh token, src/auth/session.test.ts, calculateTax › uses EU VAT for DE customer, src/billing/tax.test.ts, Expected: 19, Received: 0 | - |
| `structured-output-04` | `structured` | `structured-output` | `11093.61` | `0.220` | `0.938` | `0.218` | `0.000` | `0.000` | `0.056` | `soft_accepted` | missing_exact_anchors | date-fns-tz | - |
| `exact-format-01` | `exact_format` | `exact-format` | `8810.19` | `0.182` | `1.000` | `0.312` | `0.000` | `0.000` | `0.020` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `9365.95` | `0.121` | `0.714` | `0.319` | `0.000` | `0.000` | `0.055` | `soft_accepted` | missing_exact_anchors | SearchBox debounces network query before fetch | - |
| `exact-format-03` | `exact_format` | `exact-format` | `8012.62` | `0.183` | `1.000` | `0.307` | `0.000` | `0.000` | `0.040` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `6643.31` | `0.685` | `0.778` | `0.900` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | shadowing | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `2834.93` | `0.925` | `1.000` | `0.850` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `3149.37` | `0.743` | `1.000` | `0.886` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `6513.82` | `0.959` | `1.000` | `0.936` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `5037.52` | `0.980` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `21674.86` | `0.915` | `1.000` | `0.913` | `1.000` | `0.809` | `0.364` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `12896.90` | `0.748` | `1.000` | `0.921` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `10382.57` | `0.960` | `1.000` | `0.921` | `1.000` | `0.940` | `0.800` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `6028.04` | `0.970` | `1.000` | `0.903` | `1.000` | `0.983` | `0.944` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `11495.48` | `0.787` | `0.897` | `0.919` | `1.000` | `0.978` | `0.927` | `soft_accepted` | missing_exact_anchors | could not compile `storage` | - |
| `docker-compose-05` | `recall` | `docker-compose` | `4490.39` | `0.986` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `6214.46` | `0.987` | `1.000` | `0.948` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `5839.37` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `10539.20` | `0.798` | `0.895` | `0.946` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | --frozen-lockfile | - |
| `swift-01` | `recall` | `swift` | `4714.63` | `0.401` | `0.000` | `0.686` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | UserDecoderTests testMissingAvatarUsesPlaceholder, Tests/UserDecoderTests.swift:47, XCTAssertEqual failed, nil, Optional(placeholder.png), fatalError | - |
| `elixir-01` | `recall` | `elixir` | `8255.48` | `0.984` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `5784.29` | `0.408` | `0.000` | `0.718` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 20260518093012 AddIndexToEventsRequestId, index_events_on_request_id, events, already exists, 20260518093012_add_index_to_events_request_id.rb:3, ArgumentError | - |
| `phpunit-01` | `recall` | `phpunit` | `5164.15` | `0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `2526.80` | `0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `8644.64` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `6285.00` | `0.677` | `0.625` | `0.861` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ansible-playbook deploy.yml -i inventory/prod.ini | - |
| `bazel-01` | `recall` | `bazel` | `48761.32` | `0.501` | `0.208` | `0.832` | `1.000` | `0.962` | `0.875` | `soft_accepted` | missing_exact_anchors | XMLSyntaxError, Opening and ending tag mismatch: total line 18 and totals, services/reporting/parser.py", line 141, etree.fromstring(xml_bytes) | - |
| `powershell-01` | `recall` | `powershell` | `4434.95` | `0.984` | `1.000` | `0.937` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `5554.25` | `0.379` | `0.000` | `0.764` | `1.000` | `0.863` | `0.544` | `soft_accepted` | missing_exact_anchors | web@1.7.0, upload-sourcemaps dist --rewrite, Authentication credentials were not provided, http status: 401, exit code 1 | - |
| `python-pytest-01` | `summary` | `python-pytest` | `5132.00` | `0.968` | `1.000` | `0.919` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `3730.64` | `0.960` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `11590.53` | `0.914` | `1.000` | `0.895` | `1.000` | `0.913` | `0.710` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `2390.46` | `0.965` | `1.000` | `0.914` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `6462.17` | `0.960` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `2692.28` | `0.943` | `1.000` | `0.858` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `composer-01` | `summary` | `composer` | `5290.67` | `0.950` | `1.000` | `0.940` | `1.000` | `0.949` | `0.830` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `2295.48` | `0.939` | `1.000` | `0.846` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `9936.34` | `0.739` | `1.000` | `0.924` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `5000.28` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | auto, tests/e2e, Not, properly, terminated | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Exclude irrelevant success noise Include only items that satisfy the instruction Omit related but out-of-scope ite...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Exclude irrelevant success noise Include only items that satisfy the instruction Omit related but out-of-scope ite...' |
| `jest-01` | `summary` | `jest` | `4033.77` | `0.961` | `1.000` | `0.903` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `2040.77` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | --select, fact_orders, Compilation, Error, model | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Exclude irrelevant success noise' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Exclude irrelevant success noise' |
| `python-pytest-03` | `summary` | `python-pytest` | `8632.95` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo, schema_echo | tests/test_signup.py, FAILED, tests/test_signup.py::test_signup_is_idempotent, sqlalchemy.exc.IntegrityError, psycopg.errors.UniqueViolation | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Exclude irrelevant success noise Include only items that satisfy the instruction Omit related but out-of-scope ite...' repair_status=rejected repair_flags=['schema_echo', 'prompt_scaffold_echo'] repair_pass='tests/test_signup.py FAILED tests/test_signup.py::test_signup_is_idempotent sqlalchemy.exc.IntegrityError psycopg.errors.UniqueViolation Output form: return ...' |
| `wrangler-01` | `summary` | `wrangler` | `7636.48` | `0.772` | `0.800` | `0.896` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | deploy | - |
| `python-pytest-04` | `summary` | `python-pytest` | `3285.76` | `0.970` | `1.000` | `0.926` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `2673.03` | `0.593` | `1.000` | `0.978` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `7587.04` | `0.452` | `1.000` | `0.711` | `0.000` | `0.000` | `0.388` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `2240.46` | `0.414` | `1.000` | `0.688` | `0.000` | `0.000` | `0.071` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `12129.07` | `0.349` | `0.800` | `0.691` | `0.039` | `0.031` | `0.279` | `soft_accepted` | missing_exact_anchors | node=22, node=20 | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `5113.36` | `0.209` | `0.000` | `0.646` | `0.000` | `0.000` | `0.524` | `soft_accepted` | missing_exact_anchors | Warning Failed, secret "api-env" not found, Warning BackOff, Back-off restarting failed container api | - |
| `npm-06` | `instruction_following` | `npm` | `1942.54` | `0.682` | `1.000` | `0.739` | `0.400` | `0.400` | `1.000` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `3755.08` | `0.418` | `1.000` | `0.686` | `0.000` | `0.000` | `0.118` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `1327.50` | `0.650` | `1.000` | `0.722` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `8817.65` | `0.291` | `0.250` | `0.735` | `0.000` | `0.000` | `0.724` | `soft_accepted` | missing_exact_anchors | UserService.java:[44,17], findByEmail, UserController.java:[28,31] | - |
| `playwright-01` | `instruction_following` | `playwright` | `46490.01` | `0.143` | `0.000` | `0.532` | `0.000` | `0.000` | `0.086` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | firefox, checkout.spec.ts:44:1, pays with saved card, Payment complete | - |
| `prettier-01` | `instruction_following` | `prettier` | `954.08` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `11228.04` | `0.453` | `1.000` | `0.782` | `0.000` | `0.000` | `0.182` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `4691.54` | `0.322` | `0.333` | `0.706` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | src/auth.rs:88, billing::tests::rounds_half_even, left: 1750, right: 1749 | - |
| `shell-01` | `instruction_following` | `shell` | `5290.74` | `0.265` | `0.286` | `0.674` | `0.000` | `0.000` | `0.529` | `soft_accepted` | missing_exact_anchors | /var/backups/uploads, Permission denied (13) | - |
| `pyright-01` | `structured` | `pyright` | `9464.22` | `0.265` | `0.400` | `0.614` | `0.000` | `0.000` | `0.471` | `soft_accepted` | missing_exact_anchors | file, /repo/app/user.py, line | - |
| `terraform-10` | `structured` | `terraform` | `3920.71` | `0.288` | `0.667` | `0.519` | `0.000` | `0.000` | `0.500` | `soft_accepted` | missing_exact_anchors | resource, field | - |
| `junit-01` | `structured` | `junit` | `7001.57` | `0.247` | `0.286` | `0.523` | `0.000` | `0.000` | `0.765` | `soft_accepted` | missing_exact_anchors | Test, Error, Location, --- | - |
| `kubernetes-03` | `structured` | `kubernetes` | `10598.31` | `0.259` | `1.000` | `0.168` | `0.000` | `0.000` | `0.083` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `4446.44` | `0.190` | `0.556` | `0.291` | `0.000` | `0.000` | `0.250` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | line, column, rule, no-unused-vars | - |
| `docker-build-04` | `structured` | `docker-build` | `3645.14` | `0.407` | `0.852` | `0.694` | `0.000` | `0.000` | `1.000` | `soft_accepted` | missing_exact_anchors | pnpm | - |
| `go-test-04` | `structured` | `go-test` | `6952.36` | `0.258` | `0.879` | `0.196` | `0.000` | `0.000` | `0.688` | `soft_accepted` | missing_exact_anchors | location | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `3170.52` | `0.186` | `0.167` | `0.334` | `0.000` | `0.000` | `0.857` | `soft_accepted` | missing_exact_anchors | Job, Step, Exit, ---, test | - |
| `npm-07` | `structured` | `npm` | `5291.29` | `0.159` | `0.333` | `0.307` | `0.000` | `0.000` | `0.286` | `soft_accepted` | missing_exact_anchors | package, peer, required, 18.0.0 | - |
| `mypy-06` | `structured` | `mypy` | `6792.05` | `0.204` | `0.000` | `0.611` | `0.000` | `0.000` | `0.562` | `soft_accepted` | missing_exact_anchors | File, Line, Code, Message, ---, app/api.py | - |
| `gradle-03` | `structured` | `gradle` | `46137.24` | `0.187` | `0.697` | `0.250` | `0.000` | `0.000` | `0.059` | `soft_accepted` | missing_exact_anchors, structured_output_mismatch | :api:compileJava | - |
| `playwright-02` | `structured` | `playwright` | `3981.58` | `0.404` | `1.000` | `0.345` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `25777.94` | `0.502` | `1.000` | `0.789` | `0.000` | `0.000` | `0.652` | `accepted` | - | - | - |
| `vite-01` | `structured` | `vite` | `4309.10` | `0.269` | `1.000` | `0.216` | `0.000` | `0.000` | `0.040` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `3819.94` | `0.022` | `0.000` | `0.248` | `0.000` | `0.000` | `0.030` | `soft_accepted` | missing_exact_anchors, exact_format_style_mismatch | tests/test_a.py::test_one, tests/test_b.py::TestB::test_three | - |
| `git-04` | `exact_format` | `git` | `2467.17` | `0.028` | `0.000` | `0.245` | `0.000` | `0.000` | `0.167` | `soft_accepted` | missing_exact_anchors | 9f4c2d7a1b8e3c6d0a1234567890abcdef123456 | - |
| `docker-04` | `exact_format` | `docker` | `4295.38` | `0.024` | `0.000` | `0.250` | `0.000` | `0.000` | `0.053` | `soft_accepted` | missing_exact_anchors, exact_format_style_mismatch | ghcr.io/acme/api@sha256:aaaaaaaa11111111bbbbbbbb22222222cccccccc33333333dddddddd44444444 | - |
| `npm-08` | `exact_format` | `npm` | `2455.42` | `0.192` | `1.000` | `0.294` | `0.000` | `0.000` | `0.250` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `3630.56` | `0.028` | `0.000` | `0.253` | `0.000` | `0.000` | `0.158` | `soft_accepted` | missing_exact_anchors, exact_format_style_mismatch | github.com/acme/shop/checkout, TestCheckoutAppliesCoupon | - |
| `kubectl-09` | `exact_format` | `kubectl` | `27322.51` | `0.189` | `1.000` | `0.290` | `0.000` | `0.000` | `0.200` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `4639.61` | `0.023` | `0.000` | `0.250` | `0.000` | `0.000` | `0.030` | `soft_accepted` | missing_exact_anchors, exact_format_style_mismatch | auth::tests::rejects_expired, billing::tests::rounds_half_even | - |
| `curl-03` | `exact_format` | `curl` | `1988.76` | `0.194` | `1.000` | `0.281` | `0.000` | `0.000` | `1.000` | `soft_accepted` | exact_format_style_mismatch | - | - |
| `rails-02` | `exact_format` | `rails` | `3988.38` | `0.178` | `1.000` | `0.249` | `0.000` | `0.000` | `0.056` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `7152.52` | `0.731` | `1.000` | `0.921` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `2487.17` | `0.945` | `1.000` | `0.890` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `3241.24` | `0.877` | `1.000` | `0.887` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `2570.69` | `0.951` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `4414.53` | `0.944` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `7343.38` | `0.673` | `1.000` | `0.783` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `2721.97` | `0.710` | `0.583` | `0.837` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | contents: write | - |
| `runtime-01` | `recall` | `runtime` | `6154.32` | `0.951` | `1.000` | `0.922` | `1.000` | `0.910` | `0.700` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `2093.00` | `0.977` | `1.000` | `0.944` | `1.000` | `0.973` | `0.909` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `2026.83` | `0.662` | `0.545` | `0.936` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | /usr/src/app/index.js:12:15 | - |
| `package-management-01` | `recall` | `package-management` | `3060.89` | `0.974` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `3714.91` | `0.401` | `0.000` | `0.689` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | duplicate key value violates unique constraint, test@example.com, INSERT INTO users | - |
| `compilation-01` | `recall` | `compilation` | `3654.25` | `0.965` | `1.000` | `0.952` | `1.000` | `0.931` | `0.769` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `6240.18` | `0.918` | `1.000` | `0.884` | `1.000` | `0.841` | `0.469` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `2252.62` | `0.967` | `1.000` | `0.868` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `2178.99` | `0.903` | `1.000` | `0.858` | `1.000` | `0.815` | `0.382` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `1696.66` | `0.952` | `1.000` | `0.892` | `1.000` | `0.937` | `0.789` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `5315.08` | `0.950` | `1.000` | `0.901` | `1.000` | `0.925` | `0.750` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `3268.73` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `2288.44` | `0.966` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `2528.55` | `0.586` | `0.412` | `0.819` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Execution failed for task ':test' | - |
| `container-runtime-01` | `recall` | `container-runtime` | `873.56` | `0.979` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `2003.07` | `0.587` | `0.364` | `0.907` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | 1 error | - |
| `infrastructure-02` | `recall` | `infrastructure` | `1595.13` | `0.970` | `1.000` | `0.880` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `808.61` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `1453.69` | `0.649` | `0.500` | `0.952` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | No matching distribution found | - |
| `infrastructure-03` | `recall` | `infrastructure` | `3645.70` | `0.414` | `0.000` | `0.859` | `1.000` | `0.917` | `0.722` | `soft_accepted` | missing_exact_anchors | COPY failed, no such file or directory | - |
| `testing-04` | `recall` | `testing` | `1925.01` | `0.492` | `0.167` | `0.814` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | Failure/Error, capybara-3.34.0/lib/capybara/node/element.rb:1008 | - |
| `build-02` | `recall` | `build` | `4815.60` | `0.976` | `1.000` | `0.902` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `3492.79` | `0.620` | `0.444` | `0.920` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | ERROR: failed to fetch | - |
| `testing-05` | `recall` | `testing` | `668.71` | `0.974` | `1.000` | `0.895` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `1742.75` | `0.747` | `0.714` | `0.875` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | failing tests | - |
| `docker-05` | `summary` | `docker` | `1451.08` | `0.945` | `1.000` | `0.862` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `730.51` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `1949.11` | `0.950` | `1.000` | `0.875` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `2106.97` | `0.472` | `0.000` | `0.817` | `1.000` | `0.756` | `0.188` | `soft_accepted` | missing_exact_anchors | ERESOLVE, unable to resolve dependency tree | - |
| `rust-02` | `summary` | `rust` | `2715.94` | `0.551` | `0.000` | `0.857` | `1.000` | `0.910` | `0.700` | `soft_accepted` | missing_exact_anchors | Finished dev | - |
| `linting-01` | `instruction_following` | `linting` | `2044.20` | `0.576` | `1.000` | `0.821` | `0.200` | `0.170` | `0.500` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `3295.72` | `0.523` | `0.500` | `0.719` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors | ERROR: | - |
| `ci-05` | `instruction_following` | `ci` | `5788.24` | `0.360` | `1.000` | `0.729` | `0.000` | `0.000` | `0.043` | `soft_accepted` | structured_output_mismatch | - | - |
| `linting-02` | `structured` | `linting` | `1535.69` | `0.503` | `1.000` | `0.678` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `1558.69` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `1453.66` | `0.445` | `1.000` | `0.551` | `0.000` | `0.000` | `0.800` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `2035.69` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `5865.00` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `3475.50` | `0.502` | `1.000` | `0.856` | `0.333` | `0.300` | `0.667` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `4491.94` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | NullPointerException | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them Include only items that ...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them Include only items that ...' |
| `build-04` | `exact_format` | `build` | `2894.87` | `0.463` | `1.000` | `0.946` | `0.250` | `0.241` | `0.875` | `accepted` | - | - | - |
| `build-05` | `exact_format` | `build` | `870.10` | `0.225` | `1.000` | `0.609` | `0.000` | `0.000` | `0.286` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `4330.49` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | PATH | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them include only items that ...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary avoid headings, bullets, markdown, or extra sections unless the instruction asks for them include only items that ...' |
| `deployment-03` | `explanation` | `deployment` | `1661.54` | `0.936` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `2433.73` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | IndexError: list index out of range | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `container-runtime-02` | `explanation` | `container-runtime` | `2670.84` | `0.958` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `1894.45` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | Cannot find module 'express' | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `ci-06` | `explanation` | `ci` | `1551.42` | `0.941` | `1.000` | `0.882` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `2173.25` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | KeyError: 'username' | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `deployment-04` | `explanation` | `deployment` | `2394.55` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | password authentication failed | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `explanation-01` | `explanation` | `explanation` | `2267.24` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | Cannot find module 'react' | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `explanation-02` | `explanation` | `explanation` | `638.90` | `0.923` | `1.000` | `0.847` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `2146.60` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | no configured push destination | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `explanation-04` | `explanation` | `explanation` | `864.23` | `0.938` | `1.000` | `0.875` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `2624.36` | `0.546` | `0.000` | `0.686` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | command not found | - |
| `explanation-06` | `explanation` | `explanation` | `920.81` | `0.910` | `1.000` | `0.819` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `1542.92` | `0.629` | `0.000` | `0.880` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | SECRET_KEY setting must not be empty | - |
| `explanation-08` | `explanation` | `explanation` | `586.75` | `0.920` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `2206.36` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | would be overwritten by merge | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `explanation-10` | `explanation` | `explanation` | `2209.51` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | KeyError: 'API_KEY' | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `explanation-11` | `explanation` | `explanation` | `2491.95` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | Address already in use | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `explanation-12` | `explanation` | `explanation` | `666.98` | `0.875` | `1.000` | `0.750` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `1397.20` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `1494.88` | `0.445` | `1.000` | `0.551` | `0.000` | `0.000` | `0.800` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `2135.69` | `0.208` | `1.000` | `0.332` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `5908.50` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `1519.20` | `0.431` | `0.500` | `0.324` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors | value2 | - |
| `build-06` | `exact_format` | `build` | `2753.58` | `0.463` | `1.000` | `0.946` | `0.250` | `0.241` | `0.875` | `accepted` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `2449.26` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `5127.04` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | testError:34 | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them Include only items that ...' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them Include only items that ...' |
| `shell-08` | `exact_format` | `shell` | `807.44` | `0.230` | `1.000` | `0.298` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `1744.93` | `0.936` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `2454.27` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | IndexError: list index out of range | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `deployment-07` | `explanation` | `deployment` | `698.14` | `0.958` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `2282.60` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | cannot list resource "pods" | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `explanation-14` | `explanation` | `explanation` | `2212.16` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | password authentication failed | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `explanation-15` | `explanation` | `explanation` | `2502.85` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | Cannot find module 'lodash' | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `explanation-16` | `explanation` | `explanation` | `2471.66` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | undefined: fmt.Println | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='Return a concise plain-text recall summary Avoid headings, bullets, markdown, or extra sections unless the instruction asks for them' |
| `explanation-17` | `explanation` | `explanation` | `1410.18` | `0.000` | `0.000` | `0.000` | `0.000` | `0.000` | `1.000` | `rejected` | prompt_scaffold_echo | missing script: start | fallback output validation failed. first_pass_status=rejected first_pass_flags=['prompt_scaffold_echo'] first_pass='return a concise plain-text recall summary' repair_status=rejected repair_flags=['prompt_scaffold_echo'] repair_pass='return a concise plain-text recall summary' |
| `package-management-04` | `explanation` | `package-management` | `1279.92` | `0.648` | `0.444` | `0.747` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | nonexistent (invalid) version of flask | - |
