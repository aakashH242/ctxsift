"""Tests for agent skill install helpers."""

from pathlib import Path

import pytest

from ctxsift.agent.skills import (
    AgentSkillHost,
    AgentSkillInstallPlan,
    AgentSkillScope,
    AgentSkillSelection,
    _normalize_custom_target_path,
    _parse_selected_hosts,
    install_agent_skills,
)


def test_parse_selected_hosts_accepts_other_alias() -> None:
    hosts = _parse_selected_hosts("codex, other, claude")

    assert hosts == (
        AgentSkillHost.CODEX,
        AgentSkillHost.OTHER,
        AgentSkillHost.CLAUDE_CODE,
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
