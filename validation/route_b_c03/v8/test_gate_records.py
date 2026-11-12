"""Tests for C03 V8-A (design C03-GATE-ENFORCEMENT-V8 R2). All data is fictional.

Run: python3 -m unittest discover -s validation/route_b_c03/v8 -t validation/route_b_c03/v8
"""

from __future__ import annotations

import copy
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "scripts"))

from phase2_runtime.route_b_c03 import gate_records as g  # noqa: E402
from phase2_runtime.route_b_c03 import gate_record_builder as b  # noqa: E402

SHA_A = "A" * 64
SHA_B = "B" * 64
SHA_C = "C" * 64
CASE = "CASE-Z"


def mk(kind, refs, at, **fields):
    return b.build(kind, refs=refs, formed_at=at, method="chat_c", **fields)


def m_record(cls="C03_CONFLICT_AND_INFORMATION_GAP_REGISTER_CANDIDATE"):
    return mk(
        "M", {}, "2026-12-01T09:00:00+08:00",
        candidate={"id": "CAND-Z", "version": "v1", "output_sha256": SHA_A, "generated_at": "2026-12-01T08:00:00+08:00",
                   "class": cls, "capability": "C03", "operation": "fictional", "generator": "gen-model",
                   "generator_model_family": "FAMILY-G"},
        case={"code": CASE, "version": "v1"},
        trace_refs={"S-1": {"path": "fictional/a.pdf", "sha256": SHA_B}},
        contract_refs=[], omission_conflict_adverse_refs=[], failure_audit_refs=[],
        authority={"pack_sha256": SHA_C, "check_date": "2026-12-01", "entries": []},
        known_limitations="虚构", prohibited_uses="不得对外",
        design_version={"design_id": g.DESIGN_ID, "text_sha256": g.ADOPTED_R3_SHA256, "checklist": g.CHECKLIST_ID},
        planned_scope="C1-C11", reviewer={"code": "REVIEWER-01", "qualification_ref": "QUAL-REF-01"},
    )


ALL_PASS = {c: "通过" for c in g.CHECKLIST}
DEADLINES = [{"item": "下一期付款", "status": "适用", "expiry": "2026-12-20T00:00:00+08:00"}]


def l1_bundle():
    M = m_record()
    I = mk("I", {"M": g.record_sha256(M)}, "2026-12-01T10:00:00+08:00", reviewer_name="虚构律师",
           items={"1": "确认", "2": "确认", "3": "确认", "4": "提供并确认", "5": "确认", "6": "确认"})
    T = mk("T", {"M": g.record_sha256(M), "I": g.record_sha256(I)}, "2026-12-01T10:10:00+08:00",
           use_code="U1", output_class=M["candidate"]["class"], audience=g.AUDIENCE, next_step="内部存档整理",
           l1_positive_confirmation=True, h_query=None)
    R = mk("R", {"M": g.record_sha256(M), "I": g.record_sha256(I), "T": g.record_sha256(T)}, "2026-12-01T11:00:00+08:00",
           h_query={"answers": {}, "last_event": None}, actual_scope="C1-C11", checklist=dict(ALL_PASS),
           c11_original_verified=True, deadlines=copy.deepcopy(DEADLINES), no_deadline_declaration=False,
           validity_cutoff="2026-12-20T00:00:00+08:00", material_conflict="无", withdrawn=False,
           disposition=g.APPROVE, reason="虚构")
    return {"M": M, "I": I, "T": T, "R": R, "X": [], "V": [], "W": [], "CORR": [], "G": [], "H": []}


def rebind(bundle):
    """Recompute references after a mutation so only the intended defect remains."""
    M, I, T, R = bundle["M"], bundle["I"], bundle["T"], bundle["R"]
    I["refs"] = {"M": g.record_sha256(M)}
    T["refs"] = {"M": g.record_sha256(M), "I": g.record_sha256(I)}
    R["refs"] = {"M": g.record_sha256(M), "I": g.record_sha256(I), "T": g.record_sha256(T)}
    if bundle.get("E"):
        bundle["E"]["refs"] = {"M": g.record_sha256(M), "T": g.record_sha256(T)}
        bundle["S"]["refs"] = {"E": g.record_sha256(bundle["E"])}
        for x in bundle["X"]:
            x["refs"] = {"S": g.record_sha256(bundle["S"])}
        for v in bundle["V"]:
            v["refs"] = {"M": g.record_sha256(M), "T": g.record_sha256(T), "X": g.record_sha256(bundle["X"][0])}
        R["refs"]["X"] = g.record_sha256(bundle["X"][0])
    if bundle.get("P"):
        bundle["P"]["refs"] = {"R": g.record_sha256(R)}
    return bundle


def l2_bundle():
    bd = l1_bundle()
    M, T, R = bd["M"], bd["T"], bd["R"]
    T.update(use_code="U2", next_step="自行起草参考", l1_positive_confirmation=False,
             h_query={"answers": {}, "last_event": None})
    E = mk("E", {}, "2026-12-01T10:20:00+08:00", d_sha256=SHA_A, task_sha256=SHA_B, scope="全新会话，仅 D 与任务说明",
           allowed_fields=["结构"], receiver="CROSS-PROVIDER/model-x", conditions={k: "接受" for k in ("retention", "training", "reshare", "region")},
           config_sha256=SHA_C, window={"start": "2026-12-01T10:00:00+08:00", "end": "2026-12-02T10:00:00+08:00"}, withdrawn=False)
    S = mk("S", {}, "2026-12-01T10:31:00+08:00", sent_sha256=SHA_A, scope=E["scope"], receiver=E["receiver"],
           config_sha256=SHA_C, checks={str(i): "通过" for i in range(1, 7)}, h_last_event=None, request_id="req-1",
           sent_at="2026-12-01T10:30:00+08:00")
    X = mk("X", {}, "2026-12-01T10:40:00+08:00", opinions={c: {"value": "通过"} for c in g.CHECKLIST},
           provider="CROSS-PROVIDER", model="model-x", model_family="FAMILY-X", received_at="2026-12-01T10:40:00+08:00",
           request_id="req-1")
    bd.update(E=E, S=S, X=[X])
    R["formed_at"] = "2026-12-01T11:00:00+08:00"
    P = mk("P", {}, "2026-12-02T12:00:00+08:00", reconfirm={str(i): "已重查" for i in range(1, 5)},
           authority_recheck_at="2026-12-02T11:30:00+08:00", h_increment={"answers": {}, "last_event": None})
    bd["P"] = P
    return rebind(bd)


NOW = "2026-12-05T09:00:00+08:00"


def run(bundle, stage="review", now=NOW):
    return g.validate(bundle, now=now, stage=stage)


def reasons(bundle, **kw):
    return run(bundle, **kw)["reasons"]


class JCSTests(unittest.TestCase):
    def test_rfc8785_key_order_utf16(self):
        obj = {"€": 1, "\r": 2, "דּ": 3, "1": 4, "\U0001F600": 5, "\u0080": 6, "ö": 7}
        keys = [k for k in __import__("json").loads(g.canonical_bytes(obj).decode())]
        self.assertEqual(keys, ["\r", "1", "\u0080", "ö", "€", "\U0001F600", "דּ"])

    def test_utf16_vs_codepoint_difference(self):
        out = g.canonical_bytes({"": 1, "\U00010000": 2}).decode()
        self.assertLess(out.index("\U00010000"), out.index(""))

    def test_rejects_float_big_int_dupes_lone_surrogate(self):
        with self.assertRaises(g.RecordError):
            g.canonical_bytes({"a": 1.5})
        with self.assertRaises(g.RecordError):
            g.canonical_bytes({"a": 10**21})
        with self.assertRaises(g.RecordError):
            g.parse_record('{"a":1,"a":2}')
        with self.assertRaises(g.RecordError):
            g.canonical_bytes({"a": "\ud800"})

    def test_canonical_escapes(self):
        self.assertEqual(g.canonical_bytes({"b": "\n\u001f\"/", "a": [True, None, 0]}).decode(),
                         '{"a":[true,null,0],"b":"\\n\\u001f\\"/"}')


class PositivePaths(unittest.TestCase):
    def test_l1_positive(self):
        self.assertEqual(run(l1_bundle()), {"result": "ELIGIBLE_TO_REQUEST_AR_B_010", "reasons": []})

    def test_l2_positive(self):
        self.assertEqual(run(l2_bundle()), {"result": "ELIGIBLE_TO_REQUEST_AR_B_010", "reasons": []})

    def test_pure_no_io(self):
        # validate is called with in-memory data only; it must not need a clock or files.
        self.assertIn("result", run(l1_bundle()))


class AnnexA(unittest.TestCase):
    """Counterexamples from R3 annex A that can be expressed as records."""

    def assert_blocked(self, bundle, code, **kw):
        out = run(bundle, **kw)
        self.assertEqual(out["result"], "BLOCKED")
        self.assertIn(code, out["reasons"])

    def test_A01_A02_A29_prohibited_purpose(self):
        bd = l1_bundle(); bd["T"]["next_step"] = "作为给法院的情况说明附件"; rebind(bd)
        self.assert_blocked(bd, "PURPOSE_PROHIBITED")
        bd = l1_bundle(); bd["T"]["audience"] = "委托人"; rebind(bd)
        self.assert_blocked(bd, "PURPOSE_PROHIBITED")

    def test_A03_tier_invalid(self):
        bd = l1_bundle(); bd["T"]["l1_positive_confirmation"] = None; rebind(bd)
        self.assert_blocked(bd, "TIER_INVALID")

    def test_purpose_not_established(self):
        bd = l1_bundle(); bd["T"]["use_code"] = "U9"; rebind(bd)
        self.assert_blocked(bd, "PURPOSE_NOT_ESTABLISHED")

    def test_A04_A05_A33_stop_needs_typed_V(self):
        bd = l2_bundle(); bd["X"][0]["opinions"]["C7"] = {"value": "无法判断-可见范围内"}; rebind(bd)
        self.assert_blocked(bd, "STOP_UNRESOLVED")
        bd = l2_bundle(); bd["X"][0]["opinions"]["C5"] = {"value": "不通过"}
        bd["V"] = [mk("V", {}, "2026-12-01T10:50:00+08:00", item="C5", issue="x",
                      clearance_type="MODEL_FINDING_REFUTED_BY_ORIGINAL", evidence=[])]
        rebind(bd)
        self.assert_blocked(bd, "STOP_UNRESOLVED")

    def test_A55_same_round_refutation_clears(self):
        bd = l2_bundle(); bd["X"][0]["opinions"]["C5"] = {"value": "不通过"}
        bd["V"] = [mk("V", {}, "2026-12-01T10:50:00+08:00", item="C5", issue="x",
                      clearance_type="MODEL_FINDING_REFUTED_BY_ORIGINAL", evidence=[{"code": "S-1", "sha256": SHA_B, "locator": "p2"}])]
        rebind(bd)
        self.assertEqual(run(bd)["result"], "ELIGIBLE_TO_REQUEST_AR_B_010")

    def test_A06_checklist(self):
        bd = l1_bundle(); bd["R"]["checklist"]["C9"] = "不通过"; rebind(bd)
        self.assert_blocked(bd, "CHECKLIST_NOT_ALL_PASS")

    def test_A08_conditions_not_accepted(self):
        bd = l2_bundle(); bd["E"]["conditions"]["training"] = "未确认"; rebind(bd)
        self.assert_blocked(bd, "EGRESS_CHAIN_INVALID")

    def test_A09_c11_original(self):
        bd = l1_bundle(); bd["R"]["c11_original_verified"] = False; rebind(bd)
        self.assert_blocked(bd, "CHECKLIST_NOT_ALL_PASS")

    def test_A11_A16_binding(self):
        bd = l2_bundle(); bd["P"]["refs"] = {"R": SHA_A}
        self.assert_blocked(bd, "BINDING_MISMATCH")
        bd = l1_bundle(); bd["R"]["refs"]["M"] = SHA_A
        self.assert_blocked(bd, "BINDING_MISMATCH")

    def test_A12_cooling(self):
        bd = l2_bundle(); bd["P"]["formed_at"] = "2026-12-01T20:00:00+08:00"
        bd["P"]["authority_recheck_at"] = "2026-12-01T19:00:00+08:00"
        self.assert_blocked(bd, "COOLING_PERIOD_UNMET")

    def test_A13_exclusive_cutoff(self):
        bd = l2_bundle(); bd["P"]["formed_at"] = "2026-12-20T00:00:00+08:00"
        self.assert_blocked(bd, "VALIDITY_EXPIRED")

    def test_A17_x_other_send(self):
        bd = l2_bundle(); bd["X"][0]["refs"] = {"S": SHA_C}
        self.assert_blocked(bd, "CHAIN_BROKEN")

    def test_A21_design_version(self):
        bd = l1_bundle(); bd["M"]["design_version"]["text_sha256"] = SHA_A; rebind(bd)
        self.assert_blocked(bd, "DESIGN_VERSION_MISMATCH")

    def test_A22_A23_expired_at_check(self):
        self.assert_blocked(l1_bundle(), "VALIDITY_EXPIRED", now="2026-12-21T00:00:00+08:00")

    def test_A24_reconfirmation(self):
        bd = l2_bundle(); bd["P"]["reconfirm"]["2"] = "未发现变化"
        self.assert_blocked(bd, "RECONFIRMATION_MISSING")

    def test_A25_unknown_deadline_and_trial_shape(self):
        bd = l1_bundle(); bd["R"]["deadlines"].append({"item": "查封期限", "status": "未知", "expiry": None})
        bd["R"]["disposition"] = "KEEP BLOCKED"; rebind(bd)
        out = reasons(bd)
        self.assertIn("DEADLINE_STATUS_UNKNOWN", out)
        self.assertIn("DISPOSITION_NOT_APPROVE", out)

    def test_A26_bad_time(self):
        bd = l1_bundle(); bd["R"]["formed_at"] = "2026-02-30T10:00:00"
        self.assert_blocked(bd, "RECORD_INVALID")

    def test_A27_A28_bytes_receiver(self):
        bd = l2_bundle(); bd["S"]["sent_sha256"] = SHA_C; rebind(bd)
        self.assert_blocked(bd, "EGRESS_CHAIN_INVALID")
        bd = l2_bundle(); bd["S"]["receiver"] = "OTHER"; rebind(bd)
        self.assert_blocked(bd, "EGRESS_CHAIN_INVALID")

    def test_A32_same_family(self):
        bd = l2_bundle(); bd["X"][0]["model_family"] = "FAMILY-G"; rebind(bd)
        self.assert_blocked(bd, "SAME_MODEL_FAMILY")

    def test_A37_post_review_field_in_M(self):
        bd = l1_bundle(); bd["M"]["candidate"]["disposition"] = "APPROVE"; rebind(bd)
        out = reasons(bd)
        self.assertTrue("RECORD_INVALID" in out or "M_CONTAINS_POST_REVIEW_FIELD" in out)

    def test_A44_A45_coverage(self):
        bd = l2_bundle(); del bd["X"][0]["opinions"]["C5"]; rebind(bd)
        self.assert_blocked(bd, "CROSS_CHECK_INCOMPLETE")
        bd = l2_bundle(); bd["X"][0]["opinions"]["C6"] = {"value": "无法判断-脱敏盲区", "blind_sub": "x"}; rebind(bd)
        self.assert_blocked(bd, "CROSS_CHECK_INCOMPLETE")

    def test_A49_A50_declaration(self):
        bd = l1_bundle(); bd["I"]["formed_at"] = "2026-12-01T10:20:00+08:00"; rebind(bd)
        self.assert_blocked(bd, "PRE_REVIEW_DECLARATION_INVALID")
        bd = l1_bundle(); bd["I"]["items"]["6"] = "不确认"; rebind(bd)
        self.assert_blocked(bd, "PRE_REVIEW_DECLARATION_INVALID")

    def test_I4_three_values(self):
        for v in ("提供并确认", "仅确认", "未参与"):
            bd = l1_bundle(); bd["I"]["items"]["4"] = v; rebind(bd)
            self.assertEqual(run(bd)["result"], "ELIGIBLE_TO_REQUEST_AR_B_010", v)
        bd = l1_bundle(); bd["I"]["items"]["4"] = "确认"; rebind(bd)
        self.assert_blocked(bd, "PRE_REVIEW_DECLARATION_INVALID")

    def test_single_S_multiple_X(self):
        bd = l2_bundle(); bd["X"].append(copy.deepcopy(bd["X"][0])); bd["X"][1]["model"] = "model-y"
        self.assert_blocked(bd, "MULTIPLE_CROSS_CHECKS")

    def test_M_missing_inherited_field(self):
        bd = l1_bundle(); del bd["M"]["prohibited_uses"]; rebind(bd)
        self.assert_blocked(bd, "RECORD_INVALID")


def discovery(at, item="C5", typ="人工停点"):
    return {"event": "discovery", "type": typ, "case": CASE, "item": item, "issue": "虚构争点", "candidate": "CAND-OTHER",
            "M": SHA_C, "X": "不适用", "stage": "R 时", "at": at}


def clearance(ev, typ, at, scope=None, evidence=None):
    return {"event": "clearance", "type": typ, "refs_discovery": g.record_sha256(ev), "scope_candidate": scope,
            "evidence": evidence if evidence is not None else [], "at": at}


class StopIndex(unittest.TestCase):
    def test_A56_unanswered_relevance(self):
        bd = l1_bundle(); bd["H"] = [discovery("2026-12-01T09:30:00+08:00")]
        self.assertIn("STOP_RELEVANCE_UNANSWERED", reasons(bd))

    def test_A57_other_candidates_correction_does_not_cover(self):
        bd = l1_bundle(); ev = discovery("2026-12-01T09:30:00+08:00")
        bd["H"] = [ev, clearance(ev, "CORRECTED_IN_CANDIDATE", "2026-12-01T09:40:00+08:00", scope=["CAND-B", "v1", SHA_A])]
        bd["R"]["h_query"] = {"answers": {g.record_sha256(ev): {"relevant": "相关", "reason": "同一期限"}}, "last_event": None}
        rebind(bd)
        self.assertIn("STOP_INDEX_NOT_CLEARED", reasons(bd))

    def test_pre_r_correction_for_this_candidate_clears(self):
        bd = l1_bundle(); ev = discovery("2026-12-01T09:30:00+08:00")
        bd["H"] = [ev, clearance(ev, "CORRECTED_IN_CANDIDATE", "2026-12-01T10:50:00+08:00",
                                 scope=["CAND-Z", "v1", g.record_sha256(bd["M"])])]
        bd["R"]["h_query"] = {"answers": {g.record_sha256(ev): {"relevant": "相关", "reason": "同一期限"}}, "last_event": None}
        rebind(bd)
        self.assertEqual(run(bd)["result"], "ELIGIBLE_TO_REQUEST_AR_B_010")

    def test_A72_A73_A74_post_r_rules(self):
        # A-74: new related stop after R, no clearance -> paused
        bd = l2_bundle(); ev = discovery("2026-12-03T09:00:00+08:00"); bd["H"] = [ev]
        self.assertIn("PAUSED_PENDING_STOP", reasons(bd))
        # A-72: refuted with original evidence in M -> continues
        bd = l2_bundle(); ev = discovery("2026-12-03T09:00:00+08:00")
        bd["H"] = [ev, clearance(ev, "FINDING_REFUTED", "2026-12-03T10:00:00+08:00",
                                 evidence=[{"code": "S-1", "sha256": SHA_B, "locator": "p3"}])]
        self.assertNotIn("PAUSED_PENDING_STOP", reasons(bd))
        self.assertNotIn("R_INVALIDATED_BY_NEW_STOP", reasons(bd))
        # correction after R cannot keep the old R
        bd = l2_bundle(); ev = discovery("2026-12-03T09:00:00+08:00")
        bd["H"] = [ev, clearance(ev, "CORRECTED_IN_CANDIDATE", "2026-12-03T10:00:00+08:00",
                                 scope=["CAND-Z", "v1", g.record_sha256(bd["M"])])]
        self.assertIn("R_INVALIDATED_BY_NEW_STOP", reasons(bd))

    def test_A67_increment_marked_unrelated(self):
        bd = l2_bundle(); ev = discovery("2026-12-01T12:00:00+08:00"); bd["H"] = [ev]
        bd["P"]["h_increment"] = {"answers": {g.record_sha256(ev): {"relevant": "不相关", "reason": "不同争点"}}, "last_event": None}
        self.assertEqual(run(bd)["result"], "ELIGIBLE_TO_REQUEST_AR_B_010")


class LaterStages(unittest.TestCase):
    def q(self, name, at, prev=None):
        return mk("Q", {}, at, stage=name, rows={"期限": "满足", "依据": "满足", "资格": "满足", "撤回": "满足"},
                  h_increment={"answers": {}, "last_event": None}, auth_checks=None)

    def test_application_needs_Q1(self):
        bd = l1_bundle()
        self.assertIn("RECHECK_MISSING", reasons(bd, stage="application"))
        bd["Q1"] = self.q("Q1", "2026-12-02T09:00:00+08:00")
        self.assertEqual(run(bd, stage="application")["result"], "APPLICATION_RECORDS_COMPLETE")

    def test_A60_A61_A62_A69_A75_use_stage(self):
        bd = l1_bundle()
        bd["Q1"] = self.q("Q1", "2026-12-02T09:00:00+08:00")
        bd["Q2"] = self.q("Q2", "2026-12-02T10:00:00+08:00")
        bd["Q3"] = self.q("Q3", "2026-12-03T10:00:00+08:00")
        bd["Q3"]["auth_checks"] = {k: True for k in ("exists", "not_withdrawn", "own_deadline_ok", "count_ok", "action_scope_match")}
        bd["AUTH"] = mk("AUTH", {}, "2026-12-02T11:00:00+08:00", action="内部存档", scope="CAND-Z v1",
                        own_deadline="2026-12-10T00:00:00+08:00", max_uses=1)
        auth = g.record_sha256(bd["AUTH"])
        bd["G"] = [{"kind": "initial", "auth": auth, "used": 0}]
        self.assertEqual(run(bd, stage="use")["result"], "PRE_USE_RECORDS_COMPLETE")
        # A-75: no initial event
        bd2 = copy.deepcopy(bd); bd2["G"] = []
        self.assertIn("USAGE_COUNT_UNVERIFIED", reasons(bd2, stage="use"))
        # A-61: authorization's own deadline passed
        self.assertIn("AUTHORIZATION_INVALID", reasons(bd, stage="use", now="2026-12-11T00:00:00+08:00"))
        # A-60: withdrawn authorization
        bd3 = copy.deepcopy(bd); bd3["Q3"]["auth_checks"]["not_withdrawn"] = False
        self.assertIn("AUTHORIZATION_INVALID", reasons(bd3, stage="use"))
        # A-62: no authorization at all
        bd4 = copy.deepcopy(bd); del bd4["AUTH"]
        self.assertIn("AUTHORIZATION_INVALID", reasons(bd4, stage="use"))


class Builder(unittest.TestCase):
    def test_builder_refuses_missing_answers(self):
        with self.assertRaises(b.MissingAnswer):
            b.require_answers({"1", "2"}, {"1": "确认"})
        enum = b.enumerate_stop_events([discovery("2026-12-01T09:30:00+08:00")], CASE)
        with self.assertRaises(b.MissingAnswer):
            b.stop_query(enum, {})

    def test_builder_never_answers_relevance(self):
        enum = b.enumerate_stop_events([discovery("2026-12-01T09:30:00+08:00")], CASE)
        self.assertNotIn("relevant", enum[0])

    def test_cutoff_unknown_refused(self):
        with self.assertRaises(b.MissingAnswer):
            b.validity_cutoff("2026-12-01", [{"status": "未知"}])
        self.assertEqual(b.validity_cutoff("2026-12-01", DEADLINES), "2026-12-20T00:00+08:00")


if __name__ == "__main__":
    unittest.main()
