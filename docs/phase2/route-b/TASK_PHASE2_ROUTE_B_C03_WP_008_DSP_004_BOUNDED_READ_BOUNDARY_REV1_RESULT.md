# DSP-004 受限字节读取局部验证 REV1 — 实际结果与范围

## 1. 实际结论

本批首次完整运行结果为 **LOCAL_SYNTHETIC_BOUNDED_READ_CHECKS_PASS**：20 个封闭合成场景、187 个唯一检查全部符合运行前冻结预期，失败检查为 0。入口退出码 0、stderr 0 bytes，严格 UTF-8／JSON 接收错误为 null。

17 个场景获得方法结果，其中 6 个标记 Overflow、11 个标记 Eof；另外 2 个任务 Faulted、1 个任务 Canceled，均未释放 BoundedRead 结果。正常任务完成不等于正文可用，保护性故障／取消也不计为测试失败。

重要限定：提前 EOF 场景只记录到 3 bytes，而合成输入长度为 8。受测方法不知道预期来源长度，因此 Eof 只证明测试流返回过零字节，不证明完整来源或业务材料完整性。

DSP-004 保持 OPEN / HOLD，B-01、B-02 保持 OPEN，全部 LIMITED 和既有失败历史保留。本批不构成正式 WP-008 执行、结果接受、来源准入、真实捕获、业务集成或部署。

## 2. 固定身份

受测源码：validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_SUPERVISOR_CANDIDATE_REV2.cs，24173 bytes，SHA-256 为 9B165A04AFE786224965C5E33364140265FF3CB0B4B99A8E63A7AE7562C33E4E。

固定已有 PowerShell 运行文件 SHA-256 为 362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139，完整路径见本批计划。没有安装或更新运行环境。

本批共新增五份资产，包含本结果文档。路径相对本项目根目录，本结果文档不在自身正文中自绑定散列。

| 新资产 | SHA-256 | bytes |
| --- | --- | --- |
| validation/route_b_c03/wp_008/DSP_004_BOUNDED_READ_SYNTHETIC_FIXTURE_REV1.cs | 00EC5B2D1A6998E1E59319EBDD64C30481AF5B38A142155D9D407B19A55893B0 | 3209 |
| validation/route_b_c03/wp_008/DSP_004_BOUNDED_READ_BOUNDARY_VALIDATION_REV1.ps1 | 0EBDD2137D7260C3428B0A198D28C4C91134DCDF1A3B6A30B9D71EA200ED4AF6 | 16918 |
| validation/route_b_c03/wp_008/DSP_004_BOUNDED_READ_BOUNDARY_REV1_OBSERVED_RESULT.json | 6FDAB9BC2DCD79A8D290D0E417311CD5FCA79E199DA83E42F1AB2A09AE596B52 | 11272 |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_BOUNDED_READ_BOUNDARY_PLAN_REV1.md | C47A9E0B08CC16BE5F5017DF4BF16641BE851404F21ADA44FAFCF069EFE36EBA | 8780 |

新增 C# 内存流仅为测试支架，不是业务组件物化，也不改变已接受源码、公开 API、流预算常量或超时策略。新测试入口／支架不因测试通过而自动获得治理接受。

## 3. 实际调用与观察方式

1. 先核对受测源码、测试支架、固定运行文件的完整身份。
2. 在新的固定 PowerShell 测试进程内编译同份受测源码和新内存流。仅反射调用私有 ReadBounded(Stream, int)，不调用 RunStage、公开组合批次、时钟闸门、业务控制端或任何子进程阶段。
3. 所有输入均由固定 i % 251 模式在内存创建。测试流按预置分段与调用序号立即返回数据、异常任务、取消任务或提前 EOF；没有真实管道、文件、套接字或案件材料输入。
4. 每项先记录原生任务状态，再检查正常结果的 Count／Overflow／Eof、原生 byte[] 和逐字节正文；异常及取消项不以空正文冒充合格结果。
5. 两个 IOException 场景在同一测试进程中使用 ReferenceEquals 核对原始异常对象；3 个实际读取异常对象留在该测试进程的私有列表中，输出只含类型和引用检查布尔值，不输出 Message 或 StackTrace。
6. 传入流由测试入口创建与 Dispose，受测方法未 Dispose 这些流。每项 Dispose 均返回；这只是合成支架所有权观察，不是实际资源收敛或清理失败验证。

## 4. 逐场景实际结果

NONE 表示没有 BoundedRead 结果，不能视为零长度成功结果。所有列均与预置独立预期相符。

| ID | 原生任务状态 | Count | Overflow / Eof | 正文 bytes | 流返回 bytes / 读取次数 |
| --- | --- | --- | --- | --- | --- |
| BR-001 | RanToCompletion | 0 | false / true | 0 | 0 / 1 |
| BR-002 | RanToCompletion | 1 | true / false | 0 | 1 / 1 |
| BR-003 | RanToCompletion | 0 | false / true | 0 | 0 / 1 |
| BR-004 | RanToCompletion | 1 | false / true | 1 | 1 / 2 |
| BR-005 | RanToCompletion | 2 | true / false | 0 | 2 / 1 |
| BR-006 | RanToCompletion | 3 | false / true | 3 | 3 / 2 |
| BR-007 | RanToCompletion | 4 | false / true | 4 | 4 / 2 |
| BR-008 | RanToCompletion | 5 | true / false | 0 | 5 / 1 |
| BR-009 | RanToCompletion | 4095 | false / true | 4095 | 4095 / 2 |
| BR-010 | RanToCompletion | 4096 | false / true | 4096 | 4096 / 2 |
| BR-011 | RanToCompletion | 4097 | true / false | 0 | 4097 / 2 |
| BR-012 | RanToCompletion | 262143 | false / true | 262143 | 262143 / 65 |
| BR-013 | RanToCompletion | 262144 | false / true | 262144 | 262144 / 65 |
| BR-014 | RanToCompletion | 262145 | true / false | 0 | 262145 / 65 |
| BR-015 | RanToCompletion | 5 | true / false | 0 | 5 / 5 |
| BR-016 | RanToCompletion | 8 | false / true | 8 | 8 / 4 |
| BR-017 | Faulted | NONE | NONE / NONE | NONE | 0 / 1 |
| BR-018 | Faulted | NONE | NONE / NONE | NONE | 3 / 2 |
| BR-019 | Canceled | NONE | NONE / NONE | NONE | 0 / 1 |
| BR-020 | RanToCompletion | 3 | false / true | 3 | 3 / 2 |

关键点：

- BR-001、BR-002 验证 budget 0 的空流与首个检测字节；后者返回计数 1、Overflow=true、Eof=false，正文是原生空 byte[]。
- BR-003 至 BR-014 分别覆盖 budget 1、4、4096、262144 的空／低于／等于／多一个字节边界。超额观察可计入一个检测字节；不把 Count 大于预算一字节本身认定为无限制正文放行。
- BR-015 输入长度 9、budget 4、分段大小 1，实际只读取 5 bytes 即返回超额，不继续消耗剩余 4 bytes。它不承诺排空或完整来源。
- BR-016 以最大 3-byte 分段返回恰好 8 bytes，再观察 EOF。记录读取次数 4，说明短读取不被误判为 EOF。
- BR-017 与 BR-018 的异常类型均为 System.IO.IOException。分别在读取前和已返回 3-byte 前缀后失败，未释放结果，原始异常引用均相同。
- BR-019 的异常类型为 System.Threading.Tasks.TaskCanceledException，任务状态 Canceled，不被改写为普通 EOF 或正常结果。
- BR-020 在输入尚有 5 bytes 未读时模拟 EOF。Count=3、正文 3 bytes、Eof=true，限定为流层观察，不能用于宣称来源完整。

所有正常结果的正文在入口内逐字节比较；超额结果均比较为原生空 byte[]。接收侧依据独立输入模式、预置长度与前缀重建期望散列，核对正文长度和 SHA-256；归档不包含大段合成正文，因此不把接收侧散列检查说成第二次独立逐字节重放。

## 5. 检查数量与完整归档

| 检查组 | 实际数量 |
| --- | --- |
| 固定身份与方法／类型形状 | 5 |
| 20×7 项任务、结果隔离、计数、所有权、测试清理、输入不变 | 140 |
| 17×2 项正常结果字段与原生逐字节比较 | 34 |
| 原始 IOException 引用检查 | 2 |
| 取消任务／异常检查 | 1 |
| 后置计数、源码及支架未变、检查总数 | 5 |
| 合计 | 187 |

187 项全部为 true，ID 集合与 20 个有序场景 ID 完整、唯一。该数量不等于 187 个独立场景，不与原 189 项或前几批局部测试相加作为正式覆盖率。

| 观察身份 | 实际值 |
| --- | --- |
| 原始 stdout bytes | 41488 |
| 原始 stdout SHA-256 | C11F70D002618F378DDC896318740296034EF1E5BE0A3024B9DB08508664ACC5 |
| 原始 stdout gzip bytes | 3674 |
| LF 规范化完整记录 UTF-8 bytes | 40004 |
| LF 规范化完整记录 SHA-256 | B3655E83D38933D921C8F692B7F33F5F5138F9FFA68B3305CEDBFD6146A4C174 |
| 规范化记录 gzip bytes | 3665 |
| 入口退出码／stderr bytes | 0 / 0 |
| 外侧等待预算／实际观察 ms | 30000 / 2423 |
| 外侧等待触发 | false |

外侧 2423 ms 包括该测试进程启动、编译、执行、输出采集和本地 Dispose 观察；不是单独方法耗时、性能基准或硬停止保证。30000 ms 仅为本批有限采集等待点，不改变受测监督器原 120000 ms 预算。

归档同时保留原始 stdout 的 gzip/base64 及 LF 规范化完整记录的 gzip/base64，含每项预期、实际、输入及正文散列、读取计数、异常类型与全部检查。原始输出经严格 UTF-8 解码、CRLF 换成 LF并补最终 LF后精确得到规范化记录。

## 6. 复核、保护及备份范围

接收复核由主协调员另行执行，不冒充独立代理或第三方模型：

- 复核两份归档的 gzip 长度、解压长度和 SHA-256，拒绝重复 JSON 属性名，比较 Summary 与完整记录。
- 按运行前冻结的独立表逐项核对 20 个场景、187 个检查、原生任务状态、计数及结果释放边界。
- 用单独生成的 251-byte 固定模式重建预期输入与前缀，检查输入不变、正文长度／散列与故障／取消隔离。
- 运行前后对 38 份既有文件检查长度和 SHA-256，全部相同。集合来自计划中四个固定结果文档及其身份表；并非声称 38 份文件都获得过同一种接受。
- 新入口静态解析错误为 0；新增文件按严格 UTF-8、最终 LF、无尾随空白检查，并扫描常见秘密特征。未命中特征不等于一般秘密泄露证明。
- 本批只备份五份新增本项目合成资产，不改写已接受文件或历史失败。普通提交／推送与 CI 状态不代表治理接受、来源准入或下游授权。

## 7. 仍未覆盖

本批所有测试流任务立即完成，不证明真实异步调度、阻塞 I/O、管道压力、读超时、取消竞态、字节流在真实进程间的行为或完整后代资源收敛。

未使 Dispose／Kill／Wait 本身失败，未验证原失败与清理失败在真实流程中的并存处理。原始 IOException 引用身份只覆盖本测试进程，不扩展为跨进程保留。

不复跑 RunStage、公开组合监督器、原 189 项或先前 JSON 用例；不覆盖真实 Driver 正向 SHA、可信根、完整依赖闭包、来源授权或材料完整性。

本批没有访问独立 ACOS 或其他项目，没有来源准入、真实捕获、业务集成或部署。DSP-004 为 OPEN / HOLD，B-01、B-02 为 OPEN，全部 LIMITED 和历史失败继续保留。
