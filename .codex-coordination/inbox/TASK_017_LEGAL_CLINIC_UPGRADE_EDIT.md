# Codex Task

## 1. Task ID

TASK_017_LEGAL_CLINIC_UPGRADE_EDIT

## 2. Status

READY

## 3. Background

The initial audit `TASK_016_LEGAL_CLINIC_AUDIT` has rejected the current `phase-2/legal-clinic` state. While the Chinese legal aid / college legal clinic concept alignments are correct, it suffers from two major blockers:
1. Directory/command discoverability is missing (lives under `phase-2/` and is hidden from `marketplace.json`).
2. Core upstream stateful workflows (deadlines ledger tracking, supervisor review queue, client intake routing, semester handoff) have been compressed into static checklists.

This task is an EDIT task to physically promote the module, register it in the marketplace, clean up related documentation paths, and fully restore its stateful clinic capabilities while aligning the substance to China-law public legal services and clinic education contexts.

## 4. Goal

Physically migrate `phase-2/legal-clinic` to the root, register it, correct documentation references, and restore stateful logic to all 16 skill files under China-law context.

## 5. Allowed Scope

Allowed to read/write:
- `phase-2/legal-clinic/**` (for migration source)
- `legal-clinic/**` (for target directory promotion)
- `.claude-plugin/marketplace.json` (for registering the plugin)
- `PROJECT_USAGE_GUIDE.md` (for updating law-student and legal-clinic references)
- `docs/UPSTREAM_MAPPING_MATRIX.md` (for updating law-student and legal-clinic references)

## 6. Forbidden Actions

1. Do not modify files in other plugins.
2. Do not delete existing China-law concepts.
3. Do not perform `git commit` or `git add`.

## 7. Requirements

### 1. Structural Migration & Registration (P0)
- **Move Module**: Migrate all files from `phase-2/legal-clinic/` to root-level `legal-clinic/`. (Delete the source `phase-2/legal-clinic/` directory or its contents after move to ensure no duplicate tracking).
- **Register Plugin**: Modify `.claude-plugin/marketplace.json`. Add the promoted `legal-clinic` plugin to the marketplace list:
  ```json
  {
    "name": "legal-clinic",
    "displayName": "法律诊所与援助 (Legal Clinic & Aid)",
    "source": "./legal-clinic",
    "description": "提供中国高校法律诊所、基层法律援助中心、12348公共法律服务时效台账与导师审查流。"
  }
  ```

### 2. Documentation Path Alignment (P0 - 特批)
- Modify `PROJECT_USAGE_GUIDE.md` and `docs/UPSTREAM_MAPPING_MATRIX.md`.
- Replace all occurrences of `phase-2/law-student` with `law-student` and `phase-2/legal-clinic` with `legal-clinic` to clean up historical directory residues.

### 3. Stateful Timelines & Review Queue Restoration (P0)
- **`deadlines`**: Read and write local `deadlines-ledger.yaml`. Support CRUD (`add | report | update | complete | close`) actions for tracking procedural timelines (e.g. appeal date, evidence deadline, labor arbitration statute of limitations). Ensure warning logs are generated for close deadlines.
- **`supervisor-review-queue`**: Read and write local `review-queue.yaml`. Define strict states (`pending_review | approved | returned_with_comments`). Restrict student outputs: no communication or brief may be finalized without supervisor approval.
- **`CLAUDE.md` & `README.md`**: Update to include strict supervisor approval gates, local timeline tracking rules, and China Mainland default jurisdiction.

### 4. Client Intake & Handoff Restoration (P1)
- **`client-intake`**: Spot conflicts, perform preliminary legal aid criteria check (economic difficulties, case scope under the PRC Legal Aid Law), and require mandatory deadline handoff mapping.
- **`semester-handoff`**: Generate case handoff memos and class-level status summaries based on active deadlines and records.
- **`cold-start-interview`**: Collect clinic profile (type, supervisor name, student roster) and initialize local database paths.

### 5. Localized Skill Depth (P1)
- Map all other skills (`status`, `memo`, `draft`, `research-start`, `client-comms-log`, `ramp`, `form-generation`, `plain-language-letters`) to China litigation/aid procedures (e.g., attorney representation, court filing, service of process, execution, etc.) with detailed instructions.

## 8. Acceptance Criteria

1. `legal-clinic/` directory exists at root and contains all 16 skill folders.
2. `phase-2/legal-clinic` source files are removed/migrated.
3. `.claude-plugin/marketplace.json` successfully registers the root `legal-clinic` plugin.
4. Old `phase-2/` references are cleared from `PROJECT_USAGE_GUIDE.md` and `docs/UPSTREAM_MAPPING_MATRIX.md`.
5. Each skill file contains stateful behavioral instructions (YAML/JSON tracking, supervisor approval loops, deadlines ledger writes).
6. Validation command `python3 -c "import json; json.load(open('legal-clinic/.claude-plugin/plugin.json'))"` passes.

## 9. BLOCKED Rules

If directory move fails due to permission errors, stop and report BLOCKED.

## 10. DONE Report Format

Codex should report:
1. Status (DONE)
2. Files moved, created, and modified
3. Summary of restored capabilities
4. Validation results

## 11. Next Handoff Target

Gemini

## 12. Reason

To enable Gemini to review the promoted and upgraded legal-clinic module.
