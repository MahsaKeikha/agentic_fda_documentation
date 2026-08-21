class SubmissionGatekeeperAgent:
    name="submission_gatekeeper"
    def run(self,c:dict)->dict:return {"submission_allowed":bool(c.get("human_approved",False)),"certified":False}
