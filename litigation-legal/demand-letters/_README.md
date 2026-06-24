# demand-letters/ — 律师函与催告函工作区

本目录保存对外发送的律师函、催告函、索赔函、解除通知、保全提示函和后续清单。

## 目录结构

```
demand-letters/
└── [slug]/
    ├── intake.md
    ├── draft-v1.docx
    └── checklist.md
```

## 工作流

1. `/litigation-legal:demand-intake [title]`：采集事实、证据、金额、送达和时效信息。
2. `/litigation-legal:demand-draft [slug]`：生成中国法语境下的函件初稿和发送前清单。
3. 重大事项转入 `/litigation-legal:matter-intake`。

## 注意

- 对外发送前必须律师/法务复核。
- 不得把内部法律分析、商业秘密、个人信息或未经核实的不利事实写入对外函件。
- 送达证据需要留存，用于后续诉讼时效中断、催告履行或解除通知证明。
