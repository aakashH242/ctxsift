from __future__ import annotations

import asyncio
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import no_repeat


def stage_changed_files(repo_root: Path, changed_files: list[Path]) -> None:
    if not changed_files:
        return
    relative_files = [str(path.resolve().relative_to(repo_root.resolve())) for path in changed_files]
    subprocess.run(
        ["git", "-C", str(repo_root), "add", "--", *relative_files],
        check=True,
    )
    print(f"Restaged {len(relative_files)} files changed by no_repeat.")


async def main() -> int:
    config_path = REPO_ROOT / ".no-repeat.json"
    if not config_path.exists():
        print("Skipping no_repeat hook: .no-repeat.json not found.")
        return 0

    try:
        config = no_repeat.read_config_file(config_path)
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    results, errors = await no_repeat.apply_templates(config, REPO_ROOT)
    no_repeat.print_summary(results, errors)
    stage_changed_files(REPO_ROOT, [result.file_path for result in results if result.changed])

    if errors and config.fail_on_error:
        print("Stopping with exit code 1 because fail_on_error is true.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
