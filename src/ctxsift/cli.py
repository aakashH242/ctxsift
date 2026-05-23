"""Command-line interface for ctxsift."""

from __future__ import annotations

import asyncio
from pathlib import Path
import sys
from typing import Annotated

import typer
from pydantic import ValidationError
from rich.console import Console

from ctxsift.agent.skills import install_agent_skills, prompt_for_agent_skill_install
from ctxsift.compression import compress_input
from ctxsift.compression.intent import CompressionIntent
from ctxsift.config import (
    ConfigResolutionRequest,
    ConfigSaveRequest,
    ConfigScope,
    ConfigWriteRequest,
    discover_global_config_paths,
    render_resolved_config_rich,
    resolve_config,
    save_config,
    set_config_value,
)
from ctxsift.config.setup import run_configure_setup
from ctxsift.config.flow import prompt_for_config, prompt_for_save_scope
from ctxsift.daemon.manager import (
    daemon_statuses,
    required_daemon_specs,
    startup_statuses,
    stop_all_daemons,
    stop_daemon,
)
from ctxsift.daemon.types import DaemonStatus
from ctxsift.diagnostics.doctor import collect_doctor_report, render_doctor_report_rich
from ctxsift.execution import (
    CommandExecutionRequest,
    CommandValidationError,
    capture_launch_failure,
    execute_command,
)
from ctxsift.git_metadata import capture_git_metadata
from ctxsift.recall import recall_records, render_recall_records
from ctxsift.compression.run_payload import (
    render_run_payload,
)
from ctxsift.types import CompressionRequest
from ctxsift.workspace import detect_workspace_context
from ctxsift.workspace.setup import (
    bootstrap_config_available,
    ensure_workspace_initialized,
    should_offer_workspace_ignore,
)

app = typer.Typer(
    add_completion=False,
    help=(
        "Local-first command output compression and recall.\n\n"
        "Compress command output, save useful summaries, and recall them later.\n\n"
        "Use `ctxsift configure` to set up ctxsift and the current workspace.\n"
        "Use `ctxsift config ...` when you want to edit config values directly."
    ),
    no_args_is_help=True,
)
config_app = typer.Typer(
    help="Show or change config values directly. Use `configure` for the guided interactive setup."
)
daemon_app = typer.Typer(help="Start, stop, or inspect local ctxsift daemons.")
console = Console()

app.add_typer(config_app, name="config")
app.add_typer(daemon_app, name="daemon")


def _not_implemented(command_name: str) -> None:
    typer.echo(f"`ctxsift {command_name}` is scaffolded but not implemented yet.")
    raise typer.Exit(code=1)


@app.command()
def configure(
    write_ignore: Annotated[
        bool | None,
        typer.Option(
            "--write-ignore/--no-write-ignore",
            help="Override whether configure adds `.ctxsift/` to the workspace `.gitignore` when that DB path is used.",
        ),
    ] = None,
) -> None:
    """Guided setup for ctxsift behavior in this workspace or globally."""
    current_directory = Path.cwd()
    workspace = detect_workspace_context(current_directory)
    global_paths = discover_global_config_paths()
    resolved = resolve_config(
        ConfigResolutionRequest(
            cwd=current_directory,
        )
    )
    try:
        updated_config = prompt_for_config(resolved.config)
        selected_scope = prompt_for_save_scope(
            workspace_path=Path(workspace.workspace_config_path),
            global_path=global_paths.write_path,
        )
        effective_write_ignore = _resolve_configure_write_ignore(
            current_directory=current_directory,
            config=updated_config,
            write_ignore_override=write_ignore,
        )
        saved = save_config(
            ConfigSaveRequest(
                config=updated_config,
                cwd=current_directory,
                force_global=selected_scope is ConfigScope.GLOBAL,
            )
        )
    except (ValueError, ValidationError) as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2) from error
    agent_skill_plan = prompt_for_agent_skill_install(Path(workspace.workspace_root))
    if agent_skill_plan is not None and agent_skill_plan.selections:
        typer.echo("Please wait: installing selected agent skills...")
    agent_skill_results = install_agent_skills(
        agent_skill_plan,
        workspace_root=Path(workspace.workspace_root),
    )
    typer.echo(f"Updated {saved.scope.value} config at {saved.write_path}")
    for install_result in agent_skill_results:
        if install_result.ok:
            typer.echo(install_result.detail)
        else:
            typer.echo(f"[ctxsift warning] {install_result.detail}", err=True)
    setup_result = asyncio.run(
        run_configure_setup(
            cwd=current_directory,
            config=updated_config,
            write_ignore=effective_write_ignore,
            progress=typer.echo,
        )
    )
    if setup_result.workspace.created:
        typer.echo(f"Initialized workspace database at {setup_result.workspace.db_path}")
    if setup_result.workspace.ignore_detail:
        typer.echo(setup_result.workspace.ignore_detail)
    for preload_result in setup_result.model_preloads:
        if preload_result.ok:
            typer.echo(preload_result.detail)
        else:
            typer.echo(f"[ctxsift warning] {preload_result.detail}", err=True)
    typer.echo("")
    console.print(render_doctor_report_rich(setup_result.doctor), soft_wrap=True)


def _resolve_configure_write_ignore(
    current_directory: Path,
    config,
    write_ignore_override: bool | None,
) -> bool:
    if write_ignore_override is not None:
        return write_ignore_override
    if not should_offer_workspace_ignore(current_directory, config):
        return False
    return typer.confirm(
        "ctxsift will store data under .ctxsift/. Add .ctxsift/ to the workspace .gitignore?",
        default=True,
    )


@app.command(context_settings={"allow_extra_args": True, "ignore_unknown_options": True})
def compress(
    ctx: typer.Context,
    instruction: Annotated[
        str, typer.Argument(help="Compression instruction for the provided input.")
    ],
    intent: Annotated[
        CompressionIntent | None,
        typer.Option(
            "--intent",
            help="Explicit output contract for the compression result.",
        ),
    ] = None,
    shell: Annotated[
        bool,
        typer.Option(
            "--shell",
            help="Execute one explicit shell command string instead of reading stdin.",
        ),
    ] = False,
    max_output_tokens: Annotated[
        int | None,
        typer.Option("--max-output-tokens", help="Override the maximum output token budget."),
    ] = None,
) -> None:
    """Compress stdin or command output using an instruction."""
    if intent is None:
        typer.echo(
            "Missing option '--intent'. Choose from: " f"{_render_compress_intent_choices()}",
            err=True,
        )
        raise typer.Exit(code=2)
    command = tuple(_command_args(ctx.args))
    if not bootstrap_config_available(Path.cwd()):
        _handle_missing_bootstrap_config_for_compress(
            ctx=ctx,
            instruction=instruction,
            command=command,
            shell=shell,
        )
    if command or shell:
        resolved = resolve_config(ConfigResolutionRequest(cwd=Path.cwd()))
        _ensure_workspace_ready(resolved.config, current_directory=Path.cwd())
        result, exit_code = _invoke_command_compression(
            ctx=ctx,
            intent=intent,
            instruction=instruction,
            current_directory=Path.cwd(),
            max_output_tokens=max_output_tokens,
            shell=shell,
        )
        typer.echo(result.compressed_output)
        raise typer.Exit(code=exit_code)
    resolved = resolve_config(ConfigResolutionRequest(cwd=Path.cwd()))
    _ensure_workspace_ready(resolved.config, current_directory=Path.cwd())
    raw_input = sys.stdin.read()
    result = asyncio.run(
        compress_input(
            CompressionRequest(
                intent=intent,
                instruction=instruction,
                raw_input=raw_input,
                cwd=str(Path.cwd()),
                max_output_tokens=max_output_tokens,
            )
        )
    )
    typer.echo(result.compressed_output)


def _render_compress_intent_choices() -> str:
    return ", ".join(intent.value for intent in CompressionIntent)


@app.command()
def recall(
    query: Annotated[str, typer.Argument(help="Query used to search prior compressed records.")],
    files: Annotated[
        list[str] | None,
        typer.Option("--files", help="File paths used to filter or boost recall results."),
    ] = None,
    limit: Annotated[
        int | None,
        typer.Option("--limit", min=1, help="Maximum number of recall results to display."),
    ] = None,
) -> None:
    """Recall previously stored compressed records."""
    if not bootstrap_config_available(Path.cwd()):
        typer.echo(
            "[ctxsift warning] No workspace config, global config, or ctxsift env config is set yet. "
            "Run `ctxsift configure` first.",
            err=True,
        )
        typer.echo("No recall results.")
        return
    resolved = resolve_config(ConfigResolutionRequest(cwd=Path.cwd()))
    _ensure_workspace_ready(resolved.config, current_directory=Path.cwd())
    warnings: list[str] = []
    results = asyncio.run(
        recall_records(
            query=query,
            cwd=Path.cwd(),
            file_filters=files,
            limit=limit,
            warnings_sink=warnings,
        )
    )
    for warning in warnings:
        typer.echo(warning, err=True)
    typer.echo(render_recall_records(results))


@config_app.command("show")
def config_show(
    global_scope: Annotated[
        bool,
        typer.Option(
            "--global",
            help="Show the global config instead of resolving from the current workspace.",
        ),
    ] = False,
) -> None:
    """Show the config that ctxsift is currently using."""
    result = resolve_config(
        ConfigResolutionRequest(
            cwd=Path.cwd(),
            force_global=global_scope,
        )
    )
    console.print(render_resolved_config_rich(result), soft_wrap=True)


@config_app.command("set")
def config_set(
    key: Annotated[str, typer.Argument(help="Supported config key to update.")],
    value: Annotated[str, typer.Argument(help="Value to set for the given config key.")],
    global_scope: Annotated[
        bool,
        typer.Option(
            "--global",
            help="Write to global config instead of the current workspace config.",
        ),
    ] = False,
) -> None:
    """Change one config value directly."""
    try:
        result = set_config_value(
            ConfigWriteRequest(
                key=key,
                raw_value=value,
                cwd=Path.cwd(),
                force_global=global_scope,
            )
        )
    except (ValueError, ValidationError) as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2) from error
    typer.echo(f"Updated {key} in {result.write_path}")


@app.command()
def doctor() -> None:
    """Inspect runtime health and optional features."""
    report = asyncio.run(collect_doctor_report(Path.cwd()))
    console.print(render_doctor_report_rich(report), soft_wrap=True)


@daemon_app.command("start")
def daemon_start() -> None:
    """Start the daemons required by the effective config in this directory."""
    resolved = resolve_config(ConfigResolutionRequest(cwd=Path.cwd()))
    statuses = startup_statuses(resolved.config)
    typer.echo(_render_daemon_statuses(statuses))


@daemon_app.command("stop")
def daemon_stop(
    all_daemons: Annotated[
        bool,
        typer.Option("--all", help="Stop every registered ctxsift daemon."),
    ] = False,
) -> None:
    """Stop the daemons required by the effective config in this directory."""
    if all_daemons:
        statuses = stop_all_daemons()
    else:
        resolved = resolve_config(ConfigResolutionRequest(cwd=Path.cwd()))
        statuses = [stop_daemon(spec) for spec in required_daemon_specs(resolved.config)]
    typer.echo(_render_daemon_statuses(statuses))


@daemon_app.command("status")
def daemon_status(
    all_daemons: Annotated[
        bool,
        typer.Option("--all", help="Show every registered ctxsift daemon."),
    ] = False,
) -> None:
    """Show daemon health for the effective config in this directory."""
    resolved = resolve_config(ConfigResolutionRequest(cwd=Path.cwd()))
    statuses = daemon_statuses(resolved.config, include_all=all_daemons)
    typer.echo(_render_daemon_statuses(statuses))


async def _run_capture(request: CommandExecutionRequest):
    try:
        return await execute_command(request)
    except FileNotFoundError as error:
        return capture_launch_failure(request, error)


async def _run_command_flow(
    request: CommandExecutionRequest,
    intent: CompressionIntent,
    instruction: str,
    current_directory: Path,
    max_output_tokens: int | None,
):
    workspace = detect_workspace_context(current_directory)
    capture = await _run_capture(request)
    git_metadata = await capture_git_metadata(workspace)
    raw_input = render_run_payload(capture, workspace, git_metadata)
    result = await compress_input(
        CompressionRequest(
            intent=intent,
            instruction=instruction,
            raw_input=raw_input,
            mode="run",
            cwd=str(current_directory),
            max_output_tokens=max_output_tokens,
            command=capture.command_display,
            command_args=list(capture.argv),
            command_exit_code=capture.exit_code,
            command_duration_ms=capture.duration_ms,
            stdout_hash=_hash_or_none(capture.stdout),
            stderr_hash=_hash_or_none(capture.stderr),
            git_head=git_metadata.git_head,
            git_branch=git_metadata.git_branch,
            git_dirty=git_metadata.git_dirty,
        )
    )
    return result, capture.exit_code


def _invoke_command_compression(
    ctx: typer.Context,
    intent: CompressionIntent,
    instruction: str,
    current_directory: Path,
    max_output_tokens: int | None,
    shell: bool,
):
    command = tuple(_command_args(ctx.args))
    if not command:
        command_name = ctx.info_name or "ctxsift"
        typer.echo(
            f"`ctxsift {command_name}` requires a command after `--`.",
            err=True,
        )
        raise typer.Exit(code=2)
    try:
        request = CommandExecutionRequest(
            argv=command,
            shell=shell,
            cwd=current_directory,
        )
    except ValueError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2) from error
    try:
        return asyncio.run(
            _run_command_flow(
                request=request,
                intent=intent,
                instruction=instruction,
                current_directory=current_directory,
                max_output_tokens=max_output_tokens,
            )
        )
    except CommandValidationError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2) from error


def _ensure_workspace_ready(config, current_directory: Path) -> None:
    asyncio.run(
        ensure_workspace_initialized(
            cwd=current_directory,
            config=config,
        )
    )


def _handle_missing_bootstrap_config_for_compress(
    ctx: typer.Context,
    instruction: str,
    command: tuple[str, ...],
    shell: bool,
) -> None:
    typer.echo(
        "[ctxsift warning] No workspace config, global config, or ctxsift env config is set yet. "
        "Run `ctxsift configure` first.",
        err=True,
    )
    if command or shell:
        result, exit_code = _invoke_raw_command_passthrough(
            ctx=ctx,
            current_directory=Path.cwd(),
            shell=shell,
        )
        typer.echo(_raw_command_output(result), nl=False)
        raise typer.Exit(code=exit_code)
    raw_input = sys.stdin.read()
    typer.echo(raw_input, nl=False)
    raise typer.Exit(code=0)


def _invoke_raw_command_passthrough(
    ctx: typer.Context,
    current_directory: Path,
    shell: bool,
):
    command = tuple(_command_args(ctx.args))
    if not command:
        command_name = ctx.info_name or "ctxsift"
        typer.echo(
            f"`ctxsift {command_name}` requires a command after `--`.",
            err=True,
        )
        raise typer.Exit(code=2)
    try:
        request = CommandExecutionRequest(
            argv=command,
            shell=shell,
            cwd=current_directory,
        )
    except ValueError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2) from error
    try:
        capture = asyncio.run(_run_capture(request))
        return capture, capture.exit_code
    except CommandValidationError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2) from error


def _raw_command_output(capture) -> str:
    if capture.stdout and capture.stderr:
        return f"{capture.stdout.rstrip()}\n{capture.stderr}"
    return capture.stdout or capture.stderr


def _command_args(extra_args: list[str]) -> list[str]:
    if not extra_args:
        return []
    if extra_args[0] == "--":
        return extra_args[1:]
    return extra_args


def _hash_or_none(text: str) -> str | None:
    if not text:
        return None
    from ctxsift.shared.hashing import sha256_text

    return sha256_text(text)


def _render_daemon_statuses(statuses: list[DaemonStatus]) -> str:
    if not statuses:
        return "No ctxsift daemons."
    return "\n".join(_render_daemon_status(status) for status in statuses)


def _render_daemon_status(status: DaemonStatus) -> str:
    healthy = "healthy" if status.healthy else "inactive"
    parts = [
        f"{status.role.value}",
        healthy,
        f"model={status.model}",
        f"device={status.device}",
    ]
    if status.pid is not None:
        parts.append(f"pid={status.pid}")
    if status.port is not None:
        parts.append(f"port={status.port}")
    if status.detail:
        parts.append(f"detail={status.detail}")
    return " ".join(parts)
