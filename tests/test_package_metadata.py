from __future__ import annotations

import tomllib
from pathlib import Path


def test_flash_attn_is_not_required_on_python_313_plus() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text())

    gpu_extra = pyproject["project"]["optional-dependencies"]["gpu"]
    all_extra = pyproject["project"]["optional-dependencies"]["all"]

    expected = "flash-attn==2.8.3; platform_system != 'Windows' and python_version < '3.13'"

    assert expected in gpu_extra
    assert expected in all_extra
