# gpu-gemma4-e2b-it-no-quant

## Scenario

- track: `gpu`
- phase: `gpu-screen`
- model: `google/gemma-4-E2B-it`
- quantization: `none`
- device: `cuda`
- dtype: `auto`
- max_output_tokens: `768`
- concurrency: `1`

## Warmup

- load_ms: `605556.70`
- cpu_rss_bytes: `9042092032`
- gpu_peak_bytes: `11466671104`
- torch_num_threads: `12`
- torch_num_interop_threads: `12`
- OMP_NUM_THREADS: `null`
- MKL_NUM_THREADS: `null`

## Summary

- case_count: `280`
- success_count: `280`
- accepted_count: `267`
- soft_accepted_count: `13`
- rejected_count: `0`
- exact_pass_count: `274`
- avg_inference_ms: `162518.34`
- p95_inference_ms: `518881.69`
- avg_exact_preservation_ratio: `0.994`
- avg_summary_quality_ratio: `0.869`
- avg_format_adherence_score: `0.845`
- avg_instruction_following_score: `0.839`
- avg_brevity_ratio: `0.932`
- avg_case_score: `0.872`
- p10_case_score: `0.483`
- quality_core: `0.794`
- latency_factor: `0.850`
- final_score: `67.49`
- peak_cpu_rss_bytes: `9260822528`
- peak_gpu_bytes: `11769882624`

## Cases

| case_id | family | domain | ms | case_score | preserve | quality | format | instruction | brevity | validation | flags | missing | error |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `python-01` | `recall` | `python` | `15328.41` | `0.995` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-02` | `summary` | `python` | `271508.25` | `0.626` | `1.000` | `0.949` | `0.500` | `0.357` | `0.044` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `python-03` | `recall` | `python` | `13695.57` | `0.994` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-04` | `recall` | `python` | `17574.97` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-05` | `recall` | `python` | `16045.13` | `0.997` | `1.000` | `0.987` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-01` | `recall` | `pytest` | `22229.35` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-02` | `summary` | `pytest` | `26777.31` | `0.987` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-03` | `recall` | `pytest` | `514042.81` | `0.673` | `1.000` | `0.956` | `0.500` | `0.355` | `0.033` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `pytest-04` | `recall` | `pytest` | `253581.02` | `0.996` | `1.000` | `0.984` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-05` | `summary` | `pytest` | `269691.36` | `0.990` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-01` | `recall` | `mypy` | `18974.23` | `0.996` | `1.000` | `0.983` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-02` | `summary` | `mypy` | `35380.10` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-03` | `recall` | `mypy` | `254538.53` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-01` | `summary` | `ruff` | `254224.21` | `0.984` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-02` | `summary` | `ruff` | `254763.14` | `0.993` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-03` | `summary` | `ruff` | `274369.86` | `0.972` | `1.000` | `0.931` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-01` | `recall` | `pylint` | `11335.76` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-02` | `recall` | `pylint` | `18068.77` | `0.992` | `1.000` | `0.967` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pylint-03` | `summary` | `pylint` | `15136.16` | `0.994` | `1.000` | `0.984` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-01` | `summary` | `black` | `18251.80` | `0.996` | `1.000` | `0.991` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-02` | `summary` | `black` | `254361.35` | `0.970` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `black-03` | `recall` | `black` | `255164.66` | `0.996` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-01` | `recall` | `npm` | `23133.01` | `0.980` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-02` | `summary` | `npm` | `15475.02` | `0.983` | `1.000` | `0.958` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-03` | `summary` | `npm` | `12001.18` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-01` | `recall` | `pnpm` | `14796.05` | `0.991` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-02` | `summary` | `pnpm` | `22739.34` | `0.991` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-03` | `summary` | `pnpm` | `17861.43` | `0.991` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-01` | `summary` | `typescript` | `30033.84` | `0.983` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-02` | `recall` | `typescript` | `20836.39` | `0.995` | `1.000` | `0.979` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-03` | `summary` | `typescript` | `321124.39` | `0.699` | `1.000` | `0.956` | `0.500` | `0.440` | `0.603` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `eslint-01` | `recall` | `eslint` | `254182.02` | `0.985` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-02` | `summary` | `eslint` | `53626.88` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-03` | `recall` | `eslint` | `15748.06` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-01` | `recall` | `docker` | `255416.22` | `0.986` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-02` | `summary` | `docker` | `255591.65` | `0.988` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-03` | `summary` | `docker` | `18937.88` | `0.977` | `1.000` | `0.944` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-01` | `summary` | `docker-compose` | `7244.99` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-02` | `recall` | `docker-compose` | `11155.60` | `0.994` | `1.000` | `0.975` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-03` | `summary` | `docker-compose` | `32302.46` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-01` | `summary` | `kubectl` | `506933.33` | `0.982` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-02` | `recall` | `kubectl` | `23623.24` | `0.994` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-03` | `summary` | `kubectl` | `13708.68` | `0.993` | `1.000` | `0.981` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-04` | `recall` | `kubectl` | `21912.01` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-01` | `summary` | `terraform` | `255260.48` | `0.988` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-02` | `recall` | `terraform` | `49440.83` | `0.966` | `1.000` | `0.955` | `1.000` | `0.931` | `0.771` | `accepted` | - | - | - |
| `terraform-03` | `recall` | `terraform` | `254646.07` | `0.987` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-04` | `summary` | `terraform` | `254454.02` | `0.991` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-01` | `recall` | `mixed` | `16481.98` | `0.991` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mixed-02` | `summary` | `mixed` | `271226.46` | `0.976` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-01` | `recall` | `git` | `9317.61` | `0.972` | `1.000` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-02` | `recall` | `git` | `8980.78` | `0.986` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-03` | `recall` | `git` | `14087.99` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-01` | `recall` | `curl` | `30016.90` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `curl-02` | `summary` | `curl` | `508802.65` | `0.619` | `1.000` | `0.929` | `0.500` | `0.357` | `0.048` | `soft_accepted` | verbatim_alignment_weak | - | - |
| `ssh-01` | `summary` | `ssh` | `255202.47` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ssh-02` | `summary` | `ssh` | `253757.96` | `0.989` | `1.000` | `0.973` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-01` | `summary` | `systemd` | `11928.41` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `systemd-02` | `summary` | `systemd` | `9687.41` | `0.962` | `1.000` | `0.905` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `apt-01` | `summary` | `apt` | `269518.37` | `0.970` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dnf-01` | `recall` | `dnf` | `28746.86` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-build-01` | `summary` | `go-build` | `255226.77` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-01` | `summary` | `go-test` | `23356.64` | `0.987` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `javac-01` | `summary` | `javac` | `16867.00` | `0.978` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-01` | `summary` | `maven` | `509290.09` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-02` | `summary` | `maven` | `15580.79` | `0.990` | `1.000` | `0.976` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-01` | `recall` | `gradle` | `14091.85` | `0.992` | `1.000` | `0.970` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-02` | `summary` | `gradle` | `263087.57` | `0.978` | `1.000` | `0.946` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-01` | `summary` | `cargo` | `17977.83` | `0.988` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-02` | `summary` | `cargo` | `9959.13` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `node-runtime-01` | `recall` | `node-runtime` | `255862.57` | `0.991` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-04` | `summary` | `npm` | `13934.21` | `0.976` | `1.000` | `0.940` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tsc-01` | `summary` | `tsc` | `273802.67` | `0.993` | `1.000` | `0.983` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-04` | `summary` | `eslint` | `15036.59` | `0.991` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-runtime-01` | `summary` | `python-runtime` | `11600.81` | `0.991` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pytest-06` | `summary` | `pytest` | `268624.16` | `0.994` | `1.000` | `0.985` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-04` | `summary` | `mypy` | `36293.05` | `0.981` | `1.000` | `0.952` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-01` | `summary` | `docker-build` | `29485.03` | `0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-compose-04` | `summary` | `docker-compose` | `10793.29` | `0.988` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-05` | `summary` | `kubectl` | `255546.28` | `0.987` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-06` | `summary` | `kubectl` | `29054.10` | `0.827` | `1.000` | `0.933` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `kubectl-07` | `recall` | `kubectl` | `516795.80` | `0.993` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-05` | `recall` | `terraform` | `24523.94` | `0.997` | `1.000` | `0.989` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-06` | `summary` | `terraform` | `33312.36` | `0.979` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-07` | `summary` | `terraform` | `18902.21` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-01` | `summary` | `nginx` | `267989.38` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-02` | `summary` | `nginx` | `14183.44` | `0.988` | `1.000` | `0.971` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-01` | `recall` | `postgres` | `21418.41` | `0.998` | `1.000` | `0.991` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-02` | `summary` | `postgres` | `22224.51` | `0.986` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-01` | `summary` | `mysql` | `13974.05` | `0.994` | `1.000` | `0.986` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mysql-02` | `summary` | `mysql` | `264840.26` | `0.985` | `1.000` | `0.963` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-01` | `summary` | `redis` | `516751.15` | `0.986` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `redis-02` | `recall` | `redis` | `256419.04` | `0.988` | `1.000` | `0.954` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `github-actions-01` | `recall` | `github-actions` | `289026.93` | `0.973` | `1.000` | `0.891` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gitlab-ci-01` | `summary` | `gitlab-ci` | `15386.39` | `0.977` | `1.000` | `0.943` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jenkins-01` | `summary` | `jenkins` | `257325.41` | `0.966` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-01` | `summary` | `make` | `257732.18` | `0.980` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `tar-01` | `summary` | `tar` | `19039.59` | `0.984` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-01` | `recall` | `ansible` | `12956.10` | `0.994` | `1.000` | `0.978` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rsync-01` | `summary` | `rsync` | `256620.70` | `0.981` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-failure-01` | `recall` | `test-failure` | `32556.36` | `0.996` | `1.000` | `0.982` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compiler-error-01` | `recall` | `compiler-error` | `20908.79` | `0.990` | `1.000` | `0.961` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-log-01` | `recall` | `ci-log` | `256835.31` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-manager-01` | `recall` | `package-manager` | `28127.75` | `0.994` | `1.000` | `0.977` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `test-summary-01` | `summary` | `test-summary` | `61347.00` | `0.705` | `0.500` | `0.885` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | TestCheckoutAppliesStoreCredit, checkout_test.go:71, test timed out after 10m0s, worker.go:144 | - |
| `build-log-01` | `summary` | `build-log` | `254805.19` | `0.962` | `1.000` | `0.906` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-02` | `summary` | `docker-build` | `265515.91` | `0.753` | `0.667` | `0.923` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "/apps/web": not found | - |
| `lint-output-01` | `instruction_following` | `lint-output` | `255799.56` | `0.757` | `1.000` | `0.991` | `0.400` | `0.400` | `1.000` | `accepted` | - | - | - |
| `git-review-01` | `instruction_following` | `git-review` | `42877.87` | `0.722` | `1.000` | `0.757` | `0.500` | `0.492` | `0.944` | `accepted` | - | - | - |
| `mixed-output-01` | `instruction_following` | `mixed-output` | `20075.02` | `0.917` | `1.000` | `0.722` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-01` | `structured` | `structured-output` | `47946.74` | `0.590` | `1.000` | `0.977` | `0.000` | `0.000` | `0.967` | `accepted` | - | - | - |
| `structured-output-02` | `structured` | `structured-output` | `62381.25` | `0.536` | `1.000` | `0.786` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `structured-output-03` | `structured` | `structured-output` | `55022.65` | `0.827` | `0.929` | `0.958` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | "refresh token expired" | - |
| `structured-output-04` | `structured` | `structured-output` | `41748.49` | `0.369` | `1.000` | `0.229` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-01` | `exact_format` | `exact-format` | `51257.93` | `0.300` | `1.000` | `0.997` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-02` | `exact_format` | `exact-format` | `21597.14` | `0.233` | `1.000` | `0.330` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `exact-format-03` | `exact_format` | `exact-format` | `513012.80` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-01` | `explanation` | `diagnosis` | `33181.28` | `0.982` | `1.000` | `0.964` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `diagnosis-02` | `explanation` | `diagnosis` | `284973.26` | `0.681` | `0.750` | `0.902` | `0.500` | `0.500` | `1.000` | `soft_accepted` | missing_exact_anchors, plain_text_style_mismatch | AvatarProps.url | - |
| `diagnosis-03` | `explanation` | `diagnosis` | `48784.71` | `0.890` | `1.000` | `0.939` | `0.667` | `0.640` | `0.868` | `accepted` | - | - | - |
| `python-traceback-01` | `recall` | `python-traceback` | `19785.05` | `0.991` | `1.000` | `0.965` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `mypy-05` | `recall` | `mypy` | `256154.43` | `0.981` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `terraform-08` | `recall` | `terraform` | `30808.52` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `gradle-junit-01` | `recall` | `gradle-junit` | `15372.12` | `0.982` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-01` | `recall` | `kubernetes` | `24061.89` | `0.988` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-02` | `recall` | `go-test` | `43126.19` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `cargo-03` | `recall` | `cargo` | `31781.58` | `0.803` | `0.897` | `0.964` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | could not compile `storage` | - |
| `docker-compose-05` | `recall` | `docker-compose` | `13252.69` | `0.989` | `1.000` | `0.956` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-01` | `recall` | `typescript-tsc` | `19798.93` | `0.989` | `1.000` | `0.955` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-01` | `recall` | `ci-github-actions` | `26453.02` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `pnpm-04` | `recall` | `pnpm` | `16585.92` | `0.992` | `1.000` | `0.968` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `swift-01` | `recall` | `swift` | `12281.56` | `0.993` | `1.000` | `0.972` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `elixir-01` | `recall` | `elixir` | `17231.49` | `0.984` | `1.000` | `0.935` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rails-01` | `recall` | `rails` | `24147.82` | `0.984` | `1.000` | `0.934` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `phpunit-01` | `recall` | `phpunit` | `21309.36` | `0.994` | `1.000` | `0.974` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `nginx-03` | `recall` | `nginx` | `255685.65` | `0.987` | `1.000` | `0.950` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-03` | `recall` | `postgres` | `15337.15` | `0.989` | `1.000` | `0.957` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ansible-02` | `recall` | `ansible` | `15888.80` | `0.992` | `1.000` | `0.966` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `bazel-01` | `recall` | `bazel` | `278066.70` | `0.968` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `powershell-01` | `recall` | `powershell` | `16359.99` | `0.987` | `1.000` | `0.947` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `sentry-cli-01` | `recall` | `sentry-cli` | `12493.54` | `0.987` | `1.000` | `0.949` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-01` | `summary` | `python-pytest` | `278734.22` | `0.960` | `1.000` | `0.899` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `go-test-03` | `summary` | `go-test` | `310123.56` | `0.967` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-05` | `summary` | `npm` | `518746.04` | `0.948` | `1.000` | `0.871` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `helm-01` | `summary` | `helm` | `255704.22` | `0.971` | `1.000` | `0.928` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ruff-04` | `summary` | `ruff` | `31267.20` | `0.951` | `1.000` | `0.877` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `k6-01` | `summary` | `k6` | `261402.26` | `0.718` | `0.696` | `0.802` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | http_req_failed | - |
| `composer-01` | `summary` | `composer` | `20993.46` | `0.915` | `1.000` | `0.788` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `xcodebuild-01` | `summary` | `xcodebuild` | `356596.47` | `0.941` | `1.000` | `0.853` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `make-02` | `summary` | `make` | `623656.77` | `0.959` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-02` | `summary` | `python-pytest` | `34090.85` | `0.928` | `1.000` | `0.819` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `jest-01` | `summary` | `jest` | `266338.46` | `0.958` | `1.000` | `0.894` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `dbt-01` | `summary` | `dbt` | `337984.94` | `0.958` | `1.000` | `0.896` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-03` | `summary` | `python-pytest` | `13551.26` | `0.959` | `1.000` | `0.896` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `wrangler-01` | `summary` | `wrangler` | `274741.01` | `0.931` | `1.000` | `0.827` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-04` | `summary` | `python-pytest` | `270763.09` | `0.980` | `1.000` | `0.951` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `eslint-05` | `instruction_following` | `eslint` | `16606.52` | `0.999` | `1.000` | `0.996` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `git-diff-01` | `instruction_following` | `git-diff` | `17030.89` | `0.962` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `python-pytest-05` | `instruction_following` | `python-pytest` | `12482.50` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-02` | `instruction_following` | `ci-github-actions` | `19214.38` | `0.938` | `1.000` | `0.795` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-02` | `instruction_following` | `kubernetes` | `11831.36` | `0.919` | `1.000` | `0.730` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-06` | `instruction_following` | `npm` | `17507.59` | `0.900` | `1.000` | `0.932` | `0.800` | `0.800` | `1.000` | `accepted` | - | - | - |
| `docker-build-03` | `instruction_following` | `docker-build` | `13423.81` | `0.523` | `1.000` | `0.742` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `terraform-09` | `instruction_following` | `terraform` | `9084.17` | `0.916` | `1.000` | `0.721` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `maven-03` | `instruction_following` | `maven` | `267962.72` | `0.983` | `1.000` | `0.945` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `playwright-01` | `instruction_following` | `playwright` | `20940.11` | `0.713` | `1.000` | `0.711` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `prettier-01` | `instruction_following` | `prettier` | `8354.84` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubectl-08` | `instruction_following` | `kubectl` | `271070.64` | `0.523` | `1.000` | `0.744` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `cargo-04` | `instruction_following` | `cargo` | `48752.84` | `0.653` | `1.000` | `0.733` | `0.333` | `0.333` | `1.000` | `accepted` | - | - | - |
| `shell-01` | `instruction_following` | `shell` | `14686.86` | `0.512` | `1.000` | `0.706` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `pyright-01` | `structured` | `pyright` | `272258.25` | `0.387` | `1.000` | `0.528` | `0.000` | `0.000` | `0.286` | `accepted` | - | - | - |
| `terraform-10` | `structured` | `terraform` | `66209.65` | `0.478` | `1.000` | `0.636` | `0.000` | `0.000` | `0.875` | `accepted` | - | - | - |
| `junit-01` | `structured` | `junit` | `267340.14` | `0.849` | `1.000` | `0.498` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-03` | `structured` | `kubernetes` | `13846.91` | `0.446` | `1.000` | `0.485` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `eslint-06` | `structured` | `eslint` | `268059.26` | `0.358` | `1.000` | `0.342` | `0.000` | `0.000` | `0.556` | `accepted` | - | - | - |
| `docker-build-04` | `structured` | `docker-build` | `35679.66` | `0.376` | `1.000` | `0.463` | `0.000` | `0.000` | `0.368` | `accepted` | - | - | - |
| `go-test-04` | `structured` | `go-test` | `17947.65` | `0.483` | `1.000` | `0.611` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-03` | `structured` | `ci-github-actions` | `23623.54` | `0.846` | `1.000` | `0.694` | `1.000` | `0.812` | `0.375` | `accepted` | - | - | - |
| `npm-07` | `structured` | `npm` | `16694.58` | `0.371` | `1.000` | `0.236` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `mypy-06` | `structured` | `mypy` | `270814.72` | `0.959` | `1.000` | `0.896` | `1.000` | `0.970` | `0.900` | `accepted` | - | - | - |
| `gradle-03` | `structured` | `gradle` | `16977.75` | `0.413` | `1.000` | `0.376` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `playwright-02` | `structured` | `playwright` | `19344.84` | `0.421` | `1.000` | `0.405` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `postgres-04` | `structured` | `postgres` | `41227.56` | `0.506` | `1.000` | `0.812` | `0.000` | `0.000` | `0.625` | `accepted` | - | - | - |
| `vite-01` | `structured` | `vite` | `269326.89` | `0.268` | `1.000` | `0.215` | `0.000` | `0.000` | `0.034` | `accepted` | - | - | - |
| `python-pytest-06` | `exact_format` | `python-pytest` | `267931.89` | `0.180` | `1.000` | `0.302` | `0.000` | `0.000` | `0.001` | `accepted` | - | - | - |
| `git-04` | `exact_format` | `git` | `267420.74` | `0.180` | `1.000` | `0.298` | `0.000` | `0.000` | `0.001` | `accepted` | - | - | - |
| `docker-04` | `exact_format` | `docker` | `269093.32` | `0.182` | `1.000` | `0.322` | `0.000` | `0.000` | `0.002` | `accepted` | - | - | - |
| `npm-08` | `exact_format` | `npm` | `266990.63` | `0.180` | `1.000` | `0.301` | `0.000` | `0.000` | `0.001` | `accepted` | - | - | - |
| `go-test-05` | `exact_format` | `go-test` | `350796.83` | `0.182` | `1.000` | `0.315` | `0.000` | `0.000` | `0.004` | `accepted` | - | - | - |
| `kubectl-09` | `exact_format` | `kubectl` | `328755.86` | `0.180` | `1.000` | `0.294` | `0.000` | `0.000` | `0.005` | `accepted` | - | - | - |
| `cargo-05` | `exact_format` | `cargo` | `379502.33` | `0.533` | `1.000` | `0.334` | `0.500` | `0.350` | `0.001` | `accepted` | - | - | - |
| `curl-03` | `exact_format` | `curl` | `371767.94` | `0.178` | `1.000` | `0.283` | `0.000` | `0.000` | `0.001` | `accepted` | - | - | - |
| `rails-02` | `exact_format` | `rails` | `344580.30` | `0.179` | `1.000` | `0.285` | `0.000` | `0.000` | `0.001` | `accepted` | - | - | - |
| `python-traceback-02` | `explanation` | `python-traceback` | `751750.56` | `0.958` | `1.000` | `0.917` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `typescript-tsc-02` | `explanation` | `typescript-tsc` | `316324.85` | `0.949` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `postgres-05` | `explanation` | `postgres` | `32596.28` | `0.960` | `1.000` | `0.920` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-build-05` | `explanation` | `docker-build` | `554172.79` | `0.718` | `1.000` | `0.890` | `0.500` | `0.500` | `1.000` | `soft_accepted` | plain_text_style_mismatch | - | - |
| `kubernetes-04` | `explanation` | `kubernetes` | `422006.24` | `0.955` | `1.000` | `0.909` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `rust-01` | `explanation` | `rust` | `9224.17` | `0.895` | `1.000` | `0.790` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-github-actions-04` | `explanation` | `ci-github-actions` | `276496.32` | `0.881` | `1.000` | `0.761` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-01` | `recall` | `runtime` | `281997.88` | `0.978` | `1.000` | `0.961` | `1.000` | `0.962` | `0.875` | `accepted` | - | - | - |
| `testing-01` | `recall` | `testing` | `10572.33` | `0.990` | `1.000` | `0.960` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-02` | `recall` | `testing` | `13777.90` | `0.988` | `1.000` | `0.953` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-01` | `recall` | `package-management` | `14118.58` | `0.981` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-02` | `recall` | `runtime` | `7655.87` | `0.980` | `1.000` | `0.918` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-01` | `recall` | `compilation` | `273344.55` | `0.950` | `1.000` | `0.950` | `1.000` | `0.887` | `0.625` | `accepted` | - | - | - |
| `package-management-02` | `recall` | `package-management` | `21855.84` | `0.967` | `1.000` | `0.937` | `1.000` | `0.950` | `0.833` | `accepted` | - | - | - |
| `ci-01` | `recall` | `ci` | `9899.08` | `0.967` | `1.000` | `0.867` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-03` | `recall` | `testing` | `368488.81` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-01` | `recall` | `deployment` | `10085.33` | `0.981` | `1.000` | `0.925` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-01` | `recall` | `infrastructure` | `456238.68` | `0.973` | `1.000` | `0.922` | `1.000` | `0.977` | `0.923` | `accepted` | - | - | - |
| `compilation-02` | `recall` | `compilation` | `350673.00` | `0.992` | `1.000` | `0.969` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-02` | `recall` | `ci` | `11228.00` | `0.975` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-01` | `recall` | `build` | `521459.01` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-01` | `recall` | `container-runtime` | `14994.09` | `0.982` | `1.000` | `0.929` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `compilation-03` | `recall` | `compilation` | `27828.75` | `0.978` | `1.000` | `0.912` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-02` | `recall` | `infrastructure` | `14927.59` | `0.968` | `1.000` | `0.871` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-03` | `recall` | `runtime` | `500977.51` | `0.991` | `1.000` | `0.962` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-03` | `recall` | `package-management` | `419264.26` | `0.969` | `1.000` | `0.876` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `infrastructure-03` | `recall` | `infrastructure` | `380143.74` | `0.966` | `1.000` | `0.865` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `testing-04` | `recall` | `testing` | `358693.99` | `0.979` | `1.000` | `0.915` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-02` | `recall` | `build` | `360361.54` | `0.982` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-03` | `recall` | `ci` | `559724.13` | `0.835` | `1.000` | `0.930` | `1.000` | `1.000` | `1.000` | `soft_accepted` | missing_exact_anchors | - | - |
| `testing-05` | `recall` | `testing` | `586171.50` | `0.980` | `1.000` | `0.921` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-03` | `summary` | `build` | `11512.61` | `0.961` | `1.000` | `0.903` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `docker-05` | `summary` | `docker` | `2775321.86` | `0.945` | `1.000` | `0.862` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-05` | `summary` | `kubernetes` | `7527.91` | `0.961` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-04` | `summary` | `ci` | `8305.32` | `0.952` | `1.000` | `0.880` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `npm-09` | `summary` | `npm` | `275444.73` | `0.916` | `1.000` | `0.941` | `1.000` | `0.880` | `0.600` | `accepted` | - | - | - |
| `rust-02` | `summary` | `rust` | `9644.05` | `0.943` | `1.000` | `0.857` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-01` | `instruction_following` | `linting` | `282689.02` | `0.565` | `1.000` | `0.884` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `testing-06` | `instruction_following` | `testing` | `14291.30` | `0.817` | `1.000` | `0.945` | `0.667` | `0.600` | `0.667` | `accepted` | - | - | - |
| `ci-05` | `instruction_following` | `ci` | `8759.45` | `0.688` | `1.000` | `0.628` | `0.500` | `0.500` | `1.000` | `accepted` | - | - | - |
| `linting-02` | `structured` | `linting` | `24617.37` | `0.468` | `1.000` | `0.562` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `kubernetes-06` | `structured` | `kubernetes` | `23713.03` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-02` | `structured` | `deployment` | `25674.30` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-01` | `exact_format` | `network` | `523306.83` | `0.300` | `1.000` | `0.998` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-02` | `exact_format` | `shell` | `437944.61` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-03` | `exact_format` | `shell` | `495058.47` | `0.252` | `1.000` | `0.765` | `0.000` | `0.000` | `0.500` | `accepted` | - | - | - |
| `shell-04` | `exact_format` | `shell` | `541625.29` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-04` | `exact_format` | `build` | `974524.78` | `0.249` | `1.000` | `0.485` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `build-05` | `exact_format` | `build` | `363977.11` | `0.233` | `1.000` | `0.333` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-05` | `exact_format` | `shell` | `506392.27` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-03` | `explanation` | `deployment` | `30122.77` | `0.936` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-04` | `explanation` | `runtime` | `31837.41` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `container-runtime-02` | `explanation` | `container-runtime` | `27815.98` | `0.936` | `1.000` | `0.871` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-05` | `explanation` | `runtime` | `565319.74` | `0.950` | `1.000` | `0.901` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-06` | `explanation` | `ci` | `560443.87` | `0.941` | `1.000` | `0.883` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `runtime-06` | `explanation` | `runtime` | `531462.49` | `0.931` | `1.000` | `0.863` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-04` | `explanation` | `deployment` | `19876.26` | `0.910` | `1.000` | `0.821` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-01` | `explanation` | `explanation` | `24453.38` | `0.934` | `1.000` | `0.867` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-02` | `explanation` | `explanation` | `16908.58` | `0.944` | `1.000` | `0.888` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-03` | `explanation` | `explanation` | `15181.56` | `0.944` | `1.000` | `0.887` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-04` | `explanation` | `explanation` | `11462.62` | `0.936` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-05` | `explanation` | `explanation` | `15622.92` | `0.947` | `1.000` | `0.894` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-06` | `explanation` | `explanation` | `11548.89` | `0.878` | `1.000` | `0.857` | `1.000` | `0.850` | `0.500` | `accepted` | - | - | - |
| `explanation-07` | `explanation` | `explanation` | `20803.88` | `0.940` | `1.000` | `0.880` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-08` | `explanation` | `explanation` | `349711.79` | `0.920` | `1.000` | `0.841` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-09` | `explanation` | `explanation` | `15772.81` | `0.950` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-10` | `explanation` | `explanation` | `19641.68` | `0.948` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-11` | `explanation` | `explanation` | `12099.71` | `0.916` | `1.000` | `0.833` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-12` | `explanation` | `explanation` | `11255.85` | `0.950` | `1.000` | `0.900` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `ci-07` | `structured` | `ci` | `21057.36` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `linting-03` | `structured` | `linting` | `10933.94` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `network-02` | `exact_format` | `network` | `270163.29` | `0.300` | `1.000` | `0.998` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-06` | `exact_format` | `shell` | `5913.49` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `shell-07` | `exact_format` | `shell` | `266919.46` | `0.700` | `1.000` | `0.335` | `0.667` | `0.667` | `1.000` | `accepted` | - | - | - |
| `build-06` | `exact_format` | `build` | `684168.13` | `0.249` | `1.000` | `0.485` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `runtime-07` | `exact_format` | `runtime` | `9929.41` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `build-07` | `exact_format` | `build` | `277746.06` | `0.232` | `1.000` | `0.319` | `0.000` | `0.000` | `1.000` | `accepted` | - | - | - |
| `shell-08` | `exact_format` | `shell` | `3408.35` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-05` | `explanation` | `deployment` | `14530.57` | `0.936` | `1.000` | `0.872` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-06` | `explanation` | `deployment` | `15606.50` | `0.921` | `1.000` | `0.843` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `deployment-07` | `explanation` | `deployment` | `8400.69` | `0.958` | `1.000` | `0.916` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-13` | `explanation` | `explanation` | `11700.58` | `0.919` | `1.000` | `0.838` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-14` | `explanation` | `explanation` | `11950.41` | `0.910` | `1.000` | `0.821` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-15` | `explanation` | `explanation` | `15558.92` | `0.963` | `1.000` | `0.927` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-16` | `explanation` | `explanation` | `270996.56` | `0.913` | `1.000` | `0.825` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `explanation-17` | `explanation` | `explanation` | `495377.50` | `0.961` | `1.000` | `0.923` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
| `package-management-04` | `explanation` | `package-management` | `17599.56` | `0.949` | `1.000` | `0.897` | `1.000` | `1.000` | `1.000` | `accepted` | - | - | - |
