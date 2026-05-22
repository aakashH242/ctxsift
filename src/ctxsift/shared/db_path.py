"""Database path resolution shared across compression and recall."""

from __future__ import annotations

from pathlib import Path


def resolved_db_path(
    workspace_db_path: str | None,
    config_db_path: str | None,
) -> Path:
    """Resolve the effective database path from workspace and config sources."""
    selected = config_db_path or workspace_db_path
    if not selected:
        raise ValueError("Could not resolve a ctxsift database path.")
    return Path(selected).expanduser()
