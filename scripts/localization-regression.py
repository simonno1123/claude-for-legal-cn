#!/usr/bin/env python3
"""China localization regression checks for claude-for-legal-cn.

This script intentionally checks repository invariants, not the freshness or
coverage of any legal database. Real provider integrations and lawyer review
remain deployment/workflow responsibilities.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ROOT_MODULES = {
    "ai-governance-legal",
    "commercial-legal",
    "corporate-legal",
    "employment-legal",
    "ip-legal",
    "law-student",
    "legal-builder-hub",
    "legal-clinic",
    "litigation-legal",
    "privacy-legal",
    "product-legal",
    "regulatory-legal",
}

PHASE_1_5_WORKSPACE_MODULES = (
    "commercial-legal",
    "privacy-legal",
    "product-legal",
    "ip-legal",
    "employment-legal",
)

PHASE_1_5_LIFECYCLE_COMMANDS = (
    "status",
    "new",
    "list",
    "switch",
    "update",
    "close",
    "reopen",
    "none",
)

IGNORED_TOP_LEVEL_DIRS = {".git", ".codex-coordination"}

FORBIDDEN_DEFAULT_PHRASES = (
    "one vendor plugin",
    "twelve first-party legal plugins, one vendor plugin",
    "Westlaw / 美国法研究，不属于 `claude-for-legal-cn` 默认安装清单。中国法律研究请优先使用",
)

DEFAULT_BACKSLIDE_PATTERNS = (
    re.compile(r"default(?:s| framework| source| path)?[^.\n]*(Westlaw|CourtListener|Federal Register|Regulations\.gov)", re.I),
    re.compile(r"(Westlaw|CourtListener|Federal Register|Regulations\.gov)[^.\n]*default", re.I),
    re.compile(r"(attorney-client privilege|work product doctrine)[^.\n]*(protects|protected|shield|safe)", re.I),
)

DEFAULT_BACKSLIDE_ALLOWLIST = {
    "CLAUDE.md",
    "AGENTS.md",
    "references/international-extensions.md",
    "references/us-to-cn-legal-terms.md",
    "external_plugins/cocounsel-legal/README.md",
    "external_plugins/cocounsel-legal/skills/deep-research/SKILL.md",
}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def is_ignored(path: Path) -> bool:
    return bool(IGNORED_TOP_LEVEL_DIRS.intersection(path.relative_to(ROOT).parts))


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - report exact file path to user
        fail(errors, f"{rel(path)} is not valid JSON: {exc}")
        return None


def check_all_json(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.json")):
        if is_ignored(path):
            continue
        load_json(path, errors)


def check_marketplace(errors: list[str]) -> None:
    marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json", errors)
    if not marketplace:
        return

    plugins = marketplace.get("plugins", [])
    names = [plugin.get("name") for plugin in plugins]
    if set(names) != ROOT_MODULES:
        missing = sorted(ROOT_MODULES - set(names))
        extra = sorted(set(names) - ROOT_MODULES)
        fail(errors, f"marketplace plugins mismatch; missing={missing}, extra={extra}")

    for plugin in plugins:
        name = plugin.get("name", "")
        source = plugin.get("source", "")
        if source.startswith("./external_plugins") or "cocounsel" in name.lower():
            fail(errors, f"external/vendor plugin must not be in default marketplace: {name}")
            continue
        plugin_path = ROOT / source.removeprefix("./")
        manifest = plugin_path / ".claude-plugin" / "plugin.json"
        if not manifest.exists():
            fail(errors, f"{source} does not contain .claude-plugin/plugin.json")
            continue
        plugin_json = load_json(manifest, errors)
        if plugin_json and plugin_json.get("name") != name:
            fail(errors, f"{rel(manifest)} name does not match marketplace entry {name}")


def check_mcp(errors: list[str]) -> None:
    template = load_json(ROOT / "scripts" / "mcp-template.json", errors)
    if template:
        legal_data = template.get("baseServers", {}).get("legal-data", {})
        args = legal_data.get("args", [])
        if "connectors/legal-data/server.js" not in args:
            fail(errors, "scripts/mcp-template.json must route legal-data to connectors/legal-data/server.js")

    server = ROOT / "connectors" / "legal-data" / "server.js"
    sample_index = ROOT / "connectors" / "legal-data" / "local-index.sample.json"
    if not server.exists():
        fail(errors, "connectors/legal-data/server.js is missing")
    if not sample_index.exists():
        fail(errors, "connectors/legal-data/local-index.sample.json is missing")

    modules_config = load_json(ROOT / "scripts" / "mcp-modules.json", errors)
    if modules_config:
        raw_paths = [module.get("path") for module in modules_config.get("modules", [])]
        if not all(isinstance(path, str) and path for path in raw_paths):
            fail(errors, "scripts/mcp-modules.json contains a missing or invalid path")
        configured_paths = {path for path in raw_paths if isinstance(path, str)}
        if configured_paths != ROOT_MODULES:
            missing = sorted(ROOT_MODULES - configured_paths)
            extra = sorted(configured_paths - ROOT_MODULES)
            fail(
                errors,
                f"MCP module paths mismatch; missing={missing}, extra={extra}",
            )

    for module in sorted(ROOT_MODULES):
        mcp = load_json(ROOT / module / ".mcp.json", errors)
        if not mcp:
            continue
        if "legal-data" not in mcp.get("mcpServers", {}):
            fail(errors, f"{module}/.mcp.json must include legal-data")


def check_test_cases(errors: list[str]) -> None:
    for module in sorted(ROOT_MODULES):
        cases = ROOT / module / "references" / "test-cases-cn.md"
        if not cases.exists():
            fail(errors, f"{module} is missing references/test-cases-cn.md")
            continue
        text = cases.read_text(encoding="utf-8")
        rows = len(re.findall(r"^\|", text, flags=re.MULTILINE))
        if rows < 3:
            fail(errors, f"{rel(cases)} does not contain enough regression cases")
        if not re.search(r"中国|大陆|中华人民共和国|民法典|公司法|劳动|个人信息|监管|法考|法律援助|China Mainland|PIPL|Data Security Law", text):
            fail(errors, f"{rel(cases)} does not look China-localized")


def check_docs(errors: list[str]) -> None:
    for path in (ROOT / "CLAUDE.md", ROOT / "AGENTS.md", ROOT / "README.md"):
        text = path.read_text(encoding="utf-8")
        for phrase in FORBIDDEN_DEFAULT_PHRASES:
            if phrase in text:
                fail(errors, f"{rel(path)} still contains stale default-scope phrase: {phrase}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "legal-data" not in readme or "connectors/legal-data/server.js" not in readme:
        fail(errors, "README.md must document the local legal-data server")
    if "其他企业系统连接器仍为占位" not in readme:
        fail(errors, "README.md must distinguish legal-data from other placeholder enterprise connectors")


def require_tokens(
    path: Path,
    tokens: tuple[str, ...],
    errors: list[str],
    purpose: str,
) -> str:
    if not path.exists():
        fail(errors, f"{rel(path)} is missing ({purpose})")
        return ""

    text = path.read_text(encoding="utf-8")
    missing = [token for token in tokens if token not in text]
    if missing:
        fail(errors, f"{rel(path)} is missing {purpose} markers: {missing}")
    return text


def check_phase_1_5_workflows(errors: list[str]) -> None:
    """Validate the static contract for local, human-triggered workflows."""

    require_tokens(
        ROOT / "references" / "local-workflow-contract.md",
        (
            "matters/index.yaml",
            "matter.yaml",
            "history.yaml",
            "_archived",
            "enabled: false",
            "active_matter: null",
            "cross_matter_context: false",
            "owner:",
            "status: active",
            "deadline: null",
            "event_id:",
            "human-confirmed",
            "failure",
        ),
        errors,
        "Phase 1.5 local workflow contract",
    )

    stale_workspace_phrases = (
        "Phase 2 placeholder",
        "降级为 Phase 2",
        "Phase 1 默认关闭",
        "第一阶段默认关闭",
    )

    for module in PHASE_1_5_WORKSPACE_MODULES:
        module_root = ROOT / module
        skill = module_root / "skills" / "matter-workspace" / "SKILL.md"
        skill_text = require_tokens(
            skill,
            (
                "name: matter-workspace",
                "index.yaml",
                "matter.yaml",
                "history.yaml",
                "_archived",
                "version: 1",
                "enabled: true",
                "active_matter: null",
                "cross_matter_context: false",
                "matters: []",
            ),
            errors,
            f"{module} matter workspace schema",
        )

        if skill_text.startswith("---\n"):
            parts = skill_text.split("---", 2)
            frontmatter = parts[1] if len(parts) == 3 else ""
            missing_commands = [
                command
                for command in PHASE_1_5_LIFECYCLE_COMMANDS
                if not re.search(rf"\b{re.escape(command)}\b", frontmatter)
            ]
            if missing_commands:
                fail(
                    errors,
                    f"{rel(skill)} frontmatter is missing lifecycle commands: {missing_commands}",
                )
        else:
            fail(errors, f"{rel(skill)} is missing YAML frontmatter")

        for phrase in stale_workspace_phrases:
            if phrase in skill_text:
                fail(errors, f"{rel(skill)} still contains stale workspace status: {phrase}")

        require_tokens(
            module_root / "skills" / "cold-start-interview" / "SKILL.md",
            (
                "enabled: true",
                "active_matter: null",
                "cross_matter_context: false",
                "matters: []",
            ),
            errors,
            f"{module} workspace initialization",
        )
        require_tokens(
            module_root / "CLAUDE.md",
            ("matters/index.yaml", "active matter", "Cross-matter context"),
            errors,
            f"{module} profile preflight",
        )

    require_tokens(
        ROOT / "product-legal" / "skills" / "launch-tracker" / "SKILL.md",
        (
            "name: launch-tracker",
            "status | add | import | list | update | queue | close",
            "launch-tracker.yaml",
            "launch-tracker-history.yaml",
            "version: 1",
            "entries:",
            "launch_id:",
            "legal_review:",
            "event_id",
            "人工确认",
        ),
        errors,
        "Product local launch tracker schema",
    )
    require_tokens(
        ROOT / "product-legal" / "agents" / "launch-watcher.md",
        ("人工触发", "launch-tracker.yaml", "不后台运行", "不自动通知"),
        errors,
        "Product local launch watcher boundary",
    )

    commercial_checks = {
        "agents/deal-debrief.md": (
            "deviation-log.yaml",
            "deal_id",
            "deviation_id",
            "exclude_from_patterns",
            "去重",
        ),
        "agents/playbook-monitor.md": (
            "pattern_threshold",
            "lookback_months",
            "playbook-proposals.yaml",
            "playbook-monitor-history.yaml",
            "不得自动修改",
        ),
        "agents/renewal-watcher.md": (
            "renewal-register.yaml",
            "renewal-run-history.yaml",
            "run_id",
            "不后台运行",
        ),
        "skills/renewal-tracker/SKILL.md": (
            "renewal-register.yaml",
            "renewal_id",
            "renewal-run-history.yaml",
            "去重",
        ),
        "skills/review-proposals/SKILL.md": (
            "playbook-proposals.yaml",
            "accept",
            "reject",
            "edit",
            "defer",
            "精确 diff",
        ),
    }
    for relative_path, tokens in commercial_checks.items():
        require_tokens(
            ROOT / "commercial-legal" / relative_path,
            tokens,
            errors,
            "Commercial local workflow persistence",
        )

    documentation_checks = {
        "PHASE_2_ROADMAP.md": (
            "Phase 1.5 Implemented / Active",
            "Phase 2（Future / Planned）",
        ),
        "docs/UPSTREAM_MAPPING_MATRIX.md": (
            "Preserved responsibility (Phase 1 + 1.5)",
            "Future extension",
        ),
        "CHINA_LOCALIZATION_STATUS.md": (
            "PHASE 1 + 1.5 VALID",
            "2026-07-14 Phase 1.5 本地工作流",
        ),
        "PROJECT_USAGE_GUIDE.md": ("Phase 1.5 本地事项工作流",),
    }
    for relative_path, tokens in documentation_checks.items():
        require_tokens(
            ROOT / relative_path,
            tokens,
            errors,
            "Phase 1.5 documentation status",
        )


def check_default_backslide(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*")):
        if path.is_dir() or is_ignored(path):
            continue
        name = rel(path)
        if name in DEFAULT_BACKSLIDE_ALLOWLIST:
            continue
        if path.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".py", ".sh"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in DEFAULT_BACKSLIDE_PATTERNS:
            if pattern.search(text):
                fail(errors, f"{name} appears to reintroduce foreign-law defaults: {pattern.pattern}")


def check_matter_workspace(errors: list[str]) -> None:
    """Run the offline Matter Workspace integration gate."""

    script = ROOT / "scripts" / "test-matter-workspace.sh"
    if not script.exists():
        fail(errors, "scripts/test-matter-workspace.sh is missing")
        return

    try:
        result = subprocess.run(
            ["bash", str(script)],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        fail(errors, f"Matter Workspace integration test could not start: {exc}")
        return

    if result.returncode == 0:
        return

    lines = (result.stdout + result.stderr).strip().splitlines()
    diagnostics = "\n".join(lines[-40:]).replace(str(ROOT), ".")
    if not diagnostics:
        diagnostics = f"exit code {result.returncode} with no output"
    fail(
        errors,
        "Matter Workspace integration test failed "
        f"(scripts/test-matter-workspace.sh):\n{diagnostics}",
    )


def main() -> int:
    errors: list[str] = []
    check_all_json(errors)
    check_marketplace(errors)
    check_mcp(errors)
    check_test_cases(errors)
    check_docs(errors)
    check_phase_1_5_workflows(errors)
    check_default_backslide(errors)
    check_matter_workspace(errors)

    if errors:
        print("China localization regression FAILED:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("China localization regression OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
