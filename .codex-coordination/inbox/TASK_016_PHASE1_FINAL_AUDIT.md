# ACOS Task Artifact

## 1. Identity

```text
TASK ID: TASK_016_PHASE1_FINAL_AUDIT
ARTIFACT TYPE: TASK
PRODUCER: ChatGPT
TO: Codex
NEXT RECEIVER: Gemini
MODE: READ ONLY
```

## 2. Workflow State

```text
Task File: CREATED
Execution: PENDING
Reviewer: PENDING
Decision: PENDING
```

Creating this TASK artifact does not constitute execution of the audit. Codex must perform the audit in a separate execution step and produce a RESULT artifact before Gemini begins REVIEW or DECISION.

## 3. Project

```text
PROJECT: /Users/zhang/Documents/claude-for-legal-cn
UPSTREAM: /Users/zhang/Documents/Playground/claude-for-legal-upstream
STANDARD: /Users/zhang/Documents/claude-for-legal-cn/docs/FAITHFUL_PORT_STANDARD.md
```

The PROJECT path above is the only valid working copy for this task lifecycle. All reads, validations, evidence citations, and artifact paths must resolve from this PROJECT. Do not substitute a Downloads copy or another clone.

## 4. Objective

Perform the Phase 1 final repository audit for `claude-for-legal-cn` against the approved upstream baseline and the Faithful Port v1 governance standard.

Determine, from the actual filesystem state, whether every Phase 1 upstream capability has a discoverable and responsibility-equivalent China-law implementation, whether prior recovery work remains present and internally consistent, and whether the repository is ready to enter Release Candidate review.

This is an evidence-producing audit only. Codex may provide a factual recommendation but must not issue the final project acceptance decision.

## 5. Audit Scope

Read and assess:

- Repository root and Git state.
- `.claude-plugin/marketplace.json` and every registered plugin source.
- All root legal plugins and their manifests, `README.md`, `CLAUDE.md`, skills, commands, agents, hooks, references, and MCP configuration where present.
- Promoted `law-student/` and `legal-clinic/` modules.
- `managed-agent-cookbooks/`.
- `external_plugins/cocounsel-legal/` as an isolated compatibility asset.
- Governance and usage documents, including:
  - `README.md`
  - `PROJECT_USAGE_GUIDE.md`
  - `docs/PROJECT_SCOPE.md`
  - `docs/UPSTREAM_MAPPING_MATRIX.md`
  - `docs/FAITHFUL_PORT_STANDARD.md`
- Existing audit, RESULT, REVIEW, and DECISION artifacts only as historical context. Do not treat an artifact claim as proof unless the current repository files support it.

External provider implementation and live commercial database access are outside Phase 1 scope except where documentation falsely claims production availability or a broken configuration prevents local plugin use.

## 6. Required Analysis

### A. Git And Evidence Baseline

Report:

- Current branch and HEAD commit.
- Ahead/behind status if available without network access.
- Tracked modifications, staged changes, deletions, and untracked files.
- Whether the audit is evaluating committed state, working-tree state, or both.
- Any condition that prevents a reliable Release Candidate assessment.

Do not modify, stage, clean, stash, or commit the worktree.

### B. Marketplace And Structural Integrity

Verify:

- Every marketplace entry resolves to an existing directory.
- Every expected upstream Phase 1 module has a China-law module or an explicit, standard-compliant mapping.
- Root command and skill discoverability.
- Plugin manifests and source paths.
- Required `README.md`, `CLAUDE.md`, skills, commands, agents, hooks, references, and MCP files where the upstream responsibility requires them.
- Empty directories, duplicate promoted modules, stale `phase-2/` copies, broken links, and displaced root responsibilities.

File-count differences and consolidation are not defects by themselves. Apply responsibility equivalence rather than literal duplication.

### C. Capability And Responsibility Parity

For each upstream module and root operational asset, map:

```text
Upstream Capability
→ Upstream Responsibility
→ China-law Equivalent
→ Current Discoverability
→ Assessment
```

Classify each responsibility as:

- Preserved
- Mapped
- Expanded
- Relocated but discoverable
- Missing
- Suspended

Confirm that previously restored responsibilities remain effective, including corporate M&A root wrappers, regulatory stateful workflows, AI governance recovery, law-student learning workflows, and legal-clinic case-management and supervisor-review workflows.

### D. Operational Depth

Separately assess implementation depth for:

- Stateful files and persistence.
- Lifecycle and status transitions.
- Tracking, reminders, closure, and handoff behavior.
- Human-review or supervisor gates.
- Source provenance and reviewer-note requirements.
- No-silent-supplementation guardrails.
- Cold-start, profile update, redo, and integration-check behavior where applicable.
- Command delegation and wrapper resolution.

Operational depth differences are Observations unless they prevent an upstream responsibility from being achieved.

### E. China-Law Localization

Scan actual content for substantive residue from:

- United States federal or state law.
- Delaware corporate law.
- UCC, SEC, FRCP, ABA, U.S. bar, and U.S. clinic assumptions.
- UK, EU, GDPR, or common-law defaults.
- Foreign privilege, work-product, litigation, contract, employment, privacy, regulatory, education, or clinic workflows.

Classify every meaningful occurrence as:

- China-law default implementation.
- Compatibility wording.
- Comparative reference.
- Negative constraint.
- Isolated external-plugin content.
- Substantive localization residue requiring remediation.

Do not classify China-specific playbooks, references, templates, or provider placeholders as parity defects merely because they differ from upstream.

### F. Runtime And Static Validation

Validate without installing dependencies or contacting external providers:

- JSON syntax for marketplace, plugin manifests, MCP files, and hook files.
- YAML syntax where repository workflows depend on YAML state or configuration.
- Marketplace source resolution.
- Root command discoverability and referenced command existence.
- Wrapper and delegation target resolution.
- README and usage-guide command examples.
- Internal Markdown paths and obvious broken references.
- Duplicate plugin names or conflicting command exposure.

Provider differences, placeholder connectors, and unavailable live credentials are not Phase 1 defects unless they break a claimed local responsibility or contradict project documentation.

### G. Governance Consistency

Check current files against `PROJECT_SCOPE.md`, `UPSTREAM_MAPPING_MATRIX.md`, and `FAITHFUL_PORT_STANDARD.md` for:

- Enterprise-priority or personal-practice positioning.
- Module devaluation or Phase-2 downgrade wording.
- Stale paths for promoted modules.
- Claims of production-grade commercial database integration.
- Unsupported productization or v2 feature claims.
- Mapping-matrix drift from the actual filesystem.
- Conflicts between documentation, marketplace exposure, and executable command paths.

### H. Prior Recovery Regression Check

Verify from current files, rather than coordination claims alone, that accepted recovery work has not regressed for:

- `corporate-legal` structural discoverability and alignment.
- `regulatory-legal` workflow responsibilities.
- `ai-governance-legal` responsibility restoration.
- `managed-agent-cookbooks` and external-plugin isolation.
- `law-student` root promotion and learning safeguards.
- `legal-clinic` root promotion, deadline ledger, review queue, intake, and handoff behavior.

### I. Risks

Keep these categories separate:

- **Blocker**: A required Phase 1 capability or responsibility is absent, undiscoverable, or unusable.
- **Gap**: The responsibility exists but has a material behavioral mismatch that affects faithful achievement.
- **Observation**: A depth, organization, or implementation difference that does not prevent responsibility completion.
- **Enhancement**: A valid future improvement outside Faithful Port v1, including v2 provider or capability expansion.

For every Blocker or Gap, cite concrete paths and line numbers where practical, identify the affected upstream responsibility, and state the minimum remediation boundary.

### J. Lessons Learned

Answer:

1. Which Faithful Port principles are confirmed or challenged by the final audit?
2. Does any finding require changing future audit practice, without modifying the frozen v1 governance standard in this task?

## 7. Overall Factual Recommendation

Recommend exactly one:

- `PASS`
- `Conditional PASS`
- `ACTION REQUIRED`

This recommendation is part of the Codex RESULT evidence. It is not a Gemini REVIEW or DECISION and does not close Phase 1.

## 8. Required Validation Commands

Use read-only commands sufficient to establish the evidence, including:

```text
pwd
git branch --show-current
git rev-parse --short HEAD
git status --short --branch
git diff --stat
git diff --cached --stat
find and rg inventories for marketplace, plugins, skills, agents, commands, hooks, references, and phase-2 residues
python3 -m json.tool for JSON files in scope
read-only YAML parsing for YAML files in scope
rg checks for command references, stale paths, governance drift, and foreign-law residue
```

Do not use a validation command that writes generated files, lockfiles, caches, or formatting changes into the repository.

## 9. Forbidden Actions

- Do not modify project or plugin files.
- Do not modify governance documents.
- Do not stage files.
- Do not commit.
- Do not push.
- Do not install dependencies.
- Do not run automatic fixes or formatters.
- Do not contact live MCP providers or commercial legal databases.
- Do not create REVIEW or DECISION artifacts.
- Do not write as Gemini.
- Do not declare Phase 1 accepted or closed.
- Do not write outside the required RESULT artifact.

## 10. Output Artifact

Codex must write one RESULT artifact only:

```text
/Users/zhang/Documents/claude-for-legal-cn/.codex-coordination/outbox/TASK_016_PHASE1_FINAL_AUDIT_RESULT.md
```

The RESULT must contain:

1. Execution status (`DONE` or `BLOCKED`).
2. Workspace and Git baseline.
3. Marketplace and structure findings.
4. Capability mapping.
5. Responsibility mapping.
6. Operational depth findings.
7. Localization findings.
8. Runtime validation results.
9. Governance findings.
10. Prior recovery regression findings.
11. Risks separated into Blocker, Gap, Observation, and Enhancement.
12. Lessons Learned.
13. Overall factual recommendation.
14. Commands executed and validation summary.

## 11. BLOCKED Rules

Stop and return a `BLOCKED` RESULT if:

- `pwd` is not exactly `/Users/zhang/Documents/claude-for-legal-cn`.
- The upstream path cannot be read and no approved upstream baseline exists at the specified path.
- `docs/FAITHFUL_PORT_STANDARD.md` cannot be read.
- A filesystem or permission condition prevents collection of material audit evidence.

Do not infer evidence from another working copy.

## 12. Next Handoff

After Codex writes the RESULT:

```text
Codex RESULT
→ Gemini REVIEW
→ Gemini DECISION
```

Gemini is the only review and judgment layer for this task. Creation of the TASK or RESULT does not imply acceptance.
