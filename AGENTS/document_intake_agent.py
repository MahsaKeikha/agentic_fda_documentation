class DocumentIntakeAgent:
    name="document_intake"
    def run(self,c:dict)->dict:return {"documents":c.get("documents",[]),"indexed":True}
