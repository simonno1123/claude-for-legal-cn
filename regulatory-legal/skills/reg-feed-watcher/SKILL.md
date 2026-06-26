---
name: reg-feed-watcher
description: >
  中国官方监管动态摘要。按企业监管画像筛选法律法规、部门规章、地方规定、规范性文件、监管问答、执法案例和征求意见稿。
argument-hint: "[来源/日期范围/监管领域]"
---

# /reg-feed-watcher

## 强制规则

- 调用 `references/source-catalog.md`。
- 不使用 Federal Register、Regulations.gov 或美国 agency feed 作为默认来源。
- 未核验来源时标注 `[官方来源待查证]`。

## 输出格式

```markdown
# 中国监管动态摘要

## 高优先级
| 来源 | 文件/事项 | 状态 | 影响 | 动作 |
|---|---|---|---|---|

## 征求意见稿/草案

## 执法和监管问答

## 建议动作
- [ ] 运行 `/regulatory-legal:policy-diff`
- [ ] 建立 `/regulatory-legal:gaps` 整改项
- [ ] 评估是否提交意见 `/regulatory-legal:comments`
```
