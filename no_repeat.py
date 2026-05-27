"""
Config-driven utility for replacing repeated literal strings across files.

Rules come from .no-repeat.json and support location filtering, include/exclude
patterns, concurrent file updates, and summary reporting.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
from dataclasses import dataclass
from fnmatch import fnmatch
from pathlib import Path
from typing import Iterable, Sequence

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

CONFIG_PATH = Path(__file__).parent / ".no-repeat.json"
DEFAULT_CONCURRENCY = 8


class StringToTemplate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    value: str
    pattern: str
    locations: list[str] = Field(default_factory=list)
    exclude_extensions: list[str] = Field(default_factory=list)
    include_extensions: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_filters(self) -> "StringToTemplate":
        self.pattern = self.pattern.strip()
        if not self.pattern:
            raise ValueError("pattern must not be empty.")
        return self


class Config(BaseModel):
    model_config = ConfigDict(extra="forbid")

    concurrency: int = Field(default=DEFAULT_CONCURRENCY, ge=1)
    fail_on_error: bool = Field(default=False)
    strings_to_template: list[StringToTemplate] = Field(default_factory=list)


@dataclass(slots=True)
class FileUpdate:
    file_path: Path
    replacements: int
    changed: bool
    pattern_replacements: dict[str, int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Replace no-repeat template placeholders with concrete values.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=CONFIG_PATH,
        help=f"Path to config JSON. Defaults to {CONFIG_PATH.name}.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Repository root used to resolve relative locations. Defaults to the current working directory.",
    )
    return parser.parse_args()


def read_config_file(config_path: Path) -> Config:
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    with config_path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    return Config.model_validate(payload)


def resolve_files(config: Config, root: Path) -> tuple[dict[Path, list[StringToTemplate]], list[str]]:
    file_rules: dict[Path, list[StringToTemplate]] = {}
    errors: list[str] = []
    for rule in config.strings_to_template:
        for candidate in iter_rule_files(rule, root, errors):
            file_rules.setdefault(candidate, []).append(rule)
    return file_rules, errors


def iter_rule_files(
    rule: StringToTemplate,
    root: Path,
    errors: list[str],
) -> Iterable[Path]:
    locations = rule.locations or ["."]
    seen: set[Path] = set()
    for location in locations:
        target = (root / location).resolve() if not Path(location).is_absolute() else Path(location).resolve()
        if not target.exists():
            errors.append(f"Location not found for pattern {rule.pattern!r}: {target}")
            continue
        if target.is_file():
            if should_process_file(target, rule, root):
                if target not in seen:
                    seen.add(target)
                    yield target
            continue
        for file_path in iter_candidate_files(target, rule, root):
            if not file_path.is_file():
                continue
            resolved = file_path.resolve()
            if resolved in seen:
                continue
            if should_process_file(resolved, rule, root):
                seen.add(resolved)
                yield resolved


def iter_candidate_files(target: Path, rule: StringToTemplate, root: Path) -> Iterable[Path]:
    include_globs = include_prefilter_globs(rule.include_extensions)
    for current_root, dirs, files in os.walk(target, topdown=True):
        current_path = Path(current_root)
        dirs[:] = [name for name in dirs if not should_prune_directory(current_path / name, rule, root)]
        for filename in files:
            file_path = current_path / filename
            if include_globs is not None and not matches_prefilter_name(file_path, include_globs):
                continue
            yield file_path


def include_prefilter_globs(patterns: Sequence[str]) -> list[str] | None:
    if not patterns:
        return None
    globs: list[str] = []
    for raw_pattern in patterns:
        pattern = raw_pattern.strip()
        if not pattern:
            continue
        if "/" in pattern or "\\" in pattern:
            return None
        if pattern.startswith("."):
            if pattern != pattern.lower():
                return None
            globs.append(f"*{pattern}")
            continue
        if has_glob(pattern):
            if pattern != pattern.lower():
                return None
            globs.append(pattern)
            continue
        globs.append(pattern)
    return globs or None


def matches_prefilter_name(file_path: Path, globs: Sequence[str]) -> bool:
    normalized_name = file_path.name.lower()
    for glob_pattern in globs:
        if fnmatch(normalized_name, glob_pattern.lower()):
            return True
    return False


def should_process_file(file_path: Path, rule: StringToTemplate, root: Path) -> bool:
    is_included = True
    if rule.include_extensions:
        is_included = matches_any_pattern(file_path, rule.include_extensions, root)
    if not is_included:
        return False
    if rule.exclude_extensions and matches_any_pattern(file_path, rule.exclude_extensions, root):
        return False
    return True


def should_prune_directory(directory_path: Path, rule: StringToTemplate, root: Path) -> bool:
    if not rule.exclude_extensions:
        return False
    relative_path = safe_relative_path(directory_path, root)
    normalized_name = directory_path.name.lower()
    normalized_relative = relative_path.as_posix().lower().rstrip("/")
    probe_child = f"{normalized_relative}/__no_repeat_probe__"
    for pattern in rule.exclude_extensions:
        candidate = pattern.strip().lower().rstrip("/")
        if not candidate or candidate.startswith("."):
            continue
        if has_glob(candidate):
            if (
                fnmatch(normalized_name, candidate)
                or fnmatch(normalized_relative, candidate)
                or fnmatch(probe_child, candidate)
            ):
                return True
            continue
        if "/" in candidate:
            if normalized_relative == candidate or probe_child.startswith(f"{candidate}/"):
                return True
            continue
        if normalized_name == candidate:
            return True
    return False


def matches_any_pattern(file_path: Path, patterns: Sequence[str], root: Path) -> bool:
    relative_path = safe_relative_path(file_path, root)
    normalized_name = file_path.name.lower()
    normalized_relative = relative_path.as_posix().lower()
    for pattern in patterns:
        candidate = pattern.strip().lower()
        if not candidate:
            continue
        if has_glob(candidate):
            if fnmatch(normalized_name, candidate) or fnmatch(normalized_relative, candidate):
                return True
            continue
        if candidate.startswith("."):
            if normalized_name.endswith(candidate):
                return True
            continue
        if normalized_name == candidate or normalized_relative == candidate:
            return True
    return False


def safe_relative_path(file_path: Path, root: Path) -> Path:
    try:
        return file_path.resolve().relative_to(root.resolve())
    except ValueError:
        return Path(file_path.name)


def has_glob(pattern: str) -> bool:
    return any(token in pattern for token in "*?[]")


async def apply_templates(
    config: Config,
    root: Path,
) -> tuple[list[FileUpdate], list[str]]:
    file_rules, discovery_errors = resolve_files(config, root)
    semaphore = asyncio.Semaphore(config.concurrency)
    tasks = [
        asyncio.create_task(apply_rules_to_file(file_path, rules, semaphore))
        for file_path, rules in file_rules.items()
    ]
    results: list[FileUpdate] = []
    errors = list(discovery_errors)
    for task_result in await asyncio.gather(*tasks, return_exceptions=True):
        if isinstance(task_result, Exception):
            errors.append(str(task_result))
            continue
        results.append(task_result)
    return results, errors


async def apply_rules_to_file(
    file_path: Path,
    rules: Sequence[StringToTemplate],
    semaphore: asyncio.Semaphore,
) -> FileUpdate:
    async with semaphore:
        return await asyncio.to_thread(rewrite_file, file_path, rules)


def rewrite_file(file_path: Path, rules: Sequence[StringToTemplate]) -> FileUpdate:
    original_content = file_path.read_text(encoding="utf-8")
    updated_content = original_content
    replacements = 0
    pattern_replacements: dict[str, int] = {}
    for rule in rules:
        count = updated_content.count(rule.pattern)
        if count:
            replacements += count
            pattern_replacements[rule.pattern] = pattern_replacements.get(rule.pattern, 0) + count
            updated_content = updated_content.replace(rule.pattern, rule.value)
    changed = updated_content != original_content
    if changed:
        file_path.write_text(updated_content, encoding="utf-8")
    return FileUpdate(
        file_path=file_path,
        replacements=replacements,
        changed=changed,
        pattern_replacements=pattern_replacements,
    )


def print_summary(results: Sequence[FileUpdate], errors: Sequence[str]) -> None:
    changed_files = [result for result in results if result.changed]
    unchanged_files = len(results) - len(changed_files)
    replacement_total = sum(result.replacements for result in changed_files)
    print(
        f"Processed {len(results)} files: {len(changed_files)} changed, "
        f"{unchanged_files} unchanged, {replacement_total} replacements."
    )
    for pattern, replacement_count, file_count in collect_pattern_stats(changed_files):
        print(
            f"Pattern {pattern!r}: {replacement_count} replacements across {file_count} files."
        )
    for error in errors:
        print(f"ERROR: {error}")


def collect_pattern_stats(results: Sequence[FileUpdate]) -> list[tuple[str, int, int]]:
    replacement_totals: dict[str, int] = {}
    file_totals: dict[str, int] = {}
    for result in results:
        for pattern, count in result.pattern_replacements.items():
            replacement_totals[pattern] = replacement_totals.get(pattern, 0) + count
            file_totals[pattern] = file_totals.get(pattern, 0) + 1
    return [
        (pattern, replacement_totals[pattern], file_totals[pattern])
        for pattern in sorted(replacement_totals)
    ]


async def run(config_path: Path, root: Path) -> int:
    try:
        config = read_config_file(config_path)
    except (FileNotFoundError, ValidationError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    return await run_with_config(config, root)


async def run_with_config(config: Config, root: Path) -> int:
    results, errors = await apply_templates(config, root)
    print_summary(results, errors)
    if errors and config.fail_on_error:
        print("Stopping with exit code 1 because fail_on_error is true.")
        return 1
    return 0


def main() -> None:
    args = parse_args()
    raise SystemExit(asyncio.run(run(args.config, args.root.resolve())))


if __name__ == "__main__":
    main()
