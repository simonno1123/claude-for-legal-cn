"""Re-run the fixed synthetic suite against the installed source and saved original.

The prior suite and its output remain unchanged. Only its input paths are
redirected in memory; all test inputs, assertions and expected outcomes are reused.
This is not the formal WP-008 harness or a capability activation operation.
"""

from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
from pathlib import Path
import json
import sys
import types


ROOT = Path(__file__).resolve().parents[3]
VALIDATION = "validation/route_b_c03/wp_008/"
SUITE_PATH = VALIDATION + "test_identity_gate_rdm_dsp_002.py"
SUITE_SHA = "3ECC8614BAC8AC7960807571BA323CF24BA73D4916D83B4A59459EAED93F1833"
ORIGINAL_PATH = VALIDATION + "IDENTITY_GATE_RDM_DSP_002_PRE_REPLACEMENT.py"
ORIGINAL_SHA = "EA762C13F1DED4ABEAE27D16DD1087901D73E0B6B0A680791E3082AEFFB4D90A"
ACCEPTED_PATH = VALIDATION + "IDENTITY_GATE_RDM_DSP_002_REVISION_CANDIDATE.py"
ACCEPTED_SHA = "9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445"
ACTIVE_PATH = "scripts/phase2_runtime/route_b_c03/identity_gate.py"


def exact_bytes(relative, expected_hash):
    raw = (ROOT / relative).read_bytes()
    if sha256(raw).hexdigest().upper() != expected_hash:
        raise RuntimeError(f"Fixed input SHA mismatch: {relative}")
    return raw


def main():
    if not (sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode):
        raise RuntimeError("Use -I -S -B for this regression")
    if sys.flags.optimize:
        raise RuntimeError("Do not use optimization flags for this regression")

    active_bytes = exact_bytes(ACTIVE_PATH, ACCEPTED_SHA)
    if active_bytes != exact_bytes(ACCEPTED_PATH, ACCEPTED_SHA):
        raise RuntimeError("Installed source does not match the accepted candidate")
    exact_bytes(ORIGINAL_PATH, ORIGINAL_SHA)
    suite_bytes = exact_bytes(SUITE_PATH, SUITE_SHA)

    suite = types.ModuleType("rdm_dsp_002_fixed_suite")
    suite.__file__ = str(ROOT / SUITE_PATH)
    sys.modules[suite.__name__] = suite
    exec(compile(suite_bytes, suite.__file__, "exec"), suite.__dict__)
    suite.SOURCE_FILES["original"] = (ORIGINAL_PATH, ORIGINAL_SHA)
    suite.SOURCE_FILES["candidate"] = (ACTIVE_PATH, ACCEPTED_SHA)
    suite.SOURCE_FILES["accepted_candidate"] = (ACCEPTED_PATH, ACCEPTED_SHA)

    captured = StringIO()
    with redirect_stdout(captured):
        exit_code = suite.main()
    report = json.loads(captured.getvalue())
    exact_bytes(SUITE_PATH, SUITE_SHA)
    exact_bytes(ORIGINAL_PATH, ORIGINAL_SHA)
    if exact_bytes(ACTIVE_PATH, ACCEPTED_SHA) != exact_bytes(ACCEPTED_PATH, ACCEPTED_SHA):
        raise RuntimeError("Installed source or accepted candidate changed during execution")

    counts_valid = (
        report["scenario_count"] == 38
        and len(report["results"]) == 38
        and len({row["id"] for row in report["results"]}) == 38
        and len(report["constructor_checks"]) == 3
    )
    report["scope"] = (
        "LOCAL SYNTHETIC POST-REPLACEMENT REGRESSION ONLY; "
        "NOT FORMAL WP-008 VALIDATION OR ACTIVATION"
    )
    report["source_bindings"]["preserved_original"] = report["source_bindings"].pop("original")
    report["source_bindings"]["active_source"] = report["source_bindings"].pop("candidate")
    report["active_source_pass_count"] = report.pop("candidate_pass_count")
    report["active_source_failures"] = report.pop("candidate_failures")
    report["preserved_original_failures"] = report.pop("original_failures")
    for row in report["results"]:
        row["preserved_original"] = row.pop("original")
        row["active_source"] = row.pop("candidate")
    report["fixed_suite_binding"] = dict(path=SUITE_PATH, sha256=SUITE_SHA)
    report["regression_runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest().upper()
    report["active_source_matches_accepted_candidate"] = True
    report["coverage_counts_valid"] = counts_valid
    report["diagnostic_success"] = bool(report["diagnostic_success"] and counts_valid and exit_code == 0)
    print(json.dumps(report, ensure_ascii=True, indent=2))
    return 0 if report["diagnostic_success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
