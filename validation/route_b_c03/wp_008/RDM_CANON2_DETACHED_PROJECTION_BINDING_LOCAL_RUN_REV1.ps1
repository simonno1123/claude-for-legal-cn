$ErrorActionPreference = 'Stop'
$utf8 = [Text.UTF8Encoding]::new($false, $true)
[Console]::OutputEncoding = $utf8
$root = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/'
$executable = 'C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
$executableSha = 'B847BB9F4E48C19F585C8BF7D8B355F3F8C6D2125717ECE9C9D7E16FB9F09DE8'
$sources = @(
  @{Role='scalar';Path='validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_CANDIDATE_REV1.py';SHA256='532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4';Bytes=8234},
  @{Role='tree';Path='validation/route_b_c03/wp_008/RDM_CANON2_STRUCTURAL_LAYOUT_CANDIDATE_REV1.py';SHA256='F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87';Bytes=9953},
  @{Role='binding';Path='validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_CANDIDATE_REV1.py';SHA256='32535D3E4800E39E8AAF510166AD2AF04E0436D39E7C0BAD528B329D24E66821';Bytes=5799},
  @{Role='validation';Path='validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_VALIDATION_REV1.py';SHA256='944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476';Bytes=13142}
)
function Digest([byte[]]$Bytes) { [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($Bytes)) }
function Compress([byte[]]$Bytes) {
  $output = [IO.MemoryStream]::new()
  $gzip = [IO.Compression.GZipStream]::new($output, [IO.Compression.CompressionMode]::Compress, $true)
  try { $gzip.Write($Bytes, 0, $Bytes.Length) } finally { $gzip.Dispose() }
  $result = $output.ToArray()
  $output.Dispose()
  return ,$result
}
$payload = [ordered]@{}
foreach ($source in $sources) {
  $bytes = [IO.File]::ReadAllBytes($root + $source.Path)
  if ($bytes.Length -ne $source.Bytes -or (Digest $bytes) -cne $source.SHA256) { throw 'NEW_SOURCE_IDENTITY_MISMATCH' }
  $null = $utf8.GetString($bytes)
  $payload[$source.Role] = [ordered]@{SHA256=$source.SHA256;Base64=[Convert]::ToBase64String($bytes)}
}
if ((Digest ([IO.File]::ReadAllBytes($executable))) -cne $executableSha) { throw 'PYTHON_EXECUTABLE_IDENTITY' }
$bootstrap = @'
import ast, base64, hashlib, json, re, sys, types
sys.stdout.reconfigure(encoding="utf-8", errors="strict", newline="\n")
phase = "STARTUP"
names = {"scalar": "rdm_canon2_scalar_fixed_dependency_rev1", "tree": "rdm_canon2_tree_fixed_dependency_rev1"}
owned = {}
cleanup = {}
record = {"Outcome": "LOCAL_SYNTHETIC_DETACHED_CONSISTENCY_INCOMPLETE", "Result": None}
try:
    if not (sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode):
        raise RuntimeError("STARTUP_FLAGS")
    phase = "FIXED_SOURCE_SNAPSHOTS"
    supplied = json.loads(sys.stdin.buffer.read().decode("utf-8", "strict"))
    expected = {
        "scalar": ("532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4", 8234),
        "tree": ("F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87", 9953),
        "binding": ("32535D3E4800E39E8AAF510166AD2AF04E0436D39E7C0BAD528B329D24E66821", 5799),
        "validation": ("944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476", 13142),
    }
    if set(supplied) != set(expected) or any(name in sys.modules for name in names.values()):
        raise RuntimeError("SOURCE_OR_DEPENDENCY_SLOT")
    loaded = {}
    for role, (digest, length) in expected.items():
        item = supplied[role]
        if set(item) != {"SHA256", "Base64"}:
            raise RuntimeError("SOURCE_FIELDS")
        snapshot = base64.b64decode(item["Base64"], validate=True)
        if len(snapshot) != length or item["SHA256"] != digest or hashlib.sha256(snapshot).hexdigest().upper() != digest:
            raise RuntimeError("SOURCE_BINDING")
        text = snapshot.decode("utf-8", "strict")
        phase = "STATIC_PARSE_" + role.upper()
        ast.parse(text, filename="<fixed-synthetic-" + role + ">")
        if role in names:
            module = types.ModuleType(names[role])
            namespace = module.__dict__
        else:
            namespace = {"__name__": "rdm_canon2_detached_synthetic_" + role}
        phase = "LOCAL_LOAD_" + role.upper()
        exec(compile(snapshot, "<fixed-synthetic-" + role + ">", "exec", dont_inherit=True, optimize=0), namespace)
        loaded[role] = namespace
        if role in names:
            name = names[role]
            if name in sys.modules:
                raise RuntimeError("DEPENDENCY_SLOT_CHANGED")
            sys.modules[name] = module
            owned[name] = module
    phase = "LOCAL_SYNTHETIC_VALIDATION"
    result = loaded["validation"]["run_synthetic_checks"](loaded["binding"])
    if result["Summary"]["CheckCount"] != 106 or result["Summary"]["VectorCount"] != 3:
        raise RuntimeError("FIXED_EXPECTED_COUNTS")
    record["Result"] = result
except BaseException as error:
    record["FailurePhase"] = phase
    record["FailureType"] = type(error).__name__
    if type(error) is AssertionError and len(error.args) == 1 and type(error.args[0]) is str and re.fullmatch(r"[A-Z0-9_.-]{1,100}", error.args[0]):
        record["FailureCheck"] = error.args[0]
finally:
    for role, name in reversed(tuple(names.items())):
        if name not in owned:
            cleanup[role] = "NOT_REGISTERED"
        elif sys.modules.get(name) is owned[name]:
            del sys.modules[name]
            cleanup[role] = "OWNED_ENTRY_REMOVED"
        else:
            cleanup[role] = "OWNERSHIP_LOST_NOT_REMOVED"
if record["Result"] is not None and all(state == "OWNED_ENTRY_REMOVED" for state in cleanup.values()) and "FailureType" not in record:
    record["Outcome"] = "LOCAL_SYNTHETIC_DETACHED_CONSISTENCY_OBSERVED_ONLY"
record["DependencyCleanupState"] = cleanup
record["Runtime"] = {
    "Version": sys.version.split()[0], "Isolated": sys.flags.isolated,
    "NoSite": sys.flags.no_site, "DontWriteBytecode": sys.flags.dont_write_bytecode,
}
print(json.dumps(record, ensure_ascii=False, indent=2, allow_nan=False))
sys.exit(0 if record["Outcome"] == "LOCAL_SYNTHETIC_DETACHED_CONSISTENCY_OBSERVED_ONLY" else 1)
'@
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
# This private collector checks output budgets after capture, not as an online
# production memory guard. Its waits are observations, not physical-stop proof.
$parseFailure = $null
$record = $null
$full = [byte[]]::new(0)
try {
  if ($raw.Length -gt 262144 -or $stderr.Length -ne 0 -or $timedOut) { throw 'LOCAL_CAPTURE_BOUNDARY' }
  $text = $utf8.GetString($raw)
  $record = ConvertFrom-Json -InputObject $text -Depth 35
  $full = $utf8.GetBytes(($text.Replace("`r`n", "`n").TrimEnd([char]10) + [char]10))
} catch { $parseFailure = $_.Exception.GetType().Name }
$rawZip = Compress $raw
$fullZip = Compress $full
foreach ($source in $sources) {
  $after = [IO.File]::ReadAllBytes($root + $source.Path)
  if ($after.Length -ne $source.Bytes -or (Digest $after) -cne $source.SHA256) { throw 'NEW_SOURCE_CHANGED' }
}
[ordered]@{
  ArchiveVersion='RDM-CANON2-DETACHED-PROJECTION-BINDING-REV1-OBSERVED'
  SourceIdentities=$sources
  PythonExecutableSHA256=$executableSha
  BootstrapUTF8SHA256=(Digest ($utf8.GetBytes($bootstrap)))
  WaitBudgetMilliseconds=30000
  InputWaitBudgetMilliseconds=5000
  StreamWaitBudgetMilliseconds=5000
  WaitTimedOut=$timedOut
  ObservedElapsedMilliseconds=$elapsed
  ObservedExitCode=$exitCode
  ObservedStderrBytes=$stderr.Length
  StrictUTF8OrJsonFailureType=$parseFailure
  RawStdoutBytes=$raw.Length
  RawStdoutSHA256=(Digest $raw)
  RawStdoutGZipBytes=$rawZip.Length
  RawStdoutGZipBase64=[Convert]::ToBase64String($rawZip)
  FullRecordUTF8Bytes=$full.Length
  FullRecordSHA256=(Digest $full)
  GZipBytes=$fullZip.Length
  GZipBase64=[Convert]::ToBase64String($fullZip)
  Summary=if ($null -eq $record) { $null } else { $record.Result.Summary }
  FailurePhase=if ($null -eq $record) { $null } else { $record.FailurePhase }
  FailureType=if ($null -eq $record) { $null } else { $record.FailureType }
  FailureCheck=if ($null -eq $record) { $null } else { $record.FailureCheck }
  Scope='LOCAL SYNTHETIC TWO-LAYER CONSISTENCY ONLY; NO SOURCE OR AUTHORITY VERIFICATION'
} | ConvertTo-Json -Depth 10
