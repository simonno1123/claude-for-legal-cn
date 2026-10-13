# DSP-004 所报读写记录分类 REV1：实际本地观察

## 范围与绑定

Project Owner 已在本会话“接受并继续”，有限接受异常并存候选固定源码 `06D2729B96BEBE2EB3A29CEF66B91982CD3ABE73B0491D6BEE37C903A4E830D9`，保留全部 LIMITED。本批次继续仅本地合成核对，不将该决定扩大为集成、真实来源或实际捕获授权；新验证入口不是新 Owner 接受决定。

| 新资产 | 实际 SHA-256 | 格式 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_REPORTED_RW_CLASSIFICATION_PLAN_REV1.md` | `6FF835CA227F4965C0324678D88C3EC49AE1335408D9493BFAB8B671D3BE71A3` | 4156 UTF-8 bytes / 40 LF |
| `validation/route_b_c03/wp_008/DSP_004_REPORTED_RW_CLASSIFICATION_VALIDATION_REV1.ps1` | `FBF43F9789E1034D91B944DBAAE76CF09BC46C659985874809803310B995F1E8` | 18807 bytes / 251 LF |
| `validation/route_b_c03/wp_008/DSP_004_REPORTED_RW_CLASSIFICATION_REV1_OBSERVED_RESULT.json` | `492EE32855FDA4E8FABF34586A677BD9BBB3F7CAF377D1BDDF9D2B96C5809451` | 168431 bytes / 6493 LF |

固定清单源 `46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C`（70284 bytes）及控制端 `891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB`（25573 bytes）在入口内先读取同份字节快照、核验 SHA/长度、严格解码。清单不执行；控制端完整快照经 AST 检查十个已知顶层函数定义后，在新空白 FullLanguage runspace 装载一次。此方式不证明 OS 沙箱、可信依赖、函数冻结或全部执行能力。

## 原生比较与实际结果

单次验证入口退出码 0，`LOCAL_REPORTED_RW_CLASSIFICATION_CHECKS_PASS`；390 个唯一检查全部 true，0 个 false，无入口级失败类型或清理失败记录。六项前置检查加 96 项各四项检查（通道、对象表面、值、限定语），不是 390 个清单案例。

| 清单组 | 实际直接分类函数调用 | 完成原生比较 | 作用 |
| --- | --- | --- | --- |
| RD-001 至 RD-052 | 52 | 52 | 所报读记录分类、原生 Int32/null After、检测字节分类 |
| WR-001 至 WR-044 | 44 | 44 | 所报写记录分类、进度不确定性和固定否定字段 |
| 合计 | 96 | 96 | 仅上述两个纯分类函数，不是实际 I/O |

输入按照原清单构造并保留 String、Int32、Int64、Boolean 或 null。错误类型、大小写、零/负数请求、超量返回、stop/local-close 优先级逐项比较；序列化之前核对原生属性类型和精确字符串。WR-043/044 的 Int64 没有变为 Int32，字符串数字没有转为整数；JSON 同时保存原始 token 和原生类型名称，但 JSON 自身仍不保持 CLR 类型身份。

| 实际分类 | RD 数量 | WR 数量 |
| --- | --- | --- |
| 正常正文计数 / 正常所报全范围任务 | 3 | 2 |
| 正常正数请求返回零 | 3 | 不适用 |
| 检测字节拒绝 | 4 | 不适用 |
| 原任务 pending | 1 | 2 |
| 原任务失败 | 3 | 5 |
| 等待包装失败 | 不适用 | 5 |
| stop / local-close 保护 | 6 | 6 |
| 无效所报记录 | 32 | 24 |
| 合计 | 52 | 44 |

上述“正常”“失败”“等待”等为传给纯函数的合成声明，不是新观察到的真实任务历史。RD 零返回分类没有获得 ActualPeerEof；WR 正常分类没有 WriteByteCount、子端收取、EOF 或 SHA 确认。所有固定否定字段保持原返回字面量，CaseCompletion 为 NOT ESTABLISHED。

装载返回输出数 0；每次分类返回恰好一个预期对象，错误/警告/调试/详细/信息/进度通道均为 0。输入/原生返回比较完成后才将结果转换为 JSON。观察文件保存本次工具输出的完整父侧解析对象，按两空格/LF 排版，不是未修改的原始控制台 transcript。

## 保留边界

38 份既有保护文件与完整 SHA 绑定对照保持一致。新批次不调用单案例入口、未来 Bootstrap、Driver 检查或 Python，不执行清单源，不读取四个上游路径，不启动测试子进程。runspace Close/Dispose 调用返回只作为局部观察，不证明全部资源收敛。

本批次不执行 M 6、RQ 18、D 7、F 62；先前其他载体的检查数不能补为本清单的执行记录。主协调员只作静态和结果交叉核对，未调用独立子审查员或 Gemini，不称为独立双审。

保留全部 LIMITED；DSP-004 为 OPEN / HOLD，B-01、B-02 为 OPEN。新文件和阶段备份不构成新候选接受，不建立来源准入、实际捕获、集成或独立 ACOS 操作权限，也不建立完整 189 项或总体通过结论。
