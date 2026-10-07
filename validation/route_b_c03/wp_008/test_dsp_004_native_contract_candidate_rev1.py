"""Local synthetic type/structure diagnostic for the DSP-004 contract candidate.

Run with .venv-validation/Scripts/python.exe -I -S -B and this exact script.
Only the fixed candidate is compiled into its declared separate module identity.
No current contract or Gate module is imported or called. The synthetic objects
are not captured observations, admitted sources, same-call evidence, or boundary
review determinations. Results are console-only, not formal WP-008 validation.
The old inventory is not rewritten or treated as current environment acceptance.
"""

import ast
import builtins
import dataclasses
from enum import Enum
import hashlib
import inspect
import itertools
import json
from pathlib import Path
import sys
import types
import unittest


ROOT = Path(__file__).resolve().parents[3]
CANDIDATE_MODULE = "DSP_004_NATIVE_CONTRACT_CANDIDATE_REV1"
SUBJECT_PATH = ROOT / "validation/route_b_c03/wp_008/DSP_004_NATIVE_CONTRACT_CANDIDATE_REV1.py"
SUBJECT_SHA256 = "1544B7D8101493072E9BCA5C23B09C3C811F1B52CB1E9F5A8D73C976576FC312"
EXPECTED_RUNTIME = (3, 12, 14)
PRESERVED_INPUTS = (
    (
        "scripts/phase2_runtime/route_b_c03/contracts.py",
        "7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4",
    ),
    (
        "scripts/phase2_runtime/route_b_c03/identity_gate.py",
        "9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445",
    ),
    (
        "validation/route_b_c03/wp_008/DSP_004_EXPECTED_BASELINE_READER_CANDIDATE_REV1.py",
        "AE1389EDA1C3B9129A0546DA5764C1F68A6B0193A22DA3431CAA89BAB8DC0727",
    ),
    (
        "validation/route_b_c03/wp_008/test_dsp_004_expected_baseline_reader_candidate_rev1.py",
        "6757A99AD6A7A4461B8D52345855FDE675DBB1692D312F22BB2E27B0F9C335F9",
    ),
    (
        "docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PREPARATION_DESIGN_RECORD_REV1.md",
        "DB39150AE0428A452B2BEBE958A4B7DD91F4DE8A3790B0BC374FAEA4693868F4",
    ),
)
FIELD_NAMES = (
    "boundary", "state", "cause", "audit_correlation_id",
    "expected_source_id", "actual_source_id",
)
ALLOWED_PAIRS = (
    ("MATCH", "EXACT_EQUAL"),
    ("MISMATCH", "EXACT_UNEQUAL"),
    ("UNBOUND", "SOURCE_UNBOUND"),
    ("UNBOUND", "INVALID_REFERENCE_TYPE"),
    ("NOT_EVALUATED", "PRIOR_DENIAL"),
)
_GUARD_ACTIVE = False
_BLOCKED_EVENTS: list[str] = []


class ForbiddenCandidateSideEffect(RuntimeError):
    pass


def audit_guard(event, args):
    if _GUARD_ACTIVE and (
        event == "open"
        or event.startswith(("os.", "socket.", "subprocess.", "ctypes.", "winreg."))
    ):
        _BLOCKED_EVENTS.append(event)
        raise ForbiddenCandidateSideEffect(event)


def guarded_call(function, *args, **kwargs):
    global _GUARD_ACTIVE
    if _GUARD_ACTIVE:
        raise RuntimeError("Nested candidate guard is not permitted")
    _GUARD_ACTIVE = True
    try:
        return function(*args, **kwargs)
    finally:
        _GUARD_ACTIVE = False


def read_fixed_bytes(path, expected_sha):
    payload = path.read_bytes()
    actual_sha = hashlib.sha256(payload).hexdigest().upper()
    if actual_sha != expected_sha:
        raise RuntimeError(f"Fixed input mismatch: {path.name}: {actual_sha}")
    return payload


def verify_preserved_inputs():
    for relative_path, expected_sha in PRESERVED_INPUTS:
        read_fixed_bytes(ROOT / relative_path, expected_sha)


class NativeContractCandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if sys.version_info[:3] != EXPECTED_RUNTIME:
            raise RuntimeError("Interpreter differs from this batch's observed version")
        if (sys.flags.isolated, sys.flags.no_site, sys.flags.dont_write_bytecode) != (1, 1, 1):
            raise RuntimeError("Required -I -S -B isolation flags are absent")
        verify_preserved_inputs()
        cls.subject_bytes = read_fixed_bytes(SUBJECT_PATH, SUBJECT_SHA256)
        cls.subject_tree = ast.parse(cls.subject_bytes, filename=str(SUBJECT_PATH))
        if CANDIDATE_MODULE in sys.modules or "route_b_c03.contracts" in sys.modules:
            raise RuntimeError("Unexpected contract module already loaded")
        cls.subject = types.ModuleType(CANDIDATE_MODULE)
        cls.subject.__file__ = str(SUBJECT_PATH)
        sys.modules[CANDIDATE_MODULE] = cls.subject
        sys.addaudithook(audit_guard)
        code = compile(cls.subject_bytes, str(SUBJECT_PATH), "exec", dont_inherit=True)
        guarded_call(exec, code, cls.subject.__dict__)

    def setUp(self):
        self.blocked_before_test = len(_BLOCKED_EVENTS)

    def tearDown(self):
        if self._testMethodName != "test_audit_guard_denies_open_before_access":
            self.assertEqual(len(_BLOCKED_EVENTS), self.blocked_before_test)

    @classmethod
    def tearDownClass(cls):
        verify_preserved_inputs()
        read_fixed_bytes(SUBJECT_PATH, SUBJECT_SHA256)
        print(json.dumps({
            "diagnostic": "DSP004_NATIVE_CONTRACT_LOCAL_SYNTHETIC_ONLY",
            "candidate_module": CANDIDATE_MODULE,
            "subject_sha256": SUBJECT_SHA256,
            "runtime": sys.version,
            "isolation_flags": "-I -S -B",
            "preserved_inputs": [
                {"path": path, "sha256": sha} for path, sha in PRESERVED_INPUTS
            ],
            "preserved_inputs_unchanged": True,
            "candidate_unchanged": True,
            "blocked_audit_events_including_guard_self_test": _BLOCKED_EVENTS,
            "approved_integration_class_identity": "NOT ESTABLISHED",
            "source_admission": "NOT ESTABLISHED",
            "actual_capture": "NOT PERFORMED",
            "gate_invocation": "NOT PERFORMED",
            "formal_wp008_validation": "NOT PERFORMED",
        }, ensure_ascii=False))

    def kwargs(self, **changes):
        values = {
            "boundary": self.subject.BoundaryKind.PROJECT,
            "state": self.subject.BoundaryCheckState.MATCH,
            "cause": self.subject.BoundaryCheckCause.EXACT_EQUAL,
            "audit_correlation_id": "SYNTHETIC-CALL-001",
            "expected_source_id": "SYNTHETIC-EXPECTED-SOURCE-001",
            "actual_source_id": "SYNTHETIC-ACTUAL-SOURCE-001",
        }
        values.update(changes)
        return values

    def construct(self, **changes):
        return guarded_call(self.subject.BoundaryCheck, **self.kwargs(**changes))

    def sequence(self):
        return tuple(self.construct(boundary=boundary) for boundary in self.subject.BoundaryKind)

    def validate(self, checks):
        return guarded_call(self.subject.validate_boundary_check_sequence, checks)

    def test_runtime_and_separate_candidate_class_identity(self):
        self.assertEqual(sys.version_info[:3], EXPECTED_RUNTIME)
        for name in ("BoundaryKind", "BoundaryCheckState", "BoundaryCheckCause", "BoundaryCheck"):
            self.assertEqual(getattr(self.subject, name).__module__, CANDIDATE_MODULE)
        self.assertNotIn("route_b_c03.contracts", sys.modules)

    def test_three_enum_member_sets_and_values_are_exact_without_aliases(self):
        expected_sets = (
            (self.subject.BoundaryKind, ("PROJECT", "SESSION", "PROVIDER")),
            (self.subject.BoundaryCheckState, ("MATCH", "MISMATCH", "UNBOUND", "NOT_EVALUATED")),
            (self.subject.BoundaryCheckCause, (
                "EXACT_EQUAL", "EXACT_UNEQUAL", "SOURCE_UNBOUND",
                "INVALID_REFERENCE_TYPE", "PRIOR_DENIAL",
            )),
        )
        for enum_type, names in expected_sets:
            self.assertEqual(tuple(enum_type.__members__), names)
            self.assertEqual(tuple(member.name for member in enum_type), names)
            self.assertEqual(tuple(member.value for member in enum_type), names)
            self.assertTrue(all(type(member) is enum_type for member in enum_type))

    def test_enums_are_not_string_substitutes(self):
        self.assertNotEqual(self.subject.BoundaryKind.PROJECT, "PROJECT")
        self.assertNotEqual(self.subject.BoundaryCheckState.MATCH, "MATCH")
        self.assertNotEqual(self.subject.BoundaryCheckCause.EXACT_EQUAL, "EXACT_EQUAL")

    def test_exact_six_fields_types_order_and_no_defaults(self):
        fields = dataclasses.fields(self.subject.BoundaryCheck)
        self.assertEqual(tuple(field.name for field in fields), FIELD_NAMES)
        self.assertEqual(tuple(field.type for field in fields), (
            self.subject.BoundaryKind, self.subject.BoundaryCheckState,
            self.subject.BoundaryCheckCause, str, str | None, str | None,
        ))
        self.assertTrue(all(field.default is dataclasses.MISSING for field in fields))
        self.assertEqual(tuple(inspect.signature(self.subject.BoundaryCheck).parameters), FIELD_NAMES)

    def test_synthetic_instances_are_frozen_and_slotted(self):
        check = self.construct()
        self.assertFalse(hasattr(check, "__dict__"))
        with self.assertRaises(dataclasses.FrozenInstanceError):
            check.audit_correlation_id = "SYNTHETIC-CHANGED"
        with self.assertRaises((AttributeError, TypeError)):
            check.extra_field = "SYNTHETIC"

    def test_every_allowed_state_cause_pair_for_all_boundaries(self):
        for boundary in self.subject.BoundaryKind:
            for state_name, cause_name in ALLOWED_PAIRS:
                with self.subTest(boundary=boundary.name, state=state_name, cause=cause_name):
                    check = self.construct(
                        boundary=boundary,
                        state=self.subject.BoundaryCheckState[state_name],
                        cause=self.subject.BoundaryCheckCause[cause_name],
                    )
                    self.assertIs(type(check), self.subject.BoundaryCheck)
                    self.assertEqual((check.state.name, check.cause.name), (state_name, cause_name))

    def test_every_disallowed_state_cause_pair_is_rejected(self):
        for state in self.subject.BoundaryCheckState:
            for cause in self.subject.BoundaryCheckCause:
                if (state.name, cause.name) not in ALLOWED_PAIRS:
                    with self.subTest(state=state.name, cause=cause.name):
                        with self.assertRaises(ValueError):
                            self.construct(state=state, cause=cause)

    def test_enum_fields_reject_string_none_integer_and_wrong_enum_family(self):
        cases = {
            "boundary": ("PROJECT", None, 1, self.subject.BoundaryCheckState.MATCH),
            "state": ("MATCH", None, 1, self.subject.BoundaryKind.PROJECT),
            "cause": ("EXACT_EQUAL", None, 1, self.subject.BoundaryKind.PROJECT),
        }
        for field, values in cases.items():
            for value in values:
                with self.subTest(field=field, input_type=type(value).__name__):
                    with self.assertRaises(TypeError):
                        self.construct(**{field: value})

    def test_enum_fields_reject_foreign_same_named_and_same_module_enums(self):
        for field, enum_name in (
            ("boundary", "BoundaryKind"), ("state", "BoundaryCheckState"),
            ("cause", "BoundaryCheckCause"),
        ):
            candidate_enum = getattr(self.subject, enum_name)
            foreign = Enum(enum_name, {member.name: member.value for member in candidate_enum},
                           module=CANDIDATE_MODULE)
            with self.assertRaises(TypeError):
                self.construct(**{field: next(iter(foreign))})

    def test_correlation_rejects_non_native_string(self):
        class StringSubclass(str):
            pass
        for value in (None, 1, True, b"SYNTHETIC", StringSubclass("SYNTHETIC")):
            with self.subTest(input_type=type(value).__name__):
                with self.assertRaises(TypeError):
                    self.construct(audit_correlation_id=value)

    def test_correlation_rejects_empty_or_whitespace_only_string(self):
        for value in ("", " ", "\t\n", "\u3000"):
            with self.assertRaises(ValueError):
                self.construct(audit_correlation_id=value)

    def test_source_ids_reject_non_native_string(self):
        class StringSubclass(str):
            pass
        for field in ("expected_source_id", "actual_source_id"):
            for value in (1, True, b"SYNTHETIC", [], {}, StringSubclass("SYNTHETIC")):
                with self.subTest(field=field, input_type=type(value).__name__):
                    with self.assertRaises(TypeError):
                        self.construct(**{field: value})

    def test_source_ids_reject_empty_or_whitespace_only_in_every_allowed_pair(self):
        for state_name, cause_name in ALLOWED_PAIRS:
            for field in ("expected_source_id", "actual_source_id"):
                for value in ("", " ", "\t", "\u3000"):
                    with self.subTest(state=state_name, field=field, value=repr(value)):
                        with self.assertRaises(ValueError):
                            self.construct(
                                state=self.subject.BoundaryCheckState[state_name],
                                cause=self.subject.BoundaryCheckCause[cause_name], **{field: value},
                            )

    def test_match_and_mismatch_require_both_source_ids(self):
        for state_name, cause_name in ALLOWED_PAIRS[:2]:
            for expected_id, actual_id in ((None, None), (None, "SYNTHETIC-A"),
                                          ("SYNTHETIC-E", None)):
                with self.assertRaises(ValueError):
                    self.construct(
                        state=self.subject.BoundaryCheckState[state_name],
                        cause=self.subject.BoundaryCheckCause[cause_name],
                        expected_source_id=expected_id, actual_source_id=actual_id,
                    )

    def test_unbound_and_not_evaluated_allow_native_none_without_backfill(self):
        for state_name, cause_name in ALLOWED_PAIRS[2:]:
            for expected_id, actual_id in ((None, None), (None, "SYNTHETIC-A"),
                                          ("SYNTHETIC-E", None), ("SYNTHETIC-E", "SYNTHETIC-A")):
                check = self.construct(
                    state=self.subject.BoundaryCheckState[state_name],
                    cause=self.subject.BoundaryCheckCause[cause_name],
                    expected_source_id=expected_id, actual_source_id=actual_id,
                )
                self.assertEqual((check.expected_source_id, check.actual_source_id),
                                 (expected_id, actual_id))

    def test_valid_text_is_preserved_without_trimming_or_unicode_normalization(self):
        check = self.construct(audit_correlation_id="  SYNTHETIC-CALL  ",
                               expected_source_id="SYNTHETIC-E\u0301  ",
                               actual_source_id="  SYNTHETIC-É")
        self.assertEqual(check.audit_correlation_id, "  SYNTHETIC-CALL  ")
        self.assertEqual(check.expected_source_id, "SYNTHETIC-E\u0301  ")
        self.assertEqual(check.actual_source_id, "  SYNTHETIC-É")

    def test_required_field_omission_and_extra_field_are_rejected(self):
        for field in FIELD_NAMES:
            values = self.kwargs()
            del values[field]
            with self.assertRaises(TypeError):
                guarded_call(self.subject.BoundaryCheck, **values)
        with self.assertRaises(TypeError):
            self.construct(unapproved_field="SYNTHETIC")

    def test_sequence_returns_same_native_tuple_and_same_elements(self):
        checks = self.sequence()
        validated = self.validate(checks)
        self.assertIs(validated, checks)
        self.assertTrue(all(left is right for left, right in zip(validated, checks)))

    def test_sequence_rejects_list_dict_generator_none_and_tuple_subclass(self):
        class TupleSubclass(tuple):
            pass
        checks = self.sequence()
        for value in (list(checks), dict(enumerate(checks)), iter(checks), None,
                      TupleSubclass(checks)):
            with self.assertRaises(TypeError):
                self.validate(value)

    def test_sequence_rejects_every_wrong_length(self):
        checks = self.sequence()
        for value in ((), checks[:1], checks[:2], checks + checks[:1]):
            with self.assertRaises(ValueError):
                self.validate(value)

    def test_sequence_rejects_all_wrong_order_permutations(self):
        checks = self.sequence()
        for permutation in itertools.permutations(checks):
            if permutation != checks:
                with self.assertRaises(ValueError):
                    self.validate(permutation)

    def test_sequence_rejects_duplicate_boundary(self):
        checks = self.sequence()
        with self.assertRaises(ValueError):
            self.validate((checks[0], checks[0], checks[2]))

    def test_sequence_rejects_non_native_element_in_every_position(self):
        checks = self.sequence()
        for index in range(3):
            for value in (None, {}, "SYNTHETIC", list(dataclasses.astuple(checks[index]))):
                changed = list(checks)
                changed[index] = value
                with self.assertRaises(TypeError):
                    self.validate(tuple(changed))

    def test_sequence_rejects_same_named_foreign_class_even_with_spoofed_module(self):
        foreign_type = dataclasses.make_dataclass(
            "BoundaryCheck", [(field, object) for field in FIELD_NAMES],
            namespace={"__module__": CANDIDATE_MODULE}, frozen=True, slots=True,
        )
        foreign = foreign_type(**self.kwargs())
        with self.assertRaises(TypeError):
            self.validate((foreign, self.construct(boundary=self.subject.BoundaryKind.SESSION),
                           self.construct(boundary=self.subject.BoundaryKind.PROVIDER)))

    def test_sequence_rejects_boundary_check_subclass(self):
        class ForeignSubclass(self.subject.BoundaryCheck):
            pass
        foreign = guarded_call(ForeignSubclass, **self.kwargs())
        checks = self.sequence()
        with self.assertRaises(TypeError):
            self.validate((foreign, checks[1], checks[2]))

    def test_sequence_rejects_different_correlation_without_normalizing(self):
        checks = self.sequence()
        for correlation in ("SYNTHETIC-OTHER-CALL", " SYNTHETIC-CALL-001"):
            changed = self.construct(boundary=self.subject.BoundaryKind.SESSION,
                                     audit_correlation_id=correlation)
            with self.assertRaises(ValueError):
                self.validate((checks[0], changed, checks[2]))

    def test_sequence_accepts_mixed_allowed_pairs_without_creating_aggregate_outcome(self):
        checks = (
            self.construct(),
            self.construct(boundary=self.subject.BoundaryKind.SESSION,
                           state=self.subject.BoundaryCheckState.UNBOUND,
                           cause=self.subject.BoundaryCheckCause.SOURCE_UNBOUND,
                           expected_source_id=None, actual_source_id=None),
            self.construct(boundary=self.subject.BoundaryKind.PROVIDER,
                           state=self.subject.BoundaryCheckState.NOT_EVALUATED,
                           cause=self.subject.BoundaryCheckCause.PRIOR_DENIAL,
                           expected_source_id=None, actual_source_id=None),
        )
        self.assertIs(self.validate(checks), checks)
        self.assertFalse(hasattr(checks[0], "trusted"))
        self.assertFalse(hasattr(self.subject, "GateDecision"))
        self.assertFalse(hasattr(self.subject, "InvocationState"))

    def test_sequence_revalidates_low_level_mutation_of_synthetic_object(self):
        for field, value, error_type in (
            ("boundary", "PROJECT", TypeError),
            ("state", "MATCH", TypeError),
            ("cause", self.subject.BoundaryCheckCause.EXACT_UNEQUAL, ValueError),
            ("audit_correlation_id", "", ValueError),
            ("expected_source_id", None, ValueError),
            ("actual_source_id", 1, TypeError),
        ):
            checks = self.sequence()
            object.__setattr__(checks[0], field, value)
            with self.assertRaises(error_type):
                self.validate(checks)

    def test_sequence_rejects_uninitialized_synthetic_object(self):
        uninitialized = object.__new__(self.subject.BoundaryCheck)
        checks = self.sequence()
        with self.assertRaises(AttributeError):
            self.validate((uninitialized, checks[1], checks[2]))

    def test_source_imports_and_calls_exclude_io_gate_and_execution_entry(self):
        imports = [(node.module, tuple(alias.name for alias in node.names))
                   for node in self.subject_tree.body if isinstance(node, ast.ImportFrom)]
        self.assertEqual(imports, [("dataclasses", ("dataclass",)), ("enum", ("Enum", "unique"))])
        self.assertFalse(any(isinstance(node, ast.Import) for node in ast.walk(self.subject_tree)))
        forbidden = {"open", "eval", "exec", "compile", "input", "print", "__import__",
                     "evaluate_identity_gate", "extract_expected_baseline"}
        for node in ast.walk(self.subject_tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(node.func.id, forbidden)
        self.assertNotIn(b"if __name__", self.subject_bytes)
        self.assertNotIn("route_b_c03.contracts", sys.modules)

    def test_audit_guard_denies_open_before_access(self):
        with self.assertRaises(ForbiddenCandidateSideEffect):
            guarded_call(builtins.open, str(SUBJECT_PATH), "rb")
        self.assertEqual(_BLOCKED_EVENTS[self.blocked_before_test:], ["open"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
