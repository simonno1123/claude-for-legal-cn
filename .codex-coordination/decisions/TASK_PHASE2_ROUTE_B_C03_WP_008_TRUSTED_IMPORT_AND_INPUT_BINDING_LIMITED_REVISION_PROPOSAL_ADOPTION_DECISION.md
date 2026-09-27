# Project Owner Route B C03 WP-008 有限设计修订提案采纳决定

## 1. 决定对象与来源

| 项目 | 记录 |
| --- | --- |
| 所属项目 | `claude-for-legal-cn` |
| 决策主体 | Project Owner |
| 决策依据 | Project Owner 在本会话对上一轮固定 SHA 提案回复：“采纳” |
| 被采纳提案 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_TRUSTED_IMPORT_AND_INPUT_BINDING_LIMITED_REVISION_PROPOSAL.md` |
| 提案 SHA-256 | `AC90F5DA143256FBC4F9409F0130FCB11D187E97DA550C72931B9209C3E71516` |
| 决定 | `ADOPTED AS LIMITED DESIGN REVISION DIRECTION — SHA BOUND` |
| 修订应用状态 | `NOT APPLIED` |
| 决策存证 | 本文件记录对话级 Project Owner 决定，不声称存在另行的人身身份验证或签名文件 |
| 本轮唯一新产物 | 本采纳决定 Markdown |

本决定采纳提案所列的修订方向、边界和未解决限制，不把该提案变成已经应用的
执行规范，不代替正式技术审查，也不新增代码物化、输入准入或运行授权。
未提供单独的签署时间，本记录不推断或生成治理生效时间戳。

## 2. 采纳范围

| 主题 | 采纳的设计方向 | 保留限制 |
| --- | --- | --- |
| 可信导入边界 | 区分可信启动、AST 解析、正常字面量导入、精确绑定的 dataclass 内部生成与任意动态执行；按来源和阶段限定例外。 | 不授予一般性动态执行权限；audit hook 不能被宣称为独立沙箱；例外的可实现性及环境侧依据仍须核实。 |
| 具体输入绑定 | 保留十五个原 fixture，以另行版本化、经准入的具体输入明确现有入口、必需参数、分支前提和事前比较规则。 | 本次不生成输入绑定包或参数实例；不从 expected 推导 observed，不用 harness 补造 subject 功能。 |
| 观察范围 | 将输入未绑定、部分可观察、完整要求不可评估和实际未运行明确区分。 | 不删除原场景、不降低十五项覆盖门槛，不将 NOT EVALUABLE 或 NOT RUN 改记为 PASS。 |

提案中关于授权比较分支不可达的静态限制保持未解决。该问题不能通过输入绑定消除，
本决定不授权修改 `identity_gate.py` 或其他 subject，也不接受以避开该分支的方式证明
完整授权检查。

## 3. 历史与文件身份保全

| 对象 | 固定 SHA-256 | 本决定的效力边界 |
| --- | --- | --- |
| Validation Execution Package Revision V2 | `5265D6D422D8BC101107E81B71AFEB485DDDE300A959B3692DA944AE18829BE5` | 不改写；拟议条款尚未替代原文件。 |
| Python Runtime Dependency Manifest Preparation Plan | `8C23436CD6CD7ADE9FFC30C44241D1D944A203AC00F0605B366B9F1658BBC239` | 不改写；未来有限修订须有独立来源和新 SHA。 |
| Future Harness Source Materialization Authorization | `081624BE31AB69443DAF5C51FD169CEB8BC20577E22F107A48839FC06DC64B8B` | 不修改、扩大、重新签发或宣告耗尽；源码物化仍因设计冲突暂停。 |

提案自身保留原字节及 SHA；其中 `NOT ADOPTED` 是文件形成时的状态快照。
本决定追加记录之后发生的方向采纳，不回写该快照，亦不把其 `PENDING REVIEW`
检查点改写为通过。

既有审查、接受和 fixture 准入记录继续保留其历史身份，但不能用来证明本次新发现的
可信导入、输入完整性或代码可达性问题已经解决。十个 subject、十五个 fixture、
Python 环境及独立 ACOS 项目均不在本次修改范围内。

## 4. 明确未授权及未建立事项

| 事项 | 本决定后的边界 |
| --- | --- |
| 对被采纳提案执行正式内部或外部审查 | 本次未授权、未执行；提案的十二个检查点仍待审查。 |
| 应用有限设计修订、创建修订后的设计候选 | 尚未授权；本决定仅采纳提案方向。 |
| 修复不可达授权比较或其他 subject 行为 | 未授权；问题保持未解决。 |
| 修改原 fixture 或物化 Scenario Input Binding | 未授权。 |
| 创建或导入 `run_validation.py` | 本决定不恢复物化；导入或执行未授权。 |
| 生成运行依赖 Manifest、网络隔离凭证或运行证据 | 未授权。 |
| 启动 Python、编译、测试、依赖探测或场景调用 | 未授权、未执行。 |
| 运行就绪、操作性验证通过、blocker closure | 未由本决定建立。 |
| Route A、OCR、真实案件、法律处理、Provider 或网络调用 | 未授权。 |
| 独立 ACOS 项目访问或变更 | 未授权。 |
| Git 提交、推送、分支或远程操作 | 未授权。 |

## 5. 后续边界

下一项可由 Project Owner 单独授权的工作，是按提案限定范围准备设计修订候选，
仅处理 Execution Package 与 Manifest Preparation Plan 中的可信导入边界、
具体输入绑定及必要的交叉引用。该工作不得顺带修改代码、补建缺失功能或运行验证。

修订后的设计文件须以新 SHA 单独审查和接受；本次采纳不构成预先通过，
不自动继承旧设计的审查结论，也不将旧固定 SHA 的物化授权迁移至新设计。

```text
Limited Revision Proposal:
ADOPTED AS DESIGN DIRECTION — SHA BOUND

Formal Proposal Review:
NOT PERFORMED / NOT ESTABLISHED

Design Revision Application:
NOT APPLIED / SEPARATE AUTHORIZATION REQUIRED

Harness Materialization:
PAUSED — DESIGN CONFLICTS OPEN

Input Binding / Unobservable Requirements / Unreachable Comparison:
UNRESOLVED — NO CLOSURE CLAIM

Validation Execution:
NOT AUTHORIZED / NOT RUN

Automatic Downstream Transition:
BLOCKED
```
