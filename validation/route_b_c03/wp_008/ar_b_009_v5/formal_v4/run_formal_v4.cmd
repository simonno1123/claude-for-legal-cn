@echo off
rem C03 AR-B-009 V5 formal-run launcher (v4). Lives in the admin-protected supervisor_formal_v4 folder.
rem Started as the standard account dsp004val by go_formal_v4.cmd (runas). No administrator rights.
"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "C:\Program Files\DSP004Runtime\supervisor_formal_v4\supervisor_formal_v4.ps1"
pause
