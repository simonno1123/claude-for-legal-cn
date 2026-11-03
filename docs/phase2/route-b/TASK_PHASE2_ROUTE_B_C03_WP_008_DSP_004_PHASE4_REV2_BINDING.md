# DSP-004 阶段 4：第一版审查结果与第二版绑定

阶段 4 第一版（输入候选 REV3 与 Harness REV1）的审查，发现了 2 个阻断项。审查者是全新子代理，与记录人属于同一模型家族。审查也确认了几件事：REV3 只改了声明要改的键；新增的 13 条规则逐条对照源码，推导都正确；人工抽查的 12 个变体全部吻合。

按审查意见，记录人做了输入候选 REV4 和 Harness REV2，并在任何运行之前按确切字节绑定。第一版的文件保持原有字节不变。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_INPUT_CANDIDATE_REV4.json` | 115428 | `685BBCBF13BF96746E6DE4201C1FCE72B667CD6A07D0CE0902D9EF9A6C4235C1` |
| `validation/route_b_c03/wp_008/dsp004_phase4_harness_rev2/harness_rev2.py` | 22043 | `4A4B859405D31AD5716615E7FE5FF0330143BB48F2AAB83BC487CC9CE786D7B7` |
| `validation/route_b_c03/wp_008/DSP_004_PHASE4_REV2_BINDING.json` | 4558 | `D6DA41B9ED8593E49DE7EABF6FDA2AE9C0CEB98FC709DA3677EAE01246FE7D6D` |

| 编号 | 级别 | 问题 | 处理 |
| --- | --- | --- | --- |
| B-1 | BLOCKING | state compared by value only; wrong enum class or str subclass could pass; class checked by name | fixed: native types checked by identity (exact bound class, exact enum class, exact str) |
| B-2 | BLOCKING | an existing __pycache__ .pyc could run different code while hashes pass | fixed: subject built from the hashed bytes by a private importer; no sys.path entry; no .pyc read |
| M-1 | MAJOR | CR-010-NO-RELEASE mapped to the kill fixture | fixed in input REV4: unmapped |
| M-2 | MAJOR | six-side 'actual' was a literal dict, described as captured | fixed: separate capture function reads a context object and provider instance; input text says what it is |
| M-3 | MAJOR | no V3.2 pre-import scan or guards | fixed: AST import/call scan of subject bytes before import; audit hook blocks network, process, writes and removals |
| m-1 | MINOR | input could choose attributes via getattr | fixed: object-type allow-list; enum lookup by member name |
| m-2 | MINOR | unused overrides ignored | fixed: stop |
| m-3 | MINOR | whole scripts/ on sys.path | fixed: no sys.path entry |
| m-4 | MINOR | fixtures re-read after hashing | fixed: hashed bytes reused |
| m-5 | MINOR | flags not enforced | fixed: stop unless -I -S -B |
| m-6 | MINOR | exit codes ambiguous | fixed: 0/4/2/3/64 |
| m-7 | MINOR | conformance total mixed classes | fixed: FULL and PARTIAL counted separately |
| m-8 | MINOR | write set not compared | fixed where the mapping states it |
| m-9 | MINOR | PROTECTED-STATE mappings stretched | fixed in input REV4: unmapped |
| m-10 | MINOR | CR-004 REJECTED reinterpretation unstated | fixed in input REV4 mapping_basis |
| m-11 | MINOR | rule count said 12, is 13 | fixed |

两个阻断项的处理要点：

- **B-1（比较太宽松）**：现在比较时先按身份核对原生类型——必须是绑定的那个类、那个枚举类、确切的 `str`——然后才比较值。
- **B-2（可能执行旧的字节码）**：受测代码现在由 Harness 自己的导入器，直接用已经核对过散列的那份字节构建，不经过 `sys.path`，也不读取任何 `.pyc` 文件。

还没有审查、接受或运行第二版。DSP-004 保持 `OPEN / HOLD`。
