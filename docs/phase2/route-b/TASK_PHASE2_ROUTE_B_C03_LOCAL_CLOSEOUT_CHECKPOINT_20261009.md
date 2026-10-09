# 本项目本地收口检查点 — 2026-10-09

状态：`PARTIAL — BLOCKERS RETAINED / NOT A STAGE ACCEPTANCE`。

本报告记录本轮实际完成的本地检查，不是治理接受决定、正式 WP-008 验证结果、来源准入记录或工程上线许可。只涉及 `claude-for-legal-cn`；未访问或修改独立 ACOS、协作系统源项目或其他项目。第三方模型未调用。检查开始时的工作区干净。

## 1. 范围与方法

本轮按 Project Owner 关于本地批量推进的指令，完成可安全进行的基础检查、已有合成回归和独立只读执行前置复核。已接受文件不修改；未安装软件、下载 OCR 模型、接入真实案件材料或调用真实 Provider。

观察到的本地 Python 为 3.12.14；有限合成回归采用项目 `.venv-validation/Scripts/python.exe`，参数为 `-I -S -B`，控制台输出，不生成持久测试结果或字节码。该观察不修改旧环境清单，也不等同于 DSP-004 可信宿主或依赖链已经准入。

PowerShell 宿主版本观察为 7.6.5，Node 为 v24.19.0。版本观察及沙箱网络限制均不能证明 DSP-004 的可信装载、完整资源隔离或外侧停止能力。Git Bash 文件存在；未发现可直接使用的 `jq`。没有为绕过缺失依赖安装工具或替换既有检查程序。

## 2. 基础检查结果

| 检查 | 本轮观察 | 限定 |
| --- | --- | --- |
| Marketplace 官方清单校验 | PASS，1/1 | 结构校验不等于跨文件字段一致性 |
| 第一方插件官方清单校验 | PASS，12/12 | 保留插件根 CLAUDE.md 不自动作为项目上下文加载的既有警告 |
| 中国化回归 | PASS | 本地静态约束，不验证现行法律数据的真实性或新鲜度 |
| Cookbook 编排端工具权限检查 | PASS，5/5 | 没有部署任何托管代理 |
| 基础 JSON 语法 | PASS，47 个文件 | 单独统计的扫描范围为基础插件、scripts、connectors、references、cookbooks；不将其解释为全部阶段证据语义审查 |
| Skill frontmatter | PASS | Agent 必需 name/description；Skill/Command 必需 description |
| Skill 数量与状态文档 | MATCH，162 个可发现入口、169 个物理文件 | Corporate 历史实现文件 7 个；不是新增 7 个独立入口 |
| MCP 生成一致性只读检查 | PASS，12/12 | 使用生成器 --check，未重生成或修改配置 |
| legal-data 自检及核心冒烟调用 | PASS，样例索引 | 明确指定仓库样例；未读取真实资料索引、未联网、不是法律结论 |
| Cookbook 结构性 dry-run | PASS，5/5，合计 21 个 body | 用只读 Python/YAML 内存检查；不是原 Bash/jq 冒烟脚本的执行证明 |
| Marketplace/plugin 元数据完全一致 | FAIL，4 处 description 不一致 | name/author 未发现差异；该项必须单独保留，不能被官方结构 PASS 抵消 |

结构性 dry-run 核对：系统文本非空、所有相对引用保持在本项目内、叶节点不再调用下一层、body 中不保留 output_schema。数量为 diligence-grid 5，docket-watcher 4，launch-radar 4，reg-monitor 4，renewal-watcher 4。没有上传 Skill、创建代理或发送 API 请求。

### 2.1 四项清单一致性阻断

| 编号 | 模块 | 阻断 |
| --- | --- | --- |
| META-01 | product-legal | Marketplace description 与插件自身 description 不同 |
| META-02 | legal-builder-hub | 两处 description 不同；插件文案仍以 Phase 2 开头，与现有阶段归类存在待确认的一致性问题 |
| META-03 | law-student | 两处 description 不同 |
| META-04 | legal-clinic | 两处 description 不同 |

仓库 AGENTS 要求第一方两份清单的 name、description、author 逐字段一致。本轮没有替 Project Owner 选择不同业务文案，也没有修改既有清单。后续应明确允许范围有限的同步修订，并保留当前固定 SHA 的 DSP-004 文件不变。不能为追求测试全绿直接把其中一份描述复制到另一份，尤其不能把高权限 Phase 2 动作默认为已交付能力。

## 3. 已完成的有限合成回归

| 既有测试对象 | 实际运行方法数 | 失败 / 错误 | 结果 |
| --- | --- | --- | --- |
| DSP-004 预期基线提取候选 REV1 | 25 | 0 / 0 | PASS — LOCAL SYNTHETIC ONLY |
| DSP-004 原生边界合同候选 REV1 | 31 | 0 / 0 | PASS — LOCAL SYNTHETIC ONLY |
| DSP-004 决策组合候选 REV1 | 45 | 0 / 0 | PASS — LOCAL SYNTHETIC ONLY |
| DSP-004 拒绝结果保留候选 REV1 | 25 | 0 / 0 | PASS — LOCAL SYNTHETIC ONLY |
| DSP-004 事项逐字段诊断候选 REV1 | 35 | 0 / 0 | PASS — LOCAL SYNTHETIC ONLY |

本节合计 161 个实际测试方法，失败 0、错误 0；不是控制端 189 项清单的执行，不能相互换算。测试中的 open 拒绝记录属于刻意执行的防护自检，不是实际读取失败之后继续运行。候选及固定输入在测试前后均通过原测试的 SHA 核对。审计钩子仅提供有限 Python 调用诊断，不能证明全面沙箱、零系统副作用或分配安全。

四项原生/组合/保留/诊断回归已经独立只读副作用复核，结论为 `PASS — LIMITED TO EXISTING LOCAL SYNTHETIC REGRESSION SCOPE`。这是运行范围复核，不是测试结果预判。三个使用 contracts 的回归仅装载该文件的声明，构造或核对合成 GateDecision 元数据，不执行 identity gate、Provider、映射器或包初始化。读取固定保护清单、内存模块登记、审计钩子、临时 profiler 和控制台输出属于实际副作用，不能表述为零 I/O。

预期提取器测试的私有解析助手负向用例使用合成片段，不证明这些片段可通过真实固定 SHA 入口。真实固定 SHA 后的解码错误、格式错误和元数据冲突分支仍保留未覆盖声明。

来源准入、实际捕获、真实 Gate/Provider 执行、正式 WP-008 验证以及生产集成均未由这些结果建立。

## 4. DSP-004 执行前置复核

独立只读复核结论：`LIMITED — 现有源码边界清楚，但不具备局部验证载体执行条件`。该结论不撤销或重写既有有限源码接受。

| 项目 | 当前证据 / 缺口 | 收口状态 |
| --- | --- | --- |
| 现有载体身份、完整描述行 | 固定 SHA 匹配；静态逐行检查 M=6、RQ=18、D=7、F=62、RD=52、WR=44，连续编号与列数一致，合计 189 | 文本完整；不是原生可执行输入 |
| 可信启动根与私有执行域 | pwsh -NoProfile、版本观察和网络限制不建立解释器/依赖链身份或函数归属 | UNBOUND |
| 同份字节、完整十定义装载、八函数受控调用 | 控制端仅含定义；助手仍按名称解析；有界读取、尾检测、严格解码及受控归属无实际实现 | UNBOUND |
| 189 项原生输入与独立预期 | 当前枚举器只返回 RawTextRow；原生构造、M 多次调用、独立比较尚未实现 | UNBOUND |
| 完整返回捕获与无副作用成员比较 | 空输出、显式 null、null 属性及安全成员检查接口尚未绑定 | UNBOUND |
| 启动前输出封闭、认证与原子消费 | 没有已实现的全部流封闭入口或停止窗口内原子消费机制 | UNBOUND |
| D-007 独立准备与同份输入 | 未由独立准备责任构造、计算并绑定同份私有 20177-byte 合成输入 | UNBOUND / NOT_RUN |
| 120/5/5 计时、外侧停止、原资源与并存异常 | 仅设计预算；无真实监督实现及原操作/后代资源收束证据 | UNBOUND |

载体 batch 入口与控制端 SingleCase 入口均为无条件拒绝；本轮未装载、解析执行或调用两份 PowerShell 源码。不得通过切换拒绝开关、只运行其中 188 项、模拟布尔准入、普通超时包装或用受测检查器倒推准备完成来消除缺口。

保留：`DSP-004 OPEN / HOLD`，`B-01 OPEN`，`B-02 OPEN`；正向真实 driver SHA 分支仍 `NOT COVERED`。120/5/5 秒是提议，不是已经实现的能力。任何停止命令、Kill 返回、父进程退出或包装等待完成均不能单独证明原操作及后代资源已收束。

## 5. 固定输入完整性

以下值由本轮本地读取核对；不是外部模型计算值。测试内的其他固定输入核对以对应脚本实际输出为限。

| 资产 | SHA-256 |
| --- | --- |
| DSP_004_LOCAL_VALIDATION_CARRIER_CANDIDATE_REV1.ps1 | 46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C |
| DSP_004_OUTER_CONTROLLER_CANDIDATE_REV1.ps1 | 891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB |
| DSP_004_EXPECTED_BASELINE_READER_CANDIDATE_REV1.py | AE1389EDA1C3B9129A0546DA5764C1F68A6B0193A22DA3431CAA89BAB8DC0727 |
| DSP_004_NATIVE_CONTRACT_CANDIDATE_REV1.py | 1544B7D8101493072E9BCA5C23B09C3C811F1B52CB1E9F5A8D73C976576FC312 |
| DSP_004_ELIGIBLE_DECISION_COMBINER_CANDIDATE_REV1.py | 95156DEAD051799DA6361216EA66007F5B3FFF10257A886C0225AD3E95FDE9D6 |
| DSP_004_DENIED_DECISION_PRESERVER_CANDIDATE_REV1.py | 61D424C35D262C3CC9FE03863F4BCB4D39FF96E248E5A7A08B8EAE6F8D598245 |
| DSP_004_MATTER_FIELD_DIAGNOSTIC_CANDIDATE_REV1.py | 0322A367A607261501020EBB45BF1A2351580B54BCB0B468949E054540B02844 |
| TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_SYNTHETIC_EXPECTED_BASELINE_REV1.md | BE8C55796587BBA65E22B048291E1688A8B076D02DA2A48DE412919BEB10F368 |

## 6. 后续边界

1. 基础清单修复涉及既有文件，不能从本轮测试通过推导改写权限。
2. DSP-004 后续需要独立的新实现候选、可信装载与外侧监督实现；全部真实前置逐项具备后才能对固定候选执行局部验证。不能把本报告、Gemini 咨询或源码接受当作技术缺口已被实现。
3. Route A 的真实材料身份、来源和访问确认仍需实际输入；OCR 最终选型和安装不在本轮范围内。
4. 本报告不修改历史复核和接受记录，不签发总体隐私、安全或法律合规结论，不自动推进任何运行或集成阶段。
5. 阶段备份只保存本项目经审查可公开的检查点，不代表 Project Owner 接受或 DSP-004 关闭。

本轮开始时已核对的本地 HEAD 为 `84e3a3b1e5aeb405f0981215d86d32e3f70dd1a7`。本报告不预填尚未发生的提交、推送或远端确认结果；后续备份结果以实际提交及远端核对为准。
