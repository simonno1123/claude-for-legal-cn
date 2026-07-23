# TASK_PHASE2_C02_II_REQUEST_RIGHT_FRAMEWORK_DESIGN_DECISION

## Decision Record

| Field | Value |
|---|---|
| Decision ID | TASK_PHASE2_C02_II_REQUEST_RIGHT_FRAMEWORK_DESIGN_DECISION |
| Decision type | C02-II Design Closeout Decision |
| Decision date | 2026-07-20 |
| Decision authority | Project Owner |
| Decision | **ACCEPTED** |
| Approved Handoff SHA-256 | `42428EBC5C61A4B5C68B4940273EEEF8BDFE6CEDD0736958FFD1F5E93C64EDD0` |
| Design Spec SHA-256 | `BB4C2A1B8977A99EB46E4854BDDCF7F4B6759523F6E926654BED365F71C55FE1` |
| Design Result SHA-256 | `3BCE75F664CECB079AACBBAB622F71915DEAF15DC81B335CB8E1BBE51FC2B047` |
| Closeout Review SHA-256 | `CB6A676CF09201DF2D831E51686F00228CCE72D6A657C36E8F9C43AA02F0DD7C` |

## 1. Decision

The Project Owner accepts the C02-II Request Right Framework Design artifacts identified above.

This Decision:

1. adopts `TASK_PHASE2_C02_II_REQUEST_RIGHT_FRAMEWORK_DESIGN_SPEC.md` as the reviewed C02-II Design baseline;
2. adopts `TASK_PHASE2_C02_II_REQUEST_RIGHT_FRAMEWORK_DESIGN_RESULT.md` as the execution and boundary record;
3. closes the C02-II Request Right Framework Design stage;
4. preserves the C02-I conclusion `BLOCKED — PARTIAL VALIDATION ONLY` without reclassifying it;
5. does not authorize implementation, runtime modification or real-case analysis.

## 2. Adopted Design Boundary

The adopted design includes documentation-level models for:

- Request Right Candidate and Legal Basis Candidate;
- constituent elements and required facts;
- Raw Fact → Legal Fact Candidate → Element Fact Candidate → Claim-Relevant Fact Candidate transformation;
- burden candidates and evidence requirements;
- evidence references, conflicts and gaps;
- defense and rebuttal integration;
- request-right relationships;
- CASE-A/B/C validation interfaces;
- the qualified-lawyer Human Review Gate.

The controlled validation statuses remain:

```text
UNKNOWN
SUPPORTED
BLOCKED
```

These are descriptive candidate states and are not merits or outcome states.

## 3. Explicit Non-Authorization

This Decision does not authorize:

- C02-II Implementation;
- C02-III Validation Enhancement;
- modification of any Skill or Agent;
- modification of code, workflow, MCP, plugin, runtime schema or `CLAUDE.md`;
- creation of a database, knowledge graph or global legal-reasoning core;
- real-case merits analysis;
- automatic legal opinions, strategy selection, adjudication or success-rate calculation;
- Git staging, commit, tag, push or release.

Any next phase requires a new, separately reviewed Project Owner Handoff with exact artifact and output bindings.

## 4. Closeout Status

```text
C02-II Design Handoff:
CLOSED

C02-II Design Execution:
CLOSED

C02-II Design Spec:
ADOPTED

C02-II Design Result:
ADOPTED

C02-II Design Closeout:
ACCEPTED

C02-II Implementation:
NOT AUTHORIZED

C02-III Validation Enhancement:
NOT AUTHORIZED
```

## 5. Recommended Direction

The recommended next planning direction is a separately governed C02-III Validation Enhancement proposal addressing material binding, OCR/text availability and element–evidence revalidation before any implementation decision.

This recommendation is advisory only and creates no task or execution authority.
