"""Console-only local synthetic diagnostic for the DSP-004 denial preserver.

Run this authorized batch with the fixed local Python 3.12.14 and -I -S -B.
Load hash-pinned contracts declarations under route_b_c03.contracts without
running package initialization. No existing gate, reader, combiner, boundary
candidate, provider, or mapping module is imported or executed. Source reads
are restricted to the fixed list below and occur outside guarded calls.

All objects and reason examples are synthetic. Their successful preservation
does not establish old-gate branch execution, trusted sources, same-call origin,
actual capture, full WP-008 validation, integration, or an isolation verdict.
The finite audit hook and Python constructor profiler are diagnostic checks,
not complete security sandboxes or proof of no I/O/allocation. The historical
3.12.13 inventory is not rewritten or accepted as the current runtime.
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
CANDIDATE_MODULE = "DSP_004_DENIED_DECISION_PRESERVER_CANDIDATE_REV1"
SUBJECT_RELATIVE = "validation/route_b_c03/wp_008/DSP_004_DENIED_DECISION_PRESERVER_CANDIDATE_REV1.py"
SUBJECT_SHA256 = "61D424C35D262C3CC9FE03863F4BCB4D39FF96E248E5A7A08B8EAE6F8D598245"
EXPECTED_RUNTIME = (3, 12, 14)
EXPECTED_EXECUTABLE = ROOT / ".venv-validation/Scripts/python.exe"
PRESERVED_INPUTS = (
    ("scripts/phase2_runtime/route_b_c03/contracts.py",
     "7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4"),
    ("scripts/phase2_runtime/route_b_c03/identity_gate.py",
     "9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445"),
    ("docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PREPARATION_DESIGN_RECORD_REV1.md",
     "DB39150AE0428A452B2BEBE958A4B7DD91F4DE8A3790B0BC374FAEA4693868F4"),
    ("validation/route_b_c03/wp_008/DSP_004_EXPECTED_BASELINE_READER_CANDIDATE_REV1.py",
     "AE1389EDA1C3B9129A0546DA5764C1F68A6B0193A22DA3431CAA89BAB8DC0727"),
    ("validation/route_b_c03/wp_008/test_dsp_004_expected_baseline_reader_candidate_rev1.py",
     "6757A99AD6A7A4461B8D52345855FDE675DBB1692D312F22BB2E27B0F9C335F9"),
    ("validation/route_b_c03/wp_008/DSP_004_NATIVE_CONTRACT_CANDIDATE_REV1.py",
     "1544B7D8101493072E9BCA5C23B09C3C811F1B52CB1E9F5A8D73C976576FC312"),
    ("validation/route_b_c03/wp_008/test_dsp_004_native_contract_candidate_rev1.py",
     "8F70F0D4A458B8C5543033D10480D7C6BEE3684F8CBECDFD5B726FB2558F9CF8"),
    ("validation/route_b_c03/wp_008/DSP_004_ELIGIBLE_DECISION_COMBINER_CANDIDATE_REV1.py",
     "95156DEAD051799DA6361216EA66007F5B3FFF10257A886C0225AD3E95FDE9D6"),
    ("validation/route_b_c03/wp_008/test_dsp_004_eligible_decision_combiner_candidate_rev1.py",
     "F649617F23E4A47934F03AA4B8B0C09952F81DDEBB9D164B3CE648B8E1ABF126"),
    (".venv-validation/Scripts/python.exe",
     "560B9EF7D856608AB8DA02DED2DC8A1951AD1F424C382C0EC6A698874165A18E"),
    (".venv-validation/pyvenv.cfg",
     "7AFB3C331994D8D1CB462B711254E30BAE372DC8A28F2C485AFA79B030775461"),
    ("validation/route_b_c03/wp_008/ENVIRONMENT_MANIFEST.md",
     "EFCF1A783199F58387BDBB0704563ED943A5E6A3E319A04CE6D58E57FC5CA531"),
)
GATE_FIELDS = ("state", "reason_code", "audit_correlation_id", "permitted_write_namespaces")
DENIED_STATES = ("BLOCKED", "REJECTED")
OUT_OF_SCOPE_STATES = (
    "INVOCATION_RECEIVED", "GATE_CHECKING", "ELIGIBLE_FOR_MAPPING", "MAPPING",
    "MAPPING_CANDIDATE", "QUARANTINED", "HUMAN_REVIEW_PENDING",
)
# Handwritten reason-text samples: this is NOT old-gate branch coverage.
REASON_EXAMPLES = (
    ("BLOCKED", "BLOCKED — KILL ACTIVE"),
    ("BLOCKED", "BLOCKED — CAPABILITY NOT ACTIVE"),
    ("BLOCKED", "BLOCKED — AUTHORITY FAILURE"),
    ("BLOCKED", "BLOCKED — VERSION FAILURE"),
    ("BLOCKED", "BLOCKED — CAPABILITY IDENTITY FAILURE"),
    ("BLOCKED", "BLOCKED — DOMAIN IDENTITY FAILURE"),
    ("BLOCKED", "BLOCKED — TIER B AUTHORITY REQUIRED"),
    ("BLOCKED", "BLOCKED — INPUT SET IDENTITY FAILURE"),
    ("BLOCKED", "BLOCKED — AUTHORITY BINDING FAILURE"),
    ("REJECTED", "REJECTED — ISOLATION FAILURE"),
    ("REJECTED", "REJECTED — SCOPE FAILURE"),
    ("REJECTED", "REJECTED — OUTPUT BOUNDARY FAILURE"),
)
_PHASE = None
_BLOCKED_EVENTS = []
_SELF_TEST_EVENTS = []
_CONSTRUCTOR_COUNTS = []
_HASH_BEFORE = False
_HASH_AFTER = False
_EXAMPLE_COUNT = 0
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
        raise RuntimeError("Read outside the fixed local input list")
    if _PHASE is not None:
        raise RuntimeError("Controlled hash reads must be outside guarded calls")
    payload = (ROOT / relative).read_bytes()
    actual_sha = hashlib.sha256(payload).hexdigest().upper()
    if actual_sha != expected_sha:
        raise RuntimeError(f"Fixed SHA mismatch: {relative}: {actual_sha}")
    return payload


def verify_fixed_inputs():
    for relative, expected_sha in PRESERVED_INPUTS:
        read_fixed_bytes(relative, expected_sha)
    read_fixed_bytes(SUBJECT_RELATIVE, SUBJECT_SHA256)


def assert_static_subject(tree):
    expected_imports = [(CONTRACTS_MODULE, ("GateDecision", "InvocationState"))]
    imports = []
    allowed_calls = {"type", "TypeError", "ValueError", "_require_native_text"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            raise RuntimeError("Plain import is not allowed")
        if isinstance(node, ast.ImportFrom):
            if node.level or any(alias.asname for alias in node.names):
                raise RuntimeError("Relative or aliased import is not allowed")
            imports.append((node.module, tuple(alias.name for alias in node.names)))
        if isinstance(node, (ast.ClassDef, ast.AsyncFunctionDef, ast.Lambda)):
            raise RuntimeError("Unlisted executable or replacement-class surface")
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id not in allowed_calls:
                    raise RuntimeError(f"Unlisted call: {node.func.id}")
            elif isinstance(node.func, ast.Attribute):
                if node.func.attr != "isspace" or node.args or node.keywords:
                    raise RuntimeError("Unlisted attribute call")
            else:
                raise RuntimeError("Indirect call is not allowed")
    if imports != expected_imports:
        raise RuntimeError("Imports differ from fixed whitelist")
    functions = tuple(node.name for node in tree.body if isinstance(node, ast.FunctionDef))
    if functions != ("_require_native_text", "preserve_denied_decision"):
        raise RuntimeError("Callable surface differs from fixed whitelist")
    for node in tree.body:
        if not isinstance(node, (ast.ImportFrom, ast.FunctionDef)):
            if not (isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant)
                    and type(node.value.value) is str):
                raise RuntimeError("Unlisted module-level execution")


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


class DeniedDecisionPreserverCandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global _HASH_BEFORE
        if sys.version_info[:3] != EXPECTED_RUNTIME:
            raise RuntimeError("This batch is bound to observed Python 3.12.14")
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
            if name == "route_b_c03" or name.startswith("route_b_c03.") or name == CANDIDATE_MODULE:
                raise RuntimeError(f"Unexpected preloaded module: {name}")
        # Stdlib declarations needed by contracts are already imported above.
        sys.addaudithook(audit_guard)
        cls.parent = types.ModuleType("route_b_c03")
        cls.parent.__path__ = []
        cls.parent.__package__ = "route_b_c03"
        sys.modules["route_b_c03"] = cls.parent
        cls.contracts = load_declared_module(
            CONTRACTS_MODULE, PRESERVED_INPUTS[0][0], read_fixed_bytes(*PRESERVED_INPUTS[0]),
        )
        cls.parent.contracts = cls.contracts
        cls.subject = load_declared_module(CANDIDATE_MODULE, SUBJECT_RELATIVE, cls.subject_bytes)

    def setUp(self):
        self.events_before = len(_BLOCKED_EVENTS)

    def tearDown(self):
        self.assertEqual(len(_BLOCKED_EVENTS), self.events_before)
        self.assertIsNone(_PHASE)

    def prior(self, **changes):
        values = dict(state=self.contracts.InvocationState.BLOCKED,
                      reason_code="SYNTHETIC REASON — 完整原文  ",
                      audit_correlation_id="SYNTHETIC-CALL-001",
                      permitted_write_namespaces=())
        values.update(changes)
        return guarded_call("synthetic-prior-construction", self.contracts.GateDecision, **values)

    def snapshot(self, prior):
        if type(prior) is not self.contracts.GateDecision:
            return id(prior), ()
        return id(prior), tuple((field, id(value), type(value)) for field in GATE_FIELDS
                               for value in (getattr(prior, field, _MISSING),))

    def preserve(self, prior):
        before = self.snapshot(prior)
        constructor_code = self.contracts.GateDecision.__init__.__code__
        observed = []
        old_profile = sys.getprofile()
        if old_profile is not None:
            raise RuntimeError("Unexpected profiler")

        def observer(frame, event, argument):
            if event == "call" and frame.f_code is constructor_code:
                observed.append(id(frame.f_locals["self"]))

        sys.setprofile(observer)
        try:
            return guarded_call("preserver-call", self.subject.preserve_denied_decision, prior)
        finally:
            sys.setprofile(old_profile)
            _CONSTRUCTOR_COUNTS.append(len(observed))
            self.assertEqual(len(observed), 0, "Preserver constructed a GateDecision")
            self.assertEqual(self.snapshot(prior), before, "Preserver changed an input field")

    def reject(self, error, prior):
        with self.assertRaises(error):
            self.preserve(prior)

    def test_runtime_flags_and_exact_local_executable(self):
        self.assertEqual(sys.version_info[:3], EXPECTED_RUNTIME)
        self.assertEqual(Path(sys.executable).resolve(), EXPECTED_EXECUTABLE.resolve())
        self.assertEqual((sys.flags.isolated, sys.flags.no_site, sys.flags.dont_write_bytecode), (1, 1, 1))

    def test_exact_existing_contract_class_identity_and_fields(self):
        self.assertIs(self.subject.GateDecision, self.contracts.GateDecision)
        self.assertIs(self.subject.InvocationState, self.contracts.InvocationState)
        self.assertEqual(self.contracts.GateDecision.__module__, CONTRACTS_MODULE)
        self.assertEqual(self.contracts.InvocationState.__module__, CONTRACTS_MODULE)
        self.assertEqual(tuple(field.name for field in dataclasses.fields(self.contracts.GateDecision)),
                         GATE_FIELDS)

    def test_signature_only_has_required_prior_and_native_return_type(self):
        signature = inspect.signature(self.subject.preserve_denied_decision)
        self.assertEqual(tuple(signature.parameters), ("prior",))
        self.assertIs(signature.parameters["prior"].default, inspect.Parameter.empty)
        self.assertIs(signature.parameters["prior"].annotation, self.contracts.GateDecision)
        self.assertIs(signature.return_annotation, self.contracts.GateDecision)
        self.assertEqual(self.subject.preserve_denied_decision.__module__, CANDIDATE_MODULE)

    def test_both_denied_states_return_the_identical_object_and_field_references(self):
        for state in DENIED_STATES:
            prior = self.prior(state=self.contracts.InvocationState[state])
            result = self.preserve(prior)
            self.assertIs(result, prior)
            for field in GATE_FIELDS:
                self.assertIs(getattr(result, field), getattr(prior, field))

    def test_twelve_reason_samples_are_literal_metadata_not_gate_execution(self):
        global _EXAMPLE_COUNT
        self.assertEqual(len(REASON_EXAMPLES), 12)
        for state_name, reason in REASON_EXAMPLES:
            with self.subTest(state=state_name, reason=reason):
                prior = self.prior(state=self.contracts.InvocationState[state_name], reason_code=reason)
                self.assertIs(self.preserve(prior), prior)
                self.assertEqual(prior.reason_code, reason)
                _EXAMPLE_COUNT += 1
        self.assertEqual(_EXAMPLE_COUNT, 12)

    def test_reason_meaning_never_changes_state_or_selects_a_branch(self):
        for state_name in DENIED_STATES:
            for reason in ("SYNTHETIC UNKNOWN", "ELIGIBLE — SYNTHETIC TEXT ONLY",
                           "REJECTED — ISOLATION FAILURE", "SYNTHETIC actor-only mismatch",
                           "SYNTHETIC project/session/provider labels are not observations"):
                prior = self.prior(state=self.contracts.InvocationState[state_name], reason_code=reason)
                self.assertIs(self.preserve(prior), prior)
                self.assertIs(prior.state, self.contracts.InvocationState[state_name])

    def test_whitespace_unicode_and_full_reason_are_preserved_without_normalization(self):
        for state_name in DENIED_STATES:
            for reason, correlation in (
                ("  SYNTHETIC 原因  ", "  SYNTHETIC-CALL  "),
                ("SYNTHETIC-É", "SYNTHETIC-E\u0301"),
                ("SYNTHETIC-E\u0301\nTAIL", "\tSYNTHETIC-关联\u3000"),
            ):
                prior = self.prior(state=self.contracts.InvocationState[state_name],
                                   reason_code=reason, audit_correlation_id=correlation)
                self.assertIs(self.preserve(prior), prior)
                self.assertEqual((prior.reason_code, prior.audit_correlation_id), (reason, correlation))

    def test_non_native_prior_objects_are_rejected_without_conversion(self):
        for value in (None, {}, [], (), "SYNTHETIC", 1, True):
            self.reject(TypeError, value)

    def test_foreign_same_named_same_module_gate_fixture_is_rejected(self):
        fixture = type("ForeignGateFixture", (), {"__module__": CONTRACTS_MODULE})
        fixture.__name__ = "GateDecision"
        prior = self.prior()
        foreign = fixture()
        for field in GATE_FIELDS:
            setattr(foreign, field, getattr(prior, field))
        self.reject(TypeError, foreign)

    def test_gate_subclass_is_rejected(self):
        class ForeignSubclass(self.contracts.GateDecision):
            pass
        prior = self.prior()
        foreign = ForeignSubclass(**{field: getattr(prior, field) for field in GATE_FIELDS})
        self.reject(TypeError, foreign)

    def test_state_rejects_string_none_bool_integer_and_wrong_enum(self):
        wrong_enum = Enum("OtherState", {"BLOCKED": "BLOCKED"})
        for value in ("BLOCKED", "REJECTED", None, True, 1, wrong_enum.BLOCKED):
            self.reject(TypeError, self.prior(state=value))

    def test_foreign_same_named_invocation_enum_is_rejected(self):
        foreign = Enum("ForeignInvocationState", {"BLOCKED": "BLOCKED", "REJECTED": "REJECTED"})
        foreign.__name__ = "InvocationState"
        foreign.__module__ = CONTRACTS_MODULE
        for state in foreign:
            self.reject(TypeError, self.prior(state=state))

    def test_all_seven_out_of_scope_native_states_raise_value_error(self):
        self.assertEqual(set(self.contracts.InvocationState.__members__),
                         set(DENIED_STATES + OUT_OF_SCOPE_STATES))
        self.assertEqual(len(OUT_OF_SCOPE_STATES), 7)
        for state_name in OUT_OF_SCOPE_STATES:
            self.reject(ValueError, self.prior(state=self.contracts.InvocationState[state_name]))

    def test_reason_and_correlation_require_exact_native_string(self):
        class StringSubclass(str):
            pass
        for state_name in DENIED_STATES:
            for field in ("reason_code", "audit_correlation_id"):
                for value in (None, True, 1, b"SYNTHETIC", [], {}, StringSubclass("SYNTHETIC")):
                    self.reject(TypeError, self.prior(
                        state=self.contracts.InvocationState[state_name], **{field: value},
                    ))

    def test_empty_or_whitespace_text_is_not_repaired(self):
        for state_name in DENIED_STATES:
            for field in ("reason_code", "audit_correlation_id"):
                for value in ("", " ", "\t\n\r", "\u3000", "\u00a0"):
                    self.reject(ValueError, self.prior(
                        state=self.contracts.InvocationState[state_name], **{field: value},
                    ))

    def test_write_namespaces_require_exact_native_tuple(self):
        class TupleSubclass(tuple):
            pass
        for state_name in DENIED_STATES:
            for value in (None, [], {}, "", 1, iter(()), TupleSubclass(())):
                self.reject(TypeError, self.prior(state=self.contracts.InvocationState[state_name],
                                                 permitted_write_namespaces=value))

    def test_nonempty_native_write_tuple_is_rejected(self):
        for state_name in DENIED_STATES:
            for value in (("SYNTHETIC",), (None,), ((),), ("SYNTHETIC-A", "SYNTHETIC-B")):
                self.reject(ValueError, self.prior(state=self.contracts.InvocationState[state_name],
                                                 permitted_write_namespaces=value))

    def test_each_missing_field_and_uninitialized_object_raise_value_error(self):
        for state_name in DENIED_STATES:
            for field in GATE_FIELDS:
                prior = self.prior(state=self.contracts.InvocationState[state_name])
                object.__delattr__(prior, field)
                self.reject(ValueError, prior)
        self.reject(ValueError, object.__new__(self.contracts.GateDecision))

    def test_low_level_field_changes_are_revalidated_not_repaired(self):
        for field, value, error in (
            ("state", "BLOCKED", TypeError),
            ("state", self.contracts.InvocationState.ELIGIBLE_FOR_MAPPING, ValueError),
            ("reason_code", "", ValueError), ("reason_code", 1, TypeError),
            ("audit_correlation_id", "\u3000", ValueError),
            ("audit_correlation_id", b"SYNTHETIC", TypeError),
            ("permitted_write_namespaces", [], TypeError),
            ("permitted_write_namespaces", ("SYNTHETIC",), ValueError),
        ):
            prior = self.prior()
            object.__setattr__(prior, field, value)
            self.reject(error, prior)

    def test_valid_denial_swap_remains_literal_not_historical_evidence(self):
        prior = self.prior()
        object.__setattr__(prior, "state", self.contracts.InvocationState.REJECTED)
        object.__setattr__(prior, "reason_code", "SYNTHETIC CHANGED BEFORE CALL")
        self.assertIs(self.preserve(prior), prior)
        self.assertEqual(prior.reason_code, "SYNTHETIC CHANGED BEFORE CALL")

    def test_no_boundary_argument_is_accepted_or_observed(self):
        class MustNotBeObserved:
            def __iter__(self):
                raise AssertionError("Unexpected observation")

        prior = self.prior()
        before = self.snapshot(prior)
        with self.assertRaises(TypeError):
            guarded_call("unexpected-argument", self.subject.preserve_denied_decision,
                         prior, MustNotBeObserved())
        with self.assertRaises(TypeError):
            guarded_call("unexpected-keyword", self.subject.preserve_denied_decision,
                         prior, checks=MustNotBeObserved())
        self.assertEqual(self.snapshot(prior), before)

    def test_valid_result_keeps_original_frozen_slotted_contract(self):
        result = self.preserve(self.prior())
        self.assertFalse(hasattr(result, "__dict__"))
        with self.assertRaises(dataclasses.FrozenInstanceError):
            result.reason_code = "SYNTHETIC CHANGED"

    def test_candidate_static_calls_exclude_construction_gate_and_observation(self):
        assert_static_subject(self.subject_tree)
        self.assertNotIn(b"if __name__", self.subject_bytes)
        self.assertFalse(any(isinstance(node, ast.ClassDef) for node in ast.walk(self.subject_tree)))
        self.assertFalse(any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                             and node.func.id == "GateDecision" for node in ast.walk(self.subject_tree)))

    def test_only_contracts_module_loaded_and_package_not_initialized(self):
        self.assertEqual({name for name in sys.modules if name.startswith("route_b_c03.")},
                         {CONTRACTS_MODULE})
        for name in ("DSP_004_NATIVE_CONTRACT_CANDIDATE_REV1",
                     "DSP_004_EXPECTED_BASELINE_READER_CANDIDATE_REV1",
                     "DSP_004_ELIGIBLE_DECISION_COMBINER_CANDIDATE_REV1"):
            self.assertNotIn(name, sys.modules)
        self.assertIs(sys.modules["route_b_c03"], self.parent)
        self.assertEqual(self.parent.__path__, [])
        self.assertFalse(hasattr(self.parent, "__file__"))
        self.assertIs(sys.modules[CONTRACTS_MODULE], self.contracts)
        self.assertIs(sys.modules[CANDIDATE_MODULE], self.subject)

    def test_guard_self_test_blocks_open_before_access(self):
        before = len(_SELF_TEST_EVENTS)
        with self.assertRaises(ForbiddenCandidateSideEffect):
            guarded_call("guard-self-test", builtins.open, str(ROOT / SUBJECT_RELATIVE), "rb")
        self.assertEqual(_SELF_TEST_EVENTS[before:], [{"phase": "guard-self-test", "event": "open"}])


def main():
    global _HASH_AFTER
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(DeniedDecisionPreserverCandidateTests)
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
            "diagnostic": "DSP004_DENIED_PRESERVER_LOCAL_SYNTHETIC_ONLY",
            "candidate_module": CANDIDATE_MODULE,
            "subject_sha256": SUBJECT_SHA256,
            "actual_runtime": sys.version,
            "actual_executable": sys.executable,
            "isolation_flags": {
                "isolated": sys.flags.isolated,
                "no_site": sys.flags.no_site,
                "dont_write_bytecode": sys.flags.dont_write_bytecode,
            },
            "hash_before": _HASH_BEFORE,
            "hash_after": _HASH_AFTER,
            "postcheck_error": postcheck_error,
            "fixed_inputs": [{"path": path, "sha256": sha} for path, sha in PRESERVED_INPUTS],
            "test_methods_planned": len(loader.getTestCaseNames(DeniedDecisionPreserverCandidateTests)),
            "test_methods_run": result.testsRun if result is not None else 0,
            "failures": len(result.failures) if result is not None else None,
            "errors": len(result.errors) if result is not None else None,
            "synthetic_diagnostic_success": bool(result and result.wasSuccessful() and _HASH_AFTER),
            "synthetic_reason_examples_checked": _EXAMPLE_COUNT,
            "preserver_calls_observed": len(_CONSTRUCTOR_COUNTS),
            "python_gate_constructor_calls_during_preserver": sum(_CONSTRUCTOR_COUNTS),
            "candidate_blocked_audit_events": _BLOCKED_EVENTS,
            "intentional_guard_self_test_events": _SELF_TEST_EVENTS,
            "audit_profile_limit": "FINITE DIAGNOSTIC; NOT COMPLETE ISOLATION OR ALLOCATION PROOF",
            "source_admission": "NOT ESTABLISHED",
            "actual_capture": "NOT PERFORMED",
            "gate_invocation": "NOT PERFORMED",
            "boundary_observations": "NOT GENERATED",
            "matter_actor_diagnosis": "NOT PERFORMED",
            "old_gate_branch_execution_coverage": "NOT ESTABLISHED",
            "formal_wp008_validation": "NOT PERFORMED",
            "approved_integration": "NOT ESTABLISHED",
            "same_call_provenance": "NOT ESTABLISHED",
            "package_initialization": "NOT EXECUTED",
            "old_environment_inventory": "3.12.13; UNCHANGED; NOT CURRENT RUNTIME ACCEPTANCE",
            "persistent_evidence_output": "NOT WRITTEN; STDOUT ONLY",
        }, ensure_ascii=False))
    return 0 if result and result.wasSuccessful() and _HASH_AFTER else 1


if __name__ == "__main__":
    sys.exit(main())
