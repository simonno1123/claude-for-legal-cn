"""Supplementary (non-binding) recount for a Route A Tesseract benchmark run.

The verdict comes only from score.py, whose rules were fixed before the run.
This script recounts two things after the fact, to show whether the verdict
depends on scoring artefacts:
- CER with NFKC normalisation (full-width and half-width punctuation treated alike);
- a lenient field check: the NFKC truth text (trailing semicolon dropped) is contained
  in the text of the words assigned to the field. This forgives extra neighbouring
  characters that Tesseract merges into one word box.
Usage: python3 supplement.py <set_dir> <run_dir>
"""

from __future__ import annotations

import json
import pathlib
import sys
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import score as S  # noqa: E402


def k(s: str) -> str:
    return S.norm(unicodedata.normalize("NFKC", s))


def main() -> None:
    set_dir, run_dir = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    cer = {True: [], False: []}
    fields = {True: [0, 0], False: [0, 0]}
    per_type: dict[str, dict[bool, list]] = {}
    for tj in sorted((set_dir / "truth").glob("*.json")):
        t = json.loads(tj.read_text(encoding="utf-8"))
        clean = t["degradation"] == "clean"
        ocr = (run_dir / "ocr" / f"{tj.stem}.txt").read_text(encoding="utf-8")
        truth = k("".join(line["text"] for line in t["lines"]))
        v = S.lev(k(ocr), truth) / max(1, len(truth))
        cer[clean].append(v)
        per_type.setdefault(tj.stem.split("__")[0].rstrip("_0123456789"), {True: [], False: []})[clean].append(v)
        ws = S.words(run_dir / "ocr" / f"{tj.stem}.tsv")
        for f in t["fields"]:
            got = k("".join(w["text"] for w in S.contained(ws, f["bbox"])))
            fields[clean][0] += 1
            fields[clean][1] += k(f["text"]).rstrip(";") in got
    avg = lambda xs: round(sum(xs) / len(xs), 4) if xs else 0.0
    out = {
        "nfkc_cer_clean": avg(cer[True]),
        "nfkc_cer_degraded": avg(cer[False]),
        "lenient_field_clean": [fields[True][1], fields[True][0]],
        "lenient_field_all": [fields[True][1] + fields[False][1], fields[True][0] + fields[False][0]],
        "nfkc_cer_by_sample_type": {n: {"clean": avg(d[True]), "degraded": avg(d[False])} for n, d in per_type.items()},
        "note": "supplementary only; the verdict stands on score.py",
    }
    (run_dir / "supplement.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
