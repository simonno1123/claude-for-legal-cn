---
name: reg-gap-analysis
description: >
  中国 AI 新规、监管问答、标准、备案要求和执法案例差距分析。
argument-hint: "[法规/监管通报/标准/政策文本]"
---

# /reg-gap-analysis

## 强制规则

- 调用 `references/currency-watch.md` 和 `references/china-ai-governance-rules.md`。
- 仅使用中国官方或用户提供来源作中国结论；未核验时标注 `[待查证]`。

## 输出格式

```markdown
# 中国 AI 监管差距分析

> 文件状态：[现行有效/征求意见/标准/监管问答/执法案例]
> 待查证：

## 关键变化
| 条款/口径 | 变化 | 影响系统 | 风险 |
|---|---|---|---|

## 整改清单
| 差距 | 现状 | 要求 | 动作 | Owner |
|---|---|---|---|---|

## 需更新材料
- [ ] AI 台账
- [ ] AI 影响评估
- [ ] 供应商协议
- [ ] AI 使用制度
- [ ] 隐私政策/PIPIA
- [ ] 备案/安全评估材料
```
