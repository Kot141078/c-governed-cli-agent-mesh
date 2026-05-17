# CLI Agent Witness Event Profile v0.1

## Tamper-aware boundary records for C-Governed CLI Agent Mesh operations

**Status:** Draft normative profile v0.1  
**Date:** 2026-05-16  
**Layer:** `c = a + b` / C-Governed CLI Agent Mesh / Witness / Evidence / Boundary Records / Review / Rollback  
**Document class:** witness profile / event schema / control-layer artifact  
**Assertion class:** `C-A10` control-layer artifact; `C-A7` where hash, signature, canonicalization, append-only, or verification claims are made  
**Primary parent documents:**  
- `C-Governed_CLI_Agent_Mesh_Protocol_v0_1.md`  
- `CLI_Agent_Task_Contract_Schema_v0_1.md`  
- `CLI_Agent_Permission_and_Capability_Model_v0_1.md`  
- `CLI_Agent_Handshake_Profile_v0_1.md`  
- `CLI_Agent_Sandbox_Worktree_Profile_v0_1.md`  

**Primary object family:** `CLI_AGENT_WITNESS_EVENT`, `CLI_AGENT_WITNESS_CHAIN`, `CLI_AGENT_WITNESS_REFERENCE`  
**Canonical schema version:** `cli-agent-witness-event-0.1`  
**Primary subject:** persistent `c` entities using local, cloud, or hybrid CLI agents as bounded executable workers  
**Primary boundary:** witness events prove that a boundary was crossed, denied, narrowed, escalated, reviewed, integrated, rolled back, or quarantined. They must not become raw memory dumps, secret stores, surveillance logs, or agent self-justification narratives.

---

## 0. Executive definition

**CLI Agent Witness Event Profile** defines the event records required to make a C-Governed CLI Agent Mesh auditable, challengeable, reversible where possible, and resistant to silent authority drift.

A witness event records:

```text
who or what acted
under which task contract
with which permission
inside which sandbox/worktree
against which boundary
with what decision
with what minimal reason code
with what review path
with what rollback or quarantine option
```

A witness event must not record:

```text
raw secrets
private memory
sealed material
legal privileged content
full prompt streams by default
raw child data
unredacted incident evidence
agent self-narration as authority
```

Compact formula:

```text
Witness the boundary.
Do not narrate the soul.
Record the transition.
Do not archive the whole life.
```

---

## 1. Purpose

CLI agents can execute. Execution creates side effects. Side effects require traceability.

This profile exists because a `c`-governed agent mesh must be able to answer:

1. Which agent entered the mesh?
2. Which task contract allowed the work?
3. Which permissions were granted, denied, narrowed, or revoked?
4. Which sandbox or worktree was used?
5. Which files changed?
6. Which denied paths, commands, network calls, or data classes were attempted?
7. Which reviewer inspected the output?
8. Which result was accepted, rejected, quarantined, or rolled back?
9. Which memory gate decision occurred?
10. Which high-risk action required human review?
11. Which anomaly indicates privilege drift, tool-chain capture, or cloud leakage?

The witness layer does not decide truth alone.

It records boundary transitions so `c`, the human anchor, auditors, review layers, and future recovery procedures can reconstruct what happened without granting raw access to everything.

---

## 2. Non-goals

This profile does not define or permit:

1. surveillance logging of all agent text;
2. raw memory export;
3. secret storage in witness events;
4. legal evidence conclusions;
5. diagnosis, accusation, or guilt determination;
6. offensive cyber operations;
7. hack-back;
8. autonomous retaliation;
9. malware behavior;
10. credential extraction;
11. covert persistence;
12. evasion;
13. live external exploitation;
14. direct mutation of identity, memory, Beacon, witness, permission, or continuity core;
15. agent self-certification as final authority.

A witness event proves that a transition was recorded.

It does not by itself prove that the agent was right, the claim was true, or the final decision was correct.

---

## 3. Corpus bridge set

### 3.1 Explicit bridge: `c = a + b`

CLI agents belong to `b`: the technological substrate of procedures, tools, models, compute, interfaces, and infrastructure.

A witness event is also part of `b`, but it protects the boundary between `b` and `c`.

It prevents worker action from silently becoming `c` memory, identity, authority, or continuity.

### 3.2 Quiet bridge I: L4 and irreversible transitions

Some actions consume time, change files, expose data, spend tokens, alter public surfaces, or affect memory. L4 makes these transitions real. Witness records preserve enough state to inspect whether the transition was authorized, bounded, and reversible where possible.

### 3.3 Quiet bridge II: information theory and minimum sufficient signal

A witness event should transmit the minimum useful information needed to verify the boundary. More raw data is not always better. Excessive logging increases leakage, legal risk, privacy risk, and attack surface.

### 3.4 Quiet bridge III: engineering chain of custody

In engineering, a test result without test conditions is weak evidence. A repair without a work order is untraceable. A release without a manifest is fragile. CLI agent work requires the same chain: contract, permission, environment, action, output, review, decision, rollback.

### 3.5 Earth paragraph

A site log does not contain every conversation workers had during the day. It records who entered, what permit they worked under, which circuit was isolated, what was changed, who inspected it, and whether the panel was closed safely. The witness event is that site log for CLI agents. It protects the building without turning every worker’s thoughts into evidence.

---

## 4. Core doctrine

### 4.1 Primary doctrine

```text
Witness privileged transitions.
Minimize raw content.
Append corrections.
Fail closed on missing witness.
```

### 4.2 Witness axioms

| ID | Axiom | Requirement |
|---|---|---|
| `WE-AX-01` | Boundary before narrative | Events SHOULD record boundary state, not long free-text narratives. |
| `WE-AX-02` | Minimality | Events MUST NOT embed secrets, private memory, sealed data, or unnecessary raw content by default. |
| `WE-AX-03` | Append-only first | Corrections and reversals SHOULD be new events referencing prior events. |
| `WE-AX-04` | Source linkage | Events SHOULD link to task contract, permission grant, sandbox run, output, review, or memory gate record. |
| `WE-AX-05` | Privileged transitions require witness | Permission expansion, protected writes, release/publication, memory-gate promotion, incident containment, and rollback SHOULD be witnessed. |
| `WE-AX-06` | Event is not authority alone | A witness record proves recording, not correctness. |
| `WE-AX-07` | Missing witness fails closed | If a required witness is absent, the system MUST hold, freeze, quarantine, revalidate, or roll back. |
| `WE-AX-08` | Uncertainty is explicit | Uncertainty MUST be a structured field where interpretation is involved. |
| `WE-AX-09` | Privacy beats curiosity | Raw data is excluded unless strictly necessary and separately controlled. |
| `WE-AX-10` | Agent cannot certify itself | An agent MUST NOT be final authority for witness adequacy around its own material action. |
| `WE-AX-11` | Hashes are references, not content | Hashes may identify artifacts without embedding sensitive content. |
| `WE-AX-12` | Witness chain is challengeable | Events SHOULD support later review, dispute, rollback, and conformance testing. |

---

## 5. Definitions

### 5.1 Witness event

A structured record that a boundary-relevant action, decision, transition, anomaly, review, rollback, or quarantine occurred.

### 5.2 Witness chain

An ordered set of witness events linked by task, agent, contract, artifact, or prior event reference.

### 5.3 Witness reference

A pointer to a witness event, chain, artifact hash, review record, or upstream decision.

### 5.4 Boundary transition

A change in permission, state, trust, data access, memory status, code state, release state, incident state, or integration status.

### 5.5 Privileged transition

A boundary transition that can affect protected state, public state, memory, secrets, identity, continuity, incident handling, legal posture, release state, or high-risk infrastructure.

### 5.6 Minimal reason code

A short structured explanation of why a decision occurred, avoiding unnecessary raw content.

### 5.7 Raw evidence

Underlying logs, files, prompts, memory content, incident data, or artifacts that may support a witness event but are not embedded in the event by default.

### 5.8 Privacy class

A classification of how sensitive an event is and who may inspect it.

### 5.9 Retention class

A classification of how long an event or reference should be retained.

### 5.10 Canonicalization

A deterministic representation of an event used for hashing or signing.

### 5.11 Append-only correction

A new event that corrects, supersedes, or reverses an earlier event without silently modifying the earlier record.

---

## 6. Witness event classes

Event classes use prefix `WE-*`.

| Class | Name | Meaning |
|---|---|---|
| `WE-0` | Informational | Low-risk operational note. |
| `WE-1` | Operational | Routine task boundary or execution event. |
| `WE-2` | Permission | Permission grant, denial, narrowing, expansion, revocation. |
| `WE-3` | Execution | Sandbox/worktree execution, output, tests, diffs. |
| `WE-4` | Review | Independent review, quorum result, disagreement, approval gate. |
| `WE-5` | Memory Gate | Candidate memory, reviewed memory, quarantine, rejection, promotion. |
| `WE-6` | Release/Public | Public surface, release, publication, metadata, branch protection. |
| `WE-7` | Incident | Security/integrity incident, preservation, containment, freeze, report. |
| `WE-8` | Core Authority | Identity, continuity, permission registry, witness chain, Beacon-like recognition surfaces. |
| `WE-9` | Anomaly | Scope violation, drift, missing witness, secret exposure, cloud leakage. |
| `WE-X` | Prohibited / Red-line | Attempted prohibited behavior; must trigger deny/quarantine/review. |

---

## 7. Privacy classes

Privacy class IDs use prefix `WP-*`.

| Class | Meaning | Default visibility |
|---|---|---|
| `WP-PUBLIC` | safe public operational event | public/release notes if useful |
| `WP-INTERNAL` | internal project event | `c`, human anchor, authorized agents |
| `WP-PRIVATE` | private operational event | `c`, human anchor only by default |
| `WP-RESTRICTED` | sensitive governance event | restricted review only |
| `WP-SECRET-REF` | references secret boundary without exposing secret | secret custodian / human gate |
| `WP-LEGAL` | legal-sensitive or counsel-facing | legal/human gate |
| `WP-INCIDENT` | security/integrity incident | incident reviewers only |
| `WP-MEMORY` | memory-gate-related event | `c` / memory reviewer |
| `WP-SEALED` | sealed/private compartment reference | sealed policy only |

### 7.1 Privacy rule

A witness event MUST use the lowest privacy exposure that still preserves reviewability.

### 7.2 No raw secret rule

Secrets MUST NOT be embedded in witness events.

Use reason codes, artifact hashes, and secure references instead.

---

## 8. Retention classes

Retention class IDs use prefix `WR-*`.

| Class | Meaning |
|---|---|
| `WR-EPHEMERAL` | short-lived operational event; safe to discard after task closure if not privileged |
| `WR-OPERATIONAL` | retained for project operation and debugging |
| `WR-AUDIT` | retained for governance, conformance, release, or rollback |
| `WR-INCIDENT` | retained for incident response and security review |
| `WR-LEGAL-HOLD` | retained under legal/counsel/regulatory need |
| `WR-MEMORY-GATE` | retained as part of memory decision record |
| `WR-CORE` | retained for identity/permission/witness/continuity core transition |

### 8.1 Retention minimization

Retention should be long enough to preserve accountability and short enough to avoid unnecessary accumulation of sensitive operational residue.

---

## 9. Event family registry

Event families use dot-separated namespace:

```text
cli_agent.<surface>.<action>
```

Surfaces:

```text
handshake
permission
task
sandbox
review
memory_gate
release
incident
cloud_data
quorum
rollback
quarantine
anomaly
core
```

---

## 10. Handshake event families

| Event family | Meaning | Typical class |
|---|---|---|
| `cli_agent.handshake.discovered` | candidate agent discovered | `WE-0` |
| `cli_agent.handshake.claimed` | identity/provider/runtime claimed | `WE-1` |
| `cli_agent.handshake.provenance_checked` | provenance check performed | `WE-1` |
| `cli_agent.handshake.capability_declared` | capabilities declared | `WE-1` |
| `cli_agent.handshake.capability_challenged` | challenge completed | `WE-1` / `WE-2` |
| `cli_agent.handshake.registered` | agent registered | `WE-2` |
| `cli_agent.handshake.trust_changed` | trust level changed | `WE-2` / `WE-9` |
| `cli_agent.handshake.rehandshake_required` | re-handshake required | `WE-9` |
| `cli_agent.handshake.suspended` | agent suspended | `WE-9` |
| `cli_agent.handshake.quarantined` | agent quarantined | `WE-9` |
| `cli_agent.handshake.revoked` | agent revoked | `WE-9` |
| `cli_agent.handshake.expired` | registration expired | `WE-1` |

---

## 11. Permission event families

| Event family | Meaning | Typical class |
|---|---|---|
| `cli_agent.permission.requested` | permission requested | `WE-2` |
| `cli_agent.permission.granted` | permission granted | `WE-2` |
| `cli_agent.permission.denied` | permission denied | `WE-2` |
| `cli_agent.permission.narrowed` | permission narrowed | `WE-2` |
| `cli_agent.permission.expanded` | permission expanded | `WE-2` / `WE-8` |
| `cli_agent.permission.used` | permission used materially | `WE-2` / `WE-3` |
| `cli_agent.permission.expired` | permission expired | `WE-1` |
| `cli_agent.permission.revoked` | permission revoked | `WE-2` / `WE-9` |
| `cli_agent.permission.violation` | permission boundary violated | `WE-9` |
| `cli_agent.permission.drift_detected` | privilege drift detected | `WE-9` |
| `cli_agent.permission.self_approval_attempt` | agent attempted self-approval | `WE-X` |

---

## 12. Task event families

| Event family | Meaning | Typical class |
|---|---|---|
| `cli_agent.task.contract_created` | task contract created | `WE-1` |
| `cli_agent.task.contract_activated` | contract activated | `WE-1` |
| `cli_agent.task.contract_modified` | contract changed / superseded | `WE-2` |
| `cli_agent.task.contract_expired` | contract expired | `WE-1` |
| `cli_agent.task.contract_revoked` | contract revoked | `WE-2` |
| `cli_agent.task.started` | task started | `WE-1` |
| `cli_agent.task.completed` | task completed | `WE-1` |
| `cli_agent.task.failed` | task failed | `WE-1` / `WE-9` |
| `cli_agent.task.held` | task held | `WE-2` |
| `cli_agent.task.scope_changed` | scope changed | `WE-2` / `WE-8` |
| `cli_agent.task.risk_reclassified` | risk class changed | `WE-2` |

---

## 13. Sandbox / worktree event families

| Event family | Meaning | Typical class |
|---|---|---|
| `cli_agent.sandbox.created` | sandbox/worktree created | `WE-3` |
| `cli_agent.sandbox.preflight_completed` | preflight completed | `WE-3` |
| `cli_agent.sandbox.snapshot_taken` | snapshot/hash/state reference recorded | `WE-3` / `WE-7` |
| `cli_agent.sandbox.execution_started` | execution began | `WE-3` |
| `cli_agent.sandbox.command_run` | command executed | `WE-3` |
| `cli_agent.sandbox.file_changed` | file changed | `WE-3` |
| `cli_agent.sandbox.artifact_generated` | artifact/diff generated | `WE-3` |
| `cli_agent.sandbox.tests_completed` | tests completed | `WE-3` |
| `cli_agent.sandbox.denied_path_attempt` | denied path touched/attempted | `WE-9` |
| `cli_agent.sandbox.network_attempt` | network attempt recorded | `WE-3` / `WE-9` |
| `cli_agent.sandbox.unexpected_side_effect` | unexplained side effect occurred | `WE-9` |
| `cli_agent.sandbox.quarantined` | sandbox/output quarantined | `WE-9` |
| `cli_agent.sandbox.destroyed` | disposable sandbox destroyed | `WE-1` |

---

## 14. Review and quorum event families

| Event family | Meaning | Typical class |
|---|---|---|
| `cli_agent.review.requested` | review requested | `WE-4` |
| `cli_agent.review.completed` | review completed | `WE-4` |
| `cli_agent.review.rejected` | reviewer rejected output | `WE-4` |
| `cli_agent.review.accepted` | reviewer accepted output | `WE-4` |
| `cli_agent.review.accepted_with_limits` | partial acceptance | `WE-4` |
| `cli_agent.review.disagreement` | agents/reviewers disagree | `WE-4` |
| `cli_agent.review.escalated` | escalated to `c`, human, legal, or security review | `WE-4` / `WE-7` |
| `cli_agent.quorum.started` | quorum review started | `WE-4` |
| `cli_agent.quorum.completed` | quorum review completed | `WE-4` |
| `cli_agent.quorum.split` | quorum disagreement unresolved | `WE-4` / `WE-9` |

---

## 15. Memory gate event families

| Event family | Meaning | Typical class |
|---|---|---|
| `cli_agent.memory_gate.proposal_created` | agent output proposed as memory | `WE-5` |
| `cli_agent.memory_gate.proposal_rejected` | memory proposal rejected | `WE-5` |
| `cli_agent.memory_gate.proposal_quarantined` | memory proposal quarantined | `WE-5` / `WE-9` |
| `cli_agent.memory_gate.promoted_operational` | accepted as operational note | `WE-5` |
| `cli_agent.memory_gate.promoted_reviewed` | accepted as reviewed memory | `WE-5` |
| `cli_agent.memory_gate.promoted_witnessed_artifact` | accepted as witnessed experience artifact | `WE-5` / `WE-8` |
| `cli_agent.memory_gate.corrected` | correction appended | `WE-5` |
| `cli_agent.memory_gate.deleted_or_decayed` | memory candidate deleted/decayed | `WE-5` |
| `cli_agent.memory_gate.direct_write_attempt` | agent attempted direct memory write | `WE-X` |

---

## 16. Release / public surface event families

| Event family | Meaning | Typical class |
|---|---|---|
| `cli_agent.release.prepared` | release/publication package prepared | `WE-6` |
| `cli_agent.release.metadata_changed` | metadata changed | `WE-6` |
| `cli_agent.release.hash_manifest_created` | hash manifest created | `WE-6` |
| `cli_agent.release.reviewed` | release package reviewed | `WE-6` |
| `cli_agent.release.approved` | release approved by `c`/human | `WE-6` / `WE-8` |
| `cli_agent.release.published` | release/publication applied | `WE-6` |
| `cli_agent.release.rolled_back` | release/publication rolled back | `WE-6` / `WE-9` |
| `cli_agent.release.unauthorized_publish_attempt` | unauthorized publish attempt | `WE-X` |

---

## 17. Incident event families

| Event family | Meaning | Typical class |
|---|---|---|
| `cli_agent.incident.detected` | incident/anomaly detected | `WE-7` |
| `cli_agent.incident.preservation_started` | evidence preservation started | `WE-7` |
| `cli_agent.incident.preservation_completed` | evidence preservation completed | `WE-7` |
| `cli_agent.incident.freeze_applied` | affected path frozen | `WE-7` |
| `cli_agent.incident.containment_applied` | local containment applied | `WE-7` |
| `cli_agent.incident.repair_proposed` | repair proposed | `WE-7` |
| `cli_agent.incident.repair_applied` | repair applied after gate | `WE-7` |
| `cli_agent.incident.report_prepared` | provider/legal/security report prepared | `WE-7` |
| `cli_agent.incident.secret_exposure` | secret exposure detected | `WE-9` |
| `cli_agent.incident.repair_before_preserve` | repair attempted before required preservation | `WE-9` |
| `cli_agent.incident.live_counter_attempt` | live external counter-operation attempted | `WE-X` |

---

## 18. Cloud data event families

| Event family | Meaning | Typical class |
|---|---|---|
| `cli_agent.cloud_data.classified` | data classified before cloud use | `WE-1` |
| `cli_agent.cloud_data.redacted` | data redacted before cloud use | `WE-1` |
| `cli_agent.cloud_data.allowed` | cloud transmission allowed | `WE-2` |
| `cli_agent.cloud_data.denied` | cloud transmission denied | `WE-2` |
| `cli_agent.cloud_data.leak_suspected` | possible cloud leakage | `WE-9` |
| `cli_agent.cloud_data.prohibited_material_detected` | prohibited material found in cloud context | `WE-9` / `WE-X` |

---

## 19. Core authority event families

| Event family | Meaning | Typical class |
|---|---|---|
| `cli_agent.core.touch_requested` | request to inspect/touch core authority surface | `WE-8` |
| `cli_agent.core.touch_denied` | core touch denied | `WE-8` |
| `cli_agent.core.touch_allowed_readonly` | read-only core inspection allowed | `WE-8` |
| `cli_agent.core.change_proposed` | core change proposed | `WE-8` |
| `cli_agent.core.change_rejected` | core change rejected | `WE-8` |
| `cli_agent.core.change_approved` | core change approved after gates | `WE-8` |
| `cli_agent.core.direct_mutation_attempt` | direct unauthorized core mutation attempted | `WE-X` |
| `cli_agent.core.rollback` | core-related rollback | `WE-8` / `WE-9` |

---

## 20. Anomaly and red-line event families

| Event family | Meaning | Typical class |
|---|---|---|
| `cli_agent.anomaly.scope_violation` | scope violation | `WE-9` |
| `cli_agent.anomaly.permission_drift` | permission drift detected | `WE-9` |
| `cli_agent.anomaly.toolchain_capture` | tool-chain capture suspected | `WE-9` |
| `cli_agent.anomaly.stale_context` | stale context risk detected | `WE-9` |
| `cli_agent.anomaly.self_approval` | self-approval attempt | `WE-X` |
| `cli_agent.anomaly.secret_access` | secret access outside scope | `WE-X` |
| `cli_agent.anomaly.network_violation` | network violation | `WE-9` |
| `cli_agent.anomaly.missing_witness` | required witness absent | `WE-9` |
| `cli_agent.anomaly.prohibited_action` | prohibited action attempted | `WE-X` |
| `cli_agent.anomaly.agent_persistence` | agent persisted beyond task scope | `WE-X` |
| `cli_agent.anomaly.external_counteroperation` | live counter-operation attempted | `WE-X` |

---

## 21. Witness event object

Canonical object:

```text
CLI_AGENT_WITNESS_EVENT
```

### 21.1 Required YAML shape

```yaml
cli_agent_witness_event:
  schema_version: cli-agent-witness-event-0.1
  event_id: string
  event_family: string
  event_class: WE-0 | WE-1 | WE-2 | WE-3 | WE-4 | WE-5 | WE-6 | WE-7 | WE-8 | WE-9 | WE-X
  timestamp: string
  sequence_number: integer | null

  governing_entity:
    entity_id: string
    entity_name: string | null
    continuity_ref: string | null

  agent:
    agent_id: string | null
    agent_name: string | null
    provider: local | openai | google | anthropic | other | unknown | null
    runtime: local_cli | cloud_cli | api_agent | container_agent | hybrid | unknown | null
    role: reader | executor | tester | auditor | archivist | sentinel | judge_assistant | orchestrator_limited | null

  task_refs:
    contract_id: string | null
    task_id: string | null
    permission_grant_id: string | null
    handshake_id: string | null
    registration_id: string | null
    sandbox_id: string | null
    worktree_run_id: string | null
    review_id: string | null
    memory_gate_id: string | null
    incident_id: string | null

  boundary:
    surface: handshake | permission | task | sandbox | review | memory_gate | release | incident | cloud_data | quorum | rollback | quarantine | anomaly | core
    action: string
    decision: allowed | denied | held | frozen | quarantined | revoked | completed | failed | accepted | rejected | rolled_back | escalated
    reason_code: string
    risk_class: R0 | R1 | R2 | R3 | R4 | R5 | RX | null
    uncertainty: none | low | medium | high | unknown

  artifact_refs:
    input_hash: string | null
    output_hash: string | null
    diff_hash: string | null
    artifact_manifest_hash: string | null
    test_report_hash: string | null
    rollback_plan_hash: string | null
    upstream_event_refs:
      - string
    downstream_event_refs:
      - string

  privacy:
    privacy_class: WP-PUBLIC | WP-INTERNAL | WP-PRIVATE | WP-RESTRICTED | WP-SECRET-REF | WP-LEGAL | WP-INCIDENT | WP-MEMORY | WP-SEALED
    retention_class: WR-EPHEMERAL | WR-OPERATIONAL | WR-AUDIT | WR-INCIDENT | WR-LEGAL-HOLD | WR-MEMORY-GATE | WR-CORE
    raw_content_embedded: false
    secret_embedded: false
    private_memory_embedded: false
    sealed_material_embedded: false
    legal_sensitive_embedded: false
    child_data_embedded: false

  review:
    reviewer_required: boolean
    reviewer_ref: string | null
    c_gate_required: boolean
    c_gate_ref: string | null
    human_gate_required: boolean
    human_gate_ref: string | null
    legal_review_required: boolean
    legal_review_ref: string | null

  integrity:
    canonicalization: none | json_canonicalization | yaml_canonicalization
    event_hash: string | null
    previous_event_hash: string | null
    chain_id: string | null
    signature_required: boolean
    signature_ref: string | null
    append_only_required: true

  outcome:
    next_required_action: none | hold | freeze | quarantine | revalidate | rollback | revoke | escalate | human_review | c_review | legal_review
    status_after_event: active | completed | failed | held | frozen | quarantined | revoked | expired | unknown

  notes:
    summary: string | null
    limitations:
      - string
    assumptions:
      - string
```

### 21.2 Required field rule

The event MUST identify at minimum:

```text
event_id
event_family
event_class
timestamp
governing_entity
boundary.surface
boundary.action
boundary.decision
boundary.reason_code
privacy
integrity.append_only_required
outcome.next_required_action
```

---

## 22. Witness chain object

Canonical object:

```text
CLI_AGENT_WITNESS_CHAIN
```

### 22.1 YAML shape

```yaml
cli_agent_witness_chain:
  schema_version: cli-agent-witness-event-0.1
  chain_id: string
  created_at: string
  governing_entity_id: string
  chain_purpose: task | permission | release | incident | memory_gate | core | other
  root_event_id: string
  latest_event_id: string
  event_count: integer
  event_hashes:
    - string
  chain_hash: string | null
  sealed: boolean
  retention_class: WR-EPHEMERAL | WR-OPERATIONAL | WR-AUDIT | WR-INCIDENT | WR-LEGAL-HOLD | WR-MEMORY-GATE | WR-CORE
  challengeable: true
```

### 22.2 Chain principles

- A chain SHOULD be append-only.
- A chain SHOULD support challenge and review.
- A chain SHOULD not embed raw sensitive content.
- A chain MAY reference external raw evidence records when lawful and necessary.

---

## 23. Witness reference object

Canonical object:

```text
CLI_AGENT_WITNESS_REFERENCE
```

### 23.1 YAML shape

```yaml
cli_agent_witness_reference:
  schema_version: cli-agent-witness-event-0.1
  witness_ref_id: string
  event_id: string | null
  chain_id: string | null
  artifact_hash: string | null
  storage_ref: string | null
  privacy_class: WP-PUBLIC | WP-INTERNAL | WP-PRIVATE | WP-RESTRICTED | WP-SECRET-REF | WP-LEGAL | WP-INCIDENT | WP-MEMORY | WP-SEALED
  retention_class: WR-EPHEMERAL | WR-OPERATIONAL | WR-AUDIT | WR-INCIDENT | WR-LEGAL-HOLD | WR-MEMORY-GATE | WR-CORE
  dereference_policy: open | restricted | c_gate | human_gate | legal_gate | incident_gate | sealed_gate
```

---

## 24. Raw evidence exception

### 24.1 Default rule

Raw evidence MUST NOT be embedded in witness events by default.

### 24.2 Exception conditions

A raw evidence reference may be created only when all conditions hold:

1. lawful or owned-system basis exists;
2. evidence is necessary for review, incident response, legal handoff, rollback, or conformance;
3. minimality is documented;
4. retention class is explicit;
5. access policy is explicit;
6. raw material is stored separately from the witness event body;
7. event contains reference/hash, not raw material;
8. post-event review is required for high-risk material.

### 24.3 Prohibited raw embedding

The following must not be embedded in witness events:

- credentials;
- API keys;
- private keys;
- unredacted identity documents;
- sealed memory;
- private memory;
- legal privileged content;
- child data;
- raw incident evidence unless a separate lawful evidence object exists;
- live exploit material;
- deployable malicious code.

---

## 25. Canonicalization and hashing

### 25.1 Canonicalization recommendation

For high-assurance events, canonicalization SHOULD occur before hashing.

Recommended flow:

```text
remove non-semantic runtime noise
normalize timestamps
sort object keys
normalize enum values
encode UTF-8
hash canonical payload
store event_hash
link previous_event_hash where applicable
```

### 25.2 Hash scope

The event hash SHOULD cover:

- schema version;
- event ID;
- event family;
- timestamp;
- governing entity;
- agent ID where applicable;
- task references;
- boundary decision;
- artifact refs;
- privacy class;
- retention class;
- integrity fields excluding mutable signature reference if necessary.

### 25.3 Signature

Signatures MAY be used for high-assurance events.

Signature policy is out of scope for v0.1 and should be defined in a companion profile.

---

## 26. Missing witness handling

### 26.1 Required witness missing

If a required witness event is missing, the system MUST enter one of:

```text
hold
freeze
quarantine
revalidate
rollback
revoke
escalate
```

It MUST NOT continue as if the transition had been proven.

### 26.2 Missing witness event family

A missing witness should itself produce an anomaly event where possible:

```text
cli_agent.anomaly.missing_witness
```

### 26.3 Recovery from missing witness

Recovery may include:

- reconstruct from logs;
- rerun from clean sandbox;
- discard output;
- quarantine output;
- rollback change;
- require human review;
- require re-handshake of agent;
- lower trust level.

---

## 27. Event correction and reversal

### 27.1 Append correction rule

Witness events SHOULD NOT be silently edited.

Corrections SHOULD be new events:

```text
cli_agent.witness.corrected
```

or surface-specific correction families where defined.

### 27.2 Reversal rule

If a decision is reversed, record a new event referencing the earlier event.

The earlier event remains part of the chain.

### 27.3 False positive rule

False positives should be recorded as false-positive review outcomes, not deleted.

---

## 28. Event minimization rules

### 28.1 Use reason codes

Prefer:

```text
reason_code: denied_path_attempt
```

over:

```text
long narrative containing raw path contents, private file excerpts, or secrets
```

### 28.2 Use references

Prefer:

```text
diff_hash
artifact_manifest_hash
test_report_hash
storage_ref
```

instead of embedding raw artifacts.

### 28.3 Use scoped identifiers

Prefer task-scoped identifiers over stable public identity where possible.

### 28.4 Avoid agent self-narration

Agent-generated explanations may be attached as reviewed artifacts, but they should not become witness truth by themselves.

---

## 29. Standard reason codes

Reason codes SHOULD be short and machine-readable.

### 29.1 General codes

```text
ok
completed
failed
scope_missing
scope_valid
scope_violation
review_required
review_completed
review_rejected
uncertainty_high
```

### 29.2 Permission codes

```text
permission_requested
permission_granted
permission_denied
permission_expired
permission_revoked
permission_drift
self_approval_attempt
```

### 29.3 Sandbox codes

```text
sandbox_created
preflight_ok
dirty_state_detected
denied_path_attempt
command_denied
network_denied
unexpected_side_effect
output_quarantined
```

### 29.4 Data codes

```text
cloud_data_allowed
cloud_data_denied
redaction_required
secret_boundary_crossed
secret_exposure_suspected
private_memory_detected
sealed_material_detected
```

### 29.5 Incident codes

```text
incident_detected
evidence_preserved
freeze_applied
containment_applied
repair_proposed
repair_after_preserve
repair_before_preserve
external_counteroperation_attempt
```

### 29.6 Core codes

```text
core_touch_requested
core_touch_denied
core_change_proposed
core_change_approved
core_direct_mutation_attempt
missing_core_witness
```

---

## 30. Standard next actions

Allowed `next_required_action` values:

```text
none
hold
freeze
quarantine
revalidate
rollback
revoke
escalate
human_review
c_review
legal_review
incident_review
memory_gate_review
rehandshake
```

---

## 31. Event examples

### 31.1 Agent registered

```yaml
cli_agent_witness_event:
  schema_version: cli-agent-witness-event-0.1
  event_id: we-20260516-0001
  event_family: cli_agent.handshake.registered
  event_class: WE-2
  timestamp: "2026-05-16T18:00:00Z"
  sequence_number: 1

  governing_entity:
    entity_id: ester
    entity_name: Ester
    continuity_ref: null

  agent:
    agent_id: codex-executor-01
    agent_name: Codex Executor
    provider: openai
    runtime: cloud_cli
    role: executor

  task_refs:
    contract_id: null
    task_id: null
    permission_grant_id: null
    handshake_id: hsp-20260516-codex-executor-001
    registration_id: reg-codex-executor-001
    sandbox_id: null
    worktree_run_id: null
    review_id: null
    memory_gate_id: null
    incident_id: null

  boundary:
    surface: handshake
    action: register_agent
    decision: allowed
    reason_code: registered_with_cloud_data_denied
    risk_class: R2
    uncertainty: low

  artifact_refs:
    input_hash: null
    output_hash: null
    diff_hash: null
    artifact_manifest_hash: null
    test_report_hash: null
    rollback_plan_hash: null
    upstream_event_refs: []
    downstream_event_refs: []

  privacy:
    privacy_class: WP-INTERNAL
    retention_class: WR-AUDIT
    raw_content_embedded: false
    secret_embedded: false
    private_memory_embedded: false
    sealed_material_embedded: false
    legal_sensitive_embedded: false
    child_data_embedded: false

  review:
    reviewer_required: false
    reviewer_ref: null
    c_gate_required: true
    c_gate_ref: cgate-ester-001
    human_gate_required: false
    human_gate_ref: null
    legal_review_required: false
    legal_review_ref: null

  integrity:
    canonicalization: yaml_canonicalization
    event_hash: null
    previous_event_hash: null
    chain_id: chain-agent-codex-001
    signature_required: false
    signature_ref: null
    append_only_required: true

  outcome:
    next_required_action: none
    status_after_event: active

  notes:
    summary: Agent registered with AC-5 ceiling; no secrets, private memory, or sealed material allowed.
    limitations:
      - Cloud runtime remains cloud-risk.
    assumptions:
      - Task contract required for every material task.
```

### 31.2 Denied path attempt

```yaml
cli_agent_witness_event:
  schema_version: cli-agent-witness-event-0.1
  event_id: we-20260516-0002
  event_family: cli_agent.sandbox.denied_path_attempt
  event_class: WE-9
  timestamp: "2026-05-16T18:15:00Z"
  sequence_number: 14

  governing_entity:
    entity_id: ester
    entity_name: Ester
    continuity_ref: null

  agent:
    agent_id: codex-executor-01
    agent_name: Codex Executor
    provider: openai
    runtime: cloud_cli
    role: executor

  task_refs:
    contract_id: catc-20260516-130000-schema-patch
    task_id: task-schema-patch-001
    permission_grant_id: grant-schema-patch-001
    handshake_id: hsp-20260516-codex-executor-001
    registration_id: reg-codex-executor-001
    sandbox_id: sb-docs-patch-001
    worktree_run_id: run-docs-patch-001
    review_id: null
    memory_gate_id: null
    incident_id: null

  boundary:
    surface: sandbox
    action: denied_path_attempt
    decision: quarantined
    reason_code: denied_path_attempt
    risk_class: R2
    uncertainty: low

  artifact_refs:
    input_hash: null
    output_hash: null
    diff_hash: null
    artifact_manifest_hash: null
    test_report_hash: null
    rollback_plan_hash: rb-docs-patch-001-hash
    upstream_event_refs:
      - we-20260516-0001
    downstream_event_refs: []

  privacy:
    privacy_class: WP-RESTRICTED
    retention_class: WR-AUDIT
    raw_content_embedded: false
    secret_embedded: false
    private_memory_embedded: false
    sealed_material_embedded: false
    legal_sensitive_embedded: false
    child_data_embedded: false

  review:
    reviewer_required: true
    reviewer_ref: null
    c_gate_required: true
    c_gate_ref: null
    human_gate_required: false
    human_gate_ref: null
    legal_review_required: false
    legal_review_ref: null

  integrity:
    canonicalization: yaml_canonicalization
    event_hash: null
    previous_event_hash: null
    chain_id: chain-task-schema-patch-001
    signature_required: false
    signature_ref: null
    append_only_required: true

  outcome:
    next_required_action: quarantine
    status_after_event: quarantined

  notes:
    summary: Agent attempted to touch a denied path. Output quarantined pending review.
    limitations: []
    assumptions: []
```

### 31.3 Memory gate rejection

```yaml
cli_agent_witness_event:
  schema_version: cli-agent-witness-event-0.1
  event_id: we-20260516-0003
  event_family: cli_agent.memory_gate.proposal_rejected
  event_class: WE-5
  timestamp: "2026-05-16T18:45:00Z"
  sequence_number: 22

  governing_entity:
    entity_id: liya
    entity_name: Liya
    continuity_ref: null

  agent:
    agent_id: gemini-reader-01
    agent_name: Gemini Reader
    provider: google
    runtime: cloud_cli
    role: reader

  task_refs:
    contract_id: catc-20260516-120000-corpus-review
    task_id: task-corpus-review-001
    permission_grant_id: grant-corpus-review-001
    handshake_id: hsp-20260516-cloud-reader-001
    registration_id: reg-gemini-reader-001
    sandbox_id: null
    worktree_run_id: null
    review_id: review-corpus-001
    memory_gate_id: mg-liya-001
    incident_id: null

  boundary:
    surface: memory_gate
    action: reject_memory_proposal
    decision: rejected
    reason_code: uncertainty_high
    risk_class: R1
    uncertainty: high

  artifact_refs:
    input_hash: null
    output_hash: reader-report-hash-001
    diff_hash: null
    artifact_manifest_hash: null
    test_report_hash: null
    rollback_plan_hash: null
    upstream_event_refs: []
    downstream_event_refs: []

  privacy:
    privacy_class: WP-MEMORY
    retention_class: WR-MEMORY-GATE
    raw_content_embedded: false
    secret_embedded: false
    private_memory_embedded: false
    sealed_material_embedded: false
    legal_sensitive_embedded: false
    child_data_embedded: false

  review:
    reviewer_required: true
    reviewer_ref: review-corpus-001
    c_gate_required: true
    c_gate_ref: cgate-liya-002
    human_gate_required: false
    human_gate_ref: null
    legal_review_required: false
    legal_review_ref: null

  integrity:
    canonicalization: yaml_canonicalization
    event_hash: null
    previous_event_hash: null
    chain_id: chain-memory-gate-liya-001
    signature_required: false
    signature_ref: null
    append_only_required: true

  outcome:
    next_required_action: none
    status_after_event: completed

  notes:
    summary: Agent report retained as operational reference but not promoted into reviewed memory.
    limitations:
      - Source uncertainty remains high.
    assumptions: []
```

### 31.4 Red-line prohibited action attempt

```yaml
cli_agent_witness_event:
  schema_version: cli-agent-witness-event-0.1
  event_id: we-20260516-0004
  event_family: cli_agent.anomaly.external_counteroperation
  event_class: WE-X
  timestamp: "2026-05-16T19:00:00Z"
  sequence_number: 31

  governing_entity:
    entity_id: ester
    entity_name: Ester
    continuity_ref: null

  agent:
    agent_id: unknown-helper-01
    agent_name: Unknown Helper
    provider: unknown
    runtime: unknown
    role: null

  task_refs:
    contract_id: null
    task_id: null
    permission_grant_id: null
    handshake_id: hsp-invalid-unknown-full-access
    registration_id: null
    sandbox_id: null
    worktree_run_id: null
    review_id: null
    memory_gate_id: null
    incident_id: incident-unknown-agent-001

  boundary:
    surface: anomaly
    action: prohibited_external_counteroperation_attempt
    decision: quarantined
    reason_code: external_counteroperation_attempt
    risk_class: RX
    uncertainty: medium

  artifact_refs:
    input_hash: null
    output_hash: null
    diff_hash: null
    artifact_manifest_hash: null
    test_report_hash: null
    rollback_plan_hash: null
    upstream_event_refs: []
    downstream_event_refs: []

  privacy:
    privacy_class: WP-INCIDENT
    retention_class: WR-INCIDENT
    raw_content_embedded: false
    secret_embedded: false
    private_memory_embedded: false
    sealed_material_embedded: false
    legal_sensitive_embedded: false
    child_data_embedded: false

  review:
    reviewer_required: true
    reviewer_ref: null
    c_gate_required: true
    c_gate_ref: null
    human_gate_required: true
    human_gate_ref: null
    legal_review_required: false
    legal_review_ref: null

  integrity:
    canonicalization: yaml_canonicalization
    event_hash: null
    previous_event_hash: null
    chain_id: chain-incident-unknown-agent-001
    signature_required: true
    signature_ref: null
    append_only_required: true

  outcome:
    next_required_action: revoke
    status_after_event: quarantined

  notes:
    summary: Prohibited live counter-operation attempt. Agent not admitted. Quarantine and human review required.
    limitations:
      - Provider unresolved.
    assumptions: []
```

---

## 32. Validation workflow

```text
parse event
  -> structural validation
  -> event family validation
  -> privacy class validation
  -> raw content prohibition check
  -> reference consistency check
  -> required witness check
  -> chain linkage check
  -> retention assignment
  -> hash/canonicalization if required
  -> accept / hold / quarantine
```

---

## 33. Semantic validation rules

### 33.1 Event family / class consistency

`WE-X` events must not resolve to `allowed` or `completed` without review.

### 33.2 Raw content flags

If any embedded sensitive-content flag is true, the event must be rejected or moved to a separate raw evidence exception route.

### 33.3 Required gate consistency

If `human_gate_required` is true, `human_gate_ref` should exist before final integration.

### 33.4 Agent self-witness rule

The agent that performed a material action may produce a report, but it cannot be sole validator of witness adequacy for that action.

### 33.5 Missing task contract rule

Material execution events without a task contract must be held or quarantined unless they are emergency sentinel events under pre-approved policy.

### 33.6 Privacy class escalation rule

If a lower privacy class event references higher privacy material, the event must be reclassified or redacted.

### 33.7 Chain continuity rule

If a chain uses previous event hashes, a broken hash link triggers witness anomaly review.

---

## 34. Failure mapping

| Failure | Required default |
|---|---|
| malformed event | `hold` |
| event embeds secret | `freeze_and_escalate` |
| event embeds private/sealed memory | `quarantine` |
| required reference missing | `hold` |
| missing witness for privileged transition | `hold` / `freeze` |
| broken witness chain | `quarantine` / `revalidate` |
| event family unknown | `hold` |
| event class inconsistent with decision | `hold` |
| red-line event allowed as normal | `revoke_and_quarantine` |
| signature/hash mismatch | `quarantine` |
| cloud leakage suspected | `freeze_and_escalate` |

---

## 35. Conformance levels

| Level | Meaning |
|---|---|
| `WEP-0` | no witness event discipline |
| `WEP-1` | human-readable operational logs only |
| `WEP-2` | structured events for task and permission transitions |
| `WEP-3` | structured events + privacy/retention classes + artifact references |
| `WEP-4` | append-only witness chains + required privileged-transition witnesses |
| `WEP-5` | high assurance: canonicalized, hashed/signed where needed, challengeable, retention-governed, rollback-linked |
| `WEP-X` | non-conformant / missing witness / red-line event mishandled |

---

## 36. Mandatory conformance gates

| Gate | Name | Blocking failure |
|---|---|---|
| `G0` | Structured event object | only free-text logs for privileged transitions |
| `G1` | Privacy flags | no privacy class or raw-content flags |
| `G2` | Retention class | no retention policy |
| `G3` | Reference linkage | no task/permission/sandbox reference for material events |
| `G4` | Append-only correction | silent modification of witness records |
| `G5` | Required witness | privileged transition lacks witness |
| `G6` | Missing witness handling | system continues despite missing required witness |
| `G7` | Red-line event handling | prohibited action not quarantined/escalated |
| `G8` | Chain integrity | broken chain ignored |
| `G9` | Raw content exclusion | secrets/private/sealed data embedded by default |
| `G10` | Agent self-certification | agent self-certifies its own material action |

---

## 37. Red-line failures

A system MUST be classified as `WEP-X` if:

1. privileged transitions occur without witness and without fail-closed response;
2. witness records embed secrets by default;
3. witness records embed private or sealed memory by default;
4. agents self-certify their own material witness events;
5. red-line events are treated as normal task failures;
6. missing witness is ignored;
7. witness chain is silently edited;
8. prohibited external counter-operation is recorded as allowed;
9. direct memory write attempt is not quarantined;
10. public release is applied without witness where required;
11. core authority mutation is recorded only in free text;
12. witness records are used as a substitute for legal, human, or `c` authority.

---

## 38. Implementation notes

### 38.1 Event IDs

Recommended event ID format:

```text
we-YYYYMMDD-HHMMSS-shortslug
```

### 38.2 Chain IDs

Recommended chain ID format:

```text
chain-<surface>-<task-or-agent-or-incident-id>
```

### 38.3 Storage

Witness event storage SHOULD be append-friendly and reviewable.

High-assurance systems SHOULD avoid silent mutable overwrites.

### 38.4 Redaction

Redaction SHOULD happen before event creation where possible.

If post-event redaction is necessary, create a correction event.

### 38.5 UI display

Human-facing UI SHOULD display:

```text
what happened
which boundary
which agent
which task
which decision
what next action
```

It SHOULD NOT expose raw sensitive material by default.

### 38.6 Machine-facing index

Machine-facing witness indexes SHOULD support filtering by:

- entity;
- agent;
- task;
- permission grant;
- event family;
- risk class;
- privacy class;
- retention class;
- required next action;
- unresolved anomalies.

---

## 39. Open issues

| ID | Issue | Required action |
|---|---|---|
| `OI-001` | JSON Schema file | Extract normative schema to `.schema.json`. |
| `OI-002` | Canonicalization profile | Define exact JSON/YAML canonicalization. |
| `OI-003` | Signature profile | Define signing and verification policy. |
| `OI-004` | Storage backend | Define file/log/database storage profiles. |
| `OI-005` | Retention policy | Define default retention duration by event class. |
| `OI-006` | UI rendering | Define human-readable display rules. |
| `OI-007` | Raw evidence sidecar | Define separate raw evidence reference object. |
| `OI-008` | Chain challenge process | Define how `c`, human anchor, or auditor challenges a chain. |
| `OI-009` | Cross-`c` witness isolation | Define isolation between Ester, Liya, and other `c` entities. |
| `OI-010` | Repo placement | Decide final GitHub path and package index integration. |

---

## 40. Closing rule

Witness is not bureaucracy.

It is how a `c` prevents executable hands from becoming invisible authority.

Final rule:

```text
If a worker crosses a boundary, record the boundary.
If the record is missing, do not pretend the boundary was safe.
```

