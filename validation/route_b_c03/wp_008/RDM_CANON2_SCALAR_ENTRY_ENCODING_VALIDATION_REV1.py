"""Local synthetic oracle for the new scalar/entry projection candidate only.

No source admission, actual capture, Manifest generation, subject invocation,
file access or test dispatch at import. The external local controller supplies
one fixed candidate namespace. Expected bytes below are literal independent
vectors; no expected output is obtained by calling the encoder under test.
"""

from hashlib import sha256


def run_synthetic_checks(candidate: dict) -> dict:
    checks = []
    vectors = []
    rejected = candidate["EncodingRejected"]

    def check(identifier, condition):
        if type(condition) is not bool or not condition:
            raise AssertionError(identifier)
        checks.append({"Id": identifier, "Passed": True})

    def expect_rejection(identifier, call, code=None):
        try:
            call()
        except rejected as error:
            check(identifier, code is None or error.args == (code,))
        else:
            raise AssertionError(identifier)

    string = candidate["encode_string"]
    integer = candidate["encode_integer"]
    boolean = candidate["encode_boolean"]
    null = candidate["encode_null"]
    scalar = candidate["require_canonical_scalar"]
    parse = candidate["parse_synthetic_json"]
    aggregate = candidate["encode_ordered_entry_projection"]

    def vector(identifier, actual, expected):
        check(identifier + ".BYTES", actual == expected)
        check(identifier + ".NATIVE_BYTES", type(actual) is bytes)
        vectors.append({"Id": identifier, "Bytes": len(actual), "SHA256": sha256(actual).hexdigest().upper()})

    vector("S-EMPTY", string(""), b'""')
    vector("S-ESCAPES", string('"\\/'), b'"\\"\\\\/"')
    vector("S-UNICODE", string("中文/😀\u2028\u2029<>"), '"中文/😀\u2028\u2029<>"'.encode("utf-8"))
    control_expected = (
        b'"\\u0000\\u0001\\u0002\\u0003\\u0004\\u0005\\u0006\\u0007'
        b'\\u0008\\u0009\\u000a\\u000b\\u000c\\u000d\\u000e\\u000f'
        b'\\u0010\\u0011\\u0012\\u0013\\u0014\\u0015\\u0016\\u0017'
        b'\\u0018\\u0019\\u001a\\u001b\\u001c\\u001d\\u001e\\u001f"'
    )
    vector("S-ALL-CONTROLS", string("".join(chr(i) for i in range(32))), control_expected)
    check("S-NO-NORMALIZATION", string("é") != string("e\u0301"))
    for index, value in enumerate(("\ud800", "\udfff", "\ud800\udc00")):
        expect_rejection("S-SURROGATE-" + str(index), lambda value=value: string(value), "UNICODE_SURROGATE")
    expect_rejection("S-BYTES-NOT-STRING", lambda: string(b"x"), "STRING_TYPE")

    bound = 2**63
    vector("I-MIN", integer(-bound, -bound, bound - 1), b"-9223372036854775808")
    vector("I-MAX", integer(bound - 1, -bound, bound - 1), b"9223372036854775807")
    vector("I-BIG-EXACT", integer(10**50, 0, 10**50), b"100000000000000000000000000000000000000000000000000")
    for name, value in (("BOOL", True), ("FLOAT", 1.0), ("TEXT", "1")):
        expect_rejection("I-TYPE-" + name, lambda value=value: integer(value, 0, 10), "INTEGER_TYPE")
    expect_rejection("I-RANGE", lambda: integer(bound, -bound, bound - 1), "INTEGER_RANGE")
    expect_rejection("I-RANGE-CONTRACT", lambda: integer(0, True, 2), "INTEGER_RANGE_CONTRACT")
    vector("B-TRUE", boolean(True), b"true")
    vector("B-FALSE", boolean(False), b"false")
    expect_rejection("B-INT", lambda: boolean(1), "BOOLEAN_TYPE")
    vector("N-ALLOWED", null(True), b"null")
    expect_rejection("N-DENIED", lambda: null(False), "NULL_NOT_PERMITTED")

    for identifier, raw, kind, kwargs, value in (
        ("P-I64", b"9223372036854775807", "integer", {"minimum": -bound, "maximum": bound - 1}, bound - 1),
        ("P-TRUE", b"true", "boolean", {}, True),
        ("P-NULL", b"null", "null", {"nullable": True}, None),
        ("P-UNICODE", '"😀/中"'.encode("utf-8"), "string", {}, "😀/中"),
    ):
        result = scalar(raw, kind, **kwargs)
        check(identifier, type(result) is type(value) and result == value)
    for index, raw in enumerate((b"-0", b"1.0", b"1e0", b"NaN", b"Infinity", b"+1", b"01")):
        expect_rejection("P-NUMERIC-REJECT-" + str(index), lambda raw=raw: scalar(raw, "integer", minimum=-10, maximum=10))
    for index, raw in enumerate((b' "x"', b'"x"\n', b'"\\/"', b'"\\u4e2d"', b'"\\n"', b'"\\ud83d\\ude00"')):
        expect_rejection("P-NONCANONICAL-" + str(index), lambda raw=raw: scalar(raw, "string"), "NONCANONICAL_SCALAR_BYTES")
    for index, raw in enumerate((b'"\xff"', b'"\xc0\xaf"', b'\xef\xbb\xbf"x"')):
        expect_rejection("P-UTF8-BOM-" + str(index), lambda raw=raw: scalar(raw, "string"), "INVALID_JSON_OR_UTF8")
    expect_rejection("P-LONE-ESCAPED-SURROGATE", lambda: scalar(b'"\\ud800"', "string"), "UNICODE_SURROGATE")
    for index, raw in enumerate((b'{"a":1,"a":2}', b'{"a":1,"\\u0061":2}', b'{"x":{"b":1,"b":2}}')):
        expect_rejection("P-DECODED-DUPLICATE-" + str(index), lambda raw=raw: parse(raw), "DUPLICATE_DECODED_KEY")
    expect_rejection("P-BOOL-AS-INTEGER", lambda: scalar(b"true", "integer", minimum=0, maximum=10), "INTEGER_TYPE")
    expect_rejection("P-NULL-UNBOUND", lambda: scalar(b"null", "null"), "NULL_NOT_PERMITTED")

    # Fabricated file identifiers and digests are test data, not file bindings.
    base = {
        "ordinal": 1, "entry_id": "SYNTHETIC-A", "category": "FIXTURE_INPUT",
        "root_id": "SYNTHETIC-ROOT", "relative_path": "合成/a.txt", "byte_length": 2**63,
        "sha256": "A" * 64, "role": "SYNTHETIC-ONLY", "required_by": "SYNTHETIC-CHECK",
        "import_name": "NOT_APPLICABLE", "loader_kind": "DATA", "read_phase": "T1,T3",
        "executable": False, "network_capable": False, "reparse_state": "DIRECT",
    }
    expected = (
        b'1\x1f"SYNTHETIC-A"\x1f"FIXTURE_INPUT"\x1f"SYNTHETIC-ROOT"\x1f"'
        + "合成/a.txt".encode("utf-8")
        + b'"\x1f9223372036854775808\x1f"' + b"A" * 64
        + b'"\x1f"SYNTHETIC-ONLY"\x1f"SYNTHETIC-CHECK"\x1f"NOT_APPLICABLE"'
        b'\x1f"DATA"\x1f"T1,T3"\x1ffalse\x1ffalse\x1f"DIRECT"\n'
    )
    vector("E-ONE", aggregate((base,)), expected)
    reordered_fields = dict(reversed(tuple(base.items())))
    check("E-DICT-INSERTION-ORDER-IRRELEVANT", aggregate((reordered_fields,)) == expected)
    second = dict(base, ordinal=2, entry_id="SYNTHETIC-B", relative_path="合成/b.txt", byte_length=0)
    expected_second = expected.replace(b'1\x1f"SYNTHETIC-A"', b'2\x1f"SYNTHETIC-B"').replace(b'a.txt', b'b.txt').replace(b'9223372036854775808', b'0')
    vector("E-TWO", aggregate((base, second)), expected + expected_second)
    check("E-FRAMING", aggregate((base, second)).count(b"\x1f") == 28 and aggregate((base, second)).count(b"\n") == 2)
    control_entry = dict(base, role="x\x1f\ny")
    control_output = aggregate((control_entry,))
    check("E-NO-DELIMITER-INJECTION", control_output.count(b"\x1f") == 14 and control_output.count(b"\n") == 1 and b'"x\\u001f\\u000ay"' in control_output)
    # U+E000 precedes U+10000 by scalar value, unlike UTF-16 code-unit ordering.
    early = dict(base, relative_path="\ue000.txt")
    late = dict(second, relative_path="\U00010000.txt")
    check("E-CODEPOINT-ORDER", type(aggregate((early, late))) is bytes)
    expect_rejection("E-UTF16-ORDER-REFUSED", lambda: aggregate((dict(late, ordinal=1), dict(early, ordinal=2))), "ENTRY_ORDER")
    changes = (
        ("ORDINAL", "ordinal", 2, "ENTRY_ORDINAL"),
        ("BOOL-ORDINAL", "ordinal", True, "ENTRY_INTEGER"),
        ("NEGATIVE-LENGTH", "byte_length", -1, "ENTRY_INTEGER"),
        ("BOOL-LENGTH", "byte_length", False, "ENTRY_INTEGER"),
        ("BOOL-FLAG", "executable", 1, "ENTRY_BOOLEAN"),
        ("LOWERCASE-SHA", "sha256", "a" * 64, "ENTRY_SHA_SYNTAX"),
        ("SHORT-SHA", "sha256", "A" * 63, "ENTRY_SHA_SYNTAX"),
        ("CATEGORY", "category", "OTHER", "ENTRY_CATEGORY"),
        ("LOADER", "loader_kind", "OTHER", "ENTRY_LOADER"),
        ("PHASE-REVERSED", "read_phase", "T3,T1", "ENTRY_PHASE_ORDER"),
        ("PHASE-DUPLICATE", "read_phase", "T1,T1", "ENTRY_PHASE_ORDER"),
        ("PHASE-UNKNOWN", "read_phase", "T0", "ENTRY_PHASE_ORDER"),
        ("REPARSE", "reparse_state", "LINK", "REPARSE_MAPPING_UNSUPPORTED"),
        ("PARENT-PATH", "relative_path", "a/../b", "ENTRY_PATH"),
        ("ABS-PATH", "relative_path", "/a", "ENTRY_PATH"),
        ("BACKSLASH-PATH", "relative_path", "a\\b", "ENTRY_PATH"),
        ("EMPTY-SEGMENT", "relative_path", "a//b", "ENTRY_PATH"),
        ("WILDCARD", "relative_path", "a/*.txt", "ENTRY_UNRESOLVED_VALUE"),
        ("UNKNOWN", "root_id", "UNKNOWN", "ENTRY_UNRESOLVED_VALUE"),
    )
    for name, field, value, code in changes:
        expect_rejection("E-REJECT-" + name, lambda field=field, value=value: aggregate((dict(base, **{field: value}),)), code)
    expect_rejection("E-UNKNOWN-FIELD", lambda: aggregate((dict(base, extra="x"),)), "ENTRY_FIELDS_OR_TYPE")
    missing = dict(base)
    del missing["sha256"]
    expect_rejection("E-MISSING-FIELD", lambda: aggregate((missing,)), "ENTRY_FIELDS_OR_TYPE")
    expect_rejection("E-EMPTY-SET", lambda: aggregate(()), "ENTRY_SET_TYPE_OR_EMPTY")
    expect_rejection("E-DUPLICATE-ID", lambda: aggregate((base, dict(second, entry_id=base["entry_id"]))), "DUPLICATE_ENTRY_ID")
    expect_rejection("E-DUPLICATE-PATH", lambda: aggregate((base, dict(second, relative_path=base["relative_path"]))), "DUPLICATE_ROOT_PATH")
    expect_rejection("E-NONASCENDING", lambda: aggregate((second, base)), "ENTRY_ORDINAL")
    check("RESULT-UNIQUE-CHECK-IDS", len({item["Id"] for item in checks}) == len(checks))
    return {
        "Summary": {
            "Outcome": "LOCAL_SYNTHETIC_SCALAR_ENTRY_ENCODING_CHECKS_PASS",
            "EncodingId": "WP008-RDM-CANON-2",
            "CheckCount": len(checks), "VectorCount": len(vectors),
            "FormalManifestGenerated": False, "SourceAdmission": False,
            "WholeManifestCanonicalization": "NOT_IMPLEMENTED",
            "B01": "OPEN", "B02": "OPEN", "DSP004": "OPEN / HOLD",
        },
        "Checks": checks, "Vectors": vectors,
    }
