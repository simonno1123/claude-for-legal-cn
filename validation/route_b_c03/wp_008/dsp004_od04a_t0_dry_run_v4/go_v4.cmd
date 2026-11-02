@echo off
rem DSP-004 OD04-A v4: repeat the bound v3 supervisor run as dsp004val and collect whole-history audit evidence.
rem The owner double-clicks once per run. Nothing is installed.
net session >nul 2>&1
if errorlevel 1 (
  "%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
  if errorlevel 1 pause
  exit /b
)
cd /d "%~dp0"
set PS="C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -NonInteractive -ExecutionPolicy Bypass -File
echo [1/3] Moving any earlier run record out of the dsp004val profile ...
%PS% "%~dp0collect_v4.ps1" pre
if errorlevel 1 goto fail
echo.
echo [2/3] Starting the run as dsp004val. Type the dsp004val password below (it is not shown).
echo       A new window opens; it takes about one minute. Wait until it shows PASS or BLOCKED, then close it.
pushd "%SystemRoot%\System32"
C:\Windows\System32\runas.exe /user:dsp004val "C:\Windows\System32\cmd.exe /c \"\"C:\Program Files\DSP004Runtime\supervisor_v3\run_v3.cmd\"\""
if errorlevel 1 (popd & goto fail)
popd
echo.
echo When the dsp004val window has shown PASS or BLOCKED and is closed, press any key here.
pause >nul
echo [3/3] Collecting the run record and the audit history ...
%PS% "%~dp0collect_v4.ps1" post
if errorlevel 1 goto fail
echo.
echo DONE. Tell Claude.
pause
exit /b 0
:fail
echo.
echo STOPPED. Tell Claude what this window shows.
pause
exit /b 1
