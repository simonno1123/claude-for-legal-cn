# DSP-004 预检运行 v2 结果

按所有者授权，记录人安装了正式运行 v2，并以 `dsp004val` 身份做了第二次预检运行。**这不是正式结果。** DSP-004 保持 `OPEN / HOLD`。

**安装**：30 个文件全部与绑定一致。

**运行**：结果 `PASS_FORMAL_V2`，运行环境为 CPython 3.12.10。
- 锁定 743 个文件，散列全部一致。
- 目录树中有 721 个文件、71 个目录，与审查预计的完全相同。
- 监督程序 29/29 项检查全部通过。
- Harness 28 个变体全部通过：12 个完整符合 Fixture，5 个部分符合，11 个按设计不映射；运行时拦截没有触发。

**导入闭包**：共 96 个模块，本地模块 24 个，**不含任何禁止模块**。第一次预检中出现的 `urllib` 已经不在了。

**系统审计对照**：
- v2 监督程序在历史中只启动过 1 次，进程号与记录一致；Harness 退出码为 0。
- 安全日志记录编号从 65637 到 74348，连续，共 8712 条。
- 没有失败的登录，也没有清空日志的记录。

| 机器记录 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_PREFLIGHT_V2_RESULT.json` | 3890 | `E3172D2836891142FFDFEC73FD39CEFDFF2499EA0854F1379FB4C1471D1DF2DE` |

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `install_formal_v2_result.json` | 13524 | `543541CBF41AC18ED97F2E2F207701B1EDB36106AE4E0AAC46BFDEF19CFA7B6F` |
| `preflight2_pre_collect_result.json` | 833 | `D3FB5D38C892C9717537BAF7C51315012254AF4DA5F5BAEF85EB42DE0EDE31E0` |
| `preflight2_post_collect_result.json` | 92031 | `4CE5CE062A15950FF1B07F4E74459E068A5E5188AED96A2DCCF0A7718244DB6D` |
| `preflight2_run_record.RAW_REDACTED.json` | 392765 | `52E842271FDA939099BE9CB4B740AD255A3C2D01359081A5CA72329AFE73087F` |
| `preflight2_events_history.RAW_REDACTED.xml` | 148868 | `A690C64866E16E82179EE6BD7F882DC1B08DD04A82929CD9599C3DF02C07EB12` |
| `preflight2_import_closure.json` | 13302 | `7F82B0390DEE2BB2B20A8286A0CAC4AA8F2848AF9DDBBD00BA983FE6C4CB1342` |

DSP-004 保持 `OPEN / HOLD`。
