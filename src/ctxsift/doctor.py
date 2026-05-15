"""Runtime health checks."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sqlite3

from ctxsift.config import ConfigResolutionRequest, resolve_config
from ctxsift.embeddings import create_embedding_backend
from ctxsift.embeddings.base import EmbeddingBackendUnavailableError
from ctxsift.storage import initialize_database
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
    """Collect the currently implemented doctor checks."""
    workspace = detect_workspace_context(cwd)
    resolved_config = resolve_config(ConfigResolutionRequest(cwd=cwd))
    db_path = Path(resolved_config.config.db_path or workspace.db_path or "").expanduser()
    await initialize_database(db_path)
    checks = [
        _fts5_check(),
        await _sqlite_vec_check(db_path, resolved_config.config.embedding),
    ]
    return DoctorReport(checks=checks)


def render_doctor_report(report: DoctorReport) -> str:
    """Render doctor output for CLI display."""
    lines = []
    for check in report.checks:
        status = "ok" if check.ok else check.severity
        lines.append(f"{check.name}: {status} - {check.detail}")
    return "\n".join(lines)


def _fts5_check() -> DoctorCheck:
    try:
        connection = sqlite3.connect(":memory:")
        connection.execute("CREATE VIRTUAL TABLE temp.fts5_probe USING fts5(content)")
        connection.close()
    except sqlite3.Error as error:
        return DoctorCheck("sqlite_fts5", "error", False, f"FTS5 unavailable: {error}")
    return DoctorCheck("sqlite_fts5", "ok", True, "FTS5 is available.")


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
            "ok",
            True,
            f"sqlite-vec is available (vec_version={status.sqlite_vec_version}, dim={dimension}).",
        )
    return DoctorCheck(
        "sqlite_vec",
        "warning",
        False,
        status.warning or "sqlite-vec is unavailable; recall will use FTS5 only.",
    )
