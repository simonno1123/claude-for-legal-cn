# TASK_014_LAW_STUDENT_UPGRADE — 审查报告
# 审查方：Gemini 3.5 Flash (接替 Claude)
# 审查依据：Codex RESULT artifact（TASK_014_LAW_STUDENT_UPGRADE_RESULT）
# 审查时间：2026-07-09
# 审查模式：READ ONLY（基于 RESULT + 本地文件系统交叉验证）

---

## 一、RESULT 事实核验与诊断

经过在本地工作树及上游基线的交叉对比，确认 Codex 在审计报告中陈述的事实均准确属实：

1. **结构与根级 Parity 缺失 (P0 - Blocker)**：
   上游的 `law-student` 是顶级一等插件，而在 CN 仓库中，它被降级并“隐藏”在 `phase-2/law-student` 下，默认 `marketplace.json` 中并无该插件入口。这违反了 Faithful Port v1 的根级 Parity 规则，导致用户无法发现和载入该命令。
2. **核心“学习模式”职责严重退化 (P0 - Blocker)**：
   CN 现有的 13 个技能虽然命名一致，但代码体量极度缩水（如 `study-plan` 从上游 248 行缩水至 16 行，`bar-prep-questions` 从 270 行缩水至 24 行）。上游核心的“辅导脚手架（Scaffold）而非直接给答案（No rewrite / Anti-ghostwriting）”逻辑丢失，例如 `legal-writing` 退化成了直接帮学生生成意见书草稿的“代写工具”，违反了学术诚信护栏。
3. **有状态学习环缺失 (P1 - Gap)**：
   缺少 `study-plan.yaml` 本地化持久化配置、`session_history` 历史纪录、以及错题本/弱项权重的动态调整环，这使得原有的“循环学习系统”退化为了静态 Prompt 模板。
4. **中国化定位正确但过浅**：
   虽然指明了“法考”和“请求权基础”的方向，但因体量受限，均未展开实质性的考纲或案例研习辅导规则。

**诊断结论：ACTION REQUIRED (拒绝通过，必须进行物理重构与内容重写)。**

---

## 二、整改框架建议 (Upgrade Plan)

### 1. 结构与目录重构 (P0)
- 将 `phase-2/law-student` 目录**物理提升（Move）**至仓库根目录的顶级插件路径 `law-student/`。
- 在根目录的 `.claude-plugin/marketplace.json` 中正式注册 `law-student` 插件，恢复根级命令的可发现性。

### 2. 重建“非代写/脚手架学习”护栏 (P0)
- 重写 `CLAUDE.md` 与 `README.md`，确立“学术诚信与独立思考”大原则。
- 重写 `legal-writing` 与 `irac-practice`：严禁代写或重写学生的作业/论文，只提供结构性、逻辑性、语法与请求权基础的批判性反馈。
- 重写 `socratic-drill` 与 `cold-call-prep`：必须通过“提问-等待输入-追问（Ask-Wait-Pushback）”的交互式苏格拉底教学法运行，不得一次性倾倒答案。

### 3. 实现有状态学习环 (P1)
- 仿照 `ai-governance-legal` 模式，在 `study-plan`、`session`、`flashcards` 中建立本地配置文件 `study-plan.yaml` 与 `session_history`。
- 实现 `cold-start-interview`：收集中国法考考生的备考状态、学科弱点，并支持导入种子学习资料、暂停与恢复、多档案更新（通过 `customize` 联动）。

### 4. 深度中国化内容填充 (P1)
- **`bar-prep-questions`**：从美国 MBE/UBE 替换为中国法考客观题与主观题，支持错项解析、法考大纲重难点（民法、刑法、行政、商经等）。
- **`case-brief`**：从美国 Case Method 替换为中国商事/民事“案例研习”：案情摘要、争议焦点、请求权基础与抗辩事由、构成要件分析、裁判要旨、类案检索价值。
- **`outline-builder`**：基于中国大陆成文法法条体系及司法解释体系构建知识大纲。

---

## 三、审查结论

**REJECTED (ACTION REQUIRED)**

`law-student` 模块目前处于 `Invalid` 状态，必须进行全面重组与恢复编辑。

---

## 四、Codex RESULT 质量评估

- **诊断深度**：10/10（精准定位了 13 个技能的缩水比例与有状态缺失）。
- **整改计划可行性**：10/10（给出的 P0/P1 重写框架非常清晰，将直接作为下一步任务书的底层依据）。
