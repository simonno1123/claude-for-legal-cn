# TASK_014_LAW_STUDENT_UPGRADE_RESULT

Artifact Type: RESULT
Producer: Codex
Task: TASK_014_LAW_STUDENT_UPGRADE
Mode: READ ONLY assessment; no target files modified
Project: /Users/zhang/Documents/claude-for-legal-cn
Standard: docs/FAITHFUL_PORT_STANDARD.md
Next Receiver: Gemini

This artifact reports audit facts and an upgrade plan only. It is not a REVIEW and not a DECISION.

## Structure

### Upstream structure

Upstream path:

```text
/Users/zhang/Documents/Playground/claude-for-legal-upstream/law-student
```

Upstream contains:

- `.claude-plugin/plugin.json`
- `.mcp.json`
- `CLAUDE.md`
- `README.md`
- `hooks/hooks.json`
- 13 root skills:
  - `bar-prep-questions`
  - `case-brief`
  - `cold-call-prep`
  - `cold-start-interview`
  - `customize`
  - `exam-forecast`
  - `flashcards`
  - `irac-practice`
  - `legal-writing`
  - `outline-builder`
  - `session`
  - `socratic-drill`
  - `study-plan`

### CN current structure

CN path:

```text
phase-2/law-student
```

CN contains the same 13 skill names and the same core root files, plus `references/test-cases-cn.md`.

CN root-level parity check:

```text
root-law-student:missing
```

Marketplace check:

- `.claude-plugin/marketplace.json` does not list `law-student`.
- `PROJECT_USAGE_GUIDE.md` lists it as `phase-2/law-student`.
- `docs/UPSTREAM_MAPPING_MATRIX.md:26` identifies this as a parity risk.
- `docs/UPSTREAM_MAPPING_MATRIX.md:33` states `law-student` and `legal-clinic` are the clearest directory parity risks.

### Structural finding

Skill/file names are preserved, but module location is not. Upstream `law-student` is a root module; CN currently stores it under `phase-2/law-student` and does not expose it through the default marketplace.

This is a v1 Faithful Port root parity issue.

## Capability

### Upstream educational capability

Upstream `law-student` is not only a set of study prompts. It is a learning-mode system:

- Socratic drilling.
- Case briefing.
- Outline building.
- Bar preparation.
- Flashcards with session behavior.
- IRAC grading.
- Cold-call preparation.
- Legal writing feedback.
- Exam forecasting.
- Study plan creation and update.
- Student profile calibration.
- Progress/history tracking.
- Strong anti-ghostwriting and academic integrity guardrails.

Evidence:

- Upstream README defines the core posture as "Learning mode, not answer mode" and "study scaffold, not a model answer" at upstream `README.md:3-5`.
- Upstream README lists the 13 skills and their responsibilities at upstream `README.md:23-36`.
- Upstream README explains anti-ghostwriting / learning-mode behavior at upstream `README.md:38-50`.

### CN current capability

CN has a China-law educational capability:

- CN README says the module is for China legal study, not real case representation: `phase-2/law-student/README.md:1-3`.
- CN README lists study themes: statutes, claim-basis analysis, elements, burden of proof, adjudication rules, and legal qualification exam prep: `phase-2/law-student/README.md:16-23`.
- CN `CLAUDE.md` sets China Mainland default jurisdiction and China-law learning method: `phase-2/law-student/CLAUDE.md:7-25`.

### Capability finding

The China-law learning domain exists. However, the current implementation is much thinner than upstream and does not yet restore the full "learning-mode system" capability. It is closer to a minimal China-law command index and prompt set.

## Responsibility

### Responsibility mapping table

| Responsibility | Upstream status | CN status | Assessment |
|---|---|---|---|
| Legal education workflow | Full learning-mode system, calibrated to student profile | Present as China-law learning module | Preserved, but shallow |
| Case study workflow | Case-brief scaffolding, confidence discipline, no brief-from-name default | China case brief template exists | Localized, depth reduced |
| Exam preparation workflow | Bar jurisdiction / UBE / NextGen / state-specific, weak-subject targeting, session history | China 法考 objective/subjective question prompt exists | Localized, but tracking/adaptivity missing |
| Legal reasoning training | Socratic drill, pushback, no answer until student works | China-law question sequence exists | Preserved in minimal form |
| Research methodology | Connector verification, confidence tags, source checking | China sources listed in `CLAUDE.md` and `.mcp.json` | Localized, but skill-level citation workflow missing |
| Writing practice | Structural feedback, never rewrites, tracker | CN legal-writing can output study drafts | Gap: anti-ghostwriting weaker |
| Feedback workflow | IRAC/writing trackers, repeated pattern detection | CN session record template only | Gap |
| Student profile / cold start | Detailed interview, materials intake, integrations, pause/resume, limited-data flag | Minimal profile fields | Gap |
| Progress tracking | `study-plan.yaml`, session history, flashcard buckets, writing/IRAC trackers | Not materially implemented | Gap |
| Academic integrity | Strong honor-code / graded-work guardrails | General learning/non-advice boundary only | Gap |

### Key evidence

CN skills are present but compressed:

```text
bar-prep-questions: upstream 270 lines / CN 24 lines
case-brief: upstream 108 lines / CN 27 lines
cold-call-prep: upstream 133 lines / CN 18 lines
cold-start-interview: upstream 308 lines / CN 19 lines
customize: upstream 88 lines / CN 10 lines
exam-forecast: upstream 165 lines / CN 19 lines
flashcards: upstream 158 lines / CN 17 lines
irac-practice: upstream 178 lines / CN 20 lines
legal-writing: upstream 167 lines / CN 19 lines
outline-builder: upstream 152 lines / CN 19 lines
session: upstream 31 lines / CN 20 lines
socratic-drill: upstream 101 lines / CN 18 lines
study-plan: upstream 248 lines / CN 16 lines
```

CN `cold-start-interview` currently collects only identity, target, subjects, time, and method preference, then outputs `student_profile`: `phase-2/law-student/skills/cold-start-interview/SKILL.md:10-18`.

Upstream `cold-start-interview` includes setup reuse, integration check, quick/full setup, materials intake, pause/resume, limited-data flag, and downstream calibration: upstream `cold-start-interview/SKILL.md:14-23`, `:62-76`, `:90-107`.

CN `study-plan` currently outputs static weekly/daily tasks and stage checks: `phase-2/law-student/skills/study-plan/SKILL.md:10-15`.

Upstream `study-plan` supports build/update/status/cram modes, `study-plan.yaml`, session history, adaptive subject weighting, and plan confirmation: upstream `study-plan/SKILL.md:13-22`, `:26-30`, `:40-49`.

CN `session` records a session template: `phase-2/law-student/skills/session/SKILL.md:9-19`.

Upstream `session` runs N-question sessions, routes to bar/essay/flashcard methods, writes session history, and reports patterns.

CN `legal-writing` allows learning drafts and simulated legal opinion study drafts: `phase-2/law-student/skills/legal-writing/SKILL.md:11-18`.

Upstream `legal-writing` is stricter: structural feedback only, never rewriting, with pattern tracking.

## Localization

### Localized elements

CN localization is directionally correct:

- Case Method -> China case study / case-brief mapped in `case-brief`.
- Bar Exam -> 国家统一法律职业资格考试 / 法考 mapped in `bar-prep-questions` and README.
- Common-law reasoning -> Chinese statutory / elements / claim-basis analysis mapped in `CLAUDE.md`, `outline-builder`, `irac-practice`, and `socratic-drill`.
- Foreign cases -> guiding cases / typical cases / judicial interpretations listed as sources in `CLAUDE.md:23-25`.
- Legal writing -> China legal study writing and legal qualification exam subjective answers mapped in `legal-writing`.

### Foreign-law residue classification

Remaining foreign-law references in CN files are mainly negative constraints:

- `phase-2/law-student/CLAUDE.md:10-11` says not to use U.S. case method, Bluebook, U.S. bar exam, common law, or IRAC as the sole framework.
- `phase-2/law-student/skills/bar-prep-questions/SKILL.md:23` says not to use U.S. bar exam rules or state-law question types.
- `phase-2/law-student/references/test-cases-cn.md:9` treats Bluebook requests as a test case for redirecting to China-law sources and Chinese citation practice.

No substantive U.S. law default was found driving CN skills.

### Localization finding

Legal substance is mostly China-localized, but educational workflow depth is not yet faithfully ported.

## Operational Depth

The largest deficits are operational depth, but several affect responsibility completion:

1. Learning plans:
   - CN has static plan output.
   - Upstream has build/update/status/cram modes, study-plan persistence, weak-subject weighting, daily schedule, and session-history adaptation.

2. Progress tracking:
   - CN has a session record template.
   - Upstream writes and reads `study-plan.yaml`, `session_history`, flashcard buckets, IRAC trackers, writing feedback trackers, and exam forecast outputs.

3. Feedback loops:
   - CN has basic prompts for wrong questions and weak points.
   - Upstream has cross-session pattern detection and downstream plan adaptation.

4. Mentor / academic review:
   - CN has learning/non-advice boundaries.
   - Upstream has stronger honor-code, graded work, professor policy, and real-matter guardrails.

5. Exercises:
   - CN has question generation, flashcard generation, and subjective answer practice.
   - Upstream has richer modes, drill behavior, and confidence discipline.

6. Assessment workflow:
   - CN provides stage checks.
   - Upstream creates ongoing assessment records and uses them for future scheduling.

Assessment: some deficits are observations if treated as richness differences; however progress tracking, anti-ghostwriting, student-profile calibration, and root discoverability affect v1 responsibility completion.

## Governance

### Phase-2 downgrade issue

Current governance docs already identify this risk:

- README says `law-student` remains in `phase-2` and root parity is undecided.
- `PROJECT_USAGE_GUIDE.md` says `phase-2/law-student` directory status is not a value judgment.
- `docs/UPSTREAM_MAPPING_MATRIX.md:26` marks `law-student` as `已中国化 / 偏移风险 / 待核对`.

### Root module parity issue

Upstream path is root `law-student`. CN path is `phase-2/law-student`; root `law-student` is missing and default marketplace does not expose it. This is not merely a documentation issue because users cannot discover or install it as a root marketplace plugin under the same parity pattern as upstream.

### Should module return to root marketplace?

Factual recommendation: yes, if v1 means Complete Chinese Port of upstream root modules. The safer implementation path is:

1. Create or restore root-level `law-student/`.
2. Preserve upstream skill names and `/law-student:*` commands.
3. Add marketplace entry after Gemini accepts upgrade plan.
4. Keep any `phase-2` copy only as temporary migration evidence until final cleanup.

If project governance intentionally keeps `law-student` in `phase-2`, then `docs/UPSTREAM_MAPPING_MATRIX.md` must explicitly mark a temporary directory exception and explain how command discoverability is preserved. Current files do not complete that exception.

## Risks

### Blocker

1. Root module parity is not restored. Upstream `law-student` is a root module; CN has only `phase-2/law-student`, no root `law-student`, and no default marketplace entry.

2. Upstream's core learning-mode responsibility is not fully preserved. CN skills exist, but the anti-answer / anti-ghostwriting scaffold is not consistently rebuilt. Upstream README says every output is study scaffold, not model answer, and legal-writing never rewrites; CN legal-writing can produce learning drafts and simulated legal opinions without the same strict feedback-only boundary.

### Gap

1. Cold-start responsibility is incomplete. CN collects basic profile fields; upstream includes integration checks, quick/full setup, materials intake, pause/resume, limited-data markers, and downstream skill calibration.

2. Study-plan and session feedback loop is incomplete. CN has static study-plan/session templates; upstream has persistent `study-plan.yaml`, `session_history`, weak-subject weighting, adaptive updates, and status/cram modes.

3. Flashcard / IRAC / writing tracking is incomplete. CN has prompts; upstream has recurring session/tracker behavior and pattern learning.

4. Academic integrity / graded-work guardrails are shallow. CN says learning only, but does not yet restore equivalent honor-code/professor-policy/graded-work routing.

5. Research/citation methodology is only partially mapped. CN sources are listed and `legal-data` is configured, but skill-level citation verification and confidence tagging are not rebuilt across the module.

### Observation

1. Skill names are preserved one-to-one, which reduces upgrade risk.
2. Legal localization direction is correct: 法考, 请求权基础, 构成要件, 证明责任, 指导性案例/典型案例, 司法解释 all appear in the CN concept layer.
3. CN `.mcp.json` is China-localized and uses `legal-data` plus WPS placeholder, replacing CourtListener / Descrybe / Google Drive / Slack.

### Enhancement

1. Add China-specific learning materials intake: 法考真题/模拟题、法考大纲、教材章节、课堂讲义、案例研习材料、错题本、主观题答案和批改记录.
2. Add China-law assessment rubrics for 民法请求权基础、刑法四要件/阶层体系、行政行为合法性、三大诉讼法程序节点、商经知产劳动数据专题.
3. Add optional mentor review fields for teacher / tutor / clinic supervisor comments.
4. Add regression tests beyond `references/test-cases-cn.md` once upgrade is complete.

## Upgrade Plan

### P0 - Structural parity and command discoverability

1. Restore root-level `law-student/` module parity.
2. Add `law-student` to `.claude-plugin/marketplace.json` unless Gemini explicitly approves a temporary phase-2 exception.
3. Preserve all 13 upstream skill command names.
4. Decide whether to move `phase-2/law-student` to root or create root-level wrappers. Given this is a full module rather than a few displaced skills, moving/promoting the module is cleaner than wrappers.

### P0 - Core learning-mode responsibility

1. Rewrite README and `CLAUDE.md` to state: learning scaffold, not model answer; no ghostwriting; all output is study material, not legal advice.
2. Localize academic integrity rules to China education context:
   - school / course AI policy;
   - exam discipline;
   - graded assignments;
   - 法考 training vs cheating boundary.
3. Add China-law real-matter redirect:
   - study hypotheticals stay in `law-student`;
   - real parties / real disputes / real clients route to `legal-clinic` or licensed lawyer.

### P1 - Stateful study profile and progress loop

1. Expand `cold-start-interview`:
   - China law student / 法考考生 / 实习生 / self-study role;
   - law school year or study stage;
   - target exam / course / 法考 date;
   - weak subjects;
   - learning style;
   - materials intake;
   - China connectors / local materials check;
   - limited-data flag;
   - pause/resume.
2. Expand `study-plan`:
   - build/update/status/cram modes;
   - `study-plan.yaml`;
   - session history;
   - weak subject weighting;
   - daily/weekly plans.
3. Expand `session`, `flashcards`, `irac-practice`, `legal-writing`:
   - write session records;
   - update weak points;
   - carry forward repeated errors;
   - preserve no-rewrite/feedback-only boundaries.

### P1 - China-law skill depth

1. `bar-prep-questions`: map UBE/MBE logic to 法考客观题/主观题, 法考大纲, 科目体系, 错项解析, new-law updates.
2. `case-brief`: map case method to 中国案例研习: 案情、争点、法条、裁判要旨、请求权基础/构成要件、证明责任、类案价值.
3. `outline-builder`: use Chinese codified-law structure, statutory hierarchy, judicial interpretation, guiding cases, typical cases.
4. `socratic-drill` / `cold-call-prep`: preserve ask-wait-pushback behavior, localized to课堂提问/研讨课/案例课.
5. `exam-forecast`: avoid promise of prediction; produce review priority from 法考大纲, class scope, wrong-question history, new-law changes.

### P2 - Governance and regression

1. Update `docs/UPSTREAM_MAPPING_MATRIX.md` after Gemini decision.
2. Update `PROJECT_USAGE_GUIDE.md` if root parity is restored.
3. Expand `references/test-cases-cn.md` to cover anti-ghostwriting, real-matter redirect, source verification, and progress tracking.
4. Add automated checks for root marketplace exposure and key skill texts.

## Runtime

Validation performed:

```text
cn-plugin-json:OK
cn-mcp-json:OK
cn-hooks-json:OK
```

No runtime JSON syntax issue found.

Runtime risk:

- Current module is not default marketplace-discoverable.
- Root `/law-student:*` command docs exist in `README.md` and `PROJECT_USAGE_GUIDE.md`, but the plugin physically lives under `phase-2/law-student`.

## Lessons Learned

1. One-to-one skill names are not sufficient for Faithful Port. For educational modules, the pedagogy is part of the responsibility.
2. Operational depth can become a Gap when it carries the upstream responsibility, such as progress tracking, anti-ghostwriting, and feedback loops.
3. `phase-2` placement is not only governance wording; when a root upstream module is not marketplace-discoverable, it becomes a structural parity issue.
4. For `law-student`, China localization means replacing common-law / U.S. bar content with 法考 / 中国案例研习 / 请求权基础 / 成文法体系, while preserving the upstream learning-mode guardrails.

## Overall

Factual recommendation: ACTION REQUIRED

Rationale:

- Legal substance is directionally China-localized.
- Skill names and core files are structurally mirrored under `phase-2/law-student`.
- However, v1 root module parity is not restored.
- Core upstream educational responsibilities are materially reduced: learning-mode guardrails, anti-ghostwriting, cold-start materials intake, adaptive study planning, session history, feedback trackers, and source/citation verification are missing or only minimally represented.

NEXT RECEIVER: Gemini
