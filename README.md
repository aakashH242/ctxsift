
# CtxSift — Save tokens and extend your coding sessions

<p align="center">
  <img src="./docs/src/assets/banner.png" alt="CtxSift" width="30%" />
</p>

Command outputs and state recollection are the biggest source of token overuse. 

Agents consume raw command outputs for most tasks. But often, LLMs don't need entire outputs to be able to 
answer something or figure out a situation. This not only increases token usage but also affects time taken responses. 
It compounds in complex, multistep tasks where rounds of context compaction cause the agent to re-read and re-run
commands to get back to speed with latest code state. Just compressing command outputs is not enough - it shifts the
token tax to these recollection moments. 

**CtxSift** is a skill that helps agents sift through the repeated noise and find the real signals needed for each task.
It compresses tool outputs and caches them so that agents can do a look-up when needing context or recollecting.

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

CtxSift uses a language model to compress tool outputs. This can be a model running locally or hosted remotely.
You can choose the installation path best suited to your environment. When using local models, you can override the default
model - see the [supported models](#local-model-support) section for further details. 


> ❗ For the best experience, please see the minimum hardware requirements below.
> 
> <details>
> <summary>Requirements matrix</summary>
>
> | Compression Mode | Minimum RAM | Minimum VRAM                                       | Comments                                                   |
> |---|---|----------------------------------------------------|------------------------------------------------------------|
> | Local, no GPU | 8 GB | N/A                                                | Both embedding and compression models are loaded into RAM  |
> | Local, with GPU | 2 GB | 8 GB                                               | Both embedding and compression models get loaded into VRAM |
> | Remote, no GPU | 4 GB | N/A | Only the embedding model gets loaded into RAM              |
> | Remote, with GPU | 2 GB | 4 GB                                               | Only the embedding model gets loaded into VRAM             |
> 
> </details>


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

### First-time setup

Run a guided setup to configure your model provider and workspace settings.

```bash
ctxsift configure
```

### Verify and test your setup

```bash
# Verify
ctxsift doctor

# Test compression
echo "alpha\nbeta\ngamma" | ctxsift compress "Return only the first line, no explanations."
```

---

## Local Model Support

CtxSift uses two model uses under the hood: one model for **compression**, and one model for **embeddings** used by recall. Those two uses are configured separately.

By default, compression runs locally with a small GGUF model that is safe to start on CPU through embedded `llama.cpp`. 
If you prefer a hosted provider, you can switch compression to a remote LiteLLM-compatible endpoint instead.
Embeddings are separate: CtxSift currently uses a local Sentence Transformers-compatible embedding model for storing and recalling records, even when compression itself is remote.

| Component | Default                                                                                    | When it is used | Conditions and notes |
|---|--------------------------------------------------------------------------------------------|---|---|
| Local compression | [ibm-granite/granite-4.0-350m-GGUF](https://huggingface.co/ibm-granite/granite-4.0-350m-GGUF) | Used by default | Active when `remote.base_url` is not set. On CPU, local compression uses embedded `llama.cpp` with a Hugging Face GGUF repo id plus one GGUF filename. On CUDA, local compression uses the Transformers backend and a normal Hugging Face text-generation model id. Guided `ctxsift configure` steers CPU setups toward `ibm-granite/granite-4.0-350m-GGUF` and CUDA setups toward `LiquidAI/LFM2.5-1.2B-Instruct`. You can switch model, GGUF filename, device, dtype, attention backend, and quantization through config. |
| Remote compression | Off by default                                                                             | Used only when remote mode is configured | Becomes active when `remote.base_url` and `remote.model_name` are set. Usually also needs an API key, depending on the provider. Requires `ctxsift[remote]` because remote compression goes through LiteLLM. This replaces local compression, but not local embeddings. |
| Embeddings for recall | [microsoft/harrier-oss-v1-0.6b](https://huggingface.co/microsoft/harrier-oss-v1-0.6b)      | Used for storing and recalling records | This path is used regardless of whether compression is local or remote. The model must be compatible with Sentence Transformers. |

### Changing Models

For CPU-based environments, you can configure any GGUF-quantized text-generation models supported by `llama.cpp`. 
For GPU-based environments, any text-generation models from HuggingFace can be used. The choice is endless, based on your hardware.

We have [benchmarked](benchmark) a few models to help you get started.
You can also run the benchmark to see how a model not listed here will perform. Learn more about it [here](benchmark/README.md).
To view the latest benchmark, open `benchmark/results/viewer.html` to inspect the latest static dashboard snapshot.

**CPU models** — GGUF quantized models running on CPU via built-in llama.cpp engine. Sorted by score, highest first.

> Scores reflect the May 2026 benchmark run on an i7-12700F with 64 GiB RAM. Latency numbers are machine-specific — treat them as relative comparisons only.

| Name                                                                                                          | Avg. Inference (s) | Score | Comments |
|---------------------------------------------------------------------------------------------------------------|:-:|:-:|---|
| [Qwen3.5-0.8B-GGUF](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF) **(recommended)**                       | 5.6 | **56.14** | Best CPU model overall. Highest score, fewest rejected outputs (only 19 out of 280 cases), and a reasonable ~5–6 s per request. Recommended if you want to switch from the default. |
| [LFM2.5-1.2B-Instruct-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct-GGUF)                      | 7.4 | 52.69 | Strong second-place CPU model. Low rejection count (13 out of 280) and good quality. Slower than Qwen3.5-0.8B but a solid step up from the smaller models below. |
| [Qwen3-0.6B-GGUF](https://huggingface.co/unsloth/Qwen3-0.6B-GGUF)                                             | 15.9 | 50.86 | Decent quality but roughly 3× slower than Qwen3.5-0.8B for a lower score. The newer Qwen3.5 variant is the better pick unless you specifically want Qwen3. |
| [SmolLM2-360M-Instruct-GGUF](https://huggingface.co/unsloth/SmolLM2-360M-Instruct-GGUF)                       | 6.3 | 46.83 | Respectable for a tiny 360M model. A good fallback if you are on a very constrained machine. |
| [Qwen2.5-Coder-0.5B-Instruct-128K-GGUF](https://huggingface.co/unsloth/Qwen2.5-Coder-0.5B-Instruct-128K-GGUF) | 5.2 | 46.74 | Fast and code-aware. Slightly fewer rejections than the base Qwen2.5-0.5B and worth considering for code-heavy workloads. |
| [gemma-3-270m-it-GGUF](https://huggingface.co/unsloth/gemma-3-270m-it-GGUF)                                   | 3.7 | 43.65 | Fastest model in the group, but higher rejection rate (67 out of 280). Fine when raw speed matters more than reliability. |
| [granite-4.0-350m-GGUF](https://huggingface.co/ibm-granite/granite-4.0-350m-GGUF) **(default)**               | 2.9 | 42.92 | Very fast — the quickest model after Gemma 270M. Quality is middling and rejections are moderate. Worth trying if you need the fastest possible response time and can tolerate some misses. |
| [Qwen2.5-0.5B-Instruct-GGUF](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF)                          | 7.8 | 42.12 | Slower than Qwen3.5 with lower quality. Not the strongest choice unless you specifically want the Qwen2.5 base family. |
| [Qwen2-500M-Instruct-GGUF](https://huggingface.co/lmstudio-community/Qwen2-500M-Instruct-GGUF)                | 5.9 | 38.67 | High rejection rate (66 out of 280) and the second-lowest score. Not recommended. |
| [Kiwi-1.0-0.7B-32k-Instruct-GGUF](https://huggingface.co/mradermacher/Kiwi-1.0-0.7B-32k-Instruct-GGUF)        | 24.8 | 34.68 | Slowest and lowest-scoring CPU model tested. Not recommended. |

**GPU models** — full-precision Transformers models running on CUDA. Sorted by score, highest first. Tested on an RTX 3060 Ti (8 GiB).

> Latency on GPU depends heavily on your specific card. Use the scores as the main comparison signal.

| Name | Avg. Inference (s) | Score | Comments |
|------|:-:|:-:|---|
| [Qwen3.5-2B](https://huggingface.co/Qwen/Qwen3.5-2B) | 9.7 | **52.99** | Best overall GPU model by score. Solid quality jump over the 1–1.5B options. Good pick if you want the highest quality and don’t mind the extra wait. |
| [granite-3.3-2b-instruct](https://huggingface.co/ibm-granite/granite-3.3-2b-instruct) | 4.7 | 51.54 | IBM's 2B model. Particularly good at preserving exact values and following structured output contracts like JSON or bullet lists. Also the fastest of the 2B-class models. |
| [LFM2.5-1.2B-Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct) **(recommended)** | 1.2 | 50.38 | Fastest GPU model tested — roughly 4× faster than most others. Best speed-to-quality ratio in this class. Recommended default for GPU setups. |
| [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) | 19.5 | 49.58 | Decent quality but much slower than Qwen3.5-2B for a lower score. Hard to recommend unless you specifically want this model. |
| [granite-4.0-micro](https://huggingface.co/ibm-granite/granite-4.0-micro) | 8.5 | 48.83 | IBM's micro model. Moderate quality and speed, slightly below its 2B sibling. |
| [SmolLM2-1.7B-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct) | 4.6 | 48.78 | Fast and lightweight. A reasonable fallback if you want quick GPU inference without paying for a larger model. |
| [gemma-3-1b-it](https://huggingface.co/unsloth/gemma-3-1b-it) | 8.6 | 47.29 | Google's 1B Gemma model. Middling quality with a higher rejection count — not the strongest option at this size. |
| [Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B) | 5.5 | 50.21 | Smaller model that holds up reasonably well on GPU. Best used when VRAM is very tight and you still want decent Qwen3.5 quality. |
| [Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) | 3.6 | 45.91 | Fast and lightweight, but quality trails other GPU models at this size. Fine when throughput matters more than peak accuracy. |

**Remote / hosted models** — models accessed through a LiteLLM-compatible endpoint (e.g. OpenAI). Requires `ctxsift[remote]`. Sorted by score, highest first.

> Remote latency depends on your network and the provider's load at the time of the run. Treat latency numbers here as indicative, not fixed.

| Name | Avg. Inference (s) | Score | Comments |
|------|:-:|:-:|---|
| [gpt-4.1](https://platform.openai.com/docs/models) | 1.8 | **89.76** | Best remote model by a wide margin. Only 1 rejected case out of 280 and near-perfect anchor preservation. The ceiling for hosted compression quality. |
| [gpt-5.4-mini](https://platform.openai.com/docs/models) | 1.3 | 83.69 | Near the top of the leaderboard at a fraction of the cost of gpt-4.1. Very few rejections (2 out of 280) and fast responses. Strong everyday choice. |
| [gpt-5.4-nano](https://platform.openai.com/docs/models) | 1.5 | 83.32 | Almost identical results to gpt-5.4-mini. Nano-sized pricing with strong quality. A cost-efficient pick for high-volume setups. |
| [gpt-4o-mini](https://platform.openai.com/docs/models) | 2.1 | 77.46 | Reliable and fast. Noticeably fewer rejections than gpt-4.1-mini and a solid score. Good value for everyday compression at scale. |
| [gpt-4.1-mini](https://platform.openai.com/docs/models) | 1.8 | 73.46 | Decent performance. Slightly more rejections than gpt-4o-mini but still a reasonable choice if you are already on gpt-4.1 pricing. |
| [gpt-4o](https://platform.openai.com/docs/models) | 1.7 | 73.11 | Scores below gpt-4o-mini despite being the larger model. More rejections (24 out of 280). gpt-4o-mini is the better pick in this family. |
| [gpt-5-mini](https://platform.openai.com/docs/models) | 6.6 | 31.40 | Underperformed significantly — 132 rejected cases out of 280. Slow responses compounded by poor instruction following on structured output tasks. Not recommended in its current form. |
| [gpt-5-nano](https://platform.openai.com/docs/models) | 4.8 | 7.35 | Failed on almost every case — 244 rejections out of 280. Appears to not follow the compression contract reliably at all. Not suitable for CtxSift use right now. |

To learn more about the benchmark based on which, we recommend alternate models, please [see here](benchmark/README.md).

---

## How it works

CtxSift has two core operations that the skill injects into an agent's workflow.

1. **Compress**: CtxSift intercepts the raw tool outputs and passes them through another LLM to extract only what the agent requires. These compressed records are cached for recall.
    
    The agent specifies its needs via an instruction in either of the ways belows.
    **Pipe mode** — pipe any command output with a natural language instruction:
    ```bash
    pytest -q | ctxsift compress --intent summary "show only failing tests, useful traceback lines, and files involved"
    ```
    **Command capture mode** — let CtxSift execute the command directly for richer metadata (exit code, duration, stderr, git state):
    ```bash
    ctxsift compress --intent summary "summarize build errors and point out specific misbehaving files" -- pnpm build
    ```
2. **Recall**: Mostly after a context compaction event, agents rediscover the current state by inspecting large files which can negate tokens saved by compression. Recall lets agents search previously compressed outputs using natural language, returning relevant summaries, execution metadata, and file paths to rebuild their context efficiently.

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

CtxSift is built to run with minimal configuration overhead but, power users can change CtxSift's settings as they wish. 
Configuration can be applied using the CLI or by setting environment variables in your workspace.
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
<summary><strong>Compress configuration</strong></summary>

These knobs control how the compress command behaves. These always apply no matter which compression model you use.

```bash
# Limit compressed output size (env var: CTXSIFT_MAX_OUTPUT_TOKENS)
ctxsift config set max_output_tokens 768

# Increase request timeout to 2 minutes (env var: CTXSIFT_TIMEOUT_MS)
ctxsift config set timeout_ms 120000

# Retry remote or bounded operations twice (env var: CTXSIFT_RETRIES)
ctxsift config set retries 2
```

</details>

<details>
<summary><strong>Remote configuration</strong></summary>

Set remote configuration when you want CtxSift to send compression requests to a hosted model through LiteLLM instead of running a local model. 
The important settings are the provider base URL, the model name, and usually an API key. 
API version and reasoning mode are only needed for providers that care about them. Please note that `reasoning_mode`
does not control reasoning effort - it indicates if a model supports reasoning or not.


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

</details>

<details>
<summary><strong>Local configuration</strong></summary>

You can control the local inference settings when you want compression to run on your own machine. 
This is where you choose the local model, the device it should run on, the dtype, and advanced attention settings if you need to tune performance or compatibility.

CPU and GPU local compression do not take exactly the same model input. 
CPU local compression uses embedded `llama.cpp`, so `local.model` should be a Hugging Face GGUF repo id and 
`local.gguf_filename` should be one concrete `.gguf` file from that repo. 
CUDA local compression uses Transformers, so `local.model` should be a normal Hugging Face text-generation model id and `local.gguf_filename` is ignored.

`local.llama_context_window` is a CPU-only llama.cpp knob. It controls the runtime context window used for GGUF models 
on the llama.cpp path. If you do not set it, CtxSift uses its built-in default of `8192`. GPU Transformers compression does not currently have a matching CtxSift config key.

You do not have to set any of these manually because CtxSift already has defaults. Change them only when you want a 
different model, need to force CPU or CUDA behavior, or want to tune compatibility and performance. 

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

Everything in this section is conditional. You only need quantization settings when you are using local compression 
and the chosen model is too heavy to run comfortably without them. `local.model_cache_path` is useful when you 
want explicit control over where quantized checkpoints are stored.

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

These settings control retrieval quality, shared daemon behavior, and how long old records are kept. 
Most users can leave them alone, but they are useful when you want to tune recall quality, switch embedding models, 
change how aggressively the daemons stay warm, or shorten and extend history retention.

These are almost entirely optional tuning knobs. The embedding model and daemon settings already have defaults, 
and recall works without manual changes. Retention is also optional unless you want records kept for a shorter or longer period than the default 30 days.

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

---

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
uv tool install "ctxsift[gpu,quant]"
```

### Flash Attention

Flash Attention is mostly a throughput and memory-efficiency knob for supported CUDA runs.
It does not apply to CPU runs. CtxSift controls it through `local.attn_implementation` or `CTXSIFT_LOCAL_ATTN_IMPLEMENTATION`.

CtxSift currently supports these attention modes for local GPU compression:

- `auto`: recommended default; CtxSift chooses the safest supported backend for the current runtime
- `sdpa`: PyTorch scaled-dot-product attention; usually the most conservative and broadly compatible option
- `flash_attention_2`: the optimized Flash Attention path; can improve throughput and reduce memory use on supported CUDA setups

One practical constraint: `flash_attention_2` depends on the Flash Attention package and is not universally 
available across platforms. On Windows in particular, `auto` or `sdpa` is usually the safer recommendation.

---

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

---

## Acknowledgement

CtxSift was inspired by the original [Distill](https://github.com/samuelfaj/distill) project by [samuelfaj](https://github.com/samuelfaj). 
That work helped shape the initial direction here and motivated extending the idea toward local execution, file re-reads, and read-after-compression state recovery.

Thanks as well to the open-source tooling that makes this project practical: Hugging Face for providing opensource models, llama.cpp for efficient local inference on CPU, LiteLLM for their package to support a hundred providers and the broader libraries and communities around local LLM workflows that make projects like this possible.

---

## License

MIT
