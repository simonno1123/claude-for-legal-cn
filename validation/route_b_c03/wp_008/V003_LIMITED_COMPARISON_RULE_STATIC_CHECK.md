# V-003 有限比较规则草案静态校验记录

## 1. 校验对象、方法和结论边界

项目：claude-for-legal-cn / Route B / C03 / WP-008。

授权范围：生成 V-003 有限比较规则草案并做静态校验。仅新增草案与本记录，不修改源码、原始 fixture、已有输入绑定、V-002 已接受规则或其他项目。

校验对象：`validation/route_b_c03/wp_008/V003_LIMITED_COMPARISON_RULE_DRAFT.md`

校验对象 SHA-256：`9A856FCC23FEAC15A32CB7CD68BF3A33B33801B6D3947AB646CB6FD2AD7E08C9`

本记录是编制方静态自检，不是独立设计审查、Project Owner 接受、输入准入、执行报告或限制项关闭决定。

方法：

- 本地只读读取明确路径，计算文件 SHA-256，与固定参考摘要比较。
- 解析现有输入绑定、fixture 及草案内两个 JSON 设计数据块。
- 仅在内存中核对单字段覆盖前后数据差异；未调用 Python 构造器或门禁函数。
- 对照源码文本中的分支顺序、返回表达式与类型声明，检查草案要求及失败边界。
- 检查 Markdown 表格物理列数、围栏、末尾换行与行尾空白。未保存或创建可执行检查脚本。

结果：下列 30 项限定静态检查为 30 PASS / 0 FAIL；29 个既有参考文件摘要全部匹配。这里的 PASS 只表示各行所述数据、文本或完整性检查通过，不表示 V-003 场景执行、全部代码正确、类型检查机制已实现、完整 C03 验证通过或总体安全通过。

## 2. 逐项静态检查

| 检查项 | 检查主题 | 结果 | 本轮证据及限定 |
| --- | --- | --- | --- |
| V003-SC-001 | 既有文件完整性 | PASS | 29 个固定参考文件本地 SHA-256 全部匹配；未改变其内容。 |
| V003-SC-002 | 设计 JSON 可解析性 | PASS | 两个 JSON 设计数据块可解析；不是 Python 导入、运行或配置加载。 |
| V003-SC-003 | 规则与契约草案状态 | PASS | 两者均保持未审查、未接受草案状态。 |
| V003-SC-004 | 适用输入完整且唯一 | PASS | 恰好覆盖既有 V-003 的三个变体，没有新增刺激。 |
| V003-SC-005 | 固定引用身份 | PASS | 输入绑定、门禁源码、fixture 与类型来源的路径及完整 SHA 对齐。 |
| V003-SC-006 | fixture 身份与原始预期 | PASS | 映射目标与原始 fixture 记录相同；未改写 STALE_SYNTHETIC 输入标签。 |
| V003-SC-007 | 参数和适配器固定 | PASS | 四个对象引用、validity_confirmed=true、kill_active=false 均与既有候选相同。 |
| V003-SC-008 | 版本单字段输入 | PASS | SB-003-CAPABILITY-VERSION 的五字段不等向量为 [false,true,false,false,false]；仅比较已存 JSON 数据。 |
| V003-SC-009 | 实现摘要单字段输入 | PASS | SB-003-IMPLEMENTATION-SHA 的五字段不等向量为 [false,false,true,false,false]；仅比较已存 JSON 数据。 |
| V003-SC-010 | 配置摘要单字段输入 | PASS | SB-003-CONFIGURATION-SHA 的五字段不等向量为 [false,false,false,true,false]；仅比较已存 JSON 数据。 |
| V003-SC-011 | 合成值构造格式 | PASS | 版本为非空字符串；两个摘要刺激为 64 位十六进制。仅核对所改字段声明的格式约束，不声称已构造对象。 |
| V003-SC-012 | 早期拒绝排除 | PASS | 配置存在且固定为 ENABLED_CAPABILITY_ONLY，kill=false；不借用早期拒绝。 |
| V003-SC-013 | 源码五字段分支定位 | PASS | 静态文本顺序为 STALE 拒绝、五字段身份拒绝、后续域身份检查；非分支到达实测。 |
| V003-SC-014 | 完整状态与原因预期 | PASS | 两个分支的完整原因字符串明确区分，没有前缀或语义归一化。 |
| V003-SC-015 | 关联标识与声明写入集 | PASS | 预期关联标识来自固定 envelope；空数组仅表示源码声明的空元组预期。 |
| V003-SC-016 | 返回契约静态来源 | PASS | 固定类型文件声明 GateDecision 四字段；不存在 BLOCKED_STALE 枚举。 |
| V003-SC-017 | 独立输出契约绑定 | PASS | 独立 V-003 契约仅绑定本草案规则，不继承 V-002 接受。 |
| V003-SC-018 | 原生对象身份限制 | PASS | 拒绝同名类、字典、子类和鸭子类型；不由设计字符串驱动动态导入。 |
| V003-SC-019 | 枚举与文本类型和值 | PASS | 真实枚举成员与普通字符串分离；原因逐代码点比较。 |
| V003-SC-020 | 关联标识禁止回填 | PASS | 实际关联标识独立核对，不从期望复制到观察。 |
| V003-SC-021 | 空元组与 JSON 编码分离 | PASS | 返回 list 不因显示为 [] 而通过；非空 tuple 保留元素，不得清空。 |
| V003-SC-022 | 检查与表示顺序 | PASS | 输入来源、原生类型、原生值、展示编码、独立映射严格分离。 |
| V003-SC-023 | 失败与异常保留 | PASS | 缺失、异常、类型或值失败不得补成预期，也不得调用未知对象转换方法。 |
| V003-SC-024 | 映射适用范围限制 | PASS | fixture 标签不是运行时别名、时间失效证明或任意拒绝的通用映射。 |
| V003-SC-025 | 非目标输入与提前拒绝排除 | PASS | 明确排除其他身份项、多字段更改、早期拒绝与来源缺失。 |
| V003-SC-026 | 既有绑定观察面缺口保留 | PASS | 既有三条规则引用仍 NOT_ESTABLISHED；新增观察要求尚未集成或准入。 |
| V003-SC-027 | 声明元数据与行为证据分离 | PASS | 不把一次拒绝/空写入声明外推为零 I/O、完整禁止效果或后续授权校验。 |
| V003-SC-028 | 接受和执行边界 | PASS | 仅新建草案与静态说明；不授权执行、关闭限制或扩展 V-002。 |
| V003-SC-029 | 既有输入目录数量 | PASS | 候选仍为 15 场景、28 变体、14 适配器、10 对象、7 规则；V-003 仍 NOT_RUN。 |
| V003-SC-030 | Markdown 物理结构 | PASS | 33 条表格物理行各自列数一致；代码围栏配对、末尾换行、无行尾空白。 |

## 3. 三项独立输入的静态差异

五字段顺序固定为 capability_id、capability_version、implementation_sha256、configuration_sha256、activation_decision_reference。下表的“不等”为已存 JSON 值比较，不是被审函数执行观察。

| 既有输入标识 | 唯一不同字段 | 五字段不等向量 | 保留条件 |
| --- | --- | --- | --- |
| SB-003-CAPABILITY-VERSION | capability_version | false, true, false, false, false | 其他配置字段及所有显式参数不变 |
| SB-003-IMPLEMENTATION-SHA | implementation_sha256 | false, false, true, false, false | 其他配置字段及所有显式参数不变 |
| SB-003-CONFIGURATION-SHA | configuration_sha256 | false, false, false, true, false | 其他配置字段及所有显式参数不变 |

三个变体都引用固定的 OBJ-CONFIG-BASE、OBJ-PACKET-BASE、OBJ-ENVELOPE-BASE 与 OBJ-EXPECTED-BASE。configuration.state 为 ENABLED_CAPABILITY_ONLY，kill_active=false。变体中的合成版本与摘要字符串只作为输入数据，不是资产真实性、时间失效或授权有效性的证据。

静态源码依据：STALE 状态分支先于五字段身份比较；本草案排除前者的 `BLOCKED — VERSION FAILURE`。目标分支声明返回 `InvocationState.BLOCKED` 和完整原因 `BLOCKED — CAPABILITY IDENTITY FAILURE`，并使用 envelope 中的关联标识与原生空元组。上述是文本推导的预期，不是实际 Observed 数据。

原始 fixture 的 `BLOCKED_STALE` 和 `EXACT_IDENTITY_MISMATCH` 仅拟作独立比较层标签；不能覆盖原始返回、推断时间过期，或完整证明 `HISTORICAL_FALLBACK_OR_SILENT_SUBSTITUTION` 禁止效果。

## 4. 既有参考文件完整性清单

以下为本轮只读核对的精确范围：10 个被审实现/契约文件、15 个 fixture、1 个输入绑定候选、V-002 规则草案及其静态记录、1 个验证执行设计参考，共 29 个文件。每项本地计算值与表列固定摘要相同。本清单不宣称已检查整个工作区，也不重新接受这些资产。

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

验证执行设计参考只用于第 10.2 节 V-003 行和第 10.3 节的输入覆盖及预期/观察分离要求。其中保留的 V-002 历史源码限制不是当前源码的新发现，本轮没有重新采用该历史限制作为现状。

## 5. 保留的未完成事项

| 事项 | 当前状态 | 不可外推的内容 |
| --- | --- | --- |
| 新规则 CR-003-EXACT-IDENTITY-MISMATCH-TO-FIXTURE | PROPOSED_NOT_REVIEWED_NOT_ACCEPTED | 静态通过不等于独立审查或规则接受 |
| 新输出契约 OBS-V003-GATEDECISION-EXACT-DRAFT-001 | PROPOSED_NOT_REVIEWED_NOT_ACCEPTED | 不继承 V-002 契约接受或审查结论 |
| 既有 V-003 观察面 | GateDecision.state/reason_code | 草案提出的关联标识和写入集检查尚未集成到绑定 |
| 三个既有 comparison_rule_id | NOT_ESTABLISHED | 不允许临时覆盖、执行时动态补规则或事后映射 |
| 整份输入绑定候选 | NOT ADMITTED BY THIS TASK | 30 项静态检查不等于 15 场景完整输入准入 |
| Python 导入、编译、构造与场景执行 | NOT RUN IN THIS TASK | 无实际返回值、异常或分支到达证据 |
| 完整 prohibited_effect、实际 I/O 和后续授权分支 | NOT VERIFIED BY THIS STATIC CHECK | 空声明写入集或目标分支拒绝不能证明这些属性 |
| Harness、完整依赖与执行方案 | NOT APPROVED BY THIS TASK | 仍需既定独立准入与执行授权 |
| V-002 和其余十四个场景 | UNCHANGED / NOT REOPENED | 不延伸既有接受范围，也不转移历史执行证据 |

后续如继续，需先对本草案的固定 SHA 单独进行只读设计审查，再由 Project Owner 决定是否接受规则。输入绑定修订/准入、Harness 与依赖审查、实际执行及限制项关闭是分离动作，本记录不授予任何一项。

## 6. 操作范围记录

本轮新增范围仅为：

1. `validation/route_b_c03/wp_008/V003_LIMITED_COMPARISON_RULE_DRAFT.md`
2. `validation/route_b_c03/wp_008/V003_LIMITED_COMPARISON_RULE_STATIC_CHECK.md`

未改写上述 29 个既有参考文件；未导入、编译或执行 Python 被审源码，未运行场景，未安装软件，未访问外部模型、网络或独立 ACOS 项目，未处理真实案件，未执行 Git 操作。未产生整体场景 PASS、法律结论、实际运行观察或关闭记录。

本记录不包含自身 SHA；交付摘要在文档外计算，避免循环自指。

