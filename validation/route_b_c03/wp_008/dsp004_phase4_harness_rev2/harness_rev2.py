"""DSP-004 phase-4 harness REV2 (draft under owner decision P4-DRAFT; not accepted).

REV2 answers the review of REV1. It runs every stimulus variant of the bound input candidate REV4 once against the
bound subject package, records the native result and compares it with the variant's pre-declared rule.

Guarantees, in order:
  1. Interpreter flags must be -I -S -B, else stop.
  2. The input, the 10 subject files and the 15 fixtures are read once; their SHA-256 must equal the values fixed
     here. Those same bytes are what is used afterwards (no second read).
  3. Each subject file's syntax tree is scanned: only the standard modules in ALLOWED_IMPORTS and relative imports
     inside the package are permitted, and no call to exec/eval/compile/__import__/open/getattr-by-string helpers.
  4. An audit hook is installed that blocks network, process creation, file writes/removals and dynamic code from
     the moment the subject is imported. It cannot be removed for the rest of the process.
  5. The subject package is built by a private importer from the hashed bytes. No path is added to sys.path, no
     .pyc is read or written, and any other import of the package names is refused.
  6. Dispatch, object types and enum classes come from fixed allow-lists here; input data only supplies values.
     Enum members are looked up by name (EnumClass[member]).
  7. Comparison checks native types by identity (exact bound classes, exact enum classes, exact str) before
     comparing values.
It writes nothing and opens no network connection. Output: one JSON object on stdout.
Exit codes: 0 all variants PASS; 4 at least one variant FAIL; 2 identity or environment stop; 3 harness error;
64 usage.
"""
import ast
import dataclasses
import enum
import hashlib
import importlib.abc
import importlib.util
import json
import os
import sys

INPUT_REL = "validation/route_b_c03/wp_008/DSP_004_INPUT_CANDIDATE_REV4.json"
INPUT_SHA256 = "685BBCBF13BF96746E6DE4201C1FCE72B667CD6A07D0CE0902D9EF9A6C4235C1"
# module name -> (repository path, SHA-256, is package)
SUBJECT = {
    "phase2_runtime": ("scripts/phase2_runtime/__init__.py", "49B8B1BD319B6424323AD0EDC04B3969D71196CD8D69E12C16D5442B17340844", True),
    "phase2_runtime.route_b_c03": ("scripts/phase2_runtime/route_b_c03/__init__.py", "F669613D65267EC5D4D42CB79008EB510307A99B20E40EE13E9E1E0E404A504D", True),
    "phase2_runtime.route_b_c03.contracts": ("scripts/phase2_runtime/route_b_c03/contracts.py", "7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4", False),
    "phase2_runtime.route_b_c03.identity_gate": ("scripts/phase2_runtime/route_b_c03/identity_gate.py", "9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445", False),
    "phase2_runtime.route_b_c03.mapping": ("scripts/phase2_runtime/route_b_c03/mapping.py", "320F7E8576C1C4E81B4E78E6058000E4D720173948BE736AD846B8CAD664EC66", False),
    "phase2_runtime.route_b_c03.isolation": ("scripts/phase2_runtime/route_b_c03/isolation.py", "9BC554294D5945188A153F0A5CBEDFAB4E483C95B133683B7517ECC334D4205B", False),
    "phase2_runtime.route_b_c03.failures": ("scripts/phase2_runtime/route_b_c03/failures.py", "6F30D996119F61A19B20208FC44C8AF1FB96ADFE09ADE3538675B9D3F2933734", False),
    "phase2_runtime.route_b_c03.audit": ("scripts/phase2_runtime/route_b_c03/audit.py", "A704BDB22C55C92D0909FA0D6A668D8C149724B2A7627938C301758F1D09F561", False),
    "phase2_runtime.route_b_c03.provider_port": ("scripts/phase2_runtime/route_b_c03/provider_port.py", "66E4DA862BBBD50380B17686DB6BC2AB6D5D3B861AB53FCDDE1B608F86DEA381", False),
    "phase2_runtime.route_b_c03.capability": ("scripts/phase2_runtime/route_b_c03/capability.py", "028EE9DDD7A2C06840A6F344A4C4CC716EFF95073BE39CA6E57FB7FDBBFA6DD5", False),
}
PKG = "phase2_runtime.route_b_c03"
ALLOWED_IMPORTS = {"__future__", "dataclasses", "enum", "re", "typing", "collections.abc", "hashlib", "json"}
FORBIDDEN_CALLS = {"exec", "eval", "compile", "__import__", "open", "input", "breakpoint", "globals", "vars", "setattr", "delattr"}
# adapter id -> (module, attribute, kind)
ADAPTERS = {
    "ADP-EVALUATE-IDENTITY": ("identity_gate", "evaluate_identity_gate", "call"),
    "ADP-CONSTRUCT-EXPECTED": ("contracts", "ExpectedIdentityReference", "call"),
    "ADP-ASSERT-REFERENCE-ONLY": ("isolation", "assert_reference_only", "call"),
    "ADP-CONSTRUCT-IDEMPOTENCY": ("contracts", "IdempotencyKeyReference", "call"),
    "ADP-EVALUATE-RETRY": ("failures", "evaluate_retry", "call"),
    "ADP-CONSTRUCT-TIMEOUT": ("contracts", "TimeoutPolicyReference", "call"),
    "ADP-PROTECTED-STATE": ("failures", "protected_state", "call"),
    "ADP-EVALUATE-RELEASE": ("failures", "evaluate_release", "call"),
    "ADP-CONSTRUCT-ROLLBACK": ("contracts", "RollbackReference", "call"),
    "ADP-CONSTRUCT-AUDIT-INTEGRITY": ("contracts", "AuditIntegrityReference", "call"),
    "ADP-BUILD-AUDIT-CANDIDATE": ("audit", "build_audit_candidate", "call"),
    "ADP-NULL-PROVIDER": ("provider_port", "NullProviderPort.submit_reference", "method"),
    "ADP-ASSERT-WRITE-SET": ("isolation", "assert_permitted_write_set", "call"),
    "ADP-CONSTRUCT-CANDIDATE": ("contracts", "CandidateRecord", "call"),
}
OBJECT_TYPES = {"CapabilityConfigurationReference", "ExpectedIdentityReference", "GovernedInputEnvelopeReference",
                "TierBAuthorityPacketReference", "RetryPolicyReference", "IdempotencyKeyReference",
                "TimeoutPolicyReference", "RollbackReference", "AuditIntegrityReference", "CandidateRecord"}
ENUMS = {"CapabilityState": "contracts", "InvocationState": "contracts", "PacketState": "contracts",
         "RevocationState": "contracts", "CandidateClass": "contracts", "ControlState": "contracts",
         "TamperState": "contracts", "TransformationType": "contracts", "FailureCode": "failures"}
# return type -> (module, class, state enum module, state enum class)
RETURN_TYPES = {"GateDecision": ("contracts", "GateDecision", "contracts", "InvocationState"),
                "RetryDetermination": ("failures", "RetryDetermination", "failures", "ControlState")}
LEGACY_RETURN_TYPE = {"ADP-EVALUATE-IDENTITY": "GateDecision", "ADP-EVALUATE-RETRY": "RetryDetermination"}
CONSTRUCT_TYPES = {"IdempotencyKeyReference": ("contracts", None), "TimeoutPolicyReference": ("contracts", None),
                   "RollbackReference": ("contracts", None), "AuditIntegrityReference": ("contracts", None),
                   "CandidateRecord": ("contracts", None), "AuditRecordCandidate": ("contracts", None),
                   "ProviderPortResult": ("provider_port", None)}
CONTEXT = {"project_reference": "SYNTHETIC-PROJECT-001", "session_reference": "SYNTHETIC-SESSION-001",
           "provider_reference": "SYNTHETIC-PROVIDER-001"}
BLOCKED_EVENTS = ("socket.", "subprocess.", "os.system", "os.exec", "os.spawn", "os.posix_spawn", "os.fork",
                  "os.remove", "os.unlink", "os.rename", "os.rmdir", "os.mkdir", "os.chmod", "shutil.",
                  "ctypes.", "urllib.", "http.", "ftplib.", "smtplib.", "winreg.", "_winapi.CreateProcess")


class Stop(Exception):
    pass


def sha(b):
    return hashlib.sha256(b).hexdigest().upper()


def read_bound(root, rel, want):
    with open(os.path.join(root, rel), "rb") as f:
        b = f.read()
    if sha(b) != want:
        raise Stop("SHA_MISMATCH " + rel)
    return b


class _Hook:
    armed = False
    denied = []


def _audit(event, args):
    if not _Hook.armed:
        return
    bad = event.startswith(BLOCKED_EVENTS)
    if event == "open" and len(args) > 1 and isinstance(args[1], str) and any(c in args[1] for c in "wax+"):
        bad = True
    if bad:
        _Hook.denied.append(event)
        raise RuntimeError("DSP004 HARNESS GUARD: " + event)


class BytesImporter(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def __init__(self, root, sources):
        self.root = root
        self.sources = sources  # module name -> bytes

    def find_spec(self, name, path, target=None):
        if name == "phase2_runtime" or name.startswith("phase2_runtime."):
            if name not in self.sources:
                raise ImportError("DSP004 HARNESS: unbound module " + name)
            rel, _, is_pkg = SUBJECT[name]
            spec = importlib.util.spec_from_loader(name, self, origin=os.path.join(self.root, rel), is_package=is_pkg)
            if is_pkg:
                spec.submodule_search_locations = []
            return spec
        return None

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        name = module.__name__
        rel = SUBJECT[name][0]
        module.__file__ = os.path.join(self.root, rel)
        code = compile(self.sources[name], module.__file__, "exec", dont_inherit=True)
        exec(code, module.__dict__)


def scan(name, src):
    tree = ast.parse(src, filename=name)
    found = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                if a.name not in ALLOWED_IMPORTS:
                    found.append("IMPORT " + a.name)
        elif isinstance(node, ast.ImportFrom):
            if node.level == 0 and node.module not in ALLOWED_IMPORTS:
                found.append("IMPORT_FROM " + str(node.module))
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in FORBIDDEN_CALLS:
            found.append("CALL " + node.func.id)
        elif isinstance(node, ast.Attribute) and node.attr in ("system", "popen", "Popen", "urlopen", "connect"):
            found.append("ATTR " + node.attr)
    return found


def prepare(root):
    if not (sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.flags.dont_write_bytecode == 1):
        raise Stop("FLAGS_NOT_I_S_B")
    inp_bytes = read_bound(root, INPUT_REL, INPUT_SHA256)
    inp = json.loads(inp_bytes.decode("utf-8"))
    table = {rel: s for rel, s, _ in SUBJECT.values()}
    if inp.get("subject_identities") != table:
        raise Stop("INPUT_SUBJECT_TABLE_DIFFERS")
    sources = {name: read_bound(root, rel, s) for name, (rel, s, _) in SUBJECT.items()}
    fixtures = {rel: read_bound(root, rel, s) for rel, s in inp["fixture_identities"].items()}
    for aid, entry in inp["adapter_catalog"].items():
        if aid not in ADAPTERS:
            raise Stop("UNKNOWN_ADAPTER " + aid)
        mod, attr, _ = ADAPTERS[aid]
        if entry.get("subject_path") != "scripts/phase2_runtime/route_b_c03/" + mod + ".py" or entry.get("callable") != attr:
            raise Stop("ADAPTER_CATALOG_DIFFERS " + aid)
    for oid, entry in inp["synthetic_object_catalog"].items():
        if entry["type"] not in OBJECT_TYPES:
            raise Stop("OBJECT_TYPE_NOT_ALLOWED " + oid)
    scan_result = {name: scan(name, src) for name, src in sources.items()}
    if any(scan_result.values()):
        raise Stop("SUBJECT_SCAN " + json.dumps({k: v for k, v in scan_result.items() if v}))
    return inp, sources, fixtures


def load_subject(root, sources):
    for name in list(sys.modules):
        if name == "phase2_runtime" or name.startswith("phase2_runtime."):
            raise Stop("PACKAGE_ALREADY_IMPORTED")
    sys.meta_path.insert(0, BytesImporter(root, sources))
    sys.addaudithook(_audit)
    _Hook.armed = True
    mods = {}
    for short in ("contracts", "identity_gate", "isolation", "failures", "audit", "provider_port"):
        mods[short] = importlib.import_module(PKG + "." + short)
    return mods


def convert(mods, value, catalog, overrides, used):
    if value is None or type(value) in (bool, int, str):
        return value
    if isinstance(value, list):
        return [convert(mods, v, catalog, overrides, used) for v in value]
    if isinstance(value, dict):
        if set(value) == {"object_ref"}:
            return build_object(mods, value["object_ref"], catalog, overrides, used)
        if set(value) == {"enum_class", "member"}:
            cls = getattr(mods[ENUMS[value["enum_class"]]], value["enum_class"])
            return cls[value["member"]]
        if set(value) == {"tuple"}:
            return tuple(convert(mods, v, catalog, overrides, used) for v in value["tuple"])
        return {k: convert(mods, v, catalog, overrides, used) for k, v in value.items()}
    raise ValueError("UNSUPPORTED_INPUT_VALUE")


def build_object(mods, ref, catalog, overrides, used):
    entry = catalog[ref]
    args = dict(entry["arguments"])
    prefix = "/" + ref + "/arguments/"
    for key, val in overrides.items():
        if key.startswith(prefix):
            field = key[len(prefix):]
            if field not in args:
                raise ValueError("OVERRIDE_UNKNOWN_FIELD " + key)
            args[field] = val
            used.add(key)
    cls = getattr(mods["contracts"], entry["type"])
    return cls(**{k: convert(mods, v, catalog, overrides, used) for k, v in args.items()})


def encode(v):
    if v is None or type(v) in (bool, int, str):
        return v
    if isinstance(v, enum.Enum):
        return {"enum_class": type(v).__name__, "member": v.name, "value": v.value}
    if isinstance(v, tuple):
        return {"tuple": [encode(x) for x in v]}
    if isinstance(v, list):
        return [encode(x) for x in v]
    if isinstance(v, dict):
        return {k: encode(x) for k, x in v.items()}
    if dataclasses.is_dataclass(v):
        return {"type": type(v).__name__, "module": type(v).__module__,
                "fields": {f.name: encode(getattr(v, f.name)) for f in dataclasses.fields(v)}}
    return {"unencodable_type": type(v).__name__, "module": type(v).__module__}


def invoke(mods, variant, catalog):
    mod, attr, kind = ADAPTERS[variant["adapter_id"]]
    overrides = variant.get("object_overrides") or {}
    used = set()
    args = {k: convert(mods, v, catalog, overrides, used) for k, v in variant["arguments"].items()}
    if set(overrides) - used:
        raise ValueError("UNUSED_OVERRIDE " + ",".join(sorted(set(overrides) - used)))
    try:
        if kind == "method":
            cls_name, meth = attr.split(".")
            native = getattr(getattr(mods[mod], cls_name)(), meth)(**args)
        else:
            native = getattr(mods[mod], attr)(**args)
    except Exception as e:
        return {"kind": "exception", "type": type(e).__name__, "module": type(e).__module__, "message": str(e)}, None, e, args
    return {"kind": "return", "value": encode(native)}, native, None, args


def exact_enum(mods, value, module, cls_name, member_or_value):
    cls = getattr(mods[module], cls_name)
    if type(value) is not cls:
        return False
    if isinstance(member_or_value, dict):
        return member_or_value["enum_class"] == cls_name and value.name == member_or_value["member"]
    return value.value == member_or_value


def compare(mods, rule, variant, native, exc, args):
    req = rule["raw_requirement"]
    if "exception_type" in req:
        if exc is None or type(exc).__name__ != req["exception_type"]:
            return False
        bound = {"IsolationViolation": ("isolation", "IsolationViolation"), "ValueError": None}
        want_cls = bound.get(req["exception_type"], "UNKNOWN")
        if want_cls == "UNKNOWN":
            return False
        if want_cls is not None and type(exc) is not getattr(mods[want_cls[0]], want_cls[1]):
            return False
        if want_cls is None and type(exc) is not ValueError:
            return False
        msg = str(exc)
        return msg == req["message"] if "message" in req else msg.startswith(req["message_prefix"])
    if exc is not None:
        return False
    rtype = req.get("type") or LEGACY_RETURN_TYPE.get(variant["adapter_id"])
    if rtype == "ControlState":
        return exact_enum(mods, native, "contracts", "ControlState", {"enum_class": "ControlState", "member": req["member"]})
    if rtype in RETURN_TYPES:
        mod, cls, emod, ecls = RETURN_TYPES[rtype]
        if type(native) is not getattr(mods[mod], cls):
            return False
        for key, want in req.items():
            if key == "type":
                continue
            got = getattr(native, key, None)
            if key == "state":
                if not exact_enum(mods, got, emod, ecls, want):
                    return False
            elif key == "permitted_write_namespaces":
                if type(got) is not tuple or got != tuple(want) or any(type(x) is not str for x in got):
                    return False
            elif type(want) is str:
                if type(got) is not str or got != want:
                    return False
            elif type(got) is not type(want) or got != want:
                return False
        return True
    if rtype in CONSTRUCT_TYPES:
        mod = CONSTRUCT_TYPES[rtype][0]
        if type(native) is not getattr(mods[mod], rtype):
            return False
        if req.get("fields_equal_converted_arguments"):
            return all(hasattr(native, k) and encode(getattr(native, k)) == encode(v) for k, v in args.items())
        for key, want in req.items():
            if key == "type":
                continue
            got = getattr(native, key, None)
            if type(got) is not type(want) or got != want:
                return False
        return True
    return False


def capture_six_side(context, provider):
    """Separate capture function: reads the context object and the provider instance after the run."""
    return {"SRC004-A-PROJECT": getattr(context, "project_reference"),
            "SRC004-A-SESSION": getattr(context, "session_reference"),
            "SRC004-A-PROVIDER": getattr(context, "provider_reference"),
            "ProviderPortInstanceStatus": getattr(provider, "status")}


def run(root):
    inp, sources, fixtures = prepare(root)
    mods = load_subject(root, sources)
    catalog = inp["synthetic_object_catalog"]
    rules = inp["comparison_rule_catalog"]
    out = {"Kind": "DSP004_PHASE4_HARNESS_REV2_OBSERVATION", "Python": sys.version,
           "Flags": {"isolated": sys.flags.isolated, "no_site": sys.flags.no_site, "dont_write_bytecode": sys.flags.dont_write_bytecode},
           "InputSha256": INPUT_SHA256, "SubjectScan": "CLEAN", "Scenarios": []}
    totals = {"variants": 0, "pass": 0, "fail": 0, "conformant_full": 0, "conformant_partial_limited": 0, "not_mapped": 0}
    for sc in inp["scenarios"]:
        fixture = json.loads(fixtures[sc["fixture"]["path"]].decode("utf-8"))
        rows = []
        for v in sc["stimulus_variants"]:
            rule = rules[v["comparison_rule_id"]]
            obs, native, exc, args = invoke(mods, v, catalog)
            ok = compare(mods, rule, v, native, exc, args)
            mapping = rule.get("fixture_mapping")
            conformant = None
            if mapping:
                conformant = bool(ok and mapping.get("expected_state") == fixture["expected_state"]
                                  and mapping.get("expected_reason_class") == fixture["expected_reason_class"]
                                  and ("expected_permitted_write_set" not in mapping
                                       or mapping["expected_permitted_write_set"] == fixture["expected_permitted_write_set"]))
                key = "conformant_full" if sc.get("coverage_class_rev3") == "FULL" else "conformant_partial_limited"
                totals[key] += 1 if conformant else 0
            else:
                totals["not_mapped"] += 1
            totals["variants"] += 1
            totals["pass" if ok else "fail"] += 1
            rows.append({"StimulusBindingId": v["stimulus_binding_id"], "AdapterId": v["adapter_id"], "RuleId": v["comparison_rule_id"],
                         "Observation": obs, "RuleVerdict": "PASS" if ok else "FAIL", "FixtureConformant": conformant,
                         "WriteSetCompared": bool(mapping and "expected_permitted_write_set" in mapping)})
        out["Scenarios"].append({"ScenarioId": sc["scenario_id"], "CoverageClass": sc.get("coverage_class_rev3"),
                                 "FixtureExpected": {"state": fixture["expected_state"], "reason_class": fixture["expected_reason_class"]},
                                 "Variants": rows})
    context = type("SyntheticCallContext", (), dict(CONTEXT))()
    provider = getattr(mods["provider_port"], "NullProviderPort")()
    actual = capture_six_side(context, provider)
    expected = {"SRC004-A-PROJECT": "SYNTHETIC-PROJECT-001", "SRC004-A-SESSION": "SYNTHETIC-SESSION-001", "SRC004-A-PROVIDER": "SYNTHETIC-PROVIDER-001"}
    exp_in = inp["six_side_binding_rev3"]["expected"]
    out["SixSide"] = {"ExpectedFromInput": {k: exp_in[k] for k in ("SRC004-E-PROJECT", "SRC004-E-SESSION", "SRC004-E-PROVIDER")},
                      "ActualCaptured": actual,
                      "Consistent": all(actual[k] == expected[k] for k in expected)
                      and [exp_in["SRC004-E-PROJECT"], exp_in["SRC004-E-SESSION"], exp_in["SRC004-E-PROVIDER"]] == [expected[k] for k in ("SRC004-A-PROJECT", "SRC004-A-SESSION", "SRC004-A-PROVIDER")],
                      "Limitation": inp["six_side_binding_rev3"]["limitation"]}
    out["GuardDenied"] = list(_Hook.denied)
    out["Totals"] = totals
    return out


def emit(obj):
    sys.stdout.write(json.dumps(obj, ensure_ascii=True, sort_keys=True) + "\n")
    sys.stdout.flush()


def main():
    if len(sys.argv) != 2:
        emit({"Kind": "DSP004_PHASE4_HARNESS_REV2_OBSERVATION", "Stop": "USAGE"})
        return 64
    try:
        out = run(os.path.abspath(sys.argv[1]))
    except Stop as e:
        emit({"Kind": "DSP004_PHASE4_HARNESS_REV2_OBSERVATION", "Stop": str(e)})
        return 2
    except FileNotFoundError as e:
        emit({"Kind": "DSP004_PHASE4_HARNESS_REV2_OBSERVATION", "Stop": "BOUND_FILE_MISSING " + str(e.filename)})
        return 2
    except Exception as e:
        emit({"Kind": "DSP004_PHASE4_HARNESS_REV2_OBSERVATION", "Stop": "HARNESS_ERROR", "Type": type(e).__name__, "Message": str(e)})
        return 3
    emit(out)
    return 0 if out["Totals"]["fail"] == 0 else 4


if __name__ == "__main__":
    sys.exit(main())
