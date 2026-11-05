# AR-B-007 V4 正式运行 v3 结果

本次运行依据所有者决定 V4-RUN-FORMAL-V3，所用 Manifest 为已接受的 REV2。**结果为 `PASS_FORMAL_V3`**，尚待所有者验收。AR-B-007 保持 `OPEN / BLOCKED`。

**安装**：30 个文件，全部与绑定一致。

**运行**
- 环境：CPython 3.12.10，以 `-I -S -B` 启动，输入 REV5 的散列一致。
- 锁定 773 个文件，散列和签名都没有问题；目录树中有 751 个文件、81 个目录。
- 监督程序 29 项检查全部通过。
- 42 个变体全部通过：12 个完全符合，5 个部分符合，25 个按设计不映射。
- 针对 B1、B2、N1、N2 新增的 14 个变体全部通过，运行时拦截 0 次。

**与 Manifest REV2 对照**
- 导入的 96 个模块与 Manifest 完全相同；24 个本地模块都是 Manifest 条目；没有禁止模块。
- 与预检 v2 相比，只有 Harness 和 9 个受测模块的路径由 `project_v2` 变成了 `project_v3`；其余模块、本地模块和 `sys.path` 都相同。政策 §D1 第 10 项"导入闭包沿用预检 v2"由此得到证实。

**系统审计对照**
- 监督程序（进程号 14356）和 Harness（进程号 5720）都以普通权限运行，Harness 退出码为 0。
- 安全日志记录编号从 65637 到 78225，连续，共 12589 条。
- 没有失败的登录，没有清空日志的记录，也没有新的重启或改时间事件。
- 两个启动脚本的散列与生成时一致。
- 收集开始之前，dsp004val 已经注销。

**一处异常**
- 现象：监督程序在 01:59:59 写完记录并释放文件，之后约 2 分钟（02:01:56）才退出，退出码为 0。
- 这段时间内，dsp004val 没有启动任何进程；运行记录早已写完。
- 最可能的原因：控制台窗口处于选择状态（快速编辑模式），程序的输出被挂起。
- 这不影响结论。

| 机器记录 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/ar_b_007_v4/C03_V4_FORMAL_RUN_V3_RESULT.json` | 4800 | `1832BF88C660569AD28D456B8DBB488B4437DD9F417A584FB8667022BE6E9526` |

| 证据文件（位于 `validation/route_b_c03/wp_008/ar_b_007_v4/formal_v3_run/`，主机名、SID、用户名已替换） | 字节 | SHA-256 |
| --- | --- | --- |
| `install_formal_v3_result.json` | 13523 | `15003185286B3C582934EBE56025877A4B25413FAD05FAD7DC8F3D5974D0B797` |
| `formal_v3_pre_collect_result.json` | 830 | `F6D8A27BF4CBC6E2D96BA4AC74CDBDFABDCAF7F74449087D84D216D325B7608E` |
| `formal_v3_post_collect_result.json` | 110263 | `FB558C105ECEF09BF1EF2853DB6D455DF4B861E5A252352B2A8326DCC45EF64C` |
| `formal_v3_run_record.RAW_REDACTED.json` | 414265 | `CE1FB778474350B1D5A3EC6174F4D08C8C0617060C4A4E300499986BD3A3AC63` |
| `formal_v3_events_history.RAW_REDACTED.xml` | 184322 | `55697CFE072E2D019C94F00555D68C278EE9B05125386ED0A20FE220BE34214B` |
