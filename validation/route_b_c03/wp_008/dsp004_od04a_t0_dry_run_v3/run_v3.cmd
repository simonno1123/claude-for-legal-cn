@echo off
rem DSP-004 OD04-A T0 dry run v3 launcher. Lives in the admin-protected supervisor_v3 folder.
rem Started as the standard account dsp004val by go_v3.cmd (runas). No administrator rights.
"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "C:\Program Files\DSP004Runtime\supervisor_v3\supervisor_v3.ps1"
pause
