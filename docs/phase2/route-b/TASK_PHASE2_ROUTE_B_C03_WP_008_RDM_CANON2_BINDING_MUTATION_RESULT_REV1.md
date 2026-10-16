# Route B C03 / WP-008 — 双层一致性候选错误注入结果 REV1

## 1. 实际完成与效力

**LOCAL PREDECLARED BINDING MUTATION SENSITIVITY PASS：1 个原版基线完成，8 个预声明内存错误在指定断言被发现。**

本轮仅检查局部测试是否能识别指定的一致性保护移除。未修改原候选、原验证器、原控制端或任何已接受文件；只新增计划、私有错误注入控制端、观察归档、本报告四个本项目文件。未物化八份变异候选，它们只作为新进程中的合成测试字节快照保留。

原版完整 ValidatorResult 与上一轮观察归档解压后的 Result 一致，仍为 106 个唯一 PASS 检查及 3 个字节向量。八个错误版本各自在指定断言失败，不声称它们完成了整个测试集，也不把预期失败的 wrapper 退出 0 解释为候选通过。

未接受双层一致性候选或任何新资产；不建立正式 Manifest、可信根、来源/权限或执行资格。DSP-004 仍 OPEN / HOLD；B-01、B-02 仍 OPEN；所有 LIMITED 和历史记录保留。独立 ACOS 和其他项目未访问、未修改。

## 2. 新增文件与固定输入

| 新增文件 | SHA-256 | UTF-8 字节 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/RDM_CANON2_BINDING_PREDECLARED_MUTATION_REV1.ps1` | `B2B3BB909BEF11D8E108AFC0ADBE6F1363667E93AA6C41EA4EB1A84FEAE9B524` | 28475 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_CANON2_BINDING_MUTATION_PLAN_REV1.md` | `3A27572851A291154D09500AE3CD45C4252E0200EFF4C5C6309589F107A2B676` | 6715 |
| `validation/route_b_c03/wp_008/RDM_CANON2_BINDING_MUTATION_REV1_OBSERVED_RESULT.json` | `8718C5FFD58AE45A52C38CC845FE9B78D1441C9B37A636F08EBD2949C9A4570F` | 30700 |

原 binding 候选固定为 `32535D3E4800E39E8AAF510166AD2AF04E0436D39E7C0BAD528B329D24E66821`（5799 字节）；原验证器为 `944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476`（13142 字节）。scalar 与 tree 依赖分别保持 `532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4`、`F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87`。

本轮定点重新核验九个固定既有文件，完整 ProtectedInputs 清单及四份 FixedSources 均在观察归档中。九项全部与起始身份一致；这是本轮的定点范围，不声称再次完整重复上一轮七十项检查。Git 范围核对显示现有项目文件未改写。

## 3. 预声明错误逐项结果

每项均从同一原候选独立派生，Before 片段恰好匹配一次；每份变异源码长度、SHA、完整 gzip、Before / After、原 SHA、对应四源 CaseSpecification 均已归档。

| ID | 注入的单点错误 | 实际 AssertionError ID | 内存源码 SHA-256 | 字节 | 判定 |
| --- | --- | --- | --- | --- | --- |
| MU-B01 | 全文散列保护移除 | `L-LABEL-STALE-FULL-SHA` | `11EBD7A12AF07BEAA4EDD8245EE13100629BEACA8302B41E06C67B7CB8EFB973` | 5764 | 指定错误已观察 |
| MU-B02 | 正文聚合散列保护移除 | `B-AGGREGATE-MISMATCH` | `03CD28E0F619ED747DEFBCCF2264461B1D668E10E5D2AEA38809CFD0E115358B` | 5770 | 指定错误已观察 |
| MU-B03 | 正文条目数保护移除 | `B-COUNT-MISMATCH` | `EC5113EE8477E692805F5BCB0E59750D322A4FD7D4719655E4165B72FEE86886` | 5770 | 指定错误已观察 |
| MU-B04 | 正文总字节数保护移除 | `B-TOTAL-MISMATCH` | `73D3A0FAD551855816817F11A42D5B0014172CB19E645F9AE2D473A58438CD59` | 5771 | 指定错误已观察 |
| MU-B05 | detached 聚合散列保护移除 | `D-MISMATCH-AGGREGATE_SHA256` | `9F1E2087EA471904969BF58ADF34C4F129ACC038D5D8F971F3326C9F2A941183` | 5765 | 指定错误已观察 |
| MU-B06 | detached 条目数保护移除 | `D-MISMATCH-ENTRY_COUNT` | `E38808C8846B503EC9E7EA2D9C806DDF6DB7DEEEAF8765AF4612A141C4874D0A` | 5775 | 指定错误已观察 |
| MU-B07 | detached 总字节数保护移除 | `D-MISMATCH-BYTE_TOTAL` | `D2547E6CBA6574643CAB94FFE8662AF45AF975A297D9D94173617BD1B00E589D` | 5776 | 指定错误已观察 |
| MU-B08 | 非权威限定语不完整 | `P-ONE.QUALIFIER` | `5B3351956372A90A10A86A4EEC8D47C37595DE8289C6105CAF954F45B9C6BA88` | 5776 | 指定错误已观察 |

八个负例的共同记录均为：

- RunOutcome：EXPECTED_ASSERTION_OBSERVED。
- FailurePhase：RUN_CLOSED_VALIDATOR；FailureType：AssertionError。
- FailureAssertion 与事前计划及控制端指定字符串完全相同。
- SubjectValidationPassed：false；ValidatorResult：null。
- 编译和固定快照装载已完成，未将解析失败或装载错误充当测试发现。

MU-B08 仅测试非权威限定语丢失能否被检查到；内存中不完整返回限定语不构成任何授权或接受决定。其运行在第一个正向向量的限定语断言处结束，未输出任何业务结果。

## 4. 实际运行与原始证据

| 项目 | 观察 |
| --- | --- |
| 新 Python 进程数 | 9 |
| 原版基线 | 1；106 检查 / 3 向量完成 |
| 预声明负例 | 8；8 个指定断言均观察到 |
| 实际 Python 版本 | 3.12.14（九次相同） |
| Python 可执行文件 SHA-256 | `B847BB9F4E48C19F585C8BF7D8B355F3F8C6D2125717ECE9C9D7E16FB9F09DE8` |
| 启动参数 | -I -S -B |
| Bootstrap UTF-8 SHA-256 | `3E54951F09B53577FA5B4965424910ED7FE267D68A71D59A443FB5001209EAD7` |
| 批次逻辑计时观察 | 2019 ms |
| 九次 wrapper 退出码 / stderr 字节 | 全部 0 / 0 |
| 两个依赖槽位清理 | 九次均 OWNED_ENTRY_REMOVED，合计 18 个槽位 |
| BatchError | null |
| 完整观察记录字节 | 86749 |
| 完整观察记录 SHA-256 | `8EA53E225CC46A889006E0ECF5A732266FE0391AD951CAE8045F8E22E6DD6D2E` |
| 完整记录 gzip 字节 | 22512 |
| 物理原绑定源码修改 | 0 |

九次原始 stdout / stderr 分别保留 gzip、SHA、字节数及 parsed Record；完整父记录也以独立 gzip / SHA / 长度封装。九次每项输入角色、长度和 SHA 与预声明 CaseSpecification 一致。每个进程只装载对应四个固定内存快照，两个固定依赖名称由当前子进程独占注册，再核对所有权并移除。

复核时从观察归档解压完整记录，逐份重算九次原始 stdout / stderr 的 SHA 和字节数，严格 UTF-8 解码及 JSON 重复键检查，比对 parsed Record。对八份变异快照重新执行**字节替换重建**并与 gzip 解压字节逐字比较，不运行变异源码。原版 ValidatorResult 与上一轮 Result 全项对比一致，106 个检查 ID 唯一；未用 CheckCount 摘要替代实际检查清单。

## 5. 本轮证明什么、不证明什么

本轮证明既有验证器对表中八个具体保护移除/限定语漂移敏感；不能据此推断任意错误覆盖率、普遍健壮性、独立安全保证或业务完成比例。没有计算一般 mutation score，也不把 106 个原版检查与 8 个负例相加报告项目完成度。

全文与条目聚合一致仍仅是 DATA CONSISTENCY；调用方可以同步改写正文和 detached 数据并重算 SHA，不能因此建立可信来源或授权。下列缺口继续保留：

- B-01：可信准备根、事前准备权限和角色绑定未由本轮建立。
- B-02：正式完整 typed contract、全数组政策来源及其批准、detached 权威绑定仍未建立。
- 私有快照控制端不是生产装载器；固定 SHA 只提供本轮数据身份，不是接受或来源准入。
- -I -S -B 不是 OS 沙箱，继承环境精简仍依赖既有 OS、解释器与本地控制端。
- 缓存槽位删除不等于所有对象销毁、内存抹除或并发原子冻结。
- 输出大小在收集后检查；5000 / 30000 / 5000 ms 等待与 60000 ms 批次逻辑上限不证明在线内存硬限制、整机物理硬停止或任意子孙进程清理。
- 未覆盖真实故障、实际来源字节、真实业务捕获、集成或部署。

## 6. 交付复核与状态

本轮为本地执行与静态交付核对，不是独立审查员或 Gemini 外审；未调用第三方模型，未生成正式隐私/安全/法律总体结论。计划与控制端在 Python 执行前固定；没有通过改写原测试、改写预设断言或改变原源码来使负例符合预期。

新增文本检查严格 UTF-8、LF、末尾换行、尾空白、表格列数；常见私钥/API-token 模式扫描覆盖新增文本及解码观察/内存快照。无命中是有限模式筛查，不是普遍无敏感内容保证。首次批次运行即得到上述结果，无自动重试或失败抹除。

| 后续项目 | 状态 |
| --- | --- |
| 双层一致性候选接受 | 未发生 |
| DSP-004 | OPEN / HOLD |
| B-01 / B-02 | OPEN / OPEN |
| 正式 Manifest / 来源准入 | NOT CREATED / NOT AUTHORIZED |
| 实际捕获 / 业务集成 / 部署 | NOT AUTHORIZED |
| 既有全部 LIMITED 与历史失败 | RETAINED |
| Git 备份效力 | 仅本项目阶段备份，不构成接受或下游授权 |

本轮有限测试有效性补强完成；需要可信来源、正式合同或接受决定时，仍须相应的独立治理输入，不从本测试结果自动升级。
