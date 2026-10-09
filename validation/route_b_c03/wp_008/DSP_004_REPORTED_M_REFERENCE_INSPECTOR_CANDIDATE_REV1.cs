// DSP-004 M reference-inspection SOURCE CANDIDATE ONLY. Not compiled,
// loaded, called, accepted or integrated. No entry point, loader or DUT call.
// Recorded catalog binding:
// 4BAED6E284C92A2403117C72CFBF419BD2B6FB478A55697CA2229201C8FB149E
// Recorded P1 candidate binding (not Owner accepted):
// D585B3CE407B0D3BEAD2C2D5339E4EC1C66D0E768D2FB87B49F7BD053B50DB9D
// Recorded separate value-comparer candidate binding (not Owner accepted):
// A48B1C45A6CD3EC5999FE183730AB727BC0C90F29E6957F97459CB2440F22F83
// Literal hashes do not authenticate any supplied live object or assembly.
//
// READ-ONLY: accepts two caller-supplied object[] projections. Does not call
// the value comparer, compare values with an oracle, capture output, mutate
// inputs, perform two DUT calls or prove first -> mutation -> second order.
// Hashtable input is only enumerated. No setter / key lookup / custom comparer
// is invoked. An actual mutation path and its trusted provenance remain UNBOUND.
//
// M-004 checks ONLY the two first Hashtable target references. It does not
// require all eight records to have fresh identities. M-005 expressly imposes
// no new String identity or getter-returned-array identity requirement.
// M-006 observes visible mutable reference sites: supplied output array,
// PSObject wrapper, 27 exact visible instance NoteProperties, CaseContract
// array plus eight Hashtable records, StatusCombinations and OuterReasons
// arrays. At most 40 sites per supplied projection; sites need not be unique.
// P1's explicit wrapper/collection/same-index Hashtable pairs are reported
// separately. OuterReasons, caller output container, 27x27 NoteProperty and
// 8x8 Hashtable cross-group observations are separate supplemental fields.
// No supplemental distinctness becomes a new M pass/fail criterion. No P1
// assertion is rewritten and no earlier review result is transferred.
// ImmediateBaseObject is checked for native PSCustomObject type, NOT tested
// for fresh identity (an engine representation is not the mutable wrapper).
// Immutable String values and boxed Int32 identities are NEVER compared.
//
// Reference relations are NOT value matches, item states, complete fresh-copy
// proof, execution permission or aggregate results. Missing/uninspectable
// shapes are not ordinary value mismatches. Two cached/fabricated projections
// can satisfy this API; actual call origin, time/order and private ownership
// MUST be established separately, BEFORE invocation or mutation.
//
// Exact CLR types, ordinal names, native arrays and dictionary enumeration;
// all visible member metadata checked before NoteProperty.Value access.
// No ScriptProperty, CodeProperty, AliasProperty, adapted property, subclass,
// formatting, JSON, conversion, unknown Equals/GetHashCode/ToString or callback.
// PSObject.Properties is only a VISIBLE integrating view. Hidden metadata,
// framework-internal allocation, host/assembly/TypeTable/adapters and concurrent
// mutation remain LIMITED / UNBOUND. Local finite loops are not total resource
// or timing guarantees. A privately retained inspection exception is not proof
// of complete exception lifetime, process survival or resource settlement.
//
// ALL upstream LIMITED retained. D-007 UNBOUND / NOT_RUN; real driver positive
// SHA branch NOT COVERED. 120/5/5 are design proposals. DSP-004 OPEN / HOLD;
// B-01 and B-02 OPEN. No source admission, actual capture, tests or integration.
// No file/process/network/provider/ACOS/other-project action.

using System;
using System.Collections;
using System.Management.Automation;

namespace ClaudeForLegalCn.Dsp004.Candidates
{
    public sealed class Dsp004ReportedMReferenceRelation
    {
        public string ReferenceRelation { get; }
        public string Qualification { get; }
        public string Scope { get; }
        public string P1ExplicitReferenceRelation { get; }
        public string SupplementalOuterReasonsRelation { get; }
        public string SupplementalCallerContainerRelation { get; }
        public string SupplementalNotePropertyRelation { get; }
        public string SupplementalAllPairsHashtableRelation { get; }
        public string FirstAndSecondValueMatches { get; }
        public string FirstCopyMutation { get; }
        public string ActualCallSequence { get; }
        public string FullCaptureEvidence { get; }
        public string HiddenMutableState { get; }
        public string Authority { get; }

        private readonly Exception retainedInspectionException;

        internal Dsp004ReportedMReferenceRelation(string relation, string scope, Exception error,
            string p1 = "NOT INSPECTED", string reasons = "NOT REQUESTED",
            string container = "NOT REQUESTED", string notes = "NOT REQUESTED",
            string allCasePairs = "NOT REQUESTED")
        {
            ReferenceRelation = relation;
            Qualification = "CALLER-SUPPLIED REFERENCE PROJECTIONS ONLY - NOT AUTHENTICATED";
            Scope = scope;
            P1ExplicitReferenceRelation = p1;
            SupplementalOuterReasonsRelation = reasons;
            SupplementalCallerContainerRelation = container;
            SupplementalNotePropertyRelation = notes;
            SupplementalAllPairsHashtableRelation = allCasePairs;
            FirstAndSecondValueMatches = "NOT ESTABLISHED";
            FirstCopyMutation = "NOT PERFORMED BY THIS API / NOT ESTABLISHED";
            ActualCallSequence = "NOT ESTABLISHED";
            FullCaptureEvidence = "NOT ESTABLISHED";
            HiddenMutableState = "NOT ATTESTED";
            Authority = "NOT ESTABLISHED";
            retainedInspectionException = error;
        }
    }

    public static class Dsp004ReportedMReferenceInspectorCandidateRev1
    {
        private const int MaxReferenceSites = 40;
        private const int MaxTextCharacters = 512;

        private sealed class ReferenceSites
        {
            internal readonly object[] Items = new object[MaxReferenceSites];
            internal int Count;
            internal object FirstCaseTarget;
            internal object CallerContainer;
            internal object Wrapper;
            internal object CaseCollection;
            internal object StatusCollection;
            internal object ReasonsCollection;
            internal readonly object[] CaseTables = new object[8];
            internal readonly object[] Notes = new object[27];

            internal bool Add(object value)
            {
                if (value == null || Count == Items.Length) return false;
                Items[Count++] = value;
                return true;
            }
        }

        private static string[] FixedNames()
        {
            return new[] {
                "CandidateQualification", "DriverPath", "DriverSha256", "DriverBodyBytes",
                "DriverInputCeiling", "DriverTailDetectionBytes", "CallerPath", "CallerSha256",
                "ReaderPath", "ReaderSha256", "BaselinePath", "BaselineSha256", "StdoutBodyBudget",
                "StdoutDetectionBudget", "StderrBodyBudget", "StderrDetectionBudget",
                "WholeCaseDeadlineSeconds", "StopConfirmationMaximumSeconds", "FrameMarker",
                "CaseContract", "StatusCombinations", "OuterReasons", "AuthorityChannel",
                "ControllerFullShaBinding", "BootstrapTextEncodingAndShaBinding", "LiveAdapters",
                "CaseCompletion" };
        }

        private static bool Text(object value)
        {
            return value != null && value.GetType() == typeof(string)
                && ((string)value).Length <= MaxTextCharacters;
        }

        private static int NameIndex(string[] names, string supplied)
        {
            for (int k = 0; k < names.Length; k++)
                if (string.Equals(names[k], supplied, StringComparison.Ordinal)) return k;
            return -1;
        }

        private static bool CaseRecord(object value, ReferenceSites sites)
        {
            if (value == null || value.GetType() != typeof(Hashtable)) return false;
            Hashtable record = (Hashtable)value;
            if (record.Count != 3 || !sites.Add(record)) return false;
            string[] names = { "CaseId", "Level", "Observation" };
            bool[] seen = new bool[3];
            IDictionaryEnumerator it = record.GetEnumerator();
            int visited = 0;
            while (it.MoveNext())
            {
                if (++visited > 3) return false;
                object rawKey = it.Key;
                if (!Text(rawKey)) return false;
                int at = NameIndex(names, (string)rawKey);
                if (at < 0 || seen[at] || !Text(it.Value)) return false;
                seen[at] = true;
            }
            return visited == 3 && seen[0] && seen[1] && seen[2];
        }

        private static bool Cases(object value, ReferenceSites sites, bool addCollection)
        {
            if (value == null || value.GetType() != typeof(object[])) return false;
            object[] items = (object[])value;
            if (items.Length != 8 || (addCollection && !sites.Add(items))) return false;
            for (int k = 0; k < 8; k++)
            {
                if (!CaseRecord(items[k], sites)) return false;
                sites.CaseTables[k] = items[k];
                if (k == 0) sites.FirstCaseTarget = items[k];
            }
            return true;
        }

        private static bool Strings(object value, int count, ReferenceSites sites, bool addCollection)
        {
            if (value == null) return false;
            Type kind = value.GetType();
            if (kind != typeof(object[]) && kind != typeof(string[])) return false;
            Array items = (Array)value;
            if (items.Length != count || (addCollection && !sites.Add(items))) return false;
            for (int k = 0; k < count; k++) if (!Text(items.GetValue(k))) return false;
            return true;
        }

        private static bool IntegerField(int at)
        {
            return at == 3 || at == 4 || at == 5 || (at >= 12 && at <= 17);
        }

        private static bool FixedRecord(object value, ReferenceSites sites)
        {
            if (value == null || value.GetType() != typeof(PSObject)) return false;
            PSObject wrapper = (PSObject)value;
            object immediate = wrapper.ImmediateBaseObject;
            if (immediate == null || immediate.GetType() != typeof(PSCustomObject)
                || !sites.Add(wrapper)) return false;
            sites.Wrapper = wrapper;
            string[] names = FixedNames();
            PSNoteProperty[] notes = new PSNoteProperty[27];
            bool[] seen = new bool[27];
            int visited = 0;
            // Framework integration/allocation and hidden members are not
            // bounded or attested by this public visible-member loop.
            foreach (PSPropertyInfo property in wrapper.Properties)
            {
                if (property == null || property.GetType() != typeof(PSNoteProperty)) return false;
                PSNoteProperty note = (PSNoteProperty)property;
                if (!note.IsInstance || note.MemberType != PSMemberTypes.NoteProperty) return false;
                if (++visited > 27 || note.Name == null || note.Name.Length > 64) return false;
                int at = NameIndex(names, note.Name);
                if (at < 0 || seen[at]) return false;
                seen[at] = true;
                notes[at] = note;
            }
            if (visited != 27) return false;
            for (int k = 0; k < 27; k++)
            {
                if (!seen[k] || !sites.Add(notes[k])) return false;
                sites.Notes[k] = notes[k];
            }
            // All visible metadata has been accepted before any Value read.
            for (int k = 0; k < 27; k++)
            {
                object heldValue = notes[k].Value;
                if (k == 19)
                {
                    if (!Cases(heldValue, sites, true)) return false;
                    sites.CaseCollection = heldValue;
                }
                else if (k == 20)
                {
                    if (!Strings(heldValue, 26, sites, true)) return false;
                    sites.StatusCollection = heldValue;
                }
                else if (k == 21)
                {
                    if (!Strings(heldValue, 6, sites, true)) return false;
                    sites.ReasonsCollection = heldValue;
                }
                else if (IntegerField(k))
                {
                    if (heldValue == null || heldValue.GetType() != typeof(int)) return false;
                }
                else if (!Text(heldValue)) return false;
            }
            return true;
        }

        private static bool Projection(object value, int mode, out ReferenceSites sites)
        {
            sites = null;
            if (value == null || value.GetType() != typeof(object[])) return false;
            object[] items = (object[])value;
            int count = mode == 4 ? 8 : mode == 5 ? 26 : 1;
            if (items.Length != count) return false;
            ReferenceSites held = new ReferenceSites();
            if (!held.Add(items)) return false;
            held.CallerContainer = items;
            bool checkedShape = mode == 4 ? Cases(items, held, false)
                : mode == 5 ? Strings(items, 26, held, false) : FixedRecord(items[0], held);
            if (!checkedShape) return false;
            sites = held;
            return true;
        }

        private static bool P1FixedPairsShared(ReferenceSites first, ReferenceSites second)
        {
            if (object.ReferenceEquals(first.Wrapper, second.Wrapper)
                || object.ReferenceEquals(first.CaseCollection, second.CaseCollection)
                || object.ReferenceEquals(first.StatusCollection, second.StatusCollection)) return true;
            for (int k = 0; k < 8; k++)
                if (object.ReferenceEquals(first.CaseTables[k], second.CaseTables[k])) return true;
            return false;
        }

        private static bool AnyCrossPairShared(object[] first, object[] second)
        {
            // Arrays here are private fixed-sized reference-site holders.
            // No value-type or immutable String identity is tested.
            for (int left = 0; left < first.Length; left++)
                for (int right = 0; right < second.Length; right++)
                    if (object.ReferenceEquals(first[left], second[right])) return true;
            return false;
        }

        public static Dsp004ReportedMReferenceRelation CompareReferences(object itemId,
            object firstCallerSuppliedProjection, object secondCallerSuppliedProjection)
        {
            string scope = "UNBOUND";
            try
            {
                if (itemId == null || itemId.GetType() != typeof(string))
                    return new Dsp004ReportedMReferenceRelation("REFERENCE_PROJECTION_NOT_COMPARABLE", scope, null);
                string id = (string)itemId;
                int mode = string.Equals(id, "M-004", StringComparison.Ordinal) ? 4
                    : string.Equals(id, "M-005", StringComparison.Ordinal) ? 5
                    : string.Equals(id, "M-006", StringComparison.Ordinal) ? 6 : 0;
                if (mode == 0)
                    return new Dsp004ReportedMReferenceRelation("REFERENCE_PROJECTION_NOT_COMPARABLE", scope, null);
                scope = mode == 4 ? "FIRST TARGET HASHTABLE ONLY"
                    : mode == 5 ? "NO STRING OR GETTER-RETURNED-ARRAY FRESH-IDENTITY REQUIREMENT"
                    : "P1 EXPLICIT AND SEPARATE SUPPLEMENTAL VISIBLE RELATIONS - NO HIDDEN-STATE PROOF";
                ReferenceSites first;
                ReferenceSites second;
                if (!Projection(firstCallerSuppliedProjection, mode, out first)
                    || !Projection(secondCallerSuppliedProjection, mode, out second))
                    return new Dsp004ReportedMReferenceRelation("REFERENCE_PROJECTION_NOT_COMPARABLE", scope, null);
                if (mode == 4)
                {
                    string relation = object.ReferenceEquals(first.FirstCaseTarget, second.FirstCaseTarget)
                        ? "FIRST_TARGET_SHARED" : "FIRST_TARGET_DISTINCT";
                    return new Dsp004ReportedMReferenceRelation(
                        relation, scope, null, relation);
                }
                if (mode == 5)
                    return new Dsp004ReportedMReferenceRelation("STRING_IDENTITY_NOT_REQUIRED", scope, null,
                        "NO IDENTITY ASSERTION IN P1");
                string p1 = P1FixedPairsShared(first, second) ? "P1_LISTED_REFERENCE_SHARED" : "P1_LISTED_REFERENCES_DISTINCT";
                string reasons = object.ReferenceEquals(first.ReasonsCollection, second.ReasonsCollection)
                    ? "OUTER_REASONS_SHARED" : "OUTER_REASONS_DISTINCT";
                string container = object.ReferenceEquals(first.CallerContainer, second.CallerContainer)
                    ? "CALLER_CONTAINER_SHARED" : "CALLER_CONTAINERS_DISTINCT";
                string notes = AnyCrossPairShared(first.Notes, second.Notes)
                    ? "CROSS_GROUP_NOTE_PROPERTY_SHARED" : "CROSS_GROUP_NOTE_PROPERTIES_DISTINCT";
                string allCases = AnyCrossPairShared(first.CaseTables, second.CaseTables)
                    ? "CROSS_GROUP_HASHTABLE_SHARED" : "CROSS_GROUP_HASHTABLES_DISTINCT";
                // No combined PASS / FAIL, ordinary value comparison or new
                // mandatory M criterion is derived from these observations.
                return new Dsp004ReportedMReferenceRelation("SEPARATE_REFERENCE_OBSERVATIONS", scope, null,
                    p1, reasons, container, notes, allCases);
            }
            catch (Exception error)
            {
                return new Dsp004ReportedMReferenceRelation("INSPECTION_FAILED", scope, error);
            }
        }
    }
}
