#!/usr/bin/env python3
"""Check that every installed plugin can reach the reference files it cites.

Claude Code copies only a plugin's own directory into the install cache, so a
plugin cannot read the repository-level `references/` folder after install.
Shared files are therefore vendored into each plugin's `references/` folder.

This script checks two things:
  1. Every `references/<file>` cited inside a plugin exists inside that plugin.
  2. Every vendored copy of a root `references/` file is byte-identical to the
     root file, so the copies do not drift.

Output is ASCII and line-oriented so it can be checked by machine on any
platform (including a Windows console with a Chinese code page):
  FAIL missing <plugin> references/<file>
  FAIL drift <plugin>/references/<file>
  OK plugins=<n>

Exit code: 0 when everything passes, 1 otherwise.

Usage:
  python3 scripts/check-plugin-references.py         # check only
  python3 scripts/check-plugin-references.py --fix   # re-copy drifted root files
"""
from __future__ import annotations

import filecmp
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF_RE = re.compile(r"references/([A-Za-z0-9_.-]+\.(?:md|json|ya?ml))")
TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml"}


def force_utf8_output() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def plugin_dirs() -> list[Path]:
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    return [(ROOT / p["source"]).resolve() for p in market["plugins"]]


def main() -> int:
    force_utf8_output()
    fix = "--fix" in sys.argv[1:]
    root_refs = {p.name: p for p in (ROOT / "references").iterdir() if p.is_file()}
    plugins = plugin_dirs()
    failures: list[str] = []

    for plugin in plugins:
        files = [f for f in plugin.rglob("*") if f.is_file() and f.suffix in TEXT_SUFFIXES]
        present = {f.name for f in files}
        cited: set[str] = set()
        for f in files:
            cited.update(REF_RE.findall(f.read_text(encoding="utf-8", errors="replace")))

        for name in sorted(cited - present):
            failures.append(f"FAIL missing {plugin.name} references/{name}")

        vendored = plugin / "references"
        if vendored.is_dir():
            for copy in sorted(vendored.iterdir()):
                src = root_refs.get(copy.name)
                if src is None or filecmp.cmp(src, copy, shallow=False):
                    continue
                if fix:
                    shutil.copy2(src, copy)
                    print(f"RESYNC {rel(copy)}")
                else:
                    failures.append(f"FAIL drift {rel(copy)}")

    for line in failures:
        print(line)
    if failures:
        return 1
    print(f"OK plugins={len(plugins)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
