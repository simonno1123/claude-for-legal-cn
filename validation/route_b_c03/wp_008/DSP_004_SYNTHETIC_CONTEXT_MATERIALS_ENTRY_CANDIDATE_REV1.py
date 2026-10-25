"""DSP-004 synthetic-context materials entry candidate, REV1.

Loading identity: DSP_004_SYNTHETIC_CONTEXT_MATERIALS_ENTRY_CANDIDATE_REV1.
Formation scope: one new source candidate plus independent static review only,
under the Project Owner's explicit conversation authorization for plan 91469.
Creation does not accept, admit, load, compile, test, or execute this source.

Fixed formation dependencies, whose complete bytes were checked before writing:
DSP_004_CAPTURE_RESULT_CONTRACT_CANDIDATE_REV1.py
E9472328847617EBF629FB01A0A163C0805226690600E5E13EBE1209E2F6705C
scripts/phase2_runtime/route_b_c03/contracts.py
7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4

The single logical import below does NOT verify those bytes or establish the
origin of loaded modules, classes, or enum members. A separately approved loader
must bind the real dependency bytes, interpreter, class identities, access scope,
and permitted use before ANY loading or invocation. This candidate implements
no loader and makes no claim that another loader is absent elsewhere.

This unit only checks the selected synthetic inputs, creates one private tuple
from the supplied stimulus elements, reads that same tuple, and assembles the
existing CaptureMaterials. It is not a business-source capture adapter, source
authenticator, comparison engine, Gate caller, or completed capture-result entry.
The four vectors below are planned construction inputs from design 53728 and the
limited-adopted selection 91468, not expected-reference reads, admitted variants,
observed matches, executed coverage, or the PowerShell/.NET 189-item catalogue.

Source-identity strings are caller-supplied metadata, checked for text format
only. They are never generated from roles, values, hashes, or correlation IDs.
Separate source/use approval and evidence must bind the actual producer entry,
carrier instance, three slots, source definitions, and this invocation. The prior
must likewise belong to the same actual Gate call, attempt, and consumed inputs.
Exact classes, an eligible state, SHA-shaped text, and equal correlations cannot
authenticate any of those facts. The function has no trusted=True permission flag.

The private zero-record preflight is structural validation only. It is neither
returned nor presented as acquired materials, successful capture, receipt, or
proof that any real source had no data. Both preflight and final construction
retain the SAME invocation and prior objects; neither is rebuilt or repaired.

Only the final materials contain three references read from the SAME private
context tuple. The values come from the supplied elements, never substituted
from the planned-vector table. Identity/eligibility/variant rechecks are local
checks, not atomicity, snapshot completeness, stability, or anti-TOCTOU proofs.

The strict-str first subset excludes planned None, wrong-type, missing-source,
partial, rejection, actor, matter, and joint-boundary cases. An unexpected event
must not be ignored merely because it is outside this subset. A source value
actually obtained as None is still an obtained value; this entry's input range
does not establish source invalidity or authorize relabeling it as unacquired.
An actual Gate return of None is distinct from no return and from source None.

This function creates no CompleteCaptureReturn, completion flags, BoundaryCheck,
replacement GateDecision, CaptureFailure, IncompleteCapture, or receipt. It does
not call validate_capture_result, a Gate/provider, an expected reader,
user-supplied callbacks, a comparer, cleanup, or any result transport. It does
not directly call private contract validators; public constructors invoke
their own validators.
No normalization, stringify/repr, serialization, deep copy, file/network access,
automatic matching, logging, or observed-record SHA is provided by the entry.
Dependency initialization is still loading/execution, not harmless text access.

Parameter checks may raise their own real errors. Dependency-constructor errors
propagate without replacement. No failure is converted to a normal result, None,
or a fabricated Gate outcome. This does not implement outer retention of bad
priors, partial materials, original exceptions, or their actual event history.
Tracebacks may retain inputs, modules, and local references. Three strings and
shallow frozen carriers do not prove bounded memory, confidentiality, zero I/O,
zero disclosure, destruction, or safe retention after host/process death.

Source/root admission, trustworthy loading, complete per-stage input binding,
instance/attempt evidence, outer failure retention, resource budgets, cleanup,
and retention/disposition policy remain LIMITED. Until those prerequisites and
separate execution authority exist, the ENTIRE unit remains HOLD / NOT_RUN,
including the four normal planned vectors. If an attempt actually occurs, its
real stage and failure must be preserved; it must not be backdated to NOT_RUN.

No accepted files or original expectations are changed. No source admission,
business capture, integration, deployment, Manifest, or external-model authority
is established. DSP-004 remains OPEN / HOLD; B-01 / B-02 remain OPEN. All prior
LIMITED and historical records remain. This source is not a runtime protocol.
"""

import DSP_004_CAPTURE_RESULT_CONTRACT_CANDIDATE_REV1 as _capture_contract


_PLANNED_STIMULI = (
    (
        "DSP004-PROP-ALL-MATCH-001",
        (
            "SYNTHETIC-PROJECT-001",
            "SYNTHETIC-SESSION-001",
            "SYNTHETIC-PROVIDER-001",
        ),
    ),
    (
        "DSP004-PROP-PROJECT-ONLY-001",
        (
            "SYNTHETIC-PROJECT-002",
            "SYNTHETIC-SESSION-001",
            "SYNTHETIC-PROVIDER-001",
        ),
    ),
    (
        "DSP004-PROP-SESSION-ONLY-001",
        (
            "SYNTHETIC-PROJECT-001",
            "SYNTHETIC-SESSION-002",
            "SYNTHETIC-PROVIDER-001",
        ),
    ),
    (
        "DSP004-PROP-PROVIDER-ONLY-001",
        (
            "SYNTHETIC-PROJECT-001",
            "SYNTHETIC-SESSION-001",
            "SYNTHETIC-PROVIDER-002",
        ),
    ),
)


def build_capture_materials(
    invocation,
    stimulus_values,
    source_identities,
    prior_decision,
) -> _capture_contract.CaptureMaterials:
    """Assemble first-subset materials, not an authenticated capture result.

    Arguments retain their original values and references. All three tuple
    elements must be native str. Only the four exact planned stimulus vectors
    are selected; names do not report actual matches. Source IDs are format
    checked, not approved. External qualification is required for every use.

    The caller must separately retain real return/attempt/failure facts and any
    materials it is authorized to hold. This function neither guarantees that
    all such facts survive an exception nor grants any acquisition/retention
    permission. Whole-unit runtime prerequisites remain unresolved.
    """
    if type(invocation) is not _capture_contract.CaptureInvocationBinding:
        raise TypeError("invocation requires the fixed contract's native binding")
    if type(prior_decision) is not _capture_contract.GateDecision:
        raise TypeError("prior_decision requires the existing native GateDecision")

    # Public construction validates the original binding and prior before any
    # context or CapturedReference is created. This object stays private.
    _preflight_materials = _capture_contract.CaptureMaterials(
        invocation=invocation,
        acquired=(),
        prior_decision=prior_decision,
    )
    if (
        _preflight_materials.invocation is not invocation
        or _preflight_materials.prior_decision is not prior_decision
    ):
        raise ValueError("structural preflight did not retain the supplied objects")
    if prior_decision.state is not _capture_contract.InvocationState.ELIGIBLE_FOR_MAPPING:
        raise ValueError("this candidate requires an eligible prior decision")

    if type(stimulus_values) is not tuple:
        raise TypeError("stimulus_values requires native tuple")
    if len(stimulus_values) != 3:
        raise ValueError("stimulus_values requires exactly three elements")
    for value in stimulus_values:
        if type(value) is not str:
            raise TypeError("each stimulus requires native str")

    if type(source_identities) is not tuple:
        raise TypeError("source_identities requires native tuple")
    if len(source_identities) != 3:
        raise ValueError("source_identities requires exactly three elements")
    for source_identity in source_identities:
        if type(source_identity) is not str:
            raise TypeError("each source identity requires native str")
        if not source_identity or source_identity.isspace():
            raise ValueError("each source identity requires nonempty, non-whitespace text")

    variant_id = invocation.variant_id
    if type(variant_id) is not str:
        raise TypeError("variant_id requires native str")
    planned_values = None
    for planned_variant, planned_vector in _PLANNED_STIMULI:
        if variant_id == planned_variant:
            planned_values = planned_vector
            break
    if planned_values is None:
        raise ValueError("variant_id is outside this candidate's four planned vectors")
    if stimulus_values != planned_values:
        raise ValueError("stimulus_values differs from the selected planned vector")

    # Build once from the supplied values, not from planned_values. These same
    # element references are read only from this private context below.
    _context = (
        stimulus_values[0],
        stimulus_values[1],
        stimulus_values[2],
    )
    _project_reference = _capture_contract.CapturedReference(
        boundary=_capture_contract.CaptureBoundary.PROJECT,
        actual_source_identity=source_identities[0],
        raw_value=_context[0],
        raw_type=type(_context[0]),
    )
    _session_reference = _capture_contract.CapturedReference(
        boundary=_capture_contract.CaptureBoundary.SESSION,
        actual_source_identity=source_identities[1],
        raw_value=_context[1],
        raw_type=type(_context[1]),
    )
    _provider_reference = _capture_contract.CapturedReference(
        boundary=_capture_contract.CaptureBoundary.PROVIDER,
        actual_source_identity=source_identities[2],
        raw_value=_context[2],
        raw_type=type(_context[2]),
    )
    _acquired = (
        _project_reference,
        _session_reference,
        _provider_reference,
    )
    _materials = _capture_contract.CaptureMaterials(
        invocation=invocation,
        acquired=_acquired,
        prior_decision=prior_decision,
    )
    if (
        _materials.invocation is not invocation
        or _materials.prior_decision is not prior_decision
        or _materials.acquired is not _acquired
    ):
        raise ValueError("final materials did not retain the supplied objects")
    if prior_decision.state is not _capture_contract.InvocationState.ELIGIBLE_FOR_MAPPING:
        raise ValueError("the supplied prior is no longer eligible at the final check")
    final_variant_id = invocation.variant_id
    if type(final_variant_id) is not str:
        raise TypeError("final variant_id requires native str")
    if final_variant_id != variant_id:
        raise ValueError("the supplied binding changed its selected variant")
    return _materials
