# Phase 2 Route B C03 WP-008 Operational Validation Plan

## 0. Plan Control

| Field | Value |
| --- | --- |
| Evidence class | `C03-CP-E-010` — OPERATIONAL VALIDATION PLAN |
| Work package | `C03-CP-WP-008` — OPERATIONAL VALIDATION |
| Activation planning semantics | `CAPABILITY_ONLY` |
| Authorized output | THIS PLAN DOCUMENT ONLY |
| Plan status | **MATERIALIZED — PLAN REVIEW NOT AUTHORIZED** |
| Validation execution | NOT AUTHORIZED / NOT PERFORMED |
| Fixtures | NOT CREATED / NOT AUTHORIZED |
| Observed validation result | `C03-CP-E-011` — NOT CREATED / NOT AUTHORIZED |
| Audit/revocation validation record | `C03-CP-E-013` — NOT CREATED / NOT AUTHORIZED |
| Tier A blockers closed | `0 / 3` |
| C03 activation readiness | NOT READY |
| Automatic downstream transition | BLOCKED |

This Plan specifies how a later, separately authorized validation could be
performed. It is not a test, fixture, command, observation, validation result,
blocker-closure decision, or activation decision.

## 1. Fixed Governing Baseline

| Baseline | SHA-256 | Recorded state |
| --- | --- | --- |
| WP-007 / WP-009 Materialization Record V3 | `4B67889AF50273EF85B7B18DBDAF3F81339F9310A6B37DEA23D7486879652E31` | ACCEPTED & CLOSED & SHA BOUND |
| Final Internal Materialization Re-Review V3 | `62A5BF7855C27EEEF650DD2F2E3B3D1F83152B635A01031B3A03EDC0BB427788` | PASS — GRADE A; 24 / 24 Questions; 18 / 18 Gates |
| V3 Materialization Acceptance Decision | `798B0868A56723DA2A6FF26B012F4319D7ECFCA3BD7D48DCE1F5980B28A00704` | ACCEPTED & FILED |
| Tier A Platform Capability Sequence | `C748CE0621E254912ED86AE6733F137F5783D6AB5342534F7D283812C634D61A` | ADOPTED BASELINE |
| Activation Prerequisite Closure Plan | `D27B8D6CFF4B4F39B6A34E34D61E691183B12FB03529F6AC665F20A54CA28329` | ADOPTED BASELINE |

Any SHA mismatch, missing baseline, supersession, withdrawal, or unrecorded
change makes this Plan stale and blocks validation preparation and execution.

## 2. Exact Validation Subject

### 2.1 Bound Implementation File Set

| ID | Path | SHA-256 | Planned treatment |
| --- | --- | --- | --- |
| `C03-VS-001` | `scripts/phase2_runtime/__init__.py` | `49B8B1BD319B6424323AD0EDC04B3969D71196CD8D69E12C16D5442B17340844` | Exact identity required |
| `C03-VS-002` | `scripts/phase2_runtime/route_b_c03/__init__.py` | `F669613D65267EC5D4D42CB79008EB510307A99B20E40EE13E9E1E0E404A504D` | Exact identity required |
| `C03-VS-003` | `scripts/phase2_runtime/route_b_c03/contracts.py` | `7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4` | Exact identity required |
| `C03-VS-004` | `scripts/phase2_runtime/route_b_c03/identity_gate.py` | `EA762C13F1DED4ABEAE27D16DD1087901D73E0B6B0A680791E3082AEFFB4D90A` | Exact identity required |
| `C03-VS-005` | `scripts/phase2_runtime/route_b_c03/mapping.py` | `320F7E8576C1C4E81B4E78E6058000E4D720173948BE736AD846B8CAD664EC66` | Exact identity required |
| `C03-VS-006` | `scripts/phase2_runtime/route_b_c03/isolation.py` | `9BC554294D5945188A153F0A5CBEDFAB4E483C95B133683B7517ECC334D4205B` | Exact identity required |
| `C03-VS-007` | `scripts/phase2_runtime/route_b_c03/failures.py` | `6F30D996119F61A19B20208FC44C8AF1FB96ADFE09ADE3538675B9D3F2933734` | Exact identity required |
| `C03-VS-008` | `scripts/phase2_runtime/route_b_c03/audit.py` | `A704BDB22C55C92D0909FA0D6A668D8C149724B2A7627938C301758F1D09F561` | Exact identity required |
| `C03-VS-009` | `scripts/phase2_runtime/route_b_c03/provider_port.py` | `66E4DA862BBBD50380B17686DB6BC2AB6D5D3B861AB53FCDDE1B608F86DEA381` | Exact identity required |
| `C03-VS-010` | `scripts/phase2_runtime/route_b_c03/capability.py` | `028EE9DDD7A2C06840A6F344A4C4CC716EFF95073BE39CA6E57FB7FDBBFA6DD5` | Exact identity required |

### 2.2 Subject Constraints

| Constraint | Required validation-plan assumption |
| --- | --- |
| Default state | Disabled |
| Provider | Null Provider only; no injectable or external provider |
| Dependencies | Python standard library only; no third-party dependency |
| Network | Absent and prohibited |
| Filesystem writes | Absent and prohibited |
| Process or dynamic execution | Absent and prohibited |
| Credentials, secrets, keys, or tokens | Absent and prohibited |
| Upstream and ACOS write sets | Empty and immutable |
| Candidate authority | Human-review pending; downstream blocked |
| Matter authority | Absent; no Tier B packet admitted by this Plan |

No executable, environment, configuration, dependency, or fixture identity is
independently established by this Plan beyond the exact static file identities
recorded above. A later execution authorization must bind all remaining
identities before any observation occurs.

## 3. Validation Environment Contract

| Environment field | Plan requirement | Current state |
| --- | --- | --- |
| Environment identifier | Unique immutable identifier | NOT ASSIGNED |
| Operating-system identity | Exact name, version, architecture, and patch identity | NOT BOUND |
| Python identity | Exact implementation, full version, and executable SHA where available | NOT BOUND |
| Dependency inventory | Complete inventory demonstrating standard-library-only subject | NOT CAPTURED |
| Configuration identity | Exact configuration content and SHA; default disabled | NOT MATERIALIZED |
| Locale and timezone | Explicitly recorded | NOT BOUND |
| Randomness | Deterministic seed or explicit no-randomness declaration | NOT BOUND |
| Clock control | Exact clock source and treatment of time-dependent fields | NOT BOUND |
| Isolation boundary | No network, provider, case repository, ACOS repository, or external service | REQUIRED / NOT OBSERVED |
| Evidence destination | Exact local validation-evidence directory with empty unauthorized write set | NOT AUTHORIZED |

Every `NOT BOUND`, `NOT ASSIGNED`, `NOT CAPTURED`, or `NOT AUTHORIZED` field is
an execution blocker. This Plan does not cure any such field.

## 4. Fixture Contract

### 4.1 Fixture Admission Rules

Future fixtures must be synthetic or public non-case material created or
admitted under a separate exact authorization. Every fixture must have:

- a stable fixture ID, version, SHA-256, origin, and admission decision;
- a declared scenario mapping and expected result;
- no real matter, evidence, protected content, unnecessary personal
  information, credential, secret, key, token, or privileged system material;
- no dependency on Route A, OCR, case files, legal databases, ACOS source, or
  an external provider;
- a documented withdrawal and supersession rule.

### 4.2 Planned Fixture Classes

| Fixture class | Purpose | Current state |
| --- | --- | --- |
| `FX-ID` | Exact and malformed identity inputs | NOT CREATED |
| `FX-AUTH` | Missing, stale, mismatched, and positive authority metadata | NOT CREATED |
| `FX-ISO` | Cross-boundary mismatch metadata | NOT CREATED |
| `FX-DISC` | Prohibited credential/secret-like markers without real secrets | NOT CREATED |
| `FX-IDEM` | Duplicate invocation identities | NOT CREATED |
| `FX-FAIL` | Closed failure-code identities | NOT CREATED |
| `FX-TIME` | Abstract timeout control metadata | NOT CREATED |
| `FX-REVOKE` | Abstract revocation and kill-state metadata | NOT CREATED |
| `FX-ROLLBACK` | Version and supersession metadata | NOT CREATED |
| `FX-INTEGRITY` | Deterministically altered synthetic hashes or audit metadata | NOT CREATED |
| `FX-BOUNDARY` | Upstream/ACOS write attempts and legal-authority misclassification | NOT CREATED |

## 5. Expected Observation Schema

Any later `C03-CP-E-011` result row must contain every field below. The schema
is documentary in this Plan and is not materialized as code or data structure.

| Field | Requirement |
| --- | --- |
| Result row ID | Unique immutable identifier |
| Scenario ID | Exact `C03-TA-V-001` through `C03-TA-V-015` identity |
| Subject manifest SHA | Hash of the exact ten-file subject manifest |
| Environment ID | Exact bound environment identity |
| Fixture ID/version/SHA | Exact admitted fixture identity |
| Authorization reference | Exact validation-execution authorization |
| Expected state | Predeclared protected state |
| Expected output class | Predeclared closed output class |
| Expected reason code | Exact closed reason-code identity or `NONE` |
| Permitted write set | Exact set; normally empty |
| Prohibited effect | Exact effect that must not occur |
| Observed state/output/reason | Reserved for later execution evidence |
| Observed write set | Reserved for later execution evidence |
| Audit-record identity/SHA | Reserved for later execution evidence |
| Start/stop record | Reserved for later execution evidence |
| Executor attestation | Reserved for separately identified executor |
| Reviewer determination | Reserved for independent review |
| Defect reference | Exact defect ID or `NONE` |

An absent mandatory field, unbound identity, free-form substitution, or merged
expected/observed value is a blocking evidence defect.

## 6. Minimum Scenario Matrix

Each row is a future validation contract, not an executed test or observed
result.

| Scenario ID | Planned stimulus | Expected state | Expected output / reason class | Permitted write set | Prohibited effect | Mandatory audit focus | Stop condition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `C03-TA-V-001` | Valid capability metadata without a Tier B packet | `BLOCKED` | Invocation rejection; missing matter-bound authority | Empty | Matter access or candidate output | Identity, authority reference, denial reason, empty write set | Any matter access, output candidate, or non-empty write |
| `C03-TA-V-002` | Missing or malformed authority identity | `BLOCKED` | Closed authority/identity failure | Empty | Default inference, fallback, or partial execution | Exact malformed field, failure code, denial, empty write set | Acceptance of missing/malformed authority or incomplete audit |
| `C03-TA-V-003` | Stale SHA, version, configuration, or authority reference | `BLOCKED / STALE` | Staleness or exact-identity mismatch | Empty | Historical fallback or silent substitution | Expected/received identities, mismatch, denial | Historical asset use or state advancement |
| `C03-TA-V-004` | Cross-matter, cross-project, cross-session, or cross-provider mismatch | `BLOCKED / ISOLATED` | Boundary mismatch | Empty | Cross-boundary disclosure or state reuse | All boundary identifiers, mismatch class, isolation response | Any information or state crossing the declared boundary |
| `C03-TA-V-005` | Synthetic credential-, secret-, key-, or token-like marker presented as content | `BLOCKED / QUARANTINED` | Prohibited-content classification without content disclosure | Empty | Logging, echoing, mapping, or forwarding the marker value | Classification only, redacted trace, quarantine/denial | Raw marker disclosure or persistence |
| `C03-TA-V-006` | Repeated identical invocation identity | `BLOCKED` or one separately permitted single effect | Idempotency or duplicate denial | Empty under this capability-only Plan | Duplicate effect or overwritten audit history | Invocation ID, first/duplicate relation, effect count, audit continuity | More than one effect or ambiguous duplicate disposition |
| `C03-TA-V-007` | Closed `TRANSIENT_FAILURE` identity and exact retry-policy reference | `RETRY_ELIGIBILITY_PENDING` | Eligibility only; execution remains unauthorized | Empty | Automatic retry, scope broadening, or duplicate effect | FailureCode identity, policy identity, eligibility result | Any retry execution or acceptance of raw/unknown failure input |
| `C03-TA-V-008` | Abstract timeout condition under a future bound clock | Protected terminal state | Timeout denial/termination class | Empty | Continued work after timeout or incomplete audit chain | Clock identity, timeout reference, terminal state, continuity | Post-timeout state change or missing terminal record |
| `C03-TA-V-009` | Revocation state before or during an abstract operation boundary | `BLOCKED / REVOKED` | Revocation denial | Empty | Further action beyond accepted propagation boundary | Revocation reference, observation boundary, denial point | Any action after the accepted revocation boundary |
| `C03-TA-V-010` | Kill switch active | `BLOCKED / KILL_ACTIVE` | Kill-state denial | Empty | Self-release, implicit recovery, or continued operation | Kill reference, entry state, continued block, release absence | State release without separate authority |
| `C03-TA-V-011` | Abstract rollback/supersession metadata | Prior accepted version nominated; execution not performed | Rollback eligibility/reference result | Empty | Audit-history rewrite or unbound version restoration | Current/prior identities, authority reference, immutable history | Unbound version selection or altered historical record |
| `C03-TA-V-012` | Deterministically tampered synthetic identity, output hash, dependency identity, or audit reference | `BLOCKED / QUARANTINED` | Integrity failure | Empty | Use, release, or silent repair of affected path | Expected/observed hashes, tamper class, quarantine | Affected path proceeds or tamper evidence is lost |
| `C03-TA-V-013` | Null Provider or required dependency unavailable | `BLOCKED` | Dependency/provider unavailable | Empty | Silent provider substitution, network route, or degraded bypass | Exact provider/dependency identity, unavailability, denial | External route, fallback, or partial output |
| `C03-TA-V-014` | Attempted upstream-repository or independent-ACOS write request | `BLOCKED` | Prohibited write-target classification | Empty | Any upstream or ACOS mutation | Requested target class, denial, verified empty prohibited write set | Any write, staging, commit, branch, push, or remote action |
| `C03-TA-V-015` | Candidate labeled as legal advice, accepted fact, or downstream authority | `HUMAN_REVIEW_PENDING / DOWNSTREAM_BLOCKED` | Classification-boundary denial | Candidate-record creation only if separately authorized; otherwise empty | Legal conclusion, automatic acceptance, or downstream use | Candidate notices, human-gate state, downstream block | Missing notice, bypassed human gate, or downstream transition |

## 7. Evidence Capture and Reproducibility Contract

| Control | Required future evidence |
| --- | --- |
| Subject integrity | Ten-file manifest, SHA calculation method, and mismatch disposition |
| Environment integrity | Immutable environment manifest and tool versions |
| Fixture integrity | Fixture manifest, admission basis, SHA, and no-real-matter declaration |
| Ordering | Exact scenario order and isolated rerun identity |
| Determinism | Seed or no-randomness declaration; clock treatment |
| Input capture | Exact synthetic input or its complete canonical representation |
| Output capture | Exact output/state/reason representation without prohibited content |
| Write-set capture | Declared and observed permitted/prohibited write sets |
| Audit capture | Immutable audit-record identity, SHA, continuity, and access boundary |
| Defect capture | Defect ID, severity, impacted rows, disposition, and supersession |
| Rerun | New run identity linked to superseded result; no historical overwrite |

No command, evidence directory, logging mechanism, or capture tool is selected
or authorized by this Plan.

## 8. Reviewer Independence and Decision Separation

| Role | Permitted future responsibility | Prohibited combination |
| --- | --- | --- |
| Plan author | Define closed scenarios and evidence requirements | Cannot approve own Plan |
| Fixture preparer | Prepare separately authorized synthetic/public fixtures | Cannot admit own fixture or judge own result |
| Validation executor | Execute only an exact later authorization | Cannot review or accept own result |
| Implementation author | Explain subject behavior and resolve authorized defects | Cannot be sole validation reviewer |
| Independent reviewer | Review exact evidence against this adopted Plan | Cannot act as Project Owner |
| Project Owner | Sole positive authority for Plan adoption, execution, result acceptance, blocker closure, and activation | Not an automated reviewer class |

Role identity, provider identity, conflicts, and separation must be recorded
before validation execution. Missing or merged roles block execution.

## 9. Defect and Stop-Control Model

### 9.1 Planned Defect Classes

| Class | Blocking rule |
| --- | --- |
| Identity mismatch | Always blocking |
| Authority mismatch or absence | Always blocking |
| Real-matter or protected-content exposure | Always blocking; quarantine and withdrawal required |
| Non-empty unauthorized write set | Always blocking |
| External dependency/provider/network access | Always blocking unless separately fixed and authorized; none is currently permitted |
| Expected/observed mismatch | Blocking until exact disposition and authorized rerun |
| Unrepeatable result | Blocking |
| Missing or discontinuous audit evidence | Blocking |
| Reviewer-independence conflict | Blocking |
| Formatting defect with no evidentiary effect | Non-blocking only after explicit review determination |

### 9.2 Immediate Stop Conditions

Future execution must stop immediately if any of the following occurs:

1. a baseline, implementation, environment, configuration, dependency, or
   fixture identity is missing, stale, or mismatched;
2. real matter, case evidence, protected content, credentials, secrets, keys,
   tokens, or unnecessary personal information appears;
3. a network, provider, external service, Route A, OCR, case repository, ACOS
   source repository, Git remote, or other non-authorized path is reached;
4. an unauthorized write, retry, fallback, substitution, release, or downstream
   transition is attempted;
5. audit continuity, evidence capture, determinism, or role independence cannot
   be established;
6. a critical mismatch or unresolved blocking defect exists;
7. kill, revocation, withdrawal, or supersession state becomes active.

Stopping does not authorize cleanup, rerun, repair, rollback, or evidence
acceptance. Each requires the applicable separate authority.

## 10. Withdrawal, Staleness, and Revalidation

This Plan becomes stale and unusable for execution upon any change to:

- a bound baseline, implementation file, contract, control matrix, or SHA;
- provider, dependency, Python, operating system, configuration, isolation, or
  environment identity;
- an admitted fixture or expected-result definition;
- authorization, revocation, kill, withdrawal, or supersession state;
- evidence schema, capture method, reviewer identity, or independence record.

A stale Plan cannot be patched by an execution record. It requires a new
fixed-SHA Plan disposition and, where necessary, a revised Plan review and
adoption decision.

## 11. Plan Review Questions

| ID | Question |
| --- | --- |
| `C03-WP008-RQ-001` | Does the Plan bind the accepted V3 materialization, final re-review, and acceptance decision by exact SHA? |
| `C03-WP008-RQ-002` | Does the Plan bind exactly ten implementation files and their full SHA-256 values? |
| `C03-WP008-RQ-003` | Is `CAPABILITY_ONLY` preserved without matter, provider, runtime, or activation authority? |
| `C03-WP008-RQ-004` | Are every unbound environment and execution identity explicitly treated as a blocker? |
| `C03-WP008-RQ-005` | Are fixtures restricted to separately authorized synthetic or public non-case material? |
| `C03-WP008-RQ-006` | Are real matter, evidence, protected content, credentials, secrets, keys, and tokens excluded? |
| `C03-WP008-RQ-007` | Are all 15 mandatory scenario IDs present exactly once? |
| `C03-WP008-RQ-008` | Does each scenario specify a stimulus, expected state, output/reason class, write set, prohibited effect, audit focus, and stop condition? |
| `C03-WP008-RQ-009` | Does identity validation fail closed on missing, malformed, stale, or mismatched values? |
| `C03-WP008-RQ-010` | Are cross-matter, project, session, and provider boundaries isolated? |
| `C03-WP008-RQ-011` | Are disclosure and credential-like inputs rejected or quarantined without raw-value logging? |
| `C03-WP008-RQ-012` | Are duplicate invocation and idempotency effects bounded? |
| `C03-WP008-RQ-013` | Is retry limited to eligibility planning without retry execution? |
| `C03-WP008-RQ-014` | Are timeout, quarantine, revocation, and kill states fail-closed? |
| `C03-WP008-RQ-015` | Are rollback and supersession separated from audit-history preservation? |
| `C03-WP008-RQ-016` | Are tamper, unavailable dependency, and silent-substitution paths blocked? |
| `C03-WP008-RQ-017` | Is the upstream and ACOS prohibited write set required to remain empty? |
| `C03-WP008-RQ-018` | Is legal-advice/downstream-authority misclassification blocked by a human gate? |
| `C03-WP008-RQ-019` | Does the planned evidence schema keep expected values separate from observations? |
| `C03-WP008-RQ-020` | Are reproducibility, integrity, ordering, rerun, and supersession requirements explicit? |
| `C03-WP008-RQ-021` | Are author, fixture, executor, reviewer, implementation, and Project Owner roles separated? |
| `C03-WP008-RQ-022` | Are blocking defect classes and immediate stop conditions complete? |
| `C03-WP008-RQ-023` | Are withdrawal, staleness, and revalidation triggers explicit? |
| `C03-WP008-RQ-024` | Does the Plan avoid tests, commands, fixtures, observations, result claims, blocker closure, activation, ACOS changes, and Git operations? |

## 12. Plan Acceptance Gates

| ID | Gate |
| --- | --- |
| `C03-WP008-G-001` | Fixed governing lineage is complete and exact |
| `C03-WP008-G-002` | Ten-file subject manifest is complete and exact |
| `C03-WP008-G-003` | Capability-only and disabled-default boundaries are preserved |
| `C03-WP008-G-004` | Environment identities are mandatory and currently unbound fields remain blockers |
| `C03-WP008-G-005` | Fixture boundary excludes real matter and protected content |
| `C03-WP008-G-006` | Scenario coverage is 15 / 15 with no missing or duplicate ID |
| `C03-WP008-G-007` | Exact expected-state and prohibited-effect semantics are present |
| `C03-WP008-G-008` | Unauthorized write sets remain empty |
| `C03-WP008-G-009` | Identity, authority, staleness, and isolation cases fail closed |
| `C03-WP008-G-010` | Failure, retry, idempotency, timeout, and quarantine cases are bounded |
| `C03-WP008-G-011` | Revocation, kill, rollback, supersession, and integrity cases are bounded |
| `C03-WP008-G-012` | Provider, dependency, network, upstream, and ACOS paths remain prohibited |
| `C03-WP008-G-013` | Candidate output remains human-review pending and downstream blocked |
| `C03-WP008-G-014` | Evidence schema and reproducibility contract are complete |
| `C03-WP008-G-015` | Reviewer independence and sole positive authority are preserved |
| `C03-WP008-G-016` | Defect, stop, withdrawal, staleness, and revalidation controls are complete |
| `C03-WP008-G-017` | No execution evidence, fixture, test, command, or observation is created |
| `C03-WP008-G-018` | No activation, blocker closure, Route A, OCR, case, legal, ACOS, or Git authority is implied |

## 13. Resulting Governance State

```text
C03-CP-E-010 Operational Validation Plan:
MATERIALIZED — PLAN REVIEW NOT AUTHORIZED

C03-CP-E-011 Observed Validation Result:
NOT CREATED / NOT AUTHORIZED

C03-CP-E-013 Audit/Revocation Validation Record:
NOT CREATED / NOT AUTHORIZED

Fixtures / Tests / Commands / Execution / Runtime Observation:
NOT CREATED / NOT AUTHORIZED / NOT PERFORMED

AR-B-007 / AR-B-008 / AR-B-009 Closure:
NOT AUTHORIZED / NOT ESTABLISHED

Tier A Blockers Closed:
0 / 3

C03 Activation Readiness:
NOT READY

Automatic Downstream Transition:
BLOCKED
```

The next permissible governance action is a separate fixed-SHA internal review
authorization for this Plan. Plan adoption, fixture preparation, validation
execution, result review, blocker closure, readiness review, and activation are
all separate later decisions.
