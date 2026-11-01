# DSP-004 OD04-A T0 dry run, supervisor v2.
# Addresses independent review IR-01..IR-14 of v1. Runs only from the admin-protected directory
# C:\Program Files\DSP004Runtime\supervisor_v2, started by run_v2.cmd with an absolute powershell.exe path.
# Order: harden module loading -> host/launcher/token/hijack checks -> lock everything -> hash through handles
#   -> tree, per-item ACL, Authenticode, OpenSSL config checks -> T0 -> start child (fixed argv, minimal env, no stdin data)
#   -> outside-in identity and module enumeration -> post checks while locked -> release -> write one record.
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version 2

# 0. Module loading: no autoload, core modules only from $PSHOME, module-qualified calls.
$PSModuleAutoLoadingPreference = 'None'
$origPSModulePath = $env:PSModulePath
$env:PSModulePath = [IO.Path]::Combine($PSHOME, 'Modules')
Import-Module ([IO.Path]::Combine($PSHOME, 'Modules\Microsoft.PowerShell.Utility\Microsoft.PowerShell.Utility.psd1'))
Import-Module ([IO.Path]::Combine($PSHOME, 'Modules\Microsoft.PowerShell.Security\Microsoft.PowerShell.Security.psd1'))
Microsoft.PowerShell.Utility\Add-Type -AssemblyName System.Management

$ExpectedBoundSha = '8FE6ECF646F991D585EBD50D58BFDA5DEB88485615C6261673F8B1D180C2801E'
$Base     = 'C:\Program Files\DSP004Runtime'
$SupDir   = [IO.Path]::Combine($Base, 'supervisor_v2')
$Runtime  = [IO.Path]::Combine($Base, 'Python312')
$Prefix   = [IO.Path]::Combine($Base, 'empty_pycache_prefix')
$PyExe    = [IO.Path]::Combine($Runtime, 'python.exe')
$Probe    = [IO.Path]::Combine($SupDir, 'probe_v2.py')
$BoundP   = [IO.Path]::Combine($SupDir, 'bound_list_v2.json')
$SysDir   = [Environment]::GetFolderPath('System')
$WinDir   = [Environment]::GetFolderPath('Windows')
$OutDir   = [IO.Path]::Combine([Environment]::GetFolderPath('MyDocuments'), 'dsp004-probe')
$Out      = [IO.Path]::Combine($OutDir, 'v2_run_record.json')
$SupFiles = @('supervisor_v2.ps1', 'probe_v2.py', 'bound_list_v2.json', 'run_v2.cmd')

$rec  = [ordered]@{ Kind = 'DSP004_OD04A_T0_DRY_RUN_RECORD_V2'; Outcome = $null; BlockCode = $null; BlockDetail = $null; Pre = [ordered]@{}; Checks = [ordered]@{}; Values = [ordered]@{} }
$held = New-Object System.Collections.Generic.List[System.IO.FileStream]

function Say([string]$s) { [Console]::WriteLine($s) }
function Write-Record {
    $json = Microsoft.PowerShell.Utility\ConvertTo-Json -InputObject $rec -Depth 10
    $fs = [IO.File]::Open($Out, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
    $b = (New-Object Text.UTF8Encoding($false)).GetBytes($json)
    $fs.Write($b, 0, $b.Length); $fs.Close()
}
function Release { foreach ($h in $held) { try { $h.Dispose() } catch {} }; $held.Clear() }
$script:blocking = $false
function Block([string]$code, $detail) {
    if ($script:blocking) { exit 5 }
    $script:blocking = $true
    $rec.Outcome = 'BLOCKED'; $rec.BlockCode = $code; $rec.BlockDetail = $detail
    Release; Write-Record; Say "BLOCKED $code"; exit 3
}
function Sha-Bytes([byte[]]$b) { return ([BitConverter]::ToString([Security.Cryptography.SHA256]::Create().ComputeHash($b)) -replace '-', '') }
function Sha-Stream([IO.FileStream]$fs) {
    $fs.Position = 0; $h = [Security.Cryptography.SHA256]::Create().ComputeHash($fs); $fs.Position = 0
    return ([BitConverter]::ToString($h) -replace '-', '')
}
function Sddl-OA([string]$p) { return ((Microsoft.PowerShell.Security\Get-Acl -LiteralPath $p).Sddl -replace 'G:[^D]*(?=D:)', '') }
function ProcInfo([int]$id) {
    $s = New-Object System.Management.ManagementObjectSearcher("SELECT ProcessId,ParentProcessId,ExecutablePath,CreationDate,CommandLine FROM Win32_Process WHERE ProcessId=$id")
    $r = @($s.Get()); if ($r.Count -eq 0) { return $null }
    $o = $r[0]
    $created = $null
    if ($o['CreationDate']) { $created = [Management.ManagementDateTimeConverter]::ToDateTime([string]$o['CreationDate']).ToUniversalTime().ToString('o') }
    return [ordered]@{ Pid = [int]$o['ProcessId']; Ppid = [int]$o['ParentProcessId']; Path = [string]$o['ExecutablePath']; CreatedUtc = $created; CommandLine = [string]$o['CommandLine'] }
}
function RegValue([Microsoft.Win32.RegistryKey]$root, [string]$sub, [string]$name) {
    $k = $root.OpenSubKey($sub); if ($k -eq $null) { return $null }
    try { return $k.GetValue($name) } finally { $k.Close() }
}
function RegKeyExists([Microsoft.Win32.RegistryKey]$root, [string]$sub) { $k = $root.OpenSubKey($sub); if ($k -eq $null) { return $false }; $k.Close(); return $true }

[void][IO.Directory]::CreateDirectory($OutDir)
if ([IO.File]::Exists($Out)) { Say 'STOP RECORD_ALREADY_EXISTS'; exit 2 }
trap { $msg = $_.Exception.GetType().FullName + ': ' + $_.Exception.Message; Block 'UNEXPECTED_EXCEPTION' $msg }
$rec.Values.StartedUtc = [DateTime]::UtcNow.ToString('o')
$rec.Values.OriginalPSModulePathEntries = @(([string]$origPSModulePath).Split(';') | Where-Object { $_ -ne '' }).Count

# 1. Host, script location, launcher.
$me = [Diagnostics.Process]::GetCurrentProcess()
$hostPath = $me.MainModule.FileName
$expHost = [IO.Path]::Combine($SysDir, 'WindowsPowerShell\v1.0\powershell.exe')
$rec.Values.HostPath = $hostPath; $rec.Values.PSHOME = $PSHOME; $rec.Values.PSVersion = $PSVersionTable.PSVersion.ToString(); $rec.Values.SupervisorPid = $PID
if ($hostPath -ine $expHost) { Block 'HOST_NOT_SYSTEM_POWERSHELL' $hostPath }
if ($PSHOME -ine [IO.Path]::GetDirectoryName($expHost)) { Block 'PSHOME_UNEXPECTED' $PSHOME }
if ($PSCommandPath -ine [IO.Path]::Combine($SupDir, 'supervisor_v2.ps1')) { Block 'SCRIPT_NOT_IN_PROTECTED_DIR' $PSCommandPath }
$parent = ProcInfo ((ProcInfo $PID).Ppid)
$rec.Values.Parent = $parent
if ($parent -eq $null -or $parent.Path -ine [IO.Path]::Combine($SysDir, 'cmd.exe')) { Block 'PARENT_NOT_SYSTEM_CMD' $parent }
if ($parent.CommandLine.IndexOf([IO.Path]::Combine($SupDir, 'run_v2.cmd'), [StringComparison]::OrdinalIgnoreCase) -lt 0) { Block 'PARENT_NOT_RUN_V2_CMD' $parent.CommandLine }
$rec.Values.SupervisorCommandLine = (ProcInfo $PID).CommandLine
$rec.Values.HostSha256 = Sha-Bytes ([IO.File]::ReadAllBytes($hostPath))
$cv = 'SOFTWARE\Microsoft\Windows NT\CurrentVersion'
$rec.Values.OsBuild = [ordered]@{ CurrentBuild = RegValue ([Microsoft.Win32.Registry]::LocalMachine) $cv 'CurrentBuild'; UBR = RegValue ([Microsoft.Win32.Registry]::LocalMachine) $cv 'UBR'; DisplayVersion = RegValue ([Microsoft.Win32.Registry]::LocalMachine) $cv 'DisplayVersion' }
# CLR / .NET injection variables and modules loaded into this host.
$clrVars = @([Environment]::GetEnvironmentVariables().Keys | ForEach-Object { [string]$_ } | Where-Object { $_ -match '^(COR_ENABLE_PROFILING|COR_PROFILER(_PATH(_32|_64)?)?|COMPLUS_.*|DOTNET_.*|APPDOMAIN_MANAGER_.*)$' })
$rec.Values.ClrInjectionVariableNames = $clrVars
if ($clrVars.Count -gt 0) { Block 'CLR_INJECTION_VARIABLES_PRESENT' $clrVars }
$me.Refresh()
$hostMods = @($me.Modules | ForEach-Object { $_.FileName })
$foreign = @($hostMods | Where-Object { -not $_.StartsWith($WinDir + '\', [StringComparison]::OrdinalIgnoreCase) })
$rec.Values.HostModuleCount = $hostMods.Count
# Modules outside the Windows folder (for example the Defender AMSI provider) must be validly Microsoft-signed.
$foreignBad = @($foreign | Where-Object { $fsig = Microsoft.PowerShell.Security\Get-AuthenticodeSignature -LiteralPath $_; -not ($fsig.Status -eq 'Valid' -and $fsig.SignerCertificate -ne $null -and $fsig.SignerCertificate.Subject -match '(^|, )O=Microsoft Corporation(,|$)') })
$rec.Values.HostModulesOutsideWindows = $foreign
if ($foreignBad.Count -gt 0) { Block 'HOST_MODULE_UNTRUSTED' $foreignBad }

# 2. Token and UAC.
$isAdminToken = (New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
$groups = & ([IO.Path]::Combine($SysDir, 'whoami.exe')) /groups /fo csv /nh
$medium = @($groups | Where-Object { $_ -match '"S-1-16-8192"' }).Count -gt 0
$high   = @($groups | Where-Object { $_ -match '"S-1-16-12288"|"S-1-16-16384"' }).Count -gt 0
$lua    = RegValue ([Microsoft.Win32.Registry]::LocalMachine) 'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' 'EnableLUA'
$rec.Values.Token = [ordered]@{ AdminRoleActive = $isAdminToken; MediumIntegrity = $medium; HighOrSystemIntegrity = $high; EnableLUA = $lua }
if ($isAdminToken -or $high -or -not $medium) { Block 'TOKEN_NOT_FILTERED_MEDIUM' $rec.Values.Token }
if ($lua -ne 1) { Block 'UAC_DISABLED' $lua }

# 3. User-controlled hijack surfaces for cmd.exe and the .cmd association.
$hkcuAuto = RegValue ([Microsoft.Win32.Registry]::CurrentUser) 'Software\Microsoft\Command Processor' 'AutoRun'
$hklmAuto = RegValue ([Microsoft.Win32.Registry]::LocalMachine) 'Software\Microsoft\Command Processor' 'AutoRun'
$cmdOverride = (RegKeyExists ([Microsoft.Win32.Registry]::CurrentUser) 'Software\Classes\.cmd') -or (RegKeyExists ([Microsoft.Win32.Registry]::CurrentUser) 'Software\Classes\cmdfile')
$rec.Values.Hijack = [ordered]@{ HKCUAutoRunPresent = -not [string]::IsNullOrEmpty([string]$hkcuAuto); HKLMAutoRunPresent = -not [string]::IsNullOrEmpty([string]$hklmAuto); HKCUCmdAssociationOverride = $cmdOverride }
if ($rec.Values.Hijack.HKCUAutoRunPresent -or $rec.Values.Hijack.HKLMAutoRunPresent -or $cmdOverride) { Block 'LAUNCH_HIJACK_SURFACE_PRESENT' $rec.Values.Hijack }

# 4. Lock: bound list first, read it through the held handle.
try { $bh = [IO.File]::Open($BoundP, [IO.FileMode]::Open, [IO.FileAccess]::Read, [IO.FileShare]::Read); $held.Add($bh) } catch { Block 'LOCK_FAILED' $BoundP }
$bbytes = New-Object byte[] $bh.Length; [void]$bh.Read($bbytes, 0, $bbytes.Length); $bh.Position = 0
$bsha = Sha-Bytes $bbytes
$rec.Values.BoundListSha256 = $bsha
if ($bsha -ne $ExpectedBoundSha) { Block 'BOUND_LIST_SHA_MISMATCH' $bsha }
$bl = Microsoft.PowerShell.Utility\ConvertFrom-Json -InputObject ((New-Object Text.UTF8Encoding($false)).GetString($bbytes))

$entries = New-Object System.Collections.Generic.List[object]
foreach ($f in $bl.RuntimeFiles) { $entries.Add([pscustomobject]@{ Kind = 'RUNTIME'; Rel = $f.RelPath; Path = [IO.Path]::Combine($Base, ($f.RelPath -replace '/', '\')); Bytes = [int64]$f.Bytes; Sha = $f.SHA256; SignerOrg = $f.SignerOrg; Thumb = $f.SignerThumbprint }) }
foreach ($f in $bl.SupervisorFiles) { $entries.Add([pscustomobject]@{ Kind = 'SUPERVISOR'; Rel = $f.RelPath; Path = [IO.Path]::Combine($Base, ($f.RelPath -replace '/', '\')); Bytes = [int64]$f.Bytes; Sha = $f.SHA256; SignerOrg = $null; Thumb = $null }) }
foreach ($f in $bl.SystemDlls) { $entries.Add([pscustomobject]@{ Kind = 'SYSTEM'; Rel = $null; Path = $f.Path; Bytes = [int64]$f.Bytes; Sha = $f.SHA256; SignerOrg = 'Microsoft Corporation'; Thumb = $null }) }
$selfPath = [IO.Path]::Combine($SupDir, 'supervisor_v2.ps1')
$entries.Add([pscustomobject]@{ Kind = 'SELF'; Rel = 'supervisor_v2/supervisor_v2.ps1'; Path = $selfPath; Bytes = -1; Sha = $null; SignerOrg = $null; Thumb = $null })

foreach ($e in $entries) {
    try { $held.Add([IO.File]::Open($e.Path, [IO.FileMode]::Open, [IO.FileAccess]::Read, [IO.FileShare]::Read)) }
    catch { Block 'LOCK_FAILED' ([ordered]@{ Kind = $e.Kind; Path = $e.Path; Error = $_.Exception.GetType().Name }) }
}
$rec.Checks.LockedFiles = $held.Count

# 5. Hash through held handles (index 0 is the bound list).
$bad = @(); $selfSha = $null
for ($i = 0; $i -lt $entries.Count; $i++) {
    $e = $entries[$i]; $fs = $held[$i + 1]; $h = Sha-Stream $fs
    if ($e.Kind -eq 'SELF') { $selfSha = $h; continue }
    if ($fs.Length -ne $e.Bytes -or $h -ne $e.Sha) { $bad += [ordered]@{ Kind = $e.Kind; Path = $e.Path } }
}
$rec.Values.SupervisorSha256 = $selfSha
$rec.Checks.HashMismatches = @($bad).Count
if (@($bad).Count -gt 0) { Block 'HASH_MISMATCH' $bad }

# 6. Tree: exact file set, no bytecode/zip/path-config files, empty prefix.
function Tree-Scan {
    $files = @([IO.Directory]::EnumerateFiles($Base, '*', [IO.SearchOption]::AllDirectories) | ForEach-Object { $_.Substring($Base.Length + 1).Replace('\', '/') })
    $dirs  = @([IO.Directory]::EnumerateDirectories($Base, '*', [IO.SearchOption]::AllDirectories) | ForEach-Object { $_.Substring($Base.Length + 1).Replace('\', '/') })
    return [ordered]@{ Files = $files; Dirs = $dirs }
}
$allowed = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($e in $entries) { if ($e.Rel) { [void]$allowed.Add($e.Rel) } }
[void]$allowed.Add('supervisor_v2/bound_list_v2.json')
function Tree-Problems($t) {
    $p = @()
    foreach ($f in $t.Files) { if (-not $allowed.Contains($f)) { $p += "EXTRA:$f" } }
    $present = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
    foreach ($f in $t.Files) { [void]$present.Add($f) }
    foreach ($a in $allowed) { if (-not $present.Contains($a)) { $p += "MISSING:$a" } }
    foreach ($f in $t.Files) { if ($f -match '\.(pyc|pyo|zip|_pth)$' -or $f -match '(^|/)pyvenv\.cfg$') { $p += "FORBIDDEN:$f" } }
    foreach ($d in $t.Dirs)  { if ($d -match '(^|/)__pycache__$') { $p += "PYCACHE_DIR:$d" } }
    if (@([IO.Directory]::EnumerateFileSystemEntries($Prefix)).Count -ne 0) { $p += 'PREFIX_NOT_EMPTY' }
    return $p
}
$tree0 = Tree-Scan
$tp0 = @(Tree-Problems $tree0)
$rec.Checks.TreeProblemsBefore = $tp0.Count; $rec.Values.TreeFileCount = $tree0.Files.Count; $rec.Values.TreeDirCount = $tree0.Dirs.Count
if ($tp0.Count -gt 0) { Block 'TREE_PROBLEM' $tp0 }

# 7. Per-item ACL: base protected form; every other file and directory inherits only.
$expBase = $bl.ExpectedOwnerAccessSddl.Base; $expDir = $bl.ExpectedOwnerAccessSddl.Dir; $expFile = $bl.ExpectedOwnerAccessSddl.File
function Acl-Problems($t) {
    $p = @()
    if ((Sddl-OA $Base) -ne $expBase) { $p += 'BASE' }
    foreach ($d in $t.Dirs)  { if ((Sddl-OA ([IO.Path]::Combine($Base, $d.Replace('/', '\')))) -ne $expDir)  { $p += "DIR:$d" } }
    foreach ($f in $t.Files) { if ((Sddl-OA ([IO.Path]::Combine($Base, $f.Replace('/', '\')))) -ne $expFile) { $p += "FILE:$f" } }
    return $p
}
$ap0 = @(Acl-Problems $tree0)
$rec.Checks.AclProblemsBefore = $ap0.Count
if ($ap0.Count -gt 0) { Block 'ACL_PROBLEM' $ap0 }

# 8. Authenticode: runtime PE files signed by the Python Software Foundation; host and system DLLs signed by Microsoft.
$sigBad = @(); $signers = New-Object 'System.Collections.Generic.HashSet[string]'
foreach ($e in $entries) {
    if ([string]::IsNullOrEmpty($e.SignerOrg)) { continue }
    $s = Microsoft.PowerShell.Security\Get-AuthenticodeSignature -LiteralPath $e.Path
    $subj = $(if ($s.SignerCertificate) { $s.SignerCertificate.Subject } else { '' })
    [void]$signers.Add("$($e.Kind)|$subj")
    $orgOk = ($subj -match ('(^|, )O=' + [Regex]::Escape($e.SignerOrg) + '(,|$)'))
    $thumb = $(if ($s.SignerCertificate) { $s.SignerCertificate.Thumbprint } else { '' })
    $thumbOk = $(if ($e.Thumb) { $thumb -eq $e.Thumb } else { $true })
    $osOk = $true
    if ($e.Kind -eq 'SYSTEM') { $prop = $s.PSObject.Properties['IsOSBinary']; $osOk = ($prop -ne $null -and $prop.Value -eq $true) }
    if ($s.Status -ne 'Valid' -or -not $orgOk -or -not $thumbOk -or -not $osOk) { $sigBad += [ordered]@{ Path = $e.Path; Status = [string]$s.Status; Subject = $subj; Thumbprint = $thumb; OsBinary = $osOk } }
}
$hs = Microsoft.PowerShell.Security\Get-AuthenticodeSignature -LiteralPath $hostPath
$hp = $hs.PSObject.Properties['IsOSBinary']
if ($hs.Status -ne 'Valid' -or $hs.SignerCertificate.Subject -notmatch '(^|, )O=Microsoft Corporation(,|$)' -or $hp -eq $null -or $hp.Value -ne $true) { $sigBad += [ordered]@{ Path = $hostPath; Status = [string]$hs.Status } }
$rec.Values.Signers = @($signers)
$rec.Checks.SignatureProblems = @($sigBad).Count
if (@($sigBad).Count -gt 0) { Block 'SIGNATURE_PROBLEM' $sigBad }

# 9. OpenSSL compiled-in config locations (from libcrypto-3.dll) must not hold a config file.
$sslCnf = 'C:\Program Files\Common Files\SSL\openssl.cnf'
$rec.Values.OpenSslConfPresent = [IO.File]::Exists($sslCnf)
$rec.Values.OpenSslModulesDirPresent = [IO.Directory]::Exists('C:\Program Files\OpenSSL\lib\ossl-modules')
if ($rec.Values.OpenSslConfPresent) { Block 'OPENSSL_CONF_PRESENT' $sslCnf }

# 10. Record KnownDLLs (residual: mapped from boot-time sections, not from the locked files).
$kd = [Microsoft.Win32.Registry]::LocalMachine.OpenSubKey('SYSTEM\CurrentControlSet\Control\Session Manager\KnownDLLs')
$rec.Values.KnownDlls = @($(if ($kd) { $kd.GetValueNames() | ForEach-Object { [string]$kd.GetValue($_) } } else { @() }))

# 11. T0, then start the child once.
$rec.Values.T0 = [ordered]@{ Utc = [DateTime]::UtcNow.ToString('o'); StopwatchTicks = [Diagnostics.Stopwatch]::GetTimestamp(); Frequency = [Diagnostics.Stopwatch]::Frequency }
$argv = '-I -S -B "' + $Probe + '"'
$psi = New-Object Diagnostics.ProcessStartInfo
$psi.FileName = $PyExe; $psi.Arguments = $argv; $psi.WorkingDirectory = $Runtime
$psi.UseShellExecute = $false; $psi.CreateNoWindow = $true
$psi.RedirectStandardInput = $true; $psi.RedirectStandardOutput = $true; $psi.RedirectStandardError = $true
$psi.EnvironmentVariables.Clear()
$psi.EnvironmentVariables['SystemRoot'] = $WinDir; $psi.EnvironmentVariables['windir'] = $WinDir
$psi.EnvironmentVariables['SystemDrive'] = $WinDir.Substring(0, 2); $psi.EnvironmentVariables['PATH'] = $SysDir
$rec.Values.ChildArgv = $argv
$rec.Values.ChildEnvironmentNames = @($psi.EnvironmentVariables.Keys | Sort-Object)
$p = [Diagnostics.Process]::Start($psi)
$cpid = $p.Id
$errTask = $p.StandardError.ReadToEndAsync()
$lineTask = $p.StandardOutput.ReadLineAsync()
if (-not $lineTask.Wait(60000)) { try { $p.Kill() } catch {}; Block 'CHILD_NO_REPORT' $cpid }
$line = $lineTask.Result

# 12. Outside-in, while the child is alive and waiting on stdin EOF.
$ci = ProcInfo $cpid
$p.Refresh()
$natives = @($p.Modules | ForEach-Object { $_.FileName })
$p.StandardInput.Close()
if (-not $p.WaitForExit(30000)) { try { $p.Kill() } catch {}; Block 'CHILD_NO_EXIT' $cpid }
$p.WaitForExit()
$restOut = $p.StandardOutput.ReadToEnd(); $stderr = $errTask.Result
$rep = $null; try { $rep = Microsoft.PowerShell.Utility\ConvertFrom-Json -InputObject $line } catch { $rep = $null }
$rec.Values.Child = [ordered]@{ Pid = $cpid; System = $ci; ExitCode = $p.ExitCode; NativeModules = $natives; Stderr = $stderr; ExtraStdout = $restOut; ReportLine = $line }

$boundPaths = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($e in $entries) { [void]$boundPaths.Add($e.Path) }
$c = [ordered]@{}
# Outside-in (supervisor-observed)
$c.OI_ImagePathIsLockedPython = ($ci -ne $null) -and ($ci.Path -ieq $PyExe)
$c.OI_ParentIsSupervisor      = ($ci -ne $null) -and ($ci.Ppid -eq $PID)
$c.OI_CreatedNotBeforeT0Minus50ms = ($ci -ne $null) -and ($ci.CreatedUtc -ne $null) -and ([DateTime]::Parse($ci.CreatedUtc).ToUniversalTime() -ge [DateTime]::Parse($rec.Values.T0.Utc).ToUniversalTime().AddMilliseconds(-50))
$c.OI_ChildCommandLineExact   = ($ci -ne $null) -and ($ci.CommandLine -ceq ('"' + $PyExe + '" ' + $argv))
$c.OI_NativeModulesNonEmpty   = (@($natives).Count -ge 10)
$c.OI_NativeModulesAllBound   = (@($natives | Where-Object { -not $boundPaths.Contains($_) }).Count -eq 0)
$c.OI_ExitCodeZero            = ($p.ExitCode -eq 0)
$c.OI_StderrEmpty             = ([string]::IsNullOrEmpty($stderr))
# Child self-report (cross-check only)
$c.CR_ReportParsed = ($rep -ne $null)
if ($rep -ne $null) {
    $src = @($rep.Modules | Where-Object { $_.Loader -eq 'SourceFileLoader' -and $_.Name -ne '__main__' })
    $c.CR_PidMatches          = ([int]$rep.Pid -eq $cpid)
    $c.CR_ExecutableIsLocked  = ($rep.Executable -ieq $PyExe)
    $c.CR_MainFileIsProbe     = ($rep.MainFile -ieq $Probe)
    $c.CR_IsolationFlags      = ($rep.Flags.isolated -eq 1 -and $rep.Flags.no_site -eq 1 -and $rep.Flags.dont_write_bytecode -eq 1)
    $c.CR_NoPycachePrefix     = ($rep.PycachePrefix -eq $null)
    $c.CR_SourceModulesNonEmpty = ($src.Count -ge 10)
    $c.CR_SourceModulesAllBound = (@($src | Where-Object { -not $boundPaths.Contains([string]$_.Origin) }).Count -eq 0)
    $c.CR_OnlyKnownLoaders    = (@($rep.Modules | Where-Object { $_.Loader -ne $null -and @('SourceFileLoader', 'BuiltinImporter', 'FrozenImporter', 'ExtensionFileLoader') -notcontains [string]$_.Loader }).Count -eq 0)
    $c.CR_NoLoaderModulesNotFileBacked = (@($rep.Modules | Where-Object { $_.Loader -eq $null -and $_.Name -ne '__main__' -and $_.Origin -ne $null }).Count -eq 0)
    $expPath = @([IO.Path]::Combine($Runtime, 'python312.zip'), [IO.Path]::Combine($Runtime, 'DLLs'), [IO.Path]::Combine($Runtime, 'Lib'), $Runtime)
    $c.CR_SysPathExact        = ((@($rep.Path) -join '|') -ieq ($expPath -join '|'))
    $c.CR_EnvironMinimal      = (@($rep.EnvironNames | Where-Object { @('SYSTEMROOT', 'WINDIR', 'SYSTEMDRIVE', 'PATH') -notcontains ([string]$_).ToUpperInvariant() }).Count -eq 0)
}

# 13. Post checks while still locked: re-hash, tree, ACL.
$bad2 = 0
for ($i = 0; $i -lt $entries.Count; $i++) { $e = $entries[$i]; if ($e.Kind -eq 'SELF') { continue }; if ((Sha-Stream $held[$i + 1]) -ne $e.Sha) { $bad2++ } }
$c.POST_HashesUnchanged = ($bad2 -eq 0)
$tree1 = Tree-Scan
$c.POST_TreeClean = (@(Tree-Problems $tree1).Count -eq 0)
$c.POST_AclClean  = (@(Acl-Problems $tree1).Count -eq 0)
$rec.Checks.Run = $c
Release
$rec.Values.ReleasedUtc = [DateTime]::UtcNow.ToString('o')

$fails = @($c.Keys | Where-Object { $c[$_] -ne $true })
$rec.Values.FailedChecks = $fails
$rec.Outcome = $(if ($fails.Count -eq 0) { 'PASS_T0_DRY_RUN_V2' } else { 'CHILD_CHECK_FAILED' })
Write-Record
Say "$($rec.Outcome) record=$Out"
exit $(if ($fails.Count -eq 0) { 0 } else { 4 })
