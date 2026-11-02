"""DSP-004 OD04-A T0 dry-run child, v3.

Started only by supervisor_v3.ps1 as: python.exe -I -S -B <this file>
No extra arguments, no environment input (the supervisor passes a minimal fixed environment), no stdin data
(the supervisor closes stdin at once). It imports the harness/subject seed standard-library modules, checks without
waiting that stdin is already at EOF, writes one JSON line to stdout, pauses a fixed 10 seconds so the supervisor can
enumerate this process's loaded modules from outside, and exits. It never waits on stdin. It writes nothing to disk and runs
no harness or subject code. Everything it reports is a child self-report; the supervisor does not rely on it alone.
"""
import sys

SEEDS = ["__future__", "ctypes", "msvcrt", "os", "subprocess", "threading", "time", "hashlib", "importlib.machinery",
         "io", "types", "dataclasses", "math", "stat", "json", "pathlib", "collections.abc", "enum", "re", "typing"]


def main():
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
        loader = getattr(spec, "loader", None) if spec else None
        lname = None if loader is None else (loader.__name__ if isinstance(loader, type) else type(loader).__name__)
        mods.append({"Name": name,
                     "Origin": getattr(spec, "origin", None) if spec else getattr(mod, "__file__", None),
                     "Loader": lname})
    try:
        stdin_eof = (os.read(0, 1) == b"")
    except OSError:
        stdin_eof = None
    main_file = getattr(sys.modules.get("__main__"), "__file__", None)
    out = {"Pid": os.getpid(), "Ppid": os.getppid(), "Version": sys.version, "Executable": sys.executable,
           "MainFile": main_file, "Path": list(sys.path), "PycachePrefix": sys.pycache_prefix,
           "Flags": {"isolated": sys.flags.isolated, "no_site": sys.flags.no_site,
                     "dont_write_bytecode": sys.flags.dont_write_bytecode,
                     "ignore_environment": sys.flags.ignore_environment, "no_user_site": sys.flags.no_user_site},
           "EnvironNames": sorted(os.environ.keys()), "StdinAtEof": stdin_eof, "Seeds": seeds, "Modules": mods}
    sys.stdout.write(json.dumps(out, ensure_ascii=True) + "\n")
    sys.stdout.flush()
    import time
    time.sleep(10)  # fixed pause for outside-in enumeration; nothing is read


main()
