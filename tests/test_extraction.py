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

    assert signal.referenced_files == ["src/auth.py", "tests/test_auth.py"]
    assert signal.tests == ["tests/test_auth.py::test_login"]
    assert "AuthError" in signal.symbols
    assert signal.packages == ["litellm"]
    assert signal.command_terms == ["pytest"]
    assert signal.exit_code_lines == ["pytest exited with code 1"]
    assert signal.warning_lines == ["warning: deprecated setting"]
    assert signal.error_lines[0] == "tests/test_auth.py::test_login FAILED"
    assert ("src/auth.py", "file") in {(term.term, term.kind) for term in terms}
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
