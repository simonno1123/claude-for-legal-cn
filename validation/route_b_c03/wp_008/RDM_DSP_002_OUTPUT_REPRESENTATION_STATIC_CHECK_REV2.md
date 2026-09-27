# RDM-DSP-002 REV2 输出类型与比较表示契约静态校验

## 1. 授权、结论及限制

Project Owner 本轮“授权操作。”承接上一轮明确提出的有限范围：仅补充候选与规则中的输出类型及比较表示契约，保持业务源码、原始测试材料和预期语义不变。本轮生成独立 REV2 文件，不覆盖上一版候选、规则草案或历史校验记录。

结论：本报告列出的 **32/32 项静态检查通过**。该计数只表示 JSON 结构、限定差异、契约条款存在性与一致性、Markdown 结构及文件身份等静态条件通过；不是 Harness 实现正确性或运行用例通过率。原生类型/表示歧义已在 REV2 设计文本中补充，不据此宣布 RDM-DSP-002 关闭。

这是同一作者的有限修订后自检，不是独立审查、外部审查、规则接受、输入准入或完整 WP-008 验证。Project Owner 接受及独立固定 SHA 审查仍未建立。

## 2. 固定文件身份

| 对象 | 项目内路径 | SHA-256 |
| --- | --- | --- |
| REV2 输入绑定候选 | validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_RDM_DSP_002_REVISION_CANDIDATE_REV2.json | 6C78702FCA2D776CE0AD17F4BD00AE65FF5B5C8D216209539FCD5877122B26B9 |
| REV2 比较规则草案 | validation/route_b_c03/wp_008/RDM_DSP_002_COMPARISON_RULE_DRAFT_REV2.md | 397D3DAE4CBA243A978417DCFC0CCF68441C80ADD8A0D8413A806EF8477A82F7 |
| 上一版候选，保留原样 | validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_RDM_DSP_002_REVISION_CANDIDATE.json | 738252342529332DB521A51E653D7E6FE32ED44EC6DA66C5F278D35BAEF99ECF |
| 上一版规则草案，保留原样 | validation/route_b_c03/wp_008/RDM_DSP_002_COMPARISON_RULE_DRAFT.md | 766B611BBD04C6A37F81DED5D4F7BCFDB6D5D8D13BBC870DAA14FA61FFABB71D |
| 上一版静态自检，保留原样 | validation/route_b_c03/wp_008/RDM_DSP_002_INPUT_BINDING_STATIC_CHECK.md | 7CC09E3D7AD801A7798A3183CD31822648444F96CB7266C144DE3980CF6299A7 |
| 当前门禁源码，本轮未修改 | scripts/phase2_runtime/route_b_c03/identity_gate.py | 9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445 |
| 数据契约，本轮未修改 | scripts/phase2_runtime/route_b_c03/contracts.py | 7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4 |
| 原始输入绑定，保留原样 | validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json | 92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5 |

本轮对候选关联的 34 个去重文件进行了修订前后 SHA 核对，全部匹配。这包括固定源码、原始测试材料、既有来源记录及上一版候选/草案/自检记录。SHA 匹配不重新确认这些历史文件的接受、独立性或运行效力。

## 3. 有限修订说明

源码文本明确声明 GateDecision.state 为 InvocationState，permitted_write_namespaces 为 tuple[str, ...]，且门禁的 _decision 返回空元组。上一版新规则采用 JSON 状态字符串和空数组表达预期，同时禁止规范化，未明确原生比较与表示编码的边界。

REV2 增加唯一契约 `OBS-GATEDECISION-EXACT-V1`，仅供两条新增 V-002 草案规则、四个门禁变体引用：

- 先检查固定源码绑定的 GateDecision / InvocationState 精确类型及原生成员、内置字符串、原生空元组。
- 普通字符串不能替代枚举；列表、None 或缺失字段不能替代空元组。非空元组保留实际内容并判为不匹配，不清空。
- 原生类型和值比较后，才可生成保留枚举类型/成员与 tuple 类型来源的可逆 JSON 展示。展示相同不代表原生类型符合。
- 两条规则的原始预期值、原因、关联标识、空写入集及 fixture_mapping 保持完全一致。正向对照不套用负向 fixture。
- 未生成原始运行观察、Harness、JSON Schema 或新场景；不得复制预期填充观察，也不得以编码结果覆盖原生失败判定。

新版标识为 C03-WP008-SCENARIO-INPUT-BINDING-RDM-DSP-002-CANDIDATE-003，binding_version 为 0.3；文件名 REV2 表示本输入/规则候选的第二次交付，不改变 RDM-DSP-002 事项标识。

相对上一版，全部 15 场景、28 输入变体、14 适配器、10 合成对象、源码与 fixture 身份、5 条历史规则、两条新草案的预期语义都保持不变。仅七个顶层字段组发生授权内变化：binding_id、binding_version、artifact_role、authorization_boundary、representation_contract、comparison_rule_catalog、revision_context。

## 4. 实际静态检查清单

契约条款的检查以读取后的 JSON/Markdown 内容为依据；原生类型反例仅检查其设计要求已明确记录，没有构造 Python 对象或运行被审函数。

| ID | 静态条件 | 结果 |
| --- | --- | --- |
| R01 | Disk JSON equals intended REV2 candidate | PASS |
| R02 | Canonical two-space JSON and final newline | PASS |
| R03 | Only seven authorized top-level identity/control/contract sections differ | PASS |
| R04 | All fifteen scenario records including V-002 arguments/overrides unchanged | PASS |
| R05 | 28 unique variant IDs; V-002 five variants remain separate | PASS |
| R06 | All ten synthetic objects unchanged | PASS |
| R07 | All fourteen adapters and ten subject bindings unchanged | PASS |
| R08 | All fifteen fixture bindings unchanged | PASS |
| R09 | Design-pair references and input enum/tuple representation unchanged | PASS |
| R10 | Five historical rules unchanged | PASS |
| R11 | Both new rules retain exact raw expectation values | PASS |
| R12 | Both fixture mappings and disjoint applications unchanged | PASS |
| R13 | Rule deltas limited to comparison mode and two explicit contract references | PASS |
| R14 | Both rule references resolve to one scoped output contract | PASS |
| R15 | Output contract binds fixed contracts SHA and forbids data-driven dispatch | PASS |
| R16 | Exact native GateDecision required without duck-type or subclass replacement | PASS |
| R17 | Enum expectations preserve exact BLOCKED and ELIGIBLE members | PASS |
| R18 | Reason and correlation retain exact built-in string/code-point checks | PASS |
| R19 | Both rules require native empty tuple; array is only expectation encoding | PASS |
| R20 | Nonempty tuple and list/set/generator/None/missing/type-error paths do not pass | PASS |
| R21 | Evidence encoding retains actual enum/tuple types, member and order | PASS |
| R22 | Native type checks precede comparison/encoding; display cannot override mismatch | PASS |
| R23 | No pass from projection; no expected backfill or unknown-object conversion | PASS |
| R24 | Negative mapping follows native checks; positive excludes negative oracle | PASS |
| R25 | Both rules prohibit semantic normalization without forbidding defined lossless display | PASS |
| R26 | Review/admission/execution/closure and completeness states unchanged | PASS |
| R27 | Prior revision context unchanged and three prior artifact SHA references preserved | PASS |
| R28 | Two Markdown rule snippets exactly match REV2 JSON definitions | PASS |
| R29 | Markdown binds actual REV2 candidate hash and contract ID | PASS |
| R30 | Markdown physical tables/newline/whitespace valid | PASS |
| R31 | Draft labels negative examples as non-executed contract checks | PASS |
| R32 | 34 bound source, fixture, lineage and prior-candidate files unchanged before/after revision | PASS |

格式校验使用直接读取文件原文排除终端输出附加换行的影响；未为使检查通过而改动候选内容、预期值或放宽格式条件。

## 5. 当前边界与后续门禁

| 项目 | 本轮结论或状态 |
| --- | --- |
| 输出类型/比较表示契约有限修订 | 已物化为 REV2 草案，并完成作者静态自检 |
| 两条新规则接受 | NOT ESTABLISHED |
| 独立固定 SHA 审查 | NOT ESTABLISHED |
| 新版输入绑定准入 | NOT ESTABLISHED |
| 新版候选场景执行 | NOT RUN |
| RDM-DSP-002 关闭 | NOT ESTABLISHED |
| 完整 WP-008 / C03 就绪 | NOT ESTABLISHED |
| 自动下游转换 | BLOCKED |

本轮未启动 Python、导入或编译被审源码、执行场景、重跑前轮诊断、创建 Harness、修改业务代码/原始 fixture、安装依赖、触及真实案件或 OCR、调用外部模型、修改独立 ACOS 或执行 Git 操作。使用文件读取、SHA 核验及 JSON/字符串静态比较完成本轮检查。

后续如需独立审查、规则接受、输入准入或实际执行，仍须相应明确授权；原有其他场景的未解决项、完整依赖绑定及环境版本记录差异不由本次修订解决。本报告不追溯修改上一版自检结论，也不将上一版记录转作 REV2 的独立审查或运行证据。
