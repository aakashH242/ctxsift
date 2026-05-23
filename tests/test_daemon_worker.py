"""Tests for the daemon worker entrypoint."""

from __future__ import annotations

import io
from pathlib import Path
from types import SimpleNamespace

import pytest

import ctxsift.daemon_worker as daemon_worker


def test_daemon_worker_reads_launch_file_as_path(monkeypatch) -> None:
    captured: dict[str, object] = {}

    class ParsedArgs:
        launch_file = "C:/tmp/ctxsift-launch.json"

    class FakeParser:
        def add_argument(self, *args, **kwargs) -> None:
            return None

        def parse_args(self):
            return ParsedArgs()

    monkeypatch.setattr(daemon_worker.argparse, "ArgumentParser", lambda **kwargs: FakeParser())

    def fake_read_launch_payload(path: Path):
        captured["path"] = path
        return SimpleNamespace(log_path="C:/tmp/ctxsift-daemon.log", payload=True)

    def fake_run_daemon(payload) -> None:
        captured["payload"] = payload

    monkeypatch.setattr(daemon_worker, "read_launch_payload", fake_read_launch_payload)
    monkeypatch.setattr(daemon_worker, "run_daemon", fake_run_daemon)

    daemon_worker.main()

    assert captured["path"] == Path("C:/tmp/ctxsift-launch.json")


def test_configure_windows_console_log_tee_mirrors_console_output(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    stdout_buffer = io.StringIO()
    stderr_buffer = io.StringIO()
    registrations: list[object] = []
    log_path = tmp_path / "daemon.log"

    monkeypatch.setattr(daemon_worker.os, "name", "nt")
    monkeypatch.setattr(daemon_worker.sys, "stdout", stdout_buffer)
    monkeypatch.setattr(daemon_worker.sys, "stderr", stderr_buffer)
    monkeypatch.setattr(
        daemon_worker.atexit, "register", lambda callback: registrations.append(callback)
    )

    daemon_worker._configure_windows_console_log_tee(log_path)

    print("daemon visible")
    print("do not close", file=daemon_worker.sys.stderr)
    daemon_worker.sys.stdout.flush()
    daemon_worker.sys.stderr.flush()

    assert stdout_buffer.getvalue() == "daemon visible\n"
    assert stderr_buffer.getvalue() == "do not close\n"
    assert "daemon visible\n" in log_path.read_text(encoding="utf-8")
    assert "do not close\n" in log_path.read_text(encoding="utf-8")
    assert len(registrations) == 1
