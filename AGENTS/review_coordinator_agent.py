class ReviewCoordinatorAgent:
    name="review_coordinator"
    def run(self,c:dict)->dict:return {"reviewers":c.get("reviewers",[]),"coordinated":True}
