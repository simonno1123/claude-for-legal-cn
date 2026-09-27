# RDM-DSP-002 比较规则草案

## 1. 范围和状态

本草案仅配套新版 Scenario Input Binding 的 V-002 五种输入，依据本轮 Project Owner“授权生成该候选及比较规则草案，并进行静态校验”生成。它不是 Harness、测试执行结果、独立审查、规则接受决定或输入准入决定。

状态：`PROPOSED_NOT_REVIEWED_NOT_ACCEPTED`。RDM-DSP-002 保持开放，完整验证和业务执行未授权。

| 绑定对象 | 项目内路径 | SHA-256 |
| --- | --- | --- |
| 新版输入绑定候选 | validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_RDM_DSP_002_REVISION_CANDIDATE.json | 738252342529332DB521A51E653D7E6FE32ED44EC6DA66C5F278D35BAEF99ECF |
| 原始输入绑定（保留） | validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json | 92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5 |
| 当前已修复源码 | scripts/phase2_runtime/route_b_c03/identity_gate.py | 9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445 |
| 数据契约 | scripts/phase2_runtime/route_b_c03/contracts.py | 7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4 |
| 已接受有限设计提案 | docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_DSP_002_AUTHORITY_COMPARISON_REACHABILITY_LIMITED_SUBJECT_DESIGN_PROPOSAL.md | 85D7A4029D9667EFF7922CEDAA19570A7C6A68F36C2D6A66401F291B5F135A24 |

新版候选携带完整合成对象、全部参数及单字段覆盖。本文件说明对应规则，不提供隐式默认值、不修改原测试材料。任何冲突都必须停止使用并重新核对，不能在执行时自行选择较宽松的表述。

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
  "comparison_mode": "EXACT_FIELD_VALUES; NO NORMALIZATION, PREFIX MATCH OR REASON SUBSTITUTION",
  "mismatch_policy": "DO_NOT_ASSERT_CONFORMANCE; PRESERVE RAW MISMATCH OR EXCEPTION AND STOP THE AFFECTED COMPARISON",
  "post_hoc_change": "PROHIBITED",
  "scope": "THREE INDIVIDUAL V-002 GATE REFERENCE-CONSISTENCY MISMATCH VARIANTS ONLY",
  "authority_qualification": "METADATA CONSISTENCY ONLY; NOT AUTHORIZATION VALIDATION OR EXECUTION PERMISSION"
}
```

三种输入必须分别保留各自的原始输出，不能只测一项后把结果复制给另外两项。只有四个返回字段均精确匹配草案要求时，才能在未来获授权的比较中记录该项符合性。

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
  "comparison_mode": "EXACT_FIELD_VALUES; POSITIVE RAW CONTROL ONLY",
  "mismatch_policy": "DO_NOT_ASSERT_CONFORMANCE; PRESERVE RAW MISMATCH OR EXCEPTION AND STOP THE AFFECTED COMPARISON",
  "post_hoc_change": "PROHIBITED",
  "scope": "ONE V-002 ALL-MATCH CONTROL ONLY; NEGATIVE FIXTURE ORACLE DOES NOT APPLY",
  "authority_qualification": "ELIGIBILITY RETURN ONLY; NO AUTHORITY GRANT, BUSINESS MAPPING OR EXECUTION"
}
```

原测试材料 C03-TA-V-002 的 `expected_state: BLOCKED` 保持不变，仅用于指定负向输入。正向对照的 `fixture_mapping` 为 null，其预期直接来自已接受设计的原始返回值要求；不能修改原测试材料以迁就正向结果，也不能把正向结果重命名为 BLOCKED。

`ELIGIBLE_FOR_MAPPING` 仅表示门禁元数据分支返回资格状态，不证明真实授权存在、有效或充分，不运行映射、不授予业务调用权。原因文本中要求另行事项调用授权的语义必须完整保留。

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

- 原版 JSON、15 份测试材料、10 个合成对象以及其他 14 个场景记录保持原样。
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
