#!/usr/bin/env python3
"""China localization regression checks for claude-for-legal-cn.

This script intentionally checks repository invariants, not the freshness or
coverage of any legal database. Real provider integrations and lawyer review
remain deployment/workflow responsibilities.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FIRST_SEQUENCE_MODULES = {
    "ai-governance-legal",
    "commercial-legal",
    "corporate-legal",
    "employment-legal",
    "ip-legal",
    "legal-builder-hub",
    "litigation-legal",
    "privacy-legal",
    "product-legal",
    "regulatory-legal",
}

PHASE_2_MODULES = {
    "phase-2/law-student",
    "phase-2/legal-clinic",
}

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
        if ".git" in path.parts:
            continue
        load_json(path, errors)


def check_marketplace(errors: list[str]) -> None:
    marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json", errors)
    if not marketplace:
        return

    plugins = marketplace.get("plugins", [])
    names = [plugin.get("name") for plugin in plugins]
    if set(names) != FIRST_SEQUENCE_MODULES:
        missing = sorted(FIRST_SEQUENCE_MODULES - set(names))
        extra = sorted(set(names) - FIRST_SEQUENCE_MODULES)
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

    for module in sorted(FIRST_SEQUENCE_MODULES | PHASE_2_MODULES):
        mcp = load_json(ROOT / module / ".mcp.json", errors)
        if not mcp:
            continue
        if "legal-data" not in mcp.get("mcpServers", {}):
            fail(errors, f"{module}/.mcp.json must include legal-data")


def check_test_cases(errors: list[str]) -> None:
    required = FIRST_SEQUENCE_MODULES | PHASE_2_MODULES
    for module in sorted(required):
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


def check_default_backslide(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*")):
        if path.is_dir() or ".git" in path.parts:
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


def main() -> int:
    errors: list[str] = []
    check_all_json(errors)
    check_marketplace(errors)
    check_mcp(errors)
    check_test_cases(errors)
    check_docs(errors)
    check_default_backslide(errors)

    if errors:
        print("China localization regression FAILED:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("China localization regression OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
