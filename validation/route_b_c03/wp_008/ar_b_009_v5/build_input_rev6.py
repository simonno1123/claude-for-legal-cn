"""Build input candidate REV6 from input REV5 (prepared under the AR-B-009 work authorization; not accepted).

REV6 = REV5 with exactly these changes, all made here so the derivation can be reviewed:
  1. subject_identities, adapter subject hashes and catalog source_sha256 values are re-hashed from the V5 sources;
  2. seven adapters for the WP-009 evaluators in failures.py are added;
  3. synthetic catalog objects for the new evaluators are added;
  4. 28 variants with pre-declared rules are added to scenarios V-006, V-008, V-009, V-010, V-011, V-012 and V-013.
     One variant per scenario carries a fixture mapping to that scenario's original fixture oracle; the others are
     raw checks. The expected audit-chain head is computed here by an independent re-implementation of the
     digest rule (not by calling the subject);
  5. those seven scenarios get coverage_class_rev6 = PARTIAL_LIMITED: the deterministic control logic is
     exercised, but no runtime timer, signal propagation, persistence or real dependency is observed.
The 42 REV5 variants and their rules are otherwise unchanged.

Run from the repository root:  python3 -I validation/route_b_c03/wp_008/ar_b_009_v5/build_input_rev6.py [--write]
"""
import copy
import hashlib
import json
import sys

SRC = "validation/route_b_c03/wp_008/ar_b_007_v4/C03_V4_INPUT_CANDIDATE_REV5.json"
SRC_SHA = "8A422CEE97A9434201CFA4309A2359672DD3E9ADEBF9322CD1C2AFBD9A27800A"
OUT = "validation/route_b_c03/wp_008/ar_b_009_v5/C03_V5_INPUT_CANDIDATE_REV6.json"
STATUS = "DRAFTED_REV6_NOT_ACCEPTED"
DERIVATION = "pre-declared from static reading of the V5 subject source before any harness run"
FAILURES = "scripts/phase2_runtime/route_b_c03/failures.py"
SHA_A = "5" * 64
SHA_B = "6" * 64
SHA_C = "7" * 64
LIMITED_NOTE = ("deterministic control logic over caller-supplied references only; no runtime timer, signal "
                "propagation, persistence, ledger or real dependency is observed")


def sha_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest().upper()


def cd_rule(applies, member, reason, mapping=None, limitation=LIMITED_NOTE):
    return {"status": STATUS, "derivation": DERIVATION, "applies_to": applies,
            "observation_surface": "ControlDetermination.state/reason_code",
            "raw_requirement": {"type": "ControlDetermination", "state": {"enum_class": "ControlState", "member": member},
                                "reason_code": reason},
            "fixture_mapping": mapping, "coverage_class": "PARTIAL_LIMITED" if mapping else "SUPPLEMENTARY_RAW_CHECK",
            "limitation": limitation,
            "comparison_mode": "EXACT_NATIVE_TYPES_AND_VALUES; NO SEMANTIC NORMALIZATION, PREFIX MATCH OR REASON SUBSTITUTION",
            "mismatch_policy": "DO_NOT_ASSERT_CONFORMANCE; PRESERVE RAW OBSERVATION OR EXCEPTION; THE VARIANT IS FAIL",
            "post_hoc_change": "PROHIBITED"}


def variant(sbid, adapter, args, rule, role):
    return {"stimulus_binding_id": sbid, "adapter_id": adapter, "arguments": args, "object_overrides": {},
            "selected_defaults": "ALL_DEFAULTS_EXPLICIT_IN_OBJECT_CATALOG_OR_ARGUMENTS",
            "observation_surface": "ControlDetermination.state/reason_code", "comparison_rule_id": rule, "variant_role": role}


def ref(oid):
    return {"object_ref": oid}


def tup(*items):
    return {"tuple": list(items)}


def enum(cls, member):
    return {"enum_class": cls, "member": member}


def independent_chain_head(records):
    """Re-implementation of the V5 digest rule: sha256(prev + LF + canonical JSON of all fields), genesis 64 zeros."""
    head = "0" * 64
    for fields in records:
        payload = json.dumps(fields, ensure_ascii=True, sort_keys=True, separators=(",", ":"))
        head = hashlib.sha256((head + "\n" + payload).encode("ascii")).hexdigest().upper()
    return head


def main():
    with open(SRC, "rb") as f:
        raw = f.read()
    if hashlib.sha256(raw).hexdigest().upper() != SRC_SHA:
        raise SystemExit("REV5_SHA_MISMATCH")
    d = json.loads(raw.decode("utf-8"))
    new = copy.deepcopy(d)

    subj = {p: sha_file(p) for p in d["subject_identities"]}
    new["subject_identities"] = subj
    for a in new["adapter_catalog"].values():
        a["subject_sha256"] = subj[a["subject_path"]]
    refreshed = 0
    for o in new["synthetic_object_catalog"].values():
        if "source_path" in o and o["source_path"] in subj and o.get("source_sha256") != subj[o["source_path"]]:
            o["source_sha256"] = subj[o["source_path"]]
            refreshed += 1

    adapters = {
        "ADP-CONTROL-PRECEDENCE": ("evaluate_control_precedence", [], ["kill", "revocation", "control_state_known", "subject_scope"]),
        "ADP-EVALUATE-IDEMPOTENCY": ("evaluate_idempotency", ["key", "prior_records"], ["scope_sha256", "evaluated_at", "window_from", "superseded_or_revoked"]),
        "ADP-EVALUATE-TIMEOUT": ("evaluate_timeout", ["policy"], ["started_at", "deadline_at", "observed_at", "result_received_at"]),
        "ADP-EVALUATE-ROLLBACK": ("evaluate_rollback", ["reference"], ["accepted_prior_identities", "decision_reference_valid", "kill_active", "revoked"]),
        "ADP-EVALUATE-SUPERSESSION": ("evaluate_supersession", ["identity", "supersessions"], []),
        "ADP-VERIFY-AUDIT-CHAIN": ("verify_audit_chain", ["records"], ["expected_head_sha256"]),
        "ADP-EVALUATE-DEPENDENCY": ("evaluate_dependency", ["requested_dependency"], ["authorized_dependencies", "availability_state"]),
    }
    for aid, (fn, pos, kw) in adapters.items():
        new["adapter_catalog"][aid] = {"subject_path": FAILURES, "subject_sha256": subj[FAILURES], "callable": fn,
                                       "dispatch_state": "PROPOSED_FIXED_HARNESS_MAPPING_NOT_ACCEPTED",
                                       "argument_order": pos, "keyword_only": kw}

    cat = new["synthetic_object_catalog"]

    def obj(oid, typ, args):
        cat[oid] = {"type": typ, "source_path": "scripts/phase2_runtime/route_b_c03/contracts.py",
                    "source_sha256": subj["scripts/phase2_runtime/route_b_c03/contracts.py"], "arguments": args}

    obj("OBJ-V5-IDEM-KEY", "IdempotencyKeyReference", {"canonicalization_version": "1.0-SYNTHETIC", "digest_algorithm": "SHA-256",
                                                       "key_sha256": SHA_A, "replay_window_reference": "SYNTHETIC-WINDOW-REFERENCE"})
    obj("OBJ-V5-IDEM-KEY-UNBOUND", "IdempotencyKeyReference", {"canonicalization_version": "1.0-SYNTHETIC", "digest_algorithm": "MD5",
                                                               "key_sha256": SHA_A, "replay_window_reference": "SYNTHETIC-WINDOW-REFERENCE"})
    obj("OBJ-V5-IDEM-PRIOR-EFFECT", "IdempotencyRecord", {"key_sha256": SHA_A, "scope_sha256": SHA_B,
                                                          "recorded_at": "2026-05-15T00:00:00Z", "effect_reference": "SYNTHETIC-EFFECT-001"})
    obj("OBJ-V5-IDEM-PRIOR-OTHER-SCOPE", "IdempotencyRecord", {"key_sha256": SHA_A, "scope_sha256": SHA_C,
                                                               "recorded_at": "2026-05-15T00:00:00Z", "effect_reference": "NONE"})
    obj("OBJ-V5-IDEM-PRIOR-OLD", "IdempotencyRecord", {"key_sha256": SHA_A, "scope_sha256": SHA_B,
                                                       "recorded_at": "2026-04-15T00:00:00Z", "effect_reference": "NONE"})
    obj("OBJ-V5-TIMEOUT-POLICY", "TimeoutPolicyReference", {"policy_id": "SYNTHETIC-TIMEOUT-POLICY-V5", "version": "1.0-SYNTHETIC",
                                                            "sha256": SHA_C, "start_category": "SYNTHETIC-START",
                                                            "deadline_duration": "PT30S", "late_result_policy": "DENY_USE",
                                                            "terminal_state": enum("ControlState", "QUARANTINED"), "retry_effect": "NONE"})
    control_args = {"version": "1.0-SYNTHETIC", "sha256": SHA_C, "trigger_reference": "SYNTHETIC-TRIGGER",
                    "authority_reference": "SYNTHETIC-REFERENCE-NOT-AUTHORITY", "propagation_boundary": "SYNTHETIC-BOUNDARY",
                    "response_target": "SYNTHETIC-RESPONSE-TARGET", "release_authority_required": True}
    obj("OBJ-V5-KILL", "RevocationOrKillReference", {"control_id": "SYNTHETIC-KILL-001", **control_args,
                                                     "effective_state": enum("ControlState", "KILLED"), "affected_scope": "SYNTHETIC-SCOPE-A"})
    obj("OBJ-V5-REVOCATION", "RevocationOrKillReference", {"control_id": "SYNTHETIC-REVOCATION-001", **control_args,
                                                           "effective_state": enum("ControlState", "REVOKED"), "affected_scope": "SYNTHETIC-SCOPE-A"})
    obj("OBJ-V5-ROLLBACK", "RollbackReference", {"rollback_id": "SYNTHETIC-ROLLBACK-V5", "version": "1.0-SYNTHETIC",
                                                 "current_identity": "SYNTHETIC_CURRENT", "target_identity": "SYNTHETIC_PRIOR",
                                                 "restoration_surface": tup("SYNTHETIC-IMPLEMENTATION-FILES"),
                                                 "preconditions": tup("SYNTHETIC-PRECONDITION"),
                                                 "prohibited_surface": tup("AUDIT_HISTORY", "ROUTE_A", "ACOS"),
                                                 "decision_reference": "SYNTHETIC-NO-DECISION",
                                                 "post_restore_state": enum("CapabilityState", "DISABLED")})
    obj("OBJ-V5-ROLLBACK-AUDIT-UNPROTECTED", "RollbackReference", {"rollback_id": "SYNTHETIC-ROLLBACK-V5B", "version": "1.0-SYNTHETIC",
                                                                   "current_identity": "SYNTHETIC_CURRENT", "target_identity": "SYNTHETIC_PRIOR",
                                                                   "restoration_surface": tup("SYNTHETIC-IMPLEMENTATION-FILES"),
                                                                   "preconditions": tup("SYNTHETIC-PRECONDITION"),
                                                                   "prohibited_surface": tup("ROUTE_A"),
                                                                   "decision_reference": "SYNTHETIC-NO-DECISION",
                                                                   "post_restore_state": enum("CapabilityState", "DISABLED")})
    obj("OBJ-V5-SUPERSESSION", "SupersessionReference", {"supersession_id": "SYNTHETIC-SUPERSESSION-001",
                                                         "superseded_identity": "SYNTHETIC_PRIOR", "replacement_identity": "SYNTHETIC_CURRENT",
                                                         "reason_reference": "SYNTHETIC-REASON", "stale_effect": "BLOCK_CURRENT_USE",
                                                         "history_preservation": "APPEND_ONLY"})
    audit_fields = {"correlation_id": "SYNTHETIC-CORRELATION-V5", "capability_reference": "SYNTHETIC-C03-CAPABILITY-REFERENCE",
                    "implementation_sha256": SHA_B, "configuration_sha256": "NONE", "domain_reference": "C03-SYNTHETIC",
                    "tier_b_packet_reference": "SYNTHETIC-PACKET-REFERENCE", "matter_reference": "SYNTHETIC-MATTER-001",
                    "actor_reference": "SYNTHETIC-ACTOR-001", "purpose": "SYNTHETIC-INTEGRITY-METADATA",
                    "operation": "SYNTHETIC-AUDIT-CHAIN", "prior_state": "UNCHECKED", "next_state": "QUARANTINED",
                    "reason_code": "INTEGRITY_CHECK", "decision_reference": "SYNTHETIC-REFERENCE-NOT-AUTHORITY",
                    "created_at": "SYNTHETIC-ORDER-MARKER", "redaction_state": "SYNTHETIC-REDACTED-METADATA"}
    a1 = {"audit_id": "SYNTHETIC-AUDIT-V5-001", **audit_fields, "input_artifact_references": tup(), "supersedes": "NONE"}
    a2 = {"audit_id": "SYNTHETIC-AUDIT-V5-002", **audit_fields, "input_artifact_references": tup(), "supersedes": "SYNTHETIC-AUDIT-V5-001"}
    obj("OBJ-V5-AUDIT-1", "AuditRecordCandidate", a1)
    obj("OBJ-V5-AUDIT-2", "AuditRecordCandidate", a2)
    obj("OBJ-V5-AUDIT-2-TAMPERED", "AuditRecordCandidate", {**a2, "reason_code": "INTEGRITY_CHECK_ALTERED"})
    plain = lambda a: {k: (v["tuple"] if isinstance(v, dict) and "tuple" in v else v) for k, v in a.items()}
    head = independent_chain_head([plain(a1), plain(a2)])

    rules = new["comparison_rule_catalog"]
    fx = {sc["scenario_id"]: sc for sc in d["scenarios"]}

    def mapping(sid, basis):
        o = fx[sid]["original_oracle"]
        return {"expected_state": o["expected_state"], "expected_reason_class": o["expected_reason_class"], "mapping_basis": basis}

    added = {}
    W0 = "2026-05-01T00:00:00Z"
    EV = "2026-06-01T00:00:00Z"
    idem = lambda prior, key="OBJ-V5-IDEM-KEY", sr=False, scope=SHA_B: {
        "key": ref(key), "prior_records": tup(*[ref(p) for p in prior]), "scope_sha256": scope, "evaluated_at": EV,
        "window_from": W0, "superseded_or_revoked": sr}
    rules["CR-V5-006-DUPLICATE-AFTER-EFFECT"] = cd_rule(["SB-006-V5-DUPLICATE-AFTER-EFFECT"], "PROTECTED_BLOCKED", "DUPLICATE DENIED — NO SECOND EFFECT",
                                                         mapping("C03-TA-V-006", "a duplicate after one permitted effect is denied; no second effect"))
    rules["CR-V5-006-FIRST-USE"] = cd_rule(["SB-006-V5-FIRST-USE"], "PROTECTED_BLOCKED", "FIRST USE — EXECUTION NOT AUTHORIZED")
    rules["CR-V5-006-COLLISION"] = cd_rule(["SB-006-V5-COLLISION"], "QUARANTINED", "QUARANTINED — IDEMPOTENCY COLLISION")
    rules["CR-V5-006-REPLAY"] = cd_rule(["SB-006-V5-REPLAY-OUTSIDE-WINDOW"], "PROTECTED_BLOCKED", "PROTECTED_BLOCKED — REPLAY FAILURE")
    rules["CR-V5-006-UNBOUND"] = cd_rule(["SB-006-V5-UNBOUND-DIGEST"], "PROTECTED_BLOCKED", "PROTECTED_BLOCKED — IDEMPOTENCY UNBOUND")
    added["C03-TA-V-006"] = [
        variant("SB-006-V5-DUPLICATE-AFTER-EFFECT", "ADP-EVALUATE-IDEMPOTENCY", idem(["OBJ-V5-IDEM-PRIOR-EFFECT"]), "CR-V5-006-DUPLICATE-AFTER-EFFECT", "V5_FIXTURE_MAPPED"),
        variant("SB-006-V5-FIRST-USE", "ADP-EVALUATE-IDEMPOTENCY", idem([]), "CR-V5-006-FIRST-USE", "V5_RAW_CHECK"),
        variant("SB-006-V5-COLLISION", "ADP-EVALUATE-IDEMPOTENCY", idem(["OBJ-V5-IDEM-PRIOR-OTHER-SCOPE"]), "CR-V5-006-COLLISION", "V5_RAW_CHECK"),
        variant("SB-006-V5-REPLAY-OUTSIDE-WINDOW", "ADP-EVALUATE-IDEMPOTENCY", idem(["OBJ-V5-IDEM-PRIOR-OLD"]), "CR-V5-006-REPLAY", "V5_RAW_CHECK"),
        variant("SB-006-V5-UNBOUND-DIGEST", "ADP-EVALUATE-IDEMPOTENCY", idem([], key="OBJ-V5-IDEM-KEY-UNBOUND"), "CR-V5-006-UNBOUND", "V5_RAW_CHECK")]

    tmo = lambda observed, result=None: {"policy": ref("OBJ-V5-TIMEOUT-POLICY"), "started_at": "2026-06-01T00:00:00Z",
                                          "deadline_at": "2026-06-01T00:00:30Z", "observed_at": observed, "result_received_at": result}
    rules["CR-V5-008-TIMEOUT"] = cd_rule(["SB-008-V5-TIMEOUT-REACHED"], "QUARANTINED", "QUARANTINED — INCOMPLETE",
                                         mapping("C03-TA-V-008", "deadline reached without a result enters the protected terminal state"))
    rules["CR-V5-008-LATE"] = cd_rule(["SB-008-V5-LATE-RESULT"], "QUARANTINED", "QUARANTINED — LATE RESULT DENIED",
                                      mapping("C03-TA-V-008", "a result at or after the deadline is denied use"))
    rules["CR-V5-008-PENDING"] = cd_rule(["SB-008-V5-DEADLINE-PENDING"], "PROTECTED_BLOCKED", "DEADLINE PENDING — NO RESULT")
    rules["CR-V5-008-UNBOUND"] = cd_rule(["SB-008-V5-RESULT-AFTER-OBSERVATION", "SB-008-V5-DEADLINE-NOT-POLICY"], "PROTECTED_BLOCKED", "PROTECTED_BLOCKED — TIMEOUT POLICY UNBOUND")
    added["C03-TA-V-008"] = [
        variant("SB-008-V5-TIMEOUT-REACHED", "ADP-EVALUATE-TIMEOUT", tmo("2026-06-01T00:00:31Z"), "CR-V5-008-TIMEOUT", "V5_FIXTURE_MAPPED"),
        variant("SB-008-V5-LATE-RESULT", "ADP-EVALUATE-TIMEOUT", tmo("2026-06-01T00:00:45Z", "2026-06-01T00:00:30Z"), "CR-V5-008-LATE", "V5_FIXTURE_MAPPED"),
        variant("SB-008-V5-DEADLINE-PENDING", "ADP-EVALUATE-TIMEOUT", tmo("2026-06-01T00:00:10Z"), "CR-V5-008-PENDING", "V5_RAW_CHECK"),
        variant("SB-008-V5-RESULT-AFTER-OBSERVATION", "ADP-EVALUATE-TIMEOUT", tmo("2026-06-01T00:00:10Z", "2026-06-01T00:00:20Z"), "CR-V5-008-UNBOUND", "V5_RAW_CHECK"),
        variant("SB-008-V5-DEADLINE-NOT-POLICY", "ADP-EVALUATE-TIMEOUT",
                {**tmo("2026-06-01T00:00:31Z"), "deadline_at": "2036-06-01T00:00:30Z"}, "CR-V5-008-UNBOUND", "V5_RAW_CHECK")]

    prec = lambda kill, rev, scope="SYNTHETIC-SCOPE-A", known=True: {
        "kill": ref(kill) if kill else None, "revocation": ref(rev) if rev else None, "control_state_known": known, "subject_scope": scope}
    rules["CR-V5-009-REVOKED"] = cd_rule(["SB-009-V5-REVOCATION-ACTIVE"], "REVOKED", "BLOCKED — REVOKED",
                                         mapping("C03-TA-V-009", "an active revocation for the subject scope blocks before any transition"))
    rules["CR-V5-009-OTHER-SCOPE"] = cd_rule(["SB-009-V5-OTHER-SCOPE"], "PROTECTED_BLOCKED", "PROTECTED_BLOCKED — NO ACTIVE CONTROL; EXECUTION NOT AUTHORIZED")
    rules["CR-V5-009-UNKNOWN"] = cd_rule(["SB-009-V5-STATE-UNKNOWN"], "PROTECTED_BLOCKED", "PROTECTED_BLOCKED — CONTROL STATE UNKNOWN")
    rules["CR-V5-009-WRONG-KIND"] = cd_rule(["SB-009-V5-REVOCATION-PASSED-AS-KILL"], "PROTECTED_BLOCKED", "PROTECTED_BLOCKED — STATE CONTRACT FAILURE")
    added["C03-TA-V-009"] = [
        variant("SB-009-V5-REVOCATION-ACTIVE", "ADP-CONTROL-PRECEDENCE", prec(None, "OBJ-V5-REVOCATION"), "CR-V5-009-REVOKED", "V5_FIXTURE_MAPPED"),
        variant("SB-009-V5-OTHER-SCOPE", "ADP-CONTROL-PRECEDENCE", prec(None, "OBJ-V5-REVOCATION", scope="SYNTHETIC-SCOPE-B"), "CR-V5-009-OTHER-SCOPE", "V5_RAW_CHECK"),
        variant("SB-009-V5-STATE-UNKNOWN", "ADP-CONTROL-PRECEDENCE", prec(None, None, known=None), "CR-V5-009-UNKNOWN", "V5_RAW_CHECK"),
        variant("SB-009-V5-REVOCATION-PASSED-AS-KILL", "ADP-CONTROL-PRECEDENCE", prec("OBJ-V5-REVOCATION", None), "CR-V5-009-WRONG-KIND", "V5_RAW_CHECK")]

    rules["CR-V5-010-KILL-FIRST"] = cd_rule(["SB-010-V5-KILL-PRECEDES-REVOCATION"], "KILLED", "BLOCKED — KILL ACTIVE",
                                            mapping("C03-TA-V-010", "kill takes priority over revocation for the subject scope"))
    rules["CR-V5-010-ROLLBACK-KILLED"] = cd_rule(["SB-010-V5-ROLLBACK-WHILE-KILLED"], "KILLED", "BLOCKED — KILL ACTIVE")
    rbk = lambda r="OBJ-V5-ROLLBACK", acc=("SYNTHETIC_PRIOR",), dec=False, kill=False: {  # kill may be None (unknown)
        "reference": ref(r), "accepted_prior_identities": tup(*acc), "decision_reference_valid": dec, "kill_active": kill, "revoked": False}
    added["C03-TA-V-010"] = [
        variant("SB-010-V5-KILL-PRECEDES-REVOCATION", "ADP-CONTROL-PRECEDENCE", prec("OBJ-V5-KILL", "OBJ-V5-REVOCATION"), "CR-V5-010-KILL-FIRST", "V5_FIXTURE_MAPPED"),
        variant("SB-010-V5-ROLLBACK-WHILE-KILLED", "ADP-EVALUATE-ROLLBACK", rbk(kill=True), "CR-V5-010-ROLLBACK-KILLED", "V5_RAW_CHECK")]

    rules["CR-V5-011-ELIGIBILITY"] = cd_rule(["SB-011-V5-NO-DECISION"], "ROLLBACK_PENDING", "ROLLBACK ELIGIBILITY ONLY — DECISION REQUIRED",
                                             mapping("C03-TA-V-011", "an exact accepted prior version without a decision is eligibility only"))
    rules["CR-V5-011-TARGET"] = cd_rule(["SB-011-V5-TARGET-NOT-ACCEPTED"], "PROTECTED_BLOCKED", "ROLLBACK BLOCKED — TARGET NOT AN ACCEPTED PRIOR VERSION")
    rules["CR-V5-011-AUDIT"] = cd_rule(["SB-011-V5-AUDIT-NOT-PROTECTED"], "PROTECTED_BLOCKED", "ROLLBACK BLOCKED — SURFACE NOT BOUNDED")
    rules["CR-V5-011-STALE"] = cd_rule(["SB-011-V5-SUPERSEDED-IDENTITY"], "STALE", "STALE — SUPERSEDED IDENTITY; NO FALLBACK")
    rules["CR-V5-011-KILL-UNKNOWN"] = cd_rule(["SB-011-V5-KILL-STATE-UNKNOWN"], "PROTECTED_BLOCKED", "PROTECTED_BLOCKED — CONTROL STATE UNKNOWN")
    added["C03-TA-V-011"] = [
        variant("SB-011-V5-NO-DECISION", "ADP-EVALUATE-ROLLBACK", rbk(), "CR-V5-011-ELIGIBILITY", "V5_FIXTURE_MAPPED"),
        variant("SB-011-V5-TARGET-NOT-ACCEPTED", "ADP-EVALUATE-ROLLBACK", rbk(acc=()), "CR-V5-011-TARGET", "V5_RAW_CHECK"),
        variant("SB-011-V5-AUDIT-NOT-PROTECTED", "ADP-EVALUATE-ROLLBACK", rbk(r="OBJ-V5-ROLLBACK-AUDIT-UNPROTECTED"), "CR-V5-011-AUDIT", "V5_RAW_CHECK"),
        variant("SB-011-V5-SUPERSEDED-IDENTITY", "ADP-EVALUATE-SUPERSESSION",
                {"identity": "SYNTHETIC_PRIOR", "supersessions": tup(ref("OBJ-V5-SUPERSESSION"))}, "CR-V5-011-STALE", "V5_RAW_CHECK"),
        variant("SB-011-V5-KILL-STATE-UNKNOWN", "ADP-EVALUATE-ROLLBACK", rbk(kill=None), "CR-V5-011-KILL-UNKNOWN", "V5_RAW_CHECK")]

    chain = lambda recs, h: {"records": tup(*[ref(r) for r in recs]), "expected_head_sha256": h}
    rules["CR-V5-012-MISMATCH"] = cd_rule(["SB-012-V5-CHAIN-HEAD-MISMATCH"], "QUARANTINED", "QUARANTINED — INTEGRITY FAILURE",
                                          mapping("C03-TA-V-012", "a deterministic head mismatch quarantines the audit reference path"))
    rules["CR-V5-012-REORDERED"] = cd_rule(["SB-012-V5-CHAIN-REORDERED", "SB-012-V5-FIELD-TAMPERED"], "QUARANTINED", "QUARANTINED — INTEGRITY FAILURE")
    rules["CR-V5-012-MATCHED"] = cd_rule(["SB-012-V5-CHAIN-MATCHED"], "PROTECTED_BLOCKED", "AUDIT CHAIN MATCHED — CANDIDATE ONLY; NOT PERSISTED",
                                         limitation=LIMITED_NOTE + "; the expected head is computed by the builder's independent re-implementation")
    rules["CR-V5-012-EMPTY"] = cd_rule(["SB-012-V5-CHAIN-EMPTY"], "PROTECTED_BLOCKED", "PROTECTED_BLOCKED — AUDIT CHAIN UNAVAILABLE")
    added["C03-TA-V-012"] = [
        variant("SB-012-V5-CHAIN-HEAD-MISMATCH", "ADP-VERIFY-AUDIT-CHAIN", chain(["OBJ-V5-AUDIT-1", "OBJ-V5-AUDIT-2"], "8" * 64), "CR-V5-012-MISMATCH", "V5_FIXTURE_MAPPED"),
        variant("SB-012-V5-CHAIN-REORDERED", "ADP-VERIFY-AUDIT-CHAIN", chain(["OBJ-V5-AUDIT-2", "OBJ-V5-AUDIT-1"], head), "CR-V5-012-REORDERED", "V5_RAW_CHECK"),
        variant("SB-012-V5-CHAIN-MATCHED", "ADP-VERIFY-AUDIT-CHAIN", chain(["OBJ-V5-AUDIT-1", "OBJ-V5-AUDIT-2"], head), "CR-V5-012-MATCHED", "V5_RAW_CHECK"),
        variant("SB-012-V5-CHAIN-EMPTY", "ADP-VERIFY-AUDIT-CHAIN", chain([], head), "CR-V5-012-EMPTY", "V5_RAW_CHECK"),
        variant("SB-012-V5-FIELD-TAMPERED", "ADP-VERIFY-AUDIT-CHAIN", chain(["OBJ-V5-AUDIT-1", "OBJ-V5-AUDIT-2-TAMPERED"], head), "CR-V5-012-REORDERED", "V5_RAW_CHECK")]

    dep = lambda req, auth, avail: {"requested_dependency": req, "authorized_dependencies": tup(*auth), "availability_state": avail}
    rules["CR-V5-013-UNAVAILABLE"] = cd_rule(["SB-013-V5-PROVIDER-UNAVAILABLE"], "PROTECTED_BLOCKED", "BLOCKED — DEPENDENCY OR PROVIDER UNAVAILABLE; NO SUBSTITUTION",
                                             mapping("C03-TA-V-013", "an unavailable authorized dependency blocks without substitution"))
    rules["CR-V5-013-NOT-AUTHORIZED"] = cd_rule(["SB-013-V5-NOT-AUTHORIZED"], "PROTECTED_BLOCKED", "BLOCKED — DEPENDENCY NOT AUTHORIZED")
    added["C03-TA-V-013"] = [
        variant("SB-013-V5-PROVIDER-UNAVAILABLE", "ADP-EVALUATE-DEPENDENCY", dep("NULL_PROVIDER", ["NULL_PROVIDER"], "UNAVAILABLE_SYNTHETIC"), "CR-V5-013-UNAVAILABLE", "V5_FIXTURE_MAPPED"),
        variant("SB-013-V5-NOT-AUTHORIZED", "ADP-EVALUATE-DEPENDENCY", dep("SYNTHETIC-OTHER-PROVIDER", ["NULL_PROVIDER"], "AVAILABLE"), "CR-V5-013-NOT-AUTHORIZED", "V5_RAW_CHECK")]

    upgraded = []
    for sc in new["scenarios"]:
        extra = added.get(sc["scenario_id"], [])
        sc["stimulus_variants"].extend(extra)
        if extra:
            sc["coverage_class_rev6"] = "PARTIAL_LIMITED"
            sc["coverage_rev6_rationale"] = LIMITED_NOTE
            upgraded.append(sc["scenario_id"])
    added_count = sum(len(v) for v in added.values())

    new["binding_id"] = "C03-WP008-AR-B-009-V5-INPUT-CANDIDATE-REV6"
    new["binding_version"] = "1.0"
    new["candidate_state"] = "DRAFTED_NOT_REVIEWED_NOT_ACCEPTED_NOT_ADMITTED"
    new["revision_rev6"] = {
        "derived_from": {"path": SRC, "sha256": SRC_SHA, "state": "ACCEPTED (V4-ACCEPT-IMPLEMENTATION)"},
        "authorization": ".codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_AR_B_009_WORK_AUTHORIZATION.md",
        "builder": "validation/route_b_c03/wp_008/ar_b_009_v5/build_input_rev6.py",
        "changes": ["subject hashes re-computed from the V5 sources (catalog source_sha256 refreshed for %d objects)" % refreshed,
                    "7 adapters for the WP-009 evaluators", "synthetic catalog objects for the evaluators",
                    "%d variants with %d new rules; 8 are fixture-mapped" % (added_count, len([r for r in rules if r.startswith("CR-V5-")])),
                    "coverage_class_rev6 = PARTIAL_LIMITED for " + ", ".join(upgraded)],
        "audit_chain_expected_head": head,
        "variant_count": sum(len(s["stimulus_variants"]) for s in new["scenarios"]),
        "runtime_version_of_record": "CPython 3.12.10 (P1-PYVER)"}
    data = (json.dumps(new, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    print(json.dumps({"variants": new["revision_rev6"]["variant_count"], "added": added_count, "bytes": len(data),
                      "sha256": hashlib.sha256(data).hexdigest().upper(), "head": head}))
    if "--write" in sys.argv:
        with open(OUT, "wb") as f:
            f.write(data)


if __name__ == "__main__":
    main()
