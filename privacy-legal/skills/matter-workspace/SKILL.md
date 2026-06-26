---
name: matter-workspace
description: >
  以处理活动、产品功能、供应商、跨境项目或安全事件为单位建立中国数据合规工作台。
argument-hint: "[项目名称/处理活动/供应商/事件]"
---

# /matter-workspace

## 强制规则

- 工作台只做材料组织、状态跟踪和输出索引，不自动提交、发送、删除、签署或关闭事项。
- 默认按“中国个人信息处理活动”建档，而不是按 US/EU matter 或 privilege log 建档。

## 建档内容

- 项目名称、业务负责人、法务/隐私/安全负责人。
- 处理活动说明、数据地图、系统清单、第三方和跨境路径。
- 关联输出：triage、PIPIA、dpa-review、policy-monitor、reg-gap-analysis、dsar-response。
- 风险等级、整改动作、审批记录和复核状态。

## 输出格式

```markdown
# 数据合规工作台

## 基本信息
- 项目：
- 处理活动：
- Owner：
- 状态：

## 材料索引
| 材料 | 版本 | 来源 | 状态 |
|---|---|---|---|

## 风险与动作
| 风险 | 等级 | 动作 | Owner | 截止日期 |
|---|---|---|---|---|

## 关联命令
- `/privacy-legal:use-case-triage`
- `/privacy-legal:pia-generation`
- `/privacy-legal:dpa-review`
- `/privacy-legal:policy-monitor`
```
