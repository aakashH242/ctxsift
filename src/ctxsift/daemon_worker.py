"""Background worker entrypoint for ctxsift daemons."""

from __future__ import annotations

import argparse
import atexit
import os
from pathlib import Path
import sys
from typing import TextIO

from ctxsift.daemon.registry import read_launch_payload
from ctxsift.daemon.server import run_daemon


class _TeeTextStream:
    """Mirror daemon output to both the Windows console and the daemon log file."""

    def __init__(self, primary: TextIO, mirror: TextIO) -> None:
        self._primary = primary
        self._mirror = mirror

    @property
    def encoding(self) -> str:
        return getattr(self._primary, "encoding", "utf-8")

    @property
    def errors(self) -> str:
        return getattr(self._primary, "errors", "strict")

    def write(self, text: str) -> int:
        self._primary.write(text)
        self._mirror.write(text)
        return len(text)

    def flush(self) -> None:
        self._primary.flush()
        self._mirror.flush()

    def isatty(self) -> bool:
        return bool(getattr(self._primary, "isatty", lambda: False)())

    def fileno(self) -> int:
        return self._primary.fileno()

    def __getattr__(self, name: str):
        return getattr(self._primary, name)


def _configure_windows_console_log_tee(log_path: Path) -> None:
    if os.name != "nt":
        return
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_handle = log_path.open("a", encoding="utf-8", buffering=1)
    atexit.register(log_handle.close)
    sys.stdout = _TeeTextStream(sys.stdout, log_handle)
    sys.stderr = _TeeTextStream(sys.stderr, log_handle)


def main() -> None:
    """Read one launch payload and serve the requested daemon."""
    parser = argparse.ArgumentParser(description="Run one ctxsift background daemon.")
    parser.add_argument("--launch-file", required=True, help="Path to the daemon launch payload.")
    args = parser.parse_args()
    payload = read_launch_payload(Path(args.launch_file))
    _configure_windows_console_log_tee(Path(payload.log_path))
    run_daemon(payload)


if __name__ == "__main__":
    main()
