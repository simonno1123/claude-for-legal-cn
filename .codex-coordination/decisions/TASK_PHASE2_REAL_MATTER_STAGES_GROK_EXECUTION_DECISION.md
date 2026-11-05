# Real-Matter Stages Routing Decision (revision 2)

| Field | Value |
| --- | --- |
| Owner | 张纯熙 |
| Date | 2026-11-05 |
| Recorded by | Claude (recorder only; owner statement in chat, not a signature) |
| Supersedes | `TASK_PHASE2_REAL_MATTER_STAGES_GROK_ROUTING_DECISION.md` (Grok organizes material, Claude executes). The Codex routing it replaced remains withdrawn. |
| Owner statement | "我改主意了，后面真实案件的阶段由grok bot执行好了，你将需要交给grok的材料生成，由我黏贴给他进行操作。" |

## Decision

1. **Grok executes.** The Grok bot executes the stages that need real case material:
   - Route A (CASE-A, CASE-B, CASE-C);
   - C03 AR-B-002 to 006;
   - C03 AR-B-010, once an exact candidate output exists.
2. **Claude drafts and records.** Claude drafts the task packets. The owner pastes them to Grok. Claude records the redacted return summaries that the owner pastes back.
3. **What stays outside Grok.**
   - AR-B-001 (C03 activation) remains the owner's own decision.
   - The integration-stage items from the AR-B-008 closure are code and runtime work, not real-material work, and stay with Claude.
4. **Authorization.** Each stage still needs the owner's authorization. The owner pasting a packet to Grok is taken as that authorization for that stage.

## Packets

`docs/phase2/TASK_PHASE2_REAL_MATTER_GROK_HANDOFF_PACKETS.md`. The file contains no real case data.

## Constraints

- This repository is public. Real material stays with Grok and the owner.
- Only the redacted return summaries are committed, under opaque IDs.
- Grok output is a work product for qualified-lawyer review. It is not evidence and not a Legal Fact.
- The human confirmation gates are unchanged.

## Other changes

- The private folder `Documents\legal-cn-private\` created on the owner's computer is no longer required.
- The material request `docs/phase2/TASK_PHASE2_REAL_MATTER_MATERIAL_REQUEST_FOR_GROK.md` is superseded by the packets.
