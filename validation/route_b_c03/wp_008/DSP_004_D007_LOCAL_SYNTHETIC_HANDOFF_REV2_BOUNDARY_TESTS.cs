#nullable enable
// NEW fixed local synthetic tests, compiled with the exact REV2 snapshot.
// No process, filesystem, clock injection, reflection of private members,
// authority switch, source admission, raw DUT fixture or implementation grant.
// Artificial elapsed samples test the shared decision logic ONLY. They do not
// prove real 120-second timeout, hard stop, cleanup or descendant settlement.
public sealed class Dsp004D007LocalSyntheticHandoffRev2BoundaryTests
{
    private Dsp004D007LocalSyntheticHandoffRev2BoundaryTests() { }

    public static BoundaryCheck[] RunPureBoundaryChecks()
    {
        var checks = new System.Collections.Generic.List<BoundaryCheck>();
        CheckProgress(checks, "D-01", -1, false, "DEADLINE_REFUSED");
        CheckProgress(checks, "D-02", -1, true, "DEADLINE_REFUSED");
        CheckProgress(checks, "D-03", 0, false, "CONTINUE_NOT_COMPLETE");
        CheckProgress(checks, "D-04", 0, true, "COMPLETE_IN_TIME");
        CheckProgress(checks, "D-05", 119999, false, "CONTINUE_NOT_COMPLETE");
        CheckProgress(checks, "D-06", 119999, true, "COMPLETE_IN_TIME");
        CheckProgress(checks, "D-07", 120000, false, "DEADLINE_REFUSED");
        CheckProgress(checks, "D-08", 120000, true, "DEADLINE_REFUSED");
        CheckProgress(checks, "D-09", 120001, false, "DEADLINE_REFUSED");
        CheckProgress(checks, "D-10", 120001, true, "DEADLINE_REFUSED");
        CheckProgress(checks, "D-11", long.MaxValue, false, "DEADLINE_REFUSED");
        CheckProgress(checks, "D-12", long.MaxValue, true, "DEADLINE_REFUSED");

        const string marker = "DSP004-SNAPSHOT-ACK-V2\n";
        const string body = "{\"synthetic\":true}\n";
        CheckAck(checks, "A-01", System.Array.Empty<byte>(), false, null);
        CheckAck(checks, "A-02", System.Text.Encoding.UTF8.GetBytes(body), false, null);
        CheckAck(checks, "A-03", System.Text.Encoding.UTF8.GetBytes(marker), false, null);
        CheckAck(checks, "A-04", System.Text.Encoding.UTF8.GetBytes("DSP004-SNAPSHOT-ACK-V" + body), false, null);
        CheckAck(checks, "A-05", System.Text.Encoding.UTF8.GetBytes("DSP004-SNAPSHOT-ACK-V1\n" + body), false, null);
        CheckAck(checks, "A-06", System.Text.Encoding.UTF8.GetBytes(marker + body), true, body);
        CheckAck(checks, "A-07", System.Text.Encoding.UTF8.GetBytes(marker + " \t\r\n"), false, null);
        CheckAck(checks, "A-08", System.Text.Encoding.UTF8.GetBytes("x" + marker + body), false, null);
        CheckAck(checks, "A-09", System.Text.Encoding.UTF8.GetBytes("DSP004-SNAPSHOT-ACK-V2\r\n" + body), false, null);
        byte[] invalid = new byte[marker.Length + 1];
        System.Buffer.BlockCopy(System.Text.Encoding.ASCII.GetBytes(marker), 0, invalid, 0, marker.Length);
        invalid[marker.Length] = 255;
        string invalidOutcome;
        try
        {
            string? ignored;
            Dsp004D007LocalSyntheticHandoffSupervisorRev2.TryReadAcknowledgedBody(invalid, out ignored);
            invalidOutcome = "NO_EXPECTED_EXCEPTION";
        }
        catch (System.Text.DecoderFallbackException) { invalidOutcome = "STRICT_UTF8_REFUSED"; }
        checks.Add(new BoundaryCheck("A-10", "PURE_SYNTHETIC_ACK_DECODING", "STRICT_UTF8_REFUSED", invalidOutcome));

        checks.Add(new BoundaryCheck("Q-01", "PURE_SYNTHETIC_QUALIFICATION",
            "NO QUALIFIED CHILD SNAPSHOT ACK OBSERVATION",
            Dsp004D007LocalSyntheticHandoffSupervisorRev2.QualifySnapshotAck(false)));
        checks.Add(new BoundaryCheck("Q-02", "PURE_SYNTHETIC_QUALIFICATION",
            "FIXED BOOTSTRAP SNAPSHOT ACK OBSERVED; NOT TRUSTED ROOT OR AUTHORITY",
            Dsp004D007LocalSyntheticHandoffSupervisorRev2.QualifySnapshotAck(true)));
        return checks.ToArray();
    }

    private static void CheckProgress(System.Collections.Generic.List<BoundaryCheck> checks,
        string id, long elapsed, bool ready, string expected)
    {
        string observed = Dsp004D007LocalSyntheticHandoffSupervisorRev2.ClassifyProgress(elapsed, ready);
        checks.Add(new BoundaryCheck(id, "PURE_SYNTHETIC_DEADLINE_DECISION", expected, observed));
    }

    private static void CheckAck(System.Collections.Generic.List<BoundaryCheck> checks,
        string id, byte[] input, bool expectedAck, string? expectedBody)
    {
        string? observedBody;
        bool observedAck = Dsp004D007LocalSyntheticHandoffSupervisorRev2.TryReadAcknowledgedBody(input, out observedBody);
        bool exact = observedAck == expectedAck && string.Equals(observedBody, expectedBody, System.StringComparison.Ordinal);
        checks.Add(new BoundaryCheck(id, "PURE_SYNTHETIC_ACK_FRAMING",
            "EXACT_ACK_AND_BODY_EXPECTATION", exact ? "EXACT_ACK_AND_BODY_EXPECTATION" : "ACK_OR_BODY_MISMATCH"));
    }

    public sealed class BoundaryCheck
    {
        internal BoundaryCheck(string id, string kind, string expected, string observed)
        { Id = id; Kind = kind; Expected = expected; Observed = observed; }
        public string Id { get; }
        public string Kind { get; }
        public string Expected { get; }
        public string Observed { get; }
        public bool Passed => string.Equals(Expected, Observed, System.StringComparison.Ordinal);
    }
}
