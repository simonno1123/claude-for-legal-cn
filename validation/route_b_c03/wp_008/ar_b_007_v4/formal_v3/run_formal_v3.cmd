@echo off
rem C03 AR-B-007 V4 formal-run launcher (v3). Lives in the admin-protected supervisor_formal_v3 folder.
rem Started as the standard account dsp004val by go_formal_v3.cmd (runas). No administrator rights.
"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "C:\Program Files\DSP004Runtime\supervisor_formal_v3\supervisor_formal_v3.ps1"
pause
