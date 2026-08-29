# Repository Guidelines

## Purpose and Structure

CGAM is a bounded CLI worker mesh for `c = a + b`. Workers execute explicit task contracts; they do not own memory, identity, continuity, policy, witness, release authority, or next-goal selection. Specifications and public documentation live at the root and under `docs/`; machine contracts are in `schema/`, examples in `examples/`, conformance vectors in `conformance-tests/`, unit tests in `tests/`, and integrity/publication tools in `tools/`.

## Validation Commands

Run the complete relevant suite from the repository root:

```bash
python3 validate_examples.py
python3 conformance_validator.py --suite conformance-tests/cgam-conformance-v0.1.0.yaml
python3 tools/verify_integrity.py --strict --verify-git-history
python3 tools/verify_publication_claims.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

CI installs `jsonschema` and `pyyaml` and runs these checks. Add or update conformance fixtures and unit tests for every behavior change, including rejection and unresolved-reference cases.

## Coding and Contract Style

Match existing Python and document style: 4-space indentation, explicit types where useful, stable schema IDs, deterministic output, and fail-closed error handling. Keep receipts bounded; never place raw prompts, tool payloads, credentials, or private memory in them.

## Authority and Security Boundaries

Dangerous operations are denied by default. No worker may widen its own grant, write memory without the Memory Gate, act without the required witness path, or convert a checker PASS into permission. JWS/RS256 verification, hashes, mirrors, and receipts provide bounded evidence only; they do not prove truth, identity, continuity, or sovereignty.

Reuse mature sandboxing, workload identity, authorization, and transaction primitives. Do not create a general framework unless a named CGAM requirement cannot be satisfied otherwise.

## Commits and Pull Requests

Use short imperative subjects, commonly `docs:`, `fix:`, `test:`, or `chore:`. PRs must include the threat/failure model, exact tests run, affected contracts or fixtures, compatibility impact, evidence produced, remaining limitations, and explicit non-claims. Do not merge, tag, publish, deploy, or start the next gate without separate authorization.
