# DSP-004 OD04-A 第三版演练：运行结果

第三版演练运行了一次，结果为 `PASS_T0_DRY_RUN_V3`。监督程序的自报和系统写下的 4688/4689 事件逐项对照，24 项全部成立。运行后审查把它定性为**阶段 1 环境观察**：不是 OD-04 证据，不是正式运行，也不是接受。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。DSP-004 保持 `OPEN / HOLD`。

| 项目 | 值 |
| --- | --- |
| 机器记录 | `validation/route_b_c03/wp_008/DSP_004_OD04A_T0_DRY_RUN_V3_RESULT.json` |
| 机器记录 SHA-256 | `0909A18C301399F8FC07CC24ACC9C0197BFA8CCAC22892189A4916B9F805B3CD` |
| 机器记录字节 | 9744 |
| 运行前绑定 | PR #35，2026-11-02T04:29:56Z 合并 |
| 运行 | 所有者双击一次；安装 04:34:11Z，监督程序开始 04:34:17Z，释放 04:35:10Z，收集 04:36:32Z |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 1. 提交的文件

只做了两处字节替换：机器名改为 `REDACTED-HOST`，机器 SID 前缀改为 `S-1-5-21-REDACTED`，其他字节不变。运行记录和事件文件的未替换散列记在机器记录里。收集结果和安装结果里唯一的敏感信息是机器名，公开它们的未替换散列可能让人反推出机器名，所以不公开。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `v3_run_record.RAW_REDACTED.json` | 382430 | `39830BF1DEE9B112F58F81988920ED84CC0A2BA926D38FDA15986312E320463E` |
| `events_dsp004val.RAW_REDACTED.xml` | 22776 | `E760E9E01BB1BD6D2EFDA7F633109110ED78613A0DC0F2730F81D0F93955C1FA` |
| `collect_v3_result.RAW_REDACTED.json` | 19268 | `220048E5DEB119E1B86F2D414942499A9F4F230C20773825818D16E7F461F14C` |
| `install_v3_result.RAW_REDACTED.json` | 2956 | `CBD8F00F44C0BB5BD1CB86E94424C8D05203E17E4B8FC6529F5BED9CF41544E1` |
| `check_v3_cross.py` | 8588 | `524825B21F024902144776F7D9C19489A318610F30BB074C02602E2B8D666A26` |

## 2. 结果

- **监督程序**：在 `dsp004val` 账户下运行，中等权限，不在管理员组；69 项检查全部通过；锁定 683 个文件，散列全部一致；3 轮子进程各加载 29 个本地模块，全部在约束清单内；标准输入一开始就是空的。
- **系统事件对照**（`check_v3_cross.py`，24 项全部成立）：
  - 这段时间里 `dsp004val` 一共启动了 10 个进程：`runas` 启动 `cmd`，`cmd` 启动监督程序，监督程序启动 `whoami` 和 3 个探测进程。没有多出任何进程。
  - 每个进程都正常退出；所有进程属于同一个登录会话。
  - 探测进程的进程号、命令行、启动和退出时间都与运行记录一致，时间相差不到 10 毫秒。
  - 这段时间里没有清空日志、修改审计策略或调整系统时间的事件。
  - 运行记录写于监督程序释放文件之后、退出之前；运行后，已安装的文件与绑定的版本一致。

## 3. 运行后审查

审查者是一个没看过编写过程的全新子代理，与记录人属于同一模型家族，不是外部审查。审查没有发现阻断项。审查建议补的核对（完整进程树、全部进程的退出、登录会话、账户 SID、记录写入时间等）已加进脚本，数据全部通过。审查结论：定性为阶段 1 环境观察是恰当的，不能更强，也不必更弱。

第二版审查列出的缺口，现在的状态：

| 编号 | 缺口 | 现状 |
| --- | --- | --- |
| 1 | Detached system-written 4688/4689 | PARTLY (mostly) |
| 2 | Run count not self-reported | PARTLY |
| 3 | Supervisor identity anchored at execution | PARTLY |
| 4 | Validation host, separate standard account, >1 run | PARTLY (account closed; host by owner decision; 3 runs in one invocation) |
| 5 | v2 retry authorization | NOT ADDRESSED BY V3 (v2 governance item) |
| 6 | Raw bytes committed | PARTLY (redacted by plain substitution) |
| 7 | stdin deviation; 3.12.13 vs 3.12.10 | PARTLY (stdin resolved; version residual) |
| 8 | Outside-family review | OPEN BY OWNER DECISION |

## 4. 要成为证据还缺的

1. 所有者另行作出准入决定。
2. 能在机器之外核对的事件证据：扩大时间窗口，包括 `dsp004val` 更早的记录和登录事件 4624/4634；或者导出去标识的全部账户事件，以证明记录编号连续。
3. 证明实际执行的就是绑定的监督程序字节，并记录实际运行的 `go_v3.cmd` 的散列。
4. 重复运行几次，最好跨重启，用审计日志计数。
5. 处理 3.12.13 与 3.12.10 的差异和其余已知问题（KnownDLLs、`Users` 组的读取执行权限、本机仍有所有者的管理员账户）。
6. 如果所有者认为有必要，补一次外部审查。

DSP-004 保持 `OPEN / HOLD`。OD-04 保持 `OD04_A_DRY_RUN_OBSERVATION_NOT_EVIDENCE`。
