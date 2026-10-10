#nullable enable
using System;
using System.Security.Cryptography;

// DSP-004: new, unaccepted source candidate; generation/static review only.
// This batch does not construct the fixture, compute its digest, load, or run it.
// Future invocation requires separately bound preparation authority and a trusted
// host/hash implementation. Neither this source nor any returned value grants it.
// A: 46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C
// P1: D585B3CE407B0D3BEAD2C2D5339E4EC1C66D0E768D2FB87B49F7BD053B50DB9D
// Only D-007's recorded synthetic input and K-003 literal are carried forward.
// No real driver, accepted controller, other DUT, or historical outcome is used.
public sealed class Dsp004IndependentD007PreparationCandidateRev1
{
    private const int SyntheticByteCount = 20177;
    private const string RecordedDriverSha256 =
        "6405563F9A39B39F8E63D4330C497A76C99B38F4FE4662B0A6E310F355B69210";
    private const string HexAlphabet = "0123456789ABCDEF";

    // Private references are not an ownership/freeze/lifetime guarantee. There
    // is deliberately no raw getter, handoff, dispatch, callback, or DUT API.
    private readonly byte[]? heldSyntheticPayload;
    private readonly byte[]? heldSyntheticDigest;
    private readonly Exception? heldPreparationException;

    private Dsp004IndependentD007PreparationCandidateRev1(
        byte[]? payload,
        byte[]? digest,
        Exception? preparationException,
        string preparationRelation,
        string observationCode,
        string? syntheticDigestHex)
    {
        heldSyntheticPayload = payload;
        heldSyntheticDigest = digest;
        heldPreparationException = preparationException;
        PreparationRelation = preparationRelation;
        ObservationCode = observationCode;
        SyntheticDigestHex = syntheticDigestHex;
    }

    // Relation/observation codes describe only this preparation source's future
    // local observations. They are not any of the 189 items' execution states.
    public string PreparationRelation { get; }
    public string ObservationCode { get; }
    public string? SyntheticDigestHex { get; }

    public string DigestQualification => SyntheticDigestHex is null
        ? "NO QUALIFIED SYNTHETIC DIGEST OBSERVATION RECORDED"
        : "SYNTHETIC BYTE DIGEST ONLY; COMPARED WITH RECORDED LITERAL; NOT REAL SOURCE VERIFICATION";

    public string PayloadRetentionQualification => heldSyntheticPayload is null
        ? "NO SYNTHETIC PAYLOAD REFERENCE RECORDED"
        : "PRIVATE REFERENCE ONLY; EXCLUSIVE OWNERSHIP, FREEZE AND LIFETIME NOT ESTABLISHED";

    public string DigestRetentionQualification => heldSyntheticDigest is null
        ? "NO DIGEST REFERENCE RECORDED"
        : "PRIVATE REFERENCE ONLY; IMPLEMENTATION IDENTITY AND TRUST NOT ESTABLISHED";

    public string ExceptionRetentionQualification => heldPreparationException is null
        ? "NO PREPARATION EXCEPTION REFERENCE RECORDED"
        : "PRIVATE ORIGINAL EXCEPTION REFERENCE ONLY; NO PUBLIC EXCEPTION GETTER OR FORMATTING";

    public string Authority => "NOT ESTABLISHED";
    public string SourceAdmission => "NOT ESTABLISHED";
    public string TrustedHostIdentity => "UNBOUND";
    public string HashImplementationIdentity => "UNBOUND";
    public string FrozenHandoff => "NOT IMPLEMENTED";
    public string SamePayloadDutUse => "NOT ESTABLISHED";
    public string DutInvocation => "NOT PERFORMED BY THIS API";
    public string D007ExecutionOutcome => "NOT DETERMINED";
    public string TimingAndOuterStop => "NOT ESTABLISHED";

    // No external input, source path, alternate fixture, target digest, DUT,
    // evaluator or oracle is accepted. This is not an automatic entry point.
    // A caller can invoke a public method; there is no enforced authority gate.
    // Therefore the source must not be loaded/invoked merely because it exists.
    public static Dsp004IndependentD007PreparationCandidateRev1 PrepareD007Only()
    {
        byte[]? payload = null;
        byte[]? digest = null;

        try
        {
            payload = new byte[SyntheticByteCount];
            if (!HasRecordedZeroShape(payload))
            {
                return NotCompleted(payload, null, null,
                    "PRE_DIGEST_PAYLOAD_SHAPE_NOT_CONFIRMED");
            }

            // Standard byte[] SHA256 API, not a DUT-derived calculation.
            // Its availability/provider/assembly identity is not verified here.
            digest = SHA256.HashData(payload);

            // Checks before/after hashing do NOT prove no intervening mutation,
            // absence of shared writes, immutable storage or future same-use.
            if (!HasRecordedZeroShape(payload))
            {
                return NotCompleted(payload, digest, null,
                    "POST_DIGEST_PAYLOAD_SHAPE_NOT_CONFIRMED");
            }

            if (digest is null || digest.GetType() != typeof(byte[]) ||
                digest.Length != 32)
            {
                return NotCompleted(payload, digest, null,
                    "DIGEST_NATIVE_SHAPE_NOT_CONFIRMED");
            }

            string digestHex = EncodeQualifiedDigest(digest);
            string relation = string.Equals(digestHex, RecordedDriverSha256,
                StringComparison.Ordinal)
                ? "EQUAL_TO_RECORDED_LITERAL"
                : "DIFFERENT_FROM_RECORDED_LITERAL";

            // A differing synthetic digest is NOT permission to call the DUT.
            // This object offers no way to pass its privately held input to it.
            return new Dsp004IndependentD007PreparationCandidateRev1(
                payload, digest, null, relation,
                "BOUNDED_SYNTHETIC_DIGEST_RELATION_OBSERVED", digestHex);
        }
        catch (Exception preparationException)
        {
            // No Message, ToString, serialization, rethrow or public export.
            // This is not a guarantee that every fatal failure can be caught,
            // that result allocation succeeds, or that exception lifetime lasts.
            return NotCompleted(payload, digest, preparationException,
                "PREPARATION_EXCEPTION_REFERENCE_RECORDED");
        }
    }

    private static Dsp004IndependentD007PreparationCandidateRev1 NotCompleted(
        byte[]? payload, byte[]? digest, Exception? preparationException,
        string observationCode)
    {
        // A partial or failed digest path never publishes a qualified digest
        // string or an EQUAL/DIFFERENT relation, even if raw bytes were retained.
        return new Dsp004IndependentD007PreparationCandidateRev1(
            payload, digest, preparationException, "NOT_COMPLETED",
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
            if (payload[index] != 0)
            {
                return false;
            }
        }

        return true;
    }

    private static string EncodeQualifiedDigest(byte[] digest)
    {
        // Only called after the exact 32-byte native digest shape check.
        char[] encoded = new char[64];
        for (int index = 0; index < 32; index++)
        {
            encoded[index * 2] = HexAlphabet[digest[index] >> 4];
            encoded[index * 2 + 1] = HexAlphabet[digest[index] & 15];
        }

        return new string(encoded);
    }
}
