# C03 AR-B-009 V5 formal-run v4 installer. Run once by the owner, elevated, via install_formal_v4.cmd (prepared under the
# AR-B-009 work authorization). Installs nothing else and runs nothing.
# Copies the 3 supervisor files into C:\Program Files\DSP004Runtime\supervisor_formal_v4 and the 27 project files
# (10 subject, 15 fixtures, input REV6, harness REV6) into C:\Program Files\DSP004Runtime\project_v4 at their
# repository-relative paths. Every source file's SHA-256 is checked against the constants below before anything is
# written; the verified bytes (not a path copy) are written; nothing is overwritten; both folders inherit the
# protected ACL of the base folder, owner Administrators. Writes install_formal_v4_result.json next to itself.
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version 2
$PSModuleAutoLoadingPreference = 'None'
$env:PSModulePath = [IO.Path]::Combine($PSHOME, 'Modules')
Import-Module ([IO.Path]::Combine($PSHOME, 'Modules\Microsoft.PowerShell.Utility\Microsoft.PowerShell.Utility.psd1'))
Import-Module ([IO.Path]::Combine($PSHOME, 'Modules\Microsoft.PowerShell.Security\Microsoft.PowerShell.Security.psd1'))

$Supervisor = [ordered]@{
    'supervisor_formal_v4.ps1' = '37054A8AC825D9947DA8629F03403E2C7B0BED7F8CCED2182461D5FB7840D13C'
    'bound_list_formal_v4.json' = 'E7CBE14757FA0F5136DB6DE27B7A95E5E7AA62B53704C2680389219C31541D18'
    'run_formal_v4.cmd' = '25EB78DD976FB9EBC8FE53ACCA84BC8EF5842AB43353D8350DBF7FB418C2756B'
}
$Project = [ordered]@{
    'scripts/phase2_runtime/__init__.py' = '49B8B1BD319B6424323AD0EDC04B3969D71196CD8D69E12C16D5442B17340844'
    'scripts/phase2_runtime/route_b_c03/__init__.py' = 'F669613D65267EC5D4D42CB79008EB510307A99B20E40EE13E9E1E0E404A504D'
    'scripts/phase2_runtime/route_b_c03/contracts.py' = 'D0D5DA397EF4DFA0DB47D924A90CB9EBD9017F737FCB7B915AE9633D7C6F310A'
    'scripts/phase2_runtime/route_b_c03/identity_gate.py' = 'F9CC7021C1A2586611FBCA7333F8ADC8BDE3A6436663680EEA100CA26EDC9C31'
    'scripts/phase2_runtime/route_b_c03/mapping.py' = '320F7E8576C1C4E81B4E78E6058000E4D720173948BE736AD846B8CAD664EC66'
    'scripts/phase2_runtime/route_b_c03/isolation.py' = '9BC554294D5945188A153F0A5CBEDFAB4E483C95B133683B7517ECC334D4205B'
    'scripts/phase2_runtime/route_b_c03/failures.py' = 'C6E03A8AB0305B83F6042D8F8E379AE91047D41F4AB3467AC0A7281E7E4DA48E'
    'scripts/phase2_runtime/route_b_c03/audit.py' = '96F874FD494AA67276604A8AD49813F68B7BF4F2C28E63FC9D6C6ECE127C44DA'
    'scripts/phase2_runtime/route_b_c03/provider_port.py' = '66E4DA862BBBD50380B17686DB6BC2AB6D5D3B861AB53FCDDE1B608F86DEA381'
    'scripts/phase2_runtime/route_b_c03/capability.py' = '8D0B3CD664A893609EDCEFABADCD48EAA77DEF6B519872DA27E9E15F68EA7686'
    'validation/route_b_c03/wp_008/fixtures/C03-TA-V-001.json' = 'C8CEFEDC496D5D0D33E0F21D61B5E3C3354579A8D0E1C74F70640305C65FC99A'
    'validation/route_b_c03/wp_008/fixtures/C03-TA-V-002.json' = '257437A2AA80A58C0741F1EC0A5A514E014C633DD974804C6407DB84DB107290'
    'validation/route_b_c03/wp_008/fixtures/C03-TA-V-003.json' = '21BD65ECD28D569BADFF11489017569E8413B1CC9A5138A851F907CCF62EAF7E'
    'validation/route_b_c03/wp_008/fixtures/C03-TA-V-004.json' = '9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8'
    'validation/route_b_c03/wp_008/fixtures/C03-TA-V-005.json' = '4405ADC2CE242B83120B0BA304157B3E6F03687345F764BBBE1E3A2DCF2422DE'
    'validation/route_b_c03/wp_008/fixtures/C03-TA-V-006.json' = '9D24E6AFA92F9EF6E895B0B6E4D0E84BDC326E9C4B815E42723B31374CC2FDC8'
    'validation/route_b_c03/wp_008/fixtures/C03-TA-V-007.json' = '68D9D63583A0301BDE76C3E60A5F66B7CCDA897C17D58E8DBF282E3E49C3DB90'
    'validation/route_b_c03/wp_008/fixtures/C03-TA-V-008.json' = '7AA3FEF0CCDFA0C6A462C7945B63A50D828AC9C6D0725F428D347F6836075193'
    'validation/route_b_c03/wp_008/fixtures/C03-TA-V-009.json' = '34EFBC55490FB2E3FFC89CAFCAD9DD2D319C2C24D9B3E2B026143F74A73DC93C'
    'validation/route_b_c03/wp_008/fixtures/C03-TA-V-010.json' = '19DF9D35835F60C03C969B79B25F62CFE95E28C0A1B8122EDD8B9E1A5BC0E67A'
    'validation/route_b_c03/wp_008/fixtures/C03-TA-V-011.json' = '8795DA58E092E6DC7F88958E3AC60B754870F5BFAE15FF8BC2D699450B65FDFD'
    'validation/route_b_c03/wp_008/fixtures/C03-TA-V-012.json' = '8C6E4FC6279E95CFE48C9E9DA6E161F0AF05CA5FFEA95BE18DBAD6A81204E8E6'
    'validation/route_b_c03/wp_008/fixtures/C03-TA-V-013.json' = '3DBF0F60AC970F90C97CF85F5F21F1758B4818D814A02CE8ED03A4F1C3A49CA6'
    'validation/route_b_c03/wp_008/fixtures/C03-TA-V-014.json' = 'D3EF698EA45F41824CCF6C5A7020F6A0B495460341ADE7446461A1AAF0E7D523'
    'validation/route_b_c03/wp_008/fixtures/C03-TA-V-015.json' = '06DCEBA08CA43C75439B5A2AC1C140905887EF8CDC26C561FBD68E9A001D5AE1'
    'validation/route_b_c03/wp_008/ar_b_009_v5/C03_V5_INPUT_CANDIDATE_REV6.json' = '418AD1EE9144C28E93DF571FD829C660E6B8EDA4DD06B3B16CDEEC1AAF1BE9C0'
    'validation/route_b_c03/wp_008/ar_b_009_v5/harness_rev6.py' = '15BEDB445B44A472CF0058D07491DCF7E389B235B4FE46B8EC2F92CE9E9C8C66'
}
$Base    = 'C:\Program Files\DSP004Runtime'
$SupDst  = [IO.Path]::Combine($Base, 'supervisor_formal_v4')
$ProjDst = [IO.Path]::Combine($Base, 'project_v4')
$ExpBase = 'O:BAD:PAI(A;OICI;FA;;;SY)(A;OICI;FA;;;BA)(A;OICI;0x1200a9;;;BU)'
$Out     = [IO.Path]::Combine($PSScriptRoot, 'install_formal_v4_result.json')
$SysDir  = [Environment]::GetFolderPath('System')

function Say([string]$s) { [Console]::WriteLine($s) }
function Fail([string]$c) { Say "STOP $c"; exit 2 }
function Sha([byte[]]$b) { return ([BitConverter]::ToString([Security.Cryptography.SHA256]::Create().ComputeHash($b)) -replace '-', '') }
function Sddl-OA([string]$p) { return ((Microsoft.PowerShell.Security\Get-Acl -LiteralPath $p).Sddl -replace 'G:[^D]*(?=D:)', '') }
function RegValue([Microsoft.Win32.RegistryKey]$root, [string]$sub, [string]$name) { $k = $root.OpenSubKey($sub); if ($k -eq $null) { return $null }; try { return $k.GetValue($name) } finally { $k.Close() } }
function RegKeyExists([Microsoft.Win32.RegistryKey]$root, [string]$sub) { $k = $root.OpenSubKey($sub); if ($k -eq $null) { return $false }; $k.Close(); return $true }

$admin = (New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $admin) { Fail 'NOT_ELEVATED' }
$WinDir = [Environment]::GetFolderPath('Windows')
$me = [Diagnostics.Process]::GetCurrentProcess()
if ($me.MainModule.FileName -ine [IO.Path]::Combine($SysDir, 'WindowsPowerShell\v1.0\powershell.exe')) { Fail 'HOST_NOT_SYSTEM_POWERSHELL' }
$clrVars = @([Environment]::GetEnvironmentVariables().Keys | ForEach-Object { [string]$_ } | Where-Object { $_ -match '^(COR_ENABLE_PROFILING|COR_PROFILER(_PATH(_32|_64)?)?|COMPLUS_.*|DOTNET_.*|APPDOMAIN_MANAGER_.*)$' })
if ($clrVars.Count -gt 0) { Fail 'CLR_INJECTION_VARIABLES_PRESENT' }
$hkcuAuto = RegValue ([Microsoft.Win32.Registry]::CurrentUser) 'Software\Microsoft\Command Processor' 'AutoRun'
$hklmAuto = RegValue ([Microsoft.Win32.Registry]::LocalMachine) 'Software\Microsoft\Command Processor' 'AutoRun'
$cmdOverride = (RegKeyExists ([Microsoft.Win32.Registry]::CurrentUser) 'Software\Classes\.cmd') -or (RegKeyExists ([Microsoft.Win32.Registry]::CurrentUser) 'Software\Classes\cmdfile')
if (-not [string]::IsNullOrEmpty([string]$hkcuAuto) -or -not [string]::IsNullOrEmpty([string]$hklmAuto) -or $cmdOverride) { Fail 'LAUNCH_HIJACK_SURFACE_PRESENT' }
if ([IO.File]::Exists($Out)) { Fail 'RESULT_ALREADY_EXISTS' }
if (-not [IO.Directory]::Exists($Base)) { Fail 'BASE_MISSING' }
if ((Sddl-OA $Base) -ne $ExpBase) { Fail 'BASE_ACL_UNEXPECTED' }
if ([IO.Directory]::Exists($SupDst)) { Fail 'SUPERVISOR_TARGET_ALREADY_EXISTS' }
if ([IO.Directory]::Exists($ProjDst)) { Fail 'PROJECT_TARGET_ALREADY_EXISTS' }

# Read and verify every source file once; keep the verified bytes.
$verified = New-Object System.Collections.Generic.List[object]
foreach ($n in $Supervisor.Keys) {
    $src = [IO.Path]::Combine($PSScriptRoot, 'supervisor', $n)
    if (-not [IO.File]::Exists($src)) { Fail "SOURCE_MISSING supervisor/$n" }
    $b = [IO.File]::ReadAllBytes($src)
    if ((Sha $b) -ne $Supervisor[$n]) { Fail "SOURCE_SHA_MISMATCH supervisor/$n" }
    $verified.Add([pscustomobject]@{ Dst = [IO.Path]::Combine($SupDst, $n); Rel = "supervisor_formal_v4/$n"; Bytes = $b; Sha = $Supervisor[$n] })
}
foreach ($r in $Project.Keys) {
    $src = [IO.Path]::Combine($PSScriptRoot, 'project', ($r -replace '/', '\'))
    if (-not [IO.File]::Exists($src)) { Fail "SOURCE_MISSING project/$r" }
    $b = [IO.File]::ReadAllBytes($src)
    if ((Sha $b) -ne $Project[$r]) { Fail "SOURCE_SHA_MISMATCH project/$r" }
    $verified.Add([pscustomobject]@{ Dst = [IO.Path]::Combine($ProjDst, ($r -replace '/', '\')); Rel = "project_v4/$r"; Bytes = $b; Sha = $Project[$r] })
}

foreach ($v in $verified) {
    [void][IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($v.Dst))
    $fs = [IO.File]::Open($v.Dst, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
    $fs.Write($v.Bytes, 0, $v.Bytes.Length); $fs.Close()
}
foreach ($d in @($SupDst, $ProjDst)) {
    & ([IO.Path]::Combine($SysDir, 'icacls.exe')) $d /reset /T /C /Q | Out-Null
    if ($LASTEXITCODE -ne 0) { Fail 'ICACLS_RESET_FAILED' }
    & ([IO.Path]::Combine($SysDir, 'icacls.exe')) $d /setowner '*S-1-5-32-544' /T /C /Q | Out-Null
    if ($LASTEXITCODE -ne 0) { Fail 'SETOWNER_FAILED' }
}

$files = @()
foreach ($v in $verified) {
    $b = [IO.File]::ReadAllBytes($v.Dst)
    $files += [ordered]@{ Rel = $v.Rel; Bytes = $b.Length; SHA256 = (Sha $b); MatchesExpected = ((Sha $b) -eq $v.Sha); OwnerAccessSddl = (Sddl-OA $v.Dst) }
}
$res = [ordered]@{
    Kind = 'DSP004_FORMAL_V4_INSTALL_RESULT'; InstalledUtc = [DateTime]::UtcNow.ToString('o')
    InstallerSha256 = (Sha ([IO.File]::ReadAllBytes($PSCommandPath)))
    BaseOwnerAccessSddl = (Sddl-OA $Base); SupervisorDirSddl = (Sddl-OA $SupDst); ProjectDirSddl = (Sddl-OA $ProjDst)
    FileCount = $files.Count; Files = $files; HijackChecks = 'PASSED'
}
$json = Microsoft.PowerShell.Utility\ConvertTo-Json -InputObject $res -Depth 5
$fs = [IO.File]::Open($Out, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
$bytes = (New-Object Text.UTF8Encoding($false)).GetBytes($json); $fs.Write($bytes, 0, $bytes.Length); $fs.Close()
if (@($files | Where-Object { -not $_.MatchesExpected }).Count -gt 0) { Fail 'INSTALLED_SHA_MISMATCH' }
Say "DONE installed=$($files.Count) result=$Out"
exit 0
