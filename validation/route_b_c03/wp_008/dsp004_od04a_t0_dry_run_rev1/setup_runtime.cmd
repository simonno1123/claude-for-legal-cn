@echo off
rem DSP-004 OD04-A step 1 launcher. Right-click and choose "Run as administrator".
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0setup_runtime.ps1"
pause
