"""Agent-skill install prompts and host-specific installers."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
from importlib import resources
import json
import os
from pathlib import Path
from typing import Literal

import click
import typer

from ctxsift import __version__


class AgentSkillHost(str, Enum):
    """Supported agent hosts for skill installation."""

    COPILOT = "copilot"
    ANTIGRAVITY = "antigravity"
    CLAUDE_CODE = "claude-code"
    CODEX = "codex"
    CURSOR = "cursor"
    WINDSURF_CASCADE = "windsurf-cascade"
    CLINE = "cline"
    ROO_CODE = "roo-code"
    KILO_CODE = "kilo-code"
    CONTINUE = "continue"
    AIDER = "aider"
    OPENCODE = "opencode"
    GEMINI_CLI = "gemini-cli"
    QWEN_CODE = "qwen-code"
    KIRO = "kiro"
    JETBRAINS_JUNIE = "jetbrains-junie"
    OPENHANDS = "openhands"
    ZED_AGENT = "zed-agent"
    SOURCEGRAPH_AMP = "sourcegraph-amp"
    AUGMENT_AUGGIE = "augment-auggie"
    FACTORY_DROID = "factory-droid"
    AMAZON_Q_DEVELOPER = "amazon-q-developer"
    REPLIT_AGENT = "replit-agent"
    DEVIN = "devin"
    CODEGEN = "codegen"
    GOOGLE_JULES = "google-jules"
    OTHER = "other"


class AgentSkillScope(str, Enum):
    """Supported install scopes."""

    GLOBAL = "global"
    WORKSPACE = "workspace"
    CUSTOM = "custom"


@dataclass(frozen=True)
class AgentSkillSelection:
    """One host/scope choice collected during configure."""

    host: AgentSkillHost
    scope: AgentSkillScope
    target: Path | None = None


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


@dataclass(frozen=True)
class AgentSkillHostSpec:
    """One selectable host and its install capabilities."""

    host: AgentSkillHost
    display_name: str
    aliases: tuple[str, ...]
    global_supported: bool
    workspace_supported: bool
    global_note: str = ""
    workspace_note: str = ""
    global_default_target: str | None = None
    workspace_default_target: str | None = None
    selected_by_default: bool = False
    install_mode: Literal["builtin", "file", "managed_block", "custom"] = "file"


_MANAGED_BLOCK_START = "<!-- ctxsift:skill:start -->"
_MANAGED_BLOCK_END = "<!-- ctxsift:skill:end -->"


def prompt_for_agent_skill_install(workspace_root: Path) -> AgentSkillInstallPlan | None:
    """Collect optional skill-install preferences during configure."""
    typer.echo("")
    try:
        if not typer.confirm(
            "Install the CtxSift agent skill for supported coding agents?",
            default=False,
        ):
            return None
        selections = _prompt_selected_hosts()
        configured_selections: list[AgentSkillSelection] = []
        for host in selections:
            configured_selections.append(_prompt_selection_for_host(host, workspace_root))
        return AgentSkillInstallPlan(selections=tuple(configured_selections))
    except (click.Abort, EOFError):
        return None


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
            target = _target_path_for_selection(selection, workspace_root)
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
    spec = _spec_for_host(selection.host)
    if spec.install_mode == "builtin":
        return _install_builtin_skill(selection, workspace_root)
    if spec.install_mode == "custom":
        return _install_custom_skill(selection)
    if spec.install_mode in {"file", "managed_block"}:
        return _install_catalog_skill(selection, workspace_root)
    raise ValueError(f"Unsupported agent host: {selection.host}")


def _install_builtin_skill(
    selection: AgentSkillSelection,
    workspace_root: Path,
) -> AgentSkillInstallResult:
    host = selection.host
    if host is AgentSkillHost.COPILOT:
        return _install_copilot_skill(selection.scope, workspace_root)
    if host is AgentSkillHost.ANTIGRAVITY:
        return _install_antigravity_skill(selection.scope, workspace_root)
    if host is AgentSkillHost.CLAUDE_CODE:
        return _install_claude_code_skill(selection.scope, workspace_root)
    if host is AgentSkillHost.CODEX:
        return _install_codex_skill(selection.scope, workspace_root)
    raise ValueError(f"Unsupported built-in agent host: {host}")


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


def _install_custom_skill(selection: AgentSkillSelection) -> AgentSkillInstallResult:
    target = _require_custom_target(selection)
    changed = _write_text_file(target, _render_ctxsift_skill_markdown())
    return AgentSkillInstallResult(
        host=AgentSkillHost.OTHER,
        scope=AgentSkillScope.CUSTOM,
        ok=True,
        target=target,
        detail=_render_install_detail("Custom target", AgentSkillScope.CUSTOM, target, changed),
    )


def _prompt_selected_hosts() -> tuple[AgentSkillHost, ...]:
    ordered_hosts = _ordered_selectable_hosts()
    typer.echo("")
    typer.echo("Select one or more agent hosts.")
    for index, host in enumerate(ordered_hosts, start=1):
        typer.echo(_render_host_choice_line(index, host))
    while True:
        raw_value = typer.prompt(
            "Install for (numbers, ranges, names, or `all`)",
            default=_default_host_selection_text(ordered_hosts),
        )
        try:
            return _parse_host_selection(raw_value, ordered_hosts)
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


def _parse_host_selection(
    raw_value: str,
    ordered_hosts: tuple[AgentSkillHost, ...],
) -> tuple[AgentSkillHost, ...]:
    normalized = raw_value.strip().casefold()
    if not normalized:
        raise ValueError("Choose at least one agent host.")
    if normalized == "all":
        return tuple(
            host for host in ordered_hosts if _spec_for_host(host).install_mode != "custom"
        )
    parsed_hosts: list[AgentSkillHost] = []
    seen: set[AgentSkillHost] = set()
    for token in [item.strip() for item in raw_value.split(",") if item.strip()]:
        if token.isdigit():
            _append_host_by_index(token, ordered_hosts, parsed_hosts, seen)
            continue
        if "-" in token and _looks_like_index_range(token):
            _append_hosts_by_range(token, ordered_hosts, parsed_hosts, seen)
            continue
        host = _parse_host(token)
        if host not in seen:
            seen.add(host)
            parsed_hosts.append(host)
    if not parsed_hosts:
        raise ValueError("Choose at least one agent host.")
    return tuple(parsed_hosts)


def _parse_host(raw_value: str) -> AgentSkillHost:
    normalized = raw_value.strip().casefold().replace("_", "-")
    host = _host_aliases().get(normalized)
    if host is None:
        supported = ", ".join(spec.host.value for spec in _host_specs())
        raise ValueError(f"Unsupported agent host `{raw_value}`. Choose from: {supported}.")
    return host


def _prompt_scope_for_host(host: AgentSkillHost, workspace_root: Path) -> AgentSkillScope:
    spec = _spec_for_host(host)
    if spec.install_mode == "custom":
        return AgentSkillScope.CUSTOM
    if spec.global_supported and not spec.workspace_supported:
        target_note = _scope_target_note(host, workspace_root)
        typer.echo(f"{spec.display_name} currently installs only at global scope.\n{target_note}")
        return AgentSkillScope.GLOBAL
    if spec.workspace_supported and not spec.global_supported:
        target_note = _scope_target_note(host, workspace_root)
        typer.echo(
            f"{spec.display_name} currently installs only at workspace scope.\n{target_note}"
        )
        return AgentSkillScope.WORKSPACE
    target_note = _scope_target_note(host, workspace_root)
    typer.echo(f"{spec.display_name} targets:\n{target_note}")
    while True:
        raw_value = (
            typer.prompt(
                f"{spec.display_name} scope (global/workspace)",
                default="workspace",
            )
            .strip()
            .casefold()
        )
        if raw_value in {"global", "g"}:
            return AgentSkillScope.GLOBAL
        if raw_value in {"workspace", "w"}:
            return AgentSkillScope.WORKSPACE
        typer.echo("Invalid value. Choose `workspace` or `global`.", err=True)


def _prompt_selection_for_host(
    host: AgentSkillHost,
    workspace_root: Path,
) -> AgentSkillSelection:
    spec = _spec_for_host(host)
    scope = _prompt_scope_for_host(host, workspace_root)
    if spec.install_mode == "custom":
        target = _prompt_custom_target_path(workspace_root)
        typer.echo(f"Custom skill target: {target}")
        return AgentSkillSelection(host=host, scope=scope, target=target)
    if spec.install_mode == "builtin":
        return AgentSkillSelection(host=host, scope=scope)
    target = _prompt_catalog_target_path(host, scope, workspace_root)
    typer.echo(f"{_display_host_name(host)} target: {target}")
    return AgentSkillSelection(host=host, scope=scope, target=target)


def _prompt_custom_target_path(workspace_root: Path) -> Path:
    while True:
        raw_value = typer.prompt(
            "Custom skill path (SKILL.md file path or directory)",
            default=str(workspace_root / ".agents" / "skills" / "ctxsift"),
        ).strip()
        try:
            return _normalize_custom_target_path(raw_value, workspace_root)
        except ValueError as error:
            typer.echo(str(error), err=True)


def _normalize_custom_target_path(raw_value: str, workspace_root: Path) -> Path:
    if not raw_value:
        raise ValueError("Custom skill path cannot be empty.")
    raw_path = Path(raw_value).expanduser()
    candidate = raw_path if raw_path.is_absolute() else workspace_root / raw_path
    if _looks_like_directory_input(raw_value, candidate):
        return candidate / "SKILL.md"
    return candidate


def _looks_like_directory_input(raw_value: str, candidate: Path) -> bool:
    if raw_value.endswith(("/", "\\")) or candidate.is_dir():
        return True
    return candidate.name.casefold() != "skill.md" and candidate.suffix == ""


def _scope_target_note(host: AgentSkillHost, workspace_root: Path) -> str:
    spec = _spec_for_host(host)
    global_note = _target_note_for_scope(host, AgentSkillScope.GLOBAL, workspace_root)
    workspace_note = _target_note_for_scope(host, AgentSkillScope.WORKSPACE, workspace_root)
    if spec.global_supported and not spec.workspace_supported:
        return f"  global:    {global_note}"
    if spec.workspace_supported and not spec.global_supported:
        return f"  workspace: {workspace_note}"
    return f"  global:    {global_note}\n" f"  workspace: {workspace_note}"


def _target_path_for_host(
    host: AgentSkillHost,
    scope: AgentSkillScope,
    workspace_root: Path,
) -> Path:
    spec = _spec_for_host(host)
    if spec.install_mode == "builtin":
        return _builtin_target_path_for_host(host, scope, workspace_root)
    if spec.install_mode in {"file", "managed_block"}:
        return _resolved_catalog_target_path(host, scope, workspace_root)
    if spec.install_mode == "custom":
        raise ValueError("Custom targets must be resolved from the selection, not host/scope.")
    raise ValueError(f"Unsupported agent host: {host}")


def _builtin_target_path_for_host(
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
    raise ValueError(f"Unsupported built-in agent host: {host}")


def _target_path_for_selection(
    selection: AgentSkillSelection,
    workspace_root: Path,
) -> Path:
    if selection.host is AgentSkillHost.OTHER:
        return _require_custom_target(selection)
    return _target_path_for_host(selection.host, selection.scope, workspace_root)


def _require_custom_target(selection: AgentSkillSelection) -> Path:
    if selection.target is None:
        raise ValueError("Custom skill installation requires an explicit target path.")
    return selection.target


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
        resources.files("ctxsift").joinpath("agent_skill_template.md").read_text(encoding="utf-8")
    )
    return template.replace("{ctxsift_version}", __version__)


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
    return _spec_for_host(host).display_name


@lru_cache(maxsize=1)
def _host_specs() -> tuple[AgentSkillHostSpec, ...]:
    return _validate_host_specs(_load_catalog_specs())


def _load_catalog_specs() -> tuple[AgentSkillHostSpec, ...]:
    payload = json.loads(
        resources.files("ctxsift").joinpath("agent_hosts_catalog.json").read_text(encoding="utf-8")
    )
    specs: list[AgentSkillHostSpec] = []
    for item in payload:
        host = AgentSkillHost(str(item["name"]))
        specs.append(
            AgentSkillHostSpec(
                host=host,
                display_name=str(item["display_name"]),
                aliases=tuple(str(alias) for alias in item.get("aliases", [])),
                global_supported=bool(item.get("global_supported", False)),
                workspace_supported=bool(item.get("workspace_supported", False)),
                global_note=str(item.get("global_note", "")),
                workspace_note=str(item.get("workspace_note", "")),
                global_default_target=(
                    None
                    if item.get("global_default_target") is None
                    else str(item.get("global_default_target"))
                ),
                workspace_default_target=(
                    None
                    if item.get("workspace_default_target") is None
                    else str(item.get("workspace_default_target"))
                ),
                selected_by_default=bool(item.get("selected_by_default", False)),
                install_mode=cast_install_mode(str(item.get("install_mode", "file"))),
            )
        )
    return tuple(specs)


def cast_install_mode(raw_value: str) -> Literal["builtin", "file", "managed_block", "custom"]:
    if raw_value not in {"builtin", "file", "managed_block", "custom"}:
        raise ValueError(f"Unsupported install mode: {raw_value}")
    return raw_value  # type: ignore[return-value]


def _validate_host_specs(specs: tuple[AgentSkillHostSpec, ...]) -> tuple[AgentSkillHostSpec, ...]:
    seen_hosts: set[AgentSkillHost] = set()
    seen_aliases: dict[str, AgentSkillHost] = {}
    for spec in specs:
        if spec.host in seen_hosts:
            raise ValueError(f"Duplicate agent host definition: {spec.host.value}")
        seen_hosts.add(spec.host)
        if spec.install_mode == "builtin" and spec.host not in {
            AgentSkillHost.COPILOT,
            AgentSkillHost.ANTIGRAVITY,
            AgentSkillHost.CLAUDE_CODE,
            AgentSkillHost.CODEX,
        }:
            raise ValueError(f"Unsupported built-in install host in catalog: {spec.host.value}")
        if spec.install_mode == "custom" and spec.selected_by_default:
            raise ValueError(f"Custom-only host cannot be selected by default: {spec.host.value}")
        if spec.install_mode != "custom" and not (
            spec.global_supported or spec.workspace_supported
        ):
            raise ValueError(
                f"Host must support at least one install scope: {spec.host.value}",
            )
        for alias in _normalized_spec_aliases(spec):
            other_host = seen_aliases.get(alias)
            if other_host is not None and other_host is not spec.host:
                raise ValueError(
                    f"Agent host alias `{alias}` is defined for both "
                    f"{other_host.value} and {spec.host.value}.",
                )
            seen_aliases[alias] = spec.host
    missing_hosts = tuple(host.value for host in AgentSkillHost if host not in seen_hosts)
    if missing_hosts:
        raise ValueError(
            "Agent host catalog is missing definitions for: " + ", ".join(missing_hosts),
        )
    return specs


def _normalized_spec_aliases(spec: AgentSkillHostSpec) -> tuple[str, ...]:
    values = [
        spec.host.value,
        spec.display_name.casefold().replace(" ", "-"),
        *(alias.casefold().replace("_", "-") for alias in spec.aliases),
    ]
    return tuple(values)


def _host_aliases() -> dict[str, AgentSkillHost]:
    aliases: dict[str, AgentSkillHost] = {}
    for spec in _host_specs():
        aliases[spec.host.value] = spec.host
        aliases[spec.display_name.casefold().replace(" ", "-")] = spec.host
        for alias in spec.aliases:
            aliases[alias.casefold().replace("_", "-")] = spec.host
    return aliases


def _spec_for_host(host: AgentSkillHost) -> AgentSkillHostSpec:
    for spec in _host_specs():
        if spec.host is host:
            return spec
    raise ValueError(f"Unsupported agent host: {host}")


def _ordered_selectable_hosts() -> tuple[AgentSkillHost, ...]:
    return tuple(spec.host for spec in _host_specs())


def _render_host_choice_line(index: int, host: AgentSkillHost) -> str:
    spec = _spec_for_host(host)
    scope_bits: list[str] = []
    if spec.global_supported:
        scope_bits.append("global")
    if spec.workspace_supported:
        scope_bits.append("workspace")
    scope_text = "/".join(scope_bits) if scope_bits else "custom"
    return f"  {index}. {spec.display_name} [{scope_text}]"


def _default_host_selection_text(ordered_hosts: tuple[AgentSkillHost, ...]) -> str:
    index_map = {host: index for index, host in enumerate(ordered_hosts, start=1)}
    return ", ".join(
        str(index_map[spec.host])
        for spec in _host_specs()
        if spec.selected_by_default and spec.host in index_map
    )


def _append_host_by_index(
    token: str,
    ordered_hosts: tuple[AgentSkillHost, ...],
    parsed_hosts: list[AgentSkillHost],
    seen: set[AgentSkillHost],
) -> None:
    index = int(token)
    if index < 1 or index > len(ordered_hosts):
        raise ValueError(f"Invalid agent selection `{token}`.")
    host = ordered_hosts[index - 1]
    if host not in seen:
        seen.add(host)
        parsed_hosts.append(host)


def _append_hosts_by_range(
    token: str,
    ordered_hosts: tuple[AgentSkillHost, ...],
    parsed_hosts: list[AgentSkillHost],
    seen: set[AgentSkillHost],
) -> None:
    start_token, end_token = [part.strip() for part in token.split("-", maxsplit=1)]
    start_index = int(start_token)
    end_index = int(end_token)
    if start_index < 1 or end_index > len(ordered_hosts) or start_index > end_index:
        raise ValueError(f"Invalid agent selection range `{token}`.")
    for index in range(start_index, end_index + 1):
        host = ordered_hosts[index - 1]
        if host not in seen:
            seen.add(host)
            parsed_hosts.append(host)


def _looks_like_index_range(token: str) -> bool:
    parts = [part.strip() for part in token.split("-", maxsplit=1)]
    return len(parts) == 2 and all(part.isdigit() for part in parts)


def _target_note_for_scope(
    host: AgentSkillHost, scope: AgentSkillScope, workspace_root: Path
) -> str:
    spec = _spec_for_host(host)
    if scope is AgentSkillScope.GLOBAL:
        if not spec.global_supported:
            return "Not supported"
        default_target = _catalog_default_target_path(host, scope, workspace_root)
        if default_target is None:
            return spec.global_note or "Custom target path required."
        return f"{default_target} ({spec.global_note})" if spec.global_note else str(default_target)
    if not spec.workspace_supported:
        return "Not supported"
    default_target = _catalog_default_target_path(host, scope, workspace_root)
    if default_target is None:
        return spec.workspace_note or "Custom target path required."
    return (
        f"{default_target} ({spec.workspace_note})" if spec.workspace_note else str(default_target)
    )


def _catalog_default_target_path(
    host: AgentSkillHost,
    scope: AgentSkillScope,
    workspace_root: Path,
) -> Path | None:
    spec = _spec_for_host(host)
    raw_target = (
        spec.global_default_target
        if scope is AgentSkillScope.GLOBAL
        else spec.workspace_default_target
    )
    if raw_target is None:
        return None
    return _expand_catalog_target(raw_target, workspace_root)


def _expand_catalog_target(raw_target: str, workspace_root: Path) -> Path:
    expanded = raw_target.replace("<repo>", str(workspace_root))
    return Path(expanded).expanduser()


def _resolved_catalog_target_path(
    host: AgentSkillHost,
    scope: AgentSkillScope,
    workspace_root: Path,
) -> Path:
    target = _catalog_default_target_path(host, scope, workspace_root)
    if target is None:
        raise ValueError(
            f"{_display_host_name(host)} requires an explicit target path for {scope.value} scope."
        )
    return target


def _prompt_catalog_target_path(
    host: AgentSkillHost,
    scope: AgentSkillScope,
    workspace_root: Path,
) -> Path:
    spec = _spec_for_host(host)
    note = spec.global_note if scope is AgentSkillScope.GLOBAL else spec.workspace_note
    if note:
        typer.echo(f"{spec.display_name} documented {scope.value} locations:\n  {note}")
    default_target = _catalog_default_target_path(host, scope, workspace_root)
    while True:
        raw_value = typer.prompt(
            f"{spec.display_name} target path",
            default=str(default_target) if default_target is not None else "",
            show_default=default_target is not None,
        ).strip()
        try:
            return _normalize_custom_target_path(raw_value, workspace_root)
        except ValueError as error:
            typer.echo(str(error), err=True)


def _install_catalog_skill(
    selection: AgentSkillSelection,
    workspace_root: Path,
) -> AgentSkillInstallResult:
    spec = _spec_for_host(selection.host)
    target = selection.target or _resolved_catalog_target_path(
        selection.host,
        selection.scope,
        workspace_root,
    )
    content = _render_ctxsift_skill_markdown()
    if spec.install_mode == "managed_block":
        changed = _write_managed_markdown_block(target, content)
    else:
        changed = _write_text_file(target, content)
    return AgentSkillInstallResult(
        host=selection.host,
        scope=selection.scope,
        ok=True,
        target=target,
        detail=_render_install_detail(spec.display_name, selection.scope, target, changed),
    )


def _write_managed_markdown_block(path: Path, content: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    managed_block = f"{_MANAGED_BLOCK_START}\n" f"{content.rstrip()}\n" f"{_MANAGED_BLOCK_END}\n"
    if not path.exists():
        path.write_text(managed_block, encoding="utf-8")
        return True
    original = path.read_text(encoding="utf-8")
    if _MANAGED_BLOCK_START in original and _MANAGED_BLOCK_END in original:
        updated = _replace_managed_block(original, managed_block)
    else:
        separator = "\n\n" if original and not original.endswith("\n\n") else ""
        if original.endswith("\n"):
            separator = "\n" if not original.endswith("\n\n") else ""
        updated = (
            f"{original.rstrip()}{separator}{managed_block}" if original.strip() else managed_block
        )
    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def _replace_managed_block(original: str, managed_block: str) -> str:
    start_index = original.index(_MANAGED_BLOCK_START)
    end_index = original.index(_MANAGED_BLOCK_END, start_index) + len(_MANAGED_BLOCK_END)
    suffix = original[end_index:]
    if suffix.startswith("\r\n"):
        suffix = suffix[2:]
    elif suffix.startswith("\n"):
        suffix = suffix[1:]
    return f"{original[:start_index]}{managed_block}{suffix}"
