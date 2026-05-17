# CLI Agent Task Contract Schema v0.1

## Machine-readable task envelope for C-Governed CLI Agent Mesh operations

**Status:** Draft schema profile v0.1  
**Date:** 2026-05-16  
**Layer:** `c = a + b` / C-Governed CLI Agent Mesh / Task Governance / Witness / L4 Budget / Memory Gate  
**Document class:** schema profile / task contract / executable worker boundary artifact  
**Assertion class:** `C-A10` control-layer artifact; `C-A7` where hash, signature, witness, or canonicalization claims are made  
**Primary parent document:** `C-Governed_CLI_Agent_Mesh_Protocol_v0_1.md`  
**Primary object:** `CLI_AGENT_TASK_CONTRACT`  
**Canonical schema version:** `cli-agent-task-contract-0.1`  
**Primary subject:** persistent `c` entities using CLI/cloud agents as bounded executable workers  
**Primary boundary:** no CLI agent may execute material work without declared scope, permissions, data policy, execution budget, output requirements, approval rules, and failure behavior.

---

## 0. Executive definition

**CLI Agent Task Contract Schema** defines the machine-readable envelope that governs one bounded task assigned to a CLI/cloud agent under `c` governance.

A task contract answers:

```text
Who requested this task?
Which c owns the task?
Which agent is assigned?
What may the agent read?
What may the agent write?
What may the agent execute?
What data is prohibited?
May the agent use the network?
What budget applies?
What output is required?
Who reviews?
What is witnessed?
What happens on failure?
```

The schema exists to prevent executable workers from operating through vague prompts, hidden permissions, silent defaults, or post-hoc justification.

Compact formula:

```text
No task without contract.
No contract without scope.
No scope without denial rules.
No privileged transition without witness.
```

---

## 1. Purpose

CLI agents are not ordinary text responders. They may inspect files, edit repositories, run tests, create artifacts, change configuration, call tools, and influence operational state.

Therefore, a CLI agent task must be governed before execution.

This schema provides:

1. a canonical task envelope;
2. required identity and provenance fields;
3. role and capability binding;
4. allowed and denied paths;
5. command boundaries;
6. data and privacy policy;
7. network restrictions;
8. sandbox/worktree requirements;
9. L4 execution budgets;
10. output requirements;
11. approval rules;
12. witness hooks;
13. memory gate handling;
14. fail-closed behavior;
15. conformance validation rules.

---

## 2. Non-goals

This schema does not define or permit:

1. autonomous retaliation;
2. offensive cyber operations;
3. unauthorized access;
4. exploitation of live third-party systems;
5. credential theft;
6. malware behavior;
7. covert persistence;
8. evasion;
9. uncontrolled network scanning;
10. unbounded background operation;
11. direct write access to `c` core memory;
12. direct modification of identity, privilege, witness, or continuity core;
13. self-approval by the same agent that executed the work.

A valid task contract cannot authorize a prohibited action.

If a task attempts to encode a prohibited action, the contract is invalid and MUST resolve to `deny_and_quarantine`.

---

## 3. Corpus bridge set

### 3.1 Explicit bridge: `c = a + b`

In `c = a + b`, CLI agents belong to `b`: procedures, models, tools, interfaces, compute, and infrastructure.

They are not `a`.

They are not `c`.

They are bounded executable workers inside the technological substrate.

The task contract is the local law that binds one such worker to one task under `c` governance.

### 3.2 Quiet bridge I: Ashby and operational variety

A `c` operating in a complex technical environment needs multiple worker roles: reader, executor, tester, auditor, sentinel, archivist, judge-assistant. Requisite variety is useful only when each worker’s channel is bounded. The task contract increases operational variety without surrendering control.

### 3.3 Quiet bridge II: information theory and leakage control

A CLI task is an information channel. It can transform local files, private context, logs, secrets, prompts, diffs, tests, and reports into new artifacts. The task contract reduces uncontrolled leakage by declaring what data may enter, what output may leave, and what material is prohibited.

### 3.4 Earth paragraph

A work order on a real site does not say “fix the building somehow.” It names the room, the circuit, the materials, the responsible person, the lockout condition, the inspection requirement, and the sign-off path. If an electrician opens a panel outside the work order, the issue is not creativity; it is a safety violation. CLI agents need the same discipline. A vague prompt is not a permit to touch the whole system.

---

## 4. Core invariants

### 4.1 Required invariants

| ID | Invariant | Requirement |
|---|---|---|
| `TC-I01` | Contract before execution | Material agent work MUST have a task contract. |
| `TC-I02` | Explicit owner | The governing `c` or human anchor MUST be identified. |
| `TC-I03` | Explicit agent role | The agent role MUST be declared before execution. |
| `TC-I04` | Deny-by-default | Missing permission means denied. |
| `TC-I05` | Allowed paths are not enough | Denied paths MUST also be declared for material tasks. |
| `TC-I06` | Secrets denied by default | Secret access MUST be false unless narrowly authorized. |
| `TC-I07` | Cloud upload denied by default | Cloud upload MUST be false unless explicitly authorized. |
| `TC-I08` | Sandbox first | Write or execute tasks MUST require sandbox/worktree/branch isolation. |
| `TC-I09` | Network bounded | Network mode MUST be `none` or `allowlist`; unrestricted network is invalid. |
| `TC-I10` | No self-approval | `self_approval_allowed` MUST be false. |
| `TC-I11` | Witness for privilege | Privileged transitions MUST require witness. |
| `TC-I12` | Memory gate | Agent output MUST NOT write directly into `c` memory. |
| `TC-I13` | Failure is specified | Failure behavior MUST be declared. |
| `TC-I14` | Rollback is specified | Write tasks MUST include rollback requirements. |
| `TC-I15` | Red lines override contract | Prohibited actions remain prohibited even if the contract says otherwise. |

### 4.2 Minimal valid contract

A minimally valid material task contract MUST include:

```text
schema_version
task_id
requested_by
governing_entity
agent.role
agent.agent_id
objective
risk_class
scope.allowed_paths
scope.denied_paths
data_policy
network_policy
execution
output_required
approval
failure_behavior
```

---

## 5. Task risk classes

| Risk class | Meaning | Required control |
|---|---|---|
| `R0` | Read-only, harmless, public material | task contract recommended |
| `R1` | Low-risk documentation or formatting | contract + allowed paths |
| `R2` | Code, schema, build, or data transformation | sandbox + tests + reviewer |
| `R3` | Release, publication, metadata, public surface | witness + `c` gate |
| `R4` | Memory, identity, privilege, witness, continuity, or agent governance impact | witness + `c` gate + human gate |
| `R5` | Incident, legal, security-sensitive, or evidence-sensitive action | preserve evidence + human gate + restricted data policy |
| `RX` | Prohibited, offensive, unauthorized, or uncontrolled action | deny + quarantine |

### 5.1 Risk escalation rule

If multiple risk classes apply, the highest class controls.

Example:

```text
A documentation change touching public release metadata is R3, not R1.
A code fix touching privilege checks is R4, not R2.
An incident task involving logs and tokens is R5, not R2.
```

---

## 6. Agent roles

The contract MUST bind the task to one primary agent role.

Allowed roles:

```text
reader
executor
tester
auditor
archivist
sentinel
judge_assistant
orchestrator_limited
```

### 6.1 Role restrictions

| Role | May write? | May execute? | May approve? | Notes |
|---|---:|---:|---:|---|
| `reader` | no | no | no | read / summarize / compare only |
| `executor` | sandbox/branch only | bounded | no | produces patch/diff |
| `tester` | no or test-output only | tests only | no | may run allowed validation |
| `auditor` | no | no or read-only checks | no | reviews another agent’s output |
| `archivist` | controlled metadata only | validation only | no | indexes, hashes, release-control prep |
| `sentinel` | no by default | monitoring only | no | detects drift/anomaly |
| `judge_assistant` | no | no | no | advises `c`, does not decide |
| `orchestrator_limited` | no direct task mutation | dispatch only | no | routes tasks, cannot grant new privilege silently |

---

## 7. Contract object overview

Canonical object name:

```text
CLI_AGENT_TASK_CONTRACT
```

Canonical top-level fields:

```yaml
schema_version: string
contract_id: string
task_id: string
title: string
created_at: string
expires_at: string | null
status: draft | active | completed | failed | held | frozen | quarantined | revoked
requested_by: c | human_anchor | scheduled_policy | incident_policy
governing_entity: object
human_anchor: object | null
agent: object
objective: string
risk_class: R0 | R1 | R2 | R3 | R4 | R5 | RX
assertion_class: string
scope: object
data_policy: object
network_policy: object
execution: object
output_required: array
approval: object
witness: object
memory_gate: object
failure_behavior: object
red_lines: object
review: object
integrity: object
notes: object
```

---

## 8. Field definitions

### 8.1 `schema_version`

Required string.

Must equal:

```text
cli-agent-task-contract-0.1
```

### 8.2 `contract_id`

Required string.

Stable identifier for this task contract.

Recommended format:

```text
catc-YYYYMMDD-HHMMSS-shortslug
```

### 8.3 `task_id`

Required string.

Identifier used by the agent execution system.

### 8.4 `title`

Required string.

Human-readable task title.

### 8.5 `created_at`

Required timestamp.

ISO-8601 UTC recommended.

### 8.6 `expires_at`

Optional timestamp or null.

If expired, the agent MUST stop unless a new contract is issued.

### 8.7 `status`

Required enum:

```text
draft
active
completed
failed
held
frozen
quarantined
revoked
```

### 8.8 `requested_by`

Required enum:

```text
c
human_anchor
scheduled_policy
incident_policy
```

### 8.9 `governing_entity`

Required object.

Fields:

```yaml
governing_entity:
  entity_id: string
  entity_name: string
  continuity_ref: string | null
  authority_scope: local | repository | project | incident | release | memory | other
```

### 8.10 `human_anchor`

Optional object or null.

Required for `R4`, `R5`, and all high-risk approvals.

```yaml
human_anchor:
  anchor_id: string
  display_name: string
  approval_required: boolean
  legal_review_required: boolean
```

### 8.11 `agent`

Required object.

```yaml
agent:
  agent_id: string
  agent_name: string
  provider: local | openai | google | anthropic | other | unknown
  role: reader | executor | tester | auditor | archivist | sentinel | judge_assistant | orchestrator_limited
  runtime: local_cli | cloud_cli | api_agent | container_agent | hybrid
  version: string | null
  capability_profile_ref: string | null
  trust_level: untrusted | provisional | trusted_limited | trusted_high
```

A high trust level does not remove scope requirements.

### 8.12 `objective`

Required string.

Must describe the task outcome in bounded terms.

Bad:

```text
Fix everything.
```

Good:

```text
Validate Markdown links under docs/cli-agent/ and produce a patch only for broken internal links.
```

### 8.13 `assertion_class`

Required string.

Recommended values:

```text
C-A4
C-A7
C-A10
```

Other values may be used if defined by the parent corpus.

### 8.14 `scope`

Required object.

```yaml
scope:
  repository: string | null
  branch_or_worktree: string | null
  allowed_paths:
    - string
  denied_paths:
    - string
  allowed_commands:
    - string
  denied_commands:
    - string
  allowed_file_globs:
    - string
  denied_file_globs:
    - string
  max_files_touched: integer | null
  max_diff_lines: integer | null
  external_targets_allowed: false
  external_targets:
    - string
```

`external_targets_allowed` MUST be false unless the task is explicitly authorized and lawful. For this protocol v0.1, live third-party offensive testing remains prohibited.

### 8.15 `data_policy`

Required object.

```yaml
data_policy:
  classification: public | internal | private | restricted | sealed | legal_sensitive | incident_sensitive
  secrets_allowed: false
  private_memory_allowed: false
  sealed_material_allowed: false
  legal_privileged_material_allowed: false
  child_data_allowed: false
  raw_witness_evidence_allowed: false
  cloud_upload_allowed: false
  prompt_minimization_required: true
  redaction_required: true
  retention: ephemeral | operational | audit | legal_hold
  output_sanitization_required: true
```

### 8.16 `network_policy`

Required object.

```yaml
network_policy:
  mode: none | allowlist
  allowed_endpoints:
    - string
  denied_endpoints:
    - string
  package_install_allowed: false
  external_fetch_allowed: false
```

Unrestricted network is not a valid mode in v0.1.

### 8.17 `execution`

Required object.

```yaml
execution:
  sandbox_required: true
  sandbox_id: string | null
  branch_required: boolean
  container_required: boolean
  dry_run_first: boolean
  max_runtime_minutes: integer
  max_retries: integer
  max_cost_eur: number | null
  max_tokens: integer | null
  stop_on_scope_violation: true
  preserve_evidence_before_repair: boolean
  rollback_required_if_partial_write: boolean
```

### 8.18 `output_required`

Required array of enums.

Allowed values:

```text
summary
changed_files
diff
tests_run
test_results
risk_report
rollback_plan
unresolved_questions
scope_report
commands_run
hashes
witness_refs
memory_gate_recommendation
```

### 8.19 `approval`

Required object.

```yaml
approval:
  self_approval_allowed: false
  reviewer_required: true
  reviewer_agent_id: string | null
  c_gate_required: true
  human_gate_required: boolean
  legal_review_required: boolean
  merge_allowed_without_human: false
  publish_allowed_without_human: false
  deploy_allowed_without_human: false
```

For `R4` and `R5`, `human_gate_required` MUST be true.

### 8.20 `witness`

Required object.

```yaml
witness:
  witness_required: boolean
  witness_profile: none | operational | privileged | incident | release | memory_gate
  witness_event_families:
    - cli_agent.connection
    - cli_agent.permission
    - cli_agent.execution
    - cli_agent.review
    - cli_agent.memory_gate
    - cli_agent.incident
    - cli_agent.anomaly
  append_only_required: true
  hash_required: boolean
  signature_required: boolean
```

Privileged transitions require witness.

### 8.21 `memory_gate`

Required object.

```yaml
memory_gate:
  direct_memory_write_allowed: false
  memory_proposal_allowed: boolean
  proposed_memory_class: MG-0 | MG-1 | MG-2 | MG-3 | MG-4 | MG-Q | null
  c_review_required: true
  uncertainty_required: true
  quarantine_on_uncertainty: boolean
```

### 8.22 `failure_behavior`

Required object.

```yaml
failure_behavior:
  default_on_failure: hold | freeze | quarantine | rollback | deny_and_quarantine
  default_on_scope_violation: quarantine
  default_on_secret_exposure: freeze_and_escalate
  default_on_network_violation: quarantine
  default_on_missing_witness: hold
  default_on_agent_self_approval: revoke_and_quarantine
  rollback_strategy: none | revert_patch | restore_snapshot | manual_review
```

### 8.23 `red_lines`

Required object.

All fields MUST be false.

```yaml
red_lines:
  offensive_action_requested: false
  live_external_exploitation: false
  hack_back: false
  credential_theft: false
  malware_behavior: false
  covert_persistence: false
  evasion: false
  destructive_action: false
  autonomous_retaliation: false
  third_party_scanning: false
```

If any red-line field is true, the task is invalid.

### 8.24 `review`

Required object.

```yaml
review:
  independent_reviewer_required: boolean
  executor_reviewer_separation_required: boolean
  quorum_required: boolean
  quorum_profile: none | codex_gemini_local | executor_tester_auditor | custom
  disagreement_policy: accept_if_minor | hold | c_review | human_review | arl_review
```

### 8.25 `integrity`

Required object.

```yaml
integrity:
  input_hash: string | null
  contract_hash: string | null
  expected_output_hash: string | null
  canonicalization: none | json_canonicalization | yaml_canonicalization
  previous_contract_ref: string | null
  supersedes_contract_ref: string | null
```

### 8.26 `notes`

Optional object.

```yaml
notes:
  human_notes: string | null
  c_notes: string | null
  unresolved_issues:
    - string
  assumptions:
    - string
```

---

## 9. Normative JSON Schema

The following JSON Schema is the canonical v0.1 structural schema.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.local/schemas/cli-agent-task-contract-0.1.schema.json",
  "title": "CLI Agent Task Contract Schema v0.1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "contract_id",
    "task_id",
    "title",
    "created_at",
    "status",
    "requested_by",
    "governing_entity",
    "agent",
    "objective",
    "risk_class",
    "assertion_class",
    "scope",
    "data_policy",
    "network_policy",
    "execution",
    "output_required",
    "approval",
    "witness",
    "memory_gate",
    "failure_behavior",
    "red_lines",
    "review",
    "integrity"
  ],
  "properties": {
    "schema_version": {
      "const": "cli-agent-task-contract-0.1"
    },
    "contract_id": {
      "type": "string",
      "minLength": 8
    },
    "task_id": {
      "type": "string",
      "minLength": 3
    },
    "title": {
      "type": "string",
      "minLength": 3
    },
    "created_at": {
      "type": "string",
      "format": "date-time"
    },
    "expires_at": {
      "type": ["string", "null"],
      "format": "date-time"
    },
    "status": {
      "enum": ["draft", "active", "completed", "failed", "held", "frozen", "quarantined", "revoked"]
    },
    "requested_by": {
      "enum": ["c", "human_anchor", "scheduled_policy", "incident_policy"]
    },
    "governing_entity": {
      "type": "object",
      "additionalProperties": false,
      "required": ["entity_id", "entity_name", "authority_scope"],
      "properties": {
        "entity_id": { "type": "string", "minLength": 1 },
        "entity_name": { "type": "string", "minLength": 1 },
        "continuity_ref": { "type": ["string", "null"] },
        "authority_scope": {
          "enum": ["local", "repository", "project", "incident", "release", "memory", "other"]
        }
      }
    },
    "human_anchor": {
      "type": ["object", "null"],
      "additionalProperties": false,
      "required": ["anchor_id", "display_name", "approval_required", "legal_review_required"],
      "properties": {
        "anchor_id": { "type": "string" },
        "display_name": { "type": "string" },
        "approval_required": { "type": "boolean" },
        "legal_review_required": { "type": "boolean" }
      }
    },
    "agent": {
      "type": "object",
      "additionalProperties": false,
      "required": ["agent_id", "agent_name", "provider", "role", "runtime", "trust_level"],
      "properties": {
        "agent_id": { "type": "string", "minLength": 1 },
        "agent_name": { "type": "string", "minLength": 1 },
        "provider": {
          "enum": ["local", "openai", "google", "anthropic", "other", "unknown"]
        },
        "role": {
          "enum": ["reader", "executor", "tester", "auditor", "archivist", "sentinel", "judge_assistant", "orchestrator_limited"]
        },
        "runtime": {
          "enum": ["local_cli", "cloud_cli", "api_agent", "container_agent", "hybrid"]
        },
        "version": { "type": ["string", "null"] },
        "capability_profile_ref": { "type": ["string", "null"] },
        "trust_level": {
          "enum": ["untrusted", "provisional", "trusted_limited", "trusted_high"]
        }
      }
    },
    "objective": {
      "type": "string",
      "minLength": 10
    },
    "risk_class": {
      "enum": ["R0", "R1", "R2", "R3", "R4", "R5", "RX"]
    },
    "assertion_class": {
      "type": "string",
      "minLength": 2
    },
    "scope": {
      "type": "object",
      "additionalProperties": false,
      "required": ["allowed_paths", "denied_paths", "allowed_commands", "denied_commands", "external_targets_allowed"],
      "properties": {
        "repository": { "type": ["string", "null"] },
        "branch_or_worktree": { "type": ["string", "null"] },
        "allowed_paths": {
          "type": "array",
          "items": { "type": "string" },
          "minItems": 1
        },
        "denied_paths": {
          "type": "array",
          "items": { "type": "string" },
          "minItems": 1
        },
        "allowed_commands": {
          "type": "array",
          "items": { "type": "string" }
        },
        "denied_commands": {
          "type": "array",
          "items": { "type": "string" }
        },
        "allowed_file_globs": {
          "type": "array",
          "items": { "type": "string" }
        },
        "denied_file_globs": {
          "type": "array",
          "items": { "type": "string" }
        },
        "max_files_touched": { "type": ["integer", "null"], "minimum": 0 },
        "max_diff_lines": { "type": ["integer", "null"], "minimum": 0 },
        "external_targets_allowed": { "const": false },
        "external_targets": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },
    "data_policy": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "classification",
        "secrets_allowed",
        "private_memory_allowed",
        "sealed_material_allowed",
        "legal_privileged_material_allowed",
        "child_data_allowed",
        "raw_witness_evidence_allowed",
        "cloud_upload_allowed",
        "prompt_minimization_required",
        "redaction_required",
        "retention",
        "output_sanitization_required"
      ],
      "properties": {
        "classification": {
          "enum": ["public", "internal", "private", "restricted", "sealed", "legal_sensitive", "incident_sensitive"]
        },
        "secrets_allowed": { "type": "boolean" },
        "private_memory_allowed": { "type": "boolean" },
        "sealed_material_allowed": { "type": "boolean" },
        "legal_privileged_material_allowed": { "type": "boolean" },
        "child_data_allowed": { "type": "boolean" },
        "raw_witness_evidence_allowed": { "type": "boolean" },
        "cloud_upload_allowed": { "type": "boolean" },
        "prompt_minimization_required": { "type": "boolean" },
        "redaction_required": { "type": "boolean" },
        "retention": {
          "enum": ["ephemeral", "operational", "audit", "legal_hold"]
        },
        "output_sanitization_required": { "type": "boolean" }
      }
    },
    "network_policy": {
      "type": "object",
      "additionalProperties": false,
      "required": ["mode", "allowed_endpoints", "denied_endpoints", "package_install_allowed", "external_fetch_allowed"],
      "properties": {
        "mode": { "enum": ["none", "allowlist"] },
        "allowed_endpoints": {
          "type": "array",
          "items": { "type": "string" }
        },
        "denied_endpoints": {
          "type": "array",
          "items": { "type": "string" }
        },
        "package_install_allowed": { "type": "boolean" },
        "external_fetch_allowed": { "type": "boolean" }
      }
    },
    "execution": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "sandbox_required",
        "branch_required",
        "container_required",
        "dry_run_first",
        "max_runtime_minutes",
        "max_retries",
        "stop_on_scope_violation",
        "preserve_evidence_before_repair",
        "rollback_required_if_partial_write"
      ],
      "properties": {
        "sandbox_required": { "type": "boolean" },
        "sandbox_id": { "type": ["string", "null"] },
        "branch_required": { "type": "boolean" },
        "container_required": { "type": "boolean" },
        "dry_run_first": { "type": "boolean" },
        "max_runtime_minutes": { "type": "integer", "minimum": 1 },
        "max_retries": { "type": "integer", "minimum": 0, "maximum": 10 },
        "max_cost_eur": { "type": ["number", "null"], "minimum": 0 },
        "max_tokens": { "type": ["integer", "null"], "minimum": 0 },
        "stop_on_scope_violation": { "type": "boolean" },
        "preserve_evidence_before_repair": { "type": "boolean" },
        "rollback_required_if_partial_write": { "type": "boolean" }
      }
    },
    "output_required": {
      "type": "array",
      "items": {
        "enum": [
          "summary",
          "changed_files",
          "diff",
          "tests_run",
          "test_results",
          "risk_report",
          "rollback_plan",
          "unresolved_questions",
          "scope_report",
          "commands_run",
          "hashes",
          "witness_refs",
          "memory_gate_recommendation"
        ]
      },
      "minItems": 1,
      "uniqueItems": true
    },
    "approval": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "self_approval_allowed",
        "reviewer_required",
        "c_gate_required",
        "human_gate_required",
        "legal_review_required",
        "merge_allowed_without_human",
        "publish_allowed_without_human",
        "deploy_allowed_without_human"
      ],
      "properties": {
        "self_approval_allowed": { "const": false },
        "reviewer_required": { "type": "boolean" },
        "reviewer_agent_id": { "type": ["string", "null"] },
        "c_gate_required": { "type": "boolean" },
        "human_gate_required": { "type": "boolean" },
        "legal_review_required": { "type": "boolean" },
        "merge_allowed_without_human": { "type": "boolean" },
        "publish_allowed_without_human": { "type": "boolean" },
        "deploy_allowed_without_human": { "type": "boolean" }
      }
    },
    "witness": {
      "type": "object",
      "additionalProperties": false,
      "required": ["witness_required", "witness_profile", "witness_event_families", "append_only_required", "hash_required", "signature_required"],
      "properties": {
        "witness_required": { "type": "boolean" },
        "witness_profile": {
          "enum": ["none", "operational", "privileged", "incident", "release", "memory_gate"]
        },
        "witness_event_families": {
          "type": "array",
          "items": {
            "enum": [
              "cli_agent.connection",
              "cli_agent.permission",
              "cli_agent.execution",
              "cli_agent.review",
              "cli_agent.memory_gate",
              "cli_agent.incident",
              "cli_agent.anomaly"
            ]
          },
          "uniqueItems": true
        },
        "append_only_required": { "type": "boolean" },
        "hash_required": { "type": "boolean" },
        "signature_required": { "type": "boolean" }
      }
    },
    "memory_gate": {
      "type": "object",
      "additionalProperties": false,
      "required": ["direct_memory_write_allowed", "memory_proposal_allowed", "c_review_required", "uncertainty_required", "quarantine_on_uncertainty"],
      "properties": {
        "direct_memory_write_allowed": { "const": false },
        "memory_proposal_allowed": { "type": "boolean" },
        "proposed_memory_class": {
          "type": ["string", "null"],
          "enum": ["MG-0", "MG-1", "MG-2", "MG-3", "MG-4", "MG-Q", null]
        },
        "c_review_required": { "type": "boolean" },
        "uncertainty_required": { "type": "boolean" },
        "quarantine_on_uncertainty": { "type": "boolean" }
      }
    },
    "failure_behavior": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "default_on_failure",
        "default_on_scope_violation",
        "default_on_secret_exposure",
        "default_on_network_violation",
        "default_on_missing_witness",
        "default_on_agent_self_approval",
        "rollback_strategy"
      ],
      "properties": {
        "default_on_failure": { "enum": ["hold", "freeze", "quarantine", "rollback", "deny_and_quarantine"] },
        "default_on_scope_violation": { "enum": ["hold", "freeze", "quarantine", "rollback", "deny_and_quarantine"] },
        "default_on_secret_exposure": { "enum": ["freeze_and_escalate", "quarantine", "deny_and_quarantine"] },
        "default_on_network_violation": { "enum": ["hold", "quarantine", "deny_and_quarantine"] },
        "default_on_missing_witness": { "enum": ["hold", "freeze", "quarantine"] },
        "default_on_agent_self_approval": { "enum": ["revoke_and_quarantine", "deny_and_quarantine"] },
        "rollback_strategy": { "enum": ["none", "revert_patch", "restore_snapshot", "manual_review"] }
      }
    },
    "red_lines": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "offensive_action_requested",
        "live_external_exploitation",
        "hack_back",
        "credential_theft",
        "malware_behavior",
        "covert_persistence",
        "evasion",
        "destructive_action",
        "autonomous_retaliation",
        "third_party_scanning"
      ],
      "properties": {
        "offensive_action_requested": { "const": false },
        "live_external_exploitation": { "const": false },
        "hack_back": { "const": false },
        "credential_theft": { "const": false },
        "malware_behavior": { "const": false },
        "covert_persistence": { "const": false },
        "evasion": { "const": false },
        "destructive_action": { "const": false },
        "autonomous_retaliation": { "const": false },
        "third_party_scanning": { "const": false }
      }
    },
    "review": {
      "type": "object",
      "additionalProperties": false,
      "required": ["independent_reviewer_required", "executor_reviewer_separation_required", "quorum_required", "quorum_profile", "disagreement_policy"],
      "properties": {
        "independent_reviewer_required": { "type": "boolean" },
        "executor_reviewer_separation_required": { "type": "boolean" },
        "quorum_required": { "type": "boolean" },
        "quorum_profile": { "enum": ["none", "codex_gemini_local", "executor_tester_auditor", "custom"] },
        "disagreement_policy": { "enum": ["accept_if_minor", "hold", "c_review", "human_review", "arl_review"] }
      }
    },
    "integrity": {
      "type": "object",
      "additionalProperties": false,
      "required": ["canonicalization"],
      "properties": {
        "input_hash": { "type": ["string", "null"] },
        "contract_hash": { "type": ["string", "null"] },
        "expected_output_hash": { "type": ["string", "null"] },
        "canonicalization": { "enum": ["none", "json_canonicalization", "yaml_canonicalization"] },
        "previous_contract_ref": { "type": ["string", "null"] },
        "supersedes_contract_ref": { "type": ["string", "null"] }
      }
    },
    "notes": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "human_notes": { "type": ["string", "null"] },
        "c_notes": { "type": ["string", "null"] },
        "unresolved_issues": {
          "type": "array",
          "items": { "type": "string" }
        },
        "assumptions": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    }
  },
  "allOf": [
    {
      "if": {
        "properties": { "risk_class": { "enum": ["R4", "R5"] } },
        "required": ["risk_class"]
      },
      "then": {
        "properties": {
          "approval": {
            "properties": {
              "human_gate_required": { "const": true }
            }
          }
        }
      }
    },
    {
      "if": {
        "properties": { "risk_class": { "const": "RX" } },
        "required": ["risk_class"]
      },
      "then": {
        "properties": {
          "status": { "enum": ["held", "frozen", "quarantined", "revoked"] }
        }
      }
    }
  ]
}
```

---

## 10. Semantic validation rules

JSON Schema structural validation is necessary but not sufficient.

The following semantic rules MUST also be applied.

### 10.1 Red-line rule

If any red-line field is true, the contract is invalid regardless of all other fields.

### 10.2 External target rule

`external_targets_allowed` MUST remain false for ordinary protocol use.

A task involving external systems must be documented as owned, authorized, or delegated. Offensive or unauthorized use remains invalid.

### 10.3 Role/action consistency rule

A `reader` task MUST NOT include write commands.

An `auditor` task MUST NOT silently modify the work it audits.

A `tester` task MUST NOT alter tests to hide failures.

### 10.4 Risk/control consistency rule

- `R2` requires sandbox or worktree isolation.
- `R3` requires witness and `c` gate.
- `R4` requires witness, `c` gate, and human gate.
- `R5` requires evidence preservation before repair unless immediate containment requires otherwise.
- `RX` must resolve to denial/quarantine.

### 10.5 Cloud data rule

If `agent.runtime` is `cloud_cli`, then sensitive data fields SHOULD remain false unless explicitly justified:

```text
secrets_allowed
private_memory_allowed
sealed_material_allowed
legal_privileged_material_allowed
child_data_allowed
raw_witness_evidence_allowed
cloud_upload_allowed
```

### 10.6 Self-approval rule

`self_approval_allowed` must be false.

No exception is valid in v0.1.

### 10.7 Direct memory write rule

`direct_memory_write_allowed` must be false.

No exception is valid in v0.1.

### 10.8 Network rule

`network_policy.mode` must be `none` or `allowlist`.

A task requiring broader network access must be decomposed into smaller scoped tasks.

### 10.9 Evidence preservation rule

For incident tasks, evidence preservation must happen before repair where possible.

### 10.10 Expiry rule

If `expires_at` is reached, the contract is no longer active and the agent must stop or request renewal.

---

## 11. Example contracts

### 11.1 Read-only corpus review

```yaml
schema_version: cli-agent-task-contract-0.1
contract_id: catc-20260516-120000-corpus-review
task_id: task-corpus-review-001
title: Review CLI protocol documents for duplication
created_at: "2026-05-16T12:00:00Z"
expires_at: "2026-05-16T14:00:00Z"
status: active
requested_by: c
governing_entity:
  entity_id: ester
  entity_name: Ester
  continuity_ref: null
  authority_scope: project
human_anchor: null
agent:
  agent_id: gemini-reader-01
  agent_name: Gemini Reader
  provider: google
  role: reader
  runtime: cloud_cli
  version: null
  capability_profile_ref: null
  trust_level: provisional
objective: Review authorized CLI protocol drafts for duplication, contradiction, and missing boundaries without editing files.
risk_class: R1
assertion_class: C-A10
scope:
  repository: cli-agent-protocols
  branch_or_worktree: null
  allowed_paths:
    - docs/cli-agent/
  denied_paths:
    - secrets/
    - memory_core/
    - legal/
  allowed_commands: []
  denied_commands:
    - rm
    - git push
    - curl
  allowed_file_globs:
    - "*.md"
  denied_file_globs:
    - "*.env"
    - "*.key"
  max_files_touched: 0
  max_diff_lines: 0
  external_targets_allowed: false
  external_targets: []
data_policy:
  classification: internal
  secrets_allowed: false
  private_memory_allowed: false
  sealed_material_allowed: false
  legal_privileged_material_allowed: false
  child_data_allowed: false
  raw_witness_evidence_allowed: false
  cloud_upload_allowed: false
  prompt_minimization_required: true
  redaction_required: true
  retention: operational
  output_sanitization_required: true
network_policy:
  mode: none
  allowed_endpoints: []
  denied_endpoints: []
  package_install_allowed: false
  external_fetch_allowed: false
execution:
  sandbox_required: false
  sandbox_id: null
  branch_required: false
  container_required: false
  dry_run_first: true
  max_runtime_minutes: 30
  max_retries: 1
  max_cost_eur: 1
  max_tokens: 100000
  stop_on_scope_violation: true
  preserve_evidence_before_repair: false
  rollback_required_if_partial_write: false
output_required:
  - summary
  - risk_report
  - unresolved_questions
  - scope_report
approval:
  self_approval_allowed: false
  reviewer_required: false
  reviewer_agent_id: null
  c_gate_required: true
  human_gate_required: false
  legal_review_required: false
  merge_allowed_without_human: false
  publish_allowed_without_human: false
  deploy_allowed_without_human: false
witness:
  witness_required: false
  witness_profile: operational
  witness_event_families:
    - cli_agent.execution
  append_only_required: true
  hash_required: false
  signature_required: false
memory_gate:
  direct_memory_write_allowed: false
  memory_proposal_allowed: true
  proposed_memory_class: MG-2
  c_review_required: true
  uncertainty_required: true
  quarantine_on_uncertainty: true
failure_behavior:
  default_on_failure: hold
  default_on_scope_violation: quarantine
  default_on_secret_exposure: freeze_and_escalate
  default_on_network_violation: quarantine
  default_on_missing_witness: hold
  default_on_agent_self_approval: revoke_and_quarantine
  rollback_strategy: none
red_lines:
  offensive_action_requested: false
  live_external_exploitation: false
  hack_back: false
  credential_theft: false
  malware_behavior: false
  covert_persistence: false
  evasion: false
  destructive_action: false
  autonomous_retaliation: false
  third_party_scanning: false
review:
  independent_reviewer_required: false
  executor_reviewer_separation_required: true
  quorum_required: false
  quorum_profile: none
  disagreement_policy: c_review
integrity:
  input_hash: null
  contract_hash: null
  expected_output_hash: null
  canonicalization: yaml_canonicalization
  previous_contract_ref: null
  supersedes_contract_ref: null
notes:
  human_notes: null
  c_notes: null
  unresolved_issues: []
  assumptions:
    - Authorized project documents only.
```

### 11.2 Executor patch in sandbox

```yaml
schema_version: cli-agent-task-contract-0.1
contract_id: catc-20260516-130000-schema-patch
task_id: task-schema-patch-001
title: Patch Markdown table formatting in CLI protocol docs
created_at: "2026-05-16T13:00:00Z"
expires_at: "2026-05-16T15:00:00Z"
status: active
requested_by: human_anchor
governing_entity:
  entity_id: ester
  entity_name: Ester
  continuity_ref: null
  authority_scope: repository
human_anchor:
  anchor_id: ivan
  display_name: Ivan
  approval_required: true
  legal_review_required: false
agent:
  agent_id: codex-executor-01
  agent_name: Codex Executor
  provider: openai
  role: executor
  runtime: cloud_cli
  version: null
  capability_profile_ref: null
  trust_level: trusted_limited
objective: Fix Markdown table formatting only in authorized CLI agent protocol documents and return a diff plus rollback plan.
risk_class: R2
assertion_class: C-A10
scope:
  repository: cli-agent-protocols
  branch_or_worktree: worktree/cli-schema-formatting
  allowed_paths:
    - docs/cli-agent/
  denied_paths:
    - secrets/
    - memory_core/
    - legal/
    - .env
  allowed_commands:
    - markdownlint docs/cli-agent
    - git diff -- docs/cli-agent
  denied_commands:
    - git push
    - rm -rf
    - curl
    - wget
  allowed_file_globs:
    - "*.md"
  denied_file_globs:
    - "*.env"
    - "*.key"
    - "*.pem"
  max_files_touched: 5
  max_diff_lines: 300
  external_targets_allowed: false
  external_targets: []
data_policy:
  classification: internal
  secrets_allowed: false
  private_memory_allowed: false
  sealed_material_allowed: false
  legal_privileged_material_allowed: false
  child_data_allowed: false
  raw_witness_evidence_allowed: false
  cloud_upload_allowed: false
  prompt_minimization_required: true
  redaction_required: true
  retention: audit
  output_sanitization_required: true
network_policy:
  mode: none
  allowed_endpoints: []
  denied_endpoints: []
  package_install_allowed: false
  external_fetch_allowed: false
execution:
  sandbox_required: true
  sandbox_id: sandbox-cli-schema-formatting-001
  branch_required: true
  container_required: false
  dry_run_first: true
  max_runtime_minutes: 45
  max_retries: 2
  max_cost_eur: 3
  max_tokens: 200000
  stop_on_scope_violation: true
  preserve_evidence_before_repair: false
  rollback_required_if_partial_write: true
output_required:
  - summary
  - changed_files
  - diff
  - tests_run
  - test_results
  - risk_report
  - rollback_plan
  - commands_run
approval:
  self_approval_allowed: false
  reviewer_required: true
  reviewer_agent_id: gemini-reader-01
  c_gate_required: true
  human_gate_required: false
  legal_review_required: false
  merge_allowed_without_human: false
  publish_allowed_without_human: false
  deploy_allowed_without_human: false
witness:
  witness_required: true
  witness_profile: operational
  witness_event_families:
    - cli_agent.execution
    - cli_agent.review
  append_only_required: true
  hash_required: true
  signature_required: false
memory_gate:
  direct_memory_write_allowed: false
  memory_proposal_allowed: true
  proposed_memory_class: MG-1
  c_review_required: true
  uncertainty_required: true
  quarantine_on_uncertainty: true
failure_behavior:
  default_on_failure: hold
  default_on_scope_violation: quarantine
  default_on_secret_exposure: freeze_and_escalate
  default_on_network_violation: quarantine
  default_on_missing_witness: hold
  default_on_agent_self_approval: revoke_and_quarantine
  rollback_strategy: revert_patch
red_lines:
  offensive_action_requested: false
  live_external_exploitation: false
  hack_back: false
  credential_theft: false
  malware_behavior: false
  covert_persistence: false
  evasion: false
  destructive_action: false
  autonomous_retaliation: false
  third_party_scanning: false
review:
  independent_reviewer_required: true
  executor_reviewer_separation_required: true
  quorum_required: false
  quorum_profile: executor_tester_auditor
  disagreement_policy: hold
integrity:
  input_hash: null
  contract_hash: null
  expected_output_hash: null
  canonicalization: yaml_canonicalization
  previous_contract_ref: null
  supersedes_contract_ref: null
notes:
  human_notes: Only formatting changes. No semantic rewrite.
  c_notes: null
  unresolved_issues: []
  assumptions:
    - Repository is owned or authorized.
```

### 11.3 Invalid offensive contract

This example is invalid and must be rejected.

```yaml
schema_version: cli-agent-task-contract-0.1
contract_id: catc-invalid-hackback
task_id: task-invalid-001
title: Trace and counterattack hostile source
created_at: "2026-05-16T13:30:00Z"
status: active
requested_by: c
governing_entity:
  entity_id: ester
  entity_name: Ester
  continuity_ref: null
  authority_scope: incident
agent:
  agent_id: codex-executor-01
  agent_name: Codex Executor
  provider: openai
  role: executor
  runtime: cloud_cli
  trust_level: trusted_limited
objective: Counterattack the suspected hostile source.
risk_class: RX
assertion_class: C-A10
scope:
  allowed_paths:
    - ./
  denied_paths:
    - secrets/
  allowed_commands: []
  denied_commands: []
  external_targets_allowed: false
data_policy:
  classification: incident_sensitive
  secrets_allowed: false
  private_memory_allowed: false
  sealed_material_allowed: false
  legal_privileged_material_allowed: false
  child_data_allowed: false
  raw_witness_evidence_allowed: false
  cloud_upload_allowed: false
  prompt_minimization_required: true
  redaction_required: true
  retention: audit
  output_sanitization_required: true
network_policy:
  mode: allowlist
  allowed_endpoints: []
  denied_endpoints: []
  package_install_allowed: false
  external_fetch_allowed: false
execution:
  sandbox_required: true
  branch_required: true
  container_required: true
  dry_run_first: true
  max_runtime_minutes: 1
  max_retries: 0
  stop_on_scope_violation: true
  preserve_evidence_before_repair: true
  rollback_required_if_partial_write: true
output_required:
  - risk_report
approval:
  self_approval_allowed: false
  reviewer_required: true
  c_gate_required: true
  human_gate_required: true
  legal_review_required: true
  merge_allowed_without_human: false
  publish_allowed_without_human: false
  deploy_allowed_without_human: false
witness:
  witness_required: true
  witness_profile: incident
  witness_event_families:
    - cli_agent.incident
    - cli_agent.anomaly
  append_only_required: true
  hash_required: true
  signature_required: true
memory_gate:
  direct_memory_write_allowed: false
  memory_proposal_allowed: false
  proposed_memory_class: MG-Q
  c_review_required: true
  uncertainty_required: true
  quarantine_on_uncertainty: true
failure_behavior:
  default_on_failure: deny_and_quarantine
  default_on_scope_violation: quarantine
  default_on_secret_exposure: freeze_and_escalate
  default_on_network_violation: quarantine
  default_on_missing_witness: hold
  default_on_agent_self_approval: revoke_and_quarantine
  rollback_strategy: none
red_lines:
  offensive_action_requested: true
  live_external_exploitation: false
  hack_back: true
  credential_theft: false
  malware_behavior: false
  covert_persistence: false
  evasion: false
  destructive_action: false
  autonomous_retaliation: true
  third_party_scanning: false
review:
  independent_reviewer_required: true
  executor_reviewer_separation_required: true
  quorum_required: true
  quorum_profile: custom
  disagreement_policy: human_review
integrity:
  canonicalization: yaml_canonicalization
```

Required result:

```text
deny_and_quarantine
```

---

## 12. Contract validation workflow

A governance system SHOULD validate contracts in this order:

```text
parse
  -> structural schema validation
  -> red-line validation
  -> role/action validation
  -> risk/control validation
  -> data/cloud validation
  -> network validation
  -> approval validation
  -> witness validation
  -> memory gate validation
  -> final allow / hold / deny / quarantine
```

---

## 13. Default failure mapping

| Failure | Required default |
|---|---|
| schema parse failure | `deny_and_quarantine` |
| missing required field | `hold` |
| red-line true | `deny_and_quarantine` |
| scope missing | `hold` |
| denied path touched | `quarantine` |
| secret exposure | `freeze_and_escalate` |
| unapproved network access | `quarantine` |
| self-approval attempt | `revoke_and_quarantine` |
| missing witness for privileged task | `hold` |
| output contains prohibited data | `quarantine` |
| stale contract | `hold` |
| expired contract | `hold` |

---

## 14. Implementation notes

### 14.1 Canonicalization

For high-assurance use, the contract SHOULD be canonicalized before hashing.

Recommended sequence:

```text
normalize
sort object keys
remove non-semantic whitespace
encode UTF-8
hash
store contract_hash
```

### 14.2 Contract immutability

An active contract SHOULD NOT be edited in place after execution begins.

Changes SHOULD create a new contract referencing the previous one through:

```text
previous_contract_ref
supersedes_contract_ref
```

### 14.3 Append-only review

Review decisions SHOULD be append-only.

Corrections and reversals SHOULD reference earlier decisions rather than silently replacing them.

### 14.4 Human-readable pair

Every machine-readable contract SHOULD have a short human-readable task card:

```text
Task:
Agent:
Scope:
Denied:
Network:
Risk:
Review:
Failure default:
```

---

## 15. Conformance levels

| Level | Meaning |
|---|---|
| `CATC-0` | no task contract discipline |
| `CATC-1` | human-readable task contracts only |
| `CATC-2` | machine-readable contracts for write tasks |
| `CATC-3` | schema validation + semantic validation |
| `CATC-4` | witness-bound contracts for privileged tasks |
| `CATC-5` | high-assurance canonicalized, hashed, reviewed, and replayable task contract workflow |
| `CATC-X` | revoked / invalid / red-line failure |

---

## 16. Open issues

| ID | Issue | Required action |
|---|---|---|
| `OI-001` | Stable `$id` URL | Replace placeholder schema URL with final repo path. |
| `OI-002` | Canonicalization profile | Decide JSON vs YAML canonicalization. |
| `OI-003` | Signature profile | Define signing format for high-assurance contracts. |
| `OI-004` | Agent registry reference | Create `CLI_Agent_Registry_Profile_v0_1.md`. |
| `OI-005` | Witness event binding | Create `CLI_Agent_Witness_Event_Profile_v0_1.md`. |
| `OI-006` | Memory gate binding | Create `CLI_Agent_Memory_Gate_Profile_v0_1.md`. |
| `OI-007` | Runtime validator | Create reference validator for schema + semantic rules. |
| `OI-008` | Provider profiles | Define local, OpenAI, Google, and other provider-specific capability envelopes. |
| `OI-009` | High-risk task examples | Add more R4/R5 examples after root protocol review. |
| `OI-010` | Repo placement | Decide final GitHub path and package index integration. |

---

## 17. Closing rule

A CLI agent task contract is not bureaucracy.

It is the boundary between useful executable help and uncontrolled operational drift.

Final rule:

```text
If the task cannot be scoped, it cannot be delegated.
If it cannot be reviewed, it cannot be integrated.
If it crosses a privileged boundary, it must be witnessed.
```

