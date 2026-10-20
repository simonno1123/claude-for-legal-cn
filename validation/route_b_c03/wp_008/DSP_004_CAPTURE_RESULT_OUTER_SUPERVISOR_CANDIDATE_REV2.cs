#nullable enable
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Globalization;
using System.IO;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

// DSP-004 outer-supervisor SOURCE CANDIDATE REV2: formation/static review only.
// Predecessor source, unchanged:
// 36C90727CA87F6F6235546B8A380784CED13E40E94F2CA7799C01EE0FC094B35
// Conversation-level fixed-startup/single-loader design REV2 has no file SHA.
// The only public entry REFUSES. Every private I/O/startup reference is CLOSED.
// No loading, compilation, tests or new environment observation was performed.
//
// Adds fixed successor source pins, bootstrap-only startup descriptor, bounded
// private command/report stream framing and a serial handshake reference.
// Code input is closed separately; stdout/stderr zero-body monitors run
// concurrently, never as ACK/control and never awaited for EOF before dispatch.
// Child metadata is always UNVERIFIED_REPORT, not native assertion proof.
//
// No Process.Start path, OS handle/peer establishment, trusted resolver/full
// dependency environment, process containment or independent hard-stop driver
// is supplied. Stream arguments below are private future-owner obligations,
// not a public callback/stream injection API. Gates cannot be bypassed by an
// approval string; a later separately reviewed version/driver is required.
// Actual synchronous reads/writes/closes/kill can block. Proposed 60/2/5/5/70
// timing is NOT a verified bound. In-host task receipts are not durable outside
// ownership. On uncertainty, retain handles/tasks/original errors and HOLD.
//
// 158 recipes are NOT_RUN, not the separate 189-item plan. D-007/positive SHA
// coverage is not inferred. All LIMITED, initial failures and reviews remain.
// DSP-004 OPEN/HOLD; B-01/B-02 OPEN. No source admission, actual capture,
// integration, finding, aggregate verdict, acceptance or runtime grant.
public sealed class Dsp004CaptureResultOuterSupervisorCandidateRev2
{
    private const string CarrierFile = "validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV3.py";
    private const string CarrierSha = "329EC4A1C12351667F9A52946E4E11F6B01E287796FBDE42211FE5861CC14845";
    private const int CarrierLength = 57623;
    private const string ContractFile = "validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_CONTRACT_CANDIDATE_REV1.py";
    private const string ContractSha = "E9472328847617EBF629FB01A0A163C0805226690600E5E13EBE1209E2F6705C";
    private const int ContractLength = 18301;
    private const string DependencyFile = "scripts/phase2_runtime/route_b_c03/contracts.py";
    private const string DependencySha = "7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4";
    private const int DependencyLength = 16475;
    private const string BootstrapFile = "validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_FIXED_BOOTSTRAP_CANDIDATE_REV1.py";
    private const string BootstrapSha = "4281385A8694C870A96E7EC7B98A9CB027A470C1AC2EE5F31BABCF9D56F46007";
    private const int BootstrapLength = 10678;
    // Prior static record only; NOT reverified environment/read authority here.
    private const string InterpreterFile = "C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe";
    private const string RecordedInterpreterSha = "B07B03B9BA866A341A3C13EE69710FBC8D43D4CE2523DEE13F6DF5C25378D15B";
    private const int FixedCodeFrameLength = 26 + 3 * 73 + DependencyLength + ContractLength + CarrierLength;
    private const int ControlFrameLimit = 4096;
    private const int CodeInputLimit = 262144;
    private const string ReportVersion = "DSP004-CAPTURE-V1";
    private const string SourceVersion = "DSP004-CAPTURE-SOURCES-V1";
    private static int reserved;
    private static readonly List<OwnershipReceipt> heldOwnership = new List<OwnershipReceipt>();
    private static readonly object heldOwnershipSync = new object();
    private Dsp004CaptureResultOuterSupervisorCandidateRev2() { }

    public static RefusalObservation RunFixedLocalBatch()
    {
        // A technical one-use reservation, not a governing authorization token.
        bool repeated = Interlocked.Exchange(ref reserved, 1) != 0;
        return new RefusalObservation(repeated);
    }

    private static void RequireExecutionBinding()
    {
        // Deliberately no accepting branch. No resources/clock/source are opened.
        throw new InvalidOperationException("EXECUTION_BINDINGS_NOT_ESTABLISHED");
    }

    public sealed class RefusalObservation
    {
        internal RefusalObservation(bool repeated) { RepeatedEntry = repeated; }
        public bool RepeatedEntry { get; }
        public string Outcome => RepeatedEntry ? "REPEATED_ENTRY_REFUSED" : "START_REFUSED_UNBOUND";
        public string Qualification => "SOURCE_ENTRY_REFUSAL_ONLY_NOT_AN_ENVIRONMENT_OR_GOVERNANCE_PROOF";
        public string Coverage => "NOT_RUN_BY_THIS_ENTRY";
        public string Missing => "INTERPRETER_RESOLVER_ROOTS_AUTHORITY_BOOTSTRAP_PRIVATE_IPC_SCOPE_STOP_CLEANUP";
    }

    // Proposed fixed native byte snapshots only; no path reading or resolution.
    // The private clone is hashed and later framed without reopening a file.
    private sealed class SourceSnapshot
    {
        internal readonly string Role, File, ExpectedSha;
        internal readonly byte[] Bytes;
        internal SourceSnapshot(string role, string file, string sha, int length, byte[] bytes)
        {
            if (bytes == null || bytes.Length != length || length > CodeInputLimit)
                throw FixedFailure("SOURCE_LENGTH_MISMATCH");
            Role = role; File = file; ExpectedSha = sha;
            Bytes = (byte[])bytes.Clone();
            using (SHA256 digest = SHA256.Create())
            {
                string actual = BitConverter.ToString(digest.ComputeHash(Bytes)).Replace("-", "");
                if (!String.Equals(actual, sha, StringComparison.Ordinal))
                    throw FixedFailure("SOURCE_SHA_MISMATCH");
            }
        }
    }

    private static SourceSnapshot[] CreateSourceSnapshotsReference(byte[] dependency, byte[] contract, byte[] carrier)
    {
        return new[] {
            new SourceSnapshot("B", DependencyFile, DependencySha, DependencyLength, dependency),
            new SourceSnapshot("A", ContractFile, ContractSha, ContractLength, contract),
            new SourceSnapshot("N", CarrierFile, CarrierSha, CarrierLength, carrier)
        };
    }

    private static byte[] BuildCodeInputReference(SourceSnapshot[] sources)
    {
        // Internal fixed descriptors, never an arbitrary source/command manifest.
        if (sources == null || sources.Length != 3) throw FixedFailure("SOURCE_ORDER_MISMATCH");
        string[] roles = { "B", "A", "N" };
        string[] files = { DependencyFile, ContractFile, CarrierFile };
        string[] shas = { DependencySha, ContractSha, CarrierSha };
        int[] lengths = { DependencyLength, ContractLength, CarrierLength };
        using (var body = new MemoryStream())
        {
            WriteAscii(body, SourceVersion + "\n");
            for (int index = 0; index < sources.Length; index++)
            {
                SourceSnapshot item = sources[index];
                if (item == null || item.Role != roles[index] || item.File != files[index] ||
                    item.ExpectedSha != shas[index] || item.Bytes.Length != lengths[index])
                    throw FixedFailure("SOURCE_ORDER_MISMATCH");
                // Recheck the private snapshot, not a file reread or trust proof.
                using (SHA256 digest = SHA256.Create())
                    if (BitConverter.ToString(digest.ComputeHash(item.Bytes)).Replace("-", "") != shas[index])
                        throw FixedFailure("SOURCE_SNAPSHOT_CHANGED");
                WriteAscii(body, item.Role + "|" + item.Bytes.Length.ToString(CultureInfo.InvariantCulture) + "|" + item.ExpectedSha + "\n");
                if (body.Length + item.Bytes.Length > CodeInputLimit) throw FixedFailure("CODE_INPUT_OVERFLOW");
                body.Write(item.Bytes, 0, item.Bytes.Length);
            }
            if (body.Length != FixedCodeFrameLength) throw FixedFailure("FIXED_FRAME_LENGTH_MISMATCH");
            return body.ToArray();
        }
    }

    private static void WriteAscii(MemoryStream target, string text)
    {
        foreach (char character in text)
            if (character > 127) throw FixedFailure("NON_ASCII_FIXED_HEADER");
        byte[] bytes = Encoding.ASCII.GetBytes(text);
        if (target.Length + bytes.Length > CodeInputLimit) throw FixedFailure("CODE_INPUT_OVERFLOW");
        target.Write(bytes, 0, bytes.Length);
    }

    // Independent fixed literal mirror, never inferred from child reports.
    // This is only a candidate directory. It admits no case or source.
    private static readonly string[] CaseIds = {
        "C01-variant_id-NONE",
        "C01-variant_id-BOOL",
        "C01-variant_id-SUBCLASS",
        "C01-variant_id-EMPTY",
        "C01-variant_id-SPACE",
        "C01-attempt_id-NONE",
        "C01-attempt_id-BOOL",
        "C01-attempt_id-SUBCLASS",
        "C01-attempt_id-EMPTY",
        "C01-attempt_id-SPACE",
        "C01-input_snapshot_sha256-NONE",
        "C01-input_snapshot_sha256-BOOL",
        "C01-input_snapshot_sha256-SUBCLASS",
        "C01-input_snapshot_sha256-EMPTY",
        "C01-input_snapshot_sha256-SPACE",
        "C01-audit_correlation_id-NONE",
        "C01-audit_correlation_id-BOOL",
        "C01-audit_correlation_id-SUBCLASS",
        "C01-audit_correlation_id-EMPTY",
        "C01-audit_correlation_id-SPACE",
        "C01-HEX64-LOWER",
        "C01-HEX64-UPPER",
        "C01-SHORT",
        "C01-LONG",
        "C01-NONHEX",
        "C02-PROJECT-NONE",
        "C02-PROJECT-INT",
        "C02-PROJECT-TEXT",
        "C02-SESSION-NONE",
        "C02-SESSION-INT",
        "C02-SESSION-TEXT",
        "C02-PROVIDER-NONE",
        "C02-PROVIDER-INT",
        "C02-PROVIDER-TEXT",
        "C02-BOUNDARY-TEXT",
        "C02-TYPE-NAME",
        "C02-WRONG-TYPE",
        "C02-SOURCE-NONE",
        "C02-SOURCE-EMPTY",
        "C02-SOURCE-SPACE",
        "C03-SUBSET-0",
        "C03-SUBSET-1",
        "C03-SUBSET-2",
        "C03-SUBSET-3",
        "C03-SUBSET-4",
        "C03-SUBSET-5",
        "C03-SUBSET-6",
        "C03-SUBSET-7",
        "C03-DUPLICATE",
        "C03-REVERSED",
        "C03-FOUR",
        "C03-LIST",
        "C03-TUPLE-SUBCLASS",
        "C04-STATE-INVOCATION_RECEIVED",
        "C04-STATE-GATE_CHECKING",
        "C04-STATE-BLOCKED",
        "C04-STATE-REJECTED",
        "C04-STATE-ELIGIBLE_FOR_MAPPING",
        "C04-STATE-MAPPING",
        "C04-STATE-MAPPING_CANDIDATE",
        "C04-STATE-QUARANTINED",
        "C04-STATE-HUMAN_REVIEW_PENDING",
        "C04-STATE-TEXT",
        "C04-REASON-BOOL",
        "C04-REASON-EMPTY",
        "C04-CORRELATION-NONE",
        "C04-CORRELATION-OTHER",
        "C04-WRITES-LIST",
        "C04-WRITES-SUBCLASS",
        "C04-WRITES-NONEMPTY",
        "C05-STRUCTURAL-BLOCKED",
        "C05-STRUCTURAL-REJECTED",
        "C05-STRUCTURAL-ELIGIBLE_FOR_MAPPING",
        "C05-CAPTURE-FALSE",
        "C05-CLEANUP-FALSE",
        "C05-HANDOFF-FALSE",
        "C05-CAPTURE-INT",
        "C05-CLEANUP-INT",
        "C05-HANDOFF-INT",
        "C05-BASIS-EMPTY",
        "C05-BASIS-NONE",
        "C05-MISSING-0",
        "C05-MISSING-1",
        "C05-MISSING-2",
        "C05-NO-PRIOR",
        "C06-VALUE",
        "C06-INTERRUPT",
        "C06-EXIT",
        "C06-NONEXCEPTION-CLASS",
        "C06-NONEXCEPTION-TEXT",
        "C06-NONEXCEPTION-NONE",
        "C07-0-PRIMARY",
        "C07-0-CLEANUP",
        "C07-0-BOTH",
        "C07-0-SHARED",
        "C07-1-PRIMARY",
        "C07-1-CLEANUP",
        "C07-1-BOTH",
        "C07-1-SHARED",
        "C07-2-PRIMARY",
        "C07-2-CLEANUP",
        "C07-2-BOTH",
        "C07-2-SHARED",
        "C07-3-PRIMARY",
        "C07-3-CLEANUP",
        "C07-3-BOTH",
        "C07-3-SHARED",
        "C07-NO-ERRORS",
        "C08-INTERRUPTED_WITHOUT_EXCEPTION-0",
        "C08-INTERRUPTED_WITHOUT_EXCEPTION-1",
        "C08-INTERRUPTED_WITHOUT_EXCEPTION-2",
        "C08-INTERRUPTED_WITHOUT_EXCEPTION-3",
        "C08-NO_RETURN-0",
        "C08-NO_RETURN-1",
        "C08-NO_RETURN-2",
        "C08-NO_RETURN-3",
        "C08-MISSING_OBSERVATION-0",
        "C08-MISSING_OBSERVATION-1",
        "C08-MISSING_OBSERVATION-2",
        "C08-MISSING_OBSERVATION-3",
        "C08-CARRIER_IDENTITY_FAILURE-0",
        "C08-CARRIER_IDENTITY_FAILURE-1",
        "C08-CARRIER_IDENTITY_FAILURE-2",
        "C08-CARRIER_IDENTITY_FAILURE-3",
        "C08-HANDOFF_INCOMPLETE-0",
        "C08-HANDOFF_INCOMPLETE-1",
        "C08-HANDOFF_INCOMPLETE-2",
        "C08-HANDOFF_INCOMPLETE-3",
        "C09-DICT",
        "C09-FOREIGN",
        "C09-MATERIALS-ONLY",
        "C09-RESULT-SUBCLASS",
        "C09-REVALIDATE-COMPLETE",
        "C09-REVALIDATE-FAILURE",
        "C09-REVALIDATE-INCOMPLETE",
        "C10-CONSTRUCTOR-MISSING-CaptureInvocationBinding",
        "C10-CONSTRUCTOR-MISSING-CapturedReference",
        "C10-CONSTRUCTOR-MISSING-CaptureMaterials",
        "C10-CONSTRUCTOR-MISSING-CompleteCaptureReturn",
        "C10-CONSTRUCTOR-MISSING-FailureOccurrence",
        "C10-CONSTRUCTOR-MISSING-CaptureFailure",
        "C10-CONSTRUCTOR-MISSING-IncompleteCapture",
        "C10-REVALIDATE-MISSING-materials",
        "C10-REVALIDATE-MISSING-stage",
        "C10-REVALIDATE-MISSING-cause",
        "C11-BOUNDARY-CONSTRUCT-PSEUDO",
        "C11-BOUNDARY-CONSTRUCT-CONTROL",
        "C11-BOUNDARY-REVALIDATE-PSEUDO",
        "C11-BOUNDARY-REVALIDATE-CONTROL",
        "C11-CAUSE-CONSTRUCT-PSEUDO",
        "C11-CAUSE-CONSTRUCT-CONTROL",
        "C11-CAUSE-REVALIDATE-PSEUDO",
        "C11-CAUSE-REVALIDATE-CONTROL",
        "C11-PRIOR-CONSTRUCT-PSEUDO",
        "C11-PRIOR-CONSTRUCT-CONTROL",
        "C11-PRIOR-REVALIDATE-PSEUDO",
        "C11-PRIOR-REVALIDATE-CONTROL",
        "C12-SHALLOW-FREEZE-LIMITATION",
    };

    private sealed class MinimalReport
    {
        internal readonly int Ordinal;
        internal readonly string Id, Phase, Determination;
        internal string Qualification => "UNVERIFIED_REPORT";
        internal MinimalReport(int ordinal, string id, string phase, string determination)
        { Ordinal = ordinal; Id = id; Phase = phase; Determination = determination; }
    }

    private sealed class ReportOrderReference
    {
        private readonly object reportSync = new object();
        private int nextOrdinal = 1;
        private bool stopped;
        internal bool DirectoryReported
        { get { lock (reportSync) { return nextOrdinal == CaseIds.Length + 1 && !stopped; } } }

        internal MinimalReport ConsumeCompleteFrame(byte[] frame)
        {
            lock (reportSync) { return ConsumeOwnedFrame(frame); }
        }

        private MinimalReport ConsumeOwnedFrame(byte[] frame)
        {
            // This accepts ONE already-delimited private frame, not a Stream.
            // The new stream reader delimits frames; physical peer binding stays UNBOUND.
            try
            {
                if (stopped || nextOrdinal > CaseIds.Length) throw FixedFailure("NO_MORE_REPORTS");
                if (frame == null || frame.Length < 2 || frame.Length > ControlFrameLimit)
                    throw FixedFailure("REPORT_FRAME_BOUNDARY");
                // Validate a private bounded copy, not a later-reused read buffer.
                // This does not attest the origin or atomic receipt of the bytes.
                frame = (byte[])frame.Clone();
                if (frame[frame.Length - 1] != 10) throw FixedFailure("REPORT_FRAME_BOUNDARY");
                for (int index = 0; index < frame.Length - 1; index++)
                    if (frame[index] < 33 || frame[index] > 126) throw FixedFailure("REPORT_NONCANONICAL_ASCII");
                string text = Encoding.ASCII.GetString(frame, 0, frame.Length - 1);
                string[] fields = text.Split('|');
                if (fields.Length != 6 || fields[0] != ReportVersion || fields[5] != "UNVERIFIED_REPORT")
                    throw FixedFailure("REPORT_FIELDS_MISMATCH");
                int ordinal;
                if (!Int32.TryParse(fields[1], NumberStyles.None, CultureInfo.InvariantCulture, out ordinal) ||
                    ordinal != nextOrdinal || fields[1] != ordinal.ToString(CultureInfo.InvariantCulture) ||
                    fields[2] != CaseIds[ordinal - 1]) throw FixedFailure("REPORT_ORDER_MISMATCH");
                bool setup = fields[3] == "SETUP";
                bool active = fields[3] == "SUT" || fields[3] == "ORACLE";
                bool activeValue = fields[4] == "PASS" || fields[4] == "FAIL";
                if (!(setup && fields[4] == "NOT_EVALUABLE") && !(active && activeValue))
                    throw FixedFailure("REPORT_PHASE_DETERMINATION_MISMATCH");
                var report = new MinimalReport(ordinal, fields[2], fields[3], fields[4]);
                nextOrdinal++;
                if (report.Determination != "PASS") stopped = true;
                // Structural acceptance is not child authentication or SUT truth.
                return report;
            }
            catch { stopped = true; throw; }
        }
    }

    private sealed class ProposedDeadlineReference
    {
        internal readonly long T0, Work, Hard;
        internal ProposedDeadlineReference(long externalT0Milliseconds)
        {
            // External T0 must precede this future batch's FIRST read/hash/IPC/
            // process attempt. This class reads no clock and proves no timer.
            if (externalT0Milliseconds < 0) throw FixedFailure("INVALID_EXTERNAL_T0");
            T0 = externalT0Milliseconds;
            Work = Advance(T0, 60000);
            Hard = Advance(T0, 70000);
        }
        private void CheckSample(long sample)
        { if (sample < T0) throw FixedFailure("MONOTONIC_SAMPLE_PRECEDES_T0"); }
        internal void RequireSample(long sample) { CheckSample(sample); }
        internal long CaseDue(long dispatchSample)
        { CheckSample(dispatchSample); return Math.Min(Math.Min(Advance(dispatchSample, 2000), Work), Hard); }
        internal long TerminationDue(long sample)
        { CheckSample(sample); return Math.Min(Advance(sample, 5000), Hard); }
        internal long CleanupDue(long sample)
        { CheckSample(sample); return Math.Min(Advance(sample, 5000), Hard); }
        internal string WorkDecision(long sample, bool completionReady)
        {
            CheckSample(sample);
            if (sample >= Work || sample >= Hard) return "DEADLINE_EXPIRED";
            return completionReady ? "REPORTED_COMPLETION_IN_WINDOW" : "WAIT";
        }
        internal static int RemainingWait(long sample, long due)
        {
            if (sample < 0 || due < 0) throw FixedFailure("INVALID_WAIT_SAMPLE");
            if (sample >= due) return 0;
            return (int)Math.Min(due - sample, 5000);
        }
        private static long Advance(long sample, long amount)
        {
            try { return checked(sample + amount); }
            catch (OverflowException original)
            { throw new InvalidOperationException("UNREPRESENTABLE_DEADLINE", original); }
        }
    }

    // Strong in-host references, not durable ownership or an OS process scope.
    // Every original task is distinct from a wait wrapper or a cancellation token.
    private sealed class OwnershipReceipt
    {
        private readonly object errorAndTaskSync = new object();
        private bool stdoutReserved, stderrReserved, writeReserved;
        internal Process? Process;
        internal Task? InputWrite, StdoutRead, StderrRead, ControlRead, WaitWrapper;
        internal Task? ControlWrite, ExitWait;
        internal int DispatchAttemptedOrdinal;
        internal bool ProtocolAttempted, StopCommandAttempted;
        internal byte[]? InputSnapshot;
        internal bool StartAttempted, IoAttempted, KillRequested, KillCallReturned;
        private bool stopLatched;
        internal bool StopLatched { get { lock (errorAndTaskSync) { return stopLatched; } } }
        internal void LatchStop() { lock (errorAndTaskSync) { stopLatched = true; } }
        private Stream[]? boundStreams;
        private readonly List<byte[]> heldCommandFrames = new List<byte[]>();
        private int nextWriteOrdinal = 1;
        internal bool InputCloseReturned, OutputCloseReturned, ErrorCloseReturned, DisposeReturned;
        internal bool? ChildExitObserved, StdoutEof, StderrEof;
        internal Exception? Primary;
        internal string? PrimaryPhase;
        internal readonly List<KeyValuePair<string, Exception>> Secondary = new List<KeyValuePair<string, Exception>>();
        private readonly List<Task> allReturnedIoTasks = new List<Task>();
        internal string Disposition = "PRESTART_UNBOUND";

        internal void KeepPrimary(string phase, Exception original)
        {
            if (original == null) throw FixedFailure("MISSING_NATIVE_ERROR");
            lock (errorAndTaskSync)
            {
                // First REGISTERED error, not a claim about physical chronology.
                if (Primary == null) { Primary = original; PrimaryPhase = phase; }
                else Secondary.Add(new KeyValuePair<string, Exception>(phase, original));
                LatchStop();
            }
        }
        internal void KeepSecondary(string phase, Exception original)
        {
            if (original == null) throw FixedFailure("MISSING_NATIVE_ERROR");
            lock (errorAndTaskSync)
            {
                Secondary.Add(new KeyValuePair<string, Exception>(phase, original));
                LatchStop();
            }
        }
        internal void BeforeProcessStartAttempt(Process process)
        {
            lock (errorAndTaskSync)
            {
                if (Process != null || StartAttempted || StopLatched) throw FixedFailure("START_STATE_MISMATCH");
                Process = process ?? throw FixedFailure("MISSING_PROCESS_HANDLE");
                StartAttempted = true; // BEFORE a future Start call, including unknown return.
                Disposition = "INCOMPLETE_UNCONFIRMED";
            }
        }
        internal void ReserveRead(StandardStreamRole role)
        {
            lock (errorAndTaskSync)
            {
                if (role != StandardStreamRole.Stdout && role != StandardStreamRole.Stderr)
                    throw FixedFailure("UNBOUND_STANDARD_STREAM_ROLE");
                if (StopLatched || (role == StandardStreamRole.Stdout ? stdoutReserved : stderrReserved))
                    throw FixedFailure("ORIGINAL_READ_ALREADY_RESERVED_OR_STOPPED");
                if (role == StandardStreamRole.Stdout) stdoutReserved = true;
                else stderrReserved = true;
                IoAttempted = true; Disposition = "INCOMPLETE_UNCONFIRMED";
            }
        }
        internal void AttachRead(StandardStreamRole role, Task original)
        {
            if (original == null) throw FixedFailure("MISSING_ORIGINAL_READ_TASK");
            lock (errorAndTaskSync)
            {
                allReturnedIoTasks.Add(original);
                if (role == StandardStreamRole.Stdout && stdoutReserved && StdoutRead == null) StdoutRead = original;
                else if (role == StandardStreamRole.Stderr && stderrReserved && StderrRead == null) StderrRead = original;
                else throw FixedFailure("ORIGINAL_READ_TASK_SLOT_MISMATCH");
            }
        }
        internal void ReserveWrite(byte[] frame)
        {
            lock (errorAndTaskSync)
            {
                if (StopLatched || writeReserved) throw FixedFailure("ORIGINAL_WRITE_ALREADY_RESERVED_OR_STOPPED");
                writeReserved = true; InputSnapshot = frame;
                IoAttempted = true; Disposition = "INCOMPLETE_UNCONFIRMED";
            }
        }
        internal void AttachWrite(Task original)
        {
            if (original == null) throw FixedFailure("MISSING_ORIGINAL_WRITE_TASK");
            lock (errorAndTaskSync)
            {
                allReturnedIoTasks.Add(original);
                if (!writeReserved || InputWrite != null) throw FixedFailure("ORIGINAL_WRITE_TASK_SLOT_MISMATCH");
                InputWrite = original;
            }
        }
        internal void BindProtocolStreams(Stream[] streams)
        {
            lock (errorAndTaskSync)
            {
                if (boundStreams != null || streams == null || streams.Length != 5)
                    throw FixedFailure("ENDPOINT_BINDING_REPEATED_OR_INCOMPLETE");
                // Hold all endpoints before validation/hash/I/O; failure does not
                // discard private command/report handles or transfer their owner.
                boundStreams = (Stream[])streams.Clone();
                for (int left = 0; left < boundStreams.Length; left++)
                {
                    if (boundStreams[left] == null) throw FixedFailure("MISSING_ENDPOINT");
                    for (int right = left + 1; right < boundStreams.Length; right++)
                        if (ReferenceEquals(boundStreams[left], boundStreams[right]))
                            throw FixedFailure("ALIASED_ENDPOINT");
                }
            }
        }
        internal Task StartNextWriteReference(Stream command, byte[] frame, int ordinal,
            Stopwatch clock, ProposedDeadlineReference deadlines, long due)
        {
            RequireExecutionBinding();
            lock (errorAndTaskSync)
            {
                if (stopLatched || ordinal != nextWriteOrdinal)
                    throw FixedFailure("NEXT_WRITE_AFTER_STOP_OR_OUT_OF_ORDER");
                RequireIoWindow(this, clock, deadlines, due, false);
                byte[] owned = (byte[])frame.Clone();
                heldCommandFrames.Add(owned); // Before invoking native I/O.
                // Lock serializes stop registration and the WriteAsync START.
                // A synchronous block remains an outside-owner LIMITED; no
                // lock is claimed to make an OS call bounded or interruptible.
                RequireIoWindow(this, clock, deadlines, due, false);
                DispatchAttemptedOrdinal = ordinal;
                nextWriteOrdinal++;
                IoAttempted = true; Disposition = "INCOMPLETE_UNCONFIRMED";
                try
                {
                    Task original = command.WriteAsync(owned, 0, owned.Length);
                    AttachOperation("CONTROL_WRITE", original);
                    return original;
                }
                catch (Exception original) { KeepPrimary("NEXT_WRITE_START", original); throw; }
            }
        }
        internal Task StartStopWriteReference(Stream command, Stopwatch clock,
            ProposedDeadlineReference deadlines, long due)
        {
            RequireExecutionBinding();
            lock (errorAndTaskSync)
            {
                if (StopCommandAttempted || (ControlWrite != null &&
                    (!ControlWrite.IsCompleted || ControlWrite.IsFaulted || ControlWrite.IsCanceled)))
                    throw FixedFailure("STOP_ALREADY_ATTEMPTED_OR_WRITE_UNSETTLED");
                RequireIoWindow(this, clock, deadlines, due, true);
                byte[] owned = (byte[])StopFrame.Clone();
                heldCommandFrames.Add(owned);
                StopCommandAttempted = true;
                stopLatched = true;
                IoAttempted = true; Disposition = "INCOMPLETE_UNCONFIRMED";
                try
                {
                    RequireIoWindow(this, clock, deadlines, due, true);
                    Task original = command.WriteAsync(owned, 0, owned.Length);
                    AttachOperation("CONTROL_WRITE", original);
                    return original;
                }
                catch (Exception original) { KeepPrimary("STOP_WRITE_START", original); throw; }
            }
        }
        internal void AttachOperation(string role, Task original)
        {
            if (original == null) throw FixedFailure("MISSING_ORIGINAL_OPERATION");
            lock (errorAndTaskSync)
            {
                allReturnedIoTasks.Add(original);
                if (role == "CONTROL_READ") ControlRead = original;
                if (role == "CONTROL_WRITE") ControlWrite = original;
                if (role == "EXIT_WAIT") ExitWait = original;
                // Every returned task remains strongly rooted, not just the latest.
            }
        }
        internal void BeforeControlIo()
        {
            lock (errorAndTaskSync)
            {
                ProtocolAttempted = true;
                IoAttempted = true;
                Disposition = "INCOMPLETE_UNCONFIRMED";
            }
        }
        internal void RecordEof(StandardStreamRole role, bool eof)
        {
            lock (errorAndTaskSync)
            {
                if (role == StandardStreamRole.Stdout) StdoutEof = eof;
                else if (role == StandardStreamRole.Stderr) StderrEof = eof;
                else throw FixedFailure("UNBOUND_STANDARD_STREAM_ROLE");
            }
        }
        internal string RefusedOrIncomplete()
        {
            // NOT_RUN is only a clear pre-side-effect refusal under this owner.
            lock (errorAndTaskSync)
            {
                if (!StartAttempted && !IoAttempted) return "PRESTART_REFUSED_NOT_RUN";
                return "INCOMPLETE_UNCONFIRMED_HOLD";
            }
        }
        internal void MarkHardDeadlineUnconfirmed()
        {
            lock (errorAndTaskSync)
            {
                LatchStop();
                Disposition = RefusedOrIncomplete();
            }
            // Keep the receipt and native handles/tasks. No automatic release,
            // next case, retry, fake success or claim that the process is gone.
        }
    }

    private static OwnershipReceipt ReserveOwnershipReference()
    {
        RequireExecutionBinding();
        var receipt = new OwnershipReceipt();
        lock (heldOwnershipSync) { heldOwnership.Add(receipt); } // Before side effects.
        return receipt;
    }

    private sealed class ZeroBodyObservation
    {
        internal readonly int Count;
        internal readonly bool Eof;
        internal ZeroBodyObservation(int count, bool eof) { Count = count; Eof = eof; }
    }

    private enum StandardStreamRole { Stdout, Stderr }

    private static async Task<ZeroBodyObservation> ReadZeroBodyReference(Stream stream, OwnershipReceipt receipt, StandardStreamRole role,
        Stopwatch clock, ProposedDeadlineReference deadlines)
    {
        RequireExecutionBinding();
        RequireIoWindow(receipt, clock, deadlines, deadlines.Work, false);
        receipt.ReserveRead(role);
        // Positive one-byte detection even for ZERO permitted body. This does
        // not claim that OS redirection existed before interpreter startup.
        byte[] detection = new byte[1];
        try
        {
            RequireIoWindow(receipt, clock, deadlines, deadlines.Work, false);
            Task<int> originalTask = stream.ReadAsync(detection, 0, 1);
            receipt.AttachRead(role, originalTask);
            int count = await originalTask.ConfigureAwait(false);
            receipt.RecordEof(role, count == 0);
            if (count == 0) return new ZeroBodyObservation(0, true);
            receipt.LatchStop();
            throw FixedFailure("FORBIDDEN_STANDARD_STREAM_BYTE");
        }
        catch (Exception original)
        {
            receipt.KeepPrimary(role == StandardStreamRole.Stdout ? "STDOUT_READ" : "STDERR_READ", original);
            throw;
        }
        finally
        {
            // No raw byte is published. Clearing this local array does not prove
            // deletion of prior copies, OS buffers or framework memory.
            Array.Clear(detection, 0, detection.Length);
        }
    }

    private static async Task WriteCodeInputReference(Stream input, byte[] frame, OwnershipReceipt receipt,
        Stopwatch clock, ProposedDeadlineReference deadlines)
    {
        RequireExecutionBinding();
        if (frame == null || frame.Length != FixedCodeFrameLength || frame.Length > CodeInputLimit)
            throw FixedFailure("CODE_INPUT_OVERFLOW_OR_FIXED_LENGTH_MISMATCH");
        frame = (byte[])frame.Clone();
        RequireIoWindow(receipt, clock, deadlines, deadlines.Work, false);
        receipt.ReserveWrite(frame);
        // Keep the ORIGINAL write task before awaiting; a wait timeout is not
        // settlement and must never cause resend. A synchronous call may block.
        string phase = "INPUT_WRITE";
        try
        {
            RequireIoWindow(receipt, clock, deadlines, deadlines.Work, false);
            Task originalTask = input.WriteAsync(frame, 0, frame.Length);
            receipt.AttachWrite(originalTask);
            await originalTask.ConfigureAwait(false);
            phase = "INPUT_CLOSE";
            RequireIoWindow(receipt, clock, deadlines, deadlines.Work, false);
            input.Close();
            receipt.InputCloseReturned = true;
        }
        catch (Exception original)
        {
            receipt.KeepPrimary(phase, original);
            throw;
        }
    }

    private static void RequestStopReference(OwnershipReceipt receipt, ProposedDeadlineReference deadlines, long sample)
    {
        RequireExecutionBinding();
        try { deadlines.RequireSample(sample); }
        catch (Exception original) { receipt.KeepPrimary("STOP_SAMPLE", original); throw; }
        receipt.LatchStop();
        receipt.Disposition = receipt.RefusedOrIncomplete();
        // No real deadline observation was made by this source formation.
        // A future owner must resample between operations; this sample does not
        // establish that any later Kill/Close/Wait is interruptible or in time.
        if (sample >= deadlines.Hard) { receipt.MarkHardDeadlineUnconfirmed(); return; }
        Process? process = receipt.Process;
        if (process == null) return;
        receipt.KillRequested = true;
        try { if (!process.HasExited) { process.Kill(true); receipt.KillCallReturned = true; } }
        catch (Exception original) { receipt.KeepSecondary("KILL_REQUEST", original); }
        // Waiting, closing streams and disposing are NOT performed from this
        // stale sample. Original tasks stay retained; actual timed cleanup and
        // an independent outer stop mechanism remain NOT_IMPLEMENTED.
    }


    // Creates a descriptor only, never starts a process, opens a path or grants
    // inherited handles. Current bootstrap main also silently refuses.
    private static ProcessStartInfo FixedStartupDescriptorReference(byte[] bootstrap)
    {
        RequireExecutionBinding();
        var snapshot = new SourceSnapshot("BOOTSTRAP", BootstrapFile, BootstrapSha, BootstrapLength, bootstrap);
        string text = new UTF8Encoding(false, true).GetString(snapshot.Bytes);
        if (text.Length == 0 || text[0] == '\uFEFF' || text.IndexOf('\0') >= 0)
            throw FixedFailure("BOOTSTRAP_TEXT_BOUNDARY");
        var info = new ProcessStartInfo(InterpreterFile) {
            UseShellExecute = false, CreateNoWindow = true,
            RedirectStandardInput = true, RedirectStandardOutput = true,
            RedirectStandardError = true
        };
        info.ArgumentList.Add("-I"); info.ArgumentList.Add("-S");
        info.ArgumentList.Add("-B"); info.ArgumentList.Add("-c");
        info.ArgumentList.Add(text);
        // Ambient loader/stdlib/DLL/working-root and handle-binding facts remain
        // UNBOUND. RecordedInterpreterSha is not a verification by this method.
        return info;
    }

    private static readonly byte[] ReadyFrame = Encoding.ASCII.GetBytes("DSP004-READY-V1|158|UNVERIFIED_REPORT\n");
    private static readonly byte[] EndFrame = Encoding.ASCII.GetBytes("DSP004-END-V1|158|UNVERIFIED_REPORT\n");
    private static readonly byte[] StopFrame = Encoding.ASCII.GetBytes("DSP004-COMMAND-V1|STOP\n");
    private static readonly byte[] StoppedFrame = Encoding.ASCII.GetBytes("DSP004-STOPPED-V1|UNVERIFIED_REPORT\n");

    private static bool EqualFrame(byte[] actual, byte[] expected)
    {
        if (actual.Length != expected.Length) return false;
        for (int index = 0; index < actual.Length; index++)
            if (actual[index] != expected[index]) return false;
        return true;
    }

    private static async Task<byte[]> ReadControlFrameReference(Stream report, OwnershipReceipt receipt,
        Stopwatch clock, ProposedDeadlineReference deadlines, long due, bool allowStopped)
    {
        RequireExecutionBinding();
        RequireIoWindow(receipt, clock, deadlines, due, allowStopped);
        receipt.BeforeControlIo();
        byte[] buffer = new byte[ControlFrameLimit];
        int used = 0;
        try
        {
            while (used < buffer.Length)
            {
                RequireIoWindow(receipt, clock, deadlines, due, allowStopped);
                Task<int> original = report.ReadAsync(buffer, used, 1);
                receipt.AttachOperation("CONTROL_READ", original); // BEFORE await.
                int count = await original.ConfigureAwait(false);
                if (count != 1) throw FixedFailure("PRIVATE_REPORT_EOF_OR_INCOMPLETE");
                byte value = buffer[used++];
                if (value == 10)
                {
                    byte[] frame = new byte[used];
                    Buffer.BlockCopy(buffer, 0, frame, 0, used);
                    return frame; // No read-ahead, coalesced next frame stays on stream.
                }
                if (value < 33 || value > 126) throw FixedFailure("PRIVATE_REPORT_NONCANONICAL_ASCII");
            }
            throw FixedFailure("PRIVATE_REPORT_FRAME_OVERFLOW");
        }
        catch (Exception original) { receipt.KeepPrimary("CONTROL_READ", original); throw; }
        finally { Array.Clear(buffer, 0, buffer.Length); }
    }

    private static long SampleReference(Stopwatch clock, ProposedDeadlineReference deadlines)
    {
        if (clock == null || clock.GetType() != typeof(Stopwatch) || !clock.IsRunning)
            throw FixedFailure("NATIVE_RUNNING_MONOTONIC_CLOCK_REQUIRED");
        long sample = clock.ElapsedMilliseconds;
        deadlines.RequireSample(sample);
        return sample;
    }

    private static void RequireIoWindow(OwnershipReceipt receipt, Stopwatch clock,
        ProposedDeadlineReference deadlines, long due, bool allowStopped)
    {
        long sample = SampleReference(clock, deadlines);
        if (sample >= Math.Min(due, deadlines.Hard))
            throw FixedFailure("NO_NEW_OPERATION_AFTER_PROPOSED_DEADLINE");
        if (!allowStopped && receipt.StopLatched)
            throw FixedFailure("NO_NEW_ACTIVE_IO_AFTER_STOP");
    }

    // Original work and every wrapper remain in the receipt on timeout. A
    // timeout does not cancel, settle or transfer the underlying operation.
    private static async Task AwaitWithinReference(Task work, OwnershipReceipt receipt,
        Stopwatch clock, ProposedDeadlineReference deadlines, long due,
        Task stdout, Task stderr, bool allowStandardEof)
    {
        RequireExecutionBinding();
        due = Math.Min(due, deadlines.Hard);
        while (true)
        {
            long sample = SampleReference(clock, deadlines);
            if (sample >= due) throw FixedFailure("PROPOSED_DEADLINE_EXPIRED");
            // Faults are observed as original task errors, never rendered.
            if (stdout.IsFaulted || stdout.IsCanceled) await stdout.ConfigureAwait(false);
            if (stderr.IsFaulted || stderr.IsCanceled) await stderr.ConfigureAwait(false);
            if (!allowStandardEof && (stdout.IsCompleted || stderr.IsCompleted))
                throw FixedFailure("STANDARD_EOF_BEFORE_CONTROL_SETTLED");
            if (work.IsCompleted)
            {
                await work.ConfigureAwait(false);
                if (SampleReference(clock, deadlines) >= due)
                    throw FixedFailure("COMPLETION_OBSERVED_AFTER_PROPOSED_DEADLINE");
                return;
            }
            var pending = new List<Task> { work };
            Task delay = Task.Delay((int)Math.Min(20, due - sample));
            receipt.AttachOperation("WAIT_DELAY", delay);
            pending.Add(delay);
            if (!stdout.IsCompleted) pending.Add(stdout);
            if (!stderr.IsCompleted) pending.Add(stderr);
            Task<Task> wrapper = Task.WhenAny(pending);
            receipt.AttachOperation("WAIT_WRAPPER", wrapper);
            await wrapper.ConfigureAwait(false);
        }
    }

    private static async Task RequireControlEofReference(Stream report, OwnershipReceipt receipt,
        Stopwatch clock, ProposedDeadlineReference deadlines, long due)
    {
        RequireExecutionBinding();
        RequireIoWindow(receipt, clock, deadlines, due, true);
        receipt.BeforeControlIo();
        byte[] detection = new byte[1];
        try
        {
            RequireIoWindow(receipt, clock, deadlines, due, true);
            Task<int> original = report.ReadAsync(detection, 0, 1);
            receipt.AttachOperation("CONTROL_READ", original);
            if (await original.ConfigureAwait(false) != 0)
                throw FixedFailure("EXTRA_PRIVATE_REPORT_AFTER_STOPPED");
        }
        catch (Exception original) { receipt.KeepPrimary("CONTROL_EOF", original); throw; }
        finally { Array.Clear(detection, 0, detection.Length); }
    }

    // A future owner must establish endpoints and process identity before this
    // private reference can even be considered. This is not an injection API.
    // No Process.Start appears here; no environment/source is admitted.
    private static Task BeginClosedProtocolReference(OwnershipReceipt receipt,
        Stream code, Stream command, Stream report, Stream stdout, Stream stderr,
        byte[] dependency, byte[] contract, byte[] carrier, Stopwatch clock, long externalT0)
    {
        RequireExecutionBinding();
        lock (heldOwnershipSync)
        {
            bool held = false;
            foreach (OwnershipReceipt item in heldOwnership)
                if (ReferenceEquals(item, receipt)) { held = true; break; }
            if (!held) throw FixedFailure("UNOWNED_PROTOCOL_RECEIPT");
        }
        try
        {
            if (receipt.Process == null || !receipt.StartAttempted ||
                receipt.ProtocolAttempted || receipt.StopLatched)
                throw FixedFailure("PROTOCOL_OWNER_OR_ENDPOINTS_UNBOUND");
            receipt.ProtocolAttempted = true; // One attempt, including preparation failures.
            receipt.BindProtocolStreams(new[] { code, command, report, stdout, stderr });
            var deadlines = new ProposedDeadlineReference(externalT0);
            RequireIoWindow(receipt, clock, deadlines, deadlines.Work, false);
            // No preframed byte[] input accepted. Clone, fixed length/SHA, then
            // frame these very private snapshots internally; no file reopening.
            SourceSnapshot[] sources = CreateSourceSnapshotsReference(dependency, contract, carrier);
            byte[] input = BuildCodeInputReference(sources);
            receipt.InputSnapshot = input;
            RequireIoWindow(receipt, clock, deadlines, deadlines.Work, false);
            Task task = ClosedProtocolReference(receipt, code, command, report, stdout, stderr,
                                                input, clock, externalT0);
            receipt.AttachOperation("PROTOCOL_WRAPPER", task);
            return task;
        }
        catch (Exception original) { receipt.KeepPrimary("PROTOCOL_BEGIN", original); throw; }
    }

    private static async Task ClosedProtocolReference(OwnershipReceipt receipt,
        Stream code, Stream command, Stream report, Stream stdout, Stream stderr,
        byte[] input, Stopwatch clock, long externalT0)
    {
        RequireExecutionBinding();
        var deadlines = new ProposedDeadlineReference(externalT0);
        // T0 must be from this very clock and precede FIRST preparation read/
        // hash/IPC/start. This candidate does not establish that origin.
        var order = new ReportOrderReference();
        int reported = 0;
        string phase = "ZERO_BODY_MONITORS";
        try
        {
            RequireIoWindow(receipt, clock, deadlines, deadlines.Work, false);
            Task<ZeroBodyObservation> outTask = ReadZeroBodyReference(stdout, receipt, StandardStreamRole.Stdout, clock, deadlines);
            receipt.AttachOperation("STDOUT_WRAPPER", outTask);
            Task<ZeroBodyObservation> errTask = ReadZeroBodyReference(stderr, receipt, StandardStreamRole.Stderr, clock, deadlines);
            receipt.AttachOperation("STDERR_WRAPPER", errTask);
            // Start BOTH monitors; do not await silent live-stream EOF.
            phase = "CODE_INPUT";
            Task write = WriteCodeInputReference(code, input, receipt, clock, deadlines);
            receipt.AttachOperation("CODE_WRITE_WRAPPER", write);
            await AwaitWithinReference(write, receipt, clock, deadlines, deadlines.Work, outTask, errTask, false).ConfigureAwait(false);
            // Write/Close returned is not child EOF evidence. READY is still only
            // UNVERIFIED_REPORT; bootstrap source requires actual input EOF first.
            phase = "READY";
            Task<byte[]> ready = ReadControlFrameReference(report, receipt, clock, deadlines, deadlines.Work, false);
            receipt.AttachOperation("CONTROL_WRAPPER", ready);
            await AwaitWithinReference(ready, receipt, clock, deadlines, deadlines.Work, outTask, errTask, false).ConfigureAwait(false);
            if (!EqualFrame(await ready.ConfigureAwait(false), ReadyFrame)) throw FixedFailure("READY_FRAME_MISMATCH");

            for (int ordinal = 1; ordinal <= CaseIds.Length; ordinal++)
            {
                phase = "NEXT_DISPATCH";
                if (receipt.StopLatched) throw FixedFailure("DISPATCH_AFTER_STOP");
                long dispatch = SampleReference(clock, deadlines);
                if (dispatch >= deadlines.Work || dispatch >= deadlines.Hard) throw FixedFailure("NO_DISPATCH_TIME");
                long due = deadlines.CaseDue(dispatch);
                byte[] next = Encoding.ASCII.GetBytes("DSP004-COMMAND-V1|NEXT|" +
                    ordinal.ToString(CultureInfo.InvariantCulture) + "|" + CaseIds[ordinal - 1] + "\n");
                Task sent = receipt.StartNextWriteReference(command, next, ordinal, clock, deadlines, due);
                receipt.AttachOperation("COMMAND_WRAPPER", sent);
                await AwaitWithinReference(sent, receipt, clock, deadlines, due, outTask, errTask, false).ConfigureAwait(false);
                phase = "CASE_REPORT";
                Task<byte[]> read = ReadControlFrameReference(report, receipt, clock, deadlines, due, false);
                receipt.AttachOperation("CONTROL_WRAPPER", read);
                await AwaitWithinReference(read, receipt, clock, deadlines, due, outTask, errTask, false).ConfigureAwait(false);
                MinimalReport item = order.ConsumeCompleteFrame(await read.ConfigureAwait(false));
                reported = item.Ordinal;
                if (item.Determination != "PASS")
                {
                    receipt.LatchStop();
                    break; // SETUP NOT_EVALUABLE also stops. No unknown tail => NOT_RUN claim.
                }
            }
            if (reported == CaseIds.Length && order.DirectoryReported)
            {
                phase = "END_FRAME";
                Task<byte[]> end = ReadControlFrameReference(report, receipt, clock, deadlines, deadlines.Work, false);
                receipt.AttachOperation("CONTROL_WRAPPER", end);
                await AwaitWithinReference(end, receipt, clock, deadlines, deadlines.Work, outTask, errTask, false).ConfigureAwait(false);
                if (!EqualFrame(await end.ConfigureAwait(false), EndFrame)) throw FixedFailure("END_FRAME_MISMATCH");
            }
            phase = "STOP_COMMAND";
            receipt.LatchStop();
            long stopDue = deadlines.TerminationDue(SampleReference(clock, deadlines));
            Task stop = receipt.StartStopWriteReference(command, clock, deadlines, stopDue);
            receipt.AttachOperation("STOP_WRAPPER", stop);
            await AwaitWithinReference(stop, receipt, clock, deadlines, stopDue, outTask, errTask, true).ConfigureAwait(false);
            phase = "COMMAND_CLOSE";
            RequireIoWindow(receipt, clock, deadlines, stopDue, true);
            command.Close(); // Synchronous block remains an external-owner limitation.
            phase = "STOPPED_FRAME";
            Task<byte[]> stopped = ReadControlFrameReference(report, receipt, clock, deadlines, stopDue, true);
            receipt.AttachOperation("CONTROL_WRAPPER", stopped);
            await AwaitWithinReference(stopped, receipt, clock, deadlines, stopDue, outTask, errTask, true).ConfigureAwait(false);
            if (!EqualFrame(await stopped.ConfigureAwait(false), StoppedFrame)) throw FixedFailure("STOPPED_FRAME_MISMATCH");
            phase = "CONTROL_EOF";
            long cleanupDue = deadlines.CleanupDue(SampleReference(clock, deadlines));
            Task eof = RequireControlEofReference(report, receipt, clock, deadlines, cleanupDue);
            receipt.AttachOperation("CONTROL_WRAPPER", eof);
            await AwaitWithinReference(eof, receipt, clock, deadlines, cleanupDue, outTask, errTask, true).ConfigureAwait(false);
            phase = "DIRECT_CHILD_EXIT";
            RequireIoWindow(receipt, clock, deadlines, cleanupDue, true);
            Task exit = receipt.Process!.WaitForExitAsync();
            receipt.AttachOperation("EXIT_WAIT", exit);
            await AwaitWithinReference(exit, receipt, clock, deadlines, cleanupDue, outTask, errTask, true).ConfigureAwait(false);
            receipt.ChildExitObserved = true;
            await AwaitWithinReference(outTask, receipt, clock, deadlines, cleanupDue, outTask, errTask, true).ConfigureAwait(false);
            await AwaitWithinReference(errTask, receipt, clock, deadlines, cleanupDue, outTask, errTask, true).ConfigureAwait(false);
            // No aggregate PASS, descendant/destruction/cleanup certificate or
            // assertion of native comparisons. Even all metadata stays unverified.
            receipt.Disposition = "CONTROL_METADATA_SETTLED_UNVERIFIED_OUTSIDE_OWNERSHIP_HOLD";
        }
        catch (Exception original)
        {
            receipt.KeepPrimary(phase, original);
            try { RequestStopReference(receipt, deadlines, SampleReference(clock, deadlines)); }
            catch (Exception stopping) { receipt.KeepSecondary("STOP_PATH", stopping); }
            throw;
        }
        // Never Dispose/clear a receipt with unsettled tasks, never start another
        // batch, infer unknown tail NOT_RUN or send STOP after an uncertain write.
    }


    private static InvalidOperationException FixedFailure(string code)
    {
        // Call sites use fixed local codes only, never a source/error rendering.
        return new InvalidOperationException(code);
    }
}
