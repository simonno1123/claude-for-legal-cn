---
name: cold-start-interview
description: >
  初始化中国法律技能构建中心画像，确认团队的技能来源、审查标准、MCP
  连接器、安全边界、发布流程和人工复核要求。
---

# /legal-builder-hub:cold-start-interview

## 访谈字段

- 团队角色：个人维护者、企业法务技术团队、律所知识管理团队、开源社区。
- 技能来源：本仓库、内部技能、外部社区、商业供应商。
- 默认法域：中国大陆；是否允许涉外扩展。
- 安装策略：仅允许白名单、允许人工审核后安装、实验环境可临时安装。
- MCP 策略：只允许环境变量占位，不保存真实凭证。
- 复核策略：是否需要 AI/人工复核包、是否需要双模型对比。
- 发布策略：是否需要回归测试、版本号、CHANGELOG、Git 提交。

## 输出

生成 `builder_profile`：

```yaml
builder_profile:
  default_jurisdiction: "China Mainland"
  install_policy: "review_required"
  mcp_credentials: "env_placeholders_only"
  required_checks:
    - json_parse
    - skill_frontmatter
    - mojibake_scan
    - us_common_law_residue_scan
    - test_cases_cn
  review_packet: true
```

