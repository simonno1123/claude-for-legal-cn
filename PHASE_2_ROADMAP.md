# Phase 2 路线图

本文件记录 Phase 1 中国大陆法本土化基线完成之后的 Phase 2 工作流。当前 Phase 2 已完成，后续仅保留维护、更新和深化入口。

## Phase 2 范围

Phase 2 覆盖未进入 Phase 1 默认 Marketplace 的进阶模块。这些模块要么场景更专业，要么使用频率较低，要么属于工具生态建设。

## 中国案例规则更新层

状态：COMPLETE。

项目已加入可更新的中国案例规则层：

- `references/china-case-authority.md`
- `references/case-authority-sources.json`
- `references/case-authority-mcp.example.json`

该层为人民法院案例库、最高人民法院发布、裁判文书网和商业法律数据库预留更新接口。案例用于类案检索、裁判规则校准和风险判断，不得作为英美法意义上的判例法。

## 工作流

### 1. Corporate M&A Phase 1.5

路径：`corporate-legal/phase-2/`

目标：在公司治理、出资、股权转让和章程审查稳定后，补齐中国并购尽调、交割和投后整合工作流。

状态：COMPLETE。

已完成：

- `diligence-issue-extraction`
- `material-contract-schedule`
- `closing-checklist`
- `integration-management`
- `deal-team-summary`
- `tabular-review`
- `ai-tool-handoff`
- `references/test-cases-cn.md`

验收点：

- 已替换美国交易概念为中国股权/资产收购、工商登记、税务、劳动、反垄断、数据和国资审查逻辑。
- 已加入市场监管、外商投资、国资、经营者集中和行业许可等审批/备案检查。
- 已覆盖股权权属、出资瑕疵、关联交易、劳动社保、税务、许可、知识产权、数据合规、诉讼和重大合同。

### 2. Law Student

路径：`phase-2/law-student/`

目标：围绕中国法学院教育、法考、法条体系、请求权基础、案例研读和法律写作训练重建学习模块。

状态：COMPLETE。

已完成：

- 中国法学习画像。
- 法考客观题/主观题训练。
- 法条体系和请求权基础训练。
- 案例研读、课堂提问准备、闪卡、学习计划。
- `references/test-cases-cn.md`

验收点：

- 已移除美国 law school、Bluebook、bar exam 和 common-law case method 默认框架。
- 输出定位为学习材料，不处理真实客户事项。

### 3. Legal Clinic

路径：`phase-2/legal-clinic/`

目标：围绕中国法律诊所、法律援助、12348 公共法律服务、学生办案训练和导师复核重建工作流。

状态：COMPLETE。

已完成：

- 当事人接待和初筛。
- 法援/公服分流。
- 期限跟踪。
- 案件备忘录、文书学习稿、当事人说明信。
- 导师/律师复核队列。
- 学期交接。
- `references/test-cases-cn.md`

验收点：

- 已移除 ABA、美国学生执业规则、美国证据特权和州律师协会默认框架。
- 所有真实当事人事项均保留导师或执业律师复核门。

### 4. Legal Builder Hub

路径：`phase-2/legal-builder-hub/`

目标：作为中国法律技能和 MCP 工具链构建中心，支撑技能发现、审查、安装、禁用、更新和回归检查。

状态：COMPLETE。

已完成：

- 中国法技能 QA。
- 安装白名单。
- MCP 凭证占位检查。
- 技能启用/禁用/卸载。
- 更新计划。
- 相关技能推荐。
- `references/test-cases-cn.md`

验收点：

- 所有外部技能必须通过中国法本土化审查。
- 禁止真实凭证入库。
- 禁止未审查技能进入默认 Marketplace。

## 后续维护入口

| 方向 | 文件/模块 | 建议周期 |
|---|---|---|
| 案例规则更新 | `references/case-authority-sources.json` | 活跃模块每周，非活跃模块每月 |
| 法律法规更新 | `references/china-legal-standards.md` 与各模块 references | 每月或重大修法时 |
| 连接器落地 | `CONNECTORS.md`、各 `.mcp.json` | 按供应商或内部系统推进 |
| 回归用例维护 | 各 `references/test-cases-cn.md` | 每次重大 Prompt 修改后 |
| Phase 2 深化 | `phase-2/` 与 `corporate-legal/phase-2/` | 按需求迭代 |

## 总结

Phase 2 已完成从“暂存模块”到“中国法可用模块”的第一轮本土化。后续重点不再是法域替换，而是：

1. 增强 Practice Profile 丰富度。
2. 落地真实 MCP 连接器。
3. 建立自动化回归测试。
4. 接入可持续更新的案例与监管数据源。
