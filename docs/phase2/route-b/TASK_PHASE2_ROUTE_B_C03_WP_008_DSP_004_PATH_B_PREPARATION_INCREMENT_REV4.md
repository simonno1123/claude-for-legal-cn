# DSP-004 路径 B 筹备增量 REV4

本增量只记录路径 B 下的下一项筹备事实：一份 ORDERED 序列来源定位清点候选。它不接受资产，不准入来源，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本步授权原句是：`写下一项筹备文档，不准入、不接受资产、不关 DSP-004.`

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV3.md` |
| 前一增量 JSON | `D6D94630A3B99A04306DC9DF07A524E372CE97C9E1119F45C49B1E1290319F7A`（2493 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV4.json` |
| 本增量 JSON SHA-256 | `85001CCA85F01F526E4C8C9E0AD61E38BFCC8A532C933FE5CB14E7D65BDC1951` |
| 本增量 JSON 字节 | 3955 |

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。REV1 已经记下的 FA-02、FA-03 大纲与 FA-05 事实保持原样。REV2 已经记下的两份 REV3 文档复核保持原样。REV3 已经记下的 FA-03 捕获入口设计候选保持原样。本增量不改它们。

## 1. 新增筹备事实：ORDERED 序列来源定位清点候选

这是候选定位清点，不是来源准入，不是正式合同，也不是 Manifest 输入。`Signed` 与 `Accepted` 均为 false。准入状态是 `NOT_ADMITTED`。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_ORDERED_SOURCE_LOCATOR_INVENTORY_REV1_CANDIDATE.md` | 15858 | `8072CE39E665990DEA6EFCC0BC57E04BEB1FC9744E8387EB92060BBD65B1C9E5` |
| `validation/route_b_c03/wp_008/DSP_004_B02_ORDERED_SOURCE_LOCATOR_INVENTORY_REV1_CANDIDATE.json` | 70228 | `86C610B77CAD18A169EDBE18F792A6B69B6BE4E98B327B50B49E012F14D357E7` |

清点只做字节散列和 JSON 结构读取。读集是十五个 `C03-TA-V-001` 至 `C03-TA-V-015` Fixture、`SCENARIO_INPUT_BINDING.json`、`SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json`（`A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430`，107849 字节），以及数组政策 REV3（`39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123`，16317 字节）。没有导入，没有执行，没有写入 Fixture。

清点写明的边界是：

- `AP-006` 与 `AP-009` 是 `NOT_LOCATABLE_WITHOUT_RUNTIME_ROOT`。实际定位是 null。没有从 `ENVIRONMENT_MANIFEST.md`、历史 Windows 虚拟环境或工具缓存猜测。
- `AP-020`、`AP-021`、`AP-022` 只列出候选定位行。每一行是 `CANDIDATE_LOCATOR` / `NOT_ADMITTED`。实际序列定位保持 null。
- `AP-020` 没有 `manifest_identity.fixture_catalog`。十五个 Fixture 文件没有被拼成目录。`fixture_identities` 是 JSON 对象，键顺序不采用为 ORDERED 序列。
- `AP-021` 的两个 `$.scenarios` 数组外观都是 `C03-TA-V-001` 至 `C03-TA-V-015` 各一次。外观相符不是通过。两份文件都未准入，定位不唯一。V2 在比较规则里另有一个 `C03-TA-V-003`，没有插入场景数组。
- `AP-022` 的所见字段是 `stimulus_variants`，不是 `variants`。`variant_id` 不在。`C03-TA-V-002` 的两条候选序列分别是 2 项和 5 项，都保留。没有重排，没有补项，没有删除重复项。

三个实际侧仍为 null / `UNBOUND`：`SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。

REV1 点名的七个既有捕获候选仍是 `NOT_SELECTED` / `NOT_ADMITTED`。本增量不装载它们，也不挑选它们。

`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`DSP004-FA-04` 仍未完成。B-02 保持 `OPEN`。

## 2. 本增量故意不做的事

- 不准入任何来源，不把任何固定 SHA 接受为正式合同、Manifest 或来源准入。
- 不把两个 REV3 SHA `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` 接受为正式 B-02 合同。
- 不完成 `DSP004-FA-03`，也不完成 `DSP004-FA-04`。B-02 保持 `OPEN`。
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
- 五条 ORDERED 路径的已准入实际来源、唯一定位和逐场景登记
- `AP-006` 与 `AP-009` 在运行根确立之后的实际定位
- `AP-020` 的 `fixture_catalog`，以及 `AP-021`、`AP-022` 在两份未准入文件之间的唯一选择
- Manifest、正式运行和 DSP-004 关闭
