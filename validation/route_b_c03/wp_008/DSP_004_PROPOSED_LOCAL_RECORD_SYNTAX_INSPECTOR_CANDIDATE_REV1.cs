// DSP-004 SOURCE CANDIDATE ONLY: PROPOSED single local-record grammar.
// Not accepted, compiled, loaded, called, tested or integrated.
// No entry point, encoder, publisher, reader, consumer, DUT or worker call.
// Recorded A source binding:
// 46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C
// Recorded 189-item catalog text binding:
// 4BAED6E284C92A2403117C72CFBF419BD2B6FB478A55697CA2229201C8FB149E
// These literals do not authenticate source, bytes, objects or authority.
//
// PROPOSAL ONLY: DSP004-LOCAL-ITEM-V1|ID|STATE followed by one LF.
// This is NOT the DUT's separate DSP004-STATUS-V1 frame protocol.
// Marker and 39-byte maximum remain proposals, not Owner-accepted protocol.
// Exact case-sensitive ID membership is only the original 189 items:
// M-001..006 / RQ-001..018 / D-001..007 / F-001..062 /
// RD-001..052 / WR-001..044. No expansion, dispatch or batch loop.
// MATCH / NOT_MATCH / NOT_RUN / INCOMPLETE are REPORTED TOKENS ONLY.
// Even GRAMMAR_CONFORMS_ONLY does not determine any true execution state.
//
// Input is a caller-supplied exact native byte[]. Over 39: length rejection
// without copying, inspecting or searching its content. Within 39: at most
// 39 element reads into a private local copy, then grammar checks on that copy.
// A copy does not prove a consistent historical snapshot, freezing, origin,
// private ownership, absence of concurrent writes, memory/time safety or EOF.
// The caller's allocation, framework/host work and exception lifetime remain
// LIMITED. This is not a real reader's 39+1 tail-detection implementation.
// No record order/uniqueness, 7371-byte batch budget, atomic consumption,
// stop linearization, output closure, resource settlement or timer is proved.
//
// Exact marker / two pipes / fixed three decimal digits / one final LF.
// No normalization, culture-sensitive parsing, decoding replacement, fixing,
// unknown object conversion, Equals/GetHashCode/ToString, delegate or callback.
// Returned ID and state are only bounded recognized grammar tokens.
// No raw bytes/frame or exception message/stack/trace is returned or printed.
// An inspection exception, if a result can return, is held privately only.
// It is not a retained DUT/capture exception or total lifetime guarantee.
//
// ALL upstream LIMITED retained. D-007 UNBOUND / NOT_RUN; real driver positive
// SHA branch NOT COVERED. 120/5/5 and 39/7371 are design proposals.
// DSP-004 OPEN / HOLD; B-01 and B-02 OPEN. No source admission, capture,
// compilation, loading, tests, integration, ACOS or other-project action.

using System;

namespace ClaudeForLegalCn.Dsp004.Candidates
{
    public sealed class Dsp004ProposedLocalRecordSyntaxRelation
    {
        public string SyntaxRelation { get; }
        public string RecordedItemId { get; }
        public string RecordedStateToken { get; }
        public string SourceQualification { get; }
        public string InputSnapshot { get; }
        public string ProtocolAcceptance { get; }
        public string ExecutionState { get; }
        public string ChannelEnd { get; }
        public string BatchOrderAndUniqueness { get; }
        public string AtomicCommitStopRace { get; }
        public string Authority { get; }
        public string ResourceAndTimingGuarantee { get; }
        public string BatchCompletion { get; }

        private readonly Exception retainedInspectionException;

        internal Dsp004ProposedLocalRecordSyntaxRelation(string relation,
            string id, string token, Exception error, bool completedCopy = false)
        {
            SyntaxRelation = relation;
            RecordedItemId = id;
            RecordedStateToken = token;
            SourceQualification = "CALLER-SUPPLIED BYTE ARRAY ONLY - NOT AUTHENTICATED";
            InputSnapshot = completedCopy
                ? "COPIED ELEMENT OBSERVATIONS ONLY - NOT FROZEN OR HISTORICAL SNAPSHOT"
                : "NO COMPLETED COPY - NOT A SNAPSHOT";
            ProtocolAcceptance = "PROPOSAL ONLY - NOT OWNER ACCEPTED";
            ExecutionState = "NOT DETERMINED";
            ChannelEnd = "NOT OBSERVED";
            BatchOrderAndUniqueness = "NOT CHECKED / NO CONSUMPTION";
            AtomicCommitStopRace = "NOT IMPLEMENTED";
            Authority = "NOT ESTABLISHED";
            ResourceAndTimingGuarantee = "NOT ESTABLISHED";
            BatchCompletion = "NOT ESTABLISHED";
            retainedInspectionException = error;
        }
    }

    public static class Dsp004ProposedLocalRecordSyntaxInspectorCandidateRev1
    {
        private const string Marker = "DSP004-LOCAL-ITEM-V1";
        private const int MaximumProposedRecordBytes = 39;
        private const int MinimumProposedRecordBytes = 33;

        private static bool EqualBytes(byte[] inspected, int start, int length, string literal)
        {
            if (length != literal.Length) return false;
            for (int k = 0; k < length; k++)
                if (inspected[start + k] != (byte)literal[k]) return false;
            return true;
        }

        private static string OriginalItemId(byte[] inspected, int start, int length)
        {
            int maximum;
            int digitsAt;
            if (length == 5 && inspected[start + 1] == (byte)'-')
            {
                byte prefix = inspected[start];
                maximum = prefix == (byte)'M' ? 6 : prefix == (byte)'D' ? 7
                    : prefix == (byte)'F' ? 62 : 0;
                digitsAt = start + 2;
            }
            else if (length == 6 && inspected[start + 2] == (byte)'-')
            {
                byte first = inspected[start];
                byte second = inspected[start + 1];
                maximum = first == (byte)'R' && second == (byte)'Q' ? 18
                    : first == (byte)'R' && second == (byte)'D' ? 52
                    : first == (byte)'W' && second == (byte)'R' ? 44 : 0;
                digitsAt = start + 3;
            }
            else return null;
            if (maximum == 0) return null;
            int number = 0;
            for (int k = 0; k < 3; k++)
            {
                byte digit = inspected[digitsAt + k];
                if (digit < (byte)'0' || digit > (byte)'9') return null;
                number = number * 10 + digit - (byte)'0';
            }
            if (number < 1 || number > maximum) return null;
            char[] heldId = new char[length];
            for (int k = 0; k < length; k++) heldId[k] = (char)inspected[start + k];
            return new string(heldId);
        }

        private static string ReportedState(byte[] inspected, int start, int length)
        {
            if (EqualBytes(inspected, start, length, "MATCH")) return "MATCH";
            if (EqualBytes(inspected, start, length, "NOT_MATCH")) return "NOT_MATCH";
            if (EqualBytes(inspected, start, length, "NOT_RUN")) return "NOT_RUN";
            if (EqualBytes(inspected, start, length, "INCOMPLETE")) return "INCOMPLETE";
            return null;
        }

        private static Dsp004ProposedLocalRecordSyntaxRelation Rejected(string relation, bool copied = false)
        {
            return new Dsp004ProposedLocalRecordSyntaxRelation(relation, null, null, null, copied);
        }

        public static Dsp004ProposedLocalRecordSyntaxRelation Inspect(object callerSuppliedBytes)
        {
            bool copied = false;
            try
            {
                if (callerSuppliedBytes == null || callerSuppliedBytes.GetType() != typeof(byte[]))
                    return Rejected("NATIVE_REPORTED_BYTE_ARRAY_REQUIRED");
                byte[] reported = (byte[])callerSuppliedBytes;
                int length = reported.Length;
                // No content read, copy or search before these length guards.
                if (length > MaximumProposedRecordBytes)
                    return Rejected("PROPOSED_RECORD_LENGTH_REJECTED");
                if (length < MinimumProposedRecordBytes)
                    return Rejected("PROPOSED_RECORD_SYNTAX_REJECTED");

                byte[] inspected = new byte[length];
                for (int k = 0; k < length; k++) inspected[k] = reported[k];
                copied = true;
                // All grammar checks below read only this private copy.
                // The copy itself is NOT an attested historical snapshot.
                if (inspected[length - 1] != 10)
                    return Rejected("PROPOSED_RECORD_SYNTAX_REJECTED", copied);
                for (int k = 0; k < length - 1; k++)
                    if (inspected[k] < 33 || inspected[k] > 126)
                        return Rejected("PROPOSED_RECORD_SYNTAX_REJECTED", copied);
                if (!EqualBytes(inspected, 0, Marker.Length, Marker)
                    || inspected[Marker.Length] != (byte)'|')
                    return Rejected("PROPOSED_RECORD_SYNTAX_REJECTED", copied);

                int idStart = Marker.Length + 1;
                int secondPipe = -1;
                for (int k = idStart; k < length - 1; k++)
                {
                    if (inspected[k] != (byte)'|') continue;
                    if (secondPipe != -1)
                        return Rejected("PROPOSED_RECORD_SYNTAX_REJECTED", copied);
                    secondPipe = k;
                }
                if (secondPipe == -1)
                    return Rejected("PROPOSED_RECORD_SYNTAX_REJECTED", copied);
                string id = OriginalItemId(inspected, idStart, secondPipe - idStart);
                if (id == null) return Rejected("PROPOSED_RECORD_SYNTAX_REJECTED", copied);
                int stateStart = secondPipe + 1;
                string token = ReportedState(inspected, stateStart, length - 1 - stateStart);
                if (token == null) return Rejected("PROPOSED_RECORD_SYNTAX_REJECTED", copied);
                return new Dsp004ProposedLocalRecordSyntaxRelation(
                    "GRAMMAR_CONFORMS_ONLY", id, token, null, copied);
            }
            catch (Exception error)
            {
                // Only the real inspection exception is privately retained.
                return new Dsp004ProposedLocalRecordSyntaxRelation(
                    "INSPECTION_FAILED", null, null, error, copied);
            }
        }
    }
}
