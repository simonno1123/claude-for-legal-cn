"""CANON-2 structural-layout candidate for explicit synthetic contracts only.

The fixed local controller must supply the verified scalar module under the
synthetic dependency name below. That name is not a trust/admission interface.
No actual Manifest schema, root, source admission, accepted order registry,
filesystem/provider access, business integration or governance verdict exists
here. A caller-supplied synthetic contract does not become accepted policy.
"""

from rdm_canon2_scalar_fixed_dependency_rev1 import (
    EncodingRejected as ScalarRejected,
    encode_boolean,
    encode_integer,
    encode_null,
    encode_string,
    parse_synthetic_json,
)


MAX_DEPTH = 32
MAX_NODES = 4096
MAX_STRING_CHARACTERS = 32768
MAX_OUTPUT_BYTES = 262144


class TreeEncodingRejected(ValueError):
    """Local synthetic structural rejection, not a formal finding."""


def _require(condition, code):
    if not condition:
        raise TreeEncodingRejected(code)


class _Budget:
    def __init__(self):
        self.nodes = 0
        self.scalar_bytes = 0

    def touch(self, depth):
        _require(depth <= MAX_DEPTH, "DEPTH_LIMIT")
        self.nodes += 1
        _require(self.nodes <= MAX_NODES, "NODE_LIMIT")

    def token(self, value):
        self.scalar_bytes += len(value)
        _require(self.scalar_bytes <= MAX_OUTPUT_BYTES, "PROJECTION_BYTE_LIMIT")
        return value


def _string(value):
    _require(type(value) is str, "STRING_TYPE")
    _require(len(value) <= MAX_STRING_CHARACTERS, "STRING_LIMIT")
    try:
        return encode_string(value)
    except ScalarRejected as error:
        raise TreeEncodingRejected("SCALAR_STRING_REJECTED") from error


def _key_specs(element_spec, selector):
    _require(type(selector) is tuple, "SELECTOR_TYPE")
    if element_spec[0] in ("string", "integer"):
        _require(not selector, "SCALAR_SELECTOR_NOT_EMPTY")
        return (element_spec,)
    _require(element_spec[0] == "object" and selector, "SELECTOR_ELEMENT_KIND")
    fields = dict(element_spec[1])
    seen = set()
    result = []
    for field in selector:
        _require(type(field) is str and field in fields and field not in seen, "SELECTOR_MEMBER")
        seen.add(field)
        selected = fields[field]
        _require(selected[0] in ("string", "integer"), "SELECTOR_KEY_TYPE")
        result.append(selected)
    return tuple(result)


def _key_value(value, spec):
    if spec[0] == "string":
        _string(value)
    else:
        try:
            encode_integer(value, spec[1], spec[2])
        except ScalarRejected as error:
            raise TreeEncodingRejected("KEY_INTEGER") from error


def _validate_spec(spec, budget, active, depth=0):
    budget.touch(depth)
    _require(type(spec) is tuple and spec and type(spec[0]) is str, "CONTRACT_REQUIRED")
    _require(id(spec) not in active, "CONTRACT_CYCLE")
    active.add(id(spec))
    try:
        kind = spec[0]
        if kind in ("string", "boolean", "null"):
            _require(len(spec) == 1, "SCALAR_CONTRACT_ARITY")
        elif kind == "integer":
            _require(len(spec) == 3, "INTEGER_CONTRACT_ARITY")
            _require(type(spec[1]) is int and type(spec[2]) is int and spec[1] <= spec[2], "INTEGER_CONTRACT_RANGE")
        elif kind == "nullable":
            _require(len(spec) == 2, "NULLABLE_CONTRACT_ARITY")
            _validate_spec(spec[1], budget, active, depth + 1)
            _require(spec[1][0] not in ("null", "nullable"), "NULLABLE_AMBIGUOUS")
        elif kind == "object":
            _require(len(spec) == 2 and type(spec[1]) is tuple, "OBJECT_CONTRACT_FIELDS")
            seen = set()
            for field in spec[1]:
                _require(type(field) is tuple and len(field) == 2, "OBJECT_CONTRACT_FIELD")
                _string(field[0])
                _require(field[0] not in seen, "DUPLICATE_CONTRACT_MEMBER")
                seen.add(field[0])
                _validate_spec(field[1], budget, active, depth + 1)
        elif kind == "array":
            _require(len(spec) == 3, "ARRAY_POLICY_REQUIRED")
            _validate_spec(spec[1], budget, active, depth + 1)
            policy = spec[2]
            _require(type(policy) is tuple and policy and type(policy[0]) is str, "ARRAY_POLICY_REQUIRED")
            mode = policy[0]
            _require(mode in ("ORDERED", "SET_SORTED"), "ARRAY_POLICY_KIND")
            _require(len(policy) == (4 if mode == "ORDERED" else 2), "ARRAY_POLICY_ARITY")
            key_specs = _key_specs(spec[1], policy[1])
            if mode == "ORDERED":
                keys, repeats = policy[2:]
                _require(type(keys) is tuple and type(repeats) is bool, "ORDERED_POLICY")
                _require(len(keys) <= MAX_NODES, "ORDERED_SEQUENCE_LIMIT")
                seen = set()
                for key in keys:
                    _require(type(key) is tuple and len(key) == len(key_specs), "ORDERED_KEY_SHAPE")
                    for value, key_spec in zip(key, key_specs):
                        _key_value(value, key_spec)
                    _require(repeats or key not in seen, "ORDERED_REPEAT_UNBOUND")
                    seen.add(key)
        else:
            raise TreeEncodingRejected("CONTRACT_KIND")
    finally:
        active.remove(id(spec))


def _normalize(value, spec, budget, active, depth=0):
    budget.touch(depth)
    kind = spec[0]
    if kind == "nullable":
        return budget.token(b"null") if value is None else _normalize(value, spec[1], budget, active, depth + 1)
    if kind == "string":
        return budget.token(_string(value))
    if kind in ("integer", "boolean", "null"):
        try:
            if kind == "integer":
                token = encode_integer(value, spec[1], spec[2])
            elif kind == "boolean":
                token = encode_boolean(value)
            else:
                _require(value is None, "NULL_VALUE")
                token = encode_null(True)
        except ScalarRejected as error:
            raise TreeEncodingRejected("SCALAR_VALUE_REJECTED") from error
        return budget.token(token)

    _require(type(value) is (dict if kind == "object" else list), "CONTAINER_TYPE")
    _require(id(value) not in active, "VALUE_CYCLE")
    active.add(id(value))
    try:
        if kind == "object":
            fields = dict(spec[1])
            for key in value:
                _string(key)
            _require(set(value) == set(fields), "OBJECT_MEMBERS")
            result = []
            for key in sorted(fields):
                key_token = budget.token(_string(key))
                result.append((key_token, _normalize(value[key], fields[key], budget, active, depth + 1)))
            return ("object", tuple(result))

        element_spec, policy = spec[1:]
        selector = policy[1]
        pairs = []
        for element in value:
            node = _normalize(element, element_spec, budget, active, depth + 1)
            # Exact primitive types/ranges were validated by the element contract.
            key = tuple(element[field] for field in selector) if selector else (element,)
            pairs.append((key, node))
        keys = tuple(key for key, _node in pairs)
        if policy[0] == "ORDERED":
            _require(keys == policy[2], "ORDERED_SEQUENCE_MISMATCH")
        else:
            _require(len(set(keys)) == len(keys), "SET_SORTED_TIE")
            pairs.sort(key=lambda pair: pair[0])
        return ("array", tuple(node for _key, node in pairs))
    finally:
        active.remove(id(value))


def _render(node, pretty):
    parts = []
    size = 0

    def append(piece):
        nonlocal size
        size += len(piece)
        _require(size <= MAX_OUTPUT_BYTES, "OUTPUT_BYTE_LIMIT")
        parts.append(piece)

    def emit(current, depth):
        if type(current) is bytes:
            append(current)
            return
        kind, items = current
        opening, closing = (b"{", b"}") if kind == "object" else (b"[", b"]")
        append(opening)
        if items and pretty:
            append(b"\n")
        for index, item in enumerate(items):
            if pretty:
                append(b"  " * (depth + 1))
            if kind == "object":
                key, child = item
                append(key)
                append(b": " if pretty else b":")
            else:
                child = item
            emit(child, depth + 1)
            if index + 1 != len(items):
                append(b",")
            if pretty:
                append(b"\n")
        if items and pretty:
            append(b"  " * depth)
        append(closing)

    emit(node, 0)
    if pretty:
        append(b"\n")
    return b"".join(parts)


def _prepare(value, contract):
    _validate_spec(contract, _Budget(), set())
    return _normalize(value, contract, _Budget(), set())


def encode_synthetic_document(value, contract):
    """Encode one synthetic root object, exactly one final LF; no receipt."""
    tree = _prepare(value, contract)
    _require(contract[0] == "object", "DOCUMENT_ROOT_OBJECT_REQUIRED")
    return _render(tree, True)


def encode_compact_synthetic_value(value, contract):
    """Compact synthetic value; no insignificant whitespace or final LF."""
    return _render(_prepare(value, contract), False)


def require_canonical_synthetic_document(raw, contract):
    """Reject rather than normalize an already supplied noncanonical document.

    The returned bytes are the original bytes object, not admitted source or
    typed native observation. This does not verify any detached authority/SHA.
    """
    _require(type(raw) is bytes and len(raw) <= MAX_OUTPUT_BYTES, "RAW_BYTES_OR_LIMIT")
    try:
        value = parse_synthetic_json(raw)
    except (ScalarRejected, RecursionError) as error:
        raise TreeEncodingRejected("RAW_JSON_REJECTED") from error
    expected = encode_synthetic_document(value, contract)
    _require(raw == expected, "NONCANONICAL_DOCUMENT_BYTES")
    return raw
