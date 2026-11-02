# DSP-004 OD04-A 第三版演练：运行前绑定

本记录在运行之前把第三版演练的全部文件按确切字节绑定。这次是阶段 1 的环境演练：仍是第二版的探测，改为在独立普通账户 `dsp004val` 下运行，一次跑三轮，运行后收集系统写下的 4688/4689 事件。**还没有运行。** `Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。DSP-004 保持 `OPEN / HOLD`。

| 项目 | 值 |
| --- | --- |
| 机器记录 | `validation/route_b_c03/wp_008/DSP_004_OD04A_T0_DRY_RUN_V3_PRE_RUN_BINDING.json` |
| 机器记录 SHA-256 | `EEED96B4138632886E6B00087931C9E7108A13F62A0F96AC9AE31A5CF42E669A` |
| 机器记录字节 | 7627 |
| 依据 | 改签 REV5；阶段 1 决定 REV1、REV2；所有者对第三版说明的回复 `好的，继续。` |
| 结果上限 | 即使结果为 PASS，也只是阶段 1 环境观察，不是 OD-04 证据，不是正式运行，不是接受 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 1. 绑定的文件

文件提交在 `validation/route_b_c03/wp_008/dsp004_od04a_t0_dry_run_v3/`，按原样字节保存，不做换行转换。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `go_v3.cmd` | 1503 | `7530C3FEE3DEFBF5413710A5AAB27C9DF354456CB542B958D5EA26514E830792` |
| `install_v3.ps1` | 7514 | `56D0578FDEC308CE23B9D4E4C648837CF9351647D5242D747F5226251DECF043` |
| `run_v3.cmd` | 390 | `B430D9B22CACEDEEAE9C3124916ECFF8FD023EFABAE8D870920ECD2DAE64195A` |
| `supervisor_v3.ps1` | 24819 | `7CC3EC3D0432BFFE3D9ADAA34D90ED10DB015F5AFC241221E77E517B69C9E433` |
| `probe_v3.py` | 2669 | `3AF5FD03B9487642A7256EAA21D654F6BF072749EBAF03B967A3E307C34CB2A3` |
| `bound_list_v3.json` | 148747 | `0A349A6DBDA8B1397941EDE195D6D76E5B77DBE252BA6D3B80E0516016AAE561` |
| `collect_v3.ps1` | 8924 | `66BFF87C50714AD677CD39CEF02A6B00D7CC2E36517C20A51E714A9B9ABBA65B` |

## 2. 运行方式

1. 所有者在 `文档\dsp004-probe\v3` 里双击 `go_v3.cmd`，点一次"是"。
2. 脚本安装监督程序，然后用 `runas` 以 `dsp004val` 身份启动运行；所有者输入一次 `dsp004val` 的密码。
3. 新窗口显示 PASS 或 BLOCKED 后，所有者关掉它，在原窗口按任意键；脚本收集运行记录和系统事件。
4. 记录人通过设备桥读取结果。

## 3. 运行前审查

审查者是一个没看过编写过程的全新子代理，与记录人属于同一模型家族，不是外部审查。初审结论：不能运行，有 3 个阻断项。处理如下：

| 编号 | 级别 | 问题 | 处理 |
| --- | --- | --- | --- |
| 1 | BLOCKING | supervisor wrote v2_run_record.json; collector looks for v3_run_record.json | fixed |
| 2 | BLOCKING | collector Events() unrolls empty/one-item arrays; .Count throws under StrictMode | fixed: @(...) at call sites |
| 3 | BLOCKING | runas inherits the owner's folder as current directory; dsp004val may not open it (error 267) | fixed: pushd System32 around runas |
| 4 | MAJOR | nothing gates on auditing actually working | fixed: collector stops unless exactly 3 python.exe 4688 events for dsp004val, each with a command line |
| 5 | MAJOR | evtx export holds every account's events (owner identifiers) | handled: evtx stays on the machine, never committed; filtered XML redacted before commit |
| 6 | MINOR | net localgroup exit code unchecked | fixed |
| 7 | MINOR | collector exits 0 without a record | fixed: exit 3 |
| 8 | MINOR | runs and checks lost if run 2 or 3 blocks | fixed: attached to the record before the loop |
| 9 | MINOR | MyDocuments may be empty | fixed: fallback to UserProfile\Documents |
| 10 | MINOR | GrandParent may be gone or reused | recorded only; not used as evidence |
| 11 | MINOR | stdin BOM if code page 65001 | not changed; the check fails closed, it does not crash |
| 12 | MINOR | self-elevation uses bare powershell; silent on UAC decline | fixed |
| 13 | MINOR | dsp004val needs a non-empty password and no forced change | operational; account set with password, net user shows password required |
| 14 | MINOR | locale-dependent time format | fixed: InvariantCulture |

修复后，安装器、收集器和本记录里的散列都已重新固定。审查者做过的交叉核对（约束清单、安装器和收集器里的散列表）已用脚本重新跑过。

## 4. 已知的剩余问题

- 监督程序在运行时仍不核对自己的散列，靠本绑定、安装器常量和收集器运行后复算来锚定。
- KnownDLLs 从启动时的映射加载（IR-07）。
- 运行时目录对 `Users` 组开放读取和执行（IR-14），`dsp004val` 属于这个组。
- 运行在所有者的电脑上，也就是选定的验证机；记录里的时间来自本机时钟，收集器会统计系统时间被修改的事件（4616）。
- V3.2 写的是 3.12.13，运行时是 3.12.10，这一项没有改变。

DSP-004 保持 `OPEN / HOLD`。OD-04 保持 `OD04_A_DRY_RUN_OBSERVATION_NOT_EVIDENCE`。
