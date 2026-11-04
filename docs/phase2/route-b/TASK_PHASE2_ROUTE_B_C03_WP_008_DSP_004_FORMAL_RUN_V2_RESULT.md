# DSP-004 正式运行 v2 结果

本次运行依据所有者决定 P7-RUN，以 `dsp004val` 身份执行一次，所依据的 Manifest 为已接受的 REV1。**结果为 `PASS_FORMAL_V2`。** 这一结果尚待所有者验收（阶段 8），DSP-004 保持 `OPEN / HOLD`。

**运行**
- 环境：CPython 3.12.10，以 `-I -S -B` 启动；输入为 REV4，散列一致。
- 锁定文件 743 个，散列和签名均无问题；目录树共 721 个文件、71 个目录。
- 监督程序检查 29/29 项全部通过。
- Harness 共 28 个变体，全部通过：12 个完整符合，5 个部分符合，11 个按设计不映射；运行时拦截 0 次；六侧数据一致。

**与 Manifest 对照**
- 导入闭包共 96 个模块，与 Manifest 完全相同；24 个本地模块全部是 Manifest 条目。
- 不含禁止模块。
- 闭包与预检 v2 完全相同（模块、本地模块、`sys.path` 三项）。

**系统审计对照**
- 监督程序（进程号 6328）和 Harness（进程号 1300）的启动与退出，在审计中都有对应记录；退出码都是 0；以普通权限运行。
- 安全日志记录编号从 65637 到 75209，连续，共 9573 条。
- 没有失败的登录，也没有清空日志的记录。
- 已安装的 30 个文件全部与绑定一致。

| 机器记录 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_FORMAL_RUN_V2_RESULT.json` | 4307 | `86488C277577B259F6FE415FEF9525A43F32123808AFD127826ED01443226196` |

| 文件（位于 `validation/route_b_c03/wp_008/dsp004_phase7_formal_v2_run/`） | 字节 | SHA-256 |
| --- | --- | --- |
| `formal_v2_pre_collect_result.json` | 833 | `23537E4A6818EB753A34013645A71C1D82B0CDDE42125FA9071958565585224C` |
| `formal_v2_post_collect_result.json` | 100070 | `4C640FB23B74DE1D22CB21A1EE9DE67E75795D0665BEE6C567AAF16FA362D518` |
| `formal_v2_run_record.RAW_REDACTED.json` | 392761 | `72F5F628F90E1CD0F8A2CD07BDE33A341E377E4C1E304FF677DCC49307AC330A` |
| `formal_v2_events_history.RAW_REDACTED.xml` | 164804 | `A6F68DF4A0195538A7E7F6E33FE062D401B29CBC96F37D577E0DEB3E0987F60D` |

DSP-004 保持 `OPEN / HOLD`。
