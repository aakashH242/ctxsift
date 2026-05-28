from __future__ import annotations

import asyncio
import importlib.util
import json
from pathlib import Path
import sys

import pytest


def load_module(module_name: str, module_path: Path):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


no_repeat = load_module("no_repeat", Path(__file__).resolve().parents[1] / "no_repeat.py")
hook_module = load_module(
    "run_no_repeat_hook",
    Path(__file__).resolve().parents[1] / "tools" / "run_no_repeat_hook.py",
)


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_stage_changed_files_stages_exact_relative_paths(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    recorded: list[list[str]] = []

    def fake_run(args: list[str], check: bool) -> None:
        assert check is True
        recorded.append(args)

    monkeypatch.setattr(hook_module.subprocess, "run", fake_run)

    first = tmp_path / "README.md"
    second = tmp_path / "docs" / "guide.md"
    second.parent.mkdir()
    first.write_text("", encoding="utf-8")
    second.write_text("", encoding="utf-8")

    hook_module.stage_changed_files(tmp_path, [first, second])

    assert recorded == [
        [
            "git",
            "-C",
            str(tmp_path),
            "add",
            "--",
            "README.md",
            "docs\\guide.md",
        ]
    ]


def test_hook_main_returns_zero_when_config_missing(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(hook_module, "REPO_ROOT", tmp_path)

    exit_code = asyncio.run(hook_module.main())

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Skipping no_repeat hook" in captured.out


def test_hook_main_restages_changed_files(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    config_path = tmp_path / ".no-repeat.json"
    readme = tmp_path / "README.md"
    readme.write_text("Site: <%=public_site_url=%>\n", encoding="utf-8")
    write_json(
        config_path,
        {
            "strings_to_template": [
                {
                    "value": "https://ctxsift.dev",
                    "pattern": "<%=public_site_url=%>",
                    "locations": ["README.md"],
                }
            ]
        },
    )
    monkeypatch.setattr(hook_module, "REPO_ROOT", tmp_path)

    staged: list[tuple[Path, list[Path]]] = []

    def fake_stage(repo_root: Path, changed_files: list[Path]) -> None:
        staged.append((repo_root, changed_files))

    monkeypatch.setattr(hook_module, "stage_changed_files", fake_stage)

    exit_code = asyncio.run(hook_module.main())

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Processed 1 files: 1 changed, 0 unchanged, 1 replacements." in captured.out
    assert staged == [(tmp_path, [readme])]


def test_hook_main_honors_fail_on_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    config_path = tmp_path / ".no-repeat.json"
    write_json(
        config_path,
        {
            "fail_on_error": True,
            "strings_to_template": [
                {
                    "value": "https://ctxsift.dev",
                    "pattern": "<%=public_site_url=%>",
                    "locations": ["missing-dir"],
                }
            ],
        },
    )
    monkeypatch.setattr(hook_module, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(hook_module, "stage_changed_files", lambda *args, **kwargs: None)

    exit_code = asyncio.run(hook_module.main())

    captured = capsys.readouterr()
    assert exit_code == 1
    assert "fail_on_error is true" in captured.out
