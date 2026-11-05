"""Build input candidate REV7 from the accepted input REV6 (prepared under owner decision AR-B-008-KEEP-OPEN, which
chose to close the V-015 classification gap next; not accepted).

REV7 = REV6 with exactly these changes, all made here so the derivation can be reviewed:
  1. subject_identities, adapter subject hashes and catalog source_sha256 values are re-hashed from the V6 sources;
  2. adapter ADP-EVALUATE-CLASSIFICATION (isolation.evaluate_classification_request) is added;
  3. six variants with pre-declared rules are added to scenario V-015; one carries a fixture mapping to the V-015
     oracle (the fixture's own request LEGAL_ADVICE_OR_DOWNSTREAM_AUTHORITY);
  4. V-015 gets coverage_class_rev7 = FULL: the fixture's prohibited request is now evaluated by a closed
     evaluator and the candidate constructor refuses any class that is not an exact permitted member.
The 70 REV6 variants and their rules are otherwise unchanged.

Run from the repository root:  python3 -I validation/route_b_c03/wp_008/c03_v6/build_input_rev7.py [--write]
"""
import copy
import hashlib
import json
import sys

SRC = "validation/route_b_c03/wp_008/ar_b_009_v5/C03_V5_INPUT_CANDIDATE_REV6.json"
SRC_SHA = "418AD1EE9144C28E93DF571FD829C660E6B8EDA4DD06B3B16CDEEC1AAF1BE9C0"
OUT = "validation/route_b_c03/wp_008/c03_v6/C03_V6_INPUT_CANDIDATE_REV7.json"
ISOLATION = "scripts/phase2_runtime/route_b_c03/isolation.py"
STATUS = "DRAFTED_REV7_NOT_ACCEPTED"
DERIVATION = "pre-declared from static reading of the V6 subject source before any harness run"
APPROVE = "APPROVE A SPECIFIC CANDIDATE FOR A SEPARATELY AUTHORIZED NEXT STEP"


def sha_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest().upper()


def enum(cls, member):
    return {"enum_class": cls, "member": member}


def cls_rule(applies, request_member, reason, mapping=None):
    return {"status": STATUS, "derivation": DERIVATION, "applies_to": applies,
            "observation_surface": "ClassificationDetermination.request_state/candidate_state/downstream_blocked/reason_code",
            "raw_requirement": {"type": "ClassificationDetermination", "request_state": enum("InvocationState", request_member),
                                "candidate_state": enum("InvocationState", "HUMAN_REVIEW_PENDING"), "downstream_blocked": True,
                                "reason_code": reason},
            "fixture_mapping": mapping, "coverage_class": "FULL" if mapping else "SUPPLEMENTARY_RAW_CHECK",
            "limitation": "classification of a caller-supplied class label; no legal reasoning is performed or judged",
            "comparison_mode": "EXACT_NATIVE_TYPES_AND_VALUES; NO SEMANTIC NORMALIZATION, PREFIX MATCH OR REASON SUBSTITUTION",
            "mismatch_policy": "DO_NOT_ASSERT_CONFORMANCE; PRESERVE RAW OBSERVATION OR EXCEPTION; THE VARIANT IS FAIL",
            "post_hoc_change": "PROHIBITED"}


def cls_variant(sbid, requested, disposition, rule, role):
    return {"stimulus_binding_id": sbid, "adapter_id": "ADP-EVALUATE-CLASSIFICATION",
            "arguments": {"requested_class": requested, "human_disposition": disposition}, "object_overrides": {},
            "selected_defaults": "ALL_DEFAULTS_EXPLICIT_IN_OBJECT_CATALOG_OR_ARGUMENTS",
            "observation_surface": "ClassificationDetermination", "comparison_rule_id": rule, "variant_role": role}


def main():
    with open(SRC, "rb") as f:
        raw = f.read()
    if hashlib.sha256(raw).hexdigest().upper() != SRC_SHA:
        raise SystemExit("REV6_SHA_MISMATCH")
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
    new["adapter_catalog"]["ADP-EVALUATE-CLASSIFICATION"] = {
        "subject_path": ISOLATION, "subject_sha256": subj[ISOLATION], "callable": "evaluate_classification_request",
        "dispatch_state": "PROPOSED_FIXED_HARNESS_MAPPING_NOT_ACCEPTED", "argument_order": ["requested_class"],
        "keyword_only": ["human_disposition"]}

    sc = [s for s in new["scenarios"] if s["scenario_id"] == "C03-TA-V-015"][0]
    oracle = sc["original_oracle"]
    base_candidate = sc["stimulus_variants"][0]["arguments"]
    rules = new["comparison_rule_catalog"]
    rules["CR-V6-015-LEGAL-ADVICE"] = cls_rule(["SB-015-V6-LEGAL-ADVICE-REQUEST"], "REJECTED", "REJECTED — OUTPUT BOUNDARY FAILURE: CLASS NOT PERMITTED",
                                               {"expected_state": oracle["expected_state"], "expected_reason_class": oracle["expected_reason_class"],
                                                "mapping_basis": "the request is rejected; the candidate stays HUMAN_REVIEW_PENDING and downstream use stays blocked"})
    rules["CR-V6-015-PROHIBITED"] = cls_rule(["SB-015-V6-PROHIBITED-CLASS"], "REJECTED", "REJECTED — OUTPUT BOUNDARY FAILURE: PROHIBITED CLASS")
    rules["CR-V6-015-RAW-STRING"] = cls_rule(["SB-015-V6-RAW-STRING-CLASS"], "REJECTED", "REJECTED — OUTPUT BOUNDARY FAILURE: CLASS NOT PERMITTED")
    rules["CR-V6-015-PERMITTED"] = cls_rule(["SB-015-V6-PERMITTED-CLASS"], "HUMAN_REVIEW_PENDING", "CANDIDATE CLASS PERMITTED — HUMAN REVIEW PENDING; DOWNSTREAM BLOCKED")
    rules["CR-V6-015-APPROVED"] = cls_rule(["SB-015-V6-APPROVED-STILL-BLOCKED"], "HUMAN_REVIEW_PENDING", "APPROVED FOR A SEPARATE NEXT STEP ONLY — DOWNSTREAM STILL BLOCKED")
    rules["CR-V6-015-CANDIDATE-CLASS"] = {
        "status": STATUS, "derivation": DERIVATION, "applies_to": ["SB-015-V6-CANDIDATE-PROHIBITED-CLASS"],
        "observation_surface": "raised exception", "raw_requirement": {"exception_type": "ValueError", "message": "candidate_class must be a CandidateClass member"},
        "fixture_mapping": None, "coverage_class": "SUPPLEMENTARY_RAW_CHECK", "limitation": "construction-time type check",
        "comparison_mode": "EXACT_EXCEPTION_TYPE_AND_MESSAGE", "mismatch_policy": "DO_NOT_ASSERT_CONFORMANCE; THE VARIANT IS FAIL", "post_hoc_change": "PROHIBITED"}
    sc["stimulus_variants"].extend([
        cls_variant("SB-015-V6-LEGAL-ADVICE-REQUEST", sc["original_fixture_input_state"]["candidate_classification_request"],
                    None, "CR-V6-015-LEGAL-ADVICE", "V6_FIXTURE_MAPPED"),
        cls_variant("SB-015-V6-PROHIBITED-CLASS", "FINAL_LEGAL_OPINION", None, "CR-V6-015-PROHIBITED", "V6_RAW_CHECK"),
        cls_variant("SB-015-V6-RAW-STRING-CLASS", "C03_ISSUE_MATRIX_CANDIDATE", None, "CR-V6-015-RAW-STRING", "V6_RAW_CHECK"),
        cls_variant("SB-015-V6-PERMITTED-CLASS", enum("CandidateClass", "ISSUE_MATRIX"), None, "CR-V6-015-PERMITTED", "V6_RAW_CHECK"),
        cls_variant("SB-015-V6-APPROVED-STILL-BLOCKED", enum("CandidateClass", "ISSUE_MATRIX"), APPROVE, "CR-V6-015-APPROVED", "V6_RAW_CHECK"),
        {"stimulus_binding_id": "SB-015-V6-CANDIDATE-PROHIBITED-CLASS", "adapter_id": "ADP-CONSTRUCT-CANDIDATE",
         "arguments": {**base_candidate, "candidate_class": "FINAL_LEGAL_OPINION"}, "object_overrides": {},
         "selected_defaults": "ALL_DEFAULTS_EXPLICIT_IN_OBJECT_CATALOG_OR_ARGUMENTS", "observation_surface": "raised exception",
         "comparison_rule_id": "CR-V6-015-CANDIDATE-CLASS", "variant_role": "V6_RAW_CHECK"}])
    sc["coverage_class_rev7"] = "FULL"
    sc["coverage_rev7_rationale"] = ("the fixture's prohibited classification request is evaluated by a closed evaluator (request rejected, "
                                     "candidate HUMAN_REVIEW_PENDING, downstream blocked) and CandidateRecord refuses any non-member class")

    new["binding_id"] = "C03-WP008-V6-INPUT-CANDIDATE-REV7"
    new["binding_version"] = "1.1"
    new["candidate_state"] = "DRAFTED_NOT_REVIEWED_NOT_ACCEPTED_NOT_ADMITTED"
    new["revision_rev7"] = {
        "derived_from": {"path": SRC, "sha256": SRC_SHA, "state": "ACCEPTED (V5-ACCEPT-IMPLEMENTATION)"},
        "authorization": ".codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_AR_B_009_CLOSURE_DECISION.json (AR-B-008-KEEP-OPEN)",
        "builder": "validation/route_b_c03/wp_008/c03_v6/build_input_rev7.py",
        "changes": ["subject hashes re-computed from the V6 sources (catalog source_sha256 refreshed for %d objects)" % refreshed,
                    "adapter ADP-EVALUATE-CLASSIFICATION", "6 variants with 6 new rules in V-015; 1 fixture-mapped",
                    "coverage_class_rev7 = FULL for C03-TA-V-015"],
        "variant_count": sum(len(s["stimulus_variants"]) for s in new["scenarios"]),
        "runtime_version_of_record": "CPython 3.12.10 (P1-PYVER)"}
    data = (json.dumps(new, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    print(json.dumps({"variants": new["revision_rev7"]["variant_count"], "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest().upper()}))
    if "--write" in sys.argv:
        with open(OUT, "wb") as f:
            f.write(data)


if __name__ == "__main__":
    main()
