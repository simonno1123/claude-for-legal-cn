# DSP-004 OD04-A step 3: outer supervisor for one T0 dry run (REV1).
# Owner authorization 2026-10-31: three OD04-A steps, no asset acceptance, no Manifest, no formal run, DSP-004 not closed.
# It starts python.exe exactly once with probe_t0.py (inventory only; no harness or subject code).
# Order: lock every bound file -> hash through the held handle -> ACL and prefix checks -> T0 -> start child
#        -> two-side identity checks -> post checks -> release -> write one record (never overwrites).
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version 2

$ExpectedBoundListSha = 'F11E2920F63251135BAF9423B8DCFF3E9EDC0F57799291164568A112AB871627'
$Here   = $PSScriptRoot
$Bound  = Join-Path $Here 'bound_list.json'
$Out    = Join-Path $Here 't0_run_record.json'
$rec    = [ordered]@{ Kind = 'DSP004_OD04A_T0_DRY_RUN_RECORD_REV1'; Outcome = $null; BlockCode = $null; Checks = [ordered]@{} }
$held   = New-Object System.Collections.Generic.List[System.IO.FileStream]

function Write-Record {
    $json = $rec | ConvertTo-Json -Depth 8
    $fs = [IO.File]::Open($Out, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
    $b = (New-Object Text.UTF8Encoding($false)).GetBytes($json)
    $fs.Write($b, 0, $b.Length); $fs.Close()
}
function Release { foreach ($h in $held) { try { $h.Dispose() } catch {} }; $held.Clear() }
function Block([string]$code, $detail) {
    $rec.Outcome = 'BLOCKED'; $rec.BlockCode = $code; $rec.BlockDetail = $detail
    Release; Write-Record; Write-Host "BLOCKED $code"; exit 3
}
function Sha-Stream([IO.FileStream]$fs) {
    $alg = [Security.Cryptography.SHA256]::Create()
    $fs.Position = 0; $h = $alg.ComputeHash($fs); $fs.Position = 0
    return ([BitConverter]::ToString($h) -replace '-', '')
}
function Sha-File([string]$p) { return (Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash }
function Sddl-OwnerAccess([string]$p) { return ((Get-Acl -LiteralPath $p).Sddl -replace 'G:[^D]*(?=D:)', '') }

if (Test-Path -LiteralPath $Out) { Write-Host 'STOP RECORD_ALREADY_EXISTS'; exit 2 }

# Caller-side identity.
$me = Get-Process -Id $PID
$rec.Supervisor = [ordered]@{
    ScriptSha256 = Sha-File $PSCommandPath; HostImage = $me.Path; HostImageSha256 = Sha-File $me.Path
    Pid = $PID; PSVersion = $PSVersionTable.PSVersion.ToString(); StartedUtc = [DateTime]::UtcNow.ToString('o')
}

# Bound list identity.
if (-not (Test-Path -LiteralPath $Bound)) { Block 'BOUND_LIST_MISSING' $null }
$blBytes = [IO.File]::ReadAllBytes($Bound)   # read once; hash and parse the same bytes
$blSha = ([BitConverter]::ToString([Security.Cryptography.SHA256]::Create().ComputeHash($blBytes)) -replace '-', '')
$rec.BoundListSha256 = $blSha
if ($blSha -ne $ExpectedBoundListSha) { Block 'BOUND_LIST_SHA_MISMATCH' $blSha }
$bl = (New-Object Text.UTF8Encoding($false)).GetString($blBytes) | ConvertFrom-Json
$Base    = $bl.Base
$Runtime = Join-Path $Base $bl.RuntimeDir
$Prefix  = Join-Path $Base $bl.PrefixDir
$PyExe   = Join-Path $Runtime 'python.exe'
$Probe   = Join-Path $Here $bl.Probe.RelPath

# Build the full bound set.
$entries = New-Object System.Collections.Generic.List[object]
foreach ($f in $bl.RuntimeFiles) { $entries.Add([pscustomobject]@{ Kind = 'RUNTIME'; Path = (Join-Path $Base ($f.RelPath -replace '/', '\')); Bytes = [int64]$f.Bytes; Sha = $f.SHA256 }) }
foreach ($f in $bl.SystemDlls)   { $entries.Add([pscustomobject]@{ Kind = 'SYSTEM';  Path = $f.Path; Bytes = [int64]$f.Bytes; Sha = $f.SHA256 }) }
$entries.Add([pscustomobject]@{ Kind = 'PROBE'; Path = $Probe; Bytes = [int64]$bl.Probe.Bytes; Sha = $bl.Probe.SHA256 })

# 1. Lock: open every bound file allowing others to read only (no write, no delete, no rename).
foreach ($e in $entries) {
    try { $held.Add([IO.File]::Open($e.Path, [IO.FileMode]::Open, [IO.FileAccess]::Read, [IO.FileShare]::Read)) }
    catch { Block 'LOCK_FAILED' ([ordered]@{ Kind = $e.Kind; Path = $e.Path; Error = $_.Exception.GetType().Name }) }
}
$rec.Checks.LockedFiles = $held.Count

# 2. Hash through the held handles.
$bad = @()
for ($i = 0; $i -lt $entries.Count; $i++) {
    $e = $entries[$i]; $fs = $held[$i]
    if ($fs.Length -ne $e.Bytes -or (Sha-Stream $fs) -ne $e.Sha) { $bad += [ordered]@{ Kind = $e.Kind; Path = $e.Path } }
}
$rec.Checks.HashMismatches = @($bad).Count
if (@($bad).Count -gt 0) { Block 'HASH_MISMATCH' $bad }

# 3. No extra files in the runtime tree; prefix directory empty.
$onDisk = @(Get-ChildItem -LiteralPath $Base -Recurse -File -Force | ForEach-Object { $_.FullName.Substring($Base.Length + 1).Replace('\', '/') })
$listed = @($bl.RuntimeFiles | ForEach-Object { $_.RelPath })
$extra  = @($onDisk | Where-Object { $listed -notcontains $_ })
$rec.Checks.ExtraRuntimeFiles = $extra.Count
if ($extra.Count -gt 0) { Block 'EXTRA_RUNTIME_FILES' $extra }
$prefixCount = @(Get-ChildItem -LiteralPath $Prefix -Force).Count
$rec.Checks.PrefixEntriesBefore = $prefixCount
if ($prefixCount -ne 0) { Block 'PREFIX_NOT_EMPTY' $prefixCount }

# 4. ACL owner and access entries as set up in step 1.
$acl = [ordered]@{ Base = Sddl-OwnerAccess $Base; Runtime = Sddl-OwnerAccess $Runtime; Prefix = Sddl-OwnerAccess $Prefix; PythonExe = Sddl-OwnerAccess $PyExe }
$rec.Checks.AclBefore = $acl
foreach ($k in @('Base', 'Runtime', 'Prefix', 'PythonExe')) {
    if ($acl[$k] -ne $bl.ExpectedOwnerAccessSddl.$k) { Block 'ACL_MISMATCH' ([ordered]@{ Item = $k; Actual = $acl[$k] }) }
}

# 5. T0.
$rec.T0 = [ordered]@{ StopwatchTicks = [Diagnostics.Stopwatch]::GetTimestamp(); StopwatchFrequency = [Diagnostics.Stopwatch]::Frequency; Utc = [DateTime]::UtcNow.ToString('o') }

# 6. Start the child once, fixed arguments, no shell.
$nb = New-Object byte[] 32
[Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($nb)
$nonce = ([BitConverter]::ToString($nb) -replace '-', '')
$args6 = '-I -S -B -X "pycache_prefix=' + $Prefix + '" "' + $Probe + '"'
$psi = New-Object Diagnostics.ProcessStartInfo
$psi.FileName = $PyExe; $psi.Arguments = $args6; $psi.WorkingDirectory = $Runtime
$psi.UseShellExecute = $false; $psi.CreateNoWindow = $true
$psi.RedirectStandardInput = $true; $psi.RedirectStandardOutput = $true; $psi.RedirectStandardError = $true
$rec.Child = [ordered]@{ Arguments = $args6 }
$p = [Diagnostics.Process]::Start($psi)
$childPid = $p.Id
$cim = Get-CimInstance Win32_Process -Filter "ProcessId=$childPid"
$rec.Child.Pid = $childPid
$rec.Child.SystemImagePath = $(if ($cim) { $cim.ExecutablePath } else { $null })
$rec.Child.SystemParentPid = $(if ($cim) { [int]$cim.ParentProcessId } else { $null })
$outTask = $p.StandardOutput.ReadToEndAsync(); $errTask = $p.StandardError.ReadToEndAsync()
$p.StandardInput.WriteLine($nonce); $p.StandardInput.Close()
if (-not $p.WaitForExit(60000)) { try { $p.Kill() } catch {}; Block 'CHILD_TIMEOUT' $childPid }
$p.WaitForExit()
$stdout = $outTask.Result; $stderr = $errTask.Result
$rec.Child.ExitCode = $p.ExitCode
$rec.Child.StderrBytes = $stderr.Length
$rec.Child.Report = $null
try { $rep = $stdout | ConvertFrom-Json } catch { $rep = $null }
$rec.Child.Report = $rep

# 7. Two-side identity and child-report checks.
$c = [ordered]@{}
$c.ImagePathIsLockedPython = ($rec.Child.SystemImagePath -ne $null) -and ($rec.Child.SystemImagePath -ieq $PyExe)
$c.SystemParentIsSupervisor = ($rec.Child.SystemParentPid -eq $PID)
$c.ExitCodeZero = ($p.ExitCode -eq 0)
$c.ReportParsed = ($rep -ne $null)
if ($rep -ne $null) {
    $c.NonceEchoed = ($rep.Nonce -ceq $nonce)
    $c.ReportPidMatches = ([int]$rep.Pid -eq $childPid)
    $c.ReportPpidIsSupervisor = ([int]$rep.Ppid -eq $PID)
    $c.ReportExecutableIsLockedPython = ($rep.Executable -ieq $PyExe)
    $c.IsolationFlags = ($rep.Flags.isolated -eq 1 -and $rep.Flags.no_site -eq 1 -and $rep.Flags.dont_write_bytecode -eq 1)
    $c.PycachePrefixIsEmptyDir = ($rep.PycachePrefix -ieq $Prefix)
    $c.NoCachedBytecodeUsed = (@($rep.Modules | Where-Object { $_.CachedExists }).Count -eq 0)
    $boundPaths = @($entries | ForEach-Object { $_.Path.ToLowerInvariant() })
    $srcOut = @($rep.Modules | Where-Object { $_.Loader -eq 'SourceFileLoader' -and $_.Name -ne '__main__' -and ($boundPaths -notcontains ([string]$_.Origin).ToLowerInvariant()) } | ForEach-Object { $_.Origin })
    $natOut = @($rep.Natives | Where-Object { $boundPaths -notcontains ([string]$_).ToLowerInvariant() })
    $c.SourceModulesAllBound = ($srcOut.Count -eq 0); $rec.Child.UnboundSourceModules = $srcOut
    $c.NativeModulesAllBound = ($natOut.Count -eq 0); $rec.Child.UnboundNativeModules = $natOut
}

# 8. Post checks while still locked.
$c.PrefixStillEmpty = (@(Get-ChildItem -LiteralPath $Prefix -Force).Count -eq 0)
$aclAfter = [ordered]@{ Base = Sddl-OwnerAccess $Base; Runtime = Sddl-OwnerAccess $Runtime; Prefix = Sddl-OwnerAccess $Prefix; PythonExe = Sddl-OwnerAccess $PyExe }
$c.AclUnchanged = (($aclAfter.Values -join '|') -eq ($acl.Values -join '|'))
$rec.Checks.Run = $c
Release
$rec.Checks.ReleasedUtc = [DateTime]::UtcNow.ToString('o')

$allTrue = -not (@($c.Values | Where-Object { $_ -ne $true }).Count -gt 0)
$rec.Outcome = $(if ($allTrue) { 'PASS_T0_DRY_RUN' } else { 'CHILD_CHECK_FAILED' })
Write-Record
Write-Host "$($rec.Outcome) record=$Out"
exit $(if ($allTrue) { 0 } else { 4 })
