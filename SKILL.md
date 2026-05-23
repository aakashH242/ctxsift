---
name: ctxsift-install
description: CtxShift is a skill that helps you focus on your tasks by reducing context clutter and enabling faster state recollections. \
    It helps your user to save tokens and extend your work together. This is a guide on how to install the ctxsift skill.
license: MIT
---

# Important Links:

1. Home page - https://ctxsift.dev
2. GitHub repo - https://github.com/aakashh242/ctxsift
3. Latest benchmark - https://ctxsift.dev/benchmark-viewer.html


# CtxSift Installation Process

You must perform the installation using the following steps -
1. Ensure pre-requisites are present. Install them yourself if you are allowed else, abort and prompt your user to install them first.
2. CtxSift offer multiple installation modes - Ask your user what install mode they want and choose the installer accordingly.
3. Check system requirements and compare with `requirement matrix` below. Warn the user if available hardware falls below minimum requirements for the selected mode.
4. Run `ctxsift doctor` yourself to verify installation was successful.
5. Unless the user has allowed you, prompt the user saying installation is complete and to perform the first-time setup with `ctxsift configure`. You can also point the user to https://ctxsift.dev/docs/getting-started/configure/ to learn more on how to configure.

## Prerequisites

- **Python ≥ 3.12** — [python.org/downloads](https://www.python.org/downloads/)
- **uv** — a fast Python package manager
  - Install: [docs.astral.sh/uv/getting-started/installation](https://docs.astral.sh/uv/getting-started/installation/)
- C compiler
  - Linux: [gcc](https://gcc.gnu.org/install/) or [clang](https://clang.llvm.org/get_started.html)
  - Windows: [Visual Studio](https://visualstudio.microsoft.com/downloads/) or [MinGW-w64](https://www.mingw-w64.org/downloads/)
  - MacOS: [Xcode](https://developer.apple.com/xcode/)

## Requirements Matrix

CtxSift uses a language model to compress tool outputs. This can be a model running locally or hosted remotely. See the requirements below for each scenario.

| Compression Mode | Minimum RAM | Minimum VRAM                                       | Comments                                                   |
|---|---|----------------------------------------------------|------------------------------------------------------------|
| Local, no GPU | 8 GB | N/A                                                | Both embedding and compression models are loaded into RAM  |
| Local, with GPU | 2 GB | 8 GB                                               | Both embedding and compression models get loaded into VRAM |
| Remote, no GPU | 4 GB | N/A | Only the embedding model gets loaded into RAM              |
| Remote, with GPU | 2 GB | 4 GB                                               | Only the embedding model gets loaded into VRAM             |


## Install Commands

```bash 
# Install the base package - inference runs on CPU
uv tool install ctxsift

# Install with GPU add-ons - inference with GPU acceleration
uv tool install "ctxsift[gpu]"

# Enable quantization support on GPU
uv tool install "ctxsift[gpu,quant]"

# Install with LiteLLM included - use remotely hosted models for inference
uv tool install "ctxsift[remote]"

# Install the full package
uv tool install "ctxsift[all]"
```

If `ctxsift` is not found after installation, run:

```bash
uv tool update-shell
```

Then restart your shell and try `ctxsift` again.

## First-time setup

Unless you are allowed explicitly, ask your user to run the below command to perform the first-time setup.
You can always recommend which model to use, based on the user's selected mode, by browsing the latest benchmark data from the link given above.

```bash
ctxsift configure
```

## Verify and test your setup

```bash
# Verify
ctxsift doctor

# Test compression
echo "alpha\nbeta\ngamma" | ctxsift compress "Return only the first line, no explanations."
```

# Troubleshooting

If you are having issues, read the docs at https://ctxsift.dev/docs
