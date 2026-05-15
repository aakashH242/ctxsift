"""Runtime health checks."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ctxsift.config import ConfigResolutionRequest, resolve_config
from ctxsift.doctor_probes import (
    cuda_probe,
    fts5_probe,
    git_probe,
    optional_package_probe,
    remote_config_probe,
    sqlite_core_probe,
)
from ctxsift.embeddings import create_embedding_backend
from ctxsift.embeddings.base import EmbeddingBackendUnavailableError
from ctxsift.storage import StorageInitResult, initialize_database
from ctxsift.vector_store import vector_store_status
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
        checks.append(await _sqlite_vec_check(db_path, resolved_config.config.embedding))
    else:
        checks.append(
            DoctorCheck(
                name="sqlite_vec",
                severity="warning",
                ok=False,
                detail="Skipped sqlite-vec probe because the database could not be initialized.",
            )
        )
    checks.extend(_optional_runtime_checks())
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


async def _sqlite_vec_check(db_path: Path, config) -> DoctorCheck:
    try:
        backend = create_embedding_backend(config)
        dimension = await backend.embedding_dimension()
    except EmbeddingBackendUnavailableError as error:
        return DoctorCheck(
            "sqlite_vec",
            "warning",
            False,
            f"Embedding backend unavailable; recall will use FTS5 only. {error}",
        )
    status = await vector_store_status(db_path, backend.model_name, dimension)
    if status.available:
        return DoctorCheck(
            "sqlite_vec",
            "warning",
            True,
            f"sqlite-vec is available (vec_version={status.sqlite_vec_version}, dim={dimension}).",
        )
    return DoctorCheck(
        "sqlite_vec",
        "warning",
        False,
        status.warning or "sqlite-vec is unavailable; recall will use FTS5 only.",
    )


def _optional_runtime_checks() -> list[DoctorCheck]:
    return [
        _probe_check("cuda", "optional", cuda_probe()),
        _probe_check(
            "onnxruntime",
            "optional",
            optional_package_probe("onnxruntime", "ONNX Runtime"),
        ),
        _probe_check(
            "flashattention",
            "optional",
            optional_package_probe("flash_attn", "FlashAttention"),
        ),
    ]


def _probe_check(name: str, severity: str, probe: tuple[bool, str]) -> DoctorCheck:
    ok, detail = probe
    return DoctorCheck(name=name, severity=severity, ok=ok, detail=detail)


def _render_check_line(check: DoctorCheck) -> str:
    status = "ok" if check.ok else check.severity
    return f"[{check.severity}] {check.name}: {status} - {check.detail}"
