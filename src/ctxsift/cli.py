"""Command-line interface for ctxsift."""

from __future__ import annotations

from typing import Annotated

import typer


app = typer.Typer(
    add_completion=False,
    help="Local-first command output compression and recall.",
    no_args_is_help=True,
)


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


@app.command()
def config(
    target: Annotated[
        str | None,
        typer.Argument(help="Optional config target such as 'show' or a setting key."),
    ] = None,
) -> None:
    """Inspect or update configuration."""
    _ = target
    _not_implemented("config")


@app.command()
def doctor() -> None:
    """Inspect runtime health and optional features."""
    _not_implemented("doctor")
