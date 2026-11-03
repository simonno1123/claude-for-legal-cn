param([Parameter(Mandatory = $true)][ValidateSet('pre', 'post')][string]$Stage)
# DSP-004 formal-run v2 collector, based on the v4 collector revision 2 (used for 4 runs). Run by the owner, elevated,
# from go_formal_v2.cmd. Changes from v4 r2: the record name is formal_v2_run_record.json; the installed files checked
# are the formal supervisor and project files; the launcher files are go_formal_v2.cmd and collect_formal_v2.ps1.
# (v4 r2 text follows.) v4 repeats the bound v3 supervisor run
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
    'supervisor_formal_v2/supervisor_formal_v2.ps1' = '3463EC1E62193F84605ADD3FF8A8D695C6E92905F5BE1F68423765B5A023E1D3'
    'supervisor_formal_v2/bound_list_formal_v2.json' = '19A1CE8D54AF938F86BF81DFA54AD2DC9719F12E498F0483AC8B0B08D486BF50'
    'supervisor_formal_v2/run_formal_v2.cmd' = 'ADFBB01E415C2238568B615F351EA6A4DA0E6BB988FDD0140730EF49D8200770'
    'project_v2/scripts/phase2_runtime/__init__.py' = '49B8B1BD319B6424323AD0EDC04B3969D71196CD8D69E12C16D5442B17340844'
    'project_v2/scripts/phase2_runtime/route_b_c03/__init__.py' = 'F669613D65267EC5D4D42CB79008EB510307A99B20E40EE13E9E1E0E404A504D'
    'project_v2/scripts/phase2_runtime/route_b_c03/contracts.py' = '7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4'
    'project_v2/scripts/phase2_runtime/route_b_c03/identity_gate.py' = '9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445'
    'project_v2/scripts/phase2_runtime/route_b_c03/mapping.py' = '320F7E8576C1C4E81B4E78E6058000E4D720173948BE736AD846B8CAD664EC66'
    'project_v2/scripts/phase2_runtime/route_b_c03/isolation.py' = '9BC554294D5945188A153F0A5CBEDFAB4E483C95B133683B7517ECC334D4205B'
    'project_v2/scripts/phase2_runtime/route_b_c03/failures.py' = '6F30D996119F61A19B20208FC44C8AF1FB96ADFE09ADE3538675B9D3F2933734'
    'project_v2/scripts/phase2_runtime/route_b_c03/audit.py' = 'A704BDB22C55C92D0909FA0D6A668D8C149724B2A7627938C301758F1D09F561'
    'project_v2/scripts/phase2_runtime/route_b_c03/provider_port.py' = '66E4DA862BBBD50380B17686DB6BC2AB6D5D3B861AB53FCDDE1B608F86DEA381'
    'project_v2/scripts/phase2_runtime/route_b_c03/capability.py' = '028EE9DDD7A2C06840A6F344A4C4CC716EFF95073BE39CA6E57FB7FDBBFA6DD5'
    'project_v2/validation/route_b_c03/wp_008/fixtures/C03-TA-V-001.json' = 'C8CEFEDC496D5D0D33E0F21D61B5E3C3354579A8D0E1C74F70640305C65FC99A'
    'project_v2/validation/route_b_c03/wp_008/fixtures/C03-TA-V-002.json' = '257437A2AA80A58C0741F1EC0A5A514E014C633DD974804C6407DB84DB107290'
    'project_v2/validation/route_b_c03/wp_008/fixtures/C03-TA-V-003.json' = '21BD65ECD28D569BADFF11489017569E8413B1CC9A5138A851F907CCF62EAF7E'
    'project_v2/validation/route_b_c03/wp_008/fixtures/C03-TA-V-004.json' = '9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8'
    'project_v2/validation/route_b_c03/wp_008/fixtures/C03-TA-V-005.json' = '4405ADC2CE242B83120B0BA304157B3E6F03687345F764BBBE1E3A2DCF2422DE'
    'project_v2/validation/route_b_c03/wp_008/fixtures/C03-TA-V-006.json' = '9D24E6AFA92F9EF6E895B0B6E4D0E84BDC326E9C4B815E42723B31374CC2FDC8'
    'project_v2/validation/route_b_c03/wp_008/fixtures/C03-TA-V-007.json' = '68D9D63583A0301BDE76C3E60A5F66B7CCDA897C17D58E8DBF282E3E49C3DB90'
    'project_v2/validation/route_b_c03/wp_008/fixtures/C03-TA-V-008.json' = '7AA3FEF0CCDFA0C6A462C7945B63A50D828AC9C6D0725F428D347F6836075193'
    'project_v2/validation/route_b_c03/wp_008/fixtures/C03-TA-V-009.json' = '34EFBC55490FB2E3FFC89CAFCAD9DD2D319C2C24D9B3E2B026143F74A73DC93C'
    'project_v2/validation/route_b_c03/wp_008/fixtures/C03-TA-V-010.json' = '19DF9D35835F60C03C969B79B25F62CFE95E28C0A1B8122EDD8B9E1A5BC0E67A'
    'project_v2/validation/route_b_c03/wp_008/fixtures/C03-TA-V-011.json' = '8795DA58E092E6DC7F88958E3AC60B754870F5BFAE15FF8BC2D699450B65FDFD'
    'project_v2/validation/route_b_c03/wp_008/fixtures/C03-TA-V-012.json' = '8C6E4FC6279E95CFE48C9E9DA6E161F0AF05CA5FFEA95BE18DBAD6A81204E8E6'
    'project_v2/validation/route_b_c03/wp_008/fixtures/C03-TA-V-013.json' = '3DBF0F60AC970F90C97CF85F5F21F1758B4818D814A02CE8ED03A4F1C3A49CA6'
    'project_v2/validation/route_b_c03/wp_008/fixtures/C03-TA-V-014.json' = 'D3EF698EA45F41824CCF6C5A7020F6A0B495460341ADE7446461A1AAF0E7D523'
    'project_v2/validation/route_b_c03/wp_008/fixtures/C03-TA-V-015.json' = '06DCEBA08CA43C75439B5A2AC1C140905887EF8CDC26C561FBD68E9A001D5AE1'
    'project_v2/validation/route_b_c03/wp_008/DSP_004_INPUT_CANDIDATE_REV4.json' = '685BBCBF13BF96746E6DE4201C1FCE72B667CD6A07D0CE0902D9EF9A6C4235C1'
    'project_v2/validation/route_b_c03/wp_008/dsp004_phase7_formal_v2/harness_rev4.py' = '0B2AC413272D048B75904689C3105B4758A31624356D69FD9CF4B81C622D2394'
}
$Here   = $PSScriptRoot
$Dst    = 'C:\Program Files\DSP004Runtime'
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
$recSrc = [IO.Path]::Combine([string]$prof.GetValue('ProfileImagePath'), 'Documents\dsp004-probe\formal_v2_run_record.json')

$ColDir = [IO.Path]::Combine($Here, "collected_$($Stage)_$Inv")
if ([IO.Directory]::Exists($ColDir)) { Fail 'COLLECTED_DIR_ALREADY_EXISTS' }
[void][IO.Directory]::CreateDirectory($ColDir)
$res = [ordered]@{ Kind = 'DSP004_FORMAL_V2_COLLECT_RESULT'; Stage = $Stage; Invocation = $Inv; CollectedUtc = (Utc ([DateTime]::UtcNow)) }
$res.CollectorSha256 = Sha ([IO.File]::ReadAllBytes($PSCommandPath))
$launch = @()
foreach ($n in @('go_formal_v2.cmd', 'collect_formal_v2.ps1')) {
    $p = [IO.Path]::Combine($Here, $n)
    $launch += [ordered]@{ Name = $n; SHA256 = $(if ([IO.File]::Exists($p)) { Sha ([IO.File]::ReadAllBytes($p)) } else { 'MISSING' }) }
}
$res.LauncherFilesNow = $launch

function Move-Record {
    $script:res.RunRecordFound = [IO.File]::Exists($recSrc)
    if (-not $script:res.RunRecordFound) { return }
    $lw = [IO.File]::GetLastWriteTimeUtc($recSrc)
    $rb = [IO.File]::ReadAllBytes($recSrc)
    $dstRec = [IO.Path]::Combine($ColDir, 'formal_v2_run_record.json')
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

# Installed formal supervisor and project files.
$files = @()
foreach ($n in $Expected.Keys) {
    $p = [IO.Path]::Combine($Dst, ($n -replace '/', '\'))
    $h = $(if ([IO.File]::Exists($p)) { Sha ([IO.File]::ReadAllBytes($p)) } else { 'MISSING' })
    $files += [ordered]@{ Name = $n; SHA256 = $h; MatchesExpected = ($h -eq $Expected[$n]) }
}
$res.InstalledFiles = $files

# Window start: the creation of the current dsp004val account (event 4720 whose TargetSid is this account's SID).
# Revision 2: revision 1 required exactly one 4720 named dsp004val and stopped on finding two. All 4720 (created) and
# 4726 (deleted) events for the name are exported; the window starts at the one for the current SID.
$named = @(Events "*[System[EventID=4720] and EventData[Data[@Name='TargetUserName']='dsp004val']]")
$created = @($named | Where-Object { (DataMap $_)['TargetSid'] -eq $sid } | Sort-Object -Property RecordId)
$res.AccountCreationEvents = [ordered]@{ Named = $named.Count; ForCurrentSid = $created.Count; TimesUtc = @($named | ForEach-Object { Utc $_.TimeCreated }) }
if ($created.Count -lt 1) { Fail 'ACCOUNT_CREATION_EVENT_FOR_SID_MISSING' }   # if several, the earliest is used; all are exported
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
    "*[System[(EventID=4720 or EventID=4726)] and EventData[Data[@Name='TargetUserName']='dsp004val']]",
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
$sup = @($sum | Where-Object { $_.Id -eq 4688 -and ([string]$_.CommandLine) -like '*\supervisor_formal_v2\supervisor_formal_v2.ps1*' }).Count
$instOk = (@($files | Where-Object { -not $_.MatchesExpected }).Count -eq 0)
Say "COLLECTED record=$($res.RunRecordFound) supervisor_runs_in_history=$sup boots=$($integ.Event4608.Count) record_gaps=$gaps installed_match=$instOk"
if (-not $res.RunRecordFound) { Say 'STOP RUN_RECORD_NOT_FOUND'; exit 3 }
if (-not $res.SecurityLog.OldestBeforeWindow -or -not $res.RecordNumbers.FirstIsCreation -or $gaps -ne 0) { Say 'STOP LOG_DOES_NOT_COVER_WINDOW_OR_HAS_GAPS'; exit 4 }
if (-not $instOk) { Say 'STOP INSTALLED_FILES_CHANGED'; exit 5 }
exit 0
