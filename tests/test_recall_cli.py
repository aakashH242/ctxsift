"""CLI tests for recall output and file filtering."""

from pathlib import Path

from typer.testing import CliRunner

from ctxsift.cli import app
from ctxsift.file_fingerprint import sha256_if_reasonable
from ctxsift.storage import initialize_database, insert_record_bundle
from ctxsift.types import ExtractedTermRecord, ReferencedFileRecord, StoredRecord


runner = CliRunner()


def test_recall_command_renders_results_and_freshness(tmp_path: Path, monkeypatch) -> None:
    repo_path = tmp_path / "repo"
    git_dir = repo_path / ".git"
    git_dir.mkdir(parents=True)
    source_file = repo_path / "src" / "auth.py"
    source_file.parent.mkdir(parents=True)
    source_file.write_text("raise AuthError\n", encoding="utf-8")
    db_path = git_dir / "ctxsift" / "ctxsift.db"
    _insert_recall_record(
        db_path=db_path,
        repo_path=repo_path,
        source_file=source_file,
    )
    monkeypatch.chdir(repo_path)

    result = runner.invoke(app, ["recall", "AuthError"])

    assert result.exit_code == 0
    assert "[1] fresh" in result.stdout
    assert "Instruction: summarize auth failures" in result.stdout
    assert "Files: src/auth.py" in result.stdout


def test_recall_command_filters_with_files_option(tmp_path: Path, monkeypatch) -> None:
    repo_path = tmp_path / "repo"
    git_dir = repo_path / ".git"
    git_dir.mkdir(parents=True)
    first_file = repo_path / "src" / "auth.py"
    second_file = repo_path / "src" / "billing.py"
    first_file.parent.mkdir(parents=True)
    first_file.write_text("raise AuthError\n", encoding="utf-8")
    second_file.write_text("raise BillingError\n", encoding="utf-8")
    db_path = git_dir / "ctxsift" / "ctxsift.db"
    _insert_recall_record(
        db_path=db_path,
        repo_path=repo_path,
        source_file=first_file,
    )
    _insert_billing_record(
        db_path=db_path,
        repo_path=repo_path,
        source_file=second_file,
    )
    monkeypatch.chdir(repo_path)

    result = runner.invoke(app, ["recall", "error", "--files", "src/auth.py"])

    assert result.exit_code == 0
    assert "src/auth.py" in result.stdout
    assert "src/billing.py" not in result.stdout


def _insert_recall_record(db_path: Path, repo_path: Path, source_file: Path) -> None:
    _ensure_db(db_path)
    _insert_record(
        db_path=db_path,
        record=StoredRecord(
            instruction="summarize auth failures",
            normalized_instruction="summarize auth failures",
            compressed_output="AuthError in src/auth.py",
            raw_input_hash="hash-auth",
            mode="run",
            workspace_root=str(repo_path),
            cwd=str(repo_path),
            command="pytest tests/test_auth.py -q",
        ),
        source_file=source_file,
        term="AuthError",
    )


def _insert_billing_record(db_path: Path, repo_path: Path, source_file: Path) -> None:
    _ensure_db(db_path)
    _insert_record(
        db_path=db_path,
        record=StoredRecord(
            instruction="summarize billing failures",
            normalized_instruction="summarize billing failures",
            compressed_output="BillingError in src/billing.py",
            raw_input_hash="hash-billing",
            mode="pipe",
            workspace_root=str(repo_path),
            cwd=str(repo_path),
            command="pytest tests/test_billing.py -q",
        ),
        source_file=source_file,
        term="BillingError",
    )


def _ensure_db(db_path: Path) -> None:
    if db_path.exists():
        return
    import asyncio

    asyncio.run(initialize_database(db_path))


def _insert_record(db_path: Path, record: StoredRecord, source_file: Path, term: str) -> None:
    import asyncio

    workspace_root = record.workspace_root
    assert workspace_root is not None

    asyncio.run(
        insert_record_bundle(
            db_path,
            record,
            referenced_files=[
                ReferencedFileRecord(
                    path=source_file.relative_to(Path(workspace_root)).as_posix(),
                    abs_path=str(source_file),
                    sha256=sha256_if_reasonable(source_file),
                    exists_at_capture=True,
                )
            ],
            extracted_terms=[
                ExtractedTermRecord(term=term, kind="symbol"),
            ],
        )
    )
