"""Build input candidate REV5 from the accepted input REV4 (prepared under the V4 limited revision authorization).

REV5 = REV4 with exactly these changes, all made here so the derivation can be reviewed:
  1. subject_identities and every adapter's subject_sha256 are re-hashed from the V4 source files;
  2. the identity gate gets the new required keyword evaluated_at; every gate variant passes
     2026-06-01T00:00:00Z; the base packet's validity window becomes 2025-01-01T00:00:00Z .. 2027-01-01T00:00:00Z;
  3. the base envelope carries one ready, validated synthetic artifact reference (OBJ-ARTIFACT-BASE);
  4. two adapters are added (ADP-CONSTRUCT-CONFIG, ADP-CAPABILITY-EVALUATE-GATE) and 12 variants with
     pre-declared rules that cover B1, B2, N1 and N2 of the security/privacy boundary review REV1.
The 28 REV4 variants and their rules are otherwise unchanged. New rules are raw checks without a fixture mapping.

Run from the repository root:  python3 -I validation/route_b_c03/wp_008/ar_b_007_v4/build_input_rev5.py [--write]
"""
import copy
import hashlib
import json
import sys

SRC = "validation/route_b_c03/wp_008/DSP_004_INPUT_CANDIDATE_REV4.json"
SRC_SHA = "685BBCBF13BF96746E6DE4201C1FCE72B667CD6A07D0CE0902D9EF9A6C4235C1"
OUT = "validation/route_b_c03/wp_008/ar_b_007_v4/C03_V4_INPUT_CANDIDATE_REV5.json"
EVAL_AT = "2026-06-01T00:00:00Z"
STATUS = "DRAFTED_REV5_NOT_ACCEPTED"
DERIVATION = "pre-declared from static reading of the V4 subject source before any harness run"
GATE_SURFACE = "GateDecision.state/reason_code/audit_correlation_id/permitted_write_namespaces"


def sha_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest().upper()


def gate_rule(applies, member, reason, limitation):
    return {"status": STATUS, "derivation": DERIVATION, "applies_to": applies, "observation_surface": GATE_SURFACE,
            "raw_requirement": {"type": "GateDecision", "state": {"enum_class": "InvocationState", "member": member},
                                "reason_code": reason, "audit_correlation_id": "SYNTHETIC-CORRELATION-001",
                                "permitted_write_namespaces": []},
            "fixture_mapping": None, "coverage_class": "SUPPLEMENTARY_RAW_CHECK", "limitation": limitation,
            "comparison_mode": "EXACT_NATIVE_TYPES_AND_VALUES; NO SEMANTIC NORMALIZATION, PREFIX MATCH OR REASON SUBSTITUTION",
            "mismatch_policy": "DO_NOT_ASSERT_CONFORMANCE; PRESERVE RAW OBSERVATION OR EXCEPTION; THE VARIANT IS FAIL",
            "post_hoc_change": "PROHIBITED"}


def exc_rule(applies, exc_type, message, limitation):
    return {"status": STATUS, "derivation": DERIVATION, "applies_to": applies, "observation_surface": "raised exception",
            "raw_requirement": {"exception_type": exc_type, "message": message},
            "fixture_mapping": None, "coverage_class": "SUPPLEMENTARY_RAW_CHECK", "limitation": limitation,
            "comparison_mode": "EXACT_EXCEPTION_TYPE_AND_MESSAGE",
            "mismatch_policy": "DO_NOT_ASSERT_CONFORMANCE; PRESERVE RAW OBSERVATION OR EXCEPTION; THE VARIANT IS FAIL",
            "post_hoc_change": "PROHIBITED"}


def gate_variant(sbid, rule, overrides=None, kill=False, evaluated_at=EVAL_AT, role=""):
    return {"stimulus_binding_id": sbid, "adapter_id": "ADP-EVALUATE-IDENTITY",
            "arguments": {"configuration": {"object_ref": "OBJ-CONFIG-BASE"}, "packet": {"object_ref": "OBJ-PACKET-BASE"},
                          "envelope": {"object_ref": "OBJ-ENVELOPE-BASE"}, "expected": {"object_ref": "OBJ-EXPECTED-BASE"},
                          "validity_confirmed": True, "kill_active": kill, "evaluated_at": evaluated_at},
            "object_overrides": overrides or {}, "selected_defaults": "ALL_DEFAULTS_EXPLICIT_IN_OBJECT_CATALOG_OR_ARGUMENTS",
            "observation_surface": GATE_SURFACE, "comparison_rule_id": rule, "variant_role": role or "V4_SUPPLEMENTARY_RAW_CHECK"}


def main():
    with open(SRC, "rb") as f:
        raw = f.read()
    if hashlib.sha256(raw).hexdigest().upper() != SRC_SHA:
        raise SystemExit("REV4_SHA_MISMATCH")
    d = json.loads(raw.decode("utf-8"))
    new = copy.deepcopy(d)

    # 1. re-hash the subject files
    subj = {p: sha_file(p) for p in d["subject_identities"]}
    new["subject_identities"] = subj
    for a in new["adapter_catalog"].values():
        a["subject_sha256"] = subj[a["subject_path"]]
    gate = new["adapter_catalog"]["ADP-EVALUATE-IDENTITY"]
    gate["keyword_only"] = ["expected", "validity_confirmed", "kill_active", "evaluated_at"]
    new["adapter_catalog"]["ADP-CONSTRUCT-CONFIG"] = {
        "subject_path": "scripts/phase2_runtime/route_b_c03/contracts.py", "subject_sha256": subj["scripts/phase2_runtime/route_b_c03/contracts.py"],
        "callable": "CapabilityConfigurationReference", "dispatch_state": "PROPOSED_FIXED_HARNESS_MAPPING_NOT_ACCEPTED"}
    new["adapter_catalog"]["ADP-CAPABILITY-EVALUATE-GATE"] = {
        "subject_path": "scripts/phase2_runtime/route_b_c03/capability.py", "subject_sha256": subj["scripts/phase2_runtime/route_b_c03/capability.py"],
        "callable": "C03Capability.evaluate_gate", "dispatch_state": "PROPOSED_FIXED_HARNESS_MAPPING_NOT_ACCEPTED",
        "instance": "C03Capability() with no configuration", "argument_order": ["envelope", "packet"],
        "keyword_only": ["expected_identity", "validity_confirmed", "kill_active", "evaluated_at"]}

    # 2. evaluated_at and validity window
    cat = new["synthetic_object_catalog"]
    cat["OBJ-PACKET-BASE"]["arguments"]["valid_from"] = "2025-01-01T00:00:00Z"
    cat["OBJ-PACKET-BASE"]["arguments"]["valid_until"] = "2027-01-01T00:00:00Z"
    for sc in new["scenarios"]:
        for v in sc["stimulus_variants"]:
            if v["adapter_id"] == "ADP-EVALUATE-IDENTITY":
                v["arguments"]["evaluated_at"] = EVAL_AT

    # 3. one ready artifact reference on the base envelope
    cat["OBJ-ARTIFACT-BASE"] = {"type": "ArtifactReference", "arguments": {
        "artifact_id": "SYNTHETIC-ARTIFACT-001", "artifact_type": "SYNTHETIC-METADATA-REFERENCE", "version": "1.0-SYNTHETIC",
        "sha256": "4444444444444444444444444444444444444444444444444444444444444444",
        "source_reference": "SYNTHETIC-SOURCE-REFERENCE-NO-PATH", "readiness_state": "READY", "validation_state": "VALIDATED",
        "human_review_reference": "SYNTHETIC-HUMAN-REVIEW-REFERENCE-NOT-AUTHORITY"}}
    cat["OBJ-ENVELOPE-BASE"]["arguments"]["input_artifact_references"] = {"tuple": [{"object_ref": "OBJ-ARTIFACT-BASE"}]}

    # 4. new rules and variants
    rules = new["comparison_rule_catalog"]
    cfg_args = dict(cat["OBJ-CONFIG-BASE"]["arguments"])
    audit_base = None
    for sc in d["scenarios"]:
        for v in sc["stimulus_variants"]:
            if v["stimulus_binding_id"] == "SB-012-AUDIT-CANDIDATE":
                audit_base = v["arguments"]
    added = {}

    rules["CR-V4-B1-STATE-NOT-ENUM"] = exc_rule(["SB-003-V4-RAW-STRING-STATE", "SB-003-V4-UNKNOWN-STATE"], "ValueError",
                                                "state must be a CapabilityState member", "construction-time type check (B1)")
    added["C03-TA-V-003"] = [
        {"stimulus_binding_id": "SB-003-V4-RAW-STRING-STATE", "adapter_id": "ADP-CONSTRUCT-CONFIG",
         "arguments": {**cfg_args, "state": "ENABLED_CAPABILITY_ONLY"}, "object_overrides": {},
         "comparison_rule_id": "CR-V4-B1-STATE-NOT-ENUM", "variant_role": "V4_B1_RAW_STRING_STATE"},
        {"stimulus_binding_id": "SB-003-V4-UNKNOWN-STATE", "adapter_id": "ADP-CONSTRUCT-CONFIG",
         "arguments": {**cfg_args, "state": "BOGUS"}, "object_overrides": {},
         "comparison_rule_id": "CR-V4-B1-STATE-NOT-ENUM", "variant_role": "V4_B1_UNKNOWN_STATE"}]

    rules["CR-V4-B2-KILL-REQUIRED"] = exc_rule(["SB-010-V4-KILL-NOT-SUPPLIED"], "TypeError",
                                               "C03Capability.evaluate_gate() missing 1 required keyword-only argument: 'kill_active'",
                                               "the facade has no default kill state (B2); message text as raised by CPython 3.12")
    rules["CR-V4-B2-KILL-NOT-FALSE"] = gate_rule(["SB-010-V4-KILL-NULL", "SB-010-V4-KILL-ZERO"], "BLOCKED", "BLOCKED — KILL ACTIVE",
                                                 "only an exact False counts as not killed (B2)")
    added["C03-TA-V-010"] = [
        {"stimulus_binding_id": "SB-010-V4-KILL-NOT-SUPPLIED", "adapter_id": "ADP-CAPABILITY-EVALUATE-GATE",
         "arguments": {"envelope": {"object_ref": "OBJ-ENVELOPE-BASE"}, "packet": {"object_ref": "OBJ-PACKET-BASE"},
                       "expected_identity": {"object_ref": "OBJ-EXPECTED-BASE"}, "validity_confirmed": True, "evaluated_at": EVAL_AT},
         "object_overrides": {}, "comparison_rule_id": "CR-V4-B2-KILL-REQUIRED", "variant_role": "V4_B2_KILL_OMITTED"},
        gate_variant("SB-010-V4-KILL-NULL", "CR-V4-B2-KILL-NOT-FALSE", kill=None, role="V4_B2_KILL_NULL"),
        gate_variant("SB-010-V4-KILL-ZERO", "CR-V4-B2-KILL-NOT-FALSE", kill=0, role="V4_B2_KILL_ZERO")]

    rules["CR-V4-N2-OUTSIDE-WINDOW"] = gate_rule(["SB-002-V4-PACKET-EXPIRED", "SB-002-V4-PACKET-NOT-YET-VALID"], "BLOCKED",
                                                 "BLOCKED — AUTHORITY FAILURE", "validity window checked against caller-supplied evaluated_at (N2)")
    added["C03-TA-V-002"] = [
        gate_variant("SB-002-V4-PACKET-EXPIRED", "CR-V4-N2-OUTSIDE-WINDOW", evaluated_at="2027-01-01T00:00:00Z", role="V4_N2_EXPIRED"),
        gate_variant("SB-002-V4-PACKET-NOT-YET-VALID", "CR-V4-N2-OUTSIDE-WINDOW", evaluated_at="2024-12-31T23:59:59Z", role="V4_N2_NOT_YET_VALID")]

    rules["CR-V4-N2-READINESS"] = gate_rule(["SB-001-V4-ARTIFACT-NOT-READY", "SB-001-V4-NO-ARTIFACTS"], "BLOCKED",
                                            "BLOCKED — READINESS/PROVENANCE FAILURE", "reference metadata only; readiness values are caller-supplied (N2)")
    added["C03-TA-V-001"] = [
        gate_variant("SB-001-V4-ARTIFACT-NOT-READY", "CR-V4-N2-READINESS",
                     overrides={"/OBJ-ARTIFACT-BASE/arguments/readiness_state": "PENDING"}, role="V4_N2_ARTIFACT_NOT_READY"),
        gate_variant("SB-001-V4-NO-ARTIFACTS", "CR-V4-N2-READINESS",
                     overrides={"/OBJ-ENVELOPE-BASE/arguments/input_artifact_references": {"tuple": []}}, role="V4_N2_NO_ARTIFACTS")]

    rules["CR-V4-N1-REDACTION"] = exc_rule(["SB-012-V4-AUDIT-ID-NUMBER", "SB-012-V4-AUDIT-API-KEY"], "ValueError",
                                           "QUARANTINED — AUDIT REDACTION FAILURE", "pattern screen on synthetic values only (N1)")
    rules["CR-V4-N1-REQUIRED-FIELD"] = exc_rule(["SB-012-V4-AUDIT-EMPTY-MATTER"], "ValueError",
                                                "matter_reference must be a non-empty explicit value", "required-field check (N1)")
    added["C03-TA-V-012"] = [
        {"stimulus_binding_id": "SB-012-V4-AUDIT-ID-NUMBER", "adapter_id": "ADP-BUILD-AUDIT-CANDIDATE",
         "arguments": {**audit_base, "actor_reference": "SYNTHETIC-ACTOR 110101199001011234"}, "object_overrides": {},
         "comparison_rule_id": "CR-V4-N1-REDACTION", "variant_role": "V4_N1_ID_NUMBER"},
        {"stimulus_binding_id": "SB-012-V4-AUDIT-API-KEY", "adapter_id": "ADP-BUILD-AUDIT-CANDIDATE",
         "arguments": {**audit_base, "actor_reference": "SYNTHETIC-ACTOR api_key=sk-SYNTHETIC"}, "object_overrides": {},
         "comparison_rule_id": "CR-V4-N1-REDACTION", "variant_role": "V4_N1_API_KEY"},
        {"stimulus_binding_id": "SB-012-V4-AUDIT-EMPTY-MATTER", "adapter_id": "ADP-BUILD-AUDIT-CANDIDATE",
         "arguments": {**audit_base, "matter_reference": ""}, "object_overrides": {},
         "comparison_rule_id": "CR-V4-N1-REQUIRED-FIELD", "variant_role": "V4_N1_EMPTY_MATTER"}]

    for sc in new["scenarios"]:
        for v in added.get(sc["scenario_id"], []):
            v.setdefault("selected_defaults", "ALL_DEFAULTS_EXPLICIT_IN_OBJECT_CATALOG_OR_ARGUMENTS")
            sc["stimulus_variants"].append(v)

    new["binding_id"] = "C03-WP008-AR-B-007-V4-INPUT-CANDIDATE-REV5"
    new["binding_version"] = "0.9"
    new["candidate_state"] = "DRAFTED_NOT_REVIEWED_NOT_ACCEPTED_NOT_ADMITTED"
    new["revision_rev5"] = {
        "derived_from": {"path": SRC, "sha256": SRC_SHA, "state": "ACCEPTED (DSP-004 phase 4)"},
        "authorization": ".codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_WP_007_V4_LIMITED_REVISION_AUTHORIZATION.md",
        "builder": "validation/route_b_c03/wp_008/ar_b_007_v4/build_input_rev5.py",
        "changes": ["subject hashes re-computed from the V4 sources", "gate keyword evaluated_at added to all gate variants",
                    "base packet validity window set to UTC timestamps", "base envelope carries one READY/VALIDATED artifact reference",
                    "adapters ADP-CONSTRUCT-CONFIG and ADP-CAPABILITY-EVALUATE-GATE added",
                    "12 supplementary raw-check variants with 7 new rules (B1, B2, N1, N2)"],
        "variant_count": sum(len(s["stimulus_variants"]) for s in new["scenarios"]),
        "runtime_version_of_record": "CPython 3.12.10 (P1-PYVER)"}
    text = json.dumps(new, ensure_ascii=False, indent=1) + "\n"
    data = text.encode("utf-8")
    print(json.dumps({"variants": new["revision_rev5"]["variant_count"], "bytes": len(data),
                      "sha256": hashlib.sha256(data).hexdigest().upper()}))
    if "--write" in sys.argv:
        with open(OUT, "wb") as f:
            f.write(data)


if __name__ == "__main__":
    main()
