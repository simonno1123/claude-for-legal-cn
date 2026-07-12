---
name: aia-generation
description: >
  Stateful China AI impact assessment workflow. Compatibility command that delegates China-law assessment blocks to /security-assessment while restoring intake, seed assessment house style, policy consistency diff, inventory linkage, and output persistence.
argument-hint: "[AI system or use-case description, system ID, or triage result]"
---

# /aia-generation

This command remains compatible with the upstream AIA workflow while using the
China Mainland `security-assessment` content as the substantive legal framework.

Do not use EU AI Act FRIA, GDPR DPIA, NIST AI RMF, or US impact-assessment
templates as the default framework.

## Inputs And State

Read:

- `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`
- `ai-systems.yaml`
- `use-case-registry.yaml`
- prior seed assessment or house-style section from the profile
- AI policy commitments and prohibited-use rules

If a system ID is supplied, load that record. If not, ask whether to create or link
one via `/ai-governance-legal:ai-inventory`.

## Workflow

### Step 1: Intake

Collect:

- What the system does.
- Model/vendor/source.
- Deployment mode: assistive, augmentative, automated.
- Audience and affected people.
- Data used in training, fine-tuning, prompts, outputs, logs.
- Public-facing status and launch channel.
- Existing inventory/triage record.
- Existing assessments, PIPIA, MLPS, filing materials, vendor evidence.

### Step 2: Determine Assessment Track

Use China launch gates:

- Public-facing generative AI.
- Algorithm recommendation.
- Deep synthesis.
- Important data or cross-border data.
- Minors, medical, financial, education, recruitment, legal, credit, consumer compensation.
- Overseas/unfiled model API.
- Paid public service / telecom license review.

### Step 3: Delegate Substantive China Assessment

Load and apply `skills/security-assessment/SKILL.md` for the China AI safety and
compliance assessment blocks. Preserve its China-law requirements and P0 gates.

### Step 4: Policy Consistency Diff

Compare facts and proposed controls against:

- AI policy commitments.
- Use-case registry conditions.
- Approved vendors/tools.
- Prohibited vendors/tools.
- Human-review requirements.
- Data input prohibitions.
- External/public-service launch rules.

Flag:

- `REQUIRED`: policy says one thing, proposed use does another.
- `ADVISABLE`: policy is silent but should cover the use case.
- `WATCH`: rule status or facts are unverified.

### Step 5: Write Assessment Record

If outputs folder is configured, write an assessment draft file named:

`[system-or-use-case]-china-ai-assessment-[YYYY-MM-DD].md`

If no outputs folder is configured, output in chat and mark persistence as
`not configured`. Do not claim it was saved.

Update linked `ai-systems.yaml` record with:

- `last_assessment`
- `assessment_status`
- `open_assessment_gaps`
- `next_review`

Do not mark any system launched, approved, filed, or compliant.

## Output Format

```markdown
# China AI Impact And Safety Assessment (Draft)

> **复核提示**
> - **来源：** profile / ai-systems.yaml / registry / 用户材料 / security-assessment
> - **读取范围：** [materials read]
> - **待判断事项：** [legal/compliance/security/product questions]
> - **时效性：** [filing/status/practice items to verify]
> - **行动前：** no filing, launch, signing, or public claim without authorized review

## Assessment Track
| Track | Triggered? | Reason | Evidence gap |
|---|---:|---|---|

## China Security Assessment Blocks
[Use /security-assessment structure]

## Policy Consistency Diff
| Policy/registry item | Current commitment | System fact | Gap | Action |
|---|---|---|---|---|

## Inventory Update
| Field | Value |
|---|---|

## Next Steps
1. Remediate required gaps.
2. Update inventory and registry.
3. Run `/ai-governance-legal:policy-monitor` after assessment acknowledgment.
```
