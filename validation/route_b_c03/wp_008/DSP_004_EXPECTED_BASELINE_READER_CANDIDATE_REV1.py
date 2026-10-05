"""DSP-004 pure expected-baseline extraction candidate, REV1.

Scope: candidate source materialization only, under the conversation-level
authorization in writing block 78216. This module has not been run, imported,
compiled, tested, accepted, admitted, or integrated by its materialization.

The sole entry point accepts complete bytes supplied by a caller. It does not
open files, discover paths, capture actual values, call a Gate or provider,
compare context boundaries, or grant source/use authority. Its records are
extracted document records, not native BoundaryCheck or GateDecision objects.
The pinned SHA is a byte-identity constraint, not a trust or admission decision.
"""

from dataclasses import dataclass
from hashlib import sha256


BASELINE_SHA256 = (
    "BE8C55796587BBA65E22B048291E1688A8B076D02DA2A48DE412919BEB10F368"
)

_DOCUMENT_TITLE = "# DSP-004 合成预期基线候选 — REV1"
_SECTION_START = "## 3. 三项预期来源候选"
_SECTION_END = "## 4. 职责、冻结与使用范围"
_RECORD_VERSION = "REV1 — DOCUMENT CANDIDATE VERSION ONLY"
_RECORDED_QUALIFICATION = (
    "CANDIDATE RECORD ONLY — NOT REVIEWED / NOT ACCEPTED / NOT ADMITTED"
)
_FIELD_ORDER = (
    "Source Role",
    "Candidate Source Identity",
    "Candidate Record Version",
    "Expected Reference",
    "Producer Responsibility",
    "Materialization Authority",
    "Record Locator",
    "Proposed Logical Location",
    "Candidate Applicability",
    "Carrier SHA Binding",
    "Source Qualification",
)
_SECTION_LAYOUT = (
    (
        "### 3.1 Project 预期来源候选",
        "SRC004-E-PROJECT",
        "DSP004-EXPECTED-PROJECT-V1",
        "本文件第 3.1 节，Field = Expected Reference 的唯一表格行",
    ),
    (
        "### 3.2 Session 预期来源候选",
        "SRC004-E-SESSION",
        "DSP004-EXPECTED-SESSION-V1",
        "本文件第 3.2 节，Field = Expected Reference 的唯一表格行",
    ),
    (
        "### 3.3 Provider 预期来源候选",
        "SRC004-E-PROVIDER",
        "DSP004-EXPECTED-PROVIDER-V1",
        "本文件第 3.3 节，Field = Expected Reference 的唯一表格行",
    ),
)


class ExpectedBaselineExtractionError(ValueError):
    """Stop extraction without fallback, partial return, or a review verdict."""

    def __init__(self, code: str, detail: str) -> None:
        self.code = code
        super().__init__(f"{code}: {detail}")


@dataclass(frozen=True, slots=True)
class ExpectedBaselineRecord:
    """Literal record fields only; no trust, admission, or matching status."""

    source_role: str
    candidate_source_identity: str
    record_locator: str
    expected_reference: str


def _unique_line_index(lines: list[str], marker: str) -> int:
    positions = [index for index, line in enumerate(lines) if line == marker]
    if not positions:
        raise ExpectedBaselineExtractionError("MISSING_RECORD", marker)
    if len(positions) != 1:
        raise ExpectedBaselineExtractionError("DUPLICATE_RECORD", marker)
    return positions[0]


def _read_table_fields(section: list[str], heading: str) -> dict[str, str]:
    table_positions = []
    for index, line in enumerate(section):
        if line.lstrip().startswith("|"):
            if not line.startswith("|"):
                raise ExpectedBaselineExtractionError(
                    "FORMAT_FAILURE", f"Indented table row in {heading}"
                )
            table_positions.append(index)
    if not table_positions:
        raise ExpectedBaselineExtractionError("MISSING_RECORD", heading)
    if table_positions[-1] - table_positions[0] + 1 != len(table_positions):
        raise ExpectedBaselineExtractionError(
            "FORMAT_FAILURE", f"Non-contiguous or multiple tables in {heading}"
        )
    table = [section[index] for index in table_positions]
    if len(table) < 2 or table[:2] != [
        "| Field | Candidate Record |",
        "| --- | --- |",
    ]:
        raise ExpectedBaselineExtractionError(
            "FORMAT_FAILURE", f"Unexpected table header in {heading}"
        )

    fields: dict[str, str] = {}
    for line in table[2:]:
        if not line.startswith("| ") or not line.endswith(" |"):
            raise ExpectedBaselineExtractionError(
                "FORMAT_FAILURE", f"Unexpected row framing in {heading}"
            )
        # Remove only the exact REV1 Markdown framing, never value whitespace.
        cells = line[2:-2].split(" | ")
        if len(cells) != 2 or any("|" in cell for cell in cells):
            raise ExpectedBaselineExtractionError(
                "FORMAT_FAILURE", f"Expected two literal cells in {heading}"
            )
        field, value = cells
        if field not in _FIELD_ORDER:
            raise ExpectedBaselineExtractionError(
                "FORMAT_FAILURE", f"Unexpected field in {heading}"
            )
        if field in fields:
            code = (
                "DUPLICATE_RECORD" if fields[field] == value else "RECORD_CONFLICT"
            )
            raise ExpectedBaselineExtractionError(code, f"{heading}: {field}")
        if not value or value.isspace():
            raise ExpectedBaselineExtractionError(
                "FORMAT_FAILURE", f"Empty field in {heading}: {field}"
            )
        fields[field] = value

    missing = [field for field in _FIELD_ORDER if field not in fields]
    if missing:
        raise ExpectedBaselineExtractionError(
            "MISSING_RECORD", f"{heading}: {', '.join(missing)}"
        )
    if tuple(fields) != _FIELD_ORDER:
        raise ExpectedBaselineExtractionError(
            "FORMAT_FAILURE", f"Unexpected field order in {heading}"
        )
    return fields


def extract_expected_baseline(
    payload: bytes,
) -> tuple[ExpectedBaselineRecord, ExpectedBaselineRecord, ExpectedBaselineRecord]:
    """Extract Project, Session, Provider records from the same pinned bytes.

    The caller remains responsible for separately authorized access and use.
    No reference value is hard-coded, inferred, normalized, or backfilled.
    Any failure raises before returning records; no other source is searched.
    """
    if type(payload) is not bytes:
        raise ExpectedBaselineExtractionError(
            "INVALID_INPUT_TYPE", "Complete native bytes are required"
        )
    if sha256(payload).hexdigest().upper() != BASELINE_SHA256:
        raise ExpectedBaselineExtractionError(
            "CARRIER_SHA_MISMATCH", "Complete bytes differ from the pinned baseline"
        )
    try:
        text = payload.decode("utf-8", errors="strict")
    except UnicodeDecodeError as error:
        raise ExpectedBaselineExtractionError(
            "DECODE_FAILURE", "Strict UTF-8 decoding failed"
        ) from error
    if "\r" in text or not text.endswith("\n"):
        raise ExpectedBaselineExtractionError(
            "FORMAT_FAILURE", "REV1 requires LF lines and a final LF"
        )
    lines = text.split("\n")
    if not lines or lines[0] != _DOCUMENT_TITLE:
        raise ExpectedBaselineExtractionError(
            "FORMAT_FAILURE", "Unexpected REV1 document title"
        )

    start = _unique_line_index(lines, _SECTION_START)
    end = _unique_line_index(lines, _SECTION_END)
    positions = [_unique_line_index(lines, layout[0]) for layout in _SECTION_LAYOUT]
    if not start < positions[0] < positions[1] < positions[2] < end:
        raise ExpectedBaselineExtractionError(
            "FORMAT_FAILURE", "Candidate section order or containment differs"
        )
    expected_headings = [layout[0] for layout in _SECTION_LAYOUT]
    present_headings = [line for line in lines[start + 1:end] if line.startswith("#")]
    if present_headings != expected_headings:
        raise ExpectedBaselineExtractionError(
            "FORMAT_FAILURE", "Unexpected headings in the candidate section"
        )

    records: list[ExpectedBaselineRecord] = []
    for index, (heading, role, identity, locator) in enumerate(_SECTION_LAYOUT):
        section_end = positions[index + 1] if index < 2 else end
        fields = _read_table_fields(lines[positions[index] + 1:section_end], heading)
        required_metadata = (
            ("Source Role", role),
            ("Candidate Source Identity", identity),
            ("Candidate Record Version", _RECORD_VERSION),
            ("Record Locator", locator),
            ("Source Qualification", _RECORDED_QUALIFICATION),
        )
        for field, required_value in required_metadata:
            if fields[field] != required_value:
                raise ExpectedBaselineExtractionError(
                    "RECORD_CONFLICT", f"{heading}: unexpected {field}"
                )
        records.append(
            ExpectedBaselineRecord(
                source_role=fields["Source Role"],
                candidate_source_identity=fields["Candidate Source Identity"],
                record_locator=fields["Record Locator"],
                expected_reference=fields["Expected Reference"],
            )
        )
    return records[0], records[1], records[2]
