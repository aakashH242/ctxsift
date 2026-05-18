# Dataset Expansion Prompt

Use this prompt if you want a separate deep-research pass to expand the benchmark corpus:

```text
Build a production-grade benchmark dataset for a local coding-output compression tool.

## Purpose:
We are evaluating small local instruct models that must compress real command output into short recall-friendly summaries for later search and retrieval.

The model under test must do all of the following well:
- preserve exact filenames, symbols, test names, error codes, line numbers, package names, and commands
- identify the actual failing locus, not just any file mentioned in the log
- suppress noise from setup chatter, progress bars, repeated stack frames, and unrelated warnings
- avoid inventing fixes, causes, or remediation steps
- produce short plain-text summaries that are stable and useful for later recall

## Output format:
Return JSONL only.
Each line must be one valid JSON object with exactly these fields:
- case_id
- domain
- title
- instruction
- raw_input
- must_preserve_tokens
- ideal_summary
- tags

### Field requirements:
- case_id: stable slug-like identifier, unique
- domain: one primary domain label
- title: short human-readable case name
- instruction: a realistic compression instruction for the tool, not generic prose
- raw_input: realistic command output or captured run output
- must_preserve_tokens: 3 to 10 exact strings that must survive compression verbatim
- ideal_summary: concise plain text, typically 1 to 3 sentences
- tags: short labels for filtering and analysis

## Dataset size:
- Produce 53 cases total.

## Required domain distribution:
- Python runtime / traceback: 5
- pytest: 5
- mypy: 3
- ruff: 3
- pylint: 3
- black: 3
- npm: 3
- pnpm: 3
- TypeScript / tsc: 3
- ESLint: 3
- Docker build / run: 3
- docker compose: 3
- kubectl / Kubernetes: 4
- Terraform: 4
- mixed stdout/stderr generic command runs: 5

## Case realism requirements:
- Cases must look like real terminal output or captured process output.
- Include both short clean failures and long noisy failures.
- Include success-adjacent but non-zero cases where the failure appears late.
- Include logs where many files are mentioned but only one is the real failing locus.
- Include cases where the same symbol appears in multiple frames but only one frame is actionable.
- Include cases with progress lines, retries, repeated warnings, dependency chatter, or environment noise.
- Include normal command outputs too, not only failures:
  - examples: successful test run with one warning worth keeping, successful build with a final actionable note, successful command whose output still contains high-signal metadata
- Include at least 8 cases where stdout and stderr are mixed.
- Include at least 10 long noisy cases where the key issue is buried.
- Include at least 6 cases where multiple filenames appear.
- Include at least 6 cases where exact commands are important to preserve.
- Include at least 4 cases where line numbers matter critically.
- Include at least 4 cases where package or dependency names matter critically.
- Include at least 4 cases where the output contains tempting but irrelevant noise that the summary should ignore.

## Compression-task requirements:
For every case, the ideal summary should:
- state the real failure or key outcome first
- preserve exact must_preserve_tokens verbatim
- avoid invented explanations
- avoid generic filler like “there was an issue”
- avoid bullets unless the raw output genuinely has two distinct high-signal outcomes that must both be retained
- remain concise enough to be useful in retrieval

## Token selection rules:
must_preserve_tokens should include only the highest-signal exact strings, such as:
- failing file path
- exact test id
- exact error code
- exact command
- exact symbol or exception class
- exact package name
- exact line reference
Do not include low-value filler tokens.

## Safety and cleanliness:
- Keep every case self-contained and safe to publish.
- No secrets, private URLs, tokens, emails, internal hostnames, or proprietary repo names.
- No markdown fences inside raw_input.
- No placeholder text like “insert log here”.
- No explanatory notes outside the JSON objects.

## Quality bar:
This dataset must strongly stress:
- exact-token preservation
- noise filtering
- failing-locus identification
- command-output compression for later recall
- realistic distribution across common developer workflows

## Before finalizing, self-check the dataset against these failure modes and correct any weak cases:
- summary drops the most important filename, symbol, or error code
- summary overfocuses on noisy setup lines
- summary chooses the wrong file when multiple are present
- summary invents a cause or a fix
- summary is too generic to help later retrieval
- domain mix is uneven
- too many cases are easy and clean instead of realistic and messy

```
