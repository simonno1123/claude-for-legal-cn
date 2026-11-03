@echo off
rem DSP-004 formal-run launcher v1. Lives in the admin-protected supervisor_formal_v1 folder.
rem Started as the standard account dsp004val by go_formal_v1.cmd (runas). No administrator rights.
"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "C:\Program Files\DSP004Runtime\supervisor_formal_v1\supervisor_formal_v1.ps1"
pause
