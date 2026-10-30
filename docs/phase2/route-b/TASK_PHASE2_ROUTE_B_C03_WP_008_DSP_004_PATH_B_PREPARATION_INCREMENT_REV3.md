# DSP-004 路径 B 筹备增量 REV3

本增量只记录路径 B 下的下一项筹备事实：一份 FA-03 捕获入口设计候选。它不接受资产，不准入来源，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本步授权原句是：`写 FA-03 捕获设计候选，不准入、不执行、不从预期回填.`

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV2.md` |
| 前一增量 JSON | `BFAFB7A0867156E164EACD8FEB76DF9655F658B6F33FF42A892675BB6356EBED`（2578 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV3.json` |
| 本增量 JSON SHA-256 | `D6D94630A3B99A04306DC9DF07A524E372CE97C9E1119F45C49B1E1290319F7A` |
| 本增量 JSON 字节 | 2493 |

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。REV1 已经记下的 FA-02、FA-03 大纲与 FA-05 事实保持原样。REV2 已经记下的两份 REV3 文档复核保持原样。本增量不改它们。

## 1. 新增筹备事实：FA-03 捕获入口设计候选

这是设计候选，不是捕获入口，不是源码，也不是可导入模块。`Signed` 与 `Accepted` 均为 false。准入状态是 `NOT_ADMITTED`。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA03_CAPTURE_ENTRY_DESIGN_CANDIDATE_REV1.md` | 10668 | `479BDD82584A9189EB54D5518D5D5C23C9C478DF39AF68622F345CBCA2F58789` |
| `validation/route_b_c03/wp_008/DSP_004_FA03_CAPTURE_ENTRY_DESIGN_CANDIDATE_REV1.json` | 12081 | `73DCBAB6AC60E79955C8755D820D9377DCEF1D2F32CABB01EA279DA9B81D859A` |

候选写明的设计边界是：

- 产生者与捕获入口分开。预期维护者不能改写已经冻结的预期。产生者、捕获入口和待审调用也不能改写冻结预期。
- 实际引用只在另一次获准的未来调用发生时，由捕获入口读取。保留原生类型和来源。未观察到的实际值保持空缺。
- `audit_correlation_id` 相等、刺激帧、`NOT_SELECTED` 和禁止调用结果都不是实际侧身份。
- 本候选不调用 `identity_gate`，不写 Fixture 结果，不预填 `variant_id`、`attempt_id` 或 `input_snapshot_sha256`。

三个实际侧仍为 null / `UNBOUND`：`SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。没有把 `SYNTHETIC-PROJECT-001`、`SYNTHETIC-SESSION-001` 或 `SYNTHETIC-PROVIDER-001` 写入实际侧。

REV1 点名的七个既有捕获候选仍是 `NOT_SELECTED` / `NOT_ADMITTED`。本增量不装载它们，也不挑选它们。

`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。设计文本存在，关卡未完成。

## 2. 本增量故意不做的事

- 不准入任何捕获入口，不执行捕获代码、`identity_gate`、Fixture 或受测模块。
- 不从预期回填实际侧。
- 不把任何固定 SHA 接受为正式合同、Manifest 或来源准入。
- 不把两个 REV3 SHA `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` 接受为正式 B-02 合同。
- 不完成 `DSP004-FA-03`，也不完成 `DSP004-FA-04`。B-02 保持 `OPEN`。
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
- 五条 ORDERED 路径的实际来源、唯一定位和逐场景登记
- Manifest、正式运行和 DSP-004 关闭
