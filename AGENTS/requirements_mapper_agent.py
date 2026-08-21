class RequirementsMapperAgent:
    name="requirements_mapper"
    def run(self,c:dict)->dict:return {"requirements":c.get("requirements",[]),"mapped":True}
