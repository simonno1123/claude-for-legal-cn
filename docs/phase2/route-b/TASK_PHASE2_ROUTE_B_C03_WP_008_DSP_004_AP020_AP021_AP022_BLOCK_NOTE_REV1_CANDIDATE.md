# DSP-004 AP-020、AP-021、AP-022 BLOCK 注记候选 REV1

本注记只重述已经在 `main` 上的 ORDERED 清点，以及 REV5 独立静态复核里关于 `AP-020`、`AP-021`、`AP-022` 的所见。它不修复任何 BLOCK，不准入任何定位，不合并候选序列，不挑选其中一份，不接受资产，不准入来源，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本步授权原句是：`写下一项筹备文档，不准入、不接受资产、不关 DSP-004.`

`Signed` 与 `Accepted` 均为 false。准入状态是 `NOT_ADMITTED`。新增筹备事实的名称是 `AP020_AP021_AP022_BLOCK_NOTE_NOT_ADMITTED`。`UniqueLocatorEstablished` 保持 false。外观相符不是通过，也不是准入。

## 1. 形成基准

| 项目 | 本注记的事实 |
| --- | --- |
| 形成时 `HEAD` | `9cfc1e8b4ed4b6494c330e6c8950856ed9bf2c70` |
| 前一筹备增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV9.md` |
| 前一增量说明 SHA-256 | `AB7D4233FBDF41A362BFD0360AC9BCB82C7C45D280BB55FECB801ABD0C18D159`（9220 字节） |
| 前一增量 JSON SHA-256 | `80A76D83CE91B012608F784712F76B329F37AA7B93A5A3073C5DDE3122165C09`（8091 字节） |
| 机器可读注记 | `validation/route_b_c03/wp_008/DSP_004_AP020_AP021_AP022_BLOCK_NOTE_REV1_CANDIDATE.json` |
| 该注记 SHA-256 | `C1C00CEA5DF3D5EBE0BB7861308339B32007CC6FD97E5957981B49D1AEFBCA3D` |
| 该注记字节 | 19308 |
| 受测模块导入或执行 | 未进行 |
| `identity_gate` 导入或调用 | 未进行 |
| Fixture 执行或写入 | 未进行 |
| 场景运行器 | 未运行 |
| 捕获代码 | 未执行 |
| 商业 P0 | 未执行，未修改 |

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

本次使用本机 Python 标准库只做字节散列，并读取已经在 `main` 上的 REV9、ORDERED 清点，以及 FA-03 与 ORDERED 清点的独立静态复核。散列只固定文本身份。散列不是调用，也不是执行。本注记不重跑复核里的 21 项核对。

REV9 JSON 的 8091 字节与 `80A76D83CE91B012608F784712F76B329F37AA7B93A5A3073C5DDE3122165C09` 与 REV9 说明所记一致，也与 PR #13 所记一致。REV9 说明本次重新散列是 9220 字节，`AB7D4233FBDF41A362BFD0360AC9BCB82C7C45D280BB55FECB801ABD0C18D159`。这次重新散列不把 REV9 接受为正式合同或来源准入。当前 `HEAD` 在写入本注记之前是 `9cfc1e8b4ed4b6494c330e6c8950856ed9bf2c70`。

点名一个 SHA 只固定文本身份。本注记不把下列任何 SHA 接受为正式合同、Manifest 或来源准入。

## 2. 已经在 main 上的两份来源

清点说明与 JSON 本次重新散列。字节与 REV4、REV5 所记身份一致。不接受，不准入。

| 文件 | 字节 | SHA-256 | 本注记后的状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_ORDERED_SOURCE_LOCATOR_INVENTORY_REV1_CANDIDATE.md` | 15858 | `8072CE39E665990DEA6EFCC0BC57E04BEB1FC9744E8387EB92060BBD65B1C9E5` | 已引用，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_B02_ORDERED_SOURCE_LOCATOR_INVENTORY_REV1_CANDIDATE.json` | 70228 | `86C610B77CAD18A169EDBE18F792A6B69B6BE4E98B327B50B49E012F14D357E7` | 已引用，未准入 |

独立静态复核说明与 JSON 本次重新散列。字节与 REV5 所记身份一致。复核结论仍是所见。`Signed` 与 `Accepted` 均为 false。准入状态是 `NOT_ADMITTED`。通过表示代码有读集依据，不表示政策通过，也不表示来源准入。本注记不重跑那 21 项核对，也不把复核接受为来源准入。

| 文件 | 字节 | SHA-256 | 本注记后的状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA03_AND_ORDERED_INVENTORY_REV1_CANDIDATES_INDEPENDENT_STATIC_REVIEW.md` | 11092 | `3723F4A36E3EF9761AEE094A49D579DFAC22D317E2870FAB702B1D02A7FA51AC` | 所见已引用，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_FA03_AND_ORDERED_INVENTORY_REV1_CANDIDATES_INDEPENDENT_STATIC_REVIEW.json` | 18456 | `48AB6F18FEEB43FD15EF342B5E5516655EB8EE619261AABAF367D227027FB6A1` | 所见已引用，未准入 |

本注记只重述这三条政策。清点里的其余政策不在本注记里重写，也不修复。复核所记行数保持：`AP-020` 17，`AP-021` 2，`AP-022` 30。形成记录里的 `Reordered`、`ItemsInvented`、`DuplicatesRemoved` 均为 false。本注记不重排、不去重、不补行。

## 3. AP-020

选择器是 `manifest_identity.fixture_catalog`。政策路径是 `input_contract.fixtures`。模式是 `ORDERED`。读集里没有这份 ArtifactRef。实际序列定位保持 null。`UniqueLocatorEstablished` 为 false。十七行仍是 `CANDIDATE_LOCATOR` / `NOT_ADMITTED`。本注记不准入其中任何一行。

清点已经写下：十五个 Fixture 是各自独立的对象，点名范围是 `C03-TA-V-001` 至 `C03-TA-V-015`。每个文件只有一个 `scenario_id`，且与文件名相同。文件内没有 15 项数组。唯一的数组是空的 `expected_permitted_write_set`，不作为序列。这十五行不拼成目录。另有两行在 `$.fixture_identities`。它是 JSON 对象，不是数组。两份绑定里的对象相同。键顺序没有被采用为 ORDERED 序列。相同只是清点已经记下的只读所见。这十五个 `scenario_id` 没有缺项、乱序或重复。该外观不是通过，也不是准入。

BLOCK 恰好三条，均未修复：

| 代码 | 清点与复核已经写下的含义 |
| --- | --- |
| `FIXTURE_CATALOG_ARTIFACT_ABSENT` | 没有 `fixture_catalog` 制品。十五个文件没有被拼成目录序列。两份绑定都没有 `fixture_catalog` |
| `FIXTURE_FILES_ARE_SEPARATE_OBJECTS` | 每个 Fixture 是一个对象。`scenario_id` 与文件名相同。唯一数组是空的 `expected_permitted_write_set`。文件名相符不是目录序列 |
| `FIXTURE_IDENTITIES_IS_A_MAP` | `fixture_identities` 在两份绑定里都是 JSON 对象。键是这十五个路径，值等于文件 SHA-256。键顺序不是 ORDERED 序列。两份对象相同也不构成唯一的已准入目录 |

复核条目 `IR-13` 记下的就是这三条未修复代码。本注记不重跑 `IR-13`，也不给出修复。

## 4. AP-021

选择器是 `input_contract.binding`。政策路径是 `input_contract.scenarios`。模式是 `ORDERED`。实际序列定位保持 null。`UniqueLocatorEstablished` 为 false。两行候选的位置都是 `$.scenarios`。身份字段是 `scenario_id`。状态都是 `CANDIDATE_LOCATOR` / `NOT_ADMITTED`。本注记不准入这两行，也不挑选其中一份。

| 路径 | 字段偏移 | 计数 | 文内状态 | 本注记后的状态 |
| --- | --- | --- | --- | --- |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | 24523 | 15 | `MATERIALIZED_NOT_REVIEWED_NOT_ADMITTED` | `CANDIDATE_LOCATOR` / `NOT_ADMITTED` |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json` | 40336 | 15 | `MATERIALIZED_NOT_FORMALLY_REVIEWED_NOT_ACCEPTED_NOT_ADMITTED` | `CANDIDATE_LOCATOR` / `NOT_ADMITTED` |

两个数组的所见顺序都是 `C03-TA-V-001` 至 `C03-TA-V-015` 各一次。外观相符不是通过，也不是准入。两个数组不合并，也不挑选其中一份。

另有一条处置 `OUT_OF_ARRAY_OCCURRENCE_NOT_MERGED`，状态是 `RECORDED_NOT_INSERTED`，不是 BLOCK。它对应 V2 比较规则 `CR-003-EXACT-IDENTITY-MISMATCH-TO-FIXTURE` 上的 `C03-TA-V-003`。该值不在 `$.scenarios` 里。本注记没有把它插入数组。

BLOCK 恰好两条，均未修复：

| 代码 | 清点与复核已经写下的含义 |
| --- | --- |
| `LOCATOR_NOT_UNIQUE` | 两份未准入文件各有一个 `$.scenarios` 数组。字段偏移是 24523 与 40336。两个数组没有合并，也没有挑选 |
| `SOURCE_NOT_ADMITTED` | 文内状态分别是 `MATERIALIZED_NOT_REVIEWED_NOT_ADMITTED` 与 `MATERIALIZED_NOT_FORMALLY_REVIEWED_NOT_ACCEPTED_NOT_ADMITTED`。外观相符不是通过，也不是准入 |

复核条目 `IR-14` 记下的就是这两条未修复代码。本注记不重跑 `IR-14`，也不给出修复。

## 5. AP-022

政策路径是 `input_contract.scenarios[].variants`，身份键是 `variant_id`。两份文件里 `variant_id` 出现次数是 0。键 `variants` 出现次数是 0。所见字段是 `stimulus_variants`。观察到的身份字段是 `stimulus_binding_id`。字段没有改名。不把 `stimulus_binding_id` 或 `design_variant_id` 写成 `variant_id`。

实际序列定位保持 null。`UniqueLocatorEstablished` 为 false。每一场景在两份未准入文件里各有一行。三十行都是 `CANDIDATE_LOCATOR` / `NOT_ADMITTED`。位置是 `$.scenarios[n].stimulus_variants`。原绑定共 25 项，V2 共 28 项。本注记不准入其中任何一行。

十四个场景的 `stimulus_binding_id` 顺序外观相同，仍然是两行。外观相符不是通过，也不是准入，也不并成一条已准入序列。`C03-TA-V-002` 保留两条顺序：原绑定 2 项，V2 候选 5 项。两条都保留。不删除 `SB-002-UNREACHABLE-AUTHORITY-COMPARISON`。不把 V2 的五项补进原绑定。不把原绑定的两项改成 V2。本注记不合并这两条顺序，也不挑选其中一条。

BLOCK 恰好五条，均未修复：

| 代码 | 清点与复核已经写下的含义 |
| --- | --- |
| `POLICY_IDENTITY_FIELD_ABSENT` | 两份文件里 `variant_id` 出现 0 次。`stimulus_binding_id` 与 `design_variant_id` 没有被拿来替代它 |
| `OBSERVED_FIELD_NAME_DIFFERS` | 所见字段是 `stimulus_variants`。政策路径写的是 `variants`。键 `variants` 出现 0 次。字段没有改名 |
| `LOCATOR_NOT_UNIQUE` | 三十行分属两份未准入文件。十四个场景外观相同，仍然是两行 |
| `SOURCE_NOT_ADMITTED` | 两份绑定都不是已准入的 `input_contract.binding` |
| `CANDIDATE_SEQUENCES_DIFFER` | `C03-TA-V-002` 保留两条顺序：原绑定 2 项，V2 候选 5 项。两份名单都没有被改 |

复核条目 `IR-15` 记下的就是这五条未修复代码。`IR-16` 记下的行数仍是 30，且没有重排、没有发明项、没有去重。本注记不重跑这两项，也不给出修复。

## 6. 本注记故意不做的事

- 不修复 `AP-020`、`AP-021`、`AP-022` 的任何 BLOCK，也不修复 `NO_RUNTIME_ROOT_LOCATOR`。
- 不合并候选序列，不挑选其中一份，不把外观相符写成通过或准入。
- 不准入任何定位。三条政策的实际序列定位保持 null。`UniqueLocatorEstablished` 保持 false。
- 不生成 Manifest，不授权正式运行。
- 不调用 `identity_gate`，不执行 Fixture，不运行场景运行器，不执行捕获代码。
- 不读取 `ENVIRONMENT_MANIFEST.md`，不读取历史 Windows 虚拟环境，不读取工具缓存。
- 不选中 FA-05 的任何一个选项。`KEEP_REV1_RECORD`、`FUTURE_STATIC_IDENTITY_NOTE_ONLY`、`NOT_AVAILABLE_UNDER_PATH_B` 的 `Selected` 与 `Opened` 都保持 false。
- 不处置任何 FA-06 行。`DSP004-FA-06` 仍是 `未建立充分前提`。
- 三个实际侧仍为 null / `UNBOUND`：`SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。
- 七个 `DSP_004_CAPTURE_RESULT_*` 仍是 `NOT_SELECTED` / `NOT_ADMITTED`。
- 两个 REV3 SHA `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` 未接受为正式 B-02 合同。
- 不为来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 新增第二份设计复核文件。
- 不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。
- 不改商业 P0。

七个仍未选中的捕获候选是：

- `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_CONTRACT_CANDIDATE_REV1.py`
- `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_FIXED_BOOTSTRAP_CANDIDATE_REV1.py`
- `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV1.py`
- `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV2.py`
- `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV3.py`
- `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_OUTER_SUPERVISOR_CANDIDATE_REV1.cs`
- `validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_OUTER_SUPERVISOR_CANDIDATE_REV2.cs`

## 7. 剩余筹备缺口的次序

这一节只给仍留着的筹备缺口排次序。它不打开任何进一步的交付物，不修复任何 BLOCK，不选中 FA-05 的任何一个选项，也不处置任何 FA-06 行。本注记已经记下这三条政策的未修复 BLOCK。已准入唯一序列仍未建立。

1. `DSP004-FA-06` 的保留仍未接受。登记和独立复核都未接受。最近的资产决定是哪些 LIMITED 可以保留。本注记不写处置文件，也不处置任何一行。
2. `AP-006` 与 `AP-009` 仍是 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`。缺口注记已经写下，准入状态是 `NOT_ADMITTED`。BLOCK 代码仍是 `NO_RUNTIME_ROOT_LOCATOR`，且未修复。实际定位仍是 null。本注记不打开定位交付物。
3. `DSP004-FA-05` 的选项表已经写下，准入状态是 `NOT_ADMITTED`。三个选项都没有被选中，也都没有被打开。本注记不打开进一步的 FA-05 交付物。
4. 本 BLOCK 注记已经写下，准入状态是 `NOT_ADMITTED`。`AP-020`、`AP-021`、`AP-022` 的 BLOCK 代码仍未修复。实际序列定位仍是 null。候选行仍是 `CANDIDATE_LOCATOR` / `NOT_ADMITTED`。本注记不打开修复交付物。
5. Manifest、正式运行、`DSP004-FA-08` 和 DSP-004 关闭仍无授权，排在最后。

## 8. 本记录的效力

```text
BLOCK NOTE RECORDED — CODES UNREPAIRED — NOT ADMITTED

AP-020：17 行 CANDIDATE_LOCATOR / NOT_ADMITTED
BLOCK：FIXTURE_CATALOG_ARTIFACT_ABSENT / FIXTURE_FILES_ARE_SEPARATE_OBJECTS / FIXTURE_IDENTITIES_IS_A_MAP
AP-021：2 行 CANDIDATE_LOCATOR / NOT_ADMITTED
BLOCK：LOCATOR_NOT_UNIQUE / SOURCE_NOT_ADMITTED
AP-022：30 行 CANDIDATE_LOCATOR / NOT_ADMITTED
BLOCK：POLICY_IDENTITY_FIELD_ABSENT / OBSERVED_FIELD_NAME_DIFFERS / LOCATOR_NOT_UNIQUE / SOURCE_NOT_ADMITTED / CANDIDATE_SEQUENCES_DIFFER
实际序列定位：null / null / null
UniqueLocatorEstablished：false
序列合并或挑选：未进行
外观相符：不是通过，也不是准入
Signed / Accepted：false / false
准入：NOT_ADMITTED
DSP004-FA-06：未建立充分前提
DSP004-FA-05：未完成，选项未选中
DSP004-FA-03：MISSING_BINDING_AND_ACTUAL_ENTRY
DSP004-FA-04：未完成
B-01：OPEN
B-02：OPEN
DSP-004：OPEN / HOLD
```

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`DSP004-FA-04` 仍未完成。`DSP004-FA-05` 仍未完成。`DSP004-FA-06` 仍是 `未建立充分前提`。

本注记不接受 `AB7D4233FBDF41A362BFD0360AC9BCB82C7C45D280BB55FECB801ABD0C18D159`，也不接受 `80A76D83CE91B012608F784712F76B329F37AA7B93A5A3073C5DDE3122165C09`。本注记不接受 `8072CE39E665990DEA6EFCC0BC57E04BEB1FC9744E8387EB92060BBD65B1C9E5` 与 `86C610B77CAD18A169EDBE18F792A6B69B6BE4E98B327B50B49E012F14D357E7`。本注记也不接受 `3723F4A36E3EF9761AEE094A49D579DFAC22D317E2870FAB702B1D02A7FA51AC` 与 `48AB6F18FEEB43FD15EF342B5E5516655EB8EE619261AABAF367D227027FB6A1`。这些 SHA 都不是正式合同。
