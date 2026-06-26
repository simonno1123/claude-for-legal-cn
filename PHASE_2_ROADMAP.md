# Phase 2 Roadmap

This document starts Phase 2 after the Phase 1 China Mainland localization baseline was committed and pushed.

## Phase 2 Scope

Phase 2 covers modules intentionally excluded from the Phase 1 default marketplace because they require deeper specialization, lower-frequency workflows, or ecosystem tooling.

## Workstreams

### 1. Corporate M&A Phase 1.5

Path: `corporate-legal/phase-2/`

Goal: localize M&A workflows for China Mainland practice after the core corporate governance, capital contribution, equity transfer, and articles audit workflows are stable.

Status: IN PROGRESS. The first localization pass rewrote the core M&A diligence, closing, contract schedule, integration, deal summary, AI handoff, and tabular review skills into China Mainland workflows, and added a China M&A regression suite.

Initial skills to review:

- `diligence-issue-extraction`
- `material-contract-schedule`
- `closing-checklist`
- `integration-management`
- `deal-team-summary`
- `tabular-review`
- `ai-tool-handoff`

China localization gates:

- Replace US deal concepts with China equity/asset acquisition, business registration, tax, labor, antitrust, data, and state-owned asset review logic.
- Add filing and approval checkpoints for market regulation, foreign investment, state-owned assets, merger control, and industry-specific licenses.
- Add due diligence output matrices covering equity title, capital contribution defects, related-party transactions, labor/social insurance, tax, permits, IP, data compliance, litigation, and material contracts.
- Do not mark as complete until a China M&A regression case set exists.

### 2. Law Student

Path: `phase-2/law-student/`

Goal: rebuild the law student module around China legal education, legal doctrine learning, judicial exam preparation, and statute/case reading.

China localization gates:

- Replace US law school, common-law briefing, Bluebook, and case-method defaults.
- Add China statute hierarchy, civil/criminal/administrative/procedural law study maps, and legal professional qualification exam modes.
- Keep outputs educational only and avoid pretending to provide client-specific legal advice.

### 3. Legal Clinic

Path: `phase-2/legal-clinic/`

Goal: rebuild the clinic module around China public legal service, legal aid, community consultation, and triage workflows.

China localization gates:

- Replace US clinic intake and privilege assumptions.
- Add China legal aid eligibility, 12348/public legal service routing, labor dispute/arbitration, consumer complaint, family, tenancy, and small-claim triage.
- Add strong boundaries for conflict checks, evidence preservation, limitation periods, and referral to licensed lawyers.

### 4. Legal Builder Hub

Path: `phase-2/legal-builder-hub/`

Goal: turn the builder hub into a China legal MCP/tooling construction kit after the Phase 1 module patterns are stable.

China localization gates:

- Provide reusable templates for China-law skills, test cases, references, MCP connector placeholders, and Gemini/manual review packets.
- Encode the Phase 1 localization workflow as repeatable tooling: scan, packet, external review, implement, validate, and status update.
- Keep connector templates credential-free and document local file mode fallback.

## Acceptance Checklist

Each Phase 2 workstream is complete only when it has:

- China Mainland system alignment and no US/common-law default reasoning.
- Localized README or module guide.
- Localized core skills and command list.
- `references/test-cases-cn.md` or equivalent regression suite.
- Valid JSON and valid skill frontmatter.
- No mojibake.
- Review packet and review result saved under `review-packets/` and `review-results/` when an external review is used.

## Suggested Execution Order

1. Corporate M&A Phase 1.5
2. Legal Builder Hub
3. Legal Clinic
4. Law Student
