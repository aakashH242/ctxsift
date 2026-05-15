"""Runtime health checks."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ctxsift.config import ConfigResolutionRequest, resolve_config
from ctxsift.doctor_probes import (
    cuda_probe,
    flash_attention_probe,
    fts5_probe,
    git_probe,
    optional_package_probe,
    optional_package_probe_any,
    remote_config_probe,
    sqlite_core_probe,
)
from ctxsift.storage import StorageInitResult, initialize_database
from ctxsift.types import AppConfig, LocalQuantizationMode
from ctxsift.vector_store import probe_vector_store
from ctxsift.workspace import detect_workspace_context


@dataclass(frozen=True)
class DoctorCheck:
    """One doctor check result."""

    name: str
    severity: str
    ok: bool
    detail: str


@dataclass(frozen=True)
class DoctorReport:
    """Grouped doctor results."""

    checks: list[DoctorCheck]


async def collect_doctor_report(cwd: Path) -> DoctorReport:
    """Collect doctor checks without mutating repo-tracked files."""
    workspace = detect_workspace_context(cwd)
    resolved_config = resolve_config(ConfigResolutionRequest(cwd=cwd))
    db_path = Path(resolved_config.config.db_path or workspace.db_path or "").expanduser()
    checks: list[DoctorCheck] = [
        _probe_check("git_workspace", "warning", git_probe(workspace)),
        _probe_check("remote_config", "warning", remote_config_probe(resolved_config.config)),
        _probe_check("sqlite_core", "required", sqlite_core_probe()),
        _probe_check("sqlite_fts5", "required", fts5_probe()),
    ]
    db_check, init_result = await _database_check(db_path)
    checks.insert(0, db_check)
    if init_result is not None:
        checks.append(await _sqlite_vec_check(db_path, resolved_config.config.embedding.model))
    else:
        checks.append(
            DoctorCheck(
                name="sqlite_vec",
                severity="warning",
                ok=False,
                detail="Skipped sqlite-vec probe because the database could not be initialized.",
            )
        )
    checks.extend(_optional_runtime_checks(resolved_config.config))
    return DoctorReport(checks=checks)


def render_doctor_report(report: DoctorReport) -> str:
    """Render doctor output for CLI display."""
    return "\n".join(_render_check_line(check) for check in report.checks)


async def _database_check(db_path: Path) -> tuple[DoctorCheck, StorageInitResult | None]:
    try:
        init_result = await initialize_database(db_path)
    except Exception as error:
        return (
            DoctorCheck(
                name="database",
                severity="required",
                ok=False,
                detail=f"Database initialization failed for {db_path}: {error}",
            ),
            None,
        )
    return (
        DoctorCheck(
            name="database",
            severity="required",
            ok=True,
            detail=(
                f"Database initialized at {init_result.db_path} "
                f"(schema={init_result.schema_version})."
            ),
        ),
        init_result,
    )


async def _sqlite_vec_check(db_path: Path, configured_model_name: str) -> DoctorCheck:
    status = await probe_vector_store(db_path)
    if not status.available:
        return DoctorCheck(
            "sqlite_vec",
            "warning",
            False,
            status.warning or "sqlite-vec is unavailable; recall will use FTS5 only.",
        )
    if status.model_name and status.model_name != configured_model_name:
        return DoctorCheck(
            "sqlite_vec",
            "warning",
            False,
            (
                "sqlite-vec index model mismatch; recall will fall back to FTS5 only. "
                f"DB model={status.model_name}, configured model={configured_model_name}."
            ),
        )
    detail = f"sqlite-vec is available (vec_version={status.sqlite_vec_version}"
    if status.dimension is not None:
        detail += f", dim={status.dimension}"
    detail += ")."
    return DoctorCheck(
        "sqlite_vec",
        "warning",
        True,
        detail,
    )


def _optional_runtime_checks(config: AppConfig) -> list[DoctorCheck]:
    checks = [
        _probe_check("cuda", "optional", cuda_probe()),
        _probe_check(
            "onnxruntime",
            "optional",
            optional_package_probe("onnxruntime", "ONNX Runtime"),
        ),
        _probe_check(
            "flashattention",
            "optional",
            flash_attention_probe(),
        ),
    ]
    checks.extend(_quantization_runtime_checks(config))
    return checks


def _quantization_runtime_checks(config: AppConfig) -> list[DoctorCheck]:
    mode = config.local.quantization
    if mode is LocalQuantizationMode.NONE:
        return []
    checks = [
        _probe_check(
            "accelerate",
            "warning",
            optional_package_probe("accelerate", "Accelerate"),
        )
    ]
    if mode.value.startswith("bnb-"):
        checks.append(
            _probe_check(
                "bitsandbytes",
                "warning",
                optional_package_probe("bitsandbytes", "bitsandbytes"),
            )
        )
        return checks
    checks.append(
        _probe_check(
            "optimum_quanto",
            "warning",
            optional_package_probe_any(
                ("optimum.quanto", "optimum_quanto"),
                "Optimum Quanto",
            ),
        )
    )
    return checks


def _probe_check(name: str, severity: str, probe: tuple[bool, str]) -> DoctorCheck:
    ok, detail = probe
    return DoctorCheck(name=name, severity=severity, ok=ok, detail=detail)


def _render_check_line(check: DoctorCheck) -> str:
    status = "ok" if check.ok else check.severity
    return f"[{check.severity}] {check.name}: {status} - {check.detail}"
