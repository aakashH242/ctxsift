"""Command-line interface for ctxsift."""

from __future__ import annotations

import asyncio
from pathlib import Path
import sys
from typing import Annotated

import typer
from pydantic import ValidationError

from ctxsift.compression import compress_input
from ctxsift.config import (
    ConfigResolutionRequest,
    ConfigWriteRequest,
    render_resolved_config,
    resolve_config,
    set_config_value,
)
from ctxsift.doctor import collect_doctor_report, render_doctor_report
from ctxsift.git_metadata import capture_git_metadata
from ctxsift.recall import recall_records, render_recall_records
from ctxsift.run_capture import (
    capture_launch_failure,
    render_command,
    render_run_payload,
    run_command,
)
from ctxsift.storage import initialize_database
from ctxsift.types import CompressionRequest
from ctxsift.workspace import detect_workspace_context

app = typer.Typer(
    add_completion=False,
    help="Local-first command output compression and recall.",
    no_args_is_help=True,
)
config_app = typer.Typer(help="Inspect or update configuration.")

app.add_typer(config_app, name="config")


def _not_implemented(command_name: str) -> None:
    typer.echo(f"`ctxsift {command_name}` is scaffolded but not implemented yet.")
    raise typer.Exit(code=1)


@app.command()
def init(
    write_ignore: Annotated[
        bool,
        typer.Option(
            "--write-ignore", help="Write ignore entries during workspace initialization."
        ),
    ] = False,
) -> None:
    """Initialize the workspace database and local metadata."""
    result = resolve_config(
        ConfigResolutionRequest(
            cwd=Path.cwd(),
        )
    )
    db_path = Path(result.config.db_path or "").expanduser() if result.config.db_path else None
    target_path = db_path or Path(result.write_path).with_name("ctxsift.db")
    init_result = asyncio.run(initialize_database(target_path))
    typer.echo(f"Initialized workspace database at {init_result.db_path}")
    if write_ignore:
        typer.echo("Ignore file updates are not implemented yet; no ignore files were changed.")


@app.command()
def compress(
    instruction: Annotated[
        str, typer.Argument(help="Compression instruction for the provided input.")
    ],
    max_output_tokens: Annotated[
        int | None,
        typer.Option("--max-output-tokens", help="Override the maximum output token budget."),
    ] = None,
) -> None:
    """Compress stdin using an instruction."""
    raw_input = sys.stdin.read()
    result = asyncio.run(
        compress_input(
            CompressionRequest(
                instruction=instruction,
                raw_input=raw_input,
                cwd=str(Path.cwd()),
                max_output_tokens=max_output_tokens,
            )
        )
    )
    typer.echo(result.compressed_output)


@app.command(context_settings={"allow_extra_args": True, "ignore_unknown_options": True})
def run(
    ctx: typer.Context,
    instruction: Annotated[
        str, typer.Argument(help="Compression instruction for the command output.")
    ],
    max_output_tokens: Annotated[
        int | None,
        typer.Option("--max-output-tokens", help="Override the maximum output token budget."),
    ] = None,
) -> None:
    """Run a command, capture its output, and compress it."""
    command = _command_args(ctx.args)
    if not command:
        typer.echo("`ctxsift run` requires a command after `--`.", err=True)
        raise typer.Exit(code=2)
    result, exit_code = asyncio.run(
        _run_command_flow(
            command=command,
            instruction=instruction,
            current_directory=Path.cwd(),
            max_output_tokens=max_output_tokens,
        )
    )
    typer.echo(result.compressed_output)
    raise typer.Exit(code=exit_code)


@app.command()
def recall(
    query: Annotated[str, typer.Argument(help="Query used to search prior compressed records.")],
    files: Annotated[
        list[str] | None,
        typer.Option("--files", help="File paths used to filter or boost recall results."),
    ] = None,
) -> None:
    """Recall previously stored compressed records."""
    results = asyncio.run(
        recall_records(
            query=query,
            cwd=Path.cwd(),
            file_filters=files,
        )
    )
    typer.echo(render_recall_records(results))


@config_app.command("show")
def config_show(
    global_scope: Annotated[
        bool,
        typer.Option("--global", help="Force the global config file instead of workspace config."),
    ] = False,
) -> None:
    """Show the resolved configuration."""
    result = resolve_config(
        ConfigResolutionRequest(
            cwd=Path.cwd(),
            force_global=global_scope,
        )
    )
    typer.echo(render_resolved_config(result))


@config_app.command("set")
def config_set(
    key: Annotated[str, typer.Argument(help="Supported config key to update.")],
    value: Annotated[str, typer.Argument(help="Value to set for the given config key.")],
    global_scope: Annotated[
        bool,
        typer.Option("--global", help="Force the global config file instead of workspace config."),
    ] = False,
) -> None:
    """Set one configuration value."""
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
    typer.echo(render_doctor_report(report))


async def _run_capture(command: list[str], current_directory: Path):
    try:
        return await run_command(command, current_directory)
    except FileNotFoundError as error:
        return capture_launch_failure(command, current_directory, error)


async def _run_command_flow(
    command: list[str],
    instruction: str,
    current_directory: Path,
    max_output_tokens: int | None,
):
    workspace = detect_workspace_context(current_directory)
    capture = await _run_capture(command, current_directory)
    git_metadata = await capture_git_metadata(workspace)
    raw_input = render_run_payload(capture, workspace, git_metadata)
    result = await compress_input(
        CompressionRequest(
            instruction=instruction,
            raw_input=raw_input,
            mode="run",
            cwd=str(current_directory),
            max_output_tokens=max_output_tokens,
            command=render_command(capture.command),
            command_args=capture.command,
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


def _command_args(extra_args: list[str]) -> list[str]:
    if not extra_args:
        return []
    if extra_args[0] == "--":
        return extra_args[1:]
    return extra_args


def _hash_or_none(text: str) -> str | None:
    if not text:
        return None
    from ctxsift.compression import sha256_text

    return sha256_text(text)
