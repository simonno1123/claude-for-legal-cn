# Phase 2 Route B C03 WP-009 Recovery and Audit Control Design

## 0. Design Control

| Field | Value |
| --- | --- |
| Asset | `TASK_PHASE2_ROUTE_B_C03_WP_009_RECOVERY_AND_AUDIT_CONTROL_DESIGN.md` |
| Evidence class | `C03-CP-E-012` — RECOVERY-CONTROL MATRIX DESIGN |
| Work package | `C03-CP-WP-009` — Recovery and Audit Controls |
| Required order | `WP-007 → WP-009 → WP-008` |
| Activation semantics | `CAPABILITY_ONLY` |
| Artifact type | DESIGN DOCUMENT ONLY |
| Design status | **MATERIALIZED — INTERNAL REVIEW NOT AUTHORIZED** |
| Implementation or control execution | NOT AUTHORIZED |
| Validation record `C03-CP-E-013` | NOT CREATED / NOT AUTHORIZED |
| C03 activation or matter invocation | NOT AUTHORIZED |
| Automatic downstream transition | BLOCKED |

This document fixes the recovery, failure, revocation, audit-integrity, and
release-control design required before WP-007 and WP-009 may be considered for
joint materialization. It is not an implementation, test, observed result,
blocker-closure record, or activation authority.

## 1. Fixed Accepted Baselines

| ID | Bound asset | SHA-256 | Verification |
| --- | --- | --- | --- |
| `C03-WP9-I-001` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_ACTIVATION_PREREQUISITE_CLOSURE_PLAN.md` | `D27B8D6CFF4B4F39B6A34E34D61E691183B12FB03529F6AC665F20A54CA28329` | MATCH |
| `C03-WP9-I-002` | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_ACTIVATION_PREREQUISITE_CLOSURE_PLAN_ADOPTION_DECISION.md` | `E69D00A4CB8CBDFD71415A4830FDBF975BB3A95EA4894B467A6B20C10DBDAF40` | MATCH |
| `C03-WP9-I-003` | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_ACTIVATION_SEMANTICS_DECISION.md` | `ABD65E645CD8D7B91FCC7BFEEC472317CA56B0B3749CFDFFD8249E9DE007BDCF` | MATCH |
| `C03-WP9-I-004` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_TIER_A_PLATFORM_CAPABILITY_CLOSURE_WORK_PACKAGE_SEQUENCE.md` | `C748CE0621E254912ED86AE6733F137F5783D6AB5342534F7D283812C634D61A` | MATCH |
| `C03-WP9-I-005` | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_TIER_A_PLATFORM_CAPABILITY_CLOSURE_WORK_PACKAGE_SEQUENCE_ADOPTION_DECISION.md` | `92E2BEB8DF730C0C45B1015876318306596225AB3557333C21A9BC2F414E781F` | MATCH |
| `C03-WP9-I-006` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_007_IMPLEMENTATION_DESIGN.md` | `BD4BCC607CBFE99A7513EE938BBF4AEF792076D43190A8F3BD0805D1AEA3C545` | MATCH |
| `C03-WP9-I-007` | `.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_WP_007_IMPLEMENTATION_DESIGN_REVIEW.md` | `5A7E290A6DE71B2A528BD0E9900E3B7EFF073DCF66944A47C79BB98110C5829D` | MATCH |
| `C03-WP9-I-008` | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_WP_007_IMPLEMENTATION_DESIGN_ADOPTION_DECISION.md` | `71911C4B56C4C1D1F6101EA0A7B27E61834CB3520765D4A18D02CD8EE73F832B` | MATCH |

No historical evidence, review result, implementation status, or activation
authority is transferred beyond the exact identities recorded above.

## 2. Purpose and Non-Objectives

### 2.1 Finite Purpose

This Design:

1. closes the abstract recovery and audit-control interface left by WP-007;
2. defines fail-closed entry, retry, idempotency, timeout, quarantine,
   revocation, kill, rollback, supersession, audit-integrity, and release gates;
3. fixes finite control states, transition guards, protected terminal states,
   and empty unauthorized write sets;
4. defines the evidence that later joint WP-007/WP-009 materialization must
   record; and
5. preserves the separation between design, implementation, validation,
   blocker closure, activation, matter invocation, and deployment.

### 2.2 Explicit Non-Objectives

This Design does not:

- implement or execute retry, delay, timeout, quarantine, revocation, kill,
  rollback, supersession, persistence, retention, deletion, or release;
- create a database, queue, scheduler, worker, service, API, Connector, MCP,
  provider client, credential store, or external endpoint;
- access Route A, case material, evidence bytes, OCR output, legal analysis,
  prompts, attachments, histories, or provider payloads;
- create test fixtures, run validation, produce observed evidence, close a
  blocker, or establish activation readiness;
- issue legal advice, a filing, a strategy, an authority conclusion, a risk
  score, or a human decision; or
- modify the independent ACOS source project or perform Git operations.

## 3. Architectural Position

```text
WP-007 closed capability and gate interfaces
        │
        ▼
WP-009 protected control envelope
        ├── fail-closed entry
        ├── retry / idempotency / timeout policy references
        ├── quarantine / revocation / kill state
        ├── rollback / supersession controls
        ├── append-only audit candidate
        └── separate release-decision gate
        │
        ▼
Protected terminal or review-pending state only
```

WP-009 cannot activate WP-007, authorize a matter, select a provider, execute
a retry, or release a quarantined/revoked/killed state. It defines the closed
interfaces required for later separately authorized materialization.

## 4. Core Control Invariants

| ID | Invariant |
| --- | --- |
| `C03-WP9-CI-001` | Every missing, invalid, stale, revoked, conflicting, mixed, unsupported, or unreviewed control input fails closed |
| `C03-WP9-CI-002` | A failure cannot become success, broaden scope, mutate upstream state, or create authority |
| `C03-WP9-CI-003` | Retry is finite, explicitly eligible, deadline-bound, non-automatic by default, and cannot change purpose, matter, provider, input, or output scope |
| `C03-WP9-CI-004` | Idempotency binds exact capability, version, matter, actor, purpose, operation, input-set, and authorization identities |
| `C03-WP9-CI-005` | Duplicate or colliding identities produce denial or quarantine and never duplicate a permitted effect |
| `C03-WP9-CI-006` | Timeout enters a protected terminal state and cannot imply cancellation success, retry authority, or partial acceptance |
| `C03-WP9-CI-007` | Quarantined content or metadata cannot re-enter mapping, candidate, provider, or downstream paths without separate release authority |
| `C03-WP9-CI-008` | Revocation and kill states take precedence over retry, mapping, recovery, rollback, and release |
| `C03-WP9-CI-009` | Rollback restores only an exact accepted prior version and preserves append-only audit history |
| `C03-WP9-CI-010` | Superseded identities become stale and cannot be silently reused or treated as fallbacks |
| `C03-WP9-CI-011` | Audit candidates contain redacted governance metadata only and exclude raw material, credentials, prompts, histories, payloads, and legal analysis |
| `C03-WP9-CI-012` | Audit persistence, access, retention, deletion, and recovery remain unselected until separately designed and authorized |
| `C03-WP9-CI-013` | Release requires an exact protected-state reference, exact resolution evidence, and a separate Project Owner release decision |
| `C03-WP9-CI-014` | Human review cannot itself activate, release, retry, invoke, deploy, or create standing authority |
| `C03-WP9-CI-015` | Route A, Evidence, Matter Decision, Legal Reasoning, Human Decision, external-domain, and ACOS write sets remain empty |
| `C03-WP9-CI-016` | Provider, network, credential, dependency, environment, and storage identities cannot be silently selected or substituted |
| `C03-WP9-CI-017` | Every material transition binds exact prior/next state, versions, references, reason code, and decision identity |
| `C03-WP9-CI-018` | No design, implementation, executor, reviewer, test, or model may self-authorize, self-release, self-accept, or close a blocker |

## 5. Required Recovery-Control Matrix

| Control family | Design requirement | Protected default | Observed evidence required later |
| --- | --- | --- | --- |
| Fail-closed entry | Validate exact capability, implementation, configuration, authority, matter, domain, purpose, operation, and state references | `BLOCKED` | Rejection plus empty unauthorized write-set record |
| Retry | Finite attempts, eligible failure set, backoff reference, deadline, identical scope, and terminal condition | `NO RETRY` | Exact attempt sequence and terminal state |
| Idempotency | Closed key inputs, replay window reference, duplicate detection, collision behavior, and single-effect rule | `DENY DUPLICATE` | Duplicate-input observation with no duplicate effect |
| Timeout | Finite deadline reference, protected timeout state, late-result denial, and audit continuity | `QUARANTINED — INCOMPLETE` | Timeout and late-result observations |
| Quarantine | Isolate disputed, partial, tampered, protected, or conflicting items from all later use | `QUARANTINED` | Entry, denial, review, and release-gate records |
| Revocation | Prioritize current independently supplied revocation state before every material transition | `REVOKED / BLOCKED` | Before/during-operation revocation observations |
| Rollback | Exact prior-version identity, restoration surface, prerequisites, limitations, and audit preservation | `ROLLBACK BLOCKED` | Reproducible restoration and integrity evidence |
| Supersession | Mark historical versions stale and reject silent reuse or fallback | `STALE / BLOCKED` | Old-version rejection and new-version binding |
| Audit integrity | Append-only identity, action, state, reason, version, result, redaction, and supersession references | `AUDIT CANDIDATE ONLY` | Completeness, tamper, access, and retention checks |
| Kill switch | Exact trigger, authority reference, protected state, response target, propagation boundary, and release authority | `KILLED / BLOCKED` | Activation, propagation, denial, and controlled release |

## 6. Closed WP-009 Interface Contracts

These are abstract immutable record contracts. They do not create executable
schemas, stored records, timers, locks, processes, or external services.

### 6.1 Recovery Context Reference

| Field | Requirement |
| --- | --- |
| `control_context_id` | Stable identifier for one exact control evaluation |
| `capability_id/version` | Exact adopted C03 capability identity |
| `implementation/configuration_sha256` | Exact accepted identities when later materialized |
| `invocation_id` | Exact current invocation reference |
| `tier_b_packet_reference` | Identifier/version/SHA/state only |
| `matter/actor references` | Stable governance identifiers only |
| `purpose/operation/output_class` | Exact finite authorized values |
| `prior_state/expected_next_state` | Closed state identifiers |
| `revocation/kill/stale states` | Current independently supplied governance states |
| `audit_correlation_id` | Exact redacted audit reference |

### 6.2 Retry Policy Reference

| Field | Requirement |
| --- | --- |
| `retry_policy_id/version/sha256` | Exact accepted policy identity |
| `eligible_failure_codes` | Closed finite set; empty by default |
| `maximum_attempts` | Finite non-negative integer; default zero |
| `backoff_policy_reference` | Exact accepted reference or `NONE` |
| `deadline_reference` | Exact timeout-policy reference |
| `scope_lock` | Exact matter, purpose, operation, input, output, provider, and version identities |
| `terminal_codes` | Closed set that can never retry |
| `authorization_reference` | Separate retry authority when required |

Automatic fallback, provider substitution, input expansion, authority reuse,
and hidden retry are prohibited.

### 6.3 Idempotency Key Reference

The key identity is derived only from the exact recorded identities below; no
content inference is permitted:

```text
capability_id / capability_version
implementation_sha256 / configuration_sha256
matter_id / matter_version
actor_reference
purpose / operation / output_class
input_set_sha256
tier_b_packet_id / version / sha256
invocation_authorization_reference
```

The design requires an exact canonicalization version and digest algorithm
identity. It does not create a key, cache, replay store, or lock.

### 6.4 Timeout Policy Reference

| Field | Requirement |
| --- | --- |
| `timeout_policy_id/version/sha256` | Exact accepted policy identity |
| `start_category` | Exact system-observed event category |
| `deadline_duration` | Finite accepted duration; no model-generated governance time |
| `late_result_policy` | Always deny use and record protected late-result metadata |
| `terminal_state` | `QUARANTINED — INCOMPLETE` unless a stricter state applies |
| `retry_effect` | `NONE` unless separately eligible and authorized |

### 6.5 Quarantine Reference

| Field | Requirement |
| --- | --- |
| `quarantine_id/version` | Stable protected-state identity |
| `subject_reference` | Exact metadata reference; no raw content duplication |
| `reason_code` | Closed failure or integrity code |
| `entry_state` | Exact state before quarantine |
| `scope` | Exact affected invocation/candidate/version only |
| `redaction_state` | Mandatory determination |
| `resolution_evidence_reference` | Absent until separately admitted |
| `release_decision_reference` | Absent until separately signed |
| `state` | `ACTIVE`, `RELEASE_PENDING`, `RELEASED`, or `SUPERSEDED` |

### 6.6 Revocation and Kill References

| Field | Requirement |
| --- | --- |
| `control_id/version/sha256` | Exact accepted revocation or kill-control identity |
| `trigger_reference` | Exact supplied event/decision reference |
| `authority_reference` | Exact Project Owner or separately accepted governing authority reference |
| `effective_state` | `REVOKED` or `KILLED` |
| `affected_scope` | Exact capability/version/configuration/invocation boundary |
| `propagation_boundary` | Every material gate and transition before further action |
| `response_target` | Finite accepted maximum propagation duration reference |
| `release_authority_required` | Always true |

No clock, signal source, watcher, event bus, or propagation mechanism is
implemented by this Design.

### 6.7 Rollback Reference

| Field | Requirement |
| --- | --- |
| `rollback_id/version` | Stable decision-bound identifier |
| `current_identity` | Exact current implementation/configuration/dependency identities |
| `target_identity` | Exact previously accepted identities |
| `restoration_surface` | Closed exact file/configuration/dependency set |
| `preconditions` | Revocation, quarantine, integrity, compatibility, and authority checks |
| `prohibited_surface` | Route A, case material, evidence, legal state, human decision, ACOS, and audit-history rewrites |
| `decision_reference` | Separate exact rollback decision |
| `post_restore_state` | `DISABLED`, `STALE`, or stricter protected state only |

Rollback never activates the restored version and never deletes audit history.

### 6.8 Supersession Reference

| Field | Requirement |
| --- | --- |
| `supersession_id` | Stable change record identifier |
| `superseded_identity` | Exact historical asset/version/SHA |
| `replacement_identity` | Exact accepted replacement asset/version/SHA |
| `reason_reference` | Exact decision or correction reference |
| `stale_effect` | Historical identity becomes non-invocable |
| `history_preservation` | Historical record remains append-only and non-reusable as current authority |

### 6.9 Audit Integrity Reference

| Field | Requirement |
| --- | --- |
| `audit_integrity_id/version/sha256` | Exact accepted integrity-policy identity |
| `record_identity_fields` | Audit ID, correlation ID, capability/version, transition, reason, result |
| `chain_reference` | Prior exact audit candidate reference when applicable |
| `subject_hashes` | Exact governance-reference hashes only |
| `redaction_state` | Mandatory before any persistence consideration |
| `tamper_state` | `UNCHECKED`, `MATCHED`, `MISMATCH`, or `UNAVAILABLE` |
| `retention/access references` | `NONE` until separately designed and accepted |
| `supersedes` | Prior exact record reference only; no overwrite |

### 6.10 Release Decision Reference

| Field | Requirement |
| --- | --- |
| `release_decision_id/version/sha256` | Exact Project Owner decision identity |
| `protected_state_reference` | Exact quarantine/revocation/kill/rollback/stale state |
| `resolution_evidence_reference` | Exact separately admitted and reviewed evidence |
| `permitted_release_scope` | One exact asset, version, invocation, purpose, and operation |
| `remaining_limitations` | Closed restrictions preserved after release |
| `validity` | Exact finite validity window or one-time effect |
| `next_state` | `DISABLED` or an exact separately authorized state only |

A release decision cannot activate C03, create matter authority, select a
provider, or authorize a candidate for downstream execution.

## 7. Control State Contract

### 7.1 Control States

| State | Meaning | Permitted behavior |
| --- | --- | --- |
| `CONTROL_DISABLED` | No accepted control-materialization identity | Return protected unavailable result only |
| `PROTECTED_BLOCKED` | Missing, invalid, unauthorized, unreviewed, or unsupported condition | Terminal for current invocation |
| `RETRY_ELIGIBILITY_PENDING` | Failure may be considered under exact retry policy | No retry until policy and authority gates pass |
| `RETRY_DENIED` | Failure is ineligible, exhausted, stale, revoked, or out of scope | Terminal |
| `QUARANTINED` | Partial, disputed, protected, conflicting, or tampered subject | Terminal pending separate resolution and release |
| `REVOKED` | Governing authority withdrawn | Reject every affected action |
| `KILLED` | Kill control active | Reject every affected action with priority |
| `ROLLBACK_PENDING` | Exact rollback candidate identified | No restoration until separate decision |
| `STALE` | Identity superseded or changed | Reject current use |
| `RELEASE_PENDING` | Resolution evidence exists but release is undecided | Remain protected |
| `RELEASED_DISABLED` | Exact release decision recorded | Return to disabled state only; no activation |

### 7.2 Transition Matrix

| Prior state | Trigger | Required guards | Permitted next state |
| --- | --- | --- | --- |
| `CONTROL_DISABLED` | Any invocation | Exact materialization absent | `PROTECTED_BLOCKED` |
| Any non-killed state | Kill active | Exact kill reference | `KILLED` |
| Any non-killed/non-revoked state | Revocation active | Exact revocation reference | `REVOKED` |
| Any state | Identity/version mismatch | Exact mismatch evidence | `STALE` or `QUARANTINED` |
| Failure received | Retry evaluation requested | Exact policy, identical scope, eligibility, attempts, deadline | `RETRY_ELIGIBILITY_PENDING` or `RETRY_DENIED` |
| `RETRY_ELIGIBILITY_PENDING` | Any missing guard | Fail-closed reason | `RETRY_DENIED` |
| Any processing state | Timeout/partial/late result | Exact timeout reference | `QUARANTINED` |
| Any processing state | Integrity conflict | Exact mismatch reference | `QUARANTINED` |
| Accepted current version | Supersession recorded | Exact replacement identity | `STALE` |
| Protected state | Rollback requested | Exact target and decision absent | `ROLLBACK_PENDING` |
| Protected state | Resolution evidence admitted | Exact evidence reference | `RELEASE_PENDING` |
| `RELEASE_PENDING` | Release decision absent/invalid/stale | Fail-closed reason | Protected prior state |
| `RELEASE_PENDING` | Exact release decision valid | Scope and limitation match | `RELEASED_DISABLED` |

Unknown transitions, skipped transitions, missing guards, model-inferred state,
or silent state normalization produce `PROTECTED_BLOCKED — STATE CONTRACT
FAILURE`.

## 8. Fail-Closed Entry Contract

Before any later authorized material action, the control gate must verify exact
capability, implementation, configuration, domain, Adapter, Profile, matter,
actor, purpose, operation, output, Tier B packet, authorization, revocation,
kill, stale, and audit-correlation references.

| Condition | Required protected response |
| --- | --- |
| Required identity absent or malformed | `PROTECTED_BLOCKED — IDENTITY FAILURE` |
| Authority absent, invalid, stale, expired, withdrawn, or revoked | `PROTECTED_BLOCKED — AUTHORITY FAILURE` |
| Matter/project/session/provider mismatch | `QUARANTINED — ISOLATION FAILURE` |
| Unsupported operation or output class | `PROTECTED_BLOCKED — SCOPE FAILURE` |
| Credential or protected content presented | `QUARANTINED — CONTENT BOUNDARY FAILURE` |
| Audit correlation absent | `PROTECTED_BLOCKED — AUDIT PRECONDITION FAILURE` |
| Revocation or kill state unavailable | `PROTECTED_BLOCKED — CONTROL STATE UNKNOWN` |

The unauthorized write set is always empty.

## 9. Retry Contract

Retry is prohibited unless every following condition is explicitly satisfied:

1. the exact failure code is in an accepted eligible set;
2. the retry policy identity and integrity match;
3. the retry count remains below a finite accepted maximum;
4. the original deadline and exact scope remain valid;
5. capability, implementation, configuration, matter, actor, purpose,
   operation, input-set, output, provider, and authorization identities match;
6. no revocation, kill, stale, quarantine, integrity, credential, isolation,
   legal-boundary, or audit failure is active; and
7. the retry cannot create a duplicate effect or bypass human/Project Owner
   gates.

No eligible failure, attempt count, backoff, or deadline is selected here.

## 10. Idempotency and Replay Contract

| Condition | Required response |
| --- | --- |
| Exact duplicate with no permitted prior effect | Idempotent protected denial or exact prior protected reference |
| Exact duplicate after one permitted effect | No second effect; append duplicate-attempt audit candidate |
| Key collision across different scope | `QUARANTINED — IDEMPOTENCY COLLISION` |
| Missing canonicalization or digest identity | `PROTECTED_BLOCKED — IDEMPOTENCY UNBOUND` |
| Replay outside accepted window | `PROTECTED_BLOCKED — REPLAY FAILURE` |
| Superseded/stale/revoked identity | `PROTECTED_BLOCKED — VERSION/AUTHORITY FAILURE` |

No cache, replay database, lock, key, or digest instance is created here.

## 11. Timeout and Late-Result Contract

A timeout never implies that an external or partial action was cancelled,
rolled back, accepted, or safe to retry. The subject enters
`QUARANTINED — INCOMPLETE`; a late result cannot be consumed, mapped, released,
or represented as a candidate. Audit continuity must preserve start category,
deadline reference, timeout observation, late-result reference, and terminal
state without recording raw payloads.

## 12. Quarantine Contract

Quarantine applies to partial, disputed, conflicting, mixed-matter, protected,
tampered, late, or integrity-uncertain subjects. Quarantined references are
excluded from mapping, provider, candidate, human-approval, downstream,
rollback-success, and activation paths. Entry is immediate; release requires
separately admitted resolution evidence and an exact Project Owner decision.

Quarantine does not establish guilt, legal effect, factual truth, or a security
finding. It is a protective technical-governance state only.

## 13. Revocation and Kill Contract

Revocation and kill evaluation precedes every material transition. `KILLED`
has priority when the kill control is active; otherwise `REVOKED` has priority
over retry, mapping, rollback, release, and provider operations. A protected
state cannot be cleared by elapsed time, restart, import, configuration
default, retry, human review alone, or model output.

This Design fixes no signal transport or maximum response time. Those values
require exact later materialization and validation evidence.

## 14. Rollback and Supersession Contract

Rollback is an exact, decision-bound restoration candidate, not an automatic
recovery mechanism. It cannot broaden the file or dependency surface, rewrite
history, delete audit candidates, restore revoked authority, activate the
capability, or alter Route A, Evidence, matter, legal, human-decision, or ACOS
state. A restored version returns to `DISABLED` or a stricter protected state.

Supersession preserves old identities as historical while making them stale
for current use. No historical implementation, configuration, dependency,
authority packet, review, or decision silently transfers to a replacement.

## 15. Audit Integrity Contract

Every later material control action must produce a redacted append-only audit
candidate containing exact identities, prior/next state, reason, result,
decision reference, redaction state, and prior-record reference. It must not
contain:

```text
raw case material
evidence content
prompt or attachment content
conversation or model history
provider request or response payload
credential / secret / key / token / cookie / authorization header
private endpoint or private configuration
legal analysis, conclusion, strategy, or filing content
unnecessary personal or sensitive information
```

Audit persistence, retention, access, deletion, recovery, encryption, signing,
and tamper verification mechanisms remain unselected and unimplemented.

## 16. Release Gate Contract

Permitted protected-state dispositions are:

```text
KEEP BLOCKED
REQUEST CORRECTION
SUPERSEDE THE SUBJECT
AUTHORIZE ONE EXACT RELEASE TO DISABLED STATE
```

Only the Project Owner may issue the positive release decision. A qualified
human may recommend a disposition but cannot release, activate, invoke,
deploy, or create standing authority. Release never means validation PASS,
blocker closure, activation readiness, or permission to process a matter.

## 17. WP-007 Integration Contract

| WP-007 interface | WP-009 control requirement | Current design effect |
| --- | --- | --- |
| `retry_policy_reference` | Bind exact policy; default no retry | Interface defined only |
| `idempotency_key_reference` | Bind exact canonical identities and collision behavior | Interface defined only |
| `timeout_policy_reference` | Bind finite deadline and late-result denial | Interface defined only |
| `quarantine_reference` | Bind protected subject, reason, scope, and release gate | Interface defined only |
| `revocation_reference` | Evaluate before every material transition | Interface defined only |
| `kill_switch_reference` | Priority protected state and separate release | Interface defined only |
| `rollback_reference` | Exact restoration surface and disabled result | Interface defined only |
| `supersession_reference` | Historical identity becomes stale | Interface defined only |
| `audit_integrity_reference` | Redacted append-only candidate and chain reference | Interface defined only |
| `release_decision_reference` | Exact Project Owner decision required | Interface defined only |

The integrated future implementation may depend only on the closed local WP-007
contracts and Python standard-library facilities. No new provider, network,
storage, scheduler, queue, credential, or third-party package is selected by
this Design.

## 18. Security and Privacy Boundary

| Control | Requirement |
| --- | --- |
| Least authority | Recovery controls cannot acquire matter, provider, candidate, release, or deployment authority |
| Credential exclusion | Credential-like content is rejected/quarantined and never logged |
| Data minimization | Only exact control-decision metadata is admitted |
| Purpose limitation | Every state and audit reference binds exact finite purpose and operation |
| Isolation | Project, matter, actor, session, provider, version, invocation, and control contexts remain distinct |
| Retention | No retention or deletion mechanism until separately designed and authorized |
| Integrity | Exact SHA/version identity required for every admitted policy, implementation, configuration, authority, and record reference |
| Replay/stale | Closed idempotency, validity, revocation, and supersession references required |
| External transfer | None; provider and network are absent |
| ACOS separation | ACOS source-project read and write sets are empty |

## 19. Future Materialization and Validation Evidence

### 19.1 Joint Materialization Evidence (`C03-CP-E-009`)

Future joint WP-007/WP-009 materialization must record:

| Evidence subject | Mandatory content |
| --- | --- |
| Authorization | Exact joint materialization decision and permitted files |
| Design lineage | Exact WP-007 Design/review/adoption and this WP-009 Design/review/adoption SHAs |
| File inventory | Every created/modified path, SHA-256, size, and purpose |
| Diff boundary | Authorized versus observed change set; unauthorized change count zero |
| Dependency/configuration/provider inventory | Standard library recorded; third-party, secret, credential, provider, endpoint, and network counts zero unless separately authorized |
| Static checks | Syntax, import side effect, closed enum/record, secret, path, network, provider, and write-set checks |
| Control presence | Ten WP-009 interface points represented without claiming observed behavior |
| Defect register | Exact defects, disposition, corrections, and supersession |
| Resulting state | MATERIALIZED ONLY; review, validation, closure, activation, and deployment remain separate |

### 19.2 Later Validation Evidence (`C03-CP-E-013`)

`C03-CP-E-013` requires separately authorized observed identity, retry,
idempotency, timeout, quarantine, revocation, kill, rollback, supersession,
audit-integrity, tamper, release, and empty-write-set scenarios. It is not
created or approximated by this Design or by materialization evidence.

## 20. WP-009 Design Review Questions

| ID | Question |
| --- | --- |
| `C03-WP9-RQ-001` | Are the eight fixed accepted baselines complete and unchanged? |
| `C03-WP9-RQ-002` | Does the Design remain `CAPABILITY_ONLY` and non-executing? |
| `C03-WP9-RQ-003` | Are all ten required recovery-control families covered? |
| `C03-WP9-RQ-004` | Are all ten WP-007 interface references closed and compatible? |
| `C03-WP9-RQ-005` | Is fail-closed entry mandatory before every material action? |
| `C03-WP9-RQ-006` | Is retry finite, eligible-only, scope-locked, deadline-bound, and disabled by default? |
| `C03-WP9-RQ-007` | Does idempotency prohibit duplicate effects and quarantine collisions? |
| `C03-WP9-RQ-008` | Do timeout and late-result paths enter protected states without implied success? |
| `C03-WP9-RQ-009` | Does quarantine exclude protected subjects from all later use pending separate release? |
| `C03-WP9-RQ-010` | Do revocation and kill states take precedence over every recovery path? |
| `C03-WP9-RQ-011` | Is rollback exact-surface, decision-bound, audit-preserving, and activation-neutral? |
| `C03-WP9-RQ-012` | Does supersession make historical identities stale without deleting history? |
| `C03-WP9-RQ-013` | Are audit candidates redacted, append-only, identity-bound, and non-persisting by default? |
| `C03-WP9-RQ-014` | Does every positive release require exact evidence and Project Owner authority? |
| `C03-WP9-RQ-015` | Are all upstream, external-domain, and ACOS write sets empty? |
| `C03-WP9-RQ-016` | Are provider, network, credential, storage, scheduler, queue, and dependency selection prohibited? |
| `C03-WP9-RQ-017` | Are protected-content, prompt, history, payload, credential, and legal-content logs prohibited? |
| `C03-WP9-RQ-018` | Are state transitions finite, guarded, non-skippable, and reason-coded? |
| `C03-WP9-RQ-019` | Are unknown, missing, stale, conflicting, mixed, or unreviewed states fail-closed? |
| `C03-WP9-RQ-020` | Is human review separated from release, activation, invocation, and downstream authority? |
| `C03-WP9-RQ-021` | Does future E-009 record materialization without claiming operational conformance? |
| `C03-WP9-RQ-022` | Is E-013 reserved for separately authorized observed validation? |
| `C03-WP9-RQ-023` | Are Route A, case material, OCR, legal analysis, external contact, Git, and ACOS boundaries preserved? |
| `C03-WP9-RQ-024` | Does the Design create no code, configuration, dependency, fixture, runtime, persistence, or validation result? |

## 21. WP-009 Design Acceptance Gates

| Gate | Requirement |
| --- | --- |
| `C03-WP9-DG-001` — Baseline Integrity | All eight fixed accepted baselines match exact SHA-256 values |
| `C03-WP9-DG-002` — Ordered Dependency | WP-007 Design is adopted and WP-008 remains downstream |
| `C03-WP9-DG-003` — Closed Control Matrix | Ten required control families have finite requirements and protected defaults |
| `C03-WP9-DG-004` — Interface Compatibility | Ten WP-007 recovery/audit references are represented exactly |
| `C03-WP9-DG-005` — Fail-Closed Entry | Missing, invalid, stale, revoked, conflicting, or unreviewed state cannot act |
| `C03-WP9-DG-006` — Retry and Idempotency | Retry is finite and scope-locked; duplicates cannot create duplicate effects |
| `C03-WP9-DG-007` — Timeout and Quarantine | Partial, late, disputed, protected, or tampered paths remain isolated |
| `C03-WP9-DG-008` — Revocation and Kill | Protected authority states take precedence before every material transition |
| `C03-WP9-DG-009` — Rollback and Supersession | Exact restoration and stale-history preservation are mandatory |
| `C03-WP9-DG-010` — Audit Integrity | Redacted append-only candidates preserve exact identities and transitions |
| `C03-WP9-DG-011` — Release Authority | Positive release requires exact evidence and a separate Project Owner decision |
| `C03-WP9-DG-012` — Security and Privacy | Credentials, protected content, unnecessary personal data, and raw payloads are excluded |
| `C03-WP9-DG-013` — Empty Write Sets | Route A, Evidence, matter, legal, human-decision, external-domain, and ACOS writes are empty |
| `C03-WP9-DG-014` — Dependency Isolation | No provider, network, storage, scheduler, queue, credential, or third-party dependency is selected |
| `C03-WP9-DG-015` — Authority Separation | Design, materialization, validation, release, closure, activation, and deployment remain separate |
| `C03-WP9-DG-016` — Evidence Separation | E-009 cannot claim observed conformance and E-013 remains uncreated |
| `C03-WP9-DG-017` — Project Separation | Route A, case materials, OCR, legal analysis, Git, and ACOS remain outside the design surface |
| `C03-WP9-DG-018` — Zero Implementation Pollution | No code, configuration, dependency, fixture, test, runtime, persistence, or validation action occurs |

## 22. Current Evidence and Blocker Ledger

| Item | Current state | Effect |
| --- | --- | --- |
| `C03-CP-E-008` WP-007 Implementation Design | ADOPTED & CLOSED & SHA BOUND | WP-009 design entry gate satisfied |
| `C03-CP-E-012` WP-009 Recovery-Control Matrix Design | MATERIALIZED — REVIEW NOT AUTHORIZED | Design candidate only |
| `C03-CP-E-009` WP-007/WP-009 Materialization Record | NOT CREATED / NOT AUTHORIZED | `AR-B-007` remains open |
| `C03-CP-E-013` Audit/Revocation Validation Record | NOT CREATED / NOT AUTHORIZED | `AR-B-009` remains open |
| `C03-CP-E-010` WP-008 Operational Validation Plan | NOT CREATED / NOT AUTHORIZED | `AR-B-008` remains open |
| `C03-CP-E-011` WP-008 Observed Validation Result | NOT CREATED / NOT AUTHORIZED | `AR-B-008` remains open |

```text
Tier A Design Evidence Created:
2 / 3

Tier A Materialization or Validation Evidence Created:
0 / 3

Tier A Blockers Closed:
0 / 3

Total C03 Blockers Closed:
0 / 10

C03 Activation Readiness:
NOT READY
```

## 23. Explicit Materialization Boundary

| Activity | Status under this authorization |
| --- | --- |
| WP-009 Design document | MATERIALIZED — THIS ASSET ONLY |
| WP-009 Design review or adoption | NOT AUTHORIZED |
| WP-007/WP-009 source, configuration, or control implementation | NOT AUTHORIZED / NOT CREATED |
| `C03-CP-E-009` Materialization Record | NOT AUTHORIZED / NOT CREATED |
| `C03-CP-E-013` Validation Record | NOT AUTHORIZED / NOT CREATED |
| Dependency installation, build, lint, test, runtime, or observed validation | NOT AUTHORIZED / NOT PERFORMED |
| Database, queue, scheduler, storage, retention, deletion, or audit persistence | NOT AUTHORIZED / NOT CREATED |
| Provider, model, network, API, Connector, or MCP | NOT AUTHORIZED / NOT PERFORMED |
| Credential, secret, key, token, endpoint, or private configuration | NOT AUTHORIZED / NOT ACCESSED |
| C03 activation, matter invocation, pilot, deployment, or production | NOT AUTHORIZED |
| Route A, case material, native text, OCR, evidence, or actor access | NOT AUTHORIZED / NOT PERFORMED |
| Legal analysis, advice, filing, strategy, or external contact | NOT AUTHORIZED / NOT PERFORMED |
| ACOS source-project access or modification | NOT AUTHORIZED / NOT PERFORMED |
| Git commit, push, branch, merge, or repository mutation | NOT AUTHORIZED / NOT PERFORMED |

## 24. Required Next Governance State

```text
C03-CP-E-012 WP-009 Recovery-Control Matrix Design:
MATERIALIZED — INTERNAL REVIEW NOT AUTHORIZED

WP-007/WP-009 Joint Materialization:
NOT AUTHORIZED

C03-CP-E-013 Observed Validation Record:
NOT AUTHORIZED / NOT CREATED

Tier A Blockers Closed:
0 / 3

Total C03 Blockers Closed:
0 / 10

C03 Activation Readiness:
NOT READY

Automatic Downstream Transition:
BLOCKED
```

The next eligible action is a separate fixed-SHA Project Owner authorization
for a read-only internal architecture review of this WP-009 Design. Review or
adoption cannot authorize implementation, validation, blocker closure,
activation, invocation, provider access, deployment, ACOS changes, or Git.
