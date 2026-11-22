"""Generate FICTIONAL Chinese document images for the Route A Tesseract benchmark.

Design: docs/phase2/route-a/TASK_PHASE2_ROUTE_A_TESSERACT_CHI_SIM_BENCHMARK_DESIGN.md (confirmed).
All names, numbers and case identifiers are randomly generated and fictional. No real material is read.

Usage: python3 gen_samples.py <out_dir> [--seed N]
Writes <out_dir>/samples/*.png, <out_dir>/truth/*.json, <out_dir>/inputs/* (input-handling checks)
and <out_dir>/manifest.json (SHA-256 of every file).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import random

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

DPI = 300
W, H = 2480, 3508  # A4 at 300 dpi
SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
SANS = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
SURNAMES = "赵钱孙李周吴郑冯陈褚卫蒋沈韩杨朱秦尤许何吕施"
GIVEN = "子文思远嘉宁明华若安晨曦雨辰泽宇浩然欣怡"
GOODS = ["头层牛皮", "超纤贴皮", "植绒布", "鞋垫材料", "橡胶底", "织带", "辅料包"]
CN_DIGITS = "零壹贰叁肆伍陆柒捌玖"
COURT_TYPES = ["民初", "民终", "执"]
PROVINCES = ["浙", "苏", "沪", "皖", "闽"]


def font(size: int, sans: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(SANS if sans else SERIF, size, index=2)  # index 2 = SC face in Noto CJK collections


class Page:
    def __init__(self, sans: bool = False):
        self.img = Image.new("RGB", (W, H), "white")
        self.d = ImageDraw.Draw(self.img)
        self.sans = sans
        self.lines: list[dict] = []
        self.fields: list[dict] = []
        self.table: dict | None = None

    def text(self, x: int, y: int, s: str, size: int = 44, field: str | None = None, line: bool = True) -> tuple:
        f = font(size, self.sans)
        self.d.text((x, y), s, font=f, fill="black")
        bb = self.d.textbbox((x, y), s, font=f)
        if line:
            self.lines.append({"text": s, "bbox": list(bb)})
        return bb

    def field_in(self, x: int, y: int, prefix: str, value: str, name: str, size: int = 44) -> int:
        """Draw `prefix` + `value` on one line; record the value's own box as a field."""
        f = font(size, self.sans)
        full = prefix + value
        self.d.text((x, y), full, font=f, fill="black")
        self.lines.append({"text": full, "bbox": list(self.d.textbbox((x, y), full, font=f))})
        vx = x + int(self.d.textlength(prefix, font=f))
        self.fields.append({"name": name, "text": value, "bbox": list(self.d.textbbox((vx, y), value, font=f))})
        return y + int(size * 1.9)


def fake_name(r: random.Random) -> str:
    return r.choice(SURNAMES) + "".join(r.choice(GIVEN) for _ in range(r.choice((1, 2))))


def fake_id(r: random.Random) -> str:  # format-shaped, not a real identifier
    return "".join(str(r.randint(0, 9)) for _ in range(17)) + r.choice("0123456789X")


def fake_case_no(r: random.Random) -> str:
    return f"（{r.randint(2019, 2026)}）{r.choice(PROVINCES)}{r.randint(1000, 9999):04d}{r.choice(COURT_TYPES)}{r.randint(1, 9999)}号"


def amount(r: random.Random) -> str:
    return f"{r.randint(1000, 999999):,}.{r.randint(0, 99):02d}"


def date(r: random.Random) -> str:
    return f"{r.randint(2020, 2026)}年{r.randint(1, 12)}月{r.randint(1, 28)}日"


def cn_upper(n: int) -> str:
    units = ["", "拾", "佰", "仟", "万", "拾", "佰", "仟"]
    s, digits = "", str(n)
    for i, ch in enumerate(digits):
        pos = len(digits) - i - 1
        if ch != "0":
            s += CN_DIGITS[int(ch)] + units[pos]
        elif not s.endswith("零") and pos not in (0, 4):
            s += "零"
    return s.rstrip("零").replace("零万", "万") + "元整"


ARTICLES = ["第五百七十七条", "第五百零九条", "第六百二十六条", "第一千零六十四条", "第一百八十八条", "第五百八十四条"]


def page_judgment(r: random.Random) -> Page:
    p = Page()
    y = p.text(900, 200, "民 事 判 决 书", 72)[3] + 60
    y = p.field_in(1500, y, "", fake_case_no(r), "case_no")
    para = ["本院认为，原告与被告之间的买卖合同系双方真实意思表示，合法有效。",
            "被告未按约定支付货款，应承担继续履行及赔偿损失的违约责任。"]
    for t in para:
        y = p.text(200, y, t)[3] + 40
    y = p.field_in(200, y, "依照《中华人民共和国民法典》", r.choice(ARTICLES), "article")
    y = p.field_in(200, y, "判决被告于本判决生效之日起十日内支付货款人民币", amount(r) + "元", "amount")
    y = p.field_in(200, y, "并自", date(r), "date")
    p.text(200, y, "起按一年期贷款市场报价利率计付逾期付款损失。")
    return p


def page_statement(r: random.Random) -> Page:
    p = Page(sans=True)
    y = p.text(800, 200, "客户对账明细表", 64)[3] + 60
    y = p.field_in(200, y, "对账期间截至：", date(r), "date")
    cols = [200, 700, 1250, 1550, 1900, 2350]
    head = ["日期", "品名", "数量", "单价", "金额"]
    rows, cells = [head], []
    for _ in range(r.randint(5, 8)):
        q, u = r.randint(10, 500), r.randint(5, 90)
        rows.append([f"{r.randint(1, 12)}/{r.randint(1, 28)}", r.choice(GOODS), str(q), f"{u}.00", f"{q * u:,}.00"])
    y0 = y
    for ri, row in enumerate(rows):
        for ci, cell in enumerate(row):
            x0, x1 = cols[ci], cols[ci + 1]
            p.d.rectangle((x0, y, x1, y + 90), outline="black", width=2)
            bb = p.text(x0 + 15, y + 18, cell, 40)
            cells.append({"row": ri, "col": ci, "text": cell, "bbox": [x0, y, x1, y + 90]})
            if ri > 0 and ci == 4:
                p.fields.append({"name": "amount", "text": cell, "bbox": list(bb)})
        y += 90
    total = sum(int(c["text"].replace(",", "").split(".")[0]) for c in cells if c["row"] > 0 and c["col"] == 4)
    p.table = {"bbox": [cols[0], y0, cols[-1], y], "cells": cells, "merged": []}
    p.field_in(200, y + 60, "合计：", f"{total:,}.00", "amount")
    return p


def page_complaint(r: random.Random) -> Page:
    p = Page()
    y = p.text(950, 200, "民 事 起 诉 状", 72)[3] + 80
    for role in ("原告", "被告"):
        y = p.field_in(200, y, f"{role}：", fake_name(r), "name")
        y = p.field_in(260, y, "公民身份号码：", fake_id(r), "id_no")
        y = p.field_in(260, y, "联系电话：", "1" + "".join(str(r.randint(0, 9)) for _ in range(10)), "phone")
    y = p.text(200, y, "诉讼请求：")[3] + 30
    p.field_in(200, y, "1. 判令被告支付货款人民币", amount(r) + "元；", "amount")
    return p


def page_receipt(r: random.Random) -> Page:
    p = Page()
    n = r.randint(10000, 900000)
    y = p.text(1050, 300, "借  条", 80)[3] + 100
    y = p.field_in(200, y, "今借到", fake_name(r), "name")
    y = p.field_in(200, y, "人民币（大写）", cn_upper(n), "amount_upper")
    y = p.field_in(200, y, "（小写）￥", f"{n:,}.00", "amount")
    y = p.field_in(200, y, "约定于", date(r), "date")
    p.field_in(1400, y + 200, "借款人：", fake_name(r), "name")
    return p


def stamp(img: Image.Image, cx: int, cy: int, label: str) -> None:
    over = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    d.ellipse((cx - 260, cy - 260, cx + 260, cy + 260), outline=(220, 30, 30, 170), width=14)
    f = font(56, True)
    d.text((cx - d.textlength(label, font=f) / 2, cy - 30), label, font=f, fill=(220, 30, 30, 170))
    d.text((cx - 40, cy - 160), "★", font=font(80, True), fill=(220, 30, 30, 170))
    img.paste(Image.alpha_composite(img.convert("RGBA"), over).convert("RGB"))


def page_stamped(r: random.Random) -> Page:
    p = page_judgment(r)
    f = p.fields[-1]["bbox"]
    stamp(p.img, f[0] + 200, f[1] + 20, "虚构测试专用章")
    return p


def page_layout(r: random.Random, kind: int) -> Page:
    p = Page(sans=bool(kind % 2))
    if kind == 0:  # two columns
        for col, x in enumerate((200, 1300)):
            y = 300
            for i in range(10):
                y = p.text(x, y, f"第{col * 10 + i + 1}条 ABC合同 编号No.{r.randint(100, 999)} 金额{r.randint(1, 99)}万", 38)[3] + 40
        p.field_in(200, y + 60, "签订日期：", date(r), "date")
    elif kind == 1:  # header / footer
        p.text(200, 100, f"虚构律师事务所 · 内部测试文件 · 第 {r.randint(1, 9)} 页", 32)
        y = 400
        for _ in range(6):
            y = p.text(200, y, "全角数字１２３与半角数字123混排，英文Contract与中文合同混排。", 42)[3] + 50
        p.field_in(200, y, "金额：", amount(r) + "元", "amount")
        p.text(900, H - 180, f"— {r.randint(1, 30)} —", 32)
    else:  # table with merged cells
        y0, rows = 400, 5
        cells = []
        p.d.rectangle((200, y0, 2280, y0 + 100), outline="black", width=2)
        p.text(900, y0 + 25, "费用明细（合并表头）", 44, line=False)
        cells.append({"row": 0, "col": 0, "text": "费用明细（合并表头）", "bbox": [200, y0, 2280, y0 + 100]})
        merged = [{"row": 0, "col": 0, "rowspan": 1, "colspan": 3}]
        p.lines.append({"text": "费用明细（合并表头）", "bbox": [900, y0 + 25, 1400, y0 + 75]})
        y = y0 + 100
        for ri in range(1, rows):
            vals = [fake_name(r), r.choice(GOODS), amount(r)]
            for ci, (x0, x1) in enumerate(((200, 900), (900, 1600), (1600, 2280))):
                p.d.rectangle((x0, y, x1, y + 100), outline="black", width=2)
                bb = p.text(x0 + 20, y + 25, vals[ci], 42)
                cells.append({"row": ri, "col": ci, "text": vals[ci], "bbox": [x0, y, x1, y + 100]})
                if ci == 2:
                    p.fields.append({"name": "amount", "text": vals[ci], "bbox": list(bb)})
            y += 100
        p.table = {"bbox": [200, y0, 2280, y], "cells": cells, "merged": merged}
    return p


# ---------------------------------------------------------------- degradations

def _apply_matrix(boxes: list, M: np.ndarray) -> list:
    out = []
    for b in boxes:
        pts = np.array([[b[0], b[1]], [b[2], b[1]], [b[0], b[3]], [b[2], b[3]]], dtype=np.float32).reshape(-1, 1, 2)
        t = cv2.perspectiveTransform(pts, M).reshape(-1, 2)
        out.append([int(t[:, 0].min()), int(t[:, 1].min()), int(t[:, 0].max()), int(t[:, 1].max())])
    return out


def degrade(img: Image.Image, truth: dict, kind: str, r: random.Random) -> tuple[Image.Image, dict]:
    t = json.loads(json.dumps(truth))
    groups = [t["lines"], t["fields"]] + ([t["table"]["cells"]] if t.get("table") else [])

    def remap(M: np.ndarray) -> None:
        for g in groups:
            for item, nb in zip(g, _apply_matrix([i["bbox"] for i in g], M)):
                item["bbox"] = nb
        if t.get("table"):
            t["table"]["bbox"] = _apply_matrix([t["table"]["bbox"]], M)[0]

    a = np.array(img)
    if kind == "lowres":
        s = 150 / DPI
        M = np.array([[s, 0, 0], [0, s, 0], [0, 0, 1]], dtype=np.float64)
        out = img.resize((int(W * s), int(H * s)), Image.BILINEAR)
        remap(M)
    elif kind == "rotate":
        ang = r.choice((-3, 3))
        M2 = cv2.getRotationMatrix2D((W / 2, H / 2), ang, 1.0)
        out = Image.fromarray(cv2.warpAffine(a, M2, (W, H), borderValue=(255, 255, 255)))
        remap(np.vstack([M2, [0, 0, 1]]))
    elif kind == "blur":
        out = img.filter(ImageFilter.GaussianBlur(1.6))
    elif kind == "jpeg":
        import io
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=30)
        out = Image.open(io.BytesIO(buf.getvalue())).convert("RGB")
    elif kind == "photo":
        src = np.float32([[0, 0], [W, 0], [0, H], [W, H]])
        j = lambda: r.uniform(0.01, 0.04)
        dst = np.float32([[W * j(), H * j()], [W * (1 - j()), H * j()], [W * j(), H * (1 - j())], [W * (1 - j()), H * (1 - j())]])
        M = cv2.getPerspectiveTransform(src, dst)
        warped = cv2.warpPerspective(a, M, (W, H), borderValue=(200, 200, 200)).astype(np.float32)
        grad = np.linspace(0.75, 1.05, W, dtype=np.float32)[None, :, None]
        out = Image.fromarray(np.clip(warped * grad, 0, 255).astype(np.uint8))
        remap(M)
    else:
        raise ValueError(kind)
    t["degradation"] = kind
    return out, t


# ---------------------------------------------------------------- input-handling checks

def make_inputs(out: pathlib.Path, sample_png: pathlib.Path) -> list[dict]:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    from reportlab.pdfgen import canvas
    from pypdf import PdfReader, PdfWriter

    out.mkdir(parents=True, exist_ok=True)
    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
    hybrid = out / "hybrid.pdf"
    c = canvas.Canvas(str(hybrid), pagesize=A4)
    c.setFont("STSong-Light", 14)
    c.drawString(72, 760, "第一页为文字层：虚构测试文本，金额12,345.00元。")
    c.showPage()
    c.drawImage(str(sample_png), 0, 0, width=A4[0], height=A4[1])
    c.showPage()
    c.save()
    trunc = out / "truncated.pdf"
    data = hybrid.read_bytes()
    trunc.write_bytes(data[: len(data) // 3])
    enc = out / "encrypted.pdf"
    w = PdfWriter()
    for pg in PdfReader(str(hybrid)).pages:
        w.add_page(pg)
    w.encrypt("test-only-password")
    with enc.open("wb") as fh:
        w.write(fh)
    unsup = out / "unsupported.xyz"
    unsup.write_bytes(b"\x00\x01not a document\x02")
    return [{"file": "hybrid.pdf", "expect": "page1 native text, page2 OCR"},
            {"file": "truncated.pdf", "expect": "explicit error"},
            {"file": "encrypted.pdf", "expect": "explicit error"},
            {"file": "unsupported.xyz", "expect": "explicit error"}]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--seed", type=int, default=20261122)
    a = ap.parse_args()
    r = random.Random(a.seed)
    out = pathlib.Path(a.out)
    (out / "samples").mkdir(parents=True, exist_ok=True)
    (out / "truth").mkdir(parents=True, exist_ok=True)
    makers = [("judgment", page_judgment), ("statement", page_statement), ("complaint", page_complaint),
              ("receipt", page_receipt), ("stamped", page_stamped)]
    pages = []
    for name, fn in makers:
        for i in range(3):
            pages.append((f"{name}_{i + 1}", fn(r)))
    for i in range(3):
        pages.append((f"layout_{i + 1}", page_layout(r, i)))
    for pid, p in pages:
        truth = {"page": pid, "lines": p.lines, "fields": p.fields, "table": p.table, "degradation": "clean"}
        p.img.save(out / "samples" / f"{pid}__clean.png", dpi=(DPI, DPI))
        (out / "truth" / f"{pid}__clean.json").write_text(json.dumps(truth, ensure_ascii=False), encoding="utf-8")
        for kind in ("lowres", "rotate", "blur", "jpeg", "photo"):
            img, t = degrade(p.img, truth, kind, r)
            dpi = 150 if kind == "lowres" else DPI
            img.save(out / "samples" / f"{pid}__{kind}.png", dpi=(dpi, dpi))
            (out / "truth" / f"{pid}__{kind}.json").write_text(json.dumps(t, ensure_ascii=False), encoding="utf-8")
    checks = make_inputs(out / "inputs", out / "samples" / "statement_1__clean.png")
    (out / "inputs" / "expect.json").write_text(json.dumps(checks, ensure_ascii=False, indent=1), encoding="utf-8")
    manifest = {str(f.relative_to(out)): hashlib.sha256(f.read_bytes()).hexdigest().upper()
                for f in sorted(out.rglob("*")) if f.is_file() and f.name != "manifest.json"}
    (out / "manifest.json").write_text(json.dumps({"seed": a.seed, "files": manifest}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"pages={len(pages)} images={len(pages) * 6} files={len(manifest)}")


if __name__ == "__main__":
    main()
