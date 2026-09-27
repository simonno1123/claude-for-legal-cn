"""Fixed-source synthetic diagnostic; stdout only, not the WP-008 harness.

Run with the project validation interpreter using -I -S -B. The current source
and accepted candidate are loaded side by side without replacing either file.
Synthetic authority labels and validity flags do not represent real authority.
"""

from dataclasses import replace
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import os
import sys
import types


ROOT = Path(__file__).resolve().parents[3]
SOURCE_FILES = {
    "contracts": (
        "scripts/phase2_runtime/route_b_c03/contracts.py",
        "7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4",
    ),
    "original": (
        "scripts/phase2_runtime/route_b_c03/identity_gate.py",
        "EA762C13F1DED4ABEAE27D16DD1087901D73E0B6B0A680791E3082AEFFB4D90A",
    ),
    "candidate": (
        "validation/route_b_c03/wp_008/IDENTITY_GATE_RDM_DSP_002_REVISION_CANDIDATE.py",
        "9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445",
    ),
}
PACKAGE = "rdm_dsp_002_smoke"
DENIED_EVENTS = []


def audit_boundary(event, args):
    """Defense in depth for this process, not a complete OS sandbox claim."""
    denied = event.startswith(("socket.", "subprocess.", "os.spawn", "os.exec"))
    denied |= event in {
        "os.system", "os.remove", "os.rename", "os.rmdir", "os.mkdir",
        "os.link", "os.symlink", "os.truncate", "os.chmod", "os.chdir",
        "shutil.copyfile", "ctypes.dlopen",
    }
    if event == "open":
        _, mode, flags = args
        denied |= bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT
                                | os.O_TRUNC | os.O_APPEND))
        denied |= isinstance(mode, str) and any(c in mode for c in "wax+")
    if denied:
        DENIED_EVENTS.append(event)
        raise PermissionError(f"Diagnostic boundary denied: {event}")


def checked_bytes(name):
    relative, expected = SOURCE_FILES[name]
    raw = (ROOT / relative).read_bytes()
    if sha256(raw).hexdigest().upper() != expected:
        raise RuntimeError(f"Fixed source SHA mismatch: {relative}")
    return raw


def load_exact(name):
    """Execute exactly the checked bytes, without package initializer imports."""
    module_name = f"{PACKAGE}.{name}"
    module = types.ModuleType(module_name)
    module.__package__ = PACKAGE
    module.__file__ = str(ROOT / SOURCE_FILES[name][0])
    sys.modules[module_name] = module
    exec(compile(checked_bytes(name), module.__file__, "exec"), module.__dict__)
    return module


def main():
    if not (sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode):
        raise RuntimeError("Use -I -S -B for this diagnostic")
    if sys.flags.optimize:
        raise RuntimeError("Do not use optimization flags for this diagnostic")
    sys.addaudithook(audit_boundary)
    package = types.ModuleType(PACKAGE)
    package.__path__ = []
    sys.modules[PACKAGE] = package
    c = load_exact("contracts")
    original = load_exact("original")
    candidate = load_exact("candidate")

    configuration = c.CapabilityConfigurationReference(
        capability_id="SYNTHETIC-C03", capability_version="1",
        implementation_sha256="A" * 64, configuration_sha256="B" * 64,
        activation_decision_reference="SYNTHETIC-ACTIVATION",
        state=c.CapabilityState.ENABLED_CAPABILITY_ONLY,
    )
    expected = c.ExpectedIdentityReference(
        capability_id=configuration.capability_id,
        capability_version=configuration.capability_version,
        implementation_sha256=configuration.implementation_sha256,
        configuration_sha256=configuration.configuration_sha256,
        activation_decision_reference=configuration.activation_decision_reference,
        route="SYNTHETIC-ROUTE-B", route_version="1", domain_id="C03",
        domain_version="1", adapter_contract_version="1",
        matter_authorization_reference="SYNTHETIC-MATTER-AUTHORITY",
        execution_authorization_reference="SYNTHETIC-EXECUTION-AUTHORITY",
    )
    envelope = c.GovernedInputEnvelopeReference(
        envelope_id="SYNTHETIC-ENVELOPE", route=expected.route,
        route_version=expected.route_version, domain_id=expected.domain_id,
        domain_version=expected.domain_version,
        adapter_contract_version=expected.adapter_contract_version,
        matter_id="SYNTHETIC-MATTER", matter_version="1",
        matter_authorization_reference=expected.matter_authorization_reference,
        actor_reference="SYNTHETIC-ACTOR", role="SYNTHETIC-ROLE",
        authority_reference="SYNTHETIC-AUTHORITY", purpose="synthetic test",
        operation="metadata gate check", input_set_sha256="C" * 64,
        requested_output_scope=(c.CandidateClass.ISSUE_MATRIX,),
        prohibited_output_scope=("REAL_MATTER",),
        execution_authorization_reference=expected.execution_authorization_reference,
        audit_correlation_id="SYNTHETIC-CORRELATION",
    )
    packet = c.TierBAuthorityPacketReference(
        packet_id="SYNTHETIC-PACKET", packet_version="1", packet_sha256="D" * 64,
        matter_id=envelope.matter_id, matter_version=envelope.matter_version,
        actor_reference=envelope.actor_reference, purpose=envelope.purpose,
        operation=envelope.operation, input_set_sha256=envelope.input_set_sha256,
        output_class=c.CandidateClass.ISSUE_MATRIX,
        decision_reference=expected.execution_authorization_reference,
        valid_from="SYNTHETIC-START", valid_until="SYNTHETIC-END",
        revocation_state=c.RevocationState.CLEAR, state=c.PacketState.ACCEPTED,
    )
    base = dict(configuration=configuration, packet=packet, envelope=envelope,
                expected=expected, validity_confirmed=True, kill_active=False)
    rows = []

    def observe(module, kwargs):
        result = module.evaluate_identity_gate(**kwargs)
        return (result.state.value, result.reason_code,
                result.audit_correlation_id, result.permitted_write_namespaces)

    def check(label, state, reason, **changes):
        kwargs = dict(base, **changes)
        wanted = (state, reason, envelope.audit_correlation_id, ())
        results = {}
        for name, module in (("original", original), ("candidate", candidate)):
            try:
                actual = observe(module, kwargs)
                results[name] = dict(passed=actual == wanted, observed=actual)
            except Exception as exc:
                results[name] = dict(passed=False, error=f"{type(exc).__name__}: {exc}")
        rows.append(dict(id=label, expected=wanted, **results))

    for matter_bad, execution_bad, decision_bad in product((False, True), repeat=3):
        modified_envelope = replace(
            envelope,
            matter_authorization_reference=("SYNTHETIC-WRONG-MATTER" if matter_bad
                                            else expected.matter_authorization_reference),
            execution_authorization_reference=("SYNTHETIC-WRONG-EXECUTION" if execution_bad
                                               else expected.execution_authorization_reference),
        )
        modified_packet = replace(
            packet, decision_reference=("SYNTHETIC-WRONG-DECISION" if decision_bad
                                        else expected.execution_authorization_reference),
        )
        suffix = f"{int(matter_bad)}{int(execution_bad)}{int(decision_bad)}"
        bad = matter_bad or execution_bad or decision_bad
        check(f"authority-{suffix}", "BLOCKED" if bad else "ELIGIBLE_FOR_MAPPING",
              "BLOCKED \u2014 AUTHORITY BINDING FAILURE" if bad else
              "ELIGIBLE \u2014 SEPARATE MATTER INVOCATION AUTHORITY STILL REQUIRED",
              envelope=modified_envelope, packet=modified_packet)

    # Earlier denial paths must retain precedence even when final references differ.
    base["envelope"] = replace(envelope, matter_authorization_reference="SYNTHETIC-WRONG")
    check("kill", "BLOCKED", "BLOCKED \u2014 KILL ACTIVE", kill_active=True)
    check("missing-configuration", "BLOCKED", "BLOCKED \u2014 CAPABILITY NOT ACTIVE",
          configuration=None)
    for state, reason in ((c.CapabilityState.DISABLED, "CAPABILITY NOT ACTIVE"),
                          (c.CapabilityState.REVOKED, "AUTHORITY FAILURE"),
                          (c.CapabilityState.STALE, "VERSION FAILURE")):
        check(f"capability-{state.value}", "BLOCKED", f"BLOCKED \u2014 {reason}",
              configuration=replace(configuration, state=state,
                                    revocation_reference="SYNTHETIC-REVOCATION"))
    for field in ("capability_id", "capability_version", "implementation_sha256",
                  "configuration_sha256", "activation_decision_reference"):
        value = "E" * 64 if field.endswith("sha256") else "SYNTHETIC-MISMATCH"
        check(f"configuration-{field}", "BLOCKED", "BLOCKED \u2014 CAPABILITY IDENTITY FAILURE",
              configuration=replace(configuration, **{field: value}))
    for field in ("route", "route_version", "domain_id", "domain_version",
                  "adapter_contract_version"):
        check(f"envelope-{field}", "BLOCKED", "BLOCKED \u2014 DOMAIN IDENTITY FAILURE",
              envelope=replace(base["envelope"], **{field: "SYNTHETIC-MISMATCH"}))
    check("missing-packet", "BLOCKED", "BLOCKED \u2014 TIER B AUTHORITY REQUIRED", packet=None)
    for state in c.PacketState:
        if state is not c.PacketState.ACCEPTED:
            check(f"packet-{state.value}", "BLOCKED", "BLOCKED \u2014 AUTHORITY FAILURE",
                  packet=replace(packet, state=state))
    for state in (c.RevocationState.REVOKED, c.RevocationState.UNKNOWN):
        check(f"revocation-{state.value}", "BLOCKED", "BLOCKED \u2014 AUTHORITY FAILURE",
              packet=replace(packet, revocation_state=state))
    check("validity-unconfirmed", "BLOCKED", "BLOCKED \u2014 AUTHORITY FAILURE",
          validity_confirmed=False)
    for field in ("matter_id", "matter_version", "actor_reference"):
        check(f"isolation-{field}", "REJECTED", "REJECTED \u2014 ISOLATION FAILURE",
              packet=replace(packet, **{field: "SYNTHETIC-MISMATCH"}))
    for field in ("purpose", "operation"):
        check(f"scope-{field}", "REJECTED", "REJECTED \u2014 SCOPE FAILURE",
              packet=replace(packet, **{field: "SYNTHETIC-MISMATCH"}))
    check("input-set", "BLOCKED", "BLOCKED \u2014 INPUT SET IDENTITY FAILURE",
          packet=replace(packet, input_set_sha256="F" * 64))
    check("output-boundary", "REJECTED", "REJECTED \u2014 OUTPUT BOUNDARY FAILURE",
          envelope=replace(base["envelope"], requested_output_scope=()))

    constructor_results = []
    for label, obj, field in (
        ("missing-matter-reference", envelope, "matter_authorization_reference"),
        ("missing-execution-reference", envelope, "execution_authorization_reference"),
        ("missing-packet-decision", packet, "decision_reference"),
    ):
        try:
            replace(obj, **{field: ""})
            constructor_results.append(dict(id=label, passed=False, error="No ValueError"))
        except ValueError as exc:
            constructor_results.append(dict(id=label, passed=str(exc) ==
                                            f"{field} must be a non-empty explicit value",
                                            observed=str(exc)))

    original_failures = [row["id"] for row in rows if not row["original"]["passed"]]
    candidate_failures = [row["id"] for row in rows if not row["candidate"]["passed"]]
    expected_original_failures = [f"authority-{a}{b}{d}"
                                  for a, b, d in product((0, 1), repeat=3) if a or b or d]
    for name in SOURCE_FILES:
        checked_bytes(name)
    ok = (not candidate_failures and all(row["passed"] for row in constructor_results)
          and original_failures == expected_original_failures and not DENIED_EVENTS)
    report = dict(
        scope="LOCAL SYNTHETIC DIAGNOSTIC ONLY; NOT FORMAL WP-008 VALIDATION OR ACTIVATION",
        python_version=sys.version, executable=sys.executable,
        python_flags=dict(isolated=sys.flags.isolated, no_site=sys.flags.no_site,
                          dont_write_bytecode=sys.dont_write_bytecode),
        source_bindings={k: dict(path=v[0], sha256=v[1]) for k, v in SOURCE_FILES.items()},
        scenario_count=len(rows), candidate_pass_count=len(rows) - len(candidate_failures),
        candidate_failures=candidate_failures, original_failures=original_failures,
        baseline_defect_reproduced=original_failures == expected_original_failures,
        constructor_checks=constructor_results, denied_events=DENIED_EVENTS,
        source_hashes_unchanged=True, diagnostic_success=ok, results=rows,
    )
    print(json.dumps(report, ensure_ascii=True, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
