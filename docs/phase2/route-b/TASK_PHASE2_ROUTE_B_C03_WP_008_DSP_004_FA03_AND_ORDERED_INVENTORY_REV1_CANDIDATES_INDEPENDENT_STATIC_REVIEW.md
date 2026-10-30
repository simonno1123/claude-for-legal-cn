# DSP-004 FA-03 与 ORDERED 清点两份候选 — 独立静态复核

本记录是路径 B 筹备增量 REV4 之后的在库只读复核。对象是两份已经在 `main` 上的物理候选：FA-03 捕获入口设计候选 REV1，以及 B-02 ORDERED 序列来源定位清点候选 REV1。复核确认它们的字节，并核对文内结构与 BLOCK 代码是否有读集依据。它不把任一 SHA 接受为正式合同，不准入来源，不完成 `DSP004-FA-03` 或 `DSP004-FA-04`，也不关闭 B-01、B-02 或 DSP-004。

依据仍是已经记入的路径 B 原句：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本步授权原句是：`写下一项筹备文档，不准入、不接受资产、不关 DSP-004.`

## 1. 复核基准

| 项目 | 本记录的事实 |
| --- | --- |
| 复核时 `HEAD` | `c54e0878a0dce044dae660748114132b94d90dd8` |
| FA-03 物化提交 | `531ca6f0476e235b90430fa5fb9ec9523b12e2ef`（PR #7） |
| ORDERED 清点物化提交 | `c54e0878a0dce044dae660748114132b94d90dd8`（PR #8） |
| 前一筹备增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV4.md` |
| 前一增量 JSON | `85001CCA85F01F526E4C8C9E0AD61E38BFCC8A532C933FE5CB14E7D65BDC1951`（3955 字节） |
| 机器可读结果 | `validation/route_b_c03/wp_008/DSP_004_FA03_AND_ORDERED_INVENTORY_REV1_CANDIDATES_INDEPENDENT_STATIC_REVIEW.json` |
| 该结果 SHA-256 | `48AB6F18FEEB43FD15EF342B5E5516655EB8EE619261AABAF367D227027FB6A1` |
| 该结果字节 | 18456 |
| 受测模块导入或执行 | 未进行 |
| `identity_gate` 调用 | 未进行 |
| Fixture 执行或写入 | 未进行 |
| 场景运行器 | 未运行 |
| 商业 P0 | 未执行，未修改 |

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

本次使用本机 Python 标准库只做字节散列和 JSON 结构读取。读集是这两份候选的说明与机器结果，加上清点已经点名的十五个 `C03-TA-V-001` 至 `C03-TA-V-015` Fixture JSON、`SCENARIO_INPUT_BINDING.json`、`SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json`。两个 REV3 文本只重新散列，用来确认身份。未导入 `identity_gate`、合同模块、捕获候选或场景运行器，未执行 Fixture，未写入 Fixture，未编译 C#，未重放业务场景，未生成 Manifest。未读取 `ENVIRONMENT_MANIFEST.md`，未读取历史 Windows 虚拟环境，未读取工具缓存。

这是同仓库内的后续静态复核，不是跨供应商外审，也不是 Project Owner 对这两个候选的接受。结论只是所见。`Signed` 与 `Accepted` 均为 false。准入状态是 `NOT_ADMITTED`。

## 2. 四个物理文件

复核前 REV3、REV4 以及 PR #7、PR #8 记下的身份，与当前 `HEAD` 上的字节一致。物化之后这些文件没有再改。

| 候选 | 路径 | 字节 | SHA-256 |
| --- | --- | --- | --- |
| FA-03 说明 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA03_CAPTURE_ENTRY_DESIGN_CANDIDATE_REV1.md` | 10668 | `479BDD82584A9189EB54D5518D5D5C23C9C478DF39AF68622F345CBCA2F58789` |
| FA-03 JSON | `validation/route_b_c03/wp_008/DSP_004_FA03_CAPTURE_ENTRY_DESIGN_CANDIDATE_REV1.json` | 12081 | `73DCBAB6AC60E79955C8755D820D9377DCEF1D2F32CABB01EA279DA9B81D859A` |
| ORDERED 说明 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_ORDERED_SOURCE_LOCATOR_INVENTORY_REV1_CANDIDATE.md` | 15858 | `8072CE39E665990DEA6EFCC0BC57E04BEB1FC9744E8387EB92060BBD65B1C9E5` |
| ORDERED JSON | `validation/route_b_c03/wp_008/DSP_004_B02_ORDERED_SOURCE_LOCATOR_INVENTORY_REV1_CANDIDATE.json` | 70228 | `86C610B77CAD18A169EDBE18F792A6B69B6BE4E98B327B50B49E012F14D357E7` |

FA-03 两份文件从 `531ca6f0476e235b90430fa5fb9ec9523b12e2ef` 到当前 `HEAD` 的 diff 为空。ORDERED 两份文件的物化提交就是当前 `HEAD`，其后没有新提交。

四份文件均为 UTF-8、无 BOM、无 CR、无行尾空白。说明文件只嵌入自己配套 JSON 的 SHA-256。任一候选都不包含另一候选的 SHA-256。

点名一个 SHA 只固定文本身份。本复核不把这四个 SHA 接受为正式合同、Manifest 或来源准入。

## 3. FA-03 所见

FA-03 候选自己写明：设计文本存在，关卡未完成。本复核看到的仍是这一句。

- `ActualReadRule.BackfillFromExpected` 为 false。`ForbiddenByThisCandidate.BackfillActualFromExpected` 为 true。`SYNTHETIC-PROJECT-001`、`SYNTHETIC-SESSION-001`、`SYNTHETIC-PROVIDER-001` 的 `CopiedToActual` 均为 false。`variant_id`、`attempt_id`、`input_snapshot_sha256`、`authority_record` 均为 null。
- `Signed` 为 false，`Accepted` 为 false，准入状态是 `NOT_ADMITTED`。`CaptureEntryBound` 为 false。
- 七个 `DSP_004_CAPTURE_RESULT_*` 文件仍是 `NOT_SELECTED` / `NOT_ADMITTED`。当前字节与候选所记散列相同。本复核只做字节散列，没有导入，没有挑选。
- `SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER` 的绑定都是 `UNBOUND`。身份、版本、载体、定位、记录引用、捕获入口和观察 SHA 都是 null。
- `DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`completed` 为 false。

## 4. ORDERED BLOCK 代码的读集依据

本复核不重排、不去重、不补行。清点里的行数保持：`AP-006` 0，`AP-009` 0，`AP-020` 17，`AP-021` 2，`AP-022` 30。形成记录里的 `Reordered`、`ItemsInvented`、`DuplicatesRemoved` 均为 false。每一条 BLOCK 都未修复。通过表示代码有读集依据，不表示政策通过，也不表示来源准入。

### 4.1 AP-006 与 AP-009

两条的状态都是 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`。实际定位是 null。候选行数是 0。BLOCK 代码都是 `NO_RUNTIME_ROOT_LOCATOR`，各一条。

两份绑定文件里没有 `startup_contract`、`origin_policy`、`declared_startup_sequence` 或 `lookup_order`。十五个 Fixture 也不是启动序列或搜索序列。本复核没有读取 `ENVIRONMENT_MANIFEST.md`、历史 Windows 虚拟环境或工具缓存，也不用它们补定位。

### 4.2 AP-020

BLOCK 恰好三条，均未修复：

| 代码 | 读集依据 |
| --- | --- |
| `FIXTURE_CATALOG_ARTIFACT_ABSENT` | 两份绑定都没有 `fixture_catalog`。十五个文件没有被拼成目录序列 |
| `FIXTURE_FILES_ARE_SEPARATE_OBJECTS` | 每个 Fixture 是一个对象，`scenario_id` 与文件名相同。唯一数组是空的 `expected_permitted_write_set` |
| `FIXTURE_IDENTITIES_IS_A_MAP` | `fixture_identities` 在两份绑定里都是 JSON 对象。键是这十五个路径，值等于文件 SHA-256，两份对象相同。键顺序没有被采用为 ORDERED 序列 |

十七行仍是 `CANDIDATE_LOCATOR` / `NOT_ADMITTED`。实际序列定位保持 null。

### 4.3 AP-021

BLOCK 恰好两条，均未修复：

| 代码 | 读集依据 |
| --- | --- |
| `LOCATOR_NOT_UNIQUE` | 两个 `$.scenarios` 都是 `C03-TA-V-001` 至 `C03-TA-V-015` 各一次。字段偏移是 24523 与 40336。两个数组没有合并 |
| `SOURCE_NOT_ADMITTED` | 文内状态分别是 `MATERIALIZED_NOT_REVIEWED_NOT_ADMITTED` 与 `MATERIALIZED_NOT_FORMALLY_REVIEWED_NOT_ACCEPTED_NOT_ADMITTED` |

另有一条处置 `OUT_OF_ARRAY_OCCURRENCE_NOT_MERGED`，状态是 `RECORDED_NOT_INSERTED`，不是 BLOCK。它对应 V2 比较规则 `CR-003-EXACT-IDENTITY-MISMATCH-TO-FIXTURE` 上的 `C03-TA-V-003`。该值不在 `$.scenarios` 里。本复核没有把它插入数组。

### 4.4 AP-022

BLOCK 恰好五条，均未修复：

| 代码 | 读集依据 |
| --- | --- |
| `POLICY_IDENTITY_FIELD_ABSENT` | 两份文件里 `variant_id` 出现 0 次 |
| `OBSERVED_FIELD_NAME_DIFFERS` | 所见字段是 `stimulus_variants`。键 `variants` 出现 0 次。字段没有改名 |
| `LOCATOR_NOT_UNIQUE` | 三十行分属两份未准入文件。十四个场景外观相同，仍然是两行 |
| `SOURCE_NOT_ADMITTED` | 两份绑定都不是已准入的 `input_contract.binding` |
| `CANDIDATE_SEQUENCES_DIFFER` | `C03-TA-V-002` 保留两条顺序：原绑定 2 项，V2 候选 5 项。其余十四个场景的 `stimulus_binding_id` 顺序外观相同 |

原绑定共 25 项，V2 共 28 项。各文件内部跨场景没有重复的 `stimulus_binding_id`。本复核没有删除 `SB-002-UNREACHABLE-AUTHORITY-COMPARISON`，也没有把 V2 的五项补进原绑定。

## 5. 两个 REV3 SHA 仍不是正式合同

数组政策 REV3 仍是 16317 字节，`39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123`。类型合同 REV3 仍是 29240 字节，`AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F`。本次重新散列只核对身份。两者都不是正式 B-02 合同。

## 6. 仍然缺少的事项

候选自己的未绑定清单，加上本复核不能代替的接受，仍然包括：

- FA-03 捕获入口的准入
- 三个实际侧的来源身份、版本、载体、定位、产生者职责、授权，以及已经绑定的捕获入口
- 另一次获准调用；只有那次调用发生时才允许读取实际引用
- `variant_id`、`attempt_id`、`input_snapshot_sha256` 和授权记录
- 这两份候选的固定 SHA 接受
- 对两个 REV3 SHA 的固定 SHA 接受
- `AP-006` 与 `AP-009` 在运行根确立之后的实际定位
- `AP-020`、`AP-021`、`AP-022` 的已准入唯一序列，以及上述 BLOCK 的修复
- Manifest、正式运行和 DSP-004 关闭

`DSP004-FA-03` 因此仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`DSP004-FA-04` 仍是未完成。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

## 7. 本记录的效力

```text
INDEPENDENT STATIC REVIEW RECORDED — FINDINGS ONLY

两个候选的准入：NOT_ADMITTED
Signed / Accepted：false / false
DSP004-FA-03：MISSING_BINDING_AND_ACTUAL_ENTRY
DSP004-FA-04：未完成
B-01：OPEN
B-02：OPEN
DSP004-FA-08：未完成
DSP-004：OPEN / HOLD
```

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

本记录不接受 `479BDD82584A9189EB54D5518D5D5C23C9C478DF39AF68622F345CBCA2F58789`，不接受 `73DCBAB6AC60E79955C8755D820D9377DCEF1D2F32CABB01EA279DA9B81D859A`，不接受 `8072CE39E665990DEA6EFCC0BC57E04BEB1FC9744E8387EB92060BBD65B1C9E5`，也不接受 `86C610B77CAD18A169EDBE18F792A6B69B6BE4E98B327B50B49E012F14D357E7`。本记录也不接受 `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123`。这些 SHA 都不是正式合同。

本记录不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`，不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，也不关闭 DSP-004。不为来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 新增第二份设计复核文件。商业 P0 保持原样。没有真实案件、个人信息、凭据或供应商调用。

21 项机器核对全部通过。通过表示身份与 REV3、REV4 所记一致，FA-03 关卡仍未绑定，并且每条 ORDERED BLOCK 代码都有读集依据。通过不表示来源准入，不表示 SHA 接受，也不表示 B-02 关闭。
