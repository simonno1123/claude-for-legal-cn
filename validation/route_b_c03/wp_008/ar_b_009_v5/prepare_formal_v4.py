"""Prepare the formal-run v4 assets for the AR-B-009 V5 candidate from the accepted formal-run v3 assets (prepared
under the AR-B-009 work authorization; a run needs a separate owner authorization).

Every v4 file is the v3 file with these mechanical changes only, so the derivation can be reviewed:
  - names: formal_v3 -> formal_v4, project_v3 -> project_v4, FORMAL_V3 -> FORMAL_V4; the harness is
    ar_b_009_v5/harness_rev6.py; header comments name AR-B-009 V5;
  - fixed values: the input SHA (REV6) and the expected variant count (67);
  - the 27 project files are the V5 subject, the unchanged fixtures, input REV6 and harness REV6;
  - the bound list keeps the runtime, system DLL and prior entries of v3 and adds the installed v3 supervisor and
    project files as prior files.
Output: validation/route_b_c03/wp_008/ar_b_009_v5/formal_v4/. Run from the repository root:
  python3 -I validation/route_b_c03/wp_008/ar_b_009_v5/prepare_formal_v4.py [--write]
"""
import hashlib
import json
import os
import sys

V3 = "validation/route_b_c03/wp_008/ar_b_007_v4/formal_v3/"
OUT = "validation/route_b_c03/wp_008/ar_b_009_v5/formal_v4/"
INPUT_REL = "validation/route_b_c03/wp_008/ar_b_009_v5/C03_V5_INPUT_CANDIDATE_REV6.json"
HARNESS_REL = "validation/route_b_c03/wp_008/ar_b_009_v5/harness_rev6.py"
V3_INPUT_SHA = "8A422CEE97A9434201CFA4309A2359672DD3E9ADEBF9322CD1C2AFBD9A27800A"
V3_BOUND_SHA = "B5CBB7B1470E206751A53FF7BA047E0F6493C0DBC8A2BA21B4F6204F5B1A5562"
VARIANTS = 70


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
    return s.replace("formal_v3", "formal_v4").replace("project_v3", "project_v4").replace("FORMAL_V3", "FORMAL_V4")


def replace_block(s, start, end, block):
    head, rest = s.split(start, 1)
    _, rest = rest.split(end, 1)
    return head + block + end + rest


def main():
    if sha(rb(V3 + "bound_list_formal_v3.json")) != V3_BOUND_SHA:
        raise SystemExit("V3_BOUND_SHA_MISMATCH")
    v3bound = json.loads(rb(V3 + "bound_list_formal_v3.json").decode("utf-8"))
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

    run = sub(text(V3 + "run_formal_v3.cmd"), [("rem C03 AR-B-007 V4 formal-run launcher (v3).", "rem C03 AR-B-009 V5 formal-run launcher (v4).", 1)], "run")
    files["run_formal_v4.cmd"] = crlf(rename(run))

    prior = list(v3bound["PriorFiles"])
    for n in ("supervisor_formal_v3.ps1", "bound_list_formal_v3.json", "run_formal_v3.cmd"):
        b = rb(V3 + n)
        prior.append({"RelPath": "supervisor_formal_v3/" + n, "Bytes": len(b), "SHA256": sha(b)})
    prior.extend(v3bound["ProjectFiles"])
    bound = {"Kind": "C03_FORMAL_V4_BOUND_LIST", "Base": v3bound["Base"],
             "ExpectedOwnerAccessSddl": v3bound["ExpectedOwnerAccessSddl"], "RuntimeFiles": v3bound["RuntimeFiles"],
             "SupervisorFiles": [{"RelPath": "supervisor_formal_v4/run_formal_v4.cmd", "Bytes": len(files["run_formal_v4.cmd"]),
                                  "SHA256": sha(files["run_formal_v4.cmd"])}],
             "PriorFiles": prior,
             "ProjectFiles": [{"RelPath": "project_v4/" + rel, "Bytes": len(b), "SHA256": sha(b)} for rel, b in project.items()],
             "SystemDlls": v3bound["SystemDlls"],
             "Notes": "supervisor_formal_v4.ps1 is not listed (it embeds this file's SHA). PriorFiles are the installed v2, v3, "
                      "formal-v1, formal-v2 and formal-v3 files, unchanged."}
    files["bound_list_formal_v4.json"] = (json.dumps(bound, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    bound_sha = sha(files["bound_list_formal_v4.json"])

    s = sub(text(V3 + "supervisor_formal_v3.ps1"), [
        ("# C03 AR-B-007 V4 formal-run supervisor v3 = formal v2 with paths moved to project_v3 / harness_rev5, input REV5 and 42 variants (prepared under the V4 limited revision authorization; not accepted; a run needs a separate",
         "# C03 AR-B-009 V5 formal-run supervisor v4 = formal v3 with paths moved to project_v4 / harness_rev6, input REV6 and %d variants (prepared under the AR-B-009 work authorization; not accepted; a run needs a separate" % VARIANTS, 1),
        ("$ExpectedBoundSha = '%s'" % V3_BOUND_SHA, "$ExpectedBoundSha = '%s'" % bound_sha, 1),
        ("$ExpectedInputSha = '%s'" % V3_INPUT_SHA, "$ExpectedInputSha = '%s'" % input_sha, 1),
        ("'validation\\route_b_c03\\wp_008\\ar_b_007_v4\\harness_rev5.py'", "'validation\\route_b_c03\\wp_008\\ar_b_009_v5\\harness_rev6.py'", 1),
        ("([int]$t.variants -eq 42) -and ([int]$t.pass -eq 42)", "([int]$t.variants -eq %d) -and ([int]$t.pass -eq %d)" % (VARIANTS, VARIANTS), 1),
    ], "supervisor")
    files["supervisor_formal_v4.ps1"] = crlf(rename(s))
    sup_map = [("supervisor_formal_v4.ps1", sha(files["supervisor_formal_v4.ps1"])), ("bound_list_formal_v4.json", bound_sha),
               ("run_formal_v4.cmd", sha(files["run_formal_v4.cmd"]))]
    proj_map = [(rel, sha(b)) for rel, b in project.items()]

    ins = text(V3 + "install_formal_v3.ps1")
    block = "$Supervisor = [ordered]@{\n" + "".join("    '%s' = '%s'\n" % kv for kv in sup_map) + "}\n"
    block += "$Project = [ordered]@{\n" + "".join("    '%s' = '%s'\n" % kv for kv in proj_map) + "}\n"
    ins = replace_block(ins, "$Supervisor = [ordered]@{", "$Base ", block)
    ins = sub(ins, [("(10 subject, 15 fixtures, input REV5, harness REV5)", "(10 subject, 15 fixtures, input REV6, harness REV6)", 1),
                    ("# C03 AR-B-007 V4 formal-run v3 installer.", "# C03 AR-B-009 V5 formal-run v4 installer.", 1),
                    ("(prepared under the\n# V4 limited revision authorization)", "(prepared under the\n# AR-B-009 work authorization)", 1)], "installer")
    files["install_formal_v4.ps1"] = crlf(rename(ins))
    files["install_formal_v4.cmd"] = crlf(rename(sub(text(V3 + "install_formal_v3.cmd"),
                                                     [("rem C03 AR-B-007 V4 formal-run v3:", "rem C03 AR-B-009 V5 formal-run v4:", 1)], "install cmd")))

    col = text(V3 + "collect_formal_v3.ps1")
    block = "$Expected = [ordered]@{\n" + "".join("    'supervisor_formal_v4/%s' = '%s'\n" % kv for kv in sup_map)
    block += "".join("    'project_v4/%s' = '%s'\n" % kv for kv in proj_map) + "}\n"
    col = replace_block(col, "$Expected = [ordered]@{", "$Here ", block)
    col = sub(col, [("# C03 AR-B-007 V4 formal-run v3 collector (= formal v2 collector with v3 names and files),",
                     "# C03 AR-B-009 V5 formal-run v4 collector (= formal v2 collector with v4 names and files),", 1)], "collector")
    files["collect_formal_v4.ps1"] = crlf(rename(col))

    go = sub(text(V3 + "go_formal_v3.cmd"), [
        ("rem C03 AR-B-007 V4 formal run v3: install the v3 files if not yet installed, run the formal supervisor once as",
         "rem C03 AR-B-009 V5 formal run v4: install the v4 files if not yet installed, run the formal supervisor once as", 1),
        ("echo [0/3] Installing the v3 supervisor and project files ...", "echo [0/3] Installing the v4 supervisor and project files ...", 1)], "go")
    files["go_formal_v4.cmd"] = crlf(rename(go))

    for name, b in files.items():
        if (b"formal_v3" in b or b"project_v3" in b) and name != "bound_list_formal_v4.json":
            raise SystemExit("LEFTOVER_V3_NAME " + name)
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
