@echo off
rem C03 V7 formal-run launcher (v6). Lives in the admin-protected supervisor_formal_v6 folder.
rem Started as the standard account dsp004val by go_formal_v6.cmd (runas). No administrator rights.
"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "C:\Program Files\DSP004Runtime\supervisor_formal_v6\supervisor_formal_v6.ps1"
pause
