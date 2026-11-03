# DSP-004 路径增量 REV35

本增量记录"只收集"脚本的运行结果，以及收集脚本的第 2 版。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。DSP-004 保持 `OPEN / HOLD`。

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_INCREMENT_REV34.md` |
| 前一增量说明 | `3087A8A567CFFD7ADC252372CE68E1ACBC1C679266B6D7B0346A4433A0E47BFB`（2235 字节） |
| 前一增量 JSON | `90870F89C952AB9C2FEC33BE884B2CDC89F06A7731EEA881E839C6761A251B94`（2413 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_INCREMENT_REV35.json` |
| 本增量 JSON SHA-256 | `69BA96D043115F1BD02158B4C32A9D0B5A8DD9285403DC5DE4FBAA3D03110F38` |
| 本增量 JSON 字节 | 2408 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 1. 停下的原因

日志（`validation/route_b_c03/wp_008/dsp004_od04a_t0_dry_run_v4/invocation1_collect_only_log.txt`，32 字节，`EEF7093CDA6538E9D6C72CA0D056F1009D36E492DF50F365E50BDB4A8010D2E8`）只有一行：`STOP ACCOUNT_CREATION_EVENTS_2`。

第 1 版收集脚本要求系统日志里只有一条名为 `dsp004val` 的账户建立事件（4720），但实际找到了两条，于是按设计停下，没有移动运行记录。第一次运行后那个空的收集文件夹，也符合这个原因。运行记录仍留在 `dsp004val` 的目录里。

## 2. 第 2 版收集脚本

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `collect_v4.r2.ps1` | 13022 | `A48773E80CF31877AF71F9807E3C2D2022D9D6B50E54D6ED3F7ECBD95A261652` |

改动：时间窗口改为从"账户 SID 与当前 `dsp004val` 相同的最早一条 4720"开始；所有名为 `dsp004val` 的建立事件（4720）和删除事件（4726）都会导出并计数。所有者电脑上以 `collect_v4.ps1` 的文件名部署。仓库里的 `collect_v4.ps1` 保持第 1 版的字节不变。

这项改动很小，只由记录人核对，没有交给新的子代理审查。

| 状态记录 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_OD04A_V4_STATUS_REV2.json` | 1805 | `AC7C1455BAA5CC755856FD8A65DD863F1B2798B3B479DF4EB031EF77A235188E` |

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。
