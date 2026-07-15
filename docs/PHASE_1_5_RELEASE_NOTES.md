# Phase 1.5 Release Candidate Notes

Status: `RELEASE CANDIDATE / NOT YET GIT-FROZEN`

Date: 2026-07-15

## Summary

Phase 1.5 establishes a local, stateful and human-reviewed foundation for
organizing a China-law matter from intake through Evidence, Research,
Strategy and Drafting. It is workflow infrastructure, not an autonomous
lawyer, external legal database or document-processing service.

## Included

- shared local Matter lifecycle and storage rules;
- stateful workspaces for Commercial, Employment, IP, Privacy and Product;
- Product launch tracking and Commercial workflow persistence;
- Matter, Party, Fact, Evidence, Issue, Claim, Strategy and Decision Schemas;
- civil-litigation, enforcement and corporate templates;
- Evidence lifecycle, validation and Evidence-Fact-Issue mapping;
- Legal Research workflow with source provenance and verification state;
- Strategy options, risk assessment and Human Approval;
- Draft lifecycle and Draft-to-Fact source traceability;
- isolated real-case structural validation under TASK_026.

## Quality Baseline

```text
Phase 1.5 tests:                 44/44 PASS
Matter Workspace validator:     PASS
Evidence template validator:    PASS with expected template warnings
Legal Research validator:       PASS
Legal Strategy validator:       PASS
Legal Drafting validator:       PASS
China localization regression:  PASS
Real-case technical workflow:   CONDITIONAL PASS
```

The real-case run passed all six workflow layers. Provenance remained partial
where source authenticity and current primary authority had not been verified.
Professional acceptance remains pending Lawyer Owner review.

## Safety Boundary

- all legal judgments remain subject to identified human review;
- missing facts and authorities cannot be silently supplemented;
- structural validation does not establish truth or legal correctness;
- no final filing, signature, service or external action is automated;
- real-case material remains outside Git and ACOS artifacts.

## Not Included

- OCR or scan-content extraction;
- external legal databases;
- MCP or external providers;
- Agent orchestration or LLM call chains;
- automated fact findings, legal opinions, strategy selection or outcome
  prediction;
- court filing or document signing.

TASK_027 Evidence Intelligence is Phase 2 and is not part of this Release
Candidate.

## Release Status

The Release Candidate documentation is complete, but the current tree contains
uncommitted Phase 1.5 assets and separate Phase 2 work. Final freeze requires a
dedicated Phase 1.5-only commit, successful staged-tree regression and a
recorded commit hash. A tag may be created only after review authorization.

The canonical inventory, dependency review, validation details and limitations
are recorded in `docs/PHASE_1_5_BASELINE.md`.
