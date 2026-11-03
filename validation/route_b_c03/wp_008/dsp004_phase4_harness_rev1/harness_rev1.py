"""DSP-004 phase-4 harness REV1 (draft under owner decision P4-DRAFT; not reviewed, not accepted).

Runs every stimulus variant of the bound input candidate REV3 against the bound subject package once, records the
native result, and compares it with the variant's pre-declared comparison rule. Only standard library. It writes
nothing to disk, opens no network connection, and reads only: the input candidate, the 10 subject files, the 15
fixture files. Every one of those is checked against the SHA-256 fixed in this file before any subject import.

Dispatch is a fixed table in this file; the input's adapter catalogue is only checked against it, never used to
choose a module or function. Rules are taken from the input as written; nothing is normalised or relabelled.

Usage:  python -I -S -B harness_rev1.py <repository root>      -> one JSON object on stdout, exit 0
        (exit 2 = identity stop before any subject import; exit 3 = unexpected harness error)
"""
import dataclasses
import enum
import hashlib
import importlib
import json
import os
import sys

INPUT_REL = "validation/route_b_c03/wp_008/DSP_004_INPUT_CANDIDATE_REV3.json"
INPUT_SHA256 = "16CBAFDF8D7E12682321DA3E905A5985F042E37B5E440EE6BE9A6217FDE36D08"
SUBJECT_SHA256 = {
    "scripts/phase2_runtime/__init__.py": "49B8B1BD319B6424323AD0EDC04B3969D71196CD8D69E12C16D5442B17340844",
    "scripts/phase2_runtime/route_b_c03/__init__.py": "F669613D65267EC5D4D42CB79008EB510307A99B20E40EE13E9E1E0E404A504D",
    "scripts/phase2_runtime/route_b_c03/contracts.py": "7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4",
    "scripts/phase2_runtime/route_b_c03/identity_gate.py": "9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445",
    "scripts/phase2_runtime/route_b_c03/mapping.py": "320F7E8576C1C4E81B4E78E6058000E4D720173948BE736AD846B8CAD664EC66",
    "scripts/phase2_runtime/route_b_c03/isolation.py": "9BC554294D5945188A153F0A5CBEDFAB4E483C95B133683B7517ECC334D4205B",
    "scripts/phase2_runtime/route_b_c03/failures.py": "6F30D996119F61A19B20208FC44C8AF1FB96ADFE09ADE3538675B9D3F2933734",
    "scripts/phase2_runtime/route_b_c03/audit.py": "A704BDB22C55C92D0909FA0D6A668D8C149724B2A7627938C301758F1D09F561",
    "scripts/phase2_runtime/route_b_c03/provider_port.py": "66E4DA862BBBD50380B17686DB6BC2AB6D5D3B861AB53FCDDE1B608F86DEA381",
    "scripts/phase2_runtime/route_b_c03/capability.py": "028EE9DDD7A2C06840A6F344A4C4CC716EFF95073BE39CA6E57FB7FDBBFA6DD5",
}
PKG = "phase2_runtime.route_b_c03"
# adapter id -> (module, attribute, kind); kind: call | construct | method
ADAPTERS = {
    "ADP-EVALUATE-IDENTITY": ("identity_gate", "evaluate_identity_gate", "call"),
    "ADP-CONSTRUCT-EXPECTED": ("contracts", "ExpectedIdentityReference", "construct"),
    "ADP-ASSERT-REFERENCE-ONLY": ("isolation", "assert_reference_only", "call"),
    "ADP-CONSTRUCT-IDEMPOTENCY": ("contracts", "IdempotencyKeyReference", "construct"),
    "ADP-EVALUATE-RETRY": ("failures", "evaluate_retry", "call"),
    "ADP-CONSTRUCT-TIMEOUT": ("contracts", "TimeoutPolicyReference", "construct"),
    "ADP-PROTECTED-STATE": ("failures", "protected_state", "call"),
    "ADP-EVALUATE-RELEASE": ("failures", "evaluate_release", "call"),
    "ADP-CONSTRUCT-ROLLBACK": ("contracts", "RollbackReference", "construct"),
    "ADP-CONSTRUCT-AUDIT-INTEGRITY": ("contracts", "AuditIntegrityReference", "construct"),
    "ADP-BUILD-AUDIT-CANDIDATE": ("audit", "build_audit_candidate", "call"),
    "ADP-NULL-PROVIDER": ("provider_port", "NullProviderPort.submit_reference", "method"),
    "ADP-ASSERT-WRITE-SET": ("isolation", "assert_permitted_write_set", "call"),
    "ADP-CONSTRUCT-CANDIDATE": ("contracts", "CandidateRecord", "construct"),
}
ENUMS = {"CapabilityState": "contracts", "InvocationState": "contracts", "PacketState": "contracts",
         "RevocationState": "contracts", "CandidateClass": "contracts", "ControlState": "contracts",
         "TamperState": "contracts", "TransformationType": "contracts", "FailureCode": "failures"}
# rules without an explicit "type" name the native return type through the adapter
LEGACY_RETURN_TYPE = {"ADP-EVALUATE-IDENTITY": "GateDecision", "ADP-EVALUATE-RETRY": "RetryDetermination"}
SIX_SIDE_CONTEXT = {"SRC004-A-PROJECT": "SYNTHETIC-PROJECT-001", "SRC004-A-SESSION": "SYNTHETIC-SESSION-001",
                    "SRC004-A-PROVIDER": "SYNTHETIC-PROVIDER-001"}


class IdentityStop(Exception):
    pass


def sha_file(path):
    with open(path, "rb") as f:
        b = f.read()
    return hashlib.sha256(b).hexdigest().upper(), b


def check_identities(root):
    got, data = sha_file(os.path.join(root, INPUT_REL))
    if got != INPUT_SHA256:
        raise IdentityStop("INPUT_SHA_MISMATCH " + got)
    inp = json.loads(data.decode("utf-8"))
    if inp.get("subject_identities") != SUBJECT_SHA256:
        raise IdentityStop("INPUT_SUBJECT_TABLE_DIFFERS_FROM_HARNESS")
    for rel, want in SUBJECT_SHA256.items():
        if sha_file(os.path.join(root, rel))[0] != want:
            raise IdentityStop("SUBJECT_SHA_MISMATCH " + rel)
    for rel, want in inp["fixture_identities"].items():
        if sha_file(os.path.join(root, rel))[0] != want:
            raise IdentityStop("FIXTURE_SHA_MISMATCH " + rel)
    for aid, entry in inp["adapter_catalog"].items():
        if aid not in ADAPTERS:
            raise IdentityStop("UNKNOWN_ADAPTER " + aid)
        mod, attr, _ = ADAPTERS[aid]
        if entry.get("subject_path") != "scripts/phase2_runtime/route_b_c03/" + mod + ".py" or entry.get("callable") != attr:
            raise IdentityStop("ADAPTER_CATALOG_DIFFERS " + aid)
    return inp


def load_subject(root):
    scripts = os.path.join(root, "scripts")
    sys.path.insert(0, scripts)
    mods = {}
    for name in ("contracts", "identity_gate", "isolation", "failures", "audit", "provider_port"):
        m = importlib.import_module(PKG + "." + name)
        real = os.path.realpath(m.__file__)
        rel = os.path.relpath(real, os.path.realpath(root)).replace(os.sep, "/")
        if rel not in SUBJECT_SHA256:
            raise IdentityStop("MODULE_LOADED_FROM_UNBOUND_PATH " + name)
        mods[name] = m
    for name, m in list(sys.modules.items()):
        if name == "phase2_runtime" or name.startswith("phase2_runtime."):
            real = os.path.realpath(getattr(m, "__file__", "") or "")
            rel = os.path.relpath(real, os.path.realpath(root)).replace(os.sep, "/")
            if rel not in SUBJECT_SHA256:
                raise IdentityStop("PACKAGE_MODULE_FROM_UNBOUND_PATH " + name)
    return mods


def resolve(mods, dotted):
    mod, attr = dotted
    obj = mods[mod]
    for part in attr.split("."):
        obj = getattr(obj, part)
    return obj


def convert(mods, value, catalog, overrides):
    if value is None or isinstance(value, (bool, int, str)):
        return value
    if isinstance(value, list):
        return [convert(mods, v, catalog, overrides) for v in value]
    if isinstance(value, dict):
        if set(value) == {"object_ref"}:
            return build_object(mods, value["object_ref"], catalog, overrides)
        if set(value) == {"enum_class", "member"}:
            return getattr(getattr(mods[ENUMS[value["enum_class"]]], value["enum_class"]), value["member"])
        if set(value) == {"tuple"}:
            return tuple(convert(mods, v, catalog, overrides) for v in value["tuple"])
        return {k: convert(mods, v, catalog, overrides) for k, v in value.items()}
    raise ValueError("UNSUPPORTED_INPUT_VALUE")


def build_object(mods, ref, catalog, overrides):
    entry = catalog[ref]
    args = dict(entry["arguments"])
    prefix = "/" + ref + "/arguments/"
    for key, val in overrides.items():
        if key.startswith(prefix):
            field = key[len(prefix):]
            if field not in args:
                raise ValueError("OVERRIDE_UNKNOWN_FIELD " + key)
            args[field] = val
    cls = getattr(mods["contracts"], entry["type"])
    return cls(**{k: convert(mods, v, catalog, overrides) for k, v in args.items()})


def encode(v):
    if v is None or isinstance(v, (bool, int)) and not isinstance(v, enum.Enum):
        return v
    if isinstance(v, enum.Enum):
        return {"enum_class": type(v).__name__, "member": v.name, "value": v.value}
    if isinstance(v, str):
        return v
    if isinstance(v, tuple):
        return {"tuple": [encode(x) for x in v]}
    if isinstance(v, list):
        return [encode(x) for x in v]
    if isinstance(v, dict):
        return {k: encode(x) for k, x in v.items()}
    if dataclasses.is_dataclass(v):
        return {"type": type(v).__name__, "module": type(v).__module__,
                "fields": {f.name: encode(getattr(v, f.name)) for f in dataclasses.fields(v)}}
    return {"unencodable_type": type(v).__name__}


def invoke(mods, variant, catalog):
    mod, attr, kind = ADAPTERS[variant["adapter_id"]]
    overrides = variant.get("object_overrides") or {}
    try:
        args = {k: convert(mods, v, catalog, overrides) for k, v in variant["arguments"].items()}
    except Exception as e:  # input conversion failure is a harness/input fact, recorded as such
        return {"kind": "input_conversion_error", "type": type(e).__name__, "message": str(e)}, None
    try:
        if kind == "method":
            cls_name, meth = attr.split(".")
            result = getattr(getattr(mods[mod], cls_name)(), meth)(**args)
        else:
            result = getattr(mods[mod], attr)(**args)
    except Exception as e:
        return {"kind": "exception", "type": type(e).__name__, "module": type(e).__module__, "message": str(e)}, args
    return {"kind": "return", "value": encode(result)}, args


def state_matches(obs_state, want):
    if not (isinstance(obs_state, dict) and "member" in obs_state):
        return False
    if isinstance(want, dict):
        return obs_state["enum_class"] == want["enum_class"] and obs_state["member"] == want["member"]
    return obs_state["value"] == want


def compare(rule, variant, obs, args):
    req = rule["raw_requirement"]
    if "exception_type" in req:
        if obs["kind"] != "exception" or obs["type"] != req["exception_type"]:
            return False
        if "message" in req:
            return obs["message"] == req["message"]
        return obs["message"].startswith(req["message_prefix"])
    if obs["kind"] != "return":
        return False
    val = obs["value"]
    rtype = req.get("type") or LEGACY_RETURN_TYPE.get(variant["adapter_id"])
    if rtype == "ControlState":
        return isinstance(val, dict) and val.get("enum_class") == "ControlState" and val.get("member") == req["member"]
    if not (isinstance(val, dict) and val.get("type") == rtype):
        return False
    fields = val["fields"]
    if req.get("fields_equal_converted_arguments"):
        return all(k in fields and fields[k] == encode(v) for k, v in args.items())
    for key, want in req.items():
        if key == "type":
            continue
        if key == "state":
            if not state_matches(fields.get("state"), want):
                return False
        elif key == "permitted_write_namespaces":
            if fields.get(key) != {"tuple": list(want)}:
                return False
        elif fields.get(key) != want:
            return False
    return True


def run(root):
    inp = check_identities(root)
    mods = load_subject(root)
    catalog = inp["synthetic_object_catalog"]
    rules = inp["comparison_rule_catalog"]
    out = {"Kind": "DSP004_PHASE4_HARNESS_REV1_OBSERVATION", "Python": sys.version, "Flags": {
        "isolated": sys.flags.isolated, "no_site": sys.flags.no_site, "dont_write_bytecode": sys.flags.dont_write_bytecode},
        "InputSha256": INPUT_SHA256, "Scenarios": []}
    totals = {"variants": 0, "pass": 0, "fail": 0, "fixture_conformant": 0}
    for sc in inp["scenarios"]:
        with open(os.path.join(root, sc["fixture"]["path"]), "rb") as f:
            fixture = json.loads(f.read().decode("utf-8"))
        rows = []
        for v in sc["stimulus_variants"]:
            rule = rules[v["comparison_rule_id"]]
            obs, args = invoke(mods, v, catalog)
            ok = args is not None and compare(rule, v, obs, args)
            mapping = rule.get("fixture_mapping")
            conformant = None
            if ok and mapping:
                conformant = (mapping.get("expected_state") == fixture["expected_state"]
                              and mapping.get("expected_reason_class") == fixture["expected_reason_class"])
            totals["variants"] += 1
            totals["pass" if ok else "fail"] += 1
            totals["fixture_conformant"] += 1 if conformant else 0
            rows.append({"StimulusBindingId": v["stimulus_binding_id"], "AdapterId": v["adapter_id"],
                         "RuleId": v["comparison_rule_id"], "Observation": obs,
                         "RuleVerdict": "PASS" if ok else "FAIL", "FixtureConformant": conformant})
        out["Scenarios"].append({"ScenarioId": sc["scenario_id"], "CoverageClass": sc.get("coverage_class_rev3"),
                                 "FixtureExpected": {"state": fixture["expected_state"], "reason_class": fixture["expected_reason_class"]},
                                 "Variants": rows})
    provider = getattr(mods["provider_port"], "NullProviderPort")
    out["SixSide"] = {"Expected": {"SRC004-E-PROJECT": "SYNTHETIC-PROJECT-001", "SRC004-E-SESSION": "SYNTHETIC-SESSION-001",
                                   "SRC004-E-PROVIDER": "SYNTHETIC-PROVIDER-001"},
                      "ActualFromHarnessContext": dict(SIX_SIDE_CONTEXT), "ProviderPortStatus": provider.status,
                      "Limitation": "same harness supplies and captures the context; consistency only, not trust separation"}
    out["Totals"] = totals
    return out


def main():
    if len(sys.argv) != 2:
        print(json.dumps({"Kind": "DSP004_PHASE4_HARNESS_REV1_OBSERVATION", "Stop": "USAGE"}))
        return 2
    try:
        out = run(os.path.abspath(sys.argv[1]))
    except IdentityStop as e:
        print(json.dumps({"Kind": "DSP004_PHASE4_HARNESS_REV1_OBSERVATION", "Stop": str(e)}))
        return 2
    except Exception as e:
        print(json.dumps({"Kind": "DSP004_PHASE4_HARNESS_REV1_OBSERVATION", "Stop": "HARNESS_ERROR",
                          "Type": type(e).__name__, "Message": str(e)}))
        return 3
    sys.stdout.write(json.dumps(out, ensure_ascii=True, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
