# DSP-004 路径 B 筹备增量 REV17

本增量只记录路径 B 下的下一项筹备事实：Project Owner 张纯熙的一批与路径 B 一致的决定已经写下。OD-01、OD-02、OD-03、OD-13 选中 `RETAIN`。OD-04 以 `DEFER_WITHOUT_EVIDENCE` 明确留在没有新证据的状态。OD-06 选中 `LEAVE_UNREPAIRED`。OD-07、OD-08、OD-10、OD-11、OD-12 选中 `REFUSE`。OD-09 选中 `DO_NOT_AUTHORIZE`。OD-15 的四个动作都是 Selected false，立场是 `UNAUTHORIZED` / `DO_NOT_AUTHORIZE`。OD-05 仍是 `REFUSE_LOCATOR`。OD-14 仍是 `KEEP_REV1_RECORD`。`Decided` 是 true。`Opened` 是 false。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。它不接受资产，不准入来源，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本批授权是：2026-10-30，批量完成后续项目进度，减少人为干预。只记录与路径 B 一致的拒绝、保留、保持未修复和不授权。不发明资产。不关闭 DSP-004。本批停在资产墙前。

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV16.md` |
| 前一增量说明 | `217CA6A36DB3EED5518DA99209B958EBB291B5058BC9750AFAA65F23BF386B3C`（13470 字节） |
| 前一增量 JSON | `EFB6C33952C36B700CAE294CC61DD9A6D66D870162F43D7A6DC4D015E04CD570`（24280 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV17.json` |
| 本增量 JSON SHA-256 | `EA33B5D5962EA929560C391D6AFCB3299FAD5A3E9C017D48E9E0C1882678E3E5` |
| 本增量 JSON 字节 | 11789 |

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。REV1 至 REV16 已经记下的筹备事实保持原样。本增量不改它们。REV1 登记文件没有被改写。REV2 与 REV3 叠层没有被改写。

## 1. 新增筹备事实

新增筹备事实的名称是 `PATH_B_CONSISTENT_OWNER_DECISIONS_BATCH_REV17_RECORDED_NOT_ADMITTED`。决定批次是候选。它记载所有者的选择，准入仍是 `NOT_ADMITTED`。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_CONSISTENT_OWNER_DECISIONS_BATCH_REV17.md` | 14550 | `481CAF0A5683CDA608AD5FB26499C92BAAD72F72F8C33E25D6A227F547BD36C3` |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_CONSISTENT_OWNER_DECISIONS_BATCH_REV17.json` | 78109 | `0049114F55C4636E631FA62E4C09A277D53DB0B274C74516E81A3B829EA1D67C` |

伴随的加性状态叠层不改写 REV1、REV2 或 REV3。它的筹备事实是 `OWNER_ASSET_DECISION_STATUS_OVERLAY_REV4_NOT_ADMITTED`。

| 文件 | 字节 | SHA-256 | 状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OWNER_ASSET_DECISION_REGISTER_REV4_STATUS_OVERLAY_CANDIDATE.md` | 8435 | `D8D418D18DF5017757B25323865AF0AABCA8E1AD34BE2A21EA14CE58E2863189` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV4_STATUS_OVERLAY_CANDIDATE.json` | 19974 | `802F8882A0674C0A6356E7F1DDB24D70F8D665B71653B996CBE1A7F42A8F3651` | 已绑定，未准入 |

| 决定 | 选中项 | Selected | Decided | Opened |
| --- | --- | --- | --- | --- |
| `OD-01` | `RETAIN` | true | true | false |
| `OD-02` | `RETAIN` | true | true | false |
| `OD-03` | `RETAIN` | true | true | false |
| `OD-04` | `DEFER_WITHOUT_EVIDENCE` | true | true | false |
| `OD-05` | `REFUSE_LOCATOR` | true | true | false |
| `OD-06` | `LEAVE_UNREPAIRED` | true | true | false |
| `OD-07` | `REFUSE` | true | true | false |
| `OD-08` | `REFUSE` | true | true | false |
| `OD-09` | `DO_NOT_AUTHORIZE` | true | true | false |
| `OD-10` | `REFUSE` | true | true | false |
| `OD-11` | `REFUSE` | true | true | false |
| `OD-12` | `REFUSE` | true | true | false |
| `OD-13` | `RETAIN` | true | true | false |
| `OD-14` | `KEEP_REV1_RECORD` | true | true | false |
| `OD-15` | （四个动作都未选中） | false | true | false |

OD-15 的 `AUTHORIZE_MANIFEST`、`AUTHORIZE_FORMAL_RUN`、`COMPLETE_FA08`、`CLOSE_DSP004` 都是 Selected false。立场是 `UNAUTHORIZED` / `DO_NOT_AUTHORIZE`。`Signed` 与 `Accepted` 是 false。准入是 `NOT_ADMITTED`。

决定批次重新散列 REV16、OD-05、OD-14、REV1、REV2、REV3，以及已经点名的来源根、两个 REV3 文件和四个 Harness 文件。相符不是接受。59 条先前身份路径与磁盘相符。

## 2. 记下决定之后仍留着的状态

这一节只记下仍留着的状态。本增量不打开下一项修复、供给或 Manifest。

1. `DSP004-FA-06` 仍是 `未建立充分前提`。OD-01、OD-02、OD-03 已记下 `RETAIN`，`DISPOSE` 是 false。OD-13 已记下 `RETAIN`，`ELIMINATE` 是 false。登记仍未准入。
2. `AP-006` 与 `AP-009` 的 OD-05 仍是 `REFUSE_LOCATOR`。没有运行根路径、启动序列或导入查询顺序。OD-03 的保留只把这个拒绝当作上下文。
3. OD-04 已明确留在 `OWNER_HELD_OPEN_NO_CLOSED_OPTIONS`。路径 B 没有供给导入闭包、两侧调用身份、防替换或 T0 / PE / OS 证据。
4. `DSP004-FA-05` 的 OD-14 仍是 `KEEP_REV1_RECORD`。未来静态身份注记未写下。FA-05 仍未完成。
5. `AP-020`、`AP-021`、`AP-022` 的 BLOCK 保持未修复。实际序列定位仍是 null，且未被准入。
6. 三个实际侧仍是 `UNBOUND`。读取实际引用的调用未被授权。七个捕获候选仍是 `NOT_SELECTED` / `NOT_ADMITTED`。
7. 两个 REV3 SHA、此前候选 SHA、来源与根候选 SHA 和任何 Harness SHA 都没有被接受。
8. Manifest、正式运行、`DSP004-FA-08` 和 DSP-004 关闭仍无授权。OD-15 没有选中其中任何一项。

## 3. 本增量故意不做的事

- 不准入任何来源，不把任何固定 SHA 接受为正式合同、Manifest 或来源准入。
- 不改写 REV1 登记。那份文件的 15 行仍都未决定。
- 不改写 REV2 或 REV3 叠层。当前 15 行的状态写在 REV4 叠层。
- 不改写 OD-05 与 OD-14。
- 不把 `RETAIN` 或 `REFUSE` 写成对资产 SHA 的接受。
- 不供给 OD-04 所缺的证据。
- 不提供运行根定位，不发明启动序列，不发明导入查询顺序。
- 不修复 BLOCK，不处置 FA-06 行，不绑定实际侧，不授权调用。
- 不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，不关闭 DSP-004。
- 不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。
- 不执行捕获代码、`identity_gate`、Fixture、场景运行器或受测模块。
- 不改商业 P0。

## 4. 仍须以后的资产级动作才改变的状态

路径 B 没有代替下列边界。本增量把所有者的拒绝、保留、保持未修复和不授权记下。`Signed` 与 `Accepted` 仍是 false。准入仍是 `NOT_ADMITTED`。

- `OD-01` 已记下 `RETAIN`。`DISPOSE` 未选中。35 行未处置，登记未准入。
- `OD-02` 已记下 `RETAIN`。`DISPOSE` 未选中。16 行未处置。
- `OD-03` 已记下 `RETAIN`。`DISPOSE` 未选中。十行未处置。运行根仍未提供。
- `OD-04` 已明确不补新证据。无已关闭选项表。未准入，未供给。
- `OD-05` 仍是 `REFUSE_LOCATOR`。本增量未改写该决定。
- `OD-06` 已记下 `LEAVE_UNREPAIRED`。BLOCK 未修复。
- `OD-07` 已记下 `REFUSE`。实际序列定位未准入。
- `OD-08` 已记下 `REFUSE`。三个实际侧仍是 `UNBOUND`。
- `OD-09` 已记下 `DO_NOT_AUTHORIZE`。没有获准调用。
- `OD-10` 已记下 `REFUSE`。两个 REV3 SHA 不是正式 B-02 合同。
- `OD-11` 已记下 `REFUSE`。此前候选 SHA 与来源根 SHA 未接受。
- `OD-12` 已记下 `REFUSE`。Harness SHA 未接受。
- `OD-13` 已记下 `RETAIN`。四项 LIMITED 未消除。
- `OD-14` 仍是 `KEEP_REV1_RECORD`。FA-05 未完成。
- `OD-15` 四个动作都未选中。Manifest、正式运行、FA-08 与关闭 DSP-004 仍是 `UNAUTHORIZED`。

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。没有真实案件、个人信息、凭据或供应商调用。
