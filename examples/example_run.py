from orchestration.orchestrator import run_workflow


if __name__ == "__main__":
    result = run_workflow({"submission_pathway_confirmed": True})
    print(result["governance"])
