# Real-Matter Stages Routing Decision (revised)

| Field | Value |
| --- | --- |
| Owner | 张纯熙 |
| Date | 2026-11-05 |
| Recorded by | Claude (recorder only; owner statements and choices in chat, not a signature) |
| Supersedes | `TASK_PHASE2_REAL_MATTER_STAGES_CODEX_ROUTING_DECISION.md`; the Codex handoff is WITHDRAWN |
| Owner statement | "我改变主意了，生成材料交给grok bot" |
| Owner choices | 分工："Grok 生成材料，Claude 执行"；材料性质："基于真实案件整理" |

## Decision

1. The case material for every stage that needs real case material is produced by the Grok bot, organized from real cases.
2. Claude executes those stages. The stages are:
   - Route A;
   - C03 AR-B-001 to 006 and AR-B-010;
   - the integration-stage items handed over by the AR-B-008 closure.
3. Each stage still needs its own owner authorization before execution. This routing decision authorizes none.

## Handling of the material

The material is organized from real cases and keeps real information. The following rules therefore apply:

- **Never in the repository.** This repository is public on GitHub. The material is never committed, pushed, or quoted in an issue or pull request. Its file names and file hashes are not committed either, because they could identify a real document.
- **Where it is kept.** The material sits in a private folder on the owner's computer (proposed: `Documents\legal-cn-private\`). Claude reads it there through the linked-computer bridge for an authorized stage. Any working copy in Claude's session workspace is temporary.
- **What may be committed.** Only redacted, synthetic or aggregate results, plus records that refer to private material by an opaque ID such as `PRIV-CASE-A-001`.
- **Provenance.** Grok-organized material is a derived work product, not original evidence. Route A's gates apply unchanged:
  - a recovered or readable item is not thereby authentic or true;
  - OCR output is not fact;
  - the identity, source, matter and evidence-use decisions stay separate.
- **Confirmation gates.** The human confirmation gates are unchanged. No action with legal consequences is executed.

## Material request

The material request for the Grok bot is `docs/phase2/TASK_PHASE2_REAL_MATTER_MATERIAL_REQUEST_FOR_GROK.md`.
