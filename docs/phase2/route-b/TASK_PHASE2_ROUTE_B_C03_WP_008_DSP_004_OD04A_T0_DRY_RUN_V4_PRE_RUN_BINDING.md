# DSP-004 OD04-A 第四版：运行前绑定

第四版重复运行已经绑定并安装的第三版监督程序，一共三次，第二次和第三次之间重启一次电脑；同时把审计收集范围扩大到 `dsp004val` 账户建立以来的全部历史。第四版不安装任何东西，监督程序本身不变。**还没有运行。** `Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。DSP-004 保持 `OPEN / HOLD`。

| 项目 | 值 |
| --- | --- |
| 机器记录 | `validation/route_b_c03/wp_008/DSP_004_OD04A_T0_DRY_RUN_V4_PRE_RUN_BINDING.json` |
| 机器记录 SHA-256 | `6BBB40D21C70B0F3B334DAAB227B198BBC16EDD5D698F479AB1DB24952FE6A3C` |
| 机器记录字节 | 5207 |
| 依据 | 所有者对第四版建议的回复 `按照你的建议实施。` |
| 结果上限 | 阶段 1 环境观察，不是 OD-04 证据，不是正式运行，不是接受 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 1. 绑定的文件

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `go_v4.cmd` | 1475 | `C03B667309170D351983F82DEAE69E9008758F78CF11F9CD874D2CC35F2E78A6` |
| `collect_v4.ps1` | 12394 | `1199400BB288A6C1B9B05EC20F5D90C6F3E007AEC2BEC88BBF684430369FBD9B` |

## 2. 收集内容

每次运行后，收集脚本都会做下面这些事：
- 等 `dsp004val` 的运行结束，然后把运行记录移出该账户的目录；
- 导出 `dsp004val` 自账户建立（事件 4720）以来的全部进程事件和登录事件，以及这期间的开机事件和审计策略变更事件；
- 从 4720 那条记录起，逐条核对安全日志的记录编号是否连续；
- 统计清空日志、修改时间、日志服务停止等事件；
- 计算启动脚本、收集脚本和已安装文件当前的散列。

## 3. 运行前审查

审查者是一个没看过编写过程的全新子代理，与记录人属于同一模型家族，不是外部审查。初审结论：不能运行（1 个阻断项，5 个重要问题）。处理如下：

| 编号 | 级别 | 问题 | 处理 |
| --- | --- | --- | --- |
| 1 | BLOCKING | DataMap crashes on 4608 (empty EventData) under StrictMode | fixed: namespace-safe SelectNodes |
| 2 | MAJOR | 4720 may roll off the circular 20 MB log before all runs finish | not changed (enlarging the log is a system-setting change); runs to be done within about a day; the collector stops if 4720 is missing |
| 3 | MAJOR | record moved before queries that can fail | fixed: record moved last, after all queries |
| 4 | MAJOR | File.Move keeps the profile ACL | fixed: copy bytes, re-read and compare, then delete the profile copy |
| 5 | MAJOR | launch count by command-line substring can undercount | handled in the later checker: every dsp004val 4688 classified, records matched by supervisor PID and time; 4719 exported as full events |
| 6 | MAJOR | record-number gap check selected by time | fixed: selected by EventRecordID from the 4720 record; gap ranges listed; first must equal the 4720 record; 1100/1104/1105/1108 counted |
| 7 | MINOR | rendering every event is slow | fixed: record numbers streamed with EventLogReader |
| 8 | MINOR | Fast Startup shutdown is not a boot | instruction: use Restart |
| 9 | MINOR | owner may press the key before the record is written | fixed: post waits up to 3 minutes for any dsp004val PowerShell to end |
| 10 | MINOR | mistyped runas password gives 4625, not 4624 | fixed: 4625 collected |
| 11 | MINOR | 4634 subject query never matches | fixed: removed |
| 12 | PRIVACY | owner and host identifiers in 4720/4648/4624 and others | redacted before commit; nothing from the machine committed unredacted |

修复由记录人核对，没有再交给第二个子代理审查。

DSP-004 保持 `OPEN / HOLD`。OD-04 保持 `OD04_A_DRY_RUN_OBSERVATION_NOT_EVIDENCE`。
