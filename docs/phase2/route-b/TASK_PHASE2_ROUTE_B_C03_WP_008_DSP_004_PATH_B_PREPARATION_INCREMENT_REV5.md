# DSP-004 路径 B 筹备增量 REV5

本增量只记录路径 B 下的下一项筹备事实：FA-03 捕获入口设计候选 REV1 与 ORDERED 序列来源定位清点候选 REV1 的在库独立静态复核。它不接受资产，不准入来源，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本步授权原句是：`写下一项筹备文档，不准入、不接受资产、不关 DSP-004.`

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV4.md` |
| 前一增量 JSON | `85001CCA85F01F526E4C8C9E0AD61E38BFCC8A532C933FE5CB14E7D65BDC1951`（3955 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV5.json` |
| 本增量 JSON SHA-256 | `32527B68DAA54A5763473AF4488DA19653778B5A85BE41CF585FE7C4BFC902ED` |
| 本增量 JSON 字节 | 4678 |

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。REV1 已经记下的 FA-02、FA-03 大纲与 FA-05 事实保持原样。REV2 已经记下的两份 REV3 文档复核保持原样。REV3 已经记下的 FA-03 捕获入口设计候选保持原样。REV4 已经记下的 ORDERED 序列来源定位清点候选保持原样。本增量不改它们。

## 1. 新增筹备事实：两份候选的在库复核

REV3 写入了 FA-03 设计候选，REV4 写入了 ORDERED 定位清点。两份都还没有独立复核。该复核现已写入仓库。复核结论是身份、结构和 BLOCK 依据的所见，`Signed` 与 `Accepted` 均为 false。准入状态是 `NOT_ADMITTED`。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA03_AND_ORDERED_INVENTORY_REV1_CANDIDATES_INDEPENDENT_STATIC_REVIEW.md` | 11092 | `3723F4A36E3EF9761AEE094A49D579DFAC22D317E2870FAB702B1D02A7FA51AC` |
| `validation/route_b_c03/wp_008/DSP_004_FA03_AND_ORDERED_INVENTORY_REV1_CANDIDATES_INDEPENDENT_STATIC_REVIEW.json` | 18456 | `48AB6F18FEEB43FD15EF342B5E5516655EB8EE619261AABAF367D227027FB6A1` |

被复核的物理候选仍是：

| 候选 | 字节 | SHA-256 | 本增量后的状态 |
| --- | --- | --- | --- |
| FA-03 说明 | 10668 | `479BDD82584A9189EB54D5518D5D5C23C9C478DF39AF68622F345CBCA2F58789` | 已复核，未准入 |
| FA-03 JSON | 12081 | `73DCBAB6AC60E79955C8755D820D9377DCEF1D2F32CABB01EA279DA9B81D859A` | 已复核，未准入 |
| ORDERED 说明 | 15858 | `8072CE39E665990DEA6EFCC0BC57E04BEB1FC9744E8387EB92060BBD65B1C9E5` | 已复核，未准入 |
| ORDERED JSON | 70228 | `86C610B77CAD18A169EDBE18F792A6B69B6BE4E98B327B50B49E012F14D357E7` | 已复核，未准入 |

这些字节与 REV3、REV4 以及 PR #7、PR #8 所记身份一致。当前 `HEAD` 是 `c54e0878a0dce044dae660748114132b94d90dd8`。

复核所见：

- FA-03 没有从预期回填。准入状态是 `NOT_ADMITTED`。七个 `DSP_004_CAPTURE_RESULT_*` 仍是 `NOT_SELECTED` / `NOT_ADMITTED`。`SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER` 仍是 null / `UNBOUND`。`Signed` 与 `Accepted` 均为 false。关卡仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。
- `AP-006` 与 `AP-009` 仍是 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`。BLOCK 代码是 `NO_RUNTIME_ROOT_LOCATOR`。
- `AP-020` 的三条 BLOCK 是 `FIXTURE_CATALOG_ARTIFACT_ABSENT`、`FIXTURE_FILES_ARE_SEPARATE_OBJECTS`、`FIXTURE_IDENTITIES_IS_A_MAP`。
- `AP-021` 的两条 BLOCK 是 `LOCATOR_NOT_UNIQUE`、`SOURCE_NOT_ADMITTED`。
- `AP-022` 的五条 BLOCK 是 `POLICY_IDENTITY_FIELD_ABSENT`、`OBSERVED_FIELD_NAME_DIFFERS`、`LOCATOR_NOT_UNIQUE`、`SOURCE_NOT_ADMITTED`、`CANDIDATE_SEQUENCES_DIFFER`。分叉仍在 `C03-TA-V-002`，两条顺序都保留。
- 复核没有重排、没有去重、没有补行。没有调用 `identity_gate`，没有执行 Fixture 或场景运行器，没有读取 Manifest、历史虚拟环境或工具缓存。

`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`DSP004-FA-04` 仍未完成。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

## 2. 本增量故意不做的事

- 不准入任何来源，不把任何固定 SHA 接受为正式合同、Manifest 或来源准入。
- 不把两个 REV3 SHA `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` 接受为正式 B-02 合同。
- 不完成 `DSP004-FA-03`，也不完成 `DSP004-FA-04`。B-01 与 B-02 保持 `OPEN`。
- 不执行捕获代码、`identity_gate`、Fixture、场景运行器或受测模块。
- 不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。
- 不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，不关闭 DSP-004。
- 不为来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 新增第二份设计复核文件。
- 不改商业 P0。

## 3. 仍须以后的资产级决定

路径 B 没有代替下列决定：

- 三个实际侧的来源身份、版本、载体、定位、产生者职责、授权和已经绑定的捕获入口
- 另一次获准调用；只有那次调用发生时才允许读取实际引用
- `variant_id`、`attempt_id`、`input_snapshot_sha256` 和授权记录
- 是否对两个 REV3 SHA 作固定 SHA 接受
- 是否对 FA-03 与 ORDERED 清点的固定 SHA 作接受或准入
- 五条 ORDERED 路径的已准入实际来源、唯一定位和逐场景登记
- `AP-006` 与 `AP-009` 在运行根确立之后的实际定位
- `AP-020` 的 `fixture_catalog`，以及 `AP-021`、`AP-022` 在两份未准入文件之间的唯一选择
- Manifest、正式运行和 DSP-004 关闭
