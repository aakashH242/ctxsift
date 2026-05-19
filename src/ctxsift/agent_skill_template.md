---
name: ctxsift
description: Sift through noisy raw tool output to get exactly what you need and recover prior state quickly with the `ctxsift` CLI. Use this when terminal output is large, repetitive, or expensive to reread; when you need exact lines, identifiers, JSON, YAML, commands, or a short recall summary from noisy output; and when you may be able to recover prior facts with `ctxsift recall` instead of rerunning the same command.
---

Use this skill when working with the CtxSift CLI or when raw shell output would clutter context.

## Default workflow

Before rerunning a noisy or expensive command, first check whether the answer may already exist:

- `ctxsift recall "<query>"`

If you still need fresh output, prefer routing non-interactive command output through CtxSift:

- `some-command 2>&1 | ctxsift compress "<instruction>"`

Use raw command output only when exact uncompressed text is required or when the workflow is interactive or TUI-based.

## Rules

Always use `ctxsift compress` for most non-interactive commands when you only need selected facts, exact lines, structured output, or a concise summary.

Always use `ctxsift recall` when you need to recover prior findings, latest state, or previously extracted facts without rerunning the same command.

Skip CtxSift only when at least one of these is true:

- the user explicitly needs the full raw output
- the command is interactive or TUI-based
- you are debugging output formatting itself and compression would hide the issue

## Prompting rules for `ctxsift compress`

Your instruction must be explicit about both content and format.

Bad:

- `ctxsift compress "What matters here?"`

Good:

- `ctxsift compress "Return only the failing test ids, one per line."`
- `ctxsift compress "Return valid JSON only with keys file, line, and message."`
- `ctxsift compress "Summarize the real blocker in 2 short sentences. Preserve exactly: ModuleNotFoundError, dramatiq_abort."`
- `ctxsift compress "Return only the kubectl command to delete the failing pod. No prose."`

Prefer exact-output constraints whenever possible:

- `Return only ...`
- `Return valid JSON only ...`
- `Return YAML only ...`
- `Return only the exact lines ...`
- `No prose.`

## Examples

- `pytest -q 2>&1 | ctxsift compress "Return only the failing test node ids, one per line."`
- `git diff 2>&1 | ctxsift compress "Summarize what changed in 3 bullets. Mention only risky changes."`
- `docker build . 2>&1 | ctxsift compress "Return only the first real build failure and the file or package involved."`
- `npm run build 2>&1 | ctxsift compress "Return valid JSON only with keys file, line, code, and message for each error."`
- `terraform plan 2>&1 | ctxsift compress "Return only: SAFE, REVIEW, or UNSAFE, followed by the exact risky resources."`

## Recall guidance

Use recall before repeating prior exploration, especially after interruptions.

Examples:

- `ctxsift recall "latest pytest failure in auth tests"`
- `ctxsift recall "terraform risky resources from previous plan"`
- `ctxsift recall "docker build blocker dramatiq_abort"`

If recall gives you the needed fact, prefer using it over rerunning the original command.

## Setup and health

CtxSift should already be configured for you by the user. As defense in depth, you can use these commands to check
if `ctxsift` is ready for use or whether you need to ask the user to intervene and help you configure/manually configure it.

Use:

- `ctxsift configure` for guided local or remote setup - this is interactive.
- `ctxsift doctor` to inspect runtime health and optional dependencies
- `ctxsift daemon start`, `ctxsift daemon status`, and `ctxsift daemon stop` for daemon lifecycle work

---
