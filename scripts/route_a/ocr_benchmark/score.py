"""Score a Route A Tesseract benchmark run against fictional ground truth.

Rules fixed by the confirmed design (TASK_PHASE2_ROUTE_A_TESSERACT_CHI_SIM_BENCHMARK_DESIGN section 4-5):
- CER on whitespace-stripped page text, clean vs degraded groups;
- key fields: words assigned by containment (>= 50% of the word box inside the field box), exact match;
- locator: merged box of assigned words vs truth box, IoU >= 0.5;
- table cells (clean group): words contained in the cell box, exact match;
- low-confidence rule: word conf < 80; field flagged if any assigned word is low;
  covered = wrong & flagged; missing field (no words) = uncovered; all versions counted;
- failed page: empty output or CER > 0.5.
Usage: python3 score.py <set_dir> <run_dir>
"""

from __future__ import annotations

import csv
import json
import pathlib
import re
import sys

LOW = 80
PASS = {"cer_clean": 0.03, "cer_degraded": 0.10, "field_clean": 0.98, "cell_clean": 0.95, "loc_all": 0.95}
LIMITED = {"cer_clean": 0.08, "coverage": 0.95, "false_flag": 0.30}


def norm(s: str) -> str:
    return re.sub(r"\s+", "", s)


def lev(a: str, b: str) -> int:
    if len(a) < len(b):
        a, b = b, a
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def words(tsv: pathlib.Path) -> list[dict]:
    out = []
    with tsv.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE):
            if row.get("level") == "5" and (row.get("text") or "").strip():
                l, t, w, h = (int(row[k]) for k in ("left", "top", "width", "height"))
                out.append({"text": row["text"].strip(), "conf": float(row["conf"]), "box": [l, t, l + w, t + h]})
    return out


def area(b: list) -> float:
    return max(0, b[2] - b[0]) * max(0, b[3] - b[1])


def inter(a: list, b: list) -> float:
    return area([max(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), min(a[3], b[3])])


def contained(ws: list[dict], box: list) -> list[dict]:
    return [w for w in ws if area(w["box"]) and inter(w["box"], box) / area(w["box"]) >= 0.5]


def iou(a: list, b: list) -> float:
    i = inter(a, b)
    u = area(a) + area(b) - i
    return i / u if u else 0.0


def merge(ws: list[dict]) -> list:
    return [min(w["box"][0] for w in ws), min(w["box"][1] for w in ws), max(w["box"][2] for w in ws), max(w["box"][3] for w in ws)]


def main() -> None:
    set_dir, run_dir = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    pages, fields = [], []
    cells = {"n": 0, "ok": 0}
    for tj in sorted((set_dir / "truth").glob("*.json")):
        t = json.loads(tj.read_text(encoding="utf-8"))
        stem = tj.stem
        txt, tsv = run_dir / "ocr" / f"{stem}.txt", run_dir / "ocr" / f"{stem}.tsv"
        ocr = txt.read_text(encoding="utf-8") if txt.exists() else ""
        truth_text = norm("".join(line["text"] for line in t["lines"]))
        cer = lev(norm(ocr), truth_text) / max(1, len(truth_text))
        ws = words(tsv) if tsv.exists() else []
        clean = t["degradation"] == "clean"
        pages.append({"page": stem, "clean": clean, "cer": cer, "failed": (not norm(ocr)) or cer > 0.5})
        for f in t["fields"]:
            got = contained(ws, f["bbox"])
            text = norm("".join(w["text"] for w in got))
            correct = text == norm(f["text"])
            fields.append({"page": stem, "name": f["name"], "clean": clean, "correct": correct, "missing": not got,
                           "flagged": any(w["conf"] < LOW for w in got),
                           "loc_ok": bool(got) and iou(merge(got), f["bbox"]) >= 0.5,
                           "digit_err": lev(re.sub(r"\D", "", text), re.sub(r"\D", "", f["text"])),
                           "digits": len(re.sub(r"\D", "", f["text"]))})
        if clean and t.get("table"):
            for c in t["table"]["cells"]:
                cells["n"] += 1
                cells["ok"] += norm("".join(w["text"] for w in contained(ws, c["bbox"]))) == norm(c["text"])
    avg = lambda xs: sum(xs) / len(xs) if xs else 0.0
    m = {
        "pages": len(pages),
        "cer_clean": avg([p["cer"] for p in pages if p["clean"]]),
        "cer_degraded": avg([p["cer"] for p in pages if not p["clean"]]),
        "failed_pages": sum(p["failed"] for p in pages),
        "field_clean": avg([f["correct"] for f in fields if f["clean"]]),
        "field_all": avg([f["correct"] for f in fields]),
        "digit_error_rate": sum(f["digit_err"] for f in fields) / max(1, sum(f["digits"] for f in fields)),
        "cell_clean": cells["ok"] / cells["n"] if cells["n"] else 0.0,
        "loc_all": avg([f["loc_ok"] for f in fields]),
    }
    wrong = [f for f in fields if not f["correct"]]
    right = [f for f in fields if f["correct"]]
    m["coverage"] = avg([f["flagged"] and not f["missing"] for f in wrong]) if wrong else 1.0
    m["false_flag"] = avg([f["flagged"] for f in right]) if right else 0.0
    m["per_degradation_cer"] = {}
    for p in pages:
        k = p["page"].split("__")[1]
        m["per_degradation_cer"].setdefault(k, []).append(p["cer"])
    m["per_degradation_cer"] = {k: round(avg(v), 4) for k, v in m["per_degradation_cer"].items()}
    m["per_field_type_clean"] = {}
    for f in fields:
        if f["clean"]:
            m["per_field_type_clean"].setdefault(f["name"], []).append(f["correct"])
    m["per_field_type_clean"] = {k: round(avg(v), 4) for k, v in m["per_field_type_clean"].items()}
    inputs_ok = (run_dir / "inputs" / "_rc.txt").exists()
    passed = (m["cer_clean"] <= PASS["cer_clean"] and m["cer_degraded"] <= PASS["cer_degraded"]
              and m["field_clean"] >= PASS["field_clean"] and m["cell_clean"] >= PASS["cell_clean"]
              and m["loc_all"] >= PASS["loc_all"] and m["failed_pages"] == 0 and inputs_ok)
    limited = (m["cer_clean"] <= LIMITED["cer_clean"] and m["coverage"] >= LIMITED["coverage"]
               and m["false_flag"] <= LIMITED["false_flag"] and inputs_ok)
    m["verdict"] = "PASS" if passed else ("LIMITED" if limited else "FAIL")
    m["note"] = "input-handling expectations must be checked by hand against inputs/_rc.txt before the verdict stands"
    (run_dir / "score.json").write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
    (run_dir / "fields.json").write_text(json.dumps(fields, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(m, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
