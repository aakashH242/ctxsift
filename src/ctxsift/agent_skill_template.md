---
name: ctxsift
description: This skill helps you focus and keep the session context clutter-free to save the user tokens.
  When you need only some info from a command output but not the whole raw output, use the `compress` action this skill teaches you.
  When you need to recollect latest state, previous work, prior findings etc, use the `recall` action this skill teaches you before you re-read files or re-run commands.
license: MIT
---

# CtxSift Skill

Use this skill to reduce context waste from noisy command output and to recover prior command findings without rerunning work unnecessarily.

CtxSift is useful for large terminal output, test/build failures, CI logs, compiler/typechecker/linter output, stack traces, package-manager failures, Kubernetes/Terraform output, and other non-interactive commands where only selected facts are needed.

Do not use CtxSift just because a command exists. If the raw output is already short and useful, run the command normally.

## Decision workflow

CRITICAL: Before rerunning a noisy or expensive command, first try recall:

```bash frame="none"
ctxsift recall "<query>"
```

If recall gives the needed fact, use it instead of rerunning the original command.

If fresh output is needed and the agent is launching the command, prefer command-capture mode:

```bash frame="none"
ctxsift compress --intent <intent> "<instruction>" -- <command> <args>
```

If the command requires shell parsing, use shell command-capture mode:

```bash frame="none"
ctxsift compress --intent <intent> --shell "<instruction>" -- "<shell command>"
```

If the output already exists or direct command-capture is impractical, use pipe fallback:

```bash frame="none"
<command> 2>&1 | ctxsift compress --intent <intent> "<instruction>"
```

If the command is small, interactive, TUI-based, or the exact raw output itself is being debugged, skip CtxSift.

## Command forms

### Preferred: command-capture argv mode

Use this when no shell syntax is needed.

```bash frame="none"
ctxsift compress --intent exact-lines "Return only the failing test node ids, one per line. No prose." -- pytest -q
```

This lets CtxSift capture command metadata such as argv, exit code, duration, working directory, and git state.

### Use only when needed: command-capture shell mode

Use `--shell` only when the command needs shell parsing, such as pipes, redirects, command substitution, glob expansion, `&&`, `||`, or other shell-only syntax.

```bash frame="none"
ctxsift compress --intent summary --shell "Summarize only the final failing lines. Preserve the first real error exactly." -- "pytest -q 2>&1 | tail -n 80"
```

### Last resort: pipe fallback

Use pipe mode only when the command has already run, the output already exists, or wrapping the command directly is impractical.

```bash frame="none"
pytest -q 2>&1 | ctxsift compress --intent exact-lines "Return only the failing test node ids, one per line. No prose."
```

## Recall command

```bash frame="none"
ctxsift recall [OPTIONS] QUERY
```

Arguments:

* `QUERY`: required text query used to search prior compressed records.

Useful options:

* `--files <path>`: boost recall results related to one or more files.
* `--limit <N>`: maximum number of recall results to display.

Examples:

```bash frame="none"
ctxsift recall "latest pytest failure in auth tests"
ctxsift recall "terraform risky resources from previous plan"
ctxsift recall "docker build blocker dramatiq_abort"
ctxsift recall --files app/auth.py "last failure touching login middleware"
ctxsift recall --limit 3 "most recent npm build error"
```

Use recall before repeating prior exploration, especially after interruptions, context loss, failed edits, long test runs, or expensive commands.

## Compress command

```bash frame="none"
ctxsift compress --intent <intent> [--max-output-tokens <N>] [--shell] "<instruction>" [-- <command> <args>]
```

Supported flags:

* `--intent <summary|recall|exact-lines|exact-format|json|yaml|table|bullet-list>`: required output contract.
* `--max-output-tokens <N>`: optional output budget override.
* `--shell`: execute one explicit shell command string after `--` instead of safe argv mode.
* `--`: separates the CtxSift instruction from the command being captured.

Always include `-- <command>` in command-capture mode. Without a command or piped input, `ctxsift compress` has nothing useful to compress.

## Intent selection

Choose the narrowest intent that matches the needed output.

Use `summary` for readable current-step explanations when the exact output shape is not critical.

Use `recall` when compressing evidence mainly so it can be found again later with `ctxsift recall`, especially after context compaction or task switching.

Use `exact-lines` when every returned line must already exist in the raw input, such as failing test IDs, stack-trace lines, error lines, package names, resource names, or command lines.

Use `exact-format` when the answer must match one strict textual shape, such as one command, one verdict, one filename, or one token per line.

Use the structured intents when the next step benefits from a predictable schema or display shape:

* `json`: machine-readable objects or arrays for downstream parsing.
* `yaml`: structured config-like output.
* `table`: side-by-side comparison across rows and columns.
* `bullet-list`: compact human-readable checklist or findings list.

## Prompting rules

The instruction must state both content and format.

Prefer exact constraints:

* `Return only ...`
* `Return valid JSON only ...`
* `Return YAML only ...`
* `Return only the exact lines ...`
* `No prose.`
* `No markdown.`
* `Preserve these tokens exactly: ...`

Bad:

```bash frame="none"
ctxsift compress --intent summary "What matters here?" -- pytest -q
```

Good:

```bash frame="none"
ctxsift compress --intent exact-lines "Return only the failing test node ids, one per line. No prose." -- pytest -q
```

Good:

```bash frame="none"
ctxsift compress --intent json "Return valid JSON only with keys file, line, code, and message. No markdown." -- npm run build
```

Good:

```bash frame="none"
ctxsift compress --intent summary "Summarize the real blocker in 2 short sentences. Preserve exactly: ModuleNotFoundError, dramatiq_abort." -- pytest -q
```

Good:

```bash frame="none"
ctxsift compress --intent exact-format "Return only the kubectl command to delete the failing pod. No prose." -- kubectl get pods -A
```

## Rules

- Use `ctxsift recall` before rerunning a command when prior compressed output may already contain the answer.

- Use `ctxsift compress` for non-interactive commands when the raw output is large, repetitive, noisy, or when only selected facts are needed.

- Prefer command-capture argv mode when the agent is launching the command.

- Prefer argv mode over `--shell` unless shell parsing is required.

- Use `--shell` only for shell syntax such as pipes, redirects, glob expansion, command substitution, `&&`, `||`, or compound commands.

- Use pipe mode only as a fallback when output already exists or command-capture is impractical.

- Do not use CtxSift for small commands whose raw output is already concise, such as `pwd`, `git branch`, `git status --short`, simple `ls`, or short single-file inspection.

- Do not use CtxSift for interactive commands, TUI commands, REPLs, prompts, long-running daemons, watchers, or commands that require live user input.

- Do not use CtxSift when debugging CtxSift itself, command quoting, terminal formatting, ANSI color behavior, progress bars, streaming output, or exact raw CLI behavior.

- When investigating failures, preserve exact identifiers: failing test node IDs, file paths, line numbers, exception names, package names, resource names, exit codes, and the first real error.

- If CtxSift fails, errors, hangs, or appears misconfigured, fall back to the raw command once and continue. Do not get stuck repeatedly trying to compress the same command.

## Common examples

### Pytest failures

```bash frame="none"
ctxsift compress --intent exact-lines "Return only the failing test node ids, one per line. No prose." -- pytest -q
```

```bash frame="none"
ctxsift compress --intent summary "Summarize the real pytest blocker in 3 bullets. Preserve failing test ids, exception names, and file paths exactly." -- pytest -q
```

### Typecheck or lint errors

```bash frame="none"
ctxsift compress --intent json "Return valid JSON only. Each item must have file, line, code, and message. No markdown." -- mypy .
```

```bash frame="none"
ctxsift compress --intent exact-lines "Return only the ruff error lines that require code changes. No prose." -- ruff check .
```

### Build failures

```bash frame="none"
ctxsift compress --intent exact-format "Return only the first real build failure and the file, package, or module involved. No prose." -- npm run build
```

```bash frame="none"
ctxsift compress --intent summary "Summarize the build blocker in 2 short sentences. Preserve exact package names and error codes." -- docker build .
```

### Git diffs

```bash frame="none"
ctxsift compress --intent bullet-list "Summarize risky changes in at most 5 bullets. Mention only files with behavioral or security impact." -- git diff
```

```bash frame="none"
ctxsift compress --intent table "Return a table with columns file, change_type, risk, and reason. Include only meaningful code changes." -- git diff --stat
```

### Kubernetes

```bash frame="none"
ctxsift compress --intent exact-format "Return only the pod name and namespace for pods not Ready or not Running. No prose." -- kubectl get pods -A
```

```bash frame="none"
ctxsift compress --intent summary --shell "Summarize the first real Kubernetes error. Preserve pod names, namespaces, and event reasons exactly." -- "kubectl describe pod my-pod -n default 2>&1 | tail -n 120"
```

### Terraform

```bash frame="none"
ctxsift compress --intent exact-format "Return only: SAFE, REVIEW, or UNSAFE, followed by the exact risky resources. No prose." -- terraform plan
```

### Existing raw output

```bash frame="none"
pytest -q 2>&1 | ctxsift compress --intent exact-lines "Return only the failing test node ids, one per line. No prose."
```

## Setup and health

CtxSift should usually already be configured by the user.

Use these only when needed:

```bash frame="none"
ctxsift doctor
ctxsift daemon status
ctxsift daemon start
ctxsift daemon stop
```

`ctxsift configure` is interactive. Do not run it unless the user explicitly wants guided setup or local configuration.

If `ctxsift doctor` shows missing configuration, dependency problems, daemon problems, or unavailable model/runtime errors, report the concrete issue and ask the user to fix configuration only when the agent cannot safely proceed.
