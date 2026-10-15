"""WP008-RDM-CANON-2 scalar/ordered-entry projection candidate only.

Pure byte operations on explicitly supplied local synthetic values. No file,
network, provider, import-discovery, source admission, or Manifest generation.
This is NOT the complete typed contract, array-order registry, entry semantic
validator, trusted-root resolver, or canonical whole-Manifest implementation.
An entry's claimed SHA/root/role is syntax/data here, not verified provenance.
No result from this module grants use or closes DSP-004, B-01, or B-02.
"""

import json
import re


ENCODING_ID = "WP008-RDM-CANON-2"
FIELD_ORDER = (
    "ordinal", "entry_id", "category", "root_id", "relative_path",
    "byte_length", "sha256", "role", "required_by", "import_name",
    "loader_kind", "read_phase", "executable", "network_capable", "reparse_state",
)
_INTEGER_FIELDS = frozenset(("ordinal", "byte_length"))
_BOOLEAN_FIELDS = frozenset(("executable", "network_capable"))
_CATEGORIES = frozenset((
    "PYTHON_EXECUTABLE", "PYTHON_CONFIG", "CPYTHON_CORE_DLL", "STDLIB_SOURCE",
    "STDLIB_EXTENSION", "STDLIB_DATA", "OS_RUNTIME_DLL", "HARNESS_SOURCE",
    "SUBJECT_SOURCE", "GOVERNANCE_INPUT", "FIXTURE_INPUT", "SCENARIO_INPUT_BINDING",
))
_LOADERS = frozenset(("SOURCE", "EXTENSION", "DLL", "DATA", "CONFIG", "EXECUTABLE", "GOVERNANCE"))
_HEX = re.compile(r"[0-9A-F]{64}\Z")
_INTEGER = re.compile(r"(?:0|-[1-9][0-9]*|[1-9][0-9]*)\Z")


class EncodingRejected(ValueError):
    """A local encoding/projection rejection, not a governance finding."""


def _reject(condition: bool, code: str) -> None:
    if condition:
        raise EncodingRejected(code)


def encode_string(value: str) -> bytes:
    _reject(type(value) is not str, "STRING_TYPE")
    parts = ['"']
    for char in value:
        point = ord(char)
        _reject(0xD800 <= point <= 0xDFFF, "UNICODE_SURROGATE")
        if point == 0x22:
            parts.append('\\"')
        elif point == 0x5C:
            parts.append("\\\\")
        elif point <= 0x1F:
            parts.append("\\u00" + format(point, "02x"))
        else:
            parts.append(char)
    parts.append('"')
    return "".join(parts).encode("utf-8", "strict")


def encode_integer(value: int, minimum: int, maximum: int) -> bytes:
    _reject(type(value) is not int, "INTEGER_TYPE")
    _reject(type(minimum) is not int or type(maximum) is not int or minimum > maximum, "INTEGER_RANGE_CONTRACT")
    _reject(not minimum <= value <= maximum, "INTEGER_RANGE")
    return str(value).encode("ascii")


def encode_boolean(value: bool) -> bytes:
    _reject(type(value) is not bool, "BOOLEAN_TYPE")
    return b"true" if value else b"false"


def encode_null(nullable: bool) -> bytes:
    _reject(type(nullable) is not bool or not nullable, "NULL_NOT_PERMITTED")
    return b"null"


def _integer_from_token(token: str) -> int:
    # Check lexical form before int() erases forbidden spelling such as -0.
    _reject(_INTEGER.fullmatch(token) is None, "INTEGER_TOKEN")
    return int(token)


def _unsupported_number(_token: str):
    raise EncodingRejected("NON_INTEGER_NUMBER")


def _unique_object(pairs: list) -> dict:
    result = {}
    for key, value in pairs:
        _reject(key in result, "DUPLICATE_DECODED_KEY")
        result[key] = value
    return result


def parse_synthetic_json(raw: bytes):
    """Decode synthetic JSON without collapsing duplicates/number spellings.

    Parsing is not canonical-byte acceptance. Callers must still apply the
    exact typed contract; this candidate does not admit any parsed source.
    """
    _reject(type(raw) is not bytes, "INPUT_BYTES_TYPE")
    try:
        text = raw.decode("utf-8", "strict")
        return json.loads(
            text, parse_int=_integer_from_token, parse_float=_unsupported_number,
            parse_constant=_unsupported_number, object_pairs_hook=_unique_object,
        )
    except (UnicodeError, json.JSONDecodeError) as error:
        raise EncodingRejected("INVALID_JSON_OR_UTF8") from error


def require_canonical_scalar(raw: bytes, kind: str, *, minimum=None, maximum=None, nullable=False):
    """Return a native scalar only if its ORIGINAL bytes match the encoding.

    No normalization-and-receipt-reuse path is supplied. Ranges are explicitly
    caller-supplied synthetic contract parameters, not accepted manifest policy.
    """
    value = parse_synthetic_json(raw)
    _reject(type(kind) is not str, "SCALAR_KIND")
    if kind == "string":
        canonical = encode_string(value)
    elif kind == "integer":
        canonical = encode_integer(value, minimum, maximum)
    elif kind == "boolean":
        canonical = encode_boolean(value)
    elif kind == "null":
        _reject(value is not None, "NULL_TYPE")
        canonical = encode_null(nullable)
    else:
        raise EncodingRejected("SCALAR_KIND")
    _reject(canonical != raw, "NONCANONICAL_SCALAR_BYTES")
    return value


def _check_entry(entry: dict) -> tuple:
    _reject(type(entry) is not dict or set(entry) != set(FIELD_ORDER), "ENTRY_FIELDS_OR_TYPE")
    for field in FIELD_ORDER:
        value = entry[field]
        if field in _INTEGER_FIELDS:
            _reject(type(value) is not int or value < (1 if field == "ordinal" else 0), "ENTRY_INTEGER")
        elif field in _BOOLEAN_FIELDS:
            _reject(type(value) is not bool, "ENTRY_BOOLEAN")
        else:
            _reject(type(value) is not str or not value or value.isspace(), "ENTRY_STRING")
            encode_string(value)
            _reject(value == "UNKNOWN" or any(char in value for char in "*?[]"), "ENTRY_UNRESOLVED_VALUE")
    _reject(entry["category"] not in _CATEGORIES, "ENTRY_CATEGORY")
    _reject(entry["loader_kind"] not in _LOADERS, "ENTRY_LOADER")
    _reject(_HEX.fullmatch(entry["sha256"]) is None, "ENTRY_SHA_SYNTAX")
    path = entry["relative_path"]
    _reject("\\" in path or ":" in path or path.startswith("/") or any(ord(c) < 32 for c in path), "ENTRY_PATH")
    _reject(any(part in ("", ".", "..") for part in path.split("/")), "ENTRY_PATH")
    phases = entry["read_phase"].split(",")
    _reject(phases != [p for p in ("T1", "T2", "T3", "T4") if p in phases], "ENTRY_PHASE_ORDER")
    _reject(not phases or any(p not in ("T1", "T2", "T3", "T4") for p in phases), "ENTRY_PHASE")
    # Only the direct-path synthetic subset is implemented, not link resolution.
    _reject(entry["reparse_state"] != "DIRECT", "REPARSE_MAPPING_UNSUPPORTED")
    return tuple(entry[field] for field in ("category", "root_id", "relative_path", "entry_id"))


def encode_ordered_entry_projection(entries: tuple) -> bytes:
    """Encode the fifteen-field stream for an already ordered synthetic set.

    Do not sort, reassign ordinals, resolve files/roots, infer aliases or claim
    closure. Reject nonascending order and duplicate ID/root/path identities.
    Exact-case checks do not establish filesystem case/reparse alias freedom.
    Role/required_by/import/root acceptance and executable/network authority
    remain OUTSIDE this projection; syntax success does not verify them.
    There is no default numeric ceiling for a formal Manifest in this module.
    """
    _reject(type(entries) is not tuple or not entries, "ENTRY_SET_TYPE_OR_EMPTY")
    chunks = []
    seen_ids = set()
    seen_paths = set()
    previous = None
    for ordinal, entry in enumerate(entries, 1):
        key = _check_entry(entry)
        _reject(entry["ordinal"] != ordinal, "ENTRY_ORDINAL")
        _reject(previous is not None and key <= previous, "ENTRY_ORDER")
        _reject(entry["entry_id"] in seen_ids, "DUPLICATE_ENTRY_ID")
        path_key = (entry["root_id"], entry["relative_path"])
        _reject(path_key in seen_paths, "DUPLICATE_ROOT_PATH")
        seen_ids.add(entry["entry_id"])
        seen_paths.add(path_key)
        previous = key
        tokens = []
        for field in FIELD_ORDER:
            value = entry[field]
            if field in _INTEGER_FIELDS:
                tokens.append(str(value).encode("ascii"))
            elif field in _BOOLEAN_FIELDS:
                tokens.append(encode_boolean(value))
            else:
                tokens.append(encode_string(value))
        chunks.append(b"\x1f".join(tokens) + b"\n")
    return b"".join(chunks)
