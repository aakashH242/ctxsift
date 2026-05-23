"""Post-save configure helpers."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from ctxsift.diagnostics.doctor import DoctorReport, collect_doctor_report_for_config
from ctxsift.model_preload import ModelPreloadResult, preload_configured_models
from ctxsift.types import AppConfig
from ctxsift.workspace.setup import WorkspaceSetupResult, ensure_workspace_initialized


@dataclass(frozen=True)
class ConfigureSetupResult:
    """Results produced after configure saves one config."""

    workspace: WorkspaceSetupResult
    doctor: DoctorReport
    model_preloads: list[ModelPreloadResult]


async def run_configure_setup(
    cwd: Path,
    config: AppConfig,
    write_ignore: bool = False,
    progress: Callable[[str], None] | None = None,
) -> ConfigureSetupResult:
    """Initialize workspace state, probe health, and warm configured models."""
    _report_progress(progress, "Please wait: initializing workspace database...")
    workspace = await ensure_workspace_initialized(
        cwd=cwd,
        config=config,
        write_ignore=write_ignore,
    )
    _report_progress(progress, "Please wait: running health checks...")
    doctor = await collect_doctor_report_for_config(cwd, config)
    _report_progress(progress, "Please wait: preparing configured models...")
    model_preloads = await _run_model_preloads(config, progress)
    return ConfigureSetupResult(
        workspace=workspace,
        doctor=doctor,
        model_preloads=model_preloads,
    )


def _report_progress(progress: Callable[[str], None] | None, message: str) -> None:
    if progress is not None:
        progress(message)


async def _run_model_preloads(
    config: AppConfig,
    progress: Callable[[str], None] | None,
) -> list[ModelPreloadResult]:
    try:
        return await preload_configured_models(config, progress=progress)
    except TypeError:
        return await preload_configured_models(config)
