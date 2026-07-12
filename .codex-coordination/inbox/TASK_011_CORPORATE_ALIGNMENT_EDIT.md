# Codex Task

## 1. Task ID

TASK_011_CORPORATE_ALIGNMENT_EDIT

## 2. Status

READY

## 3. Background

Following the wrapper review under `TASK_010`, the `corporate-legal` module has been accepted with conditions. This task is an EDIT task to resolve two minor gaps identified during review: a wording conflict in cold-start interview regarding the `customize` command, and the absence of an explicit "No Silent Supplementation" section in `CLAUDE.md`.

## 4. Goal

Resolve the cold-start interview wording conflict and add the explicit "No Silent Supplementation" section to the corporate CLAUDE.md.

## 5. Allowed Scope

Allowed to modify:
- `corporate-legal/CLAUDE.md`
- `corporate-legal/skills/cold-start-interview/SKILL.md`

## 6. Forbidden Actions

1. Do not modify other plugins or other skills.
2. Do not create new files.
3. Do not run any Git commands such as add or commit.

## 7. Requirements

### 1. Wording Conflict Fix in `cold-start-interview/SKILL.md`
- Modify the file `corporate-legal/skills/cold-start-interview/SKILL.md`.
- Replace the line:
  `- 不得另设 \`customize\` 配置入口；company_profile 必须由本技能统一生成和更新。`
  with:
  `- 不得另设配置存储源；公司画像（company_profile）必须统一保存在插件的根配置文件中，其自定义更新可通过 /corporate-legal:customize 入口提出建议并由用户确认。`

### 2. Guardrail Hardening in `corporate-legal/CLAUDE.md`
- Modify the file `corporate-legal/CLAUDE.md`.
- Add a new section before `## 公司画像` (around L87):
  ```markdown
  ## No Silent Supplementation

  1. 禁止在未核验法条、注册登记口径或具体章程规则的前提下，自行编造或默认填充事实。
  2. 确有必要提供参考示例时，必须在文本中明确标注 `[待核验]` 或 `[示例建议]`。
  ```

## 8. Acceptance Criteria

1. Both target files are modified exactly according to the requirements.
2. Wording conflict in `cold-start-interview/SKILL.md` is resolved.
3. Explicit "No Silent Supplementation" section exists in `corporate-legal/CLAUDE.md`.
4. Validation command `python3 -c "import json; json.load(open('corporate-legal/.claude-plugin/plugin.json'))"` passes.
5. No changes are staged or committed.

## 9. BLOCKED Rules

If any conflict occurs or file contents differ from requirements, stop and report BLOCKED.

## 10. DONE Report Format

Codex should report:
1. Status (DONE)
2. Files modified
3. Summary of text changes
4. Validation results

## 11. Next Handoff Target

Gemini 3.5 Flash Review (replacing Claude)

## 12. Reason

To enable Gemini 3.5 Flash to review the edits and close Audit 04.
