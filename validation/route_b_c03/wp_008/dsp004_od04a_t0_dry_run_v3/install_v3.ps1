# DSP-004 OD04-A v3 installer. Run once, elevated, by go_v3.cmd.
# Copies the four pre-bound v2 files into the admin-protected C:\Program Files\DSP004Runtime\supervisor_v3.
# It verifies each file's SHA-256 against constants fixed before the run, writes the verified bytes (not a path copy),
# lets the folder inherit the protected ACL, and records the result. It never overwrites.
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version 2
$PSModuleAutoLoadingPreference = 'None'
$env:PSModulePath = [IO.Path]::Combine($PSHOME, 'Modules')
Import-Module ([IO.Path]::Combine($PSHOME, 'Modules\Microsoft.PowerShell.Utility\Microsoft.PowerShell.Utility.psd1'))
Import-Module ([IO.Path]::Combine($PSHOME, 'Modules\Microsoft.PowerShell.Security\Microsoft.PowerShell.Security.psd1'))

$Expected = [ordered]@{
    'supervisor_v3.ps1'  = '7CC3EC3D0432BFFE3D9ADAA34D90ED10DB015F5AFC241221E77E517B69C9E433'
    'probe_v3.py'        = '3AF5FD03B9487642A7256EAA21D654F6BF072749EBAF03B967A3E307C34CB2A3'
    'bound_list_v3.json' = '0A349A6DBDA8B1397941EDE195D6D76E5B77DBE252BA6D3B80E0516016AAE561'
    'run_v3.cmd'         = 'B430D9B22CACEDEEAE9C3124916ECFF8FD023EFABAE8D870920ECD2DAE64195A'
}
$Base    = 'C:\Program Files\DSP004Runtime'
$Dst     = [IO.Path]::Combine($Base, 'supervisor_v3')
$ExpBase = 'O:BAD:PAI(A;OICI;FA;;;SY)(A;OICI;FA;;;BA)(A;OICI;0x1200a9;;;BU)'
$Out     = [IO.Path]::Combine($PSScriptRoot, 'install_v3_result.json')
$SysDir  = [Environment]::GetFolderPath('System')

function Say([string]$s) { [Console]::WriteLine($s) }
function Fail([string]$c) { Say "STOP $c"; exit 2 }
function Sha([byte[]]$b) { return ([BitConverter]::ToString([Security.Cryptography.SHA256]::Create().ComputeHash($b)) -replace '-', '') }
function Sddl-OA([string]$p) { return ((Microsoft.PowerShell.Security\Get-Acl -LiteralPath $p).Sddl -replace 'G:[^D]*(?=D:)', '') }

$admin = (New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $admin) { Fail 'NOT_ELEVATED' }
function RegValue([Microsoft.Win32.RegistryKey]$root, [string]$sub, [string]$name) { $k = $root.OpenSubKey($sub); if ($k -eq $null) { return $null }; try { return $k.GetValue($name) } finally { $k.Close() } }
function RegKeyExists([Microsoft.Win32.RegistryKey]$root, [string]$sub) { $k = $root.OpenSubKey($sub); if ($k -eq $null) { return $false }; $k.Close(); return $true }
# Same launch-hijack checks as the supervisor, for this elevated session.
$WinDir = [Environment]::GetFolderPath('Windows')
$me = [Diagnostics.Process]::GetCurrentProcess()
if ($me.MainModule.FileName -ine [IO.Path]::Combine($SysDir, 'WindowsPowerShell\v1.0\powershell.exe')) { Fail 'HOST_NOT_SYSTEM_POWERSHELL' }
$clrVars = @([Environment]::GetEnvironmentVariables().Keys | ForEach-Object { [string]$_ } | Where-Object { $_ -match '^(COR_ENABLE_PROFILING|COR_PROFILER(_PATH(_32|_64)?)?|COMPLUS_.*|DOTNET_.*|APPDOMAIN_MANAGER_.*)$' })
if ($clrVars.Count -gt 0) { Fail 'CLR_INJECTION_VARIABLES_PRESENT' }
$hkcuAuto = RegValue ([Microsoft.Win32.Registry]::CurrentUser) 'Software\Microsoft\Command Processor' 'AutoRun'
$hklmAuto = RegValue ([Microsoft.Win32.Registry]::LocalMachine) 'Software\Microsoft\Command Processor' 'AutoRun'
$cmdOverride = (RegKeyExists ([Microsoft.Win32.Registry]::CurrentUser) 'Software\Classes\.cmd') -or (RegKeyExists ([Microsoft.Win32.Registry]::CurrentUser) 'Software\Classes\cmdfile')
if (-not [string]::IsNullOrEmpty([string]$hkcuAuto) -or -not [string]::IsNullOrEmpty([string]$hklmAuto) -or $cmdOverride) { Fail 'LAUNCH_HIJACK_SURFACE_PRESENT' }
$me.Refresh()
$foreign = @($me.Modules | ForEach-Object { $_.FileName } | Where-Object { -not $_.StartsWith($WinDir + '\', [StringComparison]::OrdinalIgnoreCase) })
$foreignBad = @($foreign | Where-Object { $fsig = Microsoft.PowerShell.Security\Get-AuthenticodeSignature -LiteralPath $_; -not ($fsig.Status -eq 'Valid' -and $fsig.SignerCertificate -ne $null -and $fsig.SignerCertificate.Subject -match '(^|, )O=Microsoft Corporation(,|$)') })
if ($foreignBad.Count -gt 0) { Fail 'HOST_MODULE_UNTRUSTED' }
if ([IO.File]::Exists($Out)) { Fail 'RESULT_ALREADY_EXISTS' }
if (-not [IO.Directory]::Exists($Base)) { Fail 'BASE_MISSING' }
if ((Sddl-OA $Base) -ne $ExpBase) { Fail 'BASE_ACL_UNEXPECTED' }
if ([IO.Directory]::Exists($Dst)) { Fail 'TARGET_ALREADY_EXISTS' }
# Phase-1 environment: run account exists and is not an administrator; process-creation auditing with command line.
& ([IO.Path]::Combine($SysDir, 'net.exe')) user dsp004val | Out-Null
if ($LASTEXITCODE -ne 0) { Fail 'RUN_ACCOUNT_MISSING' }
$admins = @(& ([IO.Path]::Combine($SysDir, 'net.exe')) localgroup Administrators)
if ($LASTEXITCODE -ne 0) { Fail 'NET_LOCALGROUP_FAILED' }
if (@($admins | Where-Object { $_.Trim() -ieq 'dsp004val' }).Count -gt 0) { Fail 'RUN_ACCOUNT_IS_ADMINISTRATOR' }
$auditCsv = @(& ([IO.Path]::Combine($SysDir, 'auditpol.exe')) /get '/subcategory:{0CCE922B-69AE-11D9-BED3-505054503030},{0CCE922C-69AE-11D9-BED3-505054503030}' /r)
$cmdLine = RegValue ([Microsoft.Win32.Registry]::LocalMachine) 'Software\Microsoft\Windows\CurrentVersion\Policies\System\Audit' 'ProcessCreationIncludeCmdLine_Enabled'
if ($cmdLine -ne 1) { Fail 'AUDIT_CMDLINE_NOT_ENABLED' }

# Read and verify every source file once; keep the verified bytes.
$verified = [ordered]@{}
foreach ($n in $Expected.Keys) {
    $src = [IO.Path]::Combine($PSScriptRoot, $n)
    if (-not [IO.File]::Exists($src)) { Fail "SOURCE_MISSING_$n" }
    $b = [IO.File]::ReadAllBytes($src)
    if ((Sha $b) -ne $Expected[$n]) { Fail "SOURCE_SHA_MISMATCH_$n" }
    $verified[$n] = $b
}

[void][IO.Directory]::CreateDirectory($Dst)
foreach ($n in $verified.Keys) {
    $fs = [IO.File]::Open([IO.Path]::Combine($Dst, $n), [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
    $fs.Write($verified[$n], 0, $verified[$n].Length); $fs.Close()
}
& ([IO.Path]::Combine($SysDir, 'icacls.exe')) $Dst /reset /T /C /Q | Out-Null
if ($LASTEXITCODE -ne 0) { Fail 'ICACLS_RESET_FAILED' }
& ([IO.Path]::Combine($SysDir, 'icacls.exe')) $Dst /setowner '*S-1-5-32-544' /T /C /Q | Out-Null
if ($LASTEXITCODE -ne 0) { Fail 'SETOWNER_FAILED' }

$files = @()
foreach ($n in $Expected.Keys) {
    $p = [IO.Path]::Combine($Dst, $n); $b = [IO.File]::ReadAllBytes($p)
    $files += [ordered]@{ Name = $n; Bytes = $b.Length; SHA256 = (Sha $b); MatchesExpected = ((Sha $b) -eq $Expected[$n]); OwnerAccessSddl = (Sddl-OA $p) }
}
$res = [ordered]@{
    Kind = 'DSP004_OD04A_V3_INSTALL_RESULT'; InstalledUtc = [DateTime]::UtcNow.ToString('o')
    InstallerSha256 = (Sha ([IO.File]::ReadAllBytes($PSCommandPath)))
    BaseOwnerAccessSddl = (Sddl-OA $Base); DirOwnerAccessSddl = (Sddl-OA $Dst); Files = $files
    HijackChecks = 'PASSED'; ClrInjectionVariables = 0; HostModulesOutsideWindows = $foreign
    RunAccountExists = $true; RunAccountInAdministrators = $false; AuditPolicyCsv = $auditCsv; IncludeCmdLine = $cmdLine
}
$json = Microsoft.PowerShell.Utility\ConvertTo-Json -InputObject $res -Depth 5
$fs = [IO.File]::Open($Out, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
$bytes = (New-Object Text.UTF8Encoding($false)).GetBytes($json); $fs.Write($bytes, 0, $bytes.Length); $fs.Close()
if (@($files | Where-Object { -not $_.MatchesExpected }).Count -gt 0) { Fail 'INSTALLED_SHA_MISMATCH' }
Say "DONE installed=$Dst result=$Out"
exit 0
