# DSP-004 OD04-A step 1: create an admin-owned dedicated runtime copy and set its ACL.
# Authorized by the owner on 2026-10-31 ("合并，三步都授权"). Run once, elevated, via setup_runtime.cmd.
# It never overwrites: if the target exists it stops. It does not delete or change the source install.
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version 2

$ExpectedSourcePythonSha = '4D6F5F81A4BCA11191C4C7C6B43632694D0A4CE74E068619D8FDC161D469859A'  # REV19 python.exe
$Base   = 'C:\Program Files\DSP004Runtime'
$Target = Join-Path $Base 'Python312'
$Prefix = Join-Path $Base 'empty_pycache_prefix'
$Out    = Join-Path $PSScriptRoot 'setup_result.json'

function Fail([string]$code) { Write-Host "STOP $code"; exit 2 }

$principal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) { Fail 'NOT_ELEVATED' }
if (Test-Path -LiteralPath $Out) { Fail 'RESULT_ALREADY_EXISTS' }
if (Test-Path -LiteralPath $Base) { Fail 'TARGET_ALREADY_EXISTS' }

$Src = Join-Path $env:LOCALAPPDATA 'Programs\Python\Python312'
$srcExe = Join-Path $Src 'python.exe'
if (-not (Test-Path -LiteralPath $srcExe)) { Fail 'SOURCE_NOT_FOUND' }
if ((Get-FileHash -LiteralPath $srcExe -Algorithm SHA256).Hash -ne $ExpectedSourcePythonSha) { Fail 'SOURCE_PYTHON_SHA_MISMATCH' }

# 1. Create the base directory and lock its ACL before anything is copied in, so every child inherits it.
New-Item -ItemType Directory -Path $Base | Out-Null
& icacls.exe $Base /inheritance:r /grant:r '*S-1-5-18:(OI)(CI)F' '*S-1-5-32-544:(OI)(CI)F' '*S-1-5-32-545:(OI)(CI)RX' | Out-Null
if ($LASTEXITCODE -ne 0) { Fail 'ICACLS_BASE_FAILED' }
& icacls.exe $Base /setowner '*S-1-5-32-544' | Out-Null
if ($LASTEXITCODE -ne 0) { Fail 'SETOWNER_BASE_FAILED' }

# 2. Copy data only (no source ACLs). Leave out bytecode caches, tests, GUI/IDE packages and dev headers.
& robocopy.exe $Src $Target /E /COPY:D /DCOPY:D /R:0 /W:0 /NP /NFL /NDL /NJH /NJS `
    /XD __pycache__ test idlelib turtledemo tkinter site-packages Doc Scripts include libs tcl `
    /XF *.pyc *.pyo | Out-Null
$rc = $LASTEXITCODE
if ($rc -ge 8) { Fail "ROBOCOPY_FAILED_$rc" }
New-Item -ItemType Directory -Path $Prefix | Out-Null

# 3. Make every child inherit only from the base, and owned by Administrators.
& icacls.exe "$Base\*" /reset /T /C /Q | Out-Null
if ($LASTEXITCODE -ne 0) { Fail 'ICACLS_RESET_FAILED' }
& icacls.exe $Base /setowner '*S-1-5-32-544' /T /C /Q | Out-Null
if ($LASTEXITCODE -ne 0) { Fail 'SETOWNER_TREE_FAILED' }

# 4. Record what now exists.
$files = Get-ChildItem -LiteralPath $Base -Recurse -File -Force | Sort-Object FullName | ForEach-Object {
    [ordered]@{
        RelPath = $_.FullName.Substring($Base.Length + 1).Replace('\', '/')
        Bytes   = $_.Length
        SHA256  = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash
    }
}
$prefixEntries = @(Get-ChildItem -LiteralPath $Prefix -Force).Count
$result = [ordered]@{
    Kind                 = 'DSP004_OD04A_SETUP_RESULT_REV1'
    Base                 = $Base
    SourcePythonSha256   = $ExpectedSourcePythonSha
    RobocopyExitCode     = $rc
    BaseOwner            = (Get-Acl -LiteralPath $Base).Owner
    BaseSddl             = (Get-Acl -LiteralPath $Base).Sddl
    RuntimeSddl          = (Get-Acl -LiteralPath $Target).Sddl
    PrefixSddl           = (Get-Acl -LiteralPath $Prefix).Sddl
    PythonExeSddl        = (Get-Acl -LiteralPath (Join-Path $Target 'python.exe')).Sddl
    PrefixEntryCount     = $prefixEntries
    FileCount            = @($files).Count
    Files                = @($files)
}
$json = $result | ConvertTo-Json -Depth 5
$fs = [IO.File]::Open($Out, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
$bytes = (New-Object Text.UTF8Encoding($false)).GetBytes($json)
$fs.Write($bytes, 0, $bytes.Length); $fs.Close()
Write-Host "DONE files=$(@($files).Count) result=$Out"
exit 0
