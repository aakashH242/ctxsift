"""Command-line interface for ctxsift."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from pydantic import ValidationError

from ctxsift.config import (
    ConfigResolutionRequest,
    ConfigWriteRequest,
    render_resolved_config,
    resolve_config,
    set_config_value,
)

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
        typer.Option("--write-ignore", help="Write ignore entries during workspace initialization."),
    ] = False,
) -> None:
    """Initialize the workspace database and local metadata."""
    _ = write_ignore
    _not_implemented("init")


@app.command()
def compress(
    instruction: Annotated[str, typer.Argument(help="Compression instruction for the provided input.")],
) -> None:
    """Compress stdin using an instruction."""
    _not_implemented("compress")


@app.command(context_settings={"allow_extra_args": True, "ignore_unknown_options": True})
def run(
    ctx: typer.Context,
    instruction: Annotated[str, typer.Argument(help="Compression instruction for the command output.")],
) -> None:
    """Run a command, capture its output, and compress it."""
    _ = ctx.args
    _ = instruction
    _not_implemented("run")


@app.command()
def recall(
    query: Annotated[str, typer.Argument(help="Query used to search prior compressed records.")],
    files: Annotated[
        list[str] | None,
        typer.Option("--files", help="File paths used to filter or boost recall results."),
    ] = None,
) -> None:
    """Recall previously stored compressed records."""
    _ = query
    _ = files
    _not_implemented("recall")


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
    _not_implemented("doctor")
