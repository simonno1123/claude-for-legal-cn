"""DSP-004 OD04-A v4: check every supervisor run in the run account's whole audit history.

Reads only committed RAW_REDACTED files: the latest whole-history event export (inv3), the three v4 run records,
the v3 run record, and the collect results. Prints one JSON object. Standard library only; writes nothing.
Run: python3 -I check_v4_history.py
"""
import json
import os
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
V3 = os.path.join(HERE, "..", "dsp004_od04a_t0_dry_run_v3")
NS = {"e": "http://schemas.microsoft.com/win/2004/08/events/event"}
PY = r"C:\Program Files\DSP004Runtime\Python312\python.exe"
SUPDIR = r"C:\Program Files\DSP004Runtime\supervisor_v3"
EXP_PROBE_CMD = '"' + PY + '" -I -S -B "' + SUPDIR + r'\probe_v3.py"'
EXP_SUP_CMD_TAIL = '-File "' + SUPDIR + r'\supervisor_v3.ps1"'
EXP_CMD_CMD = r'C:\Windows\System32\cmd.exe /c ""' + SUPDIR + r'\run_v3.cmd""'
ALLOWED_IMAGES = {"cmd.exe", "conhost.exe", "powershell.exe", "whoami.exe", "python.exe"}
INSTALLED = {"supervisor_v3.ps1": "7CC3EC3D0432BFFE3D9ADAA34D90ED10DB015F5AFC241221E77E517B69C9E433",
             "probe_v3.py": "3AF5FD03B9487642A7256EAA21D654F6BF072749EBAF03B967A3E307C34CB2A3",
             "bound_list_v3.json": "0A349A6DBDA8B1397941EDE195D6D76E5B77DBE252BA6D3B80E0516016AAE561",
             "run_v3.cmd": "B430D9B22CACEDEEAE9C3124916ECFF8FD023EFABAE8D870920ECD2DAE64195A"}
GO_SHA = "C03B667309170D351983F82DEAE69E9008758F78CF11F9CD874D2CC35F2E78A6"
COLLECT_R2_SHA = "A48773E80CF31877AF71F9807E3C2D2022D9D6B50E54D6ED3F7ECBD95A261652"


def load(p):
    with open(p, encoding="utf-8-sig") as f:
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
        s = head + "." + frac[:6].ljust(6, "0") + rest[len(frac):]
    return datetime.fromisoformat(s).astimezone(timezone.utc)


h = lambda s: int(s, 16)
img = lambda path: path.split("\\")[-1].lower()

events = []
for ev in ET.parse(os.path.join(HERE, "inv3_post_events_history.RAW_REDACTED.xml")).getroot().findall("e:Event", NS):
    s = ev.find("e:System", NS)
    ed = ev.find("e:EventData", NS)
    d = {x.get("Name"): (x.text or "") for x in (ed.findall("e:Data", NS) if ed is not None else [])}
    d["_Id"] = int(s.find("e:EventID", NS).text)
    d["_Rec"] = int(s.find("e:EventRecordID", NS).text)
    d["_Time"] = t(s.find("e:TimeCreated", NS).get("SystemTime"))
    events.append(d)
events.sort(key=lambda d: d["_Rec"])
ids = lambda n: [d for d in events if d["_Id"] == n]

records = [("v3", load(os.path.join(V3, "v3_run_record.RAW_REDACTED.json")))] + [
    (k, load(os.path.join(HERE, k + "_run_record.RAW_REDACTED.json"))) for k in ("inv1", "inv2", "inv3")]
posts = {k: load(os.path.join(HERE, k + "_post_collect_result.RAW_REDACTED.json")) for k in ("inv1", "inv2", "inv3")}
v3col = load(os.path.join(V3, "collect_v3_result.RAW_REDACTED.json"))

run_sid = records[0][1]["Values"]["Account"]["Sid"]
created = [d for d in ids(4720) if d["TargetSid"] == run_sid]
starts = [d for d in ids(4688) if d.get("SubjectUserName", "").lower() == "dsp004val" or d.get("TargetUserName", "").lower() == "dsp004val"]
exits = [d for d in ids(4689) if d.get("SubjectUserName", "").lower() == "dsp004val"]
sups = [d for d in starts if img(d["NewProcessName"]) == "powershell.exe"]
c = {}
detail = []

c["H01_OneCreationEventForRunAccount"] = len(created) == 1
c["H02_EveryRunAccountStartHasCommandLine"] = all(d["CommandLine"] for d in starts)
c["H03_OnlyExpectedImages"] = {img(d["NewProcessName"]) for d in starts} <= ALLOWED_IMAGES
c["H04_SupervisorLaunchesEqualRecords"] = len(sups) == len(records) == 4
c["H05_EveryStartHasOneZeroExit"] = len(exits) == len(starts) and all(
    sum(1 for x in exits if h(x["ProcessId"]) == h(d["NewProcessId"]) and x["ProcessName"].lower() == d["NewProcessName"].lower()
        and h(x["Status"]) == 0 and x["_Rec"] > d["_Rec"]) == 1 for d in starts)

ok_match = ok_pass = ok_probes = ok_tree = ok_logon = True
for name, rec in records:
    v = rec["Values"]
    sp = [d for d in sups if h(d["NewProcessId"]) == v["SupervisorPid"] and abs((d["_Time"] - t(v["StartedUtc"])).total_seconds()) < 5]
    if len(sp) != 1:
        ok_match = False
        detail.append({"Run": name, "Problem": "no unique supervisor 4688"})
        continue
    s4688 = sp[0]
    ok_match &= s4688["CommandLine"].endswith(EXP_SUP_CMD_TAIL)
    rc = rec["Checks"]["Run"]
    ok_pass &= rec["Outcome"] == "PASS_T0_DRY_RUN_V3" and len(rc) == 69 and all(x is True for x in rc.values())
    kids = [d for d in starts if h(d["ProcessId"]) == v["SupervisorPid"] and d["_Rec"] > s4688["_Rec"]
            and (d["_Time"] - s4688["_Time"]).total_seconds() < 300]
    probes = [d for d in kids if img(d["NewProcessName"]) == "python.exe"]
    ok_probes &= (len(probes) == 3 and [h(d["NewProcessId"]) for d in probes] == [r["Pid"] for r in sorted(v["Runs"], key=lambda r: r["N"])]
                  and all(d["CommandLine"] == EXP_PROBE_CMD for d in probes))
    cmd = [d for d in starts if h(d["NewProcessId"]) == h(s4688["ProcessId"]) and d["_Rec"] < s4688["_Rec"] and img(d["NewProcessName"]) == "cmd.exe"]
    ok_tree &= (len(cmd) == 1 and cmd[0]["CommandLine"] == EXP_CMD_CMD and img(cmd[0]["ParentProcessName"]) == "runas.exe"
                and sorted(img(d["NewProcessName"]) for d in kids) == ["python.exe"] * 3 + ["whoami.exe"])
    if cmd:
        lid = cmd[0]["TargetLogonId"].lower()
        lg = [d for d in ids(4624) if d.get("TargetLogonId", "").lower() == lid and d.get("TargetUserName", "").lower() == "dsp004val"]
        ex = [d for d in ids(4648) if d.get("TargetUserName", "").lower() == "dsp004val" and 0 <= (cmd[0]["_Time"] - d["_Time"]).total_seconds() < 10]
        ok_logon &= len(lg) == 1 and lg[0]["LogonType"] == "2" and len(ex) >= 1
        detail.append({"Run": name, "SupervisorStartUtc": s4688["_Time"].isoformat(), "SupervisorPid": v["SupervisorPid"], "LogonId": lid,
                       "ProbePids": [h(d["NewProcessId"]) for d in probes]})
c["H06_EachRecordMatchesOneSupervisorStart"] = ok_match
c["H07_EachRecordPass69of69"] = ok_pass
c["H08_EachRunThreeProbesPidsAndCommandLineMatch"] = ok_probes
c["H09_EachRunTreeRunasCmdSupervisorChildren"] = ok_tree
c["H10_EachRunOwnInteractiveLogonWithExplicitCredentials"] = ok_logon
lids = [x["LogonId"] for x in detail if "LogonId" in x]
c["H11_EachRunSeparateLogonSession"] = len(set(lids)) == len(lids) == 4
boots = ids(4608)
st = sorted(d["_Time"] for d in sups)
# Planned: v4 runs 1 and 2, Restart, run 3. Actual: v4 run 1, Restart, v4 runs 2 and 3 (recorded as a deviation).
c["H12_RebootBetweenV4Invocation1And2"] = len(boots) >= 1 and any(st[1] < b["_Time"] < st[2] for b in boots)
c["H13_RunsAfterRebootExist"] = sum(1 for x in st if boots and x > max(b["_Time"] for b in boots)) == 2
p3 = posts["inv3"]
rn = p3["RecordNumbers"]
c["H14_RecordNumbersContiguousFromCreation"] = rn["Gaps"] == 0 and rn["FirstIsCreation"] is True and rn["CreationRecordId"] == created[0]["_Rec"] and rn["Count"] == rn["Last"] - rn["First"] + 1
chain = [posts[k]["RecordNumbers"] for k in ("inv1", "inv2", "inv3")]
c["H15_RecordNumberChainGrowsFromSameStart"] = all(x["First"] == chain[0]["First"] for x in chain) and chain[0]["Last"] < chain[1]["Last"] < chain[2]["Last"]
ie = p3["IntegrityEvents"]
c["H16_NoLogCleared"] = ie["Event1102"]["Count"] == 0 and ie["Event1104"]["Count"] == 0 and ie["Event1105"]["Count"] == 0 and ie["Event1108"]["Count"] == 0
pol = ids(4719)
c["H17_AuditPolicyChangesOnlyAtSetup"] = len(pol) == 2 and all(abs((d["_Time"] - created[0]["_Time"]).total_seconds()) < 5 for d in pol) and {d["SubcategoryGuid"].lower() for d in pol} == {"{0cce922b-69ae-11d9-bed3-505054503030}", "{0cce922c-69ae-11d9-bed3-505054503030}"}
tc = [t(x) for x in ie["Event4616"]["TimesUtc"]]
c["H18_TimeChangesOnlyAroundReboot"] = all(any(abs((x - b["_Time"]).total_seconds()) < 120 for b in boots) for x in tc)
c["H19_InstalledFilesUnchangedAtEveryCollection"] = all(f["MatchesExpected"] and f["SHA256"] == INSTALLED[f["Name"]] for k in posts for f in posts[k]["InstalledFiles"]) and all(f["MatchesExpected"] for f in v3col["InstalledFilesAfterRun"])
c["H20_LauncherAndCollectorAsBound"] = all({x["Name"]: x["SHA256"] for x in posts[k]["LauncherFilesNow"]} == {"go_v4.cmd": GO_SHA, "collect_v4.ps1": COLLECT_R2_SHA} and posts[k]["CollectorSha256"] == COLLECT_R2_SHA for k in posts)
c["H21_LogCoversWholeHistory"] = p3["SecurityLog"]["OldestBeforeWindow"] is True
c["H22_RunAccountAlwaysMediumNotElevated"] = all(d["MandatoryLabel"] == "S-1-16-8192" and d["TokenElevationType"] == "%%1936" for d in starts)
# Added after the post-run review: nothing else by the run account, anywhere in its retained history.
sessions = set(lids)
cur = lambda d: d.get("TargetUserSid", d.get("TargetSid", "")) == run_sid or d.get("SubjectUserSid", "") == run_sid
by_acct = [d for d in events if d.get("SubjectUserName", "").lower() == "dsp004val"]
c["H23_EveryRunAccountEventInARunSession"] = all(d.get("SubjectLogonId", "").lower() in sessions for d in by_acct) and all(
    d["TargetLogonId"].lower() in sessions for d in starts if d.get("SubjectUserName", "").lower() != "dsp004val")
c["H24_ExactlyFourLogonsNoFailuresNoPrivileged"] = (
    len([d for d in ids(4624) if d.get("TargetUserSid") == run_sid]) == 4 and len([d for d in ids(4648) if d.get("TargetUserName", "").lower() == "dsp004val"]) == 4
    and len(ids(4625)) == 0 and len(ids(4672)) == 0 and len(ids(4647)) == 0)
pattern = sorted(["cmd.exe", "conhost.exe", "powershell.exe", "whoami.exe"] + ["python.exe"] * 3 + ["conhost.exe"] * 3)
c["H25_EachSessionExactlyTenStartsInPattern"] = all(
    sorted(img(d["NewProcessName"]) for d in starts
           if (d.get("SubjectLogonId", "").lower() == sid_ if d.get("SubjectUserName", "").lower() == "dsp004val" else d["TargetLogonId"].lower() == sid_)) == pattern
    for sid_ in sessions) and len(starts) == 10 * len(sessions)
old = {d["TargetSid"] for d in ids(4720) if d["TargetSid"] != run_sid}
c["H26_EarlierSameNameAccountOnlyCreatedAndDeleted"] = all(
    [x["_Id"] for x in events if old_sid in (x.get("TargetSid"), x.get("TargetUserSid"), x.get("SubjectUserSid"))] == [4720, 4726] for old_sid in old)
pres = {"invocation1": load(os.path.join(HERE, "invocation1_pre_collect_result.json")),
        "inv2": load(os.path.join(HERE, "inv2_pre_collect_result.RAW_REDACTED.json")),
        "inv3": load(os.path.join(HERE, "inv3_pre_collect_result.RAW_REDACTED.json"))}
COLLECT_R1_SHA = "1199400BB288A6C1B9B05EC20F5D90C6F3E007AEC2BEC88BBF684430369FBD9B"
c["H27_PreStagesAsBound"] = (pres["invocation1"]["CollectorSha256"] == COLLECT_R1_SHA and pres["invocation1"]["RunRecord"]["SHA256"] == "FB530784EE2BA491E0D28CFDEC5111A70B8A830F6AB93C334F10BE5AF2CC79F4"
    and all(pres[k]["CollectorSha256"] == COLLECT_R2_SHA and pres[k]["RunRecordFound"] is False for k in ("inv2", "inv3"))
    and all({x["Name"]: x["SHA256"] for x in pres[k]["LauncherFilesNow"]}["go_v4.cmd"] == GO_SHA for k in pres))
logoffs = {d["TargetLogonId"].lower() for d in ids(4634) if d.get("TargetUserName", "").lower() == "dsp004val"}
c = dict(sorted(c.items()))
print(json.dumps({"Checks": c, "Passed": sum(1 for x in c.values() if x), "Total": len(c),
                  "SupervisorStartsUtc": [x.isoformat() for x in st], "BootsUtc": [b["_Time"].isoformat() for b in boots],
                  "RunAccountStarts": len(starts), "RunAccountExits": len(exits), "Runs": detail,
                  "OtherCreationEventsForName": [{"TimeUtc": d["_Time"].isoformat(), "TargetSid": d["TargetSid"]} for d in ids(4720) if d["TargetSid"] != run_sid],
                  "DeletionEventsForName": [{"TimeUtc": d["_Time"].isoformat(), "TargetSid": d.get("TargetSid")} for d in ids(4726)],
                  "RecordNumbers": rn, "SessionsWithoutLogoffEvent": sorted(sessions - logoffs),
                  "Note": "checks were written after the data was seen; counts (4 runs, 1 reboot) are fitted to what happened"}, indent=1))
