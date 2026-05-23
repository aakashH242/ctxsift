"""Tests for workspace bootstrap helpers."""

from __future__ import annotations

from pathlib import Path

import pytest

from ctxsift.config.store import ENVIRONMENT_KEY_MAP
from ctxsift.workspace import setup as workspace_setup


def test_environment_config_exists_uses_explicit_empty_mapping(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    env_name = next(iter(ENVIRONMENT_KEY_MAP))
    monkeypatch.setenv(env_name, "configured")

    assert workspace_setup.environment_config_exists({}) is False


def test_bootstrap_config_available_respects_explicit_empty_mapping(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    env_name = next(iter(ENVIRONMENT_KEY_MAP))
    monkeypatch.setenv(env_name, "configured")
    monkeypatch.setattr(workspace_setup, "workspace_config_exists", lambda cwd: False)
    monkeypatch.setattr(workspace_setup, "global_config_exists", lambda: False)

    assert workspace_setup.bootstrap_config_available(tmp_path, env={}) is False
