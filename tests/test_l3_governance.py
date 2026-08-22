from orchestration.orchestrator import REQUIRED_GATES, evaluate_submission


def ready_context():
    c = {gate: True for gate in REQUIRED_GATES}
    c.update(
        unresolved_evidence_gaps=[],
        unresolved_conflicts=[],
        unresolved_questions=[],
        unsupported_claims=[],
        open_major_findings=[],
        human_approval=True,
    )
    return c


def test_ready_submission_requires_all_evidence_and_human_approval():
    result = evaluate_submission(ready_context())
    assert result["status"] == "READY_FOR_AUTHORIZED_SUBMISSION"
    assert result["blockers"] == []
    assert result["regulatory_clearance_claimed"] is False


def test_each_required_gate_fails_closed():
    for gate in REQUIRED_GATES:
        context = ready_context()
        context[gate] = False
        result = evaluate_submission(context)
        assert result["status"] == "BLOCKED", gate
        assert result["blockers"], gate


def test_human_approval_cannot_be_inferred():
    context = ready_context()
    context["human_approval"] = False
    result = evaluate_submission(context)
    assert result["status"] == "BLOCKED"
    assert any("approval" in item for item in result["blockers"])


def test_unsupported_claims_and_evidence_gaps_block():
    context = ready_context()
    context["unsupported_claims"] = ["performance claim"]
    context["unresolved_evidence_gaps"] = ["missing validation report"]
    result = evaluate_submission(context)
    assert result["status"] == "BLOCKED"
    assert len(result["blockers"]) >= 2


def test_unresolved_regulatory_questions_block():
    context = ready_context()
    context["unresolved_questions"] = ["pathway question"]
    assert evaluate_submission(context)["status"] == "BLOCKED"
