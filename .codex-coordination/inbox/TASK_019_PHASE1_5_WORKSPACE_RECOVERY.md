# ACOS Task Artifact

## 1. Identity

```text
TASK ID: TASK_019_PHASE1_5_WORKSPACE_RECOVERY
ARTIFACT TYPE: TASK
PRODUCER: ChatGPT
TO: Codex
NEXT RECEIVER: Codex
MODE: REVIEW_AND_CONTINUE_EDIT
PROJECT: /Users/zhang/Documents/claude-for-legal-cn
```

## 2. Workflow State

```text
Task File: CREATED
Execution: PENDING
Reviewer: PENDING
Decision: PENDING
```

## 3. Background

Prior to this task, several modifications relating to the Phase 1.5 Local Workflow Layer (including matter-workspaces, launch-tracker, and local workflow contracts) were introduced directly into the working tree. This bypasses the strict ACOS lifecycle (Task -> Result -> Review -> Decision -> Commit).

To repair this process drift, this task is initialized as a **REVIEW_AND_CONTINUE_EDIT** task. Codex must inventory the existing working-tree changes, check them against the Phase 1.5 scope boundaries, perform necessary adjustments to align them, and write a detailed RESULT report.

## 4. Allowed Scope

Codex is authorized to read and write:
- `commercial-legal/**`
- `employment-legal/**`
- `ip-legal/**`
- `privacy-legal/**`
- `product-legal/**`
- `docs/PHASE1_BASELINE_REVIEW.md`
- `references/local-workflow-contract.md`
- `.codex-coordination/`

No edits outside these paths are allowed.

## 5. Objectives & Requirements

### 1. Existing Changes Inventory & Audit (B-1)
- Run `git status` and `git diff` to compile a complete list of all currently modified and untracked files.
- Document the purpose of each change.

### 2. Scope Classification & Verification (B-2)
- Verify whether each change belongs strictly to the **Phase 1.5 Legal Workflow Layer** scope:
  - Matter Workspaces (`new/list/switch/close/none` lifecycle) using local YAML/JSON file persistence.
  - Local workflow trackers (like `launch-tracker`).
  - Company/practice profiles or local file-based context logs.
- Identify and flag any changes that cross into **Phase 2** (external database MCP integration, live APIs, automatic third-party notifications, package managers). If such items are found, mark them for removal or modification.

### 3. Continuation of Edit (B-3)
- Ensure that the workspace skills across all 5 modules (`commercial`, `privacy`, `employment`, `product`, `ip`) correctly implement the local matter lifecycle and YAML/JSON context persistence.
- Align description texts and commands to the ACOS standard.

### 4. Output Validation (B-4)
- Run JSON and YAML validations on all modified files.
- Run `python3 scripts/localization-regression.py` to ensure CI tests still pass and no regressions occur.

## 6. Output Result Format

Codex must output the following RESULT file:
`.codex-coordination/outbox/TASK_019_PHASE1_5_WORKSPACE_RECOVERY_RESULT.md`

The result must contain:
1. **Status**: DONE or BLOCKED.
2. **Existing Changes Inventory**: List of files and audit of modifications.
3. **Scope Classification**: Statement confirming compliance with Phase 1.5 boundaries.
4. **Required Adjustments / Remaining Work**: Actions taken or required to achieve clean alignment.
5. **Validation Results**: Command outputs (CI regression, JSON/YAML lint).
6. **Commit Recommendation**: Should be `HOLD` pending Gemini Review/Decision.

## 7. Next Handoff

```text
Codex RESULT
→ Gemini Review / Decision Layer
```

No git commit or git push is permitted before the final Gemini Decision.
