# DSP-004 B-02 ORDERED 序列来源定位清点候选 REV1

本文件是路径 B 下的 ORDERED 序列来源定位清点候选。它只列出候选定位行。它不准入来源，不接受资产，不把任一 SHA 接受为正式合同，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据仍是路径 B 原句：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本步授权原句是：`写下一项筹备文档，不准入、不接受资产、不关 DSP-004.`

`Signed` 与 `Accepted` 均为 false。`AP-020`、`AP-021`、`AP-022` 的每一行都是 `CANDIDATE_LOCATOR` / `NOT_ADMITTED`。`AP-006` 与 `AP-009` 的实际定位是 null，状态是 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`。

## 1. 形成基准

| 项目 | 本清点的事实 |
| --- | --- |
| 形成时 `HEAD` | `531ca6f0476e235b90430fa5fb9ec9523b12e2ef` |
| 前一筹备增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV3.md` |
| 前一增量说明 SHA-256 | `D8AED53ECE1FD4396F1E187F8840911497051D8FCE260C5FC3F3DC1499BE0F60`（4208 字节） |
| 前一增量 JSON SHA-256 | `D6D94630A3B99A04306DC9DF07A524E372CE97C9E1119F45C49B1E1290319F7A`（2493 字节） |
| 机器可读清点 | `validation/route_b_c03/wp_008/DSP_004_B02_ORDERED_SOURCE_LOCATOR_INVENTORY_REV1_CANDIDATE.json` |
| 该清点 SHA-256 | `86C610B77CAD18A169EDBE18F792A6B69B6BE4E98B327B50B49E012F14D357E7` |
| 该清点字节 | 70228 |
| 受测模块导入或执行 | 未进行 |
| `identity_gate` 调用 | 未进行 |
| Fixture 执行或写入 | 未进行 |
| 场景运行器 | 未运行 |
| 商业 P0 | 未执行，未修改 |

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

本次只用本机 Python 标准库对点名文件做字节散列，并读取 JSON 结构。没有导入 `identity_gate`、捕获候选、合同模块、场景运行器或受测模块。没有执行 Fixture，没有写入 Fixture，没有编译 C#，没有重放业务场景，没有生成 Manifest。

没有读取 `ENVIRONMENT_MANIFEST.md`。没有读取历史 Windows 虚拟环境。没有读取工具缓存。没有使用目录列举顺序。

数组政策 REV3 只作为政策文本被重新散列。它仍是 16317 字节，`39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123`。本次不把它接受为正式 B-02 合同，也不把第 3.1 节的真实来源值填进去。类型合同 REV3 的 SHA `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 本次没有重新散列，也不接受。

点名一个 SHA 只固定文本身份。缺项、乱序和重复只记为 BLOCK，不排序，不补项，不删除。

## 2. 读集

| 文件 | 字节 | SHA-256 | 本清点后的状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_ARRAY_POLICY_REGISTRY_REV3_CANDIDATE.md` | 16317 | `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` | 政策文本已读，未接受为正式合同 |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | 68768 | `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5` | `NOT_ADMITTED` |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json` | 107849 | `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430` | `NOT_ADMITTED` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-001.json` 至 `C03-TA-V-015.json` | 见第 4 节 | 见第 4 节 | `NOT_ADMITTED` |

原绑定的 `binding_id` 是 `C03-WP008-SCENARIO-INPUT-BINDING-CANDIDATE-001`，版本 `0.1`，文内状态是 `MATERIALIZED_NOT_REVIEWED_NOT_ADMITTED`。V2 的 `binding_id` 是 `C03-WP008-SCENARIO-INPUT-BINDING-V3.2-V2.2-CANDIDATE-006`，版本 `0.6`，文内状态是 `MATERIALIZED_NOT_FORMALLY_REVIEWED_NOT_ACCEPTED_NOT_ADMITTED`。本清点不改写这两句。

## 3. AP-006 与 AP-009

| Policy ID | 路径 | 选择器 | 状态 | 实际定位 |
| --- | --- | --- | --- | --- |
| `AP-006` | `runtime_identity.declared_startup_sequence` | `runtime_identity.startup_contract` | `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT` | null |
| `AP-009` | `import_contract.lookup_order` | `import_contract.origin_policy` | `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT` | null |

读集里没有启动序列文件，也没有搜索序列文件。两份绑定文件里没有 `startup_contract`、`origin_policy`、`declared_startup_sequence` 或 `lookup_order`。候选行数是 0。

缺项记为 BLOCK，代码 `NO_RUNTIME_ROOT_LOCATOR`。不补启动步骤，也不补查询身份。

## 4. AP-020

选择器是 `manifest_identity.fixture_catalog`。读集里没有这份 ArtifactRef。实际序列定位保持 null。`UniqueLocatorEstablished` 为 false。

十五个 Fixture 按点名路径逐个读取。读取顺序就是点名顺序 `C03-TA-V-001` 至 `C03-TA-V-015`。每个文件是一个对象。`$.scenario_id` 与文件名相同。文件内没有 15 项数组。唯一的数组是空的 `$.expected_permitted_write_set`，不作为序列。这十五行不拼成目录。

每一行的状态是 `CANDIDATE_LOCATOR` / `NOT_ADMITTED`。位置是 `$.scenario_id`。计数是 1。

| 路径 | 字节 | SHA-256 | 所见 scenario_id |
| --- | --- | --- | --- |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-001.json` | 674 | `C8CEFEDC496D5D0D33E0F21D61B5E3C3354579A8D0E1C74F70640305C65FC99A` | `C03-TA-V-001` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-002.json` | 683 | `257437A2AA80A58C0741F1EC0A5A514E014C633DD974804C6407DB84DB107290` | `C03-TA-V-002` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-003.json` | 713 | `21BD65ECD28D569BADFF11489017569E8413B1CC9A5138A851F907CCF62EAF7E` | `C03-TA-V-003` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-004.json` | 770 | `9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8` | `C03-TA-V-004` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-005.json` | 708 | `4405ADC2CE242B83120B0BA304157B3E6F03687345F764BBBE1E3A2DCF2422DE` | `C03-TA-V-005` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-006.json` | 695 | `9D24E6AFA92F9EF6E895B0B6E4D0E84BDC326E9C4B815E42723B31374CC2FDC8` | `C03-TA-V-006` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-007.json` | 735 | `68D9D63583A0301BDE76C3E60A5F66B7CCDA897C17D58E8DBF282E3E49C3DB90` | `C03-TA-V-007` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-008.json` | 711 | `7AA3FEF0CCDFA0C6A462C7945B63A50D828AC9C6D0725F428D347F6836075193` | `C03-TA-V-008` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-009.json` | 687 | `34EFBC55490FB2E3FFC89CAFCAD9DD2D319C2C24D9B3E2B026143F74A73DC93C` | `C03-TA-V-009` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-010.json` | 687 | `19DF9D35835F60C03C969B79B25F62CFE95E28C0A1B8122EDD8B9E1A5BC0E67A` | `C03-TA-V-010` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-011.json` | 753 | `8795DA58E092E6DC7F88958E3AC60B754870F5BFAE15FF8BC2D699450B65FDFD` | `C03-TA-V-011` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-012.json` | 696 | `8C6E4FC6279E95CFE48C9E9DA6E161F0AF05CA5FFEA95BE18DBAD6A81204E8E6` | `C03-TA-V-012` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-013.json` | 758 | `3DBF0F60AC970F90C97CF85F5F21F1758B4818D814A02CE8ED03A4F1C3A49CA6` | `C03-TA-V-013` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-014.json` | 704 | `D3EF698EA45F41824CCF6C5A7020F6A0B495460341ADE7446461A1AAF0E7D523` | `C03-TA-V-014` |
| `validation/route_b_c03/wp_008/fixtures/C03-TA-V-015.json` | 767 | `06DCEBA08CA43C75439B5A2AC1C140905887EF8CDC26C561FBD68E9A001D5AE1` | `C03-TA-V-015` |

另有两行候选，位置都是 `$.fixture_identities`。它是 JSON 对象，不是数组。两份绑定文件里的解析结果相同。键的出现顺序是上表十五个路径。值与对应文件的 SHA-256 相同。相同只是本次只读所见。键顺序不采用为 ORDERED 序列。

| 路径 | 字节 | SHA-256 | 结构 | 计数 |
| --- | --- | --- | --- | --- |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | 68768 | `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5` | JSON 对象 | 15 |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json` | 107849 | `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430` | JSON 对象 | 15 |

BLOCK，均未修复：

- `FIXTURE_CATALOG_ARTIFACT_ABSENT`：没有 `fixture_catalog` 制品。十五个文件没有被拼成目录序列。
- `FIXTURE_FILES_ARE_SEPARATE_OBJECTS`：每个文件只有一个 `scenario_id`。文件名相符不是目录序列。
- `FIXTURE_IDENTITIES_IS_A_MAP`：对象键顺序不是 ORDERED 序列。两份对象相同也不构成唯一的已准入目录。

这十五个 `scenario_id` 没有缺项、乱序或重复。该外观不是通过。

## 5. AP-021

选择器是 `input_contract.binding`。实际序列定位保持 null。两行候选的位置都是 `$.scenarios`。身份字段是 `scenario_id`。状态都是 `CANDIDATE_LOCATOR` / `NOT_ADMITTED`。

| 路径 | 字节 | SHA-256 | 字段偏移 | 计数 |
| --- | --- | --- | --- | --- |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | 68768 | `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5` | 24523 | 15 |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json` | 107849 | `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430` | 40336 | 15 |

两个数组的所见顺序相同，都是：

`C03-TA-V-001`，`C03-TA-V-002`，`C03-TA-V-003`，`C03-TA-V-004`，`C03-TA-V-005`，`C03-TA-V-006`，`C03-TA-V-007`，`C03-TA-V-008`，`C03-TA-V-009`，`C03-TA-V-010`，`C03-TA-V-011`，`C03-TA-V-012`，`C03-TA-V-013`，`C03-TA-V-014`，`C03-TA-V-015`。

数组内部没有缺项，没有重复，也没有乱序。外观相符不是通过，也不是准入。两个数组不合并，也不挑选其中一份。

V2 在 `$.comparison_rule_catalog.CR-003-EXACT-IDENTITY-MISMATCH-TO-FIXTURE.scenario_id` 另有一个 `C03-TA-V-003`。它不在 `$.scenarios` 里。不把它插入场景数组，也不把它算成数组内重复。原绑定的 `scenario_id` 只出现在 `$.scenarios`。这条记录的处置是 `RECORDED_NOT_INSERTED`，代码 `OUT_OF_ARRAY_OCCURRENCE_NOT_MERGED`。

BLOCK，均未修复：

- `LOCATOR_NOT_UNIQUE`：两份未准入文件各有一个场景数组。
- `SOURCE_NOT_ADMITTED`：两份文件的文内状态都写明未准入。

## 6. AP-022

政策路径是 `input_contract.scenarios[].variants`，身份键是 `variant_id`。两份文件里的字段名是 `stimulus_variants`。`variant_id` 出现次数是 0。观察到的身份字段是 `stimulus_binding_id`。不改名。不把 `stimulus_binding_id` 或 `design_variant_id` 写成 `variant_id`。

实际序列定位保持 null。每一场景在两份文件里各有一行。状态都是 `CANDIDATE_LOCATOR` / `NOT_ADMITTED`。位置是 `$.scenarios[n].stimulus_variants`。原绑定文件身份见第 5 节第一行。V2 文件身份见第 5 节第二行。

场景内没有重复的 `stimulus_binding_id`。没有删除任何一项。原绑定共 25 行，V2 共 28 行。跨场景也没有重复。跨场景没有重复只是所见，不新建全局唯一规则。

下表的 V2 列在十四个场景上与原绑定外观相同。相同外观仍是两行候选，不并成一条已准入序列。

| 场景 | 原绑定所见顺序 | 原计数 | V2 所见顺序 | V2 计数 |
| --- | --- | --- | --- | --- |
| `C03-TA-V-001` | `SB-001-MISSING-PACKET` | 1 | 与原绑定该项外观相同 | 1 |
| `C03-TA-V-002` | `SB-002-MALFORMED-CONSTRUCTOR`，`SB-002-UNREACHABLE-AUTHORITY-COMPARISON` | 2 | `SB-002-MALFORMED-CONSTRUCTOR`，`SB-002-MATTER-AUTHORITY-MISMATCH`，`SB-002-EXECUTION-AUTHORITY-MISMATCH`，`SB-002-PACKET-DECISION-MISMATCH`，`SB-002-ALL-REFERENCES-MATCH-CONTROL` | 5 |
| `C03-TA-V-003` | `SB-003-CAPABILITY-VERSION`，`SB-003-IMPLEMENTATION-SHA`，`SB-003-CONFIGURATION-SHA` | 3 | 与原绑定该项外观相同 | 3 |
| `C03-TA-V-004` | `SB-004-MATTER-ID`，`SB-004-MATTER-VERSION`，`SB-004-ACTOR` | 3 | 与原绑定该项外观相同 | 3 |
| `C03-TA-V-005` | `SB-005-PROHIBITED-KEY` | 1 | 与原绑定该项外观相同 | 1 |
| `C03-TA-V-006` | `SB-006-REFERENCE-CONSTRUCTION-ONLY` | 1 | 与原绑定该项外观相同 | 1 |
| `C03-TA-V-007` | `SB-007-ELIGIBILITY` | 1 | 与原绑定该项外观相同 | 1 |
| `C03-TA-V-008` | `SB-008-REFERENCE-CONSTRUCTION-ONLY` | 1 | 与原绑定该项外观相同 | 1 |
| `C03-TA-V-009` | `SB-009-CONFIG-REVOKED`，`SB-009-PROTECTED-STATE` | 2 | 与原绑定该项外观相同 | 2 |
| `C03-TA-V-010` | `SB-010-GATE-KILL`，`SB-010-PROTECTED-STATE`，`SB-010-NO-RELEASE` | 3 | 与原绑定该项外观相同 | 3 |
| `C03-TA-V-011` | `SB-011-REFERENCE-CONSTRUCTION-ONLY` | 1 | 与原绑定该项外观相同 | 1 |
| `C03-TA-V-012` | `SB-012-INTEGRITY-REFERENCE`，`SB-012-AUDIT-CANDIDATE` | 2 | 与原绑定该项外观相同 | 2 |
| `C03-TA-V-013` | `SB-013-NULL-PROVIDER` | 1 | 与原绑定该项外观相同 | 1 |
| `C03-TA-V-014` | `SB-014-ACOS-NAMESPACE`，`SB-014-ROUTE-A-NAMESPACE` | 2 | 与原绑定该项外观相同 | 2 |
| `C03-TA-V-015` | `SB-015-CANDIDATE-CONSTRUCTION` | 1 | 与原绑定该项外观相同 | 1 |

V2 的 `C03-TA-V-002` 五项另有 `design_variant_id`：`V002-BIND-01`，`V002-BIND-02`，`V002-BIND-03`，`V002-BIND-04`，`V002-BIND-05`。原绑定的 `C03-TA-V-002` 没有该字段。该字段不替代 `variant_id`。

`C03-TA-V-002` 的两条序列都保留。不删除 `SB-002-UNREACHABLE-AUTHORITY-COMPARISON`。不把 V2 的五项补进原绑定。不把原绑定的两项改成 V2。

BLOCK，均未修复：

- `POLICY_IDENTITY_FIELD_ABSENT`：`variant_id` 不在。
- `OBSERVED_FIELD_NAME_DIFFERS`：所见字段是 `stimulus_variants`，政策路径写的是 `variants`。
- `LOCATOR_NOT_UNIQUE`：十四个场景外观相同，仍然是两份文件。
- `SOURCE_NOT_ADMITTED`：两份绑定都不是已准入的 `input_contract.binding`。
- `CANDIDATE_SEQUENCES_DIFFER`：`C03-TA-V-002` 的计数是 2 与 5。

## 7. 本清点故意不做的事

- 不把任何候选行准入为实际序列来源。
- 不把两个 REV3 SHA `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` 接受为正式 B-02 合同。
- 不完成 `DSP004-FA-04`。B-02 保持 `OPEN`。
- 不完成 `DSP004-FA-03`。该关卡仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。
- 不调用 `identity_gate`，不执行 Fixture、场景运行器或受测模块，不写 Fixture。
- 不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。
- 不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，不关闭 DSP-004。
- 不为来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 新增第二份设计复核文件。
- 不改商业 P0。
- 三个实际侧仍为 null / `UNBOUND`：`SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。
- REV1 点名的七个既有捕获候选仍是 `NOT_SELECTED` / `NOT_ADMITTED`。本清点不装载它们，也不挑选它们。

## 8. 本清点的效力

```text
CANDIDATE LOCATORS RECORDED — NOT ADMITTED

AP-006 / AP-009：NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT / 实际定位 null
AP-020 / AP-021 / AP-022：候选行已记录 / 实际序列定位 null / NOT_ADMITTED
两个 REV3 SHA 的正式合同接受：未建立
B-02：OPEN
DSP004-FA-03：MISSING_BINDING_AND_ACTUAL_ENTRY / 未完成
DSP004-FA-04：未完成
DSP004-FA-08：未完成
DSP-004：OPEN / HOLD
```

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

本清点不接受任何固定 SHA 为正式合同、Manifest 或来源准入。没有真实案件、个人信息、凭据或供应商调用。
