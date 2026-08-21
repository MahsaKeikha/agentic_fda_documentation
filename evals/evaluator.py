def evaluate(r:dict)->dict:
    required=["document_intake","requirements_mapper","evidence_gap","traceability","review_coordinator","submission_gatekeeper"]
    m=[x for x in required if x not in r]
    return {"passed":not m,"missing":m}
