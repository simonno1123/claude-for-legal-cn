"""Four closed deterministic metadata mapping classes."""

from __future__ import annotations

import hashlib
import json
from typing import Any, Mapping

from .contracts import MappingRule, MappingTrace, TransformationType

OMITTED = object()


class MappingContractError(ValueError):
    """Raised when an exact mapping contract cannot be satisfied."""


def apply_mapping_rule(
    rule: MappingRule,
    source_values: Mapping[str, Any],
    *,
    source_state: str,
    source_artifact_reference: str,
    source_version: str,
    matter_invocation_authorization_reference: str,
) -> tuple[Any, MappingTrace]:
    """Apply one exact rule without inference, lookup, default, or I/O."""
    if not matter_invocation_authorization_reference.strip():
        raise MappingContractError("BLOCKED — MATTER INVOCATION AUTHORITY REQUIRED")
    if source_state not in rule.allowed_source_states:
        raise MappingContractError("BLOCKED — SOURCE STATE FAILURE")
    if not rule.provenance_required:
        raise MappingContractError("REJECTED — PROVENANCE REQUIRED")
    missing = rule.source_path not in source_values
    value = source_values.get(rule.source_path)
    if missing or value is None:
        if rule.transformation_type is TransformationType.EXPLICIT_OMISSION:
            value = OMITTED
        else:
            raise MappingContractError("BLOCKED — REQUIRED INPUT MISSING")
    if value is not OMITTED and not isinstance(value, (str, int, bool, type(None))):
        raise MappingContractError("QUARANTINED — NON-METADATA VALUE")

    if rule.transformation_type is TransformationType.DIRECT_COPY:
        result = value
    elif rule.transformation_type is TransformationType.ENUMERATION_MAP:
        pairs = dict(rule.enumeration_pairs)
        if value not in pairs:
            raise MappingContractError("REJECTED — MAPPING CONTRACT FAILURE")
        result = pairs[value]
    elif rule.transformation_type is TransformationType.FORMAT_NORMALIZATION:
        if not rule.normalization_version or not rule.normalization_pairs:
            raise MappingContractError("BLOCKED — NORMALIZATION CONTRACT REQUIRED")
        pairs = dict(rule.normalization_pairs)
        if value not in pairs:
            raise MappingContractError("REJECTED — NORMALIZATION CONTRACT FAILURE")
        result = pairs[value]
    elif rule.transformation_type is TransformationType.EXPLICIT_OMISSION:
        if not rule.omission_reason:
            raise MappingContractError("BLOCKED — OMISSION REASON REQUIRED")
        result = OMITTED
    else:  # pragma: no cover - Enum makes this defensive only.
        raise MappingContractError("REJECTED — MAPPING CONTRACT FAILURE")

    if result is not OMITTED and not isinstance(result, (str, int, bool, type(None))):
        raise MappingContractError("QUARANTINED — NON-METADATA RESULT")

    def trace_digest(item: Any) -> str:
        if item is OMITTED:
            return "OMITTED"
        encoded = json.dumps(item, ensure_ascii=False, sort_keys=True).encode("utf-8")
        return "sha256:" + hashlib.sha256(encoded).hexdigest().upper()

    trace = MappingTrace(
        rule_id=rule.rule_id,
        transformation_type=rule.transformation_type,
        source_path=rule.source_path,
        target_path=rule.target_path,
        source_artifact_reference=source_artifact_reference,
        source_version=source_version,
        original_representation=trace_digest(value),
        resulting_representation=trace_digest(result),
        authorization_reference=matter_invocation_authorization_reference,
    )
    return result, trace
