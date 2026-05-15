"""Domain-specific deterministic extraction parsers."""

from __future__ import annotations

from dataclasses import dataclass, field
import re


PYTHON_TRACEBACK_RE = re.compile(r'File ["\'](?P<path>[^"\']+)["\'], line (?P<line>\d+)(?:, in (?P<func>[^\n]+))?')
PYTHON_CAUSE_RE = re.compile(r"^(?:During handling of the above exception|The above exception was the direct cause)", re.IGNORECASE)
PYTHON_EXCEPTION_RE = re.compile(r"\b(?:[A-Z][A-Za-z0-9_]*Error|[A-Za-z_][A-Za-z0-9_]*Exception)\b")
MODULE_RE = re.compile(
    r"(?:No module named|Cannot find module|ModuleNotFoundError: No module named)\s+['\"](?P<package>[^'\"]+)['\"]"
)
PYTEST_TEST_RE = re.compile(r"(?P<test>[\w./\\-]+::[\w\[\].-]+)")
PYTEST_FAILURE_RE = re.compile(r"\b(?:FAILED|ERROR)\b")
RUFF_LINE_RE = re.compile(r"^(?P<path>.+?\.(?:py|pyi)):(?P<line>\d+):(?P<col>\d+):\s+(?P<code>[A-Z]\d{3,4})\b")
PYLINT_LINE_RE = re.compile(
    r"^(?P<path>.+?\.(?:py|pyi)):(?P<line>\d+):(?P<col>\d+):\s+(?P<code>[CRWEFI]\d{4}):\s+.+$"
)
BLACK_FILE_RE = re.compile(r"^\s*(?:would reformat|reformatted)\s+(?P<path>.+)$", re.IGNORECASE)
MYPY_LINE_RE = re.compile(
    r"^(?P<path>.+?\.(?:py|pyi)):(?P<line>\d+):\s+(?P<level>error|note):\s+.+?(?:\s+\[(?P<code>[\w-]+)\])?\s*$",
    re.IGNORECASE,
)
TS_ERROR_RE = re.compile(r"\berror TS\d+\b", re.IGNORECASE)
TSC_LINE_RE = re.compile(
    r"^(?P<path>.+?\.(?:ts|tsx|js|jsx))[\(:](?P<line>\d+)(?:,|:)(?P<col>\d+)\)?\s*[:\-]?\s*error\s+(?P<code>TS\d+)\b.+$",
    re.IGNORECASE,
)
ESLINT_RULE_RE = re.compile(r"\b(?P<rule>@?[\w-]+(?:/[\w-]+)?(?:/[\w-]+)?)\b(?=\s*$)")
ESLINT_LINE_RE = re.compile(
    r"^\s*\d+:\d+\s+(?:error|warning)\s+.+\s+(?P<rule>@?[\w-]+(?:/[\w-]+)?(?:/[\w-]+)?)\s*$",
    re.IGNORECASE,
)
DOCKER_ERROR_RE = re.compile(r"\b(?:docker|docker-compose|compose)\b.*\b(?:error|failed|denied|pull)\b", re.IGNORECASE)
KUBERNETES_ERROR_RE = re.compile(
    r"(?:Error from server|kubectl|deployment\.apps/|pod/|service/|configmap/).*(?:error|failed|forbidden|not found|crashloopbackoff)?",
    re.IGNORECASE,
)
TERRAFORM_ERROR_RE = re.compile(
    r".*\b(?:Error:|Failed to|Unsupported argument|Unsupported block type|No value for required variable|│ Error:|Initializing the backend\.\.\.)\b.*",
    re.IGNORECASE,
)
TERRAFORM_RESOURCE_RE = re.compile(r"\b(?:on\s+.+\.tf\s+line\s+\d+|with\s+[\w.\"\-\[\]]+|resource\s+[\w_]+\s+\"[^\"]+\")\b", re.IGNORECASE)
NPM_ERROR_RE = re.compile(r"^\s*npm ERR!\s+.+$", re.IGNORECASE)
PNPM_ERROR_RE = re.compile(r".*\b(?:ERR_PNPM_[A-Z0-9_]+|ELIFECYCLE)\b.*", re.IGNORECASE)
NODE_BUILD_RE = re.compile(
    r".*\b(?:missing script|command failed with exit code|cannot find module|failed to compile|module not found|error Command failed)\b.*",
    re.IGNORECASE,
)
DOCKER_COMMAND_PATTERNS = (
    ("docker compose up", re.compile(r"\bdocker\s+compose\s+up\b", re.IGNORECASE)),
    ("docker compose build", re.compile(r"\bdocker\s+compose\s+build\b", re.IGNORECASE)),
    ("docker compose pull", re.compile(r"\bdocker\s+compose\s+pull\b", re.IGNORECASE)),
    ("docker-compose up", re.compile(r"\bdocker-compose\s+up\b", re.IGNORECASE)),
    ("docker-compose build", re.compile(r"\bdocker-compose\s+build\b", re.IGNORECASE)),
    ("docker-compose pull", re.compile(r"\bdocker-compose\s+pull\b", re.IGNORECASE)),
    ("docker build", re.compile(r"\bdocker\s+build\b", re.IGNORECASE)),
    ("docker run", re.compile(r"\bdocker\s+run\b", re.IGNORECASE)),
    ("docker pull", re.compile(r"\bdocker\s+pull\b", re.IGNORECASE)),
)
DOCKER_ERROR_PATTERNS = (
    re.compile(r"^\s*(?:docker|docker-compose|compose).*\b(?:error|failed|denied|pull)\b.*$", re.IGNORECASE),
    re.compile(r"^\s*failed to solve\b.*$", re.IGNORECASE),
    re.compile(r"^\s*error response from daemon:\s*.*$", re.IGNORECASE),
    re.compile(r"\b(?:pull access denied|requested access to the resource is denied|manifest unknown|no such image)\b", re.IGNORECASE),
    re.compile(r"\b(?:cannot connect to the docker daemon|is the docker daemon running)\b", re.IGNORECASE),
    re.compile(r"\b(?:port is already allocated|bind: address already in use|network .+ not found)\b", re.IGNORECASE),
    re.compile(r"\b(?:service .+ exited with code \d+|dependency failed to start|failed to create shim task)\b", re.IGNORECASE),
)
KUBECTL_COMMAND_PATTERNS = (
    ("kubectl apply", re.compile(r"\bkubectl\s+apply\b", re.IGNORECASE)),
    ("kubectl describe", re.compile(r"\bkubectl\s+describe\b", re.IGNORECASE)),
    ("kubectl logs", re.compile(r"\bkubectl\s+logs\b", re.IGNORECASE)),
    ("kubectl get", re.compile(r"\bkubectl\s+get\b", re.IGNORECASE)),
    ("kubectl rollout", re.compile(r"\bkubectl\s+rollout\b", re.IGNORECASE)),
    ("kubectl exec", re.compile(r"\bkubectl\s+exec\b", re.IGNORECASE)),
)
KUBECTL_ERROR_PATTERNS = (
    re.compile(r"^\s*Error from server.*$", re.IGNORECASE),
    re.compile(r"^\s*error:\s+.*$", re.IGNORECASE),
    re.compile(r"\b(?:CrashLoopBackOff|ImagePullBackOff|ErrImagePull|CreateContainerConfigError|CreateContainerError|OOMKilled)\b", re.IGNORECASE),
    re.compile(r"\b(?:no matches for kind|unable to recognize|resource mapping not found)\b", re.IGNORECASE),
    re.compile(r"\b(?:forbidden|not found|already exists|timed out waiting for the condition|context deadline exceeded)\b", re.IGNORECASE),
    re.compile(r"^\s*Warning\s+\w+\s+.*\b(?:Failed|BackOff|Unhealthy|FailedMount|FailedScheduling)\b.*$", re.IGNORECASE),
)


@dataclass(frozen=True)
class DomainExtractionResult:
    """Partial signal from one domain parser."""

    domain: str
    matched: bool
    traceback_frames: list[str] = field(default_factory=list)
    tests: list[str] = field(default_factory=list)
    packages: list[str] = field(default_factory=list)
    symbols: list[str] = field(default_factory=list)
    command_terms: list[str] = field(default_factory=list)
    eslint_rules: list[str] = field(default_factory=list)
    warning_lines: list[str] = field(default_factory=list)
    error_lines: list[str] = field(default_factory=list)
    exit_code_lines: list[str] = field(default_factory=list)


def run_domain_parsers(text: str) -> list[DomainExtractionResult]:
    """Run all domain parsers against one input."""
    return [
        parse_python(text),
        parse_pytest(text),
        parse_ruff(text),
        parse_pylint(text),
        parse_black(text),
        parse_mypy(text),
        parse_node_package_manager(text),
        parse_typescript(text),
        parse_eslint(text),
        parse_docker(text),
        parse_kubernetes(text),
        parse_terraform(text),
    ]


def parse_python(text: str) -> DomainExtractionResult:
    frames = [
        _compact_frame(match.group("path"), match.group("line"), match.group("func"))
        for match in PYTHON_TRACEBACK_RE.finditer(text)
    ]
    packages = [match.group("package") for match in MODULE_RE.finditer(text)]
    symbols = [match.group(0) for match in PYTHON_EXCEPTION_RE.finditer(text)]
    error_lines = _matching_lines(text, re.compile(r"\b(?:traceback|exception|error)\b", re.IGNORECASE))
    error_lines.extend(_python_exception_lines(text))
    error_lines.extend(_matching_lines(text, PYTHON_CAUSE_RE))
    matched = bool(frames or packages or symbols or "Traceback" in text or error_lines)
    return DomainExtractionResult(
        domain="python",
        matched=matched,
        traceback_frames=frames,
        packages=packages,
        symbols=symbols,
        command_terms=["python"] if matched else [],
        error_lines=_dedupe(error_lines),
    )


def parse_pytest(text: str) -> DomainExtractionResult:
    tests = [match.group("test") for match in PYTEST_TEST_RE.finditer(text)]
    matched = bool(tests or "====" in text and "test session starts" in text.lower())
    error_lines = [line.strip() for line in text.splitlines() if PYTEST_FAILURE_RE.search(line)]
    error_lines.extend(_matching_lines(text, re.compile(r"=+ FAILURES =+", re.IGNORECASE)))
    return DomainExtractionResult(
        domain="pytest",
        matched=matched,
        tests=tests,
        command_terms=["pytest"] if "pytest" in text.lower() else [],
        error_lines=_dedupe(error_lines),
    )


def parse_ruff(text: str) -> DomainExtractionResult:
    error_lines = [line.strip() for line in text.splitlines() if RUFF_LINE_RE.search(line)]
    matched = bool(error_lines or "ruff" in text.lower())
    return DomainExtractionResult(
        domain="ruff",
        matched=matched,
        command_terms=["ruff"] if matched else [],
        error_lines=error_lines,
    )


def parse_pylint(text: str) -> DomainExtractionResult:
    error_lines = [line.strip() for line in text.splitlines() if PYLINT_LINE_RE.search(line)]
    matched = bool(error_lines or "pylint" in text.lower())
    return DomainExtractionResult(
        domain="pylint",
        matched=matched,
        command_terms=["pylint"] if matched else [],
        error_lines=error_lines,
    )


def parse_black(text: str) -> DomainExtractionResult:
    error_lines = [line.strip() for line in text.splitlines() if BLACK_FILE_RE.search(line)]
    matched = bool(error_lines or "would reformat" in text.lower() or "black" in text.lower())
    return DomainExtractionResult(
        domain="black",
        matched=matched,
        command_terms=["black"] if matched else [],
        error_lines=error_lines,
    )


def parse_mypy(text: str) -> DomainExtractionResult:
    error_lines = [line.strip() for line in text.splitlines() if MYPY_LINE_RE.search(line)]
    matched = bool(error_lines or "mypy" in text.lower())
    return DomainExtractionResult(
        domain="mypy",
        matched=matched,
        command_terms=["mypy"] if matched else [],
        error_lines=error_lines,
    )


def parse_node_package_manager(text: str) -> DomainExtractionResult:
    error_lines = [line.strip() for line in text.splitlines() if NPM_ERROR_RE.search(line)]
    error_lines.extend([line.strip() for line in text.splitlines() if PNPM_ERROR_RE.search(line)])
    error_lines.extend([line.strip() for line in text.splitlines() if NODE_BUILD_RE.search(line)])
    command_terms = []
    lower_text = text.lower()
    if "pnpm" in lower_text:
        command_terms.append("pnpm")
    if "npm" in lower_text:
        command_terms.append("npm")
    matched = bool(error_lines or command_terms)
    return DomainExtractionResult(
        domain="node_package_manager",
        matched=matched,
        command_terms=_dedupe(command_terms),
        error_lines=_dedupe(error_lines),
    )


def parse_typescript(text: str) -> DomainExtractionResult:
    error_lines = [line.strip() for line in text.splitlines() if TSC_LINE_RE.search(line)]
    error_lines.extend(_matching_lines(text, TS_ERROR_RE))
    matched = bool(
        error_lines
        or re.search(r"\btsconfig\.json\b", text, re.IGNORECASE)
        or "typescript" in text.lower()
        or "tsc" in text.lower()
    )
    return DomainExtractionResult(
        domain="typescript",
        matched=matched,
        error_lines=_dedupe(error_lines),
        command_terms=["tsc"] if matched else [],
    )


def parse_eslint(text: str) -> DomainExtractionResult:
    rules = []
    saw_eslint_marker = "eslint" in text.lower()
    for line in text.splitlines():
        rule_match = ESLINT_LINE_RE.search(line)
        if rule_match is not None:
            rules.append(rule_match.group("rule"))
    matched = bool(rules or saw_eslint_marker)
    return DomainExtractionResult(
        domain="eslint",
        matched=matched,
        eslint_rules=rules,
        command_terms=["eslint"] if saw_eslint_marker else [],
        warning_lines=_matching_lines(text, re.compile(r"\bwarning\b", re.IGNORECASE)),
        error_lines=_matching_lines(text, re.compile(r"\berror\b", re.IGNORECASE)),
    )


def parse_docker(text: str) -> DomainExtractionResult:
    error_lines = _matching_pattern_lines(text, DOCKER_ERROR_PATTERNS)
    command_terms = _matched_commands(text, DOCKER_COMMAND_PATTERNS)
    lower_text = text.lower()
    if "docker-compose" in lower_text:
        command_terms.append("docker-compose")
    if "docker compose" in lower_text:
        command_terms.append("docker compose")
    if "docker" in lower_text:
        command_terms.append("docker")
    matched = bool(error_lines or command_terms)
    return DomainExtractionResult(
        domain="docker",
        matched=matched,
        command_terms=_dedupe(command_terms),
        error_lines=_dedupe(error_lines),
    )


def parse_kubernetes(text: str) -> DomainExtractionResult:
    matched_lines = _matching_pattern_lines(text, KUBECTL_ERROR_PATTERNS)
    command_terms = _matched_commands(text, KUBECTL_COMMAND_PATTERNS)
    warning_lines = [line for line in matched_lines if line.lower().startswith("warning ")]
    error_lines = [line for line in matched_lines if line not in warning_lines]
    lower_text = text.lower()
    if "kubectl" in lower_text:
        command_terms.append("kubectl")
    matched = bool(matched_lines or command_terms)
    return DomainExtractionResult(
        domain="kubernetes",
        matched=matched,
        command_terms=_dedupe(command_terms),
        warning_lines=_dedupe(warning_lines),
        error_lines=_dedupe(error_lines),
    )


def parse_terraform(text: str) -> DomainExtractionResult:
    error_lines = [line.strip() for line in text.splitlines() if TERRAFORM_ERROR_RE.search(line)]
    error_lines.extend([line.strip() for line in text.splitlines() if TERRAFORM_RESOURCE_RE.search(line)])
    lower_text = text.lower()
    terraform_context = bool(
        "terraform" in lower_text
        or ".tf" in lower_text
        or re.search(r'\bresource\s+"', lower_text)
        or re.search(r"^\s*with\s+[\w.\"\-\[\]]+", text, re.IGNORECASE | re.MULTILINE)
        or re.search(r"^\s*on\s+.+\.tf\s+line\s+\d+", text, re.IGNORECASE | re.MULTILINE)
    )
    command_terms = []
    if "terraform" in lower_text:
        command_terms.append("terraform")
    if "terraform init" in lower_text or "initializing the backend" in lower_text:
        command_terms.append("terraform init")
    if "terraform plan" in lower_text:
        command_terms.append("terraform plan")
    if "terraform apply" in lower_text:
        command_terms.append("terraform apply")
    matched = bool(terraform_context and (error_lines or command_terms))
    return DomainExtractionResult(
        domain="terraform",
        matched=matched,
        command_terms=_dedupe(command_terms) if matched else [],
        error_lines=_dedupe(error_lines) if matched else [],
    )


def _compact_frame(path: str, line: str, func: str | None) -> str:
    if func:
        return f'{path}:{line} in {func.strip()}'
    return f"{path}:{line}"


def _matching_lines(text: str, pattern: re.Pattern[str]) -> list[str]:
    return [line.strip() for line in text.splitlines() if pattern.search(line)]


def _matching_pattern_lines(text: str, patterns: tuple[re.Pattern[str], ...]) -> list[str]:
    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if any(pattern.search(stripped) for pattern in patterns):
            lines.append(stripped)
    return lines


def _matched_commands(text: str, command_patterns: tuple[tuple[str, re.Pattern[str]], ...]) -> list[str]:
    return [command for command, pattern in command_patterns if pattern.search(text)]


def _python_exception_lines(text: str) -> list[str]:
    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("File "):
            continue
        if re.match(r"^[A-Za-z_][A-Za-z0-9_]*(?:Error|Exception):", stripped):
            lines.append(stripped)
    return lines


def _dedupe(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result
