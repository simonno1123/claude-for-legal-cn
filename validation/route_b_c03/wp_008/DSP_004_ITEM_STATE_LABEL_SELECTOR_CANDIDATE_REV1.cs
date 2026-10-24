/*
DSP-004 ITEM-STATE LABEL SELECTOR CANDIDATE REV1.

Candidate source only. Materialization and static review do not authorize
compilation, loading, invocation, testing, source admission, actual capture,
integration or deployment. All existing LIMITED qualifications remain.
DSP-004 remains OPEN / HOLD; B-01 and B-02 remain OPEN.
This file is not a live governance ledger or an acceptance decision.

This is a conditional label selector, not a fact or evidence validator.
Before requesting a single label, the caller is responsible for establishing
the same exact item, its original boundary, the relevant facts, and the
applicability of the original item-state definitions. The caller must not
omit currently established same-item labels that affect this selection;
this does not require waiting for future or unrelated material.

The input is an array of already-supported original labels, not raw helper
statuses. The caller must not concurrently change the array during selection.
The caller independently retains original facts, known mismatches and their
bases, first-comparison events, errors, and historical records. This selector
cannot verify those responsibilities or replace those records.

The original definitions are not redefined here. In particular, NOT_MATCH
does not acquire a new normal-complete-return requirement; NOT_RUN requires
all original calls and item-result consumption to be confirmed unattempted.
Actual attempt uncertainty and unknown rule attribution are not equivalent.
No state is inferred from an empty label array.

The finite conflict rule selects INCOMPLETE when the same exact item supports
both NOT_MATCH and INCOMPLETE and a single label is required. It does not
require exactly those two labels. It does not remove known mismatch facts,
establish another priority rule, or decide cleanup attribution. Refusing a
different multi-label selection does not declare that combination illegal.

A controlled refusal means this selector did not select an item-state label.
It is not a fifth item state, a DUT failure, evidence of an attempted call,
or evidence of attempt uncertainty. It must not mechanically become NOT_RUN
or INCOMPLETE, and must not overwrite an existing caller record. If a real
refusal event independently satisfies the original INCOMPLETE definition
within the item's necessary consumption boundary, that remains a caller-side
assessment under the original definition. Unexpected runtime failures are
not caught and relabeled as controlled refusals by this candidate.

The C# parameter boundary does not prove that host binding or automatic
conversion did not occur before entry. Environment compatibility, trusted
loading, capture fidelity, projection, M-item timing and actual execution
remain outside this candidate. It does not call P1, V, R or a DUT; access
files, source bytes, environment data or external services; publish a formal
conclusion; or independently retain or certify evidence.
*/

namespace ClaudeForLegalCn.RouteB.Dsp004.Candidates
{
    public static class Dsp004ItemStateLabelSelectorCandidateRev1
    {
        public static string SelectFinalItemState(
            string[] supportedItemStates,
            bool requiresSingleLabel)
        {
            const string refusalMessage = "No item-state label was selected.";

            if (supportedItemStates == null || supportedItemStates.Length == 0)
            {
                throw new System.InvalidOperationException(refusalMessage);
            }

            bool hasMatch = false;
            bool hasNotMatch = false;
            bool hasNotRun = false;
            bool hasIncomplete = false;
            bool hasInvalidLabel = false;

            // Inspect every element before any label-selection branch.
            // No input element is rewritten, trimmed, coerced or case-folded.
            // Repetition changes neither support nor evidence multiplicity.
            for (int index = 0; index < supportedItemStates.Length; index++)
            {
                string label = supportedItemStates[index];

                if (System.String.Equals(label, "MATCH", System.StringComparison.Ordinal))
                {
                    hasMatch = true;
                }
                else if (System.String.Equals(label, "NOT_MATCH", System.StringComparison.Ordinal))
                {
                    hasNotMatch = true;
                }
                else if (System.String.Equals(label, "NOT_RUN", System.StringComparison.Ordinal))
                {
                    hasNotRun = true;
                }
                else if (System.String.Equals(label, "INCOMPLETE", System.StringComparison.Ordinal))
                {
                    hasIncomplete = true;
                }
                else
                {
                    hasInvalidLabel = true;
                }
            }

            if (hasInvalidLabel || !requiresSingleLabel)
            {
                throw new System.InvalidOperationException(refusalMessage);
            }

            int distinctLabelCount = 0;
            if (hasMatch)
            {
                distinctLabelCount++;
            }
            if (hasNotMatch)
            {
                distinctLabelCount++;
            }
            if (hasNotRun)
            {
                distinctLabelCount++;
            }
            if (hasIncomplete)
            {
                distinctLabelCount++;
            }

            if (distinctLabelCount == 1)
            {
                if (hasMatch)
                {
                    return "MATCH";
                }
                if (hasNotMatch)
                {
                    return "NOT_MATCH";
                }
                if (hasNotRun)
                {
                    return "NOT_RUN";
                }

                // Only hasIncomplete can remain under the count-one guard.
                return "INCOMPLETE";
            }

            // This is a contains-both rule, not an exact-two-members rule.
            if (hasNotMatch && hasIncomplete)
            {
                return "INCOMPLETE";
            }

            // No additional multi-label priority is introduced.
            throw new System.InvalidOperationException(refusalMessage);
        }
    }
}
