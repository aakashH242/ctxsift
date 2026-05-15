"""Tests for recall search and freshness validation."""

import asyncio
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from pathlib import Path

from ctxsift.file_fingerprint import sha256_if_reasonable
from ctxsift.recall_hybrid import HybridRecallRequest, build_hybrid_records
from ctxsift.recall import recall_records
from ctxsift.recall_freshness import assess_record_freshness
from ctxsift.storage import initialize_database, insert_record_bundle
from ctxsift.types import (
    ExtractedTermRecord,
    FreshnessStatus,
    RecallStorageRecord,
    ReferencedFileRecord,
    StoredRecord,
    VectorSearchHit,
)


def test_recall_records_searches_instruction_command_files_and_terms(tmp_path: Path) -> None:
    repo_path = tmp_path / "repo"
    git_dir = repo_path / ".git"
    git_dir.mkdir(parents=True)
    db_path = git_dir / "ctxsift" / "ctxsift.db"
    target_file = repo_path / "src" / "auth.py"
    target_file.parent.mkdir(parents=True)
    target_file.write_text("raise AuthError\n", encoding="utf-8")
    asyncio.run(initialize_database(db_path))
    asyncio.run(
        insert_record_bundle(
            db_path,
            StoredRecord(
                instruction="summarize auth failures",
                normalized_instruction="summarize auth failures",
                compressed_output="AuthError in src/auth.py",
                raw_input_hash="hash-1",
                mode="run",
                workspace_root=str(repo_path),
                cwd=str(repo_path),
                command="pytest tests/test_auth.py -q",
            ),
            referenced_files=[
                ReferencedFileRecord(
                    path="src/auth.py",
                    abs_path=str(target_file),
                    sha256="badhash",
                    exists_at_capture=True,
                )
            ],
            extracted_terms=[
                ExtractedTermRecord(term="AuthError", kind="symbol"),
            ],
        )
    )

    results = asyncio.run(recall_records("AuthError", repo_path))
    file_results = asyncio.run(recall_records("auth.py", repo_path))
    instruction_results = asyncio.run(recall_records("auth failures", repo_path))
    command_results = asyncio.run(recall_records("pytest", repo_path))

    assert len(results) == 1
    assert results[0].record_id == 1
    assert "compressed_output" in results[0].matched_fields
    assert "extracted_terms" in results[0].matched_fields
    assert len(file_results) == 1
    assert "file_paths" in file_results[0].matched_fields
    assert len(instruction_results) == 1
    assert "instruction" in instruction_results[0].matched_fields
    assert len(command_results) == 1
    assert "command" in command_results[0].matched_fields


def test_recall_records_filters_by_files(tmp_path: Path) -> None:
    repo_path = tmp_path / "repo"
    git_dir = repo_path / ".git"
    git_dir.mkdir(parents=True)
    db_path = git_dir / "ctxsift" / "ctxsift.db"
    first_file = repo_path / "src" / "auth.py"
    second_file = repo_path / "src" / "billing.py"
    first_file.parent.mkdir(parents=True)
    first_file.write_text("raise AuthError\n", encoding="utf-8")
    second_file.write_text("raise BillingError\n", encoding="utf-8")
    asyncio.run(initialize_database(db_path))
    asyncio.run(
        insert_record_bundle(
            db_path,
            StoredRecord(
                instruction="summarize auth failures",
                normalized_instruction="summarize auth failures",
                compressed_output="AuthError in src/auth.py",
                raw_input_hash="hash-1",
                mode="pipe",
                workspace_root=str(repo_path),
                cwd=str(repo_path),
            ),
            referenced_files=[
                ReferencedFileRecord(
                    path="src/auth.py",
                    abs_path=str(first_file),
                    sha256=None,
                    exists_at_capture=True,
                )
            ],
        )
    )
    asyncio.run(
        insert_record_bundle(
            db_path,
            StoredRecord(
                instruction="summarize billing failures",
                normalized_instruction="summarize billing failures",
                compressed_output="BillingError in src/billing.py",
                raw_input_hash="hash-2",
                mode="pipe",
                workspace_root=str(repo_path),
                cwd=str(repo_path),
            ),
            referenced_files=[
                ReferencedFileRecord(
                    path="src/billing.py",
                    abs_path=str(second_file),
                    sha256=None,
                    exists_at_capture=True,
                )
            ],
        )
    )

    results = asyncio.run(recall_records("error", repo_path, file_filters=["src/auth.py"]))

    assert len(results) == 1
    assert results[0].referenced_files == ["src/auth.py"]


def test_recall_records_prioritize_multi_signal_matches(tmp_path: Path) -> None:
    repo_path = tmp_path / "repo"
    git_dir = repo_path / ".git"
    git_dir.mkdir(parents=True)
    db_path = git_dir / "ctxsift" / "ctxsift.db"
    auth_file = repo_path / "src" / "auth.py"
    notes_file = repo_path / "notes" / "auth.txt"
    auth_file.parent.mkdir(parents=True)
    notes_file.parent.mkdir(parents=True)
    auth_file.write_text("raise AuthError\n", encoding="utf-8")
    notes_file.write_text("auth notes\n", encoding="utf-8")
    asyncio.run(initialize_database(db_path))
    asyncio.run(
        insert_record_bundle(
            db_path,
            StoredRecord(
                instruction="fix AuthError in src/auth.py",
                normalized_instruction="fix autherror in src/auth.py",
                compressed_output="AuthError in src/auth.py after pytest failed",
                raw_input_hash="hash-1",
                mode="run",
                workspace_root=str(repo_path),
                cwd=str(repo_path),
                command="pytest tests/test_auth.py -q",
            ),
            referenced_files=[
                ReferencedFileRecord(
                    path="src/auth.py",
                    abs_path=str(auth_file),
                    sha256=sha256_if_reasonable(auth_file),
                    exists_at_capture=True,
                )
            ],
            extracted_terms=[ExtractedTermRecord(term="AuthError", kind="symbol")],
        )
    )
    asyncio.run(
        insert_record_bundle(
            db_path,
            StoredRecord(
                instruction="notes about auth",
                normalized_instruction="notes about auth",
                compressed_output="misc auth context",
                raw_input_hash="hash-2",
                mode="pipe",
                workspace_root=str(repo_path),
                cwd=str(repo_path),
                command="cat notes/auth.txt",
            ),
            referenced_files=[
                ReferencedFileRecord(
                    path="notes/auth.txt",
                    abs_path=str(notes_file),
                    sha256=sha256_if_reasonable(notes_file),
                    exists_at_capture=True,
                )
            ],
            extracted_terms=[ExtractedTermRecord(term="auth", kind="symbol")],
        )
    )

    results = asyncio.run(recall_records("AuthError src/auth.py pytest", repo_path))

    assert len(results) == 2
    assert results[0].record_id == 1
    assert "instruction" in results[0].matched_fields
    assert "compressed_output" in results[0].matched_fields
    assert "command" in results[0].matched_fields
    assert "file_paths" in results[0].matched_fields
    assert "extracted_terms" in results[0].matched_fields
    assert results[0].score > results[1].score


def test_recall_records_include_vector_only_candidates(
    tmp_path: Path,
    monkeypatch,
) -> None:
    import ctxsift.recall as recall_module

    repo_path = tmp_path / "repo"
    git_dir = repo_path / ".git"
    git_dir.mkdir(parents=True)
    db_path = git_dir / "ctxsift" / "ctxsift.db"
    target_file = repo_path / "src" / "vector_only.py"
    target_file.parent.mkdir(parents=True)
    target_file.write_text("raise VectorError\n", encoding="utf-8")
    asyncio.run(initialize_database(db_path))
    asyncio.run(
        insert_record_bundle(
            db_path,
            StoredRecord(
                instruction="investigate vector recall issue",
                normalized_instruction="investigate vector recall issue",
                compressed_output="VectorError in src/vector_only.py",
                raw_input_hash="hash-vector",
                mode="pipe",
                workspace_root=str(repo_path),
                cwd=str(repo_path),
            ),
            referenced_files=[
                ReferencedFileRecord(
                    path="src/vector_only.py",
                    abs_path=str(target_file),
                    sha256=sha256_if_reasonable(target_file),
                    exists_at_capture=True,
                )
            ],
            extracted_terms=[ExtractedTermRecord(term="VectorError", kind="symbol")],
        )
    )

    async def fake_vector_hits(*args, **kwargs):
        return [VectorSearchHit(record_id=1, distance=0.01)]

    monkeypatch.setattr(recall_module, "_vector_hits", fake_vector_hits)

    results = asyncio.run(recall_records("semantic-only query", repo_path))

    assert len(results) == 1
    assert results[0].record_id == 1
    assert "vector" in results[0].matched_fields


def test_recall_records_drop_weak_vector_only_candidates(
    tmp_path: Path,
    monkeypatch,
) -> None:
    import ctxsift.recall as recall_module

    repo_path = tmp_path / "repo"
    git_dir = repo_path / ".git"
    git_dir.mkdir(parents=True)
    db_path = git_dir / "ctxsift" / "ctxsift.db"
    target_file = repo_path / "src" / "vector_only.py"
    target_file.parent.mkdir(parents=True)
    target_file.write_text("raise VectorError\n", encoding="utf-8")
    asyncio.run(initialize_database(db_path))
    asyncio.run(
        insert_record_bundle(
            db_path,
            StoredRecord(
                instruction="investigate vector recall issue",
                normalized_instruction="investigate vector recall issue",
                compressed_output="VectorError in src/vector_only.py",
                raw_input_hash="hash-vector",
                mode="pipe",
                workspace_root=str(repo_path),
                cwd=str(repo_path),
            ),
            referenced_files=[
                ReferencedFileRecord(
                    path="src/vector_only.py",
                    abs_path=str(target_file),
                    sha256=sha256_if_reasonable(target_file),
                    exists_at_capture=True,
                )
            ],
            extracted_terms=[ExtractedTermRecord(term="VectorError", kind="symbol")],
        )
    )

    async def fake_vector_hits(*args, **kwargs):
        return [VectorSearchHit(record_id=1, distance=1.2)]

    monkeypatch.setattr(recall_module, "_vector_hits", fake_vector_hits)

    results = asyncio.run(recall_records("semantic-only query", repo_path))

    assert results == []


def test_recall_records_apply_file_filters_after_retrieval(
    tmp_path: Path,
    monkeypatch,
) -> None:
    import ctxsift.recall as recall_module

    repo_path = tmp_path / "repo"
    git_dir = repo_path / ".git"
    git_dir.mkdir(parents=True)
    db_path = git_dir / "ctxsift" / "ctxsift.db"
    auth_file = repo_path / "src" / "auth.py"
    billing_file = repo_path / "src" / "billing.py"
    auth_file.parent.mkdir(parents=True)
    auth_file.write_text("raise AuthError\n", encoding="utf-8")
    billing_file.write_text("raise BillingError\n", encoding="utf-8")
    asyncio.run(initialize_database(db_path))
    for instruction, summary, source_file, raw_hash in [
        ("auth issue", "AuthError in src/auth.py", auth_file, "hash-auth"),
        ("billing issue", "BillingError in src/billing.py", billing_file, "hash-billing"),
    ]:
        asyncio.run(
            insert_record_bundle(
                db_path,
                StoredRecord(
                    instruction=instruction,
                    normalized_instruction=instruction,
                    compressed_output=summary,
                    raw_input_hash=raw_hash,
                    mode="pipe",
                    workspace_root=str(repo_path),
                    cwd=str(repo_path),
                ),
                referenced_files=[
                    ReferencedFileRecord(
                        path=source_file.relative_to(repo_path).as_posix(),
                        abs_path=str(source_file),
                        sha256=sha256_if_reasonable(source_file),
                        exists_at_capture=True,
                    )
                ],
            )
        )

    async def fake_vector_hits(*args, **kwargs):
        return [
            VectorSearchHit(record_id=1, distance=0.02),
            VectorSearchHit(record_id=2, distance=0.01),
        ]

    monkeypatch.setattr(recall_module, "_vector_hits", fake_vector_hits)

    results = asyncio.run(recall_records("broad issue", repo_path, file_filters=["src/auth.py"]))

    assert len(results) == 1
    assert results[0].record_id == 1


def test_hybrid_recall_boosts_exact_symbol_test_and_file_hits(tmp_path: Path) -> None:
    first_file = tmp_path / "tests" / "test_auth.py"
    second_file = tmp_path / "notes" / "auth.txt"
    first_file.parent.mkdir(parents=True)
    second_file.parent.mkdir(parents=True)
    first_file.write_text("def test_login(): pass\n", encoding="utf-8")
    second_file.write_text("auth notes\n", encoding="utf-8")

    primary = RecallStorageRecord(
        record_id=1,
        created_at="2026-05-15 00:00:00",
        workspace_root=str(tmp_path),
        instruction="fix tests/test_auth.py::test_login AuthError",
        compressed_output="AuthError in tests/test_auth.py::test_login",
        command=None,
        command_exit_code=None,
        referenced_files=[
            ReferencedFileRecord(
                path="tests/test_auth.py",
                abs_path=str(first_file),
                sha256=sha256_if_reasonable(first_file),
                exists_at_capture=True,
            )
        ],
        extracted_terms=[
            ExtractedTermRecord(term="AuthError", kind="symbol"),
            ExtractedTermRecord(term="tests/test_auth.py::test_login", kind="test"),
        ],
        matched_fields=["instruction", "compressed_output", "extracted_terms"],
        score=100,
    )
    secondary = RecallStorageRecord(
        record_id=2,
        created_at="2026-05-15 00:00:01",
        workspace_root=str(tmp_path),
        instruction="auth notes",
        compressed_output="general auth context",
        command=None,
        command_exit_code=None,
        referenced_files=[
            ReferencedFileRecord(
                path="notes/auth.txt",
                abs_path=str(second_file),
                sha256=sha256_if_reasonable(second_file),
                exists_at_capture=True,
            )
        ],
        extracted_terms=[ExtractedTermRecord(term="auth", kind="symbol")],
        matched_fields=["instruction", "compressed_output"],
        score=101,
    )

    results = build_hybrid_records(
        HybridRecallRequest(
            lexical_records=[primary, secondary],
            all_records=[primary, secondary],
            vector_hits=[],
            freshness_by_record_id={
                1: FreshnessStatus.FRESH,
                2: FreshnessStatus.FRESH,
            },
            file_filters=[],
            limit=10,
            normalized_query="autherror",
            search_terms=["autherror", "tests/test_auth.py::test_login"],
            max_vector_distance=0.75,
        )
    )

    assert len(results) == 2
    assert results[0].record_id == 1
    assert results[0].score > results[1].score


def test_assess_record_freshness_labels_expected_states(tmp_path: Path) -> None:
    existing_file = tmp_path / "existing.py"
    existing_file.write_text("print('hello')\n", encoding="utf-8")
    changed_file = tmp_path / "changed.py"
    changed_file.write_text("before\n", encoding="utf-8")
    deleted_file = tmp_path / "deleted.py"
    deleted_file.write_text("gone\n", encoding="utf-8")
    deleted_file.unlink()

    fresh_record = RecallStorageRecord(
        record_id=1,
        created_at="2026-05-15 00:00:00",
        workspace_root=str(tmp_path),
        instruction="fresh",
        compressed_output="fresh",
        command=None,
        command_exit_code=None,
        referenced_files=[
            ReferencedFileRecord(
                path="existing.py",
                abs_path=str(existing_file),
                sha256=sha256_if_reasonable(existing_file),
                exists_at_capture=True,
            )
        ],
        extracted_terms=[],
        matched_fields=[],
        score=1,
    )
    changed_record = RecallStorageRecord(
        record_id=2,
        created_at="2026-05-15 00:00:00",
        workspace_root=str(tmp_path),
        instruction="changed",
        compressed_output="changed",
        command=None,
        command_exit_code=None,
        referenced_files=[
            ReferencedFileRecord(
                path="changed.py",
                abs_path=str(changed_file),
                sha256="deadbeef",
                exists_at_capture=True,
            )
        ],
        extracted_terms=[],
        matched_fields=[],
        score=1,
    )
    deleted_record = RecallStorageRecord(
        record_id=3,
        created_at="2026-05-15 00:00:00",
        workspace_root=str(tmp_path),
        instruction="deleted",
        compressed_output="deleted",
        command=None,
        command_exit_code=None,
        referenced_files=[
            ReferencedFileRecord(
                path="deleted.py",
                abs_path=str(deleted_file),
                sha256="deadbeef",
                exists_at_capture=True,
            )
        ],
        extracted_terms=[],
        matched_fields=[],
        score=1,
    )
    unverifiable_record = RecallStorageRecord(
        record_id=4,
        created_at="2026-05-15 00:00:00",
        workspace_root=str(tmp_path),
        instruction="unverifiable",
        compressed_output="unverifiable",
        command=None,
        command_exit_code=None,
        referenced_files=[],
        extracted_terms=[],
        matched_fields=[],
        score=1,
    )
    unknown_record = RecallStorageRecord(
        record_id=5,
        created_at="2026-05-15 00:00:00",
        workspace_root=str(tmp_path),
        instruction="unknown",
        compressed_output="unknown",
        command=None,
        command_exit_code=None,
        referenced_files=[
            ReferencedFileRecord(
                path="missing.py",
                abs_path=None,
                sha256=None,
                exists_at_capture=False,
            )
        ],
        extracted_terms=[],
        matched_fields=[],
        score=1,
    )

    assert asyncio.run(assess_record_freshness(fresh_record)) is FreshnessStatus.FRESH
    assert asyncio.run(assess_record_freshness(changed_record)) is FreshnessStatus.STALE_CHANGED
    assert asyncio.run(assess_record_freshness(deleted_record)) is FreshnessStatus.STALE_DELETED
    assert asyncio.run(assess_record_freshness(unverifiable_record)) is FreshnessStatus.UNVERIFIABLE
    assert asyncio.run(assess_record_freshness(unknown_record)) is FreshnessStatus.UNKNOWN


def test_assess_record_freshness_uses_mtime_when_hash_missing(tmp_path: Path) -> None:
    target_file = tmp_path / "mtime.py"
    target_file.write_text("before\n", encoding="utf-8")
    created_at = datetime.now(timezone.utc) - timedelta(minutes=5)
    target_file.touch()

    record = RecallStorageRecord(
        record_id=1,
        created_at=created_at.strftime("%Y-%m-%d %H:%M:%S"),
        workspace_root=str(tmp_path),
        instruction="mtime",
        compressed_output="mtime",
        command=None,
        command_exit_code=None,
        referenced_files=[
            ReferencedFileRecord(
                path="mtime.py",
                abs_path=str(target_file),
                sha256=None,
                exists_at_capture=True,
            )
        ],
        extracted_terms=[],
    )

    assert asyncio.run(assess_record_freshness(record)) is FreshnessStatus.STALE_CHANGED


def test_assess_record_freshness_uses_git_status_when_available(tmp_path: Path, monkeypatch) -> None:
    from ctxsift.git_file_status import GitFileStatus
    import ctxsift.recall_freshness as recall_freshness

    target_file = tmp_path / "git.py"
    target_file.write_text("same\n", encoding="utf-8")
    record = RecallStorageRecord(
        record_id=1,
        created_at="2026-05-15 00:00:00",
        workspace_root=str(tmp_path),
        instruction="git-status",
        compressed_output="git-status",
        command=None,
        command_exit_code=None,
        referenced_files=[
            ReferencedFileRecord(
                path="git.py",
                abs_path=str(target_file),
                sha256=sha256_if_reasonable(target_file),
                exists_at_capture=True,
            )
        ],
        extracted_terms=[],
    )

    async def fake_read_git_file_status(*args, **kwargs) -> GitFileStatus:
        return GitFileStatus(path="git.py", is_changed=True, raw_status=" M")

    monkeypatch.setattr(recall_freshness, "read_git_file_status", fake_read_git_file_status)

    assert asyncio.run(assess_record_freshness(record)) is FreshnessStatus.STALE_CHANGED
