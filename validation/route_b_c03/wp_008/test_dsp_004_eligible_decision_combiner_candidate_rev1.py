"""Console-only synthetic diagnostic for the independent DSP-004 combiner.

Future separately authorized invocation uses the fixed local Python 3.12.14
executable with -I -S -B. Merely creating this script does not execute it.
The fixed existing contracts source is compiled under route_b_c03.contracts;
an empty in-process parent prevents package initialization. No replacement
GateDecision or InvocationState is defined. Foreign fixtures only test rejection.
The separately bound boundary candidate retains its declared module identity.
No identity gate, expected reader, provider, mapping, or package initializer is
imported or called. No sys.path change or persistent output is made.

Every state, cause, prior, correlation, and source ID here is synthetic. This
does not establish source admission, trustworthy observations, same-call origin,
real gate execution, approved integration, or formal WP-008 validation. The
audit hook and Python-level constructor counter are finite diagnostics, not a
comprehensive runtime-isolation or allocation-proof mechanism. The historical
3.12.13 inventory remains unchanged and is not accepted as the actual runtime.
"""

import __future__
import ast
import builtins
import dataclasses
from enum import Enum
import hashlib
import inspect
import itertools
import json
from pathlib import Path
import re
import sys
import types
import typing
import unittest


ROOT = Path(__file__).resolve().parents[3]
CONTRACTS_MODULE = "route_b_c03.contracts"
NATIVE_MODULE = "DSP_004_NATIVE_CONTRACT_CANDIDATE_REV1"
CANDIDATE_MODULE = "DSP_004_ELIGIBLE_DECISION_COMBINER_CANDIDATE_REV1"
SUBJECT_RELATIVE = "validation/route_b_c03/wp_008/DSP_004_ELIGIBLE_DECISION_COMBINER_CANDIDATE_REV1.py"
SUBJECT_SHA256 = "95156DEAD051799DA6361216EA66007F5B3FFF10257A886C0225AD3E95FDE9D6"
EXPECTED_RUNTIME = (3, 12, 14)
EXPECTED_EXECUTABLE = ROOT / ".venv-validation/Scripts/python.exe"
PRESERVED_INPUTS = (
    ("scripts/phase2_runtime/route_b_c03/contracts.py",
     "7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4"),
    ("scripts/phase2_runtime/route_b_c03/identity_gate.py",
     "9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445"),
    ("validation/route_b_c03/wp_008/DSP_004_EXPECTED_BASELINE_READER_CANDIDATE_REV1.py",
     "AE1389EDA1C3B9129A0546DA5764C1F68A6B0193A22DA3431CAA89BAB8DC0727"),
    ("validation/route_b_c03/wp_008/test_dsp_004_expected_baseline_reader_candidate_rev1.py",
     "6757A99AD6A7A4461B8D52345855FDE675DBB1692D312F22BB2E27B0F9C335F9"),
    ("docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PREPARATION_DESIGN_RECORD_REV1.md",
     "DB39150AE0428A452B2BEBE958A4B7DD91F4DE8A3790B0BC374FAEA4693868F4"),
    ("validation/route_b_c03/wp_008/DSP_004_NATIVE_CONTRACT_CANDIDATE_REV1.py",
     "1544B7D8101493072E9BCA5C23B09C3C811F1B52CB1E9F5A8D73C976576FC312"),
    ("validation/route_b_c03/wp_008/test_dsp_004_native_contract_candidate_rev1.py",
     "8F70F0D4A458B8C5543033D10480D7C6BEE3684F8CBECDFD5B726FB2558F9CF8"),
    (".venv-validation/Scripts/python.exe",
     "560B9EF7D856608AB8DA02DED2DC8A1951AD1F424C382C0EC6A698874165A18E"),
    (".venv-validation/pyvenv.cfg",
     "7AFB3C331994D8D1CB462B711254E30BAE372DC8A28F2C485AFA79B030775461"),
    ("validation/route_b_c03/wp_008/ENVIRONMENT_MANIFEST.md",
     "EFCF1A783199F58387BDBB0704563ED943A5E6A3E319A04CE6D58E57FC5CA531"),
)
GATE_FIELDS = ("state", "reason_code", "audit_correlation_id", "permitted_write_namespaces")
CHECK_FIELDS = (
    "boundary", "state", "cause", "audit_correlation_id",
    "expected_source_id", "actual_source_id",
)
ELIGIBLE_PAIRS = (
    ("MATCH", "EXACT_EQUAL"),
    ("MISMATCH", "EXACT_UNEQUAL"),
    ("UNBOUND", "SOURCE_UNBOUND"),
    ("UNBOUND", "INVALID_REFERENCE_TYPE"),
)
ALLOWED_PAIRS = ELIGIBLE_PAIRS + (("NOT_EVALUATED", "PRIOR_DENIAL"),)

# Independent handwritten oracle, not a call to any candidate implementation.
# Dimensions are PROJECT, SESSION, PROVIDER; each index uses ELIGIBLE_PAIRS.
# A=all MATCH, P/S/V=one mismatch, T=multiple, U=source unbound, I=invalid.
ORACLE_CUBE = (
    (("A", "V", "U", "I"), ("S", "T", "U", "I"),
     ("U", "U", "U", "I"), ("I", "I", "I", "I")),
    (("P", "T", "U", "I"), ("T", "T", "U", "I"),
     ("U", "U", "U", "I"), ("I", "I", "I", "I")),
    (("U", "U", "U", "I"), ("U", "U", "U", "I"),
     ("U", "U", "U", "I"), ("I", "I", "I", "I")),
    (("I", "I", "I", "I"), ("I", "I", "I", "I"),
     ("I", "I", "I", "I"), ("I", "I", "I", "I")),
)
ORACLE_OUTCOMES = {
    "I": ("BLOCKED", "BLOCKED — CONTEXT REFERENCE INVALID"),
    "U": ("BLOCKED", "BLOCKED — CONTEXT SOURCE UNBOUND"),
    "T": ("REJECTED", "REJECTED — MULTIPLE CONTEXT MISMATCHES"),
    "P": ("REJECTED", "REJECTED — PROJECT CONTEXT MISMATCH"),
    "S": ("REJECTED", "REJECTED — SESSION CONTEXT MISMATCH"),
    "V": ("REJECTED", "REJECTED — PROVIDER CONTEXT MISMATCH"),
}
EXPECTED_IMPORTS = (
    (CONTRACTS_MODULE, ("GateDecision", "InvocationState")),
    (NATIVE_MODULE, (
        "BoundaryCheck", "BoundaryCheckCause", "BoundaryCheckState",
        "validate_boundary_check_sequence",
    )),
)
ALLOWED_DIRECT_CALLS = frozenset({
    "type", "TypeError", "ValueError", "_require_native_text", "_validate_prior",
    "validate_boundary_check_sequence", "any", "tuple", "sum", "GateDecision",
})
FORBIDDEN_MODULES = (
    "route_b_c03.identity_gate", "route_b_c03.expected_reader",
    "route_b_c03.provider", "route_b_c03.mapping",
    "DSP_004_EXPECTED_BASELINE_READER_CANDIDATE_REV1",
)
_GUARD_PHASE = None
_CANDIDATE_BLOCKED_EVENTS = []
_GUARD_SELF_TEST_EVENTS = []
_CONSTRUCTOR_COUNTS = []
_ORACLE_CASE_COUNT = 0
_NOT_EVALUATED_CASE_COUNT = 0
_HASH_BEFORE = False
_HASH_AFTER = False
_BOOTSTRAP_COMPLETE = False
_MISSING = object()


class ForbiddenCandidateSideEffect(RuntimeError):
    pass


def audit_guard(event, args):
    if _GUARD_PHASE is not None and (
        event in ("open", "import")
        or event.startswith(("os.", "socket.", "subprocess.", "ctypes.", "winreg."))
    ):
        record = {"phase": _GUARD_PHASE, "event": event}
        if _GUARD_PHASE == "intentional-guard-self-test":
            _GUARD_SELF_TEST_EVENTS.append(record)
        else:
            _CANDIDATE_BLOCKED_EVENTS.append(record)
        raise ForbiddenCandidateSideEffect(event)


def guarded_call(phase, function, *args, **kwargs):
    global _GUARD_PHASE
    if _GUARD_PHASE is not None:
        raise RuntimeError("Nested guarded calls are not permitted")
    _GUARD_PHASE = phase
    try:
        return function(*args, **kwargs)
    finally:
        _GUARD_PHASE = None


def read_fixed_bytes(relative, expected_sha):
    if (relative, expected_sha) not in PRESERVED_INPUTS + ((SUBJECT_RELATIVE, SUBJECT_SHA256),):
        raise RuntimeError("Read outside the fixed local input list")
    if _GUARD_PHASE is not None:
        raise RuntimeError("Controlled hash reads must remain outside the candidate guard")
    payload = (ROOT / relative).read_bytes()
    actual_sha = hashlib.sha256(payload).hexdigest().upper()
    if actual_sha != expected_sha:
        raise RuntimeError(f"Fixed input mismatch: {relative}: {actual_sha}")
    return payload


def verify_fixed_inputs():
    for relative, expected_sha in PRESERVED_INPUTS:
        read_fixed_bytes(relative, expected_sha)
    read_fixed_bytes(SUBJECT_RELATIVE, SUBJECT_SHA256)


def assert_static_subject(tree, payload):
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            raise RuntimeError("Unlisted plain import")
        if isinstance(node, ast.ImportFrom):
            if node.level or any(alias.asname is not None for alias in node.names):
                raise RuntimeError("Relative or aliased import is not allowed")
            imports.append((node.module, tuple(alias.name for alias in node.names)))
        if isinstance(node, (ast.ClassDef, ast.AsyncFunctionDef, ast.Lambda)):
            raise RuntimeError("Unlisted class or executable callable form")
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id not in ALLOWED_DIRECT_CALLS:
                    raise RuntimeError(f"Unlisted direct call: {node.func.id}")
            elif isinstance(node.func, ast.Attribute):
                if node.func.attr != "isspace" or node.args or node.keywords:
                    raise RuntimeError("Unlisted attribute call")
            else:
                raise RuntimeError("Unlisted indirect call")
    if tuple(imports) != EXPECTED_IMPORTS:
        raise RuntimeError("Subject imports differ from the fixed whitelist")
    functions = tuple(node.name for node in tree.body if isinstance(node, ast.FunctionDef))
    if functions != ("_require_native_text", "_validate_prior", "combine_eligible_decision"):
        raise RuntimeError("Subject callable surface differs from the fixed whitelist")
    for node in tree.body:
        if not isinstance(node, (ast.ImportFrom, ast.FunctionDef)):
            if not (isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant)
                    and type(node.value.value) is str):
                raise RuntimeError("Unlisted module-level execution")
    if b"if __name__" in payload:
        raise RuntimeError("Candidate execution entry is prohibited")


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


class EligibleDecisionCombinerCandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global _HASH_BEFORE, _BOOTSTRAP_COMPLETE
        if sys.version_info[:3] != EXPECTED_RUNTIME:
            raise RuntimeError("Actual interpreter must be Python 3.12.14; inventory is not acceptance")
        if Path(sys.executable).resolve() != EXPECTED_EXECUTABLE.resolve():
            raise RuntimeError("Actual executable differs from the bound local interpreter")
        if (sys.flags.isolated, sys.flags.no_site, sys.flags.dont_write_bytecode) != (1, 1, 1):
            raise RuntimeError("Required -I -S -B flags are absent")
        verify_fixed_inputs()
        _HASH_BEFORE = True
        cls.subject_bytes = read_fixed_bytes(SUBJECT_RELATIVE, SUBJECT_SHA256)
        cls.subject_tree = ast.parse(cls.subject_bytes, filename=str(ROOT / SUBJECT_RELATIVE))
        assert_static_subject(cls.subject_tree, cls.subject_bytes)
        conflicts = [name for name in sys.modules if (
            name == "route_b_c03" or name.startswith("route_b_c03.")
            or name in (NATIVE_MODULE, CANDIDATE_MODULE) + FORBIDDEN_MODULES
        )]
        if conflicts:
            raise RuntimeError(f"Preexisting module identity conflict: {conflicts}")
        # Required stdlib imports are preloaded above, before the audit hook.
        sys.addaudithook(audit_guard)
        cls.parent = types.ModuleType("route_b_c03")
        cls.parent.__path__ = []
        cls.parent.__package__ = "route_b_c03"
        sys.modules["route_b_c03"] = cls.parent
        cls.contracts = load_declared_module(
            CONTRACTS_MODULE, PRESERVED_INPUTS[0][0],
            read_fixed_bytes(*PRESERVED_INPUTS[0]),
        )
        cls.parent.contracts = cls.contracts
        cls.native = load_declared_module(
            NATIVE_MODULE, PRESERVED_INPUTS[5][0],
            read_fixed_bytes(*PRESERVED_INPUTS[5]),
        )
        cls.subject = load_declared_module(CANDIDATE_MODULE, SUBJECT_RELATIVE, cls.subject_bytes)
        _BOOTSTRAP_COMPLETE = True

    def setUp(self):
        self.blocked_before = len(_CANDIDATE_BLOCKED_EVENTS)
        self.constructors_before = len(_CONSTRUCTOR_COUNTS)

    def tearDown(self):
        self.assertEqual(len(_CANDIDATE_BLOCKED_EVENTS), self.blocked_before)
        self.assertIsNone(_GUARD_PHASE)

    def prior(self, **changes):
        values = dict(state=self.contracts.InvocationState.ELIGIBLE_FOR_MAPPING,
                      reason_code="SYNTHETIC PRIOR — FULL REASON  ",
                      audit_correlation_id="SYNTHETIC-CALL-001",
                      permitted_write_namespaces=())
        values.update(changes)
        return guarded_call("synthetic-prior-construction", self.contracts.GateDecision, **values)

    def check(self, index=0, pair=0, **changes):
        state, cause = ALLOWED_PAIRS[pair]
        values = dict(boundary=tuple(self.native.BoundaryKind)[index],
                      state=self.native.BoundaryCheckState[state],
                      cause=self.native.BoundaryCheckCause[cause],
                      audit_correlation_id="SYNTHETIC-CALL-001",
                      expected_source_id="SYNTHETIC-EXPECTED-SOURCE-001",
                      actual_source_id="SYNTHETIC-ACTUAL-SOURCE-001")
        values.update(changes)
        return guarded_call("synthetic-check-construction", self.native.BoundaryCheck, **values)

    def checks(self, pairs=(0, 0, 0), **changes):
        return tuple(self.check(index=index, pair=pair, **changes)
                     for index, pair in enumerate(pairs))

    def snapshot(self, prior, checks):
        def fields(instance, names):
            return tuple((name, id(value), type(value)) for name in names
                         for value in (getattr(instance, name, _MISSING),))
        prior_fields = fields(prior, GATE_FIELDS) if type(prior) is self.contracts.GateDecision else ()
        check_fields = tuple((id(check), fields(check, CHECK_FIELDS))
                             if type(check) is self.native.BoundaryCheck else (id(check), ())
                             for check in checks) if type(checks) is tuple else ()
        return id(prior), prior_fields, id(checks), check_fields

    def combine(self, prior, checks):
        before = self.snapshot(prior, checks)
        init_code = self.contracts.GateDecision.__init__.__code__
        constructions = []
        old_profile = sys.getprofile()
        if old_profile is not None:
            raise RuntimeError("Unexpected existing profiler")

        def constructor_observer(frame, event, argument):
            if event == "call" and frame.f_code is init_code:
                constructions.append(id(frame.f_locals["self"]))

        sys.setprofile(constructor_observer)
        try:
            return guarded_call("combiner-call", self.subject.combine_eligible_decision, prior, checks)
        finally:
            sys.setprofile(old_profile)
            _CONSTRUCTOR_COUNTS.append(len(constructions))
            self.assertEqual(self.snapshot(prior, checks), before, "Candidate changed an input field")

    def reject(self, error, prior, checks):
        with self.assertRaises(error):
            self.combine(prior, checks)
        self.assertEqual(_CONSTRUCTOR_COUNTS[-1], 0, "Rejected input constructed a GateDecision")

    def assert_outcome(self, result, prior, label):
        self.assertIs(type(result), self.contracts.GateDecision)
        self.assertIs(type(result.state), self.contracts.InvocationState)
        self.assertIs(type(result.reason_code), str)
        self.assertIs(type(result.audit_correlation_id), str)
        self.assertEqual(result.audit_correlation_id, prior.audit_correlation_id)
        self.assertIs(type(result.permitted_write_namespaces), tuple)
        self.assertEqual(result.permitted_write_namespaces, ())
        if label == "A":
            self.assertIs(result, prior)
            self.assertEqual(result.reason_code, prior.reason_code)
            self.assertEqual(_CONSTRUCTOR_COUNTS[-1], 0)
        else:
            self.assertIsNot(result, prior)
            state, reason = ORACLE_OUTCOMES[label]
            self.assertIs(result.state, self.contracts.InvocationState[state])
            self.assertEqual(result.reason_code, reason)
            self.assertEqual(_CONSTRUCTOR_COUNTS[-1], 1)

    def test_actual_runtime_flags_and_fixed_executable(self):
        self.assertEqual(sys.version_info[:3], EXPECTED_RUNTIME)
        self.assertEqual(Path(sys.executable).resolve(), EXPECTED_EXECUTABLE.resolve())
        self.assertEqual((sys.flags.isolated, sys.flags.no_site, sys.flags.dont_write_bytecode), (1, 1, 1))

    def test_existing_contract_identity_and_exact_four_fields(self):
        self.assertEqual(self.contracts.GateDecision.__module__, CONTRACTS_MODULE)
        self.assertEqual(self.contracts.InvocationState.__module__, CONTRACTS_MODULE)
        self.assertEqual(tuple(field.name for field in dataclasses.fields(self.contracts.GateDecision)),
                         GATE_FIELDS)
        self.assertIs(self.subject.GateDecision, self.contracts.GateDecision)
        self.assertIs(self.subject.InvocationState, self.contracts.InvocationState)

    def test_independent_boundary_class_identity_is_not_current_contract_integration(self):
        self.assertEqual(self.native.BoundaryCheck.__module__, NATIVE_MODULE)
        self.assertIs(self.subject.BoundaryCheck, self.native.BoundaryCheck)
        self.assertIs(self.subject.BoundaryCheckState, self.native.BoundaryCheckState)
        self.assertIs(self.subject.BoundaryCheckCause, self.native.BoundaryCheckCause)
        self.assertFalse(hasattr(self.contracts, "BoundaryCheck"))

    def test_public_signature_has_only_required_prior_and_checks(self):
        signature = inspect.signature(self.subject.combine_eligible_decision)
        self.assertEqual(tuple(signature.parameters), ("prior", "checks"))
        self.assertTrue(all(parameter.default is inspect.Parameter.empty
                            for parameter in signature.parameters.values()))
        self.assertIs(signature.return_annotation, self.contracts.GateDecision)
        self.assertEqual(self.subject.combine_eligible_decision.__module__, CANDIDATE_MODULE)

    def test_handwritten_oracle_all_64_valid_combinations(self):
        global _ORACLE_CASE_COUNT
        seen = set()
        distribution = {label: 0 for label in ("A", "P", "S", "V", "T", "U", "I")}
        for indexes in itertools.product(range(4), repeat=3):
            with self.subTest(project=indexes[0], session=indexes[1], provider=indexes[2]):
                prior = self.prior()
                checks = self.checks(indexes)
                label = ORACLE_CUBE[indexes[0]][indexes[1]][indexes[2]]
                self.assert_outcome(self.combine(prior, checks), prior, label)
                seen.add(label)
                distribution[label] += 1
                _ORACLE_CASE_COUNT += 1
        self.assertEqual(_ORACLE_CASE_COUNT, 64)
        self.assertEqual(seen, {"A", "P", "S", "V", "T", "U", "I"})
        self.assertEqual(distribution, {"A": 1, "P": 1, "S": 1, "V": 1, "T": 4, "U": 19, "I": 37})

    def test_seven_exact_branch_results(self):
        for indexes, label in (((3, 0, 0), "I"), ((0, 2, 0), "U"),
                               ((1, 1, 0), "T"), ((1, 0, 0), "P"),
                               ((0, 1, 0), "S"), ((0, 0, 1), "V"), ((0, 0, 0), "A")):
            with self.subTest(label=label):
                prior = self.prior()
                self.assert_outcome(self.combine(prior, self.checks(indexes)), prior, label)

    def test_invalid_reference_beats_unbound_and_multiple_mismatch(self):
        for indexes in ((3, 2, 1), (2, 3, 1), (1, 2, 3), (3, 1, 1), (1, 3, 1), (1, 1, 3)):
            prior = self.prior()
            self.assert_outcome(self.combine(prior, self.checks(indexes)), prior, "I")

    def test_source_unbound_beats_multiple_mismatch(self):
        for indexes in ((2, 1, 1), (1, 2, 1), (1, 1, 2)):
            prior = self.prior()
            self.assert_outcome(self.combine(prior, self.checks(indexes)), prior, "U")

    def test_multiple_mismatch_beats_each_single_branch(self):
        for indexes in ((1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)):
            prior = self.prior()
            self.assert_outcome(self.combine(prior, self.checks(indexes)), prior, "T")

    def test_all_match_returns_same_object_with_full_literal_reason(self):
        for reason in ("SYNTHETIC PRIOR", "  SYNTHETIC PRIOR — 原因  ", "SYNTHETIC-E\u0301\nTAIL"):
            prior = self.prior(reason_code=reason)
            self.assert_outcome(self.combine(prior, self.checks()), prior, "A")
            self.assertEqual(prior.reason_code, reason)

    def test_new_decisions_are_frozen_slotted_and_have_exact_empty_tuple(self):
        for indexes in ((3, 0, 0), (2, 0, 0), (1, 0, 0)):
            result = self.combine(self.prior(), self.checks(indexes))
            self.assertFalse(hasattr(result, "__dict__"))
            self.assertIs(type(result.permitted_write_namespaces), tuple)
            self.assertEqual(result.permitted_write_namespaces, ())
            with self.assertRaises(dataclasses.FrozenInstanceError):
                result.reason_code = "SYNTHETIC CHANGED"

    def test_prior_rejects_non_native_objects_without_conversion(self):
        for value in (None, {}, (), [], "SYNTHETIC", 1, True):
            with self.subTest(input_type=type(value).__name__):
                self.reject(TypeError, value, self.checks())

    def test_prior_rejects_foreign_same_named_same_module_fixture(self):
        fixture = type("ForeignGateFixture", (), {"__module__": CONTRACTS_MODULE})
        fixture.__name__ = "GateDecision"
        foreign = fixture()
        for field in GATE_FIELDS:
            setattr(foreign, field, getattr(self.prior(), field))
        self.assertEqual((type(foreign).__name__, type(foreign).__module__),
                         ("GateDecision", CONTRACTS_MODULE))
        self.reject(TypeError, foreign, self.checks())

    def test_prior_rejects_existing_gate_subclass(self):
        class ForeignSubclass(self.contracts.GateDecision):
            pass
        prior = self.prior()
        foreign = ForeignSubclass(**{field: getattr(prior, field) for field in GATE_FIELDS})
        self.reject(TypeError, foreign, self.checks())

    def test_prior_state_rejects_wrong_native_types(self):
        for value in ("ELIGIBLE_FOR_MAPPING", None, 1, True,
                      self.native.BoundaryCheckState.MATCH):
            self.reject(TypeError, self.prior(state=value), self.checks())

    def test_prior_state_rejects_foreign_same_named_same_value_enum(self):
        foreign_enum = Enum("ForeignInvocationState", {"ELIGIBLE_FOR_MAPPING": "ELIGIBLE_FOR_MAPPING"})
        foreign_enum.__name__ = "InvocationState"
        foreign_enum.__module__ = CONTRACTS_MODULE
        self.reject(TypeError, self.prior(state=foreign_enum.ELIGIBLE_FOR_MAPPING), self.checks())

    def test_all_noneligible_native_invocation_states_raise_value_error(self):
        count = 0
        for state in self.contracts.InvocationState:
            if state is not self.contracts.InvocationState.ELIGIBLE_FOR_MAPPING:
                with self.subTest(state=state.name):
                    self.reject(ValueError, self.prior(state=state), self.checks())
                count += 1
        self.assertEqual(count, 8)

    def test_prior_reason_and_correlation_require_native_str(self):
        class StringSubclass(str):
            pass
        for field in ("reason_code", "audit_correlation_id"):
            for value in (None, 1, True, b"SYNTHETIC", [], {}, StringSubclass("SYNTHETIC")):
                with self.subTest(field=field, input_type=type(value).__name__):
                    self.reject(TypeError, self.prior(**{field: value}), self.checks())

    def test_prior_text_rejects_empty_and_whitespace_without_repair(self):
        for field in ("reason_code", "audit_correlation_id"):
            for value in ("", " ", "\t\r\n", "\u3000", "\u00a0"):
                self.reject(ValueError, self.prior(**{field: value}), self.checks())

    def test_prior_write_namespaces_require_native_tuple(self):
        class TupleSubclass(tuple):
            pass
        for value in (None, [], {}, "", 1, iter(()), TupleSubclass(())):
            self.reject(TypeError, self.prior(permitted_write_namespaces=value), self.checks())

    def test_prior_write_namespaces_reject_every_nonempty_native_tuple(self):
        for value in (("SYNTHETIC",), (None,), ((),), ("SYNTHETIC-A", "SYNTHETIC-B")):
            self.reject(ValueError, self.prior(permitted_write_namespaces=value), self.checks())

    def test_prior_missing_any_field_or_all_fields_raise_value_error(self):
        for field in GATE_FIELDS:
            prior = self.prior()
            object.__delattr__(prior, field)
            self.reject(ValueError, prior, self.checks())
        self.reject(ValueError, object.__new__(self.contracts.GateDecision), self.checks())

    def test_prior_low_level_mutation_is_revalidated_and_not_repaired(self):
        for field, value, error in (
            ("state", "ELIGIBLE_FOR_MAPPING", TypeError),
            ("state", self.contracts.InvocationState.BLOCKED, ValueError),
            ("reason_code", "", ValueError), ("reason_code", 1, TypeError),
            ("audit_correlation_id", "\u3000", ValueError),
            ("permitted_write_namespaces", [], TypeError),
            ("permitted_write_namespaces", ("SYNTHETIC",), ValueError),
        ):
            prior = self.prior()
            object.__setattr__(prior, field, value)
            self.reject(error, prior, self.checks())

    def test_checks_reject_non_native_tuple_containers(self):
        class TupleSubclass(tuple):
            pass
        checks = self.checks()
        for value in (None, list(checks), dict(enumerate(checks)), iter(checks),
                      "SYNTHETIC", TupleSubclass(checks)):
            self.reject(TypeError, self.prior(), value)

    def test_checks_reject_all_wrong_lengths(self):
        checks = self.checks()
        for value in ((), checks[:1], checks[:2], checks + checks[:1], checks + checks):
            self.reject(ValueError, self.prior(), value)

    def test_checks_reject_every_wrong_project_session_provider_permutation(self):
        checks = self.checks()
        for indexes in itertools.permutations(range(3)):
            if indexes != (0, 1, 2):
                self.reject(ValueError, self.prior(), tuple(checks[index] for index in indexes))

    def test_checks_reject_duplicate_or_missing_boundary(self):
        checks = self.checks()
        for value in ((checks[0], checks[0], checks[2]), (checks[0], checks[2], checks[2]),
                      (checks[1], checks[1], checks[2])):
            self.reject(ValueError, self.prior(), value)

    def test_checks_reject_non_native_element_in_every_position(self):
        for index in range(3):
            for value in (None, {}, (), "SYNTHETIC", list(dataclasses.astuple(self.check(index)))):
                changed = list(self.checks())
                changed[index] = value
                self.reject(TypeError, self.prior(), tuple(changed))

    def test_checks_reject_foreign_same_named_same_module_fixture(self):
        fixture = type("ForeignBoundaryFixture", (), {"__module__": NATIVE_MODULE})
        fixture.__name__ = "BoundaryCheck"
        for index in range(3):
            foreign = fixture()
            original = self.check(index)
            for field in CHECK_FIELDS:
                setattr(foreign, field, getattr(original, field))
            changed = list(self.checks())
            changed[index] = foreign
            self.reject(TypeError, self.prior(), tuple(changed))

    def test_checks_reject_boundary_subclass_in_every_position(self):
        class ForeignSubclass(self.native.BoundaryCheck):
            pass
        for index in range(3):
            original = self.check(index)
            foreign = guarded_call("synthetic-foreign-construction", ForeignSubclass,
                                   **{field: getattr(original, field) for field in CHECK_FIELDS})
            changed = list(self.checks())
            changed[index] = foreign
            self.reject(TypeError, self.prior(), tuple(changed))

    def test_check_correlations_must_exactly_equal_prior_in_every_position(self):
        for index in range(3):
            for correlation in ("SYNTHETIC-OTHER-CALL", " SYNTHETIC-CALL-001",
                                "SYNTHETIC-CALL-001 ", "SYNTHETIC-CALL-001\u3000"):
                changed = list(self.checks())
                changed[index] = self.check(index, audit_correlation_id=correlation)
                self.reject(ValueError, self.prior(), tuple(changed))
        self.reject(ValueError, self.prior(audit_correlation_id="SYNTHETIC-PRIOR-OTHER"), self.checks())

    def test_equal_padded_unicode_correlations_are_preserved_for_every_outcome(self):
        for correlation in ("  SYNTHETIC-CALL-001  ", "SYNTHETIC-关联-É",
                            "SYNTHETIC-关联-E\u0301", "\tSYNTHETIC-关联\u3000"):
            for indexes, label in (((0, 0, 0), "A"), ((3, 0, 0), "I"),
                                   ((2, 0, 0), "U"), ((1, 1, 0), "T"),
                                   ((1, 0, 0), "P"), ((0, 1, 0), "S"), ((0, 0, 1), "V")):
                prior = self.prior(audit_correlation_id=correlation)
                checks = self.checks(indexes, audit_correlation_id=correlation)
                self.assert_outcome(self.combine(prior, checks), prior, label)
                self.assertEqual(prior.audit_correlation_id, correlation)

    def test_unicode_normalization_and_trimming_do_not_make_correlations_equal(self):
        for prior_correlation, check_correlation in (
            ("SYNTHETIC-É", "SYNTHETIC-E\u0301"),
            (" SYNTHETIC-CALL ", "SYNTHETIC-CALL"),
            ("SYNTHETIC-关联\u3000", "SYNTHETIC-关联 "),
        ):
            self.reject(ValueError, self.prior(audit_correlation_id=prior_correlation),
                        self.checks(audit_correlation_id=check_correlation))

    def test_checks_low_level_wrong_enum_types_are_revalidated(self):
        for index in range(3):
            for field, value in (("boundary", "PROJECT"), ("state", "MATCH"),
                                 ("cause", "EXACT_EQUAL"), ("boundary", None),
                                 ("state", self.native.BoundaryKind.PROJECT)):
                changed = self.checks()
                object.__setattr__(changed[index], field, value)
                self.reject(TypeError, self.prior(), changed)

    def test_checks_reject_foreign_same_named_enum_families(self):
        for field, enum_name in (("boundary", "BoundaryKind"), ("state", "BoundaryCheckState"),
                                 ("cause", "BoundaryCheckCause")):
            native_enum = getattr(self.native, enum_name)
            foreign_enum = Enum("ForeignEnum", {member.name: member.value for member in native_enum})
            foreign_enum.__name__ = enum_name
            foreign_enum.__module__ = NATIVE_MODULE
            changed = self.checks()
            object.__setattr__(changed[0], field, next(iter(foreign_enum)))
            self.reject(TypeError, self.prior(), changed)

    def test_checks_reject_all_disallowed_state_cause_pairs_in_every_position(self):
        for index in range(3):
            for state in self.native.BoundaryCheckState:
                for cause in self.native.BoundaryCheckCause:
                    if (state.name, cause.name) not in ALLOWED_PAIRS:
                        with self.subTest(index=index, state=state.name, cause=cause.name):
                            changed = self.checks()
                            object.__setattr__(changed[index], "state", state)
                            object.__setattr__(changed[index], "cause", cause)
                            self.reject(ValueError, self.prior(), changed)

    def test_check_correlation_rejects_non_native_and_empty_text_after_mutation(self):
        class StringSubclass(str):
            pass
        for value, error in ((None, TypeError), (1, TypeError), (True, TypeError),
                             (b"SYNTHETIC", TypeError), (StringSubclass("SYNTHETIC"), TypeError),
                             ("", ValueError), ("\t\n", ValueError), ("\u3000", ValueError)):
            for index in range(3):
                changed = self.checks()
                object.__setattr__(changed[index], "audit_correlation_id", value)
                self.reject(error, self.prior(), changed)

    def test_check_source_ids_are_revalidated_instead_of_backfilled(self):
        class StringSubclass(str):
            pass
        for field in ("expected_source_id", "actual_source_id"):
            for value, error in ((None, ValueError), (1, TypeError), (True, TypeError),
                                 (b"SYNTHETIC", TypeError), (StringSubclass("SYNTHETIC"), TypeError),
                                 ("", ValueError), ("\u3000", ValueError)):
                for index in range(3):
                    changed = self.checks()
                    object.__setattr__(changed[index], field, value)
                    self.reject(error, self.prior(), changed)

    def test_unbound_source_none_is_literal_and_does_not_establish_binding(self):
        for pair, label in ((2, "U"), (3, "I")):
            for index in range(3):
                changed = list(self.checks())
                changed[index] = self.check(index, pair, expected_source_id=None, actual_source_id=None)
                prior = self.prior()
                self.assert_outcome(self.combine(prior, tuple(changed)), prior, label)
                self.assertIsNone(changed[index].expected_source_id)
                self.assertIsNone(changed[index].actual_source_id)

    def test_checks_missing_any_native_field_raise_value_error(self):
        for index in range(3):
            for field in CHECK_FIELDS:
                changed = self.checks()
                object.__delattr__(changed[index], field)
                self.reject(ValueError, self.prior(), changed)
            changed = list(self.checks())
            changed[index] = object.__new__(self.native.BoundaryCheck)
            self.reject(ValueError, self.prior(), tuple(changed))

    def test_not_evaluated_at_any_position_raises_without_gate_construction(self):
        for index in range(3):
            pairs = [0, 0, 0]
            pairs[index] = 4
            self.reject(ValueError, self.prior(), self.checks(tuple(pairs)))
        self.reject(ValueError, self.prior(), self.checks((4, 4, 4)))

    def test_not_evaluated_precedes_all_priority_competitors(self):
        global _NOT_EVALUATED_CASE_COUNT
        for pairs in itertools.product(range(5), repeat=3):
            if 4 in pairs:
                with self.subTest(project=pairs[0], session=pairs[1], provider=pairs[2]):
                    self.reject(ValueError, self.prior(), self.checks(pairs))
                    _NOT_EVALUATED_CASE_COUNT += 1
        self.assertEqual(_NOT_EVALUATED_CASE_COUNT, 61)

    def test_source_import_and_call_whitelist_excludes_execution_surfaces(self):
        assert_static_subject(self.subject_tree, self.subject_bytes)
        forbidden = {"open", "eval", "exec", "compile", "input", "print", "__import__",
                     "evaluate_identity_gate", "extract_expected_baseline", "map_candidate",
                     "capture_actual", "invoke_provider", "__new__", "__setattr__"}
        for node in ast.walk(self.subject_tree):
            if isinstance(node, ast.Call):
                name = node.func.id if isinstance(node.func, ast.Name) else node.func.attr
                self.assertNotIn(name, forbidden)
        self.assertNotIn(b"if __name__", self.subject_bytes)

    def test_forbidden_modules_absent_and_empty_parent_not_initialized(self):
        for module in FORBIDDEN_MODULES:
            self.assertNotIn(module, sys.modules)
        self.assertIs(sys.modules["route_b_c03"], self.parent)
        self.assertEqual(self.parent.__path__, [])
        self.assertFalse(hasattr(self.parent, "__file__"))
        self.assertIs(sys.modules[CONTRACTS_MODULE], self.contracts)
        self.assertIs(sys.modules[NATIVE_MODULE], self.native)
        self.assertIs(sys.modules[CANDIDATE_MODULE], self.subject)

    def test_audit_guard_intentional_open_denied_and_excluded_from_candidate_events(self):
        candidate_before = len(_CANDIDATE_BLOCKED_EVENTS)
        self_test_before = len(_GUARD_SELF_TEST_EVENTS)
        with self.assertRaises(ForbiddenCandidateSideEffect):
            guarded_call("intentional-guard-self-test", builtins.open, str(ROOT / SUBJECT_RELATIVE), "rb")
        self.assertEqual(_GUARD_SELF_TEST_EVENTS[self_test_before:],
                         [{"phase": "intentional-guard-self-test", "event": "open"}])
        self.assertEqual(len(_CANDIDATE_BLOCKED_EVENTS), candidate_before)


def main():
    global _HASH_AFTER
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(EligibleDecisionCombinerCandidateTests)
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
            "diagnostic": "DSP004_ELIGIBLE_COMBINER_LOCAL_SYNTHETIC_ONLY",
            "candidate_module": CANDIDATE_MODULE,
            "subject_sha256": SUBJECT_SHA256,
            "runtime": sys.version,
            "actual_runtime": list(sys.version_info[:3]),
            "actual_executable": sys.executable,
            "required_runtime": list(EXPECTED_RUNTIME),
            "required_isolation_flags": "-I -S -B",
            "actual_isolation_flags": {
                "isolated": sys.flags.isolated,
                "no_site": sys.flags.no_site,
                "dont_write_bytecode": sys.flags.dont_write_bytecode,
            },
            "hash_before": _HASH_BEFORE,
            "hash_after": _HASH_AFTER,
            "postcheck_error": postcheck_error,
            "fixed_inputs": [{"path": path, "sha256": sha} for path, sha in PRESERVED_INPUTS],
            "bootstrap_completed": _BOOTSTRAP_COMPLETE,
            "test_methods_planned": len(loader.getTestCaseNames(EligibleDecisionCombinerCandidateTests)),
            "test_methods_run": result.testsRun if result is not None else 0,
            "failures": len(result.failures) if result is not None else None,
            "errors": len(result.errors) if result is not None else None,
            "synthetic_diagnostic_success": bool(result and result.wasSuccessful() and _HASH_AFTER),
            "oracle_combinations_planned": 64,
            "oracle_combinations_checked": _ORACLE_CASE_COUNT,
            "not_evaluated_combinations_planned": 61,
            "not_evaluated_combinations_checked": _NOT_EVALUATED_CASE_COUNT,
            "combiner_calls_observed": len(_CONSTRUCTOR_COUNTS),
            "python_gate_constructor_calls_during_combiner": sum(_CONSTRUCTOR_COUNTS),
            "candidate_blocked_audit_events": _CANDIDATE_BLOCKED_EVENTS,
            "guard_self_test_events_excluded_from_candidate_events": _GUARD_SELF_TEST_EVENTS,
            "audit_guard_scope": "FINITE AUDIT DIAGNOSTIC; NOT COMPREHENSIVE RUNTIME ISOLATION",
            "source_admission": "NOT ESTABLISHED",
            "actual_capture": "NOT PERFORMED",
            "gate_invocation": "NOT PERFORMED",
            "formal_wp008_validation": "NOT PERFORMED",
            "approved_real_integration": "NOT ESTABLISHED",
            "same_call_provenance": "NOT ESTABLISHED",
            "parent_package_initialization": "NOT EXECUTED",
            "historical_runtime_inventory": "3.12.13; UNCHANGED; NOT ACTUAL RUNTIME ACCEPTANCE",
            "persistent_evidence_output": "NOT WRITTEN; STDOUT ONLY",
        }, ensure_ascii=False))
    return 0 if result and result.wasSuccessful() and _HASH_AFTER else 1


if __name__ == "__main__":
    sys.exit(main())
