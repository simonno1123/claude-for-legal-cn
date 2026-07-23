# TASK_PHASE2_C01_II_IMPLEMENTATION_HANDOFF

## Identity

| Item | Value |
|---|---|
| Status | **Draft Completed — Pending Architecture Review and Project Owner Decision** |
| Type | Phase 2 Track C — Implementation Authorization Request |
| Governance layer | Planning / Authorization |
| Architecture coordinator | ChatGPT |
| Materialization executor | Codex |
| Future execution recipient | Codex |
| Current implementation authorization | **None** |
| Current code / Skill / Agent authorization | **None** |
| Draft creation date | 2026-07-18 |

This Handoff is an authorization-request artifact. It is not an Implementation
Task, an implementation approval or permission to modify `litigation-legal`.

The creation of this Draft changes no engineering authorization state.

## 1. Coordination Authority and Workflow

This Handoff materializes the Architecture Coordinator's C01-II Handoff Design
Request under the following collaboration boundary:

```text
ChatGPT / Architecture Coordination
        ↓
C01-II Handoff Design Request
        ↓
Codex repository materialization
        ↓
TASK_PHASE2_C01_II_IMPLEMENTATION_HANDOFF.md
        ↓
ChatGPT Architecture Review
        ↓
Project Owner Decision
        ↓
If specifically approved: C01-II-A documentation-only planning
        ↓
Separate review and Project Owner implementation decision
        ↓
Only then may C01-II-B implementation be considered
```

External models may provide advisory analysis only. They do not have repository
execution authority, final review authority or Project Owner decision authority.

## 2. Fixed Input Identity

Before reviewing or executing any phase described by this Handoff, the following
canonical inputs must be present in the target repository and must match exactly.

| Input | Canonical path | Required SHA-256 / state |
|---|---|---|
| C01 v0.2 reviewed design baseline | `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md` | `67C74A63EE0BCCB4B20A9035467A16CF2B43EFD624E45C2B501A60A8590ED6E5` |
| Approved C01-I Implementation Design Specification | `docs/phase2/track-c/TASK_PHASE2_C01_IMPLEMENTATION_DESIGN_SPEC.md` | `0274AB2C7542083BFBDFF98F00E7143F7D45927EEEED5675BF28BF6631A862C7` |
| C01-I Specification Review | `.codex-coordination/reviews/TASK_PHASE2_C01_I_SPEC_REVIEW.md` | PASS; `C4EE86A9FB5D37CC4E6CA69E8CECC6C1AC1B47E0012546C6F4F6699B4EC19C98` |
| C01-I Project Owner Decision | `.codex-coordination/decisions/TASK_PHASE2_C01_I_SPEC_DECISION.md` | ACCEPTED; `113837F4EB4AA3E76020FAAFE6EC08C3DA5C141EF5204D6849CFECE86CA7DF65` |
| Phase 2 Architecture Decision | `.codex-coordination/decisions/TASK_PHASE2_000_ARCHITECTURE_ALIGNMENT_ACCEPTANCE_RETRY_1_DECISION.md` | ACCEPTED; `C5457DAB074CCF3F49C8D8D8A9530FA98366E2581BF9CBBA528261084870833C` |

The canonical repository is:

```text
C:\Users\Administrator\Documents\Codex\2026-07-17\
referenced-chatgpt-conversation-this-is-untrusted\work\claude-for-legal-cn
```

Similarly named artifacts in the separate `2026-06-19\ni` workspace are not
valid substitutes for these fixed inputs.

Hash mismatch, missing input, ambiguous identity or a non-ACCEPTED governing
decision must return `BLOCKED`. Codex must not reconstruct, infer or replace a
fixed input from chat summaries or another workspace.

## 3. Objective

Prepare a controlled authorization path from the approved C01 legal-methodology
design and C01-I engineering mapping to a possible future enhancement of the
existing `litigation-legal` architecture.

The authorized transition requested by this Handoff is limited to:

```text
Approved Legal Methodology and Engineering Mapping
        ↓
Path-Specific Skill Design Mapping
        ↓
Architecture Review and Project Owner Decision
```

It does not authorize the transition from design to implementation.

## 4. C01-II Phase Model

### 4.1 C01-II-A — Skill Design Mapping

Status requested after Handoff approval: **AUTHORIZED FOR DOCUMENTATION-ONLY
PLANNING**.

C01-II-A may:

- inspect existing `litigation-legal` Skills, Agent boundaries, matter workspace
  conventions and workflow entry points;
- select candidate existing assets from the approved C01-I change-point register;
- propose a canonical ownership map for Matter, Issue / Question, Claim, Request
  Right, Element, Legal Fact, Proof, Evidence, Defense / Rebuttal and Human Review;
- identify exact future Skill, Agent or documentation paths that C01-II-B might
  request permission to modify;
- describe proposed interactions, field responsibilities, sequencing, migration
  concerns, professional gates and deterministic validation requirements;
- record unresolved architecture decisions rather than inventing new components;
- produce only the documentation artifacts listed in Section 8.

C01-II-A must not modify any current Skill, Agent, workflow, schema, prompt,
runtime file, matter data or D1-D6 artifact.

### 4.2 C01-II-B — Skill / Agent Modification

Status: **NOT AUTHORIZED**.

This future phase may be considered only after C01-II-A is completed, reviewed
and accepted. It requires a separate Project Owner-approved Implementation Task
that names exact files, allowed edits, acceptance criteria, validation methods
and rollback boundaries.

No C01-II-B action is authorized by approval of this Handoff.

### 4.3 C01-II-C — Validation

Status: **NOT AUTHORIZED**.

This future phase requires separately approved implementation artifacts,
test scope, validation cases, human-review criteria and an explicit execution
authorization. Existing China-law regression scenarios are inputs for later
planning only and must not be represented as an approved C01 validation protocol.

## 5. Candidate Future Implementation Scope

The following scope describes what a later C01-II-B authorization request may
consider. It is not current permission to change these assets.

### 5.1 Existing Skill Enhancement

Future consideration must remain inside existing canonical Skills under
`litigation-legal/skills/`, with priority given to the smallest path set capable
of supporting the approved design. Candidate responsibilities identified by
C01-I include:

| Candidate existing asset | Possible future responsibility | Current state |
|---|---|---|
| `skills/matter-workspace/SKILL.md` | Stable Matter context and reviewed analysis references | NO CHANGE AUTHORIZED |
| `skills/matter-intake/SKILL.md` | Candidate Issue / Question, Claim, Request Right, facts and gaps initialization | NO CHANGE AUTHORIZED |
| `skills/chronology/SKILL.md` | Source-bound event and Legal Fact candidate references | NO CHANGE AUTHORIZED |
| `skills/claim-chart/SKILL.md` | Candidate central mapping for Request Right, Element, Proof, Evidence and Defense / Rebuttal | NO CHANGE AUTHORIZED |
| `skills/matter-briefing/SKILL.md` | Presentation of human-reviewed mappings and unresolved gaps | NO CHANGE AUTHORIZED |
| `skills/brief-section-drafter/SKILL.md` | Consumption of approved facts, evidence and authority only | NO CHANGE AUTHORIZED |
| `skills/matter-update/SKILL.md` | Append-only invalidation or reopening signals when facts/evidence change | NO CHANGE AUTHORIZED |
| Evidence-related canonical Skills | Preservation and confidentiality safeguards for reviewed Evidence references | NO CHANGE AUTHORIZED |
| `skills/witness-trial-prep/SKILL.md` | Consumption of reviewed proof subjects and Evidence links | NO CHANGE AUTHORIZED |

Compatibility aliases remain routing shims and may not acquire independent C01
methodology ownership.

### 5.2 Existing Agent Enhancement

Future consideration may assess `litigation-legal/agents/docket-watcher.md` only
as an adjacent supplier of candidate procedural facts and deadlines.

Any Agent modification requires a separate, express Agent authorization. An
Agent must not infer final Claims, Elements, burdens, outcomes or strategy, and
must not take consequential external action.

### 5.3 Existing Workflow Integration

A future request may consider narrow integration among existing assets:

```text
matter-workspace
        ↓
matter-intake
        ↓
chronology / claim-chart
        ↓
matter-briefing / brief-section-drafter
        ↓
qualified human review
```

No new global orchestrator, parallel methodology layer or cross-plugin reasoning
service may be inferred from this candidate flow.

## 6. Implementation Exclusions

This Handoff and C01-II-A prohibit:

- a Global Legal Reasoning Core;
- a new methodology framework or parallel `methodology/` or
  `legal-reasoning-core/` tree;
- a new database, knowledge graph, matter graph or shared runtime object;
- MCP, connector or external-provider modification;
- automatic legal opinions, adjudication prediction or outcome prediction;
- automatic claim selection, filing choice or litigation strategy;
- runtime schema, MCP schema or workflow schema modification;
- creation or modification of D1-D6;
- changes to Phase 2 Architecture, `PROJECT_SCOPE.md` or
  `PHASE_2_ROADMAP.md`;
- changes outside the existing `litigation-legal` ownership boundary;
- code, Skill, Agent, Plugin, Workflow, hook, test or matter-data changes;
- staging, commit, tag, push or GitHub Release publication.

## 7. Professional and China-Law Boundary

All C01-II planning must preserve:

- candidate status for legal questions, claims, request-right bases, elements,
  facts, burdens, evidence positions and defenses;
- exact source provenance and explicit unresolved gaps;
- current-law and effective-date verification for statutes, judicial
  interpretations and other authorities;
- case-authority tiering, similarity, distinctions, retrieval date and the rule
  that cases do not replace statutes or judicial interpretations;
- authenticity, legality and relevance review for evidence;
- adverse facts, inconsistent evidence and opposing-party positions;
- qualified human legal review before consequential use.

C01 remains a lawyer-assistance analysis framework. It is not a substitute for
licensed-lawyer judgment, court fact-finding or a final legal opinion.

## 8. Proposed C01-II-A Output Boundary

If this Handoff receives explicit Architecture Review PASS and Project Owner
approval, only the following future C01-II-A outputs may be created:

1. `docs/phase2/track-c/TASK_PHASE2_C01_II_A_SKILL_DESIGN_MAPPING.md`;
2. `.codex-coordination/outbox/TASK_PHASE2_C01_II_A_SKILL_DESIGN_MAPPING_RESULT.md`.

No wildcard authorization is granted. Approval does not authorize any file under
`litigation-legal/` to be modified.

The C01-II-A Result must report `DONE` or `BLOCKED`, fixed input hashes, inspected
paths, proposed future change paths, unresolved decisions, validation results
and confirmation that no implementation asset changed.

## 9. C01-II-A Required Deliverable Content

The proposed Skill Design Mapping must contain:

1. fixed input identity and repository boundary;
2. exact existing-asset inventory used for the mapping;
3. canonical ownership decision proposal for each of the ten C01 concepts;
4. path-by-path future change matrix;
5. proposed Skill-to-Skill and optional Agent interaction contracts in Markdown;
6. human-review and China-law authority controls;
7. dependency and migration ordering;
8. compatibility-alias and deprecated-asset treatment;
9. risk register, including methodology drift, schema creep, confidentiality,
   adverse-fact suppression and Agent overreach;
10. deterministic acceptance criteria for a later C01-II-B Task;
11. explicit implementation exclusions;
12. open decisions requiring Architecture Coordinator or Project Owner action.

The deliverable must not contain full replacement prompts, code patches,
executable schemas or instructions that silently presume implementation approval.

## 10. Authorization Boundary

The controlling rule is:

```text
Approval of this Handoff does not authorize implementation.

Implementation requires separate Project Owner approval.
```

More specifically:

- Handoff approval may authorize only C01-II-A documentation-only planning at
  the two exact paths in Section 8;
- C01-II-B remains blocked until a separately reviewed Skill Design Mapping and
  a path-specific Project Owner Implementation Decision exist;
- C01-II-C remains blocked until implementation and validation prerequisites are
  separately approved;
- an existing tool grant, file permission or dirty working tree is never
  implementation authority.

## 11. Handoff Acceptance Criteria

### AC-C01-II-HO-001 — Fixed Inputs Bound

The Handoff records the exact v0.2 and approved C01-I Specification paths and
SHA-256 values, plus their accepted governance records.

Verification Method:

- recompute each listed hash;
- fail on any mismatch, ambiguity or cross-workspace substitution.

### AC-C01-II-HO-002 — Phase Separation

C01-II-A, C01-II-B and C01-II-C are separately defined, and only C01-II-A is
eligible for authorization after this Handoff's approval.

Verification Method:

- confirm A is documentation-only planning;
- confirm B and C state `NOT AUTHORIZED`;
- fail if Handoff approval is presented as implementation permission.

### AC-C01-II-HO-003 — Candidate Scope Is Existing-Architecture Only

Future candidates remain within existing `litigation-legal` Skill/Agent/workflow
architecture.

Verification Method:

- inspect every candidate path;
- fail any new global reasoning layer, plugin, database, knowledge graph or
  parallel methodology architecture.

### AC-C01-II-HO-004 — Exclusions Complete

The Handoff prohibits MCP/external-provider changes, runtime schemas, automated
opinions or strategy, D1-D6 and current implementation changes.

Verification Method:

- locate every exclusion in Section 6;
- fail any language that grants current modification authority.

### AC-C01-II-HO-005 — Professional Boundary Preserved

Planning preserves China-law authority, provenance, uncertainty, adverse facts,
evidence review and qualified-human controls.

Verification Method:

- inspect Sections 7 and 9;
- fail automated outcome, claim-selection or final-opinion behavior.

### AC-C01-II-HO-006 — Exact Future Outputs

Only the two C01-II-A documentation paths in Section 8 may become authorized by
a subsequent Project Owner approval of this Handoff.

Verification Method:

- confirm both paths are exact and under the repository;
- confirm no `litigation-legal/` file is an allowed C01-II-A output;
- confirm no wildcard path authorization exists.

### AC-C01-II-HO-007 — Current Materialization Is Handoff-Only

This materialization creates only
`.codex-coordination/inbox/TASK_PHASE2_C01_II_IMPLEMENTATION_HANDOFF.md`.

Verification Method:

- inspect the complete task change set;
- fail if a Result, C01-II-A output, D1-D6 or implementation asset is created;
- verify staging remains empty and `git diff --check` passes.

All seven criteria must pass before ChatGPT Architecture Review may recommend
Project Owner approval.

## 12. Review and Decision Flow

```text
C01-I Specification APPROVED
        ↓
C01-II Handoff Draft materialized by Codex
        ↓
Codex returns exact path, hash and validation result
        ↓
ChatGPT Architecture Review
        ↓
Project Owner Decision on this exact Handoff
        ↓
If approved: C01-II-A documentation-only planning
        ↓
Separate C01-II-A Review and Project Owner Decision
        ↓
Separate C01-II-B Implementation Task and approval
```

No gate may be skipped or interpreted by implication.

## 13. Current State

```text
Phase 2 Track C — TASK_PHASE2_C01

C01 Design Baseline: APPROVED
C01-I Implementation Design: APPROVED AND CLOSED
C01-II Handoff: DRAFT — PENDING REVIEW
C01-II-A Skill Design Mapping: NOT STARTED
C01-II-B Skill / Agent Modification: NOT AUTHORIZED
C01-II-C Validation: NOT AUTHORIZED
D1-D6: NOT AUTHORIZED
Code Change: NOT AUTHORIZED
```

## 14. Next Action

Codex must return the exact materialized Handoff path, SHA-256 and validation
result to ChatGPT / Architecture Coordination.

ChatGPT must review this exact Handoff against AC-C01-II-HO-001 through
AC-C01-II-HO-007. Project Owner approval is required before C01-II-A may create
either documentation output in Section 8.

No current action may enter code, Skill, Agent, Plugin, Workflow, Hook, Test or
Runtime Schema implementation.
