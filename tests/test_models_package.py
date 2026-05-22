"""Regression tests for lazy model package exports."""

from __future__ import annotations

import importlib


def test_importing_local_runtime_does_not_trigger_daemon_cycle() -> None:
    local_runtime = importlib.import_module("ctxsift.models.local_runtime")

    assert hasattr(local_runtime, "resolve_local_runtime")


def test_models_package_exposes_factory_and_lazy_modules() -> None:
    models = importlib.import_module("ctxsift.models")

    assert callable(models.create_compression_backend)
    assert callable(models.create_local_backend)
    assert models.hf_hub_cache is importlib.import_module("ctxsift.models.hf_hub_cache")
