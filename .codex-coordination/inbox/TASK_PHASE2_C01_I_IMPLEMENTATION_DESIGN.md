# TASK_PHASE2_C01_I_IMPLEMENTATION_DESIGN

STATUS: **DRAFT COMPLETED — PROJECT OWNER REVIEW REQUIRED**

TYPE: Phase 2 Track C — Implementation Design Task

MODE: DESIGN → ENGINEERING MAPPING ONLY

TARGET MODULE: `litigation-legal`

C01-I IMPLEMENTATION DESIGN: **AUTHORIZED FOR TASK PLANNING**

C01-II SKILL / AGENT ENHANCEMENT: **NOT AUTHORIZED**

C01-III VALIDATION EXECUTION: **NOT AUTHORIZED**

IMPLEMENTATION: **NOT AUTHORIZED**

## 1. Governance Identity

This Task is drafted under the Project Owner decision supplied on 2026-07-18:

```text
TASK_PHASE2_C01_IMPLEMENTATION_HANDOFF v0.2

Decision: APPROVED WITH CONDITIONS
Authorization: C01-I Implementation Design Authorized
Implementation: NOT AUTHORIZED
Code / Skill / Agent Modification: NOT AUTHORIZED
```

The decision authorizes preparation of an implementation-design mapping. It is
not permission to implement the mapping, create D1-D6, change runtime behavior
or modify any existing `litigation-legal` asset.

This Task file is itself a reviewable Task Draft. Its creation does not execute
the C01-I design work described below. C01-I execution may begin only after the
Project Owner approves this exact Task identity and its fixed output path.

## 2. Fixed Dependencies

Before C01-I execution, Codex must verify these exact inputs:

| Input | Canonical path / identity | Required state |
|---|---|---|
| Phase 2 Architecture Decision | `.codex-coordination/decisions/TASK_PHASE2_000_ARCHITECTURE_ALIGNMENT_ACCEPTANCE_RETRY_1_DECISION.md` | ACCEPTED |
| C01 reviewed baseline | `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md` | SHA-256 `67C74A63EE0BCCB4B20A9035467A16CF2B43EFD624E45C2B501A60A8590ED6E5` |
| C01 formalized design | `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.3.md` | SHA-256 `EEB69963715A6A52F37DFF4151DEE8CB0AA314B04E8C936E3CD4866B0ECAD857` |
| C01 Design Revision Result | `.codex-coordination/outbox/TASK_PHASE2_C01_DESIGN_REVISION_RESULT.md` | SHA-256 `F0F275B87D81BBEE99E2AA6F91078B2C523B7D161BA3FFE2E575795397B2F564` |
| C01-I Task authorization | This Task file and a subsequent explicit Project Owner approval | Required before execution |

If any fixed identity is absent, changed or ambiguous, C01-I execution must
stop. Codex must not reconstruct an input or treat a summary as a replacement.

## 3. Objective

Produce a reviewable implementation-design specification that maps the approved
C01 legal-methodology concepts to the current `litigation-legal` architecture:

```text
Legal Methodology
        ↓
Existing Skill / Agent / Matter Workspace Architecture
        ↓
Future Change Points
        ↓
Authorization Boundary
```

The specification must answer:

- which existing assets already carry part of each C01 concept;
- where coverage is partial or absent;
- which existing Skill or Agent could be a future change point;
- what conceptual inputs, outputs and interactions would be required;
- which future changes require separate authorization;
- which assets must remain untouched.

The output is an engineering mapping, not an implementation plan expressed as
code, patches, runtime schemas or executable instructions.

## 4. Canonical Output

C01-I execution may create exactly one file:

```text
docs/phase2/track-c/TASK_PHASE2_C01_IMPLEMENTATION_DESIGN_SPEC.md
```

The Mapping Matrix and Implementation Boundary Report required by the Project
Owner decision must be sections inside that single specification. They are not
separate files.

No execution Result file, D1-D6 artifact or other output path is authorized by
this Task Draft.

## 5. Read-Only Inventory Scope

C01-I may inspect, but must not modify:

- `litigation-legal/.claude-plugin/plugin.json`;
- `litigation-legal/README.md`;
- `litigation-legal/CLAUDE.md`;
- `litigation-legal/skills/*/SKILL.md` and their references;
- `litigation-legal/agents/*.md`;
- `litigation-legal/matters/`, `inbound/`, `demand-letters/` and `oc-status/`
  templates or ledgers;
- `litigation-legal/references/`;
- repository-level China-law authority and terminology references required by
  `AGENTS.md`.

Read access does not imply change authorization. Existing tool grants, including
the `docket-watcher` Agent's `Read` and `Write` tools, must not be treated as
permission for this Task to edit runtime assets or matter data.

## 6. Existing-Asset Inventory Seed

The specification must independently inspect the current files and may use the
following only as candidate entry points, not as predetermined conclusions:

| C01 area | Existing candidate assets | Initial coverage hypothesis |
|---|---|---|
| Matter context | `matter-workspace`, `matter-intake`, `matters/[slug]/matter.md` | Existing / partial |
| Issue / Question identification | `matter-intake`, `matter-briefing` | Partial; no dedicated Question representation confirmed |
| Claim / Request Right | `matter-intake`, `claim-chart` | Partial |
| Element decomposition | `claim-chart` | Gap or partial; no dedicated Element model confirmed |
| Legal Fact organization | `chronology`, `claim-chart`, matter files | Partial |
| Proof / Evidence mapping | `claim-chart`, `evidence-preservation`, `confidential-evidence-review` | Existing / partial |
| Defense / Rebuttal | `claim-chart`, `matter-briefing`, `brief-section-drafter` | Partial |
| Procedural events and candidate deadlines | `matter-update`, `docket-watcher` | Existing adjacent capability |
| Human review gate | `litigation-legal/CLAUDE.md` and reviewer-note patterns in core Skills | Existing / distributed |

For every row, the specification must cite the exact inspected file and current
behavior that supports the classification. It must use one of:

```text
EXISTS
PARTIAL
ABSENT
INCOMPATIBLE
REQUIRES DECISION
```

The specification must not describe a proposed capability as already existing.

## 7. Required Specification Structure

The single C01-I specification must contain all of the following sections.

### 7.1 Identity and Provenance

Record:

- the v0.2, v0.3 and Design Revision Result paths and hashes;
- the approved C01-I Task identity;
- the inspection date;
- every repository path inspected;
- the current plugin version;
- the fact that no implementation authorization exists.

### 7.2 Existing Architecture Inventory

Inventory current:

- Skill names and purposes;
- Agent names, tools and interaction boundaries;
- matter workspace and ledger structures;
- existing workflow entry points;
- human-review controls;
- China-law reference dependencies.

The inventory must distinguish canonical assets from compatibility commands and
must identify deprecated aliases without proposing changes to them.

### 7.3 C01 Concept-to-Asset Mapping Matrix

The primary matrix must contain one row for each of:

```text
Matter
Issue / Question
Claim
Request Right
Element
Legal Fact
Proof
Evidence
Defense / Rebuttal
Human Review
```

Required columns:

| Column | Required content |
|---|---|
| C01 concept | Exact methodology term |
| Existing asset | Exact repository path and asset name |
| Current evidence | Current behavior or output field proving the mapping |
| Coverage | EXISTS / PARTIAL / ABSENT / INCOMPATIBLE / REQUIRES DECISION |
| Future change point | Existing Skill/Agent/workflow location that could carry a later change |
| Future change type | Prompt, interaction, workspace field, validation or documentation |
| Authorization required | Exact later Handoff or Project Owner decision required |
| Current action | `NO CHANGE — DESIGN ONLY` |

### 7.4 Existing Workflow Interaction Map

Describe, without changing it, how a future C01 flow could interact with:

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

The map must also classify `matter-update`, evidence-related Skills and
`docket-watcher` as core, adjacent, optional or incompatible interaction points.
It must not create a new global orchestrator or methodology layer.

### 7.5 Conceptual Input Interface

Use Markdown tables only. Do not create YAML, JSON Schema, runtime schema or
machine-executable contracts.

At minimum, describe candidate inputs for:

- matter identity and procedural posture;
- client position and objective;
- Issue / Question candidates;
- Claim and Request Right candidates;
- facts, sources and provenance;
- evidence identifiers and proof purposes;
- governing authority with effective-date verification;
- defenses, rebuttals and adverse facts;
- uncertainty, gaps and human-review status.

### 7.6 Conceptual Output Interface

Use Markdown tables only and keep every legal conclusion at candidate status.
Describe future outputs for:

- Matter → Issue / Question → Claim / Request Right traceability;
- Element-to-fact, burden, proof-rule, evidence and gap mapping;
- Defense / Rebuttal paths;
- authority and source provenance;
- confidence and unresolved-gap statements;
- qualified-human review decisions.

The interface must not promise automated legal opinions, outcome prediction,
claim selection, litigation strategy or adjudication.

### 7.7 Skill and Agent Interaction Design

For each candidate existing Skill or Agent, record:

- current responsibility;
- potential future C01 responsibility;
- proposed interaction inputs and outputs;
- overlap or conflict with other assets;
- required future authorization;
- current status: `NO MODIFICATION AUTHORIZED`.

No new Skill or Agent may be designed as an assumed requirement. If the existing
architecture cannot carry a concept, record `REQUIRES DECISION` instead of
inventing a new component.

### 7.8 Future Change-Point Register

Each proposed future change point must state:

- exact existing asset path;
- reason it is a candidate;
- smallest conceivable future change;
- dependencies and risks;
- whether D1-D6 must first be approved;
- exact authorization still required;
- explicit statement that the change is not performed by C01-I.

### 7.9 Implementation Boundary Report

The report must separate:

```text
MAY BE CONSIDERED IN A FUTURE HANDOFF
MUST REMAIN UNCHANGED
REQUIRES ARCHITECTURE DECISION
OUT OF SCOPE
```

It must expressly prohibit current changes to code, Skills, Agents, CLAUDE.md,
Plugin metadata, MCP, workflows, runtime schemas, hooks, tests, D1-D6, Phase 2
Architecture, `PROJECT_SCOPE.md` and `PHASE_2_ROADMAP.md`.

### 7.10 Risk Register

At minimum, assess:

- methodology drift from the approved v0.3 design;
- duplication across `matter-intake`, `claim-chart` and `matter-briefing`;
- false representation of partial coverage as implemented capability;
- hard-coded or stale China-law doctrine;
- accidental automated legal-opinion or strategy behavior;
- adverse-fact suppression;
- cross-matter confidentiality or conflict leakage;
- runtime schema creep;
- compatibility-command confusion;
- Agent tool overreach;
- creation of a parallel methodology architecture.

### 7.11 Non-Modification Plan

Explain how a later implementation could be decomposed into separately
reviewable changes while this Task makes none. The plan must not include code,
patches, full prompt replacements or executable schemas.

### 7.12 Open Decisions and Next Authorization

List unresolved ownership, overlap, interface and validation questions. Conclude
with the exact review and Project Owner approval needed before any C01-II work.

## 8. Forbidden Changes

C01-I Task drafting and execution must not:

- modify or create `*.py`, `*.js`, `*.ts` or any other runtime code;
- modify or create any file under `litigation-legal/skills/`;
- modify or create any Agent or `litigation-legal/CLAUDE.md` behavior;
- modify Plugin or Marketplace metadata;
- modify MCP or connector configuration;
- modify workflow, hook, test or runtime schema assets;
- create D1-D6;
- create a Global Legal Reasoning Core, `methodology/` tree or
  `legal-reasoning-core/` tree;
- modify Phase 2 Architecture, `PROJECT_SCOPE.md` or `PHASE_2_ROADMAP.md`;
- change the approved C01 v0.2 or v0.3 documents;
- stage, commit, tag, push or publish a GitHub Release.

## 9. Acceptance Criteria

### AC-C01-I-001 — Fixed Input Identity

The specification records and verifies the exact approved v0.2, v0.3 and Design
Revision Result paths and hashes.

Verification Method:

- recompute all three hashes;
- compare them with Section 2;
- return BLOCKED on any mismatch.

### AC-C01-I-002 — Truthful Existing-Asset Inventory

Every inventory claim cites an inspected existing path and classifies coverage
without overstating current capability.

Verification Method:

- verify every inventory row has a repository path and supporting current
  behavior;
- fail any row that labels an unimplemented proposal as existing.

### AC-C01-I-003 — Complete Methodology Mapping

The primary matrix covers all ten concepts listed in Section 7.3 and identifies
coverage, future change point, authorization requirement and `NO CHANGE` status.

Verification Method:

- check each required concept occurs exactly once in the primary matrix;
- check every required column is populated;
- fail if any future change is presented as currently authorized.

### AC-C01-I-004 — Non-Executable Interface Design

Input and output interfaces are reviewable but do not create runtime or MCP
schemas.

Verification Method:

- verify interfaces are Markdown tables or prose only;
- fail if executable schema files, code, generated configs or runtime contracts
  are created.

### AC-C01-I-005 — Implementation Boundary Completeness

The Boundary Report distinguishes future candidates, protected assets,
decision-required items and out-of-scope items.

Verification Method:

- locate all four boundary categories;
- verify every proposed change point names a later authorization;
- fail if any current modification is permitted.

### AC-C01-I-006 — Professional and China-Law Boundary

The specification preserves candidate status, current-authority verification,
adverse facts and qualified human legal review.

Verification Method:

- inspect all interface and interaction sections for provenance, uncertainty,
  current-law verification and human-review controls;
- fail if automated opinion, prediction, final claim selection or strategy is
  allowed.

### AC-C01-I-007 — Single Authorized Output

C01-I execution creates only the canonical specification in Section 4.

Verification Method:

- inspect the complete Task diff;
- fail if any D1-D6, code, Skill, Agent, Plugin, MCP, workflow, schema, test or
  additional result file is created or modified;
- verify staging remains empty and `git diff --check` passes.

### AC-C01-I-008 — Review Readiness

The specification contains the complete inventory, mapping, interfaces,
interaction design, future change register, boundary report, risk register,
non-modification plan and open decisions.

Verification Method:

- verify every required Section 7 heading exists exactly once;
- verify all unresolved matters are explicitly identified rather than inferred;
- return PASS only when a reviewer can issue a deterministic approval or
  revision request without inventing missing requirements.

All eight criteria must pass before C01-I Design Review may return PASS.

## 10. Execution Validation

C01-I execution must verify:

- fixed input hashes match;
- the existing asset inventory is read-only;
- the single output path is exact;
- D1-D6 do not exist as a result of the Task;
- no code, Skill, Agent, Plugin, MCP, workflow or runtime-schema file changed;
- pre-existing user changes remain preserved;
- the staging area remains empty;
- `git diff --check` passes.

Runtime tests are not required because C01-I cannot change runtime behavior.

## 11. Execution Flow

```text
Project Owner conditional decision
        ↓
TASK_PHASE2_C01_I_IMPLEMENTATION_DESIGN Task Draft
        ↓
Project Owner Task Approval
        ↓
C01-I read-only architecture inventory and mapping
        ↓
TASK_PHASE2_C01_IMPLEMENTATION_DESIGN_SPEC.md
        ↓
C01-I Design Review
        ↓
Project Owner Approval
        ↓
Separate TASK_PHASE2_C01_IMPLEMENTATION Handoff
```

No step in this flow itself authorizes Skill, Agent or runtime implementation.

## 12. Current State

```text
Phase 2 Track C

Architecture: ACCEPTED
C01 Design Baseline: APPROVED
Implementation Handoff: APPROVED WITH CONDITIONS
C01-I Implementation Design: AUTHORIZED FOR TASK PLANNING
C01-I Task Draft: COMPLETED — PENDING PROJECT OWNER REVIEW
C01-I Design Execution: NOT STARTED
C01-II Skill / Agent Enhancement: NOT AUTHORIZED
C01-III Validation: NOT AUTHORIZED
Implementation: NOT AUTHORIZED
```

## 13. Next Action

Submit this Task Draft to Project Owner Review. Only after approval may Codex
create the single C01-I Implementation Design Specification defined in Section
4. No implementation or D1-D6 work may begin.
