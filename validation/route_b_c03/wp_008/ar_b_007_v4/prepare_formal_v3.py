"""Prepare the formal-run v3 assets for the AR-B-007 V4 revision from the formal-run v2 assets (prepared under
the V4 limited revision authorization; a run needs a separate owner authorization).

Every v3 file is the v2 file with these mechanical changes only, so the derivation can be reviewed:
  - paths and names: formal_v2 -> formal_v3, project_v2 -> project_v3; the harness is ar_b_007_v4/harness_rev5.py;
  - fixed values: the input SHA (REV5), the expected variant count (40), record kinds (C03_FORMAL_V3_*);
  - the 27 project files are the V4 subject, the unchanged fixtures, input REV5 and harness REV5;
  - the bound list keeps the runtime, system DLL and prior entries of v2 and adds the installed v2 supervisor and
    project files as prior files (they stay on the machine untouched);
  - go_formal_v3.cmd runs the installer first when it has not run yet, so the owner starts one file.
Output: validation/route_b_c03/wp_008/ar_b_007_v4/formal_v3/. Run from the repository root:
  python3 -I validation/route_b_c03/wp_008/ar_b_007_v4/prepare_formal_v3.py [--write]
"""
import hashlib
import json
import os
import sys

V2 = "validation/route_b_c03/wp_008/dsp004_phase7_formal_v2/"
OUT = "validation/route_b_c03/wp_008/ar_b_007_v4/formal_v3/"
INPUT_REL = "validation/route_b_c03/wp_008/ar_b_007_v4/C03_V4_INPUT_CANDIDATE_REV5.json"
HARNESS_REL = "validation/route_b_c03/wp_008/ar_b_007_v4/harness_rev5.py"
V2_INPUT_REL = "validation/route_b_c03/wp_008/DSP_004_INPUT_CANDIDATE_REV4.json"
V2_HARNESS_REL = "validation/route_b_c03/wp_008/dsp004_phase7_formal_v2/harness_rev4.py"
V2_INPUT_SHA = "685BBCBF13BF96746E6DE4201C1FCE72B667CD6A07D0CE0902D9EF9A6C4235C1"
V2_BOUND_SHA = "19A1CE8D54AF938F86BF81DFA54AD2DC9719F12E498F0483AC8B0B08D486BF50"
VARIANTS = 42


def rb(p):
    with open(p, "rb") as f:
        return f.read()


def sha(b):
    return hashlib.sha256(b).hexdigest().upper()


def text(p):
    """v2 .cmd/.ps1 files use CRLF; work on LF text and write CRLF back with crlf()."""
    return rb(p).decode("utf-8").replace("\r\n", "\n")


def crlf(s):
    return s.replace("\n", "\r\n").encode("utf-8")


def sub(s, pairs, where):
    for a, b, n in pairs:
        c = s.count(a)
        if c != n:
            raise SystemExit("SUBSTITUTION_COUNT %s %r expected %d got %d" % (where, a[:70], n, c))
        s = s.replace(a, b)
    return s


def rename(s):
    return s.replace("formal_v2", "formal_v3").replace("project_v2", "project_v3").replace("FORMAL_V2", "FORMAL_V3")


def main():
    v2bound = json.loads(rb(V2 + "bound_list_formal_v2.json").decode("utf-8-sig"))
    if sha(rb(V2 + "bound_list_formal_v2.json")) != V2_BOUND_SHA:
        raise SystemExit("V2_BOUND_SHA_MISMATCH")
    inp = json.loads(rb(INPUT_REL).decode("utf-8"))
    project = {}
    for rel in inp["subject_identities"]:
        project[rel] = rb(rel)
    for rel in inp["fixture_identities"]:
        project[rel] = rb(rel)
    project[INPUT_REL] = rb(INPUT_REL)
    project[HARNESS_REL] = rb(HARNESS_REL)
    for rel, want in list(inp["subject_identities"].items()) + list(inp["fixture_identities"].items()):
        if sha(project[rel]) != want:
            raise SystemExit("INPUT_TABLE_DIFFERS " + rel)
    if len(project) != 27:
        raise SystemExit("PROJECT_COUNT %d" % len(project))
    input_sha = sha(project[INPUT_REL])
    files = {}

    # run_formal_v3.cmd
    run = rename(text(V2 + "run_formal_v2.cmd"))
    run = sub(run, [("rem DSP-004 formal-run launcher v1.", "rem C03 AR-B-007 V4 formal-run launcher (v3).", 1)], "run")
    files["run_formal_v3.cmd"] = crlf(run)

    # bound list
    prior = list(v2bound["PriorFiles"])
    v2_sup = {"supervisor_formal_v2/supervisor_formal_v2.ps1": rb(V2 + "supervisor_formal_v2.ps1"),
              "supervisor_formal_v2/bound_list_formal_v2.json": rb(V2 + "bound_list_formal_v2.json"),
              "supervisor_formal_v2/run_formal_v2.cmd": rb(V2 + "run_formal_v2.cmd")}
    for rel, b in v2_sup.items():
        prior.append({"RelPath": rel, "Bytes": len(b), "SHA256": sha(b)})
    prior.extend(v2bound["ProjectFiles"])
    bound = {"Kind": "C03_FORMAL_V3_BOUND_LIST", "Base": v2bound["Base"],
             "ExpectedOwnerAccessSddl": v2bound["ExpectedOwnerAccessSddl"], "RuntimeFiles": v2bound["RuntimeFiles"],
             "SupervisorFiles": [{"RelPath": "supervisor_formal_v3/run_formal_v3.cmd", "Bytes": len(files["run_formal_v3.cmd"]),
                                  "SHA256": sha(files["run_formal_v3.cmd"])}],
             "PriorFiles": prior,
             "ProjectFiles": [{"RelPath": "project_v3/" + rel, "Bytes": len(b), "SHA256": sha(b)} for rel, b in project.items()],
             "SystemDlls": v2bound["SystemDlls"],
             "Notes": "supervisor_formal_v3.ps1 is not listed (it embeds this file's SHA). PriorFiles are the installed v2, v3, "
                      "formal-v1 and formal-v2 files (supervisor_formal_v1, project_v1, supervisor_formal_v2, project_v2), unchanged."}
    files["bound_list_formal_v3.json"] = (json.dumps(bound, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    bound_sha = sha(files["bound_list_formal_v3.json"])

    # supervisor
    s = text(V2 + "supervisor_formal_v2.ps1")
    s = sub(s, [
        ("# DSP-004 formal-run supervisor v2 = formal v1 with paths moved to project_v2 / harness_rev4 (prepared under owner decision P7-PREPARE; not accepted; a run needs a separate",
         "# C03 AR-B-007 V4 formal-run supervisor v3 = formal v2 with paths moved to project_v3 / harness_rev5, input REV5 and %d variants (prepared under the V4 limited revision authorization; not accepted; a run needs a separate" % VARIANTS, 1),
        ("$ExpectedBoundSha = '%s'" % V2_BOUND_SHA, "$ExpectedBoundSha = '%s'" % bound_sha, 1),
        ("$ExpectedInputSha = '%s'" % V2_INPUT_SHA, "$ExpectedInputSha = '%s'" % input_sha, 1),
        ("'validation\\route_b_c03\\wp_008\\dsp004_phase7_formal_v2\\harness_rev4.py'",
         "'validation\\route_b_c03\\wp_008\\ar_b_007_v4\\harness_rev5.py'", 1),
        ("([int]$t.variants -eq 28) -and ([int]$t.pass -eq 28)",
         "([int]$t.variants -eq %d) -and ([int]$t.pass -eq %d)" % (VARIANTS, VARIANTS), 1),
        ("Kind = 'DSP004_FORMAL_V2_RUN_RECORD'", "Kind = 'C03_FORMAL_V3_RUN_RECORD'", 1),
    ], "supervisor")
    s = rename(s)
    files["supervisor_formal_v3.ps1"] = crlf(s)
    sup_sha = sha(files["supervisor_formal_v3.ps1"])

    sup_map = [("supervisor_formal_v3.ps1", sup_sha), ("bound_list_formal_v3.json", bound_sha),
               ("run_formal_v3.cmd", sha(files["run_formal_v3.cmd"]))]
    proj_map = [(rel, sha(b)) for rel, b in project.items()]

    # installer
    ins = text(V2 + "install_formal_v2.ps1")
    head, rest = ins.split("$Supervisor = [ordered]@{", 1)
    _, rest = rest.split("$Base ", 1)
    block = "$Supervisor = [ordered]@{\n" + "".join("    '%s' = '%s'\n" % kv for kv in sup_map) + "}\n"
    block += "$Project = [ordered]@{\n" + "".join("    '%s' = '%s'\n" % kv for kv in proj_map) + "}\n"
    ins = head + block + "$Base " + rest
    ins = sub(ins, [("(10 subject, 15 fixtures, input REV4, harness REV4)", "(10 subject, 15 fixtures, input REV5, harness REV5)", 1),
                    ("# DSP-004 formal-run v2 installer.", "# C03 AR-B-007 V4 formal-run v3 installer.", 1),
                    ("(prepared under owner\n# decision P7-PREPARE)", "(prepared under the\n# V4 limited revision authorization)", 1)], "installer")
    ins = rename(ins)
    files["install_formal_v3.ps1"] = crlf(ins)
    files["install_formal_v3.cmd"] = crlf(sub(rename(text(V2 + "install_formal_v2.cmd")),
                                              [("rem DSP-004 formal-run v2:", "rem C03 AR-B-007 V4 formal-run v3:", 1)], "install cmd"))

    # collector
    col = text(V2 + "collect_formal_v2.ps1")
    head, rest = col.split("$Expected = [ordered]@{", 1)
    _, rest = rest.split("$Here ", 1)
    block = "$Expected = [ordered]@{\n" + "".join("    'supervisor_formal_v3/%s' = '%s'\n" % kv for kv in sup_map)
    block += "".join("    'project_v3/%s' = '%s'\n" % kv for kv in proj_map) + "}\n"
    col = head + block + "$Here " + rest
    col = sub(col, [("# DSP-004 formal-run v2 collector,", "# C03 AR-B-007 V4 formal-run v3 collector (= formal v2 collector with v3 names and files),", 1),
                    ("Kind = 'DSP004_FORMAL_V2_COLLECT_RESULT'", "Kind = 'C03_FORMAL_V3_COLLECT_RESULT'", 1)], "collector")
    col = rename(col)
    files["collect_formal_v3.ps1"] = crlf(col)

    # go: install first when needed, then the v2 sequence with v3 names
    go = text(V2 + "go_formal_v2.cmd")
    go = sub(go, [("rem DSP-004 formal run v2: run the installed formal supervisor once as dsp004val and collect the audit evidence.",
                   "rem C03 AR-B-007 V4 formal run v3: install the v3 files if not yet installed, run the formal supervisor once as\n"
                   "rem dsp004val and collect the audit evidence.", 1),
                  ('cd /d "%~dp0"\n',
                   'cd /d "%~dp0"\n'
                   'if not exist "%~dp0install_formal_v3_result.json" (\n'
                   '  echo [0/3] Installing the v3 supervisor and project files ...\n'
                   '  "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "%~dp0install_formal_v3.ps1"\n'
                   '  if errorlevel 1 goto fail\n'
                   '  echo.\n'
                   ')\n', 1)], "go")
    files["go_formal_v3.cmd"] = crlf(rename(go))

    for name, b in files.items():
        if b"formal_v2" in b and name not in ("bound_list_formal_v3.json", "collect_formal_v3.ps1", "install_formal_v3.ps1"):
            raise SystemExit("LEFTOVER_V2_NAME " + name)
    summary = {n: {"bytes": len(b), "sha256": sha(b)} for n, b in sorted(files.items())}
    summary["_project_files"] = {rel: s for rel, s in proj_map}
    summary["_counts"] = {"locked_files_expected": len(bound["RuntimeFiles"]) + len(bound["SystemDlls"]) + 1 + 1 + 1
                          + len(prior) + len(bound["ProjectFiles"]),
                          "tree_files_expected": len(bound["RuntimeFiles"]) + len(prior) + 3 + len(bound["ProjectFiles"])}
    print(json.dumps(summary, indent=1))
    if "--write" in sys.argv:
        os.makedirs(OUT, exist_ok=True)
        for n, b in files.items():
            with open(OUT + n, "wb") as f:
                f.write(b)
        with open(OUT + "prepare_summary.json", "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(summary, indent=1) + "\n")


if __name__ == "__main__":
    main()
