"""Workspace management: discovery, bootstrap, and ignore-file handling."""

from ctxsift.workspace.discovery import detect_workspace_context
from ctxsift.workspace.ignore import (
    IgnoreWriteResult,
    ensure_workspace_ignore_entry,
    requires_workspace_ignore_entry,
)

__all__ = [
    "IgnoreWriteResult",
    "detect_workspace_context",
    "ensure_workspace_ignore_entry",
    "requires_workspace_ignore_entry",
]
