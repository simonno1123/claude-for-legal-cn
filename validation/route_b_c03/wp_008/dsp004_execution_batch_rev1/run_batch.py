"""Fixed DSP-004 local-synthetic batch driver; no business-source adapter.

Run only under the separate Project Owner batch authorization. Arguments
select an append-only result attempt, never a permission flag or source path.
Source snapshots, compilation failures and unexpected test failures are kept.
Every host gets an independently owned outer Job. No accepted file is edited.
"""
from __future__ import annotations

import hashlib
import importlib.machinery
import json
import math
import os
from pathlib import Path
import sys
import time
import types

ROOT = Path("C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5")
BATCH = ROOT / "validation/route_b_c03/wp_008/dsp004_execution_batch_rev1"
PY_ROOT = Path("C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python")
PYTHON = PY_ROOT / "python.exe"
NEW_FILES = {
    "WIN": "windows_scope.py", "SUP": "supervisor_rev3.py",
    "BOOT": "bootstrap_rev2.py", "N": "carrier_rev4.py",
    "FAULT": "fault_fixture.py", "DRIVER": "run_batch.py",
}
PROTECTED = {
    "validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_FIXED_BOOTSTRAP_CANDIDATE_REV1.py":
        "4281385A8694C870A96E7EC7B98A9CB027A470C1AC2EE5F31BABCF9D56F46007",
    "validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV3.py":
        "329EC4A1C12351667F9A52946E4E11F6B01E287796FBDE42211FE5861CC14845",
    "validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_OUTER_SUPERVISOR_CANDIDATE_REV2.cs":
        "D097CBC8DEFA521F0B19ED06FF8A355881F95DB251453B760E644C33271BBE6A",
    "validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_CONTRACT_CANDIDATE_REV1.py":
        "E9472328847617EBF629FB01A0A163C0805226690600E5E13EBE1209E2F6705C",
    "scripts/phase2_runtime/route_b_c03/contracts.py":
        "7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4",
    "validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV2.py":
        "634AC0CB18B0877B619A4FFAEFBBD4AA95C8DEBAACD7018FEBFB6A4C18B03365",
    "validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_OUTER_SUPERVISOR_CANDIDATE_REV1.cs":
        "36C90727CA87F6F6235546B8A380784CED13E40E94F2CA7799C01EE0FC094B35",
}
RUNTIME = {
    "python.exe": "B07B03B9BA866A341A3C13EE69710FBC8D43D4CE2523DEE13F6DF5C25378D15B",
    "python3.dll": "F91CA7E29E8B4CC9ED7A4A935C1B2558C5C8F23398CB20D7048F977AA16FCE8B",
    "python312.dll": "3B33D49D879DBF3A8AA3FFF1BF3859275E76C188A3ADEC4E7FFE728243652A87",
    "vcruntime140.dll": "D5E4D9A3E835FA679450145D6A7D94E36573A509317111904D9B3712C30D9066",
    "vcruntime140_1.dll": "1F2D41C4AA5DB0BC33EBF7B66D72943A817D7CE6CBE880502A9403823633093F",
}
CASES = (
    "NORMAL", "EARLY_STOP", "BAD_B_SHA", "BAD_ORDER", "TRUNCATED_SOURCE",
    "EXTRA_SOURCE", "KEEP_CODE_OPEN", "BAD_COMMAND", "NEXT_DUPLICATE",
    "EXTRA_AFTER_STOP", "HANG", "STDOUT", "STDERR", "BAD_READY", "PARTIAL",
    "OVERLONG", "EARLY_EOF", "DUPLICATE", "OUT_OF_ORDER", "SETUP_NE",
    "CASE_FAIL", "TRAILER", "REAL_INTERRUPT", "DESCENDANT",
    "STDOUT_LATE", "STDERR_LATE", "HOST_HANG", "HOST_STALL_WITH_CHILD",
)
_HELD_DRIVER_ERRORS = []

def digest(data):
    return hashlib.sha256(data).hexdigest().upper()

def project_bytes(path):
    full = path.resolve(strict=True)
    if os.path.commonpath((str(ROOT.resolve()), str(full))) != str(ROOT.resolve()):
        raise RuntimeError("PROJECT_PATH_ESCAPED")
    return full.read_bytes()

def verify_protected():
    observed = {}
    for name, expected in PROTECTED.items():
        actual = digest(project_bytes(ROOT / name))
        if actual != expected:
            raise RuntimeError("PROTECTED_SHA_MISMATCH")
        observed[name] = actual
    return observed

def verify_runtime():
    if (os.name != "nt" or os.path.normcase(sys.executable) != os.path.normcase(str(PYTHON))
            or sys.version_info[:3] != (3, 12, 14) or sys.flags.isolated != 1
            or sys.flags.no_site != 1 or not sys.dont_write_bytecode):
        raise RuntimeError("FIXED_RUNTIME_OR_FLAGS_MISMATCH")
    hashes = {}
    for name, expected in RUNTIME.items():
        data = (PY_ROOT / name).read_bytes()
        actual = digest(data)
        if actual != expected:
            raise RuntimeError("RUNTIME_SHA_MISMATCH")
        hashes[name] = actual
    allowed_root = os.path.normcase(str(PY_ROOT.resolve()))
    for path in sys.path:
        if os.path.commonpath((allowed_root, os.path.normcase(os.path.abspath(path)))) != allowed_root:
            raise RuntimeError("UNEXPECTED_IMPORT_PATH")
    return {"version": sys.version, "executable": sys.executable,
            "flags": {"isolated": sys.flags.isolated, "no_site": sys.flags.no_site,
                      "dont_write_bytecode": sys.dont_write_bytecode},
            "runtime_hashes": hashes, "sys_path_recorded": list(sys.path),
            "full_dependency_provenance": "LIMITED"}

def load_owned(name, data):
    if name in sys.modules:
        raise RuntimeError("MODULE_SLOT_OCCUPIED")
    module = types.ModuleType(name)
    module.__spec__ = importlib.machinery.ModuleSpec(name, loader=None)
    module.__file__ = "<DSP004_BATCH_BYTES>"
    sys.modules[name] = module
    exec(compile(data, module.__file__, "exec", dont_inherit=True, optimize=0), module.__dict__)
    return module

def host_input(assets):
    descriptors = tuple((role, len(value), digest(value)) for role, value in assets.items())
    body = bytearray(b"DSP004-HOST-SOURCES-V1\n")
    for role, size, sha in descriptors:
        body.extend((role + "|" + str(size) + "|" + sha + "\n").encode("ascii"))
        body.extend(assets[role])
    if len(body) > 262144:
        raise RuntimeError("HOST_SOURCE_FRAME_OVERFLOW")
    # The child cannot select source paths or alternative versions.
    loader = (
        "import sys,os,json,hashlib,msvcrt,types,importlib.machinery\n"
        "from io import FileIO\n"
        "D=" + repr(descriptors) + "\n"
        "T0=" + repr(_BATCH_T0) + "\n"
        "held=[]\n"
        "def exact(stream,n):\n"
        " out=b''\n"
        " while len(out)<n:\n"
        "  part=stream.read(n-len(out))\n"
        "  if not part: raise RuntimeError('HOST_INPUT_EOF')\n"
        "  out+=part\n"
        " return out\n"
        "def send(stream,data):\n"
        " while data:\n"
        "  n=stream.write(data)\n"
        "  if type(n) is not int or n<=0: raise RuntimeError('HOST_REPORT_WRITE')\n"
        "  data=data[n:]\n"
        "def main():\n"
        " code=sys.stdin.buffer.raw\n"
        " assets={}\n"
        " if exact(code,len(b'DSP004-HOST-SOURCES-V1\\n'))!=b'DSP004-HOST-SOURCES-V1\\n': raise RuntimeError('HOST_PREFIX')\n"
        " for role,n,sha in D:\n"
        "  header=(role+'|'+str(n)+'|'+sha+'\\n').encode('ascii')\n"
        "  if exact(code,len(header))!=header: raise RuntimeError('HOST_HEADER')\n"
        "  data=exact(code,n)\n"
        "  if hashlib.sha256(data).hexdigest().upper()!=sha: raise RuntimeError('HOST_SHA')\n"
        "  assets[role]=data\n"
        " if code.read(1)!=b'': raise RuntimeError('HOST_TRAILER')\n"
        " report=FileIO(msvcrt.open_osfhandle(int(sys.argv[2]),os.O_WRONLY|os.O_BINARY),'wb')\n"
        " held.append(report)\n"
        " for role,name in (('WIN','dsp004_windows_scope'),('SUP','dsp004_supervisor')):\n"
        "  if name in sys.modules: raise RuntimeError('HOST_MODULE_OCCUPIED')\n"
        "  module=types.ModuleType(name)\n"
        "  module.__spec__=importlib.machinery.ModuleSpec(name,loader=None)\n"
        "  module.__file__='<DSP004_HOST_BYTES>'\n"
        "  sys.modules[name]=module\n"
        "  exec(compile(assets[role],module.__file__,'exec',dont_inherit=True,optimize=0),module.__dict__)\n"
        " result=sys.modules['dsp004_supervisor'].run_case(sys.argv[3],assets,os.getcwd(),T0,lambda data:send(report,data))\n"
        " data=b'DSP004-RESULT-V1|'+json.dumps(result,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode('ascii')+b'\\n'\n"
        " if len(data)>16384: raise RuntimeError('HOST_RESULT_BOUND')\n"
        " send(report,data)\n"
        " report.close()\n"
        "try:\n"
        " main()\n"
        "except BaseException as original:\n"
        " held.append(original)\n"
        " raise SystemExit(78)\n"
    ).encode("utf-8")
    return loader, bytes(body)

def expected(case, result):
    if (not result["scope_clean_observed"] or not result["writers_settled"]
            or result["cleanup_errors_held"] or result["active_after_stop"] != 0
            or not result["child_created"] or not result["child_resumed"]
            or type(result["direct_exit_observed"]) is not int
            or not all(result["standard_eof_observed"].values())):
        return False
    output_fault = case in ("STDOUT", "STDERR", "STDOUT_LATE", "STDERR_LATE")
    if not output_fault and any(result["standard_bytes_detected"].values()):
        return False
    if result["ready_observed"] != (case in (
            "NORMAL", "EARLY_STOP", "BAD_COMMAND", "NEXT_DUPLICATE", "EXTRA_AFTER_STOP",
            "DUPLICATE", "OUT_OF_ORDER", "SETUP_NE", "CASE_FAIL", "TRAILER",
            "REAL_INTERRUPT", "STDOUT_LATE", "STDERR_LATE")):
        return False
    if result["native_supplement_reports"] != (8 if case in (
            "NORMAL", "EARLY_STOP", "BAD_COMMAND", "NEXT_DUPLICATE", "EXTRA_AFTER_STOP") else 0):
        return False
    if case == "NORMAL":
        return (result["status"] == "NATIVE_DIRECTORY_REPORTED_COMPLETE"
                and result["reports"] == result["pass_reports"] == 158
                and result["native_supplement_reports"] == 8
                and result["dispatch_attempts_or_unknown"] == 158
                and result["direct_exit_observed"] == 0)
    if case == "EARLY_STOP":
        return (result["status"] == "EARLY_STOP" and result["reports"] == 0
                and result["dispatch_attempts_or_unknown"] == 0
                and result["direct_exit_observed"] == 0)
    if case in ("SETUP_NE", "CASE_FAIL"):
        phase, determination = ("SETUP", "NOT_EVALUABLE") if case == "SETUP_NE" else ("SUT", "FAIL")
        return (result["status"] == "STOPPED_ON_NONPASS" and result["reports"] == 1
                and result["dispatch_attempts_or_unknown"] == 1
                and result["last_report_phase"] == phase
                and result["last_report_determination"] == determination
                and result["direct_exit_observed"] == 0)
    if result["status"] != "PROTECTED_STOP":
        return False
    exact = {
        "HANG": "DEADLINE", "PARTIAL": "DEADLINE", "KEEP_CODE_OPEN": "DEADLINE",
        "STDOUT": "FORBIDDEN_STDOUT_BYTE", "STDERR": "FORBIDDEN_STDERR_BYTE",
        "BAD_READY": "READY_FRAME", "OVERLONG": "REPORT_OVERFLOW",
        "DUPLICATE": "REPORT_ORDER_OR_ID", "OUT_OF_ORDER": "REPORT_ORDER_OR_ID",
        "TRAILER": "EXTRA_REPORT_AFTER_STOPPED", "DESCENDANT": "DESCENDANT_STOP_EXERCISE",
        "BAD_COMMAND": "REPORT_EOF", "NEXT_DUPLICATE": "REPORT_EOF",
        "EXTRA_AFTER_STOP": "REPORT_EOF", "REAL_INTERRUPT": "REPORT_EOF",
        "EARLY_EOF": "REPORT_EOF", "STDOUT_LATE": "FORBIDDEN_STDOUT_BYTE",
        "STDERR_LATE": "FORBIDDEN_STDERR_BYTE",
    }
    if case in exact and result["reason"] != exact[case]:
        return False
    if case == "DESCENDANT" and result["maximum_active_observed"] < 2:
        return False
    counts = {
        "BAD_COMMAND": (0, 1), "NEXT_DUPLICATE": (1, 2), "EXTRA_AFTER_STOP": (158, 158),
        "DUPLICATE": (1, 2), "OUT_OF_ORDER": (0, 1), "TRAILER": (1, 1),
        "REAL_INTERRUPT": (0, 1), "STDOUT_LATE": (1, 1), "STDERR_LATE": (1, 1),
    }
    reports, attempts = counts.get(case, (0, 0))
    if (result["reports"] != reports or result["dispatch_attempts_or_unknown"] != attempts):
        return False
    if output_fault:
        role = "stdout" if case.startswith("STDOUT") else "stderr"
        return result["standard_bytes_detected"][role] >= 1
    if case in ("BAD_COMMAND", "NEXT_DUPLICATE", "EXTRA_AFTER_STOP", "REAL_INTERRUPT"):
        return result["direct_exit_observed"] == 78 and result["pass_reports"] == reports
    if case == "EARLY_EOF":
        return result["direct_exit_observed"] == 0
    if case in ("BAD_B_SHA", "BAD_ORDER", "TRUNCATED_SOURCE", "EXTRA_SOURCE"):
        # Only observed rejection/no native report; do not overclaim its cause.
        return result["direct_exit_observed"] == 78
    return True

def observe_case(case, assets, win):
    start = time.monotonic()
    outer = win.JobChild(_BATCH_T0, _BATCH_T0 + 70.0)
    received, error = None, None
    forced = case in ("HOST_HANG", "HOST_STALL_WITH_CHILD")
    outer_due = min(start + 10.0, _BATCH_T0 + 70.0)
    try:
        loader, payload = host_input(assets)
        outer.start(loader, str(BATCH), (case,))
        task = outer.write("code", payload, outer_due, close_after=True)
        outer.wait_write(task, outer_due)
        if forced:
            if outer.frame(outer_due, limit=16384) != b"DSP004-HOST-STALL-READY\n":
                raise RuntimeError("OUTER_STALL_MARKER")
            if case == "HOST_STALL_WITH_CHILD" and outer.active() < 2:
                raise RuntimeError("OUTER_CHILD_NOT_OBSERVED")
            stop_due = min(time.monotonic() + 0.3, outer_due)
            while time.monotonic() < stop_due:
                outer.monitor_zero()
                time.sleep(0.002)
            outer.kill()
        else:
            frame = outer.frame(outer_due, limit=16384)
            prefix = b"DSP004-RESULT-V1|"
            if not frame.startswith(prefix):
                raise RuntimeError("OUTER_RESULT_FRAME")
            received = json.loads(frame[len(prefix):-1])
            while True:
                outer.check(outer_due)
                outer.monitor_zero()
                tail = outer.poll("report")
                if tail == b"":
                    break
                if tail:
                    raise RuntimeError("OUTER_RESULT_TRAILER")
                time.sleep(0.002)
            while not outer.exited():
                outer.check(outer_due)
                outer.monitor_zero()
                time.sleep(0.002)
            if outer.exit_code() != 0:
                raise RuntimeError("HOST_EXIT_NONZERO")
    except BaseException as original:
        error = original
        _HELD_DRIVER_ERRORS.append((case, original))
        outer.keep_error("OUTER_OBSERVER", original)
    finally:
        clean = outer.settle(min(time.monotonic() + 5.0, _BATCH_T0 + 70.0),
                             terminate=error is not None or forced)
    outer_ok = (clean and outer.last_active == 0
                and not outer.cleanup_errors
                and outer.writers_settled()
                and all(outer.eof.get(role, False) for role in ("stdout", "stderr"))
                and not any(outer.standard_detected.values()))
    verdict = (outer_ok and error is None and
               ((forced and outer.kill_requested and outer.kill_returned)
                or (not forced and received is not None and expected(case, received))))
    return {
        "case": case, "test_determination": "PASS" if verdict else "FAIL",
        "subject_report": received,
        "outer_scope_clean_observed": clean,
        "outer_active_after_stop": outer.last_active,
        "outer_direct_exit": outer.observed_exit,
        "outer_kill_requested": outer.kill_requested,
        "outer_writers_settled": outer.writers_settled(),
        "outer_standard_bytes_detected": dict(outer.standard_detected),
        "outer_standard_eof_observed": {role: outer.eof.get(role, False) for role in ("stdout", "stderr")},
        "outer_error_type": None if error is None else type(error).__name__,
        "elapsed_seconds_observed": round(time.monotonic() - start, 6),
        "qualification": "LOCAL_SYNTHETIC_OBSERVATION_NOT_FORMAL_ACCEPTANCE",
    }

def main():
    global _BATCH_T0
    _BATCH_T0 = time.monotonic()  # Before this invocation's first source read/hash/IPC.
    if len(sys.argv) != 3 or sys.argv[1] != "--attempt" or not sys.argv[2].isdigit():
        raise RuntimeError("EXPLICIT_RESULT_ATTEMPT_REQUIRED")
    attempt = int(sys.argv[2])
    if not 1 <= attempt <= 99:
        raise RuntimeError("ATTEMPT_RANGE")
    output = BATCH / ("attempt_" + str(attempt).zfill(2) + "_result.json")
    snapshot = BATCH / ("attempt_" + str(attempt).zfill(2) + "_sources.json")
    if output.exists() or snapshot.exists():
        raise RuntimeError("PRIOR_ATTEMPT_MUST_NOT_BE_OVERWRITTEN")
    assets = {}
    result = {
        "attempt": attempt, "scope": "LOCAL_SYNTHETIC_ONLY",
        "status": "INCOMPLETE", "compilation": [], "cases": [],
        "dsp004": "OPEN / HOLD", "B-01": "OPEN", "B-02": "OPEN",
        "business_sources": "NOT_ADMITTED", "aggregate_privacy_security_legal_verdict": "NOT_ISSUED",
        "formal_acceptance": "NOT_ESTABLISHED_BY_THIS_RUN",
    }
    try:
        pins_data = project_bytes(BATCH / "candidate_pins.json")
        pins = json.loads(pins_data)
        if set(pins["new_files"]) != set(NEW_FILES):
            raise RuntimeError("PIN_ROLE_SET")
        snapshots = {}
        for role, name in NEW_FILES.items():
            data = project_bytes(BATCH / name)
            expected_sha = pins["new_files"][role]["sha256"]
            if (pins["new_files"][role]["file"] != name
                    or len(data) != pins["new_files"][role]["bytes"] or digest(data) != expected_sha):
                raise RuntimeError("NEW_SOURCE_IDENTITY_MISMATCH")
            snapshots[name] = {"sha256": digest(data), "utf8_source": data.decode("utf-8", "strict")}
            if role != "DRIVER":
                assets[role] = data
        with snapshot.open("x", encoding="utf-8", newline="\n") as stream:
            json.dump({"new_sources": snapshots, "pins_sha256": digest(pins_data)}, stream,
                      ensure_ascii=True, sort_keys=True, indent=2)
            stream.write("\n")
        result["new_source_hashes"] = {name: value["sha256"] for name, value in snapshots.items()}
        result["pins_sha256"] = digest(pins_data)
        result["protected_before"] = verify_protected()
        result["runtime_before"] = verify_runtime()
        for name, value in snapshots.items():
            try:
                compile(value["utf8_source"], name, "exec", dont_inherit=True, optimize=0)
            except BaseException:
                result["compilation"].append({"file": name, "determination": "FAIL"})
                raise
            else:
                result["compilation"].append({"file": name, "determination": "PASS"})
        assets["B"] = project_bytes(ROOT / "scripts/phase2_runtime/route_b_c03/contracts.py")
        assets["A"] = project_bytes(ROOT / "validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_CONTRACT_CANDIDATE_REV1.py")
        win = load_owned("dsp004_windows_scope", assets["WIN"])
        for index, case in enumerate(CASES):
            observed = observe_case(case, assets, win)
            result["cases"].append(observed)
            if observed["test_determination"] != "PASS":
                result["not_started_case_ids"] = list(CASES[index + 1:])
                break
        result["protected_after"] = verify_protected()
        result["runtime_after"] = verify_runtime()
        passed = sum(item["test_determination"] == "PASS" for item in result["cases"])
        failed = sum(item["test_determination"] == "FAIL" for item in result["cases"])
        result["counts"] = {"passed": passed, "failed": failed, "planned": len(CASES)}
        result["status"] = "PASS" if passed == len(CASES) and failed == 0 else "FAIL"
    except BaseException as original:
        _HELD_DRIVER_ERRORS.append(("BATCH", original))
        result["status"] = "FAIL"
        result["unexpected_error_type"] = type(original).__name__
        result["compilation_failure_details"] = (
            {"line": original.lineno, "offset": original.offset}
            if isinstance(original, SyntaxError) else None)
    result["elapsed_seconds_observed"] = round(time.monotonic() - _BATCH_T0, 6)
    result["remaining_limited"] = [
        "FULL_DEPENDENCY_PROVENANCE_AND_CHECK_TO_USE",
        "UNOBSERVED_OS_SCHEDULES_AND_NATIVE_SYNCHRONOUS_CALLS",
        "DURABLE_NATIVE_ERROR_PRESERVATION_AFTER_HOST_DEATH",
        "FULL_189_INPUT_PLAN_AND_D007_BUSINESS_SOURCE_PATH",
        "FORMAL_SOURCE_ADMISSION_ACCEPTANCE_INTEGRATION_DEPLOYMENT",
    ]
    with output.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(result, stream, ensure_ascii=True, sort_keys=True, indent=2)
        stream.write("\n")
    print(json.dumps({"attempt": attempt, "status": result["status"],
                      "counts": result.get("counts"), "result": str(output)}, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
