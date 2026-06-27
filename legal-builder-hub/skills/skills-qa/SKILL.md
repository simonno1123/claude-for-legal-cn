---
name: skills-qa
description: >
  对法律技能进行中国法本土化质量审查，输出 P0/P1/P2 问题、文件级修正
  清单和是否允许进入默认 Marketplace 的结论。
argument-hint: "[技能或插件路径]"
---

# /legal-builder-hub:skills-qa

## 审查清单

### P0 阻断

- 默认使用美国法、普通法、英美证据特权或境外监管框架。
- 输出可能直接导致签署、提交、起诉、仲裁、解雇、付款或备案但没有人工确认门。
- 写入真实 API Key、Token、账号密码或商业数据库凭证。
- JSON 不可解析或技能 frontmatter 缺失。

### P1 重要

- 中国法规则缺口明显。
- 缺少 `references/test-cases-cn.md`。
- README、`.mcp.json`、技能描述不一致。
- 仍存在境外法律数据库、美国程序法、美国律师协会规范或美国引注规范等残留术语。

### P2 优化

- 输出模板不够本地化。
- 缺少地方差异提示。
- 缺少来源分层或引用待核查标记。

## 结论格式

```markdown
## Verdict

[PASS / PASS WITH CONDITIONS / FAIL]

## P0 Blocking Issues

## P1 Important Issues

## P2 Polish

## Recommended File-Level Actions

## Regression Cases Needed
```
