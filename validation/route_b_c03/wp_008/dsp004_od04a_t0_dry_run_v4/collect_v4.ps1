param([Parameter(Mandatory = $true)][ValidateSet('pre', 'post')][string]$Stage)
# DSP-004 OD04-A v4 collector. Run by the owner, elevated, from go_v4.cmd. v4 repeats the bound v3 supervisor run
# (unchanged, already installed) and collects audit evidence over the run account's whole history.
#   pre : moves an earlier run record out of the dsp004val profile (the v3 supervisor refuses to overwrite one), and
#         records its hash. Nothing else. "Move" = read bytes, write a new file here, re-read and compare, then delete the
#         profile copy, so the new file gets this folder's ordinary permissions.
#   post: moves the new run record out; hashes the launcher files as they are at collection time and the installed v3
#         files; exports, for the whole life of dsp004val (from its creation event 4720), every 4688/4689 by or for
#         dsp004val, its logon events (4624/4625/4634/4647/4648/4672), system start-ups (4608), audit-policy changes (4719,
#         full events), counts of 1102/4616/1100/1104/1105/1108, and every Security record number from the 4720 record on,
#         to show none are missing. The record is moved only after all queries succeed.
# It changes nothing else on the machine.
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version 2
$PSModuleAutoLoadingPreference = 'None'
$env:PSModulePath = [IO.Path]::Combine($PSHOME, 'Modules')
Import-Module ([IO.Path]::Combine($PSHOME, 'Modules\Microsoft.PowerShell.Utility\Microsoft.PowerShell.Utility.psd1'))
Import-Module ([IO.Path]::Combine($PSHOME, 'Modules\Microsoft.PowerShell.Security\Microsoft.PowerShell.Security.psd1'))
Import-Module ([IO.Path]::Combine($PSHOME, 'Modules\Microsoft.PowerShell.Diagnostics\Microsoft.PowerShell.Diagnostics.psd1'))
Microsoft.PowerShell.Utility\Add-Type -AssemblyName System.Management

$Expected = [ordered]@{
    'supervisor_v3.ps1'  = '7CC3EC3D0432BFFE3D9ADAA34D90ED10DB015F5AFC241221E77E517B69C9E433'
    'probe_v3.py'        = '3AF5FD03B9487642A7256EAA21D654F6BF072749EBAF03B967A3E307C34CB2A3'
    'bound_list_v3.json' = '0A349A6DBDA8B1397941EDE195D6D76E5B77DBE252BA6D3B80E0516016AAE561'
    'run_v3.cmd'         = 'B430D9B22CACEDEEAE9C3124916ECFF8FD023EFABAE8D870920ECD2DAE64195A'
}
$Here   = $PSScriptRoot
$Dst    = 'C:\Program Files\DSP004Runtime\supervisor_v3'
$SysDir = [Environment]::GetFolderPath('System')
$Inv    = [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssZ', [Globalization.CultureInfo]::InvariantCulture)

function Say([string]$s) { [Console]::WriteLine($s) }
function Fail([string]$c) { Say "STOP $c"; exit 2 }
function Sha([byte[]]$b) { return ([BitConverter]::ToString([Security.Cryptography.SHA256]::Create().ComputeHash($b)) -replace '-', '') }
function Write-NewFile([string]$p, [byte[]]$b) { $fs = [IO.File]::Open($p, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None); $fs.Write($b, 0, $b.Length); $fs.Close() }
function Events([string]$xp) {
    try { return @(Microsoft.PowerShell.Diagnostics\Get-WinEvent -LogName Security -FilterXPath $xp) }
    catch { if ($_.FullyQualifiedErrorId -like 'NoMatchingEventsFound*') { return @() } else { throw } }
}
function DataMap($ev) {
    $d = @{}; $x = [xml]$ev.ToXml()
    $ns = New-Object Xml.XmlNamespaceManager($x.NameTable); $ns.AddNamespace('e', 'http://schemas.microsoft.com/win/2004/08/events/event')
    foreach ($n in $x.SelectNodes('//e:EventData/e:Data', $ns)) { $d[$n.GetAttribute('Name')] = $n.InnerText }
    return $d
}
function RecordIds([string]$xp) {
    # Streams record numbers only (no message rendering).
    $ids = New-Object System.Collections.Generic.List[int64]
    $rd = New-Object System.Diagnostics.Eventing.Reader.EventLogReader((New-Object System.Diagnostics.Eventing.Reader.EventLogQuery('Security', [System.Diagnostics.Eventing.Reader.PathType]::LogName, $xp)))
    try { while ($true) { $r = $rd.ReadEvent(); if ($r -eq $null) { break }; $ids.Add([int64]$r.RecordId); $r.Dispose() } } finally { $rd.Dispose() }
    return ,$ids
}
function RunAccountSupervisorActive {
    $s = New-Object System.Management.ManagementObjectSearcher("SELECT ProcessId,CommandLine FROM Win32_Process WHERE Name='powershell.exe'")
    foreach ($p in @($s.Get())) {
        try { $o = $p.InvokeMethod('GetOwner', $null) } catch { continue }
        if ($o -ne $null -and [string]$o['User'] -ieq 'dsp004val') { return $true }
    }
    return $false
}
function Utc($dt) { return $dt.ToUniversalTime().ToString('o') }

$admin = (New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $admin) { Fail 'NOT_ELEVATED' }

$sid = (New-Object Security.Principal.NTAccount([Environment]::MachineName, 'dsp004val')).Translate([Security.Principal.SecurityIdentifier]).Value
$prof = [Microsoft.Win32.Registry]::LocalMachine.OpenSubKey("SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\$sid")
if ($prof -eq $null) { Fail 'RUN_ACCOUNT_PROFILE_MISSING' }
$recSrc = [IO.Path]::Combine([string]$prof.GetValue('ProfileImagePath'), 'Documents\dsp004-probe\v3_run_record.json')

$ColDir = [IO.Path]::Combine($Here, "collected_$($Stage)_$Inv")
if ([IO.Directory]::Exists($ColDir)) { Fail 'COLLECTED_DIR_ALREADY_EXISTS' }
[void][IO.Directory]::CreateDirectory($ColDir)
$res = [ordered]@{ Kind = 'DSP004_OD04A_V4_COLLECT_RESULT'; Stage = $Stage; Invocation = $Inv; CollectedUtc = (Utc ([DateTime]::UtcNow)) }
$res.CollectorSha256 = Sha ([IO.File]::ReadAllBytes($PSCommandPath))
$launch = @()
foreach ($n in @('go_v4.cmd', 'collect_v4.ps1')) {
    $p = [IO.Path]::Combine($Here, $n)
    $launch += [ordered]@{ Name = $n; SHA256 = $(if ([IO.File]::Exists($p)) { Sha ([IO.File]::ReadAllBytes($p)) } else { 'MISSING' }) }
}
$res.LauncherFilesNow = $launch

function Move-Record {
    $script:res.RunRecordFound = [IO.File]::Exists($recSrc)
    if (-not $script:res.RunRecordFound) { return }
    $lw = [IO.File]::GetLastWriteTimeUtc($recSrc)
    $rb = [IO.File]::ReadAllBytes($recSrc)
    $dstRec = [IO.Path]::Combine($ColDir, 'v3_run_record.json')
    Write-NewFile $dstRec $rb
    $back = [IO.File]::ReadAllBytes($dstRec)
    if ((Sha $back) -ne (Sha $rb)) { Fail 'RECORD_COPY_MISMATCH' }
    [IO.File]::Delete($recSrc)
    $script:res.RunRecord = [ordered]@{ Bytes = $rb.Length; SHA256 = (Sha $rb); SourceLastWriteUtc = (Utc $lw) }
}
if ($Stage -eq 'pre') {
    Move-Record
    $json = Microsoft.PowerShell.Utility\ConvertTo-Json -InputObject $res -Depth 6
    Write-NewFile ([IO.Path]::Combine($ColDir, 'collect_result.json')) ((New-Object Text.UTF8Encoding($false)).GetBytes($json))
    Say "PRE moved_record=$($res.RunRecordFound)"
    exit 0
}

# Wait (up to 3 minutes) until no dsp004val PowerShell is running, so a late record is not missed.
$waited = 0
while ((RunAccountSupervisorActive) -and $waited -lt 180) { Start-Sleep -Seconds 5; $waited += 5 }
if (RunAccountSupervisorActive) { Fail 'RUN_STILL_ACTIVE' }
$res.WaitedSeconds = $waited

# Installed v3 files.
$files = @()
foreach ($n in $Expected.Keys) {
    $p = [IO.Path]::Combine($Dst, $n)
    $h = $(if ([IO.File]::Exists($p)) { Sha ([IO.File]::ReadAllBytes($p)) } else { 'MISSING' })
    $files += [ordered]@{ Name = $n; SHA256 = $h; MatchesExpected = ($h -eq $Expected[$n]) }
}
$res.InstalledFiles = $files

# Window start: the creation of dsp004val (event 4720).
$created = @(Events "*[System[EventID=4720] and EventData[Data[@Name='TargetUserName']='dsp004val']]")
if ($created.Count -ne 1) { Fail "ACCOUNT_CREATION_EVENTS_$($created.Count)" }
$since = $created[0].TimeCreated.ToUniversalTime()
$t = $since.ToString('yyyy-MM-ddTHH:mm:ss.fffZ', [Globalization.CultureInfo]::InvariantCulture)
$res.WindowStartUtc = Utc $since

# Run-account events over the whole window (each query has one EventData condition; results merged by record number).
$sel = @{}
$queries = @(
    "*[System[(EventID=4688 or EventID=4689)] and EventData[Data[@Name='SubjectUserName']='dsp004val']]",
    "*[System[(EventID=4688)] and EventData[Data[@Name='TargetUserName']='dsp004val']]",
    "*[System[(EventID=4624 or EventID=4625 or EventID=4634 or EventID=4647 or EventID=4648)] and EventData[Data[@Name='TargetUserName']='dsp004val']]",
    "*[System[(EventID=4672)] and EventData[Data[@Name='SubjectUserName']='dsp004val']]",
    "*[System[EventID=4719 and TimeCreated[@SystemTime>='$t']]]",
    "*[System[EventID=4720] and EventData[Data[@Name='TargetUserName']='dsp004val']]",
    "*[System[EventID=4608 and TimeCreated[@SystemTime>='$t']]]"
)
foreach ($q in $queries) { foreach ($ev in (Events $q)) { $sel[[int64]$ev.RecordId] = $ev } }
$keys = @($sel.Keys | Sort-Object)
$xmlParts = New-Object System.Collections.Generic.List[string]
$sum = New-Object System.Collections.Generic.List[object]
foreach ($k in $keys) {
    $ev = $sel[$k]; $xmlParts.Add($ev.ToXml()); $d = DataMap $ev
    $sum.Add([ordered]@{ Id = $ev.Id; RecordId = $ev.RecordId; TimeUtc = (Utc $ev.TimeCreated); NewProcessName = $d['NewProcessName']; NewProcessId = $d['NewProcessId']; ProcessId = $d['ProcessId']; CommandLine = $d['CommandLine']; LogonType = $d['LogonType']; TargetLogonId = $d['TargetLogonId'] })
}
$xmlBytes = (New-Object Text.UTF8Encoding($false)).GetBytes('<Events>' + ($xmlParts -join '') + '</Events>')
Write-NewFile ([IO.Path]::Combine($ColDir, 'events_dsp004val_history.xml')) $xmlBytes
$res.EventsXml = [ordered]@{ Bytes = $xmlBytes.Length; SHA256 = (Sha $xmlBytes); Events = $keys.Count }
$res.EventSummary = $sum

# Every Security record number from the 4720 record on, selected by number (not time): contiguous means none removed.
$firstId = [int64]$created[0].RecordId
$ids = RecordIds "*[System[EventRecordID>=$firstId]]"
$ids.Sort()
$gapList = New-Object System.Collections.Generic.List[string]
for ($i = 1; $i -lt $ids.Count; $i++) { if ($ids[$i] -ne $ids[$i - 1] + 1) { $gapList.Add("$($ids[$i - 1])-$($ids[$i])") } }
$gaps = $gapList.Count
$res.RecordNumbers = [ordered]@{ CreationRecordId = $firstId; Count = $ids.Count; First = $(if ($ids.Count) { $ids[0] } else { $null }); Last = $(if ($ids.Count) { $ids[$ids.Count - 1] } else { $null }); Gaps = $gaps; GapRanges = $gapList; FirstIsCreation = ($ids.Count -gt 0 -and $ids[0] -eq $firstId) }

$integ = [ordered]@{}
foreach ($id in @(1102, 4719, 4616, 4608, 1100, 1104, 1105, 1108)) {
    $e = @(Events "*[System[EventID=$id and TimeCreated[@SystemTime>='$t']]]")
    $integ["Event$id"] = [ordered]@{ Count = $e.Count; TimesUtc = @($e | ForEach-Object { Utc $_.TimeCreated }) }
}
$res.IntegrityEvents = $integ
$log = Microsoft.PowerShell.Diagnostics\Get-WinEvent -ListLog Security
$oldest = @(Microsoft.PowerShell.Diagnostics\Get-WinEvent -LogName Security -MaxEvents 1 -Oldest)
$res.SecurityLog = [ordered]@{ RecordCount = $log.RecordCount; MaximumSizeInBytes = $log.MaximumSizeInBytes; FileSize = $log.FileSize; LogMode = [string]$log.LogMode; OldestEventUtc = $(if ($oldest.Count) { Utc $oldest[0].TimeCreated } else { $null }) }
$res.SecurityLog.OldestBeforeWindow = ($oldest.Count -gt 0) -and ($oldest[0].TimeCreated.ToUniversalTime() -le $since)
$k2 = [Microsoft.Win32.Registry]::LocalMachine.OpenSubKey('Software\Microsoft\Windows\CurrentVersion\Policies\System\Audit')
$res.IncludeCmdLine = $(if ($k2) { $k2.GetValue('ProcessCreationIncludeCmdLine_Enabled') } else { $null })

Move-Record
$json = Microsoft.PowerShell.Utility\ConvertTo-Json -InputObject $res -Depth 6
Write-NewFile ([IO.Path]::Combine($ColDir, 'collect_result.json')) ((New-Object Text.UTF8Encoding($false)).GetBytes($json))
$sup = @($sum | Where-Object { $_.Id -eq 4688 -and ([string]$_.CommandLine) -like '*\supervisor_v3\supervisor_v3.ps1*' }).Count
$instOk = (@($files | Where-Object { -not $_.MatchesExpected }).Count -eq 0)
Say "COLLECTED record=$($res.RunRecordFound) supervisor_runs_in_history=$sup boots=$($integ.Event4608.Count) record_gaps=$gaps installed_match=$instOk"
if (-not $res.RunRecordFound) { Say 'STOP RUN_RECORD_NOT_FOUND'; exit 3 }
if (-not $res.SecurityLog.OldestBeforeWindow -or -not $res.RecordNumbers.FirstIsCreation -or $gaps -ne 0) { Say 'STOP LOG_DOES_NOT_COVER_WINDOW_OR_HAS_GAPS'; exit 4 }
if (-not $instOk) { Say 'STOP INSTALLED_FILES_CHANGED'; exit 5 }
exit 0
