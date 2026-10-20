"""Closed synthetic fault subjects. Never used as the 158-case native oracle."""
import os
import sys
import time
import msvcrt
from io import FileIO

READY = b"DSP004-READY-V1|158|UNVERIFIED_REPORT\n"
STOP = b"DSP004-COMMAND-V1|STOP\n"
STOPPED = b"DSP004-STOPPED-V1|UNVERIFIED_REPORT\n"
ALLOWED = (
    "HANG", "STDOUT", "STDERR", "BAD_READY", "PARTIAL", "OVERLONG",
    "EARLY_EOF", "DUPLICATE", "OUT_OF_ORDER", "SETUP_NE", "CASE_FAIL",
    "TRAILER", "DESCENDANT", "REAL_INTERRUPT", "STDOUT_LATE", "STDERR_LATE",
)

def read_frame(stream):
    data = bytearray()
    while len(data) < 4096:
        byte = stream.read(1)
        if not byte:
            raise RuntimeError("FIXTURE_COMMAND_EOF")
        data.extend(byte)
        if byte == b"\n":
            return bytes(data)
    raise RuntimeError("FIXTURE_COMMAND_OVERFLOW")

def write(stream, data):
    while data:
        count = stream.write(data)
        if type(count) is not int or count <= 0:
            raise RuntimeError("FIXTURE_WRITE")
        data = data[count:]

def main():
    if len(sys.argv) != 4 or sys.argv[3] not in ALLOWED:
        return 78
    command = FileIO(msvcrt.open_osfhandle(int(sys.argv[1]), os.O_RDONLY | os.O_BINARY), "rb")
    report = FileIO(msvcrt.open_osfhandle(int(sys.argv[2]), os.O_WRONLY | os.O_BINARY), "wb")
    mode = sys.argv[3]
    try:
        if mode == "HANG":
            time.sleep(60)
        elif mode in ("STDOUT", "STDERR"):
            os.write(1 if mode == "STDOUT" else 2, b"X")
            time.sleep(60)
        elif mode == "BAD_READY":
            write(report, b"BAD\n")
            time.sleep(60)
        elif mode == "PARTIAL":
            write(report, READY[:-1])
            time.sleep(60)
        elif mode == "OVERLONG":
            write(report, b"X" * 4096 + b"\n")
            time.sleep(60)
        elif mode == "EARLY_EOF":
            return 0
        elif mode == "DESCENDANT":
            import subprocess
            # Closed pure-sleep child, no shell/path discovery or business data.
            child = subprocess.Popen(
                [sys.executable, "-I", "-S", "-B", "-c", "import time; time.sleep(60)"],
                stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL, close_fds=True, creationflags=0x08000000)
            write(report, b"DSP004-DESCENDANT-V1\n")
            time.sleep(60)
            child.wait()
        else:
            write(report, READY)
            first = read_frame(command)
            if first != b"DSP004-COMMAND-V1|NEXT|1|C01-variant_id-NONE\n":
                return 79
            if mode == "REAL_INTERRUPT":
                raise KeyboardInterrupt()
            if mode == "OUT_OF_ORDER":
                write(report, b"DSP004-CAPTURE-V1|2|C01-variant_id-BOOL|SUT|PASS|UNVERIFIED_REPORT\n")
                time.sleep(60)
            elif mode == "DUPLICATE":
                frame = b"DSP004-CAPTURE-V1|1|C01-variant_id-NONE|SUT|PASS|UNVERIFIED_REPORT\n"
                write(report, frame + frame)
                time.sleep(60)
            else:
                result = b"SETUP|NOT_EVALUABLE" if mode == "SETUP_NE" else b"SUT|FAIL"
                write(report, b"DSP004-CAPTURE-V1|1|C01-variant_id-NONE|" + result + b"|UNVERIFIED_REPORT\n")
                if read_frame(command) != STOP or command.read(1) != b"":
                    return 79
                write(report, STOPPED + (b"EXTRA\n" if mode == "TRAILER" else b""))
                if mode in ("STDOUT_LATE", "STDERR_LATE"):
                    report.close()
                    os.write(1 if mode == "STDOUT_LATE" else 2, b"X")
        return 0
    finally:
        command.close()
        report.close()

if __name__ == "__main__":
    try:
        code = main()
    except BaseException:
        code = 78
    raise SystemExit(code)
