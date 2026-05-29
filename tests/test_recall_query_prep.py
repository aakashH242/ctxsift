"""Tests for recall vector query preparation helpers."""

from pathlib import Path

import ctxsift.recall.query_prep as query_prep
from ctxsift.types import ExtractedSignal


def _verbose_query() -> str:
    return (
        "Please help me figure out why the login flow started failing after the refactor "
        "and make the recall query more precise for later debugging. "
        "I need enough context to find the exact prior fix quickly."
    )


def test_prepare_vector_recall_query_prefers_strong_anchors_over_commands(
    monkeypatch,
) -> None:
    signal = ExtractedSignal(
        symbols=["AuthError"],
        tests=["tests/test_auth.py::test_login"],
        referenced_files=["src/auth.py"],
        command_terms=["git status", "docker compose up -d"],
    )
    monkeypatch.setattr(query_prep, "extract_signal", lambda *_args, **_kwargs: signal)

    prepared = query_prep.prepare_vector_recall_query(
        _verbose_query(),
        cwd=Path("."),
        workspace_root=Path("."),
        anchor_term_limit=3,
    )

    assert "AuthError" in prepared
    assert "tests/test_auth.py::test_login" in prepared
    assert "src/auth.py" in prepared
    assert "git status" not in prepared
    assert "docker compose" not in prepared


def test_prepare_vector_recall_query_uses_command_fallback_when_strong_missing(
    monkeypatch,
) -> None:
    signal = ExtractedSignal(
        symbols=["AuthError"],
        command_terms=["python -m pytest tests/test_auth.py -q", "docker compose up -d"],
    )
    monkeypatch.setattr(query_prep, "extract_signal", lambda *_args, **_kwargs: signal)

    prepared = query_prep.prepare_vector_recall_query(
        _verbose_query(),
        cwd=Path("."),
        workspace_root=Path("."),
        anchor_term_limit=3,
    )

    assert "AuthError" in prepared
    assert "python -m pytest" in prepared
    assert "docker compose" in prepared


def test_prepare_vector_recall_query_parses_quoted_python_module_command(monkeypatch) -> None:
    signal = ExtractedSignal(
        command_terms=['python -m pytest "tests/test auth.py::test_login" -q'],
    )
    monkeypatch.setattr(query_prep, "extract_signal", lambda *_args, **_kwargs: signal)

    prepared = query_prep.prepare_vector_recall_query(
        _verbose_query(),
        cwd=Path("."),
        workspace_root=Path("."),
        anchor_term_limit=2,
    )

    assert "python -m pytest" in prepared


def test_prepare_vector_recall_query_skips_noisy_command_fallback_without_command_hint(
    monkeypatch,
) -> None:
    signal = ExtractedSignal(
        symbols=["AuthError"],
        command_terms=[],
        error_lines=["docker compose up fails in CI after branch switch"],
    )
    monkeypatch.setattr(query_prep, "extract_signal", lambda *_args, **_kwargs: signal)

    prepared = query_prep.prepare_vector_recall_query(
        _verbose_query(),
        cwd=Path("."),
        workspace_root=Path("."),
        anchor_term_limit=3,
    )

    assert "AuthError" in prepared
    assert "docker compose" not in prepared


def test_prepare_vector_recall_query_allows_noisy_command_fallback_with_command_hint(
    monkeypatch,
) -> None:
    signal = ExtractedSignal(
        symbols=["AuthError"],
        command_terms=["pytest -q"],
        error_lines=["docker compose up fails in CI after branch switch"],
    )
    monkeypatch.setattr(query_prep, "extract_signal", lambda *_args, **_kwargs: signal)

    prepared = query_prep.prepare_vector_recall_query(
        _verbose_query(),
        cwd=Path("."),
        workspace_root=Path("."),
        anchor_term_limit=3,
    )

    assert "AuthError" in prepared
    assert "docker compose" in prepared


def test_prepare_vector_recall_query_returns_summary_when_anchors_already_present(
    monkeypatch,
) -> None:
    query = (
        "Please help me debug AuthError in src/auth.py. "
        "I need a very detailed recap of all possible causes and side effects after the refactor."
    )
    signal = ExtractedSignal(
        symbols=["AuthError"],
        referenced_files=["src/auth.py"],
    )
    monkeypatch.setattr(query_prep, "extract_signal", lambda *_args, **_kwargs: signal)

    prepared = query_prep.prepare_vector_recall_query(
        query,
        cwd=Path("."),
        workspace_root=Path("."),
        anchor_term_limit=3,
    )

    assert prepared == "help me debug AuthError in src/auth.py"
