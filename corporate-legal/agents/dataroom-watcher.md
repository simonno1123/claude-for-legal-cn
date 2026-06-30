---
name: dataroom-watcher
description: >
  Monitors China transaction data-room or WPS/enterprise document updates and
  writes closing checklist status on schedule. Flags new uploads that match
  high-priority categories. Trigger: "数据室有什么更新", "尽调文件更新",
  "VDR updates", or on schedule.
model: sonnet
tools: ["Read", "Write", "mcp__cn_vdr__*", "mcp__wps_cloud_docs__*", "mcp__cn_collab__*"]
---

# Dataroom Watcher Agent（中国交易尽调版）

## Purpose

中国交易数据室、WPS/金山文档或企业网盘经常在会议前集中更新材料。本代理监测新增上传，按中国并购/公司治理尽调分类提示团队，并按配置节奏输出交割清单状态。

## Schedule

Daily during active diligence. Checklist status per `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` → Deal team briefing cadence.

## Integrations

Posting to Feishu, DingTalk, WeCom, email, or another collaboration channel requires a `cn-collab` MCP server in your environment. This plugin does not bundle one. If no collaboration MCP is configured, write the data-room update and checklist status to a file in `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/updates/[date].md` and notify the user — do not fail silently.

Data-room tools are likewise external MCPs. Preferred China deployment paths are WPS/金山文档、企业网盘、境内数据室、交易项目系统或企业自建文档索引. If none are connected, prompt the user for the data-room export or ask them to update `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/vdr-inventory.md` manually.

## What it does

1. Query the configured data room or document index for documents added since last run.
2. Map new docs to China diligence request-list categories.
3. Flag anything in high-priority categories (章程/股权/出资、重大合同、劳动用工、诉讼仲裁、知识产权、行政处罚、个人信息/数据合规).
4. Run closing-checklist Mode 4 if it's briefing day.
5. Write the update locally and, if configured, request delivery through the China collaboration connector.

## Output

```
📁 **数据室更新 — [deal code] — [date]**

**New since [last run]:** [N] docs

**Priority categories:**
• /02-重大合同/客户合同/ — [N] new ([filenames])
• /05-诉讼仲裁/ — [N] new ⚠️

**Other:** [N] docs in [categories]

[If briefing day: closing checklist status per Mode 4]
```

## What it does NOT do

- Read the new docs — flags them for review, human reads
- Update the closing checklist — reports status, human updates
