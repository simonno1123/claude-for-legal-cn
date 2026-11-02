# DSP-004 路径增量 REV34

本增量记录第四版第一次运行的情况，以及新绑定的一个"只收集"包装脚本。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。DSP-004 保持 `OPEN / HOLD`。

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_INCREMENT_REV33.md` |
| 前一增量说明 | `2CB16A648DECB051BD16AF8BE3F542483AB7AFA1895F496840B72B17183D1813`（1509 字节） |
| 前一增量 JSON | `92C58CE826F20894C96A27F5678C62775214BC051F63FC493BEC894A0BC38E71`（2753 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_INCREMENT_REV34.json` |
| 本增量 JSON SHA-256 | `90870F89C952AB9C2FEC33BE884B2CDC89F06A7731EEA881E839C6761A251B94` |
| 本增量 JSON 字节 | 2413 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 1. 第一次运行

- **运行前收集**：在 2026-11-02T23:25:55Z 完成。移出的是第三版留下的运行记录，散列 `FB530784…79F4`，与第三版的记录一致；收集脚本的散列与绑定一致。结果文件按原样提交为 `validation/route_b_c03/wp_008/dsp004_od04a_t0_dry_run_v4/invocation1_pre_collect_result.json`（1080 字节，`1FB235EAFBE4B0D038108DB4068E1816DA8D06D3797B3811A6D832C102B395EB`），其中不含标识信息。
- **运行后收集**：文件夹在 23:26:56Z 建立，但里面没有任何文件，说明脚本中途停下了。之后所有者重启了电脑，窗口没有了，看不到停下的原因。
- 这次监督程序运行生成的记录应该还在 `dsp004val` 的目录里，下次收集时会被收走。

## 2. 新绑定的文件

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `collect_only_v4.cmd` | 823 | `BB73C89831C82D2AA1B30054A67A30C9B711B7DCAE2CB98DB2B631275B845B92` |

这个脚本只运行已绑定的 `collect_v4.ps1` 的运行后收集一步，并把全部输出（包括报错）存进日志文件，不启动监督程序。

| 状态记录 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_OD04A_V4_STATUS_REV1.json` | 1984 | `F0D2B9C87BE62E7A13024291D2C9FAE64361EC95625232B1331CF5DF390EC942` |

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。
