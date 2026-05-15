"""Tests for deterministic extraction."""

from pathlib import Path

from ctxsift.extraction import ExtractionContext, build_extracted_terms, extract_referenced_files, extract_signal


def test_extract_signal_finds_paths_tests_symbols_packages_and_commands(tmp_path: Path) -> None:
    workspace_root = tmp_path / "repo"
    cwd = workspace_root
    source_path = workspace_root / "src" / "auth.py"
    test_path = workspace_root / "tests" / "test_auth.py"
    source_path.parent.mkdir(parents=True)
    test_path.parent.mkdir(parents=True)
    source_path.write_text("raise AuthError\n", encoding="utf-8")
    test_path.write_text("def test_login():\n    assert False\n", encoding="utf-8")
    text = "\n".join(
        [
            'File "src/auth.py", line 9, in login',
            "tests/test_auth.py::test_login FAILED",
            "ModuleNotFoundError: No module named 'litellm'",
            "pytest exited with code 1",
            "AuthError: login failed",
            "warning: deprecated setting",
        ]
    )
    context = ExtractionContext(cwd=cwd, workspace_root=workspace_root)

    signal = extract_signal(text, context)
    terms = build_extracted_terms(signal)

    assert signal.matched_domains == ["python", "pytest"]
    assert signal.referenced_files == ["src/auth.py", "tests/test_auth.py"]
    assert signal.traceback_frames == ["src/auth.py:9 in login"]
    assert signal.tests == ["tests/test_auth.py::test_login"]
    assert "AuthError" in signal.symbols
    assert signal.packages == ["litellm"]
    assert signal.command_terms == ["python", "pytest"]
    assert signal.exit_code_lines == ["pytest exited with code 1"]
    assert signal.warning_lines == ["warning: deprecated setting"]
    assert "tests/test_auth.py::test_login FAILED" in signal.error_lines
    assert ("src/auth.py", "file") in {(term.term, term.kind) for term in terms}
    assert ("src/auth.py:9 in login", "traceback_frame") in {(term.term, term.kind) for term in terms}
    assert ("pytest", "command") in {(term.term, term.kind) for term in terms}


def test_extract_referenced_files_hashes_small_existing_files(tmp_path: Path) -> None:
    workspace_root = tmp_path / "repo"
    cwd = workspace_root / "work"
    cwd.mkdir(parents=True)
    source_path = workspace_root / "src" / "app.py"
    source_path.parent.mkdir(parents=True)
    source_path.write_text("print('hello')\n", encoding="utf-8")
    context = ExtractionContext(cwd=cwd, workspace_root=workspace_root)

    records = extract_referenced_files("src/app.py:12:4", context)

    assert len(records) == 1
    assert records[0].path == "src/app.py"
    assert records[0].exists_at_capture is True
    assert records[0].sha256 is not None


def test_extract_referenced_files_preserves_unresolved_paths(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)

    records = extract_referenced_files("missing/module.py:10", context)

    assert len(records) == 1
    assert records[0].path == "missing/module.py"
    assert records[0].exists_at_capture is False
    assert records[0].sha256 is None


def test_extract_signal_matches_typescript_and_eslint_domains(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)
    text = "\n".join(
        [
            "src/app.ts:4:7 - error TS2304: Cannot find name 'window'.",
            "src/app.ts",
            "  4:7  error  'window' is not defined  no-undef",
            "eslint",
        ]
    )

    signal = extract_signal(text, context)

    assert "typescript" in signal.matched_domains
    assert "eslint" in signal.matched_domains
    assert "no-undef" in signal.eslint_rules
    assert "tsc" in signal.command_terms
    assert any("TS2304" in line for line in signal.error_lines)


def test_extract_signal_matches_docker_domain(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)
    text = "\n".join(
        [
            "docker compose build api",
            "failed to solve: process \"/bin/sh -c pnpm build\" did not complete successfully: exit code: 2",
            "service api exited with code 2",
        ]
    )

    signal = extract_signal(text, context)

    assert "docker" in signal.matched_domains
    assert "docker compose build" in signal.command_terms
    assert "docker compose" in signal.command_terms
    assert any("failed to solve" in line for line in signal.error_lines)
    assert any("service api exited with code 2" in line for line in signal.error_lines)


def test_extract_signal_matches_kubernetes_domain(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)
    text = "\n".join(
        [
            "kubectl apply -f deploy.yaml",
            'error: resource mapping not found for name: "api" namespace: "" from "deploy.yaml": no matches for kind "Deployment" in version "apps/v2"',
        ]
    )

    signal = extract_signal(text, context)

    assert "kubernetes" in signal.matched_domains
    assert "kubectl" in signal.command_terms
    assert "kubectl apply" in signal.command_terms
    assert any("resource mapping not found" in line for line in signal.error_lines)


def test_extract_signal_matches_kubernetes_describe_warning_events(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)
    text = "\n".join(
        [
            "kubectl describe pod api-5f6b8d7c4d-9lmno",
            "Warning  FailedMount  25s (x4 over 2m)  kubelet  Unable to attach or mount volumes: unmounted volumes=[config], failed to sync secret cache",
            "Warning  BackOff  12s (x6 over 90s)  kubelet  Back-off restarting failed container",
        ]
    )

    signal = extract_signal(text, context)

    assert "kubernetes" in signal.matched_domains
    assert "kubectl describe" in signal.command_terms
    assert any("FailedMount" in line for line in signal.warning_lines)
    assert any("BackOff" in line for line in signal.warning_lines)


def test_extract_signal_falls_back_to_generic_when_no_domain_matches(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)
    text = "warning: generic issue in scripts/tool.sh\nexit code 2"

    signal = extract_signal(text, context)

    assert signal.matched_domains == ["generic"]
    assert signal.warning_lines == ["warning: generic issue in scripts/tool.sh"]
    assert signal.exit_code_lines == ["exit code 2"]


def test_extract_signal_matches_python_runtime_frames_and_causes(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)
    text = "\n".join(
        [
            "Traceback (most recent call last):",
            '  File "app.py", line 4, in <module>',
            '  File "lib/auth.py", line 9, in login',
            "ValueError: bad token",
            "During handling of the above exception, another exception occurred:",
            "RuntimeError: outer failure",
        ]
    )

    signal = extract_signal(text, context)

    assert "python" in signal.matched_domains
    assert "app.py:4 in <module>" in signal.traceback_frames
    assert "lib/auth.py:9 in login" in signal.traceback_frames
    assert "ValueError: bad token" in signal.error_lines
    assert "RuntimeError: outer failure" in signal.error_lines


def test_extract_signal_matches_ruff_domain(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)
    text = "src/app.py:4:7: F821 Undefined name `window`\nruff check failed"

    signal = extract_signal(text, context)

    assert "ruff" in signal.matched_domains
    assert "ruff" in signal.command_terms
    assert "src/app.py:4:7: F821 Undefined name `window`" in signal.error_lines


def test_extract_signal_matches_pylint_domain(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)
    text = "src/app.py:1:0: C0114: Missing module docstring (missing-module-docstring)\npylint src"

    signal = extract_signal(text, context)

    assert "pylint" in signal.matched_domains
    assert "pylint" in signal.command_terms
    assert "src/app.py:1:0: C0114: Missing module docstring (missing-module-docstring)" in signal.error_lines


def test_extract_signal_matches_black_domain(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)
    text = "would reformat src/app.py\nOh no! 1 file would be reformatted."

    signal = extract_signal(text, context)

    assert "black" in signal.matched_domains
    assert "black" in signal.command_terms
    assert "would reformat src/app.py" in signal.error_lines


def test_extract_signal_matches_mypy_domain(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)
    text = "src/app.py:8: error: Item \"None\" has no attribute \"id\"  [union-attr]\nmypy src"

    signal = extract_signal(text, context)

    assert "mypy" in signal.matched_domains
    assert "mypy" in signal.command_terms
    assert "src/app.py:8: error: Item \"None\" has no attribute \"id\"  [union-attr]" in signal.error_lines


def test_extract_signal_matches_npm_install_errors(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)
    text = "\n".join(
        [
            "npm ERR! code ERESOLVE",
            "npm ERR! ERESOLVE unable to resolve dependency tree",
            "npm ERR! While resolving: web@1.0.0",
        ]
    )

    signal = extract_signal(text, context)

    assert "node_package_manager" in signal.matched_domains
    assert "npm" in signal.command_terms
    assert any("ERESOLVE" in line for line in signal.error_lines)


def test_extract_signal_matches_pnpm_build_errors(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)
    text = "\n".join(
        [
            "> pnpm build",
            "ERR_PNPM_RECURSIVE_RUN_FIRST_FAIL Command failed with exit code 2.",
            "ELIFECYCLE Command failed with exit code 2.",
        ]
    )

    signal = extract_signal(text, context)

    assert "node_package_manager" in signal.matched_domains
    assert "pnpm" in signal.command_terms
    assert any("ERR_PNPM_RECURSIVE_RUN_FIRST_FAIL" in line for line in signal.error_lines)


def test_extract_signal_matches_tsc_compiler_output(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)
    text = "\n".join(
        [
            "src/server.ts(12,5): error TS2322: Type 'string' is not assignable to type 'number'.",
            "Found 1 error in src/server.ts:12",
        ]
    )

    signal = extract_signal(text, context)

    assert "typescript" in signal.matched_domains
    assert "tsc" in signal.command_terms
    assert any("TS2322" in line for line in signal.error_lines)


def test_extract_signal_matches_terraform_init_errors(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)
    text = "\n".join(
        [
            "terraform init",
            "Initializing the backend...",
            "Error: Failed to query available provider packages",
        ]
    )

    signal = extract_signal(text, context)

    assert "terraform" in signal.matched_domains
    assert "terraform init" in signal.command_terms
    assert any("Failed to query available provider packages" in line for line in signal.error_lines)


def test_extract_signal_matches_terraform_plan_errors(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)
    text = "\n".join(
        [
            "terraform plan",
            "Error: Unsupported argument",
            "  on main.tf line 12, in resource \"aws_s3_bucket\" \"logs\":",
            "  12:   bad_arg = true",
        ]
    )

    signal = extract_signal(text, context)

    assert "terraform" in signal.matched_domains
    assert "terraform plan" in signal.command_terms
    assert any("Unsupported argument" in line for line in signal.error_lines)
    assert any("main.tf line 12" in line for line in signal.error_lines)


def test_extract_signal_matches_terraform_apply_errors(tmp_path: Path) -> None:
    context = ExtractionContext(cwd=tmp_path, workspace_root=tmp_path)
    text = "\n".join(
        [
            "terraform apply",
            "│ Error: creating IAM Role: EntityAlreadyExists: Role with name app-role already exists",
            "│   with aws_iam_role.app_role,",
        ]
    )

    signal = extract_signal(text, context)

    assert "terraform" in signal.matched_domains
    assert "terraform apply" in signal.command_terms
    assert any("EntityAlreadyExists" in line for line in signal.error_lines)
    assert any("with aws_iam_role.app_role" in line for line in signal.error_lines)
