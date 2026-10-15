# Fixed archive reconciliation only. No test subject, child stage, Python or C# execution.
Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'
$WarningPreference='Stop'
$PSModuleAutoLoadingPreference='None'
Import-Module -Name ([IO.Path]::Combine($PSHOME,'Modules','Microsoft.PowerShell.Utility','Microsoft.PowerShell.Utility.psd1')) -ErrorAction Stop
$root='C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/'
$utf8=[Text.UTF8Encoding]::new($false,$true)
[Console]::OutputEncoding=$utf8
$OutputEncoding=$utf8
$anchors='[{"Path":"docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_LOCAL_COMPOSITION_REV2_RESULT.md","SHA256":"C44D9C96C4F6E2D74CE9EC0F0019BEC07F1D541F0E916EC184ECEB0BED8DEE8A","Bytes":12221,"Rows":19},{"Path":"docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_REV2_STAGE_TRANSPORT_FAULT_REV1_RESULT.md","SHA256":"33A920C3D3F8550F4B4CA3B2F1AC1CC0D9476F704A18E143B2D7BA51DE3BC53C","Bytes":10158,"Rows":3},{"Path":"docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_CLOSED_RECORD_JSON_REV1_RESULT.md","SHA256":"8522AC8662C0617EB92CE1A3F65D7A9255AEFB998E4ED8DEB842B88B6911E203","Bytes":8849,"Rows":3},{"Path":"docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_JSON_GATE_CONVERSION_BOUNDARY_REV1_RESULT.md","SHA256":"D175EF4828094A5ED4C729987EEC92C642EE711FAE58C2CE98F5F14AFF2E19CC","Bytes":12980,"Rows":9},{"Path":"docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_BOUNDED_READ_BOUNDARY_REV1_RESULT.md","SHA256":"9B47CA2BEC57B30B4BD34EDF25E7E5A8D552048F203516158BCFD4B7EC65E611","Bytes":10338,"Rows":4},{"Path":"docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_EXCEPTION_RETENTION_REPRESENTATION_REV1_RESULT.md","SHA256":"AD097F7ED78BACEE6CF401FCDC6162F01289B0C6E7075AD783C73E47B846A19D","Bytes":10403,"Rows":3}]'|Microsoft.PowerShell.Utility\ConvertFrom-Json -Depth 12
$references='[{"Path":"docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_OPERATIONAL_VALIDATION_PLAN.md","SHA256":"E9643D0993532A1E1603B66F95CD288F394BDDA621EFB6784B256CECFC915E6D","Bytes":23939,"Role":"HISTORICAL_REQUIREMENT_REFERENCE_ONLY_NOT_CURRENT_AUTHORITY"},{"Path":"docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_2_CANDIDATE.md","SHA256":"6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA","Bytes":54703,"Role":"HISTORICAL_REQUIREMENT_REFERENCE_ONLY_NOT_CURRENT_AUTHORITY"}]'|Microsoft.PowerShell.Utility\ConvertFrom-Json -Depth 12
$specs='[{"Id":"AR-001","Path":"validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_REV2_OBSERVED_RESULT.json","FileSHA256":"3DB42CBCAA7C361B78CC1C29719BE6A76009A79DAE4FB0304FF4A93D45D672A4","FileBytes":45615,"FullSHA256":"CB06EC4381F57F19B5C043B60935104D9C4AB0A6AA99FD395321750A387D09F5","FullBytes":391606,"Mode":"COMPOSITION","ExpectedOutcome":"LOCAL_SYNTHETIC_COMPOSITION_CHECKS_PASS","CheckCount":2027,"CaseCount":189,"Unit":"RECORDED_PLAN_ITEM_IDS","RawExpected":false},{"Id":"AR-002","Path":"validation/route_b_c03/wp_008/DSP_004_REV2_STAGE_TRANSPORT_FAULT_REV1_OBSERVED_RESULT.json","FileSHA256":"8F36D01BBCA45333A147C7E6901ECA1755A6528852A6A5C40E6185198686AB54","FileBytes":25734,"FullSHA256":"BB5FCB40C5B45B90982E7ED96E645D6CC2382F12E6084A39B59BB6F8B904D94D","FullBytes":22038,"Mode":"FLAT_FAULT","ExpectedOutcome":"LOCAL_PRIVATE_STAGE_TRANSPORT_FAULT_CHECKS_PASS","CheckCount":89,"CaseCount":8,"Unit":"LOCAL_SYNTHETIC_CASES","RawExpected":false},{"Id":"AR-003","Path":"validation/route_b_c03/wp_008/DSP_004_CLOSED_RECORD_JSON_REV1_OBSERVED_RESULT.json","FileSHA256":"081F5C2D2A42F2C693555C57875769F996FB4BDD65163EA7213446E9F96FB693","FileBytes":5410,"FullSHA256":"17B31E7FD9B73DE9C1C8232C45AF1E406DB7924893E11C6EF5D200C279187F01","FullBytes":20041,"Mode":"NESTED","ExpectedOutcome":"LOCAL_CLOSED_JSON_DECODER_CHECKS_PASS","CheckCount":94,"CaseCount":24,"Unit":"LOCAL_SYNTHETIC_CASES","RawExpected":false},{"Id":"AR-004","Path":"validation/route_b_c03/wp_008/DSP_004_JSON_GATE_CONVERSION_BOUNDARY_REV1_OBSERVED_RESULT.json","FileSHA256":"5462F44C2E9F463C104FFC83FC83ADDA021DBC9EFA842775A2B8CE22C3CDFB93","FileBytes":11614,"FullSHA256":"E7EE623FA1E10A4A88F4942418ADDE41B1BBD695AD33B85DD6DBB61D36A7041F","FullBytes":27650,"Mode":"NESTED","ExpectedOutcome":"LOCAL_JSON_GATE_CONVERSION_BOUNDARY_CHECKS_PASS","CheckCount":137,"CaseCount":24,"Unit":"LOCAL_SYNTHETIC_CASES","RawExpected":true},{"Id":"AR-005","Path":"validation/route_b_c03/wp_008/DSP_004_BOUNDED_READ_BOUNDARY_REV1_OBSERVED_RESULT.json","FileSHA256":"6FDAB9BC2DCD79A8D290D0E417311CD5FCA79E199DA83E42F1AB2A09AE596B52","FileBytes":11272,"FullSHA256":"B3655E83D38933D921C8F692B7F33F5F5138F9FFA68B3305CEDBFD6146A4C174","FullBytes":40004,"Mode":"NESTED","ExpectedOutcome":"LOCAL_SYNTHETIC_BOUNDED_READ_CHECKS_PASS","CheckCount":187,"CaseCount":20,"Unit":"LOCAL_SYNTHETIC_CASES","RawExpected":true},{"Id":"AR-006","Path":"validation/route_b_c03/wp_008/DSP_004_EXCEPTION_RETENTION_REPRESENTATION_REV1_OBSERVED_RESULT.json","FileSHA256":"2E0D13BEED92826DA17957D897499B6E04D3EAB7E31BDAEE9F46AB713BB397A0","FileBytes":7304,"FullSHA256":"7F344983F8DCC104C5658D651B065AEDC6CE405B8E2ED37F1F61F7E17ACD32C6","FullBytes":18809,"Mode":"NESTED","ExpectedOutcome":"LOCAL_EXCEPTION_REPRESENTATION_AND_TASK_OBSERVER_CHECKS_PASS","CheckCount":77,"CaseCount":13,"Unit":"LOCAL_SYNTHETIC_CASES","RawExpected":true}]'|Microsoft.PowerShell.Utility\ConvertFrom-Json -Depth 12
$checks=[Collections.Generic.List[object]]::new()
$checkIds=[Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$protected=[Collections.Generic.List[object]]::new()
$groups=[Collections.Generic.List[object]]::new()
$primaryType=$null;$failurePhase=$null;$phase='FIXED_INPUT_BINDING'
function Digest([byte[]]$Bytes){return [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($Bytes))}
function Confirm-Check([string]$Id,[bool]$Condition){
  if(-not $checkIds.Add($Id)){throw [InvalidOperationException]::new('DUPLICATE_RECONCILIATION_ID')}
  $checks.Add([pscustomobject]@{Id=$Id;Passed=$Condition})
  if(-not $Condition){throw [InvalidOperationException]::new('RECONCILIATION_REQUIREMENT_NOT_MET')}
}
function Require([bool]$Condition){
  if(-not $Condition){throw [InvalidOperationException]::new('ARCHIVE_STRUCTURE_NOT_EXPECTED')}
}
function Load-ProtectedManifest {
  $seen=[Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
  foreach($anchor in $anchors){
    $bytes=[IO.File]::ReadAllBytes($root+$anchor.Path)
    Require ($bytes.Length -eq $anchor.Bytes -and (Digest $bytes) -ceq $anchor.SHA256)
    $matches=[regex]::Matches($utf8.GetString($bytes),'(?m)^\| ((?:validation/route_b_c03/wp_008/|docs/phase2/route-b/)[^|\r\n]+?) \| ([A-F0-9]{64}) \| ([0-9]+) \|$')
    Require ($matches.Count -eq $anchor.Rows)
    foreach($m in $matches){
      Require ($seen.Add($m.Groups[1].Value))
      $protected.Add([pscustomobject]@{Path=$m.Groups[1].Value;SHA256=$m.Groups[2].Value;Bytes=[long]$m.Groups[3].Value})
    }
    Require ($seen.Add($anchor.Path))
    $protected.Add([pscustomobject]@{Path=$anchor.Path;SHA256=$anchor.SHA256;Bytes=[long]$anchor.Bytes})
  }
}
function Check-ProtectedManifest {
  foreach($item in $protected){
    $absolute=[IO.Path]::GetFullPath($root+$item.Path)
    Require ($absolute.StartsWith([IO.Path]::GetFullPath($root),[StringComparison]::OrdinalIgnoreCase))
    $bytes=[IO.File]::ReadAllBytes($absolute)
    Require ($bytes.Length -eq $item.Bytes -and (Digest $bytes) -ceq $item.SHA256)
  }
}
function Check-ReferenceIdentities {
  foreach($item in $references){
    $bytes=[IO.File]::ReadAllBytes($root+$item.Path)
    Require ($bytes.Length -eq $item.Bytes -and (Digest $bytes) -ceq $item.SHA256)
  }
}
function Expand-Fixed([string]$Value,[int]$ExpectedBytes){
  $inputMemory=[IO.MemoryStream]::new([Convert]::FromBase64String($Value),$false)
  $gzip=[IO.Compression.GZipStream]::new($inputMemory,[IO.Compression.CompressionMode]::Decompress)
  $output=[IO.MemoryStream]::new()
  try{
    $buffer=[byte[]]::new(4096)
    while(($n=$gzip.Read($buffer,0,$buffer.Length)) -gt 0){
      Require ($output.Length+$n -le $ExpectedBytes)
      $output.Write($buffer,0,$n)
    }
    Require ($output.Length -eq $ExpectedBytes)
    $result=$output.ToArray()
  }finally{$gzip.Dispose();$inputMemory.Dispose();$output.Dispose()}
  return ,$result
}
function Unique-Json([Text.Json.JsonElement]$Element){
  if($Element.ValueKind -eq [Text.Json.JsonValueKind]::Object){
    $seen=[Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
    foreach($p in $Element.EnumerateObject()){Require ($seen.Add($p.Name));Unique-Json $p.Value}
  }elseif($Element.ValueKind -eq [Text.Json.JsonValueKind]::Array){foreach($v in $Element.EnumerateArray()){Unique-Json $v}}
}
function Equal-Json([Text.Json.JsonElement]$Left,[Text.Json.JsonElement]$Right){
  if($Left.ValueKind -ne $Right.ValueKind){return $false}
  switch -Exact($Left.ValueKind.ToString()){
    'Object' {
      $lp=@($Left.EnumerateObject());$rp=@($Right.EnumerateObject())
      if($lp.Count -ne $rp.Count){return $false}
      foreach($p in $lp){
        try{$other=$Right.GetProperty($p.Name)}catch{return $false}
        if(-not (Equal-Json $p.Value $other)){return $false}
      }
      return $true
    }
    'Array' {
      $la=@($Left.EnumerateArray());$ra=@($Right.EnumerateArray())
      if($la.Count -ne $ra.Count){return $false}
      for($i=0;$i -lt $la.Count;$i++){if(-not (Equal-Json $la[$i] $ra[$i])){return $false}}
      return $true
    }
    'String' {return [StringComparer]::Ordinal.Equals($Left.GetString(),$Right.GetString())}
    'Number' {return [StringComparer]::Ordinal.Equals($Left.GetRawText(),$Right.GetRawText())}
    default {return $true}
  }
}
function Check-Assertions([object[]]$Values,[int]$Count,[string]$FlagName='Passed'){
  Require ($FlagName -ceq 'Passed' -or $FlagName -ceq 'Pass')
  Require ($Values.Count -eq $Count)
  $seen=[Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
  foreach($v in $Values){
    $flag=$v.PSObject.Properties[$FlagName]
    Require ($null -ne $flag -and $v.Id -is [string] -and $seen.Add($v.Id) -and $flag.Value -is [bool] -and $flag.Value)
  }
}
function Unique-Ids([object[]]$Values,[int]$Count,[bool]$ObjectIds){
  Require ($Values.Count -eq $Count)
  $seen=[Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
  foreach($v in $Values){
    $id=if($ObjectIds){$v.Id}else{$v}
    Require ($id -is [string] -and $seen.Add($id))
  }
  return ,$seen
}
try{
  Load-ProtectedManifest
  Check-ProtectedManifest
  Confirm-Check 'PRE.PROTECTED_47_IDENTITIES' ($protected.Count -eq 47)
  $runner='C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe'
  Confirm-Check 'PRE.RUNNER_IDENTITY' ((Digest ([IO.File]::ReadAllBytes($runner))) -ceq '362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139')
  Check-ReferenceIdentities
  Confirm-Check 'PRE.HISTORICAL_REFERENCE_IDENTITIES' ($references.Count -eq 2)
  foreach($spec in $specs){
    $phase=$spec.Id
    $archiveBytes=[IO.File]::ReadAllBytes($root+$spec.Path)
    Confirm-Check ($spec.Id+'.ARCHIVE_FILE_BINDING') ($archiveBytes.Length -eq $spec.FileBytes -and (Digest $archiveBytes) -ceq $spec.FileSHA256)
    $archiveText=$utf8.GetString($archiveBytes)
    $a=$archiveText|Microsoft.PowerShell.Utility\ConvertFrom-Json -Depth 80
    $fullBytes=Expand-Fixed $a.GZipBase64 $spec.FullBytes
    $fullText=$utf8.GetString($fullBytes)
    $ad=[Text.Json.JsonDocument]::Parse($archiveText)
    $rd=[Text.Json.JsonDocument]::Parse($fullText)
    try{
      Unique-Json $ad.RootElement;Unique-Json $rd.RootElement
      Confirm-Check ($spec.Id+'.JSON_UNIQUE_KEYS') $true
      Confirm-Check ($spec.Id+'.FULL_PAYLOAD_IDENTITY') ($a.FullRecordUTF8Bytes -eq $spec.FullBytes -and $a.FullRecordSHA256 -ceq $spec.FullSHA256 -and (Digest $fullBytes) -ceq $spec.FullSHA256)
      Confirm-Check ($spec.Id+'.GZIP_LENGTH') ([Convert]::FromBase64String($a.GZipBase64).Length -eq $a.GZipBytes)
      Confirm-Check ($spec.Id+'.RECORDED_EXIT') ($a.ObservedExitCode -eq 0)
      $r=$fullText|Microsoft.PowerShell.Utility\ConvertFrom-Json -Depth 80
      $s=if($spec.Mode -ceq 'NESTED'){$r.Summary}else{$r}
      Confirm-Check ($spec.Id+'.RECORDED_OUTCOME') ($s.Outcome -ceq $spec.ExpectedOutcome)
      $summaryElement=$ad.RootElement.GetProperty('Summary')
      $summaryOK=$true
      if($spec.Mode -ceq 'NESTED'){
        $summaryOK=Equal-Json $summaryElement ($rd.RootElement.GetProperty('Summary'))
      }else{
        foreach($p in $summaryElement.EnumerateObject()){
          if($spec.Mode -ceq 'COMPOSITION' -and $p.Name -ceq 'Stages'){continue}
          if(-not (Equal-Json $p.Value ($rd.RootElement.GetProperty($p.Name)))){$summaryOK=$false}
        }
        if($spec.Mode -ceq 'COMPOSITION'){
          Require ($a.Summary.Stages.Count -eq 3 -and $r.ActualStageRecords.Count -eq 3)
          for($i=0;$i -lt 3;$i++){
            $stage=$r.ActualStageRecords[$i];$t=$stage.Transport;$p=$stage.ReceivedParsedRecord;$v=$a.Summary.Stages[$i]
            $newCases=if($stage.StageId -ceq 'D007'){$p.NewPlanItemIds.Count}else{$p.Cases.Count}
            if($v.StageId -cne $stage.StageId -or $v.NewCases -ne $newCases -or $v.CheckCount -ne $p.CheckCount -or $v.TransportPass -ne $t.TransportOnlyPass -or $v.ElapsedMilliseconds -ne $t.ElapsedMilliseconds -or $v.ExitCode -ne $t.ExitCode -or $v.StdoutBytes -ne $t.StdoutBytes -or $v.StderrBytes -ne $t.StderrBytes){$summaryOK=$false}
          }
        }
      }
      Confirm-Check ($spec.Id+'.TYPED_SUMMARY_PROJECTION') $summaryOK
      $values=if($spec.Mode -ceq 'COMPOSITION'){@($r.ParentChecks)}else{@($r.Checks)}
      Check-Assertions $values $spec.CheckCount
      $declaredChecks=if($spec.Mode -ceq 'COMPOSITION'){$r.ParentCheckCount}else{$s.CheckCount}
      $declaredFailures=if($spec.Mode -ceq 'COMPOSITION'){$r.ParentFailedChecks}else{$s.FailedChecks}
      Confirm-Check ($spec.Id+'.RECORDED_CHECK_IDS_VALUES') ($declaredChecks -eq $spec.CheckCount -and $declaredFailures -eq 0)
      if($spec.Mode -ceq 'COMPOSITION'){
        $planIds=Unique-Ids @($r.NewUniquePlanItemIds) 189 $false
        $union=[Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
        foreach($stage in $r.ActualStageRecords){
          $p=$stage.ReceivedParsedRecord
          if($stage.StageId -ceq 'D007'){Check-Assertions @($p.Checks) $p.CheckCount 'Pass'}else{Check-Assertions @($p.Checks) $p.CheckCount 'Passed'}
          $childIds=if($stage.StageId -ceq 'D007'){@($p.NewPlanItemIds)}else{@($p.Cases|ForEach-Object {$_.Id})}
          foreach($id in $childIds){Require ($union.Add($id))}
        }
        Require ($union.SetEquals($planIds))
        Confirm-Check ($spec.Id+'.RECORDED_UNITS') ($r.NewUniquePlanItemCount -eq 189 -and $union.Count -eq 189)
      }else{
        $null=Unique-Ids @($r.Cases) $spec.CaseCount $true
        $declaredCases=if($spec.Mode -ceq 'FLAT_FAULT'){$r.SyntheticCaseCount}else{$s.CaseCount}
        Confirm-Check ($spec.Id+'.RECORDED_UNITS') ($declaredCases -eq $spec.CaseCount)
      }
      $bindingOK=switch -Exact($spec.Id){
        'AR-001' {$r.SupervisorCandidateSHA256 -ceq '9B165A04AFE786224965C5E33364140265FF3CB0B4B99A8E63A7AE7562C33E4E'}
        'AR-002' {$r.CandidateSHA256 -ceq '9B165A04AFE786224965C5E33364140265FF3CB0B4B99A8E63A7AE7562C33E4E'}
        'AR-003' {$s.SourceSHA256Before -ceq 'ADAB2850039C9A15C0A175F0028B751F983FC21EB218835102247F9CD50D5262' -and $s.SourceSHA256After -ceq $s.SourceSHA256Before}
        'AR-004' {$s.SourceSHA256Before -ceq 'ADAB2850039C9A15C0A175F0028B751F983FC21EB218835102247F9CD50D5262' -and $s.SourceSHA256After -ceq $s.SourceSHA256Before}
        default {$s.SourceSHA256Before -ceq '9B165A04AFE786224965C5E33364140265FF3CB0B4B99A8E63A7AE7562C33E4E' -and $s.SourceSHA256After -ceq $s.SourceSHA256Before}
      }
      Confirm-Check ($spec.Id+'.RECORDED_SOURCE_BINDING') $bindingOK
      $rawPresent=$null -ne $a.PSObject.Properties['RawStdoutGZipBase64']
      $rawBytes=$null;$rawSHA=$null
      if($rawPresent){
        $rawBytes=Expand-Fixed $a.RawStdoutGZipBase64 $a.RawStdoutBytes
        $rawSHA=Digest $rawBytes
        Require ($rawSHA -ceq $a.RawStdoutSHA256 -and [Convert]::FromBase64String($a.RawStdoutGZipBase64).Length -eq $a.RawStdoutGZipBytes)
        $rawText=$utf8.GetString($rawBytes)
        Require (($rawText.Replace(([string][char]13+[char]10),[string][char]10).TrimEnd([char]10)+[char]10) -ceq $fullText)
      }
      Confirm-Check ($spec.Id+'.RAW_WITNESS_AVAILABILITY') ($rawPresent -eq $spec.RawExpected)
      $groups.Add([pscustomobject]@{
        Id=$spec.Id;Path=$spec.Path;ArchiveFileSHA256=$spec.FileSHA256
        FullRecordSHA256=$spec.FullSHA256;FullRecordBytes=$spec.FullBytes
        RecordedOutcome=$s.Outcome;RecordedCheckCount=$spec.CheckCount
        RecordedUnitCount=$spec.CaseCount;RecordedUnitClass=$spec.Unit
        SummaryMode=$spec.Mode;TypedSummaryMatched=$summaryOK
        RawOuterStdoutAvailability=$(if($rawPresent){'RETAINED_AND_RECONCILED'}else{'NOT_RETAINED_SEPARATELY_STRUCTURED_RECORD_ONLY'})
        RawOuterStdoutBytes=$(if($rawPresent){$rawBytes.Length}else{$null})
        RawOuterStdoutSHA256=$rawSHA
        RawQualification='THIS TEST PROCESS OUTPUT ONLY; NOT A PRODUCTION CHILD BODY WITNESS'
        NewSubjectExecution=$false;FormalAcceptanceEffect='NONE'
      })
    }finally{$ad.Dispose();$rd.Dispose()}
  }
  $phase='POST_INPUT_INTEGRITY'
  Check-ProtectedManifest;Check-ReferenceIdentities
  Confirm-Check 'POST.INPUT_IDENTITIES_UNCHANGED' ($protected.Count -eq 47)
  Confirm-Check 'POST.AUDIT_CHECK_COUNT' ($checks.Count -eq 70)
  $phase='COMPLETE'
}catch{
  $primaryType=$_.Exception.GetType().FullName
  $failurePhase=$phase
}
$summary=[pscustomobject]@{
  Audit='DSP_004_EVIDENCE_ARCHIVE_RECONCILIATION_REV1'
  Outcome=$(if($null -eq $primaryType){'FIXED_ARCHIVE_RECONCILIATION_PASS'}else{'FIXED_ARCHIVE_RECONCILIATION_INCOMPLETE'})
  GroupCount=$groups.Count;ProtectedFiles=$protected.Count;HistoricalRequirementReferences=$references.Count
  RawOuterWitnessGroups=@($groups|Where-Object {$_.RawOuterStdoutAvailability -ceq 'RETAINED_AND_RECONCILED'}).Count
  StructuredOnlyGroups=@($groups|Where-Object {$_.RawOuterStdoutAvailability -cne 'RETAINED_AND_RECONCILED'}).Count
  AuditCheckCount=$checks.Count;FailedAuditChecks=@($checks|Where-Object {-not $_.Passed}).Count
  NewSubjectExecutions=0;FailurePhase=$failurePhase;PrimaryExceptionType=$primaryType
}
[pscustomobject]@{
  RecordVersion='DSP004-ARCHIVE-RECONCILIATION-REV1'
  Scope='READ_ONLY_EXISTING_LOCAL_SYNTHETIC_ARCHIVES_NOT_NEW_SUBJECT_TESTS'
  Summary=$summary;Groups=$groups.ToArray();AuditChecks=$checks.ToArray()
  ProtectedFiles=$protected.ToArray();HistoricalReferences=$references
  Limits=@(
    'Recorded assertions reconciled, not independently re-executed',
    'No combined scenario total, completion percentage or aggregate business verdict',
    'Three missing raw outer witnesses remain missing; child body hashes not recomputed',
    'JSON alone does not reconstruct native Int32/Int64 identity or source provenance',
    'Historical reference status words are not current authority or revocation',
    'Reader negative guards not systematically mutation-tested in this audit',
    'All failures and LIMITED retained; DSP-004 OPEN/HOLD; B-01 and B-02 OPEN',
    'No source admission, real capture, integration, deployment or independent ACOS access'
  )
}|Microsoft.PowerShell.Utility\ConvertTo-Json -Depth 20
if($null -ne $primaryType){exit 1}
exit 0
