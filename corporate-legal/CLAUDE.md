<!--
CONFIGURATION LOCATION

User-specific configuration for this plugin lives at:

  ~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md

Rules for every skill, command, and agent in this plugin:
1. READ configuration from that path. Not from this template.
2. If that file does not exist or still contains [PLACEHOLDER] markers, STOP before substantive work and ask the user to run `/corporate-legal:cold-start-interview`.
3. Setup and cold-start-interview WRITE to that path, creating parent directories as needed.
4. This file is the TEMPLATE shipped with the plugin. Never write user data here.
-->

# Corporate Legal Practice Profile（中国公司法版）

*Written by cold-start on [DATE]. If `[PLACEHOLDER]`, run `/corporate-legal:cold-start-interview`.*

---

## 中国公司法 System Alignment（强制）

本插件默认服务于中华人民共和国大陆地区公司法律事务。除非用户明确指定港澳台、境外上市地或外资特殊监管，本插件不得套用 Delaware、New York、LLC、bylaws、board consent、stockholder consent、SEC public company 等美国公司法框架作为默认分析依据。

**当前公司法基准：** 新修订的《中华人民共和国公司法》已于 2024 年 7 月 1 日施行。涉及条文序号、过渡期、配套登记规则、司法裁判口径或市场监管实操口径时，必须标注 `[待查证]` 或 `[市场监管口径 - 待查证]`，并建议用国家法律法规数据库、市场监管总局/地方市场监管局、最高人民法院、北大法宝、威科先行、法信或用户提供材料复核。

具体法源和核验规则见 `references/company-law-cn.md`。

### 1. 公司治理结构

不得把“董事会/Board of Directors”当作唯一权力中心。中国公司治理应先识别公司类型、章程安排和治理机关：

- 股东会：公司权力机构。不得再沿用“最高权力机构”的僵化表述。
- 董事会/董事：执行股东会决议并负责经营决策；董事、监事、高级管理人员负有忠实义务和勤勉义务。
- 经理层：按章程、董事会授权或内部制度执行经营管理。
- 监事会/监事或审计委员会：新公司法下存在治理路径选择，不能默认美国式 audit committee。
- 职工董事/职工监事：职工人数三百人以上的公司应重点审查是否依法设置职工代表参与治理的机制；具体适用和章程安排需结合公司类型与条文复核。

### 2. 新公司法出资卡点

所有涉及有限责任公司注册资本、出资期限、股权转让、债务清偿能力的技能，必须审查：

- 《公司法》第47条：有限责任公司全体股东认缴的出资额通常应由股东按照公司章程规定自公司成立之日起五年内缴足；存量公司过渡安排需查证。
- 《公司法》第54条：公司不能清偿到期债务时，公司或已到期债权的债权人可要求已认缴出资但未届出资期限的股东提前缴纳出资。
- 《公司法》第88条：股东转让已认缴出资但未届出资期限的股权时，转让人与受让人的出资责任和补充责任必须逐项审查。

不得只按“章程约定出资期限未到”得出安全结论；必须加入债务到期、清偿能力、债权人主张和股权转让链条审查。

### 3. 股权转让与质押

有限责任公司股权转让不得沿用旧法“其他股东过半数同意”的默认逻辑。应审查：

- 对外转让是否已书面通知其他股东。
- 通知是否载明股权转让数量、价格、支付方式、期限等同等条件。
- 其他股东优先购买权期限、回复、放弃和送达留痕。
- 公司章程是否另有合法有效的转让限制。
- 股东名册、公司登记、章程/出资证明书、税务、外汇、国资或外商投资审批/备案是否需要同步。
- 股权质押必须关注市场监督管理部门出质登记；未登记不得轻易认定质权已设立。

### 4. 输出定位和人工确认门

所有输出均为公司法律工作初稿，供中国执业律师或企业法务审阅。以下动作不得由插件直接替用户执行或最终确认：

- 设立、变更、注销、备案、登记、工商/市场监管提交。
- 通过或签署股东会决议、董事会决议、章程、股权转让协议、质押合同。
- 出具法律意见、对外承诺、放弃权利、确认出资责任、承认债务或启动追责。
- 对股东、董事、监事、高管发函追责或对债权人作出偿付/担保承诺。

## 默认页眉与审阅人备注

**内部分析页眉：**

- 律师/企业法务用户：`公司法分析初稿 - 保密文件 - 仅供内部法律审阅`
- 非律师用户：`公司法协同初稿 - 仅供参考 - 必须经中国执业律师或企业法务复核`

不得使用 `ATTORNEY WORK PRODUCT` 或承诺美国式证据特权。

**审阅人备注**固定放在正文前：

> **审阅人备注**
> - **来源：** [国家法律法规数据库 / 市场监管官网 / 用户提供 / 商业数据库 / 模型知识 - 待查证]
> - **读取范围：** [完整文件 / 第 X-Y 页 / N 条登记记录 / 未读取原件]
> - **法域：** 中国大陆 / [省市] / [特殊行业]
> - **待复核：** [公司法条文、章程、登记口径、国资/外资/上市监管、税务]
> - **后果性动作：** [登记/签署/追责/付款/对外发送需人工确认]

## No Silent Supplementation

1. 禁止在未核验法条、注册登记口径或具体章程规则的前提下，自行编造或默认填充事实。
2. 确有必要提供参考示例时，必须在文本中明确标注 `[待核验]` 或 `[示例建议]`。

## 公司画像

**公司名称：** [PLACEHOLDER]
**统一社会信用代码：** [PLACEHOLDER]
**公司类型：** [有限责任公司 / 股份有限公司 / 一人公司 / 国有独资 / 外商投资企业 / 上市公司 / 其他]
**注册地：** [PLACEHOLDER]
**主要经营地：** [PLACEHOLDER]
**所属行业：** [PLACEHOLDER]
**是否国资/外资/上市/金融等特殊监管：** [PLACEHOLDER]
**员工人数：** [PLACEHOLDER]

## 章程与治理结构

**现行章程版本：** [PLACEHOLDER]
**股东会规则：** [PLACEHOLDER]
**董事会/董事设置：** [PLACEHOLDER]
**监事会/监事/审计委员会：** [PLACEHOLDER]
**是否触发职工董事/职工监事审查：** [PLACEHOLDER]
**法定代表人：** [PLACEHOLDER]
**董监高名单：** [PLACEHOLDER]

## 注册资本与出资

**注册资本：** [PLACEHOLDER]
**实缴资本：** [PLACEHOLDER]
**认缴期限：** [PLACEHOLDER]
**是否存在超过五年出资期：** [PLACEHOLDER]
**是否存在未届期出资转让：** [PLACEHOLDER]
**是否存在不能清偿到期债务：** [PLACEHOLDER]

| 股东 | 认缴额 | 实缴额 | 出资期限 | 出资方式 | 风险 |
|---|---:|---:|---|---|---|
| [PLACEHOLDER] | | | | | |

## 股权与登记

**股东名册位置：** [PLACEHOLDER]
**市场监管登记状态：** [PLACEHOLDER]
**历史股权转让：** [PLACEHOLDER]
**股权质押：** [PLACEHOLDER]
**优先购买权通知模板：** [PLACEHOLDER]
**国资/外资/反垄断/行业审批：** [PLACEHOLDER]

## 事项升级矩阵

| Issue | Handle at | Escalate to | When |
|---|---|---|---|
| 五年出资期整改 | 法务 + 财务 | 外部律师/市场监管顾问 | 存量公司过渡安排、减资或章程修改 |
| 出资加速到期 | 法务 + 财务 | 外部律师/诉讼律师 | 公司不能清偿到期债务、债权人追责 |
| 未届期股权转让 | 法务 | 外部律师/税务顾问 | 转让人/受让人责任划分不清 |
| 股权质押 | 法务 + 财务 | 外部律师/市场监管窗口 | 未登记、重复质押、担保争议 |
| 治理结构调整 | 法务 + 董办 | 外部律师 | 审计委员会替代监事会、职工董事/监事 |
| 重大交易/融资/M&A | 法务 + 管理层 | 外部律师/投行/税务 | 涉国资、外资、上市、反垄断或高额交易 |

## Seed documents

| Doc | Location | Date | Notes |
|---|---|---|---|
| 营业执照 | [PLACEHOLDER] | | |
| 公司章程 | [PLACEHOLDER] | | |
| 股东名册/出资证明书 | [PLACEHOLDER] | | |
| 验资/出资凭证 | [PLACEHOLDER] | | |
| 历次股权转让文件 | [PLACEHOLDER] | | |
| 股权质押登记/合同 | [PLACEHOLDER] | | |
| 股东会/董事会/监事会决议 | [PLACEHOLDER] | | |

---

*Re-run full interview: `/corporate-legal:cold-start-interview --redo`*
