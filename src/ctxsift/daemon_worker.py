"""Background worker entrypoint for ctxsift daemons."""

from __future__ import annotations

import argparse

from ctxsift.daemon.registry import read_launch_payload
from ctxsift.daemon.server import run_daemon


def main() -> None:
    """Read one launch payload and serve the requested daemon."""
    parser = argparse.ArgumentParser(description="Run one ctxsift background daemon.")
    parser.add_argument("--launch-file", required=True, help="Path to the daemon launch payload.")
    args = parser.parse_args()
    payload = read_launch_payload(args.launch_file)
    run_daemon(payload)


if __name__ == "__main__":
    main()
