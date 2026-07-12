# Codex Task

## 1. Task ID

TASK_010_CORPORATE_WRAPPER_REVIEW

## 2. Status

READY

## 3. Background

The `corporate-legal` module has completed its Phase 1 deep changes for the new 2024 China Company Law (governance, capital contribution, articles of association audit, equity transfer). However, the audit cycle (`Audit 04`) remains in a `Pending Review` state because the corporate wrapper review was not finalized, and there are known structural alignment items (S-03: M&A skills in phase-2) and missing skills (M-03: `customize` skill).

This task is a READ ONLY task to audit the `corporate-legal` directory, list all active/suspended skills, identify gaps against the upstream baseline, and provide a clear status report.

## 4. Goal

Perform a comprehensive review of the `corporate-legal` directory, files, and skills, mapping them against the upstream structure, and output a detailed status report.

## 5. Allowed Scope

Read-only access to:
- `corporate-legal/` directory and all contents inside it.
- Upstream baseline at `/Users/zhang/Documents/Playground/claude-for-legal-upstream/corporate-legal/` (if accessible) or downloads copy at `/Users/zhang/Downloads/claude-for-legal-main/corporate-legal/`.

## 6. Forbidden Actions

1. Do not modify any files (including skills, agents, or configs).
2. Do not create any files outside of `.codex-coordination/outbox/`.
3. Do not run any write or modification commands.
4. Do not stage or commit files.

## 7. Requirements

1. **Structure Audit**: Compare active skills in `corporate-legal/skills/` and suspended skills in `corporate-legal/phase-2/skills/` (M&A skills) against the upstream skills list. Identify any structural gaps.
2. **`customize` Skill Check**: Verify if the `customize` skill exists in CN corporate-legal. If not, verify what happened to the upstream `corporate-legal/skills/customize` and how it should be mapped under China law.
3. **CLAUDE.md Guardrails Check**: Verify if the corporate CLAUDE.md includes standard operational guardrails (reviewer notes, source provenance, no silent supplementation).
4. **Validation Check**: Run JSON syntax validation on corporate-legal JSON configurations.
5. **Output**: Write the findings to `.codex-coordination/outbox/TASK_010_CORPORATE_WRAPPER_REVIEW_RESULT.md`.

## 8. Acceptance Criteria

1. Audit results file is created in `.codex-coordination/outbox/TASK_010_CORPORATE_WRAPPER_REVIEW_RESULT.md`.
2. The results file contains a complete list of active/suspended corporate skills and matches them against upstream.
3. No files are modified or created outside of `.codex-coordination/outbox/`.

## 9. BLOCKED Rules

If the directory structure is missing or there are permission issues, stop and report BLOCKED.

## 10. DONE Report Format

Codex should report:
1. Status (DONE)
2. List of active skills and line counts
3. List of phase-2 M&A skills
4. Gaps identified against upstream
5. Validation result (JSON status)

## 11. Next Handoff Target

Gemini 3.5 Flash Review (replacing Claude)

## 12. Reason

To enable Gemini 3.5 Flash to review the audit results and decide whether to close Audit 04 or issue a recovery plan.
