#nullable enable
namespace Dsp004SyntheticStops
{
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

// NEW closed local test carrier ONLY; not accepted/integrated. REV2 is unchanged.
// No real driver, business input, source admission, arbitrary script/path,
// callback, runtime grant, external model or other project is accepted.
// REV2 internal pure classifiers are reused; THIS I/O/stop implementation is
// distinct. Its outcomes cannot be transferred to REV2 production coverage.
// Synthetic ACKs are NOT input-SHA verification or authority evidence.
public sealed class Dsp004LocalSyntheticStopPathCarrierRev1
{
    private const string Executable = "C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe";
    private const int ShortBudgetMilliseconds = 5000;
    private const long ClassifierOffsetMilliseconds = 115000;
    private static int reserved;
    private Dsp004LocalSyntheticStopPathCarrierRev1() { }

    public static CaseObservation[] RunFixedSyntheticBatch()
    {
        if (Interlocked.Exchange(ref reserved, 1) != 0)
            return new[] { new CaseObservation("BATCH-REPEAT", "REPEATED_TEST_BATCH_REFUSED") };
        string executableSha = Convert.ToHexString(SHA256.HashData(File.ReadAllBytes(Executable)));
        var observations = new List<CaseObservation>();
        for (int caseNumber = 1; caseNumber <= 7; caseNumber++)
            observations.Add(RunOneFixedCase(caseNumber, executableSha));
        return observations.ToArray();
    }

    private static string FixedScript(int caseNumber)
    {
        const string prefix = "$ErrorActionPreference='Stop'; $PSModuleAutoLoadingPreference='None'; ";
        const string ack = "[Console]::Out.Write('DSP004-SNAPSHOT-ACK-V2' + [char]10); ";
        const string body = "[Console]::Out.Write('{\"synthetic\":\"CONTROL_ONLY\"}' + [char]10); [Console]::Out.Flush(); ";
        return caseNumber switch
        {
            1 => prefix + ack + body + "exit 0",
            2 => prefix + ack + body + "[Threading.Thread]::Sleep(15000); exit 0",
            3 => prefix + "[Console]::Out.Write([string]::new([char]88,65537)); [Console]::Out.Flush(); [Threading.Thread]::Sleep(15000); exit 0",
            4 => prefix + "[Console]::Error.Write('X'); [Console]::Error.Flush(); [Threading.Thread]::Sleep(15000); exit 0",
            5 => prefix + body + "exit 0",
            6 => prefix + ack + body + "exit 7",
            7 => prefix + "exit 0",
            _ => throw new InvalidOperationException("FIXED_CASE_NOT_DEFINED")
        };
    }

    private static void CheckShortDeadline(Stopwatch timer)
    {
        long mapped = timer.ElapsedMilliseconds + ClassifierOffsetMilliseconds;
        if (Dsp004D007LocalSyntheticHandoffSupervisorRev2.ClassifyProgress(mapped, false) == "DEADLINE_REFUSED")
            throw new TimeoutException("SYNTHETIC_SHORT_DEADLINE");
    }

    private static CaseObservation RunOneFixedCase(int caseNumber, string executableSha)
    {
        var observation = new CaseObservation("S-" + caseNumber.ToString("D2"), "NOT_COMPLETED");
        observation.ExecutableFileSHA256 = executableSha;
        var timer = Stopwatch.StartNew();
        Process? process = null;
        Task<ReadObservation>? stdoutTask = null;
        Task<ReadObservation>? stderrTask = null;
        ReadObservation? stdout = null;
        ReadObservation? stderr = null;
        try
        {
            string temporaryDirectory = Path.Combine(Path.GetTempPath(), "dsp004-stop-test-" + Guid.NewGuid().ToString("N"));
            Directory.CreateDirectory(temporaryDirectory);
            string target = caseNumber == 7
                ? Path.Combine(temporaryDirectory, "NO_EXECUTABLE_FOR_SYNTHETIC_START_FAILURE.exe")
                : Executable;
            var start = new ProcessStartInfo(target)
            {
                UseShellExecute = false, CreateNoWindow = true,
                RedirectStandardOutput = true, RedirectStandardError = true,
                StandardOutputEncoding = new UTF8Encoding(false, true),
                StandardErrorEncoding = new UTF8Encoding(false, true),
                WorkingDirectory = temporaryDirectory
            };
            start.ArgumentList.Add("-NoLogo");
            start.ArgumentList.Add("-NoProfile");
            start.ArgumentList.Add("-NonInteractive");
            start.ArgumentList.Add("-EncodedCommand");
            start.ArgumentList.Add(Convert.ToBase64String(Encoding.Unicode.GetBytes(FixedScript(caseNumber))));
            start.Environment.Clear();
            string systemRoot = Environment.GetFolderPath(Environment.SpecialFolder.Windows);
            start.Environment["SystemRoot"] = systemRoot;
            start.Environment["WINDIR"] = systemRoot;
            start.Environment["TEMP"] = temporaryDirectory;
            start.Environment["TMP"] = temporaryDirectory;
            start.Environment["USERPROFILE"] = temporaryDirectory;
            start.Environment["POWERSHELL_TELEMETRY_OPTOUT"] = "1";
            start.Environment["DOTNET_CLI_TELEMETRY_OPTOUT"] = "1";
            process = new Process { StartInfo = start };
            CheckShortDeadline(timer);
            observation.StartAttempted = true;
            observation.FirstReason = "START_FAILURE";
            observation.ChildStarted = process.Start();
            if (!observation.ChildStarted) throw new InvalidOperationException("START_NOT_CONFIRMED");
            observation.FirstReason = "UNEXPECTED_IO_OR_RUNTIME_FAILURE";
            CheckShortDeadline(timer);
            stdoutTask = ReadBounded(process.StandardOutput.BaseStream, 65536);
            stderrTask = ReadBounded(process.StandardError.BaseStream, 0);
            while (true)
            {
                observation.FirstReason = "SYNTHETIC_TEST_DEADLINE";
                CheckShortDeadline(timer);
                observation.FirstReason = "UNEXPECTED_IO_OR_RUNTIME_FAILURE";
                if (stdoutTask.IsFaulted) throw stdoutTask.Exception!;
                if (stderrTask.IsFaulted) throw stderrTask.Exception!;
                if (stdoutTask.IsCanceled || stderrTask.IsCanceled)
                    throw new OperationCanceledException("READ_TASK_CANCELED");
                if (stdoutTask.IsCompletedSuccessfully && stdoutTask.Result.Overflow)
                {
                    observation.FirstReason = "STDOUT_OVER_BUDGET";
                    throw new InvalidOperationException("SYNTHETIC_STDOUT_DETECTION");
                }
                if (stderrTask.IsCompletedSuccessfully && stderrTask.Result.Overflow)
                {
                    observation.FirstReason = "UNEXPECTED_STDERR";
                    throw new InvalidOperationException("SYNTHETIC_STDERR_DETECTION");
                }
                observation.ChildExitObserved = process.HasExited;
                bool complete = observation.ChildExitObserved && stdoutTask.IsCompletedSuccessfully && stderrTask.IsCompletedSuccessfully;
                string decision = Dsp004D007LocalSyntheticHandoffSupervisorRev2.ClassifyProgress(
                    timer.ElapsedMilliseconds + ClassifierOffsetMilliseconds, complete);
                if (decision == "DEADLINE_REFUSED")
                {
                    observation.FirstReason = "SYNTHETIC_TEST_DEADLINE";
                    throw new TimeoutException("SYNTHETIC_SHORT_DEADLINE");
                }
                if (decision == "COMPLETE_IN_TIME")
                {
                    stdout = stdoutTask.Result;
                    stderr = stderrTask.Result;
                    observation.ExitCode = process.ExitCode;
                    if (!stdout.Eof || !stderr.Eof || stdout.Count == 0)
                        throw new InvalidOperationException("SYNTHETIC_COMPLETION_SHAPE_REJECTED");
                    if (observation.ExitCode != 0)
                    {
                        observation.FirstReason = "NONZERO_CHILD_EXIT";
                        throw new InvalidOperationException("SYNTHETIC_NONZERO_EXIT");
                    }
                    string? body;
                    if (!Dsp004D007LocalSyntheticHandoffSupervisorRev2.TryReadAcknowledgedBody(stdout.Body, out body))
                    {
                        observation.FirstReason = "ACK_ABSENT";
                        throw new InvalidOperationException("SYNTHETIC_ACK_ABSENT");
                    }
                    if (!string.Equals(body, "{\"synthetic\":\"CONTROL_ONLY\"}\n", StringComparison.Ordinal))
                        throw new InvalidOperationException("SYNTHETIC_CONTROL_BODY_REJECTED");
                    observation.FirstReason = "SYNTHETIC_TEST_DEADLINE";
                    CheckShortDeadline(timer);
                    observation.FirstReason = "SYNTHETIC_CONTROL_CAPTURED_ONLY";
                    observation.SyntheticFrameQualified = true;
                    observation.ControlBodyRecorded = true;
                    observation.CompletionDecisionElapsedMilliseconds = timer.ElapsedMilliseconds;
                    break;
                }
                Thread.Sleep(10);
            }
        }
        catch (Exception error)
        {
            observation.RetainPrimary(error);
            observation.StopLatched = true;
            observation.ControlBodyRecorded = false;
            observation.SyntheticFrameQualified = false;
            observation.CompletionDecisionElapsedMilliseconds = -1;
            if (process != null && observation.ChildStarted)
            {
                try
                {
                    if (!process.HasExited)
                    {
                        observation.KillRequested = true;
                        process.Kill(true);
                        observation.KillCallReturned = true;
                    }
                }
                catch (Exception stopError) { observation.RetainSecondary(stopError); }
                try { observation.ChildExitObserved = process.WaitForExit(2000); }
                catch (Exception waitError) { observation.RetainSecondary(waitError); }
                if (observation.ChildExitObserved)
                {
                    try { observation.ExitCode = process.ExitCode; }
                    catch (Exception exitError) { observation.RetainSecondary(exitError); }
                }
                if (stdoutTask != null && stderrTask != null)
                {
                    try { Task.WaitAll(new Task[] { stdoutTask, stderrTask }, 2000); }
                    catch (Exception streamError) { observation.RetainSecondary(streamError); }
                }
            }
        }
        finally
        {
            if (stdoutTask?.IsCompletedSuccessfully == true) stdout = stdoutTask.Result;
            if (stderrTask?.IsCompletedSuccessfully == true) stderr = stderrTask.Result;
            observation.StdoutTaskEnded = stdoutTask?.IsCompleted == true;
            observation.StderrTaskEnded = stderrTask?.IsCompleted == true;
            observation.StdoutEofObserved = stdout?.Eof == true;
            observation.StderrEofObserved = stderr?.Eof == true;
            observation.StdoutReadCount = stdout?.Count ?? -1;
            observation.StderrReadCount = stderr?.Count ?? -1;
            observation.StopResultNotRestored = observation.StopLatched && !observation.ControlBodyRecorded && !observation.SyntheticFrameQualified;
            if (process != null)
            {
                try { process.Dispose(); observation.LocalProcessDisposeReturned = true; }
                catch (Exception disposeError) { observation.RetainSecondary(disposeError); }
            }
            observation.ElapsedMilliseconds = timer.ElapsedMilliseconds;
        }
        return observation;
    }

    private static async Task<ReadObservation> ReadBounded(Stream stream, int budget)
    {
        using var body = new MemoryStream();
        int count = 0;
        while (true)
        {
            byte[] buffer = new byte[Math.Min(4096, budget - count + 1)];
            int returned = await stream.ReadAsync(buffer.AsMemory()).ConfigureAwait(false);
            if (returned == 0) return new ReadObservation(body.ToArray(), count, false, true);
            count += returned;
            if (count > budget) return new ReadObservation(Array.Empty<byte>(), count, true, false);
            body.Write(buffer, 0, returned);
        }
    }

    private sealed class ReadObservation
    {
        internal byte[] Body { get; }
        internal int Count { get; }
        internal bool Overflow { get; }
        internal bool Eof { get; }
        internal ReadObservation(byte[] body, int count, bool overflow, bool eof)
        { Body = body; Count = count; Overflow = overflow; Eof = eof; }
    }

    public sealed class CaseObservation
    {
        private Exception? primary;
        private readonly List<Exception> secondary = new List<Exception>();
        internal CaseObservation(string id, string reason) { CaseId = id; FirstReason = reason; }
        internal void RetainPrimary(Exception error) { primary = error; }
        internal void RetainSecondary(Exception error) { secondary.Add(error); }
        public string CaseId { get; }
        public string FirstReason { get; internal set; }
        public string? ExecutableFileSHA256 { get; internal set; }
        public bool StartAttempted { get; internal set; }
        public bool ChildStarted { get; internal set; }
        public bool ChildExitObserved { get; internal set; }
        public int ExitCode { get; internal set; } = -1;
        public bool StopLatched { get; internal set; }
        public bool KillRequested { get; internal set; }
        public bool KillCallReturned { get; internal set; }
        public bool StdoutTaskEnded { get; internal set; }
        public bool StderrTaskEnded { get; internal set; }
        public bool StdoutEofObserved { get; internal set; }
        public bool StderrEofObserved { get; internal set; }
        public int StdoutReadCount { get; internal set; } = -1;
        public int StderrReadCount { get; internal set; } = -1;
        public bool SyntheticFrameQualified { get; internal set; }
        public bool ControlBodyRecorded { get; internal set; }
        public bool StopResultNotRestored { get; internal set; }
        public bool LocalProcessDisposeReturned { get; internal set; }
        public long CompletionDecisionElapsedMilliseconds { get; internal set; } = -1;
        public long ElapsedMilliseconds { get; internal set; } = -1;
        public string? PrimaryFailureType => primary?.GetType().FullName;
        public int SecondaryFailureCount => secondary.Count;
        public string ObservationScope => "NEW INDEPENDENT SYNTHETIC TEST ADAPTER; NOT REV2 PUBLIC RUNTIME PATH";
        public string AckQualification => "SYNTHETIC OUTPUT FRAME ONLY; NO INPUT SHA VERIFICATION OR AUTHORITY";
        public string TimeQualification => CaseId == "BATCH-REPEAT"
            ? "NOT TIMED; REPEATED TEST BATCH REFUSED"
            : "SHORT TEST CASE BUDGET 5000MS; OFFSET MAPPED TO SHARED PURE CLASSIFIER; NOT REV2 120SECOND EXECUTION";
        public string SettlementQualification => "SINGLE CHILD/TASK OBSERVATIONS ONLY; COMPLETE RESOURCES AND DESCENDANTS NOT ESTABLISHED";
        public string Authority => "NOT ESTABLISHED";
        public string SourceAdmission => "NOT ESTABLISHED";
    }
}
}
