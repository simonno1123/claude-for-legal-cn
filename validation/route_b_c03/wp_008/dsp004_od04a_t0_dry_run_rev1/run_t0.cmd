@echo off
rem DSP-004 OD04-A step 3 launcher: one supervised T0 dry run. Double-click; no administrator rights needed.
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0supervisor_t0.ps1"
pause
