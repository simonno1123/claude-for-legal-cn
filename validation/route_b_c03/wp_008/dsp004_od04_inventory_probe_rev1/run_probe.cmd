@echo off
rem DSP-004 OD-04 inventory-only probe launcher. Runs the fixed per-user CPython once, isolated, no site, no bytecode writes.
"%LOCALAPPDATA%\Programs\Python\Python312\python.exe" -I -S -B "%~dp0probe_inventory.py" > "%~dp0probe_stdout.txt" 2>&1
