# RDM-DSP-002 比较规则草案 REV2 — 输出类型与表示契约

## 1. 范围和状态

本草案仅配套 REV2 Scenario Input Binding 的 V-002 五种输入。依据 Project Owner 本轮“授权操作。”对上一轮明确提出的“仅补充候选与规则中的输出类型及比较表示契约”进行有限修订及静态校验。它不是 Harness、测试执行结果、独立审查、规则接受决定或输入准入决定。上一版候选、草案和静态校验记录保留原样；本轮不追溯修改历史结论。

状态：`PROPOSED_NOT_REVIEWED_NOT_ACCEPTED`。RDM-DSP-002 保持开放，完整验证和业务执行未授权。

| 绑定对象 | 项目内路径 | SHA-256 |
| --- | --- | --- |
| 新版输入绑定候选 | validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_RDM_DSP_002_REVISION_CANDIDATE_REV2.json | 6C78702FCA2D776CE0AD17F4BD00AE65FF5B5C8D216209539FCD5877122B26B9 |
| 原始输入绑定（保留） | validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json | 92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5 |
| 当前已修复源码 | scripts/phase2_runtime/route_b_c03/identity_gate.py | 9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445 |
| 数据契约 | scripts/phase2_runtime/route_b_c03/contracts.py | 7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4 |
| 已接受有限设计提案 | docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_DSP_002_AUTHORITY_COMPARISON_REACHABILITY_LIMITED_SUBJECT_DESIGN_PROPOSAL.md | 85D7A4029D9667EFF7922CEDAA19570A7C6A68F36C2D6A66401F291B5F135A24 |

新版候选携带完整合成对象、全部参数及单字段覆盖。本文件说明对应规则，不提供隐式默认值、不修改原测试材料。任何冲突都必须停止使用并重新核对，不能在执行时自行选择较宽松的表述。

上一版候选 SHA：`738252342529332DB521A51E653D7E6FE32ED44EC6DA66C5F278D35BAEF99ECF`；上一版规则草案 SHA：`766B611BBD04C6A37F81DED5D4F7BCFDB6D5D8D13BBC870DAA14FA61FFABB71D`。它们不被新文件覆盖，旧静态自检也不能代替本次输出表示契约的校验。

## 2. 五种输入与规则分离

| 设计变体 | 输入标识 | 唯一目标差异 | 规则 | 比较性质 |
| --- | --- | --- | --- | --- |
| V002-BIND-01 | SB-002-MALFORMED-CONSTRUCTOR | ExpectedIdentityReference 的 matter_authorization_reference 为空字符串 | CR-002-CONSTRUCTOR-FAILURE | 保留既有构造失败规则；不调用门禁 |
| V002-BIND-02 | SB-002-MATTER-AUTHORITY-MISMATCH | envelope.matter_authorization_reference 与 expected 对应值不一致 | CR-002-AUTHORITY-BINDING-FAILURE | 负向门禁参考一致性比较 |
| V002-BIND-03 | SB-002-EXECUTION-AUTHORITY-MISMATCH | envelope.execution_authorization_reference 与 expected 对应值不一致 | CR-002-AUTHORITY-BINDING-FAILURE | 负向门禁参考一致性比较 |
| V002-BIND-04 | SB-002-PACKET-DECISION-MISMATCH | packet.decision_reference 与 expected.execution_authorization_reference 不一致 | CR-002-AUTHORITY-BINDING-FAILURE | 负向门禁参考一致性比较 |
| V002-BIND-05 | SB-002-ALL-REFERENCES-MATCH-CONTROL | 无字段覆盖；所有引用匹配 | CR-002-ALL-MATCH-CONTROL | 正向原始返回值对照；不映射负向测试材料 |

构造失败要求保持原样：异常类型 `ValueError`，消息 `matter_authorization_reference must be a non-empty explicit value`。该规则的历史定义不在本轮改写；其旧输入绑定下的接受记录不自动接纳整个新版候选。

新增两条而非合并为一条规则，是为了覆盖已接受设计要求的负向门禁比较和正向对照。不是增加新的业务操作或扩大测试范围。

## 3. 新增负向比较规则

以下定义与候选中的同名目录项一致：

```json
{
  "status": "PROPOSED_NOT_REVIEWED_NOT_ACCEPTED",
  "applies_to": [
    "SB-002-MATTER-AUTHORITY-MISMATCH",
    "SB-002-EXECUTION-AUTHORITY-MISMATCH",
    "SB-002-PACKET-DECISION-MISMATCH"
  ],
  "observation_surface": "GateDecision.state/reason_code/audit_correlation_id/permitted_write_namespaces",
  "raw_requirement": {
    "state": "BLOCKED",
    "reason_code": "BLOCKED — AUTHORITY BINDING FAILURE",
    "audit_correlation_id": "SYNTHETIC-CORRELATION-001",
    "permitted_write_namespaces": []
  },
  "fixture_mapping": {
    "expected_state": "BLOCKED",
    "expected_reason_class": "AUTHORITY_OR_IDENTITY_FAILURE"
  },
  "comparison_mode": "EXACT_NATIVE_TYPES_AND_VALUES; LOSSLESS_EVIDENCE_ENCODING_ONLY; NO SEMANTIC NORMALIZATION, PREFIX MATCH OR REASON SUBSTITUTION",
  "mismatch_policy": "DO_NOT_ASSERT_CONFORMANCE; PRESERVE RAW MISMATCH OR EXCEPTION AND STOP THE AFFECTED COMPARISON",
  "post_hoc_change": "PROHIBITED",
  "scope": "THREE INDIVIDUAL V-002 GATE REFERENCE-CONSISTENCY MISMATCH VARIANTS ONLY",
  "authority_qualification": "METADATA CONSISTENCY ONLY; NOT AUTHORIZATION VALIDATION OR EXECUTION PERMISSION",
  "observation_contract_id": "OBS-GATEDECISION-EXACT-V1",
  "raw_requirement_qualification": "TYPED_EXPECTATION_JSON_ENCODING_ONLY; NOT_RAW_OBSERVATION; APPLY_OBS-GATEDECISION-EXACT-V1_BEFORE_EVIDENCE_ENCODING"
}
```

三种输入必须分别保留各自的原始输出，不能只测一项后把结果复制给另外两项。只有原生返回容器和四个字段的类型及值均按第 4.1 节精确匹配草案要求时，才能在未来获授权的比较中记录该项符合性。

原始 `GateDecision` 与测试材料抽象分开保存。不得把其他 BLOCKED 原因、早期拒绝、异常或缺失字段视为本规则成功。不得截断原因、替换字符、进行前缀匹配、补齐关联标识或把非空写入集清空。

## 4. 新增正向对照规则

以下定义与候选中的同名目录项一致：

```json
{
  "status": "PROPOSED_NOT_REVIEWED_NOT_ACCEPTED",
  "applies_to": [
    "SB-002-ALL-REFERENCES-MATCH-CONTROL"
  ],
  "observation_surface": "GateDecision.state/reason_code/audit_correlation_id/permitted_write_namespaces",
  "raw_requirement": {
    "state": "ELIGIBLE_FOR_MAPPING",
    "reason_code": "ELIGIBLE — SEPARATE MATTER INVOCATION AUTHORITY STILL REQUIRED",
    "audit_correlation_id": "SYNTHETIC-CORRELATION-001",
    "permitted_write_namespaces": []
  },
  "fixture_mapping": null,
  "comparison_mode": "EXACT_NATIVE_TYPES_AND_VALUES; LOSSLESS_EVIDENCE_ENCODING_ONLY; POSITIVE RAW CONTROL ONLY; NO SEMANTIC NORMALIZATION",
  "mismatch_policy": "DO_NOT_ASSERT_CONFORMANCE; PRESERVE RAW MISMATCH OR EXCEPTION AND STOP THE AFFECTED COMPARISON",
  "post_hoc_change": "PROHIBITED",
  "scope": "ONE V-002 ALL-MATCH CONTROL ONLY; NEGATIVE FIXTURE ORACLE DOES NOT APPLY",
  "authority_qualification": "ELIGIBILITY RETURN ONLY; NO AUTHORITY GRANT, BUSINESS MAPPING OR EXECUTION",
  "observation_contract_id": "OBS-GATEDECISION-EXACT-V1",
  "raw_requirement_qualification": "TYPED_EXPECTATION_JSON_ENCODING_ONLY; NOT_RAW_OBSERVATION; APPLY_OBS-GATEDECISION-EXACT-V1_BEFORE_EVIDENCE_ENCODING"
}
```

原测试材料 C03-TA-V-002 的 `expected_state: BLOCKED` 保持不变，仅用于指定负向输入。正向对照的 `fixture_mapping` 为 null，其预期直接来自已接受设计的原始返回值要求；不能修改原测试材料以迁就正向结果，也不能把正向结果重命名为 BLOCKED。

`ELIGIBLE_FOR_MAPPING` 仅表示门禁元数据分支返回资格状态，不证明真实授权存在、有效或充分，不运行映射、不授予业务调用权。原因文本中要求另行事项调用授权的语义必须完整保留。

## 4.1. 原生比较与 JSON 展示契约

唯一契约标识：`OBS-GATEDECISION-EXACT-V1`。候选将完整定义存放于 `representation_contract.gate_decision_output`，两条新草案规则通过 `observation_contract_id` 引用它。仅适用于 V002-BIND-02 至 V002-BIND-05；包括构造器规则在内的五条历史规则均不采用或继承本新增契约。

`raw_requirement` 字段名为兼容上一版保持不变，其 JSON 值是**带类型约束的预期编码，不是原始观察值**。状态字符串、完整原因、关联标识和空写入集的预期语义均不改变；JSON 编码相同不等于原生类型相同。

| 观察对象或字段 | 原生类型与比较要求 | 允许的 JSON 展示编码 |
| --- | --- | --- |
| 返回容器 | 必须恰为固定 contracts 源码所绑定的 GateDecision 类，不接受字典、同名类、子类、异常或鸭子类型替代 | 仅展示已观察字段，并保留实际类来源；候选中的类型名称不是动态导入指令 |
| state | 必须恰为同一绑定模块的 InvocationState；负向是 BLOCKED 单例，正向是 ELIGIBLE_FOR_MAPPING 单例；不能仅靠 str 枚举与字符串相等通过 | 原样记录实际成员的 value，同时保留枚举类型、成员 name 和 value；不从普通字符串构造成员 |
| reason_code | 必须恰为内置 str；按完整 Unicode 码点序列比较，不裁剪、不规范化、不替换、不作前缀匹配 | 原样复制实际字符串；JSON 转义还原后须得到相同码点序列 |
| audit_correlation_id | 必须恰为内置 str；与固定预期逐码点一致，不补齐或从预期回填 | 原样复制实际字符串，遵守同一可逆转义要求 |
| permitted_write_namespaces | 必须恰为内置 tuple；若存在元素，每项恰为内置 str；两规则的原生预期均是空元组 ()；非空元组不符合预期，列表、集合、生成器、None 或缺失字段不能替代 | 类型检查通过后，实际 tuple 按原顺序编码为 JSON 数组，并在同一来源记录保留原始 tuple 类型；空元组对应 []，非空元组必须保留所有元素，不能清空 |

执行顺序仅为未来获授权 Harness 的设计要求，本轮没有创建或运行 Harness：

1. 先绑定同一份固定源码的真实类对象及逐变体实际返回来源。独立加载的同名类、未准入模块或者期望值复制都不能替代。
2. 先检查原生容器和全部四个字段的精确类型，再比较原生枚举成员、完整字符串和空元组；禁止先通用转换再比较。
3. 对类型合规的实际观察，可生成保留类型来源的无损 JSON 展示；即使值不匹配，也必须保留实际值与不匹配判定，不能改成预期。编码只是展示，不得改变原生比较结果。
4. 类型错误、缺失观察、异常或任意值不匹配时，保留可用原始来源与失败信息，停止对应比较，不得用未知对象的转换方法制造可序列化观察。
5. 只有负向变体的原生比较全部符合，才可采用原有 `fixture_mapping`。正向对照始终不映射负向 fixture。任何 JSON 展示值单独出现都不能建立符合性。

预期编码、原生观察及类型来源、可选 JSON 展示、比较判定须按每个变体分开记录；不得回填、跨变体复制或覆盖。此要求不在本轮生成任何运行证据文件或新 JSON Schema。

下列为**契约反例检查要求，并非已执行用例**：

| 情形 | 契约要求 |
| --- | --- |
| 真正的 InvocationState.BLOCKED 与普通字符串 "BLOCKED" 显示相同 | 普通字符串是类型失败，不能靠字符串相等通过 |
| 真正的空元组 () 与普通空列表 [] 可能序列化相同 | 列表是类型失败；只有经类型核验的原生空元组满足空写入集 |
| 非空字符串元组 | 原生值不匹配；展示必须保留元素，不能编码为 [] |
| None、缺失字段或错误元素类型 | 类型或观察失败；不得补成空元组或空数组 |
| 原因文本增加空白或改变 Unicode 字符 | 原生值不匹配；不得在比较前做规范化 |
| 正向返回满足原生类型和值 | 仅为正向原始对照符合性；不产生授权或负向 BLOCKED 结论 |

REV2 将上一版“NO NORMALIZATION”明确为禁止语义规范化、为通过而强制类型转换和事后预期修改；仅允许本节已界定的、保留类型来源的可逆展示编码。不是在原始比较中把数组与元组视为等价。输入对象既有 enum/tuple 转换契约保持原样，不替代或扩张本输出契约。

## 5. 静态前置条件与未来比较边界

| 前置条件 | 绑定要求 |
| --- | --- |
| 配置状态 | OBJ-CONFIG-BASE 为 ENABLED_CAPABILITY_ONLY；不代表真实能力被启用 |
| 配置身份 | capability_id、capability_version、implementation_sha256、configuration_sha256、activation_decision_reference 与 expected 对应值一致 |
| 域身份 | route、route_version、domain_id、domain_version、adapter_contract_version 与 expected 对应值一致 |
| 授权包状态 | OBJ-PACKET-BASE 为 ACCEPTED，revocation_state 为 CLEAR |
| 有效性和停机输入 | validity_confirmed 为 true，kill_active 为 false；只为合成布尔输入，不是实际时间或撤销校验 |
| 事项和主体 | packet 与 envelope 的 matter_id、matter_version、actor_reference 一致 |
| 范围和集合 | packet 与 envelope 的 purpose、operation、input_set_sha256 一致 |
| 输出范围 | packet.output_class 在 envelope.requested_output_scope 中 |
| 最终引用 | 三个负向变体各只有目标引用不一致；正向变体三个引用全一致 |
| 观察约束 | 关联标识原样返回；允许写入命名空间为空；不产生业务副作用 |

这些条件是对候选 JSON 值与固定源码文本的静态对齐要求，不是本轮运行结果。原始数据、预期、未来观察与比较判定必须分开；缺失观察不得用预期值填充。未来 Harness 不得自行生成总体合格结论或改变失败判据。

## 6. 版本、其他场景与未完成项

- 相对上一版候选，本轮全部 15 个场景（含 V-002 的五种输入）、28 个变体、14 个适配器、10 个合成对象、全部源码身份、原始预期与 fixture_mapping 均保持原样；仅补充输出契约及其规则引用、比较口径与版本来源。
- 完整候选包含 15 个场景、28 种输入、14 个适配器、10 个合成对象、7 条规则目录项，其中 5 条为未改写的历史定义，2 条为本轮新增草案。
- ADP-EVALUATE-IDENTITY 的源码 SHA 是共享引用。其他场景内容虽然未变，其旧 SHA 下的审查或执行证据不能自动转移到新源码。
- 原有五条规则中的 PROPOSED_NOT_ACCEPTED 文字作为形成时快照保留；已有旧版脱离式接受记录不等于新版输入绑定或新增规则接受。本轮不重审、不重写其他事项的结论。
- 独立固定 SHA 规则审查、Project Owner 接受、新版输入绑定准入、完整运行依赖绑定及正式执行仍未完成。
- 本轮静态检查只是作者自检，不称为独立审查、跨供应商审查或正式阶段接受。
- 不改源码、不创建 Harness、不安装依赖、不执行场景、不接入真实事项、不运行 OCR、不访问外部模型或独立 ACOS，不执行 Git 提交/推送。

## 7. 后续审查重点

1. 新版候选与本草案的固定 SHA、每项输入标识及适用范围是否一致。
2. 三项单独不匹配的非目标字段是否足以通过前置检查，且不能被构造失败替代。
3. 负向原始返回值与测试材料抽象是否严格分离。
4. 正向对照是否完全排除负向测试材料映射，并保留另行授权要求。
5. 原始原因、关联标识、写入集及缺失/异常处理是否禁止事后补正。
6. 既有规则、其他场景及原始材料是否保持原样，且不转移旧 SHA 的执行证据。
7. 是否仍保持未接受、未准入、未执行和 RDM-DSP-002 未关闭状态。
8. 是否先验证原生类型和值，再进行保留类型来源的展示编码；空数组、字符串或缺失字段不得掩盖原生类型错误。
