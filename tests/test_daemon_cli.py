"""CLI tests for daemon subcommands."""

from __future__ import annotations

from types import SimpleNamespace

import pytest
from typer.testing import CliRunner

import ctxsift.cli as cli
from ctxsift.cli import app
from ctxsift.daemon.types import DaemonRole, DaemonStatus
from ctxsift.types import AppConfig

runner = CliRunner()


@pytest.fixture(autouse=True)
def fake_resolved_config(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        cli,
        "resolve_config",
        lambda request: SimpleNamespace(config=AppConfig()),
    )


def test_daemon_start_renders_started_statuses(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        cli,
        "startup_statuses",
        lambda config: [
            DaemonStatus(
                role=DaemonRole.EMBEDDING,
                signature_hash="embed",
                model="emb",
                device="cpu",
                pid=101,
                port=4001,
                healthy=True,
                detail="started",
            ),
            DaemonStatus(
                role=DaemonRole.COMPRESSION,
                signature_hash="compress",
                model="comp",
                device="cpu",
                pid=102,
                port=4002,
                healthy=True,
                detail="already running",
            ),
            DaemonStatus(
                role=DaemonRole.COMPRESSION,
                signature_hash="old-compress",
                model="old-comp",
                device="cpu",
                pid=99,
                port=3999,
                healthy=False,
                detail="superseded by current config (comp cpu)",
            ),
        ],
    )

    result = runner.invoke(app, ["daemon", "start"])

    assert result.exit_code == 0
    assert "embedding healthy model=emb" in result.stdout
    assert "compression healthy model=comp" in result.stdout
    assert "old-comp" in result.stdout
    assert "superseded by current config" in result.stdout


def test_daemon_stop_all_uses_global_stop_path(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        cli,
        "stop_all_daemons",
        lambda: [
            DaemonStatus(
                role=DaemonRole.EMBEDDING,
                signature_hash="embed",
                model="emb",
                device="cpu",
                healthy=False,
                detail="stopped",
            )
        ],
    )

    result = runner.invoke(app, ["daemon", "stop", "--all"])

    assert result.exit_code == 0
    assert "embedding inactive model=emb" in result.stdout
    assert "detail=stopped" in result.stdout


def test_daemon_status_all_uses_registry_view(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        cli,
        "daemon_statuses",
        lambda config, include_all=False: [
            DaemonStatus(
                role=DaemonRole.COMPRESSION,
                signature_hash="compress",
                model="comp",
                device="cuda",
                pid=303,
                port=5050,
                healthy=True,
                detail="running",
            )
        ],
    )

    result = runner.invoke(app, ["daemon", "status", "--all"])

    assert result.exit_code == 0
    assert "compression healthy model=comp device=cuda" in result.stdout
