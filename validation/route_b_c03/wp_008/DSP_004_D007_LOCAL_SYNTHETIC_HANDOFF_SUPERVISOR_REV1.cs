#nullable enable
using System;
using System.Diagnostics;
using System.IO;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

// NEW local batch supervisor, not an accepted/platform execution interface.
// One process launch per compiled supervisor instance; no retry/input switches.
// Bound UTF-8 snapshot is sent on stdin to a fixed bounded bootstrap, rather
// than re-reading the harness by -File after its hash verification.
// Streams use remaining-budget + one detection-byte reads. Unexpected stderr,
// overflow, failures or deadline latch a failed outcome; no raw failure output.
// Host compilation/source reads/start/close/kill/dispose are synchronous and
// NOT proven bounded. Timers and kill requests do not prove complete engine or
// descendant settlement. Adversarial stop/overflow paths are not tested here.
public sealed class Dsp004D007LocalSyntheticHandoffSupervisorRev1
{
    private const string HarnessPath = "C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/DSP_004_D007_LOCAL_SYNTHETIC_HANDOFF_VALIDATION_REV1.ps1";
    private const string HarnessSha = "49D058C495432D6028ED32D33A356CCA0D0F7B02FC8A162FBFB607266C643749";
    private const int HarnessLength = 25015;
    private const string Executable = "C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe";
    private const int DeadlineMilliseconds = 120000;
    private static int reserved;
    private Dsp004D007LocalSyntheticHandoffSupervisorRev1() { }

    public static Observation RunSingleLocalBatch()
    {
        if (Interlocked.Exchange(ref reserved, 1) != 0)
        {
            return new Observation("REPEATED_BATCH_REFUSED", null, 0, false, false, false, false, -1, -1, -1, null, null, null, null);
        }

        var timer = Stopwatch.StartNew();
        Process? process = null;
        Task<BoundedRead>? stdoutTask = null;
        Task<BoundedRead>? stderrTask = null;
        Task? writeTask = null;
        bool launchAttempted = false;
        bool inputCloseReturned = false;
        bool stopRequested = false;
        bool exited = false;
        string? failureType = null;
        Exception? heldFailure = null;
        string? observedExeSha = null;
        string? tempDirectory = null;
        string outcome = "LOCAL_BATCH_FAILED";
        string? safeBody = null;
        int exitCode = -1;
        BoundedRead? stdout = null;
        BoundedRead? stderr = null;

        try
        {
            byte[] snapshot = File.ReadAllBytes(HarnessPath);
            if (snapshot.Length != HarnessLength || Convert.ToHexString(SHA256.HashData(snapshot)) != HarnessSha)
                throw new InvalidOperationException("FIXED_HARNESS_SNAPSHOT_MISMATCH");
            _ = new UTF8Encoding(false, true).GetString(snapshot);
            observedExeSha = Convert.ToHexString(SHA256.HashData(File.ReadAllBytes(Executable)));
            tempDirectory = Path.Combine(Path.GetTempPath(), "dsp004-d007-local-" + Guid.NewGuid().ToString("N"));
            Directory.CreateDirectory(tempDirectory);

            string bootstrap = @"$ErrorActionPreference='Stop'; $PSModuleAutoLoadingPreference='None'; try {
$inputStream=[Console]::OpenStandardInput(); $payload=[byte[]]::new(25015); $offset=0;
while($offset -lt 25015) { $n=$inputStream.Read($payload,$offset,25015-$offset); if($n -le 0) { throw [InvalidOperationException]::new() }; $offset+=$n };
if($inputStream.ReadByte() -ne -1) { throw [InvalidOperationException]::new() };
if([Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($payload)) -cne '49D058C495432D6028ED32D33A356CCA0D0F7B02FC8A162FBFB607266C643749') { throw [InvalidOperationException]::new() };
$text=[Text.UTF8Encoding]::new($false,$true).GetString($payload); & ([ScriptBlock]::Create($text))
} catch { [Console]::Error.Write('FIXED_BOOTSTRAP_FAILURE'); exit 2 }";
            var start = new ProcessStartInfo(Executable)
            {
                UseShellExecute = false,
                CreateNoWindow = true,
                RedirectStandardInput = true,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                StandardInputEncoding = new UTF8Encoding(false),
                StandardOutputEncoding = new UTF8Encoding(false, true),
                StandardErrorEncoding = new UTF8Encoding(false, true),
                WorkingDirectory = tempDirectory
            };
            start.ArgumentList.Add("-NoLogo");
            start.ArgumentList.Add("-NoProfile");
            start.ArgumentList.Add("-NonInteractive");
            start.ArgumentList.Add("-EncodedCommand");
            start.ArgumentList.Add(Convert.ToBase64String(Encoding.Unicode.GetBytes(bootstrap)));
            start.Environment.Clear();
            string systemRoot = Environment.GetFolderPath(Environment.SpecialFolder.Windows);
            start.Environment["SystemRoot"] = systemRoot;
            start.Environment["WINDIR"] = systemRoot;
            start.Environment["TEMP"] = tempDirectory;
            start.Environment["TMP"] = tempDirectory;
            start.Environment["USERPROFILE"] = tempDirectory;
            start.Environment["POWERSHELL_TELEMETRY_OPTOUT"] = "1";
            start.Environment["DOTNET_CLI_TELEMETRY_OPTOUT"] = "1";
            process = new Process { StartInfo = start };
            launchAttempted = true;
            if (!process.Start()) throw new InvalidOperationException("START_NOT_CONFIRMED");

            stdoutTask = ReadBounded(process.StandardOutput.BaseStream, 65536);
            stderrTask = ReadBounded(process.StandardError.BaseStream, 0);
            writeTask = process.StandardInput.BaseStream.WriteAsync(snapshot, 0, snapshot.Length);
            while (true)
            {
                if (writeTask.IsFaulted) throw writeTask.Exception!;
                if (stdoutTask.IsFaulted) throw stdoutTask.Exception!;
                if (stderrTask.IsFaulted) throw stderrTask.Exception!;
                if (writeTask.IsCanceled) throw new OperationCanceledException("INPUT_TASK_CANCELED");
                if (writeTask.IsCompletedSuccessfully && !inputCloseReturned)
                {
                    process.StandardInput.Close();
                    inputCloseReturned = true;
                }
                if (stdoutTask.IsCompletedSuccessfully && stdoutTask.Result.Overflow)
                    throw new InvalidOperationException("STDOUT_OVER_BUDGET");
                if (stderrTask.IsCompletedSuccessfully && stderrTask.Result.Overflow)
                    throw new InvalidOperationException("UNEXPECTED_STDERR");
                exited = process.HasExited;
                if (exited && inputCloseReturned && stdoutTask.IsCompletedSuccessfully && stderrTask.IsCompletedSuccessfully)
                {
                    stdout = stdoutTask.Result;
                    stderr = stderrTask.Result;
                    exitCode = process.ExitCode;
                    if (!stdout.Eof || !stderr.Eof || stdout.Count == 0)
                        throw new InvalidOperationException("CHILD_COMPLETION_GATE_FAILED");
                    safeBody = new UTF8Encoding(false, true).GetString(stdout.Body);
                    // Nonzero normal exit is preserved as failed observation,
                    // not retried or converted to PASS. Caller must parse the
                    // bounded body as the exact expected JSON schema before use.
                    outcome = exitCode == 0 ? "LOCAL_CHILD_NORMAL_RETURN_OBSERVED" : "LOCAL_CHILD_NONZERO_EXIT_OBSERVED";
                    break;
                }
                if (timer.ElapsedMilliseconds >= DeadlineMilliseconds)
                    throw new TimeoutException("LOCAL_DEADLINE_EXCEEDED");
                Thread.Sleep(10);
            }
        }
        catch (Exception error)
        {
            heldFailure = error;
            failureType = error.GetType().FullName;
            safeBody = null;
            if (process != null && launchAttempted)
            {
                stopRequested = true;
                try { if (!process.HasExited) process.Kill(true); }
                catch (Exception stopError) { heldFailure = new AggregateException(error, stopError); }
                try { exited = process.WaitForExit(5000); }
                catch { exited = false; }
                try
                {
                    if (stdoutTask != null && stderrTask != null)
                        Task.WaitAll(new Task[] { stdoutTask, stderrTask }, 5000);
                }
                catch { /* task failure/settlement remains separately unconfirmed */ }
            }
            if (stdoutTask?.IsCompletedSuccessfully == true) stdout = stdoutTask.Result;
            if (stderrTask?.IsCompletedSuccessfully == true) stderr = stderrTask.Result;
        }

        // No Dispose call is treated as a settlement certificate. A normal
        // child is observed exited with both bounded reads EOF; failed tasks
        // may remain unsettled. Original errors stay private in this record.
        return new Observation(outcome, safeBody, timer.ElapsedMilliseconds,
            launchAttempted, inputCloseReturned, exited, stopRequested,
            exitCode, stdout?.Count ?? -1, stderr?.Count ?? -1,
            failureType, observedExeSha, tempDirectory, heldFailure);
    }

    private static async Task<BoundedRead> ReadBounded(Stream stream, int budget)
    {
        using var body = new MemoryStream();
        int count = 0;
        while (true)
        {
            byte[] buffer = new byte[Math.Min(4096, budget - count + 1)];
            int returned = await stream.ReadAsync(buffer.AsMemory(0, buffer.Length)).ConfigureAwait(false);
            if (returned == 0) return new BoundedRead(body.ToArray(), count, false, true);
            count += returned;
            if (count > budget) return new BoundedRead(Array.Empty<byte>(), count, true, false);
            body.Write(buffer, 0, returned);
        }
    }

    private sealed class BoundedRead
    {
        internal byte[] Body { get; }
        internal int Count { get; }
        internal bool Overflow { get; }
        internal bool Eof { get; }
        internal BoundedRead(byte[] body, int count, bool overflow, bool eof)
        { Body = body; Count = count; Overflow = overflow; Eof = eof; }
    }

    public sealed class Observation
    {
        private readonly Exception? heldFailure;
        internal Observation(string outcome, string? body, long elapsed, bool launch, bool closed,
            bool exited, bool stop, int exitCode, int stdout, int stderr,
            string? failureType, string? executableSha, string? temp, Exception? failure)
        {
            Outcome = outcome; ChildJsonBody = body; ElapsedMilliseconds = elapsed;
            LaunchAttempted = launch; InputCloseReturned = closed; ChildExitObserved = exited;
            StopRequested = stop; ExitCode = exitCode; StdoutBytes = stdout; StderrBytes = stderr;
            FailureType = failureType; ExecutableFileSHA256 = executableSha;
            TemporaryDirectory = temp; heldFailure = failure;
        }
        public string Outcome { get; }
        public string? ChildJsonBody { get; }
        public long ElapsedMilliseconds { get; }
        public bool LaunchAttempted { get; }
        public bool InputCloseReturned { get; }
        public bool ChildExitObserved { get; }
        public bool StopRequested { get; }
        public int ExitCode { get; }
        public int StdoutBytes { get; }
        public int StderrBytes { get; }
        public string? FailureType { get; }
        public string? ExecutableFileSHA256 { get; }
        public string? TemporaryDirectory { get; }
        public string InputSnapshotQualification => "FIXED HARNESS SNAPSHOT VERIFIED AGAIN IN CHILD; NOT TRUSTED ROOT";
        public string StopQualification => "NO ADVERSARIAL STOP OR COMPLETE DESCENDANT SETTLEMENT PROOF";
    }
}
