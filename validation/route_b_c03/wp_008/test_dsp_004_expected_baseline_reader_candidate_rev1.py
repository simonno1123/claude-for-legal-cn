"""Authorized local synthetic diagnostic for the fixed DSP-004 reader candidate.

Run with .venv-validation/Scripts/python.exe -I -S -B and this exact script.
This is not the WP-008 Harness, source admission, actual capture, or a context
boundary comparison. It does not amend or accept the candidate or old manifest.
The runtime version below binds this batch's observed interpreter, not the
older inventory's version. Results are emitted to the console only.

Public-entry mutation tests retain the real pinned SHA guard. Parser-negative
and value-preservation probes call private pure helpers on synthetic fragments;
they do not establish admission or public-entry acceptance of those fragments.
The candidate's bytes, globals, and functions are not patched or rewritten.
"""

import ast
import builtins
import dataclasses
import hashlib
import json
from pathlib import Path
import sys
import types
import unittest


ROOT = Path(__file__).resolve().parents[3]
SUBJECT_PATH = (
    ROOT / "validation/route_b_c03/wp_008/"
    "DSP_004_EXPECTED_BASELINE_READER_CANDIDATE_REV1.py"
)
BASELINE_PATH = (
    ROOT / "docs/phase2/route-b/"
    "TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_SYNTHETIC_EXPECTED_BASELINE_REV1.md"
)
SUBJECT_SHA256 = "AE1389EDA1C3B9129A0546DA5764C1F68A6B0193A22DA3431CAA89BAB8DC0727"
BASELINE_SHA256 = "BE8C55796587BBA65E22B048291E1688A8B076D02DA2A48DE412919BEB10F368"
EXPECTED_RUNTIME = (3, 12, 14)
PROJECT_HEADING = "### 3.1 Project 预期来源候选"
SESSION_HEADING = "### 3.2 Session 预期来源候选"
ORIGINAL_REFERENCE_ROW = "| Expected Reference | SYNTHETIC-PROJECT-001 |"
EXPECTED_RECORDS = (
    (
        "SRC004-E-PROJECT",
        "DSP004-EXPECTED-PROJECT-V1",
        "本文件第 3.1 节，Field = Expected Reference 的唯一表格行",
        "SYNTHETIC-PROJECT-001",
    ),
    (
        "SRC004-E-SESSION",
        "DSP004-EXPECTED-SESSION-V1",
        "本文件第 3.2 节，Field = Expected Reference 的唯一表格行",
        "SYNTHETIC-SESSION-001",
    ),
    (
        "SRC004-E-PROVIDER",
        "DSP004-EXPECTED-PROVIDER-V1",
        "本文件第 3.3 节，Field = Expected Reference 的唯一表格行",
        "SYNTHETIC-PROVIDER-001",
    ),
)

_GUARD_ACTIVE = False
_BLOCKED_EVENTS: list[str] = []


class ForbiddenCandidateSideEffect(RuntimeError):
    pass


def audit_guard(event, args):
    """Deny audited file/OS/network/process effects during subject calls only."""
    if _GUARD_ACTIVE and (
        event == "open"
        or event.startswith(("os.", "socket.", "subprocess.", "ctypes.", "winreg."))
    ):
        _BLOCKED_EVENTS.append(event)
        raise ForbiddenCandidateSideEffect(event)


def guarded_call(function, *args):
    global _GUARD_ACTIVE
    if _GUARD_ACTIVE:
        raise RuntimeError("Nested candidate guard is not permitted")
    _GUARD_ACTIVE = True
    try:
        return function(*args)
    finally:
        _GUARD_ACTIVE = False


def read_fixed_bytes(path, expected_sha):
    payload = path.read_bytes()
    actual_sha = hashlib.sha256(payload).hexdigest().upper()
    if actual_sha != expected_sha:
        raise RuntimeError(f"Fixed input mismatch: {path.name}: {actual_sha}")
    return payload


class ExpectedBaselineReaderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if sys.version_info[:3] != EXPECTED_RUNTIME:
            raise RuntimeError("Interpreter differs from this batch's observed version")
        if not (
            sys.flags.isolated == 1
            and sys.flags.no_site == 1
            and sys.flags.dont_write_bytecode == 1
        ):
            raise RuntimeError("Required -I -S -B isolation flags are absent")
        cls.subject_bytes = read_fixed_bytes(SUBJECT_PATH, SUBJECT_SHA256)
        cls.baseline_bytes = read_fixed_bytes(BASELINE_PATH, BASELINE_SHA256)
        cls.subject_tree = ast.parse(cls.subject_bytes, filename=str(SUBJECT_PATH))
        baseline_lines = cls.baseline_bytes.decode("utf-8").split("\n")
        start = baseline_lines.index(PROJECT_HEADING) + 1
        end = baseline_lines.index(SESSION_HEADING)
        cls.project_section = baseline_lines[start:end]
        cls.project_table = [line for line in cls.project_section if line.startswith("|")]
        cls.subject = types.ModuleType("dsp004_reader_local_diagnostic_rev1")
        cls.subject.__file__ = str(SUBJECT_PATH)
        sys.modules[cls.subject.__name__] = cls.subject
        sys.addaudithook(audit_guard)
        subject_code = compile(
            cls.subject_bytes, str(SUBJECT_PATH), "exec", dont_inherit=True, optimize=0
        )
        guarded_call(exec, subject_code, cls.subject.__dict__)
        cls.blocked_events_before_tests = len(_BLOCKED_EVENTS)

    def setUp(self):
        self.blocked_before_test = len(_BLOCKED_EVENTS)

    def tearDown(self):
        if self._testMethodName != "test_audit_guard_rejects_open_before_access":
            self.assertEqual(len(_BLOCKED_EVENTS), self.blocked_before_test)

    @classmethod
    def tearDownClass(cls):
        read_fixed_bytes(SUBJECT_PATH, SUBJECT_SHA256)
        read_fixed_bytes(BASELINE_PATH, BASELINE_SHA256)
        print(json.dumps({
            "diagnostic": "DSP004_READER_LOCAL_SYNTHETIC_ONLY",
            "runtime": sys.version,
            "subject_sha256": SUBJECT_SHA256,
            "baseline_sha256": BASELINE_SHA256,
            "isolation_flags": "-I -S -B",
            "inputs_unchanged": True,
            "blocked_audit_events_including_guard_self_test": _BLOCKED_EVENTS,
            "source_admission": "NOT ESTABLISHED",
            "actual_capture": "NOT PERFORMED",
            "formal_wp008_validation": "NOT PERFORMED",
            "unexercised_public_branches": [
                "DECODE_FAILURE after valid pinned SHA",
                "Malformed document branches after valid pinned SHA",
                "Metadata conflict branch after valid pinned SHA",
            ],
        }, ensure_ascii=False))

    def assert_extraction_error(self, code, function, *args):
        with self.assertRaises(self.subject.ExpectedBaselineExtractionError) as caught:
            guarded_call(function, *args)
        self.assertEqual(caught.exception.code, code)

    def read_fields(self, table):
        return guarded_call(self.subject._read_table_fields, table, PROJECT_HEADING)

    def replace_reference(self, value):
        return [
            f"| Expected Reference | {value} |" if line == ORIGINAL_REFERENCE_ROW else line
            for line in self.project_table
        ]

    def test_runtime_isolation_and_fixed_input_identity(self):
        self.assertEqual(sys.version_info[:3], EXPECTED_RUNTIME)
        self.assertEqual((sys.flags.isolated, sys.flags.no_site, sys.flags.dont_write_bytecode),
                         (1, 1, 1))
        self.assertEqual(self.subject.BASELINE_SHA256, BASELINE_SHA256)

    def test_public_entry_extracts_three_exact_records(self):
        records = guarded_call(self.subject.extract_expected_baseline, self.baseline_bytes)
        self.assertIs(type(records), tuple)
        self.assertEqual(len(records), 3)
        observed = []
        for record in records:
            self.assertIs(type(record), self.subject.ExpectedBaselineRecord)
            values = (record.source_role, record.candidate_source_identity,
                      record.record_locator, record.expected_reference)
            self.assertTrue(all(type(value) is str for value in values))
            observed.append(values)
        self.assertEqual(tuple(observed), EXPECTED_RECORDS)

    def test_output_has_only_four_literal_fields_and_is_frozen(self):
        record = guarded_call(self.subject.extract_expected_baseline, self.baseline_bytes)[0]
        self.assertEqual(tuple(field.name for field in dataclasses.fields(record)),
                         ("source_role", "candidate_source_identity", "record_locator",
                          "expected_reference"))
        self.assertFalse(hasattr(record, "__dict__"))
        with self.assertRaises(dataclasses.FrozenInstanceError):
            record.expected_reference = "SYNTHETIC-CHANGED"

    def test_repeated_calls_keep_exact_values_without_partial_reuse(self):
        first = guarded_call(self.subject.extract_expected_baseline, self.baseline_bytes)
        second = guarded_call(self.subject.extract_expected_baseline, self.baseline_bytes)
        self.assertEqual(first, second)
        self.assertTrue(all(left is not right for left, right in zip(first, second)))

    def test_public_entry_rejects_non_native_bytes(self):
        class BytesSubclass(bytes):
            pass
        for value in (None, 1, "text", bytearray(self.baseline_bytes),
                      memoryview(self.baseline_bytes), BytesSubclass(self.baseline_bytes)):
            with self.subTest(input_type=type(value).__name__):
                self.assert_extraction_error("INVALID_INPUT_TYPE",
                                             self.subject.extract_expected_baseline, value)

    def test_public_entry_rejects_empty_truncated_and_appended_bytes(self):
        for value in (b"", self.baseline_bytes[:-1], self.baseline_bytes + b"\n"):
            with self.subTest(length=len(value)):
                self.assert_extraction_error("CARRIER_SHA_MISMATCH",
                                             self.subject.extract_expected_baseline, value)

    def test_public_entry_rejects_changed_value_and_metadata_without_rebinding(self):
        for original, replacement in (
            (b"SYNTHETIC-PROJECT-001", b"SYNTHETIC-PROJECT-999"),
            (b"SRC004-E-SESSION", b"SRC004-E-OTHER"),
            (b"DSP004-EXPECTED-PROVIDER-V1", b"DSP004-EXPECTED-PROVIDER-V2"),
        ):
            self.assertIn(original, self.baseline_bytes)
            self.assert_extraction_error("CARRIER_SHA_MISMATCH",
                                         self.subject.extract_expected_baseline,
                                         self.baseline_bytes.replace(original, replacement, 1))

    def test_public_entry_sha_guard_precedes_decode_and_format_checks(self):
        for value in (b"\xff", self.baseline_bytes.replace(b"\n", b"\r\n"),
                      b"\xef\xbb\xbf" + self.baseline_bytes):
            with self.subTest(length=len(value)):
                self.assert_extraction_error("CARRIER_SHA_MISMATCH",
                                             self.subject.extract_expected_baseline, value)

    def test_unique_line_helper_accepts_only_one_exact_marker(self):
        self.assertEqual(guarded_call(self.subject._unique_line_index,
                                     ["before", PROJECT_HEADING, "after"], PROJECT_HEADING), 1)

    def test_unique_line_helper_rejects_missing_or_nonexact_marker(self):
        for lines in ([], [PROJECT_HEADING + " "], [" " + PROJECT_HEADING]):
            self.assert_extraction_error("MISSING_RECORD", self.subject._unique_line_index,
                                         lines, PROJECT_HEADING)

    def test_unique_line_helper_rejects_duplicate_marker(self):
        self.assert_extraction_error("DUPLICATE_RECORD", self.subject._unique_line_index,
                                     [PROJECT_HEADING, PROJECT_HEADING], PROJECT_HEADING)

    def test_parser_helper_accepts_fixed_project_table(self):
        fields = self.read_fields(self.project_section)
        self.assertEqual(fields["Source Role"], "SRC004-E-PROJECT")
        self.assertEqual(fields["Expected Reference"], "SYNTHETIC-PROJECT-001")
        self.assertEqual(len(fields), 11)

    def test_parser_helper_rejects_missing_table(self):
        self.assert_extraction_error("MISSING_RECORD", self.subject._read_table_fields,
                                     ["synthetic prose"], PROJECT_HEADING)

    def test_parser_helper_rejects_indented_table_row(self):
        table = list(self.project_table)
        table[2] = " " + table[2]
        self.assert_extraction_error("FORMAT_FAILURE", self.subject._read_table_fields,
                                     table, PROJECT_HEADING)

    def test_parser_helper_rejects_noncontiguous_or_multiple_tables(self):
        for table in (self.project_table[:3] + [""] + self.project_table[3:],
                      self.project_table + [""] + self.project_table):
            self.assert_extraction_error("FORMAT_FAILURE", self.subject._read_table_fields,
                                         table, PROJECT_HEADING)

    def test_parser_helper_rejects_header_and_separator_drift(self):
        for index in (0, 1):
            table = list(self.project_table)
            table[index] = "| UNRECOGNIZED | HEADER |"
            self.assert_extraction_error("FORMAT_FAILURE", self.subject._read_table_fields,
                                         table, PROJECT_HEADING)

    def test_parser_helper_rejects_missing_reference(self):
        table = [line for line in self.project_table if line != ORIGINAL_REFERENCE_ROW]
        self.assert_extraction_error("MISSING_RECORD", self.subject._read_table_fields,
                                     table, PROJECT_HEADING)

    def test_parser_helper_rejects_duplicate_reference(self):
        self.assert_extraction_error("DUPLICATE_RECORD", self.subject._read_table_fields,
                                     self.project_table + [ORIGINAL_REFERENCE_ROW], PROJECT_HEADING)

    def test_parser_helper_rejects_conflicting_reference(self):
        table = self.project_table + ["| Expected Reference | SYNTHETIC-PROJECT-999 |"]
        self.assert_extraction_error("RECORD_CONFLICT", self.subject._read_table_fields,
                                     table, PROJECT_HEADING)

    def test_parser_helper_rejects_unknown_or_out_of_order_field(self):
        table = list(self.project_table)
        table[2] = "| Unknown Field | SYNTHETIC |"
        self.assert_extraction_error("FORMAT_FAILURE", self.subject._read_table_fields,
                                     table, PROJECT_HEADING)
        table = list(self.project_table)
        table[2], table[3] = table[3], table[2]
        self.assert_extraction_error("FORMAT_FAILURE", self.subject._read_table_fields,
                                     table, PROJECT_HEADING)

    def test_parser_helper_rejects_bad_framing_columns_and_literal_pipe(self):
        for row in ("| Expected Reference | SYNTHETIC | EXTRA |",
                    "| Expected Reference | SYNTHETIC|PIPE |",
                    "|Expected Reference | SYNTHETIC |",
                    "| Expected Reference | SYNTHETIC|"):
            table = [row if line == ORIGINAL_REFERENCE_ROW else line
                     for line in self.project_table]
            self.assert_extraction_error("FORMAT_FAILURE", self.subject._read_table_fields,
                                         table, PROJECT_HEADING)

    def test_parser_helper_rejects_empty_and_whitespace_only_reference(self):
        for value in ("", "   ", "\t"):
            self.assert_extraction_error("FORMAT_FAILURE", self.subject._read_table_fields,
                                         self.replace_reference(value), PROJECT_HEADING)

    def test_parser_helper_preserves_value_whitespace_and_unicode_exactly(self):
        for value in ("  SYNTHETIC-PROJECT-002  ", "SYNTHETIC-É", "SYNTHETIC-E\u0301"):
            self.assertEqual(self.read_fields(self.replace_reference(value))["Expected Reference"],
                             value)

    def test_source_imports_are_standard_library_only_and_no_main_guard(self):
        imports = [(node.module, tuple(alias.name for alias in node.names))
                   for node in self.subject_tree.body if isinstance(node, ast.ImportFrom)]
        self.assertEqual(imports, [("dataclasses", ("dataclass",)), ("hashlib", ("sha256",))])
        self.assertFalse(any(isinstance(node, ast.Import) for node in ast.walk(self.subject_tree)))
        forbidden_calls = {"open", "eval", "exec", "compile", "input", "print", "__import__"}
        for node in ast.walk(self.subject_tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(node.func.id, forbidden_calls)
        self.assertNotIn(b"if __name__", self.subject_bytes)

    def test_audit_guard_rejects_open_before_access(self):
        with self.assertRaises(ForbiddenCandidateSideEffect):
            guarded_call(builtins.open, str(SUBJECT_PATH), "rb")
        self.assertEqual(_BLOCKED_EVENTS[self.blocked_before_test:], ["open"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
