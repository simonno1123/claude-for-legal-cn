#!/usr/bin/env python3
"""
Local Gemini reviewer for claude-for-legal-cn.

This script is meant to be run by the user's own terminal, not through the
Codex gemini-review MCP. It reads the Gemini API key locally and sends a
review packet directly from the machine that runs it.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


DEFAULT_KEY_FILE = Path.home() / "Desktop" / "gemini_api.md"
DEFAULT_MODEL = "gemini-3.5-flash"

DEFAULT_FILE_NAMES = {
    "CLAUDE.md",
    "README.md",
    "SKILL.md",
    "plugin.json",
    ".mcp.json",
    "currency-watch.md",
    "test-cases-cn.md",
}

TEXT_SUFFIXES = {
    ".md",
    ".json",
    ".yaml",
    ".yml",
    ".txt",
}


def read_api_key(path: Path) -> str:
    env_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if env_key:
        return env_key

    if not path.exists():
        raise SystemExit(
            f"Gemini API key not found. Set GEMINI_API_KEY or create {path}"
        )

    text = path.read_text(encoding="utf-8", errors="ignore").strip()
    match = re.search(r"(AIza[0-9A-Za-z_\-]{20,})", text)
    if match:
        return match.group(1)

    for line in text.splitlines():
        line = line.strip().strip("`").strip()
        if line and not line.startswith("#"):
            if "=" in line:
                line = line.split("=", 1)[1].strip().strip('"').strip("'")
            return line

    raise SystemExit(f"No usable API key found in {path}")


def should_include(path: Path) -> bool:
    if path.name in DEFAULT_FILE_NAMES:
        return True
    if path.suffix.lower() in TEXT_SUFFIXES and (
        "references" in path.parts or "agents" in path.parts
    ):
        return True
    return False


def collect_module_text(root: Path, module: str, max_chars: int) -> str:
    module_dir = root / module
    if not module_dir.exists():
        raise SystemExit(f"Module not found: {module_dir}")

    chunks: list[str] = []
    used = 0

    for path in sorted(module_dir.rglob("*")):
        if not path.is_file() or not should_include(path):
            continue
        rel = path.relative_to(root).as_posix()
        try:
            body = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            body = path.read_text(encoding="utf-8", errors="replace")

        block = f"\n\n--- FILE: {rel} ---\n\n{body}"
        if used + len(block) > max_chars:
            remaining = max_chars - used
            if remaining > 1000:
                chunks.append(block[:remaining] + "\n\n[TRUNCATED BY PACKET LIMIT]\n")
            break
        chunks.append(block)
        used += len(block)

    return "".join(chunks)


def build_prompt(module: str, module_text: str, extra_prompt: str) -> str:
    return f"""你是 Gemini，本次任务是作为独立审查方，复核 claude-for-legal-cn 的 `{module}` 模块中国化改造质量。

审查目标：
1. 判断该模块是否可以标记为 Phase 1 Complete。
2. 找出美国法、普通法、欧盟法或境外工具链残留。
3. 找出中国大陆法律体系下缺失的核心场景、法条路径、监管机关和工作流。
4. 给出文件级修正清单，按 P0/P1/P2 排序。
5. 如需新增测试用例，请给出 6-12 个中国法高压回归用例。

输出格式：
## Verdict
## P0 Blocking Issues
## P1 Important Issues
## P2 Polish
## China Law Gaps
## Recommended File-Level Actions
## Regression Cases

额外问题：
{extra_prompt or "无"}

以下是待审查材料：
{module_text}
"""


def call_gemini(api_key: str, model: str, prompt: str) -> str:
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        + model
        + ":generateContent?key="
        + api_key
    )
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}],
            }
        ],
        "generationConfig": {
            "temperature": 0.2,
        },
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw = resp.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Gemini API HTTP {exc.code}:\n{detail}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"Gemini API request failed: {exc}") from exc

    obj = json.loads(raw)
    parts: list[str] = []
    for cand in obj.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            text = part.get("text")
            if text:
                parts.append(text)
    if not parts:
        return json.dumps(obj, ensure_ascii=False, indent=2)
    return "\n\n".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", required=True, help="Module directory, e.g. ip-legal")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--api-key-file", default=str(DEFAULT_KEY_FILE))
    parser.add_argument("--max-chars", type=int, default=180_000)
    parser.add_argument("--extra-prompt", default="")
    parser.add_argument("--dry-run", action="store_true", help="Only write review packet, do not call API")
    args = parser.parse_args()

    root = Path.cwd()
    if not (root / args.module).exists():
        raise SystemExit("Run this script from the claude-for-legal-cn repository root.")

    now = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    packets = root / "review-packets"
    results = root / "review-results"
    packets.mkdir(exist_ok=True)
    results.mkdir(exist_ok=True)

    module_text = collect_module_text(root, args.module, args.max_chars)
    prompt = build_prompt(args.module, module_text, args.extra_prompt)
    packet_path = packets / f"{args.module}-{now}.md"
    packet_path.write_text(prompt, encoding="utf-8")

    print(f"Review packet written: {packet_path}")
    if args.dry_run:
        print("Dry run complete. Paste the packet into Gemini manually if desired.")
        return 0

    api_key = read_api_key(Path(args.api_key_file))
    answer = call_gemini(api_key, args.model, prompt)
    result_path = results / f"{args.module}-{args.model}-{now}.md"
    result_path.write_text(answer, encoding="utf-8")
    print(f"Gemini review written: {result_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
