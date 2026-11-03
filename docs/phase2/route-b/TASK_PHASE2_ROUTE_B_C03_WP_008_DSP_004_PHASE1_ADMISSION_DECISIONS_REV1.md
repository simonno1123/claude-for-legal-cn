# DSP-004 阶段 1 准入决定 REV1

所有者张纯熙对阶段 1 作出了四项决定，**准入了阶段 1 的验证环境**。准入的只是验证环境，不是 OD-04 证据，不是正式运行，也不关闭 DSP-004。DSP-004 保持 `OPEN / HOLD`。

| 项目 | 值 |
| --- | --- |
| 机器记录 | `validation/route_b_c03/wp_008/DSP_004_PHASE1_ADMISSION_DECISIONS_REV1.json` |
| 机器记录 SHA-256 | `0989FCEFD6A59FD6C2376BDE54882A142C111631C7A18086DEA311B81D154664` |
| 机器记录字节 | 2712 |
| 依据 | 第四版结果 `validation/route_b_c03/wp_008/DSP_004_OD04A_V4_RESULT.json`（`9F5813AD6DA40B6B2B3F8D6B35985A1C4C77403F81114D962EB39FCE7CE3CAE0`） |
| 方式 | 所有者在记录人的提问中选择选项，选项文字由记录人起草 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 1. 四项决定

| 编号 | 问题 | 所有者的选择 |
| --- | --- | --- |
| P1-PYVER | V3.2 写的是 3.12.13，实际验证的运行时是 3.12.10 | 以 3.12.10 为准。V3.2 中的版本一行由本决定取代，V3.2 本身的字节不改 |
| P1-RESIDUALS | KnownDLLs、`Users` 组的读取执行权限、本机上的所有者管理员账户 | 作为已知局限接受 |
| P1-EXTREVIEW | 准入前是否需要外部审查 | 暂不需要；记录中如实注明所有审查都来自同一模型家族 |
| P1-ADMIT | 是否准入阶段 1 的验证环境 | 准入 |

## 2. 准入的范围

准入的是验证环境：这台验证机、`dsp004val` 账户、进程创建审计、已绑定的运行时（`C:\Program Files\DSP004Runtime` 下的 CPython 3.12.10），以及第三版监督程序和它的约束清单，具体以 REV30 至 REV36 的记录为准。

附带条件：
- 适用 P1-RESIDUALS 所列的已知局限；
- 没有外部审查；
- 按本机策略，`dsp004val` 的密码约在 2026-12-13 到期；
- 安全日志是 20 MB 的循环日志，以后的运行要在账户历史被覆盖之前完成收集，除非所有者另作决定。

不包括：OD-04 证据（状态不变）、任何正式运行、Harness、输入、比较映射、Manifest，以及 DSP-004 的关闭。

DSP-004 保持 `OPEN / HOLD`。OD-04 保持 `OD04_A_DRY_RUN_OBSERVATION_NOT_EVIDENCE`。B-01、B-02 保持 `OPEN`。
