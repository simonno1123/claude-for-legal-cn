# C03 V6 正式运行 v5 结果

本次运行依据所有者决定 V6-RUN-FORMAL-V5，所用的 Manifest 为已接受的 REV4。**结果为 `PASS_FORMAL_V5`。**

**安装**：30 个文件，全部与绑定一致。

**运行**
- 环境：CPython 3.12.10；输入 REV7 的散列与绑定一致。
- 锁定 833 个文件，散列和签名都没有问题；目录树中有 811 个文件、101 个目录；监督程序 29 项检查全部通过。
- 76 个变体全部通过：13 个完全符合 Fixture，13 个部分符合，50 个不映射；运行时拦截 0 次，被测代码扫描 CLEAN。
- V6 新增的 6 个变体全部通过。其中映射 V-015 Fixture 的变体结果为：请求 `REJECTED`，候选 `HUMAN_REVIEW_PENDING`，下游阻断。

**与 Manifest REV4 对照**
- 实际导入的 96 个模块与 Manifest 完全相同，没有超出 Manifest 的文件，也没有禁止模块。
- 与正式运行 v4 相比，只有 `__main__`（Harness REV7）和项目路径不同；24 个原生模块和 `sys.path` 完全一致。政策 §D1 第 10 项由此得到证实。

**系统审计对照**
- 全部进程都以普通权限运行；Harness 和监督程序的退出码都是 0。监督程序在释放文件后 0.06 秒退出。
- 安全日志记录编号从 65637 到 78871，连续，共 13235 条；没有清空日志，也没有新的重启或改时间事件。
- 两个启动脚本的散列都与生成时一致；收集开始前，运行账户已注销。
- **1 次失败登录**：04:17:48（UTC），从所有者本人的会话以 runas 登录 dsp004val，原因是密码错误（0xC000006A）。之后没有任何 dsp004val 进程；重新启动后于 04:18:08 登录成功。所有者已确认是本人输错密码。
- 启动脚本共被调用三次：04:07 完成安装；04:17:45 第一次预收集，因密码错误而中止；04:18:03 第二次预收集，随后正常运行。

| 机器记录 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/c03_v6/C03_V6_FORMAL_RUN_V5_RESULT.json` | 4800 | `EABCD699C0A54A5CF31D77E0F727147910BC9D24523E80016C3C82571FB0A1E7` |

| 证据文件（位于 `validation/route_b_c03/wp_008/c03_v6/formal_v5_run/`，主机名、SID、用户名已替换） | 字节 | SHA-256 |
| --- | --- | --- |
| `install_formal_v5_result.json` | 13514 | `C316682E71F4A07DA79EE984F86FCF9E931577B7926A6286300BB211ECF053CA` |
| `formal_v5_pre1_collect_result.json` | 830 | `64826F12678E0E25ACC404B65E2B89C759AAB8CBDDBCA335711A860007603365` |
| `formal_v5_pre2_collect_result.json` | 830 | `FD9C007D900E53340B54898D7ABA5D34A66D544794876EF09366A3568A26B3D7` |
| `formal_v5_post_collect_result.json` | 129017 | `6EE14C2DB0521F100F7E4B81591C4AE6B03FD8D91060CB6AEC8D0156D4B83E26` |
| `formal_v5_run_record.RAW_REDACTED.json` | 462133 | `CF835C2B1D60B13DADAFC557C43D384D0FF01D24788EA091323BA2C7570B1D43` |
| `formal_v5_events_history.RAW_REDACTED.xml` | 221289 | `A0CD5BF0302D8855038C77BAC9E2028773C78078402BE2B47D081B928E206C57` |
