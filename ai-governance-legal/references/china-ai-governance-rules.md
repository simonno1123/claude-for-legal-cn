# China AI Governance Core Rules

This is the default rulebook for `ai-governance-legal`. It assumes China Mainland jurisdiction unless the user expressly identifies an overseas or cross-border scenario.

## Governing Regulations (法规依据)

| # | 监管赛道 | 法规全称 | 发布机关 | 施行日期 |
|---|---------|---------|---------|---------|
| 1 | 算法推荐备案 | 《互联网信息服务算法推荐管理规定》 | 国家互联网信息办公室等四部门 | 2022-03-01 |
| 2 | 深度合成标识与备案 | 《互联网信息服务深度合成管理规定》 | 国家互联网信息办公室等三部门 | 2023-01-10 |
| 3 | 生成式 AI 服务备案与安全评估 | 《生成式人工智能服务管理暂行办法》 | 国家互联网信息办公室等七部门 | 2023-08-15 |
| 4 | 网络安全等级保护 (MLPS 2.0) | 《网络安全等级保护条例》及《信息安全技术 网络安全等级保护基本要求》(GB/T 22239-2019) | 公安部 / TC260 | 2019-12-01 |
| 5 | 数据出境安全评估 | 《数据出境安全评估办法》 | 国家互联网信息办公室 | 2022-09-01 |

> 上述法规名称为正式引用名称。模块内部各技能以概念描述方式引用对应义务时，均应可溯源至本表。如法规发生修订或废止，应同步更新本表及相关技能文件。

## Non-Negotiable Alignment

- Outputs are internal compliance drafts only.
- Do not promise regulatory approval, filing success, launch clearance, evidence privilege, or common-law work-product protection.
- Do not use EU AI Act, NIST AI RMF, FTC, GDPR DPIA, Colorado AI Act, or US state-law taxonomies as the China Mainland default framework.
- For public-facing AI services, do not collapse all obligations into one vague "filing/safety assessment" item.
- If current filing status, official catalog, provincial CAC practice, MIIT filing status, MLPS level, telecom license status, or standard version has not been verified, mark it as `[to verify]`.

## Multi-Track Compliance Map

### 1. Algorithm Recommendation Filing

Use this path when the service provides recommendation, sorting, ranking, search sorting, personalized display, content distribution, pricing display, or other algorithmic recommendation services.

Core checks:
- Public opinion attributes or social mobilization capability.
- Algorithm filing through the Internet Information Service Algorithm Filing System.
- User option to turn off personalized recommendation.
- Non-personalized display option.
- No algorithmic discrimination, addictive design, price discrimination, or unreasonable differential treatment.

### 2. Generative AI Service Filing And Security Assessment

Use this path when the service provides public-facing text, image, audio, video, code, virtual human, chatbot, AI search, AI writing, or similar generative AI services in China.

Core checks:
- Public-facing China service.
- Public opinion attributes or social mobilization capability.
- Security assessment materials for the registered-place provincial CAC.
- Generative AI service filing path.
- Model source, training data, content safety, real-name authentication, complaint handling, user agreement, minor protection.

### 3. Deep Synthesis Obligations

Use this path when the service creates, edits, or simulates face, body, voice, image, video, virtual scene, text, or biometric-like content.

Core checks:
- Real-name authentication.
- Visible marking in a prominent place where synthetic content may mislead the public.
- Implicit marking such as metadata or digital watermark where required by technical standards.
- Authorization for another person's portrait, voice, name, identity, or biometric-like characteristics.
- Anti-tampering and traceability controls.

### 4. MIIT Infrastructure And Telecom Prerequisites

Public-facing AI services must not ignore launch infrastructure gates.

Core checks:
- ICP filing for public-facing websites or web services.
- App filing for mobile apps and distribution through app stores.
- Mini-program platform requirements such as WeChat/Alipay entry review where applicable.
- Value-added telecom license, usually B25 ICP License, where paid information service, SaaS subscription, API billing, membership fee, or commercial operation is triggered.
- App SDK, personal information, and mobile app compliance requirements where mobile apps are involved.

### 5. MLPS 2.0 And Public Security Requirements

For public-facing AI systems and systems used in algorithm/generative AI filing/security assessment, check Cybersecurity Multi-Level Protection Scheme (MLPS 2.0 / dengbao).

Core checks:
- MLPS filing and assessment status.
- Level 3 assessment as default expectation for high-risk/public-facing AI systems unless local practice accepts Level 2.
- Assessment report number, testing institution, assessment date, scope, and整改 status.
- Public security authority reporting/coordination where AI fraud, deepfake fraud, network security incident, or illegal content risk appears.

### 6. Important Data And Cross-Border Data Flow

Do not focus only on personal information. AI training, prompt logs, uploaded files, model evaluation data, industrial data, vehicle data, medical data, financial data, mapping/geolocation data, and government/critical-sector data may involve important data.

Core checks:
- Data classification and grading.
- Important data catalog or sector-specific rules.
- Localized storage requirement.
- Whether data export involves important data, critical information infrastructure operator, or large-scale personal information.
- Apply the 2024 CAC `促进和规范数据跨境流动规定` as an effective baseline:
  - Non-CIIO exporting fewer than 100,000 individuals' non-sensitive PI since Jan 1 of the current year is exempt from data export security assessment, standard contract filing, and certification.
  - Non-CIIO exporting 100,000 or more but fewer than 1,000,000 individuals' PI since Jan 1 of the current year, or fewer than 10,000 individuals' sensitive PI, routes to personal information export standard contract or personal information protection certification.
  - Non-CIIO exporting 1,000,000 or more individuals' PI since Jan 1 of the current year, or 10,000 or more individuals' sensitive PI, routes to CAC data export security assessment.
  - Important data, CIIO scenarios, and sector-specific catalogues override the personal-information exemption path.
  - Even if exempt, PIPIA, notice/consent or lawful basis, contract controls, minimization, retention, audit evidence, and security measures still apply.

## TC260-PG-20241A Safety Assessment Baseline

For generative AI service safety review, use TC260-PG-20241A, `生成式人工智能服务安全基本要求`, as the operational baseline unless a newer official version applies.

Minimum review dimensions:
- Organization security.
- Corpus security.
- Annotation security.
- Model security.
- Service security.
- Assessment materials.

Quantitative items to request where applicable:
- Safety assessment test set size.
- Refusal test set size, with 500 as a key check item where applicable.
- Overall safety test set, with 2,000 as a key check item where applicable.
- Labeler consistency and quality-control ratio.
- Sampling inspection ratio.
- Log retention period, with no less than six months where network logs must be retained.

## Content Safety Stop-Filter

For illegal or harmful generated content, require:

1. Detect and intercept.
2. Stop transmission or generation.
3. Preserve records and logs.
4. Dispose of user account or function permissions where appropriate.
5. Report to the local CAC within 24 hours where required.
6. Report to public security authority where crime, fraud, public security, or cybersecurity incident risk appears.

## Launch Decision Labels

- `PROCEED`: Low-risk internal use with no public-facing, sensitive data, automated decision, training, vendor, or infrastructure red flags. Still requires human review.
- `ASSESSMENT REQUIRED`: AI compliance assessment, PIPIA, supplier review, IP/data review, MIIT filing check, MLPS check, or policy approval is needed.
- `SPECIAL REVIEW`: Filing/security assessment, high-risk sector, public opinion, deep synthesis, minors, medical/financial/legal, important data, telecom license, MLPS, or cross-border issues are triggered.
- `STOP`: Real-name, ICP/App filing, ICP License, MLPS, data source, important data export, content safety, sensitive PI, vendor, or illegal-harmful content red line blocks launch.
