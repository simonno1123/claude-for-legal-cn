# Route B C03 / WP-008 — CANON-2 双层 detached 一致性候选结果 REV1

## 1. 本轮结论与效力

**LOCAL SYNTHETIC DETACHED CONSISTENCY OBSERVED ONLY — 106 / 106 CHECKS；3 BYTE VECTORS。**

本轮新增一个纯数据候选，将完整合成文档 SHA 与十五字段条目流 SHA、条目数、字节总数进行双层一致性核验。候选、验证器、私有运行器、事前计划、原始观察归档和本报告为六个新增项目文件；未修改已有文件。

这不是完整 Manifest 或可信装载器，不是来源/签名/授权/新鲜度核验，不生成正式 Manifest，不建立接受决定。候选状态为 **PREPARED / LOCALLY CHECKED — NOT PROJECT OWNER ACCEPTED**。DSP-004 保持 OPEN / HOLD；B-01、B-02 保持 OPEN，全部 LIMITED 保留。备份不构成治理接受。

## 2. 事前固定与新增资产

执行前已物化计划，固定 106 个局部断言、3 个字节向量及四份输入快照。受保护的 70 个项目文件和 2 个本项目历史参考在运行前后均未变；保护清单不意味着全部资产具有相同接受状态。

| 新增文件 | SHA-256 | UTF-8 字节 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_CANDIDATE_REV1.py` | `32535D3E4800E39E8AAF510166AD2AF04E0436D39E7C0BAD528B329D24E66821` | 5799 |
| `validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_VALIDATION_REV1.py` | `944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476` | 13142 |
| `validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_LOCAL_RUN_REV1.ps1` | `20AD3881CB7EAD15930290537AE1921B617909F51D950CC21704C6695D2612E2` | 10172 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_CANON2_DETACHED_PROJECTION_BINDING_PLAN_REV1.md` | `BC93B49AF201F8E33D04CC477BA7CEA7EF5376CF55F71930B04C984680FE3939` | 6803 |
| `validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_REV1_OBSERVED_RESULT.json` | `5F3755FC6CB37BE210710FC8CB0287ABB0EDDAC6CEF550F9A7F557081701B63C` | 10762 |

两个原有固定依赖保持原样：标量/十五字段编码候选 `532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4`（8234 字节），结构布局候选 `F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87`（9953 字节）。使用它们不追认其正式接受或准入。

## 3. 实际局部运行

| 观察项 | 实际记录 |
| --- | --- |
| Python 可执行文件 SHA-256 | `B847BB9F4E48C19F585C8BF7D8B355F3F8C6D2125717ECE9C9D7E16FB9F09DE8` |
| 实际 Python 版本 | 3.12.14 |
| 启动模式 | -I -S -B；清空继承环境后只留系统路径与 UTF-8 设置 |
| Bootstrap UTF-8 SHA-256 | `9E458D4BF84ADD637378E569D93C7EE4D1290DD4DBE37A21AD3BA7836186D085` |
| 子进程数 | 1 |
| 实际等待耗时 | 590 ms |
| 退出码 / stderr 字节 / 超时 | 0 / 0 / false |
| 完成的检查 / 字节向量 | 106 / 3 |
| 两个依赖缓存槽位清理 | scalar 与 tree 均为 OWNED_ENTRY_REMOVED |
| 原始 stdout 字节 / SHA-256 | 15751 / `81161C6602A6EAC5DFE977E2F277B959A829CFD77792093B24CF901AAAA2D154` |
| LF 观察记录字节 / SHA-256 | 15751 / `81161C6602A6EAC5DFE977E2F277B959A829CFD77792093B24CF901AAAA2D154` |
| 原始与 LF 记录 gzip 字节 | 3200 / 3200 |
| 完整记录结果 | LOCAL_SYNTHETIC_DETACHED_CONSISTENCY_OBSERVED_ONLY |

观察 JSON 同时保存原始 stdout 和 LF 观察记录的 gzip / Base64、长度、SHA、固定输入身份、退出码及局部预算。原始 stdout 已是 LF，因此本次二者字节与 SHA 相同；仍分别保留，未用摘要替换原始输出。完整记录内有每项 Check、三个 DocumentBase64 / StreamBase64、两层 SHA、条目数及十进制字节总数字符串；大整数未经 JavaScript/PowerShell 浮点转录。

运行后从归档解压重算两层记录 SHA，严格 UTF-8 / JSON 重复键检查，确认 106 个检查 ID 唯一且均为 PASS，核对摘要与正文一致。再以独立 .NET JSON token / BigInteger 路径，从归档文档的十五个字段重建条目流，逐字比对三个流及数量/总数，不重新运行被测候选。

## 4. 分项结果

| 局部组 | 检查数 | 结果与范围 |
| --- | --- | --- |
| P：三个正向向量 | 18 | 原生五元 tuple、固定非权威限定语、两层 SHA、原生整数计数/总数、调用方元数据未改写 |
| L：正文与聚合分离 | 5 | 标签改动但聚合不变；旧全文 SHA 拒绝；重算后的调用方数据只返回一致性，不产生授权 |
| D：detached 字段 | 39 | 原生类型、精确字段集、scope/encoding、64 位大写 SHA、整数范围及不匹配拒绝 |
| R：原 bytes / 规范布局 | 12 | 字符串/bytearray/超长、CRLF、LF、缩进、重复键、BOM、UTF-8 和根类型拒绝 |
| B：正文与条目一致性 | 30 | 正文 scope/encoding、标签、自散列、aggregate、条目类型/范围/顺序/重复身份、空集和 129 条目拒绝 |
| Q：输出效力界限 | 2 | 返回值无权威成员；固定限定语不输出 PASS 或治理结论 |
| 合计 | 106 | 仅本轮有限合成范围，不作总体覆盖率或业务完成比例 |

正文 entries 的字节 SHA 字符串均是合成 fixture 值，不是读取真实文件后获得的身份事实。无来源文件、真实根目录或业务记录被送入候选。

### 三个独立字节向量

| 向量 | 完整文档 SHA-256 | 十五字段流 SHA-256 | 条目数 | 字节总数（十进制原文） |
| --- | --- | --- | --- | --- |
| P-ONE | `B8EF6C02B75D367EE342B0219CA82693FD3718EF345232425381174907E1E43B` | `ABEA0FF04EE8FA92AFAE4AA647CC54B37F684E1EEF002406015F6656CB6175DF` | 1 | `7` |
| P-TWO | `04E6860D94635D2B9A4D0C09291894F4B65CB1A0DBD4724882D8BB46C27A237B` | `3A7CBC18A01A85567CA43EDFF235307543291E04C1DC2B1476927F573FF48F7E` | 2 | `18` |
| P-LARGE-UNICODE | `68A81300A77795B8C6A8B13033224DC498A40C83F932900BDA18B109021BC834` | `71676357B2DAE7CC1FBBA758B5AF596CC5DDFD03ECA3171E35297F613C5A0362` | 1 | `9223372036854775817` |

验证器的条目规范 JSON 文本与预期十五字段 tokens 独立写明，不调用被测编码器生成预期。独立负例构造使用标准 JSON，仅适用于这些受限合成值，不据此替代通用 CANON-2 编码规则。

## 5. 最重要的反例与限制

标签由 fixture-alpha 改为 fixture-bravo，不影响条目流 SHA，但改变完整文档 SHA；继续提交旧 detached 全文 SHA 时，候选拒绝 DOCUMENT_SHA_MISMATCH。调用方若同步重算 detached 全文 SHA，候选返回：

`DATA_CONSISTENCY_ONLY_NO_SOURCE_OR_AUTHORITY`

这正说明**散列一致不是来源可信**：原 bytes、正文 aggregate 与 detached 都可以是同一调用方构造的数据。无可信根、准备授权、外部签署/批准或角色分离时，不能据此建立来源准入、执行权、新鲜度或治理接受。

本轮合同只有 aggregate、encoding、entries、projection_label、scope 五个玩具根字段和六个 detached 字段；128 条目、uint64 单条长度等是本轮显式合成范围，不是正式 Manifest 政策。仍不覆盖完整 Manifest 分组、所有数组政策来源、根目录/大小写/重解析别名证明、运行依赖闭包、角色授权或真实来源内容散列比对。

私有进程以固定名称装入两个依赖模块，只在当前新进程内使用固定快照，非业务集成或生产装载。删除自身缓存槽位不保证所有对象被销毁或内存被抹除；-I -S -B 也不是 OS 沙箱或任意不可信代码隔离证明。继承环境精简不消除解释器、OS 和本地控制端原有信任依赖。

输入等待 5 秒、运行等待 30 秒、停止与输出流等待各 5 秒；262144 字节输出检查在捕获后进行，不是在线内存硬上限、整机物理停止或所有子孙进程清理保证。真实故障、并发冻结、跨子进程身份链和外侧硬停止 LIMITED 全部保留。

## 6. 失败记录与自检边界

本轮 Python 测试子进程一次执行完成，未出现候选测试失败。准备阶段第一次只读散列清单查询因 PowerShell foreach 后直接接管道触发 ParserError；该查询未运行 Python、未写文件，改为数组表达式后恢复。本报告不将该工具语法错误隐瞒为“全过程零错误”。

完成的是本地执行与交付静态复核；未调用独立子代理或 Gemini，未声称获得独立外审。新文件已核对严格 UTF-8、LF/末尾换行、尾空白、Markdown 表格列数与常见私钥/API-token 模式；模式扫描无命中仅是有限筛查，不是普遍无敏感信息保证。

## 7. 后续状态

| 项目 | 保留状态 |
| --- | --- |
| 新候选接受 | 未发生；不得由本报告或 Git 备份代行 Project Owner 决定 |
| DSP-004 | OPEN / HOLD |
| B-01 可信准备根及事前权限 | OPEN |
| B-02 正式完整合同与 detached 权威绑定 | OPEN |
| 正式 Manifest / 来源准入 | NOT CREATED / NOT AUTHORIZED |
| 实际业务捕获 / 业务集成 / 部署 | NOT AUTHORIZED |
| 所有既有 LIMITED、原失败及历史观察 | RETAINED |
| 独立 ACOS / 其他项目 | 未访问、未修改 |

本轮技术补强到此闭合。下一层可信准备记录、完整合同政策或准入决定不能从调用方重算的 SHA 自动产生；不据此宣布全项目跑通或授权任何真实业务路径。
