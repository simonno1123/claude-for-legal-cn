# Real-Matter Stages Routing Decision (revision 3)

| Field | Value |
| --- | --- |
| Owner | 张纯熙 |
| Date | 2026-11-07 |
| Recorded by | Claude (recorder; owner choices in chat, not a signature) |
| Supersedes | `TASK_PHASE2_REAL_MATTER_STAGES_GROK_EXECUTION_DECISION.md` for any stage where the material is on the owner's computer |
| Owner statement | "C:\workmate-us 案件材料已经在本地可以读取。" Owner choices: "改由 Claude 在本机执行（推荐）"; first stage: "补齐 CASE-A（推荐）" |

## Decision

1. Claude executes the real-material stages on the owner's computer, through the linked-computer bridge, reading only from `C:\workmate-us`.
2. Grok no longer executes these stages. The two Grok returns already recorded stay valid as history.
3. Claude opens only the folders and files relevant to the authorized stage. The rest of the owner's working files are not scanned.
4. Real material, file names, paths and hashes of real documents stay on the owner's computer. The private registry is kept at `Documents\legal-cn-private\`.
5. The public repository receives only status-level, redacted results.
6. Route A gates and the human confirmation gates are unchanged. OCR of real material is used only where the owner authorizes it.
