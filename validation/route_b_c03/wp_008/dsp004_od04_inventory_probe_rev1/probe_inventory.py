"""DSP-004 OD-04 inventory-only probe (REV1).

Authorized by the owner's Path B re-sign sentence of 2026-10-31: one read-only inventory probe run that reads the
interpreter version, built-in and frozen modules, and the actual origins of loaded modules. It imports only standard
library modules named by the harness and subject direct-import inventories. It writes exactly one JSON file next to
itself and nothing else. Run with:  python.exe -I -S -B probe_inventory.py
"""
import sys

T_START = None
SEEDS = ["__future__", "ctypes", "msvcrt", "os", "subprocess", "threading", "time", "hashlib", "importlib.machinery",
         "io", "types", "dataclasses", "math", "stat", "json", "pathlib", "collections.abc", "enum", "re", "typing"]


def module_rows():
    rows = []
    for name, mod in sorted(sys.modules.items()):
        spec = getattr(mod, "__spec__", None)
        rows.append({
            "Name": name,
            "Origin": getattr(spec, "origin", None) if spec else getattr(mod, "__file__", None),
            "Loader": type(getattr(spec, "loader", None)).__name__ if spec else None,
            "Cached": getattr(spec, "cached", None) if spec else None,
        })
    return rows


def main():
    import _imp
    startup = module_rows()
    flags = {k: getattr(sys.flags, k) for k in dir(sys.flags) if not k.startswith("_") and isinstance(getattr(sys.flags, k), int)}
    out = {
        "ProbeKind": "DSP004_OD04_INVENTORY_ONLY_PROBE_REV1",
        "Version": sys.version,
        "VersionInfo": list(sys.version_info),
        "Implementation": sys.implementation.name,
        "Executable": sys.executable,
        "BaseExecutable": getattr(sys, "_base_executable", None),
        "Prefix": sys.prefix, "BasePrefix": sys.base_prefix,
        "Flags": flags,
        "DontWriteBytecode": sys.dont_write_bytecode,
        "Path": list(sys.path),
        "BuiltinModuleNames": sorted(sys.builtin_module_names),
        "FrozenModuleNames": sorted(_imp._frozen_module_names()) if hasattr(_imp, "_frozen_module_names") else None,
        "ModulesAtStartup": startup,
    }
    import importlib
    seed_results = []
    for s in SEEDS:
        try:
            importlib.import_module(s)
            seed_results.append({"Seed": s, "Imported": True})
        except Exception as e:  # recorded, not raised
            seed_results.append({"Seed": s, "Imported": False, "Error": type(e).__name__})
    out["SeedImports"] = seed_results
    out["ModulesAfterSeeds"] = module_rows()

    # Loaded native modules of this process (inventory only), with read-only SHA-256 of each file.
    import ctypes, hashlib
    from ctypes import wintypes as w
    psapi = ctypes.WinDLL("psapi", use_last_error=True)
    k32 = ctypes.WinDLL("kernel32", use_last_error=True)
    k32.GetCurrentProcess.restype = w.HANDLE
    proc = k32.GetCurrentProcess()
    arr = (w.HMODULE * 1024)()
    needed = w.DWORD()
    psapi.EnumProcessModulesEx.argtypes = [w.HANDLE, ctypes.POINTER(w.HMODULE), w.DWORD, ctypes.POINTER(w.DWORD), w.DWORD]
    psapi.GetModuleFileNameExW.argtypes = [w.HANDLE, w.HMODULE, w.LPWSTR, w.DWORD]
    ok = psapi.EnumProcessModulesEx(proc, arr, ctypes.sizeof(arr), ctypes.byref(needed), 0x03)
    natives = []
    if ok:
        for i in range(min(needed.value // ctypes.sizeof(w.HMODULE), 1024)):
            buf = ctypes.create_unicode_buffer(32768)
            psapi.GetModuleFileNameExW(proc, arr[i], buf, 32768)
            p = buf.value
            row = {"Path": p}
            try:
                with open(p, "rb") as f:
                    b = f.read()
                row["Bytes"] = len(b)
                row["SHA256"] = hashlib.sha256(b).hexdigest().upper()
            except OSError as e:
                row["ReadError"] = type(e).__name__
            natives.append(row)
    out["NativeModulesLoaded"] = natives
    out["EnumProcessModulesOk"] = bool(ok)

    import json, os
    dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), "probe_inventory_result.json")
    with open(dst, "x", encoding="utf-8") as f:  # 'x': never overwrite an earlier result
        json.dump(out, f, ensure_ascii=False, indent=1)
    print("WROTE", dst)


main()
