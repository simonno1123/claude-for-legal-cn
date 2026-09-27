# V-003 输入绑定接入候选 REV3 — 静态校验记录

## 1. 范围与结论

项目：claude-for-legal-cn / Route B / C03 / WP-008。

本轮依据 Project Owner 对“生成接入 V-003 规则与输出契约的新版输入绑定候选，并进行静态校验”的授权，生成独立 REV3 候选。旧版输入绑定、源码、fixture、已接受规则原文及旧校验记录均保留。

候选文件：`validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_RDM_DSP_002_REVISION_CANDIDATE_REV3.json`

候选 SHA-256：`45AB3117389A22DA9F502319467CE8BDDA731539C3B023BF92D7F0E2D93F0C6B`

候选身份：`C03-WP008-SCENARIO-INPUT-BINDING-RDM-DSP-002-CANDIDATE-004`；数据版本：`0.4`。

当前状态：`MATERIALIZED_NOT_FORMALLY_REVIEWED_NOT_ACCEPTED_NOT_ADMITTED`。

静态结果：27 / 27 检查通过；31 份受保护参考文件在候选生成前后均与固定摘要匹配。该结论仅是编制方数据/文本/完整性自检，不是独立候选审查、输入准入、Python 或场景执行，也不关闭 RDM-DSP-002。

## 2. 固定来源与接受边界

| 来源 | SHA-256 | 本轮用途 |
| --- | --- | --- |
| REV2 输入绑定候选 | 6C78702FCA2D776CE0AD17F4BD00AE65FF5B5C8D216209539FCD5877122B26B9 | 新候选的数据及历史来源；原文件不改，未由本轮准入 |
| V-003 已接受设计文件 | 9A856FCC23FEAC15A32CB7CD68BF3A33B33801B6D3947AB646CB6FD2AD7E08C9 | 原样复制其中两个 JSON 设计块；接受仅覆盖规则和输出契约设计 |
| V-003 原静态自检记录 | A46CCD928EE8CC4EB46D6BEBCBCF7CF53176EF2BF6ACC1116BDCDFBB9309A1D5 | 保留旧记录与参考身份；不是本次独立审查证据 |
| V-002 规则文件 | 94A6A193F299D9A42B40899D1708AE3CD29D435C11911DB424BB7CAAEC9BF875 | 保留其既有对话级接受范围，不重审、不扩张、不撤销 |

V-003 的 `CR-003-EXACT-IDENTITY-MISMATCH-TO-FIXTURE` 和 `OBS-V003-GATEDECISION-EXACT-DRAFT-001` 已有对话级 Project Owner 设计接受。本轮没有创建接受决定文件、时间戳或签名，也没有把此前同供应商独立设计审查记成跨供应商审查或本候选的独立审查。

复制的两个完整 JSON 块与固定接受文件按解析值逐项相同，其中形成时的 `PROPOSED_NOT_REVIEWED_NOT_ACCEPTED`、`existing binding`、`this document` 等文字不追溯改写。新候选的 `revision_context.v003_integration_revision.copied_design_snapshot_qualification` 明确列出五处状态/来源说明字段：

- 它们描述原设计文件形成时及其 REV2 输入引用，不代表撤回后来对话级设计接受。
- 它们不描述 REV3 已经被审查、准入或执行；当前整份候选仍未接受、未准入。
- 原生类型、固定输入、完整值、映射、失败与范围规则全部保持原文。
- 规则中的 `binding_reference` 继续固定到 REV2 的原始输入数据，不冒充 REV3 自身 SHA。三个刺激的实际参数及原始 fixture 必须与该固定来源一致。

## 3. 接入变化及不变范围

| 项目 | REV2 | REV3 候选 |
| --- | --- | --- |
| 场景 / 输入变体 | 15 / 28 | 15 / 28，身份与顺序不变 |
| 适配器 / 合成对象 | 14 / 10 | 14 / 10，完整内容不变 |
| 规则目录 | 7 | 8，原七条完整保留，仅新增 V-003 规则 |
| 输出契约 | 既有 V-002 契约 | 原契约不变，新增独立 V-003 契约 |
| 三个 V-003 comparison_rule_id | NOT_ESTABLISHED | 指向固定 V-003 规则，仅候选级声明 |
| 三个 V-003 observation_surface | state/reason_code | state/reason_code/audit_correlation_id/permitted_write_namespaces |
| V-003 分类 | 旧的映射未接受类别 | 集成候选待审查、待准入类别，不计为执行通过 |
| 其余十四场景 | REV2 记录 | 完整 JSON 值不变 |
| 全部原始预期、实际输入与源码 | 固定参考 | 不变 |
| 整份候选准入 / 执行 | 未建立 | 仍未建立 |

为避免新文件把历史形成时状态误报为当前事实，候选的修订/接受说明及相关未完成项区分了 V-002、V-003 的已接受设计与整份绑定未准入。没有因此改写 V-002 场景、既有七条规则、旧输出契约或任何旧文件。非目标限制项继续保留，未重新裁定。

现有 `original_oracle` 完整保留，包括 `BLOCKED_STALE`、`EXACT_IDENTITY_MISMATCH`、空写入集及禁止效果。接入不是改写测试答案：原始返回仍必须按接受设计检查为准确原生类型及完整值，再单独记录 fixture 抽象。空写入声明、一次拒绝或标签对应不能证明实际零 I/O、时间失效或完整禁止效果。

## 4. 逐项静态校验

方法仅包括：明确路径的本地读取与 SHA-256；JSON 数据解析/比较；原文与来源核对；JSON/Markdown 格式检查。未导入、编译或执行 Python 源码，未构造被审 Python 对象，未执行 Harness 或场景，未保存可执行校验脚本。

| 编号 | 检查主题 | 结果 | 依据及限定 |
| --- | --- | --- | --- |
| V003-INT-001 | 既有参考完整性 | PASS | 31 份既有文件在生成前与固定 SHA 完全匹配。 |
| V003-INT-002 | JSON 结构与修订身份 | PASS | REV3 为独立候选；JSON 数据可解析，保留 2 空格缩进和末尾换行。 |
| V003-INT-003 | 结构差异白名单 | PASS | 43 个差异路径全部位于接入字段或明确的修订/状态/来源说明；新增对象按一个路径计，不按叶字段计。 |
| V003-INT-004 | 全部场景身份与顺序 | PASS | 15 场景不增删、不重排。 |
| V003-INT-005 | 非目标场景原样保留 | PASS | 包括 V-002 在内的其余 14 个场景完整 JSON 值不变；旧状态文案按形成时快照说明，不是重新裁定。 |
| V003-INT-006 | 全部输入身份与内容保留 | PASS | 28 个变体的名称、适配器、调用参数、单字段覆盖与 defaults 不变；只改 V-003 六个接入字段。 |
| V003-INT-007 | 原始预期与标签保留 | PASS | 15 场景的完整 original_oracle、原始 input_state 和 fixture 引用均不变。 |
| V003-INT-008 | 对象与适配器保留 | PASS | 10 个基础对象和 14 个适配器完整保留。 |
| V003-INT-009 | 源码和 fixture 身份保留 | PASS | 10 个源码身份及 15 个 fixture 身份无变化。 |
| V003-INT-010 | 既有七条规则保留 | PASS | 七条原规则完整保留，不改 V-002 接受范围或原始返回要求。 |
| V003-INT-011 | 既有表示契约保留 | PASS | 旧输入表示及 V-002 输出契约不变，仅新增独立 V-003 契约。 |
| V003-INT-012 | 接受设计正文无值漂移 | PASS | 两个完整 JSON 设计块按值逐项相同，包括原因码、类型、表示、失败及范围限定；不是重写规则。 |
| V003-INT-013 | 规则和契约唯一关联 | PASS | 1 个新规则及 1 个新契约，不复用 V-002 契约 ID。 |
| V003-INT-014 | 仅三个目标消费者 | PASS | 新规则仅被三个 V-003 变体引用，其余场景不引用。 |
| V003-INT-015 | 四字段观察声明 | PASS | 观察面与原生契约四个字段一致；只是声明接入，不是 Harness 实现或实际观察。 |
| V003-INT-016 | 单字段与前置数据一致 | PASS | 不等向量仍为 01000、00100、00010；未改为 STALE、kill 或多字段错配。仅比较 JSON 数据，不运行门禁。 |
| V003-INT-017 | 原因和关联预期来源 | PASS | 完整原因与关联标识不变；[] 仅为原生空 tuple 的带类型预期编码。 |
| V003-INT-018 | 形成时状态与当前候选分离 | PASS | 列明五处原文快照字段，解释 PROPOSED/this document/existing binding 的来源语境；不把旧文字当作本候选执行权限。 |
| V003-INT-019 | 完整 SHA 与来源绑定 | PASS | 规则 binding_reference 保留为 REV2 固定输入来源；不冒充 REV3 自身 SHA，不转移执行证据。 |
| V003-INT-020 | 目录与分类计数 | PASS | 15 场景/28 变体/14 适配器/10 对象/8 规则；V-003 从旧映射未接受类别移至集成待审类别，不计作已通过。 |
| V003-INT-021 | 未完成项有限更新 | PASS | 只更正设计接受与输入准入的相关状态描述；其余阻断项不变，保留完整 prohibited_effect 未验证。 |
| V003-INT-022 | 接受不等于整份候选准入 | PASS | 仅记录已发生的对话级设计接受，没有伪造决策文件、签名或时间，也不把原设计审查迁移给 REV3。 |
| V003-INT-023 | 执行与关闭仍阻断 | PASS | 15 场景均 NOT_RUN；RDM-DSP-002 未关闭，未产生整体 PASS 或自动下游授权。 |
| V003-INT-024 | 工具与非目标权限不扩张 | PASS | 禁止项、设计对、合成数据声明及 CAPABILITY_ONLY 边界原样保留。 |
| V003-INT-025 | 文件文本格式 | PASS | 2 空格 JSON 格式、末尾换行，无行尾空白。 |
| V003-INT-026 | 落盘 JSON 与准备内容一致 | PASS | 实际新文件完整读取并解析；逐值及文本均与已检查的候选一致，无序列化遗漏。 |
| V003-INT-027 | 生成后受保护文件未变 | PASS | 新候选生成后，31 份受保护参考文件 SHA 再次全部匹配，包括 REV2、V-003 接受设计与旧静态记录。 |

三个变体静态不等向量的字段顺序为 capability_id、capability_version、implementation_sha256、configuration_sha256、activation_decision_reference。结果仍分别为 `01000`、`00100`、`00010`；这只是既有 JSON 值的比较，不是原函数的执行结果。

## 5. 精确结构差异清单

以下是与固定 REV2 对象比较得到的 43 个差异路径；一个新对象/数组项整体加入计一个路径，不声称只有 43 个叶字段改变。差异仅包括版本/授权/来源说明、新规则、新契约、V-003 六个接入字段、V-003 待准入状态和派生计数。

```text
/binding_id
/binding_version
/artifact_role
/authorization_boundary/authority
/authorization_boundary/permitted
/representation_contract/v003_gate_decision_output
/comparison_rule_catalog/CR-003-EXACT-IDENTITY-MISMATCH-TO-FIXTURE
/scenarios/2/binding_state
/scenarios/2/stimulus_variants/0/observation_surface
/scenarios/2/stimulus_variants/0/comparison_rule_id
/scenarios/2/stimulus_variants/1/observation_surface
/scenarios/2/stimulus_variants/1/comparison_rule_id
/scenarios/2/stimulus_variants/2/observation_surface
/scenarios/2/stimulus_variants/2/comparison_rule_id
/scenarios/2/unbound_requirements/0
/scenarios/2/unbound_requirements/1
/scenarios/2/coverage_limitations/1
/scenarios/2/coverage_limitations/2
/completeness_summary/complete_existing_calls_with_open_oracle_mismatch
/completeness_summary/comparison_rule_count
/completeness_summary/v003_integration_bindings_pending_review_and_admission
/completeness_summary/v003_rule_entries_added_from_accepted_design
/completeness_summary/count_qualification
/blocking_items/1
/blocking_items/2
/blocking_items/12
/resulting_state/new_comparison_rules
/resulting_state/v003_integration
/revision_context/change_scope/0
/revision_context/change_scope/1
/revision_context/change_scope/2
/revision_context/change_scope/3
/revision_context/change_scope/4
/revision_context/preservation_scope/0
/revision_context/preservation_scope/1
/revision_context/preservation_scope/2
/revision_context/preservation_scope/3
/revision_context/preservation_scope/4
/revision_context/preservation_scope/5
/revision_context/preservation_scope/6
/revision_context/preservation_scope/7
/revision_context/new_rule_acceptance
/revision_context/v003_integration_revision
```

## 6. 受保护参考完整性

核验范围仅限下列 31 个已固定参考文件；不宣称检查整个工作区。每项本地摘要在生成前后均与下列值匹配。

| 项目内路径 | 固定 SHA-256 / 本地匹配值 | 结果 |
| --- | --- | --- |
| scripts/phase2_runtime/__init__.py | 49B8B1BD319B6424323AD0EDC04B3969D71196CD8D69E12C16D5442B17340844 | MATCH |
| scripts/phase2_runtime/route_b_c03/__init__.py | F669613D65267EC5D4D42CB79008EB510307A99B20E40EE13E9E1E0E404A504D | MATCH |
| scripts/phase2_runtime/route_b_c03/contracts.py | 7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4 | MATCH |
| scripts/phase2_runtime/route_b_c03/identity_gate.py | 9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445 | MATCH |
| scripts/phase2_runtime/route_b_c03/mapping.py | 320F7E8576C1C4E81B4E78E6058000E4D720173948BE736AD846B8CAD664EC66 | MATCH |
| scripts/phase2_runtime/route_b_c03/isolation.py | 9BC554294D5945188A153F0A5CBEDFAB4E483C95B133683B7517ECC334D4205B | MATCH |
| scripts/phase2_runtime/route_b_c03/failures.py | 6F30D996119F61A19B20208FC44C8AF1FB96ADFE09ADE3538675B9D3F2933734 | MATCH |
| scripts/phase2_runtime/route_b_c03/audit.py | A704BDB22C55C92D0909FA0D6A668D8C149724B2A7627938C301758F1D09F561 | MATCH |
| scripts/phase2_runtime/route_b_c03/provider_port.py | 66E4DA862BBBD50380B17686DB6BC2AB6D5D3B861AB53FCDDE1B608F86DEA381 | MATCH |
| scripts/phase2_runtime/route_b_c03/capability.py | 028EE9DDD7A2C06840A6F344A4C4CC716EFF95073BE39CA6E57FB7FDBBFA6DD5 | MATCH |
| validation/route_b_c03/wp_008/fixtures/C03-TA-V-001.json | C8CEFEDC496D5D0D33E0F21D61B5E3C3354579A8D0E1C74F70640305C65FC99A | MATCH |
| validation/route_b_c03/wp_008/fixtures/C03-TA-V-002.json | 257437A2AA80A58C0741F1EC0A5A514E014C633DD974804C6407DB84DB107290 | MATCH |
| validation/route_b_c03/wp_008/fixtures/C03-TA-V-003.json | 21BD65ECD28D569BADFF11489017569E8413B1CC9A5138A851F907CCF62EAF7E | MATCH |
| validation/route_b_c03/wp_008/fixtures/C03-TA-V-004.json | 9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8 | MATCH |
| validation/route_b_c03/wp_008/fixtures/C03-TA-V-005.json | 4405ADC2CE242B83120B0BA304157B3E6F03687345F764BBBE1E3A2DCF2422DE | MATCH |
| validation/route_b_c03/wp_008/fixtures/C03-TA-V-006.json | 9D24E6AFA92F9EF6E895B0B6E4D0E84BDC326E9C4B815E42723B31374CC2FDC8 | MATCH |
| validation/route_b_c03/wp_008/fixtures/C03-TA-V-007.json | 68D9D63583A0301BDE76C3E60A5F66B7CCDA897C17D58E8DBF282E3E49C3DB90 | MATCH |
| validation/route_b_c03/wp_008/fixtures/C03-TA-V-008.json | 7AA3FEF0CCDFA0C6A462C7945B63A50D828AC9C6D0725F428D347F6836075193 | MATCH |
| validation/route_b_c03/wp_008/fixtures/C03-TA-V-009.json | 34EFBC55490FB2E3FFC89CAFCAD9DD2D319C2C24D9B3E2B026143F74A73DC93C | MATCH |
| validation/route_b_c03/wp_008/fixtures/C03-TA-V-010.json | 19DF9D35835F60C03C969B79B25F62CFE95E28C0A1B8122EDD8B9E1A5BC0E67A | MATCH |
| validation/route_b_c03/wp_008/fixtures/C03-TA-V-011.json | 8795DA58E092E6DC7F88958E3AC60B754870F5BFAE15FF8BC2D699450B65FDFD | MATCH |
| validation/route_b_c03/wp_008/fixtures/C03-TA-V-012.json | 8C6E4FC6279E95CFE48C9E9DA6E161F0AF05CA5FFEA95BE18DBAD6A81204E8E6 | MATCH |
| validation/route_b_c03/wp_008/fixtures/C03-TA-V-013.json | 3DBF0F60AC970F90C97CF85F5F21F1758B4818D814A02CE8ED03A4F1C3A49CA6 | MATCH |
| validation/route_b_c03/wp_008/fixtures/C03-TA-V-014.json | D3EF698EA45F41824CCF6C5A7020F6A0B495460341ADE7446461A1AAF0E7D523 | MATCH |
| validation/route_b_c03/wp_008/fixtures/C03-TA-V-015.json | 06DCEBA08CA43C75439B5A2AC1C140905887EF8CDC26C561FBD68E9A001D5AE1 | MATCH |
| validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_RDM_DSP_002_REVISION_CANDIDATE_REV2.json | 6C78702FCA2D776CE0AD17F4BD00AE65FF5B5C8D216209539FCD5877122B26B9 | MATCH |
| validation/route_b_c03/wp_008/RDM_DSP_002_COMPARISON_RULE_DRAFT_REV2.md | 94A6A193F299D9A42B40899D1708AE3CD29D435C11911DB424BB7CAAEC9BF875 | MATCH |
| validation/route_b_c03/wp_008/RDM_DSP_002_OUTPUT_REPRESENTATION_STATIC_CHECK_REV2.md | 7B142E513EB1688B20185CA837A9337A0B1552B7AECD4A6CB488AF8940B00A4F | MATCH |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V3_1_CANDIDATE.md | 3432D99D22AA288668C8D4E2CF58975A794ED545B62EB05FCA9E0B41525AEDDB | MATCH |
| validation/route_b_c03/wp_008/V003_LIMITED_COMPARISON_RULE_DRAFT.md | 9A856FCC23FEAC15A32CB7CD68BF3A33B33801B6D3947AB646CB6FD2AD7E08C9 | MATCH |
| validation/route_b_c03/wp_008/V003_LIMITED_COMPARISON_RULE_STATIC_CHECK.md | A46CCD928EE8CC4EB46D6BEBCBCF7CF53176EF2BF6ACC1116BDCDFBB9309A1D5 | MATCH |

## 7. 仍须分离处理的后续事项

| 事项 | 当前效力 |
| --- | --- |
| 原 V-003 规则及输出契约设计接受 | 对话级接受保持；不扩张到整个候选 |
| REV3 固定 SHA 独立审查 | NOT AUTHORIZED / NOT PERFORMED BY THIS TASK |
| REV3 接受与完整输入准入 | NOT AUTHORIZED / NOT ESTABLISHED |
| Harness、依赖与可信导入边界最终准入 | 未由本轮建立 |
| 全部 15 场景执行 | NOT_RUN |
| RDM-DSP-002 | OPEN_NOT_CLOSED |
| 完整 C03 验证及总体合格结论 | NOT ESTABLISHED |
| 真实案件、OCR、外部模型、网络、独立 ACOS、Git | 本轮未操作、未授权推进 |

本轮只新增 REV3 候选及本静态记录；未改旧文件。下一步如获单独授权，可针对候选固定 SHA 进行只读接入审查；接受、准入、实际执行和限制项关闭仍是不同步骤。

本记录不包含自身 SHA；摘要在文档外计算，避免循环自指。
