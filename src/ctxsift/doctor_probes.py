"""Reusable runtime probes for doctor checks."""

from __future__ import annotations

import importlib
import sqlite3

from ctxsift.types import AppConfig, WorkspaceContext


def sqlite_core_probe() -> tuple[bool, str]:
    """Probe whether core SQLite is usable."""
    try:
        connection = sqlite3.connect(":memory:")
        connection.close()
    except sqlite3.Error as error:
        return False, f"SQLite unavailable: {error}"
    return True, "SQLite is available."


def fts5_probe() -> tuple[bool, str]:
    """Probe whether SQLite FTS5 is usable."""
    try:
        connection = sqlite3.connect(":memory:")
        connection.execute("CREATE VIRTUAL TABLE temp.fts5_probe USING fts5(content)")
        connection.close()
    except sqlite3.Error as error:
        return False, f"FTS5 unavailable: {error}"
    return True, "FTS5 is available."


def git_probe(workspace: WorkspaceContext) -> tuple[bool, str]:
    """Probe whether git-backed workspace metadata is available."""
    if workspace.is_git_repo and workspace.git_dir:
        return True, f"Git metadata is available via {workspace.git_dir}."
    return False, "Not inside a Git repo; git metadata features will be reduced."


def remote_config_probe(config: AppConfig) -> tuple[bool, str]:
    """Probe whether remote config is complete when remote mode is intended."""
    remote_selected = config.run_mode.value == "remote" or bool(config.remote.base_url.strip())
    if not remote_selected:
        return True, "Remote backend is disabled; local-only mode is active."
    if not config.remote.base_url.strip():
        return False, "Remote backend selected but remote.base_url is missing."
    if not config.remote.model_name.strip():
        return False, "Remote backend selected but remote.model_name is missing."
    return True, "Remote backend configuration is complete."


def cuda_probe() -> tuple[bool, str]:
    """Probe whether CUDA is available through torch."""
    try:
        torch = importlib.import_module("torch")
    except ImportError:
        return False, "PyTorch is not installed; CUDA acceleration is unavailable."
    if torch.cuda.is_available():
        return True, "CUDA is available."
    return False, "CUDA is unavailable."


def optional_package_probe(module_name: str, label: str) -> tuple[bool, str]:
    """Probe whether one optional package can be imported."""
    try:
        importlib.import_module(module_name)
    except ImportError:
        return False, f"{label} is not installed."
    except Exception as error:
        return False, f"{label} could not be imported: {error}"
    return True, f"{label} is available."
