# TASK_PHASE2_C02_CLOSURE_AND_REDIRECTION_DECISION

| Field | Value |
|---|---|
| Decision ID | TASK_PHASE2_C02_CLOSURE_AND_REDIRECTION_DECISION |
| Type | Line Closure and Redirection Decision |
| Status | **ACCEPTED** |
| Date | 2026-11-04 |
| Approved by | Project Owner（张纯熙，在记录人提出的问题中选择"收尾并改向"；选项由记录人 Claude 起草） |
| Supersedes | TASK_PHASE2_C02_IV_INPUT_READINESS_DESIGN_DECISION 中的"Hold State" |

## 决定

1. **C02（请求权基础）这条线结束。** C02-I 至 C02-IV 的成果保持已接受状态，作为参考资料，不再在本仓库内推进 C02-V 或 C02 实现。
2. **分层改向：**
   - **方法层**：请求权基础分析方法做成独立项目 `simonno1123/claim-basis-cn`（独立仓库、单独发版），供本仓库的 `claim-chart`、`matter-intake`、`demand-draft`、`law-student` 等技能引用，并锁定版本。
   - **数据层**：法律、司法解释与案例由数据库连接器提供（见 `references/china-connectors.md`），不写入方法技能。
   - **输入层**：案件材料与 OCR 问题归入输入准备的工作，不再阻塞方法开发。
3. **首版范围**：检索顺序与三段式检验；涵摄与举证责任；竞合与请求权关系；执行程序中的运用。
4. **验证方式**：用虚构案例回归；法律内容由所有者以律师身份审定。

## 理由

- C02 四个阶段产出了记录结构与验证治理文档，但请求权基础的分析方法本身（检索顺序、三段式检验、涵摄、竞合处理）没有落地到任何技能。
- C02-I 与 C02-III 受阻于真实案件材料和 OCR，属于输入层问题，与方法无关。
- 方法独立成项目，便于被多个技能引用，也便于在 claude.ai 中单独使用。

## 不变事项

- 本决定不修改 `litigation-legal/` 下任何技能；引用新项目需要另行决定。
- C02-I 的结论"BLOCKED — PARTIAL VALIDATION ONLY"不作重新定性。
