# CtxSift — Save tokens and extend sessions

Command outputs and state recollection are the biggest source of token overuse. 

Agents consume raw command outputs for most tasks. But often, LLMs don't need entire outputs to be able to 
answer something or figure out a situation. This not only increases token usage but also affects time taken. 
It compounds in complex, multistep tasks where rounds of context compaction cause the agent to re-read and re-run
commands to get back to speed with latest code state.

**CtxSift** is a skill that helps agents sift through the repeated noise and find the real signals needed for every task.
It compresses tool outputs and caches them so that agents can look them up when needing context.

---

## Getting Started

### Prerequisites

- **Python ≥ 3.12** — [python.org/downloads](https://www.python.org/downloads/)
- **uv** — a fast Python package manager
  - Install: [docs.astral.sh/uv/getting-started/installation](https://docs.astral.sh/uv/getting-started/installation/)
- C compiler
  - Linux: [gcc](https://gcc.gnu.org/install/) or [clang](https://clang.llvm.org/get_started.html)
  - Windows: [Visual Studio](https://visualstudio.microsoft.com/downloads/) or [MinGW-w64](https://www.mingw-w64.org/downloads/)
  - MacOS: [Xcode](https://developer.apple.com/xcode/)

### Install

CtxSift uses a LLM to compress tool outputs. This can be a model running locally or hosted remotely.
You can choose the installation path best suited to your environment. When using local models, you can override the default
model - see the [supported models](#local-model-support) section for further details. 

```bash 
# Install the base package - inference runs on CPU
uv add ctxsift

# Install with GPU add-ons - inference with GPU acceleration
uv add "ctxsift[gpu]"

# Enable quantization support on GPU
uv add "ctxsift[gpu,quant]"

# Install with LiteLLM included - use remotely hosted models for inference
uv add "ctxsift[remote]"

# Install the full package
uv add "ctxsift[all]"
```

### First-time setup

Run a guided setup to configure your model provider and workspace settings.

```bash
ctxsift configure
```

### Verify your setup

```bash
ctxsift doctor
```

---

## Local Model Support

CtxSift uses two model uses under the hood: one model for **compression**, and one model for **embeddings** used by recall. Those two uses are configured separately.

By default, compression runs locally with a small GGUF model that is safe to start on CPU through embedded `llama.cpp`. 
If you prefer a hosted provider, you can switch compression to a remote LiteLLM-compatible endpoint instead. 
Embeddings are separate: CtxSift currently uses a local Sentence Transformers-compatible embedding model for storing and recalling records, even when compression itself is remote.

| Component | Default                                                                                    | When it is used | Conditions and notes |
|---|--------------------------------------------------------------------------------------------|---|---|
| Local compression | [ibm-granite/granite-4.0-350m-GGUF](https://huggingface.co/ibm-granite/granite-4.0-h-350m) | Used by default | Active when `remote.base_url` is not set. On CPU, local compression uses embedded `llama.cpp` with a Hugging Face GGUF repo id plus one GGUF filename. On CUDA, local compression uses the Transformers backend and a normal Hugging Face text-generation model id. Guided `ctxsift configure` will steer CUDA systems toward `Qwen/Qwen3.5-0.8B` on `cuda`, and in CPU mode it tells you to use a GGUF repo id plus one `.gguf` file from that repo's Files tab. You can switch model, GGUF filename, device, dtype, attention backend, and quantization through config. |
| Remote compression | Off by default                                                                             | Used only when remote mode is configured | Becomes active when `remote.base_url` and `remote.model_name` are set. Usually also needs an API key, depending on the provider. Requires `ctxsift[remote]` because remote compression goes through LiteLLM. This replaces local compression, but not local embeddings. |
| Embeddings for recall | [microsoft/harrier-oss-v1-0.6b](https://huggingface.co/microsoft/harrier-oss-v1-0.6b)      | Used for storing and recalling records | This path is used regardless of whether compression is local or remote. The model must be compatible with Sentence Transformers. |

### Recommended Models

For CPU-based environments, you can configure any GGUF-quantized text-generation models supported by `llama.cpp`. Based on our [benchmarks](benchmark), we recommend the following.


For GPU-based environments, any text-generation models from HuggingFace can be configured. The choice is endless, based on your hardware but here are a few we suggest.




## How it works

CtxSift has two core operations that the skill injects into an agent's workflow.

1. **Compress**: CtxSift intercepts the raw tool outputs and passes them through another LLM to extract only what the agent requires. These compressed records are cached for recall.
    The agent specifies its needs via an instruction in either of the ways belows.  
    **Pipe mode** — pipe any command output with a natural language instruction:
    ```bash
    pytest -q | ctxsift compress "show only failing tests, useful traceback lines, and files involved"
    ```
    **Command capture mode** — let CtxSift execute the command directly for richer metadata (exit code, duration, stderr, git state):
    ```bash
    ctxsift compress "summarize build errors and point out specific misbehaving files" -- npm run build
    ```
2. **Recall**: When recollecting current state or recovering after a context compaction event, the agent discovers the latest relevant state in the cached compressed outputs. This helps reduce large file inspection commands which consume token quickly. 
    The agent recalls using the below commands.
    ```bash
    # Base call    
    ctxsift recall "auth test failure"
   
    # Boost results by referenced files
    ctxsift recall "auth test failure" --files tests/test_auth.py src/auth/tokens.py
   
    # Limit the number of results
    ctxsift recall "docker networking" --limit 5
    ```
    
    Each result is labeled with a **freshness status**:
    
    | Status | Meaning                                         |
    |---|-------------------------------------------------|
    | `fresh` | Referenced files still exist and no changes |
    | `stale_changed` | A referenced file has changed since capture     |
    | `stale_deleted` | A referenced file was deleted                   |
    | `unverifiable` | No file references were captured                |
    | `unknown` | No git/file metadata available                  |

---

## Configuration

> See [.env.example](.env.example) for more details on each setting.

After your initial setup, you can change CtxSift's settings per your requirements. Configuration can be applied using the CLI or by setting environment variables in your workspace.
There are two types of settings - global and local. Global settings are common to all workspaces and used by default.
Workspace settings are local to a workspace and override global configuration. The CLI can be used to set both global and workspace configurations.
Environment variables only affect the current workspace and override the workspace configuration. All environment variables have their corresponding CLI knob.

The order of precedence for configuration knobs is -
```
Environment variable > Workspace config > Global config > Default
```

Global settings are stored in CtxSift's platform-native user config directory as `config.toml`. 
On Linux this is typically `~/.config/ctxsift/config.toml`. On Windows, CtxSift currently uses the path 
returned by `platformdirs`, which is typically `%LOCALAPPDATA%\ctxsift\ctxsift\config.toml`.

Workspace settings are separate from the global file and live alongside the workspace itself: in `.git/ctxsift/config.toml` for Git repositories, or `.ctxsift/config.toml` in the workspace root when the folder is not a Git repo.

### Config Options

The config CLI shows workspace-native settings by default. Use the `--global` flag to reference the global settings.

```bash
# Show current resolved config (secrets are redacted)
ctxsift config show

# Show current resolved global config (secrets are redacted)
ctxsift config show --global

# Use --global to write to global config instead of workspace
ctxsift config set local.device auto --global
```

`ctxsift config set` changes one key at a time. The most useful keys and their corresponding environment variables are grouped below by what they control.

<details>
<summary><strong>Common configuration</strong></summary>

Use these when you want to change behavior that applies no matter which compression model you use. This is where you control how long CtxSift waits, how many retries it makes, how large compressed outputs are allowed to be, and whether the workspace DB lives somewhere custom.

Nothing in this section is required for a normal setup. These are all optional overrides on top of sensible defaults.

```bash
# Limit compressed output size (env var: CTXSIFT_MAX_OUTPUT_TOKENS)
ctxsift config set max_output_tokens 768

# Increase request timeout to 2 minutes (env var: CTXSIFT_TIMEOUT_MS)
ctxsift config set timeout_ms 120000

# Retry remote or bounded operations twice (env var: CTXSIFT_RETRIES)
ctxsift config set retries 2

# Store the database in a custom location (env var: CTXSIFT_DB_PATH)
ctxsift config set db_path .ctxsift/ctxsift.db
```

</details>

<details>
<summary><strong>Remote configuration</strong></summary>

Use remote configuration when you want CtxSift to send compression requests to a hosted model through LiteLLM instead of running a local model. In practice, the important settings are the provider base URL, the model name, and usually an API key. API version and reasoning mode are only needed for providers that care about them.

If you are using remote compression, `remote.base_url` and `remote.model_name` are required. `remote.api_key` is usually required by hosted providers, but that depends on the provider you are talking to. `remote.api_version` is only needed for providers that require one, and `remote.reasoning_mode` is optional.

```bash
# Point ctxsift at a LiteLLM-compatible endpoint (env var: CTXSIFT_LLM_BASE_URL)
ctxsift config set remote.base_url https://api.openai.com/v1

# Choose the remote model used for compression (env var: CTXSIFT_LLM_MODEL)
ctxsift config set remote.model_name gpt-4o-mini

# Save an API key into config if you want to keep it there (env var: CTXSIFT_LLM_API_KEY)
ctxsift config set remote.api_key YOUR_API_KEY

# Optional provider API version (env var: CTXSIFT_LLM_API_VERSION)
ctxsift config set remote.api_version 2025-01-01

# Optional reasoning mode: auto, true, or false (env var: CTXSIFT_LLM_REASONING_MODE)
ctxsift config set remote.reasoning_mode auto
```

If remote mode is enabled, CtxSift expects LiteLLM to be installed. If it is missing, `ctxsift doctor` and `ctxsift configure` will warn and remote compression will not work until you install `ctxsift[remote]`.

Remote mode only replaces the compression side of the pipeline. It does **not** globally disable daemon support. When `remote.base_url` is set, CtxSift stops using the local **compression daemon** because compression requests now go out through LiteLLM instead. But if `daemon.enabled=true`, the **embedding daemon** can still be used for recall and vector indexing. In other words: remote compression disables the local compression-daemon path, not the entire daemon subsystem.

</details>

<details>
<summary><strong>Local configuration</strong></summary>

Use local configuration when you want compression to run on your own machine. This is where you choose the local model, the device it should run on, the dtype, and advanced attention settings if you need to tune performance or compatibility.

CPU and GPU local compression do not take exactly the same model input. CPU local compression uses embedded `llama.cpp`, so `local.model` should be a Hugging Face GGUF repo id and `local.gguf_filename` should be one concrete `.gguf` file from that repo. CUDA local compression uses Transformers, so `local.model` should be a normal Hugging Face text-generation model id and `local.gguf_filename` is ignored.

`local.llama_context_window` is a CPU-only llama.cpp knob. It controls the runtime context window used for GGUF models on the llama.cpp path. If you do not set it, CtxSift uses its built-in default of `8192`. GPU Transformers compression does not currently have a matching CtxSift config key.

If you stay on local compression, you do not have to set any of these manually because CtxSift already has defaults. Change them only when you want a different model, need to force CPU or CUDA behavior, or want to tune compatibility and performance. The default `local.device` is `auto`, but a GGUF-style CPU config still stays on the `llama.cpp` path until you actually switch to a CUDA/Transformers-style model choice.

```bash
# Pick a different local compression model (env var: CTXSIFT_LOCAL_MODEL)
ctxsift config set local.model Qwen/Qwen3.5-0.8B

# Let ctxsift auto-pick the device (env var: CTXSIFT_LOCAL_DEVICE)
ctxsift config set local.device auto

# Force a dtype (env var: CTXSIFT_LOCAL_DTYPE)
ctxsift config set local.dtype bfloat16

# Override the local attention backend (env var: CTXSIFT_LOCAL_ATTN_IMPLEMENTATION)
ctxsift config set local.attn_implementation sdpa

# Override the CPU GGUF repo + filename when local compression runs on llama.cpp
ctxsift config set local.model ibm-granite/granite-4.0-350m-GGUF
ctxsift config set local.gguf_filename smollm2-360m-instruct-q4_k_m.gguf

# Increase the CPU llama.cpp runtime context window (env var: CTXSIFT_LOCAL_LLAMA_CONTEXT_WINDOW)
ctxsift config set local.llama_context_window 16384
```

</details>

<details>
<summary><strong>Quantization configuration</strong></summary>

Quantization is only relevant for local GPU Transformers models and is off by default. It trades some quality or compatibility for lower memory usage, which is useful when the model you want does not fit comfortably in VRAM. CPU local compression now uses llama.cpp with GGUF models instead of the old Transformers-plus-Quanto path. However, for smaller models, quantization hurts accuracy and performance, as per our [benchmark](benchmark). 
Start conservative unless you already know your runtime supports a more aggressive setup.

Everything in this section is conditional. You only need quantization settings when you are using local compression and the chosen model is too heavy to run comfortably without them. `local.model_cache_path` is only useful when you want explicit control over where quantized checkpoints are stored.

```bash
# No quantization (env var: CTXSIFT_LOCAL_QUANTIZATION)
ctxsift config set local.quantization none

# Lower memory use with bitsandbytes 8-bit (env var: CTXSIFT_LOCAL_QUANTIZATION)
ctxsift config set local.quantization bnb-8bit

# More aggressive 4-bit mode (env var: CTXSIFT_LOCAL_QUANTIZATION)
ctxsift config set local.quantization bnb-4bit-nf4

# Persist saved quantized checkpoints under a custom cache root (env var: CTXSIFT_MODEL_CACHE_PATH)
ctxsift config set local.model_cache_path D:/model-cache
```

</details>

<details>
<summary><strong>Embeddings, recall, daemon, and retention configuration</strong></summary>

These settings control retrieval quality, shared daemon behavior, and how long old records are kept. Most users can leave them alone, but they are useful when you want to tune recall quality, switch embedding models, change how aggressively the daemons stay warm, or shorten and extend history retention.

These are almost entirely optional tuning knobs. The embedding model and daemon settings already have defaults, and recall works without manual changes. Retention is also optional unless you want records kept for a shorter or longer period than the default 30 days.

```bash
# Use a different embedding model (env var: CTXSIFT_EMBEDDING_MODEL)
ctxsift config set embedding.model sentence-transformers/all-MiniLM-L6-v2

# Let ctxsift choose the embedding backend automatically (env var: CTXSIFT_EMBEDDING_BACKEND)
ctxsift config set embedding.backend auto

# Set embedding device preference (env var: CTXSIFT_EMBEDDING_DEVICE)
ctxsift config set embedding.device auto

# Adjust recall candidate limits (env vars: CTXSIFT_RECALL_DEFAULT_LIMIT, CTXSIFT_RECALL_LEXICAL_CANDIDATE_LIMIT, CTXSIFT_RECALL_VECTOR_CANDIDATE_LIMIT)
ctxsift config set recall.default_limit 10
ctxsift config set recall.lexical_candidate_limit 50
ctxsift config set recall.vector_candidate_limit 50

# Tune daemon behavior (env vars: CTXSIFT_DAEMON_ENABLED, CTXSIFT_DAEMON_IDLE_TIMEOUT_SECONDS, CTXSIFT_DAEMON_STARTUP_TIMEOUT_MS)
ctxsift config set daemon.enabled true
ctxsift config set daemon.idle_timeout_seconds 900
ctxsift config set daemon.startup_timeout_ms 30000

# Adjust embedding daemon batching behavior (env vars: CTXSIFT_DAEMON_EMBEDDING_BATCH_WINDOW_MS, CTXSIFT_DAEMON_EMBEDDING_MAX_BATCH_SIZE)
ctxsift config set daemon.embedding_batch_window_ms 20
ctxsift config set daemon.embedding_max_batch_size 16

# Keep records for 30 days before cleanup removes old entries (env var: CTXSIFT_RETENTION_MAX_AGE_DAYS)
ctxsift config set retention.max_age_days 30
```

</details>


## Quantization And Flash Attention Support

### Quantization

When local compression runs on CUDA through the Transformers backend, CtxSift can use quantization to reduce VRAM usage for larger models. 
This is mainly a fit-and-memory tool: it helps when a model is close to fitting on your GPU or fails to load at full precision. 
It is not a general-purpose performance win, and on smaller models it can reduce output quality, increase inference time or make runtime behavior less predictable.

CPU local compression uses `llama.cpp` with GGUF artifacts, 
so `local.quantization` does not apply there. On CPU, the right way to save memory is to choose a GGUF model 
that is already quantized for `llama.cpp` and tune context window with the setting `llama_context_window` or the env variable `CTXSIFT_LOCAL_LLAMA_CONTEXT_WINDOW`.

CtxSift currently supports these quantization modes for local GPU compression:

- `none`
- `bnb-8bit`
- `bnb-4bit-fp4`
- `bnb-4bit-nf4`

Quantized GPU loads require the optional quantization dependencies:

```bash
uv add "ctxsift[gpu,quant]"
```

### Flash Attention
 
Attention backend selection changes how the model computes attention during inference. 
Flash Attention is mostly a throughput and memory-efficiency knob for supported CUDA runs.

It does not apply to CPU `llama.cpp` runs. CtxSift controls it through `local.attn_implementation` or `CTXSIFT_LOCAL_ATTN_IMPLEMENTATION`.

CtxSift currently supports these attention modes for local GPU compression:

- `auto`: recommended default; CtxSift chooses the safest supported backend for the current runtime
- `sdpa`: PyTorch scaled-dot-product attention; usually the most conservative and broadly compatible option
- `flash_attention_2`: the optimized Flash Attention path; can improve throughput and reduce memory use on supported CUDA setups

One practical constraint: `flash_attention_2` depends on the optional Flash Attention package and is not universally 
available across platforms. On Windows in particular, `auto` or `sdpa` is usually the safer recommendation.

## Daemons

CtxSift serves local models through background daemons. This allows batching requests and allows the models to be loaded only once:

- local compression: one daemon per effective local runtime signature
- embeddings: one daemon per effective embedding runtime signature

These daemons auto-start on first use, stay warm across workspaces when the effective runtime signature matches, and shut down after an idle timeout.

If you switch from local compression to remote compression, only the local compression daemon becomes unnecessary. The embedding daemon can still stay active and continue serving recall-related embedding work when daemon support is enabled. Existing daemons are not force-killed and stay alive until they age out, unless you stop them yourself with `ctxsift daemon stop` or `ctxsift daemon stop --all`.

```bash
ctxsift daemon start
ctxsift daemon status
ctxsift daemon stop

# Inspect or stop every registered daemon
ctxsift daemon status --all
ctxsift daemon stop --all
```

## License

MIT
