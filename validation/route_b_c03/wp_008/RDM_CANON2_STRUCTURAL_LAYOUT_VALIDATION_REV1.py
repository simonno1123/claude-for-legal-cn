"""Closed local synthetic vectors; not a real Manifest or accepted registry.

All expected rendered bytes are literal independent oracles. Contract tuples
below live only in this private validation batch; none is admission authority.
The module exposes one validation function and has no automatic test dispatch.
"""

from hashlib import sha256


def run_synthetic_checks(candidate):
    checks = []
    vectors = []
    rejected = candidate["TreeEncodingRejected"]
    document = candidate["encode_synthetic_document"]
    compact = candidate["encode_compact_synthetic_value"]
    require = candidate["require_canonical_synthetic_document"]
    string = ("string",)
    integer = ("integer", -10, 10)
    boolean = ("boolean",)

    def obj(*fields):
        return ("object", fields)

    def ordered(element, keys, repeats=False, selector=()):
        return ("array", element, ("ORDERED", selector, keys, repeats))

    def sorted_set(element, selector=()):
        return ("array", element, ("SET_SORTED", selector))

    def check(identifier, condition):
        if type(condition) is not bool or not condition:
            raise AssertionError(identifier)
        checks.append({"Id": identifier, "Passed": True})

    def vector(identifier, actual, expected):
        check(identifier + ".BYTES", actual == expected)
        check(identifier + ".NATIVE_BYTES", type(actual) is bytes)
        vectors.append({"Id": identifier, "Bytes": len(actual), "SHA256": sha256(actual).hexdigest().upper()})

    def deny(identifier, call, code):
        try:
            call()
        except rejected as error:
            check(identifier, error.args == (code,))
        else:
            raise AssertionError(identifier)

    vector("T-EMPTY", document({}, obj()), b"{}\n")
    mixed_spec = obj(("z", integer), ("a", sorted_set(integer)))
    mixed = {"z": 1, "a": [2, 1]}
    mixed_expected = b'{\n  "a": [\n    1,\n    2\n  ],\n  "z": 1\n}\n'
    vector("T-MIXED", document(mixed, mixed_spec), mixed_expected)
    ordered_spec = obj(("search", ordered(string, (("z",), ("a",)))))
    ordered_value = {"search": ["z", "a"]}
    ordered_expected = b'{\n  "search": [\n    "z",\n    "a"\n  ]\n}\n'
    vector("T-ORDERED", document(ordered_value, ordered_spec), ordered_expected)
    nullable_spec = obj(("a", ("nullable", string)), ("b", boolean), ("c", ("null",)))
    vector("T-NULLABLE", document({"c": None, "b": True, "a": None}, nullable_spec), b'{\n  "a": null,\n  "b": true,\n  "c": null\n}\n')
    unicode_spec = obj(("\U00010000", integer), ("\ue000", integer))
    vector("T-CODEPOINT-KEYS", document({"\U00010000": 2, "\ue000": 1}, unicode_spec), '{\n  "\ue000": 1,\n  "\U00010000": 2\n}\n'.encode("utf-8"))
    escaped_spec = obj(('"', string), ("\n", string))
    vector("T-ESCAPED-KEYS", document({'"': "中/😀", "\n": "\x00\x1f"}, escaped_spec), '{\n  "\\u000a": "\\u0000\\u001f",\n  "\\\"": "中/😀"\n}\n'.encode("utf-8"))
    row_spec = obj(("id", string), ("values", ordered(integer, ((2,), (1,)))))
    nested_spec = obj(("groups", sorted_set(row_spec, ("id",))))
    nested = {"groups": [{"id": "b", "values": [2, 1]}, {"values": [2, 1], "id": "a"}]}
    nested_expected = (
        b'{\n  "groups": [\n    {\n      "id": "a",\n      "values": [\n        2,\n        1\n      ]\n    },\n'
        b'    {\n      "id": "b",\n      "values": [\n        2,\n        1\n      ]\n    }\n  ]\n}\n'
    )
    vector("T-NESTED", document(nested, nested_spec), nested_expected)
    vector("T-EMPTY-CONTAINERS", document({"b": {}, "a": []}, obj(("b", obj()), ("a", ordered(string, ())))), b'{\n  "a": [],\n  "b": {}\n}\n')
    vector("T-COMPACT", compact(mixed, mixed_spec), b'{"a":[1,2],"z":1}')
    composite_spec = obj(("items", sorted_set(obj(("group", string), ("index", integer)), ("group", "index"))))
    vector("T-COMPOSITE-KEY", document({"items": [{"group": "a", "index": 2}, {"group": "b", "index": -1}, {"group": "a", "index": 1}]}, composite_spec),
           b'{\n  "items": [\n    {\n      "group": "a",\n      "index": 1\n    },\n    {\n      "group": "a",\n      "index": 2\n    },\n    {\n      "group": "b",\n      "index": -1\n    }\n  ]\n}\n')
    repeat_spec = obj(("a", ordered(integer, ((1,), (1,)), True)))
    vector("T-EXPLICIT-REPEATS", document({"a": [1, 1]}, repeat_spec), b'{\n  "a": [\n    1,\n    1\n  ]\n}\n')
    big_spec = obj(("i", ("integer", 0, 2**63)))
    vector("T-BIG-INTEGER", document({"i": 2**63}, big_spec), b'{\n  "i": 9223372036854775808\n}\n')

    check("P-ORIGINAL-BYTES-RETURNED", require(mixed_expected, mixed_spec) is mixed_expected)
    check("P-INSERTION-ORDER-IRRELEVANT", document({"a": [2, 1], "z": 1}, mixed_spec) == mixed_expected)
    check("P-SET-PERMUTATION-INVARIANT", document({"z": 1, "a": [1, 2]}, mixed_spec) == mixed_expected)
    check("P-INPUT-NOT-MUTATED", mixed == {"z": 1, "a": [2, 1]} and nested["groups"][0]["id"] == "b")
    check("P-EXACT-FINAL-LF", mixed_expected.endswith(b"}\n") and not mixed_expected.endswith(b"\n\n"))
    check("P-COMPACT-NO-FINAL-LF", not compact(mixed, mixed_spec).endswith(b"\n"))
    check("P-NULLABLE-NONNULL", document({"a": "x", "b": False, "c": None}, nullable_spec) == b'{\n  "a": "x",\n  "b": false,\n  "c": null\n}\n')

    simple = obj(("a", integer))
    class TextSubclass(str):
        pass
    cycle = {}
    cycle["a"] = cycle
    invalids = (
        ("N-CONTRACT-UNBOUND", lambda: document({}, None), "CONTRACT_REQUIRED"),
        ("N-UNKNOWN-KIND", lambda: document({}, ("mystery",)), "CONTRACT_KIND"),
        ("N-SCALAR-ARITY", lambda: document("x", ("string", 1)), "SCALAR_CONTRACT_ARITY"),
        ("N-INTEGER-BOUNDS", lambda: document(1, ("integer", True, 10)), "INTEGER_CONTRACT_RANGE"),
        ("N-DUPLICATE-SPEC-MEMBER", lambda: document({"a": 1}, obj(("a", integer), ("a", integer))), "DUPLICATE_CONTRACT_MEMBER"),
        ("N-NONNATIVE-SPEC-KEY", lambda: document({"a": 1}, obj((TextSubclass("a"), integer))), "STRING_TYPE"),
        ("N-NONNATIVE-VALUE-KEY", lambda: document({TextSubclass("a"): 1}, simple), "STRING_TYPE"),
        ("N-MISSING-MEMBER", lambda: document({}, simple), "OBJECT_MEMBERS"),
        ("N-UNKNOWN-MEMBER", lambda: document({"a": 1, "b": 2}, simple), "OBJECT_MEMBERS"),
        ("N-ROOT-TYPE", lambda: document([1], ordered(integer, ((1,),))), "DOCUMENT_ROOT_OBJECT_REQUIRED"),
        ("N-TUPLE-NOT-JSON-ARRAY", lambda: document({"a": (1,)}, obj(("a", sorted_set(integer)))), "CONTAINER_TYPE"),
        ("N-BOOL-NOT-INTEGER", lambda: document({"a": True}, simple), "SCALAR_VALUE_REJECTED"),
        ("N-FLOAT-NOT-INTEGER", lambda: document({"a": 1.0}, simple), "SCALAR_VALUE_REJECTED"),
        ("N-NULL-NOT-STRING", lambda: document({"a": None}, obj(("a", string))), "STRING_TYPE"),
        ("N-NULL-VALUE", lambda: document({"a": 0}, obj(("a", ("null",)))), "NULL_VALUE"),
        ("N-NULLABLE-AMBIGUOUS", lambda: document({"a": None}, obj(("a", ("nullable", ("null",))))), "NULLABLE_AMBIGUOUS"),
        ("N-POLICY-MISSING", lambda: document({"a": []}, obj(("a", ("array", string)))), "ARRAY_POLICY_REQUIRED"),
        ("N-POLICY-UNKNOWN", lambda: document({"a": []}, obj(("a", ("array", string, ("AUTO", ()))))), "ARRAY_POLICY_KIND"),
        ("N-POLICY-OVERLAP-ARITY", lambda: document({"a": []}, obj(("a", ("array", string, ("SET_SORTED", (), "ORDERED"))))), "ARRAY_POLICY_ARITY"),
        ("N-ORDERED-WRONG-SEQUENCE", lambda: document({"search": ["a", "z"]}, ordered_spec), "ORDERED_SEQUENCE_MISMATCH"),
        ("N-ORDERED-WRONG-MEMBERSHIP", lambda: document({"search": ["z", "b"]}, ordered_spec), "ORDERED_SEQUENCE_MISMATCH"),
        ("N-ORDERED-REPEAT-UNBOUND", lambda: document({"a": [1, 1]}, obj(("a", ordered(integer, ((1,), (1,)))))), "ORDERED_REPEAT_UNBOUND"),
        ("N-ORDERED-EXPECTED-BOOL", lambda: document({"a": [1]}, obj(("a", ordered(integer, ((True,),))))), "KEY_INTEGER"),
        ("N-SORT-TIE", lambda: document({"a": [1, 1]}, obj(("a", sorted_set(integer)))), "SET_SORTED_TIE"),
        ("N-OBJECT-KEY-TIE", lambda: document({"groups": [{"id": "x", "values": [2, 1]}, {"id": "x", "values": [2, 1]}]}, nested_spec), "SET_SORTED_TIE"),
        ("N-SELECTOR-MISSING", lambda: document({"a": []}, obj(("a", sorted_set(row_spec, ("missing",))))), "SELECTOR_MEMBER"),
        ("N-SELECTOR-DUPLICATE", lambda: document({"a": []}, obj(("a", sorted_set(row_spec, ("id", "id"))))), "SELECTOR_MEMBER"),
        ("N-SELECTOR-BOOL", lambda: document({"a": []}, obj(("a", sorted_set(obj(("b", boolean)), ("b",))))), "SELECTOR_KEY_TYPE"),
        ("N-SELECTOR-ARRAY", lambda: document({"a": []}, obj(("a", sorted_set(row_spec, ("values",))))), "SELECTOR_KEY_TYPE"),
        ("N-SCALAR-SELECTOR", lambda: document({"a": []}, obj(("a", sorted_set(string, ("x",))))), "SCALAR_SELECTOR_NOT_EMPTY"),
        ("N-VALUE-CYCLE", lambda: document(cycle, obj(("a", obj(("b", integer))))), "VALUE_CYCLE"),
        ("N-STRING-LIMIT", lambda: document({"a": "x" * 32769}, obj(("a", string))), "STRING_LIMIT"),
        ("N-RAW-BYTES-LIMIT", lambda: require(b" " * 262145, obj()), "RAW_BYTES_OR_LIMIT"),
    )
    for identifier, call, code in invalids:
        deny(identifier, call, code)
    for identifier, raw in (
        ("R-KEY-ORDER", b'{\n  "z": 1,\n  "a": [\n    1,\n    2\n  ]\n}\n'),
        ("R-SET-ORDER", b'{\n  "a": [\n    2,\n    1\n  ],\n  "z": 1\n}\n'),
        ("R-COMPACT", b'{"a":[1,2],"z":1}'),
        ("R-DOUBLE-LF", mixed_expected + b"\n"),
        ("R-CRLF", mixed_expected.replace(b"\n", b"\r\n")),
    ):
        deny(identifier, lambda raw=raw: require(raw, mixed_spec), "NONCANONICAL_DOCUMENT_BYTES")
    for identifier, raw in (
        ("R-DUPLICATE", b'{"a":1,"a":2}'),
        ("R-ESCAPED-DUPLICATE", b'{"a":1,"\\u0061":2}'),
        ("R-NONINTEGER-TOKEN", b'{"a":1e0}'),
        ("R-NEGATIVE-ZERO", b'{"a":-0}'),
        ("R-BOM", b'\xef\xbb\xbf{"a":1}'),
        ("R-BAD-UTF8", b'{"a":"\xff"}'),
    ):
        deny(identifier, lambda raw=raw: require(raw, simple), "RAW_JSON_REJECTED")
    deny("R-LONE-SURROGATE", lambda: require(b'{"a":"\\ud800"}', obj(("a", string))), "SCALAR_STRING_REJECTED")
    deep_spec, deep_value = integer, 1
    for _index in range(34):
        deep_spec, deep_value = obj(("a", deep_spec)), {"a": deep_value}
    deny("L-DEPTH", lambda: document(deep_value, deep_spec), "DEPTH_LIMIT")
    many_spec = obj(("a", sorted_set(integer)))
    deny("L-NODES", lambda: document({"a": list(range(-10, 10)) * 205}, many_spec), "NODE_LIMIT")
    long_list_spec = obj(("a", sorted_set(string)))
    deny("L-PROJECTION-BYTES", lambda: document({"a": [str(i) + "x" * 32000 for i in range(10)]}, long_list_spec), "PROJECTION_BYTE_LIMIT")
    deny("L-OUTPUT-BYTES", lambda: document({"a": [format(i, "04d") + "x" * 58 for i in range(4092)]}, long_list_spec), "OUTPUT_BYTE_LIMIT")
    check("RESULT-UNIQUE-CHECK-IDS", len({item["Id"] for item in checks}) == len(checks))
    return {
        "Summary": {
            "Outcome": "LOCAL_SYNTHETIC_STRUCTURAL_LAYOUT_CHECKS_PASS",
            "EncodingId": "WP008-RDM-CANON-2",
            "CheckCount": len(checks), "VectorCount": len(vectors),
            "FormalManifestGenerated": False, "SourceAdmission": False,
            "StructuralLayout": "EXPLICIT_SYNTHETIC_CONTRACTS_ONLY",
            "FormalTypedContract": "NOT_ESTABLISHED_BY_THIS_BATCH",
            "FormalOrderRegistry": "NOT_ESTABLISHED_BY_THIS_BATCH",
            "B01": "OPEN", "B02": "OPEN", "DSP004": "OPEN / HOLD",
        },
        "Checks": checks, "Vectors": vectors,
    }
