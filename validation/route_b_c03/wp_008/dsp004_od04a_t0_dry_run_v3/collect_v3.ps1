# DSP-004 OD04-A v3 collector. Run by the owner, elevated, from go_v3.cmd after the dsp004val run window closes.
# Copies the run record out of the dsp004val profile, re-hashes the installed v3 files, and exports the Windows
# Security log events written by the system for the run window: 4688/4689 (process creation/exit), plus counts of
# 1102 (log cleared), 4719 (audit policy changed) and 4616 (system time changed). It changes nothing on the machine.
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version 2
$PSModuleAutoLoadingPreference = 'None'
$env:PSModulePath = [IO.Path]::Combine($PSHOME, 'Modules')
Import-Module ([IO.Path]::Combine($PSHOME, 'Modules\Microsoft.PowerShell.Utility\Microsoft.PowerShell.Utility.psd1'))
Import-Module ([IO.Path]::Combine($PSHOME, 'Modules\Microsoft.PowerShell.Security\Microsoft.PowerShell.Security.psd1'))
Import-Module ([IO.Path]::Combine($PSHOME, 'Modules\Microsoft.PowerShell.Diagnostics\Microsoft.PowerShell.Diagnostics.psd1'))

$Expected = [ordered]@{
    'supervisor_v3.ps1'  = '7CC3EC3D0432BFFE3D9ADAA34D90ED10DB015F5AFC241221E77E517B69C9E433'
    'probe_v3.py'        = '3AF5FD03B9487642A7256EAA21D654F6BF072749EBAF03B967A3E307C34CB2A3'
    'bound_list_v3.json' = '0A349A6DBDA8B1397941EDE195D6D76E5B77DBE252BA6D3B80E0516016AAE561'
    'run_v3.cmd'         = 'B430D9B22CACEDEEAE9C3124916ECFF8FD023EFABAE8D870920ECD2DAE64195A'
}
$Here    = $PSScriptRoot
$Dst     = 'C:\Program Files\DSP004Runtime\supervisor_v3'
$SysDir  = [Environment]::GetFolderPath('System')
$Out     = [IO.Path]::Combine($Here, 'collect_v3_result.json')
$ColDir  = [IO.Path]::Combine($Here, 'collected')

function Say([string]$s) { [Console]::WriteLine($s) }
function Fail([string]$c) { Say "STOP $c"; exit 2 }
function Sha([byte[]]$b) { return ([BitConverter]::ToString([Security.Cryptography.SHA256]::Create().ComputeHash($b)) -replace '-', '') }
function Write-NewFile([string]$p, [byte[]]$b) { $fs = [IO.File]::Open($p, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None); $fs.Write($b, 0, $b.Length); $fs.Close() }
function Events([string]$xp) {
    try { return @(Microsoft.PowerShell.Diagnostics\Get-WinEvent -LogName Security -FilterXPath $xp) }
    catch { if ($_.FullyQualifiedErrorId -like 'NoMatchingEventsFound*') { return @() } else { throw } }
}

$admin = (New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $admin) { Fail 'NOT_ELEVATED' }
if ([IO.File]::Exists($Out)) { Fail 'RESULT_ALREADY_EXISTS' }
if ([IO.Directory]::Exists($ColDir)) { Fail 'COLLECTED_DIR_ALREADY_EXISTS' }
$instP = [IO.Path]::Combine($Here, 'install_v3_result.json')
if (-not [IO.File]::Exists($instP)) { Fail 'INSTALL_RESULT_MISSING' }
$inst = Microsoft.PowerShell.Utility\ConvertFrom-Json -InputObject ([IO.File]::ReadAllText($instP))
$sinceUtc = [DateTime]::Parse($inst.InstalledUtc).ToUniversalTime().AddMinutes(-1)
$untilUtc = [DateTime]::UtcNow
[void][IO.Directory]::CreateDirectory($ColDir)
$res = [ordered]@{ Kind = 'DSP004_OD04A_V3_COLLECT_RESULT'; CollectedUtc = $untilUtc.ToString('o'); WindowStartUtc = $sinceUtc.ToString('o'); WindowEndUtc = $untilUtc.ToString('o') }
$res.CollectorSha256 = Sha ([IO.File]::ReadAllBytes($PSCommandPath))

# 1. Run record from the dsp004val profile.
$sid = (New-Object Security.Principal.NTAccount([Environment]::MachineName, 'dsp004val')).Translate([Security.Principal.SecurityIdentifier]).Value
$prof = [Microsoft.Win32.Registry]::LocalMachine.OpenSubKey("SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\$sid")
$profPath = $(if ($prof) { [string]$prof.GetValue('ProfileImagePath') } else { $null })
$recSrc = $(if ($profPath) { [IO.Path]::Combine($profPath, 'Documents\dsp004-probe\v3_run_record.json') } else { $null })
$res.RunRecordFound = ($recSrc -ne $null) -and [IO.File]::Exists($recSrc)
if ($res.RunRecordFound) {
    $rb = [IO.File]::ReadAllBytes($recSrc)
    Write-NewFile ([IO.Path]::Combine($ColDir, 'v3_run_record.json')) $rb
    $res.RunRecord = [ordered]@{ Bytes = $rb.Length; SHA256 = (Sha $rb); SourceLastWriteUtc = [IO.File]::GetLastWriteTimeUtc($recSrc).ToString('o') }
}

# 2. Installed v3 files after the run.
$files = @()
foreach ($n in $Expected.Keys) {
    $p = [IO.Path]::Combine($Dst, $n)
    $h = $(if ([IO.File]::Exists($p)) { Sha ([IO.File]::ReadAllBytes($p)) } else { 'MISSING' })
    $files += [ordered]@{ Name = $n; SHA256 = $h; MatchesExpected = ($h -eq $Expected[$n]) }
}
$res.InstalledFilesAfterRun = $files

# 3. System-written events for the window. The .evtx export holds every account's events in the window and is
#    kept on this machine only (never committed); the filtered XML holds only dsp004val's events.
$t = $sinceUtc.ToString('yyyy-MM-ddTHH:mm:ss.fffZ', [Globalization.CultureInfo]::InvariantCulture)
$xpProc = "*[System[(EventID=4688 or EventID=4689) and TimeCreated[@SystemTime>='$t']]]"
$all = @(Events $xpProc)
$keep = New-Object System.Collections.Generic.List[string]
$sum = New-Object System.Collections.Generic.List[object]
foreach ($ev in $all) {
    $x = $ev.ToXml(); $doc = [xml]$x
    $d = @{}
    foreach ($n in $doc.Event.EventData.Data) { $d[$n.GetAttribute('Name')] = $n.InnerText }
    $subj = [string]$d['SubjectUserName']; $targ = [string]$d['TargetUserName']
    if ($subj -ieq 'dsp004val' -or $targ -ieq 'dsp004val') {
        $keep.Add($x)
        $sum.Add([ordered]@{ Id = $ev.Id; RecordId = $ev.RecordId; TimeUtc = $ev.TimeCreated.ToUniversalTime().ToString('o'); NewProcessName = $d['NewProcessName']; ProcessName = $d['ProcessName']; NewProcessId = $d['NewProcessId']; ProcessId = $d['ProcessId']; CommandLine = $d['CommandLine']; Status = $d['Status']; TokenElevationType = $d['TokenElevationType']; MandatoryLabel = $d['MandatoryLabel'] })
    }
}
$xmlBytes = (New-Object Text.UTF8Encoding($false)).GetBytes('<Events>' + ($keep -join '') + '</Events>')
Write-NewFile ([IO.Path]::Combine($ColDir, 'events_dsp004val.xml')) $xmlBytes
$res.ProcessEventsInWindow = $all.Count
$res.ProcessEventsForRunAccount = $keep.Count
$res.EventsXml = [ordered]@{ Bytes = $xmlBytes.Length; SHA256 = (Sha $xmlBytes) }
$res.EventSummary = $sum
$evtx = [IO.Path]::Combine($ColDir, 'window_4688_4689.evtx')
& ([IO.Path]::Combine($SysDir, 'wevtutil.exe')) epl Security $evtx "/q:$xpProc"
if ($LASTEXITCODE -ne 0) { $res.EvtxExport = "FAILED $LASTEXITCODE" } else { $res.EvtxExport = [ordered]@{ Bytes = (New-Object IO.FileInfo($evtx)).Length; SHA256 = (Sha ([IO.File]::ReadAllBytes($evtx))) } }

$integ = [ordered]@{}
foreach ($id in @(1102, 4719, 4616)) {
    $e = @(Events "*[System[EventID=$id and TimeCreated[@SystemTime>='$t']]]")
    $integ["Event$id"] = [ordered]@{ Count = $e.Count; TimesUtc = @($e | ForEach-Object { $_.TimeCreated.ToUniversalTime().ToString('o') }) }
}
$res.IntegrityEvents = $integ
$log = Microsoft.PowerShell.Diagnostics\Get-WinEvent -ListLog Security
$oldest = @(Microsoft.PowerShell.Diagnostics\Get-WinEvent -LogName Security -MaxEvents 1 -Oldest)
$res.SecurityLog = [ordered]@{ RecordCount = $log.RecordCount; MaximumSizeInBytes = $log.MaximumSizeInBytes; FileSize = $log.FileSize; LogMode = [string]$log.LogMode; IsLogFull = $log.IsLogFull; OldestEventUtc = $(if ($oldest.Count) { $oldest[0].TimeCreated.ToUniversalTime().ToString('o') } else { $null }) }
$res.SecurityLog.OldestBeforeWindow = ($res.SecurityLog.OldestEventUtc -ne $null) -and ([DateTime]::Parse($res.SecurityLog.OldestEventUtc).ToUniversalTime() -le $sinceUtc)
$res.AuditPolicyCsv = @(& ([IO.Path]::Combine($SysDir, 'auditpol.exe')) /get '/subcategory:{0CCE922B-69AE-11D9-BED3-505054503030},{0CCE922C-69AE-11D9-BED3-505054503030}' /r)
$cmdLineVal = $null; $k = [Microsoft.Win32.Registry]::LocalMachine.OpenSubKey('Software\Microsoft\Windows\CurrentVersion\Policies\System\Audit')
if ($k) { $cmdLineVal = $k.GetValue('ProcessCreationIncludeCmdLine_Enabled'); $k.Close() }
$res.IncludeCmdLine = $cmdLineVal

$json = Microsoft.PowerShell.Utility\ConvertTo-Json -InputObject $res -Depth 6
Write-NewFile $Out ((New-Object Text.UTF8Encoding($false)).GetBytes($json))
$pyEv = @($sum | Where-Object { $_.Id -eq 4688 -and ([string]$_.NewProcessName) -like '*\DSP004Runtime\Python312\python.exe' })
$py = $pyEv.Count
$pyCmd = @($pyEv | Where-Object { -not [string]::IsNullOrEmpty([string]$_.CommandLine) }).Count
$instOk = (@($files | Where-Object { -not $_.MatchesExpected }).Count -eq 0)
Say "COLLECTED record=$($res.RunRecordFound) events=$($keep.Count) python_starts=$py with_cmdline=$pyCmd installed_match=$instOk"
if (-not $res.RunRecordFound) { Say 'STOP RUN_RECORD_NOT_FOUND'; exit 3 }
if ($py -ne 3 -or $pyCmd -ne 3) { Say 'STOP AUDIT_EVENTS_NOT_AS_EXPECTED'; exit 4 }
if (-not $instOk) { Say 'STOP INSTALLED_FILES_CHANGED'; exit 5 }
exit 0
