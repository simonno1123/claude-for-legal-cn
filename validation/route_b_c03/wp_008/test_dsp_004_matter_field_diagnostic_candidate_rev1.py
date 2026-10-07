"""Console-only authorized synthetic tests for the DSP-004 matter diagnostic.

Use the observed local Python 3.12.14 with -I -S -B. Explicit harness source
reads use the fixed list below, outside guarded calls. Interpreter/stdlib
startup and source hashing are not zero-I/O execution. No evidence is written.
Only contracts declarations, the accepted denial preserver, and the new
candidate are executed under declared module identities. Package initialization
and the existing identity gate, other candidates, and providers are not run.

Caller-supplied objects/values are entirely synthetic. Partial or deliberately
malformed objects test the selected-field diagnostic, not valid construction,
source admission, capture, prior gate execution, same-call provenance, real
isolation, fixture conformance, or full WP-008 validation. The finite audit
guard/profiler and AST whitelist are diagnostic checks, not complete sandboxes,
allocation proofs, or runtime environment acceptance. Historical 3.12.13
inventory stays unchanged; it is not the observed current runtime.
"""

import __future__
import ast
import builtins
import dataclasses
from enum import Enum
import hashlib
import inspect
import json
from pathlib import Path
import re
import sys
import types
import typing
import unittest


ROOT = Path(__file__).resolve().parents[3]
CONTRACTS_MODULE = "route_b_c03.contracts"
PRESERVER_MODULE = "DSP_004_DENIED_DECISION_PRESERVER_CANDIDATE_REV1"
CANDIDATE_MODULE = "DSP_004_MATTER_FIELD_DIAGNOSTIC_CANDIDATE_REV1"
SUBJECT_RELATIVE = "validation/route_b_c03/wp_008/DSP_004_MATTER_FIELD_DIAGNOSTIC_CANDIDATE_REV1.py"
SUBJECT_SHA256 = "0322A367A607261501020EBB45BF1A2351580B54BCB0B468949E054540B02844"
EXPECTED_RUNTIME = (3, 12, 14)
EXPECTED_EXECUTABLE = ROOT / ".venv-validation/Scripts/python.exe"
PRESERVED_INPUTS = (
    ("scripts/phase2_runtime/route_b_c03/contracts.py",
     "7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4"),
    ("scripts/phase2_runtime/route_b_c03/identity_gate.py",
     "9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445"),
    ("docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PREPARATION_DESIGN_RECORD_REV1.md",
     "DB39150AE0428A452B2BEBE958A4B7DD91F4DE8A3790B0BC374FAEA4693868F4"),
    ("validation/route_b_c03/wp_008/DSP_004_DENIED_DECISION_PRESERVER_CANDIDATE_REV1.py",
     "61D424C35D262C3CC9FE03863F4BCB4D39FF96E248E5A7A08B8EAE6F8D598245"),
    ("validation/route_b_c03/wp_008/test_dsp_004_denied_decision_preserver_candidate_rev1.py",
     "7AD706C2C8EA377069C404A7F95B1079293E9E096616E74CA1E17C67AE4E6292"),
    ("validation/route_b_c03/wp_008/DSP_004_EXPECTED_BASELINE_READER_CANDIDATE_REV1.py",
     "AE1389EDA1C3B9129A0546DA5764C1F68A6B0193A22DA3431CAA89BAB8DC0727"),
    ("validation/route_b_c03/wp_008/DSP_004_NATIVE_CONTRACT_CANDIDATE_REV1.py",
     "1544B7D8101493072E9BCA5C23B09C3C811F1B52CB1E9F5A8D73C976576FC312"),
    ("validation/route_b_c03/wp_008/DSP_004_ELIGIBLE_DECISION_COMBINER_CANDIDATE_REV1.py",
     "95156DEAD051799DA6361216EA66007F5B3FFF10257A886C0225AD3E95FDE9D6"),
    (".venv-validation/Scripts/python.exe",
     "560B9EF7D856608AB8DA02DED2DC8A1951AD1F424C382C0EC6A698874165A18E"),
    (".venv-validation/pyvenv.cfg",
     "7AFB3C331994D8D1CB462B711254E30BAE372DC8A28F2C485AFA79B030775461"),
    ("validation/route_b_c03/wp_008/ENVIRONMENT_MANIFEST.md",
     "EFCF1A783199F58387BDBB0704563ED943A5E6A3E319A04CE6D58E57FC5CA531"),
)
FIELD_NAMES = ("matter_id", "matter_version", "actor_reference")
GATE_FIELDS = ("state", "reason_code", "audit_correlation_id", "permitted_write_namespaces")
CHECK_FIELDS = ("field_kind", "state", "cause", "packet_reference",
                "envelope_reference", "audit_correlation_id")
# Handwritten eight-case oracle; this is not existing-gate execution coverage.
LITERAL_CASES = (
    ((False, False, False), ("MATCH", "MATCH", "MATCH")),
    ((False, False, True), ("MATCH", "MATCH", "MISMATCH")),
    ((False, True, False), ("MATCH", "MISMATCH", "MATCH")),
    ((False, True, True), ("MATCH", "MISMATCH", "MISMATCH")),
    ((True, False, False), ("MISMATCH", "MATCH", "MATCH")),
    ((True, False, True), ("MISMATCH", "MATCH", "MISMATCH")),
    ((True, True, False), ("MISMATCH", "MISMATCH", "MATCH")),
    ((True, True, True), ("MISMATCH", "MISMATCH", "MISMATCH")),
)
_PHASE = None
_BLOCKED_EVENTS = []
_SELF_TEST_EVENTS = []
_GATE_CONSTRUCTOR_COUNTS = []
_HASH_BEFORE = False
_HASH_AFTER = False
_CASE_COUNT = 0
_MISSING = object()


class ForbiddenCandidateSideEffect(RuntimeError):
    pass


def audit_guard(event, args):
    if _PHASE is not None and (
        event in ("open", "import")
        or event.startswith(("os.", "socket.", "subprocess.", "ctypes.", "winreg."))
    ):
        record = {"phase": _PHASE, "event": event}
        (_SELF_TEST_EVENTS if _PHASE == "guard-self-test" else _BLOCKED_EVENTS).append(record)
        raise ForbiddenCandidateSideEffect(event)


def guarded_call(phase, function, *args, **kwargs):
    global _PHASE
    if _PHASE is not None:
        raise RuntimeError("Nested guard is prohibited")
    _PHASE = phase
    try:
        return function(*args, **kwargs)
    finally:
        _PHASE = None


def read_fixed_bytes(relative, expected_sha):
    if (relative, expected_sha) not in PRESERVED_INPUTS + ((SUBJECT_RELATIVE, SUBJECT_SHA256),):
        raise RuntimeError("Read outside fixed local inputs")
    if _PHASE is not None:
        raise RuntimeError("Source hashing must occur outside candidate calls")
    payload = (ROOT / relative).read_bytes()
    if hashlib.sha256(payload).hexdigest().upper() != expected_sha:
        raise RuntimeError(f"Fixed SHA mismatch: {relative}")
    return payload


def verify_fixed_inputs():
    for pair in PRESERVED_INPUTS + ((SUBJECT_RELATIVE, SUBJECT_SHA256),):
        read_fixed_bytes(*pair)


def assert_static_subject(tree):
    expected_imports = [
        ("dataclasses", ("dataclass",)), ("enum", ("Enum", "unique")),
        (CONTRACTS_MODULE, ("GateDecision", "GovernedInputEnvelopeReference",
                            "InvocationState", "TierBAuthorityPacketReference")),
        (PRESERVER_MODULE, ("preserve_denied_decision",)),
    ]
    allowed_calls = {
        "type", "TypeError", "ValueError", "object", "getattr", "len", "enumerate",
        "dataclass", "unique", "preserve_denied_decision", "_require_native_text",
        "_require_isolation_prior", "_validate_field_check", "_validate_diagnostic",
        "_diagnose_field", "MatterFieldCheck", "MatterFieldDiagnostic",
    }
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            raise RuntimeError("Unlisted plain import")
        if isinstance(node, ast.ImportFrom):
            if node.level or any(alias.asname for alias in node.names):
                raise RuntimeError("Unlisted import identity")
            imports.append((node.module, tuple(alias.name for alias in node.names)))
        if isinstance(node, (ast.AsyncFunctionDef, ast.Lambda)):
            raise RuntimeError("Unlisted executable surface")
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id not in allowed_calls:
                    raise RuntimeError(f"Unlisted candidate call: {node.func.id}")
            elif isinstance(node.func, ast.Attribute):
                if node.func.attr != "isspace" or node.args or node.keywords:
                    raise RuntimeError("Unlisted candidate attribute call")
            else:
                raise RuntimeError("Indirect candidate call")
    if imports != expected_imports:
        raise RuntimeError("Candidate import whitelist mismatch")
    if tuple(node.name for node in tree.body if isinstance(node, ast.ClassDef)) != (
        "MatterFieldKind", "MatterFieldState", "MatterFieldCause",
        "MatterFieldCheck", "MatterFieldDiagnostic",
    ):
        raise RuntimeError("Candidate type surface mismatch")
    if tuple(node.name for node in tree.body if isinstance(node, ast.FunctionDef)) != (
        "_require_native_text", "_require_isolation_prior", "_validate_field_check",
        "_validate_diagnostic", "_diagnose_field", "diagnose_matter_fields",
    ):
        raise RuntimeError("Candidate function surface mismatch")
    for node in tree.body:
        if isinstance(node, (ast.ImportFrom, ast.ClassDef, ast.FunctionDef)):
            continue
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and type(node.value.value) is str:
            continue
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            if node.targets[0].id in ("_MISSING", "_FIELD_ORDER"):
                continue
        raise RuntimeError("Unlisted module-level candidate execution")


def load_declared_module(name, relative, payload):
    if name in sys.modules:
        raise RuntimeError(f"Module identity conflict: {name}")
    module = types.ModuleType(name)
    module.__file__ = str(ROOT / relative)
    module.__package__ = "route_b_c03" if name == CONTRACTS_MODULE else ""
    sys.modules[name] = module
    code = compile(payload, module.__file__, "exec", dont_inherit=True)
    guarded_call(f"fixed-load:{name}", exec, code, module.__dict__)
    return module


class MatterFieldDiagnosticCandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global _HASH_BEFORE
        if sys.version_info[:3] != EXPECTED_RUNTIME:
            raise RuntimeError("Batch bound to observed Python 3.12.14")
        if Path(sys.executable).resolve() != EXPECTED_EXECUTABLE.resolve():
            raise RuntimeError("Unexpected local interpreter")
        if (sys.flags.isolated, sys.flags.no_site, sys.flags.dont_write_bytecode) != (1, 1, 1):
            raise RuntimeError("Required -I -S -B flags are absent")
        verify_fixed_inputs()
        _HASH_BEFORE = True
        cls.subject_bytes = read_fixed_bytes(SUBJECT_RELATIVE, SUBJECT_SHA256)
        cls.subject_tree = ast.parse(cls.subject_bytes, filename=str(ROOT / SUBJECT_RELATIVE))
        assert_static_subject(cls.subject_tree)
        for name in sys.modules:
            if (name == "route_b_c03" or name.startswith("route_b_c03.")
                    or name in (PRESERVER_MODULE, CANDIDATE_MODULE)):
                raise RuntimeError(f"Unexpected preloaded module: {name}")
        sys.addaudithook(audit_guard)
        cls.parent = types.ModuleType("route_b_c03")
        cls.parent.__path__ = []
        cls.parent.__package__ = "route_b_c03"
        sys.modules["route_b_c03"] = cls.parent
        cls.contracts = load_declared_module(
            CONTRACTS_MODULE, PRESERVED_INPUTS[0][0], read_fixed_bytes(*PRESERVED_INPUTS[0]),
        )
        cls.parent.contracts = cls.contracts
        cls.preserver = load_declared_module(
            PRESERVER_MODULE, PRESERVED_INPUTS[3][0], read_fixed_bytes(*PRESERVED_INPUTS[3]),
        )
        cls.subject = load_declared_module(CANDIDATE_MODULE, SUBJECT_RELATIVE, cls.subject_bytes)

    def setUp(self):
        self.events_before = len(_BLOCKED_EVENTS)

    def tearDown(self):
        self.assertEqual(len(_BLOCKED_EVENTS), self.events_before)
        self.assertIsNone(_PHASE)

    def prior(self, **changes):
        values = dict(state=self.contracts.InvocationState.REJECTED,
                      reason_code="REJECTED — ISOLATION FAILURE",
                      audit_correlation_id="SYNTHETIC-CALL-001", permitted_write_namespaces=())
        values.update(changes)
        return guarded_call("synthetic-prior-construction", self.contracts.GateDecision, **values)

    def packet(self, **changes):
        values = dict(packet_id="SYNTHETIC-PACKET", packet_version="SYNTHETIC-V1",
                      packet_sha256="0" * 64, matter_id="SYNTHETIC-MATTER",
                      matter_version="SYNTHETIC-V1", actor_reference="SYNTHETIC-ACTOR",
                      purpose="SYNTHETIC-PURPOSE", operation="SYNTHETIC-OPERATION",
                      input_set_sha256="0" * 64,
                      output_class=self.contracts.CandidateClass.ISSUE_MATRIX,
                      decision_reference="SYNTHETIC-DECISION", valid_from="SYNTHETIC-NOT-A-TIME",
                      valid_until="SYNTHETIC-NOT-A-TIME",
                      revocation_state=self.contracts.RevocationState.CLEAR,
                      state=self.contracts.PacketState.ACCEPTED)
        values.update(changes)
        return guarded_call("synthetic-packet-construction",
                            self.contracts.TierBAuthorityPacketReference, **values)

    def envelope(self, **changes):
        values = dict(envelope_id="SYNTHETIC-ENVELOPE", route="SYNTHETIC-ROUTE",
                      route_version="SYNTHETIC-V1", domain_id="SYNTHETIC-DOMAIN",
                      domain_version="SYNTHETIC-V1", adapter_contract_version="SYNTHETIC-V1",
                      matter_id="SYNTHETIC-MATTER", matter_version="SYNTHETIC-V1",
                      matter_authorization_reference="SYNTHETIC-AUTHORITY",
                      actor_reference="SYNTHETIC-ACTOR", role="SYNTHETIC-ROLE",
                      authority_reference="SYNTHETIC-AUTHORITY", purpose="SYNTHETIC-PURPOSE",
                      operation="SYNTHETIC-OPERATION", input_set_sha256="0" * 64,
                      requested_output_scope=(self.contracts.CandidateClass.ISSUE_MATRIX,),
                      prohibited_output_scope=(), execution_authorization_reference="SYNTHETIC-EXECUTION",
                      audit_correlation_id="SYNTHETIC-CALL-001")
        values.update(changes)
        return guarded_call("synthetic-envelope-construction",
                            self.contracts.GovernedInputEnvelopeReference, **values)

    def arguments(self):
        return self.prior(), self.packet(), self.envelope()

    def snapshot(self, value):
        if type(value) not in (self.contracts.GateDecision,
                               self.contracts.TierBAuthorityPacketReference,
                               self.contracts.GovernedInputEnvelopeReference):
            return id(value), ()
        return id(value), tuple((field.name, id(item), type(item))
                               for field in dataclasses.fields(value)
                               for item in (getattr(value, field.name, _MISSING),))

    def diagnose(self, prior, packet, envelope):
        snapshots = tuple(self.snapshot(value) for value in (prior, packet, envelope))
        constructor_code = self.contracts.GateDecision.__init__.__code__
        observed = []
        if sys.getprofile() is not None:
            raise RuntimeError("Unexpected profiler")

        def observer(frame, event, argument):
            if event == "call" and frame.f_code is constructor_code:
                observed.append(id(frame.f_locals["self"]))

        sys.setprofile(observer)
        try:
            return guarded_call("matter-diagnostic-call", self.subject.diagnose_matter_fields,
                                prior, packet, envelope)
        finally:
            sys.setprofile(None)
            _GATE_CONSTRUCTOR_COUNTS.append(len(observed))
            self.assertEqual(observed, [], "Diagnostic constructed a replacement GateDecision")
            self.assertEqual(tuple(self.snapshot(value) for value in (prior, packet, envelope)), snapshots)

    def reject(self, error, arguments):
        with self.assertRaises(error):
            self.diagnose(*arguments)

    def field_check(self, **changes):
        values = dict(field_kind=self.subject.MatterFieldKind.MATTER_ID,
                      state=self.subject.MatterFieldState.MATCH,
                      cause=self.subject.MatterFieldCause.EXACT_EQUAL,
                      packet_reference="SYNTHETIC-MATTER", envelope_reference="SYNTHETIC-MATTER",
                      audit_correlation_id="SYNTHETIC-CALL-001")
        values.update(changes)
        return guarded_call("synthetic-field-check", self.subject.MatterFieldCheck, **values)

    def diagnostic_record(self, prior, checks):
        return guarded_call("synthetic-diagnostic-record", self.subject.MatterFieldDiagnostic, prior, checks)

    def test_runtime_and_isolation_flags(self):
        self.assertEqual(sys.version_info[:3], EXPECTED_RUNTIME)
        self.assertEqual(Path(sys.executable).resolve(), EXPECTED_EXECUTABLE.resolve())
        self.assertEqual((sys.flags.isolated, sys.flags.no_site, sys.flags.dont_write_bytecode), (1, 1, 1))

    def test_exact_existing_class_and_preserver_identity(self):
        for name in ("GateDecision", "InvocationState", "TierBAuthorityPacketReference",
                     "GovernedInputEnvelopeReference"):
            self.assertIs(getattr(self.subject, name), getattr(self.contracts, name))
        self.assertIs(self.subject.preserve_denied_decision, self.preserver.preserve_denied_decision)

    def test_five_independent_types_and_exact_native_contracts(self):
        for name in ("MatterFieldKind", "MatterFieldState", "MatterFieldCause",
                     "MatterFieldCheck", "MatterFieldDiagnostic"):
            candidate_type = getattr(self.subject, name)
            self.assertEqual(candidate_type.__module__, CANDIDATE_MODULE)
            self.assertFalse(hasattr(self.contracts, name))
        self.assertEqual(tuple(self.subject.MatterFieldKind.__members__),
                         ("MATTER_ID", "MATTER_VERSION", "ACTOR_REFERENCE"))
        self.assertEqual(tuple(self.subject.MatterFieldState.__members__), ("MATCH", "MISMATCH", "NOT_EVALUATED"))
        self.assertEqual(tuple(self.subject.MatterFieldCause.__members__),
                         ("EXACT_EQUAL", "EXACT_UNEQUAL", "FIELD_UNAVAILABLE", "INVALID_REFERENCE_TYPE"))
        self.assertEqual(tuple(field.name for field in dataclasses.fields(self.subject.MatterFieldCheck)), CHECK_FIELDS)
        self.assertEqual(tuple(field.name for field in dataclasses.fields(self.subject.MatterFieldDiagnostic)),
                         ("prior_decision", "checks"))

    def test_signature_requires_only_three_native_inputs(self):
        signature = inspect.signature(self.subject.diagnose_matter_fields)
        self.assertEqual(tuple(signature.parameters), ("prior", "packet", "envelope"))
        for name, native in (("prior", self.contracts.GateDecision),
                             ("packet", self.contracts.TierBAuthorityPacketReference),
                             ("envelope", self.contracts.GovernedInputEnvelopeReference)):
            self.assertIs(signature.parameters[name].annotation, native)
            self.assertIs(signature.parameters[name].default, inspect.Parameter.empty)
        self.assertIs(signature.return_annotation, self.subject.MatterFieldDiagnostic)

    def test_all_eight_literal_match_patterns(self):
        global _CASE_COUNT
        self.assertEqual(len(LITERAL_CASES), 8)
        for mismatches, expected_states in LITERAL_CASES:
            with self.subTest(mismatches=mismatches):
                prior, packet, envelope = self.arguments()
                for field, mismatched in zip(FIELD_NAMES, mismatches):
                    if mismatched:
                        object.__setattr__(packet, field, getattr(packet, field) + "-DIFFERENT")
                result = self.diagnose(prior, packet, envelope)
                self.assertIs(result.prior_decision, prior)
                self.assertIs(type(result.checks), tuple)
                self.assertEqual(tuple(check.state.name for check in result.checks), expected_states)
                self.assertEqual(tuple(check.field_kind.name for check in result.checks),
                                 ("MATTER_ID", "MATTER_VERSION", "ACTOR_REFERENCE"))
                for field, check, expected_state in zip(FIELD_NAMES, result.checks, expected_states):
                    self.assertIs(check.packet_reference, getattr(packet, field))
                    self.assertIs(check.envelope_reference, getattr(envelope, field))
                    self.assertEqual(check.cause.name, "EXACT_EQUAL" if expected_state == "MATCH" else "EXACT_UNEQUAL")
                _CASE_COUNT += 1
        self.assertEqual(_CASE_COUNT, 8)

    def test_actor_only_mismatch_has_no_matter_mismatch_or_routing_verdict(self):
        prior, packet, envelope = self.arguments()
        object.__setattr__(packet, "actor_reference", "SYNTHETIC-ACTOR-OTHER")
        result = self.diagnose(prior, packet, envelope)
        self.assertEqual(tuple(check.state.name for check in result.checks), ("MATCH", "MATCH", "MISMATCH"))
        self.assertIs(result.prior_decision, prior)
        self.assertEqual(prior.reason_code, "REJECTED — ISOLATION FAILURE")
        for field in ("matter_mismatch", "eligible", "permission", "boundary_checks", "aggregate_verdict"):
            self.assertFalse(hasattr(result, field))

    def test_all_match_exposes_relationship_contradiction_without_clearing_rejection(self):
        prior, packet, envelope = self.arguments()
        result = self.diagnose(prior, packet, envelope)
        self.assertEqual(tuple(check.state.name for check in result.checks), ("MATCH", "MATCH", "MATCH"))
        self.assertIs(result.prior_decision, prior)
        self.assertIs(prior.state, self.contracts.InvocationState.REJECTED)
        self.assertEqual(prior.reason_code, "REJECTED — ISOLATION FAILURE")
        self.assertEqual(prior.permitted_write_namespaces, ())
        self.assertFalse(hasattr(result, "cause_attribution"))
        self.assertIn("input relationship\ncontradiction", self.subject.__doc__)

    def test_partial_check_cannot_hide_a_known_mismatch_or_establish_complete_attribution(self):
        prior, packet, envelope = self.arguments()
        object.__setattr__(packet, "matter_id", "SYNTHETIC-MATTER-OTHER")
        object.__delattr__(packet, "actor_reference")
        result = self.diagnose(prior, packet, envelope)
        self.assertEqual(tuple(check.state.name for check in result.checks), ("MISMATCH", "MATCH", "NOT_EVALUATED"))
        self.assertIs(result.prior_decision, prior)
        self.assertFalse(hasattr(result, "complete_attribution"))

    def test_equal_correlation_is_only_structural_not_same_call_proof(self):
        first = self.arguments()
        second = self.arguments()
        self.assertNotEqual(id(first[1]), id(second[1]))
        result = self.diagnose(first[0], second[1], second[2])
        self.assertIs(result.prior_decision, first[0])
        self.assertFalse(hasattr(result, "same_call_verified"))
        self.assertIn("Equal correlation strings do not prove one call", self.subject.__doc__)

    def test_whitespace_case_and_unicode_are_not_normalized(self):
        for left, right in ((" SYNTHETIC ", "SYNTHETIC"), ("SYNTHETIC-A", "synthetic-a"),
                            ("SYNTHETIC-É", "SYNTHETIC-E\u0301"), ("\tSYNTHETIC\n", "\tSYNTHETIC\n")):
            prior, packet, envelope = self.arguments()
            object.__setattr__(packet, "matter_id", left)
            object.__setattr__(envelope, "matter_id", right)
            check = self.diagnose(prior, packet, envelope).checks[0]
            self.assertIs(check.packet_reference, left)
            self.assertIs(check.envelope_reference, right)
            self.assertEqual(check.state.name, "MATCH" if left == right else "MISMATCH")

    def test_each_of_six_missing_fields_is_not_evaluated_without_echo(self):
        for side in (1, 2):
            for position, field in enumerate(FIELD_NAMES):
                arguments = self.arguments()
                object.__delattr__(arguments[side], field)
                result = self.diagnose(*arguments)
                for index, check in enumerate(result.checks):
                    self.assertEqual(check.state.name, "NOT_EVALUATED" if index == position else "MATCH")
                check = result.checks[position]
                self.assertEqual(check.cause.name, "FIELD_UNAVAILABLE")
                self.assertIsNone(check.packet_reference)
                self.assertIsNone(check.envelope_reference)

    def test_invalid_each_side_field_is_not_evaluated_without_conversion(self):
        class StringSubclass(str):
            pass

        class MustNotConvert:
            def __str__(self):
                raise AssertionError("Unexpected conversion")

        invalid_values = (None, True, 1, b"SYNTHETIC", [], {}, "", "\t\n\u3000", "\u00a0",
                          StringSubclass("SYNTHETIC"), MustNotConvert())
        for side in (1, 2):
            for position, field in enumerate(FIELD_NAMES):
                for value in invalid_values:
                    arguments = self.arguments()
                    object.__setattr__(arguments[side], field, value)
                    result = self.diagnose(*arguments)
                    check = result.checks[position]
                    self.assertEqual((check.state.name, check.cause.name),
                                     ("NOT_EVALUATED", "INVALID_REFERENCE_TYPE"))
                    self.assertIsNone(check.packet_reference)
                    self.assertIsNone(check.envelope_reference)
                    self.assertTrue(all(other.state.name == "MATCH" for index, other in enumerate(result.checks)
                                        if index != position))

    def test_missing_side_takes_precedence_over_invalid_other_side(self):
        arguments = self.arguments()
        object.__delattr__(arguments[1], "matter_id")
        object.__setattr__(arguments[2], "matter_id", 1)
        check = self.diagnose(*arguments).checks[0]
        self.assertEqual(check.cause.name, "FIELD_UNAVAILABLE")
        self.assertIsNone(check.packet_reference)
        self.assertIsNone(check.envelope_reference)

    def test_internal_field_selection_is_closed_to_exact_three_pairs(self):
        prior, packet, envelope = self.arguments()
        for kind, attribute in (
            (self.subject.MatterFieldKind.MATTER_ID, "packet_sha256"),
            (self.subject.MatterFieldKind.MATTER_ID, "purpose"),
            (self.subject.MatterFieldKind.MATTER_ID, "actor_reference"),
            (self.subject.MatterFieldKind.ACTOR_REFERENCE, "matter_version"),
        ):
            with self.assertRaises(ValueError):
                guarded_call("closed-field-selector", self.subject._diagnose_field,
                             kind, attribute, packet, envelope, prior.audit_correlation_id)
        class TextSubclass(str):
            pass
        for kind, attribute in (("MATTER_ID", "matter_id"),
                                (self.subject.MatterFieldKind.MATTER_ID, TextSubclass("matter_id"))):
            with self.assertRaises(TypeError):
                guarded_call("native-field-selector", self.subject._diagnose_field,
                             kind, attribute, packet, envelope, prior.audit_correlation_id)

    def test_internal_helper_rejects_foreign_inputs_before_attribute_access(self):
        prior, packet, envelope = self.arguments()
        class MustNotBeObserved:
            def __getattribute__(self, name):
                raise AssertionError("Unexpected foreign attribute access")
        for left, right in ((MustNotBeObserved(), envelope), (packet, MustNotBeObserved())):
            with self.assertRaises(TypeError):
                guarded_call("native-helper-inputs", self.subject._diagnose_field,
                             self.subject.MatterFieldKind.MATTER_ID, "matter_id",
                             left, right, prior.audit_correlation_id)
        for correlation, error in ((None, TypeError), ("", ValueError), ("\u3000", ValueError)):
            with self.assertRaises(error):
                guarded_call("native-helper-correlation", self.subject._diagnose_field,
                             self.subject.MatterFieldKind.MATTER_ID, "matter_id",
                             packet, envelope, correlation)

    def test_upstream_constructor_failure_never_invokes_diagnostic_or_repairs_inputs(self):
        before = len(_GATE_CONSTRUCTOR_COUNTS)
        with self.assertRaises(ValueError):
            self.packet(matter_id="")
        with self.assertRaises(ValueError):
            self.envelope(matter_version="")
        self.assertEqual(len(_GATE_CONSTRUCTOR_COUNTS), before)

    def test_non_native_and_foreign_prior_is_rejected(self):
        _, packet, envelope = self.arguments()
        for value in (None, {}, [], (), "REJECTED", True):
            self.reject(TypeError, (value, packet, envelope))
        foreign = type("GateDecision", (), {"__module__": CONTRACTS_MODULE})()
        self.reject(TypeError, (foreign, packet, envelope))
        class GateSubclass(self.contracts.GateDecision):
            pass
        prior = self.prior()
        subclass = GateSubclass(**{field: getattr(prior, field) for field in GATE_FIELDS})
        self.reject(TypeError, (subclass, packet, envelope))

    def test_other_prior_states_and_nonexact_reason_are_out_of_scope(self):
        _, packet, envelope = self.arguments()
        for state in self.contracts.InvocationState:
            if state is not self.contracts.InvocationState.REJECTED:
                self.reject(ValueError, (self.prior(state=state), packet, envelope))
        for reason in ("REJECTED — SCOPE FAILURE", " REJECTED — ISOLATION FAILURE",
                       "REJECTED — ISOLATION FAILURE ", "REJECTED - ISOLATION FAILURE", "SYNTHETIC"):
            self.reject(ValueError, (self.prior(reason_code=reason), packet, envelope))

    def test_prior_native_state_and_text_are_revalidated(self):
        _, packet, envelope = self.arguments()
        wrong = Enum("ForeignInvocationState", {"REJECTED": "REJECTED"})
        for value in ("REJECTED", None, 1, True, wrong.REJECTED):
            self.reject(TypeError, (self.prior(state=value), packet, envelope))
        class TextSubclass(str):
            pass
        for field in ("reason_code", "audit_correlation_id"):
            for value, error in ((None, TypeError), (b"SYNTHETIC", TypeError),
                                 (TextSubclass("SYNTHETIC"), TypeError), ("", ValueError), ("\u3000", ValueError)):
                self.reject(error, (self.prior(**{field: value}), packet, envelope))

    def test_prior_namespace_and_missing_fields_are_not_repaired(self):
        _, packet, envelope = self.arguments()
        for value, error in (([], TypeError), (None, TypeError), (("SYNTHETIC",), ValueError)):
            self.reject(error, (self.prior(permitted_write_namespaces=value), packet, envelope))
        for field in GATE_FIELDS:
            prior = self.prior()
            object.__delattr__(prior, field)
            self.reject(ValueError, (prior, packet, envelope))

    def test_packet_and_envelope_require_exact_existing_types(self):
        for side, native in ((1, self.contracts.TierBAuthorityPacketReference),
                             (2, self.contracts.GovernedInputEnvelopeReference)):
            for value in (None, {}, [], (), "SYNTHETIC", True):
                arguments = list(self.arguments())
                arguments[side] = value
                self.reject(TypeError, arguments)
            arguments = list(self.arguments())
            foreign = type(native.__name__, (), {"__module__": CONTRACTS_MODULE})()
            arguments[side] = foreign
            self.reject(TypeError, arguments)
            subclass = type("SyntheticSubclass", (native,), {})
            arguments = list(self.arguments())
            source = arguments[side]
            arguments[side] = subclass(**{field.name: getattr(source, field.name) for field in dataclasses.fields(source)})
            self.reject(TypeError, arguments)

    def test_envelope_correlation_requires_native_initialized_matching_text(self):
        class TextSubclass(str):
            pass
        for value, error in ((None, TypeError), (True, TypeError), (TextSubclass("SYNTHETIC"), TypeError),
                             ("", ValueError), ("\u3000", ValueError), ("SYNTHETIC-OTHER-CALL", ValueError)):
            arguments = self.arguments()
            object.__setattr__(arguments[2], "audit_correlation_id", value)
            self.reject(error, arguments)
        arguments = self.arguments()
        object.__delattr__(arguments[2], "audit_correlation_id")
        self.reject(ValueError, arguments)

    def test_native_check_state_cause_pairing_is_closed(self):
        for state in self.subject.MatterFieldState:
            for cause in self.subject.MatterFieldCause:
                values = dict(state=state, cause=cause)
                if state.name == "MISMATCH":
                    values["envelope_reference"] = "SYNTHETIC-OTHER"
                if state.name == "NOT_EVALUATED":
                    values.update(packet_reference=None, envelope_reference=None)
                allowed = ((state.name, cause.name) in (("MATCH", "EXACT_EQUAL"),
                           ("MISMATCH", "EXACT_UNEQUAL"), ("NOT_EVALUATED", "FIELD_UNAVAILABLE"),
                           ("NOT_EVALUATED", "INVALID_REFERENCE_TYPE")))
                if allowed:
                    self.field_check(**values)
                else:
                    with self.assertRaises(ValueError):
                        self.field_check(**values)

    def test_candidate_enums_reject_strings_and_foreign_enums(self):
        for field, name, member in (("field_kind", "MatterFieldKind", "MATTER_ID"),
                                    ("state", "MatterFieldState", "MATCH"),
                                    ("cause", "MatterFieldCause", "EXACT_EQUAL")):
            foreign = Enum(name, {member: member})
            foreign.__module__ = CANDIDATE_MODULE
            for value in (member, None, True, foreign[member]):
                with self.assertRaises(TypeError):
                    self.field_check(**{field: value})

    def test_check_literal_equality_and_none_display_rules(self):
        for changes in (
            {"envelope_reference": "SYNTHETIC-OTHER"},
            {"state": self.subject.MatterFieldState.MISMATCH, "cause": self.subject.MatterFieldCause.EXACT_UNEQUAL},
            {"state": self.subject.MatterFieldState.NOT_EVALUATED,
             "cause": self.subject.MatterFieldCause.FIELD_UNAVAILABLE},
        ):
            with self.assertRaises(ValueError):
                self.field_check(**changes)
        for field in ("packet_reference", "envelope_reference", "audit_correlation_id"):
            with self.assertRaises(TypeError):
                self.field_check(**{field: 1})
            with self.assertRaises(ValueError):
                self.field_check(**{field: " "})

    def test_diagnostic_tuple_shape_order_and_duplicates_are_closed(self):
        result = self.diagnose(*self.arguments())
        class TupleSubclass(tuple):
            pass
        for value in (list(result.checks), None, TupleSubclass(result.checks)):
            with self.assertRaises(TypeError):
                self.diagnostic_record(result.prior_decision, value)
        for value in ((), result.checks[:2], result.checks + (result.checks[0],),
                      tuple(reversed(result.checks)), (result.checks[0],) * 3):
            with self.assertRaises(ValueError):
                self.diagnostic_record(result.prior_decision, value)

    def test_diagnostic_revalidates_each_check_field_and_correlation(self):
        mutations = (("field_kind", "MATTER_ID", TypeError), ("state", "MATCH", TypeError),
                     ("cause", "EXACT_EQUAL", TypeError), ("packet_reference", 1, TypeError),
                     ("envelope_reference", "SYNTHETIC-OTHER", ValueError),
                     ("audit_correlation_id", "SYNTHETIC-OTHER-CALL", ValueError))
        for field, value, error in mutations:
            result = self.diagnose(*self.arguments())
            object.__setattr__(result.checks[0], field, value)
            with self.assertRaises(error):
                self.diagnostic_record(result.prior_decision, result.checks)
        for field in CHECK_FIELDS:
            result = self.diagnose(*self.arguments())
            object.__delattr__(result.checks[0], field)
            with self.assertRaises(ValueError):
                self.diagnostic_record(result.prior_decision, result.checks)

    def test_foreign_and_subclass_diagnostic_checks_cannot_spoof_identity(self):
        result = self.diagnose(*self.arguments())
        foreign = type("MatterFieldCheck", (), {"__module__": CANDIDATE_MODULE})()
        with self.assertRaises(TypeError):
            self.diagnostic_record(result.prior_decision, (foreign,) + result.checks[1:])
        subclass = type("SyntheticCheckSubclass", (self.subject.MatterFieldCheck,), {})
        with self.assertRaises(TypeError):
            guarded_call("synthetic-subclass", subclass,
                         **{field: getattr(result.checks[0], field) for field in CHECK_FIELDS})

    def test_output_is_frozen_slotted_and_prior_fields_keep_identity(self):
        prior, packet, envelope = self.arguments()
        result = self.diagnose(prior, packet, envelope)
        self.assertFalse(hasattr(result, "__dict__"))
        self.assertFalse(hasattr(result.checks[0], "__dict__"))
        with self.assertRaises(dataclasses.FrozenInstanceError):
            result.prior_decision = self.prior()
        with self.assertRaises(dataclasses.FrozenInstanceError):
            result.checks[0].state = self.subject.MatterFieldState.MISMATCH
        for field in GATE_FIELDS:
            self.assertIs(getattr(result.prior_decision, field), getattr(prior, field))

    def test_extra_arguments_do_not_create_a_boundary_or_authority_surface(self):
        arguments = self.arguments()
        with self.assertRaises(TypeError):
            guarded_call("extra-argument", self.subject.diagnose_matter_fields, *arguments, ())
        with self.assertRaises(TypeError):
            guarded_call("extra-keyword", self.subject.diagnose_matter_fields, *arguments, source_bound=True)

    def test_partial_uninitialized_packet_is_not_valid_upstream_construction(self):
        prior, _, envelope = self.arguments()
        packet = object.__new__(self.contracts.TierBAuthorityPacketReference)
        result = self.diagnose(prior, packet, envelope)
        self.assertEqual(tuple(check.state.name for check in result.checks), ("NOT_EVALUATED",) * 3)
        self.assertEqual(tuple(check.cause.name for check in result.checks), ("FIELD_UNAVAILABLE",) * 3)
        self.assertIs(result.prior_decision, prior)
        self.assertFalse(hasattr(result, "valid_upstream_construction"))

    def test_selected_fields_do_not_validate_complete_packet_or_authority(self):
        arguments = self.arguments()
        object.__setattr__(arguments[1], "packet_sha256", "SYNTHETIC-NOT-A-HASH")
        object.__setattr__(arguments[1], "state", self.contracts.PacketState.REVOKED)
        object.__setattr__(arguments[2], "matter_authorization_reference", "")
        result = self.diagnose(*arguments)
        self.assertEqual(tuple(check.state.name for check in result.checks), ("MATCH",) * 3)
        self.assertIs(result.prior_decision, arguments[0])
        self.assertFalse(hasattr(result, "authority_validated"))
        self.assertIn("validate the complete\npacket/envelope", self.subject.__doc__)

    def test_static_candidate_excludes_gate_invocation_io_and_routing(self):
        assert_static_subject(self.subject_tree)
        self.assertNotIn(b"if __name__", self.subject_bytes)
        self.assertFalse(any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                             and node.func.id in ("GateDecision", "evaluate_identity_gate", "open")
                             for node in ast.walk(self.subject_tree)))

    def test_only_fixed_modules_loaded_without_package_initialization(self):
        self.assertEqual({name for name in sys.modules if name.startswith("route_b_c03.")}, {CONTRACTS_MODULE})
        self.assertIs(sys.modules["route_b_c03"], self.parent)
        self.assertEqual(self.parent.__path__, [])
        self.assertFalse(hasattr(self.parent, "__file__"))
        for name in ("DSP_004_NATIVE_CONTRACT_CANDIDATE_REV1", "DSP_004_EXPECTED_BASELINE_READER_CANDIDATE_REV1",
                     "DSP_004_ELIGIBLE_DECISION_COMBINER_CANDIDATE_REV1"):
            self.assertNotIn(name, sys.modules)

    def test_guard_self_test_blocks_open_before_access(self):
        before = len(_SELF_TEST_EVENTS)
        with self.assertRaises(ForbiddenCandidateSideEffect):
            guarded_call("guard-self-test", builtins.open, str(ROOT / SUBJECT_RELATIVE), "rb")
        self.assertEqual(_SELF_TEST_EVENTS[before:], [{"phase": "guard-self-test", "event": "open"}])


def main():
    global _HASH_AFTER
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(MatterFieldDiagnosticCandidateTests)
    result = None
    postcheck_error = None
    try:
        result = unittest.TextTestRunner(verbosity=2).run(suite)
    finally:
        try:
            verify_fixed_inputs()
            _HASH_AFTER = True
        except Exception as error:
            postcheck_error = f"{type(error).__name__}: {error}"
        print(json.dumps({
            "diagnostic": "DSP004_MATTER_FIELDS_LOCAL_SYNTHETIC_ONLY",
            "candidate_module": CANDIDATE_MODULE,
            "subject_sha256": SUBJECT_SHA256,
            "actual_runtime": sys.version,
            "actual_executable": sys.executable,
            "isolation_flags": {"isolated": sys.flags.isolated, "no_site": sys.flags.no_site,
                                "dont_write_bytecode": sys.flags.dont_write_bytecode},
            "hash_before": _HASH_BEFORE, "hash_after": _HASH_AFTER, "postcheck_error": postcheck_error,
            "fixed_inputs": [{"path": path, "sha256": sha} for path, sha in PRESERVED_INPUTS],
            "test_methods_planned": len(loader.getTestCaseNames(MatterFieldDiagnosticCandidateTests)),
            "test_methods_run": result.testsRun if result is not None else 0,
            "failures": len(result.failures) if result is not None else None,
            "errors": len(result.errors) if result is not None else None,
            "synthetic_diagnostic_success": bool(result and result.wasSuccessful() and _HASH_AFTER),
            "literal_field_patterns_checked": _CASE_COUNT,
            "diagnostic_calls_observed": len(_GATE_CONSTRUCTOR_COUNTS),
            "python_gate_constructor_calls_during_diagnostic": sum(_GATE_CONSTRUCTOR_COUNTS),
            "candidate_blocked_audit_events": _BLOCKED_EVENTS,
            "intentional_guard_self_test_events": _SELF_TEST_EVENTS,
            "audit_profile_limit": "FINITE DIAGNOSTIC; NOT COMPLETE ISOLATION OR ALLOCATION PROOF",
            "same_call_provenance": "NOT ESTABLISHED", "source_admission": "NOT ESTABLISHED",
            "actual_capture": "NOT PERFORMED", "gate_invocation": "NOT PERFORMED",
            "old_gate_branch_execution_coverage": "NOT ESTABLISHED",
            "context_boundary_observations": "NOT GENERATED", "aggregate_matter_verdict": "NOT ISSUED",
            "full_packet_envelope_validation": "NOT PERFORMED",
            "formal_wp008_validation": "NOT PERFORMED", "approved_integration": "NOT ESTABLISHED",
            "package_initialization": "NOT EXECUTED",
            "old_environment_inventory": "3.12.13; UNCHANGED; NOT CURRENT RUNTIME ACCEPTANCE",
            "persistent_evidence_output": "NOT WRITTEN; STDOUT ONLY",
        }, ensure_ascii=False))
    return 0 if result and result.wasSuccessful() and _HASH_AFTER else 1


if __name__ == "__main__":
    sys.exit(main())
