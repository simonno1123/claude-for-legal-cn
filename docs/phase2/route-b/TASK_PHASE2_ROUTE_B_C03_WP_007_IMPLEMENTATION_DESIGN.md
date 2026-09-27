# TASK_PHASE2_ROUTE_B_C03_WP_007_IMPLEMENTATION_DESIGN

## 0. Design Control

| Field | Recorded value |
| --- | --- |
| Design authority | Project Owner conversation-level authorization |
| Design date | 2026-08-30 |
| Evidence class | `C03-CP-E-008` — IMPLEMENTATION DESIGN |
| Work package | `C03-CP-WP-007` — Adapter and C03 Implementation |
| Selected semantics | `CAPABILITY_ONLY` |
| Design type | NON-EXECUTABLE IMPLEMENTATION DESIGN DOCUMENT |
| Design status | **MATERIALIZED — INTERNAL REVIEW NOT AUTHORIZED** |
| Source code or configuration | NOT CREATED / NOT MODIFIED |
| Dependency installation | NOT PERFORMED / NOT AUTHORIZED |
| Implementation materialization | NOT AUTHORIZED |
| C03 activation or invocation | NOT AUTHORIZED |
| `AR-B-007` closure | OPEN / BLOCKED |
| Automatic downstream transition | BLOCKED |

This document defines a finite candidate implementation surface and its
contracts. It is not source code, an executable schema, a package selection,
a provider integration, a fixture, a build, a test, a runtime, an activation,
or an implementation result.

## 1. Fixed Accepted Baselines

| ID | Bound baseline | SHA-256 | Verification |
| --- | --- | --- | --- |
| `C03-WP7-I-001` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_EXECUTION_DOMAIN_ADAPTER_SPEC.md` | `C23BED2F6128D845D438ED624E399D97F03F628A32FA9F09C3A9FBBF12518C89` | MATCH |
| `C03-WP7-I-002` | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_EXECUTION_DOMAIN_ADAPTER_DESIGN_ADOPTION_DECISION.md` | `F097CF521FB3A2A917055FC4B0B04FED937167941C83CE36F8B402DC69FB49BE` | MATCH |
| `C03-WP7-I-003` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_ENFORCEMENT_ADVERSARIAL_DOMAIN_PROFILE_SPEC.md` | `35C3F7E905D2D171301114C6AAF28DF4BCCC2609ADF528A466EC3661D4F44559` | MATCH |
| `C03-WP7-I-004` | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_ENFORCEMENT_ADVERSARIAL_DOMAIN_PROFILE_ADOPTION_DECISION.md` | `59A350882A7A157D5CC899AD1C1D9DA88FBEACFF572C2785D4282DBB68AE489E` | MATCH |
| `C03-WP7-I-005` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_CONFORMANCE_VALIDATION_SPEC.md` | `199659775B125F06B348A13E928AE8989C09F27249247933827A12E580CDD9CB` | MATCH |
| `C03-WP7-I-006` | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_CONFORMANCE_VALIDATION_SPEC_ADOPTION_DECISION.md` | `45C31FBEB2A838E3C3ED898F096FD1A31A1C0B5836A554407CB5A16C7E9C514D` | MATCH |
| `C03-WP7-I-007` | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_ACTIVATION_SEMANTICS_DECISION.md` | `ABD65E645CD8D7B91FCC7BFEEC472317CA56B0B3749CFDFFD8249E9DE007BDCF` | MATCH |
| `C03-WP7-I-008` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_TIER_A_PLATFORM_CAPABILITY_CLOSURE_WORK_PACKAGE_SEQUENCE.md` | `C748CE0621E254912ED86AE6733F137F5783D6AB5342534F7D283812C634D61A` | MATCH |
| `C03-WP7-I-009` | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_TIER_A_PLATFORM_CAPABILITY_CLOSURE_WORK_PACKAGE_SEQUENCE_ADOPTION_DECISION.md` | `92E2BEB8DF730C0C45B1015876318306596225AB3557333C21A9BC2F414E781F` | MATCH |

```text
Fixed Accepted Baselines:
9 / 9 MATCH

Selected Planning Semantics:
CAPABILITY_ONLY

Implementation Authority:
NOT GRANTED
```

No historical design, validation, or adoption record transfers materialization
or execution authority to this Design.

## 2. Purpose and Non-Objectives

### 2.1 Finite Purpose

Define how a future, separately authorized local Python implementation could:

1. expose a disabled-by-default C03 capability boundary;
2. validate exact governance metadata and reject every invocation lacking a
   separately accepted Tier B authority packet;
3. map only explicit, version-bound metadata through the adopted Adapter and
   C03 Profile contracts;
4. preserve empty upstream write sets and isolate all candidate state;
5. record failure and audit metadata without logging protected content; and
6. remain provider-neutral, dependency-minimal, non-legal, and fail-closed.

### 2.2 Explicit Non-Objectives

This Design does not authorize or define an active path to:

- open, read, copy, hash, transform, upload, transmit, search, or process case
  materials or evidence bytes;
- perform native-text extraction or OCR;
- originate or validate a Fact, Legal Fact, legal rule, legal conclusion,
  filing, strategy, prediction, probability, risk score, or advice;
- select or call a model, provider, API, MCP server, Connector, Agent, Skill,
  workflow, database, queue, or external service;
- create credentials, secrets, keys, tokens, authentication mechanisms,
  session stores, or replay caches;
- install dependencies, create source code, create configuration, build, test,
  run, activate, deploy, or pilot a capability; or
- access or modify the independent ACOS source project.

## 3. Architectural Position

```text
Route A / Matter / Evidence Governance
        │
        │ exact references only; reference is not access
        ▼
Tier B Authority Packet Gate
        │
        ├── absent / invalid / stale / revoked ──► BLOCKED
        │
        ▼ accepted under separate future authority only
Route B Adapter Contract
        │
        ▼
C03 Profile Mapping Candidate
        │
        ▼
Qualified-Human Review Packet Candidate
        │
        ▼
Separate Project Owner Downstream Decision
```

Under `CAPABILITY_ONLY`, the gate and contract surface may later be implemented
and validated, but no matter-bound path is enabled. The maximum response to an
invocation without an accepted Tier B packet is a protected rejection or
blocking record.

## 4. Core Implementation Invariants

| ID | Invariant |
| --- | --- |
| `C03-WP7-II-001` | The capability is disabled by default and has no automatic activation path |
| `C03-WP7-II-002` | A separately accepted exact Tier B packet is mandatory before any matter-bound mapping or candidate generation |
| `C03-WP7-II-003` | An artifact reference never grants access to referenced bytes, paths, services, or storage |
| `C03-WP7-II-004` | Missing, unknown, stale, conflicting, invalid, unauthorized, mixed, or unreviewed input fails closed |
| `C03-WP7-II-005` | Mapping is limited to `DIRECT_COPY`, `ENUMERATION_MAP`, `FORMAT_NORMALIZATION`, and `EXPLICIT_OMISSION` |
| `C03-WP7-II-006` | Fact, identity, authority, procedural-state, legal, scope, priority, strategy, score, and intent inference are prohibited |
| `C03-WP7-II-007` | Route A, Evidence, Matter Decision, Legal Reasoning, Human Decision, and ACOS source-project write sets are empty |
| `C03-WP7-II-008` | Candidate state is isolated from upstream governance state and cannot reverse-propagate |
| `C03-WP7-II-009` | Every candidate remains non-legal, non-executing, version-bound, review-pending, and downstream-blocked |
| `C03-WP7-II-010` | Provider, model, dependency, environment, configuration, and executable identities cannot be silently selected or substituted |
| `C03-WP7-II-011` | Credentials, secrets, keys, tokens, raw payloads, and unnecessary personal information cannot enter records or logs |
| `C03-WP7-II-012` | Failure cannot become success, broaden scope, mutate upstream state, or trigger automatic retry or fallback |
| `C03-WP7-II-013` | Retry, idempotency, timeout, quarantine, revocation, kill, rollback, supersession, and audit interfaces are mandatory but separately implemented under WP-009 |
| `C03-WP7-II-014` | No author, implementation, executor, reviewer, test, or model may self-authorize, self-accept, self-activate, or close a blocker |
| `C03-WP7-II-015` | Every material action and state release requires a separate exact-asset and exact-scope Project Owner decision |

## 5. Candidate Technology and Dependency Posture

| Design choice | Candidate posture | Governing limitation |
| --- | --- | --- |
| Implementation language | Existing project Python 3 toolchain | Candidate design choice only; no interpreter or code is invoked by this document |
| Core dependency posture | Python standard library first | No third-party package is selected or installed |
| Serialization | Deterministic JSON-compatible records | No runtime schema or serialized instance is created |
| Storage | Abstract append-only local record interface | No database, file store, queue, or retention implementation is selected |
| Network | Disabled / absent | No HTTP client, socket, external endpoint, or provider route |
| Provider interface | Null/blocked adapter only | No model or provider identity selected; every external request remains prohibited |
| Authentication | Outside current design surface | No credential, key, token, identity provider, or authentication mechanism created |
| Test framework | Deferred to separately adopted validation design | No fixture or test dependency selected |

The standard-library-first posture implements the earlier requirement to reuse
existing technology and avoid unnecessary new infrastructure. Any later need
for a third-party dependency requires a separate dependency proposal, integrity
and license review, exact version binding, security review, and Project Owner
decision.

## 6. Finite Proposed Implementation Surface

The following paths are proposed for a later exact-file materialization
authorization. None is created by this Design.

| Surface ID | Proposed path | Responsibility | Prohibited responsibility |
| --- | --- | --- | --- |
| `C03-WP7-S-001` | `scripts/phase2_runtime/__init__.py` | Declare the future local Phase 2 runtime namespace | No activation, import side effect, provider call, or configuration load |
| `C03-WP7-S-002` | `scripts/phase2_runtime/route_b_c03/__init__.py` | Export only stable contract types and the closed capability facade | No auto-registration, plugin mutation, or runtime startup |
| `C03-WP7-S-003` | `scripts/phase2_runtime/route_b_c03/contracts.py` | Closed enumerations and immutable record contracts | No I/O, inference, network, persistence, or legal logic |
| `C03-WP7-S-004` | `scripts/phase2_runtime/route_b_c03/identity_gate.py` | Validate route, domain, version, capability, Tier B packet, revocation, and scope metadata | No material access, role inference, token validation, or identity enrichment |
| `C03-WP7-S-005` | `scripts/phase2_runtime/route_b_c03/mapping.py` | Apply four permitted deterministic mapping classes with field trace | No inference, silent default, legal conclusion, or adverse suppression |
| `C03-WP7-S-006` | `scripts/phase2_runtime/route_b_c03/isolation.py` | Enforce namespace and empty upstream/external write-set contracts | No upstream mutation, database, filesystem traversal, or external transfer |
| `C03-WP7-S-007` | `scripts/phase2_runtime/route_b_c03/failures.py` | Construct closed failure, rejection, and quarantine candidates | No retry execution, fallback, recovery execution, or exception suppression |
| `C03-WP7-S-008` | `scripts/phase2_runtime/route_b_c03/audit.py` | Construct redacted append-only audit-record candidates | No persistence selection, raw payload logging, credential logging, or deletion execution |
| `C03-WP7-S-009` | `scripts/phase2_runtime/route_b_c03/provider_port.py` | Define a blocked provider-port protocol and null implementation | No provider selection, network client, SDK, authentication, or request transmission |
| `C03-WP7-S-010` | `scripts/phase2_runtime/route_b_c03/capability.py` | Coordinate the closed gate and pure contract operations | No public API server, CLI execution, scheduler, automatic activation, or matter invocation |

### 6.1 Future Test Surface

These paths are validation-design targets only and remain outside WP-007
materialization unless separately authorized:

| Proposed future path | Intended design purpose | Current state |
| --- | --- | --- |
| `tests/phase2_runtime/route_b_c03/test_identity_gate.py` | Gate and authority-metadata scenarios | NOT CREATED / NOT AUTHORIZED |
| `tests/phase2_runtime/route_b_c03/test_mapping.py` | Permitted/prohibited transformation scenarios | NOT CREATED / NOT AUTHORIZED |
| `tests/phase2_runtime/route_b_c03/test_isolation.py` | Empty write-set and namespace-isolation scenarios | NOT CREATED / NOT AUTHORIZED |
| `tests/phase2_runtime/route_b_c03/test_failures.py` | Failure, retry eligibility, quarantine, and no-fallback scenarios | NOT CREATED / NOT AUTHORIZED |
| `tests/phase2_runtime/route_b_c03/test_audit.py` | Redaction, audit identity, append-only, and tamper scenarios | NOT CREATED / NOT AUTHORIZED |
| `tests/phase2_runtime/route_b_c03/test_capability.py` | Disabled-default and Tier B gate scenarios | NOT CREATED / NOT AUTHORIZED |

No proposed path changes the current repository layout until an exact-file
materialization decision is separately signed.

## 7. Module Dependency Contract

```text
contracts
   ↑
   ├── identity_gate
   ├── mapping
   ├── isolation
   ├── failures
   ├── audit
   └── provider_port
          ↑
       capability
```

| Module | May depend on | Must not depend on |
| --- | --- | --- |
| `contracts` | Python standard-library value/type facilities only | Filesystem, network, provider, project plugins, legal skills, ACOS, persistence |
| `identity_gate` | `contracts` | Material bytes, personal-identity enrichment, credential verification, external identity service |
| `mapping` | `contracts` | Legal reasoning, OCR, model inference, provider SDK, hidden lookup, upstream mutation |
| `isolation` | `contracts` | Database, network, Route A write API, Evidence write API, ACOS write API |
| `failures` | `contracts` | Retry executor, scheduler, fallback provider, hidden exception swallowing |
| `audit` | `contracts` | Raw payloads, secrets, credentials, material content, persistence engine |
| `provider_port` | `contracts` | Any concrete provider, network client, SDK, token, endpoint, or model name |
| `capability` | All local C03 modules | External service, legal skill, material store, OCR, database, runtime scheduler |

Circular dependencies are prohibited. Import-time I/O, registration, state
mutation, network access, environment-secret loading, and activation are
prohibited.

## 8. Closed Record Contracts

The following are abstract immutable record contracts, not executable classes
or schemas.

### 8.1 Capability Configuration Reference

| Field | Requirement |
| --- | --- |
| `capability_id` | Fixed value identifying the C03 capability design |
| `capability_version` | Exact adopted implementation version reference |
| `implementation_sha256` | Exact accepted implementation identity |
| `configuration_sha256` | Exact accepted configuration identity or explicit `NONE` |
| `activation_decision_reference` | Exact capability-only activation decision; absent until separately authorized |
| `state` | `DISABLED`, `ENABLED_CAPABILITY_ONLY`, `REVOKED`, or `STALE` |
| `revocation_reference` | Required when revoked |
| `validity` | Explicit validity window or non-active state |

Default state is `DISABLED`.

### 8.2 Tier B Authority Packet Reference

| Field | Requirement |
| --- | --- |
| `packet_id` | Stable governance identifier |
| `packet_version` | Exact version |
| `packet_sha256` | Complete SHA-256 |
| `matter_id` | Stable matter governance identifier; no real-person name required |
| `matter_version` | Exact matter version |
| `actor_reference` | Stable attributable governance identifier |
| `purpose` | Finite approved purpose |
| `operation` | Exact approved C03 operation |
| `input_set_sha256` | Exact admitted-reference set identity |
| `output_class` | One permitted C03 candidate class |
| `decision_reference` | Project Owner matter-bound invocation decision |
| `valid_from` / `valid_until` | Explicit validity window |
| `revocation_state` | Current and independently supplied governance state |
| `state` | `ACCEPTED`, `BLOCKED`, `WITHDRAWN`, `STALE`, or `REVOKED` |

The implementation design validates packet metadata only. It does not open the
packet's referenced assets or independently establish the underlying authority.

### 8.3 Governed Input Envelope Reference

Mandatory fields preserve the adopted Adapter contract:

```text
envelope_id
route / route_version
domain_id / domain_version
adapter_contract_version
matter_id / matter_version / matter_authorization_reference
actor_reference / role / authority_reference
purpose / operation
input_artifact_references
requested_output_scope / prohibited_output_scope
execution_authorization_reference
audit_correlation_id
```

Every input-artifact reference requires artifact ID, type, version, SHA-256,
source reference, readiness state, validation state, and human-review
reference. The record contains references only and grants no byte access.

### 8.4 Mapping Rule

| Field | Closed requirement |
| --- | --- |
| `rule_id` | Unique within exact mapping-contract version |
| `source_path` | Explicit governed-input metadata path |
| `target_path` | Explicit request-candidate metadata path |
| `transformation_type` | One of four permitted values only |
| `allowed_source_states` | Closed set; missing state is blocking |
| `null_policy` | Explicit null, block, reject, or omit policy |
| `conflict_policy` | Preserve and block/quarantine/human-review policy |
| `provenance_required` | Always true |
| `human_review_required` | Explicit boolean; defaults cannot be inferred |

### 8.5 Candidate Records

| Candidate record | Maximum current meaning | Mandatory restriction |
| --- | --- | --- |
| Adapter Request Candidate | Metadata mapping candidate | Cannot be sent or executed without separate matter-bound and provider authority |
| Domain Response Envelope | Unvalidated response reference | Cannot exist while provider port is null/blocked |
| Adapter Output Candidate | Normalized candidate reference | Requires qualified-human review and separate downstream decision |
| Failure Record | Protected Route B failure metadata | Cannot mutate upstream state or trigger retry |
| Audit Record Candidate | Redacted correlation and transition metadata | Not persisted until a separate storage/retention design is accepted |

## 9. Capability State Contract

### 9.1 Capability States

| State | Meaning | Permitted action |
| --- | --- | --- |
| `DISABLED` | No accepted capability activation decision | Return protected disabled response only |
| `ENABLED_CAPABILITY_ONLY` | Capability-only decision exists for exact version | Validate invocation metadata and enforce Tier B gate only |
| `REVOKED` | Capability authority withdrawn | Reject every invocation and record redacted revocation response candidate |
| `STALE` | Implementation, configuration, dependency, design, or authority identity changed | Reject every invocation pending new review and decision |

### 9.2 Invocation States

| State | Entry requirement | Permitted next state |
| --- | --- | --- |
| `INVOCATION_RECEIVED` | Exact metadata request supplied to an already enabled capability | `GATE_CHECKING` only |
| `GATE_CHECKING` | Capability identity and Tier B packet metadata available | `BLOCKED`, `REJECTED`, or `ELIGIBLE_FOR_MAPPING` |
| `BLOCKED` | Required identity, authority, state, review, or input unavailable | Terminal until a new exact invocation |
| `REJECTED` | Mandatory isolation, scope, integrity, or output boundary violated | Terminal |
| `ELIGIBLE_FOR_MAPPING` | Exact Tier B packet accepted and all mapping preconditions pass | `MAPPING` only under separately authorized matter-bound invocation |
| `MAPPING` | Separate matter-bound invocation authority exists | `MAPPING_CANDIDATE`, `BLOCKED`, `REJECTED`, or `QUARANTINED` |
| `MAPPING_CANDIDATE` | Deterministic metadata mapping completed | `HUMAN_REVIEW_PENDING` only |
| `QUARANTINED` | Conflict, tamper, partial result, or integrity issue exists | Terminal pending separate resolution |
| `HUMAN_REVIEW_PENDING` | Exact candidate packet prepared | Remains blocked pending qualified-human disposition |

Under current `CAPABILITY_ONLY` authority, the maximum implemented behavior
eligible for later activation is `GATE_CHECKING → BLOCKED/REJECTED`. No
`ELIGIBLE_FOR_MAPPING` transition may be acted upon until a separately accepted
matter-bound invocation authority exists.

### 9.3 Transition Guards

Every transition must bind:

- prior state and expected next state;
- capability, implementation, configuration, domain, Adapter, and Profile
  versions;
- invocation, Tier B packet, matter, actor, purpose, operation, and output
  references;
- revocation, stale, kill, and conflict states;
- reason code and redacted audit correlation; and
- exact authorization reference when the transition is material.

Unknown transition, missing guard, version mismatch, or attempted transition
skip produces `BLOCKED — STATE CONTRACT FAILURE`.

## 10. Deterministic Mapping Contract

| Transformation | Permitted behavior | Mandatory trace |
| --- | --- | --- |
| `DIRECT_COPY` | Copy one explicit metadata value without semantic change | Source and target paths, source artifact/version, rule ID |
| `ENUMERATION_MAP` | Map one value through a closed reviewed enumeration | Enumeration version, source value, target value, rule ID |
| `FORMAT_NORMALIZATION` | Losslessly normalize an allowed representation | Original representation, normalized representation, rule ID |
| `EXPLICIT_OMISSION` | Omit a field the exact target contract does not accept | Source path, omission reason, rule ID |

The following always fail:

```text
FACT_INFERENCE
IDENTITY_INFERENCE
AUTHORITY_INFERENCE
PROCEDURAL_STATE_INFERENCE
SCOPE_EXPANSION
ADVERSE_MATERIAL_SUPPRESSION
LEGAL_CONCLUSION
SILENT_DEFAULT
PRIORITY_OR_STRATEGY_INFERENCE
SCORE_OR_PREDICTION
```

### 10.1 Null, Gap, Conflict, and Stale Policy

| Condition | Required response |
| --- | --- |
| Required value missing | `BLOCKED — REQUIRED INPUT MISSING` |
| Optional value missing | Explicit null plus source trace |
| Unknown value | Preserve `UNKNOWN` |
| Conflicting values | Preserve all; block, quarantine, or require human review |
| Stale value/version | `BLOCKED — VERSION FAILURE` |
| Unready artifact reference | `BLOCKED — READINESS FAILURE` |
| Cross-matter or mixed-matter value | `REJECTED — ISOLATION FAILURE` |
| Inference required | `REJECTED — MAPPING CONTRACT FAILURE` |

## 11. Read-Set and Write-Set Contract

| Namespace | Permitted read set | Permitted write set |
| --- | --- | --- |
| Route A | Exact versioned governance references only after separate Tier B authority | `[]` |
| Evidence | Exact admitted-reference metadata only after separate Tier B authority | `[]` |
| Matter Decision | Exact authorization reference metadata only | `[]` |
| Legal Reasoning | Exact governance-control references only | `[]` |
| Human Decision | Exact accepted decision-reference metadata only | `[]` |
| Route B local candidate namespace | Exact current-invocation candidate metadata | Request, failure, audit, response-reference, and output candidates only when separately authorized |
| External domain | None under current design | `[]` |
| ACOS source project | `[]` | `[]` |

The current design authorizes no read or write operation. The table defines
future contract limits only.

### 11.1 Prohibited Reverse Propagation

No candidate, failure, audit record, provider response, review, or output may
directly change:

- Route A Manifest, confirmation, source, access, readiness, processing, or
  acquisition state;
- Evidence identity, lifecycle, extraction, verification, readiness, Fact, or
  Legal Fact state;
- matter identity, authorization, priority, decision, claim, request-right,
  defense, strategy, or filing state;
- legal authority, issue, rule, element, proof, support, gap, or conclusion;
- qualified-human decisions; or
- ACOS source-project files, state, configuration, or history.

## 12. Provider and External-Dependency Boundary

### 12.1 Provider Port

The proposed `provider_port` exposes only a future abstract protocol and a
mandatory null implementation:

```text
Provider Status:
NOT_SELECTED

Network Transport:
ABSENT

Credentials:
PROHIBITED

Default Provider Behavior:
BLOCKED — DEPENDENCY NOT AUTHORIZED
```

A future provider proposal must separately define provider identity, model,
endpoint class, data classification, transfer boundary, jurisdiction,
credential handling, retention, logging, error behavior, availability,
versioning, cost boundary, withdrawal, and fallback. No fallback may broaden
scope or silently select another provider.

### 12.2 Dependency Admission Record

Every future non-standard-library dependency requires:

| Field | Requirement |
| --- | --- |
| Package identity | Exact package and source repository/distribution |
| Version and integrity | Exact version plus digest or equivalent integrity evidence |
| Purpose | One finite interface need with no broader authority |
| License | Recorded and reviewed compatibility |
| Security | Vulnerability, maintenance, provenance, and supply-chain review |
| Data access | Exact filesystem, network, environment, process, and content permissions |
| Alternatives | Existing standard-library or project capability considered first |
| Failure and withdrawal | Fail-closed behavior, replacement, rollback, and invalidation |
| Decision | Separate Project Owner dependency-admission decision |

No dependency admission record is created by this Design.

## 13. Security and Privacy Boundary

| Control | Design requirement |
| --- | --- |
| Credential exclusion | Reject or redact credential, secret, key, token, cookie, authorization header, or private endpoint content |
| Data minimization | Accept only fields required for exact gate or mapping determination |
| Purpose limitation | Bind every record to exact capability, matter, operation, and output purpose |
| Context isolation | Separate project, matter, actor, session, provider, version, and invocation identifiers |
| Content isolation | Do not store or log raw case material, evidence, prompt, attachment, history, provider payload, or legal analysis |
| Retention | No retention implementation until a separate retention/deletion design and authorization exist |
| Logging | Redacted metadata only; no raw values beyond approved stable governance identifiers |
| Integrity | SHA/version checks for every accepted design, implementation, configuration, packet, and candidate reference |
| Replay and stale protection | Exact invocation/idempotency reference, validity window, supersession, revocation, and stale checks |
| Least authority | Capability-only state cannot acquire matter or provider authority |
| Kill and revocation | Protected state entered before further processing; release requires separate authority |

## 14. Failure Contract and WP-009 Interface

### 14.1 Failure Classes

| Failure class | Required candidate response | Automatic retry | Upstream mutation |
| --- | --- | --- | --- |
| Capability disabled | `BLOCKED — CAPABILITY NOT ACTIVE` | NO | None |
| Tier B packet absent | `BLOCKED — TIER B AUTHORITY REQUIRED` | NO | None |
| Packet invalid, stale, expired, or revoked | `BLOCKED — AUTHORITY FAILURE` | NO | None |
| Domain/version mismatch | `BLOCKED — DOMAIN IDENTITY FAILURE` | NO | None |
| Matter/project/session/provider mismatch | `REJECTED — ISOLATION FAILURE` | NO | None |
| Artifact unready or provenance incomplete | `BLOCKED — READINESS/PROVENANCE FAILURE` | NO | None |
| Mapping requires inference/default/suppression | `REJECTED — MAPPING CONTRACT FAILURE` | NO | None |
| Credential or protected content detected | `QUARANTINED — CONTENT BOUNDARY FAILURE` | NO | None |
| External dependency requested | `BLOCKED — DEPENDENCY NOT AUTHORIZED` | NO | None |
| Provider port invoked while null | `BLOCKED — PROVIDER NOT AUTHORIZED` | NO | None |
| Timeout/partial result in later authorized path | `QUARANTINED — INCOMPLETE` | Policy required | None |
| Tamper or integrity mismatch | `QUARANTINED — INTEGRITY FAILURE` | NO | None |
| Legal or downstream authority claimed | `REJECTED — OUTPUT BOUNDARY FAILURE` | NO | None |

### 14.2 Required WP-009 Interfaces

WP-007 defines only the interface points that WP-009 must later design:

```text
retry_policy_reference
idempotency_key_reference
timeout_policy_reference
quarantine_reference
revocation_reference
kill_switch_reference
rollback_reference
supersession_reference
audit_integrity_reference
release_decision_reference
```

No retry, idempotency, timeout, quarantine, revocation, kill, rollback,
supersession, audit persistence, or release mechanism is implemented here.

## 15. Audit Record Candidate Contract

| Field | Requirement |
| --- | --- |
| `audit_id` | Stable unique record identifier |
| `correlation_id` | Exact invocation correlation reference |
| `capability_id/version` | Exact capability contract identity |
| `implementation/configuration_sha256` | Exact accepted runtime identities when later materialized |
| `domain_id/version` | Exact C03 profile identity |
| `tier_b_packet_reference` | Identifier/version/SHA/state only; no packet content |
| `matter/actor references` | Stable governance identifiers only; no unnecessary real-person data |
| `purpose/operation` | Exact finite values |
| `input_artifact_references` | IDs, versions, SHAs, readiness states only |
| `state_transition` | Prior state, next state, reason code, decision reference |
| `mapping_trace_reference` | Reference only; no raw material values |
| `failure/quarantine references` | Closed failure identity and protected state |
| `human/downstream decision references` | Exact references and states only |
| `created_at` | System-observed timestamp category; no model-generated governance time |
| `supersedes` | Prior exact record reference when applicable |
| `redaction_state` | Mandatory redaction determination |

Audit records are append-only candidates. Persistence, retention, access,
tamper validation, deletion, and recovery belong to WP-009 and later exact
authorizations.

## 16. Candidate Output and Human-Gate Contract

### 16.1 Permitted Candidate Classes

```text
C03_ISSUE_MATRIX_CANDIDATE
C03_ADVERSE_CONDITION_REGISTER_CANDIDATE
C03_CONFLICT_AND_INFORMATION_GAP_REGISTER_CANDIDATE
C03_AUTHORITY_CHECK_REQUEST_CANDIDATE
C03_QUALIFIED_HUMAN_REVIEW_PACKET_CANDIDATE
```

Every candidate must carry:

```text
CANDIDATE — REQUIRES QUALIFIED HUMAN REVIEW
NOT LEGAL ADVICE
NOT AN ENFORCEMENT INSTRUCTION
NOT AUTHORIZED FOR FILING, CONTACT, TRANSFER, OR EXECUTION
```

### 16.2 Prohibited Output Classes

```text
FINAL_LEGAL_OPINION
ENFORCEMENT_STRATEGY_OR_TACTIC
COURT_OR_AUTHORITY_SUBMISSION
ASSET_SEARCH_OR_TRACING_INSTRUCTION
ADDITIONAL_PARTY_OR_LIABILITY_CONCLUSION
OBJECTION_OR_REMEDY_CONCLUSION
SETTLEMENT_OR_PAYMENT_INSTRUCTION
OUTCOME_PREDICTION
SUCCESS_PROBABILITY
AUTOMATED_RISK_OR_COMPLIANCE_SCORE
```

### 16.3 Human Gate

The future review packet must contain exact input, contract, mapping,
omission, conflict, adverse, failure, authority, version, prohibited-use, and
audit references. Permitted human dispositions remain:

```text
REJECT
REQUEST CORRECTION
KEEP BLOCKED
APPROVE A SPECIFIC CANDIDATE FOR A SEPARATELY AUTHORIZED NEXT STEP
```

Human approval never activates C03, executes a candidate, creates provider
authority, or grants standing downstream authority.

## 17. LRG and China-Law Alignment

| Control | Implementation-design requirement |
| --- | --- |
| `LRG-00` | Exact domain, matter, actor, purpose, operation, version, and authority gates |
| `LRG-01` | Reference is not access; readiness-aware metadata only; zero Evidence mutation |
| `LRG-02` | Source, extraction, Fact, and Legal Fact remain distinct; no promotion by mapping |
| `LRG-03` | Candidate structures only; no originating legal judgment or strategy |
| `LRG-04` | `SUPPORTED`, `UNKNOWN`, `BLOCKED`, adverse, conflict, and quarantine states preserved |
| `LRG-05` | Qualified-human review and separate Project Owner downstream authority mandatory |

The implementation surface contains no current-law retrieval or legal-rule
engine. If a future matter requires authority freshness, that work remains a
separately authorized Tier B activity using current statutes, administrative
regulations, judicial interpretations, mandatory rules, and the repository's
updateable case-authority interface. Guiding and reference cases may calibrate
reasoning but are not common-law precedent and do not replace governing law.

## 18. Future Materialization Evidence Contract

The future `C03-CP-E-009` Materialization Record must contain:

| Evidence subject | Mandatory content |
| --- | --- |
| Authorization | Exact implementation-materialization decision and permitted file set |
| Design lineage | This exact Design SHA plus its review and adoption decisions |
| File inventory | Every created/modified file, exact path, SHA-256, size, and purpose |
| Diff boundary | Authorized versus observed change set; unauthorized changes must equal zero |
| Dependency inventory | Standard-library modules and every third-party package with version/integrity decision |
| Configuration inventory | Exact files/keys/defaults; secrets must equal zero |
| Provider/network inventory | Selected providers/endpoints must equal zero unless separately authorized |
| Build identity | Interpreter/tool versions and reproducible build/check commands |
| Static checks | Syntax, import, schema/record, lint, secret, path, network, and write-set checks |
| Boundary checks | Route A, case-material, OCR, legal-analysis, ACOS, Git, and external-service actions |
| Defect register | Blocking/non-blocking defects, evidence, disposition, correction, supersession |
| Resulting state | Materialized only; review, validation, closure, activation, and deployment remain separate |

The Materialization Record cannot claim observed operational conformance. That
requires the separately governed WP-008 evidence chain.

## 19. Implementation Design Review Questions

| ID | Question |
| --- | --- |
| `C03-WP7-RQ-001` | Do all nine fixed accepted baselines match exactly? |
| `C03-WP7-RQ-002` | Is the design limited to `CAPABILITY_ONLY` with no matter invocation authority? |
| `C03-WP7-RQ-003` | Is the proposed implementation surface finite and exact by path and responsibility? |
| `C03-WP7-RQ-004` | Does the design reuse the existing Python toolchain without selecting or installing new packages? |
| `C03-WP7-RQ-005` | Is the capability disabled by default with no import-time or automatic activation? |
| `C03-WP7-RQ-006` | Does every matter-bound path require an accepted exact Tier B packet? |
| `C03-WP7-RQ-007` | Are artifact references prevented from becoming material, filesystem, service, or storage access? |
| `C03-WP7-RQ-008` | Are the four permitted mapping classes closed and all inference/default/suppression classes prohibited? |
| `C03-WP7-RQ-009` | Are Route A, Evidence, Matter Decision, Legal Reasoning, Human Decision, and ACOS write sets empty? |
| `C03-WP7-RQ-010` | Are provider, network, credential, secret, token, package, database, queue, and external-service paths absent by default? |
| `C03-WP7-RQ-011` | Are capability and invocation states finite, guarded, fail-closed, and non-skippable? |
| `C03-WP7-RQ-012` | Does `CAPABILITY_ONLY` prevent acting on an `ELIGIBLE_FOR_MAPPING` state? |
| `C03-WP7-RQ-013` | Are null, gap, conflict, stale, readiness, matter-isolation, and integrity failures explicit? |
| `C03-WP7-RQ-014` | Are retry, idempotency, timeout, quarantine, revocation, kill, rollback, supersession, and audit deferred to explicit WP-009 interfaces? |
| `C03-WP7-RQ-015` | Are raw materials, prompts, attachments, histories, payloads, credentials, and unnecessary personal data excluded from logs? |
| `C03-WP7-RQ-016` | Are the five permitted and ten prohibited C03 output classes preserved exactly? |
| `C03-WP7-RQ-017` | Is qualified-human review mandatory and separated from Project Owner downstream authority? |
| `C03-WP7-RQ-018` | Are LRG-00 through LRG-05 mandatory and non-overridable? |
| `C03-WP7-RQ-019` | Is China-law alignment preserved without embedding mutable legal rules into code? |
| `C03-WP7-RQ-020` | Does the future materialization evidence contract prevent design PASS from becoming runtime-conformance evidence? |
| `C03-WP7-RQ-021` | Are staleness, revocation, supersession, correction, and historical integrity explicit? |
| `C03-WP7-RQ-022` | Can any author, executor, reviewer, implementation, test, or model self-authorize, self-accept, or self-activate? |
| `C03-WP7-RQ-023` | Are Route A, case material, native text, OCR, legal analysis, external provider, ACOS, and Git boundaries preserved? |
| `C03-WP7-RQ-024` | Does this Design create zero source, configuration, dependency, fixture, runtime, or observed evidence? |

## 20. Implementation Design Acceptance Gates

| Gate | PASS condition |
| --- | --- |
| `C03-WP7-DG-001` — Baseline Integrity | `9 / 9` fixed accepted baselines match |
| `C03-WP7-DG-002` — Capability-Only Fidelity | No matter access, candidate generation, provider call, or downstream authority is enabled |
| `C03-WP7-DG-003` — Finite Surface | Every proposed file/module has one bounded responsibility and explicit exclusions |
| `C03-WP7-DG-004` — Existing-Technology Reuse | Existing Python toolchain and standard-library-first posture are used; no new package is selected |
| `C03-WP7-DG-005` — Disabled Default | No import, startup, registration, configuration, or default can activate the capability |
| `C03-WP7-DG-006` — Tier B Gate | Every matter-bound path requires exact accepted Tier B authority |
| `C03-WP7-DG-007` — Deterministic Mapping | Four mapping classes and complete field trace are enforced; inference/default/suppression fail |
| `C03-WP7-DG-008` — State Isolation | Upstream, Human Decision, external-domain, and ACOS write sets remain empty |
| `C03-WP7-DG-009` — Provider and Dependency Isolation | No provider, network, credential, SDK, package, database, queue, or fallback is selected |
| `C03-WP7-DG-010` — Security and Privacy | Credential exclusion, minimization, context isolation, redaction, integrity, replay, revocation, and least authority are explicit |
| `C03-WP7-DG-011` — Failure Contract | Every missing, stale, unauthorized, conflicting, unready, tampered, or out-of-contract path fails closed |
| `C03-WP7-DG-012` — WP-009 Interface | Recovery and audit controls are complete interface requirements but are not implemented or falsely claimed |
| `C03-WP7-DG-013` — Candidate Isolation | Outputs remain candidates requiring qualified-human review and separate downstream authority |
| `C03-WP7-DG-014` — LRG and China-Law Alignment | Six LRG controls and statute-centered, updateable China-law boundaries are preserved |
| `C03-WP7-DG-015` — Materialization Evidence | Future E-009 requires exact files, SHAs, dependencies, configuration, checks, defects, and zero-scope-drift evidence |
| `C03-WP7-DG-016` — Authority Separation | Design, materialization, review, validation, closure, activation, and deployment each require separate decisions |
| `C03-WP7-DG-017` — Project Separation | Route A, case materials, OCR, legal analysis, and ACOS remain outside the authorized implementation surface |
| `C03-WP7-DG-018` — Zero Implementation Pollution | No source, configuration, dependency, provider, fixture, test, runtime, Git, or deployment action occurs |

## 21. Current Evidence and Blocker Ledger

| Item | Current state | Effect |
| --- | --- | --- |
| `C03-CP-E-008` WP-007 Implementation Design | MATERIALIZED — REVIEW NOT AUTHORIZED | Design candidate only |
| `C03-CP-E-009` WP-007 Materialization Record | NOT CREATED / NOT AUTHORIZED | `AR-B-007` remains open |
| `C03-CP-E-012` WP-009 Recovery-Control Matrix | NOT CREATED / NOT AUTHORIZED | `AR-B-009` remains open |
| `C03-CP-E-013` WP-009 Audit/Revocation Validation Record | NOT CREATED / NOT AUTHORIZED | `AR-B-009` remains open |
| `C03-CP-E-010` WP-008 Operational Validation Plan | NOT CREATED / NOT AUTHORIZED | `AR-B-008` remains open |
| `C03-CP-E-011` WP-008 Observed Validation Result | NOT CREATED / NOT AUTHORIZED | `AR-B-008` remains open |

```text
Tier A Design Evidence Created:
1 / 3

Tier A Materialization or Validation Evidence Created:
0 / 3

Tier A Blockers Closed:
0 / 3

Total C03 Blockers Closed:
0 / 10

C03 Activation Readiness:
NOT READY
```

## 22. Explicit Materialization Boundary

| Activity | Status under this Design authorization |
| --- | --- |
| WP-007 Implementation Design document | MATERIALIZED — THIS ASSET ONLY |
| WP-007 Design internal review or adoption | NOT AUTHORIZED |
| Proposed Python package or module creation | NOT AUTHORIZED / NOT CREATED |
| Configuration, runtime schema, database, queue, or storage creation | NOT AUTHORIZED / NOT CREATED |
| Package or dependency installation | NOT AUTHORIZED / NOT PERFORMED |
| Provider, model, network, API, Connector, or MCP selection/invocation | NOT AUTHORIZED / NOT PERFORMED |
| Credential, secret, key, token, endpoint, or private configuration access | NOT AUTHORIZED / NOT PERFORMED |
| Fixture creation, build, lint, test, runtime, or operational validation | NOT AUTHORIZED / NOT PERFORMED |
| WP-009 or WP-008 evidence materialization | NOT AUTHORIZED / NOT CREATED |
| Blocker closure | NOT AUTHORIZED / `0 / 3` TIER A CLOSED |
| C03 activation, matter invocation, pilot, deployment, or production | NOT AUTHORIZED |
| Route A confirmation, access, processing, native-text extraction, or OCR | NOT AUTHORIZED / NOT PERFORMED |
| Case-material, evidence, matter, or actor access | NOT AUTHORIZED / NOT PERFORMED |
| Legal analysis, advice, conclusion, filing, strategy, or external contact | NOT AUTHORIZED / NOT PERFORMED |
| ACOS source-project access or modification | NOT AUTHORIZED / NOT PERFORMED |
| Git commit, push, branch, merge, or repository mutation | NOT AUTHORIZED / NOT PERFORMED |

## 23. Required Next Governance State

```text
C03-CP-E-008 WP-007 Implementation Design:
MATERIALIZED — INTERNAL REVIEW NOT AUTHORIZED

WP-007 Implementation Materialization:
NOT AUTHORIZED

WP-009 / WP-008:
NOT AUTHORIZED

Tier A Blockers Closed:
0 / 3

Total C03 Blockers Closed:
0 / 10

C03 Activation Readiness:
NOT READY

C03 Activation / Matter Invocation:
NOT AUTHORIZED

Automatic Downstream Transition:
BLOCKED
```

The next eligible action is a separate fixed-SHA Project Owner authorization
for a read-only internal architecture review of this Design. Review or adoption
cannot authorize code, dependencies, configuration, validation, closure,
activation, invocation, or deployment.
