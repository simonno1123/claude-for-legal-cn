# DSP-004 异常保留表示与任务观察局部验证 REV1 — 实际结果与范围

## 1. 本批结论

实际结果为 **LOCAL_EXCEPTION_REPRESENTATION_AND_TASK_OBSERVER_CHECKS_PASS**：13 个封闭合成场景、77 个唯一检查全部符合预置预期，失败检查为 0。测试入口退出码 0、stderr 0 bytes，严格 UTF-8／JSON 接收错误为 null。

8 个场景只检查内部异常状态的表示，5 个场景只调用私有 Task 错误观察方法。没有令实际 Kill、Wait、Close 或 Dispose 失败，没有验证真实清理故障与原始失败在 RunStage 中的组合控制流。

确认两个不能省略的限定：

- get-only 观察属性不等于不可变冻结快照：同一观察对象会反映测试侧后来追加的内部次级异常。
- 待完成 Task 的错误观察方法正常返回，不等于 Task 已完成或资源已收敛；本批随后仅由测试创建者完成该合成 Task。

DSP-004 保持 OPEN / HOLD，B-01、B-02 保持 OPEN，全部 LIMITED 与历史失败保留。不接受正式 WP-008 结果，不准入来源、不实际捕获、不业务集成或部署。

## 2. 固定身份与新增资产

受测源码为 validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_SUPERVISOR_CANDIDATE_REV2.cs，24173 bytes，SHA-256 为 9B165A04AFE786224965C5E33364140265FF3CB0B4B99A8E63A7AE7562C33E4E。该文件未修改。

使用已有固定 PowerShell，SHA-256 为 362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139，完整路径见计划。未安装或更新运行环境。

本批新增四份资产，包括本结果文档。路径相对本项目根目录；本结果文档不在自身正文中自绑定散列。

| 新资产 | SHA-256 | bytes |
| --- | --- | --- |
| validation/route_b_c03/wp_008/DSP_004_EXCEPTION_RETENTION_REPRESENTATION_VALIDATION_REV1.ps1 | ADF9F458E629684B44DA3DABD77D9FE496A0E9AEF9D7C39D94EAF9B462386462 | 16586 |
| validation/route_b_c03/wp_008/DSP_004_EXCEPTION_RETENTION_REPRESENTATION_REV1_OBSERVED_RESULT.json | 2E0D13BEED92826DA17957D897499B6E04D3EAB7E31BDAEE9F46AB713BB397A0 | 7304 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_EXCEPTION_RETENTION_REPRESENTATION_PLAN_REV1.md | B9A2D032BE744A50033BEFB06C6D9890F0B0E03189A54F4D4EC892C72FD49E47 | 7718 |

本批新入口与观察不因测试通过而自动获得治理接受，也不替代已接受源码的后续审查。

## 3. 实际调用范围

在新的固定测试进程内将相同受测 C# 编译到内存，只调用 StageState 的构造器、KeepPrimary、KeepSecondary、StageObservation 构造器／选定只读属性，以及私有 ObserveTaskFailure(Task)。

没有调用 RunStage、ReadBounded、公开组合批次、控制端、真实 Driver 或任何 child 阶段。内部状态用固定合成标记的散列作测试元数据，不代表真实 stage 资产身份、来源或权限。

异常实例均为固定合成值。原生引用仅保留和比较于本测试进程，归档只输出类型、阶段、计数及布尔比较，不序列化 Exception 对象、Message 或 StackTrace。Task 捕获辅助函数只去掉 PowerShell／反射包装，不调用 GetBaseException 或 flatten，避免改变原始 AggregateException 外层身份。

## 4. 内部异常状态表示的实际观察

NONE 表示 null，不是一次真实运行没有故障的证明。

| ID | primary 外层类型 | primary 阶段 | secondary 条数 | primary 引用／secondary 引用及顺序相同 |
| --- | --- | --- | --- | --- |
| ER-001 | NONE | NONE | 0 | true / true |
| ER-002 | System.IO.IOException | PRIMARY_READ | 0 | true / true |
| ER-003 | NONE | NONE | 1 | true / true |
| ER-004 | System.IO.IOException | PRIMARY_READ | 1 | true / true |
| ER-005 | System.IO.IOException | PRIMARY_READ | 3 | true / true |
| ER-006 | System.IO.IOException | PRIMARY_READ | 2 | true / true |
| ER-007 | System.AggregateException | PRIMARY_AGGREGATE | 1 | true / true |
| ER-008 | System.IO.IOException | PRIMARY_READ | 1 | true / true |

逐项限定：

- ER-001：默认空模型，无 primary／secondary。
- ER-002：保留原始 IOException 对象及 PRIMARY_READ 阶段。
- ER-003：只有 INPUT_CLOSE 次级 IOException，primary 仍为 null；没有把次级错误提升或伪装成 primary。
- ER-004：原始 IOException 与 INPUT_CLOSE InvalidOperationException 分别保留。
- ER-005：KILL_REQUEST、EXIT_WAIT、OUTPUT_CLOSE 三个次级阶段按加入顺序保留，其类型依次为 InvalidOperationException、TimeoutException、IOException。
- ER-006：同一 IOException 实例以 INPUT_CLOSE 与 PROCESS_DISPOSE 两个阶段加入，记录为两条，不自动去重。
- ER-007：原始与次级 AggregateException 保留外层类型；本批不以内部 IOException 代替它们。
- ER-008：先构造观察对象，次级计数为 0；测试侧直接调用内部方法追加后，同一观察对象计数变为 1。之前复制的选定投影保留 0，之后投影显示 1。

8 个选定投影的 TransportOnlyPass 均为默认 false。这只是手工构造模型的默认标记，不能说成实际 transport 验证、拒绝路径或资源清理已经执行。

ER-008 使用测试侧的内部反射访问，不表示普通公开调用者获得修改内部状态的权限，也不是自动认定的产品漏洞。结论仅是“只读属性”不能单独证明 backing state 被冻结。

每项选定投影包含 FailureType、FailurePhase、SecondaryFailureCount、SecondaryFailureStagesAndTypes、TransportOnlyPass、FailureRetentionQualification。私有消息哨兵在这些投影中均未出现；接收侧也未在完整观察文本中找到哨兵。该事实不等于全部属性、日志、所有异常内容或一般脱敏安全证明。

## 5. 私有 Task 观察的实际结果

| ID | 调用前状态 | 方法结果 | 抛出异常外层类型 | 方法返回／抛出后状态 | 测试创建者收尾后的状态 |
| --- | --- | --- | --- | --- | --- |
| ER-009 | RanToCompletion | RETURN | NONE | RanToCompletion | RanToCompletion |
| ER-010 | Faulted | THROW | System.IO.IOException | Faulted | Faulted |
| ER-011 | Canceled | THROW | System.Threading.Tasks.TaskCanceledException | Canceled | Canceled |
| ER-012 | WaitingForActivation | RETURN | NONE | WaitingForActivation | RanToCompletion |
| ER-013 | Faulted | THROW | System.AggregateException | Faulted | Faulted |

- ER-009：已完成任务的方法正常返回 null，不产生新结果或状态变化。
- ER-010：抛出原始 System.IO.IOException 实例，ReferenceEquals=true，任务仍为 Faulted。
- ER-011：抛出 System.Threading.Tasks.TaskCanceledException，取消 token 与构造该任务时的原 token 相同，任务仍为 Canceled。
- ER-012：任务在方法返回后仍为 WaitingForActivation；之后由测试创建者 TrySetResult，才变为 RanToCompletion。不是受测方法完成了它。
- ER-013：抛出原始 System.AggregateException 实例，ReferenceEquals=true；保留一个 IOException inner，不把 outer 变成 inner。

故障／取消场景各移除了一层实际反射包装；未对原始 AggregateException 执行扁平化。该观察只覆盖表列原生 Task，不覆盖真实异步调度、取消竞态、线程停止或等待／清理过程。

## 6. 检查数量与完整观察身份

| 检查组 | 实际数量 |
| --- | --- |
| 固定身份与方法／属性形状 | 5 |
| 8×6 项异常状态、投影与边界检查 | 48 |
| 动态视图专项 | 1 |
| 5×3 项 Task 方法判定、状态不变、void 返回 | 15 |
| 故障 Task 原生异常引用 | 2 |
| 取消 token、创建者收尾、Aggregate 外层保留 | 3 |
| 后置场景数、受测源码未变、检查总数 | 3 |
| 合计 | 77 |

77 项均为 true；13 个有序场景 ID、77 个检查 ID 均完整且唯一。检查数不等于独立场景数，也不与前批计数合并为正式覆盖率。

| 观察身份 | 实际值 |
| --- | --- |
| 原始 stdout bytes | 19417 |
| 原始 stdout SHA-256 | F7F205728BBFFC22702F8DED2AAA5DC96D60DF013161244A2763B7028A473ACD |
| 原始 stdout gzip bytes | 2244 |
| LF 规范化完整记录 UTF-8 bytes | 18809 |
| LF 规范化完整记录 SHA-256 | 7F344983F8DCC104C5658D651B065AEDC6CE405B8E2ED37F1F61F7E17ACD32C6 |
| 规范化记录 gzip bytes | 2230 |
| 入口退出码／stderr bytes | 0 / 0 |
| 外侧采集等待预算／实际观察 ms | 30000 / 2288 |
| 外侧等待触发 | false |

2288 ms 包括测试进程启动、编译、执行、输出接收与本地 Dispose 观察，不是方法性能基准或硬时限保证。该采集预算不改变原监督器的 120000 ms 策略。

归档同时留存原始 stdout 字节与按 LF 规范化的完整结构化记录，不只有摘要。原始输出严格 UTF-8 解码、CRLF 换为 LF并补最终 LF后，精确得到规范化记录。

## 7. 接收复核与文件保护

主协调员另行执行接收侧只读复核，不冒充独立代理或第三方模型：

- 核对两份 gzip 长度、解压长度、完整 SHA-256 和原始到规范化文本的确定关系；拒绝重复 JSON 键。
- 比较完整记录与 Summary，逐项核对 13 个场景、77 个唯一检查、原生引用布尔值、阶段顺序、选定投影及 Task 判定。
- 独立检查 ER-008 的 0→1 观察边界、待完成任务创建者收尾、取消 token 和 Aggregate 外层身份记录。
- 运行前后核对 43 份既有文件的长度及 SHA-256，全部相同；集合由计划中五个固定结果文档和身份表绑定，不表示这些文件均获得同一种接受。
- 新入口静态解析错误为 0；新增文件按严格 UTF-8、最终 LF、尾随空白及常见秘密特征检查。未命中特征不等于一般秘密泄露证明。
- 备份仅包括本批四份新增项目内合成资产，普通提交／推送不等于治理接受或下游授权。

## 8. 未覆盖与继续保留

本批不覆盖实际清理异常注入、RunStage 组合控制流、完整后代／任务资源收敛、外侧强停止、冻结快照实现、重复 KeepPrimary 的覆盖语义、完整脱敏或跨进程原生异常保留。

没有复跑原 189 项、先前局部验证或正式 WP-008。没有来源准入、实际捕获、业务集成、部署，也未访问独立 ACOS 或其他项目。

本批通过不关闭 DSP-004、B-01、B-02 或任何 LIMITED，不接受正式结果，不自动触发任何后续阶段。
