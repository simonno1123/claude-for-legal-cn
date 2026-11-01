# DSP-004 路径 B 筹备增量 REV23

本增量记录两项筹备事实：

1. Project Owner 张纯熙再次改签路径 B（签署记录 REV3），授权按 `OD04-A` 推进三步；
2. 三步已完成，监督下的 T0 演练结果为 `PASS_T0_DRY_RUN`。

结果是候选，不是证据准入。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。不生成 Manifest，不正式运行，不关闭 DSP-004。

现行范围原句：`授权按 OD04-A 推进三步：①由所有者以管理员身份运行记录人提供的脚本，建立专用运行时目录并设置访问控制；②由记录人编写外层监督程序，审查后绑定其 SHA；③用监督程序做一次只跑清单探测的 T0 演练。不接受资产、不生成 Manifest、不正式运行、不关闭 DSP-004。`

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV22.md` |
| 前一增量说明 | `9C3296334159F6BE08C81913EF4CC8370D4E1476A1C9233DFB09B7316B851372`（2487 字节） |
| 前一增量 JSON | `A3B5721CA683D8F333AB84A47DC7553AAF652A59ED1550F47E17A912C181AC39`（5763 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV23.json` |
| 本增量 JSON SHA-256 | `D82B8D579F65CDD6A9E56D7A63C3438ACF9365B6E906B308F07DDA884CC8C746` |
| 本增量 JSON 字节 | 7073 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 1. 新增筹备事实

| 事实 | 文件 | 字节 | SHA-256 |
| --- | --- | --- | --- |
| `PATH_B_SCOPE_RESIGNED_REV3_OD04A_THREE_STEPS` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_SCOPE_SIGNING_RECORD_REV3.md` | 2007 | `CEAE5606AFF5CA5D945AB746B8AE73CE7B969BA05F436785A0ACFECEBC0FA20A` |
| 同上 | `validation/route_b_c03/wp_008/DSP_004_PATH_B_SCOPE_SIGNING_RECORD_REV3.json` | 2188 | `51FC43CED82C5DB8C3A52F6139D714745E8B96A8FC753C25DBE682D1495BB077` |
| `OD04A_T0_DRY_RUN_REV1_PASSED_NOT_ADMITTED` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD04A_T0_DRY_RUN_REV1_RESULT.md` | 4842 | `AE7A83D413C7049EBC96855E10E8BDB0A4A6BEADA7AE84BD16D2A66403676779` |
| 同上 | `validation/route_b_c03/wp_008/DSP_004_OD04A_T0_DRY_RUN_REV1_RESULT.json` | 8331 | `69377802A25CD249FD2FEA337A37FBF84D84D1F5801641780A0F0BF6502CD79E` |

## 2. 本机环境的改动

所有者按第 ①步，以管理员身份建立了 `C:\Program Files\DSP004Runtime`，并设置为只有管理员能写。这是本系列记录里第一次改动所有者的电脑。它没有改动、也没有删除原来按用户安装的 Python。

## 3. OD-04 现状

六个组成部分（T0、两侧调用身份、检查到使用的防替换、导入闭包、PE、OS）都已经有一次演练得到的候选观察。要把它们准入为证据，还差两步：

1. 一次独立审查（目前只有记录人自审）；
2. 所有者的准入决定。

剩余限制写在演练结果记录第 4 节。

## 4. 本增量故意不做的事

- 不准入运行根或任何证据，不接受任何 SHA。
- 不改 OD-05（AP-006 / AP-009 的运行根定位）及其他 OD 决定。
- 不生成 Manifest，不正式运行，没有运行 Harness 或受测代码，不完成 FA-08，不关闭 DSP-004。

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。没有真实案件、个人信息、凭据或供应商调用。
