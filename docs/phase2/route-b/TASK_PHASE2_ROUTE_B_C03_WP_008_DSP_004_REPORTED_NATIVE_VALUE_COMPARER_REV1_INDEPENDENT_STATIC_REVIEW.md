# DSP-004 传入原生值投影比较核心 REV1 — 独立静态复核记录

本记录属于 `claude-for-legal-cn` 的局部新候选与静态复核批次。只记录实际完成的独立源码复核，不是 Owner 接受、189 项运行结果、完整捕获证明或执行准入。

## 1. 固定复核对象

- 源码：`validation/route_b_c03/wp_008/DSP_004_REPORTED_NATIVE_VALUE_COMPARER_CANDIDATE_REV1.cs`。
- 实际字节数：21186；物理行数：385；UTF-8、无 BOM、LF、最终 LF。
- 实际 SHA-256：`A48B1C45A6CD3EC5999FE183730AB727BC0C90F29E6957F97459CB2440F22F83`。
- 定位：调用侧提供原生 `object[]` 值投影与独立提供预期之间的有限比较核心，**不是管道捕获器**。
- 编译 / 装载 / 调用 / 测试 / 集成：`NOT PERFORMED`。
- Owner 接受及运行前置：`NOT ESTABLISHED`。

原主审说明 `TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_REPORTED_NATIVE_VALUE_COMPARER_REV1_PRIMARY_STATIC_CHECK.md` 保持原文；SHA-256 为 `B30160BAB3BBB57AC6A579ECD5D7B594E15DA70374F0A9C4E0D5CDBA7F7C07D5`。其中额度中断、独立复核未完成和未备份状态是上一轮检查点的真实记录，不回写为通过。本记录记载后续恢复并实际完成的新复核，不能把旧检查点当作当前独立复核或备份状态。

## 2. 实际独立只读复核

独立子审查员完整读取固定候选，并仅对获准的 P1 预期结构及已接受控制端前八函数的返回结构进行只读核对。结论：

```text
STATIC PASS / LIMITED — CALLER-SUPPLIED VALUE PROJECTION SOURCE ONLY

Blocking Source Defects Observed Within Reviewed Scope:
0

Candidate Acceptance / Execution Qualification:
NOT ESTABLISHED
```

| 复核项 | 静态评定 | 定位与保留边界 |
| --- | --- | --- |
| 固定编号与返回数量 | PASS | 160–189 行：M6 / RQ18 / D7 / F62 / RD52 / WR44，三位数字编号；M 对应 8/26/1 个单次投影值 |
| 字段名与原生类型 | PASS | 121–158 行：Case3 / Fixed27 / D6 / F10 / RD7 / WR9 对应 P1/B；没有通用转换 |
| 集合与 null 表示 | PASS | 279–331 行：固定集合数量与顺序、精确标量类型；可空 Int32 单独处理；空数组、单 null 槽、null 字段仅在传入表示层分开 |
| 元数据先于 Value | PASS / LIMITED | 242–276 行：先验证全部可见属性的 exact instance PSNoteProperty、成员类型、名称与唯一性，再读 Value；隐藏成员不在证明范围 |
| 避免自定义行为 | PASS / LIMITED | 精确 CLR 类型、ordinal 字符串、原生数组与字典枚举；不调用任意对象 Equals、ToString、转换或未知属性 getter；框架身份/内部行为未验证 |
| oracle 与值关系归因 | PASS / LIMITED | 351–375 行：参考/实际投影分别处理不可比较状态；oracle 来源、独立性和权威未认证；EQUAL 不等于 MATCH、完成或捕获证明 |
| M 多次调用与引用身份 | LIMITED | 36–37、81 行明确未实现 first → mutation → second 以及可变对象引用断言；只能分别比较传入值 |
| 资源、并发与异常 | PASS / LIMITED | 固定形状与局部循环有限，非实际时间/内存保证；并发冻结、内部整合分配、外侧监督和完整异常寿命未建立；原异常仅在结果成功返回时私有持有 |

复核没有编译、AST、装载、调用、测试、环境探测、Git 或文件修改；没有读取控制端后两个 bootstrap/run 函数，也没有访问非目标上游资产或其他项目。适用根 AGENTS 已读取。本结论不是环境兼容性或真实测试结果。

## 3. 不转移的实现与证据缺口

1. 只有调用侧传入的 native value projection；真实 PowerShell 输出计数、包装适配、完整捕获、完成事件、预期认证与私有所有权未建立。
2. `EQUAL / DIFFERENT / REFERENCE_NOT_COMPARABLE / ACTUAL_NOT_COMPARABLE / INSPECTION_FAILED` 仅为内部值关系，不转换为 `MATCH / NOT_MATCH / NOT_RUN / INCOMPLETE`，也不建立第五项目状态、执行许可或聚合结论。
3. Public Properties 是可见整合视图；隐藏元数据、TypeTable / adapter、程序集身份与框架内分配必须由外侧另行绑定。源码中的有限循环不能证明整个框架有界。
4. oracle 与传入值的独占、防并发、冻结、真实来源未认证；原生类型检查与摘要字面量不证明这些前置。
5. M-004/005/006 的完整多次调用、首次副本变更与引用身份检查仍未实现。不得将单次值相同记为隔离或 fresh 通过。
6. 同份受控源码字节装载、完整十定义/八函数与 helper 归属、启动前全部输出封锁、结果提交与首次停止的原子裁决、真实计时及外侧资源停止仍未实现或未绑定。
7. D-007 独立准备、同份私有输入摘要门仍 `UNBOUND / NOT_RUN`；真实 driver SHA 正向分支仍 `NOT COVERED`。本批未访问 driver / caller / reader / baseline 四份上游资产。
8. 120/5/5 秒仍为设计提议；异常原对象的完整寿命、主/次异常并存、进程损失与原操作/后代资源收束未建立。
9. 全部上游 `LIMITED` 保留；`DSP-004 OPEN / HOLD`、`B-01 OPEN`、`B-02 OPEN`。
10. 不准入来源、不实际捕获、不集成、不安装 OCR/软件、不调用第三方模型；不涉及独立 ACOS、协作系统源项目或其他项目。四处既有 manifest description 不一致未修订。

## 4. 固定输入完整性

恢复复核后主审再次读取本地摘要，下列文件仍与原固定值相同；没有修改它们：

| 文件 | 字节数 | SHA-256 |
| --- | --- | --- |
| DSP_004_LOCAL_VALIDATION_CARRIER_CANDIDATE_REV1.ps1 | 70284 | 46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C |
| DSP_004_OUTER_CONTROLLER_CANDIDATE_REV1.ps1 | 25573 | 891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB |
| DSP_004_NATIVE_INPUT_ORACLE_CANDIDATE_REV1.ps1 | 286568 | D585B3CE407B0D3BEAD2C2D5339E4EC1C66D0E768D2FB87B49F7BD053B50DB9D |

P1 候选的 Owner 接受仍未建立，本记录不升格其状态，也不借用它或其他旧源码的接受/测试结论。

## 5. 阶段备份范围

本批形成的里程碑仅为：有限投影比较核心新候选完成实际独立静态复核，保留全部 LIMITED。

备份若完成，只处理以下三个新文件：

- 新比较核心源码；
- 原主审静态核对说明，作为上一轮真实中断检查点保留；
- 本独立静态复核记录。

复核前已确认本地 HEAD 与实际远端 main 都是 `c86eb81e8878ccf2653c079fa81b4a97d4458506`。使用普通提交和推送，不强推、不改写历史或无关文件。提交 SHA、推送结果须以实际操作为准，不在此预填。备份不等于 Owner 接受、运行授权或阶段关闭。
