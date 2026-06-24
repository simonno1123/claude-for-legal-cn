# inbound/ — 来函、来文与程序材料

本目录保存外部进入的法律材料：律师函、催告函、解除通知、法院文书、仲裁通知、协助执行通知、律师调查令、监管函、执行文书等。

## 目录结构

```
inbound/
└── [slug]/
    ├── incoming.pdf
    ├── triage.md
    └── response-v1.docx
```

## 命名

- `letter-acme-2026-04`
- `court-notice-beijing-2026-04`
- `investigation-order-platform-2026-04`
- `enforcement-assistance-2026-04`

## 工作流

| 类型 | 命令 | 输出 |
|---|---|---|
| 收到律师函/催告函 | `/litigation-legal:demand-received [path]` | 来函分析和回复选项 |
| 法院文书/调查令/协助执行 | `/litigation-legal:subpoena-triage [path]` | 文书甄别、期限和响应方案 |
| 形成正式案件 | `/litigation-legal:matter-intake` | 案件台账和案情文件 |
