# Local Compression Model Profiles

## Goal

Define one stable `model_profile` layer for local compression models so `ctxsift` can:

- use family-appropriate prompt structure
- use conservative generation defaults for compression
- clean up family-specific output artifacts
- fall back safely when no family profile matches

This is for **compression** only, not embedding or recall.

## Why this layer exists

The current local backend can load multiple Hugging Face model families, but not all of them want the same prompt or generation settings.

Examples:

- Qwen 3 explicitly supports thinking and non-thinking behavior.
- Granite explicitly supports `<think></think>` and `<response></response>` reasoning structure.
- Phi wants strict chat-format prompts.
- SmolLM2 gives an explicit sampled generation example.
- Gemma uses role-based prompt templates and different handling depending on text-only vs image-text generation.

If we force one prompt and one decode strategy across all families, we get:

- style drift
- headings/bullets when we want plain text
- `<think>` or other reasoning wrappers
- weaker exact-token preservation

So the profile layer should be the contract between:

- generic `ctxsift` compression requirements
- model-family-specific usage guidance

## Product rule: compression is not chat

The model-card examples are mostly chat examples. `ctxsift` is not using these models for open-ended chat.

`ctxsift` compression is a constrained summarization task:

- preserve exact filenames, symbols, test ids, line numbers, commands, package names, and error codes
- avoid invented fixes
- avoid long explanations
- return short plain text useful for later recall

Because of that, the default compression path should be **more deterministic and more constrained** than typical chat settings.

## Profile schema

Every family profile should define:

- `family_name`
- `match_prefixes`
- `prompt_shape`
- `generation_defaults`
- `cleanup_rules`
- `validation_rules`
- `notes`

Recommended internal structure:

```text
ModelProfile
  family_name
  match_prefixes
  prompt_builder_kind
  generation_kind
  cleanup_kind
  validation_kind
```

That keeps implementation small and composable.

## Shared compression contract

All local family profiles should obey the same output contract:

- plain text only
- no markdown bullets
- no headings
- no field labels
- no XML-style tags
- no fixes or recommendations
- preserve exact anchor tokens verbatim
- 1 to 3 sentences by default

Shared prompt intent:

1. raw input is the source of truth
2. extracted signal is guidance only
3. high-signal anchors must survive exactly
4. likely failing locus should be stated first

## Prompt shape

The prompt should not dump the entire extracted-signal structure.

Bad shape for compression:

- Domains:
- Files:
- Traceback:
- Symbols:
- Commands:
- Errors:

That makes many chat models echo the structure back.

Preferred shape:

```text
System:
You compress coding command output for later recall.
Return plain text only.
Do not use bullets, headings, markdown, or tags.
Do not invent causes or fixes.
Preserve exact filenames, symbols, test names, line numbers, commands, and error codes.

User:
Task: Summarize this command output for later recall.

Preserve exactly:
- ...
- ...
- ...

Likely failing locus:
...

Raw output:
...

Return 1-3 plain sentences only.
```

This keeps the extracted signal but avoids turning it into a response template.

## Family profiles

### 1. Gemma

#### Match

- `google/gemma-`
- `gemma-`

#### Official basis

- Google’s Hugging Face inference docs recommend structured prompt templates for chat-style use.
- Gemma text generation should use the text-generation path for text-only tasks.

Sources:
- <https://ai.google.dev/gemma/docs/core/huggingface_inference>
- <https://huggingface.co/docs/transformers/chat_templating>

#### Prompt structure

- standard chat-template flow
- `system` + `user`
- `add_generation_prompt=True`
- text-only compression path

#### Generation defaults for ctxsift

Start with:

- `do_sample=False`
- `max_new_tokens=<configured>`
- explicit `pad_token_id`
- explicit `eos_token_id` when available

Why:

- vendor docs show normal chat usage, not compression-specific sampling guidance
- for compression we want deterministic, low-drift behavior

#### Cleanup rules

- strip edge tags like `<turn|>`
- strip leading headings like `Summary:`
- strip bullets if they appear

#### Validation focus

- exact-token preservation
- no markdown headings
- no list formatting

#### Notes

- Gemma 4 cards/docs often emphasize multimodal support, but `ctxsift` compression should stay on the text-only path

### 2. Qwen2.5

#### Match

- `Qwen/Qwen2.5-`
- `qwen2.5-`

#### Official basis

- Qwen2.5 instruct cards show standard Transformers `AutoTokenizer`, `AutoModelForCausalLM`, and `apply_chat_template` usage.

Source:
- <https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct>

#### Prompt structure

- standard chat-template flow
- `system` + `user`
- `add_generation_prompt=True`

#### Generation defaults for ctxsift

Start with:

- `do_sample=False`

Why:

- the card does not give compression-specific decode guidance
- deterministic decode is the safest first profile for recall-oriented compression

#### Cleanup rules

- strip headings
- strip bullets
- collapse extra blank lines

#### Validation focus

- preserve exact command and file tokens
- suppress schema-like structured output

#### Notes

- Qwen2.5 is one of the cleanest baseline families for `ctxsift`

### 3. Qwen3

#### Match

- `Qwen/Qwen3-`
- `qwen3-`

#### Official basis

- Qwen3 has explicit thinking vs non-thinking behavior.
- Official guidance says that with `enable_thinking=True` the model outputs a `<think>...</think>` block.
- Official non-thinking suggestions mention:
  - `Temperature=0.7`
  - `TopP=0.8`
  - `TopK=20`
  - `MinP=0`
  - some distributions also mention `PresencePenalty=1.5`

Sources:
- <https://huggingface.co/Qwen/Qwen3-1.7B/blob/main/README.md>
- <https://huggingface.co/Qwen/Qwen3-1.7B-GGUF>

#### Prompt structure

- standard chat-template flow
- force `enable_thinking=False`

#### Generation defaults for ctxsift

Two profiles are worth keeping:

1. `qwen3_deterministic_compress`
   - `do_sample=False`

2. `qwen3_official_non_thinking_sampled`
   - `enable_thinking=False`
   - `do_sample=True`
   - `temperature=0.7`
   - `top_p=0.8`
   - `top_k=20`
   - `min_p=0`
   - optional `presence_penalty=1.5` if supported cleanly

Use deterministic first.
Only try sampled second if greedy output is too rigid or low quality.

#### Cleanup rules

- strip `<think>...</think>` if it leaks anyway
- strip headings and bullets

#### Validation focus

- confirm non-thinking mode really suppresses reasoning wrappers
- confirm sampled mode does not degrade exact-token preservation too much

#### Notes

- Qwen3 is promising, but only if we control thinking mode explicitly

### 4. Qwen3.5

#### Match

- `Qwen/Qwen3.5-`
- `qwen3.5-`

#### Official basis

- small official checkpoints like `Qwen3.5-0.8B` are documented as image-text-to-text / multimodal-family models.

Source:
- <https://huggingface.co/Qwen/Qwen3.5-0.8B>
- <https://huggingface.co/docs/transformers/main/en/model_doc/qwen3_5>

#### Prompt structure

- if used in `ctxsift`, keep compression prompt text-only
- do not assume multimodal inputs

#### Generation defaults for ctxsift

Start with:

- `do_sample=False`

Why:

- this is already a more complex family fit
- deterministic decode reduces one moving part during evaluation

#### Cleanup rules

- same as generic cleanup
- aggressively reject multimodal formatting leakage

#### Validation focus

- verify the text-only compression path is stable
- watch for architecture-driven verbosity or odd formatting

#### Notes

- `Qwen3.5` should be treated as a second-wave challenger, not the first baseline path

### 5. SmolLM2

#### Match

- `HuggingFaceTB/SmolLM2-`
- `smollm2-`

#### Official basis

- SmolLM2 cards show standard `apply_chat_template(..., add_generation_prompt=True)` usage.
- The direct generation example also uses:
  - `temperature=0.2`
  - `top_p=0.9`
  - `do_sample=True`

Source:
- <https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct>

#### Prompt structure

- standard chat-template flow
- `system` + `user`

#### Generation defaults for ctxsift

Two profiles are worth testing:

1. `smollm2_deterministic_compress`
   - `do_sample=False`

2. `smollm2_official_sampled`
   - `do_sample=True`
   - `temperature=0.2`
   - `top_p=0.9`

Use deterministic first.
If output becomes too clipped or shallow, compare directly to the sampled profile.

#### Cleanup rules

- strip headings
- strip bullets

#### Validation focus

- quality-vs-speed tradeoff on CPU
- whether sampled mode helps fidelity more than it hurts stability

#### Notes

- SmolLM2 is one of the best candidates to benchmark in both deterministic and official sampled modes

### 6. Granite

#### Match

- `ibm-granite/`
- `granite-`

#### Official basis

- Granite 3.3 Instruct explicitly supports structured reasoning with `<think>` and `<response>` tags.
- The example uses `thinking=True`.

Source:
- <https://huggingface.co/ibm-granite/granite-3.3-2b-instruct>

#### Prompt structure

- standard chat-template flow
- force no reasoning mode if that switch is available

#### Generation defaults for ctxsift

Start with:

- `do_sample=False`

Why:

- the official example is reasoning-oriented
- `ctxsift` compression does not want explicit reasoning tags

#### Cleanup rules

- strip `<think>`
- strip `<response>`
- strip headings/bullets

#### Validation focus

- no structured reasoning leakage
- good exact-token retention despite aggressive cleanup

#### Notes

- Granite is a challenger model, not the safest baseline family

### 7. Phi

#### Match

- `microsoft/Phi-`
- `phi-`

#### Official basis

- Phi instruct cards say the model is best used with chat-format prompts.
- The cards show role-token chat formatting and `apply_chat_template`.

Source:
- <https://huggingface.co/microsoft/Phi-3.5-mini-instruct>

#### Prompt structure

- strict chat format
- `system` + `user`
- `add_generation_prompt=True`

#### Generation defaults for ctxsift

Start with:

- `do_sample=False`

#### Cleanup rules

- generic cleanup only

#### Validation focus

- exact-token retention
- no extra role-token leakage

#### Notes

- Some Phi families may require `trust_remote_code=True`, which should be treated as a profile capability flag

## Fallback profile

Yes, if no profile matches, there must be a default path.

### Match

- fallback

### Prompt structure

- generic chat-template flow
- `system` + `user`
- `add_generation_prompt=True`

### Generation defaults

- `do_sample=False`
- configured `max_new_tokens`
- explicit `pad_token_id` / `eos_token_id` when available

### Cleanup rules

- strip short edge tags
- strip headings
- strip bullets
- collapse blank lines

### Validation rules

- preserve exact anchors
- reject empty output

### Notes

- fallback should be safe, simple, and conservative
- it should never try model-specific reasoning features
- when fallback fails, just return raw output with warning model did not give good response

## Determinism policy

For compression, deterministic decode should be the first benchmark path almost everywhere.

Use:

- `do_sample=False`

Official Transformers docs describe greedy search as the basic deterministic decoding strategy and sampling as a creativity/diversity strategy. Compression is not a creativity task.

Source:
- <https://huggingface.co/docs/transformers/generation_strategies>

Important distinction:

- vendor sampling settings may still be useful for a second profile comparison
- but `ctxsift` should not start from chatty/random defaults

## Validation and repair

All family profiles should share a post-generation validation step:

1. exact anchors preserved?
2. plain-text-only contract respected?
3. output short enough?
4. no reasoning tags?

If validation fails:

- run one repair pass with a stricter prompt
- include the missing anchors
- do not allow unlimited retries

This repair path should be shared, not family-specific.

## Recommended implementation order

1. add a profile registry keyed by model-name prefix
2. move prompt building behind profile selection
3. move generation kwargs behind profile selection
4. add shared cleanup + validation
5. add one repair retry
6. benchmark deterministic profiles first
7. benchmark selected official-sampled profiles second

## Initial profile decisions

Use these as the first implementation defaults:

- Gemma: deterministic profile
- Qwen2.5: deterministic profile
- Qwen3: deterministic non-thinking profile
- Qwen3 second profile: official non-thinking sampled profile
- Qwen3.5: deterministic profile only
- SmolLM2: deterministic profile
- SmolLM2 second profile: official sampled profile
- Granite: deterministic no-reasoning profile
- Phi: deterministic strict-chat profile
- Fallback: generic deterministic profile

## Sources

- Gemma HF inference docs: <https://ai.google.dev/gemma/docs/core/huggingface_inference>
- Transformers chat templating: <https://huggingface.co/docs/transformers/chat_templating>
- Transformers generation strategies: <https://huggingface.co/docs/transformers/generation_strategies>
- Qwen2.5-1.5B-Instruct: <https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct>
- Qwen3-1.7B README: <https://huggingface.co/Qwen/Qwen3-1.7B/blob/main/README.md>
- Qwen3-1.7B-GGUF: <https://huggingface.co/Qwen/Qwen3-1.7B-GGUF>
- Qwen3.5-0.8B: <https://huggingface.co/Qwen/Qwen3.5-0.8B>
- Qwen3.5 Transformers docs: <https://huggingface.co/docs/transformers/main/en/model_doc/qwen3_5>
- SmolLM2-1.7B-Instruct: <https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct>
- Granite-3.3-2b-instruct: <https://huggingface.co/ibm-granite/granite-3.3-2b-instruct>
- Phi-3.5-mini-instruct: <https://huggingface.co/microsoft/Phi-3.5-mini-instruct>
