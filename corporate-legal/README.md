# 公司法律事务插件（中国新公司法版）

面向中国企业法务、董办、股东、高管和外部律师的公司治理、章程旧转新、出资责任、股权变动、实体合规和市场监管登记事项工作流。第一批深改以 2024 年 7 月 1 日施行的新修订《中华人民共和国公司法》为核心基准。

> **专业提示：** 本插件输出均为公司法律工作初稿，必须由中国执业律师或企业法务复核。涉及章程修改、登记备案、股权转让、股权质押、出资追责、董监高责任或对外承诺前，不得直接依赖模型输出执行。

## 核心卡点

- 不再默认套用 Delaware、Board Consent、Bylaws、Stockholder Consent、LLC 等美国公司法框架。
- 新公司法下公司治理先识别公司类型、章程、股东会、董事会/董事、经理层、监事会/监事或审计委员会。
- 对职工人数三百人以上公司的职工董事/职工监事设置进行强制审查。
- 对有限责任公司五年出资期、出资加速到期和未届期股权转让责任进行强制审查。
- 对股权转让的书面通知、优先购买权、送达留痕，以及股权质押市场监管出质登记进行强制审查。

## 首次运行

```bash
/corporate-legal:cold-start-interview
```

配置文件存放于：

```text
~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md
```

## 技能矩阵

| Skill | 用途 |
|---|---|
| `/corporate-legal:cold-start-interview` | 建立中国公司画像：公司类型、注册地、章程、治理结构、股东出资、股权登记、国资/外资/上市等特殊监管 |
| `/corporate-legal:articles-of-association-audit` | 新公司法章程旧转新全量审计，输出章程修改对照表建议稿 |
| `/corporate-legal:governance-audit` | 新公司法“三会一层”治理审计：三百人职工董事红线、审计委员会平替、影子董事责任、董监高义务 |
| `/corporate-legal:capital-contribution-audit` | 股东出资期限、五年出资期、出资加速到期、未届期股权转让责任审计 |
| `/corporate-legal:equity-transfer-pledge-review` | 股权转让、优先购买权通知、股权质押和市场监管出质登记审查 |
| `/corporate-legal:board-minutes` | 股东会、董事会、监事会或审计委员会会议记录/纪要草案 |
| `/corporate-legal:written-consent` | 中国公司书面决议/传签决议审查与草案，先判断章程和事项是否允许书面决议 |
| `/corporate-legal:entity-compliance` | 实体合规台账、登记事项、年度报告、章程/登记健康检查 |
| `/corporate-legal:matter-workspace` | 多事项工作区管理 |

## 第一批深改状态

已完成：

- 插件级 `CLAUDE.md` 注入中国新公司法 System Alignment。
- `board-minutes` 从董事会会议纪要模板改为中国股东会/董事会/监事会/审计委员会会议记录。
- `written-consent` 从美国 unanimous written consent 改为中国书面决议/传签决议审查。
- `cold-start-interview` 已改成中国公司画像访谈。
- `entity-compliance` 已改成市场监管、年报、章程、登记事项合规台账。
- 新增 `articles-of-association-audit` 章程旧转新全量审计。
- 重写 `governance-audit` 为新公司法“三会一层”内部治理审计，强制覆盖三百人职工董事红线、审计委员会平替机制和影子董事连带责任。
- 重写 `capital-contribution-audit`，强制覆盖五年出资期、出资加速到期、第88条责任分流和董事催缴责任。
- 新增 `equity-transfer-pledge-review`。
- 新增 `references/test-cases-cn.md` 作为公司法 Prompt 回归测试靶场。
- 新增 `references/articles-old-to-new.md` 作为章程旧法残留到新公司法口径的强制替换表。

## Phase 1.5 规划：并购与投融资交易

M&A / 投融资相关技能已暂移至 `phase-2/skills/`，不作为公司法第一阶段主线入口。后续将在公司治理、章程、出资和股权底座稳定后，按中国股权/资产交易、国资/外资/反垄断、税务和登记交割逻辑重写：

- `diligence-issue-extraction`
- `tabular-review`
- `deal-team-summary`
- `material-contract-schedule`
- `closing-checklist`
- `integration-management`
- `ai-tool-handoff`

## 数据和材料

优先提供：

- 营业执照、公司章程、股东名册、出资证明书。
- 验资/出资凭证、银行流水、财务报表、债务清单。
- 历次股权转让协议、质押合同、市场监管登记材料。
- 股东会/董事会/监事会/审计委员会会议记录和决议。
- 国资、外资、上市、行业审批或备案材料。

未配置云端 MCP 时，可直接上传本地 `.docx`、`.pdf`、`.xlsx`、扫描件 OCR 文本作为 Local File Mode 输入。
