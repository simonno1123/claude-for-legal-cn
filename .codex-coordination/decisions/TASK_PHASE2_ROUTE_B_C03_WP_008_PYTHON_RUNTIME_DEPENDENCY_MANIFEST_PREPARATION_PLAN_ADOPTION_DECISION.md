# Project Owner Route B C03 WP-008 Runtime Dependency Manifest Preparation Plan Adoption Decision

## 0. Decision Control

| Field | Value |
| --- | --- |
| Adopted asset | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN.md` |
| Bound Plan SHA-256 | `8C23436CD6CD7ADE9FFC30C44241D1D944A203AC00F0605B366B9F1658BBC239` |
| Bound internal review | `.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVIEW.md` |
| Bound internal review SHA-256 | `64AFB34D60B3C1C7FAD798AD2C226128C87D8C15BE33A4DA90E20F8149B85AEA` |
| Review authorization SHA-256 | `664630B60EBAB9C2DCFFE7F72544A3004E216A399F00CF15FD57D3A6E0E4AB83` |
| Review outcome | `PASS — GRADE A` |
| Review coverage | `20 / 20 Questions; 16 / 16 Gates` |
| Design defects | `0 blocking / 0 non-blocking` |
| Recorded limitations | `1 non-blocking` |
| Decision authority | `Project Owner — SOLE POSITIVE AUTHORITY` |
| Decision source | `CONVERSATION-LEVEL PROJECT OWNER ACCEPTANCE` |
| Decision | **ADOPTED & CLOSED & SHA BOUND** |

## 1. Adoption Decision

The Project Owner adopts the exact fixed-SHA Python Runtime Dependency
Manifest Preparation Plan identified above. The Plan is the governing design
for sequencing, generating, reviewing, accepting, and invalidating the future
exact Manifest candidate.

Adoption accepts only the preparation design. It does not establish a harness
SHA, harness import set, runtime dependency closure, Manifest entry, aggregate
SHA, Manifest file SHA, network isolation, execution authority, validation
result, or activation condition.

## 2. Adopted Sequencing

| Order | Required separately governed action | Current state |
| ---: | --- | --- |
| 1 | Materialize, review, and accept the exact harness source without executing it | NOT AUTHORIZED |
| 2 | Authorize deterministic Manifest generation against the accepted harness, subjects, and environment | NOT AUTHORIZED |
| 3 | Materialize the final Manifest candidate and calculate its file SHA | NOT AUTHORIZED |
| 4 | Independently review import, bootstrap, PE, OS, data, exclusion, and aggregate closure | NOT AUTHORIZED |
| 5 | Project Owner accepts or rejects the exact Manifest SHA | NOT AUTHORIZED |
| 6 | Continue to separately governed network-attestation and execution prerequisites | BLOCKED |

No stage follows automatically. A current runtime-tree enumeration, wildcard,
placeholder, inferred harness import, or previous observation cannot substitute
for an exact accepted harness-dependent closure.

## 3. Adopted Manifest Boundaries

| Boundary | Adopted state |
| --- | --- |
| Root model | `PROJECT_ROOT`, `VENV_ROOT`, `RUNTIME_ROOT`, and `SYSTEM_ROOT` with accepted resolution |
| Path model | Root-token plus exact normalized relative path; no free resolution |
| Entry model | Explicit fixed file identity, bytes, SHA, role, provenance, loader, phase, and capability fields |
| Import model | Harness, subject, recursive standard-library, built-in, frozen, extension, data, and denied sets separated |
| Binary model | CPython bootstrap, extension PE, runtime-owned DLL, and OS DLL closure required |
| Exclusions | `site-packages`, dynamic imports, denied capability modules, installers, tests, bytecode, cache, metadata, and unused assets denied by default |
| Generation | Deterministic, static, non-importing, non-executing, and no-overwrite |
| Canonical identity | Canonical entry stream, aggregate SHA, canonical JSON, and external Manifest file SHA |
| Governance | Independent review and Project Owner acceptance required; any identity change makes the Manifest stale |

## 4. Preserved Limitation

| Limitation ID | Record | Disposition |
| --- | --- | --- |
| `C03-WP008-RDM-L-001` | Shared base runtime gained one 2,238-byte `.pyc` cache file after Plan materialization | NON-BLOCKING / BYTECODE AND CACHE REMAIN EXCLUDED / FINAL GENERATOR MUST RECALCULATE |

The limitation demonstrates runtime-tree volatility. It grants no read
authority and cannot be copied into the future Manifest.

## 5. Explicitly Not Authorized or Established

| Subject | State |
| --- | --- |
| Harness source materialization | NOT AUTHORIZED / NOT CREATED |
| Harness review or acceptance | NOT AUTHORIZED / NOT ESTABLISHED |
| Final `PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json` creation | NOT AUTHORIZED / PRECONDITION BLOCKED |
| Manifest generator, runtime probe, or process-module observation | NOT AUTHORIZED |
| Network-isolation attestation | NOT AUTHORIZED / NOT CREATED |
| Python, module, DLL, fixture, subject, or harness execution/import | NOT AUTHORIZED |
| Evidence directory, `E-011`, or `E-013` creation | NOT AUTHORIZED / NOT CREATED |
| Operational conformance or Tier A blocker closure | NOT ESTABLISHED / `0 / 3` |
| C03 readiness, activation, pilot, deployment, or production | NOT AUTHORIZED / NOT READY |
| Route A, OCR, case, legal, matter, or evidence activity | NOT AUTHORIZED |
| Provider, model, network, API, Connector, or MCP invocation | NOT AUTHORIZED |
| Independent ACOS project access or modification | NOT AUTHORIZED |
| Git commit, push, branch, merge, or remote action | NOT AUTHORIZED |

## 6. Resulting Governance State

```text
Python Runtime Dependency Manifest Preparation Plan:
ADOPTED & CLOSED & SHA BOUND

Internal Review:
PASS — GRADE A

Final PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json:
NOT CREATED / PRECONDITION BLOCKED

Accepted Harness / Harness Import Set:
NOT CREATED / NOT ESTABLISHED

Manifest Generation / Review / Acceptance:
NOT AUTHORIZED / NOT ESTABLISHED

Validation Execution / Evidence / E-011 / E-013:
NOT AUTHORIZED / NOT CREATED

Operational Tier A Blockers Closed:
0 / 3

C03 Activation Readiness:
NOT READY

Automatic Downstream Transition:
BLOCKED
```

## 7. Project Owner Confirmation

```text
Project Owner Decision:
ACCEPTED, ADOPTED & FILED

Signature Basis:
CONVERSATION-LEVEL PROJECT OWNER CONFIRMATION
```

The next permissible action is a separate exact-scope Project Owner
authorization for document/code materialization of the future harness source
without executing it. This adoption does not authorize that action.
