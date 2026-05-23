"""Runtime metric helpers for benchmark execution."""

from __future__ import annotations

import importlib
import os
from typing import Any


def current_process_rss_bytes() -> int | None:
    """Return current process RSS in bytes when psutil is available."""
    try:
        psutil = importlib.import_module("psutil")
    except ImportError:
        return None
    process = psutil.Process()
    return int(process.memory_info().rss)


def torch_module_or_none() -> Any | None:
    """Return torch when installed."""
    try:
        return importlib.import_module("torch")
    except ImportError:
        return None


def reset_gpu_peak_memory(torch_module: Any | None) -> None:
    """Reset tracked GPU peak memory when CUDA is available."""
    if torch_module is None:
        return
    if not bool(torch_module.cuda.is_available()):
        return
    torch_module.cuda.reset_peak_memory_stats()


def gpu_peak_memory_bytes(torch_module: Any | None) -> int | None:
    """Return peak GPU memory allocation in bytes when CUDA is available."""
    if torch_module is None:
        return None
    if not bool(torch_module.cuda.is_available()):
        return None
    return int(torch_module.cuda.max_memory_allocated())


def torch_num_threads(torch_module: Any | None) -> int | None:
    """Return torch intra-op thread count when available."""
    if torch_module is None:
        return None
    getter = getattr(torch_module, "get_num_threads", None)
    if not callable(getter):
        return None
    return int(getter())


def torch_num_interop_threads(torch_module: Any | None) -> int | None:
    """Return torch inter-op thread count when available."""
    if torch_module is None:
        return None
    getter = getattr(torch_module, "get_num_interop_threads", None)
    if not callable(getter):
        return None
    return int(getter())


def thread_env_value(name: str) -> str | None:
    """Return one thread-related environment variable when set."""
    value = os.environ.get(name)
    if value is None:
        return None
    stripped = value.strip()
    return stripped or None
