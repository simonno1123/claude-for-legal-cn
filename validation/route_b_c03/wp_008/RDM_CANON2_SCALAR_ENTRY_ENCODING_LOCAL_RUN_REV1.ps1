$ErrorActionPreference = 'Stop'
$utf8 = [Text.UTF8Encoding]::new($false, $true)
[Console]::OutputEncoding = $utf8
$root = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/'
$executable = 'C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
$executableSha = 'B847BB9F4E48C19F585C8BF7D8B355F3F8C6D2125717ECE9C9D7E16FB9F09DE8'
$sources = @(
  @{Role='candidate';Path='validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_CANDIDATE_REV1.py';SHA256='532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4';Bytes=8234},
  @{Role='validation';Path='validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_VALIDATION_REV1.py';SHA256='1F473042AFE4455A194DD5DFD95DED9EEBBEDE2B77F5228AA8B1DE6759270485';Bytes=10002}
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
import ast, base64, hashlib, json, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="strict", newline="\n")
phase = "STARTUP"
record = {"Outcome": "LOCAL_SYNTHETIC_ENCODING_INCOMPLETE", "Result": None}
try:
    if not (sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode):
        raise RuntimeError("STARTUP_FLAGS")
    phase = "FIXED_SOURCE_SNAPSHOTS"
    supplied = json.loads(sys.stdin.buffer.read().decode("utf-8", "strict"))
    expected = {
        "candidate": "532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4",
        "validation": "1F473042AFE4455A194DD5DFD95DED9EEBBEDE2B77F5228AA8B1DE6759270485",
    }
    if set(supplied) != set(expected):
        raise RuntimeError("SOURCE_MEMBERS")
    loaded = {}
    for role, digest in expected.items():
        item = supplied[role]
        snapshot = base64.b64decode(item["Base64"], validate=True)
        if item["SHA256"] != digest or hashlib.sha256(snapshot).hexdigest().upper() != digest:
            raise RuntimeError("SOURCE_BINDING")
        text = snapshot.decode("utf-8", "strict")
        phase = "STATIC_PARSE_" + role.upper()
        ast.parse(text, filename="<fixed-synthetic-" + role + ">")
        namespace = {"__name__": "rdm_canon2_fixed_synthetic_" + role}
        phase = "LOCAL_LOAD_" + role.upper()
        exec(compile(snapshot, "<fixed-synthetic-" + role + ">", "exec", dont_inherit=True, optimize=0), namespace)
        loaded[role] = namespace
    phase = "LOCAL_SYNTHETIC_VALIDATION"
    result = loaded["validation"]["run_synthetic_checks"](loaded["candidate"])
    if result["Summary"]["CheckCount"] != 93 or result["Summary"]["VectorCount"] != 12:
        raise RuntimeError("FIXED_EXPECTED_COUNTS")
    record = {"Outcome": "LOCAL_SYNTHETIC_ENCODING_OBSERVED_ONLY", "Result": result}
except BaseException as error:
    record["FailurePhase"] = phase
    record["FailureType"] = type(error).__name__
    if type(error) is AssertionError and len(error.args) == 1 and type(error.args[0]) is str and re.fullmatch(r"[A-Z0-9_.-]{1,100}", error.args[0]):
        record["FailureCheck"] = error.args[0]
record["Runtime"] = {
    "Version": sys.version.split()[0], "Isolated": sys.flags.isolated,
    "NoSite": sys.flags.no_site, "DontWriteBytecode": sys.flags.dont_write_bytecode,
}
print(json.dumps(record, ensure_ascii=False, indent=2, allow_nan=False))
sys.exit(0 if record["Outcome"] == "LOCAL_SYNTHETIC_ENCODING_OBSERVED_ONLY" else 1)
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
  ArchiveVersion='RDM-CANON2-SCALAR-ENTRY-REV1-OBSERVED'
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
  Scope='LOCAL SYNTHETIC SCALAR/ENTRY PROJECTION ONLY; NO MANIFEST OR SOURCE ADMISSION'
} | ConvertTo-Json -Depth 10
