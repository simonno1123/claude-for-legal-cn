@echo off
rem C03 AR-B-009 V5 formal-run v4: install the supervisor and project files (owner, elevated, once). Runs nothing.
net session >nul 2>&1
if errorlevel 1 (
  "%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
  if errorlevel 1 pause
  exit /b
)
cd /d "%~dp0"
set PS="C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -NonInteractive -ExecutionPolicy Bypass -File
%PS% "%~dp0install_formal_v4.ps1"
if errorlevel 1 (echo. & echo STOPPED. Tell Claude what this window shows. & pause & exit /b 1)
echo.
echo DONE. Tell Claude.
pause
