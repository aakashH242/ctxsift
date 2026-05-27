"""Reusable runtime probes for doctor checks."""

from __future__ import annotations

import importlib
import importlib.util
import sqlite3
import subprocess
import sys

from ctxsift.types import AppConfig, WorkspaceContext

CUDA_PROBE_TIMEOUT_SECONDS = 8.0


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
    if not config.remote.base_url.strip():
        return True, "Remote backend is disabled; local-only mode is active."
    if not config.remote.model_name.strip():
        return (
            False,
            "Remote backend is enabled by remote.base_url but remote.model_name is missing.",
        )
    return True, "Remote backend configuration is complete."


def cuda_probe() -> tuple[bool, str]:
    """Probe whether CUDA is available through torch."""
    probe_code = (
        "import importlib\n"
        "try:\n"
        "    torch = importlib.import_module('torch')\n"
        "except ImportError:\n"
        "    print('IMPORT_ERROR')\n"
        "    raise SystemExit(0)\n"
        "print('CUDA_AVAILABLE' if torch.cuda.is_available() else 'CUDA_UNAVAILABLE')\n"
    )
    try:
        completed = subprocess.run(
            [sys.executable, "-c", probe_code],
            capture_output=True,
            text=True,
            timeout=CUDA_PROBE_TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return (
            False,
            (
                "CUDA probe timed out while importing PyTorch or querying CUDA state. "
                "Run `ctxsift doctor` later for a full probe once the local GPU stack is healthy."
            ),
        )
    stdout = completed.stdout.strip()
    if "IMPORT_ERROR" in stdout:
        return False, "PyTorch is not installed; CUDA acceleration is unavailable."
    if "CUDA_AVAILABLE" in stdout:
        return True, "CUDA is available."
    if "CUDA_UNAVAILABLE" in stdout:
        return False, "CUDA is unavailable."
    stderr = completed.stderr.strip()
    if stderr:
        return False, f"CUDA probe failed: {stderr}"
    return False, "CUDA probe failed without a usable result."


def optional_package_probe(module_name: str, label: str) -> tuple[bool, str]:
    """Probe whether one optional package can be imported."""
    try:
        importlib.import_module(module_name)
    except ImportError:
        return False, f"{label} is not installed."
    except Exception as error:
        return False, f"{label} could not be imported: {error}"
    return True, f"{label} is available."


def optional_package_probe_any(module_names: tuple[str, ...], label: str) -> tuple[bool, str]:
    """Probe whether any supported import path for one optional package is usable."""
    for module_name in module_names:
        try:
            importlib.import_module(module_name)
        except ImportError:
            continue
        except Exception as error:
            return False, f"{label} could not be imported: {error}"
        return True, f"{label} is available."
    return False, f"{label} is not installed."


def flash_attention_probe() -> tuple[bool, str]:
    """Probe whether any supported Flash Attention provider is installed."""
    if importlib.util.find_spec("flash_attn") is not None:
        return True, "FlashAttention is available via flash_attn."
    if importlib.util.find_spec("kernels") is not None:
        return True, "FlashAttention kernels are available via the kernels package."
    return False, "FlashAttention is not installed."
