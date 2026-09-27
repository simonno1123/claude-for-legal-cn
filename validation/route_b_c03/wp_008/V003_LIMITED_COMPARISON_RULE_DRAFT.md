# V-003 有限比较规则草案

## 1. 范围、授权与状态

本文件属于 claude-for-legal-cn 项目 Route B / C03 / WP-008，依据 Project Owner 对“生成 V-003 有限比较规则草案并做静态校验”的明确授权编制。

状态：`PROPOSED_NOT_REVIEWED_NOT_ACCEPTED`。仅提出三个既有合成输入的有条件比较映射以及独立的输出类型/表示契约，不修改原始输入绑定、源码、fixture、V-002 已接受规则或历史校验记录。静态自检不等于独立审查、规则接受、输入准入、执行或限制项关闭。

本文件不是 Harness、可执行配置、JSON Schema、测试结果或业务授权。下列 JSON 代码块是非可执行的设计数据。

## 2. 固定参考身份

| 参考对象 | 项目内路径 | SHA-256 | 作用 |
| --- | --- | --- | --- |
| 现有输入绑定候选 | validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_RDM_DSP_002_REVISION_CANDIDATE_REV2.json | 6C78702FCA2D776CE0AD17F4BD00AE65FF5B5C8D216209539FCD5877122B26B9 | 引用 V-003 三种输入、四个基础对象与显式参数；尚未准入，本轮不改写 |
| 当前门禁源码 | scripts/phase2_runtime/route_b_c03/identity_gate.py | 9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445 | 静态核对身份比较分支及实际声明的返回路径 |
| 数据契约 | scripts/phase2_runtime/route_b_c03/contracts.py | 7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4 | 构造参数、枚举、返回类与字段类型的来源 |
| 原始 V-003 测试材料 | validation/route_b_c03/wp_008/fixtures/C03-TA-V-003.json | 21BD65ECD28D569BADFF11489017569E8413B1CC9A5138A851F907CCF62EAF7E | 保留原始 expected_state、reason class 与写入集预期 |
| 验证执行设计参考 | docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V3_1_CANDIDATE.md | 3432D99D22AA288668C8D4E2CF58975A794ED545B62EB05FCA9E0B41525AEDDB | 仅引用 V-003 逐字段覆盖及 Expected / Observed / Comparison 分离要求 |

当前接受的 V-002 规则文件 SHA 为 `94A6A193F299D9A42B40899D1708AE3CD29D435C11911DB424BB7CAAEC9BF875`，本轮只将其视为不得改写或扩展的边界，不把其接受决定传递给 V-003。本草案具有自己的规则及输出契约标识。

## 3. 三个限定输入与目标分支

三种输入都使用固定候选内 ADP-EVALUATE-IDENTITY 的相同显式参数：configuration、packet、envelope、expected 分别引用 OBJ-CONFIG-BASE、OBJ-PACKET-BASE、OBJ-ENVELOPE-BASE、OBJ-EXPECTED-BASE；validity_confirmed 为 true，kill_active 为 false。这些只是合成输入，不证明真实有效期、撤销状态或授权成立。

仅允许各行对应的单字段覆盖；其余字段必须与固定候选中的基础对象和参数逐项一致。每项须独立保留实际输入及来源，禁止只检查变体名称、复用结果或以多字段同时不匹配代替逐字段覆盖。

| 输入标识 | 唯一覆盖位置 | 固定 expected 值 | 合成覆盖值 |
| --- | --- | --- | --- |
| SB-003-CAPABILITY-VERSION | /OBJ-CONFIG-BASE/arguments/capability_version | 1.0-SYNTHETIC | 2.0-SYNTHETIC-MISMATCH |
| SB-003-IMPLEMENTATION-SHA | /OBJ-CONFIG-BASE/arguments/implementation_sha256 | 028EE9DDD7A2C06840A6F344A4C4CC716EFF95073BE39CA6E57FB7FDBBFA6DD5 | DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD |
| SB-003-CONFIGURATION-SHA | /OBJ-CONFIG-BASE/arguments/configuration_sha256 | AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA | EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE |

这些 SHA 形状的合成值只是字符串比较刺激，不是新物理资产摘要，不能据此读取文件或宣称真实资产过期。

### 3.1 前置与分支区分

| 条件 | 限定要求与静态依据 |
| --- | --- |
| 构造参数 | 当前版本刺激是非空字符串；两项合成摘要均为 64 位十六进制，满足固定构造器声明的格式条件。任何实际构造异常都不能替代门禁比较结果 |
| kill | 固定 false，不允许用 KILL ACTIVE 的提前拒绝覆盖身份不匹配 |
| configuration | 必须存在，状态为固定 CapabilityState.ENABLED_CAPABILITY_ONLY；不得改成 DISABLED、REVOKED 或 STALE |
| 五项身份比较 | capability_id、capability_version、implementation_sha256、configuration_sha256、activation_decision_reference 中，必须只有选定版本/实现摘要/配置摘要那一项不相等 |
| 另外两项身份 | capability_id 和 activation_decision_reference 必须相等；它们虽然能触发同一个源码原因，但不在本规则范围内 |
| 其他参数 | 所有非目标字段、packet/envelope/expected 元数据与固定候选保持一致，不从 fixture 的 STALE_SYNTHETIC 标签反推或构造新输入 |
| 后续检查 | 当前目标身份分支在域身份、packet、事项/主体、输出范围及最终授权引用检查之前；此次拒绝不证明后续检查已执行或实际授权有效 |

固定源码先处理 STALE 状态并返回 `BLOCKED — VERSION FAILURE`，随后才进行上述五字段身份比较。三个获准输入保持 ENABLED_CAPABILITY_ONLY，仅改变对应字符串，因此依据源码文本和输入数据应关联的是 `BLOCKED — CAPABILITY IDENTITY FAILURE`。这属于静态预期推导，不是已执行的分支到达证明。

## 4. 拟议规则定义

仅在未来完成规则接受、输入集成/准入、依赖与 Harness 审查及执行授权后，才可使用下述映射。此文件不在现有候选内登记该规则。

```json
{
  "rule_id": "CR-003-EXACT-IDENTITY-MISMATCH-TO-FIXTURE",
  "status": "PROPOSED_NOT_REVIEWED_NOT_ACCEPTED",
  "scenario_id": "C03-TA-V-003",
  "binding_reference": {
    "path": "validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_RDM_DSP_002_REVISION_CANDIDATE_REV2.json",
    "sha256": "6C78702FCA2D776CE0AD17F4BD00AE65FF5B5C8D216209539FCD5877122B26B9",
    "qualification": "READ-ONLY INPUT REFERENCE; NOT ADMISSION OR IN-PLACE INTEGRATION"
  },
  "subject_reference": {
    "path": "scripts/phase2_runtime/route_b_c03/identity_gate.py",
    "sha256": "9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445",
    "callable": "evaluate_identity_gate"
  },
  "fixture_reference": {
    "path": "validation/route_b_c03/wp_008/fixtures/C03-TA-V-003.json",
    "sha256": "21BD65ECD28D569BADFF11489017569E8413B1CC9A5138A851F907CCF62EAF7E",
    "fixture_id": "C03-WP008-FX-003",
    "fixture_version": "1.0"
  },
  "applies_to": [
    "SB-003-CAPABILITY-VERSION",
    "SB-003-IMPLEMENTATION-SHA",
    "SB-003-CONFIGURATION-SHA"
  ],
  "input_condition": "Exact fixed variant arguments plus its one declared configuration-field override; all other object fields unchanged. Kill is false, configuration is present and ENABLED_CAPABILITY_ONLY; only the selected one of five identity comparisons is unequal.",
  "observation_contract_id": "OBS-V003-GATEDECISION-EXACT-DRAFT-001",
  "observation_surface": "GateDecision.state/reason_code/audit_correlation_id/permitted_write_namespaces",
  "observation_scope_qualification": "Proposed V-003 comparison requirements only. Existing binding still records state/reason and NOT_ESTABLISHED; no observation surface or rule ID is installed by this document.",
  "raw_requirement": {
    "state": "BLOCKED",
    "reason_code": "BLOCKED — CAPABILITY IDENTITY FAILURE",
    "audit_correlation_id": "SYNTHETIC-CORRELATION-001",
    "permitted_write_namespaces": []
  },
  "raw_requirement_qualification": "TYPED EXPECTATION JSON ENCODING; NOT AN OBSERVED VALUE. Use the separately proposed V-003 output contract, not the accepted V-002 contract.",
  "fixture_mapping": {
    "expected_state": "BLOCKED_STALE",
    "expected_reason_class": "EXACT_IDENTITY_MISMATCH",
    "expected_permitted_write_set": []
  },
  "mapping_qualification": "Only a separate per-variant fixture abstraction after exact input and native output checks; never replace raw state/reason, create a runtime enum alias, or assert chronological staleness.",
  "comparison_mode": "EXACT_VARIANT_AND_NATIVE_TYPES_AND_VALUES; NO SEMANTIC NORMALIZATION, PREFIX MATCH, FALLBACK OR POST-HOC SUBSTITUTION",
  "mismatch_policy": "Do not map or assert conformance on unknown/mismatched identity, any unintended input difference, missing provenance, type failure, exception, wrong output value or earlier denial. Preserve actual facts; stop the affected comparison and obey the separately accepted run stop policy.",
  "post_hoc_change": "PROHIBITED",
  "acceptance_or_execution_effect": "NONE; NO V-002 SCOPE EXTENSION, INPUT ADMISSION, HARNESS OR SUBJECT EXECUTION, BLOCKER CLOSURE OR AGGREGATE VERDICT"
}
```

### 4.1 原始返回与 fixture 标签不能混同

`BLOCKED_STALE` 继续保留为固定 fixture 的抽象预期标签，不作为 InvocationState 的新枚举成员、全局别名或被审函数的原始返回。对应关系只针对三个固定单字段 exact-identity mismatch 输入，不能由任意 BLOCKED 状态或相同原因字符串单独触发。

此处的 STALE 标签不证明旧版本、时间过期、撤销、历史回退、摘要所代表文件真实性或真实配置失效。版本值不相等甚至可能是“较新”版本；本规则只拟证明固定预期身份与具体刺激不相等后，源码门禁返回限定拒绝。

未来必须分开保留：原始 fixture 预期、实际输入及来源、原生返回/类型来源、可选展示编码、采用的已接受比较规则和单项判定。规则应用不得覆盖原始状态或原因，也不得把预期拷贝为实际观察。

fixture 的 `prohibited_effect` 不因一次返回符合而整体被证明。空允许写入集仅是返回的声明性元数据，不等于已经观察到零实际 I/O、无所有历史回退行为或操作系统写入阻断。缺少单独观察证据的要求继续保留为未验证，不生成场景总体或项目总体 PASS。

## 5. 独立 V-003 输出类型与表示契约草案

此契约是本轮新提议，未接受；不引用 V-002 的 `OBS-GATEDECISION-EXACT-V1` 作为适用契约，不继承其接受或审查结论。

```json
{
  "contract_id": "OBS-V003-GATEDECISION-EXACT-DRAFT-001",
  "status": "PROPOSED_NOT_REVIEWED_NOT_ACCEPTED",
  "applies_to_rule_ids": [
    "CR-003-EXACT-IDENTITY-MISMATCH-TO-FIXTURE"
  ],
  "type_source": {
    "path": "scripts/phase2_runtime/route_b_c03/contracts.py",
    "sha256": "7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4"
  },
  "type_binding": "Exact GateDecision and InvocationState objects from the same fixed, future-admitted module. Descriptive names are not dynamic import/getattr/eval directives; a later independently reviewed literal harness mapping is required.",
  "native_container": "Exactly the bound GateDecision class; no dictionary, subclass, same-name independently loaded class or duck-typed substitution.",
  "fields": {
    "state": {
      "native_type": "Exactly the bound InvocationState enum",
      "native_expectation": "Identity with InvocationState.BLOCKED",
      "encoding": "Actual member value plus original enum type/member/value provenance; a plain string BLOCKED is not an enum observation."
    },
    "reason_code": {
      "native_type": "Exactly built-in str",
      "native_expectation": "BLOCKED — CAPABILITY IDENTITY FAILURE",
      "encoding": "Actual string unchanged; JSON escaping must round-trip identical Unicode code points. No trim, case fold or normalization."
    },
    "audit_correlation_id": {
      "native_type": "Exactly built-in str",
      "native_expectation": "SYNTHETIC-CORRELATION-001",
      "encoding": "Actual string unchanged with the same reversible JSON escaping; no expected-value backfill."
    },
    "permitted_write_namespaces": {
      "native_type": "Exactly built-in tuple; every element, if present, exactly built-in str",
      "native_expectation": "Exactly empty tuple ()",
      "encoding": "Type-valid tuple may be displayed as ordered JSON array while retaining original tuple type; preserve all elements. [] is only the empty-tuple expectation/display encoding, never acceptance of a returned list."
    }
  },
  "sequence": [
    "Verify fixed source, exact input variant and actual return provenance.",
    "Check the exact native container and all four field types before equality shortcuts or conversion.",
    "Compare actual enum singleton, exact code-point strings and empty tuple; preserve any value mismatch.",
    "Optionally encode type-valid actual values losslessly with type provenance for display; encoding cannot turn a mismatch into conformance.",
    "Only after all checks pass, record the fixture abstraction separately from expected values, native observations, display encoding and comparison determination."
  ],
  "failure_policy": "No pass from a JSON projection alone. None, missing fields, wrong types, empty lists, nonempty tuples, changed strings and exceptions cannot be repaired into expected data. Preserve available failure provenance without calling unknown-object conversion methods.",
  "side_effect_limit": "An empty permitted-write tuple is only declared return metadata, not proof of zero actual I/O or successful OS enforcement.",
  "independence": "New unaccepted V-003 draft only. Does not reuse, extend, amend or inherit acceptance of OBS-GATEDECISION-EXACT-V1 or either V-002 rule."
}
```

其中预期 JSON 的空数组表示待比较的原生空元组，不能接纳实际返回的空列表。枚举必须是固定模块中的真实成员单例；普通字符串即使显示同名，也不能通过原生类型检查。所有表示编码在原生类型与值比较之后发生，且保留实际类型和不匹配事实。

现有 V-003 绑定只声明 `GateDecision.state/reason_code`，三个 `comparison_rule_id` 均为 `NOT_ESTABLISHED`。本草案提出同时检查关联标识与允许写入集，但不声称原绑定已包含这两项观察。未来如采纳，必须另行授权修订并审查相应输入绑定的观察面和规则引用；未完成之前不能直接把本文件当执行覆盖层。

## 6. 排除项与失败处理

下表是设计约束反例，不是新测试输入、测试执行或观察结果。

| 情形 | 规则处理要求 |
| --- | --- |
| 仅将 configuration.state 设为 STALE | 不适用；VERSION FAILURE 不等于本规则的 CAPABILITY IDENTITY FAILURE |
| kill、disabled、revoked 等提前拒绝 | 不适用；不能因其同为 BLOCKED 就登记身份比较符合 |
| capability_id 或 activation_decision_reference 不匹配 | 不适用；即使原因相同也不在三个授权输入之内 |
| 多项身份同时不匹配，或其他输入被更改 | 不适用；不能证明指定单字段变体 |
| 只给变体名称、输出或预期，缺少固定输入/实际来源 | 不可评价；不得从输出反推已到达目标分支 |
| 构造异常、缺失返回、类型错误或任一字段值不匹配 | 保留实际失败或异常，停止对应比较，不进行 fixture 映射 |
| 完整原因被截短、翻译、换字符或规范化 | 不符合原生字符串精确要求；禁止前缀匹配或事后补正 |
| 字符串代替枚举、列表/None 代替空元组 | 类型失败；不按 JSON 展示相同而视为符合 |
| 原生 tuple 非空 | 值不匹配，保留真实元素及顺序，不清空以迁就 fixture |
| 规则或来源 SHA 不匹配、撤回，或尚未准入/授权 | 停止，不转移旧 SHA 的执行证据或临时选择其他材料 |

实际运行若另行获授权，停止与后续 NOT RUN 行为须遵守该次已接受的执行方案；本草案不授权继续、重试、修复输入、更改 oracle、注入故障或运行额外对照。

## 7. 变更、接受与执行边界

- 本轮仅新增本草案和配套静态校验说明；不创建新版 SCENARIO_INPUT_BINDING，不增删场景、变体或 fixture，不改变源码及原始预期。
- 固定候选中的未接受或 NOT_ESTABLISHED 字段保持原文。本文件作为新草案存在，不使其自动变为已准入配置。
- 独立固定 SHA 审查、Project Owner 规则接受、新版输入绑定集成与准入、完整依赖绑定、Harness、正式执行以及限制项关闭仍需相应授权和证据。
- V-002 的对话级接受决定不因本轮编制而扩大或撤销。其他十四个场景和全部既有规则的结论不在本轮重审。
- 不调用、导入、编译或执行 Python 被审源码，不安装软件、不运行 OCR、不处理真实案件、不访问外部模型/网络/独立 ACOS，不执行 Git 操作。
- 本轮没有创建实际运行观察或证据，不能据静态分析声称总体安全、法律结论、生产可用或完整 C03 验证通过。

## 8. 后续只读审查重点

1. 三项单字段输入及五字段不等关系是否与固定候选和源码分支严格一致。
2. 是否把 STALE 状态分支、其他身份不匹配或任意 BLOCKED 错归到此规则。
3. fixture 标签对应是否仅作为独立比较层，且没有隐含时间过期或完整 prohibited_effect 已证实的外推。
4. 原生类型、字符串、关联标识和空元组是否先核对再展示，缺失或异常是否保持失败。
5. 新 V-003 输出契约是否保持独立草案，且现有绑定观察面仍需另行集成与准入。
6. 原始文件、既有接受范围及所有非目标事项是否保持原样。
