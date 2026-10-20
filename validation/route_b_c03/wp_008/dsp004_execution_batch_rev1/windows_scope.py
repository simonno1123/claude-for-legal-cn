"""Owned Windows-only synthetic process scope; not a sandbox or authority API.

Sources: Microsoft CreateProcessW / UpdateProcThreadAttribute / Job Objects.
JOB_LIST assigns the new child at creation, avoiding create-then-assign gaps.
Only five declared pipe handles are inherited; job handle is NOT inherited.
All operations concern this scope's own native handles. No global process
search, PID-based killing, shell execution, installation or network calls.
Unsettled writers/handles/errors stay strongly held. OS calls are not claimed
interruptible; a separate driver process owns an outer kill-on-close job.
"""
from __future__ import annotations

import ctypes as c
from ctypes import wintypes as w
import msvcrt
import os
import subprocess
import threading
import time

PYTHON = "C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe"
_HELD_SCOPES = []
K = c.WinDLL("kernel32", use_last_error=True)
SIZE_T = c.c_size_t
HANDLE = w.HANDLE

class _Startup(c.Structure):
    _fields_ = [
        ("cb", w.DWORD), ("lpReserved", w.LPWSTR), ("lpDesktop", w.LPWSTR),
        ("lpTitle", w.LPWSTR), ("dwX", w.DWORD), ("dwY", w.DWORD),
        ("dwXSize", w.DWORD), ("dwYSize", w.DWORD),
        ("dwXCountChars", w.DWORD), ("dwYCountChars", w.DWORD),
        ("dwFillAttribute", w.DWORD), ("dwFlags", w.DWORD),
        ("wShowWindow", w.WORD), ("cbReserved2", w.WORD),
        ("lpReserved2", c.c_void_p), ("hStdInput", HANDLE),
        ("hStdOutput", HANDLE), ("hStdError", HANDLE),
    ]

class _StartupEx(c.Structure):
    _fields_ = [("startup", _Startup), ("attributes", c.c_void_p)]

class _ProcessInfo(c.Structure):
    _fields_ = [("process", HANDLE), ("thread", HANDLE),
                ("pid", w.DWORD), ("tid", w.DWORD)]

class _BasicLimit(c.Structure):
    _fields_ = [
        ("process_time", c.c_longlong), ("job_time", c.c_longlong),
        ("flags", w.DWORD), ("min_working_set", SIZE_T),
        ("max_working_set", SIZE_T), ("active_limit", w.DWORD),
        ("affinity", SIZE_T), ("priority", w.DWORD), ("scheduling", w.DWORD),
    ]

class _IoCounters(c.Structure):
    _fields_ = [(name, c.c_ulonglong) for name in (
        "read_ops", "write_ops", "other_ops", "read_bytes", "write_bytes", "other_bytes")]

class _ExtendedLimit(c.Structure):
    _fields_ = [("basic", _BasicLimit), ("io", _IoCounters),
                ("process_memory", SIZE_T), ("job_memory", SIZE_T),
                ("peak_process", SIZE_T), ("peak_job", SIZE_T)]

class _Accounting(c.Structure):
    _fields_ = [
        ("user_time", c.c_longlong), ("kernel_time", c.c_longlong),
        ("period_user_time", c.c_longlong), ("period_kernel_time", c.c_longlong),
        ("page_faults", w.DWORD), ("total", w.DWORD),
        ("active", w.DWORD), ("terminated", w.DWORD),
    ]

def _declare(name, result, arguments):
    function = getattr(K, name)
    function.restype, function.argtypes = result, arguments
    return function

_create_job = _declare("CreateJobObjectW", HANDLE, [c.c_void_p, w.LPCWSTR])
_set_job = _declare("SetInformationJobObject", w.BOOL, [HANDLE, c.c_int, c.c_void_p, w.DWORD])
_query_job = _declare("QueryInformationJobObject", w.BOOL, [HANDLE, c.c_int, c.c_void_p, w.DWORD, c.c_void_p])
_kill_job = _declare("TerminateJobObject", w.BOOL, [HANDLE, w.UINT])
_close = _declare("CloseHandle", w.BOOL, [HANDLE])
_wait = _declare("WaitForSingleObject", w.DWORD, [HANDLE, w.DWORD])
_exit_code = _declare("GetExitCodeProcess", w.BOOL, [HANDLE, c.POINTER(w.DWORD)])
_resume = _declare("ResumeThread", w.DWORD, [HANDLE])
_init_attributes = _declare("InitializeProcThreadAttributeList", w.BOOL,
    [c.c_void_p, w.DWORD, w.DWORD, c.POINTER(SIZE_T)])
_update_attribute = _declare("UpdateProcThreadAttribute", w.BOOL,
    [c.c_void_p, w.DWORD, SIZE_T, c.c_void_p, SIZE_T, c.c_void_p, c.c_void_p])
_delete_attributes = _declare("DeleteProcThreadAttributeList", None, [c.c_void_p])
_create_process = _declare("CreateProcessW", w.BOOL,
    [w.LPCWSTR, w.LPWSTR, c.c_void_p, c.c_void_p, w.BOOL, w.DWORD,
     c.c_void_p, w.LPCWSTR, c.c_void_p, c.POINTER(_ProcessInfo)])
_peek = _declare("PeekNamedPipe", w.BOOL,
    [HANDLE, c.c_void_p, w.DWORD, c.c_void_p, c.POINTER(w.DWORD), c.c_void_p])

class BoundaryFailure(RuntimeError):
    """Fixed local code only; never includes payload/error rendering."""

def _require(ok, code):
    if not ok:
        error = c.get_last_error()
        raise OSError(error, code)

class _Write:
    def __init__(self, owner, role, payload, close_after):
        self.owner, self.role = owner, role
        self.payload = payload  # Owned immutable bytes, held while native write runs.
        self.close_after = close_after
        self.done = threading.Event()
        self.error = None
        self.thread = threading.Thread(target=self._run, daemon=True)

    def _run(self):
        try:
            offset = 0
            while offset < len(self.payload):
                count = os.write(self.owner.fds[self.role], self.payload[offset:])
                if not 0 < count <= len(self.payload) - offset:
                    raise BoundaryFailure("INCOMPLETE_WRITE")
                offset += count
            if self.close_after:
                self.owner.close_fd(self.role)
        except BaseException as original:
            self.error = original
            self.owner.keep_error("WRITE_" + self.role.upper(), original)
        finally:
            self.done.set()

class JobChild:
    """Internal test harness primitive. Possession is NOT execution permission."""
    def __init__(self, t0, hard_due):
        self.t0, self.hard_due = t0, hard_due
        self.lock = threading.RLock()
        self.fds = {}
        self.child_fds = []
        self.writes = []
        self.errors = []
        self.cleanup_errors = []
        self.stopped = False
        self.job = None
        self.info = _ProcessInfo()  # Rooted before CreateProcessW.
        self.created = False
        self.resumed = False
        self.kill_requested = False
        self.kill_returned = False
        self.clean = False
        self.last_active = None
        self.observed_exit = None
        self.standard_detected = {"stdout": 0, "stderr": 0}
        self.eof = {}
        self.attr_buffer = None
        self.attribute_initialized = False
        self.handle_values = None
        self.job_values = None
        _HELD_SCOPES.append(self)  # Before job/pipe/process attempts.

    def check(self, due, protective=False):
        if time.monotonic() >= min(due, self.hard_due):
            raise BoundaryFailure("DEADLINE")
        if self.stopped and not protective:
            raise BoundaryFailure("STOP_LATCHED")

    def keep_error(self, phase, original):
        with self.lock:
            self.errors.append((phase, original))
            self.stopped = True

    def stop_latch(self):
        with self.lock:
            self.stopped = True

    def close_fd(self, role):
        with self.lock:
            fd = self.fds.get(role)
            if fd is not None:
                os.close(fd)
                del self.fds[role]

    def start(self, script, cwd, extra_arguments=()):
        self.check(self.hard_due)
        if (os.name != "nt" or type(script) is not bytes or self.created
                or any(type(value) is not str for value in extra_arguments)):
            raise BoundaryFailure("FIXED_NATIVE_START_BOUNDARY")
        try:
            self.job = _create_job(None, None)
            _require(self.job, "CREATE_OWN_JOB")
            limits = _ExtendedLimit()
            limits.basic.flags = 0x2000 | 0x8 | 0x100  # kill-on-close, active limit, process memory
            limits.basic.active_limit = 8
            limits.process_memory = 256 * 1024 * 1024
            _require(_set_job(self.job, 9, c.byref(limits), c.sizeof(limits)), "SET_OWN_JOB_LIMITS")
            child_roles = []
            for role, parent_writes in (
                ("code", True), ("command", True), ("report", False),
                ("stdout", False), ("stderr", False),
            ):
                self.check(self.hard_due)
                read_fd, write_fd = os.pipe()
                parent_fd, child_fd = (write_fd, read_fd) if parent_writes else (read_fd, write_fd)
                self.fds[role] = parent_fd
                self.child_fds.append(child_fd)
                parent_handle = msvcrt.get_osfhandle(parent_fd)
                child_handle = msvcrt.get_osfhandle(child_fd)
                os.set_handle_inheritable(parent_handle, False)
                os.set_handle_inheritable(child_handle, True)
                child_roles.append(child_handle)
            self.handle_values = (HANDLE * 5)(*child_roles)
            self.job_values = (HANDLE * 1)(self.job)
            size = SIZE_T()
            _init_attributes(None, 2, 0, c.byref(size))  # Expected sizing failure.
            if not 0 < size.value <= 65536:
                raise BoundaryFailure("ATTRIBUTE_SIZE")
            self.attr_buffer = c.create_string_buffer(size.value)
            _require(_init_attributes(self.attr_buffer, 2, 0, c.byref(size)), "INITIALIZE_ATTRIBUTES")
            self.attribute_initialized = True
            _require(_update_attribute(self.attr_buffer, 0, 0x00020002,
                self.handle_values, c.sizeof(self.handle_values), None, None), "EXPLICIT_HANDLE_LIST")
            _require(_update_attribute(self.attr_buffer, 0, 0x0002000D,
                self.job_values, c.sizeof(self.job_values), None, None), "ATOMIC_JOB_LIST")
            startup = _StartupEx()
            startup.startup.cb = c.sizeof(startup)
            startup.startup.dwFlags = 0x100  # STARTF_USESTDHANDLES
            startup.startup.hStdInput = child_roles[0]
            startup.startup.hStdOutput = child_roles[3]
            startup.startup.hStdError = child_roles[4]
            startup.attributes = c.addressof(self.attr_buffer)
            arguments = [PYTHON, "-I", "-S", "-B", "-c", script.decode("utf-8", "strict"),
                         str(child_roles[1]), str(child_roles[2]), *extra_arguments]
            command = subprocess.list2cmdline(arguments)
            if len(command) >= 32767:
                raise BoundaryFailure("NATIVE_COMMAND_LENGTH")
            root = os.environ.get("SystemRoot", "C:\\Windows")
            if not os.path.isabs(root):
                raise BoundaryFailure("SYSTEM_ROOT_UNBOUND")
            environment = c.create_unicode_buffer(
                "PATH=" + os.path.dirname(PYTHON) + ";" + root + "\\System32\0"
                + "SystemRoot=" + root + "\0WINDIR=" + root + "\0\0")
            self.check(self.hard_due)
            # Job assignment is atomic with creation. No create-then-assign fallback.
            flags = 0x4 | 0x80000 | 0x8000000 | 0x400  # suspended/ex/start-hidden/unicode env
            _require(_create_process(PYTHON, c.create_unicode_buffer(command),
                None, None, True, flags, environment, cwd, c.byref(startup),
                c.byref(self.info)), "CREATE_OWN_SUSPENDED_CHILD")
            self.created = True
            for fd in tuple(self.child_fds):
                os.close(fd)
                self.child_fds.remove(fd)
            self.check(self.hard_due)
            result = _resume(self.info.thread)
            _require(result != 0xFFFFFFFF, "RESUME_OWN_CHILD")
            self.resumed = True
            _require(_close(self.info.thread), "CLOSE_OWN_PRIMARY_THREAD")
            self.info.thread = None
        except BaseException as original:
            self.keep_error("START", original)
            raise
        finally:
            if self.attribute_initialized:
                _delete_attributes(self.attr_buffer)
                self.attribute_initialized = False

    def write(self, role, payload, due, *, close_after=False, stopping=False):
        with self.lock:
            self.check(due, protective=stopping)
            if role not in ("code", "command") or type(payload) is not bytes:
                raise BoundaryFailure("WRITE_ROLE_OR_BYTES")
            previous = [task for task in self.writes if task.role == role]
            if previous and (not previous[-1].done.is_set()
                             or previous[-1].thread.is_alive() or previous[-1].error is not None):
                raise BoundaryFailure("PREVIOUS_WRITE_UNSETTLED")
            task = _Write(self, role, payload, close_after)
            self.writes.append(task)  # Before starting native work.
            self.check(due, protective=stopping)
            task.thread.start()  # Serialized with the stop latch.
            return task

    def poll(self, role, maximum=1):
        fd = self.fds[role]
        available = w.DWORD()
        ok = _peek(msvcrt.get_osfhandle(fd), None, 0, None, c.byref(available), None)
        if not ok:
            error = c.get_last_error()
            if error == 109:
                data = os.read(fd, 1)  # Actual zero-read after broken-writer observation.
                if data != b"":
                    raise BoundaryFailure("PIPE_EOF_CHANGED")
                self.eof[role] = True
                return b""
            raise OSError(error, "PEEK_OWN_PIPE")
        if not available.value:
            return None
        return os.read(fd, min(maximum, available.value))

    def monitor_zero(self):
        for role in ("stdout", "stderr"):
            data = self.poll(role)
            if data:
                self.standard_detected[role] += len(data)
                self.stop_latch()
                raise BoundaryFailure("FORBIDDEN_" + role.upper() + "_BYTE")

    def wait_write(self, task, due, protective=False):
        while True:
            self.check(due, protective=protective)
            self.monitor_zero()
            if task.done.is_set() and not task.thread.is_alive():
                if task.error is not None:
                    raise task.error
                return
            time.sleep(0.002)

    def frame(self, due, limit=4096, protective=False):
        data = bytearray()
        while len(data) < limit:
            self.check(due, protective=protective)
            self.monitor_zero()
            piece = self.poll("report")
            if piece == b"":
                raise BoundaryFailure("REPORT_EOF")
            if piece is None:
                time.sleep(0.002)
                continue
            data.extend(piece)
            if piece == b"\n":
                return bytes(data)
            if not 32 <= piece[0] <= 126:
                raise BoundaryFailure("REPORT_NON_ASCII")
        raise BoundaryFailure("REPORT_OVERFLOW")

    def active(self):
        if not self.job:
            return 0
        accounting = _Accounting()
        _require(_query_job(self.job, 1, c.byref(accounting), c.sizeof(accounting), None),
                 "QUERY_OWN_JOB")
        self.last_active = int(accounting.active)
        return self.last_active

    def exited(self):
        if not self.created:
            return True
        result = _wait(self.info.process, 0)
        if result == 0xFFFFFFFF:
            raise OSError(c.get_last_error(), "WAIT_OWN_CHILD")
        return result == 0

    def exit_code(self):
        if not self.created or not self.exited():
            return None
        code = w.DWORD()
        _require(_exit_code(self.info.process, c.byref(code)), "OWN_CHILD_EXIT_CODE")
        return int(code.value)

    def kill(self):
        self.stop_latch()
        if self.job:
            self.kill_requested = True
            _require(_kill_job(self.job, 79), "TERMINATE_OWN_JOB")
            self.kill_returned = True

    def settle(self, due, *, terminate):
        """No task/stream is discarded as a consequence of a timeout alone."""
        self.stop_latch()
        if terminate and self.job:
            try:
                self.kill()
            except BaseException as original:
                self.cleanup_errors.append(("JOB_TERMINATE", original))
        while time.monotonic() < due:
            try:
                if self.exited() and self.active() == 0 and self.writers_settled():
                    break
            except BaseException as original:
                self.cleanup_errors.append(("SETTLEMENT_OBSERVE", original))
                return False
            time.sleep(0.002)
        try:
            settled = (self.exited() and self.active() == 0 and self.writers_settled())
        except BaseException as original:
            self.cleanup_errors.append(("SETTLEMENT_FINAL_OBSERVE", original))
            return False
        if not settled:
            return False  # Keep all handles/tasks and the outer guardian.
        if self.created:
            self.observed_exit = self.exit_code()
        # On a partial start, our still-owned child pipe ends can themselves
        # keep writers open. No live child remains, so close each owned end
        # before demanding EOF; retain any failed close, do not clear blindly.
        for fd in tuple(self.child_fds):
            try:
                os.close(fd)
                self.child_fds.remove(fd)
            except BaseException as original:
                self.cleanup_errors.append(("CHILD_END_CLOSE", original))
                return False
        # Exited/zero-active does not prove silence. Consume the owned standard
        # read ends to ACTUAL EOF before they may be closed; retain only counts.
        for role in ("stdout", "stderr"):
            if role not in self.fds:
                continue
            while not self.eof.get(role):
                if time.monotonic() >= min(due, self.hard_due):
                    return False
                try:
                    data = self.poll(role, maximum=4096)
                except BaseException as original:
                    self.cleanup_errors.append(("FINAL_STANDARD_READ", original))
                    return False
                if data:
                    self.standard_detected[role] += len(data)
                elif data is None:
                    time.sleep(0.002)
        for task in self.writes:
            task.thread.join(0)
        for role in tuple(self.fds):
            try:
                self.close_fd(role)
            except BaseException as original:
                self.cleanup_errors.append(("PIPE_CLOSE", original))
        for field in ("thread", "process"):
            value = getattr(self.info, field)
            if value:
                try:
                    _require(_close(value), "CLOSE_OWN_" + field.upper())
                    setattr(self.info, field, None)
                except BaseException as original:
                    self.cleanup_errors.append(("HANDLE_CLOSE", original))
        if self.job:
            try:
                _require(_close(self.job), "CLOSE_OWN_JOB")
                self.job = None
            except BaseException as original:
                self.cleanup_errors.append(("JOB_CLOSE", original))
        self.clean = not self.cleanup_errors and not self.fds and not self.child_fds
        return self.clean

    def writers_settled(self):
        # Event publication occurs just BEFORE _run returns; it is not thread exit.
        return all(task.done.is_set() and not task.thread.is_alive() for task in self.writes)
