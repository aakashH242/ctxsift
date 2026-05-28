from __future__ import annotations

import asyncio
import importlib.util
import json
from pathlib import Path
import sys

import pytest


def load_no_repeat_module():
    module_path = Path(__file__).resolve().parents[1] / "no_repeat.py"
    spec = importlib.util.spec_from_file_location("no_repeat", module_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


no_repeat = load_no_repeat_module()


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_string_rule_allows_include_and_exclude_together() -> None:
    rule = no_repeat.StringToTemplate(
        value="https://ctxsift.dev",
        pattern="<%=public_site_url=%>",
        include_extensions=[".md"],
        exclude_extensions=["docs/private/*"],
    )

    assert rule.include_extensions == [".md"]
    assert rule.exclude_extensions == ["docs/private/*"]


def test_apply_templates_replaces_only_matching_files(tmp_path: Path) -> None:
    readme = tmp_path / "README.md"
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    docs_page = docs_dir / "guide.md"
    astro_page = docs_dir / "page.astro"
    ignored = docs_dir / ".gitignore"

    placeholder = "<%=public_site_url=%>"
    readme.write_text(f"Go to {placeholder}\n", encoding="utf-8")
    docs_page.write_text(f"Visit {placeholder}\n", encoding="utf-8")
    astro_page.write_text(f"url = '{placeholder}'\n", encoding="utf-8")
    ignored.write_text(f"{placeholder}\n", encoding="utf-8")

    config = no_repeat.Config.model_validate(
        {
            "concurrency": 4,
            "fail_on_error": False,
            "strings_to_template": [
                {
                    "value": "https://ctxsift.dev",
                    "pattern": placeholder,
                    "include_extensions": [".md"],
                    "locations": ["README.md", "docs/"],
                }
            ],
        }
    )

    results, errors = asyncio.run(no_repeat.apply_templates(config, tmp_path))

    assert not errors
    assert sum(result.changed for result in results) == 2
    assert readme.read_text(encoding="utf-8") == "Go to https://ctxsift.dev\n"
    assert docs_page.read_text(encoding="utf-8") == "Visit https://ctxsift.dev\n"
    assert astro_page.read_text(encoding="utf-8") == f"url = '{placeholder}'\n"
    assert ignored.read_text(encoding="utf-8") == f"{placeholder}\n"


def test_apply_templates_uses_root_when_locations_are_missing(tmp_path: Path) -> None:
    target = tmp_path / "nested" / "doc.md"
    target.parent.mkdir()
    target.write_text("Site: <%=public_site_url=%>\n", encoding="utf-8")

    config = no_repeat.Config.model_validate(
        {
            "strings_to_template": [
                {
                    "value": "https://ctxsift.dev",
                    "pattern": "<%=public_site_url=%>",
                    "include_extensions": [".md"],
                }
            ]
        }
    )

    results, errors = asyncio.run(no_repeat.apply_templates(config, tmp_path))

    assert not errors
    assert len(results) == 1
    assert target.read_text(encoding="utf-8") == "Site: https://ctxsift.dev\n"


def test_apply_templates_supports_include_and_exclude_together(tmp_path: Path) -> None:
    docs_dir = tmp_path / "docs"
    private_dir = docs_dir / "private"
    private_dir.mkdir(parents=True)
    kept = docs_dir / "guide.md"
    skipped = private_dir / "secret.md"
    ignored_type = docs_dir / "note.txt"
    placeholder = "<%=public_site_url=%>"

    kept.write_text(f"{placeholder}\n", encoding="utf-8")
    skipped.write_text(f"{placeholder}\n", encoding="utf-8")
    ignored_type.write_text(f"{placeholder}\n", encoding="utf-8")

    config = no_repeat.Config.model_validate(
        {
            "strings_to_template": [
                {
                    "value": "https://ctxsift.dev",
                    "pattern": placeholder,
                    "locations": ["docs/"],
                    "include_extensions": [".md"],
                    "exclude_extensions": ["docs/private/*"],
                }
            ]
        }
    )

    results, errors = asyncio.run(no_repeat.apply_templates(config, tmp_path))

    assert not errors
    assert len(results) == 1
    assert kept.read_text(encoding="utf-8") == "https://ctxsift.dev\n"
    assert skipped.read_text(encoding="utf-8") == f"{placeholder}\n"
    assert ignored_type.read_text(encoding="utf-8") == f"{placeholder}\n"


def test_apply_templates_continues_when_missing_location_and_fail_on_error_false(
    tmp_path: Path,
) -> None:
    target = tmp_path / "README.md"
    target.write_text("Site: <%=public_site_url=%>\n", encoding="utf-8")
    config = no_repeat.Config.model_validate(
        {
            "fail_on_error": False,
            "strings_to_template": [
                {
                    "value": "https://ctxsift.dev",
                    "pattern": "<%=public_site_url=%>",
                    "include_extensions": [".md"],
                    "locations": ["README.md", "missing-dir"],
                }
            ],
        }
    )

    results, errors = asyncio.run(no_repeat.apply_templates(config, tmp_path))

    assert len(results) == 1
    assert len(errors) == 1
    assert "missing-dir" in errors[0]
    assert target.read_text(encoding="utf-8") == "Site: https://ctxsift.dev\n"


def test_apply_templates_updates_same_file_once_for_multiple_rules(tmp_path: Path) -> None:
    target = tmp_path / "README.md"
    target.write_text(
        "Site: <%=public_site_url=%>\nDocs: <%=docs_url=%>\n",
        encoding="utf-8",
    )
    config = no_repeat.Config.model_validate(
        {
            "strings_to_template": [
                {
                    "value": "https://ctxsift.dev",
                    "pattern": "<%=public_site_url=%>",
                    "locations": ["README.md"],
                },
                {
                    "value": "https://ctxsift.dev/docs",
                    "pattern": "<%=docs_url=%>",
                    "locations": ["README.md"],
                },
            ]
        }
    )

    results, errors = asyncio.run(no_repeat.apply_templates(config, tmp_path))

    assert not errors
    assert len(results) == 1
    assert results[0].replacements == 2
    assert results[0].pattern_replacements == {
        "<%=docs_url=%>": 1,
        "<%=public_site_url=%>": 1,
    }
    assert (
        target.read_text(encoding="utf-8")
        == "Site: https://ctxsift.dev\nDocs: https://ctxsift.dev/docs\n"
    )


def test_run_returns_error_for_missing_config(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    exit_code = asyncio.run(no_repeat.run(tmp_path / ".no-repeat.json", tmp_path))

    captured = capsys.readouterr()
    assert exit_code == 1
    assert "Config file not found" in captured.out


def test_run_returns_error_when_fail_on_error_is_true(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
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

    exit_code = asyncio.run(no_repeat.run(config_path, tmp_path))

    captured = capsys.readouterr()
    assert exit_code == 1
    assert "Location not found" in captured.out
    assert "fail_on_error is true" in captured.out


def test_run_continues_when_fail_on_error_is_false(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    config_path = tmp_path / ".no-repeat.json"
    target = tmp_path / "README.md"
    target.write_text("Site: <%=public_site_url=%>\n", encoding="utf-8")
    write_json(
        config_path,
        {
            "fail_on_error": False,
            "strings_to_template": [
                {
                    "value": "https://ctxsift.dev",
                    "pattern": "<%=public_site_url=%>",
                    "locations": ["README.md", "missing-dir"],
                }
            ],
        },
    )

    exit_code = asyncio.run(no_repeat.run(config_path, tmp_path))

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Location not found" in captured.out
    assert "fail_on_error is true" not in captured.out


def test_print_summary_logs_pattern_counts(capsys: pytest.CaptureFixture[str]) -> None:
    results = [
        no_repeat.FileUpdate(
            file_path=Path("README.md"),
            replacements=2,
            changed=True,
            pattern_replacements={
                "<%=docs_url=%>": 1,
                "<%=public_site_url=%>": 1,
            },
        ),
        no_repeat.FileUpdate(
            file_path=Path("docs/guide.md"),
            replacements=1,
            changed=True,
            pattern_replacements={
                "<%=public_site_url=%>": 1,
            },
        ),
    ]

    no_repeat.print_summary(results, [])

    captured = capsys.readouterr()
    assert "Processed 2 files: 2 changed, 0 unchanged, 3 replacements." in captured.out
    assert "Pattern '<%=docs_url=%>': 1 replacements across 1 files." in captured.out
    assert "Pattern '<%=public_site_url=%>': 2 replacements across 2 files." in captured.out


def test_read_config_file_uses_defaults_for_optional_fields(tmp_path: Path) -> None:
    config_path = tmp_path / ".no-repeat.json"
    write_json(
        config_path,
        {
            "strings_to_template": [
                {
                    "value": "https://ctxsift.dev",
                    "pattern": "<%=public_site_url=%>",
                }
            ]
        },
    )

    config = no_repeat.read_config_file(config_path)

    assert config.concurrency == no_repeat.DEFAULT_CONCURRENCY
    assert config.fail_on_error is False
    assert config.strings_to_template[0].locations == []


def test_include_prefilter_globs_uses_fast_patterns_for_simple_includes() -> None:
    assert no_repeat.include_prefilter_globs([".md", "*.txt", "README.md"]) == [
        "*.md",
        "*.txt",
        "README.md",
    ]


def test_include_prefilter_globs_falls_back_for_complex_or_mixed_case_patterns() -> None:
    assert no_repeat.include_prefilter_globs(["docs/**/*.md"]) is None
    assert no_repeat.include_prefilter_globs([".MD"]) is None


def test_should_prune_directory_matches_relative_path_patterns(tmp_path: Path) -> None:
    private_dir = tmp_path / "docs" / "private"
    private_dir.mkdir(parents=True)
    rule = no_repeat.StringToTemplate(
        value="x",
        pattern="y",
        exclude_extensions=["docs/private/*"],
    )

    assert no_repeat.should_prune_directory(private_dir, rule, tmp_path) is True
