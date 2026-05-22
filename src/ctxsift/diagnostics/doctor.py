"""Runtime health checks."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from rich.console import Group
from rich.text import Text

from ctxsift.config import ConfigResolutionRequest, resolve_config
from ctxsift.diagnostics.probes import (
    cuda_probe,
    flash_attention_probe,
    fts5_probe,
    git_probe,
    optional_package_probe,
    remote_config_probe,
    sqlite_core_probe,
)
from ctxsift.models.hf_hub_cache import resolve_cached_hf_file
from ctxsift.storage import StorageInitResult, initialize_database
from ctxsift.models.local_runtime import required_gguf_filename, resolve_local_runtime
from ctxsift.models.base import BackendUnavailableError
from ctxsift.types import AppConfig, LocalQuantizationMode
from ctxsift.storage.vector import probe_vector_store
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
    resolved_config = resolve_config(ConfigResolutionRequest(cwd=cwd))
    return await collect_doctor_report_for_config(cwd, resolved_config.config)


async def collect_doctor_report_for_config(cwd: Path, config: AppConfig) -> DoctorReport:
    """Collect doctor checks for one explicit config snapshot."""
    workspace = detect_workspace_context(cwd)
    db_path = Path(config.db_path or workspace.db_path or "").expanduser()
    checks: list[DoctorCheck] = [
        _probe_check("git_workspace", "warning", git_probe(workspace)),
        _probe_check("remote_config", "warning", remote_config_probe(config)),
        _probe_check("sqlite_core", "required", sqlite_core_probe()),
        _probe_check("sqlite_fts5", "required", fts5_probe()),
    ]
    db_check, init_result = await _database_check(db_path)
    checks.insert(0, db_check)
    if init_result is not None:
        checks.append(await _sqlite_vec_check(db_path, config.embedding.model))
    else:
        checks.append(
            DoctorCheck(
                name="sqlite_vec",
                severity="warning",
                ok=False,
                detail="Skipped sqlite-vec probe because the database could not be initialized.",
            )
        )
    checks.extend(_optional_runtime_checks(config))
    return DoctorReport(checks=checks)


def render_doctor_report(report: DoctorReport) -> str:
    """Render doctor output for CLI display."""
    return "\n".join(_render_check_line(check) for check in report.checks)


def render_doctor_report_rich(report: DoctorReport):
    """Render doctor output for richer CLI display."""
    return Group(*(_render_check_text(check) for check in report.checks))


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
    checks.extend(_remote_runtime_checks(config))
    checks.extend(_local_runtime_checks(config))
    checks.extend(_quantization_runtime_checks(config))
    return checks


def _local_runtime_checks(config: AppConfig) -> list[DoctorCheck]:
    if config.remote.base_url.strip():
        return []
    try:
        runtime = resolve_local_runtime(config.local)
    except BackendUnavailableError as error:
        return [
            DoctorCheck(
                name="local_runtime",
                severity="warning",
                ok=False,
                detail=str(error),
            )
        ]
    if runtime.uses_llama_cpp:
        checks = [
            _probe_check(
                "llama_cpp",
                "optional",
                optional_package_probe("llama_cpp", "llama-cpp-python"),
            )
        ]
        checks.append(_gguf_resolution_check(config))
        return checks
    return []


def _remote_runtime_checks(config: AppConfig) -> list[DoctorCheck]:
    if not config.remote.base_url.strip():
        return []
    ok, detail = optional_package_probe("litellm", "LiteLLM")
    if ok:
        return [DoctorCheck("litellm", "warning", True, detail)]
    return [
        DoctorCheck(
            name="litellm",
            severity="warning",
            ok=False,
            detail=(
                'LiteLLM is not installed. Install it with `uv tool install "ctxsift[remote]"`; '
                "remote compression will not work until it is available."
            ),
        )
    ]


def _quantization_runtime_checks(config: AppConfig) -> list[DoctorCheck]:
    if config.remote.base_url.strip():
        return []
    try:
        runtime = resolve_local_runtime(config.local)
    except BackendUnavailableError:
        return []
    if runtime.uses_llama_cpp:
        return []
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
    return checks


def _gguf_resolution_check(config: AppConfig) -> DoctorCheck:
    try:
        import huggingface_hub  # noqa: F401
    except ImportError as error:
        return DoctorCheck(
            name="gguf_artifact",
            severity="warning",
            ok=False,
            detail=f"huggingface_hub is unavailable: {error}",
        )
    try:
        filename = required_gguf_filename(config.local)
        path = resolve_cached_hf_file(
            repo_id=config.local.model,
            filename=filename,
            cache_dir=config.local.model_cache_path,
        )
    except Exception as error:
        return DoctorCheck(
            name="gguf_artifact",
            severity="warning",
            ok=False,
            detail=str(error),
        )
    if path is None:
        return DoctorCheck(
            name="gguf_artifact",
            severity="warning",
            ok=True,
            detail=(
                f"Configured GGUF artifact {config.local.model}/{filename} is not cached locally yet. "
                "Configure or first use will download it."
            ),
        )
    return DoctorCheck(
        name="gguf_artifact",
        severity="warning",
        ok=True,
        detail=f"Resolved GGUF artifact at {path}.",
    )


def _probe_check(name: str, severity: str, probe: tuple[bool, str]) -> DoctorCheck:
    ok, detail = probe
    return DoctorCheck(name=name, severity=severity, ok=ok, detail=detail)


def _render_check_line(check: DoctorCheck) -> str:
    status = "ok" if check.ok else check.severity
    return f"[{check.severity}] {check.name}: {status} - {check.detail}"


def _render_check_text(check: DoctorCheck) -> Text:
    text = Text()
    text.append(f"[{check.severity}] ", style=_severity_style(check.severity))
    text.append(f"{check.name}: ", style="bold bright_white")
    text.append(_status_label(check), style=_status_style(check))
    text.append(" - ", style="dim")
    text.append(check.detail, style=_detail_style(check))
    text.no_wrap = True
    return text


def _status_label(check: DoctorCheck) -> str:
    if check.ok:
        return "ok"
    if check.severity == "required":
        return "fail"
    if check.severity == "warning":
        return "warning"
    return "optional"


def _severity_style(severity: str) -> str:
    if severity == "required":
        return "bold cyan"
    if severity == "warning":
        return "bold yellow"
    return "bold blue"


def _status_style(check: DoctorCheck) -> str:
    if check.ok:
        return "bold green"
    if check.severity == "required":
        return "bold red"
    return "bold yellow"


def _detail_style(check: DoctorCheck) -> str:
    if check.ok:
        return "green"
    if check.severity == "required":
        return "red"
    return "yellow"
