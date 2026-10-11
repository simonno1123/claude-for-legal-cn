#nullable enable
using System;
using System.Security.Cryptography;

// DSP-004: new, unaccepted source candidate. Materialization/static review only.
// This batch does not compile, load, prepare a fixture, hash it, or invoke it.
// A: 46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C
// B: 891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB
// P: CFCECB173FB5941958649C7135E77B638BAFF41AAA96074971DE53050BA301B5
// P remains unchanged: no reflection, raw getter, historical-array reuse or
// transfer of its prior digest observations. This source owns a NEW future
// synthetic array if separately authorized to run. Its digest is not a grant.
//
// IMPLEMENTED IN SOURCE: preparation of the recorded synthetic shape; a private
// parameter slot retaining that exact preparation-array reference; local slot
// identity checks; one reservation per returned instance, then refusal.
// NOT IMPLEMENTED: trusted loading, a fixed invocation adapter, actual Payload
// binding, DUT calls, capture/comparison, result publication, timing/outer stop,
// immutable/exclusive ownership, dependency trust or complete resource closure.
// The private slot is NOT a PowerShell command, actual binding or handoff proof.
// No callback, script, path, runspace, permission flag or alternate input is
// accepted. No automatic entry point, public raw-reference getter or enable
// switch exists. Public methods still require separate load/run authority.
public sealed class Dsp004D007ControlledSamePayloadHandoffCandidateRev1
{
    private const int SyntheticByteCount = 20177;
    private const string RecordedDriverSha256 =
        "6405563F9A39B39F8E63D4330C497A76C99B38F4FE4662B0A6E310F355B69210";
    private const string HexAlphabet = "0123456789ABCDEF";

    private readonly byte[]? heldPayload;
    private readonly byte[]? heldDigest;
    private readonly PrivatePayloadSlot? heldSlot;
    private readonly Exception? heldPrimaryException;
    private readonly object requestSync = new object();
    private bool requestReserved;

    private Dsp004D007ControlledSamePayloadHandoffCandidateRev1(
        byte[]? payload,
        byte[]? digest,
        PrivatePayloadSlot? slot,
        Exception? primaryException,
        string relation,
        string observationCode,
        string? digestHex)
    {
        heldPayload = payload;
        heldDigest = digest;
        heldSlot = slot;
        heldPrimaryException = primaryException;
        PreparationRelation = relation;
        ObservationCode = observationCode;
        SyntheticDigestHex = digestHex;
    }

    // Read-only metadata is neither authority nor an externally verified fact.
    public string PreparationRelation { get; }
    public string ObservationCode { get; }
    public string? SyntheticDigestHex { get; }
    public string FixedTargetName => "Test-DSP004DriverBytesInMemory";
    public string FixedParameterName => "Payload";
    public string RecordedParameterSignature => "SINGLE OBJECT PARAMETER; BYTE ARRAY VALUE REQUIRED";
    public string ParameterSlotQualification => string.Equals(PreparationRelation,
        "DIFFERENT_FROM_RECORDED_LITERAL", StringComparison.Ordinal) &&
        SyntheticDigestHex is not null && heldPayload is not null &&
        heldSlot is not null && heldSlot.HasSameReference(heldPayload)
        ? "INTERNAL PREPARATION-TO-SLOT REFERENCE ONLY; ACTUAL ARGUMENT BINDING NOT OBSERVED"
        : "NO QUALIFIED INTERNAL PARAMETER SLOT RECORDED";
    public string PayloadRetentionQualification => heldPayload is null
        ? "NO SYNTHETIC PAYLOAD REFERENCE RECORDED"
        : "PRIVATE REFERENCE ONLY; EXCLUSIVE OWNERSHIP, FREEZE AND LIFETIME NOT ESTABLISHED";
    public string DigestRetentionQualification => heldDigest is null
        ? "NO DIGEST REFERENCE RECORDED"
        : "PRIVATE REFERENCE ONLY; IMPLEMENTATION IDENTITY AND TRUST NOT ESTABLISHED";
    public string ExceptionRetentionQualification => heldPrimaryException is null
        ? "NO PREPARATION EXCEPTION REFERENCE RECORDED"
        : "PRIVATE ORIGINAL EXCEPTION REFERENCE ONLY; RETENTION LIFETIME NOT GUARANTEED";
    public string DigestQualification => SyntheticDigestHex is null
        ? "NO QUALIFIED SYNTHETIC DIGEST OBSERVATION RECORDED"
        : "SYNTHETIC BYTE DIGEST ONLY; RECORDED LITERAL COMPARISON; NOT REAL SOURCE VERIFICATION";
    public string Authority => "NOT ESTABLISHED";
    public string SourceAdmission => "NOT ESTABLISHED";
    public string TrustedLoadIdentity => "UNBOUND";
    public string HashImplementationIdentity => "UNBOUND";
    public string FixedInvocationAdapter => "NOT IMPLEMENTED";
    public string ActualParameterIdentity => "NOT OBSERVED";
    public string FrozenHandoff => "NOT IMPLEMENTED";
    public string SamePayloadDutUse => "NOT ESTABLISHED";
    public string DutInvocation => "NOT PERFORMED BY THIS API";
    public string D007ItemOutcome => "NOT DETERMINED BY THIS API";
    public string TimingAndOuterStop => "NOT ESTABLISHED";
    public string PrivateFailureRetentionQualification =>
        "NO EXCEPTION GETTER OR FORMATTING; FAILURE RETENTION LIMITED";

    // Future preparation only. No external array, target, digest, provider,
    // function/delegate, script, permission assertion or execution evidence is
    // accepted. A slot is local bookkeeping, not actual function binding.
    public static Dsp004D007ControlledSamePayloadHandoffCandidateRev1
        PrepareD007ParameterSlotOnly()
    {
        byte[]? payload = null;
        byte[]? digest = null;
        PrivatePayloadSlot? slot = null;

        try
        {
            payload = new byte[SyntheticByteCount];
            if (!HasRecordedZeroShape(payload))
            {
                return NotCompleted(payload, null, null, null,
                    "PRE_DIGEST_PAYLOAD_SHAPE_NOT_CONFIRMED");
            }

            digest = SHA256.HashData(payload);
            if (!HasRecordedZeroShape(payload))
            {
                return NotCompleted(payload, digest, null, null,
                    "POST_DIGEST_PAYLOAD_SHAPE_NOT_CONFIRMED");
            }

            if (digest is null || digest.GetType() != typeof(byte[]) ||
                digest.Length != 32)
            {
                return NotCompleted(payload, digest, null, null,
                    "DIGEST_NATIVE_SHAPE_NOT_CONFIRMED");
            }

            string digestHex = EncodeQualifiedDigest(digest);
            if (string.Equals(digestHex, RecordedDriverSha256,
                    StringComparison.Ordinal))
            {
                // Equal is a preparation relation, not a DUT match/outcome.
                // No slot is created; this source still cannot call any DUT.
                return new Dsp004D007ControlledSamePayloadHandoffCandidateRev1(
                    payload, digest, null, null, "EQUAL_TO_RECORDED_LITERAL",
                    "SLOT_NOT_CREATED_EQUAL_RELATION", digestHex);
            }

            slot = new PrivatePayloadSlot(payload);
            if (!slot.HasSameReference(payload) || !HasRecordedZeroShape(payload))
            {
                return NotCompleted(payload, digest, slot, null,
                    "INTERNAL_SLOT_REFERENCE_OR_SHAPE_NOT_CONFIRMED");
            }

            // Exactly the array hashed above is retained in the private slot.
            // This does NOT prove no intervening/native mutation, immutable
            // storage, actual PowerShell binding or any future DUT consumption.
            return new Dsp004D007ControlledSamePayloadHandoffCandidateRev1(
                payload, digest, slot, null, "DIFFERENT_FROM_RECORDED_LITERAL",
                "INTERNAL_SLOT_REFERENCE_RECORDED_ONLY", digestHex);
        }
        catch (Exception primaryException)
        {
            // Keep the actual origin-process object only. No Message, ToString,
            // stack, serialization, artificial recreation, rethrow or export.
            // Fatal faults/result allocation failure can prevent any result.
            return NotCompleted(payload, digest, slot, primaryException,
                "PREPARATION_EXCEPTION_REFERENCE_RECORDED");
        }
    }

    // This request is per-instance bookkeeping followed by refusal. It never
    // reads the payload, resolves a function, binds an argument or attempts DUT
    // result consumption. The reservation is NOT evidence a DUT was attempted.
    // Even qualified preparation cannot open a dispatch path. A future live
    // adapter requires a separately authorized new candidate, not a bool/flag.
    // Monitor waiting and record allocation may block/fail. This method does
    // not catch/retain every request failure or prove silent/bounded invocation.
    // The factory can create another owner. This is NOT a batch-wide attempt
    // latch, stop coordinator or proof that external retries cannot occur.
    public FixedHandoffRequestRecord RequestFixedD007Handoff()
    {
        lock (requestSync)
        {
            if (requestReserved)
            {
                return new FixedHandoffRequestRecord("REPEATED_REQUEST_REFUSED");
            }

            requestReserved = true;
            return new FixedHandoffRequestRecord("FIRST_REQUEST_REFUSED_UNBOUND");
        }
    }

    private static Dsp004D007ControlledSamePayloadHandoffCandidateRev1 NotCompleted(
        byte[]? payload,
        byte[]? digest,
        PrivatePayloadSlot? slot,
        Exception? primaryException,
        string observationCode)
    {
        // Partial references are never promoted to a qualified preparation
        // digest or invocation permission. An allocated slot alone is no proof.
        return new Dsp004D007ControlledSamePayloadHandoffCandidateRev1(
            payload, digest, slot, primaryException, "NOT_COMPLETED",
            observationCode, null);
    }

    private static bool HasRecordedZeroShape(byte[] payload)
    {
        if (payload.GetType() != typeof(byte[]) ||
            payload.Length != SyntheticByteCount)
        {
            return false;
        }

        for (int index = 0; index < SyntheticByteCount; index++)
        {
            if (payload[index] != 0) { return false; }
        }

        return true;
    }

    private static string EncodeQualifiedDigest(byte[] digest)
    {
        char[] encoded = new char[64];
        for (int index = 0; index < 32; index++)
        {
            encoded[index * 2] = HexAlphabet[digest[index] >> 4];
            encoded[index * 2 + 1] = HexAlphabet[digest[index] & 15];
        }

        return new string(encoded);
    }

    // Not a PowerShell parameter/command object. No raw getter or public slot
    // exists. This is not an ownership or trans-process identity certificate.
    private sealed class PrivatePayloadSlot
    {
        private readonly byte[] value;
        internal PrivatePayloadSlot(byte[] value) { this.value = value; }
        internal bool HasSameReference(byte[] expected) =>
            object.ReferenceEquals(value, expected);
    }

    public sealed class FixedHandoffRequestRecord
    {
        internal FixedHandoffRequestRecord(string requestCode)
        {
            RequestCode = requestCode;
        }

        public string RequestCode { get; }
        public string ReservationQualification => "PER-INSTANCE LOCAL REQUEST ONLY; NOT A DUT ATTEMPT RECORD";
        public string Disposition => "UNCONDITIONALLY REFUSED; NO FIXED INVOCATION ADAPTER";
        public string LocalAttemptQualification =>
            "THIS API HAS NOT ATTEMPTED DUT CALL OR DUT RESULT CONSUMPTION";
        public string ItemOutcome => "NOT DETERMINED; EXTERNAL ATTEMPT EVIDENCE NOT INSPECTED";
        public string ResourceSettlement => "NOT OBSERVED; NO LIVE DUT RESOURCES CREATED BY THIS API";
        public string Authority => "NOT ESTABLISHED";
    }
}
