# DSP-004 路径 B 筹备增量 REV24

本增量记录 OD04-A T0 演练的独立静态复核结论，并更正 REV23 的说法。

复核结论：不能把这次演练准入为 OD-04 证据，最多只能算非证据性的工程演练观察。OD-04 的状态因此记为 `OD04_A_DRY_RUN_OBSERVATION_NOT_EVIDENCE`。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。DSP-004 保持 `OPEN / HOLD`。

现行范围原句：`授权按 OD04-A 推进三步：①由所有者以管理员身份运行记录人提供的脚本，建立专用运行时目录并设置访问控制；②由记录人编写外层监督程序，审查后绑定其 SHA；③用监督程序做一次只跑清单探测的 T0 演练。不接受资产、不生成 Manifest、不正式运行、不关闭 DSP-004。`

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV23.md` |
| 前一增量说明 | `DE59CFEFFE9398598F05C92D8CCD4604C0508FE6BF9F74BAA4B5B44730DF9D95`（3399 字节） |
| 前一增量 JSON | `D82B8D579F65CDD6A9E56D7A63C3438ACF9365B6E906B308F07DDA884CC8C746`（7073 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV24.json` |
| 本增量 JSON SHA-256 | `A6CD76B4491D764242D583F1F8EDA0CE2A94E7F8057669D293552163CB05ED87` |
| 本增量 JSON 字节 | 6927 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 1. 新增筹备事实

新增筹备事实的名称是 `OD04A_T0_DRY_RUN_INDEPENDENT_REVIEW_RECORDED_NOT_ADMITTED`。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD04A_T0_DRY_RUN_REV1_INDEPENDENT_STATIC_REVIEW.md` | 6053 | `569A0058BE4571ED87EFD6C17DD795E37A6E37DE86B7FA70E1FFA0C593CF162A` |
| `validation/route_b_c03/wp_008/DSP_004_OD04A_T0_DRY_RUN_REV1_INDEPENDENT_STATIC_REVIEW.json` | 23712 | `40355F11BAFE72317F73E654DA4CE3960C7ED08C9D2DC05BE712FF279AAE0F62` |

复核共有 17 项发现：阻止准入 1 项，需写明限制 10 项，次要 3 项，备注 3 项。复核者原文完整保存在机器记录的 `ReviewerReportVerbatim` 字段。

## 2. 对 REV23 的更正

REV23 的字节保持不变，更正写在这里：

1. REV23 说 T0 和两侧调用身份"已在演练中观察到"，说过头了。实际观察到的，只是一个未经准入、运行前未绑定的启动器所报告的时间点和子进程身份（IR-01、IR-15）。
2. REV23 的剩余限制漏列了这些：同一用户的进程可篡改、令牌和用户账户控制状态未记录、环境变量和 OpenSSL 输入未控制、部分加载器未检查、KnownDLLs、运行时只是"首次信任"、"实际运行版本"缺乏机器证据、SHA 在运行之后才绑定、脱敏副本是重新序列化的（IR-03 至 IR-11）。
3. REV23 说第 ②步"审查后绑定 SHA"。实际上监督程序的 SHA 在演练之后才首次提交（02:16Z，T0 是 02:13Z），审查也只是记录人自审（IR-10）。这是记录人的流程失误。
4. REV23 的 `*.SANITIZED.json` 是重新序列化的副本，无法与原始 SHA 对应。本增量另外提交了按字节替换生成的脱敏原始记录（`*.RAW_REDACTED.json`），替换规则写在复核机器记录里，所有者可以用本机原件逐字节复现（IR-11）。

## 3. 要成为证据还需要什么（复核者给出的条件）

1. 启动器在运行前绑定，放在管理员保护的位置，并核验宿主程序；
2. 监督程序从进程外部枚举子进程加载的模块；
3. 清空并记录环境变量，并与 PF-004 一致；
4. 记录令牌和用户账户控制的状态；
5. 运行后再扫描一次目录树，并逐个文件记录访问控制；
6. 原始记录可核对，并再经独立复核。

这些都需要所有者另行授权。本增量不打开其中任何一项。

## 4. 本增量故意不做的事

- 不准入任何证据，不接受任何 SHA，不改 REV23 的字节。
- 不再运行任何程序，不改动环境。
- 不生成 Manifest，不正式运行，不关闭 DSP-004。

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。没有真实案件、个人信息、凭据或供应商调用。
