# DSP-004 OD-14 FA-05 选项决定记录 REV1

本记录只记下 Project Owner 张纯熙对 OD-14 的选择。选中的是 `KEEP_REV1_RECORD`。`FUTURE_STATIC_IDENTITY_NOTE_ONLY` 与 `NOT_AVAILABLE_UNDER_PATH_B` 未选中。`Decided` 是 true。`Opened` 是 false。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。选项表没有被改写，也没有被准入。REV12 独立静态复核没有被接受，也没有被准入。未来静态身份注记没有写下。`DSP004-FA-05` 仍未完成。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

所有者本步选择是：在三个未选的 FA-05 选项中选择 `KEEP_REV1_RECORD`。这个选择把 REV1 已经记下的 FA-05 事实保留为被选中的那一项。它不打开未来静态身份注记，不把 FA-05 写成完成，不准入选项表，不准入 REV12 复核，也不接受任何 Harness SHA、REV3 SHA 或来源根 SHA。

新增筹备事实的名称是 `OD14_FA05_KEEP_REV1_RECORD_RECORDED_NOT_ADMITTED`。

形成时 `HEAD` 是 `8160eee3e42b8a44305545705eef95a89f99477b`（PR #19）。本决定记录在这个 `HEAD` 上还不存在。REV1 登记文件没有被改写。OD-05 的 `REFUSE_LOCATOR` 记录没有被改写。

| 项目 | 值 |
| --- | --- |
| 机器记录 | `validation/route_b_c03/wp_008/DSP_004_OD14_FA05_OPTION_DECISION_REV1.json` |
| 机器记录 SHA-256 | `E382AE8D8AD6F6033A7526C79559BE641AC0A2AED51D3500523A76A0C0E7982A` |
| 机器记录字节 | 17592 |
| 决定 | `OD-14` |
| 事项 | 在三个未选的 FA-05 选项中选择一项 |
| 选中 | `KEEP_REV1_RECORD` Selected true |
| 未选中 | `FUTURE_STATIC_IDENTITY_NOTE_ONLY` Selected false；`NOT_AVAILABLE_UNDER_PATH_B` Selected false |
| 行 Selected / Decided / Opened | true / true / false |
| Signed / Accepted | false / false |
| 准入 | `NOT_ADMITTED` |
| 未来静态身份注记 | 未写下 |
| FA-05 | 仍未完成 |
| 机器核对 | 12 项通过 |
| 通过的含义 | 字段与已记录筹备状态相符 |

行 `Selected` 为 true，只因为 `KEEP_REV1_RECORD` 是被选中的那一项。`Opened` 沿用 REV1 登记的字段含义：true 表示随后打开了注记或其他 FA-05 交付物。保留 REV1 记录没有打开其中任何一项，所以 `Opened` 保持 false。

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

本次使用本机 Python 标准库只做字节散列和 JSON 结构读取。散列只固定文本身份。散列不是调用，也不是执行。未导入受测模块，未调用 `identity_gate`，未执行 Fixture，未运行场景运行器，未执行捕获代码。未读取 `ENVIRONMENT_MANIFEST.md`，未读取历史 Windows 虚拟环境，未读取工具缓存。未生成 Manifest。

## 1. 记下的选择

| 字段 | 值 |
| --- | --- |
| Owner | 张纯熙 |
| DecisionId | `OD-14` |
| Subject | `FA05_OPTION_SELECTION` |
| `KEEP_REV1_RECORD` | Selected true，Opened false |
| `FUTURE_STATIC_IDENTITY_NOTE_ONLY` | Selected false，Opened false |
| `NOT_AVAILABLE_UNDER_PATH_B` | Selected false，Opened false |
| Selected | true |
| Decided | true |
| Opened | false |
| Signed | false |
| Accepted | false |
| Admission | `NOT_ADMITTED` |
| FutureStaticIdentityNoteWritten | false |
| OptionsSheetAdmitted | false |
| OptionsReviewAdmitted | false |
| FA05Completed | false |

选项表上的三个选项仍全部未选中。那是未改写的选项表快照。所有者后来的选择写在本记录。

## 2. 已重新散列、仍未接受的身份

下表只固定指针文件的文本身份。点名一个 SHA 不构成接受或准入。选项表与 REV12 复核仍是 `NOT_ADMITTED`。OD-05 仍是 `REFUSE_LOCATOR`。本记录不改写这些文件。

| 文件 | 字节 | SHA-256 | 状态 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV15.md` | 12006 | `ECFE6BC3F44E549789342C02125A60111B0D995D1287F0E1EFA700424FEA4943` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV15.json` | 20253 | `E3817F182B51460F7E8C59CF0104A6355A21CA3B8474970EECD3944670590DA9` | 已绑定，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD05_RUNTIME_ROOT_LOCATOR_DECISION_REV1.md` | 9876 | `30CA669C6EFE30EDDEE294CF2CAF2B9C3109E168E211753DDF62229EC3700192` | 已绑定，未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OD05_RUNTIME_ROOT_LOCATOR_DECISION_REV1.json` | 14234 | `96CD4504DF67A06F00968024F5877F685B99FE43B4144BFFA747FAEA054E62B0` | 已绑定，未改写，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OWNER_ASSET_DECISION_REGISTER_REV2_STATUS_OVERLAY_CANDIDATE.md` | 6210 | `A069DE20BEE610B0FF4E7DD3FBC4F02654C3469C0F673DEC1421F75B52870A3A` | 已绑定，未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV2_STATUS_OVERLAY_CANDIDATE.json` | 16111 | `8BFE26CAF66524E43B4D11AE8909ED7F1ADDE13BCF8FA7B1DD852137A89B55CF` | 已绑定，未改写，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OWNER_ASSET_DECISION_REGISTER_REV1_CANDIDATE.md` | 37989 | `0821B18800B4FC9FF008160A80DA6E6D0DAD38273415CF6A62CADF05AD65AB91` | 已绑定，未改写，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_OWNER_ASSET_DECISION_REGISTER_REV1_CANDIDATE.json` | 82247 | `EC5233D541108CF59EF1DF7BCAA3E9E64F9CE61D1B29A05D8F40DC900789CFF3` | 已绑定，未改写，未接受 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA05_OPTIONS_SHEET_REV1_CANDIDATE.md` | 10924 | `6C6F505258E30C1A31033E35C85797969CD387D79357E312830DF17DB785BEC4` | 已引用，未改写，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_FA05_OPTIONS_SHEET_REV1_CANDIDATE.json` | 12147 | `88F4B087169910561F51874E83C4B41A4D7873916136048F1A3DFF30E287CAF8` | 已引用，未改写，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA05_OPTIONS_SHEET_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.md` | 17974 | `7EFB324FAEC1F33EDAF87444FB82C79A1115C4EB0DBE4928F1CA2F6960F6E69A` | 已引用，未接受，未准入 |
| `validation/route_b_c03/wp_008/DSP_004_FA05_OPTIONS_SHEET_REV1_CANDIDATE_INDEPENDENT_STATIC_REVIEW.json` | 35336 | `3BEC8B6BE1173C4A22374F21C3726218F8F16AA7C520C9391D10B1752889755A` | 已引用，未接受，未准入 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV12.md` | 12277 | `E44A36331C3679C04B3923E000077F1AF83329B075AF5D27ECD19DD92D68D063` | 已绑定，未接受 |
| `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV12.json` | 10089 | `1C84529D4746327835622CDCA713F6FC714D992CAC474A8425C322B6EAEDDB17` | 已绑定，未接受 |

REV15 的筹备事实仍是 `OD05_RUNTIME_ROOT_LOCATOR_REFUSED_RECORDED_NOT_ADMITTED`。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。`RuntimeRootAdmitted` 仍是 false。REV15 JSON 的 20253 字节与 `E3817F182B51460F7E8C59CF0104A6355A21CA3B8474970EECD3944670590DA9` 与 REV15 说明所记一致，也与 PR #19 所在的 `HEAD` `8160eee3e42b8a44305545705eef95a89f99477b` 上的文件一致。OD-05 决定记录的选中项仍是 `REFUSE_LOCATOR`。`PROVIDE_LOCATOR` 仍未选中。定位路径、启动序列、导入查询顺序仍是 null。`NO_RUNTIME_ROOT_LOCATOR` 仍未修复。

选项表的筹备事实仍是 `FA05_OPTIONS_SHEET_NOT_SELECTED_NOT_ADMITTED`。磁盘上三个选项的 `Selected` 与 `Opened` 仍是 false。REV12 复核的筹备事实仍是 `FA05_OPTIONS_SHEET_INDEPENDENT_STATIC_REVIEW_NOT_ACCEPTED`。`FutureStaticIdentityNoteWritten` 仍是 false。`OptionSelectedByThisReview` 仍是 false。REV12 增量的筹备事实与该复核相同，准入仍是 `NOT_ADMITTED`。

登记 JSON 里 OD-14 的 `Selected`、`Decided`、`Opened` 仍是 false。三个选项在那份文件里的 `Selected` 仍是 false。这是未改写的登记快照。REV2 叠层仍是只记下 OD-05 的那一版，已决定行数仍是 1。本记录不改写它。

## 3. 对 FA-05 与 OD-05 的效力边界

`KEEP_REV1_RECORD` 表示所有者选择保留 REV1 已经记下的 FA-05 事实，作为三个选项里被选中的一项。输入候选在选项表上的准入仍是 `NOT_ADMITTED`。没有 Harness SHA 被接受。本记录不把选项表里点过名的固定 SHA 再抄成接受。

`DSP004-FA-05` 因此仍是未完成。记下选择不等于完成 FA-05。

OD-05 仍是 `REFUSE_LOCATOR`。本记录重新散列该决定，不改它，也不发明运行根。OD-03 仍未决定。十行 `REQUIRES_RUNTIME_ROOT` 的行号仍是 2、5、7、10、12、15、48、55、60、61。这些行未被处置。

OD-01、OD-02、OD-04，以及 OD-06 至 OD-13，和 OD-15，本记录都不作决定。

## 4. 本记录故意不做的事

- 不改写 REV1 所有者资产决定登记。那份文件的 OD-14 仍是未决定。
- 不改写 REV2 状态叠层。那份文件仍只记下 OD-05。
- 不改写 OD-05 决定记录。`REFUSE_LOCATOR` 保持原样。
- 不改写 FA-05 选项表，不准入该选项表。
- 不接受、不准入 REV12 独立静态复核。
- 不写下未来静态身份注记。`FUTURE_STATIC_IDENTITY_NOTE_ONLY` 保持未选中、未打开。
- 不把 `DSP004-FA-05` 写成完成。
- 不准入任何来源，不把任何固定 SHA 接受为正式合同、Manifest 或来源准入。
- 不接受任何 Harness SHA，不接受任何 REV3 SHA，不接受任何来源根 SHA。
- 不提供运行根定位，不写入定位路径，不发明启动序列，不发明导入查询顺序。
- 不修复 `NO_RUNTIME_ROOT_LOCATOR`。不修复 AP-020、AP-021、AP-022 的 BLOCK。
- 不处置任何 FA-06 行。OD-03 保持未决定。
- 不绑定 `SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。
- 不执行捕获代码、`identity_gate`、Fixture、场景运行器或受测模块。
- 不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。
- 不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，不关闭 DSP-004。
- 不把本记录的 SHA 接受为正式合同或来源准入。
- 不改商业 P0。

## 5. 本记录的效力

```text
OD-14 DECISION RECORDED — FINDINGS ONLY

Owner：张纯熙
KEEP_REV1_RECORD：Selected true，Opened false
FUTURE_STATIC_IDENTITY_NOTE_ONLY：Selected false，Opened false
NOT_AVAILABLE_UNDER_PATH_B：Selected false，Opened false
Selected / Decided / Opened：true / true / false
Signed / Accepted：false / false
准入：NOT_ADMITTED
未来静态身份注记：未写下
选项表：未改写，未准入
REV12 复核：未接受，未准入
FA-05：未完成
OD-05：REFUSE_LOCATOR，未改写，运行根未准入
OD-01、OD-02、OD-03、OD-04、OD-06 至 OD-13、OD-15：未决定
REV1 登记：未改写，其 OD-14 仍未决定
DSP004-FA-06：未建立充分前提
DSP004-FA-03：MISSING_BINDING_AND_ACTUAL_ENTRY
DSP004-FA-04：未完成
DSP004-FA-08：未完成
B-01：OPEN
B-02：OPEN
DSP-004：OPEN / HOLD
```

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

12 项机器核对全部通过。通过表示所引身份与当前磁盘相符，并且本记录的字段就是上面的筹备状态。通过不表示来源准入，不表示 SHA 接受，不表示选项表准入，不表示 FA-05 完成，也不表示 DSP-004 关闭。

本记录不接受 `E382AE8D8AD6F6033A7526C79559BE641AC0A2AED51D3500523A76A0C0E7982A`。该 SHA 只固定机器记录的文本身份。
