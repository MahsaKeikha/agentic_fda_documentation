class EvidenceGapAgent:
    name="evidence_gap"
    def run(self,c:dict)->dict:return {"gaps":c.get("evidence_gaps",[]),"reviewed":True}
