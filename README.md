# Agentic FDA Documentation

F54 standalone multi-agent regulatory documentation support system.

## Agents

- [`document_intake_agent.py`](AGENTS/document_intake_agent.py)
- [`requirements_mapper_agent.py`](AGENTS/requirements_mapper_agent.py)
- [`evidence_gap_agent.py`](AGENTS/evidence_gap_agent.py)
- [`traceability_agent.py`](AGENTS/traceability_agent.py)
- [`review_coordinator_agent.py`](AGENTS/review_coordinator_agent.py)
- [`submission_gatekeeper_agent.py`](AGENTS/submission_gatekeeper_agent.py)

## Tools

- [`document_indexer.py`](TOOLS/document_indexer.py)
- [`requirements_matrix.py`](TOOLS/requirements_matrix.py)
- [`evidence_gap_checker.py`](TOOLS/evidence_gap_checker.py)
- [`traceability_builder.py`](TOOLS/traceability_builder.py)
- [`review_tracker.py`](TOOLS/review_tracker.py)

## Skills

- [`document_intake.py`](SKILLS/document_intake.py)
- [`requirements_mapping.py`](SKILLS/requirements_mapping.py)
- [`evidence_gap_analysis.py`](SKILLS/evidence_gap_analysis.py)
- [`traceability_review.py`](SKILLS/traceability_review.py)
- [`submission_readiness.py`](SKILLS/submission_readiness.py)

Supporting layers include orchestration, memory, state, schemas, prompts, config, safety, observability, evals, benchmarks, examples, tests, docs, and CI.

This repository supports drafting, organization, and traceability. It does not certify compliance or approval readiness.
