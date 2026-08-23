# F54 Agentic FDA Documentation

**Maturity:** L3 Gold Standard candidate  
**Version:** 1.0.0

A six-agent reference architecture for organizing, mapping, reviewing, and governing FDA-facing medical-device documentation. The system coordinates document intake, regulatory requirement mapping, evidence-gap analysis, traceability, review coordination, and submission-readiness gating while keeping all regulatory judgments and submission authority with qualified humans.

F54 is designed as an engineering and regulatory-documentation reference. It helps teams structure evidence, detect missing or inconsistent records, preserve provenance, and make review status inspectable. It does not determine regulatory classification, choose a submission pathway, certify compliance, prepare an official legal opinion, or represent that a product is cleared, approved, authorized, or ready for submission without qualified review.

## Reference lifecycle

```text
controlled source documents
          |
          v
 Document Intake Agent
          |
          v
Requirements Mapper Agent
          |
          v
  Evidence Gap Agent
          |
          v
  Traceability Agent
          |
          v
Review Coordinator Agent
          |
          v
Submission Gatekeeper Agent
          |
          v
 qualified regulatory review
```

The workflow is intentionally evidence-first. A polished submission package is not treated as complete when underlying design, risk, verification, validation, clinical, labeling, software, cybersecurity, manufacturing, or quality evidence is missing.

## Agents

| Agent | Responsibility | Core question |
|---|---|---|
| Document Intake Agent | Register, classify, version, and normalize controlled source documents | What evidence exists, which version is current, and where did it come from? |
| Requirements Mapper Agent | Map applicable documentation requirements to evidence | Which requirement is supported by which controlled artifact? |
| Evidence Gap Agent | Detect missing, incomplete, stale, contradictory, or unsupported evidence | What must be resolved before qualified regulatory review can proceed? |
| Traceability Agent | Build links among claims, requirements, risks, tests, results, labeling, and supporting evidence | Can every material statement be traced back to controlled evidence? |
| Review Coordinator Agent | Track owners, reviewers, comments, open questions, and closure state | Has the right qualified reviewer examined the right evidence? |
| Submission Gatekeeper Agent | Apply fail-closed readiness criteria | Are critical evidence and review requirements complete enough for human submission-readiness review? |

## Repository architecture

```text
AGENTS/
├── document_intake_agent.py
├── requirements_mapper_agent.py
├── evidence_gap_agent.py
├── traceability_agent.py
├── review_coordinator_agent.py
└── submission_gatekeeper_agent.py

SKILLS/
├── document_intake.py
├── requirements_mapping.py
├── evidence_gap_analysis.py
├── traceability_review.py
└── submission_readiness.py

TOOLS/
├── document_indexer.py
├── requirements_matrix.py
├── evidence_gap_checker.py
├── traceability_builder.py
└── review_tracker.py

benchmarks/
evals/
examples/
memory/
observability/
orchestration/
safety/
schemas/
state/
tests/
config/
docs/
.github/workflows/ci.yml
```

The repository separates reasoning agents from deterministic registries, matrices, traceability structures, review state, safety policy, and evaluation.

## Document intake and control

The Document Intake Agent provides the first control point. Regulatory documentation should not rely on an unversioned folder of files with uncertain status.

A production document record can include:

```text
document_id
document_type
title
version
status
owner
source_system
effective_date
supersedes
approval_state
checksum
confidentiality
```

`TOOLS/document_indexer.py` provides the reference indexing layer.

The system should preserve superseded versions for auditability while clearly identifying the current controlled version.

## Regulatory requirement mapping

`TOOLS/requirements_matrix.py` supports mapping requirements to controlled evidence.

A useful record can include:

```text
requirement_id
source
section
applicability
rationale
evidence_ids
owner
review_status
gap_status
```

Applicable requirements vary by device, classification, product code, technology, intended use, software content, cybersecurity profile, clinical evidence, and submission pathway. F54 can organize a requirement set supplied or approved by qualified regulatory professionals, but it must not independently determine legal applicability.

## Evidence domains

Depending on the device and submission, evidence may include:

- device description
- intended use and indications
- claims
- substantial-equivalence evidence where applicable
- design inputs and outputs
- requirements traceability
- risk-management records
- verification reports
- validation reports
- software documentation
- cybersecurity documentation
- interoperability evidence
- electrical safety or EMC evidence where applicable
- biocompatibility evidence where applicable
- sterilization or packaging evidence where applicable
- bench testing
- performance testing
- human-factors documentation
- clinical evidence
- labeling
- manufacturing information
- complaint/post-market planning
- quality-system records

The exact documentation set must be determined by qualified regulatory and technical personnel.

## Evidence-gap analysis

The Evidence Gap Agent and `TOOLS/evidence_gap_checker.py` are designed to surface gaps explicitly rather than hide them inside prose.

Examples of gaps include:

```text
MISSING DOCUMENT
STALE VERSION
UNAPPROVED EVIDENCE
UNSUPPORTED CLAIM
TRACEABILITY GAP
TEST REPORT MISSING
ACCEPTANCE CRITERIA MISSING
RISK CONTROL UNVERIFIED
LABELING INCONSISTENCY
CYBERSECURITY EVIDENCE MISSING
CLINICAL EVIDENCE REVIEW REQUIRED
QUALIFIED REVIEWER REQUIRED
```

A gap remains open until supported by controlled evidence or formally dispositioned by an authorized reviewer.

## Traceability

`TOOLS/traceability_builder.py` supports end-to-end evidence linkage.

A useful traceability chain is:

```text
claim / intended use
      |
      v
user need / requirement
      |
      v
risk / risk control
      |
      v
design output
      |
      v
verification / validation evidence
      |
      v
labeling / submission section
```

Traceability should preserve evidence identifiers and document versions. The system should not infer that a test supports a claim merely because the wording appears similar.

## Claims discipline

Product claims require particular care because they can affect regulatory scope, evidence burden, labeling, and clinical interpretation.

F54 should distinguish:

- intended use
- indications
- marketing language
- technical performance claims
- clinical performance claims
- comparative claims
- safety claims

Unsupported or stronger-than-evidence claims should be flagged for qualified review rather than rewritten to appear compliant.

## Design and risk evidence

Submission documentation should remain consistent with the controlled design record.

Relevant links can include:

```text
requirement -> design output -> verification
hazard -> risk control -> implementation -> verification
user need -> validation evidence
software requirement -> software test evidence
cybersecurity requirement -> security verification evidence
```

F54 should surface conflicts between the submission narrative and underlying engineering evidence.

## Verification and validation evidence

Verification and validation reports should be reviewed for more than file presence.

Useful checks include:

- protocol/report identity
- approved version
- requirement or claim covered
- test configuration
- acceptance criteria
- sample or unit identity
- deviations
- results
- failures
- statistical basis where applicable
- conclusion
- reviewer approval

The system must not convert an incomplete or failed test into a passing result.

## Software documentation

When software is in scope, documentation may include, depending on device and applicable FDA expectations:

- software description
- architecture
- requirements
- design information
- traceability
- risk controls
- software testing
- unresolved anomalies
- configuration and release identification
- third-party software information
- cybersecurity evidence

F54 can organize these records but cannot determine that software evidence is sufficient without qualified review.

## Cybersecurity documentation

Connected devices can require documentation covering areas such as:

- threat modeling
- security architecture
- trust boundaries
- authentication and authorization
- secure update mechanisms
- cryptographic protections
- vulnerability management
- SBOM-related records where applicable
- logging
- recovery
- post-market vulnerability response

Cybersecurity gaps that affect safety, availability, integrity, confidentiality, or essential performance should remain visible across the evidence package.

## Human factors and labeling

Human-factors evidence and labeling should be mutually consistent.

Review can examine:

- intended users
- use environments
- critical tasks
- use-related risks
- instructions for use
- warnings
- contraindications
- precautions
- training requirements
- labeling-supported claims

A labeling statement unsupported by usability, risk, technical, or clinical evidence should be flagged.

## Clinical evidence boundary

F54 may index, map, and trace clinical evidence, but it must not:

- fabricate study outcomes
- infer clinical efficacy from engineering data
- replace statistical review
- determine that clinical evidence is unnecessary
- make unsupported medical claims
- decide that a clinical study establishes safety or effectiveness without qualified review

Clinical and regulatory interpretation remains with appropriately qualified professionals.

## Review coordination

`TOOLS/review_tracker.py` supports structured review state.

A review record can include:

```text
artifact_id
review_type
reviewer_role
reviewer
status
comments
open_questions
decision
review_date
```

Production systems should authenticate reviewers and preserve controlled approvals. A model-generated statement that a document was reviewed is not valid evidence of human review.

## Submission readiness

The Submission Gatekeeper applies fail-closed readiness logic.

A package should be blocked when critical conditions such as these remain unresolved:

- uncontrolled document versions
- unresolved intended-use or claim issues
- incomplete requirement mapping
- missing traceability
- missing risk documentation
- unverified risk controls
- incomplete verification or validation evidence
- software evidence gaps
- cybersecurity evidence gaps
- human-factors evidence gaps
- clinical-evidence gaps where applicable
- labeling inconsistencies
- missing reviewer approvals
- unresolved conflicts
- unresolved questions
- open critical risks

Passing the gate means the package may be eligible for qualified human submission-readiness review. It does not mean FDA acceptance, clearance, approval, or authorization.

## Human authority boundaries

F54 must not autonomously:

- determine device classification
- select the final regulatory pathway
- determine legal applicability of requirements
- approve intended use or indications
- approve product claims
- accept residual risk
- certify verification or validation
- decide clinical-evidence sufficiency
- approve labeling
- sign regulatory declarations
- submit to FDA
- respond officially to FDA on behalf of a sponsor
- claim clearance, approval, authorization, or compliance

These decisions remain with authorized regulatory, quality, clinical, legal, and executive personnel as applicable.

## Shared state, memory, and provenance

The repository includes explicit state and memory layers so evidence does not disappear between agents.

Production state should preserve:

- document identity and version
- requirement mapping
- evidence links
- gap status
- comments and reviewer status
- submission-section mapping
- open questions
- risk and conflict state
- approval state
- timestamps and provenance

Superseded records should remain auditable.

## Observability

`observability/tracing.py` supports inspectable workflow execution.

Useful trace fields include:

- workflow ID
- submission/package ID
- document IDs and versions
- agent execution order
- tool calls
- mapped requirements
- detected gaps
- traceability links
- review events
- gate results
- unresolved questions
- human decisions

The orchestration trace is not a substitute for formal regulatory or quality-system records.

## End-to-end reference workflow

A typical F54 workflow is:

1. Register the device/documentation package.
2. Index controlled source documents and versions.
3. Load the regulatory requirement set approved for use.
4. Map requirements to evidence.
5. Detect missing, stale, contradictory, or unsupported evidence.
6. Build traceability across claims, requirements, risks, tests, and labeling.
7. Route artifacts to qualified reviewers.
8. Track comments, questions, and closure state.
9. Re-run gap and traceability checks after changes.
10. Apply fail-closed submission-readiness gates.
11. Require qualified regulatory/quality review.
12. Record the human readiness decision and preserve provenance.

## Reproduce the reference implementation

```bash
python -m pip install -e '.[dev]'
ruff check .
pytest -q
python -m evals.heldout_suite
python examples/example_run.py
```

CI is defined under `.github/workflows/ci.yml`.

## Benchmarks and evaluation

The repository includes:

```text
benchmarks/benchmark.py
benchmarks/RESULTS.md
evals/evaluator.py
evals/heldout_suite.py
```

Evaluation should test governance behavior rather than prose quality alone.

Useful dimensions include:

- document-version detection
- requirement-mapping completeness
- evidence-gap recall
- unsupported-claim detection
- traceability correctness
- stale-evidence detection
- contradictory-evidence detection
- reviewer-status accuracy
- unresolved-question propagation
- fail-closed gate behavior
- human-authority enforcement

Strong held-out cases should intentionally contain missing evidence, superseded documents, inconsistent claims, incomplete traceability, open reviews, and unsupported readiness assertions.

## Failure states

Useful explicit states include:

```text
DOCUMENT CONTROL INCOMPLETE
REQUIREMENT MAP INCOMPLETE
EVIDENCE GAP OPEN
TRACEABILITY GAP
CLAIM UNSUPPORTED
RISK EVIDENCE INCOMPLETE
VERIFICATION EVIDENCE INCOMPLETE
VALIDATION EVIDENCE INCOMPLETE
CYBERSECURITY REVIEW REQUIRED
CLINICAL EVIDENCE REVIEW REQUIRED
LABELING REVIEW REQUIRED
QUALIFIED REVIEWER REQUIRED
CRITICAL RISK OPEN
SUBMISSION NOT READY
HUMAN REGULATORY REVIEW REQUIRED
```

The system should never fabricate evidence, document approvals, test outcomes, reviewer decisions, regulatory interpretations, or FDA status.

## CI and reproducibility

Production implementations should additionally control:

- document hashes and version IDs
- requirement-set versions
- mapping logic versions
- submission-section versions
- reviewer identities
- audit logs
- access controls
- e-signatures where required
- retention rules
- export formats
- controlled repository integration

This makes it possible to reconstruct exactly which evidence package a readiness decision was based on.

## L3 Gold Standard candidate

F54 is structured as an L3 Gold Standard candidate through specialist-agent separation, deterministic evidence tools, explicit state, traceability, held-out evaluation, CI, fail-closed readiness behavior, and human authority boundaries.

This maturity label describes the repository architecture. It is not FDA clearance, FDA approval, regulatory certification, QMS certification, legal advice, or an official determination of submission readiness.

## Extending F54

Common extensions include:

- eQMS integration
- document-management systems
- requirements-management platforms
- risk-management systems
- test-management systems
- ALM platforms
- regulatory information-management systems
- submission publishing systems
- eSTAR preparation workflows where appropriate
- electronic signatures
- clinical evidence repositories
- labeling-management systems
- cybersecurity evidence repositories
- SBOM systems
- complaint/CAPA/post-market systems

Integrations should preserve provenance, least privilege, document control, reviewer identity, and auditability.

## Design principles

1. Treat controlled evidence as the source of truth.
2. Separate regulatory requirements from supporting evidence.
3. Preserve document versions and provenance.
4. Make evidence gaps explicit.
5. Trace claims to requirements, risks, tests, and labeling.
6. Never infer regulatory approval from document completeness.
7. Keep reviewer identity and closure state explicit.
8. Fail closed when critical evidence or review is missing.
9. Preserve unresolved risks and questions through every stage.
10. Keep regulatory and submission authority with qualified humans.

## Documentation, citation, and reuse

See `docs/ARCHITECTURE.md` for architecture notes. The repository is intended to be referenced as a multi-agent regulatory-documentation architecture and can be adapted under its applicable license terms.

## Responsible use

Use F54 as a regulatory-documentation organization, traceability, and review-governance reference. Validate requirement applicability, evidence sufficiency, claims, clinical support, labeling, software, cybersecurity, quality records, and submission strategy with qualified professionals. Final FDA submissions, regulatory interpretations, official communications, and market-authority decisions remain under authorized human control.