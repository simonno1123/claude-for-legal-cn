"""DSP-004 OD04-A T0 dry-run child (REV1).

Started only by supervisor_t0.ps1 with: python.exe -I -S -B -X pycache_prefix=<empty dir> probe_t0.py
Reads one nonce line from stdin, imports the harness/subject seed standard-library modules, and writes one JSON
line to stdout. It writes nothing to disk and runs no harness or subject code.
"""
import sys

SEEDS = ["__future__", "ctypes", "msvcrt", "os", "subprocess", "threading", "time", "hashlib", "importlib.machinery",
         "io", "types", "dataclasses", "math", "stat", "json", "pathlib", "collections.abc", "enum", "re", "typing"]


def main():
    nonce = sys.stdin.readline().strip()
    import importlib
    seeds = []
    for s in SEEDS:
        try:
            importlib.import_module(s)
            seeds.append([s, True])
        except Exception as e:
            seeds.append([s, type(e).__name__])
    import os, json
    mods = []
    for name, mod in sorted(sys.modules.items()):
        spec = getattr(mod, "__spec__", None)
        origin = getattr(spec, "origin", None) if spec else getattr(mod, "__file__", None)
        cached = getattr(spec, "cached", None) if spec else None
        mods.append({"Name": name, "Origin": origin,
                     "Loader": type(getattr(spec, "loader", None)).__name__ if spec else None,
                     "Cached": cached, "CachedExists": bool(cached) and os.path.exists(cached)})
    import ctypes
    from ctypes import wintypes as w
    psapi = ctypes.WinDLL("psapi", use_last_error=True)
    k32 = ctypes.WinDLL("kernel32", use_last_error=True)
    k32.GetCurrentProcess.restype = w.HANDLE
    psapi.EnumProcessModulesEx.argtypes = [w.HANDLE, ctypes.POINTER(w.HMODULE), w.DWORD, ctypes.POINTER(w.DWORD), w.DWORD]
    psapi.GetModuleFileNameExW.argtypes = [w.HANDLE, w.HMODULE, w.LPWSTR, w.DWORD]
    proc = k32.GetCurrentProcess()
    arr = (w.HMODULE * 1024)()
    need = w.DWORD()
    natives = []
    if psapi.EnumProcessModulesEx(proc, arr, ctypes.sizeof(arr), ctypes.byref(need), 0x03):
        for i in range(min(need.value // ctypes.sizeof(w.HMODULE), 1024)):
            buf = ctypes.create_unicode_buffer(32768)
            psapi.GetModuleFileNameExW(proc, arr[i], buf, 32768)
            natives.append(buf.value)
    out = {
        "Nonce": nonce, "Pid": os.getpid(), "Ppid": os.getppid(),
        "Version": sys.version, "Executable": sys.executable, "Prefix": sys.prefix,
        "PycachePrefix": sys.pycache_prefix, "DontWriteBytecode": sys.dont_write_bytecode,
        "Flags": {"isolated": sys.flags.isolated, "no_site": sys.flags.no_site,
                  "dont_write_bytecode": sys.flags.dont_write_bytecode, "ignore_environment": sys.flags.ignore_environment,
                  "no_user_site": sys.flags.no_user_site},
        "Path": list(sys.path), "Seeds": seeds, "Modules": mods, "Natives": natives,
    }
    sys.stdout.write(json.dumps(out, ensure_ascii=True) + "\n")
    sys.stdout.flush()


main()
