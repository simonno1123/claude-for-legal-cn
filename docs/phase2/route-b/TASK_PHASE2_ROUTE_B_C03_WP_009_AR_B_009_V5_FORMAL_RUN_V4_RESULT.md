# AR-B-009 V5 正式运行 v4 结果

本次运行依据所有者决定 V5-RUN-FORMAL-V4，所用的 Manifest 为已接受的 REV3。**结果为 `PASS_FORMAL_V4`**，尚待所有者验收。

**安装**：30 个文件，全部与绑定一致。

**运行**
- 环境：CPython 3.12.10；输入 REV6 的散列与绑定一致。
- 锁定 803 个文件，散列和签名都没有问题；目录树中有 781 个文件、91 个目录；监督程序 29 项检查全部通过。
- 70 个变体全部通过：
  - 12 个完全符合 Fixture；
  - 13 个部分符合，其中 8 个是 V5 新增并映射到 Fixture 的变体；
  - 45 个不映射。
- V5 新增的 28 个变体全部通过；运行时拦截 0 次。

**与 Manifest REV3 对照**
- 实际导入的 96 个模块与 Manifest 完全相同，没有超出 Manifest 的文件，也没有禁止模块。
- 与预检 v2 相比，只有项目路径不同，其余完全一致。政策 §D1 第 10 项"导入闭包沿用预检 v2"由此得到证实。

**系统审计对照**
- 全部进程都以普通权限运行；Harness 和监督程序的退出码都是 0。
- 监督程序在释放文件后 0.07 秒退出，上次出现的延迟这次没有再出现。
- 安全日志记录编号从 65637 到 78529，连续，共 12893 条。
- 没有失败登录，没有清空日志，也没有新的重启或改时间事件。
- 两个启动脚本的散列都与生成时一致；收集开始前，运行账户已注销。

| 机器记录 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/ar_b_009_v5/C03_V5_FORMAL_RUN_V4_RESULT.json` | 4087 | `C75E5E4BFB24C9BECC970A5EB2643E7441D37881E5F2E50904D9452589FB3774` |

| 证据文件（位于 `validation/route_b_c03/wp_008/ar_b_009_v5/formal_v4_run/`，主机名、SID、用户名已替换） | 字节 | SHA-256 |
| --- | --- | --- |
| `install_formal_v4_result.json` | 13524 | `F4A2D11C45A554002BDD58F281EE52555B90DC31A4E636019BB134A1CCA61D03` |
| `formal_v4_pre_collect_result.json` | 830 | `089C7A5F0B322B2B4AEBB257D668AC75BF23B3407A430067C6303CAB2460F794` |
| `formal_v4_post_collect_result.json` | 119376 | `828FCC880B3C0B878CEB561E31168C2B07D71D3FBE4351A0DCA9EBE967DBE620` |
| `formal_v4_run_record.RAW_REDACTED.json` | 443879 | `1A5C202F9378DCA0B131DA4B48D1CD56CE6D5AE20F9F5D93B42622516E9152C1` |
| `formal_v4_events_history.RAW_REDACTED.xml` | 202048 | `7375613597EE6FC4D7E0D7630223771BA0BA8E0373ED83E593D5CB2F3E9302A6` |
