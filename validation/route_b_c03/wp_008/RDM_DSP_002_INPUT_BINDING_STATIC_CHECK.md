# RDM-DSP-002 新版输入绑定与比较规则草案静态校验

## 1. 授权范围与结论

依据本轮 Project Owner“授权生成该候选及比较规则草案，并进行静态校验”完成生成与静态自检。后续“继续”仅用于继续完成本轮交付，不被解释为准入、接受或正式执行授权。

结论：33/33 项静态检查通过。本结论仅为同一作者的生成后自检，不是独立审查、跨供应商审查、规则接受、输入准入或完整 WP-008 验证通过。

本轮未导入、编译或调用 Python 被审源码，没有构造被审 Python 对象、执行任何场景或重新运行前轮诊断。使用只读文件读取、SHA 计算、JSON 数据比较和 Markdown 结构检查完成校验。

## 2. 固定交付物与基线

| 对象 | 项目内路径 | SHA-256 |
| --- | --- | --- |
| 新版完整输入绑定候选 | validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_RDM_DSP_002_REVISION_CANDIDATE.json | 738252342529332DB521A51E653D7E6FE32ED44EC6DA66C5F278D35BAEF99ECF |
| 两条新规则的说明草案 | validation/route_b_c03/wp_008/RDM_DSP_002_COMPARISON_RULE_DRAFT.md | 766B611BBD04C6A37F81DED5D4F7BCFDB6D5D8D13BBC870DAA14FA61FFABB71D |
| 保持原样的旧输入绑定 | validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json | 92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5 |
| 本轮只读的当前修复源码 | scripts/phase2_runtime/route_b_c03/identity_gate.py | 9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445 |

候选中的 10 项源码、15 项测试材料及 7 项修订来源文件的 SHA 均与本地实际文件匹配。这些计数是文件身份检查，不是场景执行通过数量，也不意味着所有来源记录已重新进行正式审查。

## 3. 有限变更摘要

| 项目 | 原版 | 新候选 |
| --- | --- | --- |
| 场景数 | 15 | 15 |
| 输入变体数 | 25 | 28 |
| V-002 变体数 | 2 | 5 |
| 适配器数 | 14 | 14 |
| 合成对象数 | 10 | 10 |
| 规则目录项数 | 5 | 7：5 条未改写历史定义，2 条新草案 |
| 当前源码 SHA 绑定 | 旧身份 | 已修复源码身份 |
| 接受与准入 | 原版未准入 | 新候选未接受、未准入 |

V-002 五种输入分别为：构造器空事项授权引用、事项授权引用不匹配、执行授权引用不匹配、授权包决策引用不匹配、所有引用匹配的正向对照。

负向三个门禁变体只覆盖各自的一个字段；静态数据比对显示其非目标引用及前置门禁所需字段匹配。正向对照没有字段覆盖，三个引用均匹配。这是 JSON 元数据的静态一致性检查，不是对门禁函数的模拟运行或运行结果。

原始负向测试材料的 BLOCKED 预期未改写。正向对照采用独立的原始返回值比较规则，其 fixture_mapping 为 null，明确禁止套用负向预期。三项不匹配规则与正向对照都保留原始状态、完整原因、关联标识和空写入集检查，不赋予业务执行权。

其他 14 个场景、15 项测试材料绑定、10 个合成对象、其他 9 项源码身份、其他 13 个适配器及原有 5 条规则定义经结构化比较保持原样。共享 identity-gate 适配器的源码 SHA 已变更，因此其他场景内容不变不等于旧执行证据自动适用于新源码。

## 4. 静态检查明细

下列明细为实际执行的 JSON/字符串/文件身份检查。PASS 只限定于各行静态条件。

| ID | 静态检查内容 | 结果 |
| --- | --- | --- |
| S01 | Candidate identity and unaccepted/unadmitted state explicit | PASS |
| S02 | Canonical two-space JSON without duplicate properties | PASS |
| S03 | 15 scenarios and 28 variants | PASS |
| S04 | 28 unique stimulus IDs | PASS |
| S05 | Five design variants represented exactly once | PASS |
| S06 | Other 14 scenarios structurally unchanged | PASS |
| S07 | All 15 fixture bindings unchanged | PASS |
| S08 | All 10 synthetic objects unchanged | PASS |
| S09 | Other 13 adapters unchanged | PASS |
| S10 | Other 9 subject identities unchanged | PASS |
| S11 | Both identity-gate bindings use the repaired source SHA | PASS |
| S12 | Identity adapter changed only subject SHA | PASS |
| S13 | Five historical rule definitions unchanged | PASS |
| S14 | Constructor stimulus and historical comparison unchanged | PASS |
| S15 | Four gate stimuli resolve fixed references and retain explicit original arguments | PASS |
| S16 | Static data satisfy earlier-gate prerequisites; no subject invoked | PASS |
| S17 | Three single-reference mismatches and one no-override all-match control | PASS |
| S18 | Negative raw result and fixture abstraction exact and separate | PASS |
| S19 | Positive control exact and excluded from negative fixture mapping | PASS |
| S20 | Empty write set and exact correlation for both new rules | PASS |
| S21 | Exact disjoint rule applications | PASS |
| S22 | Original fixture/oracle retained and positive control excluded | PASS |
| S23 | New rules remain drafts with post-hoc changes prohibited | PASS |
| S24 | No runtime execution, admission or closure asserted | PASS |
| S25 | Derived counts balance: 15 scenarios / 28 variants / 14 adapters / 10 objects / 7 rules | PASS |
| S26 | Only declared revision and derived fields changed; old top-level fields retained | PASS |
| S27 | 10/10 actual subject-file hashes match | PASS |
| S28 | 15/15 actual fixture-file hashes match | PASS |
| S29 | 7/7 actual revision-lineage file hashes match | PASS |
| S30 | Fixed source text places comparison before eligibility; no source execution | PASS |
| S31 | Draft rule snippets and candidate SHA exactly match | PASS |
| S32 | Markdown columns, final newlines and whitespace valid | PASS |
| S33 | Original input binding remains byte-identical | PASS |

## 5. 缺陷与保留限制

- 本轮上述 33 项静态条件未检出失败项；不据此声明运行时零缺陷、全项目零缺陷或阶段接受。
- 两条新规则均为 PROPOSED_NOT_REVIEWED_NOT_ACCEPTED；独立固定 SHA 审查和 Project Owner 接受尚未建立。
- 新版候选尚未准入。原有五条规则的历史接受范围不能自动扩展为新候选的接受或执行权限。
- 原文件保持未修改；候选携带的其他场景及非目标限制是保留的准备期快照，本轮未重新裁定其当前状态。
- 全部场景仍为 NOT_RUN。前轮源文件诊断不作为本候选场景的观察值或执行证据填入。
- RDM-DSP-002 仍未关闭；V-003 比较问题及其他未解决项未由本轮修复。
- 完整依赖绑定、环境版本记录差异、正式 Harness、正式证据准入及执行授权不由此校验解决。
- 未修改任何源码、旧候选、测试材料或历史审查/接受记录；没有进行 Git 操作、外部调用、独立 ACOS 项目变更、真实事项处理或 OCR。

本轮新增三个文件：输入绑定候选、比较规则草案及本静态校验记录。后续只能在相应授权下开展固定 SHA 审查与接受/准入决策，不能由本报告自动进入执行。
