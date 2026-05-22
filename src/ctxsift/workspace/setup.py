"""Workspace bootstrap helpers shared by CLI commands."""

from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path

from ctxsift.config.store import ENVIRONMENT_KEY_MAP, discover_global_config_paths
from ctxsift.storage import initialize_database
from ctxsift.types import AppConfig
from ctxsift.workspace.discovery import detect_workspace_context
from ctxsift.workspace.ignore import ensure_workspace_ignore_entry, requires_workspace_ignore_entry


@dataclass(frozen=True)
class WorkspaceSetupResult:
    """Workspace bootstrap result."""

    db_path: Path
    created: bool
    ignore_detail: str | None = None


def global_config_exists() -> bool:
    """Return whether a real saved global config file exists."""
    paths = discover_global_config_paths()
    return paths.write_path.exists() or paths.legacy_path.exists()


def workspace_config_exists(cwd: Path) -> bool:
    """Return whether the current workspace has a saved workspace config file."""
    workspace = detect_workspace_context(cwd)
    return Path(workspace.workspace_config_path).exists()


def environment_config_exists(env: dict[str, str] | None = None) -> bool:
    """Return whether any ctxsift config env var is present."""
    source = env or os.environ
    return any(bool(source.get(name)) for name in ENVIRONMENT_KEY_MAP)


def bootstrap_config_available(cwd: Path, env: dict[str, str] | None = None) -> bool:
    """Return whether ctxsift has any real config source to run with."""
    return workspace_config_exists(cwd) or global_config_exists() or environment_config_exists(env)


def workspace_db_path(cwd: Path, config: AppConfig) -> Path:
    """Resolve the database path for the current workspace and config."""
    if config.db_path:
        return Path(config.db_path).expanduser()
    workspace = detect_workspace_context(cwd)
    if workspace.db_path is None:
        raise RuntimeError("Workspace discovery did not provide a database path.")
    return Path(workspace.db_path)


def should_offer_workspace_ignore(cwd: Path, config: AppConfig) -> bool:
    """Return whether configure should offer to add .ctxsift/ to the workspace .gitignore."""
    workspace = detect_workspace_context(cwd)
    target_path = workspace_db_path(cwd, config)
    return requires_workspace_ignore_entry(workspace, target_path)


async def ensure_workspace_initialized(
    cwd: Path,
    config: AppConfig,
    write_ignore: bool = False,
) -> WorkspaceSetupResult:
    """Initialize the current workspace database when needed."""
    workspace = detect_workspace_context(cwd)
    target_path = workspace_db_path(cwd, config)
    created = not target_path.exists()
    await initialize_database(target_path)
    ignore_detail: str | None = None
    if write_ignore:
        ignore_result = ensure_workspace_ignore_entry(workspace, target_path)
        ignore_detail = ignore_result.detail
    return WorkspaceSetupResult(
        db_path=target_path,
        created=created,
        ignore_detail=ignore_detail,
    )
