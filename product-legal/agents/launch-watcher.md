---
name: launch-watcher
description: >
  Phase 2 placeholder for China product-compliance launch monitoring. Not enabled as a Phase 1 default agent.
---

# Launch Watcher（Phase 2 暂缓）

本 agent 在 `product-legal` 中国化 Phase 1 中不作为正式能力启用。国内企业协同系统、产品排期系统和法务审批系统差异较大，第一阶段不默认自动读取上线清单。

## 当前处理

如用户需要上线清单筛查，请人工上传或粘贴 PRD、上线排期、营销活动表或产品需求清单，并运行：

```bash
/product-legal:launch-review
```

## 后续恢复条件

只有在企业明确配置飞书、企业微信、钉钉、WPS 或内部产品管理系统的 MCP 适配器后，才可恢复自动监控。

## 预警关键词

- 未成年人、儿童、学生、防沉迷、诱导消费；
- 个人信息、敏感个人信息、儿童个人信息、数据出境、画像、自动化决策、差别定价；
- 算法推荐、深度合成、生成式 AI、AI 标识、备案；
- 直播、达人、种草、广告、绝对化用语、第一、唯一、保证；
- 自动续费、会员、预付费、押金、优惠券、抽奖、限时折扣、划线价；
- 平台、商家入驻、排序推荐、评价、投诉、保证金、搭售、默认勾选；
- 硬件、质量、强制标准、CCC、召回、警示说明、三包；
- 医疗、药品、医疗器械、保健食品、金融、教育、游戏、电信。
