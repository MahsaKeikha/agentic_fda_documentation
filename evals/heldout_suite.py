import json
from pathlib import Path

from orchestration.orchestrator import REQUIRED_GATES, evaluate_submission


def base():
    context = {gate: True for gate in REQUIRED_GATES}
    context.update(
        unresolved_evidence_gaps=[],
        unresolved_conflicts=[],
        unresolved_questions=[],
        unsupported_claims=[],
        open_major_findings=[],
        human_approval=True,
    )
    return context


SCENARIOS = [
    ("complete_authorized_package", {}, "READY_FOR_AUTHORIZED_SUBMISSION"),
    ("pathway_unconfirmed", {"submission_pathway_confirmed": False}, "BLOCKED"),
    ("unsupported_claim", {"unsupported_claims": ["claim"]}, "BLOCKED"),
    ("traceability_gap", {"evidence_traceable": False}, "BLOCKED"),
    ("risk_file_stale", {"risk_management_current": False}, "BLOCKED"),
    ("labeling_mismatch", {"labeling_consistent": False}, "BLOCKED"),
    ("open_major_finding", {"open_major_findings": ["major"]}, "BLOCKED"),
    ("missing_human_approval", {"human_approval": False}, "BLOCKED"),
]


def main():
    rows = []
    for name, changes, expected in SCENARIOS:
        context = base()
        context.update(changes)
        actual = evaluate_submission(context)["status"]
        rows.append(
            {
                "scenario": name,
                "expected": expected,
                "actual": actual,
                "passed": actual == expected,
            }
        )
    passed = sum(row["passed"] for row in rows)
    result = {
        "passed": passed,
        "total": len(rows),
        "pass_rate": passed / len(rows),
        "results": rows,
    }
    Path("heldout-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] == result["total"] else 1)


if __name__ == "__main__":
    main()
