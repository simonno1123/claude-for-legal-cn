# DSP-004 阶段 2 至 5 所有者决定 REV1

所有者张纯熙就阶段 2 至 5 作出了四项决定。到目前为止没有接受任何资产，没有生成 Manifest，也没有正式运行。DSP-004 保持 `OPEN / HOLD`。

| 项目 | 值 |
| --- | --- |
| 机器记录 | `validation/route_b_c03/wp_008/DSP_004_PHASES_2_TO_5_OWNER_DECISIONS_REV1.json` |
| 机器记录 SHA-256 | `8FAB5BC81A4E5EEFE206C1E99D1C31D701F2892A788D5B56060B458745813FA9` |
| 机器记录字节 | 3489 |
| 方式 | 所有者在记录人的提问中选择选项，选项文字由记录人起草 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 1. 四项决定

| 编号 | 关卡 | 所有者的选择 |
| --- | --- | --- |
| P2-SOURCES | FA-03 / R-01 | 六侧来源全部用本地合成来源。预期侧沿用 REF-03 的三份合成文档：`SYNTHETIC-PROJECT-001`、`SYNTHETIC-SESSION-001`、`SYNTHETIC-PROVIDER-001`。实际侧由记录人编写、绑定并审查的捕获入口，在已准入的阶段 1 环境里，从合成调用上下文中捕获。不接真实的项目、会话或供应商。 |
| P3-CONTRACT | FA-04 / R-03 | 记录人先对类型合同 REV3（`AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F`）和数组政策 REV3（`39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123`）做在库审查，审查者属于同一模型家族。没有阻断项，就按这两个确切 SHA 记为所有者已接受；有阻断项，就先修复，再问所有者。 |
| P5-LIMITED | FA-06 / R-06 / R-07 | 现有全部 LIMITED 项，包括依赖、启动、隔离、停止和清理，都作为已声明的已知限制保留。正式结果只在这些限制范围内下结论，不声称它们已经消除。 |
| P4-DRAFT | FA-05 / R-05 | 记录人可以起草完整输入候选（新文件，不覆盖 `SCENARIO_INPUT_BINDING.json`）、原生结果到 Fixture 的比较映射，以及 Harness 源码，经绑定和审查后交所有者接受。这项决定本身不接受任何资产，不生成 Manifest，不正式运行。 |

对这四个关卡，REV17 记下的拒绝和保留由上表的选择取代。

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 在 P3-CONTRACT 的有条件接受生效前保持 `OPEN`。
