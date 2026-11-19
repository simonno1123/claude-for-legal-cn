"""Public-repository privacy guard.

Blocks text that must never enter this public repository: real-case identifiers and
local-machine identifiers. Two layers:

1. Generic patterns (always on, safe to run in CI): PRC resident ID numbers, mobile
   numbers, bank-card-length digit runs, PRC court case numbers, Windows user paths,
   host names, machine SIDs, the private material folder name.
2. A private term list (optional, never committed): one term per line in a file kept
   in the owner's private folder (party names, case numbers, distinctive amounts,
   file names). Pass it with --terms or the PRIVACY_GUARD_TERMS environment variable.

3. Case-fact wording: in a file that names a matter code (CASE-A, CASE-B, ...), added
   lines that use enforcement-fact words (freezing, seizure, payments received, amounts,
   filing status, spouse, whereabouts ...). Public records about a matter carry only
   codes, record names, validator results and disposition wording, so such a line is
   almost always a leak. This layer is a heuristic: it cannot recognise every way of
   describing a fact, so the rule itself still applies.

A line that must legitimately contain a match can carry the marker
"privacy-guard: allow" (for example inside an HTML comment); use it sparingly.

Usage:
  python3 check_public_text.py --staged [--terms FILE]        # added lines in the git index
  python3 check_public_text.py --base REF [--terms FILE]      # added lines in REF...HEAD
  python3 check_public_text.py --tree                         # every tracked text file
  python3 check_public_text.py FILE ... [--terms FILE]
Exit status 1 when anything is found. Matched text is masked in the report.
"""

from __future__ import annotations

import argparse
import os
import pathlib
import re
import subprocess
import sys

_B = r"(?<![0-9A-Za-z])"
_E = r"(?![0-9A-Za-z])"
GENERIC = {
    "PRC_ID_NUMBER": re.compile(_B + r"[1-9]\d{5}(?:19|20)\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])\d{3}[\dXx]" + _E),
    "MOBILE_NUMBER": re.compile(_B + r"1[3-9]\d{9}" + _E),
    "CARD_LENGTH_DIGITS": re.compile(_B + r"\d{16,19}" + _E),
    "COURT_CASE_NUMBER": re.compile(r"[（(]\s*(?:19|20)\d{2}\s*[）)]\s*[一-龥]{1,2}\s*\d{2,6}\s*[一-龥]{1,6}[（(]?[一-龥]{0,4}[）)]?\s*\d+\s*号"),
    "WINDOWS_USER_PATH": re.compile(r"[A-Za-z]:\\+Users\\+[^\\\s]+", re.I),
    "HOST_NAME": re.compile(r"DESKTOP-(?!REDACTED)[A-Z0-9]{5,}", re.I),
    "MACHINE_SID": re.compile(r"S-1-5-21-(?!REDACTED)\d+"),
    "PRIVATE_FOLDER": re.compile(r"legal-cn-private|workmate-us", re.I),
}
CASE_CODE = re.compile(r"CASE-[A-Z]\b")
CASE_FACT = re.compile(r"冻结|查封|扣押|扣划|续冻|续封|执保|终本|终结本次|已付|付款|还款|分得|受偿|未签发|撤诉|配偶|下落|住址|\d+(?:\.\d+)?\s*(?:万元|元)")
ALLOW_MARK = "privacy-guard: allow"
# Known fictional or generic values that appear in existing synthetic fixtures.
BENIGN = {"9223372036854775807", "9223372036854775808", "9223372036854775817", "110101199001011234"}
_BENIGN_PATH = re.compile(r"Users\\+(?:Administrator|USER|REDACTED-OWNER|<[^>]+>)", re.I)
TEXT_SUFFIXES = {".md", ".txt", ".json", ".jsonl", ".py", ".yml", ".yaml", ".sh", ".toml", ".csv", ".html", ".js", ".ts"}
# Files that legitimately quote the patterns themselves.
SELF_EXEMPT = {"scripts/privacy_guard/check_public_text.py", "validation/privacy_guard/test_check_public_text.py"}


def load_terms(path: str | None) -> list[str]:
    path = path or os.environ.get("PRIVACY_GUARD_TERMS")
    if not path:
        return []
    terms = []
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        t = line.strip()
        if t and not t.startswith("#") and len(t) >= 2:
            terms.append(t)
    return terms


def mask(text: str) -> str:
    return text[0] + "*" * max(len(text) - 2, 1) + text[-1] if len(text) > 2 else "**"


def scan_line(line: str, terms: list[str], case_file: bool = False) -> list[tuple[str, str]]:
    if ALLOW_MARK in line:
        return []
    hits = [(name, m.group(0)) for name, rx in GENERIC.items() for m in rx.finditer(line)
            if m.group(0) not in BENIGN and not (name == "WINDOWS_USER_PATH" and _BENIGN_PATH.search(m.group(0)))]
    if case_file:
        hits += [("CASE_FACT_WORD", m.group(0)) for m in CASE_FACT.finditer(line)]
    low = line.lower()
    hits += [("PRIVATE_TERM", t) for t in terms if t.lower() in low]
    return hits


def _git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True, encoding="utf-8").stdout


def added_lines(diff: str):
    path, lineno = None, 0
    for raw in diff.splitlines():
        if raw.startswith("+++ "):
            path = raw[6:] if raw.startswith("+++ b/") else None
        elif raw.startswith("@@"):
            m = re.search(r"\+(\d+)", raw)
            lineno = int(m.group(1)) if m else 0
        elif path and raw.startswith("+") and not raw.startswith("+++"):
            yield path, lineno, raw[1:]
            lineno += 1
        elif path and not raw.startswith("-"):
            lineno += 1


def file_lines(paths):
    for p in paths:
        fp = pathlib.Path(p)
        if fp.suffix.lower() not in TEXT_SUFFIXES or not fp.is_file():
            continue
        try:
            text = fp.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            yield str(p), i, line


def _is_case_file(path: str, cache: dict) -> bool:
    if path not in cache:
        try:
            cache[path] = bool(CASE_CODE.search(pathlib.Path(path).read_text(encoding="utf-8")))
        except (OSError, UnicodeDecodeError):
            cache[path] = False
    return cache[path]


def run(lines, terms: list[str], case_check: bool = True) -> list[str]:
    report, cache = [], {}
    for path, lineno, line in lines:
        if path.replace("\\", "/") in SELF_EXEMPT:
            continue
        case_file = case_check and _is_case_file(path, cache)
        for rule, text in scan_line(line, terms, case_file):
            report.append(f"{path}:{lineno}: {rule}: {mask(text)}")
    return report


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--staged", action="store_true")
    src.add_argument("--base")
    src.add_argument("--tree", action="store_true")
    ap.add_argument("--terms")
    ap.add_argument("files", nargs="*")
    a = ap.parse_args(argv)
    terms = load_terms(a.terms)
    if a.staged:
        lines = added_lines(_git("diff", "--cached", "--unified=0", "--no-color"))
    elif a.base:
        lines = added_lines(_git("diff", f"{a.base}...HEAD", "--unified=0", "--no-color"))
    elif a.tree:
        lines = file_lines(_git("ls-files").splitlines())
    else:
        lines = file_lines(a.files)
    report = run(lines, terms, case_check=not a.tree)
    for r in report:
        print(r)
    print(f"privacy guard: {len(report)} finding(s); private term list: {'loaded, ' + str(len(terms)) + ' terms' if terms else 'not loaded'}",
          file=sys.stderr)
    return 1 if report else 0


if __name__ == "__main__":
    raise SystemExit(main())
