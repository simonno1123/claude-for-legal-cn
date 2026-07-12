# Codex Task

## 1. Task ID

TASK_015_LAW_STUDENT_UPGRADE_EDIT

## 2. Status

READY

## 3. Background

The initial audit `TASK_014_LAW_STUDENT_UPGRADE` has rejected the current `phase-2/law-student` state. While the China-law legal domain directions are correct, it suffers from two major blockers:
1. Directory/command discoverability is missing (lives under `phase-2/` and is hidden from `marketplace.json`).
2. Core upstream "learning mode" responsibilities and stateful workflows (academic integrity, ask-wait-pushback, progress plan persistence, session history) have been compressed out.

This task is an EDIT task to physically promote the module, register it in the marketplace, and fully restore its stateful learning capabilities while aligning the substance to China-law education contexts.

## 4. Goal

Physically migrate `phase-2/law-student` to the root, register it, and restore stateful learning-mode logic to all 13 skill files under China-law context.

## 5. Allowed Scope

Allowed to read/write:
- `phase-2/law-student/**` (for migration)
- `law-student/**` (for target directory promotion)
- `.claude-plugin/marketplace.json` (for registering the plugin)

## 6. Forbidden Actions

1. Do not modify files in other plugins.
2. Do not delete existing China-law concepts (法考, 请求权基础, 中国案例研习, etc.).
3. Do not perform `git commit` or `git add`.

## 7. Requirements

### 1. Structural Migration & Registration (P0)
- **Move Module**: Migrate all files from `phase-2/law-student/` to root-level `law-student/`. (Delete the source `phase-2/law-student/` directory or its contents after move to ensure no duplicate tracking).
- **Register Plugin**: Modify `.claude-plugin/marketplace.json`. Add the promoted `law-student` plugin to the marketplace list:
  ```json
  {
    "name": "law-student",
    "displayName": "法学生助手 (Law Student Assistant)",
    "description": "提供中国法考备考、请求权基础训练、民商事案例研习与苏格拉底提问式辅导。",
    "source": "./law-student"
  }
  ```

### 2. CLAUDE.md & Academic Integrity Restoration (P0)
- Rewrite `law-student/CLAUDE.md` and `README.md` to state:
  - Output is study scaffolding, never a model answer.
  - Strict academic integrity / anti-ghostwriting rules (never rewrite essays/opinions, only give structural feedback).
  - Hypotheticals vs. real disputes redirect (real disputes must route to `legal-clinic` or licensed attorneys).

### 3. Stateful Study Profiling & Tracking (P1)
- **`cold-start-interview`**: Collect student role (法考考生 / 实习律师 / 在校生), school, target exam date, weak subjects, and allow loading local training materials. Initialize state files.
- **`study-plan`**: Read and write local `study-plan.yaml`. Support `build | update | status | cram` modes. Calculate weak-subject weights based on session history.
- **`session`**: Run sessions tracking objective/subjective practice, and append to local `session_history` log.

### 4. Rebuild Learning-Mode and Socratic Workflows (P1)
- **`socratic-drill` & `cold-call-prep`**: Enforce an interactive "Ask-Wait-Pushback" workflow. The model must ask one question, wait for student input, and then critique/ask follow-ups. It must never dump all answers at once.
- **`legal-writing` & `irac-practice`**: Restrict behavior to structural, elements-based, and citation critiques. Prohibit rewriting or writing assignments for the student.

### 5. Localized Skill Depth (P1)
- **`bar-prep-questions`**: Focus strictly on China's National Unified Legal Qualification Exam (法考). Support objective/subjective question structures, grading rubrics, and wrong-item explanations.
- **`case-brief`**: Map to Chinese civil/commercial Case Study (案例研习): 案情要点, 争议焦点, 请求权基础/构成要件, 证明责任, 裁判要旨, 类案检索要点.
- **`outline-builder`**: Structure review outlines based on Chinese codified law, statutory hierarchy, and judicial interpretations.

## 8. Acceptance Criteria

1. `law-student/` directory exists at root and contains all 13 skill folders.
2. `phase-2/law-student` source files are removed/migrated.
3. `.claude-plugin/marketplace.json` successfully registers the root `law-student` plugin.
4. Each skill file contains stateful behavioral instructions or interactive rules (YAML/JSON tracking, ask-wait flow, anti-ghostwriting gates).
5. Validation command `python3 -c "import json; json.load(open('law-student/.claude-plugin/plugin.json'))"` passes.

## 9. BLOCKED Rules

If directory move fails due to permission errors, stop and report BLOCKED.

## 10. DONE Report Format

Codex should report:
1. Status (DONE)
2. Files moved and modified
3. Summary of restored capabilities
4. Validation results

## 11. Next Handoff Target

Gemini

## 12. Reason

To enable Gemini to review the promoted and upgraded law-student module.
