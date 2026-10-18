# DSP-004 环境身份重绑定准备候选 REV1

## 0. 形成范围与效力

| 项目 | 准备记录 |
| --- | --- |
| 所属项目 | claude-for-legal-cn / Phase 2 Route B C03 WP-008 / DSP-004 |
| 文档性质 | ENVIRONMENT IDENTITY REBINDING PREPARATION CANDIDATE — DOCUMENT ONLY |
| 会话设计来源 | 环境身份重绑定准备方案 REV1，writing 37184 |
| 本批次授权 | 仅新增本候选，使用上一轮已经取得的 7 文件观测，完成独立静态复核 |
| 环境访问边界 | 本次物化不重新读取 7 个环境文件，不扩展原观察范围 |
| 物化与复核 | 形成记录不预填复核 PASS；完成文件 SHA 和复核结论在会话中分离报告 |
| 环境重绑定 / 来源准入 | NOT ESTABLISHED BY THIS CANDIDATE |
| Manifest / 装载 / 测试 / 实际捕获 / 集成 / 部署 | NOT AUTHORIZED |
| 保留状态 | DSP-004 OPEN / HOLD；B-01、B-02 OPEN；全部 LIMITED 保留 |

“重绑定”是准备事项名称，不是已经完成重绑定、根接受、来源准入或执行许可的声明。
物化及静态复核不自动接受本物理候选；对候选的有限接受也不批准运行环境可用。

仅允许新增本 Markdown 文件，不新增第三份审查或接受记录。不修改已接受文件、
189 项输入与预期清单、唯一候选源码、旧计划或历史观测。
不启动 Python，不装载目标或候选，不运行测试，不安装、替换、复制或冻结环境，
不改变权限，不准入来源，不生成 Manifest，不实际捕获、不集成或部署。
不访问独立 ACOS 或其他项目。

## 1. 依据与观测资格

### 1.1 已有限接受的文档合同

以下两个文件是本次物化前只读摘要核对的准确对象；它们只接受了设计文档内容，
不提供实际环境、根、输入或序列来源准入。

| 文档 | 字节数 | SHA-256 |
| --- | --- | --- |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_TYPED_CONTRACT_REV3_CANDIDATE.md | 29240 | AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_ARRAY_POLICY_REGISTRY_REV3_CANDIDATE.md | 16317 | 39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123 |

本候选不修改这些准确字节，也不为其补入后来的接受状态。
自己的完整文件 SHA 只在形成后通过分离会话记录报告，不嵌入自身。
没有未来 Manifest、运行、审查或接受凭证的预填 SHA。

### 1.2 三组记录的来源与限制

| 记录组 | 定位 | 本文使用方式 |
| --- | --- | --- |
| 旧计划记录 | Plan V2.2 第 3.1—3.2 节，路径见下文 | 只比较其中记录的字节数及 SHA，不宣称重新读取了旧二进制文件 |
| 此前会话观测 | 本对话此前保存的 7 文件观测记录 | 使用已经记录的数值，不宣称存在另一份已准入物理来源文件 |
| 最近一次已记录观测 | 本对话刚完成的“7 文件只读身份核对及会话层差异复核”批次 | 复用已保存的观测与比较结果，不在本物化批次重新访问环境 |

旧计划定位：
docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_2_CANDIDATE.md。
其既有记录 SHA 为：
6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA。
该值用于识别被引用的历史计划记录，不声称在本物化批次独立重算该文件或原始环境。

“最近一次已记录”只说明本文选择的会话观测事件，不保证这些字节现在仍在磁盘上。
缺少足以界定变化区间的可信时点记录，因此本文不填造时间字段，
不把会话记录次序或本文件物化时间当作文件更新发生时间。
本候选及后续静态复核不能补足这项历史时间限制。

### 1.3 原观察方法，不是本轮新执行

最近一次已记录的环境观察由限定 7 文件的顺序只读取得：

- 对每个文件的同一份已读字节计算 SHA，并记录该份字节长度。
- 配置内容从已计算摘要的同一份配置字节解析。
- 输出显示每个文件读取前后长度、最后写入元数据及属性比较结果均相同。
- 输出显示检查到的各文件及限定父目录没有 ReparsePoint 标记。
- 观察没有启动 Python、导入模块、装载候选、测试或变更环境。

这里只复述已保存输出。没有独立重新验证上述原观察方法实现，
不将输出布尔值提升为防篡改、原子性、来源真实性或根可信性的证明。
元数据相同不能排除未被观察到的替换，也不能保证检查后的使用完整性。

## 2. 已记录的 7 文件身份

本节数值来自最近一次已保存观测，不是本次物化时的新读数。
路径中的 / 是显示形式，不建立大小写、重解析或规范目录接受政策。
“相同”只表示字节数及 SHA 都与相应记录相同，不表示环境资格相同。

| 行号 | 准确观察路径 | 观测字节数 | 观测 SHA-256 | 对旧计划记录 | 对此前会话观测 |
| --- | --- | --- | --- | --- | --- |
| EIR-001 | C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/.venv-validation/pyvenv.cfg | 460 | 7AFB3C331994D8D1CB462B711254E30BAE372DC8A28F2C485AFA79B030775461 | 相同 | 相同 |
| EIR-002 | C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/.venv-validation/Scripts/python.exe | 262144 | 560B9EF7D856608AB8DA02DED2DC8A1951AD1F424C382C0EC6A698874165A18E | 相同 | 相同 |
| EIR-003 | C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe | 107304 | B07B03B9BA866A341A3C13EE69710FBC8D43D4CE2523DEE13F6DF5C25378D15B | 不同 | 不同 |
| EIR-004 | C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python3.dll | 71984 | F91CA7E29E8B4CC9ED7A4A935C1B2558C5C8F23398CB20D7048F977AA16FCE8B | 不同 | 不同 |
| EIR-005 | C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python312.dll | 6985520 | 3B33D49D879DBF3A8AA3FFF1BF3859275E76C188A3ADEC4E7FFE728243652A87 | 不同 | 不同 |
| EIR-006 | C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/vcruntime140.dll | 124544 | D5E4D9A3E835FA679450145D6A7D94E36573A509317111904D9B3712C30D9066 | 相同 | 相同 |
| EIR-007 | C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/vcruntime140_1.dll | 49792 | 1F2D41C4AA5DB0BC33EBF7B66D72943A817D7CE6CBE880502A9403823633093F | 相同 | 相同 |

行号仅用于本候选内部定位，不是新建的正式证据准入标识。
结果分别为：对旧计划记录 4 相同 / 3 不同；对此前会话观测 4 相同 / 3 不同。
读取前后元数据比较相同为 7 项；它不是 7 项来源资格 PASS。

### 2.1 三项变化的历史比较值

下表两组历史值均只按既有记录使用，没有在本批次重新读取历史二进制来源。

| 行号 | 旧计划记录字节数 | 旧计划记录 SHA-256 | 此前会话观测字节数 | 此前会话观测 SHA-256 |
| --- | --- | --- | --- | --- |
| EIR-003 | 91648 | D8E3F0ADF246DB00358C0C4ED349CF714898178F9558FB0E944F79F5C07F8EAA | 107312 | B847BB9F4E48C19F585C8BF7D8B355F3F8C6D2125717ECE9C9D7E16FB9F09DE8 |
| EIR-004 | 56320 | 2D2330CE33D1443C67B1804BBF1A561653499DD4DCF8918048747CC17D1A63C4 | 71984 | FE6A4470D1F6BAD6A2BFEB7258884B94538A21A508CF8A23E4CA3EC74962CE49 |
| EIR-005 | 6969856 | 64A1DAD031E97F13B1A0BAC26C689D8E14A18D7DD1EAB06E17F70E22373F4EEC | 6985520 | 2B6FFFDE96CF24A57FCA642AAEFD5788816AB5EF8624EA63B722CBCEB94D49B1 |

字节数相同而 SHA 不同仍是文件身份差异。不能因文件名、长度相同或仍能找到路径
而沿用旧身份。差异本身不证明官方版本更新、恶意篡改、版本号或兼容性结论。

## 3. 配置、路径和过程限定

### 3.1 配置记录不等于实际解释器版本

从 EIR-001 同份已散列字节取得的原输出记录：

| 配置项 | 已记录值 | 资格 |
| --- | --- | --- |
| home | C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\python | 原输出按固定目录字符串比较匹配；不是规范根接受 |
| version | 3.12.13 | 配置文本值，不是实际解释器版本执行结果 |
| include-system-site-packages | false | 配置文本值，不证明执行时已落实 -S 或隔离能力 |
| 重复键或畸形配置行 | 原输出未报告 | 不代替独立配置解析器验证 |

当前基础解释器及库的实际版本、架构、来源真实性和兼容性均未由本候选验证。
不从配置的 3.12.13、旧资源版本、路径名称或 SHA 变化推导新版本号。
本次没有执行版本命令、读取新的版本资源或兼容性测试。

### 3.2 有限父目录观察

原输出只检查下列目录的存在及 ReparsePoint 属性，没有枚举目录内容：

- C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5
- C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/.venv-validation
- C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/.venv-validation/Scripts
- C:/Users/Administrator/.cache/codex-runtimes
- C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime
- C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies
- C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python

这些输出均未报告 ReparsePoint，但没有覆盖完整祖先链、全部解析行为、
对象持久身份、权限真实性或检查至使用完整性，也没有原子冻结七文件集合。
不能据此宣布 PROJECT_ROOT、VENV_ROOT、RUNTIME_ROOT 或 SYSTEM_ROOT 已被接受。
SYSTEM_ROOT 的来源、目录及 OS 依赖闭包未在这次 7 文件观察中取得。

### 3.3 观察与准入分开

准确路径及 SHA 只是待处置的身份事实，不产生读取、装载、运行或目录范围权限。
本候选不把共享运行时目录变成允许枚举的根，不把七文件扩大成完整依赖闭包。
未被观察的文件、来源或机制继续未绑定，不通过零计数或省略隐藏缺失。

### 3.4 原汇总过程记录保留

前一轮首次内存汇总因 JSON 段落边界定位假设不适用而失败；
随后对同一份已保存观测修正边界定位并完成比较，没有因此重新读取环境。
该失败属于汇总过程，不是运行时或候选执行失败；本候选保留其存在，
不宣称原流程首次全通过，也不将修复后的汇总当作新增来源证据。

## 4. 依赖、历史及重绑定准备

### 4.1 三层处置不得合并

| 层次 | 本候选能做什么 | 本候选不能建立什么 |
| --- | --- | --- |
| 身份记录 | 保留 7 项既有观测及两个比较基线 | 持续不变、官方来源、根可信性 |
| 准备与复核 | 明确差异、缺失证据、依赖和后续停点 | 环境准入、完整闭包、原子冻结、运行合格 |
| 可用性及执行 | 仅指出需要另外准确绑定和批准 | 不批准任何实际读取、装载、生成、测试或运行 |

即使本候选经静态复核或有限接受，也只接受其准确记录与限定，不能将任何
未核验项目转成已满足。不存在“新 SHA 已记录，所以环境已接受”的推论。

### 4.2 影响范围

| 对象 | 准备性处理 |
| --- | --- |
| 后续确实依赖 EIR-003、004、005 旧身份的环境、启动或闭包证据 | 不得将旧摘要当作当前匹配；在受影响使用前需另行准确重绑定及复核 |
| 已有限接受的类型合同和数组政策设计文档 | 保持原固定字节和接受范围；不因运行时差异自动重写或废止 |
| 第 1.2 节所引用的旧计划及此前观察 | 作为历史记录保留，不将旧值替换成新值并保留旧 SHA |
| 相关历史输出 | 仅在实际依赖及可证实时间范围足够时评估影响；没有证据时保留不确定性 |
| 未证明依赖这三文件的其他成果 | 不自动宣告失效，也不越权宣告全部未受影响 |

按依赖关系及可证实的时间范围，评估变化对后续使用和相关历史输出的影响。
正常版本更新不自动推翻历史结果；历史记录始终保留，不自动废止全部项目成果。
本候选没有开展历史资产调查、撤销、补测或重新验收，没有证明本次差异属于正常更新。

### 4.3 后续准确重绑定所需项目

以下是后续需要建立或核实的事项，不是本批次已经完成的准入门禁：

| 项目 | 仍需的准确依据 | 缺失时处理 |
| --- | --- | --- |
| 适用授权 | 明确对象、范围、读取方法及准备 / 使用阶段的批准 | 不能以本候选或旧批次授权替代 |
| 环境身份 | 完整解释器、配置、所需库及实际依赖关系 | 七文件观察不能代替完整环境身份 |
| 来源真实性与版本限定 | 可定位的来源及独立证据，适用版本 / 架构事实 | 未核验，不用名称、资源字符串或摘要猜测 |
| 根绑定 | 根来源、规范身份、解析器、大小写、重解析及独立处置 | 不从目录存在推定根接受 |
| 检查至使用完整性 | 准确机制、适用范围、证据及残余限制 | 不能用重复散列或顺序元数据比较冒充完整性控制 |
| 准确操作与范围 | bootstrap、loader、操作类别及用途 / 阶段的绑定 | 不能由文件身份扩展成执行许可 |
| 依赖与历史处置 | 真实依赖、可证实时间范围及必要的单独决定 | 不进行全项目自动废止或追溯追认 |
| 独立复核及 Owner 处置 | 对完成对象的分离固定 SHA 复核和准确决定 | 候选静态复核不转移为环境准入 |

如果共享运行时继续发生身份变化，在受影响后续使用前停止，记录差异并等待处置。
不以反复读取、反复计算 SHA 或补写记录替代稳定性控制，也不自动安装、复制、
换根、改权限或制造新环境。另选环境需要新的明确范围和授权。

## 5. 本批次静态复核边界与后续停点

独立静态复核仅核对本候选的：

1. 七文件行、字节数及完整 SHA 是否忠实于已保存观测。
2. 两个比较基线及 4 相同 / 3 不同的统计是否一致。
3. 版本、来源、时间和路径资格是否没有过度陈述。
4. 身份记录、候选接受、根 / 来源准入及执行是否明确分开。
5. 依赖和历史处理、全部 LIMITED 及原有记录是否保留。
6. 文档字节、表格结构及唯一新增文件范围。

复核不得重新访问七文件或环境，不通过测试补足来源，不创建另一份报告文件；
结论在会话中绑定本候选完成后的准确 SHA。不能预填未知运行或接受凭证。

本次物化不改变环境，不自动消费或建立后续准入、Manifest 生成、运行或审查权限。
任一物理来源改变都不能在旧文件中静默替换并沿用旧摘要或旧决定。
DSP-004 OPEN / HOLD；B-01、B-02 OPEN；全部 LIMITED 及历史记录继续保留。
