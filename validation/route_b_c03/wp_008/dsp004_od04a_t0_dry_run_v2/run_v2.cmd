@echo off
rem DSP-004 OD04-A T0 dry run v2 launcher. Lives in the admin-protected supervisor_v2 folder. Double-click; no administrator rights.
"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "C:\Program Files\DSP004Runtime\supervisor_v2\supervisor_v2.ps1"
pause
