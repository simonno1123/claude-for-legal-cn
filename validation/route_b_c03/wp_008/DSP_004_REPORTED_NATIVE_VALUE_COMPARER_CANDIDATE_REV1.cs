// DSP-004 P2 comparison-core SOURCE CANDIDATE ONLY. Not compiled, loaded,
// invoked, accepted or integrated. No entry point, loader, DUT call or grant.
// Controller recorded binding:
// 891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB
// Independent input/oracle candidate recorded binding (not yet accepted):
// D585B3CE407B0D3BEAD2C2D5339E4EC1C66D0E768D2FB87B49F7BD053B50DB9D
// Catalog recorded binding:
// 4BAED6E284C92A2403117C72CFBF419BD2B6FB478A55697CA2229201C8FB149E
// Literal identities do not authenticate the live objects supplied to Compare.
//
// This core compares a CALLER-SUPPLIED native object[] projection against a
// separately owned data oracle. It does NOT capture PowerShell output, unwrap
// pipeline PSObject scalars, authenticate provenance, establish completion,
// issue the four item states, or commit/publish any observation.
// An empty supplied array, one null slot, and null field values are distinct
// represented inputs, NOT proof a real capturer preserved those distinctions.
//
// Direct CLR type checks and ordinal strings avoid PowerShell ETS method
// dispatch, conversion hooks, object.Equals, formatting, JSON and ToString.
// Dictionaries are exact Hashtable / OrderedDictionary only; their keys are
// enumerated rather than searched through caller-provided equality comparers.
// Custom records require exact PSObject and exact immediate PSCustomObject.
// ALL visible property metadata is checked BEFORE any property Value is read.
// Only exact, instance PSNoteProperty is accepted: no subclass, ScriptProperty,
// CodeProperty, AliasProperty, adapted property or type-data note is read.
// Public PSObject.Properties is a VISIBLE integrating view. Hidden metadata
// and framework-internal enumeration/allocation are NOT bounded or attested by
// this core. These remain explicit LIMITED, not an all-members safety proof.
// Host/assembly identity, TypeTable/adapters, private ownership, early-output
// closure and outside resource supervision must be bound BEFORE invocation.
//
// Local loops/tree shapes are finite; name/string and collection limits are
// source-level inspection limits, not measured time/memory guarantees. Objects
// must be exclusively owned: snapshotting/copying does not defeat concurrent
// mutation, prove freezing or authenticate the independent oracle.
// M-004/005/006 compare one call at a time. The first-check/mutation/second-call
// sequence and mutable-reference freshness assertions are NOT implemented here.
// A private exception reference is retained in the result on inspection error;
// there is no public exception/message/trace accessor. Lifetime, process loss,
// primary-plus-cleanup exception handling and real resource settlement remain
// UNBOUND. The caller must privately retain the result; no retention is proven.
//
// EQUAL / DIFFERENT / *_NOT_COMPARABLE / INSPECTION_FAILED are internal VALUE
// RELATIONS, NOT a fifth item state, execution permission or aggregate verdict.
// ALL upstream LIMITED remain. D-007 UNBOUND / NOT_RUN; positive driver SHA
// NOT COVERED. 120/5/5 budgets are design proposals only. DSP-004 OPEN / HOLD;
// B-01 and B-02 OPEN. No source admission, actual capture, tests or integration.
// No file/process/network/provider/ACOS/other-project operation is present.
//
// Public API references (not local SDK/assembly verification):
// https://learn.microsoft.com/en-us/dotnet/api/system.management.automation.psnoteproperty
// https://learn.microsoft.com/en-us/dotnet/api/system.management.automation.psobject.properties
// https://learn.microsoft.com/en-us/dotnet/api/system.management.automation.psobject.immediatebaseobject

using System;
using System.Collections;
using System.Collections.Specialized;
using System.Management.Automation;

namespace ClaudeForLegalCn.Dsp004.Candidates
{
    public sealed class Dsp004ReportedValueComparison
    {
        public string ValueRelation { get; }
        public string Qualification { get; }
        public string FullCaptureEvidence { get; }
        public string Authority { get; }
        public string RecordView { get; }
        public string MSequenceAndFreshness { get; }

        // Intentionally private and never formatted or exported by this API.
        private readonly Exception retainedInspectionException;

        internal Dsp004ReportedValueComparison(string relation, Exception error)
        {
            ValueRelation = relation;
            Qualification = "CALLER-SUPPLIED NATIVE VALUE PROJECTION ONLY - NOT AUTHENTICATED";
            FullCaptureEvidence = "NOT ESTABLISHED";
            Authority = "NOT ESTABLISHED";
            RecordView = "VISIBLE PSOBJECT PROPERTIES ONLY - HIDDEN METADATA NOT ATTESTED";
            MSequenceAndFreshness = "NOT ESTABLISHED";
            retainedInspectionException = error;
        }
    }

    public static class Dsp004ReportedNativeValueComparerCandidateRev1
    {
        private const int MaxNameCharacters = 64;
        private const int MaxValueCharacters = 512;

        private enum Shape
        {
            Text, Boolean, Int32, NullableInt32,
            Cases, Tuples, Reasons, CaseRecord, FixedRecord,
            DriverRecord, FrameRecord, ReadRecord, WriteRecord
        }

        private enum Inspection { Ok, Different, Uninspectable }

        private sealed class Field
        {
            internal readonly string Name;
            internal readonly Shape Kind;
            internal Field(string name, Shape kind) { Name = name; Kind = kind; }
        }

        // All nodes are newly created private inspection data, not original
        // objects or an externally authenticated frozen handoff.
        private sealed class Node
        {
            internal readonly Shape Kind;
            internal readonly object Leaf;
            internal readonly Node[] Children;
            internal Node(Shape kind, object leaf, Node[] children)
            { Kind = kind; Leaf = leaf; Children = children; }
        }

        private static Field S(string name) { return new Field(name, Shape.Text); }
        private static Field I(string name) { return new Field(name, Shape.Int32); }

        private static Field[] Fields(Shape kind)
        {
            switch (kind)
            {
                case Shape.CaseRecord:
                    return new[] { S("CaseId"), S("Level"), S("Observation") };
                case Shape.FixedRecord:
                    return new[] {
                        S("CandidateQualification"), S("DriverPath"), S("DriverSha256"),
                        I("DriverBodyBytes"), I("DriverInputCeiling"), I("DriverTailDetectionBytes"),
                        S("CallerPath"), S("CallerSha256"), S("ReaderPath"), S("ReaderSha256"),
                        S("BaselinePath"), S("BaselineSha256"), I("StdoutBodyBudget"),
                        I("StdoutDetectionBudget"), I("StderrBodyBudget"), I("StderrDetectionBudget"),
                        I("WholeCaseDeadlineSeconds"), I("StopConfirmationMaximumSeconds"),
                        S("FrameMarker"), new Field("CaseContract", Shape.Cases),
                        new Field("StatusCombinations", Shape.Tuples), new Field("OuterReasons", Shape.Reasons),
                        S("AuthorityChannel"), S("ControllerFullShaBinding"),
                        S("BootstrapTextEncodingAndShaBinding"), S("LiveAdapters"), S("CaseCompletion") };
                case Shape.DriverRecord:
                    return new[] { S("TextCheck"), S("Authority"), S("SourceAdmission"),
                        S("FrozenHandoff"), S("ChildLengthEofShaVerification"), S("CaseCompletion") };
                case Shape.FrameRecord:
                    return new[] { S("TextCheck"), S("RecordedAction"),
                        new Field("ProtectionRecord", Shape.Boolean), S("Qualification"),
                        S("PeerEof"), S("TaskSettlement"), S("ProcessExit"), S("Deadline"),
                        S("Authority"), S("CaseCompletion") };
                case Shape.ReadRecord:
                    return new[] { S("Classification"), new Field("ReportedBodyBytesAfter", Shape.NullableInt32),
                        S("DetectionByte"), S("Qualification"), S("ActualPeerEof"),
                        S("ResourceOwnership"), S("CaseCompletion") };
                case Shape.WriteRecord:
                    return new[] { S("Classification"), S("ActualPartialProgress"), S("WriteByteCount"),
                        S("ChildLengthEofShaVerification"), S("InputClose"), S("AutomaticResend"),
                        S("Qualification"), S("ResourceOwnership"), S("CaseCompletion") };
                default:
                    return null;
            }
        }

        private static bool Item(object suppliedId, out Shape kind, out int outputCount)
        {
            kind = Shape.Text;
            outputCount = 1;
            if (suppliedId == null || suppliedId.GetType() != typeof(string)) return false;
            string id = (string)suppliedId;
            int dash = id.IndexOf('-');
            if (dash < 1 || dash > 2 || id.Length != dash + 4) return false;
            int number = 0;
            for (int k = dash + 1; k < id.Length; k++)
            {
                if (id[k] < '0' || id[k] > '9') return false;
                number = number * 10 + (id[k] - '0');
            }
            if (number < 1) return false;
            string group = id.Substring(0, dash);
            if (group == "M" && number <= 6)
            {
                int family = (number - 1) % 3;
                kind = family == 0 ? Shape.Cases : family == 1 ? Shape.Tuples : Shape.FixedRecord;
                outputCount = family == 0 ? 8 : family == 1 ? 26 : 1;
                return true;
            }
            if (group == "RQ" && number <= 18) { kind = Shape.Boolean; return true; }
            if (group == "D" && number <= 7) { kind = Shape.DriverRecord; return true; }
            if (group == "F" && number <= 62) { kind = Shape.FrameRecord; return true; }
            if (group == "RD" && number <= 52) { kind = Shape.ReadRecord; return true; }
            if (group == "WR" && number <= 44) { kind = Shape.WriteRecord; return true; }
            return false;
        }

        // No custom Equals, conversion or property getters are used here.
        private static bool KnownSimple(object value)
        {
            if (value == null) return true;
            Type t = value.GetType();
            return t == typeof(string) || t == typeof(bool) || t == typeof(int) || t == typeof(long)
                || t == typeof(object[]) || t == typeof(string[]) || t == typeof(byte[]) || t == typeof(int[]);
        }

        private static int FieldIndex(Field[] fields, string key)
        {
            for (int k = 0; k < fields.Length; k++)
                if (string.Equals(fields[k].Name, key, StringComparison.Ordinal)) return k;
            return -1;
        }

        private static Inspection DictionaryValues(object value, bool expected, Shape kind,
            Field[] fields, out object[] values)
        {
            values = null;
            if (value == null) return Inspection.Different;
            Type required = kind == Shape.CaseRecord ? typeof(Hashtable) : typeof(OrderedDictionary);
            // Non-case data oracles are OrderedDictionary; native actual
            // custom records must take the separately checked NoteProperty path.
            if (!expected && kind != Shape.CaseRecord) return Inspection.Uninspectable;
            if (value.GetType() != required)
                return KnownSimple(value) ? Inspection.Different : Inspection.Uninspectable;
            IDictionary table = (IDictionary)value;
            if (table.Count != fields.Length) return Inspection.Different;
            object[] heldValues = new object[fields.Length];
            bool[] seen = new bool[fields.Length];
            IDictionaryEnumerator it = table.GetEnumerator();
            int visited = 0;
            while (it.MoveNext())
            {
                if (++visited > fields.Length) return Inspection.Uninspectable;
                object rawKey = it.Key;
                if (rawKey == null || rawKey.GetType() != typeof(string)) return Inspection.Uninspectable;
                string key = (string)rawKey;
                if (key.Length > MaxNameCharacters) return Inspection.Different;
                int at = FieldIndex(fields, key);
                if (at < 0 || seen[at]) return Inspection.Different;
                seen[at] = true;
                heldValues[at] = it.Value;
            }
            if (visited != fields.Length) return Inspection.Uninspectable;
            for (int k = 0; k < seen.Length; k++) if (!seen[k]) return Inspection.Uninspectable;
            values = heldValues;
            return Inspection.Ok;
        }

        private static Inspection VisibleNoteValues(object value, Field[] fields, out object[] values)
        {
            values = null;
            if (value == null) return Inspection.Different;
            if (value.GetType() != typeof(PSObject))
                return KnownSimple(value) ? Inspection.Different : Inspection.Uninspectable;
            PSObject wrapper = (PSObject)value;
            object immediate = wrapper.ImmediateBaseObject;
            if (immediate == null || immediate.GetType() != typeof(PSCustomObject)) return Inspection.Uninspectable;
            PSNoteProperty[] notes = new PSNoteProperty[fields.Length];
            bool[] seen = new bool[fields.Length];
            int visited = 0;
            // The framework may internally integrate/allocate metadata before
            // this finite loop. Hidden members are not attested. Outside host
            // identity/resource bounds remain mandatory and UNBOUND.
            foreach (PSPropertyInfo property in wrapper.Properties)
            {
                if (property == null || property.GetType() != typeof(PSNoteProperty)) return Inspection.Uninspectable;
                PSNoteProperty note = (PSNoteProperty)property;
                if (!note.IsInstance || note.MemberType != PSMemberTypes.NoteProperty) return Inspection.Uninspectable;
                if (++visited > fields.Length) return Inspection.Different;
                string key = note.Name;
                if (key == null || key.Length > MaxNameCharacters) return Inspection.Uninspectable;
                int at = FieldIndex(fields, key);
                if (at < 0 || seen[at]) return Inspection.Different;
                seen[at] = true;
                notes[at] = note;
            }
            if (visited != fields.Length) return Inspection.Different;
            for (int k = 0; k < seen.Length; k++) if (!seen[k]) return Inspection.Uninspectable;
            // No Value read is reached until ALL visible metadata is accepted.
            object[] heldValues = new object[fields.Length];
            for (int k = 0; k < notes.Length; k++) heldValues[k] = notes[k].Value;
            values = heldValues;
            return Inspection.Ok;
        }

        private static Inspection Snapshot(object value, Shape kind, bool expected, out Node node)
        {
            node = null;
            if (kind == Shape.Text || kind == Shape.Boolean || kind == Shape.Int32 || kind == Shape.NullableInt32)
            {
                if (value == null)
                {
                    if (kind != Shape.NullableInt32) return Inspection.Different;
                    node = new Node(kind, null, null);
                    return Inspection.Ok;
                }
                Type wanted = kind == Shape.Text ? typeof(string) : kind == Shape.Boolean ? typeof(bool) : typeof(int);
                if (value.GetType() != wanted)
                    return KnownSimple(value) ? Inspection.Different : Inspection.Uninspectable;
                if (kind == Shape.Text && ((string)value).Length > MaxValueCharacters) return Inspection.Different;
                node = new Node(kind, value, null);
                return Inspection.Ok;
            }
            if (kind == Shape.Cases || kind == Shape.Tuples || kind == Shape.Reasons)
            {
                int count = kind == Shape.Cases ? 8 : kind == Shape.Tuples ? 26 : 6;
                if (value == null) return Inspection.Different;
                Type t = value.GetType();
                // These are explicit native collection carriers, not conversions.
                // P1 string[] oracle versus controller object[] string collection
                // is compared by exact native String elements and fixed order.
                if (t != typeof(object[]) && !(kind != Shape.Cases && t == typeof(string[]))) return Inspection.Uninspectable;
                Array array = (Array)value;
                if (array.Length != count) return Inspection.Different;
                Node[] children = new Node[count];
                Shape childKind = kind == Shape.Cases ? Shape.CaseRecord : Shape.Text;
                for (int k = 0; k < count; k++)
                {
                    Inspection state = Snapshot(array.GetValue(k), childKind, expected, out children[k]);
                    if (state != Inspection.Ok) return state;
                }
                node = new Node(kind, null, children);
                return Inspection.Ok;
            }
            Field[] fields = Fields(kind);
            if (fields == null) return Inspection.Uninspectable;
            object[] values;
            Inspection recordState = expected || kind == Shape.CaseRecord
                ? DictionaryValues(value, expected, kind, fields, out values)
                : VisibleNoteValues(value, fields, out values);
            if (recordState != Inspection.Ok) return recordState;
            Node[] recordChildren = new Node[fields.Length];
            for (int k = 0; k < fields.Length; k++)
            {
                Inspection state = Snapshot(values[k], fields[k].Kind, expected, out recordChildren[k]);
                if (state != Inspection.Ok) return state;
            }
            node = new Node(kind, null, recordChildren);
            return Inspection.Ok;
        }

        private static bool Equal(Node left, Node right)
        {
            if (left.Kind != right.Kind) return false;
            if (left.Children != null || right.Children != null)
            {
                if (left.Children == null || right.Children == null || left.Children.Length != right.Children.Length) return false;
                for (int k = 0; k < left.Children.Length; k++)
                    if (!Equal(left.Children[k], right.Children[k])) return false;
                return true;
            }
            if (left.Leaf == null || right.Leaf == null) return left.Leaf == null && right.Leaf == null;
            if (left.Kind == Shape.Text) return string.Equals((string)left.Leaf, (string)right.Leaf, StringComparison.Ordinal);
            if (left.Kind == Shape.Boolean) return (bool)left.Leaf == (bool)right.Leaf;
            return (int)left.Leaf == (int)right.Leaf;
        }

        public static Dsp004ReportedValueComparison Compare(object itemId,
            object callerSuppliedNativeItems, object independentlyOwnedExpectedValue)
        {
            try
            {
                Shape kind;
                int count;
                if (!Item(itemId, out kind, out count))
                    return new Dsp004ReportedValueComparison("REFERENCE_NOT_COMPARABLE", null);
                Node expected;
                if (Snapshot(independentlyOwnedExpectedValue, kind, true, out expected) != Inspection.Ok)
                    return new Dsp004ReportedValueComparison("REFERENCE_NOT_COMPARABLE", null);
                // No IEnumerable adapters, array coercion or automatic PSObject
                // scalar unwrapping. This is a supplied projection, not capture.
                if (callerSuppliedNativeItems == null || callerSuppliedNativeItems.GetType() != typeof(object[]))
                    return new Dsp004ReportedValueComparison("ACTUAL_NOT_COMPARABLE", null);
                object[] items = (object[])callerSuppliedNativeItems;
                if (items.Length != count) return new Dsp004ReportedValueComparison("DIFFERENT", null);
                Node actual;
                object selected = kind == Shape.Cases || kind == Shape.Tuples ? (object)items : items[0];
                Inspection actualState = Snapshot(selected, kind, false, out actual);
                if (actualState != Inspection.Ok)
                    return new Dsp004ReportedValueComparison(actualState == Inspection.Different
                        ? "DIFFERENT" : "ACTUAL_NOT_COMPARABLE", null);
                return new Dsp004ReportedValueComparison(Equal(expected, actual) ? "EQUAL" : "DIFFERENT", null);
            }
            catch (Exception error)
            {
                // Not normal checkable mismatch; the real exception is retained
                // privately, with no diagnostic details in the public relation.
                return new Dsp004ReportedValueComparison("INSPECTION_FAILED", error);
            }
        }
    }
}
