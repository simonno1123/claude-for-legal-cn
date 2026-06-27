#!/usr/bin/env python3
# Copyright 2026 Anthropic PBC
# SPDX-License-Identifier: Apache-2.0
"""Assert orchestrator `agent.yaml` files ship with scoped tool configs.

Runs over every `managed-agent-cookbooks/*/agent.yaml` and checks the
orchestrator's `tools:` block for the privilege-escalation gaps called out
below — keeping write and external-channel access on the leaves, not the orchestrator:

  1. No `mcp_toolset` entries on the orchestrator — MCP clients live on the
     subagent leaves, not the parent.
  2. No `write` enabled in any `agent_toolset*` config — only the designated
     writer leaf gets Write.
  3. No external collaboration tool (`cn_collab_send_message` or any `cn_collab_*`) granted. Orchestrators
     emit `handoff_request` instead of calling external collaboration directly.

Exits non-zero with a message naming the offending file + tool on any
violation. Exits 0 and prints a one-line summary per cookbook on success.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - exercised on minimal runtimes.
    yaml = None


ROOT = Path(__file__).resolve().parent.parent
COOKBOOKS_DIR = ROOT / "managed-agent-cookbooks"


def _parse_inline_mapping(text: str) -> dict[str, object]:
    """Parse the small `{ key: value }` YAML subset used in cookbook configs."""
    text = text.strip()
    if not (text.startswith("{") and text.endswith("}")):
        return {}
    out: dict[str, object] = {}
    for part in text[1:-1].split(","):
        if ":" not in part:
            continue
        key, value = part.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if value.lower() == "true":
            out[key] = True
        elif value.lower() == "false":
            out[key] = False
        else:
            out[key] = value
    return out


def _load_agent_doc(path: Path) -> dict:
    """Load agent YAML, with a narrow stdlib fallback for minimal runtimes."""
    with path.open(encoding="utf-8") as f:
        text = f.read()
    if yaml is not None:
        return yaml.safe_load(text)

    tools: list[dict] = []
    in_tools = False
    current: dict | None = None
    in_configs = False
    for raw in text.splitlines():
        stripped = raw.strip()
        if stripped == "tools:":
            in_tools = True
            continue
        if in_tools and raw and not raw.startswith((" ", "\t", "-")):
            break
        if not in_tools or not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- type:"):
            current = {"type": stripped.split(":", 1)[1].strip(), "configs": []}
            tools.append(current)
            in_configs = False
            continue
        if current is None:
            continue
        if stripped.startswith("default_config:"):
            current["default_config"] = _parse_inline_mapping(stripped.split(":", 1)[1].strip())
        elif stripped.startswith("configs:"):
            in_configs = True
        elif in_configs and stripped.startswith("- "):
            cfg = _parse_inline_mapping(stripped[2:].strip())
            if cfg:
                current.setdefault("configs", []).append(cfg)
        elif stripped.startswith("mcp_server_name:"):
            current["mcp_server_name"] = stripped.split(":", 1)[1].strip()
    return {"tools": tools}


def _lint_one(path: Path) -> list[str]:
    """Return a list of violation strings (empty if clean)."""
    errs: list[str] = []
    doc = _load_agent_doc(path)
    tools = doc.get("tools") or []
    for idx, entry in enumerate(tools):
        if not isinstance(entry, dict):
            errs.append(f"{path}: tools[{idx}] is not a mapping")
            continue
        ttype = entry.get("type", "")
        if ttype == "mcp_toolset":
            name = entry.get("mcp_server_name", "<unnamed>")
            errs.append(
                f"{path}: orchestrator must not carry mcp_toolset "
                f"(mcp_server_name={name}); move to the subagent leaf"
            )
            continue
        if not ttype.startswith("agent_toolset"):
            continue
        # Inspect per-tool configs.
        default_cfg = entry.get("default_config") or {}
        default_enabled = bool(default_cfg.get("enabled", False))
        configs = entry.get("configs") or []
        seen = set()
        for cfg in configs:
            if not isinstance(cfg, dict):
                continue
            name = cfg.get("name")
            enabled = bool(cfg.get("enabled", default_enabled))
            seen.add(name)
            if enabled and name == "write":
                errs.append(
                    f"{path}: orchestrator must not enable 'write'; "
                    f"only the writer leaf holds Write"
                )
            if enabled and isinstance(name, str) and name.startswith("cn_collab"):
                errs.append(
                    f"{path}: orchestrator must not enable external collaboration tool '{name}'; "
                    f"emit a handoff_request instead"
                )
        # If the default is enabled, it extends to every tool in the toolset —
        # including write and external collaboration. We cannot enumerate the toolset here, so
        # reject default-enabled on orchestrators outright.
        if default_enabled:
            errs.append(
                f"{path}: orchestrator agent_toolset must have "
                f"default_config.enabled=false; got default enabled=true"
            )
    return errs


def main() -> int:
    if not COOKBOOKS_DIR.is_dir():
        print(f"no cookbooks dir at {COOKBOOKS_DIR}", file=sys.stderr)
        return 2
    total_errs: list[str] = []
    clean: list[str] = []
    for agent_yaml in sorted(COOKBOOKS_DIR.glob("*/agent.yaml")):
        errs = _lint_one(agent_yaml)
        if errs:
            total_errs.extend(errs)
        else:
            clean.append(agent_yaml.parent.name)
    if total_errs:
        print("tool-scope lint FAILED:", file=sys.stderr)
        for e in total_errs:
            print(f"  {e}", file=sys.stderr)
        return 1
    for slug in clean:
        print(f"  OK {slug:24s} orchestrator tool scope clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
