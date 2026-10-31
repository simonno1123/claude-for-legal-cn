# DSP-004 所有者资产决定状态叠层候选 REV4

本叠层是路径 B 下的加性状态注记。它不改写 REV1 所有者资产决定登记，也不把那份登记接受为资产。它也不改写 REV2 或 REV3 叠层。REV1 仍是 15 行都未决定的快照。REV2 仍是只记下 OD-05 的叠层。REV3 仍是只记下 OD-05 与 OD-14 的叠层。本叠层记下 OD-05、OD-14 和本批其余决定的当前状态。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

叠层筹备事实的名称是 `OWNER_ASSET_DECISION_STATUS_OVERLAY_REV4_NOT_ADMITTED`。它所指向的决定批次筹备事实是 `PATH_B_CONSISTENT_OWNER_DECISIONS_BATCH_REV17_RECORDED_NOT_ADMITTED`。

| 项目 | 值 |
| --- | --- |
| 机器记录 | `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV4_STATUS_OVERLAY_CANDIDATE.json` |
| 机器记录 SHA-256 | `802F8882A0674C0A6356E7F1DDB24D70F8D665B71653B996CBE1A7F42A8F3651` |
| 机器记录字节 | 19974 |
| 决定行 | 15 |
| 已决定 / 未决定 / 已打开 | 15 / 0 / 0 |
| 行 Selected 为 true | 14 |
| OD-15 行 Selected | false |
| Signed / Accepted | false / false |
| 准入 | `NOT_ADMITTED` |
| 机器核对 | 10 项通过 |
| 通过的含义 | 字段与已记录筹备状态相符 |

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

## 1. 不改写的 REV1、REV2、REV3

| 文件 | 字节 | SHA-256 | 状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OWNER_ASSET_DECISION_REGISTER_REV1_CANDIDATE.md` | 37989 | `0821B18800B4FC9FF008160A80DA6E6D0DAD38273415CF6A62CADF05AD65AB91` | 未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV1_CANDIDATE.json` | 82247 | `EC5233D541108CF59EF1DF7BCAA3E9E64F9CE61D1B29A05D8F40DC900789CFF3` | 未改写，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OWNER_ASSET_DECISION_REGISTER_REV2_STATUS_OVERLAY_CANDIDATE.md` | 6210 | `A069DE20BEE610B0FF4E7DD3FBC4F02654C3469C0F673DEC1421F75B52870A3A` | 未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV2_STATUS_OVERLAY_CANDIDATE.json` | 16111 | `8BFE26CAF66524E43B4D11AE8909ED7F1ADDE13BCF8FA7B1DD852137A89B55CF` | 未改写，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OWNER_ASSET_DECISION_REGISTER_REV3_STATUS_OVERLAY_CANDIDATE.md` | 9306 | `972F15B5E1C4BAE478DFD1BD2BAA3271DB5D47C0CDA47ADCA7FF7920F5DC0C4A` | 未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV3_STATUS_OVERLAY_CANDIDATE.json` | 25452 | `F93F3CFD7E7342D301D722D9978734FCF7BFA8B53EB747D525D9881B98C67800` | 未改写，未准入 |

REV1 JSON 里 15 行的 `Selected`、`Decided`、`Opened` 仍是 false。本叠层不把那份快照改成当前状态，也不把它准入。

## 2. 本叠层指向的批次，以及重新散列的 OD-05 与 OD-14

| 文件 | 字节 | SHA-256 | 状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_CONSISTENT_OWNER_DECISIONS_BATCH_REV17.md` | 14550 | `481CAF0A5683CDA608AD5FB26499C92BAAD72F72F8C33E25D6A227F547BD36C3` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_CONSISTENT_OWNER_DECISIONS_BATCH_REV17.json` | 78109 | `0049114F55C4636E631FA62E4C09A277D53DB0B274C74516E81A3B829EA1D67C` | 已绑定，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD05_RUNTIME_ROOT_LOCATOR_DECISION_REV1.md` | 9876 | `30CA669C6EFE30EDDEE294CF2CAF2B9C3109E168E211753DDF62229EC3700192` | 已绑定，未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OD05_RUNTIME_ROOT_LOCATOR_DECISION_REV1.json` | 14234 | `96CD4504DF67A06F00968024F5877F685B99FE43B4144BFFA747FAEA054E62B0` | 已绑定，未改写，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD14_FA05_OPTION_DECISION_REV1.md` | 11599 | `DA0871EBAAE92B48C40043AA9CDAF3387EC447610F9DD7BA6BA4DE5953F756E9` | 已绑定，未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OD14_FA05_OPTION_DECISION_REV1.json` | 17592 | `E382AE8D8AD6F6033A7526C79559BE641AC0A2AED51D3500523A76A0C0E7982A` | 已绑定，未改写，未准入 |

## 3. 十五行的当前状态

每一行的 `Signed` 与 `Accepted` 都是 false。准入都是 `NOT_ADMITTED`。除 OD-15 外，每一行的 `Selected` 是 true，并且只因为该行的选择键被选中。没有任何一行的 `Opened` 是 true。

| 决定 | 事项 | 选中项 | Selected | Decided | Opened | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| `OD-01` | 保留或处置 FA-06 里证据状态为 EVIDENCE_PRESENT_UNACCEPTED 的行 | `RETAIN` | true | true | false | `RETAIN_RECORDED_NOT_ADMITTED` |
| `OD-02` | 保留或处置 FA-06 里证据状态为 EVIDENCE_ABSENT 的行 | `RETAIN` | true | true | false | `RETAIN_RECORDED_NOT_ADMITTED` |
| `OD-03` | 保留或处置 FA-06 里证据状态为 REQUIRES_RUNTIME_ROOT 的行 | `RETAIN` | true | true | false | `RETAIN_RECORDED_NOT_ADMITTED` |
| `OD-04` | 导入闭包、两侧调用身份、检查到使用的防替换，以及 T0 / PE / OS 证据 | `DEFER_WITHOUT_EVIDENCE` | true | true | false | `OWNER_HELD_OPEN_NO_CLOSED_OPTIONS` |
| `OD-05` | 提供或拒绝 AP-006 与 AP-009 的运行根定位 | `REFUSE_LOCATOR` | true | true | false | `REFUSE_LOCATOR_RECORDED_NOT_ADMITTED` |
| `OD-06` | 是否以及如何修复 AP-020、AP-021、AP-022 的 BLOCK | `LEAVE_UNREPAIRED` | true | true | false | `LEAVE_UNREPAIRED_RECORDED_NOT_ADMITTED` |
| `OD-07` | 准入或拒绝 AP-020、AP-021、AP-022 的实际序列定位 | `REFUSE` | true | true | false | `REFUSE_RECORDED_NOT_ADMITTED` |
| `OD-08` | 准入或拒绝三个实际侧及其捕获入口 | `REFUSE` | true | true | false | `REFUSE_RECORDED_NOT_ADMITTED` |
| `OD-09` | 是否另作一次获准调用，以便读取实际引用 | `DO_NOT_AUTHORIZE` | true | true | false | `DO_NOT_AUTHORIZE_RECORDED_NOT_ADMITTED` |
| `OD-10` | 是否把两个 REV3 SHA 接受为正式 B-02 合同 | `REFUSE` | true | true | false | `REFUSE_RECORDED_NOT_ADMITTED` |
| `OD-11` | 是否接受或准入此前候选的固定 SHA | `REFUSE` | true | true | false | `REFUSE_RECORDED_NOT_ADMITTED` |
| `OD-12` | 是否接受任何 Harness SHA | `REFUSE` | true | true | false | `REFUSE_RECORDED_NOT_ADMITTED` |
| `OD-13` | 四项已经点名的 LIMITED 审查项是消除还是继续保留 | `RETAIN` | true | true | false | `RETAIN_RECORDED_NOT_ADMITTED` |
| `OD-14` | 在三个未选的 FA-05 选项中选择一项 | `KEEP_REV1_RECORD` | true | true | false | `KEEP_REV1_RECORD_RECORDED_NOT_ADMITTED` |
| `OD-15` | Manifest、正式运行、FA-08 与关闭 DSP-004 | `（无）` | false | true | false | `UNAUTHORIZED_DO_NOT_AUTHORIZE_RECORDED_NOT_ADMITTED` |

OD-04 的选择键 `DEFER_WITHOUT_EVIDENCE` 不表示已经供给证据。REV1 的选项表仍是空的。OD-15 的四个动作都没有被选中。`CLOSE_DSP004` 的 Selected 是 false。

## 4. 本叠层故意不做的事

- 不改写 REV1 登记，不把 REV1 的 SHA 接受为资产。
- 不改写 REV2 或 REV3。REV4 是加性当前状态。
- 不把本叠层写成准入登记。`Signed` 与 `Accepted` 保持 false。
- 不改写 OD-05，不提供运行根定位。
- 不改写 OD-14，不写下未来静态身份注记，不把 FA-05 写成完成。
- 不修复 BLOCK，不处置 FA-06 行，不绑定实际侧。
- 不接受任何 SHA，不生成 Manifest，不授权正式运行，不完成 FA-08，不关闭 DSP-004。

## 5. 效力

```text
STATUS OVERLAY RECORDED — FINDINGS ONLY

REV1：未改写，未接受
REV2：未改写，未准入
REV3：未改写，未准入
已决定 / 未决定 / 已打开：15 / 0 / 0
OD-15：四个动作 Selected false
CLOSE_DSP004：Selected false
Signed / Accepted：false / false
准入：NOT_ADMITTED
RuntimeRootAdmitted：false
DSP-004：OPEN / HOLD
B-01：OPEN
B-02：OPEN
```

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

10 项机器核对全部通过。通过表示 REV1、REV2、REV3、OD-05、OD-14 与本批记录的身份和字段与当前磁盘相符。通过不表示接受。

本叠层不接受 `802F8882A0674C0A6356E7F1DDB24D70F8D665B71653B996CBE1A7F42A8F3651`。该 SHA 只固定机器记录的文本身份。
