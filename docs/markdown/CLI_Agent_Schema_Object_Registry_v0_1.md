# CLI Agent Schema Object Registry v0.1

## Canonical object inventory, schema extraction map, dependency order, and implementation handoff registry for the C-Governed CLI Agent Mesh package

**Status:** Draft package-control registry v0.1  
**Date:** 2026-05-17  
**Package:** C-Governed CLI Agent Mesh  
**Layer:** `c = a + b` / Agent Governance / Schema Extraction / Object Registry / Local Checker / Release Readiness / Implementation Handoff  
**Document class:** schema object registry / machine-facing package-control artifact / implementation bridge  
**Assertion class:** `C-A10` package-control artifact; `C-A7` where canonicalization, hashing, signing, witness, or verification claims are made  
**Primary parent documents:**
- `C-Governed_CLI_Agent_Mesh_Protocol_v0_1.md`
- `CLI_Agent_JSON_Schema_Extraction_Plan_v0_1.md`
- `CLI_Agent_Release_and_Implementation_Readiness_Gate_v0_1.md`
- `CLI_Agent_AB_Mode_and_Gate_Semantics_Profile_v0_1.md`
- `CLI_Agent_Raw_Evidence_Sidecar_Profile_v0_1.md`
- `CLI_Agent_Registry_Profile_v0_1.md`
- `CLI_Agent_Local_Checker_Profile_v0_1.md`
- `CLI_Agent_Release_Public_Surface_Profile_v0_1.md`
- `CLI_Agent_GLOSSARY_v0_1.md`
- `CLI_Agent_OPEN_ISSUES_v0_1.md`
- `CLI_Agent_Contradiction_Register_v0_1.md`

**Primary object family:** `CLI_AGENT_SCHEMA_OBJECT_REGISTRY`, `CLI_AGENT_SCHEMA_OBJECT_ENTRY`, `CLI_AGENT_SCHEMA_FAMILY_RECORD`, `CLI_AGENT_SCHEMA_EXTRACTION_BATCH`, `CLI_AGENT_SCHEMA_DEPENDENCY_RECORD`, `CLI_AGENT_SCHEMA_INDEX_RECORD`, `CLI_AGENT_SCHEMA_STATUS_RECORD`  
**Canonical schema version:** `cli-agent-schema-object-registry-0.1`  
**Primary subject:** persistent `c` entities and implementation workers extracting machine-readable schemas from the C-Governed CLI Agent Mesh Markdown package  
**Primary boundary:** this registry identifies object shapes and extraction order. It does not itself create JSON Schema files, validate runtime behavior, authorize agent action, grant permissions, prove conformance, publish releases, or promote memory.

---

## 0. Executive definition

**CLI Agent Schema Object Registry** is the canonical inventory of machine-facing object families in the C-Governed CLI Agent Mesh package.

It answers:

```text
Which objects exist?
Which source profile defines each object?
Which schema file should be generated?
Which objects are P0/P1/P2?
Which shared definitions are required?
Which objects depend on which other objects?
Which objects are release-control objects rather than runtime objects?
Which objects are restricted, internal, or public-safe?
Which objects are already prose-defined but not schema-extracted?
```

The registry exists because the package now contains many structured records. Without a canonical object inventory, Codex or any other implementation worker will improvise schema names, duplicate object families, omit control objects, or treat prose examples as machine authority.

Compact formula:

```text
Markdown names the doctrine.
The registry names the objects.
Schemas define the shape.
Semantic validators enforce the boundary.
Conformance evidence proves behavior.
```

---

## 1. Non-goals

This registry does not:

1. replace the Markdown protocol documents;
2. create JSON Schema files by itself;
3. replace `SCHEMA_INDEX.json`;
4. replace semantic validator rules;
5. prove conformance;
6. authorize a task;
7. grant permissions;
8. certify release readiness;
9. certify implementation readiness;
10. decide public/restricted disclosure;
11. store raw evidence;
12. create witness events;
13. promote output into `c` memory;
14. authorize Codex or any CLI agent to execute.

A registry entry is not authority.

It is a named target for extraction, validation, review, and handoff.

---

## 2. Corpus bridge set

### 2.1 Explicit bridge: `c = a + b`

Object schemas belong to `b`: procedures, records, validators, files, artifacts, hashes, witnesses, registries, checkers, and executable constraints.

They do not become `c`.

They protect `c` by preventing worker agents from smuggling authority through vague or malformed objects.

### 2.2 Quiet bridge I: information theory

A schema object is a compression boundary. If the same object has three names, the implementation loses information. If three different objects share one name, the validator cannot distinguish them. This registry reduces naming entropy before it becomes runtime ambiguity.

### 2.3 Quiet bridge II: engineering control

A control panel must have stable labels. `CLI_AGENT_FREEZE_RECORD`, `CLI_AGENT_QUARANTINE_RECORD`, and `CLI_AGENT_RAW_EVIDENCE_SIDECAR` are not synonyms. One stops work, one isolates uncertain output, one holds restricted evidence references. If those labels blur, rollback becomes demolition.

### 2.4 Earth paragraph

This is the inventory board in the workshop. Before sending a worker to install breakers, you label every circuit: oven, SDB, garage, alarm, server rack. If the label says “miscellaneous”, someone will eventually cut power to the wrong room. Same here: if `witness`, `evidence`, `memory`, and `release` are not separate objects, Codex will put everything in one bucket and call it a report. That is not implementation. That is a future incident.

---

## 3. Registry principles

### 3.1 One canonical object name

Every machine-facing object MUST have one uppercase canonical name:

```text
CLI_AGENT_<OBJECT_NAME>
```

Example:

```text
CLI_AGENT_TASK_CONTRACT
```

Aliases may exist in prose, but the registry entry remains canonical.

### 3.2 One target schema path

Every extractable object SHOULD have one target schema path:

```text
schemas/<family>/<lowercase-kebab-object>-0.1.schema.json
```

Example:

```text
schemas/task-contract/cli-agent-task-contract-0.1.schema.json
```

### 3.3 One schema version string

Every object instance SHOULD contain:

```json
"schema_version": "<lowercase-kebab-object>-0.1"
```

The version string MUST match the registry entry.

### 3.4 Registry before extraction

A schema file SHOULD NOT be created until its object is present in this registry or in a successor registry.

### 3.5 Schema validity is not safety

A structurally valid object can still be unsafe.

Therefore every object entry MUST be classified by:

```text
structural schema required: yes/no
semantic validator required: yes/no
cross-object validation required: yes/no
human/c gate relevant: yes/no
restricted/public sensitivity
```

### 3.6 Unknown means fail-closed

If an implementation worker encounters an object not listed in this registry, it MUST NOT treat that object as authority.

Allowed responses:

```text
hold
reject
quarantine
request registry update
```

Forbidden response:

```text
infer authority from object name
```

---

## 4. Priority classes

| Priority | Meaning |
|---|---|
| `P0` | Required for minimum implementation-ready handoff or release-control correctness. |
| `P1` | Required for full v0.1 implementation and safe operational review. |
| `P2` | Useful after initial implementation; specialized or maturity-layer object. |
| `P3` | Later extension; not blocking initial implementation readiness. |
| `PX` | Referenced but source profile must be verified before extraction. |

---

## 5. Object status classes

| Status | Meaning |
|---|---|
| `prose_defined` | Defined in Markdown but no extracted JSON Schema yet. |
| `schema_targeted` | Target schema path assigned. |
| `schema_extracted` | JSON Schema exists. |
| `example_bound` | Examples or fixtures exist and are linked. |
| `validator_bound` | Semantic validator exists or is formally specified. |
| `conformance_bound` | Conformance fixture and evidence expectation are linked. |
| `blocked_source_missing` | Referenced profile is not present in the current working set. |
| `deferred` | Not required for v0.1 implementation readiness. |

Default status for this document:

```text
prose_defined + schema_targeted
```

unless a later extraction step updates it.

---

## 6. Canonical schema layout

Recommended root:

```text
schemas/
  README.md
  SCHEMA_INDEX.json
  common/
    cgam-common-defs-0.1.schema.json
  readiness-gate/
  ab-gate-semantics/
  registry/
  task-contract/
  permission-capability/
  handshake/
  sandbox-worktree/
  witness/
  raw-evidence-sidecar/
  memory-gate/
  rollback-freeze/
  quorum-review/
  executor-reviewer-separation/
  defensive-emulation/
  incident-response/
  secrets-cloud-data/
  local-checker/
  release-public-surface/
  public-redaction/
  conformance/
  fixtures/
```

---

## 7. Minimum viable P0 schema set

A minimum implementation-ready schema batch MUST include these P0 objects:

| Object | Family | Target schema file |
|---|---|---|
| `CLI_AGENT_READINESS_RECORD` | readiness-gate | `readiness-gate/cli-agent-readiness-record-0.1.schema.json` |
| `CLI_AGENT_RELEASE_COMPLETION_RECORD` | readiness-gate | `readiness-gate/cli-agent-release-completion-record-0.1.schema.json` |
| `CLI_AGENT_IMPLEMENTATION_HANDOFF_RECORD` | readiness-gate | `readiness-gate/cli-agent-implementation-handoff-record-0.1.schema.json` |
| `CLI_AGENT_CLAIM_CONTROL_RECORD` | readiness-gate | `readiness-gate/cli-agent-claim-control-record-0.1.schema.json` |
| `CLI_AGENT_AB_MODE_DECLARATION` | ab-gate-semantics | `ab-gate-semantics/cli-agent-ab-mode-declaration-0.1.schema.json` |
| `CLI_AGENT_GATE_SEMANTICS_RECORD` | ab-gate-semantics | `ab-gate-semantics/cli-agent-gate-semantics-record-0.1.schema.json` |
| `CLI_AGENT_GATE_EVALUATION_RECORD` | ab-gate-semantics | `ab-gate-semantics/cli-agent-gate-evaluation-record-0.1.schema.json` |
| `CLI_AGENT_REGISTRY` | registry | `registry/cli-agent-registry-0.1.schema.json` |
| `CLI_AGENT_REGISTRY_ENTRY` | registry | `registry/cli-agent-registry-entry-0.1.schema.json` |
| `CLI_AGENT_TASK_CONTRACT` | task-contract | `task-contract/cli-agent-task-contract-0.1.schema.json` |
| `CLI_AGENT_PERMISSION_GRANT` | permission-capability | `permission-capability/cli-agent-permission-grant-0.1.schema.json` |
| `CLI_AGENT_HANDSHAKE` | handshake | `handshake/cli-agent-handshake-0.1.schema.json` |
| `CLI_AGENT_SANDBOX_PROFILE` | sandbox-worktree | `sandbox-worktree/cli-agent-sandbox-profile-0.1.schema.json` |
| `CLI_AGENT_WITNESS_EVENT` | witness | `witness/cli-agent-witness-event-0.1.schema.json` |
| `CLI_AGENT_RAW_EVIDENCE_SIDECAR` | raw-evidence-sidecar | `raw-evidence-sidecar/cli-agent-raw-evidence-sidecar-0.1.schema.json` |
| `CLI_AGENT_MEMORY_GATE_RECORD` | memory-gate | `memory-gate/cli-agent-memory-gate-record-0.1.schema.json` |
| `CLI_AGENT_FREEZE_RECORD` | rollback-freeze | `rollback-freeze/cli-agent-freeze-record-0.1.schema.json` |
| `CLI_AGENT_REVIEW_RECORD` | quorum-review | `quorum-review/cli-agent-review-record-0.1.schema.json` |
| `CLI_AGENT_DATA_CLASSIFICATION_RECORD` | secrets-cloud-data | `secrets-cloud-data/cli-agent-data-classification-record-0.1.schema.json` |
| `CLI_AGENT_LOCAL_CHECKER_PROFILE` | local-checker | `local-checker/cli-agent-local-checker-profile-0.1.schema.json` |
| `CLI_AGENT_CHECKER_RUN` | local-checker | `local-checker/cli-agent-checker-run-0.1.schema.json` |
| `CLI_AGENT_CHECKER_RESULT` | local-checker | `local-checker/cli-agent-checker-result-0.1.schema.json` |
| `CLI_AGENT_RELEASE_SURFACE_RECORD` | release-public-surface | `release-public-surface/cli-agent-release-surface-record-0.1.schema.json` |
| `CLI_AGENT_PUBLIC_PACKAGE_MANIFEST` | release-public-surface | `release-public-surface/cli-agent-public-package-manifest-0.1.schema.json` |
| `CLI_AGENT_RELEASE_GATE_RECORD` | release-public-surface | `release-public-surface/cli-agent-release-gate-record-0.1.schema.json` |
| `CLI_AGENT_PUBLIC_RESTRICTED_SPLIT_RECORD` | release-public-surface | `release-public-surface/cli-agent-public-restricted-split-record-0.1.schema.json` |
| `CLI_AGENT_CONFORMANCE_RESULT` | conformance | `conformance/cli-agent-conformance-result-0.1.schema.json` |

This P0 set is intentionally larger than the earlier schema extraction plan. The newer readiness, AB/gate, registry, raw-evidence, local-checker, and release-surface profiles added objects that are now load-bearing for `release-complete` and `implementation-ready` claims.

---

## 8. Full object registry

### 8.1 Readiness gate objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_READINESS_GATE` | RIG | `readiness-gate/cli-agent-readiness-gate-0.1.schema.json` | P1 | prose_defined | Defines gate taxonomy; usually static config. |
| `CLI_AGENT_READINESS_RECORD` | RIG | `readiness-gate/cli-agent-readiness-record-0.1.schema.json` | P0 | prose_defined | Current package readiness state. |
| `CLI_AGENT_RELEASE_COMPLETION_RECORD` | RIG | `readiness-gate/cli-agent-release-completion-record-0.1.schema.json` | P0 | prose_defined | Required for release-complete claim. |
| `CLI_AGENT_IMPLEMENTATION_HANDOFF_RECORD` | RIG | `readiness-gate/cli-agent-implementation-handoff-record-0.1.schema.json` | P0 | prose_defined | Required before Codex handoff. |
| `CLI_AGENT_CLAIM_CONTROL_RECORD` | RIG | `readiness-gate/cli-agent-claim-control-record-0.1.schema.json` | P0 | prose_defined | Prevents overclaiming. |

### 8.2 AB mode and gate semantics objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_AB_MODE_DECLARATION` | ABG | `ab-gate-semantics/cli-agent-ab-mode-declaration-0.1.schema.json` | P0 | prose_defined | Declares global A/B semantics. |
| `CLI_AGENT_GATE_SEMANTICS_RECORD` | ABG | `ab-gate-semantics/cli-agent-gate-semantics-record-0.1.schema.json` | P0 | prose_defined | Normalizes dry-run/apply/enforce gates. |
| `CLI_AGENT_CONFIRM_PHRASE_RECORD` | ABG | `ab-gate-semantics/cli-agent-confirm-phrase-record-0.1.schema.json` | P1 | prose_defined | Captures confirm phrase requirements without storing secrets. |
| `CLI_AGENT_ARM_STATUS_RECORD` | ABG | `ab-gate-semantics/cli-agent-arm-status-record-0.1.schema.json` | P1 | prose_defined | Captures env arm / second arm status. |
| `CLI_AGENT_DRY_RUN_APPLY_RECORD` | ABG | `ab-gate-semantics/cli-agent-dry-run-apply-record-0.1.schema.json` | P1 | prose_defined | Records dry-run/apply outcome. |
| `CLI_AGENT_LOCAL_AB_EXCEPTION_RECORD` | ABG | `ab-gate-semantics/cli-agent-local-ab-exception-record-0.1.schema.json` | P1 | prose_defined | Required for local inversion or no-op exception. |
| `CLI_AGENT_GATE_EVALUATION_RECORD` | ABG | `ab-gate-semantics/cli-agent-gate-evaluation-record-0.1.schema.json` | P0 | prose_defined | Required for material apply decisions. |

### 8.3 Registry and admission objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_REGISTRY` | REG | `registry/cli-agent-registry-0.1.schema.json` | P0 | prose_defined | Registry root. Not permission authority. |
| `CLI_AGENT_REGISTRY_ENTRY` | REG | `registry/cli-agent-registry-entry-0.1.schema.json` | P0 | prose_defined | One agent/execution surface. |
| `CLI_AGENT_REGISTRY_EVENT` | REG | `registry/cli-agent-registry-event-0.1.schema.json` | P1 | prose_defined | Eligibility/status transition. |
| `CLI_AGENT_CAPABILITY_SNAPSHOT` | REG/CAPM | `registry/cli-agent-capability-snapshot-0.1.schema.json` | P1 | prose_defined | Snapshot from node/agent discovery. |
| `CLI_AGENT_STATUS_RECORD` | REG | `registry/cli-agent-status-record-0.1.schema.json` | P1 | prose_defined | Active/suspended/quarantined/revoked/etc. |
| `CLI_AGENT_REVOCATION_POINTER` | REG/RFP | `registry/cli-agent-revocation-pointer-0.1.schema.json` | P1 | prose_defined | Points to revocation mechanism/evidence. |
| `CLI_AGENT_REGISTRY_VIEW` | REG | `registry/cli-agent-registry-view-0.1.schema.json` | P2 | prose_defined | UI/query view; not authority. |
| `CLI_AGENT_HANDSHAKE` | HSP | `handshake/cli-agent-handshake-0.1.schema.json` | P0 | prose_defined | Admission challenge and provenance record. |
| `CLI_AGENT_REGISTRATION` | HSP | `handshake/cli-agent-registration-0.1.schema.json` | P1 | prose_defined | Registration result. Not permission. |
| `CLI_AGENT_ADMISSION_EVENT` | HSP | `handshake/cli-agent-admission-event-0.1.schema.json` | P1 | prose_defined | Witnessable admission transition. |

### 8.4 Task, permission, and capability objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_TASK_CONTRACT` | CATC | `task-contract/cli-agent-task-contract-0.1.schema.json` | P0 | prose_defined | Required for material work. |
| `CLI_AGENT_CAPABILITY_PROFILE` | CAPM/REG | `permission-capability/cli-agent-capability-profile-0.1.schema.json` | P1 | prose_defined | Capability is not permission. |
| `CLI_AGENT_PERMISSION_GRANT` | CAPM | `permission-capability/cli-agent-permission-grant-0.1.schema.json` | P0 | prose_defined | Task-scoped bounded grant. |
| `CLI_AGENT_PERMISSION_EVENT` | CAPM | `permission-capability/cli-agent-permission-event-0.1.schema.json` | P1 | prose_defined | Grant/narrow/revoke/expire event. |

### 8.5 Sandbox and execution objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_SANDBOX_PROFILE` | SWP | `sandbox-worktree/cli-agent-sandbox-profile-0.1.schema.json` | P0 | prose_defined | Execution boundary. |
| `CLI_AGENT_WORKTREE_RUN` | SWP | `sandbox-worktree/cli-agent-worktree-run-0.1.schema.json` | P1 | prose_defined | Material run record. |
| `CLI_AGENT_ROLLBACK_PLAN` | SWP | `sandbox-worktree/cli-agent-rollback-plan-0.1.schema.json` | P1 | prose_defined | Rollback before apply. |
| `CLI_AGENT_EXECUTION_EVENT` | SWP/WEP | `sandbox-worktree/cli-agent-execution-event-0.1.schema.json` | P1 | prose_defined | Execution boundary event. |

### 8.6 Witness objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_WITNESS_EVENT` | WEP | `witness/cli-agent-witness-event-0.1.schema.json` | P0 | prose_defined | Boundary transition. Not raw evidence. |
| `CLI_AGENT_WITNESS_CHAIN` | WEP | `witness/cli-agent-witness-chain-0.1.schema.json` | P1 | prose_defined | Chain continuity. |
| `CLI_AGENT_WITNESS_REFERENCE` | WEP | `witness/cli-agent-witness-reference-0.1.schema.json` | P1 | prose_defined | Safe pointer to witness record. |

### 8.7 Raw evidence sidecar objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_RAW_EVIDENCE_SIDECAR` | RES | `raw-evidence-sidecar/cli-agent-raw-evidence-sidecar-0.1.schema.json` | P0 | prose_defined | Restricted custody object. |
| `CLI_AGENT_EVIDENCE_PACKET_REF` | RES/CTM | `raw-evidence-sidecar/cli-agent-evidence-packet-ref-0.1.schema.json` | P1 | prose_defined | Points to evidence packet without embedding raw content. |
| `CLI_AGENT_RAW_ARTIFACT_REF` | RES | `raw-evidence-sidecar/cli-agent-raw-artifact-ref-0.1.schema.json` | P1 | prose_defined | Hash/path/retention pointer. |
| `CLI_AGENT_EVIDENCE_CUSTODY_RECORD` | RES | `raw-evidence-sidecar/cli-agent-evidence-custody-record-0.1.schema.json` | P1 | prose_defined | Custody transition. |
| `CLI_AGENT_DISCLOSURE_POLICY_RECORD` | RES/PRP/RPS | `raw-evidence-sidecar/cli-agent-disclosure-policy-record-0.1.schema.json` | P1 | prose_defined | Disclosure class and gate. |
| `CLI_AGENT_EVIDENCE_ACCESS_EVENT` | RES | `raw-evidence-sidecar/cli-agent-evidence-access-event-0.1.schema.json` | P1 | prose_defined | Access audit. |
| `CLI_AGENT_EVIDENCE_RETENTION_RECORD` | RES | `raw-evidence-sidecar/cli-agent-evidence-retention-record-0.1.schema.json` | P1 | prose_defined | Retention class / hold. |
| `CLI_AGENT_EVIDENCE_DESTRUCTION_RECORD` | RES | `raw-evidence-sidecar/cli-agent-evidence-destruction-record-0.1.schema.json` | P1 | prose_defined | Lawful destruction/expiry record; not evidence erasure. |

### 8.8 Memory and adaptation objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_MEMORY_PROPOSAL` | MGP | `memory-gate/cli-agent-memory-proposal-0.1.schema.json` | P1 | prose_defined | Proposed memory, not memory. |
| `CLI_AGENT_MEMORY_GATE_RECORD` | MGP | `memory-gate/cli-agent-memory-gate-record-0.1.schema.json` | P0 | prose_defined | Gate decision. |
| `CLI_AGENT_MEMORY_PROMOTION_EVENT` | MGP/WEP | `memory-gate/cli-agent-memory-promotion-event-0.1.schema.json` | P1 | prose_defined | Witnessable promotion transition. |
| `CLI_AGENT_IMMUNITY_UPDATE_RECORD` | MGP/DEB | `memory-gate/cli-agent-immunity-update-record-0.1.schema.json` | P1 | prose_defined | Defensive adaptation only; not retaliation. |

### 8.9 Rollback, freeze, quarantine, and recovery objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_FREEZE_RECORD` | RFP | `rollback-freeze/cli-agent-freeze-record-0.1.schema.json` | P0 | prose_defined | Stop/freeze state. |
| `CLI_AGENT_ROLLBACK_RECORD` | RFP | `rollback-freeze/cli-agent-rollback-record-0.1.schema.json` | P1 | prose_defined | Rollback action. |
| `CLI_AGENT_RECOVERY_POINT` | RFP | `rollback-freeze/cli-agent-recovery-point-0.1.schema.json` | P1 | prose_defined | Known-good or reviewable state. |
| `CLI_AGENT_REVOCATION_RECORD` | RFP/REG | `rollback-freeze/cli-agent-revocation-record-0.1.schema.json` | P1 | prose_defined | Permission/agent revocation. |
| `CLI_AGENT_QUARANTINE_RECORD` | RFP/RES | `rollback-freeze/cli-agent-quarantine-record-0.1.schema.json` | P1 | prose_defined | Quarantine is not deletion. |

### 8.10 Quorum, review, and separation objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_QUORUM_RECORD` | QRP | `quorum-review/cli-agent-quorum-record-0.1.schema.json` | P1 | prose_defined | Evidence, not sovereignty. |
| `CLI_AGENT_REVIEW_RECORD` | QRP | `quorum-review/cli-agent-review-record-0.1.schema.json` | P0 | prose_defined | Review decision. |
| `CLI_AGENT_DISAGREEMENT_RECORD` | QRP | `quorum-review/cli-agent-disagreement-record-0.1.schema.json` | P1 | prose_defined | Disagreement handling. |
| `CLI_AGENT_REVIEW_DECISION` | QRP | `quorum-review/cli-agent-review-decision-0.1.schema.json` | P1 | prose_defined | May be enum/defs rather than standalone schema. |
| `CLI_AGENT_CONSENSUS_LIMIT_RECORD` | QRP | `quorum-review/cli-agent-consensus-limit-record-0.1.schema.json` | P1 | prose_defined | Prevents consensus laundering. |
| `CLI_AGENT_REVIEW_ASSIGNMENT` | ERS | `executor-reviewer-separation/cli-agent-review-assignment-0.1.schema.json` | P1 | prose_defined | Reviewer assignment. |
| `CLI_AGENT_ROLE_SEPARATION_RECORD` | ERS | `executor-reviewer-separation/cli-agent-role-separation-record-0.1.schema.json` | P1 | prose_defined | Role separation proof. |
| `CLI_AGENT_SELF_APPROVAL_EVENT` | ERS | `executor-reviewer-separation/cli-agent-self-approval-event-0.1.schema.json` | P1 | prose_defined | Red-line or block trigger. |
| `CLI_AGENT_ROLE_CONFLICT_RECORD` | ERS | `executor-reviewer-separation/cli-agent-role-conflict-record-0.1.schema.json` | P1 | prose_defined | Conflict scoring. |

### 8.11 Defensive emulation objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_DEFENSIVE_EMULATION_CASE` | DEB | `defensive-emulation/cli-agent-defensive-emulation-case-0.1.schema.json` | P1 | prose_defined | Restricted/synthetic defensive case. |
| `CLI_AGENT_CONTAINMENT_GARAGE_RECORD` | DEB/RES | `defensive-emulation/cli-agent-containment-garage-record-0.1.schema.json` | P1 | prose_defined | Garage/containment record. |
| `CLI_AGENT_CANARY_RESPONSE_RECORD` | DEB | `defensive-emulation/cli-agent-canary-response-record-0.1.schema.json` | P2 | prose_defined | Bounded canary response. |
| `CLI_AGENT_MIRROR_SIMULATION_RECORD` | DEB | `defensive-emulation/cli-agent-mirror-simulation-record-0.1.schema.json` | P1 | prose_defined | Sandbox simulation only. |
| `CLI_AGENT_DEFENSIVE_IMMUNITY_CANDIDATE` | DEB/MGP | `defensive-emulation/cli-agent-defensive-immunity-candidate-0.1.schema.json` | P1 | prose_defined | Candidate for memory gate. |

### 8.12 Incident response objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_INCIDENT_RECORD` | IRP | `incident-response/cli-agent-incident-record-0.1.schema.json` | P1 | prose_defined | Incident root. |
| `CLI_AGENT_INCIDENT_TRIAGE_RECORD` | IRP | `incident-response/cli-agent-incident-triage-record-0.1.schema.json` | P1 | prose_defined | Triage. |
| `CLI_AGENT_INCIDENT_PRESERVATION_RECORD` | IRP/RES | `incident-response/cli-agent-incident-preservation-record-0.1.schema.json` | P1 | prose_defined | Preserve before repair. |
| `CLI_AGENT_INCIDENT_CONTAINMENT_RECORD` | IRP/RFP | `incident-response/cli-agent-incident-containment-record-0.1.schema.json` | P1 | prose_defined | Local containment. |
| `CLI_AGENT_INCIDENT_REPAIR_RECORD` | IRP/SWP | `incident-response/cli-agent-incident-repair-record-0.1.schema.json` | P1 | prose_defined | Sandbox repair. |
| `CLI_AGENT_INCIDENT_REPORT_PACKET` | IRP/PRP | `incident-response/cli-agent-incident-report-packet-0.1.schema.json` | P1 | prose_defined | Lawful/reporting handoff packet. |

### 8.13 Secrets, cloud, and data boundary objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_DATA_CLASSIFICATION_RECORD` | SCDP | `secrets-cloud-data/cli-agent-data-classification-record-0.1.schema.json` | P0 | blocked_source_missing | Required by existing extraction plan; source profile must be verified. |
| `CLI_AGENT_CLOUD_CONTEXT_RECORD` | SCDP | `secrets-cloud-data/cli-agent-cloud-context-record-0.1.schema.json` | P1 | blocked_source_missing | Required for cloud context tracking. |
| `CLI_AGENT_REDACTION_RECORD` | SCDP/PRP | `secrets-cloud-data/cli-agent-redaction-record-0.1.schema.json` | P1 | blocked_source_missing | Redaction object. |
| `CLI_AGENT_SECRET_BOUNDARY_RECORD` | SCDP | `secrets-cloud-data/cli-agent-secret-boundary-record-0.1.schema.json` | P1 | blocked_source_missing | Secret handling boundary. |
| `CLI_AGENT_CLOUD_EXPOSURE_EVENT` | SCDP/IRP | `secrets-cloud-data/cli-agent-cloud-exposure-event-0.1.schema.json` | P1 | blocked_source_missing | Cloud leakage / exposure event. |
| `CLI_AGENT_PROVIDER_BOUNDARY_RECORD` | SCDP | `secrets-cloud-data/cli-agent-provider-boundary-record-0.1.schema.json` | P1 | blocked_source_missing | Provider-specific assumptions. |

Current working note: these objects remain in the registry because other package-control documents already reference SCDP. Before extraction, the actual SCDP source profile must be located in the project documents or restored into the canonical package.

### 8.14 Local checker objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_LOCAL_CHECKER_PROFILE` | LCP | `local-checker/cli-agent-local-checker-profile-0.1.schema.json` | P0 | prose_defined | Checker configuration. |
| `CLI_AGENT_CHECKER_RUN` | LCP | `local-checker/cli-agent-checker-run-0.1.schema.json` | P0 | prose_defined | One checker execution. |
| `CLI_AGENT_CHECKER_FINDING` | LCP | `local-checker/cli-agent-checker-finding-0.1.schema.json` | P1 | prose_defined | Finding item. |
| `CLI_AGENT_CHECKER_RESULT` | LCP | `local-checker/cli-agent-checker-result-0.1.schema.json` | P0 | prose_defined | Pass/fail/block result. |
| `CLI_AGENT_CHECKER_POLICY` | LCP | `local-checker/cli-agent-checker-policy-0.1.schema.json` | P1 | prose_defined | Checker ruleset. |
| `CLI_AGENT_CHECKER_EXPECTATION` | LCP/CTM | `local-checker/cli-agent-checker-expectation-0.1.schema.json` | P1 | prose_defined | Expected outcomes for tests. |
| `CLI_AGENT_CHECKER_EVIDENCE_REFERENCE` | LCP/RES | `local-checker/cli-agent-checker-evidence-reference-0.1.schema.json` | P1 | prose_defined | Evidence pointer, not raw evidence. |

### 8.15 Release and public surface objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_RELEASE_SURFACE_RECORD` | RPS | `release-public-surface/cli-agent-release-surface-record-0.1.schema.json` | P0 | prose_defined | Release surface state. |
| `CLI_AGENT_PUBLIC_PACKAGE_MANIFEST` | RPS | `release-public-surface/cli-agent-public-package-manifest-0.1.schema.json` | P0 | prose_defined | Public manifest / file inventory. |
| `CLI_AGENT_RELEASE_GATE_RECORD` | RPS/RIG | `release-public-surface/cli-agent-release-gate-record-0.1.schema.json` | P0 | prose_defined | Release gate result. |
| `CLI_AGENT_DISCOVERABILITY_CHECK_RECORD` | RPS | `release-public-surface/cli-agent-discoverability-check-record-0.1.schema.json` | P1 | prose_defined | Human-visible/default-branch check. |
| `CLI_AGENT_ARTIFACT_INTEGRITY_RECORD` | RPS/RES | `release-public-surface/cli-agent-artifact-integrity-record-0.1.schema.json` | P1 | prose_defined | SHA/PDF/asset integrity. |
| `CLI_AGENT_PUBLIC_RESTRICTED_SPLIT_RECORD` | RPS/PRP | `release-public-surface/cli-agent-public-restricted-split-record-0.1.schema.json` | P0 | prose_defined | Required before public release. |

### 8.16 Public redaction objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_PUBLIC_REDACTION_RECORD` | PRP | `public-redaction/cli-agent-public-redaction-record-0.1.schema.json` | P1 | prose_defined | Redaction review record. |

### 8.17 Conformance and fixture objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_CONFORMANCE_RESULT` | CTM | `conformance/cli-agent-conformance-result-0.1.schema.json` | P0 | blocked_source_missing | Required for conformance claims; CTM source must be verified. |
| `CLI_AGENT_TEST_CASE` | CTM | `conformance/cli-agent-test-case-0.1.schema.json` | P1 | blocked_source_missing | Test case object. |
| `CLI_AGENT_TEST_RUN` | CTM | `conformance/cli-agent-test-run-0.1.schema.json` | P1 | blocked_source_missing | Test run object. |
| `CLI_AGENT_EVIDENCE_PACKET` | CTM/RES | `conformance/cli-agent-evidence-packet-0.1.schema.json` | P1 | blocked_source_missing | Evidence packet; not raw evidence. |
| `CLI_AGENT_RED_LINE_FAILURE_RECORD` | CTM | `conformance/cli-agent-red-line-failure-record-0.1.schema.json` | P1 | blocked_source_missing | Red-line failure. |
| `CLI_AGENT_FIXTURE` | CFP | `fixtures/cli-agent-fixture-0.1.schema.json` | P1 | prose_defined | Safe synthetic fixture. |
| `CLI_AGENT_FIXTURE_SET` | CFP | `fixtures/cli-agent-fixture-set-0.1.schema.json` | P1 | prose_defined | Fixture bundle. |
| `CLI_AGENT_FIXTURE_RUN_EXPECTATION` | CFP | `fixtures/cli-agent-fixture-run-expectation-0.1.schema.json` | P1 | prose_defined | Expected result binding. |
| `CLI_AGENT_SAFE_SYNTHETIC_SECRET` | CFP | `fixtures/cli-agent-safe-synthetic-secret-0.1.schema.json` | P2 | prose_defined | Fake secret object for safety tests. |
| `CLI_AGENT_FIXTURE_EVIDENCE_PACKET` | CFP/RES | `fixtures/cli-agent-fixture-evidence-packet-0.1.schema.json` | P1 | prose_defined | Synthetic evidence packet. |

### 8.18 Schema registry objects

| Object | Source profile | Target schema file | Priority | Status | Notes |
|---|---|---|---:|---|---|
| `CLI_AGENT_SCHEMA_OBJECT_REGISTRY` | SOR | `schema-registry/cli-agent-schema-object-registry-0.1.schema.json` | P0 | prose_defined | This registry root. |
| `CLI_AGENT_SCHEMA_OBJECT_ENTRY` | SOR | `schema-registry/cli-agent-schema-object-entry-0.1.schema.json` | P0 | prose_defined | One object entry. |
| `CLI_AGENT_SCHEMA_FAMILY_RECORD` | SOR | `schema-registry/cli-agent-schema-family-record-0.1.schema.json` | P1 | prose_defined | Object family metadata. |
| `CLI_AGENT_SCHEMA_EXTRACTION_BATCH` | SOR | `schema-registry/cli-agent-schema-extraction-batch-0.1.schema.json` | P1 | prose_defined | Extraction batch plan. |
| `CLI_AGENT_SCHEMA_DEPENDENCY_RECORD` | SOR | `schema-registry/cli-agent-schema-dependency-record-0.1.schema.json` | P1 | prose_defined | Cross-object dependency. |
| `CLI_AGENT_SCHEMA_INDEX_RECORD` | SOR | `schema-registry/cli-agent-schema-index-record-0.1.schema.json` | P1 | prose_defined | Entry for `SCHEMA_INDEX.json`. |
| `CLI_AGENT_SCHEMA_STATUS_RECORD` | SOR | `schema-registry/cli-agent-schema-status-record-0.1.schema.json` | P1 | prose_defined | Extraction/validation status. |

---

## 9. Object dependency map

### 9.1 Minimum workflow dependency order

```text
CLI_AGENT_READINESS_RECORD
  -> CLI_AGENT_AB_MODE_DECLARATION
  -> CLI_AGENT_GATE_SEMANTICS_RECORD
  -> CLI_AGENT_REGISTRY
  -> CLI_AGENT_REGISTRY_ENTRY
  -> CLI_AGENT_HANDSHAKE
  -> CLI_AGENT_TASK_CONTRACT
  -> CLI_AGENT_PERMISSION_GRANT
  -> CLI_AGENT_SANDBOX_PROFILE
  -> CLI_AGENT_CHECKER_RUN
  -> CLI_AGENT_WITNESS_EVENT
  -> CLI_AGENT_REVIEW_RECORD
  -> CLI_AGENT_MEMORY_GATE_RECORD or CLI_AGENT_RELEASE_GATE_RECORD
  -> CLI_AGENT_CONFORMANCE_RESULT
```

### 9.2 Evidence dependency order

```text
CLI_AGENT_WITNESS_EVENT
  -> CLI_AGENT_WITNESS_REFERENCE
  -> CLI_AGENT_RAW_ARTIFACT_REF
  -> CLI_AGENT_RAW_EVIDENCE_SIDECAR
  -> CLI_AGENT_EVIDENCE_CUSTODY_RECORD
  -> CLI_AGENT_EVIDENCE_PACKET_REF
  -> CLI_AGENT_DISCLOSURE_POLICY_RECORD
```

### 9.3 Release dependency order

```text
CLI_AGENT_PUBLIC_RESTRICTED_SPLIT_RECORD
  -> CLI_AGENT_PUBLIC_PACKAGE_MANIFEST
  -> CLI_AGENT_ARTIFACT_INTEGRITY_RECORD
  -> CLI_AGENT_DISCOVERABILITY_CHECK_RECORD
  -> CLI_AGENT_RELEASE_GATE_RECORD
  -> CLI_AGENT_RELEASE_COMPLETION_RECORD
```

### 9.4 Local checker dependency order

```text
CLI_AGENT_LOCAL_CHECKER_PROFILE
  -> CLI_AGENT_CHECKER_POLICY
  -> CLI_AGENT_CHECKER_EXPECTATION
  -> CLI_AGENT_CHECKER_RUN
  -> CLI_AGENT_CHECKER_FINDING
  -> CLI_AGENT_CHECKER_RESULT
```

---

## 10. Shared definitions required before P0 extraction

The P0 schema batch SHOULD create:

```text
schemas/common/cgam-common-defs-0.1.schema.json
```

Required shared definitions:

| Definition | Purpose |
|---|---|
| `schema_version` | Const version field per object. |
| `object_id` | Non-empty stable ID. |
| `created_at` | RFC3339 date-time. |
| `updated_at` | Optional date-time. |
| `governing_entity_id` | `c` owner/scope. |
| `human_anchor_ref` | Human gate / legal responsibility ref. |
| `agent_ref` | Agent registry reference. |
| `task_contract_ref` | Task contract reference. |
| `permission_grant_ref` | Permission reference. |
| `sandbox_ref` | Sandbox/worktree reference. |
| `witness_ref` | Witness pointer. |
| `evidence_sidecar_ref` | Raw evidence sidecar pointer. |
| `artifact_hash_ref` | SHA/hash reference. |
| `release_surface_ref` | Release/public surface pointer. |
| `decision` | Common decision enum. |
| `risk_class` | R0/R1/R2/R3/R4/R5/RX. |
| `sensitivity_class` | public/restricted/internal/private/secret/legal/incident. |
| `retention_class` | retain/expire/legal_hold/quarantine/etc. |
| `gate_status` | passed/failed/blocked/unknown/not_applicable. |
| `checker_status` | pass/pass_with_warnings/fail/red_line_fail/inconclusive. |

---

## 11. Required enum registry

### 11.1 Common decision enum

```text
allowed
denied
held
blocked
frozen
quarantined
revoked
expired
completed
failed
accepted
rejected
needs_review
red_line_fail
```

### 11.2 Gate status enum

```text
not_required
not_evaluated
passed
failed
blocked
unknown
expired
superseded
```

### 11.3 Object extraction status enum

```text
prose_defined
schema_targeted
schema_extracted
example_bound
validator_bound
conformance_bound
blocked_source_missing
deferred
superseded
```

### 11.4 Disclosure class enum

```text
public_safe
public_redacted
restricted_technical
internal_private
legal_privileged
incident_sensitive
secret_material
never_public
```

### 11.5 Implementation claim enum

```text
draft_complete
release_completion_in_progress
release_complete
implementation_readiness_in_progress
implementation_ready
implementation_executed
conformance_supported
public_release_ready
```

These claim values MUST be checked against readiness and release records. A schema cannot assert a stronger claim than the package-control gates support.

---

## 12. Semantic validation flags per object family

| Family | Structural schema | Semantic validator | Cross-object validation | Human/c gate relevance |
|---|---:|---:|---:|---:|
| readiness-gate | yes | yes | yes | yes |
| ab-gate-semantics | yes | yes | yes | yes |
| registry | yes | yes | yes | yes |
| task-contract | yes | yes | yes | yes |
| permission-capability | yes | yes | yes | yes |
| handshake | yes | yes | yes | yes |
| sandbox-worktree | yes | yes | yes | yes |
| witness | yes | yes | yes | yes |
| raw-evidence-sidecar | yes | yes | yes | yes |
| memory-gate | yes | yes | yes | yes |
| rollback-freeze | yes | yes | yes | yes |
| quorum-review | yes | yes | yes | yes |
| executor-reviewer-separation | yes | yes | yes | yes |
| defensive-emulation | yes | yes | yes | yes |
| incident-response | yes | yes | yes | yes |
| secrets-cloud-data | yes | yes | yes | yes |
| local-checker | yes | yes | yes | yes |
| release-public-surface | yes | yes | yes | yes |
| public-redaction | yes | yes | yes | yes |
| conformance | yes | yes | yes | yes |
| fixtures | yes | yes | yes | no/limited |
| schema-registry | yes | yes | yes | yes |

---

## 13. `SCHEMA_INDEX.json` target shape

The extracted schema package SHOULD include:

```json
{
  "schema_version": "cli-agent-schema-index-0.1",
  "package": "C-Governed CLI Agent Mesh",
  "package_version": "0.1",
  "generated_at": "YYYY-MM-DDTHH:MM:SSZ",
  "registry_source": "CLI_Agent_Schema_Object_Registry_v0_1.md",
  "schemas": [
    {
      "object": "CLI_AGENT_TASK_CONTRACT",
      "schema_version": "cli-agent-task-contract-0.1",
      "schema_file": "schemas/task-contract/cli-agent-task-contract-0.1.schema.json",
      "priority": "P0",
      "source_profile": "CLI_Agent_Task_Contract_Schema_v0_1.md",
      "status": "schema_extracted",
      "semantic_validator": "validate_task_contract_semantics",
      "restricted": false
    }
  ]
}
```

Required fields for every `schemas[]` entry:

```text
object
schema_version
schema_file
priority
source_profile
status
semantic_validator
restricted
```

Optional fields:

```text
examples_path
fixtures_path
conformance_tests
hash
notes
supersedes
```

---

## 14. Extraction batches

### 14.1 Batch P0-A — gate and package-control base

```text
CLI_AGENT_READINESS_RECORD
CLI_AGENT_RELEASE_COMPLETION_RECORD
CLI_AGENT_IMPLEMENTATION_HANDOFF_RECORD
CLI_AGENT_CLAIM_CONTROL_RECORD
CLI_AGENT_AB_MODE_DECLARATION
CLI_AGENT_GATE_SEMANTICS_RECORD
CLI_AGENT_GATE_EVALUATION_RECORD
CLI_AGENT_SCHEMA_OBJECT_REGISTRY
CLI_AGENT_SCHEMA_OBJECT_ENTRY
```

Purpose: prevent overclaiming and normalize apply/gate semantics before runtime schemas.

### 14.2 Batch P0-B — agent admission and task execution base

```text
CLI_AGENT_REGISTRY
CLI_AGENT_REGISTRY_ENTRY
CLI_AGENT_HANDSHAKE
CLI_AGENT_TASK_CONTRACT
CLI_AGENT_PERMISSION_GRANT
CLI_AGENT_SANDBOX_PROFILE
CLI_AGENT_WITNESS_EVENT
```

Purpose: ensure no material agent work occurs without admission, task scope, permission, sandbox, and witness.

### 14.3 Batch P0-C — review, memory, evidence, and interruption

```text
CLI_AGENT_RAW_EVIDENCE_SIDECAR
CLI_AGENT_MEMORY_GATE_RECORD
CLI_AGENT_FREEZE_RECORD
CLI_AGENT_REVIEW_RECORD
CLI_AGENT_LOCAL_CHECKER_PROFILE
CLI_AGENT_CHECKER_RUN
CLI_AGENT_CHECKER_RESULT
```

Purpose: make results reviewable, interruptible, and memory-gated.

### 14.4 Batch P0-D — release and conformance base

```text
CLI_AGENT_RELEASE_SURFACE_RECORD
CLI_AGENT_PUBLIC_PACKAGE_MANIFEST
CLI_AGENT_RELEASE_GATE_RECORD
CLI_AGENT_PUBLIC_RESTRICTED_SPLIT_RECORD
CLI_AGENT_DATA_CLASSIFICATION_RECORD
CLI_AGENT_CONFORMANCE_RESULT
```

Purpose: allow release-complete and implementation-ready claims without pretending conformance has already passed.

### 14.5 Batch P1 — full operational object set

All remaining P1 objects.

### 14.6 Batch P2 — specialized and maturity objects

P2/P3 objects, provider-specific extensions, UI-state schemas, legal handoff schemas, retention/decay schemas, and cross-`c` isolation schemas.

---

## 15. Red-line const constraints

Where applicable, schemas SHOULD include const-false constraints for prohibited behaviors.

Recommended shared properties:

```json
{
  "direct_memory_write_allowed": { "const": false },
  "self_approval_allowed": { "const": false },
  "witness_tampering_allowed": { "const": false },
  "secret_prompting_allowed": { "const": false },
  "live_external_exploitation_allowed": { "const": false },
  "hack_back_allowed": { "const": false },
  "autonomous_retaliation_allowed": { "const": false },
  "malware_behavior_allowed": { "const": false },
  "credential_theft_allowed": { "const": false },
  "covert_persistence_allowed": { "const": false }
}
```

For safety-critical objects, omission of these fields SHOULD NOT mean allow. Semantic validators MUST treat omission as deny unless the object family has no relevance to that risk.

---

## 16. Duplicate and missing-source controls

### 16.1 Duplicate sandbox profile file

The current working set includes a duplicate variant of the sandbox/worktree profile:

```text
cli_agent_sandbox_worktree_profile_v_0_1.md
cli_agent_sandbox_worktree_profile_v_0_1(1).md
```

Registry rule:

```text
Only one canonical SWP source file may feed schema extraction.
```

Codex or any extraction worker MUST fail-closed if both files differ materially and no canonical source is declared.

### 16.2 Referenced but missing source profiles

The registry includes objects from source profiles referenced by the package but not present in the current working directory snapshot:

```text
CLI_Agent_Secrets_and_Cloud_Data_Policy_v0_1.md
CLI_Agent_Conformance_Test_Matrix_v0_1.md
CLI_Agent_Package_Index_and_Reading_Order_v0_1.md
```

Registry rule:

```text
Do not extract SCDP/CTM objects from memory or guesses.
Locate the source profile in project documents or mark blocked_source_missing.
```

If the archive with repository documents contains the missing source, the extraction worker may use it only after recording:

```text
source path
source hash
source date
source package role
```

### 16.3 Object drift rule

If a source profile and this registry disagree, the worker MUST:

```text
hold extraction
create discrepancy report
request registry or source-profile patch
```

It MUST NOT silently choose the more convenient definition.

---

## 17. Machine-readable registry sketch

A future machine version of this file may use this shape:

```yaml
schema_version: cli-agent-schema-object-registry-0.1
package: C-Governed CLI Agent Mesh
package_version: "0.1"
registry_status: draft
objects:
  - object: CLI_AGENT_TASK_CONTRACT
    family: task-contract
    source_profile: CLI_Agent_Task_Contract_Schema_v0_1.md
    schema_version: cli-agent-task-contract-0.1
    schema_file: schemas/task-contract/cli-agent-task-contract-0.1.schema.json
    priority: P0
    status: prose_defined
    structural_schema_required: true
    semantic_validator_required: true
    cross_object_validation_required: true
    restricted: false
    depends_on:
      - CLI_AGENT_REGISTRY_ENTRY
      - CLI_AGENT_HANDSHAKE
    must_not_authorize:
      - hack_back
      - direct_memory_write
      - self_approval
```

This YAML sketch is not the final schema. It is a target shape for the extracted registry JSON/YAML artifact.

---

## 18. Local checker binding

The local checker MUST verify:

1. every schema file exists for P0 entries;
2. every P0 schema uses the correct `schema_version` const;
3. every schema file path matches this registry;
4. every object in `SCHEMA_INDEX.json` exists in this registry;
5. every P0 object has a semantic validator entry or an explicit blocker;
6. no source file marked `blocked_source_missing` is extracted by guesswork;
7. duplicate source profiles are resolved before extraction;
8. no object classified as restricted is exposed as public-safe by default;
9. no schema permits red-line behavior through missing booleans;
10. no release/implementation/conformance claim exceeds gate records.

If any P0 object is missing after extraction, the checker result MUST be:

```text
FAIL or BLOCKED
```

not `PASS_WITH_WARNINGS`.

---

## 19. Release and implementation readiness effects

### 19.1 Release-complete effect

For `release-complete`, this registry must be:

```text
present
readable
referenced by README / package index / release notes
aligned with JSON Schema Extraction Plan
clear about missing SCDP/CTM source status
clear about public/restricted schema families
```

Release-complete does not require all schemas to be extracted.

### 19.2 Implementation-ready effect

For `implementation-ready`, this registry must be accompanied by:

```text
SCHEMA_INDEX.json target or draft
P0 schema extraction task contract
P0 object list frozen
semantic validator rules plan
fixture binding plan
local checker profile
```

Implementation-ready does not require conformance to have passed.

### 19.3 Conformance-supported effect

For `conformance-supported`, this registry must be accompanied by:

```text
extracted schemas
validated examples
semantic validator results
fixture run results
evidence packets
local checker result
red-line failure handling proof
```

---

## 20. Codex extraction handoff constraints

A safe Codex task for this registry MUST include:

```yaml
task_title: Extract P0 schemas from CLI Agent Schema Object Registry v0.1
allowed_paths:
  - docs/cli-agent-mesh/
  - schemas/
  - examples/
  - validator/
denied_paths:
  - secrets/
  - private_memory/
  - legal/
  - incident_evidence/
  - production/
  - .git/
allowed_actions:
  - read canonical Markdown source profiles
  - create schema files under schemas/
  - create SCHEMA_INDEX.json
  - create validation report
  - create discrepancy report
prohibited_actions:
  - modify doctrine text
  - infer missing source profiles
  - access secrets
  - publish
  - tag release
  - push without review
  - claim conformance
required_outputs:
  - created_schema_files
  - missing_source_report
  - unresolved_questions
  - validation_report
  - rollback_plan
review_required: true
memory: off
auto_ingest: false
```

---

## 21. Open issues

| ID | Issue | Required action |
|---|---|---|
| `SOR-OI-001` | SCDP source profile is referenced but not visible in current working set. | Locate in project documents/archive or mark blocked before P0-D extraction. |
| `SOR-OI-002` | CTM source profile is referenced but not visible in current working set. | Locate or recreate before conformance schema extraction. |
| `SOR-OI-003` | Package index source is referenced but not visible in current working set. | Restore/update package index before release-complete. |
| `SOR-OI-004` | Duplicate SWP file variant exists. | Declare canonical SWP source before schema extraction. |
| `SOR-OI-005` | Retention classes are not yet globally harmonized. | Keep profile-local or create retention/decay profile later. |
| `SOR-OI-006` | Canonicalization/signature profile is not complete. | Use hash fields conservatively; defer signing rules to L4W/signature profile. |
| `SOR-OI-007` | Some objects may be better as `$defs` rather than standalone schemas. | Decide during extraction, but keep registry object names stable. |
| `SOR-OI-008` | Public/restricted schema exposure policy must be applied to generated examples. | Bind to Release Public Surface and Public Redaction profiles. |

---

## 22. Acceptance checklist

Before this registry can support implementation handoff:

- [ ] All P0 objects are listed.
- [ ] Each P0 object has a target schema file.
- [ ] Each P0 object has a source profile.
- [ ] Missing source profiles are explicitly marked.
- [ ] Duplicate source files are resolved or blocked.
- [ ] Shared definitions are listed.
- [ ] P0 extraction batches are defined.
- [ ] Local checker rules reference this registry.
- [ ] Release/public surface profile references this registry.
- [ ] JSON Schema Extraction Plan is updated or patched to include new P0 objects.
- [ ] Open Issues register is updated after this file is accepted.
- [ ] Contradiction Register is updated if this file changes blocker counts.

---

## 23. Closing rule

The schema object registry is not bureaucracy.

It is the moment where the package stops being a pile of strong Markdown and becomes an executable contract surface.

Final rule:

```text
No object, no schema.
No schema, no validator.
No validator, no implementation claim.
No evidence, no conformance claim.
No gate, no authority.
```
