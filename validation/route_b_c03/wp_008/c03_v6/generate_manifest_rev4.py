"""C03 V6 Manifest generator REV4 = the accepted REV3 generator with its inputs moved to the V6 assets (prepared
under owner decision AR-B-008-KEEP-OPEN; not accepted).

Changes from REV3, all by substitution: input REV7, harness REV7, bound list formal v5 (PROJECT_ROOT project_v5),
support policies REV4, generation authority = the AR-B-009 closure decision record (AR-B-008-KEEP-OPEN), pre-run
review = the V6 revision review, PROJECT_ROOT integrity evidence = the v5 installer constants, harness identifiers
HARNESS-REV7, manifest_version REV4, output c03_v6/PYTHON_RUNTIME_DEPENDENCY_MANIFEST_REV4.json. The import closure
is still the observed preflight-v2 closure, confirmed unchanged by formal runs v3 and v4.

Run from the repository root:
  python3 -I validation/route_b_c03/wp_008/c03_v6/generate_manifest_rev4.py [--write]
"""
import hashlib
import json
import os
import sys

W = "validation/route_b_c03/wp_008/"
D = "docs/phase2/route-b/"
OUT = W + "c03_v6/PYTHON_RUNTIME_DEPENDENCY_MANIFEST_REV4.json"
P = {
    "package": D + "TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V3_2_CANDIDATE.md",
    "plan": D + "TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_2_CANDIDATE.md",
    "adoption": ".codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_WP_008_V3_2_V2_2_DESIGN_PAIR_ADOPTION_RECORD.md",
    "contract": D + "TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_TYPED_CONTRACT_REV3_CANDIDATE.md",
    "registry": D + "TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_ARRAY_POLICY_REGISTRY_REV3_CANDIDATE.md",
    "contract_acceptance": W + "DSP_004_B02_CONTRACT_ACCEPTANCE_REV1.json",
    "env": W + "DSP_004_PHASE1_ADMISSION_DECISIONS_REV1.json",
    "authority": ".codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_AR_B_009_CLOSURE_DECISION.json",
    "p25": W + "DSP_004_PHASES_2_TO_5_OWNER_DECISIONS_REV1.json",
    "p4accept": W + "DSP_004_PHASE4_ACCEPTANCE_REV1.json",
    "policies": D + "TASK_PHASE2_ROUTE_B_C03_WP_008_C03_V6_MANIFEST_SUPPORT_POLICIES_REV4.md",
    "input": W + "c03_v6/C03_V6_INPUT_CANDIDATE_REV7.json",
    "harness": W + "c03_v6/harness_rev7.py",
    "bound": W + "c03_v6/formal_v5/bound_list_formal_v5.json",
    "v2binding": ".codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_V6_REVISION_REVIEW_REV1.md",
    "closure": W + "dsp004_phase7_preflight_v2/preflight2_import_closure.json",
    "preflight": W + "DSP_004_PREFLIGHT_V2_RESULT.json",
    "install": W + "c03_v6/formal_v5/prepare_summary.json",
    "ordered": W + "DSP_004_ORDERED_SOURCE_REGISTRY_REV1_CANDIDATE.json",
}
RUNTIME_DIR = "C:\\Program Files\\DSP004Runtime\\Python312\\"
SYSTEM_DIR = "C:\\WINDOWS\\SYSTEM32\\"
PROJECT_DIR = "C:\\Program Files\\DSP004Runtime\\project_v5\\"
CATEGORIES = ["PYTHON_EXECUTABLE", "PYTHON_CONFIG", "CPYTHON_CORE_DLL", "STDLIB_SOURCE", "STDLIB_EXTENSION", "STDLIB_DATA",
              "OS_RUNTIME_DLL", "HARNESS_SOURCE", "SUBJECT_SOURCE", "GOVERNANCE_INPUT", "FIXTURE_INPUT", "SCENARIO_INPUT_BINDING"]
ROLE = {"PYTHON_EXECUTABLE": "VALIDATION_ENTRYPOINT", "PYTHON_CONFIG": "VALIDATION_ENVIRONMENT_CONFIG",
        "CPYTHON_CORE_DLL": "CPYTHON_BOOTSTRAP_LIBRARY", "STDLIB_SOURCE": "APPROVED_STDLIB_SOURCE",
        "STDLIB_EXTENSION": "APPROVED_STDLIB_EXTENSION", "STDLIB_DATA": "APPROVED_LITERAL_DATA",
        "OS_RUNTIME_DLL": "APPROVED_OS_BOOTSTRAP_LIBRARY", "HARNESS_SOURCE": "VALIDATION_HARNESS_SOURCE",
        "SUBJECT_SOURCE": "FIXED_SUBJECT_SOURCE", "GOVERNANCE_INPUT": "PREFLIGHT_GOVERNANCE_INPUT",
        "FIXTURE_INPUT": "ORIGINAL_SCENARIO_FIXTURE", "SCENARIO_INPUT_BINDING": "ADMITTED_CONCRETE_INPUT_BINDING"}
DENIED_MODULES = ["ssl", "http", "urllib", "ftplib", "smtplib", "imaplib", "poplib", "telnetlib", "webbrowser",
                  "subprocess", "multiprocessing", "ctypes"]
DENIED_CAPS = ["NETWORK_IO", "PROCESS_CREATION", "DYNAMIC_CODE_OUTSIDE_APPROVED_OPERATIONS", "UNDECLARED_FILE_ACCESS",
               "IMPORT_SEARCH_PATH_MUTATION", "GUARD_STATE_MUTATION", "UNREVIEWED_EXTENSION_LOADING",
               "EXTERNAL_TOOL_INVOCATION", "TARGET_PRELOAD_IN_T1", "LATE_LOADING_IN_T4"]
EXCLUSION_CATEGORIES = ["SITE_PACKAGES", "INSTALLATION_TOOL", "DEVELOPMENT_HEADER", "UNUSED_TEST_ASSET", "TK_TCL",
                        "PACKAGE_METADATA", "DOCUMENTATION", "BYTECODE", "CACHE", "UNUSED_ASSET"]
PHASE_RANK = {"T1": 1, "T2": 2, "T3": 3, "T4": 4}


def raw(p):
    with open(p, "rb") as f:
        return f.read()


def sha(b):
    return hashlib.sha256(b).hexdigest().upper()


def load(p):
    return json.loads(raw(p).decode("utf-8-sig"))


def aref(key, locator):
    b = raw(P[key])
    return {"path": P[key], "sha256": sha(b), "locator": locator}


# ---------- CANON-2 encoder (typed contract section 5) ----------
def enc_str(s):
    out = ['"']
    for ch in s:
        o = ord(ch)
        if 0xD800 <= o <= 0xDFFF:
            raise ValueError("SURROGATE")
        if ch == '"':
            out.append('\\"')
        elif ch == "\\":
            out.append("\\\\")
        elif o < 0x20:
            out.append("\\u%04x" % o)
        else:
            out.append(ch)
    out.append('"')
    return "".join(out)


def enc_scalar(v):
    if v is True:
        return "true"
    if v is False:
        return "false"
    if isinstance(v, int):
        if v < 0:
            raise ValueError("NEGATIVE")
        return str(v)
    if isinstance(v, str):
        return enc_str(v)
    raise ValueError("BAD_SCALAR %r" % (v,))


def cp_key(s):
    return [ord(c) for c in s]


def enc(v, depth=0):
    pad = "  " * (depth + 1)
    end = "  " * depth
    if isinstance(v, dict):
        if not v:
            return "{}"
        items = sorted(v.items(), key=lambda kv: cp_key(kv[0]))
        return "{\n" + ",\n".join(pad + enc_str(k) + ": " + enc(x, depth + 1) for k, x in items) + "\n" + end + "}"
    if isinstance(v, list):
        if not v:
            return "[]"
        return "[\n" + ",\n".join(pad + enc(x, depth + 1) for x in v) + "\n" + end + "]"
    return enc_scalar(v)


# ---------- helpers ----------
def fileref(root, rel, bts, sh):
    return {"root_id": root, "relative_path": rel, "byte_length": bts, "sha256": sh}


def main():
    write = "--write" in sys.argv
    inp = load(P["input"])
    bound = load(P["bound"])
    closure = load(P["closure"])
    ordered = load(P["ordered"])
    rt = {f["RelPath"][len("Python312/"):].lower(): f for f in bound["RuntimeFiles"]}
    sysd = {f["Path"].split("\\")[-1].lower(): f for f in bound["SystemDlls"]}
    proj = {f["RelPath"][len("project_v5/"):]: f for f in bound["ProjectFiles"]}

    def rt_ref(abs_or_rel):
        rel = abs_or_rel[len(RUNTIME_DIR):] if abs_or_rel.lower().startswith(RUNTIME_DIR.lower()) else abs_or_rel
        f = rt[rel.replace("\\", "/").lower()]
        return fileref("RUNTIME_ROOT", f["RelPath"][len("Python312/"):], f["Bytes"], f["SHA256"])

    def sys_ref(name):
        f = sysd[name.lower()]
        return fileref("SYSTEM_ROOT", f["Path"].split("\\")[-1], f["Bytes"], f["SHA256"])

    def proj_ref(rel):
        f = proj[rel]
        return fileref("PROJECT_ROOT", rel, f["Bytes"], f["SHA256"])

    harness_rel = "validation/route_b_c03/wp_008/c03_v6/harness_rev7.py"
    input_rel = "validation/route_b_c03/wp_008/c03_v6/C03_V6_INPUT_CANDIDATE_REV7.json"
    assert sha(raw(P["harness"])) == proj[harness_rel]["SHA256"]
    assert sha(raw(P["input"])) == proj[input_rel]["SHA256"]
    harness = proj_ref(harness_rel)
    python_exe = rt_ref("python.exe")
    core = rt_ref("python312.dll")

    # ---------- entries ----------
    entries = []

    def add(cat, ref, loader, phase, required_by, import_name="NOT_APPLICABLE", executable=False, net=False):
        entries.append({"entry_id": "%s:%s:%s" % (cat, ref["root_id"], ref["relative_path"]), "category": cat,
                        "root_id": ref["root_id"], "relative_path": ref["relative_path"], "byte_length": ref["byte_length"],
                        "sha256": ref["sha256"], "role": ROLE[cat], "required_by": required_by, "import_name": import_name,
                        "loader_kind": loader, "read_phase": phase, "executable": executable, "network_capable": net,
                        "reparse_state": "DIRECT"})

    natives = closure["NativeModules"]
    add("PYTHON_EXECUTABLE", python_exe, "EXECUTABLE", "T1", "BOOTSTRAP", executable=True)
    for n in natives:
        if n.lower().startswith(RUNTIME_DIR.lower()):
            rel = n[len(RUNTIME_DIR):]
            if rel.lower() in ("python.exe",):
                continue
            if "\\" not in rel:
                add("CPYTHON_CORE_DLL", rt_ref(rel), "DLL", "T1", "BOOTSTRAP")
            elif rel.lower() == "dlls\\_hashlib.pyd":
                add("STDLIB_EXTENSION", rt_ref(rel), "EXTENSION", "T1,T3", "HARNESS-REV7", import_name="_hashlib")
            elif rel.lower() == "dlls\\libcrypto-3.dll":
                add("STDLIB_EXTENSION", rt_ref(rel), "DLL", "T1,T3", "EXTENSION-_hashlib")
            else:
                raise SystemExit("UNCLASSIFIED_RUNTIME_NATIVE " + n)
        elif n.lower().startswith(SYSTEM_DIR.lower()):
            name = n.split("\\")[-1]
            add("OS_RUNTIME_DLL", sys_ref(name), "DLL", "T1", "PE-CLOSURE", net=(name.lower() == "ws2_32.dll"))
        else:
            raise SystemExit("NATIVE_OUTSIDE_ROOTS " + n)
    src_modules = [m for m in closure["Modules"] if m["Loader"] == "SourceFileLoader"]
    seen = set()
    for m in src_modules:
        ref = rt_ref(m["Origin"])
        if ref["relative_path"] in seen:
            continue
        seen.add(ref["relative_path"])
        add("STDLIB_SOURCE", ref, "SOURCE", "T1,T3", "HARNESS-REV7", import_name=m["Name"])
    add("HARNESS_SOURCE", harness, "SOURCE", "T1", "BOOTSTRAP", import_name="__main__")
    loaded_subject = {m["Name"]: m for m in closure["Modules"] if m["Loader"] == "BytesImporter"}
    subj_names = {}
    for rel in inp["subject_identities"]:
        mod = rel[len("scripts/"):-3].replace("/", ".")
        if mod.endswith(".__init__"):
            mod = mod[: -len(".__init__")]
        subj_names[rel] = mod
        add("SUBJECT_SOURCE", proj_ref(rel), "SOURCE", "T2,T3", "HARNESS-REV7", import_name=mod)
    for rel in inp["fixture_identities"]:
        add("FIXTURE_INPUT", proj_ref(rel), "DATA", "T2", "HARNESS-REV7")
    add("SCENARIO_INPUT_BINDING", proj_ref(input_rel), "DATA", "T2", "HARNESS-REV7")

    # uniqueness, then canonical sort and numbering (contract rule 12)
    ids = [e["entry_id"] for e in entries]
    files = [(e["root_id"], e["relative_path"].lower()) for e in entries]
    dup = (len(ids) - len(set(ids))) + (len(files) - len(set(files)))
    entries.sort(key=lambda e: (cp_key(e["category"]), cp_key(e["root_id"]), cp_key(e["relative_path"]), cp_key(e["entry_id"])))
    for i, e in enumerate(entries, 1):
        e["ordinal"] = i
    order15 = ["ordinal", "entry_id", "category", "root_id", "relative_path", "byte_length", "sha256", "role", "required_by",
               "import_name", "loader_kind", "read_phase", "executable", "network_capable", "reparse_state"]
    stream = b"".join(("\x1f".join(enc_scalar(e[k]) for k in order15) + "\n").encode("utf-8") for e in entries)
    agg_sha = sha(stream)
    counts = {c: 0 for c in CATEGORIES}
    for e in entries:
        counts[e["category"]] += 1

    # ---------- modules ----------
    interp = {"kind": "INTERPRETER", "identity": core, "symbol": "importlib._bootstrap._find_and_load",
              "basis": aref("policies", "§O1")}
    modules = []
    for m in closure["Modules"]:
        name, loader = m["Name"], m["Loader"]
        parent = name.rsplit(".", 1)[0] if "." in name else "NOT_APPLICABLE"
        if loader == "SourceFileLoader":
            kind, ident, ld = "SOURCE", rt_ref(m["Origin"]), {"kind": "INTERPRETER", "identity": core, "symbol": "SourceFileLoader", "basis": aref("policies", "§O1")}
            phases = ["T1", "T3"]
        elif loader == "ExtensionFileLoader":
            kind, ident, ld = "EXTENSION", rt_ref(m["Origin"]), {"kind": "INTERPRETER", "identity": core, "symbol": "ExtensionFileLoader", "basis": aref("policies", "§O1")}
            phases = ["T1", "T3"]
        elif loader in ("BuiltinImporter", "FrozenImporter"):
            kind, ident, ld = ("BUILTIN" if loader == "BuiltinImporter" else "FROZEN"), core, {"kind": "INTERPRETER", "identity": core, "symbol": loader, "basis": aref("policies", "§O1")}
            phases = ["T1", "T3"]
        elif loader == "BytesImporter":
            rel = [r for r, n in subj_names.items() if n == name][0]
            kind, ident, ld = "SOURCE", proj_ref(rel), {"kind": "FILE", "identity": harness, "symbol": "BytesImporter", "basis": aref("policies", "§O1")}
            phases = ["T3"]
        elif name == "__main__":
            kind, ident, ld = "SOURCE", harness, {"kind": "INTERPRETER", "identity": core, "symbol": "main script execution (python.exe <harness>)", "basis": aref("policies", "§O1")}
            phases = ["T1"]
        elif name in ("typing.io", "typing.re"):
            kind, ident, ld = "SOURCE", rt_ref("Lib\\typing.py"), {"kind": "FILE", "identity": rt_ref("Lib\\typing.py"), "symbol": "typing pseudo-module registration", "basis": aref("policies", "§C1")}
            phases = ["T1", "T3"]
        else:
            raise SystemExit("UNCLASSIFIED_MODULE " + name)
        modules.append({"module_name": name, "parent": parent, "kind": kind, "identity": ident, "loader": ld, "caller": interp,
                        "read_phases": phases, "evidence": [aref("closure", "$.Modules[Name=%s]" % name)]})
    modules.sort(key=lambda r: cp_key(r["module_name"]))
    module_names = {m["module_name"] for m in modules}
    denied_overlap = sorted(n for n in module_names if n.split(".")[0] in DENIED_MODULES)
    unresolved = sum(1 for m in modules if m["kind"] in ("SOURCE", "EXTENSION") and m["identity"]["root_id"] not in ("RUNTIME_ROOT", "PROJECT_ROOT"))

    # ---------- startup and lookup (ORDERED, from the ORDERED registry + harness REV7) ----------
    steps = []
    for s in ordered["Policies"]["AP-006"]["sequence"]:
        f = harness if s["step_id"] == "STARTUP-04-HARNESS" else s["file"]
        steps.append({"step_id": s["step_id"], "ordinal": s["ordinal"], "file": f, "role": s["role"],
                      "required_by": "BOOTSTRAP", "basis": aref("ordered", "$.Policies.AP-006")})
    lookups = []
    for it in ordered["Policies"]["AP-009"]["sequence"]:
        loc = it["location"]
        lookups.append({"lookup_kind": it["lookup_kind"], "root_id": it["root_id"],
                        "location": {"kind": "ROOT_SELF"} if loc["kind"] == "ROOT_SELF" else {"kind": "RELATIVE", "relative_path": loc["relative_path"]},
                        "basis": aref("ordered", "$.Policies.AP-009")})

    # ---------- read scopes ----------
    purpose = {"EXECUTABLE": "BOOTSTRAP_LOAD", "DLL": "BOOTSTRAP_LOAD", "EXTENSION": "LITERAL_IMPORT"}
    scopes = {"PROJECT_ROOT": [], "RUNTIME_ROOT": [], "SYSTEM_ROOT": []}
    for e in entries:
        f = fileref(e["root_id"], e["relative_path"], e["byte_length"], e["sha256"])
        for ph in e["read_phase"].split(","):
            if e["category"] == "HARNESS_SOURCE":
                pu = "BOOTSTRAP_LOAD"
            elif e["category"] == "SUBJECT_SOURCE":
                pu = "SOURCE_PARSE" if ph == "T2" else "LITERAL_IMPORT"
            elif e["category"] == "FIXTURE_INPUT":
                pu = "FIXTURE_READ"
            elif e["category"] == "SCENARIO_INPUT_BINDING":
                pu = "BINDING_READ"
            elif e["category"] == "STDLIB_SOURCE":
                pu = "LITERAL_IMPORT"
            else:
                pu = purpose[e["loader_kind"]]
            scopes[e["root_id"]].append({"file": f, "purpose": pu, "phase": ph, "basis": aref("policies", "§R1")})
    for k in scopes:
        scopes[k].sort(key=lambda s: (cp_key(s["file"]["root_id"]), cp_key(s["file"]["relative_path"]), cp_key(s["purpose"]), cp_key(s["phase"])))

    def root_binding(rid, directory, resolver, version, source, review, owner, limits):
        ev = sorted([aref("install", "$._project_files"), aref("preflight", "$.Run"), aref("bound", "$")],
                    key=lambda a: (cp_key(a["path"]), cp_key(a["locator"])))
        return {"root_id": rid, "canonical_directory": directory, "source_record": source, "independent_review": review,
                "owner_decision": owner, "resolver": resolver, "resolver_version": version,
                "case_policy": aref("policies", "§R1 case"), "reparse_policy": aref("policies", "§R1 reparse"),
                "read_scope": scopes[rid], "integrity_evidence": ev, "residual_limitations": sorted(limits, key=cp_key)}

    review = aref("v2binding", "whole record")
    roots = [
        root_binding("PROJECT_ROOT", PROJECT_DIR[:-1], {"kind": "FILE", "identity": harness, "symbol": "read_bound / BytesImporter path join", "basis": aref("policies", "§R1")},
                     "harness_rev7", aref("install", "$.install_formal_v5.ps1"), review, aref("authority", "$.Decisions[Id=AR-B-008-KEEP-OPEN]"),
                     ["project files bound by installer constants and supervisor re-hash; no object-access auditing"]),
        root_binding("RUNTIME_ROOT", RUNTIME_DIR[:-1], {"kind": "INTERPRETER", "identity": core, "symbol": "sys.path PathFinder", "basis": aref("policies", "§O1")},
                     "CPython 3.12.10", aref("env", "$.Phase1Environment"), review, aref("env", "$.Decisions[Id=P1-ADMIT]"),
                     ["BUILTIN\\Users read/execute on the runtime (P1-RESIDUALS)"]),
        root_binding("SYSTEM_ROOT", "C:\\Windows\\System32", {"kind": "INTERPRETER", "identity": sys_ref("ntdll.dll"), "symbol": "Windows loader (LdrLoadDll)", "basis": aref("policies", "§O1")},
                     "Windows build recorded in the run record", aref("env", "$.Phase1Environment"), review, aref("env", "$.Decisions[Id=P1-RESIDUALS]"),
                     ["KnownDLLs are mapped from boot-time sections, not from the hashed files (P1-RESIDUALS)"]),
    ]
    roots.sort(key=lambda r: cp_key(r["root_id"]))

    # ---------- input contract ----------
    subjects = sorted([{"subject_id": subj_names[r], "file": proj_ref(r), "callable_record": aref("input", "$.adapter_catalog")}
                       for r in inp["subject_identities"]], key=lambda s: cp_key(s["subject_id"]))
    fixtures = [{"scenario_id": s["scenario_id"], "file": proj_ref(s["fixture"]["path"])} for s in inp["scenarios"]]
    adapters = inp["adapter_catalog"]
    scenarios = []
    for i, s in enumerate(inp["scenarios"]):
        vs = []
        for j, v in enumerate(s["stimulus_variants"]):
            subj_path = adapters[v["adapter_id"]]["subject_path"]
            lim = [] if s["coverage_class_rev3"] == "FULL" else [aref("p25", "$.Decisions[Id=P5-LIMITED]")]
            vs.append({"variant_id": v["stimulus_binding_id"], "input_locator": "$.scenarios[%d].stimulus_variants[%d]" % (i, j),
                       "expected_locator": "$.comparison_rule_catalog[%s]" % v["comparison_rule_id"],
                       "subject_id": subj_names[subj_path], "callable_id": v["adapter_id"],
                       "observation_policy": aref("input", "$.comparison_rule_catalog[%s]" % v["comparison_rule_id"]),
                       "limitation_dispositions": lim})
        scenarios.append({"scenario_id": s["scenario_id"], "fixture": proj_ref(s["fixture"]["path"]), "variants": vs})
    input_binding = proj_ref(input_rel)

    def sorted_refs(refs):
        return sorted(refs, key=lambda a: (cp_key(a["path"]), cp_key(a["locator"])))

    def op(oid, cls, origin, phases, sites, limits):
        return {"operation_id": oid, "operation_class": cls, "origin": origin, "read_phases": phases,
                "declaration_sites": sorted(sites, key=lambda s: cp_key(s["declaration_id"])),
                "content_policy": aref("policies", "§T1 %s content" % cls), "namespace_policy": aref("policies", "§T1 %s namespace" % cls),
                "input_policy": aref("policies", "§T1 %s input" % cls),
                "enforcement_evidence": sorted_refs([aref("harness", "docstring points 3-5"), aref("preflight", "$.Run.HarnessTotals.guard_denied")]),
                "limitations": sorted(limits, key=cp_key)}
    dc_src = rt_ref("Lib\\dataclasses.py")
    ast_src = rt_ref("Lib\\ast.py")
    ops = sorted([
        op("OP-STATIC-AST-PARSE", "STATIC_AST_PARSE", {"kind": "FILE", "identity": ast_src, "symbol": "ast.parse", "basis": aref("policies", "§T1")}, ["T2"],
           [{"declaration_id": "SITE-HARNESS-SCAN", "kind": "FILE_SITE", "identity": harness, "locator": "def scan", "basis": aref("policies", "§T1")}],
           ["the scan does not catch calls reached through module attributes"]),
        op("OP-NORMAL-LITERAL-IMPORT", "NORMAL_LITERAL_IMPORT", {"kind": "INTERPRETER", "identity": core, "symbol": "importlib._bootstrap._find_and_load", "basis": aref("policies", "§O1")}, ["T1", "T3"],
           [{"declaration_id": "SITE-HARNESS-LOAD-SUBJECT", "kind": "FILE_SITE", "identity": harness, "locator": "def load_subject", "basis": aref("policies", "§T1")}],
           ["caller attribution per module is not recorded (§O1)"]),
        op("OP-DATACLASS-INTERNAL-GENERATION", "DATACLASS_INTERNAL_GENERATION", {"kind": "FILE", "identity": dc_src, "symbol": "dataclasses._create_fn", "basis": aref("policies", "§T1")}, ["T1", "T3"],
           [{"declaration_id": "SITE-SUBJECT-CAPABILITY", "kind": "FILE_SITE", "identity": proj_ref("scripts/phase2_runtime/route_b_c03/capability.py"), "locator": "@dataclass C03Capability", "basis": aref("policies", "§T1")},
            {"declaration_id": "SITE-SUBJECT-CONTRACTS", "kind": "FILE_SITE", "identity": proj_ref("scripts/phase2_runtime/route_b_c03/contracts.py"), "locator": "@dataclass declarations (22)", "basis": aref("policies", "§T1")},
            {"declaration_id": "SITE-SUBJECT-ISOLATION", "kind": "FILE_SITE", "identity": proj_ref("scripts/phase2_runtime/route_b_c03/isolation.py"), "locator": "@dataclass ClassificationDetermination", "basis": aref("policies", "§T1")},
            {"declaration_id": "SITE-SUBJECT-FAILURES", "kind": "FILE_SITE", "identity": proj_ref("scripts/phase2_runtime/route_b_c03/failures.py"), "locator": "@dataclass RetryDetermination, ControlDetermination", "basis": aref("policies", "§T1")},
            {"declaration_id": "SITE-SUBJECT-PROVIDER-PORT", "kind": "FILE_SITE", "identity": proj_ref("scripts/phase2_runtime/route_b_c03/provider_port.py"), "locator": "@dataclass ProviderPortResult", "basis": aref("policies", "§T1")}],
           ["the audit hook is not a tamper-proof sandbox"]),
    ], key=lambda o: cp_key(o["operation_id"]))

    gen_auth = aref("authority", "$.Decisions[Id=AR-B-008-KEEP-OPEN]")
    manifest = {
        "manifest_identity": {
            "manifest_id": "DSP004-PYTHON-RUNTIME-DEPENDENCY-MANIFEST", "manifest_version": "REV4", "encoding_version": "WP008-RDM-CANON-2",
            "package": aref("package", "whole document; Python version superseded by P1-PYVER"), "preparation_plan": aref("plan", "whole document"),
            "design_adoption": aref("adoption", "whole record"), "typed_contract": aref("contract", "whole document (accepted REV40; P6-INPUT-PATH, P6-ENTRY-ID, P6-VENV-ROOT apply)"),
            "array_registry": aref("registry", "whole document (accepted REV40)"), "input_binding": input_binding, "harness": harness,
            "environment_record": aref("env", "$.Phase1Environment"), "subject_catalog": aref("input", "$.subject_identities"),
            "fixture_catalog": aref("input", "$.scenarios[*].fixture"), "generation_authority": gen_auth},
        "root_bindings": roots,
        "runtime_identity": {
            "implementation_record": "CPython", "version_record": closure["Python"], "architecture_record": "64 bit (AMD64)",
            "identity_basis": aref("preflight", "$.Run.Python"), "environment_acceptance": aref("env", "$.Decisions[Id=P1-ADMIT]"),
            "validation_launcher": python_exe, "base_executable_identity": python_exe, "configuration": "NOT_APPLICABLE",
            "core_libraries": sorted([rt_ref("python312.dll"), rt_ref("python3.dll"), rt_ref("vcruntime140.dll")], key=lambda f: (cp_key(f["root_id"]), cp_key(f["relative_path"]))),
            "declared_startup_sequence": steps, "startup_contract": aref("policies", "§S1"),
            "startup_prerequisite_evidence": sorted_refs([aref("preflight", "$.Run"), aref("env", "$.Phase1Environment")]),
            "limitations": sorted(["configuration has no file; recorded NOT_APPLICABLE (§D1 item 2)",
                                   "launcher and supervisor are outside the four roots (§R3)"], key=cp_key)},
        "import_contract": {"lookup_order": lookups, "modules": modules, "denied_modules": sorted(DENIED_MODULES, key=cp_key),
                            "socket_guard_origin": {"kind": "FILE", "identity": harness, "symbol": "make_guard", "basis": aref("policies", "§T1")},
                            "origin_policy": aref("policies", "§O1")},
        "trusted_operation_contract": {"operations": ops, "default_denied": True, "policy": aref("policies", "§T1")},
        "input_contract": {"binding": input_binding, "admission": aref("p4accept", "$.Accepted"), "subjects": subjects, "fixtures": fixtures,
                           "scenarios": scenarios, "observation_dispositions": sorted_refs([aref("p25", "$.Decisions[Id=P5-LIMITED]"), aref("input", "$.completeness_summary_rev3")])},
        "entries": [{k: e[k] for k in order15} for e in entries],
        "excluded_sets": {"denied_modules": sorted(DENIED_MODULES, key=cp_key), "denied_capabilities": sorted(DENIED_CAPS, key=cp_key),
                          "rules": sorted([{"kind": "CATEGORY", "category": c, "basis": aref("policies", "§X1 %s" % c)} for c in EXCLUSION_CATEGORIES], key=lambda r: (cp_key(r["kind"]), cp_key(r["category"]))),
                          "policy": aref("policies", "§X1")},
        "closure_evidence": {
            "static_source_resolver": {"kind": "FILE", "identity": harness, "symbol": "scan", "basis": aref("policies", "§T1")},
            "pe_resolver": {"kind": "INTERPRETER", "identity": sys_ref("ntdll.dll"), "symbol": "loaded-module list observed by the supervisor", "basis": aref("preflight", "$.Run.NativeModules")},
            "os_resolver": {"kind": "INTERPRETER", "identity": sys_ref("ntdll.dll"), "symbol": "Windows loader", "basis": aref("policies", "§O1")},
            "origin_policy": aref("policies", "§O1"),
            "resolution_evidence": sorted_refs([aref("closure", "$.Modules"), aref("closure", "$.NativeModules"), aref("preflight", "$.Run")]),
            "entry_classification": sorted([{"entry_id": e["entry_id"], "basis": aref("policies", "§C1 %s" % e["category"])} for e in entries], key=lambda c: cp_key(c["entry_id"])),
            "unresolved_count": unresolved, "duplicate_count": dup,
            "limitations": sorted(["per-module import phase not observed; stdlib read_phase is the permitted window (§C1)",
                                   "mapping.py is hashed and parsed but not imported (§C1)",
                                   "typing.io and typing.re are pseudo-modules of Lib/typing.py (§C1)"], key=cp_key)},
        "aggregate_identity": {"entry_count": len(entries), "byte_total": sum(e["byte_length"] for e in entries),
                               "category_counts": sorted([{"category": c, "count": counts[c]} for c in CATEGORIES], key=lambda x: cp_key(x["category"])),
                               "entry_aggregate_sha256": agg_sha},
        "governance": {"generation_authority": gen_auth, "materializer_role": "RECORDER_ONLY",
                       "independent_review_policy": aref("policies", "§V1"), "owner_decision_policy": aref("policies", "§V1"),
                       "independent_review_required": True, "owner_acceptance_required": True, "execution_grant_in_manifest": False},
    }
    text = enc(manifest) + "\n"
    data = text.encode("utf-8")
    summary = {"entries": len(entries), "category_counts": counts, "byte_total": manifest["aggregate_identity"]["byte_total"],
               "entry_aggregate_sha256": agg_sha, "modules": len(modules), "denied_overlap": denied_overlap,
               "unresolved": unresolved, "duplicates": dup, "manifest_bytes": len(data), "manifest_sha256": sha(data),
               "read_scopes": {k: len(v) for k, v in scopes.items()}}
    print(json.dumps(summary, indent=1))
    if denied_overlap or unresolved or dup:
        print("BLOCKED: denied overlap, unresolved or duplicate entries")
        return 2
    if write:
        with open(OUT, "wb") as f:
            f.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
