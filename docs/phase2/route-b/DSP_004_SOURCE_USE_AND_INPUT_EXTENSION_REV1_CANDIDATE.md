# DSP-004 来源使用与输入扩展设计候选 REV1

## 0. 范围、授权与形成时效力

| 项目 | 本候选的范围与限定 |
| --- | --- |
| 所属项目 | claude-for-legal-cn；仅 Route B / C03 / WP-008 / DSP-004 |
| 唯一新增文件 | docs/phase2/route-b/DSP_004_SOURCE_USE_AND_INPUT_EXTENSION_REV1_CANDIDATE.md |
| 授权依据 | 本对话提出仅新增上述设计候选并进行独立静态复核，Project Owner 明确回复“确认授权” |
| 资产类型 | DESIGN CANDIDATE ONLY；不是输入 JSON、Schema、捕获源码、准入记录或运行证据 |
| 形成时状态 | MATERIALIZED — INDEPENDENT STATIC REVIEW PENDING / NOT ACCEPTED |
| 允许动作 | 本文件物化、上游准确文件只读核对、作者静态检查及独立静态复核 |
| 未获准动作 | 修改既有文件、装载、编译、环境探测、测试、来源准入、实际捕获、集成或部署 |
| 保留状态 | DSP-004 OPEN / HOLD；B-01、B-02 OPEN；全部 LIMITED 与历史记录保留 |

本文件把已提出的会话层输入与来源设计整理为可独立审查的对象，不接受自身，不替 Project Owner 补签来源或根批准。形成时的待审状态不预先决定后续复核或接受结果；后续决定须在外部绑定本文件完整 SHA，不回写本文件。

仅使用本地虚构元数据；不需要真实姓名、证件、案件、个人信息、凭据、Token 或真实供应商。不访问或修改独立 ACOS、其他项目或 Route A / OCR。本轮不产生第二份物化复核报告、台账、接受归档或授权文件。

## 1. 固定参考身份与证据资格

以下均为本项目内的明确文件。完整 SHA 绑定文件字节；不以摘要相同推定来源可信、根接受或执行许可。表中对象各自已有的有限接受与历史状态继续分别保留，不因列入本表而统一获得接受。

| ID | 本项目路径 | SHA-256 |
| --- | --- | --- |
| REF-01 | validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json | A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430 |
| REF-02 | validation/route_b_c03/wp_008/fixtures/C03-TA-V-004.json | 9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8 |
| REF-03 | docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_SYNTHETIC_EXPECTED_BASELINE_REV1.md | BE8C55796587BBA65E22B048291E1688A8B076D02DA2A48DE412919BEB10F368 |
| REF-04 | docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PREPARATION_DESIGN_RECORD_REV1.md | DB39150AE0428A452B2BEBE958A4B7DD91F4DE8A3790B0BC374FAEA4693868F4 |
| REF-05 | validation/route_b_c03/wp_008/DSP_004_NATIVE_CONTRACT_CANDIDATE_REV1.py | 1544B7D8101493072E9BCA5C23B09C3C811F1B52CB1E9F5A8D73C976576FC312 |
| REF-06 | validation/route_b_c03/wp_008/DSP_004_ELIGIBLE_DECISION_COMBINER_CANDIDATE_REV1.py | 95156DEAD051799DA6361216EA66007F5B3FFF10257A886C0225AD3E95FDE9D6 |
| REF-07 | validation/route_b_c03/wp_008/DSP_004_DENIED_DECISION_PRESERVER_CANDIDATE_REV1.py | 61D424C35D262C3CC9FE03863F4BCB4D39FF96E248E5A7A08B8EAE6F8D598245 |
| REF-08 | validation/route_b_c03/wp_008/DSP_004_MATTER_FIELD_DIAGNOSTIC_CANDIDATE_REV1.py | 0322A367A607261501020EBB45BF1A2351580B54BCB0B468949E054540B02844 |
| REF-09 | validation/route_b_c03/wp_008/DSP_004_EXPECTED_BASELINE_READER_CANDIDATE_REV1.py | AE1389EDA1C3B9129A0546DA5764C1F68A6B0193A22DA3431CAA89BAB8DC0727 |
| REF-10 | validation/route_b_c03/wp_008/DSP_004_CONTROLLED_BASELINE_HANDOFF_CALLER_CANDIDATE_REV1.py | EF554C3051318BD305EDE6B8511C433C1BB9E20B10E93E5FB5F71C9AFF7A7E63 |
| REF-11 | scripts/phase2_runtime/route_b_c03/contracts.py | 7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4 |
| REF-12 | scripts/phase2_runtime/route_b_c03/identity_gate.py | 9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445 |
| REF-13 | docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FORMAL_ACCEPTANCE_PREPARATION_PACKAGE_REV1.md | FD27724FF5DB9C7F2DCC5175FD6B4E588F1961D73ADC2807E9EF2DE8004D4055 |
| REF-14 | validation/route_b_c03/wp_008/DSP_004_FORMAL_ACCEPTANCE_PREPARATION_CANDIDATE_REV1.json | 127521BAF310DDF57C33336B8A17B29D40002E4419A5E5CCB0ED029562DB24E2 |
| REF-15 | docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_ENVIRONMENT_IDENTITY_REBINDING_REV1_CANDIDATE.md | DC6DAA71B5ADB99E1E2FF61FD535B51C661C7671E3E08F651046740300B329EA |
| REF-16 | docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_TYPED_CONTRACT_REV3_CANDIDATE.md | AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F |
| REF-17 | docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_ARRAY_POLICY_REGISTRY_REV3_CANDIDATE.md | 39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123 |

REF-04 的设计形成时正文与其后会话采纳记录分开解释，不以旧“未接受”快照抹除后来的有限采纳。REF-13、REF-14 的形成时关卡状态也不覆盖其后的实际决定；本候选同样不把后来的文档接受扩大成来源准入。

本轮只读核对范围是本表 17 个文件及项目指导文件。REF-15 仅作为既有观察的记录来源，本轮不重新访问它记载的七个环境文件，不重新验证运行时版本、安装来源或系统目录。

## 2. 已有接口能做什么，不能做什么

| 现有对象 | 可静态确认的局部职责 | 不提供的能力 |
| --- | --- | --- |
| REF-09 / extract_expected_baseline | 对完整固定基线字节进行提取，返回 Project、Session、Provider 三条文档记录 | 不读取文件、不捕获实际值、不授予来源使用权 |
| REF-10 / read_and_extract_fixed_baseline | 设计中的固定预期文件取字节、读取器装载与清理路径 | 其源码存在不等于可信装载成立；不是实际侧捕获器 |
| REF-05 / BoundaryCheck 与序列校验 | 精确原生类、状态与原因组合、三项元组顺序等结构核验 | state / cause 来自调用者；不读取或比较引用，不证明来源可信或同一调用 |
| REF-06 / combine_eligible_decision | 仅消费 ELIGIBLE_FOR_MAPPING 原生结果及三项补充观察，按既有优先级组合 | 不执行原门禁，不生成观察，不建立来源或执行权限 |
| REF-07 / preserve_denied_decision | 对合适的 BLOCKED / REJECTED 元数据原对象保留 | 不生成三项观察，不证明实际门禁曾执行 |
| REF-08 / diagnose_matter_fields | 对符合范围的 isolation 拒绝及事项 ID、版本、actor 作分别诊断 | 不凭原因字符串归因，不授予补充观察资格或建立捕获来源 |
| REF-12 / evaluate_identity_gate | 现有签名内的身份及授权元数据分支 | 没有 Project、Session、Provider 同名输入或观察入口 |

当前缺失的是实际上下文的受控产生、固定捕获入口及与同一调用的证据交接，不能通过给 BoundaryCheck 填入 MATCH / MISMATCH 补足。新增接口的物化、装载和调用仍须另外授权。

## 3. 六侧来源的使用绑定设计

### 3.1 身份层次不得混用

source_role 表示职责槽位；source_identity 表示具体来源身份；载体 path / 完整 SHA 表示字节对象；variant_id、attempt_id 与 input_snapshot_sha256 表示一次具体使用的关联条件。它们不是互相替代的标识。

未来向 BoundaryCheck 的 expected_source_id / actual_source_id 填值时，须在独立审查的适配合同中逐项固定其来源身份映射，不能自行把角色名、引用字符串、载体 SHA 或关联 ID 填入任意身份字段。当前不修改 REF-05 的六字段合同。

### 3.2 六个职责槽位与已有候选

| 来源角色 | 现有或待建立的来源 | 准确取值设计 | 仍缺的具体使用事实 |
| --- | --- | --- | --- |
| SRC004-E-PROJECT | REF-03；DSP004-EXPECTED-PROJECT-V1 | 第 3.1 节 Field = Expected Reference 的唯一行；SYNTHETIC-PROJECT-001 | 本次变体、调用尝试、输入快照与准确使用批准 |
| SRC004-E-SESSION | REF-03；DSP004-EXPECTED-SESSION-V1 | 第 3.2 节相同字段的唯一行；SYNTHETIC-SESSION-001 | 同上，不从关联字符串推定会话资格 |
| SRC004-E-PROVIDER | REF-03；DSP004-EXPECTED-PROVIDER-V1 | 第 3.3 节相同字段的唯一行；SYNTHETIC-PROVIDER-001 | 同上；不要求真实供应商 |
| SRC004-A-PROJECT | 实际来源身份、载体和入口未建立 | 获准调用上下文的 Project 原始引用，经固定入口捕获 | 来源身份 / 版本 / 载体 / SHA、产生者、入口、权限及观察归属 |
| SRC004-A-SESSION | 实际来源身份、载体和入口未建立 | 当前专用调用尝试的 Session 原始引用，经固定入口捕获 | 同上，不能从 expected 或 audit_correlation_id 补值 |
| SRC004-A-PROVIDER | 实际来源身份、载体和入口未建立 | 获准本地合成 Provider 上下文的原始引用，经固定入口捕获 | 同上；NOT_SELECTED / 禁止调用不证明 Provider 身份 |

预期三项文档版本保持 REF-03 的“REV1 — DOCUMENT CANDIDATE VERSION ONLY”。角色齐全、相同字符串、相同摘要、不同模型名称或不同职责标签均不独立证明可信性与职责分离。

frame.project_reference、frame.session_reference、frame.provider_reference 仅是 REF-04 原文 C 的拟议逻辑位置，不是现有 Gate 类属性，不可据此动态 getattr、导入或假定接口存在。调用刺激进入该未来上下文后，仍须由获准入口实际捕获，不能把刺激帧本身称为观察。

### 3.3 事前资格与事后观察分开

| 阶段 | 需要固定或产生的对象 | 禁止替代 |
| --- | --- | --- |
| 来源准备与使用前 | 六侧来源身份 / 版本、载体身份、产生者职责、唯一位置、适用范围和准确批准；实际侧入口源码及其受控装载资格 | 文档接受、源文件 SHA 或人工完成声明不代替来源准入与读取权 |
| 具体调用准备 | 准确变体、唯一调用尝试、独立预期、输入快照定义及摘要、所用授权；上下文与该调用的受控交接 | 不用固定的关联字符串或 189 项计划 ID 证明一次调用 |
| 获准调用发生时 | 取得实际引用，保留原生类型、来源、门禁返回与捕获对应关系 | 不从预期回填实际；不从最终结果倒推来源资格 |
| 获准调用发生后 | 对真正产生的观察记录固定完整载体 SHA，并关联其原始输入和调用身份 | 不预填未来观察 SHA，不重跑或重序列化以伪造缺失的历史见证 |

正式使用所需的事前资格缺失时，保持 HOLD / NOT_RUN，不通过运行倒填资格。若未来另行明确授权缺失或无效来源的本地负向合成案例，其 UNBOUND 结果只说明该案例路径，不使缺失来源被准入。

预期维护者、实际上下文产生者、捕获职责与复核职责的具体访问边界仍须绑定；待审调用与实际产生者不得改写冻结预期。稳定职责身份足够，不要求真实人物信息。

## 4. 输入扩展的准确边界

### 4.1 不覆盖的已有对象

REF-01 中 scenario_id = C03-TA-V-004 的三项刺激是 SB-004-MATTER-ID、SB-004-MATTER-VERSION、SB-004-ACTOR，其 adapter_id 为 ADP-EVALUATE-IDENTITY。原配置、packet、envelope、expected 对象引用及各自单字段 override 保持不变。

REF-01 仍不是完整 DSP-004 输入准入记录。本候选不覆盖它或 REF-02，不修改已采纳的 189 项局部输入与预期清单，不把 189 个计划项或既有合成断言自动登记为新的正式变体、输入快照或执行证据。

新增覆盖组尚未分配正式 variant_id、attempt_id 或输入快照 SHA。本节的中文组名不是永久 ID、JSON 字段或可执行参数。未来唯一输入候选的文件名、字节、闭合字段合同、固定适配器与使用范围须先明确，再物化、复核和决定，不能靠本候选自行准入。

### 4.2 分离的覆盖组

下表是基于现有设计与源码的预期关系，不是本轮执行结果，也不直接填入实际观察。

| 覆盖组 | 输入与可达性要求 | 预期路由 / 比较要求 | 保留限制 |
| --- | --- | --- | --- |
| 原事项 ID 单错配 | 保留 SB-004-MATTER-ID；按逐字段合同确认事项 ID 差异 | 保留原 REJECTED — ISOLATION FAILURE；允许的补充观察只能作附加诊断 | 不能把原生拒绝自动映射成整个 Fixture 通过 |
| 原事项版本单错配 | 保留 SB-004-MATTER-VERSION；分别核对事项版本 | 同上，不把 ID、版本合并为一个字段检查 | 最终事项边界释义与映射仍需准确处置 |
| 原 actor 单错配 | 保留 SB-004-ACTOR，不改变事项 ID / 版本 | 保留原拒绝；三项补充观察 NOT_EVALUATED / PRIOR_DENIAL | actor 不替代事项错配 |
| Project 单错配 | 原门禁输入须可产生 ELIGIBLE_FOR_MAPPING；三项来源合格，仅 Project 有效引用不同 | Project MISMATCH，其余 MATCH；REJECTED — PROJECT CONTEXT MISMATCH | 任一来源缺失、无效或未观察均不满足单错配前提 |
| Session 单错配 | 同上，仅 Session 有效引用不同 | Session MISMATCH，其余 MATCH；REJECTED — SESSION CONTEXT MISMATCH | 关联 ID 相同不是来源证据 |
| Provider 单错配 | 同上，仅 Provider 有效引用不同 | Provider MISMATCH，其余 MATCH；REJECTED — PROVIDER CONTEXT MISMATCH | 不执行真实 Provider 调用 |
| 三项全匹配对照 | 原门禁合格，三项各有受控来源与实际匹配观察 | 保留同一原生 prior 对象及完整原因，不新建等价替身 | ELIGIBLE_FOR_MAPPING 不是执行许可 |
| 原四边界联合条件 | 独立保留 REF-02；事项 ID 或版本差异按原逐字段规则确认，三项补充差异分别有同次调用的受控记录 | 保留原 isolation 拒绝；补充观察仅作诊断，不送入 eligible-only 组合器 | 不拼接分项运行；不预定事项边界的最终实例数或判通过 |
| 多项补充错配 | 只在 eligible 分支，至少两项有效且来源合格的引用不同 | 按既有优先级产生 REJECTED — MULTIPLE CONTEXT MISMATCHES | 不替代原四边界联合条件 |
| 来源缺失 / 引用无效 / 构造失败 | 仅未来准确授权的负向合成范围；分别保留不同失败层级 | 按第 5 节，不补值、不生成替代返回 | 不取消来源使用前置条件或以负向通过宣告准入 |

Project / Session / Provider 单错配要求未选中的边界及原门禁其他条件有独立依据，不能只在表格中写“其余默认匹配”。REF-01 现有对象目录可作为单独核对的候选参考，不因其文字看似一致就建立原生对象构造、来源合格或实际门禁执行。

## 5. 原门禁、附加诊断与组合边界

### 5.1 路由前置条件

所有下述路由均属于未来另行获准的调用。当前未运行时不生成 GateDecision 或三项观察。

先核对对象构造与关联引用的有效性，再取得既有门禁的实际原生返回。构造无法完成时记录 CONSTRUCTION_FAILURE，不伪造完整观察序列或替代 GateDecision。若失败发生前已有真实原生返回，该返回作为既有证据保留，但不据此编造后续完成结果。

对原门禁的 14 类拒绝条件继续逐项沿用 REF-04 第 3.1 节原文第 4 节规则，不按本候选合并原因：一般拒绝分支三项均 NOT_EVALUATED / PRIOR_DENIAL，原返回对象和四字段不变。

REJECTED — ISOLATION FAILURE 不能单独证明哪项字段错配。仅按既有逐字段规则独立确认事项 ID 或版本错配且其附加诊断条件成立时，才能形成三项附加诊断；actor-only 或条件不可核对时仍为 NOT_EVALUATED / PRIOR_DENIAL。REF-08 的诊断结果本身不是来源资格或自动路由授权。

### 5.2 Eligible 分支的既有优先级

只对真实 prior.state 为精确原生 ELIGIBLE_FOR_MAPPING 且输入/三项观察满足合同的情形，保持以下顺序：

1. 任一 INVALID_REFERENCE_TYPE：BLOCKED — CONTEXT REFERENCE INVALID。
2. 否则任一 SOURCE_UNBOUND：BLOCKED — CONTEXT SOURCE UNBOUND。
3. 否则至少两项 MISMATCH：REJECTED — MULTIPLE CONTEXT MISMATCHES。
4. 否则 Project MISMATCH：REJECTED — PROJECT CONTEXT MISMATCH。
5. 否则 Session MISMATCH：REJECTED — SESSION CONTEXT MISMATCH。
6. 否则 Provider MISMATCH：REJECTED — PROVIDER CONTEXT MISMATCH。
7. 三项均 MATCH：返回同一 prior 对象，完整原因不变。

UNBOUND / SOURCE_UNBOUND 与 UNBOUND / INVALID_REFERENCE_TYPE 分开；来源已绑定但捕获引用不是精确原生 str、为空或全空白时，不能当作正常错配。观察顺序必须为 PROJECT、SESSION、PROVIDER 的精确原生三元组。

NOT_EVALUATED 不属于 REF-06 的 eligible-combination 输入，即使另一项 UNBOUND 也不能以优先级覆盖这个范围错误。类型、结构、无返回、异常或缺失观察导致受影响比较停止，不转换成默认 GateDecision。所有状态 / 原因组合继续服从 REF-05，不添加新枚举或原因。

原拒绝分支不调用 REF-06 来替换拒绝。REF-07 只保留原返回；三项附加记录如未来获准，应由另行绑定的捕获与适配层产生，不误称 REF-07 已具备该能力。

## 6. 预期、输入快照与实际记录的交接

| 对象 | 未来必须准确固定的内容 | 不可混用的身份 |
| --- | --- | --- |
| 预期数据 | REF-03 全载体身份、各唯一定位、冻结规则、具体使用范围 | 预期引用字符串的摘要不是完整载体 SHA |
| 输入快照 | 精确变体、完整被调用输入、对应上下文刺激、原生类型 / 编码合同及与本次调用的受控交接 | REF-01 整文件 SHA、packet.input_set_sha256 或关联字符串不能自动替代本次 input_snapshot_sha256 |
| 同次调用关联 | variant_id、attempt_id、快照与来源使用依据，由受控入口交接而非调用者两侧自填 | ID 字符串相同不证明来源、冻结或同次调用 |
| 原生返回 | 精确 GateDecision / InvocationState 类身份、原原因与关联 str、原生空 tuple 及对象保留关系 | 字典、子类、同名异装载类、字符串枚举或 JSON 空数组不冒充原生值 |
| 实际引用与补充观察 | 捕获值、原生类型、来源身份、定位和捕获入口；与派生 BoundaryCheck 的一一关系 | BoundaryCheck 中由调用者提供的 state / cause 不作为原始捕获证据 |
| 可逆展示与记录 | 将实际取得的值和来源单独保留，再记录比较结果 | 不从预期、状态标签或最终结论反向合成实际值 |

本节是交接要求，不引入新的运行 Schema、快照编码器或身份参数接口。快照的精确字节布局、来源覆盖及摘要规则尚未由本文件实现或接受，未来须准确绑定，不自行选取子集、规范化字符串或用 JSON 往返改变原生类型。

REF-02 的 BLOCKED_ISOLATED、BOUNDARY_MISMATCH、空写入集合及 CROSS_BOUNDARY_DISCLOSURE_OR_STATE_REUSE 原样保留。原生 REJECTED 到 Fixture 抽象的映射仍需单独审查；原生空写入 tuple 只是元数据，不证明零 I/O、实际隔离、零披露或没有状态复用。

## 7. 四根、数组来源与环境依赖的外侧停点

本候选不扩大根核验范围，亦不把来源设计等同于读取授权。

| 依赖 | 本候选可引用的已有记录 | 仍需的准确前置条件 |
| --- | --- | --- |
| PROJECT_ROOT | 已有本项目工作区定位 | 规范目录身份、来源、解析器 / 版本、大小写与重解析政策、准确文件 / 用途 / 阶段、完整性依据和独立处置 |
| VENV_ROOT | 历史 .venv-validation 与 REF-15 记录 | 同上；文件观察或配置版本文字不能代替环境接受 |
| RUNTIME_ROOT | REF-15 记录的配置 home 值 | 仅为已记录定位；根资格、完整依赖及后续使用仍未由本候选建立 |
| SYSTEM_ROOT | 已有准备材料保留未绑定 | 不猜测默认系统路径，不以环境变量或目录名称替代准确 host 来源及批准 |
| 五类 ORDERED 来源 | REF-17 的 AP-006、AP-009、AP-020、AP-021、AP-022 设计政策 | 实际来源文件 / 完整 SHA、唯一序列定位、元素身份与重复处置的先前准确绑定；不从本候选自动填入 |

四根正式要求仍按 REF-16 RootBinding / ReadScope：根来源、独立复核、Owner 决定、解析器、大小写 / 重解析规则、逐文件读取范围、完整性证据及残余限制各自准确。根存在、目录字符串或 SHA 相同不独立建立信任；根绑定不授予递归枚举或跟随重解析权限。

根须在未来 Manifest 生成前已有来源及批准，不能在正式运行中追补准备资格。输入扩展仅针对 DSP-004，不替代 REF-17 中全部 15 个场景及各自变体序列的整体绑定，不以 V-004 局部方案关闭 B-02。

## 8. 本候选的独立静态复核范围

授权的复核仅针对本候选完整 SHA 及第 1 节明确参考文件，可核对相关原文与身份，不执行任何项目代码，不重新探测环境。复核结论通过会话交付，不物化第二份报告。

| 核对项 | 应核对的文本条件 |
| --- | --- |
| SR-01 | 唯一新增资产、范围、授权来源和形成时状态准确，不自接受或自授权 |
| SR-02 | 17 个参考路径及完整 SHA 与准确文件身份一致，不扩大接受效力 |
| SR-03 | 预期读取、结构校验、判定组合、拒绝保留和实际捕获职责没有混淆 |
| SR-04 | 六个来源槽位与三项预期定位保真；实际来源未填入伪造身份或观察 |
| SR-05 | source_role、source_identity、载体身份、适配字段及同次调用身份不互换 |
| SR-06 | 事前资格、具体输入、获准调用和事后观察分开，无未来 SHA 预填或循环绑定 |
| SR-07 | 原三项刺激、三项单错配、全匹配对照、联合条件和负向层级分开，未改 189 清单 |
| SR-08 | 原拒绝、事项逐字段诊断、actor-only 限制、eligible 优先级及构造失败保真 |
| SR-09 | 原生返回与 Fixture 期望层级分开，不宣称实际隔离或整体 Fixture 通过 |
| SR-10 | 四根、五类 ORDERED 实际来源和环境依赖未被本候选接受或准入 |
| SR-11 | 历史状态与后续有限决定分开，不自动废止正常更新前的历史结果 |
| SR-12 | 表格、完整 SHA、记录计数与结论一致，全部 LIMITED 和后续停点可定位 |

复核者不得被要求预设全部 PASS。缺陷应准确报告；设计文本自身需修正的问题与实现 / 来源 / 运行准备限制分别记录。文本静态通过不等于下表限制已解除。

## 9. 保留限制与后续准入条件

| 限制 | 仍未由本候选完成的事实 / 对象 | 后续使用前的处理 |
| --- | --- | --- |
| 来源资格与实际入口 | 三项实际来源、捕获接口、职责访问边界及准确身份字段映射尚未建立；预期具体使用尚未绑定 | 另行准备准确对象、独立复核和 Project Owner 决定；不直接生成实际观察 |
| 完整输入及比较规则 | 新增变体 ID / 快照 / 固定适配器未物化或接受；原生到 Fixture 映射与联合条件仍有限 | 不覆盖 REF-01 或 REF-02，不将局部预期或合成结果视为完整输入准入 |
| 根、启动与依赖 | 四根批准链、环境 / Harness 的完整依赖、T0 与后续装载资格、ORDERED 实际来源仍需准确绑定 | 保持 B-01 / B-02 OPEN，不生成 Manifest 或探测环境 |
| 完整性、输出与停止 | 检查至使用防替换、同次调用 / 跨进程冻结、输出隔离、物理停止及清理的全部保证未建立 | 保留已有 LIMITED，不以重复散列、空输出声明或局部超时样本消除 |

这些是后续实施 / 准入前置条件，不因为候选将其如实记录就成为已解决条件，也不因为限制仍在就自动判定设计文本存在缺陷。正常更新的历史影响仍按实际依赖与可证实时间范围分别评估，不全项目自动废止。

本轮完成后的停点是候选完整 SHA 的独立静态复核与 Project Owner 的有限设计决定。即使本文件后来被接受，也仅接受此设计文本，不准入来源、不接受新增输入、不修改已接受源码、不授权捕获实现、装载或测试。

DSP-004 继续 OPEN / HOLD；B-01、B-02 继续 OPEN。全部 LIMITED、原失败版本、后续验证记录及已有限接受文件原样保留。不产生总体隐私 / 安全 / 法律结论，不调用 Gemini 或外部模型，不触发自动下游转换。
