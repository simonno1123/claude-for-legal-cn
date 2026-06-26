---
name: use-case-triage
description: >
  中国个人信息处理活动初筛。判断新功能、营销活动、SDK 接入、AI 训练、员工数据处理或跨境共享是否可推进、需 PIPIA、需专项复核或应暂停。
argument-hint: "[处理活动说明/产品需求/数据流/SDK 或供应商说明]"
---

# /use-case-triage

## 强制规则

- 调用 `references/china-privacy-data-playbook.md`。
- 输出分类只能使用：`PROCEED`、`PIPIA REQUIRED`、`SPECIAL REVIEW`、`STOP`。
- 不得输出 GDPR DPIA、CCPA、US sectoral law 作为默认判断。

## 判断路径

1. 明确处理者身份、数据主体、个人信息类型、处理目的、处理方式、保存期限。
2. 检查是否涉及敏感个人信息、未成年人、自动化决策、委托处理、共同处理、对外提供、公开、跨境提供。
3. 检查告知同意、单独同意、最小必要、拒绝授权后可用性、撤回同意机制。
4. 检查是否与隐私政策、SDK 清单、App 权限、合同承诺不一致。
5. 如涉及重要数据、CII、境外传输、监管高压行业，标注专项复核。

## 输出格式

```markdown
# 个人信息处理活动初筛

> 来源：
> 法域：中国大陆 / [涉外因素]
> 待补材料：

## 结论
**CLASSIFICATION:** [PROCEED / PIPIA REQUIRED / SPECIAL REVIEW / STOP]

## 触发依据
| 触发项 | 是否命中 | 事实 | 处理要求 |
|---|---|---|---|

## 条件清单
- [ ] 告知/同意
- [ ] 单独同意
- [ ] PIPIA
- [ ] 第三方协议
- [ ] 隐私政策/SDK 清单更新
- [ ] 跨境专项复核

## 建议下一步
1. `/privacy-legal:pia-generation`
2. `/privacy-legal:dpa-review`
3. `/privacy-legal:policy-monitor`
```
