@echo off
rem DSP-004 phase 1 setup. Run by the owner. Double-click; click "Yes" on the UAC prompt.
net session >nul 2>&1
if errorlevel 1 (
  powershell -NoProfile -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
  exit /b
)
cd /d "%~dp0"
echo.
net user dsp004val >nul 2>&1
if errorlevel 1 (
  echo [1/3] Creating standard account dsp004val. Type the password twice ^(it is not shown^):
  net user dsp004val * /add
) else (
  echo [1/3] Account dsp004val already exists, skipped.
)
echo [2/3] Enabling process creation / termination auditing ...
auditpol /set /subcategory:{0CCE922B-69AE-11D9-BED3-505054503030} /success:enable
auditpol /set /subcategory:{0CCE922C-69AE-11D9-BED3-505054503030} /success:enable
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System\Audit /v ProcessCreationIncludeCmdLine_Enabled /t REG_DWORD /d 1 /f
echo [3/3] Writing check output ...
(
  whoami /groups | findstr /i "S-1-16"
  auditpol /get /subcategory:{0CCE922B-69AE-11D9-BED3-505054503030},{0CCE922C-69AE-11D9-BED3-505054503030}
  reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System\Audit /v ProcessCreationIncludeCmdLine_Enabled
  net localgroup Administrators
  net user dsp004val
) > "%~dp0phase1_setup_check.txt" 2>&1
echo.
echo DONE. Result saved to phase1_setup_check.txt
pause
