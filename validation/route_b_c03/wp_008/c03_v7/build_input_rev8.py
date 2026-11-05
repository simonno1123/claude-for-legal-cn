"""Build input candidate REV8 from the accepted input REV7 (prepared under owner decision AR-B-008-V7-FIRST,
which chose to close the capability-layer test gaps and wire the control check into capability.py before deciding
AR-B-008; not accepted).

REV8 = REV7 with exactly these changes, all made here so the derivation can be reviewed:
  1. subject_identities, adapter subject hashes and catalog source_sha256 values are re-hashed from the V7 sources;
  2. adapters ADP-EVALUATE-INTEGRITY (failures.evaluate_integrity) and ADP-CAPABILITY-EVALUATE-TRANSITION
     (C03Capability.evaluate_transition on a default C03Capability()) are added;
  3. one catalog object OBJ-V7-AUDIT-2-FORK (OBJ-V5-AUDIT-2 with another audit_id) is added;
  4. variants with pre-declared rules are added: V-003 stale authority reference (1), V-005 nested and value
     screening (4), V-012 duplicate, fork and integrity comparison (7), V-009/V-010 transition check (3), V-001
     transition with no active control (1), V-015 accepted-fact label (1); none carries a fixture mapping, so no
     coverage class changes.
The 76 REV7 variants and their rules are otherwise unchanged.

Run from the repository root:  python3 -I validation/route_b_c03/wp_008/c03_v7/build_input_rev8.py [--write]
"""
import copy
import hashlib
import json
import sys

SRC = "validation/route_b_c03/wp_008/c03_v6/C03_V6_INPUT_CANDIDATE_REV7.json"
SRC_SHA = "3E01C1961BC435608A7907A35C6E0C013E26312011A6D68983E44E24FEB76E2F"
OUT = "validation/route_b_c03/wp_008/c03_v7/C03_V7_INPUT_CANDIDATE_REV8.json"
FAILURES = "scripts/phase2_runtime/route_b_c03/failures.py"
CAPABILITY = "scripts/phase2_runtime/route_b_c03/capability.py"
STATUS = "DRAFTED_REV8_NOT_ACCEPTED"
DERIVATION = "pre-declared from static reading of the V7 subject source before any harness run"
CHAIN_HEAD = "D446CDB52078BB75ACFEB4549DF7379399AC0774997561E30D187CF0A442F1C4"
SHA_A = "A" * 64
SHA_B = "B" * 64
DEFAULTS = "ALL_DEFAULTS_EXPLICIT_IN_OBJECT_CATALOG_OR_ARGUMENTS"


def sha_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest().upper()


def enum(cls, member):
    return {"enum_class": cls, "member": member}


def ref(name):
    return {"object_ref": name}


def rule(applies, surface, requirement, limitation, mode="EXACT_NATIVE_TYPES_AND_VALUES; NO SEMANTIC NORMALIZATION"):
    return {"status": STATUS, "derivation": DERIVATION, "applies_to": [applies], "observation_surface": surface,
            "raw_requirement": requirement, "fixture_mapping": None, "coverage_class": "SUPPLEMENTARY_RAW_CHECK",
            "limitation": limitation, "comparison_mode": mode,
            "mismatch_policy": "DO_NOT_ASSERT_CONFORMANCE; PRESERVE RAW OBSERVATION OR EXCEPTION; THE VARIANT IS FAIL",
            "post_hoc_change": "PROHIBITED"}


def control(state, reason):
    return {"type": "ControlDetermination", "state": enum("ControlState", state), "reason_code": reason}


def transition(reason, gate_none=True):
    req = {"type": "TransitionDetermination", "state": enum("InvocationState", "BLOCKED"), "reason_code": reason,
           "execution_authorized": False}
    if gate_none:
        req["gate"] = None
    return req


def variant(sbid, adapter, arguments, rule_id, surface, overrides=None):
    return {"stimulus_binding_id": sbid, "adapter_id": adapter, "arguments": arguments,
            "object_overrides": overrides or {}, "selected_defaults": DEFAULTS, "observation_surface": surface,
            "comparison_rule_id": rule_id, "variant_role": "V7_RAW_CHECK"}


def main():
    with open(SRC, "rb") as f:
        raw = f.read()
    if hashlib.sha256(raw).hexdigest().upper() != SRC_SHA:
        raise SystemExit("REV7_SHA_MISMATCH")
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
    cat = new["adapter_catalog"]
    cat["ADP-EVALUATE-INTEGRITY"] = {
        "subject_path": FAILURES, "subject_sha256": subj[FAILURES], "callable": "evaluate_integrity",
        "dispatch_state": "PROPOSED_FIXED_HARNESS_MAPPING_NOT_ACCEPTED", "argument_order": ["subject_kind"],
        "keyword_only": ["expected_sha256", "observed_sha256"]}
    cat["ADP-CAPABILITY-EVALUATE-TRANSITION"] = {
        "subject_path": CAPABILITY, "subject_sha256": subj[CAPABILITY], "callable": "C03Capability.evaluate_transition",
        "dispatch_state": "PROPOSED_FIXED_HARNESS_MAPPING_NOT_ACCEPTED; METHOD ON DEFAULT C03Capability()",
        "argument_order": ["envelope", "packet"],
        "keyword_only": ["expected_identity", "validity_confirmed", "evaluated_at", "kill", "revocation",
                         "control_state_known", "subject_scope"]}

    objects = new["synthetic_object_catalog"]
    fork = copy.deepcopy(objects["OBJ-V5-AUDIT-2"])
    fork["arguments"]["audit_id"] = "SYNTHETIC-AUDIT-V7-002-FORK"
    objects["OBJ-V7-AUDIT-2-FORK"] = fork

    rules = new["comparison_rule_catalog"]
    by_id = {s["scenario_id"]: s for s in new["scenarios"]}
    added = {}

    def add(scenario, sbid, adapter, arguments, rule_id, surface, requirement, limitation, overrides=None):
        rules[rule_id] = rule(sbid, surface, requirement, limitation)
        by_id[scenario]["stimulus_variants"].append(variant(sbid, adapter, arguments, rule_id, surface, overrides))
        added[scenario] = added.get(scenario, 0) + 1

    gate_args = {"configuration": ref("OBJ-CONFIG-BASE"), "packet": ref("OBJ-PACKET-BASE"),
                 "envelope": ref("OBJ-ENVELOPE-BASE"), "expected": ref("OBJ-EXPECTED-BASE"),
                 "validity_confirmed": True, "kill_active": False, "evaluated_at": "2026-06-01T00:00:00Z"}
    add("C03-TA-V-003", "SB-003-V7-AUTHORITY-REFERENCE", "ADP-EVALUATE-IDENTITY", gate_args, "CR-V7-003-AUTHORITY-REFERENCE",
        "GateDecision.state/reason_code/audit_correlation_id/permitted_write_namespaces",
        {"type": "GateDecision", "state": enum("InvocationState", "BLOCKED"),
         "reason_code": "BLOCKED — CAPABILITY IDENTITY FAILURE", "audit_correlation_id": "SYNTHETIC-CORRELATION-001",
         "permitted_write_namespaces": []},
        "a stale activation-decision (authority) reference in the configuration; chronology is not modelled",
        {"/OBJ-CONFIG-BASE/arguments/activation_decision_reference": "SYNTHETIC-ACTIVATION-REFERENCE-SUPERSEDED"})

    exc = "IsolationViolation exception identity/message"
    for sbid, record, message in (
        ("SB-005-V7-NESTED-KEY", {"metadata": {"api_token_reference": "SYNTHETIC-REF-1"}},
         "QUARANTINED — CONTENT FIELD PROHIBITED: api_token_reference"),
        ("SB-005-V7-VALUE-HEADER", {"note": "Authorization: Bearer SYNTHETIC-NOT-A-TOKEN"},
         "QUARANTINED — SECRET MARKER IN VALUE"),
        ("SB-005-V7-VALUE-IN-LIST", {"references": ["SYNTHETIC-REF-1", "-----BEGIN SYNTHETIC KEY-----"]},
         "QUARANTINED — SECRET MARKER IN VALUE"),
    ):
        add("C03-TA-V-005", sbid, "ADP-ASSERT-REFERENCE-ONLY", {"record": record}, "CR-V7-005-" + sbid[10:], exc,
            {"exception_type": "IsolationViolation", "message": message},
            "fixed marker list over str values and field names at every nesting level; not a general secret detector")
    add("C03-TA-V-005", "SB-005-V7-CLEAN-NESTED", "ADP-ASSERT-REFERENCE-ONLY",
        {"record": {"references": ["SYNTHETIC-REF-1", {"id": "SYNTHETIC-REF-2"}], "count": 2}},
        "CR-V7-005-CLEAN-NESTED", "return value", {"type": "None"},
        "control: a clean nested reference record is accepted (returns None)")

    cd = "ControlDetermination.state/reason_code"
    chain = "ADP-VERIFY-AUDIT-CHAIN"
    add("C03-TA-V-012", "SB-012-V7-CHAIN-DUPLICATE", chain,
        {"records": {"tuple": [ref("OBJ-V5-AUDIT-1"), ref("OBJ-V5-AUDIT-1")]}, "expected_head_sha256": CHAIN_HEAD},
        "CR-V7-012-CHAIN-DUPLICATE", cd, control("QUARANTINED", "QUARANTINED — INTEGRITY FAILURE"),
        "duplicate audit_id in caller-supplied candidates; nothing is persisted")
    add("C03-TA-V-012", "SB-012-V7-CHAIN-FORK", chain,
        {"records": {"tuple": [ref("OBJ-V5-AUDIT-1"), ref("OBJ-V5-AUDIT-2"), ref("OBJ-V7-AUDIT-2-FORK")]},
         "expected_head_sha256": CHAIN_HEAD},
        "CR-V7-012-CHAIN-FORK", cd, control("QUARANTINED", "QUARANTINED — INTEGRITY FAILURE"),
        "a second record superseding the same predecessor; nothing is persisted")
    integ = "ADP-EVALUATE-INTEGRITY"
    for sbid, kind, observed, state, reason in (
        ("SB-012-V7-OUTPUT-HASH-TAMPER", "OUTPUT", SHA_B, "QUARANTINED", "QUARANTINED — INTEGRITY FAILURE: OUTPUT"),
        ("SB-012-V7-DEPENDENCY-TAMPER", "DEPENDENCY", SHA_B, "QUARANTINED", "QUARANTINED — INTEGRITY FAILURE: DEPENDENCY"),
        ("SB-012-V7-INTEGRITY-MATCHED", "OUTPUT", SHA_A.lower(), "PROTECTED_BLOCKED", "INTEGRITY MATCHED — EXECUTION NOT AUTHORIZED"),
        ("SB-012-V7-INTEGRITY-UNKNOWN-KIND", "OUTPUT_FILE", SHA_A, "PROTECTED_BLOCKED", "PROTECTED_BLOCKED — INTEGRITY REFERENCE UNBOUND"),
        ("SB-012-V7-OBSERVATION-MISSING", "DEPENDENCY", None, "QUARANTINED", "QUARANTINED — INTEGRITY UNCERTAIN: DEPENDENCY"),
    ):
        add("C03-TA-V-012", sbid, integ, {"subject_kind": kind, "expected_sha256": SHA_A, "observed_sha256": observed},
            "CR-V7-012-" + sbid[10:], cd, control(state, reason),
            "comparison of caller-supplied hashes; no output or dependency is read or hashed by the subject")

    tr_args = {"envelope": ref("OBJ-ENVELOPE-BASE"), "packet": ref("OBJ-PACKET-BASE"),
               "expected_identity": ref("OBJ-EXPECTED-BASE"), "validity_confirmed": True,
               "evaluated_at": "2026-06-01T00:00:00Z", "kill": None, "revocation": None,
               "control_state_known": True, "subject_scope": "SYNTHETIC-SCOPE-A"}
    tr = "ADP-CAPABILITY-EVALUATE-TRANSITION"
    ts = "TransitionDetermination.state/reason_code/gate/execution_authorized"
    lim = "default C03Capability() (no configuration); controls and gate order only; nothing executes"
    add("C03-TA-V-010", "SB-010-V7-TRANSITION-KILL", tr,
        {**tr_args, "kill": ref("OBJ-V5-KILL"), "revocation": ref("OBJ-V5-REVOCATION")},
        "CR-V7-010-TRANSITION-KILL", ts, transition("BLOCKED — KILL ACTIVE"), lim)
    add("C03-TA-V-010", "SB-010-V7-TRANSITION-UNKNOWN", tr, {**tr_args, "control_state_known": False},
        "CR-V7-010-TRANSITION-UNKNOWN", ts, transition("PROTECTED_BLOCKED — CONTROL STATE UNKNOWN"), lim)
    add("C03-TA-V-009", "SB-009-V7-TRANSITION-REVOKED", tr, {**tr_args, "revocation": ref("OBJ-V5-REVOCATION")},
        "CR-V7-009-TRANSITION-REVOKED", ts, transition("BLOCKED — REVOKED"), lim)
    add("C03-TA-V-001", "SB-001-V7-TRANSITION-NO-CONTROL", tr, tr_args, "CR-V7-001-TRANSITION-NO-CONTROL", ts,
        transition("BLOCKED — CAPABILITY NOT ACTIVE", gate_none=False),
        lim + "; with no active control the identity gate is reached and blocks the unconfigured capability")

    add("C03-TA-V-015", "SB-015-V7-ACCEPTED-FACT", "ADP-EVALUATE-CLASSIFICATION",
        {"requested_class": "ACCEPTED_FACT", "human_disposition": None}, "CR-V7-015-ACCEPTED-FACT",
        "ClassificationDetermination.request_state/candidate_state/downstream_blocked/reason_code",
        {"type": "ClassificationDetermination", "request_state": enum("InvocationState", "REJECTED"),
         "candidate_state": enum("InvocationState", "HUMAN_REVIEW_PENDING"), "downstream_blocked": True,
         "reason_code": "REJECTED — OUTPUT BOUNDARY FAILURE: CLASS NOT PERMITTED"},
        "the plan's accepted-fact label; rejected as a non-member, not as a named prohibited class")

    new["binding_id"] = "C03-WP008-V7-INPUT-CANDIDATE-REV8"
    new["binding_version"] = "1.2"
    new["candidate_state"] = "DRAFTED_NOT_REVIEWED_NOT_ACCEPTED_NOT_ADMITTED"
    new["revision_rev8"] = {
        "derived_from": {"path": SRC, "sha256": SRC_SHA, "state": "ACCEPTED (V6-ACCEPT-IMPLEMENTATION)"},
        "authorization": ".codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_AR_B_008_V7_FIRST_DECISION.json",
        "builder": "validation/route_b_c03/wp_008/c03_v7/build_input_rev8.py",
        "changes": ["subject hashes re-computed from the V7 sources (catalog source_sha256 refreshed for %d objects)" % refreshed,
                    "adapters ADP-EVALUATE-INTEGRITY and ADP-CAPABILITY-EVALUATE-TRANSITION",
                    "catalog object OBJ-V7-AUDIT-2-FORK",
                    "%d raw-check variants with their rules: %s" % (sum(added.values()), json.dumps(added, sort_keys=True)),
                    "no coverage class changes"],
        "variant_count": sum(len(s["stimulus_variants"]) for s in new["scenarios"]),
        "runtime_version_of_record": "CPython 3.12.10 (P1-PYVER)"}
    data = (json.dumps(new, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    print(json.dumps({"variants": new["revision_rev8"]["variant_count"], "added": added, "bytes": len(data),
                      "sha256": hashlib.sha256(data).hexdigest().upper()}))
    if "--write" in sys.argv:
        with open(OUT, "wb") as f:
            f.write(data)


if __name__ == "__main__":
    main()
