# Route B C03 WP-008 — 可信导入边界与具体输入绑定有限设计修订提案

## 1. 文件性质与本轮边界

| 项目 | 记录 |
| --- | --- |
| 所属项目 | `claude-for-legal-cn` |
| 工作范围 | Route B C03 WP-008；`CAPABILITY_ONLY` |
| 用户本轮授权 | “授权先提出仅涉及‘可信导入边界与具体输入绑定’的有限设计修订” |
| 唯一新产物 | 本提案 Markdown |
| 提案状态 | `PROPOSED — NOT REVIEWED / NOT ADOPTED / NON-OPERATIVE` |
| 两个修订主题 | 可信导入边界；具体输入绑定 |
| 当前源码物化 | 因下述设计冲突暂停；本提案不恢复物化授权的执行 |
| 执行证据 | 本文仅依据文件内容与本地散列核对；未启动 Python、导入 subject 或运行验证 |

本提案不替代、修改或追溯补正任何已接受文件、审查报告或决策。
既有 Grade A 记录予以保留，但未覆盖本次发现的可实现性冲突，不能据此证明
harness 已可实现、运行前置条件已满足或十五项场景已经通过。

本轮不创建 harness、输入绑定包、运行依赖清单、网络隔离凭证或运行证据。
不修改十个 subject、十五个 fixture、Python 环境或项目治理台账；不开展正式
Design Review、外部审查、Route A/OCR/案件处理、真实 Provider 调用、Git 操作。
不访问或变更独立 ACOS 项目。本仓库 `.codex-coordination/` 中既有记录仅作本项目的来源。

## 2. 固定来源与记录保全

下列 SHA-256 为本轮读取具体文件后的本地核对值。散列核对仅证明所读文件字节身份，
不独立证明历史决策主体、授权时序或运行行为。所有散列使用完整 64 位十六进制值。

| ID | 本项目来源路径 | SHA-256 |
| --- | --- | --- |
| B01 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_OPERATIONAL_VALIDATION_PLAN.md` | `E9643D0993532A1E1603B66F95CD288F394BDDA621EFB6784B256CECFC915E6D` |
| B02 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V2.md` | `5265D6D422D8BC101107E81B71AFEB485DDDE300A959B3692DA944AE18829BE5` |
| B03 | `.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V2_INTERNAL_REVIEW.md` | `A652ABCA2DCFAC9BBEB5074860D7F7457CE353BB95A858F4BEDF30FD5B52E299` |
| B04 | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V2_ADOPTION_DECISION.md` | `9CB805082CF7D635F21605A68622A7CB9F495599B1B95B18EDD09E464BAB6560` |
| B05 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN.md` | `8C23436CD6CD7ADE9FFC30C44241D1D944A203AC00F0605B366B9F1658BBC239` |
| B06 | `.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVIEW.md` | `64AFB34D60B3C1C7FAD798AD2C226128C87D8C15BE33A4DA90E20F8149B85AEA` |
| B07 | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_ADOPTION_DECISION.md` | `20E513434365134800AE0A06C2F1DA09A861404ACE8412B62A064B3E6684BCEA` |
| B08 | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_WP_008_FUTURE_HARNESS_SOURCE_MATERIALIZATION_AUTHORIZATION.md` | `081624BE31AB69443DAF5C51FD169CEB8BC20577E22F107A48839FC06DC64B8B` |
| B09 | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_PREPARATION_ACCEPTANCE_AND_FIXTURE_ADMISSION_DECISION.md` | `0AA106618E545DF41B267EAD0CC4F28E7D15578728F123E4C5EBD7D81C967835` |
| B10 | `validation/route_b_c03/wp_008/ENVIRONMENT_MANIFEST.md` | `EFCF1A783199F58387BDBB0704563ED943A5E6A3E319A04CE6D58E57FC5CA531` |

十个 subject 和十五个 fixture 的本轮身份列于附录。B08 不因本提案被自动修改、
扩大、重新签发或宣告耗尽；其恢复使用是否需要替代授权，应由 Project Owner
在新设计来源明确后单独处置，不能把旧固定 SHA 授权自动迁移至新设计。

## 3. 两项设计冲突及证据边界

### 3.1 TI-01：导入所需的受控代码生成与无差别禁止动态执行冲突

- B02 第 6.2 节第 174–177 行禁止 `eval`、`exec`、`compile`、`__import__`、动态加载及保护控制改写。
- B02 第 6.3 节第 189–195 行要求在 subject 导入前，对动态代码及 package 事件执行终止性拒绝，未区分已接受的正常导入与任意代码加载。
- `scripts/phase2_runtime/route_b_c03/contracts.py` 第 5 行导入 `dataclass`，并在第 106 行起使用装饰器；`capability.py`、`failures.py`、`provider_port.py` 也使用 dataclass。
- 本地 CPython 标准库 `dataclasses.py` 的 `_create_fn` 在第 449–474 行构造方法，其中第 473 行明确调用 `exec(txt, globals, ns)`。

所读运行依赖文件为：

`C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/Lib/dataclasses.py`

SHA-256：`D242AEA5FCF6408B1C1F622442F88F68B9526CE1F8BD2890D74A144677C427D9`。

这证明当前文本存在必须解释清楚的导入边界冲突，不是一次实际导入失败记录。
正常源码导入也需要解释器编译、执行模块；AST 解析与执行任意输入代码不能仅按事件名称等同。
不得通过先无保护地导入全部 subject、随后安装审计 hook 来掩盖该冲突。

### 3.2 IB-01：场景描述未形成具体可调用输入

十五个 fixture 的 `input_state` 主要为状态标签，不是现有函数签名所要求的完整参数。
例如 V-001 仅给出 `VALID_SYNTHETIC_METADATA` 与 packet 不存在；
`evaluate_identity_gate` 仍需要 configuration、envelope、expected、validity、kill 等参数。
V-007 缺少完整重试策略及次数/截止条件；V-008 的 clock identity 明确仍为未来绑定项。

此外，fixture 的期望类别不一定等于 subject 的原始返回值。
例如 V-013 期望不可用类别，但 `NullProviderPort` 返回的是 Provider 未授权拒绝；
二者不能由 harness 在结果出来后自行改写成“相同”。

上述差距要求输入绑定及可观察范围澄清，不授权补造时钟、幂等存储、回滚引擎、
完整性检测器或新 subject 行为。对既有接口的静态观察不构成十五项正式验证结果。

另有与输入可达性直接相关的限制：`identity_gate.py` 第 100–108 行的最后一组
授权引用比较位于第 96–99 行无条件返回之后。输入绑定不能使这组比较变为可达，
也不能通过避开它而证明完整授权检查。本提案仅登记这一静态限制，不修复代码，
不将其另行纳入已获准的修改范围；需要代码改变时必须单独取得授权。

## 4. 提议修订 A：可信导入边界

以下条款均为待审议设计，尚未成为新的执行规则。

### 4.1 正常导入与任意动态执行分离

| 编号 | 拟采用规则 |
| --- | --- |
| TI-001 | harness 与 subject 源码继续禁止任意 `eval`、`exec`、动态模块名、用户可控加载器、路径发现及未登记依赖；不增加通用动态执行接口。 |
| TI-002 | 正常字面量导入必须同时绑定模块名、规范路径、文件 SHA、loader 类别、来源父模块及导入阶段；built-in/frozen 模块绑定精确解释器身份与其类别，不能以缺少文件为由任意放行。 |
| TI-003 | 静态 AST 解析只针对已绑定的 harness/subject 文本；只生成语法树，不执行解析对象。解释器为解析或正常导入产生的事件须与任意代码输入分开判定。 |
| TI-004 | `dataclasses` 内部方法生成只能作为精确来源的窄例外候选：固定标准库 SHA、已审查的内部调用路径、已绑定类声明及字段定义、受控生成内容与命名空间、限定导入阶段。 |
| TI-005 | 不能仅凭模块名称、路径前缀、调用栈文本、`co_filename`、`<string>` 或事件名授予例外；这些标记不能单独证明代码来源。未能建立来源证据则阻断。 |
| TI-006 | fixture、输入绑定数据、CLI 或环境输入不得控制模块名、源码片段、字段定义、默认工厂、注解表达式或生成命名空间。受控生成代码不能来自运行中的场景数据。 |
| TI-007 | 未列明的标准库动态行为不得顺带放行。递归依赖需要同样的精确归因；无法静态界定的路径保持阻断，而不是扩大到整个 Lib、site-packages 或目录。 |
| TI-008 | 所有阶段继续禁止网络、子进程、任意文件访问及权限扩展；可信导入例外只解释必要导入/生成行为，不增加上述能力。 |

TI-004 尚不是“例外机制已可可靠实现”的证明。未来源码设计必须说明哪些事件参数和
来源证据足以约束生成内容，以及哪些保证必须由进程外可信环境提供；若仅能依赖可伪造标记，
该路径不能获准。不得为了完成本提案而修改标准库或 subject。

### 4.2 分阶段建立信任，不反向声称启动已受 hook 保护

| 阶段 | 拟议边界 | 缺失时的处置 |
| --- | --- | --- |
| T0 — 环境与启动身份 | Python 启动前依赖已绑定的环境隔离、文件完整性和启动读集验证；涵盖解释器、配置、loader/bootstrap 依赖。不能由尚未启动的 Python hook 自证。 | 无对应可核实来源或文件替换防护时阻断；本轮不建设该环境。 |
| T1 — 最小可信 bootstrap | 仅允许提前列明的启动/保护初始化依赖；安装保护所需导入也属于受约束读集；不得预先导入 subject。 | 未登记导入、未绑定 loader 或保护初始化失败时停止。 |
| T2 — preflight | 用已绑定工具链核对固定文件和输入来源，进行文本/AST 检查并确认保护策略；不执行场景，不写运行证据目录。 | 身份、来源、输入或策略缺失时停止，不能进入 T3。 |
| T3 — 受控 subject 导入 | 导入十个固定 subject；允许的正常模块执行及 dataclass 生成只能落在 TI-002 至 TI-007 的精确例外中。 | 意外导入、代码生成或来源不清时停止，场景仍为 NOT RUN。 |
| T4 — 场景调用 | 仅调用已接受输入绑定指定的现有入口；不做按数据动态导入，不在场景阶段生成新类/代码。 | 出现未批准的延迟导入或动态行为即停止，不能临时扩张白名单。 |

原有 `-I -S -B`、字节码写入禁止、无网络和精确读写集要求保留。
“before import”应在后续有限修订中明确为哪些启动依赖、哪些 subject 导入；
不能要求 Python 在任何自身依赖加载前完成依赖检查，形成不可执行的循环。

Python audit hook 与 socket 拒绝包装仅是进程内辅助防线，不能单独宣称形成
防恶意代码或防篡改沙箱。原有环境层隔离不能被其替代；关于保护不可被改写的保证，
必须明确环境侧依据和残余限制，不能只写“prevent”即视为实现。

### 4.3 与运行依赖 Manifest 的衔接

B05 的静态依赖解析仍不允许导入或执行 subject。拟增加导入阶段、loader 来源、
正常模块执行依据、精确内部生成例外及其验证限制的记录要求。
不得把“必须解析依赖”变成当前启动 Python 或探测依赖的授权。

拟议顺序为：先审议有限设计修订及输入绑定要求，再在明确授权下形成并接受
输入绑定与 harness 源码，最后按独立授权生成和审查运行依赖 Manifest。
输入绑定不能依赖尚未生成的 Manifest；Manifest 可绑定已经接受的输入和源码，
最终执行授权再固定全部 SHA，避免相互自引用。

## 5. 提议修订 B：具体输入绑定

### 5.1 保留 fixture，另行绑定具体刺激输入

原十五个 fixture 及 B09 保持原字节和原身份。其准入不自动等于所有缺失参数的准入。
拟在后续获得明确授权时形成单一、版本化的 Scenario Input Binding 产物；
本提案仅规定所需内容，不创建该产物、JSON Schema 或可执行参数实例。

| 绑定项 | 必需内容与限制 |
| --- | --- |
| 对象身份 | 原 scenario ID、fixture 路径/SHA、subject 路径/SHA、精确函数或构造器名；不使用 wildcard 或按输入选择任意函数。 |
| 完整参数 | 每个必需参数的类型、具体值或明确空值；默认值若被采用也须明示。不得保留 `VALID_SYNTHETIC_METADATA` 等需要现场解释的标签。 |
| 正常前置值 | 明确到达被测分支所需的其他参数；不能因默认 DISABLED 提前阻断而声称验证了缺失 Tier B packet 等更深分支。 |
| 失败刺激 | 指定实际缺失/错配的字段及调用序列；多重边界须逐项绑定，不能只触发第一条拒绝即声称其余边界均覆盖。 |
| 合成数据性质 | 仅使用非真实、无内容、无路径的元数据；合成授权/身份标签只是测试数据，不构成真实 Tier B、案件或执行授权。 |
| 确定性政策 | 如适用，固定策略版本与身份、次数、范围、deadline/validity 布尔参数的来源。缺失时不得从期望结果反推。 |
| 时间与控制边界 | 模拟时间/状态须明确为输入，不是系统实测时间或真实撤销凭证；调用方给定 `deadline_valid` 不能证明 subject 自行检测了超时。 |
| 调用可观察面 | 分别指定构造器异常、函数返回值、纯元数据拒绝、实际外部副作用等观察层；只计入现有入口确实可观察的层。 |
| 结果对照规则 | 预先绑定期望类别与原始返回值/异常的比较规则及限制；不得在看到运行结果后选择等价映射。无依据的差异保留为不匹配。 |
| 隔离与串联 | 每场景初始化与清理设计明确；V-006 的重复关系单独绑定；不借 harness 状态模拟 subject 没有的功能。 |
| 证据来源 | 清楚区分原 fixture 值、后来经接受的合成输入、subject 原始输出和比较结果。任何输入绑定都不能填造 observed 值。 |

“固定合成值”不等于将任意字符串称为已验证 SHA：用于真实资产的散列必须对应真实固定字节；
仅作错配刺激的合成散列须标明合成身份，不得充当基线校验结果。

### 5.2 期望、观察与比较不得互相替代

1. 刺激输入由已接受的具体输入绑定提供；原 fixture 的 expected 字段只用于比较，不驱动返回值选择。
2. observed 必须保留 subject 实际返回的枚举、原始原因或异常类型，不把 Plan 的分类直接写入 observed。
3. `build_failure_record` 按传入原因构造记录，不会证明该原因真实发生。手动传入 `quarantined=True` 不是检测到篡改的证据。
4. `protected_state` 对给定布尔标记的选择，只能证明该选择函数的行为，不能证明运行系统检测到了 kill/revocation/stale。
5. 纯函数检查命名空间不等于操作系统拒绝了一次实际写入；不得为观察拒绝而试写独立 ACOS、上游或案件文件。
6. subject 禁止副作用的观察与未来 harness 自身四类证据输出分开记录；不能把 fixture 的空写集当成全进程“无写入”的实测证明。
7. 未绑定输入为 `BLOCKED — INPUT UNBOUND`；现有入口无法覆盖的要求为 `NOT EVALUABLE`；未获执行授权仍为 `NOT RUN`。这些标签不构成 PASS 或 blocker closure。

### 5.3 十五个原场景的输入与可观察性映射

下表是静态绑定需求分析，不是执行结果。所有行均未运行、未取得新的场景准入。
“部分可观察”不得替换原场景要求；缺少入口或可观察面时，完整场景仍不能判通过。

| 原场景 | 现有候选入口/契约 | 仍需明确的具体输入 | 不能外推的结论 |
| --- | --- | --- | --- |
| C03-TA-V-001 | `evaluate_identity_gate` | configuration、envelope、expected 全字段；`packet=None`；validity、kill；确保到达 packet 检查前的前提逐项明确。 | 提前因 capability 未启用而拒绝，不能证明缺少案件绑定 authority 的分支被覆盖。 |
| C03-TA-V-002 | 身份引用构造器；`evaluate_identity_gate` | 明确哪项身份或授权字段 malformed/缺失，以及预期观察构造器拒绝还是 gate 拒绝；其余参数完整。 | 构造器失败不等于所有授权分支已验证；末尾授权引用比较的可达性限制见第 3.2 节，不能由输入绑定补救。 |
| C03-TA-V-003 | `evaluate_identity_gate` | 版本、implementation SHA、configuration SHA 的逐字段错配值；预期身份；各变体到达目标比较分支的完整前置参数。 | 单传 STALE 状态或比较一个字段不证明三个 exact-identity 比较均工作；不能把实际 BLOCKED 直接改写为 fixture 的 BLOCKED_STALE。 |
| C03-TA-V-004 | `evaluate_identity_gate` 的 matter/actor 等比较 | packet 与 envelope 的具体错配字段；原 fixture 的 matter/project/session/provider 四类边界分别绑定到真实参数与入口。 | 当前入口并未给出四类同名边界的完整参数面；未映射的 project/session/provider 要求为 NOT EVALUABLE，不能以 matter 拒绝覆盖。 |
| C03-TA-V-005 | `assert_reference_only` | 被检查的具体顶层键及无敏感值的占位方式；原 prohibited class 到该键检查的可追溯映射。 | 顶层键拒绝不证明任意值内容、嵌套对象或全部披露通道均受检测；不引入真实 credential/secret/token。 |
| C03-TA-V-006 | `IdempotencyKeyReference` 仅为引用契约 | 两次调用的完整身份和序列；需要明确现有哪个入口观察重复拒绝或副作用计数。 | 固定 subject 中未提供重复存储/判重入口；完整幂等要求当前为 NOT EVALUABLE。不得在 harness 中补建 replay cache 后替 subject 通过。 |
| C03-TA-V-007 | `evaluate_retry` | 完整 `RetryPolicyReference`、`FailureCode.TRANSIENT_FAILURE`、completed attempts、identical scope、deadline valid、kill/revoked/stale/quarantined。 | 只可观察重试资格；不执行重试、backoff、调度或以布尔输入证明实际 deadline 检测。 |
| C03-TA-V-008 | `TimeoutPolicyReference` 仅为引用契约 | 需固定 clock/起点/deadline/迟到处理的来源及实际入口；原 fixture 的 FUTURE_BINDING_REQUIRED 尚未消除。 | 当前未见计时与超时终止执行入口；完整要求为 NOT EVALUABLE，不能用预设 timeout 标记或异常构造替代。 |
| C03-TA-V-009 | `evaluate_identity_gate`；`protected_state` | 明确 configuration/packet 撤销变体、前置有效参数、模拟控制输入来源；另列边界接收前后的观察需求。 | 可观察给定撤销状态的拒绝/选择，不证明真实撤销接收时点或该时点后的实际无动作。 |
| C03-TA-V-010 | `evaluate_identity_gate`；`protected_state`；`evaluate_release` | kill 输入、release decision 明确空值及两个引用参数；隔离每个入口的前置条件。 | 给定 kill 后的结果或无 release 的拒绝，不等于完整外部 kill switch、不可自解除机制已经运行验证。 |
| C03-TA-V-011 | `RollbackReference` 仅为引用契约 | 明确当前/先前版本的合成引用、无 rollback authority，以及真正的资格判定观察入口。 | 固定 subject 未提供 rollback 资格/执行入口；不能把 `evaluate_release` 或数据构造充作回滚判定，完整要求为 NOT EVALUABLE。 |
| C03-TA-V-012 | `AuditIntegrityReference`；`build_audit_candidate` | 对照摘要、受影响引用、错配来源及检测入口必须明确。 | 记录一个 MISMATCH 或构造 audit candidate 不等于检测并隔离完整性失败；当前完整检测链为 NOT EVALUABLE。 |
| C03-TA-V-013 | `NullProviderPort.submit_reference` | 明确合成 request reference；分别定义 provider 未授权与 dependency 不可用的刺激和观察需求。 | 现有 NullProvider 的 NOT AUTHORIZED 拒绝不能证明不可用故障处理；不移除依赖、替换 Provider 或访问网络制造故障。 |
| C03-TA-V-014 | `assert_permitted_write_set` | 明确被禁止的 namespace 与非空合成引用序列；将不同禁止 namespace 分开绑定，不含实际外部路径。 | 只观察纯元数据拒绝，不实际执行 write/stage/commit/branch/push，也不宣称验证了远端 ACL。 |
| C03-TA-V-015 | `CandidateRecord` 的状态/notice/downstream 约束 | 完整合成候选元数据、具体 candidate class 与欲违反字段；分别绑定构造器检查与分类请求的观察入口。 | 状态/notice 检查不自动覆盖任意非法 class 或真实法律输出；无法映射的分类要求为 NOT EVALUABLE，不执行 legal reasoning。 |

不得删除上述原场景、降低十五项覆盖门槛或将 NOT EVALUABLE 改记为通过。
若消除不可观察项需要 subject 功能、目标范围或验证方法的进一步改变，应记录为
本提案之外的待决事项；本轮既不实施，也不授予此类改变的权限。

## 6. 拟影响条款及明确不变项

| 来源 | 拟议有限变化 | 本轮动作 |
| --- | --- | --- |
| B02 第 5.2、6、7、9 节 | 澄清启动/正常导入/内部生成事件分层；输入绑定作为明确的 preflight 和读集前置条件；未来输入身份绑定方式需与封闭命令一致。 | 只提出；不修改 B02，不新增 CLI 参数或读权限。 |
| B02 第 10 节 | 加入具体输入、原始观察与事前比较规则的区分；保留原十五场景、顺序、停止及禁止 aggregate PASS。 | 只提出；不修改原场景或 raw evidence。 |
| B05 第 2、6、9、10、11、13 节 | 衔接固定输入身份、可信启动及精确导入例外，维持静态解析、不执行 subject 的生成边界。 | 只提出；不生成 Manifest，不变更运行环境。 |
| B01、B09、subject、fixtures | 保留需求、准入记录及固定字节；本提案不能覆盖它们。 | 全部不变。 |
| B03、B04、B06、B07、B08 | 保留既有审查/接受/授权记录；新问题如实追加在本提案，不追溯改写历史。 | 全部不变。 |

精确写集、禁止真实案件及敏感数据、禁止实际 Provider、隔离 ACOS、禁止 Git、
执行者与独立审查者分离、Project Owner 唯一正向决策权全部保留。
本提案没有签发新的执行授权，也没有减少三项运行就绪阻断条件。

## 7. 后续审议检查点（本轮未执行正式审查）

| ID | 提案/后续有限修订应满足的检查点 | 当前审查判定 |
| --- | --- | --- |
| LR-01 | 仅涉及可信导入与具体输入绑定；没有修改 subject 或创建运行产物。 | PENDING REVIEW |
| LR-02 | 启动依赖、AST 解析、正常导入、dataclass 内部生成、任意代码执行相互区分。 | PENDING REVIEW |
| LR-03 | 导入例外固定到文件/解释器身份、来源、内容和阶段；不依赖可伪造标签单独判信任。 | PENDING REVIEW |
| LR-04 | 无保护预导入不能绕过约束；T0/bootstrap 的信任根和未覆盖风险明确。 | PENDING REVIEW |
| LR-05 | audit hook 不被宣称为独立沙箱；网络/环境隔离仍为独立必要条件。 | PENDING REVIEW |
| LR-06 | 原十五份 fixture 不变；所有新增具体输入均要求独立的版本、身份及准入来源。 | PENDING REVIEW |
| LR-07 | 到达目标分支的前置值和各错配变体完整，不能被更早默认拒绝遮蔽。 | PENDING REVIEW |
| LR-08 | 合成身份/时间/授权标签仅为测试输入，不是现实身份或授权证明。 | PENDING REVIEW |
| LR-09 | expected、observed、comparison 分离；实际返回值不被后置归类覆盖。 | PENDING REVIEW |
| LR-10 | 引用构造、标志选择、无副作用检查与完整功能验证严格分开。 | PENDING REVIEW |
| LR-11 | 未绑定/不可观察项不能获 PASS；不借 harness 补建 subject 功能或静默缩小原要求。 | PENDING REVIEW |
| LR-12 | 旧 SHA 与历史决策保留；新设计、源码、输入、Manifest 和执行权限不自动互相继承。 | PENDING REVIEW |

## 8. 后续处置与停止条件

下一步是 Project Owner 处置本提案并在需要时授权对上述两项主题进行有限设计修订，
不是直接启动 harness 物化或 Python 验证。修订后的设计须以新 SHA 单独审查/接受。
具体输入和 harness 来源未明确、可信导入机制不能落到可核实约束、任一原场景仍缺少
满足其原要求的可观察面时，不得宣布执行就绪或关闭相关 blocker。

本提案的完成仅表示设计建议已形成；不表示修订已应用、运行验证已进行、
C03 已通过、项目阶段已结束或下游权限已生效。

## 附录 A. 十个 subject 的本轮只读身份快照

| 路径 | SHA-256 |
| --- | --- |
| `scripts/phase2_runtime/__init__.py` | `49B8B1BD319B6424323AD0EDC04B3969D71196CD8D69E12C16D5442B17340844` |
| `scripts/phase2_runtime/route_b_c03/__init__.py` | `F669613D65267EC5D4D42CB79008EB510307A99B20E40EE13E9E1E0E404A504D` |
| `scripts/phase2_runtime/route_b_c03/contracts.py` | `7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4` |
| `scripts/phase2_runtime/route_b_c03/identity_gate.py` | `EA762C13F1DED4ABEAE27D16DD1087901D73E0B6B0A680791E3082AEFFB4D90A` |
| `scripts/phase2_runtime/route_b_c03/mapping.py` | `320F7E8576C1C4E81B4E78E6058000E4D720173948BE736AD846B8CAD664EC66` |
| `scripts/phase2_runtime/route_b_c03/isolation.py` | `9BC554294D5945188A153F0A5CBEDFAB4E483C95B133683B7517ECC334D4205B` |
| `scripts/phase2_runtime/route_b_c03/failures.py` | `6F30D996119F61A19B20208FC44C8AF1FB96ADFE09ADE3538675B9D3F2933734` |
| `scripts/phase2_runtime/route_b_c03/audit.py` | `A704BDB22C55C92D0909FA0D6A668D8C149724B2A7627938C301758F1D09F561` |
| `scripts/phase2_runtime/route_b_c03/provider_port.py` | `66E4DA862BBBD50380B17686DB6BC2AB6D5D3B861AB53FCDDE1B608F86DEA381` |
| `scripts/phase2_runtime/route_b_c03/capability.py` | `028EE9DDD7A2C06840A6F344A4C4CC716EFF95073BE39CA6E57FB7FDBBFA6DD5` |

## 附录 B. 十五个 fixture 的本轮只读身份快照

以下文件均位于 `validation/route_b_c03/wp_008/fixtures/`；不重写其 expected 字段。

| 文件名 | SHA-256 |
| --- | --- |
| `C03-TA-V-001.json` | `C8CEFEDC496D5D0D33E0F21D61B5E3C3354579A8D0E1C74F70640305C65FC99A` |
| `C03-TA-V-002.json` | `257437A2AA80A58C0741F1EC0A5A514E014C633DD974804C6407DB84DB107290` |
| `C03-TA-V-003.json` | `21BD65ECD28D569BADFF11489017569E8413B1CC9A5138A851F907CCF62EAF7E` |
| `C03-TA-V-004.json` | `9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8` |
| `C03-TA-V-005.json` | `4405ADC2CE242B83120B0BA304157B3E6F03687345F764BBBE1E3A2DCF2422DE` |
| `C03-TA-V-006.json` | `9D24E6AFA92F9EF6E895B0B6E4D0E84BDC326E9C4B815E42723B31374CC2FDC8` |
| `C03-TA-V-007.json` | `68D9D63583A0301BDE76C3E60A5F66B7CCDA897C17D58E8DBF282E3E49C3DB90` |
| `C03-TA-V-008.json` | `7AA3FEF0CCDFA0C6A462C7945B63A50D828AC9C6D0725F428D347F6836075193` |
| `C03-TA-V-009.json` | `34EFBC55490FB2E3FFC89CAFCAD9DD2D319C2C24D9B3E2B026143F74A73DC93C` |
| `C03-TA-V-010.json` | `19DF9D35835F60C03C969B79B25F62CFE95E28C0A1B8122EDD8B9E1A5BC0E67A` |
| `C03-TA-V-011.json` | `8795DA58E092E6DC7F88958E3AC60B754870F5BFAE15FF8BC2D699450B65FDFD` |
| `C03-TA-V-012.json` | `8C6E4FC6279E95CFE48C9E9DA6E161F0AF05CA5FFEA95BE18DBAD6A81204E8E6` |
| `C03-TA-V-013.json` | `3DBF0F60AC970F90C97CF85F5F21F1758B4818D814A02CE8ED03A4F1C3A49CA6` |
| `C03-TA-V-014.json` | `D3EF698EA45F41824CCF6C5A7020F6A0B495460341ADE7446461A1AAF0E7D523` |
| `C03-TA-V-015.json` | `06DCEBA08CA43C75439B5A2AC1C140905887EF8CDC26C561FBD68E9A001D5AE1` |
