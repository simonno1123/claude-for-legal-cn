# DSP-004 异常保留表示与任务观察局部验证计划 REV1

## 1. 范围与不变边界

按 Project Owner 已授权的后续仅本地合成批次及本轮“继续”，仅新增本批测试入口、计划、观察归档和结果说明。不修改已接受文件或历史结果，不涉及独立 ACOS 或其他项目。

本批直接在内存构造固定源码的内部 StageState，调用 KeepPrimary／KeepSecondary，观察 StageObservation 的选定元数据投影；另调用私有 ObserveTaskFailure 检查固定原生 Task 场景。它是表示与方法单元验证，**不是实际 RunStage 清理操作失败的验证**。

不调用公开组合批次、RunStage 或 ReadBounded，不启动 child 阶段、不接入真实流或材料。所有 LIMITED 保留；DSP-004 为 OPEN / HOLD，B-01、B-02 为 OPEN。不接受正式 WP-008 结果，不准入来源、不真实捕获、不集成或部署。

## 2. 固定身份与执行方式

| 角色 | 路径 | SHA-256 | bytes |
| --- | --- | --- | --- |
| 已有限接受受测源码 | validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_SUPERVISOR_CANDIDATE_REV2.cs | 9B165A04AFE786224965C5E33364140265FF3CB0B4B99A8E63A7AE7562C33E4E | 24173 |
| 本批新测试入口 | validation/route_b_c03/wp_008/DSP_004_EXCEPTION_RETENTION_REPRESENTATION_VALIDATION_REV1.ps1 | ADF9F458E629684B44DA3DABD77D9FE496A0E9AEF9D7C39D94EAF9B462386462 | 16586 |

使用已有固定 PowerShell 运行文件，SHA-256 为 362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139，路径为 C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe。不安装或更新运行环境。

在新的固定测试进程内将同份受测 C# 编译到内存，只反射指定构造器、字段及方法。对外公开 API 和固定受测源码均不改写；没有新的业务参数或生产接入通道。

内部状态的 entry 元数据以固定合成标记的实际 SHA 赋值，不代表真实 stage 资产身份或来源准入；选定投影不输出该元数据。测试异常消息使用固定私有哨兵，不从真实内容取值。

入口明确 UTF-8 输出；外侧以原始字节接收后严格解码，同时保留原始 stdout 与 LF 规范化记录及其身份。外侧等待 30000 ms 仅为本批采集边界，不改变受测监督器预算或宣称硬停止保证。

## 3. 运行前冻结的预期

| ID | 场景 | 预期 |
| --- | --- | --- |
| ER-001 | 空异常状态 | primary=null，secondary=0 |
| ER-002 | 只有原始 IOException | 原生引用与阶段不变，投影显示外层类型 |
| ER-003 | 只有 INPUT_CLOSE IOException | primary 仍为 null，secondary=1，不冒充 transport pass |
| ER-004 | 原始 IOException + INPUT_CLOSE InvalidOperationException | 两条原始引用分别保留 |
| ER-005 | 原始 IOException + 三个不同阶段／类型次级异常 | 次级数量 3，引用及添加顺序保留 |
| ER-006 | 同一 IOException 引用以两个阶段重复加入 | 记录 2 条，不自动去重 |
| ER-007 | 原始及次级 AggregateException | 外层类型、原始引用保持，不隐式扁平化 |
| ER-008 | 先建立观察对象，再追加次级异常 | 同一观察对象的计数从 0 变 1；是动态视图，不是冻结快照 |
| ER-009 | 已完成 Task | 方法正常返回 null，不改变任务状态 |
| ER-010 | IOException 故障 Task | 抛出原始 IOException 实例，任务仍 Faulted |
| ER-011 | 预取消 Task | TaskCanceledException，原取消 token 绑定，任务仍 Canceled |
| ER-012 | 尚未完成 Task | 方法立即返回，不擅自完成任务；之后仅由测试创建者完成它 |
| ER-013 | AggregateException 故障 Task | 抛出原始外层 AggregateException，不降为 inner IOException |

8 个状态场景只验证内存表示。default TransportOnlyPass=false 不能被解释为运行过实际 transport 判定。ER-008 的只读属性限制不等于 backing state 不可变化。

异常捕获辅助函数仅移除 PowerShell RuntimeException 和反射 TargetInvocationException 包装；禁止 GetBaseException 或 flatten 破坏 ER-013 原始 AggregateException 身份。原始引用比较只限本测试进程，归档仅保存布尔结果及类型／阶段字符串。

选定投影仅包含 FailureType、FailurePhase、SecondaryFailureCount、SecondaryFailureStagesAndTypes、TransportOnlyPass、FailureRetentionQualification。哨兵检查只针对该投影，不扩张为所有属性、日志或一般脱敏证明。

## 4. 预期检查数

| 检查组 | 数量 |
| --- | --- |
| 固定源码／运行文件身份、保留方法形状、观察属性形状、Task 方法签名 | 5 |
| 8×6 项状态原生引用／顺序、投影、消息边界及默认标记 | 48 |
| ER-008 动态视图专项 | 1 |
| 5×3 项 Task 方法判定、状态未变及 void 返回边界 | 15 |
| 2 项故障 Task 原生异常身份 | 2 |
| 取消 token、待完成任务创建者收尾、Aggregate 外层保留各 1 项 | 3 |
| 后置场景数、受测源码未变、检查总数 | 3 |
| 合计 | 77 |

原生异常对象只保留在该测试进程内，不写入 JSON，也不声称跨进程保留。待完成 Task 场景由测试入口在观察后完成，不将其说成被受测方法收敛。

## 5. 保护集合与结果留存

43 份既有文件在运行前后核对长度与完整 SHA-256。先核对五个锚点文档，再读取其限定身份表；表格共 38 份文件加五个文档，禁止重复路径或越界。

| 锚点文档 | SHA-256 | bytes | 身份表文件数 |
| --- | --- | --- | --- |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_LOCAL_COMPOSITION_REV2_RESULT.md | C44D9C96C4F6E2D74CE9EC0F0019BEC07F1D541F0E916EC184ECEB0BED8DEE8A | 12221 | 19 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_REV2_STAGE_TRANSPORT_FAULT_REV1_RESULT.md | 33A920C3D3F8550F4B4CA3B2F1AC1CC0D9476F704A18E143B2D7BA51DE3BC53C | 10158 | 3 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_CLOSED_RECORD_JSON_REV1_RESULT.md | 8522AC8662C0617EB92CE1A3F65D7A9255AEFB998E4ED8DEB842B88B6911E203 | 8849 | 3 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_JSON_GATE_CONVERSION_BOUNDARY_REV1_RESULT.md | D175EF4828094A5ED4C729987EEC92C642EE711FAE58C2CE98F5F14AFF2E19CC | 12980 | 9 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_BOUNDED_READ_BOUNDARY_REV1_RESULT.md | 9B47CA2BEC57B30B4BD34EDF25E7E5A8D552048F203516158BCFD4B7EC65E611 | 10338 | 4 |

这些文件包含已接受源码、历史失败及测试说明，不意味着它们均获得同一种治理接受。不改写历史 PENDING、未覆盖或失败记录。

接收侧另行解压核对两份 stdout 归档、散列、确定的换行规范化关系、Summary、13 个有序场景和 77 个唯一检查。复核由主协调员执行，不冒充独立代理或 Gemini。

意外失败时先保留入口及失败观察，不默改预期或受测源码。备份仅处理本批新增的本项目公开适宜合成文件，核对秘密特征、格式、固定身份和远端 main 后普通提交／推送；备份不等于治理接受。

## 6. 明确保留的缺口

没有令 Kill、Wait、Close 或 Dispose 实际失败，没有验证这些失败与真实原始错误在 RunStage 里的组合控制流。不证明资源全部收敛、外侧强停止、取消竞态或真实异步调度。

未验证重复调用 KeepPrimary 的语义，不把本批有限引用检查推广为不可变记录、全局首因锁定、完整脱敏或审计持久化。

不复跑原 189 项或上一批边界场景，不触发来源准入、真实捕获、业务集成、部署、正式阶段接受或任何下游自动转换。
