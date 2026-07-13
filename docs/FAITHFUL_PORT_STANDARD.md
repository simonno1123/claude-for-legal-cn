# Faithful Port Standard

Status: v1 Engineering Standard; Phase 1 scope reclassified on 2026-07-13

## 1. Purpose

This document defines the engineering standard for a Faithful Port of an AI legal
project into the China Mainland legal system.

For `claude-for-legal-cn`, this standard governs responsibility mapping and
Phase 1 acceptance. It is written as
an engineering specification rather than a project overview so that the same
method can be reused for future China-law ports of comparable AI legal projects.

The core rule is:

> Responsibility Equivalence, not Literal Duplication.

The port must preserve traceability to what the upstream project is responsible
for achieving. A responsibility may be assigned to Phase 1, Phase 1.5, or Phase 2
under `docs/PROJECT_SCOPE.md`; approved deferral must remain explicit and must not
be represented as an implemented Phase 1 capability.
It does not need to duplicate the exact upstream wording, interaction shape,
provider choice, or file granularity when a China-law implementation achieves
the same responsibility.

## 2. Scope

This standard applies to:

- plugin structure review;
- upstream-to-China responsibility mapping;
- China-law localization review;
- runtime and reference integrity review;
- governance compliance review;
- plugin-level audit reports;
- v1 acceptance decisions.

This standard does not authorize Phase 1.5 or Phase 2 expansion work. Stateful
workflow infrastructure, MCP provider integrations,
commercial legal database integrations, OCR, company search, judgment search,
enforcement intelligence, and specialized practice packs remain governed by
`docs/PROJECT_SCOPE.md`.

## 3. Definitions

| Term | Definition |
|---|---|
| Upstream | The original `claude-for-legal` project used as the reference implementation. |
| Port | The engineering process of mapping upstream responsibilities into China-law implementations. |
| Faithful Port | A port that preserves upstream capabilities and responsibilities while replacing legal substance with China-law equivalents. |
| Capability | The broad ability a plugin provides, such as contract review, privacy review, employment review, or litigation support. |
| Responsibility | A required function that must exist for a capability to be complete. |
| Operational Depth | Implementation detail, workflow richness, interaction depth, examples, learning behavior, or provider-specific affordances. Operational depth differences do not default to defects. |
| Localization | Replacement of foreign legal substance, sources, examples, citations, assumptions, and review gates with China-law equivalents. |
| Connector | An interface or integration layer that allows external capabilities or data to be accessed. |
| Provider | A specific external data or service source, such as PKULAW, Faxin, official legal databases, OCR providers, company search, or court data services. |
| Compatibility Wording | Legacy or upstream-compatible names retained for structural continuity while the substance has been localized. |
| Design Difference | A deliberate implementation difference that does not prevent the upstream responsibility from being achieved. |
| Observation | A non-blocking implementation or depth difference that should be recorded but does not affect responsibility completion. |
| Phase 1 Baseline | China-law substantive alignment, root discoverability, mandatory runtime validation, and truthful documentation required for the Release Candidate. |
| Phase 1.5 Legal Workflow Layer | Local, human-triggered persistence, tracking, matter isolation, and lifecycle behavior. |
| Phase 2 Advanced Integration | External providers, automatic monitoring, privileged ecosystem actions, and specialized cross-border capabilities. |

## 4. Responsibility Mapping Principle

Audits must not start by asking whether each upstream file was copied or each
skill was translated literally. Audits must start by mapping responsibility.

Use this sequence:

| Step | Question |
|---|---|
| Upstream | What upstream module, skill, agent, workflow, or document is being reviewed? |
| Capability | What broad capability does it support? |
| Responsibility | What required responsibility does it perform? |
| CN Equivalent | What China-law implementation performs the same responsibility? |
| Assessment | Is the responsibility preserved, mapped, expanded, missing, or only different in operational depth? |

One upstream responsibility may map to one or more China-law implementations.
Multiple upstream implementation details may also consolidate into a single
China-law workflow, provided the upstream responsibility remains fully
achievable.

When an approved scope decision assigns a responsibility to Phase 1.5 or Phase 2,
the Phase 1 implementation may provide only a compatibility entry, safe intake,
planning template, or explicit handoff. The mapping matrix must identify that
boundary; the deferred responsibility must not be described as complete.

Example:

| Upstream | Capability | Responsibility | CN Equivalent | Assessment |
|---|---|---|---|---|
| `customize` | Preference Management | Update user profile and review preferences | `cold-start-interview --update` or equivalent preference refresh workflow | Mapped, pending command-level verification |

## 5. Audit Standard

Every plugin audit must use the same review order:

1. Structure
2. Capability
3. Responsibility
4. Operational Depth
5. Localization
6. Runtime
7. Governance
8. Risks
9. Lessons Learned
10. Overall

### 5.1 Structure

Review plugin manifests, README files, `CLAUDE.md`, skills, commands, agents,
references, hooks, `.mcp.json`, and marketplace compatibility.

Structural differences are defects only when they break runtime behavior,
remove an upstream responsibility, or create an unresolved v1 mapping decision.

### 5.2 Capability

Identify the upstream capability and confirm that the China-law plugin still
serves the same capability category.

Capability loss inside the phase currently under acceptance is a Blocker. An
explicitly approved later-phase capability is not a Phase 1 Blocker.

### 5.3 Responsibility

Map upstream responsibilities to China-law equivalents. Treat file
consolidation, command renaming, or China-specific workflow design as acceptable
when the responsibility remains achievable.

Responsibility loss inside the phase currently under acceptance is a Blocker.
Responsibility impairment is a Gap. An approved Phase 1.5 or Phase 2 assignment
is a scope classification, not a Phase 1 defect, when the current boundary is truthful.

### 5.4 Operational Depth

Record differences in interaction depth, learning behavior, seed documents,
automation richness, examples, playbooks, and provider-specific integrations.

Operational depth differences are Observations unless they prevent a
responsibility from being completed.

### 5.5 Localization

Confirm that statutes, legal assumptions, examples, sources, prompts, workflows,
and review gates are localized to the China Mainland legal system.

Foreign-law references may remain when they are:

- negative constraints;
- compatibility wording;
- comparative context;
- isolated external/vendor content;
- explicit v2+ connector or provider placeholders.

Foreign-law substance that still drives the China-law workflow is a Gap or
Blocker depending on severity.

### 5.6 Runtime

Check command paths, skill references, marketplace source paths, internal links,
`.mcp.json` syntax, hooks, and obvious broken references.

Runtime defects that prevent a plugin from being used are Blockers or Gaps.
Provider differences are not runtime defects unless the configured local runtime
actually breaks.

### 5.7 Governance

Check compliance with:

- `docs/PROJECT_SCOPE.md`;
- `docs/UPSTREAM_MAPPING_MATRIX.md`;
- this standard.

The audit must flag business-priority drift, module devaluation, product-specific
positioning, stale phase assignments, premature later-phase completion claims,
or claims of production provider integration that are not implemented.

## 6. Severity Model

| Severity | Meaning | Typical Result |
|---|---|---|
| Blocker | A capability or required responsibility in the accepted phase is absent, or mandatory runtime is unusable. | ACTION REQUIRED |
| Gap | A responsibility in the accepted phase exists but behavior is materially different in a way that affects completion. | ACTION REQUIRED or Conditional PASS depending on scope |
| Observation | Responsibility works, but operational depth, workflow richness, examples, or implementation shape differs. | PASS or Conditional PASS |
| Enhancement | Future improvement or an approved later-phase item. | PASS or Conditional PASS |

Severity must be assigned by effect on capability and responsibility, not by
literal file differences.

## 7. Acceptance Rule

| Result | Definition |
|---|---|
| PASS | Phase 1 capabilities are present, China-law localization is sufficient, mandatory runtime passes, phase mappings are truthful, and no governance issue blocks acceptance. |
| Conditional PASS | Phase 1 capabilities are substantially present, but mapping confirmations, Observations, Enhancements, or limited non-blocking Gaps remain. |
| ACTION REQUIRED | A Phase 1 Blocker exists, or a Gap materially prevents Phase 1 baseline acceptance. |

An audit may not mark a plugin ACTION REQUIRED only because upstream operational
depth is richer. It must identify the responsibility that is actually missing or
impaired.

## 8. Non-goals

The following do not default to parity defects:

- connector differences;
- provider differences;
- local placeholder MCP implementations;
- China-specific references;
- China-specific playbooks;
- China-specific templates;
- command or workflow consolidation;
- compatibility names retained for upstream traceability;
- richer China-law examples than upstream examples.
- responsibilities assigned to Phase 1.5 or Phase 2 by an accepted scope decision.

They become defects only if they prevent an upstream capability or
responsibility from being achieved, break runtime use, or violate
`docs/PROJECT_SCOPE.md`.

## 9. Audit Report Format

Each audit report must use this structure:

```markdown
# Audit NN

Plugin: <plugin-name>
Standard: FAITHFUL_PORT_STANDARD v1
Mode: REVIEW ONLY

## Revision History

| Date | Event | Overall | Reason |
|---|---|---|---|

## Structure

## Capability

## Responsibility

## Operational Depth

## Localization

## Runtime

## Governance

## Risks

### Blocker

### Gap

### Observation

### Enhancement

## Lessons Learned

1. Which Faithful Port principles did this plugin validate?
2. Should later plugin audits adjust the standard?

## Overall

PASS / Conditional PASS / ACTION REQUIRED
```

Audit reports are historical records. Do not erase earlier judgments. When an
audit is reclassified under a newer standard, add a new Revision History entry
and explain the reason.

## 10. Lessons Learned Requirement

Every audit must include Lessons Learned.

Lessons Learned are part of the engineering process, not optional commentary.
They record how the standard was validated or refined while auditing real
plugins. Later audits should apply accumulated lessons without rewriting
historical audit records.
