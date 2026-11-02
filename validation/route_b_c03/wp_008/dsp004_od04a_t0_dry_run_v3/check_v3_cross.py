"""DSP-004 OD04-A v3: cross-check the supervisor's run record against the system-written Security events.

Reads only the committed RAW_REDACTED files next to this script and prints one JSON object with each check.
Run: python3 -I check_v3_cross.py   (standard library only, no network, writes nothing)
"""
import json
import os
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
NS = {"e": "http://schemas.microsoft.com/win/2004/08/events/event"}
PY = r"C:\Program Files\DSP004Runtime\Python312\python.exe"
PROBE = r"C:\Program Files\DSP004Runtime\supervisor_v3\probe_v3.py"
SUP = r"C:\Program Files\DSP004Runtime\supervisor_v3\supervisor_v3.ps1"
RUNCMD = r"C:\Program Files\DSP004Runtime\supervisor_v3\run_v3.cmd"
BINDING_MERGE_UTC = "2026-11-02T04:29:56Z"  # PR #35 merged_at (GitHub)


def load(name):
    with open(os.path.join(HERE, name), encoding="utf-8-sig") as f:
        return json.load(f)


def t(s):
    s = s.replace("Z", "+00:00")
    if "." in s:
        head, rest = s.split(".", 1)
        frac = ""
        for ch in rest:
            if not ch.isdigit():
                break
            frac += ch
        tz = rest[len(frac):]
        s = head + "." + frac[:6].ljust(6, "0") + tz
    return datetime.fromisoformat(s).astimezone(timezone.utc)


rec = load("v3_run_record.RAW_REDACTED.json")
col = load("collect_v3_result.RAW_REDACTED.json")
ins = load("install_v3_result.RAW_REDACTED.json")
root = ET.parse(os.path.join(HERE, "events_dsp004val.RAW_REDACTED.xml")).getroot()

events = []
for ev in root.findall("e:Event", NS):
    sysn = ev.find("e:System", NS)
    d = {x.get("Name"): (x.text or "") for x in ev.find("e:EventData", NS).findall("e:Data", NS)}
    d["_Id"] = int(sysn.find("e:EventID", NS).text)
    d["_Time"] = t(sysn.find("e:TimeCreated", NS).get("SystemTime"))
    events.append(d)
events.sort(key=lambda d: d["_Time"])
h = lambda s: int(s, 16)
starts = [d for d in events if d["_Id"] == 4688]
exits = [d for d in events if d["_Id"] == 4689]
py_starts = [d for d in starts if d["NewProcessName"].lower() == PY.lower()]
v = rec["Values"]
runs = v["Runs"]
sup_pid = v["SupervisorPid"]
parent = v["Parent"]
exp_cmd = '"' + PY + '" -I -S -B "' + PROBE + '"'

c = {}
c["X01_ThreeProbeStartsInSystemLog"] = len(py_starts) == 3 == len(runs)
pairs = list(zip(py_starts, sorted(runs, key=lambda r: r["N"])))
c["X02_ProbePidsMatchRecord"] = all(h(e["NewProcessId"]) == r["Pid"] for e, r in pairs)
c["X03_ProbeCreatorIsSupervisor"] = all(h(e["ProcessId"]) == sup_pid for e, _ in pairs)
c["X04_ProbeCommandLineExact"] = all(e["CommandLine"] == exp_cmd == r["System"]["CommandLine"] for e, r in pairs)
c["X05_ProbeExitedZeroInSystemLog"] = all(
    any(x["ProcessId"] and h(x["ProcessId"]) == r["Pid"] and x["ProcessName"].lower() == PY.lower()
        and h(x["Status"]) == 0 and x["_Time"] >= e["_Time"] for x in exits) for e, r in pairs)
c["X06_ProbeCreateTimeWithin1sOfRecord"] = all(abs((e["_Time"] - t(r["System"]["CreatedUtc"])).total_seconds()) < 1 for e, r in pairs)
sup_ev = [d for d in starts if h(d["NewProcessId"]) == sup_pid]
c["X07_SupervisorStartInSystemLog"] = (len(sup_ev) == 1 and sup_ev[0]["NewProcessName"].lower().endswith(r"\windowspowershell\v1.0\powershell.exe")
                                       and SUP.lower() in sup_ev[0]["CommandLine"].lower() and h(sup_ev[0]["ProcessId"]) == parent["Pid"])
cmd_ev = [d for d in starts if h(d["NewProcessId"]) == parent["Pid"]]
c["X08_LauncherStartInSystemLog"] = (len(cmd_ev) == 1 and cmd_ev[0]["CommandLine"] == parent["CommandLine"] and RUNCMD.lower() in cmd_ev[0]["CommandLine"].lower())
# TargetUserName is "-" when the new process runs as its creator; the launcher cmd.exe is created by the secondary-logon
# service (subject = machine account) on behalf of dsp004val, so its TargetUserName is dsp004val.
c["X09_AllRunAccountStartsMediumAndRunAccount"] = all(
    d["MandatoryLabel"] == "S-1-16-8192"
    and ((d["SubjectUserName"].lower() == "dsp004val" and d["TargetUserName"] == "-") or d["TargetUserName"].lower() == "dsp004val")
    for d in starts)
c["X17_LauncherStartedByRunas"] = len(cmd_ev) == 1 and cmd_ev[0]["ParentProcessName"].lower() == r"c:\windows\system32\runas.exe" and cmd_ev[0]["TargetUserName"].lower() == "dsp004val"
c["X10_NoOtherPythonStartsByRunAccount"] = len([d for d in starts if d["NewProcessName"].lower().endswith("python.exe")]) == 3
ie = col["IntegrityEvents"]
c["X11_NoLogClearPolicyChangeOrTimeChangeInWindow"] = all(ie[k]["Count"] == 0 for k in ("Event1102", "Event4719", "Event4616"))
c["X12_LogCoversWholeWindow"] = col["SecurityLog"]["OldestBeforeWindow"] is True and col["SecurityLog"]["IsLogFull"] is False
c["X13_InstalledFilesUnchangedAfterRun"] = all(f["MatchesExpected"] for f in col["InstalledFilesAfterRun"])
run_checks = rec["Checks"]["Run"]
c["X14_SupervisorRecordPass"] = (rec["Outcome"] == "PASS_T0_DRY_RUN_V3" and len(run_checks) == 69 and all(x is True for x in run_checks.values())
                                 and rec["Checks"]["LockedFiles"] == 683 and rec["Checks"]["HashMismatches"] == 0)
c["X15_RunAccountNotAdmin"] = (v["Account"]["Name"].lower().endswith("\\dsp004val") and v["Account"]["AdministratorsGroupInToken"] is False
                               and v["Token"]["AdminRoleActive"] is False and v["Token"]["MediumIntegrity"] is True)
# Complete process tree of the run account in the window (added after the post-run review).
by_pid = {h(d["NewProcessId"]): d for d in starts}
img = lambda d: d["NewProcessName"].split("\\")[-1].lower()
cmd_pid = parent["Pid"]
edges = sorted((img(by_pid[h(d["ProcessId"])]) if h(d["ProcessId"]) in by_pid else d["ParentProcessName"].split("\\")[-1].lower(), img(d)) for d in starts)
c["X18_ProcessTreeExactlyAsExpected"] = (len(starts) == 10 and edges == sorted(
    [("runas.exe", "cmd.exe"), ("cmd.exe", "conhost.exe"), ("cmd.exe", "powershell.exe"), ("powershell.exe", "whoami.exe")]
    + [("powershell.exe", "python.exe")] * 3 + [("python.exe", "conhost.exe")] * 3))
c["X19_EveryStartHasZeroStatusExit"] = all(
    sum(1 for x in exits if h(x["ProcessId"]) == h(d["NewProcessId"]) and x["ProcessName"].lower() == d["NewProcessName"].lower()
        and h(x["Status"]) == 0 and x["_Time"] >= d["_Time"]) == 1 for d in starts) and len(exits) == len(starts)
logon = cmd_ev[0]["TargetLogonId"].lower() if cmd_ev else None
c["X20_SingleLogonSession"] = logon is not None and all(
    (d["SubjectLogonId"].lower() == logon) for d in events if d["SubjectUserName"].lower() == "dsp004val")
c["X21_RunAccountSidMatchesRecord"] = all(
    d["SubjectUserSid"] == v["Account"]["Sid"] for d in events if d["SubjectUserName"].lower() == "dsp004val")
# (the launcher's 4688 carries TargetUserName dsp004val but TargetUserSid S-1-0-0, so the SID is taken from subject fields)
sup_exit = [x for x in exits if h(x["ProcessId"]) == sup_pid and x["ProcessName"].lower().endswith("powershell.exe")]
rec_write = t(col["RunRecord"]["SourceLastWriteUtc"])
c["X22_RecordWrittenAfterReleaseBeforeSupervisorExit"] = len(sup_exit) == 1 and t(v["ReleasedUtc"]) <= rec_write <= sup_exit[0]["_Time"]
who = [d for d in starts if img(d) == "whoami.exe"]
c["X23_WhoamiByInstalledSupervisorAfterStart"] = len(who) == 1 and h(who[0]["ProcessId"]) == sup_pid and who[0]["_Time"] >= t(v["StartedUtc"])
c["X24_ProbeExitTimesMatchRecord"] = all(
    any(h(x["ProcessId"]) == r["Pid"] and x["ProcessName"].lower() == PY.lower() and abs((x["_Time"] - t(r["ExitSeenUtc"])).total_seconds()) < 1 for x in exits)
    for r in runs)
c["X06_ProbeCreateTimeWithin1sOfRecord"] = all(abs((e["_Time"] - t(r["System"]["CreatedUtc"])).total_seconds()) < 0.01 for e, r in pairs)
order = [t(BINDING_MERGE_UTC), t(ins["InstalledUtc"]), cmd_ev[0]["_Time"] if cmd_ev else None,
         sup_ev[0]["_Time"] if sup_ev else None, t(v["StartedUtc"]), py_starts[0]["_Time"] if py_starts else None,
         py_starts[-1]["_Time"] if py_starts else None, t(v["ReleasedUtc"]), rec_write,
         sup_exit[0]["_Time"] if sup_exit else None, t(col["CollectedUtc"])]
c["X16_TimelineOrdered"] = None not in order and all(a <= b for a, b in zip(order, order[1:]))
other = sorted({d["NewProcessName"].split("\\")[-1].lower() for d in starts})
c = dict(sorted(c.items()))
print(json.dumps({"Checks": c, "Passed": sum(1 for x in c.values() if x), "Total": len(c),
                  "RunAccountProcessImages": other, "RunAccountEvents": {"4688": len(starts), "4689": len(exits)},
                  "Timeline": [x.isoformat() if x else None for x in order]}, indent=1))
