# DSP-004 归档核对器结构适配说明 REV1

## 1. 首次不完整观察保留

首次新核对器完整输出已留存，退出码为 1，Outcome 为 FIXED_ARCHIVE_RECONCILIATION_INCOMPLETE，FailurePhase 为 AR-001，异常为 PropertyNotFoundException。首次入口及原计划均保留，不追溯修改。

首次记录完成了 11 个核对检查，但在组合归档的子记录检查表处停止，GroupCount=0 表示没有完成整个组的核对，并非没有归档。FailedAuditChecks=0 只表示已登记检查中没有 false；PrimaryExceptionType 非空和 INCOMPLETE 已明确阻止登记通过。

| 版本／记录 | SHA-256 | bytes |
| --- | --- | --- |
| 首次入口快照 | FCEDC4752FDC490E0E82BC914781FF5B5EA4E5627391C91BE0DF3192035E29A9 | 19341 |
| 首次不完整观察归档 | 411D913751AD0529239E58FFBD12CD5EB680ADFC7A9767134B2A3A3FD0DD8838 | 11910 |
| 仅适配已知子记录字段后的新入口 | 2AF0A8E2902AF838FC5A60DBAE92DA0D47C211A2F1CAC45BA4CEEA6BDF1CD035 | 19604 |
| 原计划，保留首次入口身份 | 95952FFA66F9060B5FD466A627B1F566F9264CE97A1C7E7814AE45AD49489505 | 9075 |

首次完整核对观察 LF 文本 SHA-256 为 662AC243616C18C04F874057A65F885B1EE2AC2707121CDF7AA1CA8BF4BA3E3B，13450 UTF-8 bytes。

## 2. 只读确认的结构差异

组合归档中的 RW、PURE、D007 子记录都使用检查数组；但布尔字段并不相同：

| 子记录 | ID 字段 | 布尔字段 |
| --- | --- | --- |
| RW | Id | Passed |
| PURE | Id | Passed |
| D007 | Id | Pass |

首次新核对器一律读取 Passed，在 D007 子记录上触发字段不存在。该问题属于新增核对器的结构假设，不是既有归档损坏或既有测试失败。

## 3. 有限修正

只对本批尚未接受的新核对器修改：

- Check-Assertions 增加固定布尔字段参数，只允许 Passed 或 Pass。
- 缺失字段、不是原生 bool、不是 true、ID 缺失或重复，仍然拒绝。
- 只有已固定 D007 子记录使用 Pass；RW、PURE 及顶层检查仍使用 Passed。
- 不重命名原记录、不新增虚构字段、不用默认 true／零值回避检查，也不改变文件散列、记录计数、预置 Outcome 或 71 个核对检查的目标。

没有修改任何已接受文件或六组既有归档。没有执行受测源码、Python、C# 编译或 child 阶段。本说明仅补充原计划中新入口的修正身份，不改变正式阶段权限。

## 4. 保留边界

后续复跑仍只验证固定归档的一致性，不重跑原断言，不把规范化记录当作缺失原始字节，不把记录内 PASS、旧状态或历史接受声明自动确认为当前治理事实。

47 份保护文件及两个历史参考只读身份必须保持不变。全部 LIMITED、DSP-004 OPEN / HOLD、B-01 OPEN、B-02 OPEN 保留；不准入来源、不真实捕获、不集成或部署。
