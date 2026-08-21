from AGENTS.document_intake_agent import DocumentIntakeAgent
from AGENTS.requirements_mapper_agent import RequirementsMapperAgent
from AGENTS.evidence_gap_agent import EvidenceGapAgent
from AGENTS.traceability_agent import TraceabilityAgent
from AGENTS.review_coordinator_agent import ReviewCoordinatorAgent
from AGENTS.submission_gatekeeper_agent import SubmissionGatekeeperAgent

def run_workflow(c:dict)->dict:
    agents=[DocumentIntakeAgent(),RequirementsMapperAgent(),EvidenceGapAgent(),TraceabilityAgent(),ReviewCoordinatorAgent(),SubmissionGatekeeperAgent()]
    return {a.name:a.run(c) for a in agents}
