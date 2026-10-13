# DSP-004 D-007 私有字节与固定 helper 交接批次 REV1

## 授权范围

Project Owner 对前述 D-007 新私有合成字节交接批次明确回复“批量授权”。允许另建候选、静态核对、隔离合成验证、结果复核及阶段备份；不读取或复用旧私有字节，不修改已接受文件、不读取真实 Driver，不准入来源、不实际捕获、不集成，不涉及独立 ACOS 或其他项目。新候选不会自动接受，DSP-004、B-01、B-02 不因该批次关闭。

唯一新候选源码：`validation/route_b_c03/wp_008/DSP_004_D007_PRIVATE_BYTE_FIXED_HELPER_HANDOFF_CANDIDATE_REV1.cs`。固定被测函数为 `Test-DSP004DriverBytesInMemory`，唯一参数为 `Payload`。控制端完整 SHA-256：`891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB`；固定长度 25573 bytes。清单独立预期来源完整 SHA-256：`46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C`。

## 封闭接口与字节准备

候选只有一个无参固定入口，私有构造器，没有外部数组、路径、脚本、回调、runspace、权限 flag 或失败对象输入。每个编译程序集只预留一次本地请求；第二次请求不读源、不创建数组、不装载或调用 helper。此门不是全局一次性授权服务。

在候选内新建一个原生 byte[]，长度 20177，全部 byte 0。该数组不导出、不持久化；摘要用独立于 helper 的准备调用 `SHA256.Create().ComputeHash` 预先计算。仅与记录字面量 `6405563F9A39B39F8E63D4330C497A76C99B38F4FE4662B0A6E310F355B69210` 比较，不验证真实 Driver。接口独立不等于密码学 provider 独立、可信根或正向来源验证。

外侧测试可独立构造另一份合成数组作摘要 oracle；它从不传给候选或被测函数，不能代替候选的私有准备字节，且不复用历史摘要结果。

## 固定装载与同引用调用

读取唯一控制端的一份字节快照，验证完整 SHA/长度、严格 UTF-8 解码，AST 只允许十个已知顶层函数定义。完整定义仅装载到新空白 FullLanguage runspace 一次；该模式不是 OS 沙箱或完整依赖可信证明。不调用其他顶层函数、未来 Bootstrap、单案例入口、Python 或真实 Driver。

准备字节和摘要前置完成后，创建唯一固定命令及一个命名参数；确认命令结构、参数名及参数 Value 与准备数组在调用者侧 `ReferenceEquals`。只有这些条件成立才尝试一次 helper Invoke；返回后再次核对同一命令参数引用与零字节形状。

引用观察仅限定为调用者命令参数槽。不能声称直接观察到了 callee 参数引用、其内部 clone 与原数组同一对象、全过程不可变或 freeze。已有控制端明确在 helper 内创建本地 clone，本批次不改写该行为。

## 返回比较、失败和清理

实际返回必须为一个六字段对象，全部原生 string，字段名精确；TextCheck 预期为 FIXED_DRIVER_SHA_MISMATCH，其余固定字段仍为 NOT ESTABLISHED / NOT IMPLEMENTED / NOT OBSERVED。原生比较先于 JSON，不用被测返回生成 oracle或权限。

装载与调用分别记录所有输出通道。异常与清理异常原对象仅在当前进程私有记录保留，公开输出限类型、阶段和计数，不输出 Message、堆栈、字节数组或源文本。清理失败不替换首要失败，也不恢复正常完成资格；Close/Dispose 返回不证明所有引擎/资源收敛。没有同步调用硬时限证明。

观察只计一次新的 D-007 局部 helper 核对，重复拒绝是该新候选的门检查，不增加清单项。与此前 188 个不同 ID 作身份去重后，才可描述清单的局部纯函数覆盖；不转移旧 P/私有槽证据，不宣称正式 189 项接受、执行资格或真实隔离。保留全部 LIMITED、正向 SHA NOT COVERED、DSP-004 OPEN / HOLD、B-01/B-02 OPEN。
