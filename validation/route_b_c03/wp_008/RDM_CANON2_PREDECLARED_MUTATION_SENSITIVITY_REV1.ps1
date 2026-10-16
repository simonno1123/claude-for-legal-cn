$ErrorActionPreference = 'Stop'
$utf8 = [Text.UTF8Encoding]::new($false, $true)
[Console]::OutputEncoding = $utf8
$root = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/'
$executable = 'C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
$executableSha = 'B847BB9F4E48C19F585C8BF7D8B355F3F8C6D2125717ECE9C9D7E16FB9F09DE8'
$sources = '[{"Role":"scalar","Path":"validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_CANDIDATE_REV1.py","SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},{"Role":"scalar_validation","Path":"validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_VALIDATION_REV1.py","SHA256":"1F473042AFE4455A194DD5DFD95DED9EEBBEDE2B77F5228AA8B1DE6759270485","Bytes":10002},{"Role":"tree","Path":"validation/route_b_c03/wp_008/RDM_CANON2_STRUCTURAL_LAYOUT_CANDIDATE_REV1.py","SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},{"Role":"tree_validation","Path":"validation/route_b_c03/wp_008/RDM_CANON2_STRUCTURAL_LAYOUT_VALIDATION_REV1.py","SHA256":"182F6E64EEACD3BC4B29180CD01E11913CCC0CFFCDDFCC432ED0A5FE34113D39","Bytes":11526}]' | ConvertFrom-Json
$definitions = '[{"Id":"MU-S01","TargetRole":"scalar","Before":"format(point, \"02x\")","After":"format(point, \"02X\")","ExpectedAssertion":"S-ALL-CONTROLS.BYTES","Topic":"控制字符十六进制大小写","Matches":1,"MutatedSHA256":"331377B2D0678C91EEFABAD42A3D52494F2D5967ED72A4E6B50FD0F8C58043D9","MutatedBytes":8234},{"Id":"MU-S02","TargetRole":"scalar","Before":"return b\"true\" if value else b\"false\"","After":"return b\"false\" if value else b\"true\"","ExpectedAssertion":"B-TRUE.BYTES","Topic":"布尔编码反转","Matches":1,"MutatedSHA256":"C9F9C737304298F8CA907FE9F70172D1860E856F8A2E2089E61AE0B5F16C4BC3","MutatedBytes":8234},{"Id":"MU-S03","TargetRole":"scalar","Before":"_reject(key in result, \"DUPLICATE_DECODED_KEY\")","After":"_reject(False, \"DUPLICATE_DECODED_KEY\")","ExpectedAssertion":"P-DECODED-DUPLICATE-0","Topic":"重复键防线移除","Matches":1,"MutatedSHA256":"FAC557DD990C9E3976F809D7806F0E234059B6670081952F68973F1AB0748BA3","MutatedBytes":8226},{"Id":"MU-S04","TargetRole":"scalar","Before":"_reject(previous is not None and key <= previous, \"ENTRY_ORDER\")","After":"_reject(False, \"ENTRY_ORDER\")","ExpectedAssertion":"E-UTF16-ORDER-REFUSED","Topic":"条目排序防线移除","Matches":1,"MutatedSHA256":"78DF7AB168C383010E78EF447151D51C9E14071F5BA47711E7E60C0B9A487D9B","MutatedBytes":8199},{"Id":"MU-T01","TargetRole":"tree","Before":"for key in sorted(fields):","After":"for key in sorted(fields, reverse=True):","ExpectedAssertion":"T-MIXED.BYTES","Topic":"对象键倒序","Matches":1,"MutatedSHA256":"70FA9086D6DA1C5CA8A9BD834A9C1814D13018BC5C67E53C57D8DFC7583BC5C3","MutatedBytes":9967},{"Id":"MU-T02","TargetRole":"tree","Before":"_require(len(set(keys)) == len(keys), \"SET_SORTED_TIE\")","After":"_require(True, \"SET_SORTED_TIE\")","ExpectedAssertion":"N-SORT-TIE","Topic":"数组同 key 防线移除","Matches":1,"MutatedSHA256":"4B34FB7D711D6E83A1ABC42192418F2D8D25C57B693B7C064E11BFE2260A3195","MutatedBytes":9930},{"Id":"MU-T03","TargetRole":"tree","Before":"    if pretty:\n        append(b\"\\n\")\n    return b\"\".join(parts)","After":"    if pretty:\n        append(b\"\")\n    return b\"\".join(parts)","ExpectedAssertion":"T-EMPTY.BYTES","Topic":"文档最终 LF 移除","Matches":1,"MutatedSHA256":"6F27BA03EB704C858A5F82F2752C75E79D17444DF7E78C7E4C98C28F63912783","MutatedBytes":9951},{"Id":"MU-T04","TargetRole":"tree","Before":"_require(raw == expected, \"NONCANONICAL_DOCUMENT_BYTES\")","After":"_require(True, \"NONCANONICAL_DOCUMENT_BYTES\")","ExpectedAssertion":"R-KEY-ORDER","Topic":"原始字节一致性防线移除","Matches":1,"MutatedSHA256":"E0A55AFCF1E10155F17900CB0521C12B0CE08117325B6C9A7DFF925E26CEEF60","MutatedBytes":9942}]' | ConvertFrom-Json
$cases = '[{"Id":"BASE-SCALAR","Mode":"scalar","ExpectedAssertion":null,"Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"scalar_validation":{"SHA256":"1F473042AFE4455A194DD5DFD95DED9EEBBEDE2B77F5228AA8B1DE6759270485","Bytes":10002}}},{"Id":"BASE-TREE","Mode":"tree","ExpectedAssertion":null,"Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"tree_validation":{"SHA256":"182F6E64EEACD3BC4B29180CD01E11913CCC0CFFCDDFCC432ED0A5FE34113D39","Bytes":11526}}},{"Id":"MU-S01","Mode":"scalar","ExpectedAssertion":"S-ALL-CONTROLS.BYTES","Sources":{"scalar":{"SHA256":"331377B2D0678C91EEFABAD42A3D52494F2D5967ED72A4E6B50FD0F8C58043D9","Bytes":8234},"scalar_validation":{"SHA256":"1F473042AFE4455A194DD5DFD95DED9EEBBEDE2B77F5228AA8B1DE6759270485","Bytes":10002}}},{"Id":"MU-S02","Mode":"scalar","ExpectedAssertion":"B-TRUE.BYTES","Sources":{"scalar":{"SHA256":"C9F9C737304298F8CA907FE9F70172D1860E856F8A2E2089E61AE0B5F16C4BC3","Bytes":8234},"scalar_validation":{"SHA256":"1F473042AFE4455A194DD5DFD95DED9EEBBEDE2B77F5228AA8B1DE6759270485","Bytes":10002}}},{"Id":"MU-S03","Mode":"scalar","ExpectedAssertion":"P-DECODED-DUPLICATE-0","Sources":{"scalar":{"SHA256":"FAC557DD990C9E3976F809D7806F0E234059B6670081952F68973F1AB0748BA3","Bytes":8226},"scalar_validation":{"SHA256":"1F473042AFE4455A194DD5DFD95DED9EEBBEDE2B77F5228AA8B1DE6759270485","Bytes":10002}}},{"Id":"MU-S04","Mode":"scalar","ExpectedAssertion":"E-UTF16-ORDER-REFUSED","Sources":{"scalar":{"SHA256":"78DF7AB168C383010E78EF447151D51C9E14071F5BA47711E7E60C0B9A487D9B","Bytes":8199},"scalar_validation":{"SHA256":"1F473042AFE4455A194DD5DFD95DED9EEBBEDE2B77F5228AA8B1DE6759270485","Bytes":10002}}},{"Id":"MU-T01","Mode":"tree","ExpectedAssertion":"T-MIXED.BYTES","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"70FA9086D6DA1C5CA8A9BD834A9C1814D13018BC5C67E53C57D8DFC7583BC5C3","Bytes":9967},"tree_validation":{"SHA256":"182F6E64EEACD3BC4B29180CD01E11913CCC0CFFCDDFCC432ED0A5FE34113D39","Bytes":11526}}},{"Id":"MU-T02","Mode":"tree","ExpectedAssertion":"N-SORT-TIE","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"4B34FB7D711D6E83A1ABC42192418F2D8D25C57B693B7C064E11BFE2260A3195","Bytes":9930},"tree_validation":{"SHA256":"182F6E64EEACD3BC4B29180CD01E11913CCC0CFFCDDFCC432ED0A5FE34113D39","Bytes":11526}}},{"Id":"MU-T03","Mode":"tree","ExpectedAssertion":"T-EMPTY.BYTES","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"6F27BA03EB704C858A5F82F2752C75E79D17444DF7E78C7E4C98C28F63912783","Bytes":9951},"tree_validation":{"SHA256":"182F6E64EEACD3BC4B29180CD01E11913CCC0CFFCDDFCC432ED0A5FE34113D39","Bytes":11526}}},{"Id":"MU-T04","Mode":"tree","ExpectedAssertion":"R-KEY-ORDER","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"E0A55AFCF1E10155F17900CB0521C12B0CE08117325B6C9A7DFF925E26CEEF60","Bytes":9942},"tree_validation":{"SHA256":"182F6E64EEACD3BC4B29180CD01E11913CCC0CFFCDDFCC432ED0A5FE34113D39","Bytes":11526}}}]' | ConvertFrom-Json
function Digest([byte[]]$Bytes) { [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($Bytes)) }
function Zip([byte[]]$Bytes) {
  $output = [IO.MemoryStream]::new()
  $gzip = [IO.Compression.GZipStream]::new($output, [IO.Compression.CompressionMode]::Compress, $true)
  try { $gzip.Write($Bytes, 0, $Bytes.Length) } finally { $gzip.Dispose() }
  $result = $output.ToArray(); $output.Dispose()
  return ,$result
}
$originals = @{}
foreach ($s in $sources) {
  $bytes = [IO.File]::ReadAllBytes($root + $s.Path)
  if ($bytes.Length -ne $s.Bytes -or (Digest $bytes) -cne $s.SHA256) { throw 'FIXED_SOURCE_IDENTITY' }
  $null = $utf8.GetString($bytes)
  $originals[$s.Role] = $bytes
}
if ((Digest ([IO.File]::ReadAllBytes($executable))) -cne $executableSha) { throw 'PYTHON_EXECUTABLE_IDENTITY' }
$mutants = @{}
$snapshots = [Collections.Generic.List[object]]::new()
foreach ($d in $definitions) {
  $original = $originals[$d.TargetRole]
  $text = $utf8.GetString($original)
  $matches = ([regex]::Matches($text, [regex]::Escape($d.Before))).Count
  if ($matches -ne 1) { throw 'MUTATION_SITE_NOT_UNIQUE' }
  $bytes = $utf8.GetBytes($text.Replace($d.Before, $d.After))
  if ($bytes.Length -ne $d.MutatedBytes -or (Digest $bytes) -cne $d.MutatedSHA256) { throw 'MUTANT_IDENTITY' }
  $mutants[$d.Id] = $bytes
  $zipBytes = Zip $bytes
  $snapshots.Add([ordered]@{Id=$d.Id;TargetRole=$d.TargetRole;OriginalSHA256=(Digest $original);PatchMatches=$matches;Before=$d.Before;After=$d.After;ExpectedAssertion=$d.ExpectedAssertion;UTF8Bytes=$bytes.Length;SHA256=(Digest $bytes);GZipBytes=$zipBytes.Length;GZipBase64=[Convert]::ToBase64String($zipBytes);Qualification='IN-MEMORY SINGLE-FAULT TEST FIXTURE ONLY; NO PHYSICAL SOURCE MODIFIED'})
}
$bootstrap = @'
import ast, base64, hashlib, json, re, sys, types
sys.stdout.reconfigure(encoding="utf-8", errors="strict", newline="\n")
CASES = json.loads(r'''{"BASE-SCALAR":{"Id":"BASE-SCALAR","Mode":"scalar","ExpectedAssertion":null,"Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"scalar_validation":{"SHA256":"1F473042AFE4455A194DD5DFD95DED9EEBBEDE2B77F5228AA8B1DE6759270485","Bytes":10002}}},"BASE-TREE":{"Id":"BASE-TREE","Mode":"tree","ExpectedAssertion":null,"Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87","Bytes":9953},"tree_validation":{"SHA256":"182F6E64EEACD3BC4B29180CD01E11913CCC0CFFCDDFCC432ED0A5FE34113D39","Bytes":11526}}},"MU-S01":{"Id":"MU-S01","Mode":"scalar","ExpectedAssertion":"S-ALL-CONTROLS.BYTES","Sources":{"scalar":{"SHA256":"331377B2D0678C91EEFABAD42A3D52494F2D5967ED72A4E6B50FD0F8C58043D9","Bytes":8234},"scalar_validation":{"SHA256":"1F473042AFE4455A194DD5DFD95DED9EEBBEDE2B77F5228AA8B1DE6759270485","Bytes":10002}}},"MU-S02":{"Id":"MU-S02","Mode":"scalar","ExpectedAssertion":"B-TRUE.BYTES","Sources":{"scalar":{"SHA256":"C9F9C737304298F8CA907FE9F70172D1860E856F8A2E2089E61AE0B5F16C4BC3","Bytes":8234},"scalar_validation":{"SHA256":"1F473042AFE4455A194DD5DFD95DED9EEBBEDE2B77F5228AA8B1DE6759270485","Bytes":10002}}},"MU-S03":{"Id":"MU-S03","Mode":"scalar","ExpectedAssertion":"P-DECODED-DUPLICATE-0","Sources":{"scalar":{"SHA256":"FAC557DD990C9E3976F809D7806F0E234059B6670081952F68973F1AB0748BA3","Bytes":8226},"scalar_validation":{"SHA256":"1F473042AFE4455A194DD5DFD95DED9EEBBEDE2B77F5228AA8B1DE6759270485","Bytes":10002}}},"MU-S04":{"Id":"MU-S04","Mode":"scalar","ExpectedAssertion":"E-UTF16-ORDER-REFUSED","Sources":{"scalar":{"SHA256":"78DF7AB168C383010E78EF447151D51C9E14071F5BA47711E7E60C0B9A487D9B","Bytes":8199},"scalar_validation":{"SHA256":"1F473042AFE4455A194DD5DFD95DED9EEBBEDE2B77F5228AA8B1DE6759270485","Bytes":10002}}},"MU-T01":{"Id":"MU-T01","Mode":"tree","ExpectedAssertion":"T-MIXED.BYTES","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"70FA9086D6DA1C5CA8A9BD834A9C1814D13018BC5C67E53C57D8DFC7583BC5C3","Bytes":9967},"tree_validation":{"SHA256":"182F6E64EEACD3BC4B29180CD01E11913CCC0CFFCDDFCC432ED0A5FE34113D39","Bytes":11526}}},"MU-T02":{"Id":"MU-T02","Mode":"tree","ExpectedAssertion":"N-SORT-TIE","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"4B34FB7D711D6E83A1ABC42192418F2D8D25C57B693B7C064E11BFE2260A3195","Bytes":9930},"tree_validation":{"SHA256":"182F6E64EEACD3BC4B29180CD01E11913CCC0CFFCDDFCC432ED0A5FE34113D39","Bytes":11526}}},"MU-T03":{"Id":"MU-T03","Mode":"tree","ExpectedAssertion":"T-EMPTY.BYTES","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"6F27BA03EB704C858A5F82F2752C75E79D17444DF7E78C7E4C98C28F63912783","Bytes":9951},"tree_validation":{"SHA256":"182F6E64EEACD3BC4B29180CD01E11913CCC0CFFCDDFCC432ED0A5FE34113D39","Bytes":11526}}},"MU-T04":{"Id":"MU-T04","Mode":"tree","ExpectedAssertion":"R-KEY-ORDER","Sources":{"scalar":{"SHA256":"532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4","Bytes":8234},"tree":{"SHA256":"E0A55AFCF1E10155F17900CB0521C12B0CE08117325B6C9A7DFF925E26CEEF60","Bytes":9942},"tree_validation":{"SHA256":"182F6E64EEACD3BC4B29180CD01E11913CCC0CFFCDDFCC432ED0A5FE34113D39","Bytes":11526}}}}''')
phase = "STARTUP"
module_name = "rdm_canon2_scalar_fixed_dependency_rev1"
owned = None
registered = False
cleanup = "NOT_REGISTERED"
record = {"RunOutcome": "UNEXPECTED_OR_INVALID", "ValidatorResult": None, "SubjectValidationPassed": False, "ObservedSources": []}
case = None
try:
    if not (sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode):
        raise RuntimeError("STARTUP_FLAGS")
    phase = "CLOSED_CASE_INPUT"
    payload = json.loads(sys.stdin.buffer.read().decode("utf-8", "strict"))
    if set(payload) != {"CaseId", "Sources"} or payload["CaseId"] not in CASES:
        raise RuntimeError("CASE_INPUT")
    case = CASES[payload["CaseId"]]
    record["CaseId"] = case["Id"]
    record["ExpectedAssertion"] = case["ExpectedAssertion"]
    if set(payload["Sources"]) != set(case["Sources"]) or module_name in sys.modules:
        raise RuntimeError("SOURCE_MEMBERS_OR_SLOT")
    loaded = {}
    for role, identity in case["Sources"].items():
        field = payload["Sources"][role]
        if set(field) != {"Base64"}:
            raise RuntimeError("SOURCE_FIELD")
        snapshot = base64.b64decode(field["Base64"], validate=True)
        digest = hashlib.sha256(snapshot).hexdigest().upper()
        if len(snapshot) != identity["Bytes"] or digest != identity["SHA256"]:
            raise RuntimeError("SOURCE_IDENTITY")
        record["ObservedSources"].append({"Role": role, "SHA256": digest, "Bytes": len(snapshot)})
        text = snapshot.decode("utf-8", "strict")
        phase = "STATIC_PARSE_" + role.upper()
        ast.parse(text, filename="<fixed-memory-case-" + role + ">")
        if role == "scalar" and case["Mode"] == "tree":
            owned = types.ModuleType(module_name)
            namespace = owned.__dict__
        else:
            namespace = {"__name__": "rdm_mutation_private_" + role}
        phase = "LOCAL_LOAD_" + role.upper()
        exec(compile(snapshot, "<fixed-memory-case-" + role + ">", "exec", dont_inherit=True, optimize=0), namespace)
        loaded[role] = namespace
        if role == "scalar" and case["Mode"] == "tree":
            if module_name in sys.modules:
                raise RuntimeError("DEPENDENCY_SLOT_CHANGED")
            sys.modules[module_name] = owned
            registered = True
    phase = "RUN_CLOSED_VALIDATOR"
    result = loaded[case["Mode"] + "_validation"]["run_synthetic_checks"](loaded[case["Mode"]])
    record["ValidatorResult"] = result
    record["SubjectValidationPassed"] = True
    if case["ExpectedAssertion"] is None:
        expected_count = 93 if case["Mode"] == "scalar" else 81
        expected_outcome = "LOCAL_SYNTHETIC_SCALAR_ENTRY_ENCODING_CHECKS_PASS" if case["Mode"] == "scalar" else "LOCAL_SYNTHETIC_STRUCTURAL_LAYOUT_CHECKS_PASS"
        if result["Summary"]["CheckCount"] != expected_count or result["Summary"]["VectorCount"] != 12 or result["Summary"]["Outcome"] != expected_outcome:
            raise RuntimeError("BASELINE_COUNTS_OR_OUTCOME")
        record["RunOutcome"] = "BASELINE_VALIDATOR_PASS"
    else:
        record["RunOutcome"] = "MUTANT_SURVIVED"
except BaseException as error:
    record["FailurePhase"] = phase
    record["FailureType"] = type(error).__name__
    identifier = error.args[0] if type(error) is AssertionError and len(error.args) == 1 and type(error.args[0]) is str else None
    if identifier is not None and re.fullmatch(r"[A-Z0-9_.-]{1,100}", identifier):
        record["FailureAssertion"] = identifier
    if case is not None and case["ExpectedAssertion"] is not None and phase == "RUN_CLOSED_VALIDATOR" and type(error) is AssertionError and identifier == case["ExpectedAssertion"]:
        record["RunOutcome"] = "EXPECTED_ASSERTION_OBSERVED"
finally:
    if registered:
        if sys.modules.get(module_name) is owned:
            del sys.modules[module_name]
            cleanup = "OWNED_ENTRY_REMOVED"
        else:
            cleanup = "OWNERSHIP_LOST_NOT_REMOVED"
record["DependencyCleanupState"] = cleanup
record["Runtime"] = {"Version": sys.version.split()[0], "Isolated": sys.flags.isolated, "NoSite": sys.flags.no_site, "DontWriteBytecode": sys.flags.dont_write_bytecode}
expected_cleanup = "OWNED_ENTRY_REMOVED" if case is not None and case["Mode"] == "tree" else "NOT_REGISTERED"
ok = record["RunOutcome"] in ("BASELINE_VALIDATOR_PASS", "EXPECTED_ASSERTION_OBSERVED") and cleanup == expected_cleanup
print(json.dumps(record, ensure_ascii=False, indent=2, allow_nan=False))
sys.exit(0 if ok else 1)
'@
function Invoke-ClosedProcess([object]$payload) {
  $start = [Diagnostics.ProcessStartInfo]::new($executable)
  $start.UseShellExecute = $false
  $start.CreateNoWindow = $true
  $start.RedirectStandardInput = $true
  $start.RedirectStandardOutput = $true
  $start.RedirectStandardError = $true
  $start.WorkingDirectory = $root
  $start.Environment.Clear()
  $systemDirectory = [Environment]::GetFolderPath([Environment+SpecialFolder]::Windows)
  $start.Environment['SystemRoot'] = $systemDirectory
  $start.Environment['WINDIR'] = $systemDirectory
  $start.Environment['PYTHONIOENCODING'] = 'utf-8'
  foreach ($arg in @('-I', '-S', '-B', '-c', $bootstrap)) { $start.ArgumentList.Add($arg) }
  $process = [Diagnostics.Process]::new()
  $process.StartInfo = $start
  $outBytes = [IO.MemoryStream]::new()
  $errBytes = [IO.MemoryStream]::new()
  $timer = [Diagnostics.Stopwatch]::StartNew()
  $timedOut = $false
  $started = $false
  try {
    if (-not $process.Start()) { throw 'LOCAL_PROCESS_START' }
    $started = $true
    $outTask = $process.StandardOutput.BaseStream.CopyToAsync($outBytes)
    $errTask = $process.StandardError.BaseStream.CopyToAsync($errBytes)
    $inputBytes = $utf8.GetBytes(($payload | ConvertTo-Json -Depth 5 -Compress))
    $writeTask = $process.StandardInput.BaseStream.WriteAsync($inputBytes, 0, $inputBytes.Length)
    if (-not $writeTask.Wait(5000)) { throw 'LOCAL_INPUT_WAIT' }
    $null = $writeTask.GetAwaiter().GetResult()
    $process.StandardInput.Close()
    if (-not $process.WaitForExit(30000)) {
      $timedOut = $true
      $process.Kill($true)
      if (-not $process.WaitForExit(5000)) { throw 'LOCAL_STOP_NOT_OBSERVED' }
    }
    if (-not [Threading.Tasks.Task]::WaitAll([Threading.Tasks.Task[]]@($outTask, $errTask), 5000)) { throw 'LOCAL_STREAM_WAIT' }
    $null = $outTask.GetAwaiter().GetResult()
    $null = $errTask.GetAwaiter().GetResult()
    $raw = $outBytes.ToArray()
    $stderr = $errBytes.ToArray()
    $exitCode = $process.ExitCode
    $elapsed = $timer.ElapsedMilliseconds
  } finally {
    if ($started -and -not $process.HasExited) { $process.Kill($true); $null = $process.WaitForExit(5000) }
    $process.Dispose()
    $outBytes.Dispose()
    $errBytes.Dispose()
  }
  return [pscustomobject]@{Raw=$raw;Stderr=$stderr;ExitCode=$exitCode;ElapsedMilliseconds=$elapsed;TimedOut=$timedOut}
}
$batchTimer = [Diagnostics.Stopwatch]::StartNew()
$runs = [Collections.Generic.List[object]]::new()
$batchError = $null
$baselinePasses = 0
$mutantsDetected = 0
foreach ($case in $cases) {
  try {
    if ($batchTimer.ElapsedMilliseconds -ge 60000) { throw 'LOGICAL_BATCH_DEADLINE' }
    $caseSources = [ordered]@{}
    foreach ($p in $case.Sources.PSObject.Properties) {
      $bytes = if ($mutants.ContainsKey($case.Id) -and $p.Name -ceq ($definitions | Where-Object Id -CEQ $case.Id).TargetRole) { $mutants[$case.Id] } else { $originals[$p.Name] }
      if ($bytes.Length -ne $p.Value.Bytes -or (Digest $bytes) -cne $p.Value.SHA256) { throw 'CASE_SOURCE_SNAPSHOT' }
      $caseSources[$p.Name] = @{Base64=[Convert]::ToBase64String($bytes)}
    }
    $capture = Invoke-ClosedProcess ([ordered]@{CaseId=$case.Id;Sources=$caseSources})
    $raw = $capture.Raw; $stderr = $capture.Stderr
    $parseFailure = $null; $record = $null
    try {
      if ($raw.Length -gt 262144 -or $stderr.Length -ne 0 -or $capture.TimedOut) { throw 'CASE_CAPTURE_BOUNDARY' }
      $record = ConvertFrom-Json -InputObject ($utf8.GetString($raw)) -Depth 40
    } catch { $parseFailure = $_.Exception.GetType().Name }
    $rawZip = Zip $raw; $errZip = Zip $stderr
    $isBaseline = $null -eq $case.ExpectedAssertion
    $expectedOutcome = if ($isBaseline) { 'BASELINE_VALIDATOR_PASS' } else { 'EXPECTED_ASSERTION_OBSERVED' }
    $expectedCleanup = if ($case.Mode -ceq 'tree') { 'OWNED_ENTRY_REMOVED' } else { 'NOT_REGISTERED' }
    $satisfied = $null -ne $record -and $capture.ExitCode -eq 0 -and $null -eq $parseFailure -and $record.CaseId -ceq $case.Id -and $record.RunOutcome -ceq $expectedOutcome -and $record.DependencyCleanupState -ceq $expectedCleanup
    if (-not $isBaseline) { $satisfied = $satisfied -and $record.SubjectValidationPassed -eq $false -and $record.FailureType -ceq 'AssertionError' -and $record.FailurePhase -ceq 'RUN_CLOSED_VALIDATOR' -and $record.FailureAssertion -ceq $case.ExpectedAssertion }
    $runs.Add([ordered]@{CaseId=$case.Id;Mode=$case.Mode;ExpectedAssertion=$case.ExpectedAssertion;ExpectedRunOutcome=$expectedOutcome;EvaluationSatisfied=$satisfied;ObservedExitCode=$capture.ExitCode;ObservedElapsedMilliseconds=$capture.ElapsedMilliseconds;WaitTimedOut=$capture.TimedOut;StrictUTF8OrJsonFailureType=$parseFailure;RawStdoutBytes=$raw.Length;RawStdoutSHA256=(Digest $raw);RawStdoutGZipBytes=$rawZip.Length;RawStdoutGZipBase64=[Convert]::ToBase64String($rawZip);RawStderrBytes=$stderr.Length;RawStderrSHA256=(Digest $stderr);RawStderrGZipBytes=$errZip.Length;RawStderrGZipBase64=[Convert]::ToBase64String($errZip);Record=$record})
    if (-not $satisfied) { throw 'CASE_EXPECTATION_NOT_MET' }
    if ($isBaseline) { $baselinePasses++ } else { $mutantsDetected++ }
    if ($batchTimer.ElapsedMilliseconds -ge 60000) { throw 'LOGICAL_BATCH_DEADLINE' }
  } catch { $batchError = [ordered]@{CaseId=$case.Id;Type=$_.Exception.GetType().Name;Code='BATCH_STOPPED_NO_AUTOMATIC_RETRY'}; break }
}
foreach ($s in $sources) {
  $after = [IO.File]::ReadAllBytes($root + $s.Path)
  if ($after.Length -ne $s.Bytes -or (Digest $after) -cne $s.SHA256) { throw 'ORIGINAL_SOURCE_CHANGED' }
}
$complete = $null -eq $batchError -and $runs.Count -eq 10 -and $baselinePasses -eq 2 -and $mutantsDetected -eq 8
$summary = [ordered]@{Outcome=if($complete){'LOCAL_PREDECLARED_MUTATION_SENSITIVITY_PASS'}else{'LOCAL_MUTATION_SENSITIVITY_INCOMPLETE'};BaselineRuns=$baselinePasses;PredeclaredMutants=8;MutantsDetectedAtExpectedAssertions=$mutantsDetected;ObservedProcesses=$runs.Count;OriginalBoundSourceModifications=0;FormalManifestGenerated=$false;SourceAdmission=$false;GeneralizedMutationScore='NOT CLAIMED';DSP004='OPEN / HOLD';B01='OPEN';B02='OPEN'}
$fullRecord = [ordered]@{Summary=$summary;FixedSources=$sources;CaseSpecifications=$cases;MutatedMemorySnapshots=$snapshots;Runs=$runs;BatchError=$batchError;ObservedBatchElapsedMilliseconds=$batchTimer.ElapsedMilliseconds;BootstrapUTF8SHA256=(Digest ($utf8.GetBytes($bootstrap)));PythonExecutableSHA256=$executableSha;BudgetQualification='PER-PROCESS 5000/30000/5000 MS; LOGICAL BATCH 60000 MS; POST-CAPTURE OUTPUT CHECKS; NOT PHYSICAL STOP/MEMORY PROOF'}
$text = ($fullRecord | ConvertTo-Json -Depth 50).Replace("`r`n","`n").TrimEnd([char]10)+[char]10
$bytes = $utf8.GetBytes($text); $compressed = Zip $bytes
[ordered]@{ArchiveVersion='RDM-CANON2-PREDECLARED-MUTATION-SENSITIVITY-REV1-OBSERVED';FullRecordUTF8Bytes=$bytes.Length;FullRecordSHA256=(Digest $bytes);GZipBytes=$compressed.Length;GZipBase64=[Convert]::ToBase64String($compressed);Summary=$summary}|ConvertTo-Json -Depth 10
