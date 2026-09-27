"""Namespace and reference-only isolation checks with no I/O."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

LOCAL_CANDIDATE_NAMESPACE = "route_b_c03.local_candidate"
PROHIBITED_WRITE_NAMESPACES = (
    "route_a",
    "evidence",
    "matter_decision",
    "legal_reasoning",
    "human_decision",
    "external_domain",
    "acos_source_project",
)
PROHIBITED_REFERENCE_KEYS = (
    "bytes",
    "content",
    "payload",
    "prompt",
    "attachment",
    "history",
    "credential",
    "secret",
    "token",
    "cookie",
    "authorization_header",
    "private_endpoint",
)


class IsolationViolation(ValueError):
    """Raised when a namespace or reference crosses the closed boundary."""


def assert_permitted_write_set(write_set: Mapping[str, Sequence[str]]) -> None:
    for namespace in PROHIBITED_WRITE_NAMESPACES:
        if tuple(write_set.get(namespace, ())) != ():
            raise IsolationViolation(f"REJECTED — PROHIBITED WRITE: {namespace}")
    unknown = set(write_set) - set(PROHIBITED_WRITE_NAMESPACES) - {
        LOCAL_CANDIDATE_NAMESPACE
    }
    if unknown:
        raise IsolationViolation("REJECTED — UNKNOWN WRITE NAMESPACE")


def assert_reference_only(record: Mapping[str, object]) -> None:
    for key in record:
        normalized = key.lower().replace("-", "_")
        if any(term in normalized for term in PROHIBITED_REFERENCE_KEYS):
            raise IsolationViolation(f"QUARANTINED — CONTENT FIELD PROHIBITED: {key}")
