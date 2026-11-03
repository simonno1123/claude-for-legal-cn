# DSP-004 预检运行 v1 结果

按所有者授权，记录人在已准入的环境中，用已绑定的正式运行 v1 资产，以 `dsp004val` 身份做了一次预检运行。目的是观察 Harness 在 Windows 上实际导入了哪些模块，供生成 Manifest 使用。**这不是正式结果。** DSP-004 保持 `OPEN / HOLD`。

| 机器记录 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_PREFLIGHT_V1_RESULT.json` | 4081 | `9251F51F4CFB41672A2EAD387058B34801CECA9330535FE8FE12BA7D72EEAD1A` |

## 1. 结果

**安装**：30 个文件全部与绑定一致，完成于 2026-11-03T17:21Z。

**运行**：结果为 `PASS_FORMAL_V1`。
- 运行环境：CPython 3.12.10（`dsp004val`，中等权限）。
- 监督程序锁定 713 个文件，散列全部一致。
- 监督程序的 29/29 项检查全部通过。
- Harness：28 个变体全部通过；12 个完整符合 Fixture，5 个部分符合，11 个按设计不映射；运行时拦截没有触发。
- 导入闭包：共 125 个模块，本地模块 26 个。

**系统审计对照**：
- 该账户历史上只启动过 1 次正式监督程序，进程号与记录一致。
- Harness 的启动命令行完全一致，退出码 0。
- 安全日志记录编号从 65637 到 72702，连续，共 7066 条。
- 没有清空日志的记录；审计策略只在当初建立时改过。

## 2. 提交的文件

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `install_formal_v1_result.json` | 13524 | `262F9AA2D073692B1096072CB8F49A47A679D8083779ECE6A7229F5287794C4D` |
| `preflight_pre_collect_result.json` | 833 | `CE5D1C2CC8DB114F76EF1EE8CC36D036318C7CC85CF27BEB4FAA348B29C77C33` |
| `preflight_post_collect_result.json` | 82906 | `F2D6D74D33D7264462140E68F08A5789A4F932AF0A018DCCAA7FFCAF7473CEA8` |
| `preflight_run_record.RAW_REDACTED.json` | 382951 | `8855C048FEA91A8C922F64106191ED6483900CCFEE1D516576FA304A9003E5D6` |
| `preflight_events_history.RAW_REDACTED.xml` | 131140 | `1124A9701AECD3281CB0628719321368F0FF8F35513964CB69471BD0B7C90FEE` |
| `preflight_import_closure.json` | 17303 | `207317E902E72E7AE8A00DFD68C81AF0234A5C6F4AC05736EB06F42453145CD1` |

`preflight_import_closure.json` 是从运行记录中抽出的导入闭包，供生成 Manifest 使用。

DSP-004 保持 `OPEN / HOLD`。
