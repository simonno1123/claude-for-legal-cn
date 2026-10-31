# DSP-004 所有者资产决定状态叠层候选 REV3

本叠层是路径 B 下的加性状态注记。它不改写 REV1 所有者资产决定登记，也不把那份登记接受为资产。它也不改写 REV2 叠层。REV1 仍是 15 行都未决定的快照。REV2 仍是只记下 OD-05 的叠层。本叠层记下后来的 OD-05 选择与后来的 OD-14 选择，并保持其余 13 行未决定。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

叠层筹备事实的名称是 `OWNER_ASSET_DECISION_STATUS_OVERLAY_REV3_NOT_ADMITTED`。它所指向的新决定记录筹备事实是 `OD14_FA05_KEEP_REV1_RECORD_RECORDED_NOT_ADMITTED`。OD-05 的筹备事实仍是 `OD05_RUNTIME_ROOT_LOCATOR_REFUSED_RECORDED_NOT_ADMITTED`。

| 项目 | 值 |
| --- | --- |
| 机器记录 | `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV3_STATUS_OVERLAY_CANDIDATE.json` |
| 机器记录 SHA-256 | `F93F3CFD7E7342D301D722D9978734FCF7BFA8B53EB747D525D9881B98C67800` |
| 机器记录字节 | 25452 |
| 决定行 | 15 |
| 已决定 / 未决定 / 已打开 | 2 / 13 / 0 |
| 已决定的两行 | `OD-05` `REFUSE_LOCATOR`；`OD-14` `KEEP_REV1_RECORD` |
| Signed / Accepted | false / false |
| 准入 | `NOT_ADMITTED` |
| 机器核对 | 10 项通过 |
| 通过的含义 | 字段与已记录筹备状态相符 |

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

## 1. 不改写的 REV1 与 REV2

| 文件 | 字节 | SHA-256 | 状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OWNER_ASSET_DECISION_REGISTER_REV1_CANDIDATE.md` | 37989 | `0821B18800B4FC9FF008160A80DA6E6D0DAD38273415CF6A62CADF05AD65AB91` | 未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV1_CANDIDATE.json` | 82247 | `EC5233D541108CF59EF1DF7BCAA3E9E64F9CE61D1B29A05D8F40DC900789CFF3` | 未改写，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OWNER_ASSET_DECISION_REGISTER_REV2_STATUS_OVERLAY_CANDIDATE.md` | 6210 | `A069DE20BEE610B0FF4E7DD3FBC4F02654C3469C0F673DEC1421F75B52870A3A` | 未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV2_STATUS_OVERLAY_CANDIDATE.json` | 16111 | `8BFE26CAF66524E43B4D11AE8909ED7F1ADDE13BCF8FA7B1DD852137A89B55CF` | 未改写，未准入 |

REV1 JSON 里 OD-05 与 OD-14 的 `Selected`、`Decided`、`Opened` 仍是 false。REV2 仍是已决定 1 行、未决定 14 行。本叠层不把这两份快照改成当前状态，也不把它们准入。

## 2. 重新散列的 OD-05，以及本叠层指向的 OD-14

| 文件 | 字节 | SHA-256 | 状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD05_RUNTIME_ROOT_LOCATOR_DECISION_REV1.md` | 9876 | `30CA669C6EFE30EDDEE294CF2CAF2B9C3109E168E211753DDF62229EC3700192` | 已绑定，未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OD05_RUNTIME_ROOT_LOCATOR_DECISION_REV1.json` | 14234 | `96CD4504DF67A06F00968024F5877F685B99FE43B4144BFFA747FAEA054E62B0` | 已绑定，未改写，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD14_FA05_OPTION_DECISION_REV1.md` | 11599 | `DA0871EBAAE92B48C40043AA9CDAF3387EC447610F9DD7BA6BA4DE5953F756E9` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OD14_FA05_OPTION_DECISION_REV1.json` | 17592 | `E382AE8D8AD6F6033A7526C79559BE641AC0A2AED51D3500523A76A0C0E7982A` | 已绑定，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV15.md` | 12006 | `ECFE6BC3F44E549789342C02125A60111B0D995D1287F0E1EFA700424FEA4943` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV15.json` | 20253 | `E3817F182B51460F7E8C59CF0104A6355A21CA3B8474970EECD3944670590DA9` | 已绑定，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA05_OPTIONS_SHEET_REV1_CANDIDATE.md` | 10924 | `6C6F505258E30C1A31033E35C85797969CD387D79357E312830DF17DB785BEC4` | 已引用，未改写，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_FA05_OPTIONS_SHEET_REV1_CANDIDATE.json` | 12147 | `88F4B087169910561F51874E83C4B41A4D7873916136048F1A3DFF30E287CAF8` | 已引用，未改写，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA05_OPTIONS_SHEET_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.md` | 17974 | `7EFB324FAEC1F33EDAF87444FB82C79A1115C4EB0DBE4928F1CA2F6960F6E69A` | 已引用，未接受，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_FA05_OPTIONS_SHEET_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.json` | 35336 | `3BEC8B6BE1173C4A22374F21C3726218F8F16AA7C520C9391D10B1752889755A` | 已引用，未接受，未准入 |

OD-05 决定记录里 `REFUSE_LOCATOR` 的 `Selected` 是 true，`PROVIDE_LOCATOR` 的 `Selected` 是 false，`Decided` 是 true，`Opened` 是 false。运行根未准入。本叠层不改这个决定。

OD-14 决定记录里 `KEEP_REV1_RECORD` 的 `Selected` 是 true，另外两个选项的 `Selected` 是 false，`Decided` 是 true，`Opened` 是 false，`Signed` 与 `Accepted` 是 false，准入是 `NOT_ADMITTED`。未来静态身份注记未写下。FA-05 未完成。选项表与 REV12 复核未准入。

## 3. 十五行的当前状态

每一行的 `Signed` 与 `Accepted` 都是 false。准入都是 `NOT_ADMITTED`。只有 OD-05 与 OD-14 的 `Selected` 与 `Decided` 是 true。没有任何一行的 `Opened` 是 true。

| 决定 | 事项 | Selected | Decided | Opened | 状态 |
| --- | --- | --- | --- | --- | --- |
| `OD-01` | 保留或处置 FA-06 里证据状态为 EVIDENCE_PRESENT_UNACCEPTED 的行 | false | false | false | 仍未决定 |
| `OD-02` | 保留或处置 FA-06 里证据状态为 EVIDENCE_ABSENT 的行 | false | false | false | 仍未决定 |
| `OD-03` | 保留或处置 FA-06 里证据状态为 REQUIRES_RUNTIME_ROOT 的行 | false | false | false | 仍未决定 |
| `OD-04` | 导入闭包、两侧调用身份、检查到使用的防替换，以及 T0 / PE / OS 证据 | false | false | false | 仍未决定 |
| `OD-05` | 提供或拒绝 AP-006 与 AP-009 的运行根定位 | true | true | false | `REFUSE_LOCATOR` 已记下，未改写 |
| `OD-06` | 是否以及如何修复 AP-020、AP-021、AP-022 的 BLOCK | false | false | false | 仍未决定 |
| `OD-07` | 准入或拒绝 AP-020、AP-021、AP-022 的实际序列定位 | false | false | false | 仍未决定 |
| `OD-08` | 准入或拒绝三个实际侧及其捕获入口 | false | false | false | 仍未决定 |
| `OD-09` | 是否另作一次获准调用，以便读取实际引用 | false | false | false | 仍未决定 |
| `OD-10` | 是否把两个 REV3 SHA 接受为正式 B-02 合同 | false | false | false | 仍未决定 |
| `OD-11` | 是否接受或准入此前候选的固定 SHA | false | false | false | 仍未决定 |
| `OD-12` | 是否接受任何 Harness SHA | false | false | false | 仍未决定 |
| `OD-13` | 四项已经点名的 LIMITED 审查项是消除还是继续保留 | false | false | false | 仍未决定 |
| `OD-14` | 在三个未选的 FA-05 选项中选择一项 | true | true | false | `KEEP_REV1_RECORD` 已记下，未准入 |
| `OD-15` | Manifest、正式运行、FA-08 与关闭 DSP-004 | false | false | false | 仍未决定 |

OD-03 仍未决定。十行 `REQUIRES_RUNTIME_ROOT` 的行号仍是 2、5、7、10、12、15、48、55、60、61。OD-05 的拒绝只是这十行的上下文。这十行未被保留为决定，也未被处置。

## 4. 本叠层故意不做的事

- 不改写 REV1 登记，不把 REV1 的 SHA 接受为资产。
- 不改写 REV2 叠层。REV3 是加性当前状态，不是对 REV2 的覆盖写入。
- 不把本叠层写成准入登记。`Signed` 与 `Accepted` 保持 false。
- 不改写 OD-05。不提供运行根定位，不写入路径、启动序列或导入查询顺序。
- 不修复 `NO_RUNTIME_ROOT_LOCATOR`，也不修复 AP-020、AP-021、AP-022 的 BLOCK。
- 不写下未来静态身份注记，不把 FA-05 写成完成。
- 不准入选项表，不接受 REV12 复核。
- 不处置 FA-06 行，不绑定实际侧。
- 不接受任何 SHA，不生成 Manifest，不授权正式运行，不完成 FA-08，不关闭 DSP-004。

## 5. 效力

```text
STATUS OVERLAY RECORDED — FINDINGS ONLY

REV1：未改写，未接受
REV2：未改写，未准入
OD-05：REFUSE_LOCATOR Selected true；PROVIDE_LOCATOR Selected false；未改写
OD-14：KEEP_REV1_RECORD Selected true；另外两项 Selected false
Decided / Opened：true / false
其余 13 行：未决定
Signed / Accepted：false / false
准入：NOT_ADMITTED
未来静态身份注记：未写下
选项表：未准入
REV12 复核：未接受
FA-05：未完成
RuntimeRootAdmitted：false
DSP-004：OPEN / HOLD
B-01：OPEN
B-02：OPEN
```

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

10 项机器核对全部通过。通过表示 REV1、REV2、OD-05、OD-14、选项表与 REV12 复核的身份和字段与当前磁盘相符。通过不表示接受。

本叠层不接受 `F93F3CFD7E7342D301D722D9978734FCF7BFA8B53EB747D525D9881B98C67800`。该 SHA 只固定机器记录的文本身份。
