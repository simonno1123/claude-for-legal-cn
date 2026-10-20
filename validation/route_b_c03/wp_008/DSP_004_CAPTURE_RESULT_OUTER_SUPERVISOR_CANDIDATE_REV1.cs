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

// DSP-004 outer-supervisor SOURCE CANDIDATE REV1. Static formation/review only.
// No loading, compilation, tests, environment probing or runtime is authorized.
// The only public entry REFUSES before file I/O, clocks, IPC or process creation.
// No bool grant, path/command argument, callback, public constructor or setter.
// Private reference helpers are not an execution interface or security sandbox.
//
// Fixed design basis: executor-handoff design REV2 (conversation text, no SHA).
// Reused SOURCE PATTERNS ONLY, not historical authority, execution or acceptance:
// O: 891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB
// S: FA6625FA2917B056801A598B445C3A68E86A147C2A237260893A784B4449A066
// C: 9B165A04AFE786224965C5E33364140265FF3CB0B4B99A8E63A7AE7562C33E4E
// S swallows some wait exceptions; only C's explicit primary/secondary paths
// inform failure classification here. Neither old supervisor proves ownership
// transfer of unsettled tasks, a full descendant scope or bounded synchronous I/O.
//
// This source implements private REFERENCE logic for byte snapshots, framing,
// report order, proposed deadlines and in-host ownership receipts. It does NOT
// implement a fixed Python bootstrap/resolver, OS private-channel creation,
// interpreter identity binding, complete process containment, independent hard
// stopping, durable cleanup ownership, actual loading or a runnable batch loop.
// Creating a wire frame is not delivering it. Decoding a frame authenticates
// neither the child nor the asserted comparison. All child data is UNVERIFIED.
// No stdout ACK, JSON report, legacy 8/189-case outcome or old 120-second budget
// transfers to this new 158-item source directory.
//
// L1 environment/roots/authority/resolver and same-byte physical use are UNBOUND.
// L2 158 recipes/oracles/pseudo-member behavior are NOT_RUN; not the 189-item plan.
// L3 channel/output/timing/stop/cleanup execution is NOT_IMPLEMENTED. 4KiB is a
// proposed per-control-frame ceiling, not a verified physical channel capacity.
// Code-input framing has a distinct 256KiB proposed ceiling; it does NOT enlarge
// a former accepted 64KiB input contract. Neither new ceiling has runtime approval.
// 60/2/5/5/70 seconds are proposed arithmetic only. Old 5-second exit/task waits
// were not complete termination/cleanup guarantees. No budget proves 158 finishes.
//
// All retained native exceptions/handles below are private and only in this
// host process. Closure/Dispose/kill return/EOF/exit are separate observations;
// none proves destruction, all descendants ended, or lossless error preservation.
// Host termination can lose these receipts. The still-missing outside controller
// and continued ownership must be bound BEFORE any future execution.
// DSP-004 OPEN/HOLD; B-01/B-02 OPEN. No aggregate privacy/security/legal verdict,
// source admission, actual capture, finding, integration, acceptance or deployment.
public sealed class Dsp004CaptureResultOuterSupervisorCandidateRev1
{
    private const string CarrierFile = "validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV2.py";
    private const string CarrierSha = "634AC0CB18B0877B619A4FFAEFBBD4AA95C8DEBAACD7018FEBFB6A4C18B03365";
    private const int CarrierLength = 53568;
    private const string ContractFile = "validation/route_b_c03/wp_008/DSP_004_CAPTURE_RESULT_CONTRACT_CANDIDATE_REV1.py";
    private const string ContractSha = "E9472328847617EBF629FB01A0A163C0805226690600E5E13EBE1209E2F6705C";
    private const int ContractLength = 18301;
    private const string DependencyFile = "scripts/phase2_runtime/route_b_c03/contracts.py";
    private const string DependencySha = "7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4";
    private const int DependencyLength = 16475;
    private const int ControlFrameLimit = 4096;
    private const int CodeInputLimit = 262144;
    private const string ReportVersion = "DSP004-CAPTURE-V1";
    private const string SourceVersion = "DSP004-CAPTURE-SOURCES-V1";
    private static int reserved;
    private static readonly List<OwnershipReceipt> heldOwnership = new List<OwnershipReceipt>();
    private Dsp004CaptureResultOuterSupervisorCandidateRev1() { }

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
            // The physical accumulator, peer binding and channel are UNIMPLEMENTED.
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
        internal byte[]? InputSnapshot;
        internal bool StartAttempted, IoAttempted, KillRequested, KillCallReturned;
        internal volatile bool StopLatched;
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
                StopLatched = true;
            }
        }
        internal void KeepSecondary(string phase, Exception original)
        {
            if (original == null) throw FixedFailure("MISSING_NATIVE_ERROR");
            lock (errorAndTaskSync)
            {
                Secondary.Add(new KeyValuePair<string, Exception>(phase, original));
                StopLatched = true;
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
                StopLatched = true;
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
        heldOwnership.Add(receipt); // Strong root BEFORE future side-effect calls.
        return receipt;
    }

    private sealed class ZeroBodyObservation
    {
        internal readonly int Count;
        internal readonly bool Eof;
        internal ZeroBodyObservation(int count, bool eof) { Count = count; Eof = eof; }
    }

    private enum StandardStreamRole { Stdout, Stderr }

    private static async Task<ZeroBodyObservation> ReadZeroBodyReference(Stream stream, OwnershipReceipt receipt, StandardStreamRole role)
    {
        RequireExecutionBinding();
        receipt.ReserveRead(role);
        // Positive one-byte detection even for ZERO permitted body. This does
        // not claim that OS redirection existed before interpreter startup.
        byte[] detection = new byte[1];
        try
        {
            Task<int> originalTask = stream.ReadAsync(detection, 0, 1);
            receipt.AttachRead(role, originalTask);
            int count = await originalTask.ConfigureAwait(false);
            receipt.RecordEof(role, count == 0);
            if (count == 0) return new ZeroBodyObservation(0, true);
            receipt.StopLatched = true;
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

    private static async Task WriteCodeInputReference(Stream input, byte[] frame, OwnershipReceipt receipt)
    {
        RequireExecutionBinding();
        if (frame == null || frame.Length > CodeInputLimit) throw FixedFailure("CODE_INPUT_OVERFLOW");
        receipt.ReserveWrite(frame);
        // Keep the ORIGINAL write task before awaiting; a wait timeout is not
        // settlement and must never cause resend. A synchronous call may block.
        string phase = "INPUT_WRITE";
        try
        {
            Task originalTask = input.WriteAsync(frame, 0, frame.Length);
            receipt.AttachWrite(originalTask);
            await originalTask.ConfigureAwait(false);
            phase = "INPUT_CLOSE";
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
        receipt.StopLatched = true;
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

    private static InvalidOperationException FixedFailure(string code)
    {
        // Call sites use fixed local codes only, never a source/error rendering.
        return new InvalidOperationException(code);
    }
}
