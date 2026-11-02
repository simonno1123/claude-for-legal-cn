@echo off
rem DSP-004 OD04-A v4: run only the post (collect) stage of the bound collect_v4.ps1, saving all its output,
rem including any error text, to a log file next to this file. Used when a post stage stopped without a visible message.
net session >nul 2>&1
if errorlevel 1 (
  "%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
  if errorlevel 1 pause
  exit /b
)
cd /d "%~dp0"
set LOG=%~dp0collect_only_log_%RANDOM%%RANDOM%.txt
echo Collecting; this can take a few minutes ...
"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "%~dp0collect_v4.ps1" post > "%LOG%" 2>&1
echo EXIT_CODE %errorlevel%>> "%LOG%"
type "%LOG%"
echo.
echo Done. Tell Claude.
pause
