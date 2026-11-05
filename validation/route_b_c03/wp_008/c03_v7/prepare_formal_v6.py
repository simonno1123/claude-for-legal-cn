"""Prepare the formal-run v6 assets for the V7 candidate from the accepted formal-run v5 assets (prepared under
owner decision AR-B-008-V7-FIRST; a run needs a separate owner authorization).

Every v6 file is the v5 file with these mechanical changes only, so the derivation can be reviewed:
  - names: formal_v5 -> formal_v6, project_v5 -> project_v6, FORMAL_V5 -> FORMAL_V6; the harness is
    c03_v7/harness_rev8.py; header comments name C03 V7;
  - fixed values: the input SHA (REV8) and the expected variant count (93);
  - the 27 project files are the V7 subject, the unchanged fixtures, input REV8 and harness REV8;
  - the bound list keeps the runtime, system DLL and prior entries of v5 and adds the installed v5 supervisor and
    project files as prior files.
Output: validation/route_b_c03/wp_008/c03_v7/formal_v6/. Run from the repository root:
  python3 -I validation/route_b_c03/wp_008/c03_v7/prepare_formal_v6.py [--write]
"""
import hashlib
import json
import os
import sys

V3 = "validation/route_b_c03/wp_008/c03_v6/formal_v5/"
OUT = "validation/route_b_c03/wp_008/c03_v7/formal_v6/"
INPUT_REL = "validation/route_b_c03/wp_008/c03_v7/C03_V7_INPUT_CANDIDATE_REV8.json"
HARNESS_REL = "validation/route_b_c03/wp_008/c03_v7/harness_rev8.py"
V3_INPUT_SHA = "3E01C1961BC435608A7907A35C6E0C013E26312011A6D68983E44E24FEB76E2F"
V3_BOUND_SHA = "C41C6FE46E30BDE4595F6714599E72931E053E0C06411DD30700C94951BF8E2F"
VARIANTS = 93


def rb(p):
    with open(p, "rb") as f:
        return f.read()


def sha(b):
    return hashlib.sha256(b).hexdigest().upper()


def text(p):
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
    return s.replace("formal_v5", "formal_v6").replace("project_v5", "project_v6").replace("FORMAL_V5", "FORMAL_V6")


def replace_block(s, start, end, block):
    head, rest = s.split(start, 1)
    _, rest = rest.split(end, 1)
    return head + block + end + rest


def main():
    if sha(rb(V3 + "bound_list_formal_v5.json")) != V3_BOUND_SHA:
        raise SystemExit("V3_BOUND_SHA_MISMATCH")
    v3bound = json.loads(rb(V3 + "bound_list_formal_v5.json").decode("utf-8"))
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

    run = sub(text(V3 + "run_formal_v5.cmd"), [("rem C03 V6 formal-run launcher (v5).", "rem C03 V7 formal-run launcher (v6).", 1)], "run")
    files["run_formal_v6.cmd"] = crlf(rename(run))

    prior = list(v3bound["PriorFiles"])
    for n in ("supervisor_formal_v5.ps1", "bound_list_formal_v5.json", "run_formal_v5.cmd"):
        b = rb(V3 + n)
        prior.append({"RelPath": "supervisor_formal_v5/" + n, "Bytes": len(b), "SHA256": sha(b)})
    prior.extend(v3bound["ProjectFiles"])
    bound = {"Kind": "C03_FORMAL_V6_BOUND_LIST", "Base": v3bound["Base"],
             "ExpectedOwnerAccessSddl": v3bound["ExpectedOwnerAccessSddl"], "RuntimeFiles": v3bound["RuntimeFiles"],
             "SupervisorFiles": [{"RelPath": "supervisor_formal_v6/run_formal_v6.cmd", "Bytes": len(files["run_formal_v6.cmd"]),
                                  "SHA256": sha(files["run_formal_v6.cmd"])}],
             "PriorFiles": prior,
             "ProjectFiles": [{"RelPath": "project_v6/" + rel, "Bytes": len(b), "SHA256": sha(b)} for rel, b in project.items()],
             "SystemDlls": v3bound["SystemDlls"],
             "Notes": "supervisor_formal_v6.ps1 is not listed (it embeds this file's SHA). PriorFiles are the installed v2, v3, "
                      "formal-v1 to formal-v5 files, unchanged."}
    files["bound_list_formal_v6.json"] = (json.dumps(bound, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    bound_sha = sha(files["bound_list_formal_v6.json"])

    s = sub(text(V3 + "supervisor_formal_v5.ps1"), [
        ("# C03 V6 formal-run supervisor v5 = formal v4 with paths moved to project_v5 / harness_rev7, input REV7 and 76 variants (prepared under owner decision AR-B-008-KEEP-OPEN; not accepted; a run needs a separate",
         "# C03 V7 formal-run supervisor v6 = formal v5 with paths moved to project_v6 / harness_rev8, input REV8 and %d variants (prepared under owner decision AR-B-008-V7-FIRST; not accepted; a run needs a separate" % VARIANTS, 1),
        ("$ExpectedBoundSha = '%s'" % V3_BOUND_SHA, "$ExpectedBoundSha = '%s'" % bound_sha, 1),
        ("$ExpectedInputSha = '%s'" % V3_INPUT_SHA, "$ExpectedInputSha = '%s'" % input_sha, 1),
        ("'validation\\route_b_c03\\wp_008\\c03_v6\\harness_rev7.py'", "'validation\\route_b_c03\\wp_008\\c03_v7\\harness_rev8.py'", 1),
        ("([int]$t.variants -eq 76) -and ([int]$t.pass -eq 76)", "([int]$t.variants -eq %d) -and ([int]$t.pass -eq %d)" % (VARIANTS, VARIANTS), 1),
    ], "supervisor")
    files["supervisor_formal_v6.ps1"] = crlf(rename(s))
    sup_map = [("supervisor_formal_v6.ps1", sha(files["supervisor_formal_v6.ps1"])), ("bound_list_formal_v6.json", bound_sha),
               ("run_formal_v6.cmd", sha(files["run_formal_v6.cmd"]))]
    proj_map = [(rel, sha(b)) for rel, b in project.items()]

    ins = text(V3 + "install_formal_v5.ps1")
    block = "$Supervisor = [ordered]@{\n" + "".join("    '%s' = '%s'\n" % kv for kv in sup_map) + "}\n"
    block += "$Project = [ordered]@{\n" + "".join("    '%s' = '%s'\n" % kv for kv in proj_map) + "}\n"
    ins = replace_block(ins, "$Supervisor = [ordered]@{", "$Base ", block)
    ins = sub(ins, [("(10 subject, 15 fixtures, input REV7, harness REV7)", "(10 subject, 15 fixtures, input REV8, harness REV8)", 1),
                    ("# C03 V6 formal-run v5 installer.", "# C03 V7 formal-run v6 installer.", 1),
                    ("(prepared under owner\n# decision AR-B-008-KEEP-OPEN)", "(prepared under owner\n# decision AR-B-008-V7-FIRST)", 1)], "installer")
    files["install_formal_v6.ps1"] = crlf(rename(ins))
    files["install_formal_v6.cmd"] = crlf(rename(sub(text(V3 + "install_formal_v5.cmd"),
                                                     [("rem C03 V6 formal-run v5:", "rem C03 V7 formal-run v6:", 1)], "install cmd")))

    col = text(V3 + "collect_formal_v5.ps1")
    block = "$Expected = [ordered]@{\n" + "".join("    'supervisor_formal_v6/%s' = '%s'\n" % kv for kv in sup_map)
    block += "".join("    'project_v6/%s' = '%s'\n" % kv for kv in proj_map) + "}\n"
    col = replace_block(col, "$Expected = [ordered]@{", "$Here ", block)
    col = sub(col, [("# C03 V6 formal-run v5 collector (= formal v2 collector with v5 names and files),",
                     "# C03 V7 formal-run v6 collector (= formal v2 collector with v6 names and files),", 1)], "collector")
    files["collect_formal_v6.ps1"] = crlf(rename(col))

    go = sub(text(V3 + "go_formal_v5.cmd"), [
        ("rem C03 V6 formal run v5: install the v5 files if not yet installed, run the formal supervisor once as",
         "rem C03 V7 formal run v6: install the v6 files if not yet installed, run the formal supervisor once as", 1),
        ("echo [0/3] Installing the v5 supervisor and project files ...", "echo [0/3] Installing the v6 supervisor and project files ...", 1)], "go")
    files["go_formal_v6.cmd"] = crlf(rename(go))

    for name, b in files.items():
        if (b"formal_v5" in b or b"project_v5" in b) and name != "bound_list_formal_v6.json":
            raise SystemExit("LEFTOVER_V5_NAME " + name)
    summary = {n: {"bytes": len(b), "sha256": sha(b)} for n, b in sorted(files.items())}
    summary["_project_files"] = {rel: s for rel, s in proj_map}
    summary["_counts"] = {"locked_files_expected": len(bound["RuntimeFiles"]) + len(bound["SystemDlls"]) + 3
                          + len(prior) + len(bound["ProjectFiles"]),
                          "tree_files_expected": len(bound["RuntimeFiles"]) + len(prior) + 3 + len(bound["ProjectFiles"])}
    print(json.dumps({k: v for k, v in summary.items() if k != "_project_files"}, indent=1))
    if "--write" in sys.argv:
        os.makedirs(OUT, exist_ok=True)
        for n, b in files.items():
            with open(OUT + n, "wb") as f:
                f.write(b)
        with open(OUT + "prepare_summary.json", "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(summary, indent=1) + "\n")


if __name__ == "__main__":
    main()
