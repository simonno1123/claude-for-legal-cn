# TASK_020_PHASE1_5_ALIGNMENT_EDIT

STATUS: READY

FROM: ChatGPT

TO: Codex

MODE: EDIT

PROJECT:
`/Users/zhang/Documents/claude-for-legal-cn`

## OBJECTIVE

根据：

`TASK_019_PHASE1_5_WORKSPACE_RECOVERY_DECISION`

完成 Phase 1.5 已实现能力的项目状态对齐。

目标：使文档、回归检查和项目状态描述与当前实际实现一致。

本任务不新增 Phase 1.5 功能。

## ALLOWED PATHS

### Documentation

允许：

- `PHASE_2_ROADMAP.md`
- `docs/**`
- `CHINA_LOCALIZATION_STATUS.md`
- `PROJECT_USAGE_GUIDE.md`

### Regression

允许：

- `scripts/**`

### References

允许：

- `references/**`

## REQUIRED ACTIONS

### 1. Phase 1.5 状态同步

更新：

- Phase 1.5 工作流能力状态；
- Matter Workspace 状态；
- Local Workflow Contract 状态。

确保文档反映以下能力已经完成：

- local matter workspace；
- workflow lifecycle；
- YAML persistence；
- launch tracker；
- commercial workflow persistence。

禁止继续描述为：

- deferred；
- placeholder；
- future only。

### 2. Roadmap Alignment

更新 `PHASE_2_ROADMAP.md`。

要求明确：

- Phase 1.5：`Implemented / Active`；
- Phase 2：保持 `Future / Planned`。

避免阶段混淆。

### 3. Mapping Matrix Alignment

更新 `docs/UPSTREAM_MAPPING_MATRIX.md`。

要求区分：

- Upstream responsibility preserved；
- Future extension。

避免已实现能力被错误标记为缺失。

### 4. Regression Enhancement

检查 `scripts/**`。

如适当，增加 Phase 1.5 基础验证，包括：

- matter workspace 目录；
- YAML schema；
- lifecycle command；
- tracker 结构。

不得引入外部服务。

## FORBIDDEN

禁止：

- 新增 skill；
- 新增 workflow；
- 修改业务逻辑；
- 扩展 litigation execution；
- 执行衍生诉讼专项系统；
- MCP 接入；
- 北大法宝接入；
- 裁判文书接入；
- WPS API 接入；
- 外部系统连接；
- git add；
- git commit。

## OUTPUT

生成：

`.codex-coordination/outbox/TASK_020_PHASE1_5_ALIGNMENT_EDIT_RESULT.md`

RESULT 必须包含：

1. Modified Files
2. Documentation Changes
3. Regression Changes
4. Validation Results
5. Remaining Phase 2 Items
6. Commit Recommendation

## NEXT RECEIVER

```text
Codex RESULT
-> Gemini Review / Decision Layer
```
