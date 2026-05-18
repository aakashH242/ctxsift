"""Post-save configure helpers."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ctxsift.doctor import DoctorReport, collect_doctor_report_for_config
from ctxsift.model_preload import ModelPreloadResult, preload_configured_models
from ctxsift.types import AppConfig
from ctxsift.workspace_setup import WorkspaceSetupResult, ensure_workspace_initialized


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
) -> ConfigureSetupResult:
    """Initialize workspace state, probe health, and warm configured models."""
    workspace = await ensure_workspace_initialized(
        cwd=cwd,
        config=config,
        write_ignore=write_ignore,
    )
    doctor = await collect_doctor_report_for_config(cwd, config)
    model_preloads = await preload_configured_models(config)
    return ConfigureSetupResult(
        workspace=workspace,
        doctor=doctor,
        model_preloads=model_preloads,
    )
