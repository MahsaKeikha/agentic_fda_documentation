from __future__ import annotations

from typing import Any

from AGENTS.document_intake_agent import DocumentIntakeAgent
from AGENTS.evidence_gap_agent import EvidenceGapAgent
from AGENTS.requirements_mapper_agent import RequirementsMapperAgent
from AGENTS.review_coordinator_agent import ReviewCoordinatorAgent
from AGENTS.submission_gatekeeper_agent import SubmissionGatekeeperAgent
from AGENTS.traceability_agent import TraceabilityAgent


REQUIRED_GATES = {
    "submission_pathway_confirmed": "submission pathway is not confirmed",
    "intended_use_consistent": "intended use or indications are inconsistent",
    "claims_supported": "one or more claims lack supporting evidence",
    "requirements_current": "applicable requirements are not current",
    "document_set_complete": "submission document set is incomplete",
    "evidence_traceable": "evidence is not traceable to claims and requirements",
    "verification_evidence_complete": "verification evidence is incomplete",
    "validation_evidence_complete": "validation evidence is incomplete",
    "risk_management_current": "risk-management evidence is incomplete or stale",
    "human_factors_addressed": "human-factors evidence is incomplete where applicable",
    "cybersecurity_addressed": "cybersecurity documentation is incomplete where applicable",
    "software_documentation_complete": "software documentation is incomplete where applicable",
    "labeling_consistent": "labeling is inconsistent with intended use, risks, or evidence",
    "data_integrity_verified": "submission data integrity has not been verified",
    "review_complete": "required quality/regulatory review is incomplete",
}


def _specialist_outputs(context: dict[str, Any]) -> dict[str, Any]:
    agents = [
        DocumentIntakeAgent(),
        RequirementsMapperAgent(),
        EvidenceGapAgent(),
        TraceabilityAgent(),
        ReviewCoordinatorAgent(),
        SubmissionGatekeeperAgent(),
    ]
    return {agent.name: agent.run(context) for agent in agents}


def evaluate_submission(context: dict[str, Any]) -> dict[str, Any]:
    blockers = [message for gate, message in REQUIRED_GATES.items() if not context.get(gate, False)]
    if context.get("unresolved_evidence_gaps"):
        blockers.append("unresolved evidence gaps remain")
    if context.get("unresolved_conflicts"):
        blockers.append("unresolved document or reviewer conflicts remain")
    if context.get("unresolved_questions"):
        blockers.append("unresolved regulatory questions remain")
    if context.get("unsupported_claims"):
        blockers.append("unsupported claims remain in the submission")
    if context.get("open_major_findings"):
        blockers.append("major review findings remain open")
    if context.get("human_approval") is not True:
        blockers.append("final authorized quality/regulatory approval is required")
    return {
        "status": "READY_FOR_AUTHORIZED_SUBMISSION" if not blockers else "BLOCKED",
        "blockers": blockers,
        "human_approval_required": True,
        "regulatory_clearance_claimed": False,
        "notes": (
            "This workflow supports documentation readiness and traceability. "
            "It does not determine FDA classification, guarantee acceptance or clearance, "
            "replace qualified regulatory professionals, or authorize submission on its own."
        ),
    }


def run_workflow(context: dict[str, Any]) -> dict[str, Any]:
    return {"specialists": _specialist_outputs(context), "governance": evaluate_submission(context)}
