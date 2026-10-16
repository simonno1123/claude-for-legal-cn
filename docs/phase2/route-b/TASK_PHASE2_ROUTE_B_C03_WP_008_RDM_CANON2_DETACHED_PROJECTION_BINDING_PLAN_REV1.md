# Route B C03 / WP-008 — CANON-2 双层 detached 一致性候选计划 REV1

## 1. 授权与边界

本轮承接 Project Owner 的本项目批量继续指令，仅新增本地合成候选及验证记录，不修改任何已接受文件。起始 main 提交为 `a5ce2dd5b61d6c306689b0d2a0acee35ae1d7c57`。运行前固定保护清单为 70 个项目文件及 2 个本项目历史参考；它们具有不同历史状态，不因列入保护清单而全部成为已接受资产。

目标是连接全文字节散列与十五字段条目流散列的**数据一致性**，不是完成正式 Manifest、可信根、签名验证、来源准入、实际捕获、集成或部署。DSP-004 保持 OPEN / HOLD；B-01、B-02 保持 OPEN；全部 LIMITED 保留。独立 ACOS 与其他项目完全不在范围内。

## 2. 固定输入

| 角色 | 项目文件 | SHA-256 | UTF-8 字节 |
| --- | --- | --- | --- |
| scalar | `validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_CANDIDATE_REV1.py` | `532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4` | 8234 |
| tree | `validation/route_b_c03/wp_008/RDM_CANON2_STRUCTURAL_LAYOUT_CANDIDATE_REV1.py` | `F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87` | 9953 |
| binding | `validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_CANDIDATE_REV1.py` | `32535D3E4800E39E8AAF510166AD2AF04E0436D39E7C0BAD528B329D24E66821` | 5799 |
| validation | `validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_VALIDATION_REV1.py` | `944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476` | 13142 |

运行器固定使用 Python 可执行文件 `C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`，预绑定 SHA-256 为 `B847BB9F4E48C19F585C8BF7D8B355F3F8C6D2125717ECE9C9D7E16FB9F09DE8`，不发现或切换其他解释器。运行器本身的最终散列在执行前另行记录。

## 3. 唯一候选与玩具合同

新增 `RDM_CANON2_DETACHED_PROJECTION_BINDING_CANDIDATE_REV1.py`。输入仅为原生不可变 bytes 与原生 dict detached 数据，返回五元原生 tuple：

`(DATA_CONSISTENCY_ONLY_NO_SOURCE_OR_AUTHORITY, 全文字节 SHA, 条目流 SHA, 条目数, 字节总数)`。

合成文档只允许 aggregate、encoding、entries、projection_label、scope 五个根字段；detached 只允许 encoding、scope、document_sha256、aggregate_sha256、entry_count、byte_total 六个字段。它们只是局部玩具投影，不代表已批准的完整 Manifest 分组或模式。

- encoding 固定为 WP008-RDM-CANON-2；scope 固定为 LOCAL_SYNTHETIC_PROJECTION_ONLY。
- entries 使用既有十五字段顺序；文档对象键按 codepoint 排序；数组显式使用 SET_SORTED(category, root_id, relative_path, entry_id)。
- 合成条目上限 128，单条 byte_length 为 0 至 2^64−1，ordinal 为 1 至 128；总字节上限为 128×(2^64−1)。这些是本轮合成范围选择，不为正式 Manifest 补立数值政策。
- projection_label 仅作为非空、最长 128 字符的局部元数据，不证明身份。
- 全文散列覆盖原 bytes（含末尾 LF），包含 aggregate 字段；条目流散列仅覆盖十五字段流，不含 aggregate、标签或 detached 字段。
- 文档不得包含全文自散列字段，拒绝非规范字节而不自动修复。
- 同时核对文档内 aggregate、detached 和独立计算的条目数、字节总数、条目流 SHA。所有 SHA 必须为完整大写 64 位十六进制。
- detached 是调用方数据，可被调用方与正文一起重算。局部浅复制并不提供并发原子冻结、来源真实性、权限或新鲜度。

## 4. 预先声明的验证

预计 106 个局部断言、3 个正向字节向量；必须逐项通过，不以运行器退出成功替代测试结果。若失败，保存真实失败并停止本轮交付，不改写成成功。

三个正向向量：单条、双条、大于有符号 64 位上界的整数与中文/非 BMP 路径。预期规范条目 JSON 文本及十五字段 tokens 在验证器内独立写明，不调用被测编码器制造预期；只对这些受限合成值使用标准 JSON 来构造负例。大整数在观察摘要中转十进制字符串，在原向量中保留字节，避免跨语言数值转录损失。

覆盖：返回原生 tuple 与整数、元数据不被改写、正文标签改变但聚合不变、全文 stale 拒绝、detached 缺失/多余/类型/范围/SHA 格式与不匹配、CRLF/缩进/末尾 LF/重复键/BOM/非法 UTF-8/非对象、正文 scope/encoding/aggregate 不匹配、自散列字段、条目字段类型与溢出、路径/相位/loader/类别/重解析状态/序号/重复身份/顺序、空条目和 129 条目。

另有明确反例：调用方改变标签并重算全文 detached SHA 可以得到一致性 tuple，**只能证明两份调用方数据一致，不能建立来源或操作权限**。

## 5. 私有运行与证据

只执行固定本项目运行器；它将四份固定源码快照通过 stdin 送入新 Python 子进程，使用 -I -S -B、清空继承环境，仅留系统路径与 UTF-8 配置。先严格 UTF-8、SHA/长度及 AST 检查，再编译同一快照。两个依赖仅以预先固定名称注册到当前子进程模块缓存，结束时只删除自己仍拥有的两个缓存槽位。

这不是 OS 安全沙箱，不是生产装载器、来源准入或项目集成；缓存槽位移除也不等于所有对象已销毁或内存抹除。运行器自身及解释器需要原有可信本地环境，本轮不解决 B-01 的可信根与预先授权。

局部输入等待 5 秒、子进程等待 30 秒、停止/流等待各 5 秒；输出 262144 字节检查在收集后进行，不是在线内存硬限制、整机物理停止或任意子孙进程终止保证。

保留原始 stdout gzip/长度/SHA、严格 UTF-8 解码后的 LF 规范观察记录 gzip/长度/SHA、退出码、stderr 字节数、实际耗时、解释器版本、两个缓存槽位清理结果。后续仅用 apply_patch 写入新归档文件，不由测试写文件。

## 6. 交付与剩余缺口

计划交付六个新增文件：候选、验证器、运行器、本计划、观察 JSON、结果报告。执行前进行静态格式/范围检查；执行后重新核验固定文件、向量字节、摘要与逐项计数。阶段备份仅提交这些已审查文件，不表示候选被接受。

不产生正式隐私/安全结论，不调用 Gemini 或任何外部审查模型，不接触真实案卷、身份、凭据、OCR、业务来源或外部提供商。B-02 的正式完整 typed contract、所有数组政策来源与批准、全文 detached 权威绑定仍未建立。通用一致性工具不代替上述治理批准，也不关闭任何既有 LIMITED。
