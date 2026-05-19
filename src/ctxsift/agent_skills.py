"""Agent-skill install prompts and host-specific installers."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from importlib import resources
import json
import os
from pathlib import Path

import typer

from ctxsift import __version__


class AgentSkillHost(str, Enum):
    """Supported agent hosts for skill installation."""

    COPILOT = "copilot"
    ANTIGRAVITY = "antigravity"
    CLAUDE_CODE = "claude-code"
    CODEX = "codex"


class AgentSkillScope(str, Enum):
    """Supported install scopes."""

    GLOBAL = "global"
    WORKSPACE = "workspace"


@dataclass(frozen=True)
class AgentSkillSelection:
    """One host/scope choice collected during configure."""

    host: AgentSkillHost
    scope: AgentSkillScope


@dataclass(frozen=True)
class AgentSkillInstallPlan:
    """Structured multi-host install request."""

    selections: tuple[AgentSkillSelection, ...]


@dataclass(frozen=True)
class AgentSkillInstallResult:
    """Result for one installed host skill."""

    host: AgentSkillHost
    scope: AgentSkillScope
    ok: bool
    target: Path
    detail: str


def prompt_for_agent_skill_install(workspace_root: Path) -> AgentSkillInstallPlan | None:
    """Collect optional skill-install preferences during configure."""
    typer.echo("")
    if not typer.confirm(
        "Install the CtxSift agent skill for supported coding agents?",
        default=False,
    ):
        return None
    typer.echo("")
    typer.echo(
        "Agents: copilot, antigravity, claude-code, codex\n"
        "Enter one or more names separated by commas."
    )
    selections = _prompt_selected_hosts()
    configured_selections: list[AgentSkillSelection] = []
    for host in selections:
        scope = _prompt_scope_for_host(host, workspace_root)
        configured_selections.append(AgentSkillSelection(host=host, scope=scope))
    return AgentSkillInstallPlan(selections=tuple(configured_selections))


def install_agent_skills(
    plan: AgentSkillInstallPlan | None,
    workspace_root: Path,
) -> list[AgentSkillInstallResult]:
    """Install the CtxSift skill for all selected hosts."""
    if plan is None:
        return []
    results: list[AgentSkillInstallResult] = []
    for selection in plan.selections:
        try:
            results.append(_install_selection(selection, workspace_root))
        except OSError as error:
            target = _target_path_for_host(selection.host, selection.scope, workspace_root)
            results.append(
                AgentSkillInstallResult(
                    host=selection.host,
                    scope=selection.scope,
                    ok=False,
                    target=target,
                    detail=(
                        f"Failed to install CtxSift skill for {_display_host_name(selection.host)} "
                        f"({selection.scope.value}) at {target}: {error}"
                    ),
                )
            )
    return results


def _install_selection(
    selection: AgentSkillSelection,
    workspace_root: Path,
) -> AgentSkillInstallResult:
    if selection.host is AgentSkillHost.COPILOT:
        return _install_copilot_skill(selection.scope, workspace_root)
    if selection.host is AgentSkillHost.ANTIGRAVITY:
        return _install_antigravity_skill(selection.scope, workspace_root)
    if selection.host is AgentSkillHost.CLAUDE_CODE:
        return _install_claude_code_skill(selection.scope, workspace_root)
    if selection.host is AgentSkillHost.CODEX:
        return _install_codex_skill(selection.scope, workspace_root)
    raise ValueError(f"Unsupported agent host: {selection.host}")


def _install_copilot_skill(
    scope: AgentSkillScope,
    workspace_root: Path,
) -> AgentSkillInstallResult:
    target = _copilot_skill_path(scope, workspace_root)
    changed = _write_text_file(target, _render_ctxsift_skill_markdown())
    return AgentSkillInstallResult(
        host=AgentSkillHost.COPILOT,
        scope=scope,
        ok=True,
        target=target,
        detail=_render_install_detail("Copilot", scope, target, changed),
    )


def _install_claude_code_skill(
    scope: AgentSkillScope,
    workspace_root: Path,
) -> AgentSkillInstallResult:
    target = _claude_code_skill_path(scope, workspace_root)
    changed = _write_text_file(target, _render_ctxsift_skill_markdown())
    return AgentSkillInstallResult(
        host=AgentSkillHost.CLAUDE_CODE,
        scope=scope,
        ok=True,
        target=target,
        detail=_render_install_detail("Claude Code", scope, target, changed),
    )


def _install_codex_skill(
    scope: AgentSkillScope,
    workspace_root: Path,
) -> AgentSkillInstallResult:
    target = _codex_skill_path(scope, workspace_root)
    changed = _write_text_file(target, _render_ctxsift_skill_markdown())
    return AgentSkillInstallResult(
        host=AgentSkillHost.CODEX,
        scope=scope,
        ok=True,
        target=target,
        detail=_render_install_detail("Codex", scope, target, changed),
    )


def _install_antigravity_skill(
    scope: AgentSkillScope,
    workspace_root: Path,
) -> AgentSkillInstallResult:
    plugin_root = _antigravity_plugin_root(scope, workspace_root)
    target = plugin_root / "skills" / "ctxsift" / "SKILL.md"
    skill_changed = _write_text_file(target, _render_ctxsift_skill_markdown())
    manifest_changed = _write_text_file(
        plugin_root / "plugin.json",
        _render_antigravity_plugin_manifest(),
    )
    changed = skill_changed or manifest_changed
    return AgentSkillInstallResult(
        host=AgentSkillHost.ANTIGRAVITY,
        scope=scope,
        ok=True,
        target=target,
        detail=_render_install_detail("Antigravity", scope, target, changed),
    )


def _prompt_selected_hosts() -> tuple[AgentSkillHost, ...]:
    while True:
        raw_value = typer.prompt(
            "Install for (comma-separated)",
            default="copilot, antigravity, claude-code, codex",
        )
        try:
            return _parse_selected_hosts(raw_value)
        except ValueError as error:
            typer.echo(str(error), err=True)


def _parse_selected_hosts(raw_value: str) -> tuple[AgentSkillHost, ...]:
    raw_items = [item.strip() for item in raw_value.split(",")]
    normalized_items = [item for item in raw_items if item]
    if not normalized_items:
        raise ValueError("Choose at least one agent host.")
    parsed_hosts: list[AgentSkillHost] = []
    seen: set[AgentSkillHost] = set()
    for item in normalized_items:
        host = _parse_host(item)
        if host not in seen:
            seen.add(host)
            parsed_hosts.append(host)
    return tuple(parsed_hosts)


def _parse_host(raw_value: str) -> AgentSkillHost:
    normalized = raw_value.strip().casefold().replace("_", "-")
    aliases = {
        "copilot": AgentSkillHost.COPILOT,
        "github-copilot": AgentSkillHost.COPILOT,
        "antigravity": AgentSkillHost.ANTIGRAVITY,
        "anti-gravity": AgentSkillHost.ANTIGRAVITY,
        "claude": AgentSkillHost.CLAUDE_CODE,
        "claude-code": AgentSkillHost.CLAUDE_CODE,
        "codex": AgentSkillHost.CODEX,
    }
    host = aliases.get(normalized)
    if host is None:
        supported = ", ".join(host.value for host in AgentSkillHost)
        raise ValueError(f"Unsupported agent host `{raw_value}`. Choose from: {supported}.")
    return host


def _prompt_scope_for_host(host: AgentSkillHost, workspace_root: Path) -> AgentSkillScope:
    if host is AgentSkillHost.CODEX:
        target = _codex_skill_path(AgentSkillScope.GLOBAL, workspace_root)
        typer.echo(f"Codex currently installs only at global scope: {target}")
        return AgentSkillScope.GLOBAL
    target_note = _scope_target_note(host, workspace_root)
    typer.echo(f"{_display_host_name(host)} targets:\n{target_note}")
    while True:
        raw_value = typer.prompt(
            f"{_display_host_name(host)} scope (global/workspace)",
            default="workspace",
        ).strip().casefold()
        if raw_value in {"global", "g"}:
            return AgentSkillScope.GLOBAL
        if raw_value in {"workspace", "w"}:
            return AgentSkillScope.WORKSPACE
        typer.echo("Invalid value. Choose `workspace` or `global`.", err=True)


def _scope_target_note(host: AgentSkillHost, workspace_root: Path) -> str:
    global_target = _target_path_for_host(host, AgentSkillScope.GLOBAL, workspace_root)
    workspace_target = _target_path_for_host(host, AgentSkillScope.WORKSPACE, workspace_root)
    return (
        f"  global:    {global_target}\n"
        f"  workspace: {workspace_target}"
    )


def _target_path_for_host(
    host: AgentSkillHost,
    scope: AgentSkillScope,
    workspace_root: Path,
) -> Path:
    if host is AgentSkillHost.COPILOT:
        return _copilot_skill_path(scope, workspace_root)
    if host is AgentSkillHost.ANTIGRAVITY:
        return _antigravity_plugin_root(scope, workspace_root) / "skills" / "ctxsift" / "SKILL.md"
    if host is AgentSkillHost.CLAUDE_CODE:
        return _claude_code_skill_path(scope, workspace_root)
    if host is AgentSkillHost.CODEX:
        return _codex_skill_path(scope, workspace_root)
    raise ValueError(f"Unsupported agent host: {host}")


def _copilot_skill_path(scope: AgentSkillScope, workspace_root: Path) -> Path:
    if scope is AgentSkillScope.GLOBAL:
        return Path.home() / ".copilot" / "skills" / "ctxsift" / "SKILL.md"
    return workspace_root / ".github" / "skills" / "ctxsift" / "SKILL.md"


def _claude_code_skill_path(scope: AgentSkillScope, workspace_root: Path) -> Path:
    if scope is AgentSkillScope.GLOBAL:
        return Path.home() / ".claude" / "skills" / "ctxsift" / "SKILL.md"
    return workspace_root / ".claude" / "skills" / "ctxsift" / "SKILL.md"


def _codex_skill_path(scope: AgentSkillScope, workspace_root: Path) -> Path:
    del workspace_root
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    if scope is not AgentSkillScope.GLOBAL:
        raise ValueError("Codex skill installation currently supports only global scope.")
    return codex_home / "skills" / "ctxsift" / "SKILL.md"


def _antigravity_plugin_root(scope: AgentSkillScope, workspace_root: Path) -> Path:
    if scope is AgentSkillScope.GLOBAL:
        return Path.home() / ".gemini" / "config" / "plugins" / "ctxsift"
    hidden_root = workspace_root / ".agents" / "plugins"
    underscored_root = workspace_root / "_agents" / "plugins"
    if underscored_root.exists() and not hidden_root.exists():
        return underscored_root / "ctxsift"
    return hidden_root / "ctxsift"


def _render_ctxsift_skill_markdown() -> str:
    template = (
        resources.files("ctxsift")
        .joinpath("agent_skill_template.md")
        .read_text(encoding="utf-8")
    )
    return template.format(ctxsift_version=__version__)


def _render_antigravity_plugin_manifest() -> str:
    return json.dumps({"name": "ctxsift"}, indent=2) + "\n"


def _write_text_file(path: Path, content: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def _render_install_detail(
    host_name: str,
    scope: AgentSkillScope,
    target: Path,
    changed: bool,
) -> str:
    action = "Installed" if changed else "Already current"
    return f"{action} CtxSift skill for {host_name} ({scope.value}) at {target}"


def _display_host_name(host: AgentSkillHost) -> str:
    if host is AgentSkillHost.COPILOT:
        return "Copilot"
    if host is AgentSkillHost.ANTIGRAVITY:
        return "Antigravity"
    if host is AgentSkillHost.CLAUDE_CODE:
        return "Claude Code"
    if host is AgentSkillHost.CODEX:
        return "Codex"
    raise ValueError(f"Unsupported agent host: {host}")
