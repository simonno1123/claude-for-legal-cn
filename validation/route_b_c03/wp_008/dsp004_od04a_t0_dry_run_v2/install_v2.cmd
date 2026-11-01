@echo off
rem DSP-004 OD04-A v2 installer launcher. Right-click and choose "Run as administrator".
"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "%~dp0install_v2.ps1"
pause
