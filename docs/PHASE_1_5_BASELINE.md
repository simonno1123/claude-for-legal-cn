# Phase 1.5 Release Candidate Baseline

Status: `RC DOCUMENTED / ENGINEERING PASS / GIT FREEZE PENDING`

Review date: 2026-07-15

Project: `claude-for-legal-cn`

Branch at review: `feature/matter-workspace`

HEAD at review: `b68191b`

## 1. Baseline Decision

Phase 1.5 has an engineering-complete Release Candidate for the local,
human-reviewed legal workflow foundation. The accepted dependency direction is:

```text
Matter
  +-- Evidence
  +-- Issue
        +-- Research
              +-- Strategy
                    +-- Drafting
```

The current working tree is not an immutable Git baseline. TASK_022 through
TASK_025 assets remain uncommitted, and TASK_027 Phase 2 files are also present
in the same working tree. A dedicated commit and optional tag are required
before declaring `PHASE_1_5_GIT_FREEZE`.

```text
PHASE_1_5_RC_DOCUMENTED = YES
PHASE_1_5_ENGINEERING_VALIDATION = PASS
PHASE_1_5_REAL_CASE_TECHNICAL_VALIDATION = CONDITIONAL_PASS
PHASE_1_5_GIT_FREEZE = PENDING
PHASE_1_5_FINAL_ACCEPTANCE = PENDING_LAWYER_REVIEW
```

## 2. Scope

The baseline contains two compatible layers:

1. Module-local workflow state from `3b45e30`, including the shared local
   workflow contract, five stateful module workspaces, Product launch tracking
   and Commercial workflow persistence.
2. The cross-workflow foundation from TASK_021 through TASK_026: Matter,
   Evidence, Research, Strategy, Drafting and isolated real-case validation.

The following TASK_027 Phase 2 assets are expressly outside this baseline:

- `core/evidence-intelligence/`
- `tests/matter-workspace/test_evidence_intelligence.py`

No real-case material or case-derived working record is part of this repository
baseline.

## 3. Asset Map

### 3.1 Module-Local Workflow Layer

| Capability | Baseline assets |
|---|---|
| Shared lifecycle and storage contract | `references/local-workflow-contract.md` |
| Stateful Matter Workspace | `commercial-legal`, `employment-legal`, `ip-legal`, `privacy-legal`, and `product-legal` Matter Workspace Skills |
| Product launch state | `product-legal/skills/launch-tracker/` and `product-legal/agents/launch-watcher.md` |
| Commercial state | Matter Workspace, renewal tracker, review proposals, playbook monitor, renewal watcher and deal debrief assets |
| Regression routing | `scripts/localization-regression.py` |

### 3.2 Cross-Workflow Foundation

| Layer | Schemas | Templates / examples | Documentation | Validator | Tests |
|---|---:|---:|---:|---:|---:|
| Matter Workspace | 8 | 26 templates, 9 sample records | 1 validation guide | 1 core validator | 13 |
| Evidence Workflow and Validation | included in Matter Schema count | 19 Evidence templates | 2 workflow/validation guides | 1 Evidence validator | 9 |
| Legal Research | 3 | 3 examples | 1 workflow guide | 1 | 7 |
| Legal Strategy | 3 | 7 examples | 1 workflow guide | 1 | 7 |
| Legal Drafting | 3 | 5 examples | 1 workflow guide | 1 | 8 |
| **Total** | **17** | **26 templates, 24 examples** | **6 guides** | **5** | **44** |

Primary paths:

- `core/matter-workspace/`
- `core/legal-research/`
- `core/legal-strategy/`
- `core/legal-drafting/`
- `tests/matter-workspace/`

### 3.3 Real-Case Validation Evidence

TASK_026 validation evidence remains outside the product repository. The
sanitized ACOS result is
`TASK_026-B_REAL_CASE_VALIDATION_EXECUTION_VALIDATION_RESULT.md`. It records
structural validation only and contains no party identity, document text or
legal conclusion.

## 4. Dependency Review

| Consumer | Required upstream records | Boundary |
|---|---|---|
| Evidence | Matter, Fact and Issue references | Evidence review does not establish a Fact automatically |
| Research | Matter and Issue references; verified source records | Unverified sources cannot become approved rules |
| Strategy | Matter, Issue and Research references | Options and recommendations remain human-selected |
| Drafting | Matter, Issue, Research and Strategy references; Evidence/Fact source trace | No final document exists without legal review and approval |

The Schema references and validators flow downstream only. Matter Workspace
does not import Research, Strategy or Drafting Schemas, and Research does not
import Strategy or Drafting. No circular Schema dependency was found.

Responsibility overlap is intentional only at control points:

- each layer records its own lifecycle state;
- each layer preserves a Human Review gate;
- cross-layer IDs provide provenance without copying upstream conclusions.

## 5. Validation Baseline

The following checks were rerun on 2026-07-15. TASK_027 tests were excluded
from the Phase 1.5-only count.

| Check | Result |
|---|---|
| Phase 1.5 unit and integration tests | `44/44 PASS` |
| Matter Workspace core validator | PASS: 8 Schemas, 26 templates, 9 sample records, 31 sample references |
| Evidence template validator | PASS with four expected incomplete-template warnings requiring human completion |
| Legal Research validator | PASS: 3 Schemas, 3 examples, 12 cross references |
| Legal Strategy validator | PASS: 3 Schemas, 7 examples, 44 cross references |
| Legal Drafting validator | PASS: 3 Schemas, 5 examples, 32 cross references |
| China localization regression | PASS |

TASK_026-B technical validation recorded PASS for Matter, Evidence, Issue,
Research, Strategy and Drafting. Data isolation, inventory, structural
integrity, referential integrity, no-silent-supplementation, human review,
traceability and operational safety gates passed. Provenance was `PARTIAL`
because source authenticity and primary legal authority remained unverified.
Final practical acceptance remains subject to Lawyer Owner review.

## 6. Human Review Boundary

The baseline does not authorize autonomous legal work. It requires:

- explicit Evidence review before verification;
- source verification before an approved Research position;
- human selection and approval before a Strategy recommendation;
- legal review, revision and approval before Draft archival or use;
- no silent supplementation of missing facts, authorities or case material.

Structural validation proves format and traceability, not truth, evidentiary
weight, legal correctness, outcome probability or filing readiness.

## 7. Known Limitations Register

| Limitation | Frozen status | Future boundary |
|---|---|---|
| Material intake and content structuring | Manual | Phase 2 may define separately authorized extraction capabilities |
| OCR and scan-only document extraction | Not implemented | Phase 2 |
| External legal databases and current-authority retrieval | Not connected | Phase 2 |
| MCP and external provider integrations | Not connected | Phase 2 |
| Agent orchestration and LLM call chains | Not implemented | Separate future authorization |
| Isolated real-case workspace validator command | No reusable product command | Future engineering task; case data must remain outside Git |
| Matter root navigation to every downstream record | IDs resolve, but navigation is not exhaustive | Operational-depth enhancement |
| Professional acceptance of CASE-001 | Pending Lawyer Owner | Required before claiming practical acceptance |

These are declared limitations, not hidden Phase 1.5 capabilities.

## 8. Freeze Requirements

A later commit task may declare the immutable Phase 1.5 baseline only after:

1. staging only Phase 1.5 assets and these closure documents;
2. excluding TASK_027 and all other Phase 2 files from that commit;
3. rerunning the 44 Phase 1.5 tests and localization regression on the exact
   staged tree;
4. recording the resulting commit hash and, if approved, a release tag;
5. preserving the conditional real-case and Lawyer Owner review status.

Until then, this document is the Release Candidate definition, not proof of a
clean or immutable Git release.
