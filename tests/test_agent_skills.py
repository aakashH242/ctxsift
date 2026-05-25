"""Tests for agent skill install helpers."""

from pathlib import Path

import pytest

from ctxsift.agent.skills import (
    AgentSkillHost,
    AgentSkillHostSpec,
    AgentSkillInstallPlan,
    AgentSkillScope,
    AgentSkillSelection,
    _default_host_selection_text,
    _ordered_selectable_hosts,
    _parse_host_selection,
    _normalize_custom_target_path,
    _parse_selected_hosts,
    _validate_host_specs,
    install_agent_skills,
)


def test_parse_selected_hosts_accepts_other_alias() -> None:
    hosts = _parse_selected_hosts("codex, other, claude")

    assert hosts == (
        AgentSkillHost.CODEX,
        AgentSkillHost.OTHER,
        AgentSkillHost.CLAUDE_CODE,
    )


def test_parse_host_selection_accepts_numbers_and_ranges() -> None:
    ordered_hosts = _ordered_selectable_hosts()

    hosts = _parse_host_selection("1, 3-4", ordered_hosts)

    assert hosts == (
        AgentSkillHost.COPILOT,
        AgentSkillHost.CLAUDE_CODE,
        AgentSkillHost.CODEX,
    )


def test_parse_host_selection_accepts_all_and_excludes_custom_other() -> None:
    ordered_hosts = _ordered_selectable_hosts()

    hosts = _parse_host_selection("all", ordered_hosts)

    assert AgentSkillHost.OTHER not in hosts
    assert AgentSkillHost.CURSOR in hosts


def test_default_host_selection_text_prefers_builtin_hosts() -> None:
    ordered_hosts = _ordered_selectable_hosts()

    assert _default_host_selection_text(ordered_hosts) == "1, 2, 3, 4"


def test_validate_host_specs_rejects_duplicate_aliases() -> None:
    with pytest.raises(ValueError, match="alias `shared`"):
        _validate_host_specs(
            (
                AgentSkillHostSpec(
                    host=AgentSkillHost.COPILOT,
                    display_name="Copilot",
                    aliases=("shared",),
                    global_supported=True,
                    workspace_supported=True,
                    install_mode="builtin",
                ),
                AgentSkillHostSpec(
                    host=AgentSkillHost.CURSOR,
                    display_name="Cursor",
                    aliases=("shared",),
                    global_supported=True,
                    workspace_supported=True,
                ),
            )
        )


def test_validate_host_specs_requires_every_declared_host() -> None:
    with pytest.raises(ValueError, match="missing definitions for: codex"):
        _validate_host_specs(
            tuple(
                AgentSkillHostSpec(
                    host=host,
                    display_name=host.value.title(),
                    aliases=(host.value,),
                    global_supported=True,
                    workspace_supported=True,
                    install_mode="builtin" if host is AgentSkillHost.COPILOT else "file",
                )
                for host in AgentSkillHost
                if host is not AgentSkillHost.CODEX
            )
        )


def test_normalize_custom_target_path_uses_workspace_for_relative_file(
    tmp_path: Path,
) -> None:
    target = _normalize_custom_target_path(".agents/custom/ctxsift.md", tmp_path)

    assert target == tmp_path / ".agents" / "custom" / "ctxsift.md"


def test_normalize_custom_target_path_appends_skill_filename_for_directories(
    tmp_path: Path,
) -> None:
    target = _normalize_custom_target_path(".agents/custom/", tmp_path)

    assert target == tmp_path / ".agents" / "custom" / "SKILL.md"


def test_normalize_custom_target_path_treats_nonexistent_default_dir_as_directory(
    tmp_path: Path,
) -> None:
    target = _normalize_custom_target_path(".agents/skills/ctxsift", tmp_path)

    assert target == tmp_path / ".agents" / "skills" / "ctxsift" / "SKILL.md"


def test_install_agent_skills_writes_custom_target(
    tmp_path: Path,
) -> None:
    target = tmp_path / "custom-skills" / "ctxsift" / "SKILL.md"

    results = install_agent_skills(
        plan=AgentSkillInstallPlan(
            selections=(
                AgentSkillSelection(
                    host=AgentSkillHost.OTHER,
                    scope=AgentSkillScope.CUSTOM,
                    target=target,
                ),
            )
        ),
        workspace_root=tmp_path,
    )

    assert len(results) == 1
    assert results[0].ok is True
    assert results[0].target == target
    assert target.exists()
    assert "CtxSift" in target.read_text(encoding="utf-8")


def test_install_agent_skills_writes_catalog_host_target(
    tmp_path: Path,
) -> None:
    target = tmp_path / ".cursor" / "skills" / "ctxsift" / "SKILL.md"

    results = install_agent_skills(
        plan=AgentSkillInstallPlan(
            selections=(
                AgentSkillSelection(
                    host=AgentSkillHost.CURSOR,
                    scope=AgentSkillScope.WORKSPACE,
                    target=target,
                ),
            )
        ),
        workspace_root=tmp_path,
    )

    assert len(results) == 1
    assert results[0].ok is True
    assert results[0].target == target
    assert target.exists()
    assert "CtxSift" in target.read_text(encoding="utf-8")


def test_install_agent_skills_writes_builtin_host_target_from_catalog(
    tmp_path: Path,
) -> None:
    results = install_agent_skills(
        plan=AgentSkillInstallPlan(
            selections=(
                AgentSkillSelection(
                    host=AgentSkillHost.COPILOT,
                    scope=AgentSkillScope.WORKSPACE,
                ),
            )
        ),
        workspace_root=tmp_path,
    )

    target = tmp_path / ".github" / "skills" / "ctxsift" / "SKILL.md"
    assert len(results) == 1
    assert results[0].ok is True
    assert results[0].target == target
    assert target.exists()
    assert "CtxSift" in target.read_text(encoding="utf-8")


def test_install_agent_skills_uses_catalog_default_target_when_target_missing(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    home_dir = tmp_path / "home"
    monkeypatch.setenv("USERPROFILE", str(home_dir))
    monkeypatch.setenv("HOME", str(home_dir))

    results = install_agent_skills(
        plan=AgentSkillInstallPlan(
            selections=(
                AgentSkillSelection(
                    host=AgentSkillHost.CURSOR,
                    scope=AgentSkillScope.GLOBAL,
                ),
            )
        ),
        workspace_root=tmp_path,
    )

    expected = home_dir / ".cursor" / "skills" / "ctxsift" / "SKILL.md"
    assert len(results) == 1
    assert results[0].target == expected
    assert expected.exists()


def test_install_agent_skills_manages_shared_instruction_file_without_overwrite(
    tmp_path: Path,
) -> None:
    target = tmp_path / "GEMINI.md"
    target.write_text("Project instructions\n", encoding="utf-8")

    results = install_agent_skills(
        plan=AgentSkillInstallPlan(
            selections=(
                AgentSkillSelection(
                    host=AgentSkillHost.GEMINI_CLI,
                    scope=AgentSkillScope.WORKSPACE,
                    target=target,
                ),
            )
        ),
        workspace_root=tmp_path,
    )

    assert len(results) == 1
    assert results[0].ok is True
    rendered = target.read_text(encoding="utf-8")
    assert "Project instructions" in rendered
    assert "<!-- ctxsift:skill:start -->" in rendered
    assert "<!-- ctxsift:skill:end -->" in rendered


def test_install_agent_skills_requires_custom_target(
    tmp_path: Path,
) -> None:
    with pytest.raises(ValueError, match="explicit target path"):
        install_agent_skills(
            plan=AgentSkillInstallPlan(
                selections=(
                    AgentSkillSelection(
                        host=AgentSkillHost.OTHER,
                        scope=AgentSkillScope.CUSTOM,
                    ),
                )
            ),
            workspace_root=tmp_path,
        )
