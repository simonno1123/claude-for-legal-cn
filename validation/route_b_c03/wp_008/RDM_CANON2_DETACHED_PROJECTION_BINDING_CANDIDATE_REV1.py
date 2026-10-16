"""Two-layer byte consistency for a closed LOCAL SYNTHETIC projection only.

This is not the formal Manifest schema or an accepted policy registry. Detached
metadata is caller data, not a signature, trusted preparation receipt, source
admission, freshness proof, capability or execution grant. A caller can replace
both bytes and metadata and still obtain DATA CONSISTENCY ONLY.

The private controller supplies the verified dependency modules in memory.
This candidate performs no filesystem, provider, network or subprocess access.
It neither emits a Manifest nor changes any accepted file or governance state.
"""

import hashlib
import re

from rdm_canon2_scalar_fixed_dependency_rev1 import (
    EncodingRejected,
    encode_ordered_entry_projection,
    parse_synthetic_json,
)
from rdm_canon2_tree_fixed_dependency_rev1 import (
    TreeEncodingRejected,
    require_canonical_synthetic_document,
)


ENCODING = "WP008-RDM-CANON-2"
SCOPE = "LOCAL_SYNTHETIC_PROJECTION_ONLY"
QUALIFIER = "DATA_CONSISTENCY_ONLY_NO_SOURCE_OR_AUTHORITY"
MAX_ENTRIES = 128
MAX_ENTRY_BYTES = (1 << 64) - 1
MAX_DOCUMENT_BYTES = 262144

# Deliberately closed toy contract. These finite ranges are synthetic test
# choices, not an authorization to define/admit production Manifest fields.
_TEXT = ("string",)
_ENTRY = ("object", (
    ("ordinal", ("integer", 1, MAX_ENTRIES)),
    ("entry_id", _TEXT), ("category", _TEXT), ("root_id", _TEXT),
    ("relative_path", _TEXT),
    ("byte_length", ("integer", 0, MAX_ENTRY_BYTES)),
    ("sha256", _TEXT), ("role", _TEXT), ("required_by", _TEXT),
    ("import_name", _TEXT), ("loader_kind", _TEXT), ("read_phase", _TEXT),
    ("executable", ("boolean",)), ("network_capable", ("boolean",)),
    ("reparse_state", _TEXT),
))
_DOCUMENT = ("object", (
    ("aggregate", ("object", (
        ("byte_total", ("integer", 0, MAX_ENTRIES * MAX_ENTRY_BYTES)),
        ("entry_count", ("integer", 1, MAX_ENTRIES)), ("sha256", _TEXT),
    ))),
    ("encoding", _TEXT),
    ("entries", ("array", _ENTRY, (
        "SET_SORTED", ("category", "root_id", "relative_path", "entry_id"),
    ))),
    ("projection_label", _TEXT), ("scope", _TEXT),
))
_DETACHED_FIELDS = frozenset((
    "encoding", "scope", "document_sha256", "aggregate_sha256",
    "entry_count", "byte_total",
))


class ProjectionBindingRejected(ValueError):
    """Synthetic consistency rejection, not a finding or admission decision."""


def _require(condition, code):
    if not condition:
        raise ProjectionBindingRejected(code)


def _sha(value):
    return type(value) is str and re.fullmatch(r"[0-9A-F]{64}", value) is not None


def _detached_snapshot(value):
    _require(type(value) is dict, "DETACHED_TYPE")
    # A local shallow snapshot with primitive validation is not an atomic
    # freeze of hostile concurrent caller state and does not establish trust.
    data = value.copy()
    _require(all(type(key) is str for key in data), "DETACHED_KEY_TYPE")
    _require(set(data) == _DETACHED_FIELDS, "DETACHED_FIELDS")
    _require(type(data["encoding"]) is str and data["encoding"] == ENCODING, "DETACHED_ENCODING")
    _require(type(data["scope"]) is str and data["scope"] == SCOPE, "DETACHED_SCOPE")
    _require(_sha(data["document_sha256"]) and _sha(data["aggregate_sha256"]), "DETACHED_SHA_FORMAT")
    _require(type(data["entry_count"]) is int and 1 <= data["entry_count"] <= MAX_ENTRIES, "DETACHED_COUNT_RANGE")
    _require(type(data["byte_total"]) is int and 0 <= data["byte_total"] <= MAX_ENTRIES * MAX_ENTRY_BYTES, "DETACHED_TOTAL_RANGE")
    return data


def verify_synthetic_projection(raw, detached):
    """Return a native tuple of computed values, never an authority receipt.

    Tuple: (fixed qualifier, full-document SHA, entry-stream SHA, count, total).
    Original canonical bytes, including final LF, are hashed without repair.
    Internal aggregate metadata is excluded from the fifteen-field stream but
    included in the full-document hash. No self-hash member is permitted.
    """
    data = _detached_snapshot(detached)
    _require(type(raw) is bytes and len(raw) <= MAX_DOCUMENT_BYTES, "RAW_BYTES_OR_LIMIT")
    document_sha = hashlib.sha256(raw).hexdigest().upper()
    _require(document_sha == data["document_sha256"], "DOCUMENT_SHA_MISMATCH")
    try:
        require_canonical_synthetic_document(raw, _DOCUMENT)
        document = parse_synthetic_json(raw)
    except (TreeEncodingRejected, EncodingRejected, RecursionError) as error:
        raise ProjectionBindingRejected("CANONICAL_DOCUMENT_REJECTED") from error
    _require(document["encoding"] == ENCODING, "DOCUMENT_ENCODING")
    _require(document["scope"] == SCOPE, "DOCUMENT_SCOPE")
    _require(1 <= len(document["projection_label"]) <= 128, "DOCUMENT_LABEL")
    entries = tuple(document["entries"])
    _require(1 <= len(entries) <= MAX_ENTRIES, "ENTRY_COUNT_RANGE")
    try:
        stream = encode_ordered_entry_projection(entries)
    except EncodingRejected as error:
        raise ProjectionBindingRejected("ENTRY_STREAM_REJECTED") from error
    stream_sha = hashlib.sha256(stream).hexdigest().upper()
    count = len(entries)
    total = sum(entry["byte_length"] for entry in entries)
    aggregate = document["aggregate"]
    _require(_sha(aggregate["sha256"]), "BODY_SHA_FORMAT")
    _require(aggregate["sha256"] == stream_sha, "BODY_AGGREGATE_SHA_MISMATCH")
    _require(aggregate["entry_count"] == count, "BODY_COUNT_MISMATCH")
    _require(aggregate["byte_total"] == total, "BODY_TOTAL_MISMATCH")
    _require(data["aggregate_sha256"] == stream_sha, "DETACHED_AGGREGATE_SHA_MISMATCH")
    _require(data["entry_count"] == count, "DETACHED_COUNT_MISMATCH")
    _require(data["byte_total"] == total, "DETACHED_TOTAL_MISMATCH")
    return (QUALIFIER, document_sha, stream_sha, count, total)
