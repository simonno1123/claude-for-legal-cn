# 跨模型复核改在 GitHub PR 上进行（决定记录）

| 字段 | 值 |
| --- | --- |
| 所有者 | 张纯熙 |
| 日期 | 2026-11-12 |
| 选择 | "改用 PR 评审（推荐）" |
| 试行 | PR #112：V8 设计 R1 经 Codex 评审为 FAIL，改为 R2 后评审未发现问题 |

## 做法

1. 记录人把待审文件放在功能分支的 PR 中，在 PR 里评论 `@codex review`，写明审查对象和要求。触发评论以所有者的 GitHub 账号发出，评论中注明"由 Claude 代所有者账号发出"。
2. Codex 按 `AGENTS.md` 的 Code Review Rules 在 PR 上评审：用中文，标注 BLOCKING／NON-BLOCKING，给出结论。
3. 记录人读取评审意见，修改后再次触发评审。评审原文转存到 `.codex-coordination/outbox/`。
4. 所有者不再需要复制粘贴。采纳、关闭、授权仍由所有者决定。

## 局限

- GitHub 评审只报 P0 和 P1 级问题，内容比长篇任务报告简略。
- `.codex-coordination/inbox/` 的任务文件仍可作为长篇复核的备用途径。
