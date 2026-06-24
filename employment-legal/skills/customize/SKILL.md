---
name: customize
description: >
  地方司法裁审口径与企业用工画像定制。用于在 cold-start-interview 之外补充北京、上海、广东、深圳、浙江等地方口径、社平工资、假期和仲裁时效差异；不再作为独立初始化入口。
argument-hint: "[省市/用工城市/需要定制的劳动法主题]"
---

# /customize

## 定位

`customize` 不再承担独立初始化入口。企业基础画像应通过 `/employment-legal:cold-start-interview` 建立；本技能仅用于补充地方裁审口径、社平工资、最低工资、病假工资、产假/育儿假、竞业限制补偿、仲裁时效等差异化配置。

## Instructions

1. 先读取 `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`。
2. 如未完成 cold-start，要求先运行 `/employment-legal:cold-start-interview`。
3. 采集并输出地方口径字段：
   - 用工城市、合同履行地、社保/公积金缴纳地；
   - 适用主题：解除、社保、工时、假期、竞业、双倍工资、年休假、病假工资；
   - 用户已提供的地方规定、裁判口径或律师意见；
   - 仍需查证的口径，统一标注 `[地方规定 - 待查证]`。
4. 不得编造地方规定或把一个城市口径套用于全国。

## 输出格式

```markdown
# 地方劳动法口径定制

## 1. 适用城市与场景

## 2. 已确认地方口径

## 3. 待查证地方口径

## 4. 对当前技能的影响
```
