# Law Student (中国法学习助手)

本插件是 `law-student` 上游能力在中国法律教育场景下的 Faithful Port：保留学习画像、苏格拉底式训练、案例研习、大纲构建、法考练习、写作反馈、错题追踪和长期学习计划等职责，同时将实体内容映射到中国大陆法律体系、国家统一法律职业资格考试和中国法学院课程训练。

**本插件是学习脚手架，不是答案生成器。** 它帮助学生拆解问题、定位法条、训练请求权基础和构成要件分析、记录薄弱点并安排复习；它不代写作业、不生成可直接提交的课程论文或考试答案，也不处理真实客户委托。

## 适用对象

- 中国法学院本科生、研究生、LLM 或辅修法律课程的学生。
- 国家统一法律职业资格考试客观题/主观题备考者。
- 在监督下进行模拟训练的实习生、法援/诊所学生。
- 以自学为目的的法律学习者。

## 首次设置

所有命令都依赖学习画像：

```text
/law-student:cold-start-interview
```

学习画像存放在：

```text
~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md
```

状态文件包括：

```text
~/.claude/plugins/config/claude-for-legal/law-student/study-plan.yaml
~/.claude/plugins/config/claude-for-legal/law-student/session_history/
~/.claude/plugins/config/claude-for-legal/law-student/flashcards/
~/.claude/plugins/config/claude-for-legal/law-student/irac-sessions/
~/.claude/plugins/config/claude-for-legal/law-student/writing-feedback/
```

## 核心命令

| 命令 | 作用 |
|---|---|
| `/law-student:cold-start-interview` | 建立或更新学生画像、学习目标、法考时间、薄弱科目、资料目录和学术诚信边界 |
| `/law-student:study-plan` | 读写 `study-plan.yaml`，按弱项、考试日期、会话历史生成或更新学习计划 |
| `/law-student:session` | 运行一次客观题/主观题/案例/法条定位学习会话，并写入 `session_history` |
| `/law-student:socratic-drill` | 一问一答式追问训练，必须等待学生回答后再反馈和追问 |
| `/law-student:cold-call-prep` | 课堂提问准备，围绕案例事实、争点、法条和老师可能追问进行演练 |
| `/law-student:case-brief` | 中国案例研习：案情、争点、请求权基础/构成要件、证明责任、裁判规则和类案检索 |
| `/law-student:outline-builder` | 按中国成文法体系、司法解释和课程材料搭建复习大纲 |
| `/law-student:bar-prep-questions` | 法考客观题/主观题练习、错项解释和错题模式追踪 |
| `/law-student:flashcards` | 生成和复习法条、概念、构成要件、期限、易混点卡片 |
| `/law-student:irac-practice` | 法考主观题和课程论证训练；可用 IRAC 表达，但实体分析以中国法为准 |
| `/law-student:legal-writing` | 对学习稿提供结构、论证、引用和事实代入反馈；不重写、不代写 |
| `/law-student:exam-forecast` | 基于课程范围、法考大纲、错题和过往材料生成复习权重，不承诺命题预测 |
| `/law-student:customize` | 局部更新学习画像、考试目标、弱项权重和输出偏好 |

## 学习模式规则

- 每个学习输出均标注为“学习笔记 / 非法律意见”。
- 对 graded work、课程论文、考试作业、竞赛文书，只能给结构化反馈、问题清单和练习建议，不得代写、改写或生成可提交文本。
- `socratic-drill`、`cold-call-prep`、`irac-practice` 和 `legal-writing` 必须优先让学生自己回答，再给反馈。
- 如果用户输入真实当事人、真实案件、真实期限、真实委托事实或真实法律风险，停止学习流程并提示转入 `legal-clinic`、学校诊所/指导老师或执业律师。
- 使用 IRAC 时仅作为表达结构；实体判断必须回到中国法的法条、构成要件、请求权基础、证明责任、司法解释和裁判规则。

## 中国法学习主线

- 民法：请求权基础、构成要件、抗辩、举证责任、责任承担。
- 刑法：构成要件、违法性、责任、罪数、量刑情节。
- 行政法：行政行为合法性、程序、复议、诉讼、赔偿。
- 民诉/刑诉/行政诉讼：管辖、期限、证据、程序节点、救济路径。
- 商经/知产/劳动/数据：以现行法条、监管口径、司法解释和典型案例辅助。

## 资料来源

优先使用国家法律法规数据库、中国人大网、最高人民法院/最高人民检察院、司法部、法考大纲、指导性案例、典型案例和用户提供教材。

如果法律依据、考试大纲、案例状态或有效日期可能变化，必须标记“待核验”，优先要求用户提供教材、法条文本、课程资料或通过 `legal-data` 查询。不得编造案号、案例事实、裁判理由或法考真题。
