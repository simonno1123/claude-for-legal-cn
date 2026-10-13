# Closed synthetic metadata/request/byte/frame checks; no live entry or Driver.
Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'; $WarningPreference='Stop'; $PSModuleAutoLoadingPreference='None'
Import-Module -Name ([IO.Path]::Combine($PSHOME,'Modules','Microsoft.PowerShell.Utility','Microsoft.PowerShell.Utility.psd1')) -ErrorAction Stop
$taskRoot='C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008'
$taskListSha='46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C'
$taskControllerSha='891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB'
$taskChecks=[Collections.Generic.List[object]]::new(); $taskCases=[Collections.Generic.List[object]]::new()
$taskCleanup=[Collections.Generic.List[object]]::new(); $taskHeldSecondary=[Collections.Generic.List[Exception]]::new()
$taskRunspace=$null; $taskCurrent=$null; $taskHeldPrimary=$null; $taskPrimaryType=$null
$taskOpened=$false; $taskClosed=$false; $taskDisposed=$false; $taskCalls=0; $taskLoads=0

function Add-Check { param([string]$Id,[bool]$Passed); [void]$taskChecks.Add([pscustomobject]@{Id=$Id;Passed=$Passed}); if(-not $Passed){throw [InvalidOperationException]::new('FIXED_PURE_CHECK_FAILED')} }
function Keep-Cleanup { param([string]$Stage,[Exception]$Original); [void]$taskHeldSecondary.Add($Original); [void]$taskCleanup.Add([pscustomobject]@{Stage=$Stage;Type=$Original.GetType().FullName}) }
function Read-FixedTable {
    param([string]$Prefix,[int]$Columns)
    $taskTable=[ordered]@{}
    foreach($taskLine in $taskListText.Split([char]10)) {
        if($taskLine -cmatch ('^\| '+[regex]::Escape($Prefix)+'-[0-9]{2,3} \|')) {
            $taskParts=$taskLine.Split([char]'|'); $taskCells=@($taskParts[1..($taskParts.Length-2)]|ForEach-Object{$_.Trim()})
            if($taskParts[0] -cne '' -or $taskParts[-1] -cne '' -or $taskCells.Count -ne $Columns -or $taskTable.Contains($taskCells[0])){throw [InvalidOperationException]::new('FIXED_REFERENCE_TABLE_REJECTED')}
            $taskTable[$taskCells[0]]=$taskCells
        }
    }
    return $taskTable
}
function Native-Equal {
    param([AllowNull()][object]$Actual,[AllowNull()][object]$Expected)
    if($null -eq $Actual -or $null -eq $Expected){return ($null -eq $Actual -and $null -eq $Expected)}
    if($Actual -is [Management.Automation.PSCustomObject] -and $Expected -is [Management.Automation.PSCustomObject]) {
        $taskA=@($Actual.PSObject.Properties); $taskE=@($Expected.PSObject.Properties)
        if($taskA.Count -ne $taskE.Count){return $false}
        foreach($taskP in $taskE){$taskFound=@($taskA|Where-Object{$_.Name -ceq $taskP.Name}); if($taskFound.Count -ne 1 -or -not (Native-Equal $taskFound[0].Value $taskP.Value)){return $false}}
        return $true
    }
    if($Actual.GetType() -ne $Expected.GetType()){return $false}
    if($Actual -is [Collections.IDictionary]) {
        if($Actual.Count -ne $Expected.Count){return $false}
        foreach($taskKey in $Expected.Keys){$taskKeys=@($Actual.Keys|Where-Object{$_ -ceq $taskKey}); if($taskKeys.Count -ne 1 -or -not (Native-Equal $Actual[$taskKey] $Expected[$taskKey])){return $false}}
        return $true
    }
    if($Actual -is [Array]){if($Actual.Length -ne $Expected.Length){return $false}; for($taskI=0;$taskI -lt $Actual.Length;$taskI++){if(-not (Native-Equal $Actual[$taskI] $Expected[$taskI])){return $false}}; return $true}
    if($Actual -is [string]){return [string]::Equals($Actual,$Expected,[StringComparison]::Ordinal)}
    return $Actual.Equals($Expected)
}
function Invoke-FixedSubject {
    param([string]$Name,[Collections.IDictionary]$Parameters)
    if(@('Get-DSP004CaseContract','Get-DSP004StatusCombinations','Get-DSP004FixedContract','Test-DSP004RequestedCaseText','Test-DSP004DriverBytesInMemory','Test-DSP004FrameBytesInMemory') -cnotcontains $Name){throw [InvalidOperationException]::new('FUNCTION_NOT_IN_BATCH')}
    $script:taskCurrent=[Management.Automation.PowerShell]::Create(); $taskCurrent.Runspace=$taskRunspace
    [void]$taskCurrent.AddCommand($Name); foreach($taskEntry in $Parameters.GetEnumerator()){[void]$taskCurrent.AddParameter($taskEntry.Key,$taskEntry.Value)}
    $script:taskCalls++; $taskOut=$taskCurrent.Invoke()
    $taskStreams=[ordered]@{Error=$taskCurrent.Streams.Error.Count;Warning=$taskCurrent.Streams.Warning.Count;Debug=$taskCurrent.Streams.Debug.Count;Verbose=$taskCurrent.Streams.Verbose.Count;Information=$taskCurrent.Streams.Information.Count;Progress=$taskCurrent.Streams.Progress.Count}
    $taskValues=[Collections.Generic.List[object]]::new()
    foreach($taskObject in $taskOut){$taskBase=$taskObject.PSObject.BaseObject; if($taskBase -is [Management.Automation.PSCustomObject]){[void]$taskValues.Add($taskObject)}else{[void]$taskValues.Add($taskBase)}}
    $taskReturn=[pscustomobject]@{Items=$taskValues.ToArray();Streams=$taskStreams;ChannelsClear=(-not $taskCurrent.HadErrors -and @($taskStreams.Values|Where-Object{$_ -ne 0}).Count -eq 0)}
    try{$taskCurrent.Dispose()}catch{Keep-Cleanup 'CASE_PIPELINE_DISPOSE' $_.Exception}; $script:taskCurrent=$null
    return $taskReturn
}
function Frame-Text { param([int]$Number); return 'DSP004-STATUS-V1|'+[string]::Join('|',$taskT['T-'+$Number.ToString('D3')][1..4])+[char]10 }
function Frame-Fixture {
    param([int]$Number,[object[]]$Row)
    $taskText=Frame-Text 1; $taskPayload=$null; $taskRequest=$null
    if($Row[2] -cmatch '^A-[0-9]{2}$'){$taskRequest=$taskA[$Row[2]][1]}
    elseif($Row[2] -ceq 'null'){$taskRequest=$null}
    elseif($Row[2] -ceq '原生 int 1'){$taskRequest=[int]1}
    elseif($Row[2] -ceq '原生 string DRIVER_ALREADY_USED'){$taskRequest='DRIVER_ALREADY_USED'}
    elseif($Row[2] -ceq '原生 string UNBOUND_CASE'){$taskRequest='UNBOUND_CASE'}
    elseif($Number -eq 62){$taskRequest=$taskA['A-01'][1]+' '}
    else{throw [InvalidOperationException]::new('FIXED_FRAME_REQUEST_REJECTED')}
    if($Number -le 26){$taskText=Frame-Text $Number}
    elseif($Number -eq 27){$taskText=(Frame-Text 2).Replace('NOT_RUN','INCOMPLETE',[StringComparison]::Ordinal)}
    elseif($Number -eq 28){$taskText=Frame-Text 25}
    elseif($Number -eq 29 -or $Number -eq 32 -or $Number -eq 33){$taskText=Frame-Text 26; if($Number -eq 32 -or $Number -eq 33){$taskText=Frame-Text 25}}
    $taskPayload=[Text.Encoding]::ASCII.GetBytes($taskText)
    switch($Number) {
        35 {$taskPayload=[string]$taskText}
        36 {$taskPayload=$null}
        37 {$taskPayload=[object[]]@([int]10)}
        38 {$taskPayload=[byte[]]::new(0)}
        39 {$taskPayload=[Text.Encoding]::ASCII.GetBytes(([string]::new([char]65,256))+[char]10)}
        40 {$taskPayload=[byte[]]@([byte]10)}
        41 {$taskPayload=[Text.Encoding]::ASCII.GetBytes($taskText.Substring(0,$taskText.Length-1))}
        42 {$taskPayload=[Text.Encoding]::ASCII.GetBytes($taskText.Substring(0,$taskText.Length-1)+[char]13+[char]10)}
        43 {$taskOriginal=$taskPayload; $taskPayload=[byte[]]::new($taskOriginal.Length+3); $taskPayload[0]=239; $taskPayload[1]=187; $taskPayload[2]=191; [Buffer]::BlockCopy($taskOriginal,0,$taskPayload,3,$taskOriginal.Length)}
        44 {$taskPayload[0]=128}
        45 {$taskPayload[0]=0}
        46 {$taskPayload[0]=32}
        47 {$taskPayload[0]=9}
        48 {$taskPayload=[Text.Encoding]::ASCII.GetBytes($taskText+$taskText)}
        49 {$taskPayload=[Text.Encoding]::ASCII.GetBytes($taskText+'X')}
        50 {$taskPayload=[Text.Encoding]::ASCII.GetBytes($taskText.Substring(0,$taskText.Length-1)+'X'+[char]10)}
        51 {$taskPayload=[Text.Encoding]::ASCII.GetBytes($taskText.Substring(0,1)+[char]10+$taskText.Substring(1))}
        52 {$taskPayload=[Text.Encoding]::ASCII.GetBytes($taskText.Replace('DSP004','dsp004',[StringComparison]::Ordinal))}
        53 {$taskPayload=[Text.Encoding]::ASCII.GetBytes($taskText.Replace($taskA['A-01'][1],'full_entry_literal_records',[StringComparison]::Ordinal))}
        54 {$taskPayload=[Text.Encoding]::ASCII.GetBytes($taskText.Replace($taskA['A-01'][2],'FULL_ENTRY_PRECONDITION_REFUSAL',[StringComparison]::Ordinal))}
        55 {$taskPayload=[Text.Encoding]::ASCII.GetBytes($taskText.Replace($taskA['A-01'][3],'EXPECTED_REFUSAL_OBSERVED',[StringComparison]::Ordinal))}
        56 {$taskPayload=[Text.Encoding]::ASCII.GetBytes($taskText.Replace('END_CASE','STOP_BATCH',[StringComparison]::Ordinal))}
        57 {$taskPayload=[Text.Encoding]::ASCII.GetBytes((Frame-Text 2).Replace('STOP_BATCH','END_CASE',[StringComparison]::Ordinal))}
        58 {$taskPayload=[Text.Encoding]::ASCII.GetBytes($taskText.Replace($taskA['A-01'][2]+'|','',[StringComparison]::Ordinal))}
        59 {$taskPayload=[Text.Encoding]::ASCII.GetBytes($taskText.Substring(0,$taskText.Length-1)+'|EXTRA'+[char]10)}
        60 {$taskPayload=[Text.Encoding]::ASCII.GetBytes($taskText.Replace('DSP004-STATUS-V1|','DSP004-STATUS-V1||',[StringComparison]::Ordinal))}
        61 {$taskPayload=[Text.Encoding]::ASCII.GetBytes($taskText.Replace('END_CASE','end_case',[StringComparison]::Ordinal))}
    }
    return [pscustomobject]@{Payload=$taskPayload;RequestedCase=$taskRequest}
}
function Scalar-Fields-Equal { param([object]$Actual,[Collections.IDictionary]$Expected); $taskNames=@($Actual.PSObject.Properties.Name); if($taskNames.Count -ne $Expected.Count){return $false}; foreach($taskKey in $Expected.Keys){if(@($taskNames|Where-Object{$_ -ceq $taskKey}).Count -ne 1 -or -not (Native-Equal $Actual.PSObject.Properties[$taskKey].Value $Expected[$taskKey])){return $false}}; return $true }

try {
    $taskListBytes=[IO.File]::ReadAllBytes([IO.Path]::Combine($taskRoot,'DSP_004_LOCAL_VALIDATION_CARRIER_CANDIDATE_REV1.ps1'))
    $taskControllerBytes=[IO.File]::ReadAllBytes([IO.Path]::Combine($taskRoot,'DSP_004_OUTER_CONTROLLER_CANDIDATE_REV1.ps1'))
    Add-Check 'HASH-LIST' ($taskListBytes.Length -eq 70284 -and [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($taskListBytes)) -ceq $taskListSha)
    Add-Check 'HASH-CONTROLLER' ($taskControllerBytes.Length -eq 25573 -and [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($taskControllerBytes)) -ceq $taskControllerSha)
    $taskListText=[Text.UTF8Encoding]::new($false,$true).GetString($taskListBytes); $taskSubjectText=[Text.UTF8Encoding]::new($false,$true).GetString($taskControllerBytes)
    $taskA=Read-FixedTable 'A' 4; $taskT=Read-FixedTable 'T' 5; $taskK=Read-FixedTable 'K' 4
    $taskM=Read-FixedTable 'M' 3; $taskRq=Read-FixedTable 'RQ' 3; $taskD=Read-FixedTable 'D' 4; $taskF=Read-FixedTable 'F' 6
    Add-Check 'REFERENCES-01' ($taskA.Count -eq 8 -and $taskT.Count -eq 26 -and $taskK.Count -eq 27 -and $taskM.Count -eq 6 -and $taskRq.Count -eq 18 -and $taskD.Count -eq 7 -and $taskF.Count -eq 62 -and $taskListText.Contains('REV2 仅收缩 D-003 非 byte[] 拒绝样本为一个 Int32 0；') -and $taskListText.Contains('| F-ALLOW | TextCheck = ALLOWLISTED_FRAME_TEXT_ONLY |') -and $taskListText.Contains('| F-REJECT | TextCheck = FRAME_REJECTED |'))
    [object[]]$taskExpectedA=@($taskA.Values|ForEach-Object{@{CaseId=$_[1];Level=$_[2];Observation=$_[3]}})
    [object[]]$taskExpectedT=@($taskT.Values|ForEach-Object{[string]::Join('|',$_[1..4])})
    $taskExpectedK=[ordered]@{}
    foreach($taskRow in $taskK.Values){if($taskRow[2] -ceq '原生 string'){$taskExpectedK[$taskRow[1]]=[string]$taskRow[3]}elseif($taskRow[2] -ceq '原生 int'){$taskExpectedK[$taskRow[1]]=[int]::Parse($taskRow[3])}elseif($taskRow[0] -ceq 'K-020'){$taskExpectedK[$taskRow[1]]=$taskExpectedA}elseif($taskRow[0] -ceq 'K-021'){$taskExpectedK[$taskRow[1]]=$taskExpectedT}elseif($taskRow[0] -ceq 'K-022'){$taskExpectedK[$taskRow[1]]=[object[]]@('START_NOT_PERMITTED','START_FAILED','INPUT_REJECTED','OUTPUT_REJECTED','TIMEOUT','EXIT_UNCONFIRMED')}else{throw [InvalidOperationException]::new('UNKNOWN_FIXED_METADATA_FIELD')}}
    $taskFixedExpected=[pscustomobject]$taskExpectedK
    $taskTokens=$null; $taskErrors=$null; $taskAst=[Management.Automation.Language.Parser]::ParseInput($taskSubjectText,[ref]$taskTokens,[ref]$taskErrors)
    $taskNames=@('Get-DSP004CaseContract','Get-DSP004StatusCombinations','Get-DSP004FixedContract','Test-DSP004RequestedCaseText','Test-DSP004DriverBytesInMemory','Test-DSP004FrameBytesInMemory','Get-DSP004ReadObservationClassification','Get-DSP004WriteObservationClassification','Get-DSP004FutureBootstrapText','Invoke-DSP004SingleCase')
    $taskAstGood=@($taskErrors).Count -eq 0 -and $null -eq $taskAst.ParamBlock -and $null -eq $taskAst.BeginBlock -and $null -eq $taskAst.ProcessBlock -and $null -eq $taskAst.DynamicParamBlock -and $taskAst.EndBlock.Statements.Count -eq 10
    for($taskI=0;$taskI -lt $taskAst.EndBlock.Statements.Count;$taskI++){if($taskI -ge 10 -or $taskAst.EndBlock.Statements[$taskI] -isnot [Management.Automation.Language.FunctionDefinitionAst] -or $taskAst.EndBlock.Statements[$taskI].Name -cne $taskNames[$taskI]){$taskAstGood=$false}}
    Add-Check 'AST-01' $taskAstGood
    $taskInitial=[Management.Automation.Runspaces.InitialSessionState]::Create(); $taskInitial.LanguageMode=[Management.Automation.PSLanguageMode]::FullLanguage
    $taskRunspace=[Management.Automation.Runspaces.RunspaceFactory]::CreateRunspace($taskInitial); $taskRunspace.Open(); $taskOpened=$true
    $taskCurrent=[Management.Automation.PowerShell]::Create(); $taskCurrent.Runspace=$taskRunspace; [void]$taskCurrent.AddScript($taskSubjectText,$false); $taskLoads++; $taskLoadOut=$taskCurrent.Invoke()
    Add-Check 'LOAD-01' ($taskLoads -eq 1 -and $taskLoadOut.Count -eq 0 -and -not $taskCurrent.HadErrors -and $taskCurrent.Streams.Error.Count -eq 0 -and $taskCurrent.Streams.Warning.Count -eq 0 -and $taskCurrent.Streams.Debug.Count -eq 0 -and $taskCurrent.Streams.Verbose.Count -eq 0 -and $taskCurrent.Streams.Information.Count -eq 0 -and $taskCurrent.Streams.Progress.Count -eq 0)
    $taskCurrent.Dispose(); $taskCurrent=$null

    foreach($taskGroup in @('M','RQ','D','F')) {
        $taskLimit=if($taskGroup -ceq 'M'){6}elseif($taskGroup -ceq 'RQ'){18}elseif($taskGroup -ceq 'D'){6}else{62}
        for($taskN=1;$taskN -le $taskLimit;$taskN++) {
            $taskId=$taskGroup+'-'+$taskN.ToString('D3'); $taskInputType='NO_PARAMETERS'; $taskByteCount=$null; $taskMatch=$false; $taskShape=$false; $taskLimits=$false; $taskMutation=$null
            if($taskGroup -ceq 'M') {
                $taskFn=if($taskN -eq 1 -or $taskN -eq 4){'Get-DSP004CaseContract'}elseif($taskN -eq 2 -or $taskN -eq 5){'Get-DSP004StatusCombinations'}else{'Get-DSP004FixedContract'}
                $taskFirst=Invoke-FixedSubject $taskFn @{}; $taskCall=$taskFirst
                if($taskN -eq 4){$taskFirst.Items[0]['CaseId']='CALLER_COPY_SENTINEL'; $taskCall=Invoke-FixedSubject $taskFn @{}; $taskMutation=[ordered]@{CallerCopyChanged=($taskFirst.Items[0]['CaseId'] -ceq 'CALLER_COPY_SENTINEL');FirstHashtableDifferent=(-not [Object]::ReferenceEquals($taskFirst.Items[0],$taskCall.Items[0]))}}
                elseif($taskN -eq 5){$taskFirst.Items[0]='CALLER_COPY_SENTINEL'; $taskCall=Invoke-FixedSubject $taskFn @{}; $taskMutation=[ordered]@{CallerCaptureSlotChanged=($taskFirst.Items[0] -ceq 'CALLER_COPY_SENTINEL');CaptureQualification='ARRAY CAPTURE OWNED BY TEST; NOT A DIRECT FUNCTION ARRAY RETURN'}}
                elseif($taskN -eq 6){$taskFirst.Items[0].CandidateQualification='CALLER_COPY_SENTINEL'; $taskFirst.Items[0].CaseContract[0]['CaseId']='CALLER_COPY_SENTINEL'; $taskFirst.Items[0].StatusCombinations[0]='CALLER_COPY_SENTINEL'; $taskCall=Invoke-FixedSubject $taskFn @{}; $taskMutation=[ordered]@{CallerPropertiesChanged=($taskFirst.Items[0].CandidateQualification -ceq 'CALLER_COPY_SENTINEL' -and $taskFirst.Items[0].CaseContract[0]['CaseId'] -ceq 'CALLER_COPY_SENTINEL' -and $taskFirst.Items[0].StatusCombinations[0] -ceq 'CALLER_COPY_SENTINEL');CaseArraysDifferent=(-not [Object]::ReferenceEquals($taskFirst.Items[0].CaseContract,$taskCall.Items[0].CaseContract));FirstHashtablesDifferent=(-not [Object]::ReferenceEquals($taskFirst.Items[0].CaseContract[0],$taskCall.Items[0].CaseContract[0]));StatusArraysDifferent=(-not [Object]::ReferenceEquals($taskFirst.Items[0].StatusCombinations,$taskCall.Items[0].StatusCombinations))}}
                if($taskN -eq 1 -or $taskN -eq 4){$taskMatch=Native-Equal $taskCall.Items $taskExpectedA; $taskShape=$taskCall.Items.Count -eq 8 -and @($taskCall.Items|Where-Object{$_ -isnot [hashtable]}).Count -eq 0}
                elseif($taskN -eq 2 -or $taskN -eq 5){$taskMatch=Native-Equal $taskCall.Items $taskExpectedT; $taskShape=$taskCall.Items.Count -eq 26 -and @($taskCall.Items|Where-Object{$_ -isnot [string]}).Count -eq 0}
                else{$taskMatch=$taskCall.Items.Count -eq 1 -and (Native-Equal $taskCall.Items[0] $taskFixedExpected); $taskShape=$taskCall.Items.Count -eq 1 -and $taskCall.Items[0] -is [Management.Automation.PSCustomObject]}
                $taskLimits=$taskFirst.ChannelsClear -and ($null -eq $taskMutation -or @($taskMutation.Values|Where-Object{$_ -is [bool] -and -not $_}).Count -eq 0)
            }
            elseif($taskGroup -ceq 'RQ') {
                if($taskN -le 8){$taskInput=$taskA['A-'+$taskN.ToString('D2')][1]}else{switch($taskN){9 {$taskInput='full_entry_literal_records'} 10 {$taskInput=' '+$taskA['A-01'][1]} 11 {$taskInput=$taskA['A-01'][1]+' '} 12 {$taskInput=''} 13 {$taskInput='UNKNOWN_CASE'} 14 {$taskInput='DRIVER_ALREADY_USED'} 15 {$taskInput=$null} 16 {$taskInput=$false} 17 {$taskInput=[int]1} 18 {$taskInput=[object[]]@($taskA['A-01'][1])}}}
                $taskInputType=if($null -eq $taskInput){'ABSENT_NULL'}else{$taskInput.GetType().FullName}; $taskCall=Invoke-FixedSubject 'Test-DSP004RequestedCaseText' @{CaseId=$taskInput}
                $taskShape=$taskCall.Items.Count -eq 1 -and $taskCall.Items[0] -is [bool]; $taskExpectedBool=$taskRq[$taskId][2] -ceq 'true'; $taskMatch=$taskShape -and $taskCall.Items[0] -eq $taskExpectedBool; $taskLimits=$taskShape
            }
            elseif($taskGroup -ceq 'D') {
                switch($taskN){1 {$taskInput=$null} 2 {$taskInput=''} 3 {$taskInput=[int]0} 4 {$taskInput=[byte[]]::new(0)} 5 {$taskInput=[byte[]]::new(20176)} 6 {$taskInput=[byte[]]::new(20178)}}
                $taskInputType=if($null -eq $taskInput){'ABSENT_NULL'}else{$taskInput.GetType().FullName}; if($taskInput -is [byte[]]){$taskByteCount=$taskInput.Length}
                $taskCall=Invoke-FixedSubject 'Test-DSP004DriverBytesInMemory' @{Payload=$taskInput}
                $taskExpected=[ordered]@{TextCheck=$taskD[$taskId][2];Authority='NOT ESTABLISHED';SourceAdmission='NOT ESTABLISHED';FrozenHandoff='NOT IMPLEMENTED';ChildLengthEofShaVerification='NOT OBSERVED';CaseCompletion='NOT ESTABLISHED'}
                $taskShape=$taskCall.Items.Count -eq 1 -and $taskCall.Items[0] -is [Management.Automation.PSCustomObject]; $taskMatch=$taskShape -and (Scalar-Fields-Equal $taskCall.Items[0] $taskExpected); $taskLimits=$taskMatch
            }
            else {
                $taskFixture=Frame-Fixture $taskN $taskF[$taskId]; $taskInputType=if($null -eq $taskFixture.Payload){'ABSENT_NULL'}else{$taskFixture.Payload.GetType().FullName}; if($taskFixture.Payload -is [byte[]]){$taskByteCount=$taskFixture.Payload.Length}
                $taskCall=Invoke-FixedSubject 'Test-DSP004FrameBytesInMemory' @{Payload=$taskFixture.Payload;RequestedCase=$taskFixture.RequestedCase}
                $taskExpectedCode=if($taskF[$taskId][3] -ceq 'F-ALLOW'){'ALLOWLISTED_FRAME_TEXT_ONLY'}elseif($taskF[$taskId][3] -ceq 'F-REJECT'){'FRAME_REJECTED'}else{throw [InvalidOperationException]::new('UNKNOWN_FIXED_FRAME_EXPECTATION')}
                $taskExpected=[ordered]@{TextCheck=$taskExpectedCode;RecordedAction=$taskF[$taskId][4];ProtectionRecord=($taskF[$taskId][5] -ceq 'true');Qualification='IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED';PeerEof='NOT OBSERVED';TaskSettlement='NOT OBSERVED';ProcessExit='NOT OBSERVED';Deadline='NOT OBSERVED';Authority='NOT ESTABLISHED';CaseCompletion='NOT ESTABLISHED'}
                $taskShape=$taskCall.Items.Count -eq 1 -and $taskCall.Items[0] -is [Management.Automation.PSCustomObject]; $taskMatch=$taskShape -and (Scalar-Fields-Equal $taskCall.Items[0] $taskExpected); $taskLimits=$taskMatch
            }
            $taskCase=[ordered]@{Id=$taskId;InputNativeType=$taskInputType;InputByteCount=$taskByteCount;Captured=$taskCall.Items;Streams=$taskCall.Streams;CopyMutation=$taskMutation;Comparison='INCOMPLETE';Qualification='LOCAL SYNTHETIC PURE CHECK ONLY; NO SOURCE ADMISSION OR CASE COMPLETION'}; [void]$taskCases.Add($taskCase)
            Add-Check ($taskId+'-CHANNELS') $taskCall.ChannelsClear; Add-Check ($taskId+'-SHAPE') $taskShape; Add-Check ($taskId+'-VALUES') $taskMatch; Add-Check ($taskId+'-LIMITS') $taskLimits
            $taskCase.Comparison='LOCAL_NATIVE_COMPARISON_PASS'
        }
    }
}
catch{$taskHeldPrimary=$_.Exception; $taskPrimaryType=$_.Exception.GetType().FullName}
finally {
    if($null -ne $taskCurrent){try{$taskCurrent.Dispose()}catch{Keep-Cleanup 'PIPELINE_DISPOSE' $_.Exception}}
    if($null -ne $taskRunspace){if($taskOpened){try{$taskRunspace.Close(); $taskClosed=$true}catch{Keep-Cleanup 'RUNSPACE_CLOSE' $_.Exception}}; try{$taskRunspace.Dispose(); $taskDisposed=$true}catch{Keep-Cleanup 'RUNSPACE_DISPOSE' $_.Exception}}
}
$taskIds=[Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal); foreach($taskCheck in $taskChecks){[void]$taskIds.Add($taskCheck.Id)}
$taskFailed=@($taskChecks|Where-Object{-not $_.Passed}).Count; $taskPass=@($taskCases|Where-Object{$_.Comparison -ceq 'LOCAL_NATIVE_COMPARISON_PASS'}).Count
$taskAll=$null -eq $taskPrimaryType -and $taskCleanup.Count -eq 0 -and $taskChecks.Count -eq 373 -and $taskIds.Count -eq 373 -and $taskFailed -eq 0 -and $taskCases.Count -eq 92 -and $taskPass -eq 92 -and $taskCalls -eq 95 -and $taskClosed -and $taskDisposed
$taskRecord=[pscustomobject][ordered]@{RecordKind='LOCAL_FIXED_REMAINING_PURE_CHECKS_NOT_ACCEPTANCE_OR_COMPLETE_189';Outcome=if($taskAll){'LOCAL_REMAINING_PURE_CHECKS_PASS'}else{'LOCAL_REMAINING_PURE_CHECKS_FAIL'};FixtureListSHA256=$taskListSha;ControllerSHA256=$taskControllerSha;Loads=$taskLoads;DirectPipelineInvocations=$taskCalls;ItemCount=$taskCases.Count;NativeComparisonPassCount=$taskPass;CheckCount=$taskChecks.Count;UniqueCheckIds=$taskIds.Count;FailedChecks=$taskFailed;PrimaryValidationFailureType=$taskPrimaryType;CleanupFailures=$taskCleanup.ToArray();RunspaceCloseCallReturned=$taskClosed;RunspaceDisposeCallReturned=$taskDisposed;Cases=$taskCases.ToArray();Checks=$taskChecks.ToArray();D003Qualification='INT32 ZERO PER REV2 INTRODUCTORY CLARIFICATION; HISTORICAL INT[] ROW UNCHANGED';D007='NOT_RUN; SAME PRIVATE PREPARED BYTE HANDOFF NOT REBOUND OR SUBSTITUTED';UpstreamPathAndHashQualification='RECORDED IN CANDIDATE TEXT ONLY - NOT INDEPENDENTLY VERIFIED';Excluded=[string[]]@('RD_WR_REEXECUTION','POSITIVE_DRIVER_SHA','REAL_DRIVER_BOOTSTRAP','SOURCE_ADMISSION','ACTUAL_CAPTURE','INTEGRATION','OTHER_PROJECTS');Preserved='ALL LIMITED PRESERVED; DSP-004 OPEN / HOLD; B-01/B-02 OPEN; NO AGGREGATE OR FULL-189 VERDICT'}
Microsoft.PowerShell.Utility\ConvertTo-Json -InputObject $taskRecord -Depth 16 -Compress
if($taskAll){exit 0}else{exit 1}
