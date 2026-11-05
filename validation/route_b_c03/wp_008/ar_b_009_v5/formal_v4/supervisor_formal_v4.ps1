# C03 AR-B-009 V5 formal-run supervisor v4 = formal v3 with paths moved to project_v4 / harness_rev6, input REV6 and 70 variants (prepared under the AR-B-009 work authorization; not accepted; a run needs a separate
# owner authorization). Based on supervisor_v3 (bound REV31, run 4 times under v3/v4). Changes from v3:
#   - runs harness_rev4.py from the admin-protected PROJECT_ROOT C:\Program Files\DSP004Runtime\project_v4 once,
#     with argv -I -S -B "<harness>" "<PROJECT_ROOT>", instead of the probe three times;
#   - locks and hashes the 27 installed project files (10 subject, 15 fixtures, input REV4, harness) as well;
#   - replaces the probe self-report checks with checks on the harness result (all 28 variants PASS, no mapped
#     variant non-conformant, no guard denial, input SHA) and on its reported import closure;
#   - record file formal_v4_run_record.json; Windows audit events 4688/4689 are collected afterwards.
# Runs only from the admin-protected directory C:\Program Files\DSP004Runtime\supervisor_formal_v4, as dsp004val.
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version 2

# 0. Module loading: no autoload, core modules only from $PSHOME, module-qualified calls.
$PSModuleAutoLoadingPreference = 'None'
$origPSModulePath = $env:PSModulePath
$env:PSModulePath = [IO.Path]::Combine($PSHOME, 'Modules')
Import-Module ([IO.Path]::Combine($PSHOME, 'Modules\Microsoft.PowerShell.Utility\Microsoft.PowerShell.Utility.psd1'))
Import-Module ([IO.Path]::Combine($PSHOME, 'Modules\Microsoft.PowerShell.Security\Microsoft.PowerShell.Security.psd1'))
Microsoft.PowerShell.Utility\Add-Type -AssemblyName System.Management

$ExpectedBoundSha = 'E7CBE14757FA0F5136DB6DE27B7A95E5E7AA62B53704C2680389219C31541D18'
$ExpectedInputSha = '418AD1EE9144C28E93DF571FD829C660E6B8EDA4DD06B3B16CDEEC1AAF1BE9C0'
$Base     = 'C:\Program Files\DSP004Runtime'
$SupDir   = [IO.Path]::Combine($Base, 'supervisor_formal_v4')
$Runtime  = [IO.Path]::Combine($Base, 'Python312')
$Prefix   = [IO.Path]::Combine($Base, 'empty_pycache_prefix')
$PyExe    = [IO.Path]::Combine($Runtime, 'python.exe')
$ProjRoot = [IO.Path]::Combine($Base, 'project_v4')
$Harness  = [IO.Path]::Combine($ProjRoot, 'validation\route_b_c03\wp_008\ar_b_009_v5\harness_rev6.py')
$BoundP   = [IO.Path]::Combine($SupDir, 'bound_list_formal_v4.json')
$SysDir   = [Environment]::GetFolderPath('System')
$WinDir   = [Environment]::GetFolderPath('Windows')
$DocsDir  = [Environment]::GetFolderPath('MyDocuments')
if ([string]::IsNullOrEmpty($DocsDir)) { $DocsDir = [IO.Path]::Combine([Environment]::GetFolderPath('UserProfile'), 'Documents') }
$OutDir   = [IO.Path]::Combine($DocsDir, 'dsp004-probe')
$Out      = [IO.Path]::Combine($OutDir, 'formal_v4_run_record.json')
$SupFiles = @('supervisor_formal_v4.ps1', 'bound_list_formal_v4.json', 'run_formal_v4.cmd')

$rec  = [ordered]@{ Kind = 'C03_FORMAL_V4_RUN_RECORD'; Outcome = $null; BlockCode = $null; BlockDetail = $null; Checks = [ordered]@{}; Values = [ordered]@{} }
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
if ($PSCommandPath -ine [IO.Path]::Combine($SupDir, 'supervisor_formal_v4.ps1')) { Block 'SCRIPT_NOT_IN_PROTECTED_DIR' $PSCommandPath }
$parent = ProcInfo ((ProcInfo $PID).Ppid)
$rec.Values.Parent = $parent
if ($parent -eq $null -or $parent.Path -ine [IO.Path]::Combine($SysDir, 'cmd.exe')) { Block 'PARENT_NOT_SYSTEM_CMD' $parent }
if ($parent.CommandLine.IndexOf([IO.Path]::Combine($SupDir, 'run_formal_v4.cmd'), [StringComparison]::OrdinalIgnoreCase) -lt 0) { Block 'PARENT_NOT_RUN_FORMAL_V4_CMD' $parent.CommandLine }
$rec.Values.SupervisorCommandLine = (ProcInfo $PID).CommandLine
$rec.Values.GrandParent = ProcInfo $parent.Ppid
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
# Separate run account: exactly <machine>\dsp004val, with no Administrators group in the token at all (not even deny-only).
$wid = [Security.Principal.WindowsIdentity]::GetCurrent()
$baPresent = @($groups | Where-Object { $_ -match '"S-1-5-32-544"' }).Count -gt 0
$rec.Values.Account = [ordered]@{ Name = $wid.Name; Sid = $wid.User.Value; AdministratorsGroupInToken = $baPresent }
if ($wid.Name -ine ([Environment]::MachineName + '\dsp004val')) { Block 'NOT_RUN_ACCOUNT' $wid.Name }
if ($baPresent) { Block 'RUN_ACCOUNT_IS_ADMINISTRATOR' $rec.Values.Account }
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
foreach ($f in $bl.PriorFiles) { $entries.Add([pscustomobject]@{ Kind = 'PRIOR'; Rel = $f.RelPath; Path = [IO.Path]::Combine($Base, ($f.RelPath -replace '/', '\')); Bytes = [int64]$f.Bytes; Sha = $f.SHA256; SignerOrg = $null; Thumb = $null }) }
foreach ($f in $bl.ProjectFiles) { $entries.Add([pscustomobject]@{ Kind = 'PROJECT'; Rel = $f.RelPath; Path = [IO.Path]::Combine($Base, ($f.RelPath -replace '/', '\')); Bytes = [int64]$f.Bytes; Sha = $f.SHA256; SignerOrg = $null; Thumb = $null }) }
foreach ($f in $bl.SystemDlls) { $entries.Add([pscustomobject]@{ Kind = 'SYSTEM'; Rel = $null; Path = $f.Path; Bytes = [int64]$f.Bytes; Sha = $f.SHA256; SignerOrg = 'Microsoft Corporation'; Thumb = $null }) }
$selfPath = [IO.Path]::Combine($SupDir, 'supervisor_formal_v4.ps1')
$entries.Add([pscustomobject]@{ Kind = 'SELF'; Rel = 'supervisor_formal_v4/supervisor_formal_v4.ps1'; Path = $selfPath; Bytes = -1; Sha = $null; SignerOrg = $null; Thumb = $null })

foreach ($e in $entries) {
    try { $held.Add([IO.File]::Open($e.Path, [IO.FileMode]::Open, [IO.FileAccess]::Read, [IO.FileShare]::Read)) }
    catch { Block 'LOCK_FAILED' ([ordered]@{ Kind = $e.Kind; Path = $e.Path; Error = $_.Exception.GetType().Name }) }
}
$rec.Checks.LockedFiles = $held.Count

# 5. Hash through held handles (index 0 is the bound list).
$bad = @(); $selfSha = $null
$perFile = New-Object System.Collections.Generic.List[object]
for ($i = 0; $i -lt $entries.Count; $i++) {
    $e = $entries[$i]; $fs = $held[$i + 1]; $h = Sha-Stream $fs
    $perFile.Add([ordered]@{ K = $e.Kind; P = $(if ($e.Rel) { $e.Rel } else { $e.Path }); B = $fs.Length; H = $h })
    if ($e.Kind -eq 'SELF') { $selfSha = $h; continue }
    if ($fs.Length -ne $e.Bytes -or $h -ne $e.Sha) { $bad += [ordered]@{ Kind = $e.Kind; Path = $e.Path } }
}
$rec.Values.PerFileHashes = $perFile
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
[void]$allowed.Add('supervisor_formal_v4/bound_list_formal_v4.json')
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
$rec.Values.TreeDirs = $tree0.Dirs
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
$sigBad = @(); $perSig = New-Object System.Collections.Generic.List[object]; $signers = New-Object 'System.Collections.Generic.HashSet[string]'
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
    $perSig.Add([ordered]@{ P = $(if ($e.Rel) { $e.Rel } else { $e.Path }); S = [string]$s.Status; T = $thumb; Os = $osOk })
    if ($s.Status -ne 'Valid' -or -not $orgOk -or -not $thumbOk -or -not $osOk) { $sigBad += [ordered]@{ Path = $e.Path; Status = [string]$s.Status; Subject = $subj; Thumbprint = $thumb; OsBinary = $osOk } }
}
$hs = Microsoft.PowerShell.Security\Get-AuthenticodeSignature -LiteralPath $hostPath
$hp = $hs.PSObject.Properties['IsOSBinary']
if ($hs.Status -ne 'Valid' -or $hs.SignerCertificate.Subject -notmatch '(^|, )O=Microsoft Corporation(,|$)' -or $hp -eq $null -or $hp.Value -ne $true) { $sigBad += [ordered]@{ Path = $hostPath; Status = [string]$hs.Status } }
$rec.Values.Signers = @($signers)
$rec.Values.PerFileSignatures = $perSig
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

# 11-12. One child run of the harness. Each: T0, start (fixed argv, minimal env, stdin redirected and closed at once, no data),
# read the one report line, enumerate from outside while the child pauses, then wait for its own exit.
$boundPaths = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($e in $entries) { [void]$boundPaths.Add($e.Path) }
$argv = '-I -S -B "' + $Harness + '" "' + $ProjRoot + '"'
$rec.Values.ChildArgv = $argv
$c = [ordered]@{}
$runs = New-Object System.Collections.Generic.List[object]
$RunCount = 1
$rec.Values.RunCount = $RunCount
$rec.Values.Runs = $runs
$rec.Checks.Run = $c
for ($n = 1; $n -le $RunCount; $n++) {
    $t0 = [ordered]@{ Utc = [DateTime]::UtcNow.ToString('o'); StopwatchTicks = [Diagnostics.Stopwatch]::GetTimestamp(); Frequency = [Diagnostics.Stopwatch]::Frequency }
    $psi = New-Object Diagnostics.ProcessStartInfo
    $psi.FileName = $PyExe; $psi.Arguments = $argv; $psi.WorkingDirectory = $Runtime
    $psi.UseShellExecute = $false; $psi.CreateNoWindow = $true
    $psi.RedirectStandardInput = $true; $psi.RedirectStandardOutput = $true; $psi.RedirectStandardError = $true
    $psi.EnvironmentVariables.Clear()
    $psi.EnvironmentVariables['SystemRoot'] = $WinDir; $psi.EnvironmentVariables['windir'] = $WinDir
    $psi.EnvironmentVariables['SystemDrive'] = $WinDir.Substring(0, 2); $psi.EnvironmentVariables['PATH'] = $SysDir
    if ($n -eq 1) { $rec.Values.ChildEnvironmentNames = @($psi.EnvironmentVariables.Keys | Sort-Object) }
    $p = [Diagnostics.Process]::Start($psi)
    $p.StandardInput.Close()
    $cpid = $p.Id
    $errTask = $p.StandardError.ReadToEndAsync()
    $lineTask = $p.StandardOutput.ReadLineAsync()
    if (-not $lineTask.Wait(120000)) { try { $p.Kill() } catch {}; Block 'CHILD_NO_REPORT' ([ordered]@{ Run = $n; Pid = $cpid }) }
    $line = $lineTask.Result
    $ci = ProcInfo $cpid
    $p.Refresh()
    $natives = @($p.Modules | ForEach-Object { $_.FileName })
    if (-not $p.WaitForExit(60000)) { try { $p.Kill() } catch {}; Block 'CHILD_NO_EXIT' ([ordered]@{ Run = $n; Pid = $cpid }) }
    $p.WaitForExit()
    $exitUtc = [DateTime]::UtcNow.ToString('o')
    $restOut = $p.StandardOutput.ReadToEnd(); $stderr = $errTask.Result
    $rep = $null; try { $rep = Microsoft.PowerShell.Utility\ConvertFrom-Json -InputObject $line } catch { $rep = $null }
    $runs.Add([ordered]@{ N = $n; T0 = $t0; Pid = $cpid; System = $ci; ExitCode = $p.ExitCode; ExitSeenUtc = $exitUtc; NativeModules = $natives; Stderr = $stderr; ExtraStdout = $restOut; ReportLine = $line })
    $k = 'R' + $n + '_'
    # Outside-in (supervisor-observed)
    $c[$k + 'OI_ImagePathIsLockedPython'] = ($ci -ne $null) -and ($ci.Path -ieq $PyExe)
    $c[$k + 'OI_ParentIsSupervisor']      = ($ci -ne $null) -and ($ci.Ppid -eq $PID)
    $c[$k + 'OI_CreatedNotBeforeT0Minus50ms'] = ($ci -ne $null) -and ($ci.CreatedUtc -ne $null) -and ([DateTime]::Parse($ci.CreatedUtc).ToUniversalTime() -ge [DateTime]::Parse($t0.Utc).ToUniversalTime().AddMilliseconds(-50))
    $c[$k + 'OI_ChildCommandLineExact']   = ($ci -ne $null) -and ($ci.CommandLine -ceq ('"' + $PyExe + '" ' + $argv))
    $c[$k + 'OI_NativeModulesNonEmpty']   = (@($natives).Count -ge 10)
    $c[$k + 'OI_NativeModulesAllBound']   = (@($natives | Where-Object { -not $boundPaths.Contains($_) }).Count -eq 0)
    $c[$k + 'OI_ExitCodeZero']            = ($p.ExitCode -eq 0)
    $c[$k + 'OI_StderrEmpty']             = ([string]::IsNullOrEmpty($stderr))
    $c[$k + 'OI_NoExtraStdout']           = ([string]::IsNullOrEmpty($restOut))
    # Harness result and self-report (cross-check)
    $c[$k + 'HX_ReportParsed'] = ($rep -ne $null)
    $hasStop = ($rep -ne $null) -and ($rep.PSObject.Properties['Stop'] -ne $null)
    if ($rep -ne $null) { $c[$k + 'HX_NoStop'] = (-not $hasStop) }
    if ($rep -ne $null -and -not $hasStop) {
        $t = $rep.Totals
        $c[$k + 'HX_InputSha']             = ($rep.InputSha256 -ceq $ExpectedInputSha)
        $c[$k + 'HX_AllVariantsPass']      = ($t -ne $null) -and ([int]$t.variants -eq 70) -and ([int]$t.pass -eq 70) -and ([int]$t.fail -eq 0)
        $c[$k + 'HX_MappedAllConformant']  = ($t -ne $null) -and ([int]$t.mapped_not_conformant -eq 0)
        $c[$k + 'HX_NoGuardDenial']        = ($t -ne $null) -and ([int]$t.guard_denied -eq 0)
        $c[$k + 'HX_IsolationFlags']       = ($rep.Flags.isolated -eq 1 -and $rep.Flags.no_site -eq 1 -and $rep.Flags.dont_write_bytecode -eq 1)
        $pr = $rep.Process
        $c[$k + 'HX_PidMatches']           = ([int]$pr.Pid -eq $cpid)
        $c[$k + 'HX_ExecutableIsLocked']   = ($pr.Executable -ieq $PyExe)
        $c[$k + 'HX_MainFileIsHarness']    = ($pr.MainFile -ieq $Harness)
        $c[$k + 'HX_NoPycachePrefix']      = ($pr.PycachePrefix -eq $null)
        $expPath = @([IO.Path]::Combine($Runtime, 'python312.zip'), [IO.Path]::Combine($Runtime, 'DLLs'), [IO.Path]::Combine($Runtime, 'Lib'), $Runtime)
        $c[$k + 'HX_SysPathExact']         = ((@($pr.Path) -join '|') -ieq ($expPath -join '|'))
        $c[$k + 'HX_EnvironMinimal']       = (@($pr.EnvironNames | Where-Object { @('SYSTEMROOT', 'WINDIR', 'SYSTEMDRIVE', 'PATH') -notcontains ([string]$_).ToUpperInvariant() }).Count -eq 0)
        $mods = @($rep.Modules)
        $src  = @($mods | Where-Object { $_.Loader -eq 'SourceFileLoader' -and $_.Name -ne '__main__' })
        $bi   = @($mods | Where-Object { $_.Loader -eq 'BytesImporter' })
        $c[$k + 'HX_SourceModulesAllBound'] = ($src.Count -ge 10) -and (@($src | Where-Object { -not $boundPaths.Contains([string]$_.Origin) }).Count -eq 0)
        $c[$k + 'HX_SubjectModulesFromProjectRoot'] = ($bi.Count -ge 1) -and (@($bi | Where-Object { -not ([string]$_.Name).StartsWith('phase2_runtime') -or -not $boundPaths.Contains([string]$_.Origin) }).Count -eq 0)
        $c[$k + 'HX_OnlyKnownLoaders']     = (@($mods | Where-Object { $_.Loader -ne $null -and @('SourceFileLoader', 'BuiltinImporter', 'FrozenImporter', 'ExtensionFileLoader', 'BytesImporter') -notcontains [string]$_.Loader }).Count -eq 0)
        $c[$k + 'HX_NoLoaderModulesNotFileBacked'] = (@($mods | Where-Object { $_.Loader -eq $null -and $_.Name -ne '__main__' -and $_.Origin -ne $null }).Count -eq 0)
    }
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
$rec.Outcome = $(if ($fails.Count -eq 0) { 'PASS_FORMAL_V4' } else { 'FORMAL_V4_CHECK_FAILED' })
Write-Record
Say "$($rec.Outcome) record=$Out"
exit $(if ($fails.Count -eq 0) { 0 } else { 4 })
