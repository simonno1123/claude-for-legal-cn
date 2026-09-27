"""Blocked provider protocol; no provider, transport, credential, or payload."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True, slots=True)
class ProviderPortResult:
    allowed: bool
    status: str
    reason_code: str
    request_reference: str


class ProviderPort(Protocol):
    status: str

    def submit_reference(self, request_reference: str) -> ProviderPortResult: ...


class NullProviderPort:
    status = "NOT_SELECTED"
    network_transport = "ABSENT"
    credentials = "PROHIBITED"

    def submit_reference(self, request_reference: str) -> ProviderPortResult:
        return ProviderPortResult(
            allowed=False,
            status=self.status,
            reason_code="BLOCKED — PROVIDER NOT AUTHORIZED",
            request_reference=request_reference,
        )
