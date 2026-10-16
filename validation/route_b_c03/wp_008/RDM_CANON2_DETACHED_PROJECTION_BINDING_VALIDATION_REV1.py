"""Independent literal fixtures for a private local synthetic consistency run.

Expected entry tokens and canonical entry text below are literals, not emitted
by the candidate or its dependencies. stdlib JSON is used only for negative
case construction / independent parsing of these restricted fixture values.
No source admission, real file contents or business observations are supplied.
"""

import base64
import copy
import hashlib
import json


ENTRY_A = '''    {
      "byte_length": 7,
      "category": "HARNESS_SOURCE",
      "entry_id": "e01",
      "executable": true,
      "import_name": "fixture_a",
      "loader_kind": "SOURCE",
      "network_capable": false,
      "ordinal": 1,
      "read_phase": "T1,T2",
      "relative_path": "a.py",
      "reparse_state": "DIRECT",
      "required_by": "synthetic_runner",
      "role": "FIXTURE",
      "root_id": "synthetic-root",
      "sha256": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    }'''
ENTRY_B = '''    {
      "byte_length": 11,
      "category": "HARNESS_SOURCE",
      "entry_id": "e02",
      "executable": true,
      "import_name": "fixture_b",
      "loader_kind": "SOURCE",
      "network_capable": false,
      "ordinal": 2,
      "read_phase": "T1,T2",
      "relative_path": "b.py",
      "reparse_state": "DIRECT",
      "required_by": "synthetic_runner",
      "role": "FIXTURE",
      "root_id": "synthetic-root",
      "sha256": "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
    }'''
TOKENS_A = (
    b'1', b'"e01"', b'"HARNESS_SOURCE"', b'"synthetic-root"', b'"a.py"', b'7',
    b'"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"',
    b'"FIXTURE"', b'"synthetic_runner"', b'"fixture_a"', b'"SOURCE"',
    b'"T1,T2"', b'true', b'false', b'"DIRECT"',
)
TOKENS_B = (
    b'2', b'"e02"', b'"HARNESS_SOURCE"', b'"synthetic-root"', b'"b.py"', b'11',
    b'"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"',
    b'"FIXTURE"', b'"synthetic_runner"', b'"fixture_b"', b'"SOURCE"',
    b'"T1,T2"', b'true', b'false', b'"DIRECT"',
)
SCOPE = "LOCAL_SYNTHETIC_PROJECTION_ONLY"
ENCODING = "WP008-RDM-CANON-2"
QUALIFIER = "DATA_CONSISTENCY_ONLY_NO_SOURCE_OR_AUTHORITY"


def digest(raw):
    return hashlib.sha256(raw).hexdigest().upper()


def literal_document(entry_texts, count, total, aggregate_sha, label="fixture-alpha"):
    return (
        '{\n  "aggregate": {\n    "byte_total": ' + str(total)
        + ',\n    "entry_count": ' + str(count)
        + ',\n    "sha256": "' + aggregate_sha
        + '"\n  },\n  "encoding": "WP008-RDM-CANON-2",\n  "entries": [\n'
        + ',\n'.join(entry_texts)
        + '\n  ],\n  "projection_label": "' + label
        + '",\n  "scope": "LOCAL_SYNTHETIC_PROJECTION_ONLY"\n}\n'
    ).encode("utf-8")


def native_document(value):
    # Only independent negative-case construction, never an expected-byte oracle
    # for arbitrary Unicode/control escaping or the production CANON-2 rules.
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n").encode("utf-8")


def detached_for(raw, stream_sha, count, total):
    return {
        "encoding": ENCODING, "scope": SCOPE, "document_sha256": digest(raw),
        "aggregate_sha256": stream_sha, "entry_count": count, "byte_total": total,
    }


def run_synthetic_checks(candidate):
    verify = candidate["verify_synthetic_projection"]
    rejected = candidate["ProjectionBindingRejected"]
    checks = []
    vectors = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append({"Check": name, "Status": "PASS"})

    def refuse(name, raw, metadata, expected_code):
        try:
            verify(raw, metadata)
        except rejected as error:
            check(name, error.args == (expected_code,))
        else:
            raise AssertionError(name)

    row_a = b"\x1f".join(TOKENS_A) + b"\n"
    row_b = b"\x1f".join(TOKENS_B) + b"\n"
    one = literal_document((ENTRY_A,), 1, 7, digest(row_a))
    two = literal_document((ENTRY_A, ENTRY_B), 2, 18, digest(row_a + row_b))
    large = (1 << 63) + 9
    big_text = ENTRY_A.replace('"byte_length": 7', '"byte_length": 9223372036854775817').replace('"a.py"', '"合同/😀.py"')
    big_tokens = list(TOKENS_A)
    big_tokens[4] = '"合同/😀.py"'.encode("utf-8")
    big_tokens[5] = b"9223372036854775817"
    big_stream = b"\x1f".join(big_tokens) + b"\n"
    big = literal_document((big_text,), 1, large, digest(big_stream))
    metadata = detached_for(one, digest(row_a), 1, 7)

    for name, raw, stream, count, total in (
        ("P-ONE", one, row_a, 1, 7),
        ("P-TWO", two, row_a + row_b, 2, 18),
        ("P-LARGE-UNICODE", big, big_stream, 1, large),
    ):
        supplied = detached_for(raw, digest(stream), count, total)
        before = supplied.copy()
        result = verify(raw, supplied)
        check(name + ".NATIVE_TUPLE", type(result) is tuple and len(result) == 5)
        check(name + ".QUALIFIER", result[0] == QUALIFIER)
        check(name + ".DOCUMENT_SHA", result[1] == digest(raw))
        check(name + ".STREAM_SHA", result[2] == digest(stream))
        check(name + ".COUNT_TOTAL", type(result[3]) is int and type(result[4]) is int and result[3:] == (count, total))
        check(name + ".METADATA_UNCHANGED", supplied == before)
        vectors.append({
            "Vector": name, "DocumentBytes": len(raw), "DocumentSHA256": digest(raw),
            "DocumentBase64": base64.b64encode(raw).decode("ascii"),
            "StreamBytes": len(stream), "StreamSHA256": digest(stream),
            "StreamBase64": base64.b64encode(stream).decode("ascii"),
            "EntryCount": count, "ByteTotalDecimal": str(total), "Qualifier": result[0],
        })

    # Metadata outside the entry stream is protected by the FULL document hash.
    changed_label = one.replace(b'fixture-alpha', b'fixture-bravo')
    refuse("L-LABEL-STALE-FULL-SHA", changed_label, metadata, "DOCUMENT_SHA_MISMATCH")
    changed_metadata = detached_for(changed_label, digest(row_a), 1, 7)
    changed_result = verify(changed_label, changed_metadata)
    check("L-LABEL-SAME-AGGREGATE", changed_result[2] == digest(row_a))
    check("L-LABEL-DIFFERENT-FULL-SHA", changed_result[1] != digest(one))
    check("L-RECOMPUTED-PAIR-NOT-AUTHORITY", changed_result[0] == QUALIFIER)
    check("L-CALLER-ORIGINAL-UNCHANGED", metadata == detached_for(one, digest(row_a), 1, 7))

    class DictSubclass(dict):
        pass

    for name, value in (("NONE", None), ("LIST", []), ("SUBCLASS", DictSubclass(metadata))):
        refuse("D-TYPE-" + name, one, value, "DETACHED_TYPE")
    bad = metadata.copy()
    bad[7] = "not a string key"
    refuse("D-KEY-TYPE", one, bad, "DETACHED_KEY_TYPE")
    for field in metadata:
        bad = metadata.copy()
        del bad[field]
        refuse("D-MISSING-" + field.upper(), one, bad, "DETACHED_FIELDS")
    bad = dict(metadata, authorization="not permitted")
    refuse("D-EXTRA-FIELD", one, bad, "DETACHED_FIELDS")
    for field, values, code in (
        ("encoding", ("OTHER", None, 1), "DETACHED_ENCODING"),
        ("scope", ("PRODUCTION", None, 1), "DETACHED_SCOPE"),
        ("entry_count", (True, 0, 129, 1.0, "1"), "DETACHED_COUNT_RANGE"),
        ("byte_total", (True, -1, 128 * ((1 << 64) - 1) + 1, 7.0, "7"), "DETACHED_TOTAL_RANGE"),
    ):
        for index, value in enumerate(values):
            bad = metadata.copy()
            bad[field] = value
            refuse("D-" + field.upper() + "-" + str(index), one, bad, code)
    for field in ("document_sha256", "aggregate_sha256"):
        for name, value in (("LOWER", "a" * 64), ("SHORT", "A" * 63), ("NONHEX", "G" * 64), ("TYPE", 123)):
            bad = metadata.copy()
            bad[field] = value
            refuse("D-" + field.upper() + "-" + name, one, bad, "DETACHED_SHA_FORMAT")
    for field, value, code in (
        ("document_sha256", "0" * 64, "DOCUMENT_SHA_MISMATCH"),
        ("aggregate_sha256", "0" * 64, "DETACHED_AGGREGATE_SHA_MISMATCH"),
        ("entry_count", 2, "DETACHED_COUNT_MISMATCH"),
        ("byte_total", 8, "DETACHED_TOTAL_MISMATCH"),
    ):
        bad = metadata.copy()
        bad[field] = value
        refuse("D-MISMATCH-" + field.upper(), one, bad, code)
    for name, raw in (("STRING", one.decode("utf-8")), ("BYTEARRAY", bytearray(one)), ("LIMIT", b" " * 262145)):
        refuse("R-" + name, raw, metadata, "RAW_BYTES_OR_LIMIT")

    malformed = (
        ("CRLF", one.replace(b"\n", b"\r\n")),
        ("EXTRA-LF", one + b"\n"), ("NO-FINAL-LF", one[:-1]),
        ("COMPACT", json.dumps(json.loads(one), separators=(",", ":"), sort_keys=True).encode()),
        ("INDENT4", (json.dumps(json.loads(one), sort_keys=True, indent=4) + "\n").encode()),
        ("DUPLICATE-KEY", one.replace(b'  "encoding":', b'  "scope": "LOCAL_SYNTHETIC_PROJECTION_ONLY",\n  "encoding":')),
        ("BOM", b"\xef\xbb\xbf" + one), ("UTF8", one + b"\xff"),
        ("ROOT-ARRAY", b"[]\n"),
    )
    for name, raw in malformed:
        refuse("R-CANONICAL-" + name, raw, detached_for(raw, digest(row_a), 1, 7), "CANONICAL_DOCUMENT_REJECTED")

    original = json.loads(one)

    def changed(name, alter, expected_code, base=original, stream_sha=None, count=1, total=7):
        value = copy.deepcopy(base)
        alter(value)
        raw = native_document(value)
        supplied = detached_for(raw, digest(row_a) if stream_sha is None else stream_sha, count, total)
        refuse(name, raw, supplied, expected_code)

    changed("B-ENCODING", lambda v: v.update(encoding="OTHER"), "DOCUMENT_ENCODING")
    changed("B-SCOPE", lambda v: v.update(scope="PRODUCTION"), "DOCUMENT_SCOPE")
    for name, label in (("EMPTY", ""), ("LIMIT", "x" * 129)):
        changed("B-LABEL-" + name, lambda v, label=label: v.update(projection_label=label), "DOCUMENT_LABEL")
    changed("B-SELF-HASH-FORBIDDEN", lambda v: v.update(document_sha256="A" * 64), "CANONICAL_DOCUMENT_REJECTED")
    changed("B-EMPTY-ENTRIES", lambda v: v.update(entries=[]), "ENTRY_COUNT_RANGE")
    changed("B-COUNT-MISMATCH", lambda v: v["aggregate"].update(entry_count=2), "BODY_COUNT_MISMATCH")
    changed("B-TOTAL-MISMATCH", lambda v: v["aggregate"].update(byte_total=8), "BODY_TOTAL_MISMATCH")
    changed("B-AGGREGATE-MISMATCH", lambda v: v["aggregate"].update(sha256="0" * 64), "BODY_AGGREGATE_SHA_MISMATCH")
    changed("B-AGGREGATE-LOWER", lambda v: v["aggregate"].update(sha256="a" * 64), "BODY_SHA_FORMAT")
    for name, alter in (
        ("BOOLEAN-COUNT", lambda v: v["aggregate"].update(entry_count=True)),
        ("FLOAT-TOTAL", lambda v: v["aggregate"].update(byte_total=7.0)),
        ("BOOL-ENTRY-LENGTH", lambda v: v["entries"][0].update(byte_length=True)),
        ("NEGATIVE-LENGTH", lambda v: v["entries"][0].update(byte_length=-1)),
        ("UINT64-OVERFLOW", lambda v: v["entries"][0].update(byte_length=1 << 64)),
        ("MISSING-ENTRY-FIELD", lambda v: v["entries"][0].pop("role")),
        ("EXTRA-ENTRY-FIELD", lambda v: v["entries"][0].update(secret="prohibited")),
    ):
        changed("B-CONTRACT-" + name, alter, "CANONICAL_DOCUMENT_REJECTED")
    for name, field, value in (
        ("ORDINAL", "ordinal", 2), ("SHA-LOWER", "sha256", "a" * 64),
        ("CATEGORY", "category", "OTHER"), ("LOADER", "loader_kind", "OTHER"),
        ("RELATIVE-PATH", "relative_path", "../a.py"),
        ("PHASE-ORDER", "read_phase", "T2,T1"), ("REPARSE", "reparse_state", "LINK"),
        ("EMPTY-ID", "entry_id", ""),
    ):
        changed("B-ENTRY-" + name, lambda v, f=field, x=value: v["entries"][0].update({f: x}), "ENTRY_STREAM_REJECTED")
    two_native = json.loads(two)
    changed("B-UNSORTED-ENTRIES", lambda v: v["entries"].reverse(), "CANONICAL_DOCUMENT_REJECTED", base=two_native, stream_sha=digest(row_a + row_b), count=2, total=18)
    changed("B-DUPLICATE-ID", lambda v: v["entries"][1].update(entry_id="e01"), "ENTRY_STREAM_REJECTED", base=two_native, count=2, total=18)
    changed("B-DUPLICATE-PATH", lambda v: v["entries"][1].update(relative_path="a.py"), "ENTRY_STREAM_REJECTED", base=two_native, count=2, total=18)
    changed("B-STALE-STREAM-AFTER-ENTRY-CHANGE", lambda v: v["entries"][0].update(byte_length=8), "BODY_AGGREGATE_SHA_MISMATCH")

    def too_many(value):
        prototype = value["entries"][0]
        value["entries"] = [dict(prototype, entry_id="z" + str(i).zfill(3), relative_path="z" + str(i).zfill(3) + ".py") for i in range(129)]
        value["aggregate"]["entry_count"] = 128

    changed("B-129-ENTRIES", too_many, "ENTRY_COUNT_RANGE")
    check("Q-NO-AUTHORITY-OUTPUT-MEMBER", len(changed_result) == 5 and changed_result[0] == QUALIFIER)
    check("Q-FIXED-QUALIFIER-NO-PASS-VERDICT", "PASS" not in QUALIFIER and "NO_SOURCE_OR_AUTHORITY" in QUALIFIER)
    return {
        "Summary": {
            "CheckCount": len(checks), "VectorCount": len(vectors),
            "AllChecksPassed": True,
            "Scope": "LOCAL SYNTHETIC DETACHED CONSISTENCY ONLY; NOT SOURCE OR AUTHORITY VERIFICATION",
        },
        "Checks": checks, "Vectors": vectors,
    }
