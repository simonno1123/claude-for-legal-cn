# 国际企业可选连接器

以下配置来自原 `claude-for-legal` 项目，已从 `claude-for-legal-cn` 第一阶段主线 `.mcp.json` 中移除。外企、跨国企业或出海业务团队如确需 Slack、Google Drive、Box、iManage、CourtListener、Trellis、Westlaw/CoCounsel 等国际系统，可参考本文件自行复制到本地 MCP 配置。

> 注意：这些连接器不构成中国版默认法律资料源。涉及中国法律结论时，仍应优先使用国家法律法规数据库、中国监管机关官网、北大法宝、威科先行、法信、Alpha、裁判文书网等中国资料源。

## commercial-legal

```json
{
  "mcpServers": {
    "Ironclad": {
      "type": "http",
      "url": "https://mcp.na1.ironcladapp.com/mcp",
      "title": "Ironclad",
      "description": "Search your contract repository and workflows using plain language — expiring MSAs, termination clauses, vendor agreements — scoped to your permissions."
    },
    "DocuSign": {
      "type": "http",
      "url": "https://mcp.docusign.com/mcp",
      "title": "DocuSign",
      "description": "Agreement search, status tracking, and signature workflows."
    },
    "iManage": {
      "type": "http",
      "url": "https://cloudimanage.com/mcp/work",
      "title": "iManage",
      "description": "Governed iManage content connected to Claude — documents stay in iManage, access is permission-bound and auditable."
    },
    "TopCounsel": {
      "type": "http",
      "url": "https://api.techgc.co/api/mcp/topcounsel",
      "title": "TopCounsel",
      "description": "Outside counsel recommendations from The L Suite — 5,000+ in-house counsel community sentiment, rankings, and expertise evidence."
    },
    "Definely": {
      "type": "http",
      "url": "https://mcp.uk.definely.com/api/proxy/core-mcp",
      "title": "Definely",
      "description": "Live, deterministic access to contract structure — resolve definitions, validate cross-references, map dependencies, run structural diffs."
    },
    "Slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp",
      "title": "Slack",
      "description": "Search messages, read channels, find discussions across your workspace."
    },
    "Google Drive": {
      "type": "http",
      "url": "https://drivemcp.googleapis.com/mcp/v1",
      "title": "Google Drive",
      "description": "Search, read, and fetch documents from Google Drive."
    }
  }
}
```

## privacy-legal

```json
{
  "mcpServers": {
    "Slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp",
      "title": "Slack",
      "description": "Search messages, read channels, find discussions across your workspace."
    },
    "Google Drive": {
      "type": "http",
      "url": "https://drivemcp.googleapis.com/mcp/v1",
      "title": "Google Drive",
      "description": "Search, read, and fetch documents from Google Drive."
    }
  }
}
```

## corporate-legal

```json
{
  "mcpServers": {
    "Slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp",
      "title": "Slack",
      "description": "Search messages, read channels, find discussions across your workspace."
    },
    "Google Drive": {
      "type": "http",
      "url": "https://drivemcp.googleapis.com/mcp/v1",
      "title": "Google Drive",
      "description": "Search, read, and fetch documents from Google Drive."
    },
    "Box": {
      "type": "http",
      "url": "https://mcp.box.com/mcp",
      "title": "Box",
      "description": "Data room and document management."
    },
    "iManage": {
      "type": "http",
      "url": "https://cloudimanage.com/mcp/work",
      "title": "iManage",
      "description": "Governed iManage content connected to Claude — documents stay in iManage, access is permission-bound and auditable."
    },
    "TopCounsel": {
      "type": "http",
      "url": "https://api.techgc.co/api/mcp/topcounsel",
      "title": "TopCounsel",
      "description": "Outside counsel recommendations from The L Suite — 5,000+ in-house counsel community sentiment, rankings, and expertise evidence."
    },
    "Definely": {
      "type": "http",
      "url": "https://mcp.uk.definely.com/api/proxy/core-mcp",
      "title": "Definely",
      "description": "Live, deterministic access to contract structure — resolve definitions, validate cross-references, map dependencies, run structural diffs."
    },
    "Solve Intelligence": {
      "type": "http",
      "url": "https://api.solveintelligence.com/mcp/",
      "title": "Solve Intelligence",
      "description": "Patent workflows — search patent and non-patent literature, legal texts, SEP technical standards, prior art, claim analysis."
    }
  }
}
```

## employment-legal

```json
{
  "mcpServers": {
    "Slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp",
      "title": "Slack",
      "description": "Search messages, read channels, find discussions across your workspace."
    },
    "Google Drive": {
      "type": "http",
      "url": "https://drivemcp.googleapis.com/mcp/v1",
      "title": "Google Drive",
      "description": "Search, read, and fetch documents from Google Drive."
    }
  }
}
```

## product-legal

```json
{
  "mcpServers": {
    "Slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp",
      "title": "Slack",
      "description": "Search messages, read channels, find discussions across your workspace."
    },
    "Google Drive": {
      "type": "http",
      "url": "https://drivemcp.googleapis.com/mcp/v1",
      "title": "Google Drive",
      "description": "Search, read, and fetch documents from Google Drive."
    },
    "Linear": {
      "type": "http",
      "url": "https://mcp.linear.app/mcp",
      "title": "Linear",
      "description": "Issue tracking and project management."
    },
    "Atlassian": {
      "type": "http",
      "url": "https://mcp.atlassian.com/v1/sse",
      "title": "Atlassian",
      "description": "Jira issues and Confluence pages."
    },
    "Asana": {
      "type": "http",
      "url": "https://mcp.asana.com/sse",
      "title": "Asana",
      "description": "Tasks and project tracking."
    }
  }
}
```

## regulatory-legal

```json
{
  "mcpServers": {
    "Slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp",
      "title": "Slack",
      "description": "Search messages, read channels, find discussions across your workspace."
    },
    "Google Drive": {
      "type": "http",
      "url": "https://drivemcp.googleapis.com/mcp/v1",
      "title": "Google Drive",
      "description": "Search, read, and fetch documents from Google Drive."
    }
  }
}
```

## ai-governance-legal

```json
{
  "mcpServers": {
    "Slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp",
      "title": "Slack",
      "description": "Search messages, read channels, find discussions across your workspace."
    },
    "Google Drive": {
      "type": "http",
      "url": "https://drivemcp.googleapis.com/mcp/v1",
      "title": "Google Drive",
      "description": "Search, read, and fetch documents from Google Drive."
    }
  }
}
```

## ip-legal

```json
{
  "mcpServers": {
    "Solve Intelligence": {
      "type": "http",
      "url": "https://api.solveintelligence.com/mcp/",
      "title": "Solve Intelligence",
      "description": "Patent workflows — search patent and non-patent literature, legal texts, SEP technical standards, prior art, claim analysis."
    },
    "CourtListener": {
      "type": "http",
      "url": "https://mcp.courtlistener.com/",
      "title": "CourtListener",
      "description": "Free Law Project's legal research platform — millions of U.S. court opinions, PACER dockets, judge profiles, oral arguments, and citation verification."
    },
    "Descrybe": {
      "type": "http",
      "url": "https://mcp.descrybe.com/mcp",
      "title": "Descrybe",
      "description": "Primary law research — search cases by concept or wording, find cases from citations, extract authorities, check treatment, verify quoted language."
    },
    "Slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp",
      "title": "Slack",
      "description": "Search messages, read channels, find discussions across your workspace."
    },
    "Google Drive": {
      "type": "http",
      "url": "https://drivemcp.googleapis.com/mcp/v1",
      "title": "Google Drive",
      "description": "Search, read, and fetch documents from Google Drive."
    }
  }
}
```

## litigation-legal

```json
{
  "mcpServers": {
    "Slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp",
      "title": "Slack",
      "description": "Search messages, read channels, find discussions across your workspace."
    },
    "Google Drive": {
      "type": "http",
      "url": "https://drivemcp.googleapis.com/mcp/v1",
      "title": "Google Drive",
      "description": "Search, read, and fetch documents from Google Drive."
    },
    "Everlaw": {
      "type": "http",
      "url": "https://api.everlaw.com/v1/mcp",
      "title": "Everlaw",
      "description": "Search, organize, and retrieve documents from your Everlaw projects — metadata, keywords, document types — with review links."
    },
    "TopCounsel": {
      "type": "http",
      "url": "https://api.techgc.co/api/mcp/topcounsel",
      "title": "TopCounsel",
      "description": "Outside counsel recommendations from The L Suite — 5,000+ in-house counsel community sentiment, rankings, and expertise evidence."
    },
    "CourtListener": {
      "type": "http",
      "url": "https://mcp.courtlistener.com/",
      "title": "CourtListener",
      "description": "Free Law Project's legal research platform — millions of U.S. court opinions, PACER dockets, judge profiles, oral arguments, and citation verification."
    },
    "Aurora": {
      "type": "http",
      "url": "https://mcp.ai.consilio.com",
      "title": "Aurora",
      "description": "Read-only Consilio ediscovery — find matters, list workspaces, full-text search, AI-powered cross-matter investigations, every record cited to source."
    },
    "Trellis": {
      "type": "http",
      "url": "https://mcp.trellis.law/anthropic",
      "title": "Trellis",
      "description": "The largest state trial court dataset in the U.S. — dockets, rulings, verdicts, filings, judge and opposing counsel analytics, expert witness vetting."
    }
  }
}
```

