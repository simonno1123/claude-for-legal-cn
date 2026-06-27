---
name: customize
description: >
  局部更新中国法律技能构建中心配置。初始化入口仍以 cold-start-interview 为准。
---

# /legal-builder-hub:customize

用于修改已存在的 `builder_profile`，例如新增允许的 MCP 连接器、调整复核门槛、增加白名单来源或变更发布流程。

不得降低以下硬门槛：

- 中国大陆默认法域。
- 无真实凭证入库。
- JSON/frontmatter/乱码检查。
- 美国法默认框架残留扫描。
- 人工复核门。

