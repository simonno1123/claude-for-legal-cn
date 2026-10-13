#nullable enable
using System;
using System.Collections.Generic;
using System.Threading;

namespace Dsp004SyntheticFailureCoexistence
{
// Closed in-memory synthetic candidate only. No process/stream/resource cleanup
// is performed or proven. Accepted files and their outcomes remain unchanged.
// Actual exceptions from fixed synthetic operations are retained by reference
// privately; public metadata is not cross-process retention or authority proof.
public sealed class Dsp004SyntheticFailureCoexistenceCandidateRev1
{
    private static int reserved;
    private Dsp004SyntheticFailureCoexistenceCandidateRev1() { }

    public static CaseObservation[] RunFixedSyntheticBatch()
    {
        if (Interlocked.Exchange(ref reserved, 1) != 0)
            return new[] { new CaseObservation(RetainedCase.RefusedRepeat()) };
        var result = new List<CaseObservation>();
        for (int number = 1; number <= 9; number++)
            result.Add(RunOneFixedCase(number));
        return result.ToArray();
    }

    private static CaseObservation RunOneFixedCase(int number)
    {
        bool primaryFails = number == 2 || number == 4 || number == 5 || number == 6 || number == 8;
        bool closeFails = number == 3 || number == 4 || number == 5 || number == 6 || number == 7 || number == 8 || number == 9;
        bool disposeFails = number == 5 || number == 6 || number == 7;
        Exception? originalPrimary = primaryFails ? new InvalidOperationException("FIXED_SYNTHETIC_PRIMARY") : null;
        Exception? closeFailure = closeFails ? new InvalidOperationException("FIXED_SYNTHETIC_CLOSE") : null;
        Exception? disposeFailure = disposeFails
            ? (number == 6 ? closeFailure : new ObjectDisposedException("FIXED_SYNTHETIC_DISPOSE"))
            : null;
        var record = new RetainedCase("F-" + number.ToString("D2"), originalPrimary);
        try
        {
            record.PrimaryAttempted = true;
            if (originalPrimary != null) throw originalPrimary;
            record.PrimaryReturned = true;
        }
        catch (Exception caught) { record.RetainPrimary(caught); }

        // F-08 attempts completion while the primary stop is already latched.
        // F-09 tentatively completes, then revokes that result on cleanup error.
        if (number == 8 || number == 9) record.TryCompleteSyntheticResult();
        record.StopLatchedBeforeCleanup = record.StopLatched;
        RunFixedCleanup(record, "SYNTHETIC_CLOSE", closeFailure);
        RunFixedCleanup(record, "SYNTHETIC_DISPOSE", disposeFailure);
        RunFixedCleanup(record, "SYNTHETIC_FINALIZE", null);
        record.TryCompleteSyntheticResult();
        return new CaseObservation(record);
    }

    private static void RunFixedCleanup(RetainedCase record, string stage, Exception? original)
    {
        record.CleanupAttempts++;
        var operation = new SyntheticCleanupOperation(original);
        try
        {
            operation.Dispose();
            record.CleanupReturned++;
        }
        catch (Exception caught) { record.RetainCleanup(stage, original, caught); }
    }

    private sealed class SyntheticCleanupOperation : IDisposable
    {
        private readonly Exception? original;
        internal SyntheticCleanupOperation(Exception? original) { this.original = original; }
        public void Dispose() { if (original != null) throw original; }
    }

    internal sealed class RetainedFailure
    {
        internal readonly string Stage;
        internal readonly Exception? Original;
        internal readonly Exception Caught;
        internal RetainedFailure(string stage, Exception? original, Exception caught)
        { Stage = stage; Original = original; Caught = caught; }
    }

    internal sealed class RetainedCase
    {
        internal readonly string Id;
        internal readonly Exception? OriginalPrimary;
        internal Exception? Primary;
        internal readonly List<RetainedFailure> CleanupFailures = new List<RetainedFailure>();
        internal bool PrimaryAttempted;
        internal bool PrimaryReturned;
        internal bool StopLatched;
        internal bool StopLatchedBeforeCleanup;
        internal bool BodyRecorded;
        internal bool RepeatRefused;
        internal int CleanupAttempts;
        internal int CleanupReturned;
        internal int CompletionAttempts;
        internal int HistoricalCompletionSuccesses;
        internal string FirstReason = "NO_SYNTHETIC_FAILURE";
        internal RetainedCase(string id, Exception? originalPrimary)
        { Id = id; OriginalPrimary = originalPrimary; }
        internal static RetainedCase RefusedRepeat()
        {
            return new RetainedCase("F-REPEAT", null)
            { RepeatRefused = true, FirstReason = "REPEATED_LOCAL_BATCH_REFUSED" };
        }
        private void LatchStop(string reason)
        {
            if (!StopLatched) FirstReason = reason;
            StopLatched = true;
            BodyRecorded = false;
        }
        internal void RetainPrimary(Exception caught)
        {
            if (Primary != null) throw new InvalidOperationException("PRIMARY_ALREADY_RECORDED");
            Primary = caught;
            LatchStop("PRIMARY_FAILURE");
        }
        internal void RetainCleanup(string stage, Exception? original, Exception caught)
        {
            CleanupFailures.Add(new RetainedFailure(stage, original, caught));
            LatchStop("CLEANUP_FAILURE_WITHOUT_PRIMARY");
        }
        internal bool TryCompleteSyntheticResult()
        {
            CompletionAttempts++;
            if (StopLatched || RepeatRefused) return false;
            BodyRecorded = true;
            HistoricalCompletionSuccesses++;
            return true;
        }
    }

    public sealed class CaseObservation
    {
        // The record is kept private after construction. No public Exception,
        // mutable array, setter, callback or operation is exposed by this object.
        private readonly RetainedCase retained;
        internal CaseObservation(RetainedCase retained) { this.retained = retained; }
        public string CaseId => retained.Id;
        public string FirstReason => retained.FirstReason;
        public bool PrimaryAttempted => retained.PrimaryAttempted;
        public bool PrimaryReturned => retained.PrimaryReturned;
        public bool PrimaryFailurePresent => retained.Primary != null;
        public string? PrimaryFailureType => retained.Primary?.GetType().FullName;
        public bool PrimaryReferenceRetained => retained.Primary != null && ReferenceEquals(retained.OriginalPrimary, retained.Primary);
        public int CleanupAttempts => retained.CleanupAttempts;
        public int CleanupReturned => retained.CleanupReturned;
        public int CleanupFailureOccurrences => retained.CleanupFailures.Count;
        public string CleanupFailureTypes
        {
            get
            {
                var types = new List<string>();
                foreach (RetainedFailure failure in retained.CleanupFailures)
                    types.Add(failure.Caught.GetType().FullName!);
                return string.Join(";", types);
            }
        }
        public string CleanupFailureStages
        {
            get
            {
                var stages = new List<string>();
                foreach (RetainedFailure failure in retained.CleanupFailures) stages.Add(failure.Stage);
                return string.Join(";", stages);
            }
        }
        public bool AllCleanupReferencesRetained
        {
            get
            {
                foreach (RetainedFailure failure in retained.CleanupFailures)
                    if (!ReferenceEquals(failure.Original, failure.Caught)) return false;
                return true;
            }
        }
        public bool SameExceptionHasTwoCleanupOccurrences => retained.CleanupFailures.Count == 2 &&
            ReferenceEquals(retained.CleanupFailures[0].Caught, retained.CleanupFailures[1].Caught);
        public bool StopLatched => retained.StopLatched;
        public bool StopLatchedBeforeCleanup => retained.StopLatchedBeforeCleanup;
        public bool SyntheticBodyRecorded => retained.BodyRecorded;
        public bool StoppedResultNotRestored => retained.StopLatched && !retained.BodyRecorded;
        public int CompletionAttempts => retained.CompletionAttempts;
        public int HistoricalCompletionSuccesses => retained.HistoricalCompletionSuccesses;
        public bool RepeatRefused => retained.RepeatRefused;
        public string ObservationScope => "NEW FIXED IN-MEMORY SYNTHETIC OPERATIONS ONLY; NOT ACCEPTED SUPERVISOR OR PROCESS CLEANUP";
        public string IdentityQualification => "IN-PROCESS REFERENCE CHECK ONLY; NO CROSS-PROCESS RETENTION OR FREEZE PROOF";
        public string CleanupQualification => "SYNTHETIC DISPOSE METHODS ONLY; NO OS RESOURCE OR DESCENDANT SETTLEMENT CLAIM";
        public string Authority => "NOT ESTABLISHED";
        public string SourceAdmission => "NOT ESTABLISHED";
    }
}
}
