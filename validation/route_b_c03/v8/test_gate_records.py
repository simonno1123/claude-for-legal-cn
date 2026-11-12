"""Tests for C03 V8-A (design C03-GATE-ENFORCEMENT-V8 R2). All data is fictional.

Run: python3 -m unittest discover -s validation/route_b_c03/v8 -t validation/route_b_c03/v8
"""

from __future__ import annotations

import copy
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))

from phase2_runtime.route_b_c03 import gate_records as g  # noqa: E402
from phase2_runtime.route_b_c03 import gate_record_builder as b  # noqa: E402

SHA_A, SHA_B, SHA_C, SHA_D = "A" * 64, "B" * 64, "C" * 64, "D" * 64
CASE = "CASE-Z"
NOW = "2026-12-05T09:00:00+08:00"
EVID = [{"code": "S-1", "sha256": SHA_B, "locator": "p2"}]
EMPTY_Q = {"answers": {}, "last_event": None}
DEADLINES = [{"item": "下一期付款", "status": "适用", "expiry": "2026-12-20T00:00:00+08:00"}]
CUTOFF = "2026-12-20T00:00:00+08:00"


def mk(kind, at, refs=None, **fields):
    return b.build(kind, refs=refs or {}, formed_at=at, method="chat_c", **fields)


def sha(rec):
    return g.record_sha256(rec)


def opinions(**over):
    ops = {c: {"visible": "通过", "blind": None} for c in g.CHECKLIST}
    ops.update(over)
    return ops


def l1_bundle():
    M = mk("M", "2026-12-01T09:00:00+08:00",
           candidate={"id": "CAND-Z", "version": "v1", "output_sha256": SHA_A, "generated_at": "2026-12-01T08:00:00+08:00",
                      "class": "C03_CONFLICT_AND_INFORMATION_GAP_REGISTER_CANDIDATE", "capability": "C03",
                      "operation": "fictional", "generator": "gen-model", "generator_model_family": "FAMILY-G"},
           case={"code": CASE, "version": "v1"},
           trace_refs={"S-1": {"path": "fictional/a.pdf", "sha256": SHA_B}},
           contract_refs=[], omission_conflict_adverse_refs=[], failure_audit_refs=[],
           authority={"pack_sha256": SHA_C, "check_date": "2026-12-01", "entries": []},
           known_limitations="虚构", prohibited_uses="不得对外",
           design_version={"design_id": g.DESIGN_ID, "text_sha256": g.ADOPTED_R3_SHA256, "checklist": g.CHECKLIST_ID},
           planned_scope="C1-C11", reviewer={"code": "REVIEWER-01", "qualification_ref": "QUAL-REF-01"})
    I = mk("I", "2026-12-01T10:00:00+08:00", reviewer_name="虚构律师",
           items={"1": "确认", "2": "确认", "3": "确认", "4": "提供并确认", "5": "确认", "6": "确认"})
    T = mk("T", "2026-12-01T10:10:00+08:00", use_code="U1", output_class=M["candidate"]["class"], audience=g.AUDIENCE,
           next_step="内部存档整理", l1_positive_confirmation=True, h_query=None, corrections=[])
    R = mk("R", "2026-12-01T11:00:00+08:00", h_query=copy.deepcopy(EMPTY_Q), actual_scope="C1-C11",
           checklist={c: "通过" for c in g.CHECKLIST}, c11_original_verified=True, deadlines=copy.deepcopy(DEADLINES),
           no_deadline_declaration=False, validity_cutoff=CUTOFF, material_conflict="无", withdrawn=False,
           disposition=g.APPROVE, reason="虚构")
    return rebind({"M": M, "I": I, "T": T, "R": R, "X": [], "V": [], "W": [], "CORR": [], "G": [], "H": []})


def l2_bundle():
    bd = l1_bundle()
    bd["T"].update(use_code="U2", next_step="自行起草参考", l1_positive_confirmation=False, h_query=copy.deepcopy(EMPTY_Q))
    bd["E"] = mk("E", "2026-12-01T10:20:00+08:00", d_sha256=SHA_A, task_sha256=SHA_B, scope="全新会话，仅 D 与任务说明",
                 allowed_fields=["结构"], receiver="CROSS/model-x", conditions={k: "接受" for k in ("retention", "training", "reshare", "region")},
                 config_sha256=SHA_C, window={"start": "2026-12-01T10:00:00+08:00", "end": "2026-12-02T10:00:00+08:00"}, withdrawn=False)
    bd["S"] = mk("S", "2026-12-01T10:31:00+08:00", sent_sha256=SHA_A, scope="全新会话，仅 D 与任务说明", receiver="CROSS/model-x",
                 config_sha256=SHA_C, checks={str(i): "通过" for i in range(1, 7)}, h_check=copy.deepcopy(EMPTY_Q),
                 request_id="req-1", sent_at="2026-12-01T10:30:00+08:00")
    bd["X"] = [mk("X", "2026-12-01T10:40:00+08:00", opinions=opinions(), provider="CROSS", model="model-x",
                  model_family="FAMILY-X", received_at="2026-12-01T10:40:00+08:00", request_id="req-1")]
    bd["P"] = mk("P", "2026-12-02T12:00:00+08:00", reconfirm={str(i): "已重查" for i in range(1, 5)},
                 authority_recheck_at="2026-12-02T11:30:00+08:00", h_increment=copy.deepcopy(EMPTY_Q))
    return rebind(bd)


def rebind(bd):
    """Recompute references top-down after a mutation so only the intended defect remains."""
    M, I, T, R = bd["M"], bd["I"], bd["T"], bd["R"]
    I["refs"] = {"M": sha(M)}
    T["refs"] = {"M": sha(M), "I": sha(I)}
    if bd.get("E"):
        bd["E"]["refs"] = {"M": sha(M), "T": sha(T)}
        bd["S"]["refs"] = {"E": sha(bd["E"])}
        for x in bd["X"]:
            x["refs"] = {"S": sha(bd["S"])}
        for v in bd["V"]:
            v["refs"] = {"M": sha(M), "T": sha(T), "X": sha(bd["X"][0])}
    for w in bd["W"]:
        w["refs"] = {**w["refs"], "M": sha(M), "T": sha(T)}
    R["refs"] = {"M": sha(M), "I": sha(I), "T": sha(T)}
    if bd.get("E") and bd["X"]:
        R["refs"]["X"] = sha(bd["X"][0])
    for prefix in ("V", "W"):
        for i, h in enumerate(sorted(sha(x) for x in bd[prefix]), 1):
            R["refs"][f"{prefix}{i}"] = h
    for i, h in enumerate(sorted({a["clearance"] for a in R["h_query"]["answers"].values() if a["clearance"]}), 1):
        R["refs"][f"CL{i}"] = h
    if bd.get("P"):
        bd["P"]["refs"] = {"R": sha(R)}
    for corr in bd["CORR"]:
        corr["refs"] = {"R": sha(R)}
    return bd


def run(bd, stage="review", now=NOW):
    return g.validate(copy.deepcopy(bd), now=now, stage=stage)


def reasons(bd, **kw):
    return run(bd, **kw)["reasons"]


def disc(at, item="C5", typ="人工停点", cand="CAND-OTHER"):
    return {"event": "discovery", "type": typ, "case": CASE, "item": item, "issue": "虚构争点", "candidate": cand,
            "M": SHA_C, "X": "不适用", "stage": "R 时", "at": at}


def clear(ev, typ, at, scope=None, evidence=None):
    return {"event": "clearance", "type": typ, "refs_discovery": sha(ev), "scope_candidate": scope,
            "evidence": evidence if evidence is not None else copy.deepcopy(EVID), "at": at}


def answer(ev, relevant="相关", cl=None):
    if relevant == "不相关":
        return {sha(ev): {"relevant": "不相关", "reason": "不同争点", "covered": "不适用", "clearance": None}}
    if cl is None:
        return {sha(ev): {"relevant": "相关", "reason": "同一期限", "covered": "未覆盖", "clearance": None}}
    return {sha(ev): {"relevant": "相关", "reason": "同一期限", "covered": "已覆盖", "clearance": sha(cl)}}


class JCSTests(unittest.TestCase):
    def test_rfc8785_key_order_utf16(self):
        obj = {"€": 1, "\r": 2, "דּ": 3, "1": 4, "\U0001F600": 5, "\u0080": 6, "ö": 7}
        keys = list(json.loads(g.canonical_bytes(obj).decode()))
        self.assertEqual(keys, ["\r", "1", "\u0080", "ö", "€", "\U0001F600", "דּ"])

    def test_utf16_vs_codepoint_difference(self):
        out = g.canonical_bytes({"": 1, "\U00010000": 2}).decode()
        self.assertLess(out.index("\U00010000"), out.index(""))

    def test_rejects_float_big_int_dupes_lone_surrogate(self):
        for bad in ({"a": 1.5}, {"a": 10**21}, {"a": "\ud800"}):
            with self.assertRaises(g.RecordError):
                g.canonical_bytes(bad)
        with self.assertRaises(g.RecordError):
            g.parse_record('{"a":1,"a":2}')

    def test_canonical_escapes(self):
        self.assertEqual(g.canonical_bytes({"b": "\n\u001f\"/", "a": [True, None, 0]}).decode(),
                         '{"a":[true,null,0],"b":"\\n\\u001f\\"/"}')


class PositivePaths(unittest.TestCase):
    def test_l1_positive(self):
        self.assertEqual(run(l1_bundle()), {"result": "ELIGIBLE_TO_REQUEST_AR_B_010", "reasons": []})

    def test_l2_positive(self):
        self.assertEqual(run(l2_bundle()), {"result": "ELIGIBLE_TO_REQUEST_AR_B_010", "reasons": []})


class Contracts(unittest.TestCase):
    """Codex PR #113 finding 1: content and types of M fields, not only key presence."""

    def test_M_field_contents(self):
        cases = [
            lambda m: m.update(reviewer={}),
            lambda m: m["candidate"].update(capability=""),
            lambda m: m["candidate"].update(output_sha256="invalid"),
            lambda m: m.update(prohibited_uses=""),
            lambda m: m["authority"].update(check_date="2026-13-01"),
            lambda m: m.update(trace_refs={"S-1": {"path": "x", "sha256": "bad"}}),
        ]
        for mutate in cases:
            bd = l1_bundle(); mutate(bd["M"]); rebind(bd)
            self.assertIn("RECORD_INVALID", reasons(bd))

    def test_M_missing_each_inherited_field(self):
        for field in g.SPECS["M"]:
            bd = l1_bundle(); del bd["M"][field]; rebind(bd)
            self.assertIn("RECORD_INVALID", reasons(bd), field)


class AnnexA(unittest.TestCase):
    def blocked(self, bd, code, **kw):
        out = run(bd, **kw)
        self.assertEqual(out["result"], "BLOCKED")
        self.assertIn(code, out["reasons"])

    def test_A01_A02_A29_prohibited_purpose(self):
        bd = l1_bundle(); bd["T"]["next_step"] = "作为给法院的情况说明附件"; rebind(bd)
        self.blocked(bd, "PURPOSE_PROHIBITED")
        bd = l1_bundle(); bd["T"]["audience"] = "委托人"; rebind(bd)
        self.blocked(bd, "PURPOSE_PROHIBITED")

    def test_A03_tier_and_unknown_use(self):
        bd = l1_bundle(); bd["T"]["l1_positive_confirmation"] = None; rebind(bd)
        self.blocked(bd, "TIER_INVALID")
        bd = l1_bundle(); bd["T"]["use_code"] = "U9"; rebind(bd)
        self.blocked(bd, "PURPOSE_NOT_ESTABLISHED")

    def test_A04_A05_A33_stops_need_typed_V(self):
        bd = l2_bundle(); bd["X"][0]["opinions"]["C7"] = {"visible": "无法判断-可见范围内", "blind": None}; rebind(bd)
        self.blocked(bd, "STOP_UNRESOLVED")

    def test_A55_same_round_refutation_clears(self):
        bd = l2_bundle(); bd["X"][0]["opinions"]["C5"] = {"visible": "不通过", "blind": None}
        bd["V"] = [mk("V", "2026-12-01T10:50:00+08:00", item="C5", issue="x",
                      clearance_type="MODEL_FINDING_REFUTED_BY_ORIGINAL", evidence=copy.deepcopy(EVID))]
        rebind(bd)
        # Codex PR #113 round 2: a model stop must also be in H with a refutation (R3 §6.5 item 2)
        self.assertIn("STOP_INDEX_NOT_CLEARED", reasons(bd))
        ev = {"event": "discovery", "type": "模型停点", "case": CASE, "item": "C5", "issue": "x", "candidate": "CAND-Z",
              "M": sha(bd["M"]), "X": sha(bd["X"][0]), "stage": "X 返回", "at": "2026-12-01T10:41:00+08:00"}
        cl = clear(ev, "FINDING_REFUTED", "2026-12-01T10:51:00+08:00")
        bd["H"] = [ev, cl]; bd["R"]["h_query"]["answers"] = answer(ev, cl=cl); rebind(bd)
        self.assertEqual(run(bd)["result"], "ELIGIBLE_TO_REQUEST_AR_B_010")

    def test_R_binds_its_basis(self):
        bd = l2_bundle(); r_before = copy.deepcopy(bd["R"])
        bd["X"][0]["model"] = "model-z"; bd["X"][0]["refs"] = {"S": sha(bd["S"])}
        bd["R"] = r_before  # R not re-formed after its basis changed
        self.assertIn("BINDING_MISMATCH", reasons(bd))

    def test_future_records_rejected(self):
        self.assertIn("EVENT_ORDER_INVALID", reasons(l2_bundle(), now="2026-12-01T12:00:00+08:00"))

    def test_blind_scope_rules(self):
        # Codex PR #113 finding 7: blind only for the listed sub-judgment; visible part still judged
        bd = l2_bundle(); bd["X"][0]["opinions"]["C5"] = {"visible": "通过", "blind": {"sub": "任意文字", "value": "无法判断-脱敏盲区"}}; rebind(bd)
        self.blocked(bd, "CROSS_CHECK_INCOMPLETE")
        bd = l2_bundle(); bd["X"][0]["opinions"]["C6"] = {"visible": "通过", "blind": {"sub": "x", "value": "无法判断-脱敏盲区"}}; rebind(bd)
        self.blocked(bd, "CROSS_CHECK_INCOMPLETE")
        bd = l2_bundle(); bd["X"][0]["opinions"]["C5"] = {"visible": "通过", "blind": {"sub": g.BLIND_SUBS["C5"], "value": "无法判断-脱敏盲区"}}
        rebind(bd)
        self.blocked(bd, "STOP_UNRESOLVED")  # A-47: needs a blind-scope V
        bd["V"] = [mk("V", "2026-12-01T10:50:00+08:00", item="C5", issue="真实日期",
                      clearance_type="ORIGINAL_VERIFICATION_OF_BLIND_SCOPE", evidence=copy.deepcopy(EVID))]
        rebind(bd)
        self.assertEqual(run(bd)["result"], "ELIGIBLE_TO_REQUEST_AR_B_010")
        bd = l2_bundle(); bd["X"][0]["opinions"]["C5"] = {"visible": "无法判断-脱敏盲区", "blind": None}; rebind(bd)
        self.blocked(bd, "CROSS_CHECK_INCOMPLETE")

    def test_A06_A09_checklist(self):
        bd = l1_bundle(); bd["R"]["checklist"]["C9"] = "不通过"; rebind(bd)
        self.blocked(bd, "CHECKLIST_NOT_ALL_PASS")
        bd = l1_bundle(); bd["R"]["c11_original_verified"] = False; rebind(bd)
        self.blocked(bd, "CHECKLIST_NOT_ALL_PASS")

    def test_trial_correction_record(self):
        bd = l1_bundle()
        for c in ("C2", "C3", "C4"):
            bd["R"]["checklist"][c] = "不通过"
        rebind(bd)
        self.blocked(bd, "CHECKLIST_NOT_ALL_PASS")
        bd["CORR"] = [mk("CORR", "2026-12-01T12:00:00+08:00", items={"C2": "通过", "C3": "通过", "C4": "通过"}, statement="漏点")]
        rebind(bd)
        self.assertEqual(run(bd)["result"], "ELIGIBLE_TO_REQUEST_AR_B_010")

    def test_A08_conditions(self):
        bd = l2_bundle(); bd["E"]["conditions"]["training"] = "未确认"; rebind(bd)
        self.blocked(bd, "EGRESS_CHAIN_INVALID")

    def test_A11_A16_binding(self):
        bd = l2_bundle(); bd["P"]["refs"] = {"R": SHA_A}
        self.blocked(bd, "BINDING_MISMATCH")
        bd = l1_bundle(); bd["R"]["refs"]["M"] = SHA_A
        self.blocked(bd, "BINDING_MISMATCH")

    def test_A12_A13_cooling_and_cutoff(self):
        bd = l2_bundle(); bd["P"]["formed_at"] = "2026-12-01T20:00:00+08:00"; bd["P"]["authority_recheck_at"] = "2026-12-01T19:00:00+08:00"
        self.blocked(bd, "COOLING_PERIOD_UNMET")
        bd = l2_bundle(); bd["P"]["formed_at"] = CUTOFF
        self.blocked(bd, "VALIDITY_EXPIRED")

    def test_A17_x_other_send(self):
        bd = l2_bundle(); bd["X"][0]["refs"] = {"S": SHA_C}
        self.blocked(bd, "CHAIN_BROKEN")

    def test_A21_design_version(self):
        bd = l1_bundle(); bd["M"]["design_version"]["text_sha256"] = SHA_A; rebind(bd)
        self.blocked(bd, "DESIGN_VERSION_MISMATCH")

    def test_A22_A23_expired(self):
        self.blocked(l1_bundle(), "VALIDITY_EXPIRED", now="2026-12-21T00:00:00+08:00")

    def test_A24_reconfirmation(self):
        bd = l2_bundle(); bd["P"]["reconfirm"]["2"] = "未发现变化"
        self.blocked(bd, "RECONFIRMATION_MISSING")

    def test_A25_trial_shape(self):
        bd = l1_bundle(); bd["R"]["deadlines"].append({"item": "查封期限", "status": "未知", "expiry": None})
        bd["R"]["disposition"] = "KEEP BLOCKED"; rebind(bd)
        out = reasons(bd)
        self.assertIn("DEADLINE_STATUS_UNKNOWN", out)
        self.assertIn("DISPOSITION_NOT_APPROVE", out)

    def test_A26_bad_time(self):
        bd = l1_bundle(); bd["R"]["formed_at"] = "2026-02-30T10:00:00"
        self.blocked(bd, "RECORD_INVALID")

    def test_A27_A28_bytes_receiver(self):
        bd = l2_bundle(); bd["S"]["sent_sha256"] = SHA_C; rebind(bd)
        self.blocked(bd, "EGRESS_CHAIN_INVALID")
        bd = l2_bundle(); bd["S"]["receiver"] = "OTHER"; rebind(bd)
        self.blocked(bd, "EGRESS_CHAIN_INVALID")

    def test_A32_same_family(self):
        bd = l2_bundle(); bd["X"][0]["model_family"] = "FAMILY-G"; rebind(bd)
        self.blocked(bd, "SAME_MODEL_FAMILY")

    def test_A37_post_review_field_in_M(self):
        bd = l1_bundle(); bd["M"]["candidate"]["disposition"] = "APPROVE"; rebind(bd)
        self.blocked(bd, "RECORD_INVALID")

    def test_A44_coverage(self):
        bd = l2_bundle(); del bd["X"][0]["opinions"]["C5"]; rebind(bd)
        self.blocked(bd, "CROSS_CHECK_INCOMPLETE")

    def test_A49_A50_declaration_and_I4(self):
        bd = l1_bundle(); bd["I"]["formed_at"] = "2026-12-01T10:20:00+08:00"; rebind(bd)
        self.blocked(bd, "PRE_REVIEW_DECLARATION_INVALID")
        bd = l1_bundle(); bd["I"]["items"]["6"] = "不确认"; rebind(bd)
        self.blocked(bd, "PRE_REVIEW_DECLARATION_INVALID")
        for v in ("提供并确认", "仅确认", "未参与"):
            bd = l1_bundle(); bd["I"]["items"]["4"] = v; rebind(bd)
            self.assertEqual(run(bd)["result"], "ELIGIBLE_TO_REQUEST_AR_B_010", v)

    def test_single_S_multiple_X(self):
        bd = l2_bundle(); x2 = copy.deepcopy(bd["X"][0]); x2["model"] = "model-y"; bd["X"].append(x2)
        self.blocked(bd, "MULTIPLE_CROSS_CHECKS")


class StopIndex(unittest.TestCase):
    def test_A56_unanswered(self):
        bd = l1_bundle(); bd["H"] = [disc("2026-12-01T09:30:00+08:00")]
        self.assertIn("STOP_RELEVANCE_UNANSWERED", reasons(bd))

    def test_A57_other_candidates_correction(self):
        bd = l1_bundle(); ev = disc("2026-12-01T09:30:00+08:00")
        cl = clear(ev, "CORRECTED_IN_CANDIDATE", "2026-12-01T09:40:00+08:00", scope=["CAND-B", "v1", SHA_A],
                   evidence=[{"record": "W", "sha256": SHA_D}])
        bd["H"] = [ev, cl]; bd["R"]["h_query"]["answers"] = answer(ev, cl=cl); rebind(bd)
        self.assertIn("STOP_INDEX_NOT_CLEARED", reasons(bd))

    def test_l1_correction_requires_W(self):
        # Codex PR #113 finding 4: a clearance alone is not enough
        bd = l1_bundle(); ev = disc("2026-12-01T09:30:00+08:00")
        bd["T"]["corrections"] = [{"discovery": sha(ev), "description": "改正期限先后", "diff_ref": SHA_D}]
        rebind(bd)
        scope = [bd["M"]["candidate"]["id"], bd["M"]["candidate"]["version"], sha(bd["M"])]
        no_w = clear(ev, "CORRECTED_IN_CANDIDATE", "2026-12-01T10:50:00+08:00", scope=scope,
                     evidence=[{"record": "W", "sha256": SHA_D}])
        bd["H"] = [ev, no_w]; bd["R"]["h_query"]["answers"] = answer(ev, cl=no_w); rebind(bd)
        self.assertIn("STOP_INDEX_NOT_CLEARED", reasons(bd))
        # with a W that passes, formed before the clearance: W -> clearance -> R
        W = mk("W", "2026-12-01T10:40:00+08:00", refs={"discovery": sha(ev)}, result="通过", location=copy.deepcopy(EVID))
        bd["W"] = [W]; rebind(bd)
        ok = clear(ev, "CORRECTED_IN_CANDIDATE", "2026-12-01T10:50:00+08:00", scope=scope,
                   evidence=[{"record": "W", "sha256": sha(bd["W"][0])}])
        bd["H"] = [ev, ok]; bd["R"]["h_query"]["answers"] = answer(ev, cl=ok); rebind(bd)
        self.assertEqual(run(bd)["result"], "ELIGIBLE_TO_REQUEST_AR_B_010")

    def test_reviewer_must_answer_coverage(self):
        # Codex PR #113 finding 8: reviewer says 未覆盖 even though a clearance exists -> not cleared
        bd = l1_bundle(); ev = disc("2026-12-01T09:30:00+08:00")
        cl = clear(ev, "FINDING_REFUTED", "2026-12-01T10:00:00+08:00")
        bd["H"] = [ev, cl]; bd["R"]["h_query"]["answers"] = answer(ev); rebind(bd)
        self.assertIn("STOP_INDEX_NOT_CLEARED", reasons(bd))
        bd["R"]["h_query"]["answers"] = answer(ev, cl=cl); rebind(bd)
        self.assertEqual(run(bd)["result"], "ELIGIBLE_TO_REQUEST_AR_B_010")

    def test_A59_A70_pre_send_check(self):
        # Codex PR #113 finding 6: stop after T and before sending, refuted only after sending
        bd = l2_bundle(); ev = disc("2026-12-01T10:25:00+08:00")
        cl = clear(ev, "FINDING_REFUTED", "2026-12-01T10:45:00+08:00")
        bd["H"] = [ev, cl]; bd["R"]["h_query"]["answers"] = answer(ev, cl=cl); rebind(bd)
        self.assertIn("EGRESS_CHAIN_INVALID", reasons(bd))

    def test_A72_A73_A74_post_r(self):
        # Codex PR #113 finding 5
        ev = disc("2026-12-03T09:00:00+08:00")
        bd = l2_bundle(); bd["H"] = [ev]
        self.assertIn("PAUSED_PENDING_STOP", reasons(bd))  # A-74
        cl = clear(ev, "FINDING_REFUTED", "2026-12-03T10:00:00+08:00")
        bd = l2_bundle(); bd["H"] = [ev, cl]
        self.assertIn("PAUSED_PENDING_STOP", reasons(bd))  # refuted, but no re-formed stage record
        q1 = LaterStages.q1(bd, "2026-12-03T11:00:00+08:00"); q1["h_increment"]["answers"] = answer(ev, cl=cl)
        bd["Q1"] = q1
        self.assertEqual(run(bd, stage="application")["result"], "APPLICATION_RECORDS_COMPLETE")  # A-72
        bd = l2_bundle()
        scope = [bd["M"]["candidate"]["id"], bd["M"]["candidate"]["version"], sha(bd["M"])]
        bd["H"] = [ev, clear(ev, "CORRECTED_IN_CANDIDATE", "2026-12-03T10:00:00+08:00", scope=scope,
                             evidence=[{"record": "W", "sha256": SHA_D}])]
        self.assertIn("R_INVALIDATED_BY_NEW_STOP", reasons(bd))  # A-73 / correction cannot keep old R

    def test_stop_at_check_instant(self):
        # Codex PR #113 round 3: a stop registered exactly at the check time must pause
        bd = LaterStages().full(); bd["H"] = [disc(NOW)]
        self.assertIn("PAUSED_PENDING_STOP", reasons(bd, stage="use"))

    def test_A67_unrelated(self):
        bd = l2_bundle(); ev = disc("2026-12-01T12:00:00+08:00"); bd["H"] = [ev]
        bd["P"]["h_increment"]["answers"] = answer(ev, "不相关")
        self.assertEqual(run(bd)["result"], "ELIGIBLE_TO_REQUEST_AR_B_010")


class LaterStages(unittest.TestCase):
    @staticmethod
    def rows(bd):
        return {"deadlines": copy.deepcopy(bd["R"]["deadlines"]), "new_deadlines": "无", "expired_deadlines": "无",
                "cutoff": CUTOFF, "authority": "仍有效", "qualification": "无变化", "withdrawal": "未撤回"}

    @staticmethod
    def q1(bd, at):
        refs = {"R": sha(bd["R"]), "application_body": SHA_D}
        if bd.get("P"):
            refs["P"] = sha(bd["P"])
        return mk("Q", at, refs=refs, stage="Q1", rows=LaterStages.rows(bd), h_increment=copy.deepcopy(EMPTY_Q), auth_checks=None)

    def full(self, max_uses=1):
        bd = l1_bundle()
        bd["Q1"] = self.q1(bd, "2026-12-02T09:00:00+08:00")
        bd["Q2"] = mk("Q", "2026-12-02T10:00:00+08:00", refs={"Q1": sha(bd["Q1"]), "application_body": SHA_D}, stage="Q2",
                      rows=self.rows(bd), h_increment=copy.deepcopy(EMPTY_Q), auth_checks=None)
        bd["AUTH"] = mk("AUTH", "2026-12-02T11:00:00+08:00", refs={"Q2": sha(bd["Q2"]), "application_body": SHA_D},
                        action="内部存档整理", scope={"candidate": "CAND-Z", "version": "v1", "M": sha(bd["M"])},
                        own_deadline="2026-12-10T00:00:00+08:00", max_uses=max_uses)
        bd["Q3"] = mk("Q", "2026-12-03T10:00:00+08:00", refs={"AUTH": sha(bd["AUTH"]), "Q2": sha(bd["Q2"])}, stage="Q3",
                      rows=self.rows(bd), h_increment=copy.deepcopy(EMPTY_Q),
                      auth_checks={k: True for k in g.AUTH_CHECK_KEYS})
        bd["G"] = [{"kind": "initial", "auth": sha(bd["AUTH"]), "max_uses": max_uses, "used": 0, "at": "2026-12-02T11:00:00+08:00"}]
        return bd

    def test_application_and_use_positive(self):
        bd = l1_bundle()
        self.assertIn("RECHECK_MISSING", reasons(bd, stage="application"))
        self.assertEqual(run(self.full(), stage="use")["result"], "PRE_USE_RECORDS_COMPLETE")

    def test_q_rows_closed(self):
        # Codex PR #113 finding 3
        bd = l1_bundle(); bd["Q1"] = self.q1(bd, "2026-12-02T09:00:00+08:00"); bd["Q1"]["rows"] = {"anything": "满足"}
        self.assertIn("RECHECK_MISSING", reasons(bd, stage="application"))
        bd = l1_bundle(); bd["Q1"] = self.q1(bd, "2026-12-02T09:00:00+08:00")
        bd["Q1"]["rows"]["deadlines"][0]["expiry"] = "2026-12-16T00:00:00+08:00"  # A-51 rescheduled deadline
        self.assertIn("RECHECK_MISSING", reasons(bd, stage="application"))

    def test_q_and_auth_chain(self):
        # Codex PR #113 finding 2 and A-48
        bd = self.full(); bd["Q1"]["refs"] = {}
        self.assertIn("BINDING_MISMATCH", reasons(bd, stage="use"))
        bd = self.full(); bd["AUTH"]["scope"]["candidate"] = "CAND-OTHER"
        self.assertIn("AUTHORIZATION_INVALID", reasons(bd, stage="use"))
        bd = self.full(); bd["Q3"]["refs"] = {"AUTH": SHA_A, "Q2": sha(bd["Q2"])}
        self.assertIn("AUTHORIZATION_INVALID", reasons(bd, stage="use"))

    def test_auth_after_Q2(self):
        bd = self.full(); bd["AUTH"]["formed_at"] = "2026-12-02T09:30:00+08:00"
        bd["Q3"]["refs"] = {"AUTH": sha(bd["AUTH"]), "Q2": sha(bd["Q2"])}
        bd["G"][0]["auth"] = sha(bd["AUTH"]); bd["G"][0]["at"] = "2026-12-02T09:30:00+08:00"
        self.assertIn("AUTHORIZATION_INVALID", reasons(bd, stage="use"))

    def test_A60_A61_A62(self):
        bd = self.full(); bd["Q3"]["auth_checks"]["not_withdrawn"] = False
        self.assertIn("AUTHORIZATION_INVALID", reasons(bd, stage="use"))
        self.assertIn("AUTHORIZATION_INVALID", reasons(self.full(), stage="use", now="2026-12-11T00:00:00+08:00"))
        bd = self.full(); del bd["AUTH"]
        self.assertIn("AUTHORIZATION_INVALID", reasons(bd, stage="use"))

    def test_A69_A75_usage_log(self):
        # Codex PR #113 finding 9
        bd = self.full(); bd["G"] = []
        self.assertIn("USAGE_COUNT_UNVERIFIED", reasons(bd, stage="use"))
        bd = self.full(max_uses=2); bd["G"].append({"kind": "use", "auth": sha(bd["AUTH"])})
        self.assertIn("RECORD_INVALID", reasons(bd, stage="use"))
        bd = self.full(max_uses=1)
        bd["G"].append({"kind": "use", "auth": sha(bd["AUTH"]), "q3": SHA_D, "at": "2026-12-02T12:00:00+08:00"})
        self.assertIn("USAGE_COUNT_UNVERIFIED", reasons(bd, stage="use"))


class Builder(unittest.TestCase):
    def test_refuses_missing_answers(self):
        with self.assertRaises(b.MissingAnswer):
            b.require_answers({"1", "2"}, {"1": "确认"})
        ev = disc("2026-12-01T09:30:00+08:00")
        enum = b.enumerate_stop_events([ev], CASE)
        with self.assertRaises(b.MissingAnswer):
            b.stop_query(enum, {})
        with self.assertRaises(b.MissingAnswer):  # relevance without a coverage answer
            b.stop_query(enum, {sha(ev): {"relevant": "相关", "reason": "x"}})

    def test_enumeration_lists_clearances_and_never_judges(self):
        ev = disc("2026-12-01T09:30:00+08:00"); cl = clear(ev, "FINDING_REFUTED", "2026-12-01T10:00:00+08:00")
        enum = b.enumerate_stop_events([ev, cl], CASE)
        item = enum["discoveries"][0]
        self.assertEqual(item["clearances"][0]["sha256"], sha(cl))
        self.assertNotIn("relevant", item)
        self.assertNotIn("covered", item)
        out = b.stop_query(enum, {sha(ev): {"relevant": "相关", "reason": "同一期限", "covered": "已覆盖", "clearance": sha(cl)}})
        self.assertEqual(out["answers"][sha(ev)]["covered"], "已覆盖")

    def test_cutoff(self):
        with self.assertRaises(b.MissingAnswer):
            b.validity_cutoff("2026-12-01", [{"status": "未知"}])
        self.assertEqual(b.validity_cutoff("2026-12-01", DEADLINES), "2026-12-20T00:00+08:00")


if __name__ == "__main__":
    unittest.main()
