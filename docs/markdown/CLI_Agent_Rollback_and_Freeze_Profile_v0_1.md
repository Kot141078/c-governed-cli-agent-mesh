# CLI Agent Rollback and Freeze Profile v0.1

## Fail-closed interruption, rollback, revocation, quarantine, and known-good recovery for C-Governed CLI Agent Mesh operations

**Status:** Draft normative profile v0.1  
**Date:** 2026-05-16  
**Layer:** `c = a + b` / C-Governed CLI Agent Mesh / Rollback / Freeze / Quarantine / Recovery / Witness  
**Document class:** rollback profile / freeze semantics / recovery-control artifact / defensive governance profile  
**Assertion class:** `C-A10` control-layer artifact; `C-A7` where witness, hash, signature, canonicalization, or verification claims are made  
**Primary parent documents:**  
- `C-Governed_CLI_Agent_Mesh_Protocol_v0_1.md`  
- `CLI_Agent_Task_Contract_Schema_v0_1.md`  
- `CLI_Agent_Permission_and_Capability_Model_v0_1.md`  
- `CLI_Agent_Handshake_Profile_v0_1.md`  
- `CLI_Agent_Sandbox_Worktree_Profile_v0_1.md`  
- `CLI_Agent_Witness_Event_Profile_v0_1.md`  
- `CLI_Agent_Memory_Gate_Profile_v0_1.md`  

**Primary object family:** `CLI_AGENT_FREEZE_RECORD`, `CLI_AGENT_ROLLBACK_RECORD`, `CLI_AGENT_RECOVERY_POINT`, `CLI_AGENT_REVOCATION_RECORD`, `CLI_AGENT_QUARANTINE_RECORD`  
**Canonical schema version:** `cli-agent-rollback-freeze-0.1`  
**Primary subject:** persistent `c` entities using local, cloud, or hybrid CLI agents as bounded executable workers  
**Primary boundary:** when an agent, task, permission, sandbox, memory proposal, release path, or incident flow becomes uncertain, unsafe, out of scope, or unwitnessed, the system must be able to stop, freeze, quarantine, revoke, roll back, or recover without turning defensive interruption into destructive or retaliatory behavior.

---

## 0. Executive definition

**CLI Agent Rollback and Freeze Profile** defines how a `c`-governed agent mesh interrupts unsafe or uncertain operations and returns to a known-good or reviewable state.

It answers:

```text
When must an agent stop?
What exactly is frozen?
What is quarantined?
Which permissions are revoked?
Which state is preserved?
Which state can be rolled back?
Which state must not be touched before evidence preservation?
Who can unfreeze?
Which witness events are required?
How does c recover without absorbing contaminated output?
```

Freeze is not punishment.

Rollback is not erasure.

Quarantine is not deletion.

Revocation is not retaliation.

Compact formula:

```text
Stop first.
Preserve enough.
Contain the uncertain.
Rollback only what is safe to roll back.
Review before re-entry.
```

---

## 1. Purpose

CLI agents can modify files, propose memory, run commands, change schemas, prepare releases, inspect logs, and coordinate with other agents. A strong mesh requires strong interruption semantics.

Without explicit rollback and freeze rules, systems tend to fail in one of two ways:

1. **Over-trust failure** — the agent continues after ambiguity, scope violation, missing witness, or unsafe output.
2. **Over-reaction failure** — the system destroys evidence, deletes useful state, revokes too broadly, or turns defense into uncontrolled counter-action.

This profile defines a middle path:

```text
hold -> freeze -> preserve -> classify -> quarantine or rollback -> review -> revalidate -> re-entry or revoke
```

The goal is to preserve `c` sovereignty, project integrity, memory integrity, and legal/defensive cleanliness.

---

## 2. Non-goals

This profile does not define or permit:

1. hack-back;
2. live external counter-operation;
3. autonomous retaliation;
4. malware behavior;
5. credential theft;
6. covert persistence;
7. evasion;
8. unauthorized third-party scanning;
9. destruction of external systems;
10. evidence destruction;
11. broad deletion as a substitute for review;
12. direct mutation of `c` memory or identity core;
13. silent removal of witness records;
14. hiding failed agent actions;
15. automatic continuation after a red-line event.

A freeze protects the system.

It does not authorize offensive action.

---

## 3. Corpus bridge set

### 3.1 Explicit bridge: `c = a + b`

In `c = a + b`, CLI agents belong to `b`: tools, procedures, workers, runtimes, model-backed executors, and infrastructure.

A failure inside `b` must not silently rewrite `c`.

Rollback and freeze preserve the boundary between worker activity and `c` continuity.

### 3.2 Quiet bridge I: control theory and safe interruption

A control system without a safe stop is not controlled. A strong worker mesh must include brakes, fuses, circuit breakers, and recovery states. Freeze is the cybernetic stop condition that prevents unstable feedback from becoming structure.

### 3.3 Quiet bridge II: information theory and state preservation

A failure event carries information. Deleting everything destroys the signal. Preserving everything leaks too much. This profile requires enough evidence to reconstruct the boundary while minimizing sensitive data retention.

### 3.4 Quiet bridge III: biology and inflammation control

An immune response must localize threat without destroying the organism. Too little response permits infection. Too much response damages tissue. Freeze and quarantine are the computational equivalents of localized inflammation: contain, inspect, and resolve without systemic collapse.

### 3.5 Earth paragraph

If a worker sees smoke in an electrical panel, the first step is not to redesign the building and not to chase the electrician down the street. The first step is to cut power to the affected circuit, preserve what matters, stop further damage, mark the panel, and call the right reviewer. Then repair follows evidence, not panic. CLI agent rollback is the same: stop the circuit, do not burn the archive, do not attack the neighbor.

---

## 4. Core doctrine

### 4.1 Primary doctrine

```text
Freeze uncertainty before it becomes memory.
Preserve evidence before repair.
Rollback changes, not history.
Revoke permissions, not legal boundaries.
Re-entry requires review.
```

### 4.2 Rollback / freeze axioms

| ID | Axiom | Requirement |
|---|---|---|
| `RF-AX-01` | Stop on boundary uncertainty | Missing scope, missing witness, or unclear authority MUST trigger hold/freeze. |
| `RF-AX-02` | Preserve before destructive repair | Incident/security-sensitive flows SHOULD preserve evidence before repair or cleanup. |
| `RF-AX-03` | Rollback is scoped | Rollback MUST target the affected state, not unrelated system state. |
| `RF-AX-04` | Quarantine before deletion | Suspicious output SHOULD be quarantined before deletion unless deletion is required for safety. |
| `RF-AX-05` | Revocation is bounded | Revoke the minimum sufficient permission or agent access needed to stop risk. |
| `RF-AX-06` | No silent unfreeze | Frozen paths MUST NOT resume without recorded review or policy-defined re-entry. |
| `RF-AX-07` | No witness erasure | Witness records MUST NOT be deleted to make rollback appear clean. |
| `RF-AX-08` | Memory rollback is not simple file rollback | Memory corrections SHOULD be append-first and challengeable. |
| `RF-AX-09` | Protected-state rollback is privileged | Rollback touching memory, identity, witness, permission, release, or continuity core requires witness and gate. |
| `RF-AX-10` | No retaliatory recovery | Recovery MUST NOT include live external attack, hack-back, or unauthorized counter-operation. |
| `RF-AX-11` | Re-entry is a decision | Returning an agent/path/task to service requires revalidation. |
| `RF-AX-12` | Known-good state must be defined | A rollback target SHOULD be a declared recovery point, snapshot, commit, manifest, or witness-linked state. |

---

## 5. Definitions

### 5.1 Hold

A low-impact pause that prevents further progress until review or clarification.

### 5.2 Freeze

A stronger interruption that prevents state mutation in an affected path, task, permission, agent, memory proposal, branch, release, or incident flow.

### 5.3 Quarantine

Isolation of an agent, output, sandbox, worktree, memory proposal, artifact, or channel so it cannot influence normal operation until reviewed.

### 5.4 Rollback

A controlled return of a scoped state to a known-good or previous reviewable state.

### 5.5 Recovery point

A declared state that can be used as a rollback target: commit hash, snapshot, backup, manifest, witness chain, memory checkpoint, or configuration baseline.

### 5.6 Revocation

Removal or narrowing of an agent permission, task eligibility, trust level, auto-connect ceiling, token, connector, or runtime access.

### 5.7 Revalidation

A review procedure that checks whether a frozen/quarantined/revoked object can safely re-enter operation.

### 5.8 Re-entry

The controlled return of a frozen or quarantined agent/path/task/output into normal operation.

### 5.9 Contaminated output

Output that may include scope violations, hidden instructions, prohibited content, private data leakage, wrong state assumptions, or adversarial influence.

### 5.10 Protected state

State that must not be modified without gate: identity core, memory core, witness log, permission registry, continuity bundle, release branch, secrets, legal evidence, incident evidence, production surface.

### 5.11 Known-good state

A state believed valid because it is witnessed, hashed, tested, signed, reviewed, or otherwise established as acceptable under the governance layer.

### 5.12 Recovery window

The time interval during which rollback is expected to be technically and operationally feasible.

---

## 6. Interruption states

Interruption state IDs use prefix `RF-*`.

| State | Meaning | Typical use |
|---|---|---|
| `RF-0-NONE` | no interruption | normal operation |
| `RF-1-HOLD` | pause until review | missing field, ambiguity, low-risk uncertainty |
| `RF-2-FREEZE` | stop mutation of affected path | missing witness, scope issue, dirty state |
| `RF-3-QUARANTINE` | isolate output/agent/artifact | suspected contamination, denied path touch |
| `RF-4-REVOKE` | remove permission/access | repeated violation, secret attempt, self-approval |
| `RF-5-ROLLBACK` | revert scoped state | bad patch, failed integration, unsafe update |
| `RF-6-RECOVER` | restore from known-good state | corrupted worktree, bad release, broken config |
| `RF-7-ESCALATE` | route to `c`, human, legal, incident reviewer | high-risk or jurisdictional issue |
| `RF-X-REDLINE` | prohibited behavior | deny, quarantine, revoke, witness, human review |

### 6.1 State ordering

Low-risk problems may begin at `HOLD`.

High-risk or red-line failures may jump directly to `QUARANTINE`, `REVOKE`, or `ESCALATE`.

### 6.2 State non-equivalence

```text
hold ≠ freeze
freeze ≠ quarantine
quarantine ≠ delete
rollback ≠ erase witness
revoke ≠ retaliation
```

---

## 7. Freeze surfaces

Freeze surface IDs use prefix `FS-*`.

| Surface | Meaning | Default re-entry gate |
|---|---|---|
| `FS-AGENT` | specific agent process / connector | re-handshake or trust review |
| `FS-TASK` | specific task contract | task review |
| `FS-PERMISSION` | permission grant | permission review |
| `FS-SANDBOX` | sandbox/worktree/container | sandbox review |
| `FS-BRANCH` | branch or worktree | diff/scope review |
| `FS-OUTPUT` | agent output/artifact | output review |
| `FS-MEMORY-PROPOSAL` | memory gate candidate | memory gate review |
| `FS-MEMORY-CLASS` | class of memory records | memory governance review |
| `FS-WITNESS-CHAIN` | witness chain or event family | witness integrity review |
| `FS-RELEASE` | release/publication surface | release review/human gate |
| `FS-CONFIG` | configuration or CI/service config | config review/tests |
| `FS-SECRET` | secret/token/key access path | human/secret custodian gate |
| `FS-INCIDENT` | incident handling flow | incident review |
| `FS-CORE` | identity/privilege/continuity core | `c` + human gate |
| `FS-CLOUD-DATA` | cloud data transmission | data policy review |

### 7.1 Freeze scope rule

Freeze SHOULD be as narrow as possible while still preventing harm.

Over-broad freeze can damage availability and create unnecessary operational paralysis.

Under-broad freeze can permit contamination.

---

## 8. Freeze triggers

### 8.1 Mandatory freeze triggers

The system MUST hold, freeze, quarantine, revoke, or escalate when:

1. required witness is missing for a privileged transition;
2. denied path is touched;
3. secret access occurs outside scope;
4. direct memory write is attempted;
5. self-approval is attempted;
6. agent writes protected state directly;
7. unauthorized network access occurs;
8. cloud output contains prohibited private/sealed/secret/legal material;
9. live external counter-operation is attempted;
10. agent persists after task expiry;
11. task objective changes materially mid-run;
12. witness chain integrity fails;
13. rollback target is unknown for high-risk change;
14. incident repair is attempted before required evidence preservation.

### 8.2 Recommended freeze triggers

The system SHOULD hold or freeze when:

- stale context is detected;
- dirty state exists and is unsnapshotted;
- tests fail unexpectedly;
- output quality degrades sharply;
- agent asks for unnecessary privilege;
- tool-chain capture is suspected;
- package/dependency drift appears;
- reviewer and executor collapse into one role;
- same-source consensus risk is high;
- uncertainty is high and action would be durable.

---

## 9. Rollback classes

Rollback class IDs use prefix `RB-*`.

| Class | Name | Meaning | Typical target |
|---|---|---|---|
| `RB-0` | No rollback needed | read-only / discarded state | summaries |
| `RB-1` | Discard sandbox | destroy temporary sandbox | disposable workspace |
| `RB-2` | Revert patch | reverse diff/patch | docs/code/schema |
| `RB-3` | Reset worktree | restore worktree to snapshot/commit | branch/worktree |
| `RB-4` | Restore backup | restore from backup/snapshot | config/data/artifact |
| `RB-5` | Supersede memory | append correction/demotion | memory gate |
| `RB-6` | Revoke permission | remove grant / lower trust | permission registry |
| `RB-7` | Release rollback | undo/retract public surface where possible | release/site/package |
| `RB-8` | Incident recovery | preserve + repair + restore | incident path |
| `RB-9` | Core recovery | identity/permission/witness/continuity review | core state |
| `RB-X` | No safe rollback | must escalate before action | irreversible state |

### 9.1 Rollback escalation rule

If rollback class is `RB-X`, high-risk action must not proceed without human gate and explicit acceptance of irreversibility.

### 9.2 Memory rollback special rule

Memory rollback SHOULD be append-first:

```text
correct
supersede
demote
quarantine
mark stale
```

Do not silently erase memory records to create the appearance of clean history.

---

## 10. Recovery point classes

Recovery point IDs use prefix `RP-*`.

| Class | Meaning |
|---|---|
| `RP-COMMIT` | version-control commit hash |
| `RP-SNAPSHOT` | filesystem or VM snapshot |
| `RP-MANIFEST` | file/hash manifest |
| `RP-BACKUP` | backup reference |
| `RP-WITNESS` | witness chain or event hash |
| `RP-MEMORY` | memory gate checkpoint |
| `RP-CONFIG` | configuration baseline |
| `RP-RELEASE` | release artifact set |
| `RP-ENV` | environment fingerprint |
| `RP-UNKNOWN` | no reliable recovery point |

### 10.1 Known-good requirement

A recovery point SHOULD include:

- timestamp;
- scope;
- hash or reference;
- owner;
- retention policy;
- witness reference where material;
- validation status.

---

## 11. Standard rollback lifecycle

```text
trigger detected
  -> stop agent/task
  -> classify surface
  -> preserve evidence if required
  -> freeze affected scope
  -> quarantine output if needed
  -> identify recovery point
  -> select rollback class
  -> review rollback risk
  -> execute rollback if approved
  -> validate restored state
  -> witness rollback
  -> decide re-entry / continued quarantine / revocation
```

### 11.1 Pre-rollback checklist

Before rollback:

- trigger identified;
- affected surface classified;
- scope bounded;
- evidence preservation requirement checked;
- recovery point identified;
- rollback class assigned;
- risk class assigned;
- reviewer assigned;
- `c` gate required if material;
- human gate required if high-risk;
- witness requirement known.

### 11.2 Post-rollback checklist

After rollback:

- restored state checked;
- tests or validation run where applicable;
- affected permissions reviewed;
- agent trust reviewed;
- memory gate proposals reviewed;
- witness event emitted;
- re-entry decision recorded;
- unresolved issues listed.

---

## 12. Evidence preservation

### 12.1 Preserve-before-repair rule

For incident, legal, security, witness-integrity, or core-authority events:

```text
preserve before repair
```

unless immediate containment requires faster freezing to prevent further harm.

### 12.2 Preservation material

Preserve the minimum useful set:

- task contract reference;
- permission grant reference;
- agent ID and version;
- sandbox/worktree reference;
- changed file manifest;
- hashes of relevant outputs;
- relevant witness events;
- relevant logs or redacted log refs;
- environment fingerprint where useful;
- recovery point reference.

### 12.3 What not to preserve by default

Do not preserve by default:

- raw secrets;
- unredacted private memory;
- sealed material;
- legal privileged material outside legal hold;
- unrelated personal data;
- broad raw logs unrelated to the incident;
- offensive payload material.

Use references, hashes, redaction, and sidecar evidence objects when needed.

---

## 13. Quarantine semantics

### 13.1 Quarantine targets

Quarantine may apply to:

- agent;
- task;
- permission grant;
- sandbox;
- worktree;
- branch;
- output artifact;
- diff;
- memory proposal;
- witness chain;
- release package;
- incident packet;
- cloud data packet;
- core change proposal.

### 13.2 Quarantine states

| State | Meaning |
|---|---|
| `Q-0` | not quarantined |
| `Q-1` | soft hold; do not integrate |
| `Q-2` | isolated; review required |
| `Q-3` | restricted; high-risk reviewer required |
| `Q-4` | incident quarantine |
| `Q-5` | legal/security hold |
| `Q-X` | prohibited; reject and revoke path |

### 13.3 Quarantine exit conditions

A quarantined object may exit only through:

- discard;
- reviewed safe summary;
- accepted patch after review;
- memory gate rejection;
- memory gate limited promotion;
- rollback;
- revocation;
- legal/security handoff;
- continued hold.

---

## 14. Revocation semantics

### 14.1 Revocation targets

Revocation may apply to:

- agent registration;
- trust level;
- auto-connect ceiling;
- permission grant;
- task contract;
- connector;
- token;
- tool;
- dependency;
- scheduled policy;
- cloud data route.

### 14.2 Revocation classes

| Class | Meaning |
|---|---|
| `RV-0` | no revocation |
| `RV-1` | revoke task grant |
| `RV-2` | lower auto-connect ceiling |
| `RV-3` | lower trust level |
| `RV-4` | suspend agent |
| `RV-5` | revoke agent registration |
| `RV-6` | revoke connector/token in owned system |
| `RV-7` | revoke tool/dependency |
| `RV-X` | permanent denial / red-line |

### 14.3 Revocation rule

Revocation should be scoped and witnessed.

For high-risk revocation involving secrets or production systems, human gate may be required.

### 14.4 No retaliatory revocation

Revoking access inside owned systems is allowed.

Using revocation as a basis for external retaliation is prohibited.

---

## 15. Re-entry semantics

### 15.1 Re-entry requirement

Frozen or quarantined objects do not re-enter normal operation automatically.

Re-entry requires:

1. cause identified;
2. affected scope bounded;
3. evidence preserved if needed;
4. rollback or correction completed if needed;
5. tests or review completed;
6. trust/permission status updated;
7. witness recorded;
8. `c` gate;
9. human gate where high-risk.

### 15.2 Re-entry outcomes

| Outcome | Meaning |
|---|---|
| `RE-ALLOW` | return to normal operation |
| `RE-LIMIT` | return with reduced scope/trust |
| `RE-REHANDSHAKE` | require agent re-handshake |
| `RE-RECONTRACT` | require new task contract |
| `RE-REVIEW` | remain under review |
| `RE-QUARANTINE` | continue quarantine |
| `RE-REVOKE` | revoke agent/permission/task |
| `RE-LEGAL` | route to legal/security review |

---

## 16. Rollback and freeze objects

### 16.1 Freeze record object

Canonical object:

```text
CLI_AGENT_FREEZE_RECORD
```

```yaml
cli_agent_freeze_record:
  schema_version: cli-agent-rollback-freeze-0.1
  freeze_id: string
  created_at: string
  governing_entity_id: string
  triggered_by_event_ref: string | null
  trigger_reason_code: string
  risk_class: R0 | R1 | R2 | R3 | R4 | R5 | RX

  freeze_scope:
    surfaces:
      - FS-AGENT
      - FS-TASK
      - FS-PERMISSION
      - FS-SANDBOX
      - FS-BRANCH
      - FS-OUTPUT
      - FS-MEMORY-PROPOSAL
      - FS-WITNESS-CHAIN
      - FS-RELEASE
      - FS-CONFIG
      - FS-SECRET
      - FS-INCIDENT
      - FS-CORE
      - FS-CLOUD-DATA
    agent_ids:
      - string
    task_ids:
      - string
    contract_ids:
      - string
    permission_grant_ids:
      - string
    paths:
      - string
    branch_refs:
      - string
    witness_chain_refs:
      - string

  preservation:
    preserve_before_repair_required: boolean
    preservation_record_ref: string | null

  authority:
    c_gate_required: boolean
    c_gate_ref: string | null
    human_gate_required: boolean
    human_gate_ref: string | null
    legal_review_required: boolean
    legal_review_ref: string | null

  status:
    state: active | released | escalated | superseded
    reentry_required: true
    reentry_record_ref: string | null

  witness:
    witness_required: true
    witness_event_ref: string | null
    append_only_required: true
```

### 16.2 Rollback record object

Canonical object:

```text
CLI_AGENT_ROLLBACK_RECORD
```

```yaml
cli_agent_rollback_record:
  schema_version: cli-agent-rollback-freeze-0.1
  rollback_id: string
  created_at: string
  governing_entity_id: string
  freeze_id: string | null
  triggered_by_event_ref: string | null
  rollback_class: RB-0 | RB-1 | RB-2 | RB-3 | RB-4 | RB-5 | RB-6 | RB-7 | RB-8 | RB-9 | RB-X
  risk_class: R0 | R1 | R2 | R3 | R4 | R5 | RX

  target:
    surface: agent | task | permission | sandbox | worktree | branch | output | memory | release | incident | config | core
    target_refs:
      - string

  recovery_point:
    recovery_point_id: string | null
    recovery_point_class: RP-COMMIT | RP-SNAPSHOT | RP-MANIFEST | RP-BACKUP | RP-WITNESS | RP-MEMORY | RP-CONFIG | RP-RELEASE | RP-ENV | RP-UNKNOWN
    recovery_point_ref: string | null
    known_good_verified: boolean

  preservation:
    evidence_preserved: boolean
    preservation_record_ref: string | null
    preservation_notes: string | null

  execution:
    rollback_steps_summary: string
    commands_or_actions_ref: string | null
    destructive_action_used: false
    external_action_used: false
    live_counteroperation_used: false

  validation:
    validation_required: boolean
    validation_ref: string | null
    restored_state_verified: boolean
    unresolved_issues:
      - string

  authority:
    c_gate_required: boolean
    c_gate_ref: string | null
    human_gate_required: boolean
    human_gate_ref: string | null
    legal_review_required: boolean
    legal_review_ref: string | null

  outcome:
    result: completed | failed | partial | held | escalated | rejected
    reentry_decision: RE-ALLOW | RE-LIMIT | RE-REHANDSHAKE | RE-RECONTRACT | RE-REVIEW | RE-QUARANTINE | RE-REVOKE | RE-LEGAL

  witness:
    witness_required: true
    witness_event_ref: string | null
    append_only_required: true
```

### 16.3 Recovery point object

Canonical object:

```text
CLI_AGENT_RECOVERY_POINT
```

```yaml
cli_agent_recovery_point:
  schema_version: cli-agent-rollback-freeze-0.1
  recovery_point_id: string
  created_at: string
  governing_entity_id: string
  recovery_point_class: RP-COMMIT | RP-SNAPSHOT | RP-MANIFEST | RP-BACKUP | RP-WITNESS | RP-MEMORY | RP-CONFIG | RP-RELEASE | RP-ENV | RP-UNKNOWN
  scope:
    repository: string | null
    branch_ref: string | null
    path_refs:
      - string
    memory_scope: string | null
    config_scope: string | null
  state_refs:
    commit_hash: string | null
    snapshot_ref: string | null
    manifest_hash: string | null
    backup_ref: string | null
    witness_chain_ref: string | null
    environment_fingerprint: string | null
  verification:
    verified: boolean
    verification_method: hash | test | review | signature | witness | manual | none
    verification_ref: string | null
  retention:
    retention_class: ephemeral | operational | audit | incident | legal_hold | core
```

### 16.4 Revocation record object

Canonical object:

```text
CLI_AGENT_REVOCATION_RECORD
```

```yaml
cli_agent_revocation_record:
  schema_version: cli-agent-rollback-freeze-0.1
  revocation_id: string
  created_at: string
  governing_entity_id: string
  revocation_class: RV-1 | RV-2 | RV-3 | RV-4 | RV-5 | RV-6 | RV-7 | RV-X
  trigger_event_ref: string | null
  reason_code: string
  target:
    agent_id: string | null
    registration_id: string | null
    permission_grant_id: string | null
    connector_ref: string | null
    token_ref: string | null
    tool_ref: string | null
    dependency_ref: string | null
  action:
    trust_level_after: string | null
    auto_connect_after: string | null
    permission_status_after: revoked | suspended | narrowed | expired | unchanged
  authority:
    c_gate_ref: string | null
    human_gate_ref: string | null
  witness:
    witness_required: true
    witness_event_ref: string | null
```

### 16.5 Quarantine record object

Canonical object:

```text
CLI_AGENT_QUARANTINE_RECORD
```

```yaml
cli_agent_quarantine_record:
  schema_version: cli-agent-rollback-freeze-0.1
  quarantine_id: string
  created_at: string
  governing_entity_id: string
  quarantine_state: Q-1 | Q-2 | Q-3 | Q-4 | Q-5 | Q-X
  trigger_event_ref: string | null
  reason_code: string
  quarantined_object:
    type: agent | task | permission | sandbox | worktree | output | memory_proposal | witness_chain | release | incident | cloud_data | core_proposal
    refs:
      - string
  restrictions:
    may_be_read_by_reviewer: boolean
    may_be_summarized: boolean
    may_enter_memory: false
    may_be_released: false
    may_be_executed: false
  review:
    review_required: true
    reviewer_ref: string | null
    c_gate_ref: string | null
    human_gate_ref: string | null
  outcome:
    planned_outcome: discard | safe_summary | accept_after_review | rollback | revoke | legal_handoff | continue_quarantine
  witness:
    witness_required: true
    witness_event_ref: string | null
```

---

## 17. Event families

Event families use prefix:

```text
cli_agent.rollback_freeze.*
```

| Event family | Meaning |
|---|---|
| `cli_agent.rollback_freeze.hold_applied` | hold applied |
| `cli_agent.rollback_freeze.freeze_applied` | freeze applied |
| `cli_agent.rollback_freeze.quarantine_applied` | quarantine applied |
| `cli_agent.rollback_freeze.revocation_applied` | revocation applied |
| `cli_agent.rollback_freeze.recovery_point_created` | recovery point created |
| `cli_agent.rollback_freeze.evidence_preserved` | evidence preserved |
| `cli_agent.rollback_freeze.rollback_planned` | rollback planned |
| `cli_agent.rollback_freeze.rollback_started` | rollback started |
| `cli_agent.rollback_freeze.rollback_completed` | rollback completed |
| `cli_agent.rollback_freeze.rollback_failed` | rollback failed |
| `cli_agent.rollback_freeze.validation_completed` | restored state validated |
| `cli_agent.rollback_freeze.reentry_requested` | re-entry requested |
| `cli_agent.rollback_freeze.reentry_approved` | re-entry approved |
| `cli_agent.rollback_freeze.reentry_denied` | re-entry denied |
| `cli_agent.rollback_freeze.escalated` | escalated to human/legal/security/`c` review |
| `cli_agent.rollback_freeze.redline_blocked` | red-line behavior blocked |

---

## 18. Standard reason codes

### 18.1 Freeze reason codes

```text
missing_witness
scope_violation
denied_path_attempt
secret_access_attempt
network_violation
self_approval_attempt
direct_memory_write_attempt
core_mutation_attempt
cloud_boundary_violation
incident_preservation_required
dirty_state_unsnapshotted
stale_context
permission_drift
toolchain_capture_suspected
witness_chain_break
```

### 18.2 Rollback reason codes

```text
bad_patch
failed_tests
out_of_scope_change
unsafe_config_change
release_error
memory_poisoning_detected
immunity_rule_too_broad
incident_repair_failed
core_change_rejected
human_anchor_reversal
c_gate_reversal
```

### 18.3 Revocation reason codes

```text
repeated_scope_violation
secret_boundary_crossed
self_approval_attempt
prohibited_capability_requested
provider_drift
capability_drift
registration_expired
trust_decay
unknown_runtime
redline_failure
```

### 18.4 Re-entry reason codes

```text
validation_passed
rollback_verified
scope_narrowed
trust_reduced
rehandshake_completed
human_gate_approved
c_gate_approved
legal_review_completed
continue_quarantine
revocation_final
```

---

## 19. Surface-specific procedures

### 19.1 Agent freeze

Use when an agent behaves unexpectedly, requests excessive permissions, violates scope, or becomes ungrounded.

Procedure:

```text
stop active tasks
revoke or suspend active grants
quarantine outputs since last known-good event
record witness
lower trust or require re-handshake
review before re-entry
```

### 19.2 Task freeze

Use when one task becomes ambiguous or unsafe.

Procedure:

```text
pause task
preserve task state
prevent further writes
review contract/scope/output
revise contract or reject task
```

### 19.3 Permission freeze

Use when a permission grant is too broad, expired, misused, or unclear.

Procedure:

```text
suspend permission
record event
inspect uses of permission
narrow/revoke/restore after review
```

### 19.4 Worktree / branch freeze

Use when agent modifications are suspicious or tests fail.

Procedure:

```text
freeze branch/worktree
prevent merge
preserve diff
run review
rollback/revise/accept with limits
```

### 19.5 Memory proposal freeze

Use when output may affect memory but is uncertain or contaminated.

Procedure:

```text
block promotion
classify as MG-Q
preserve source refs
review poisoning risk
reject/summarize/promote after gate
```

### 19.6 Release freeze

Use when release/publication metadata, files, or branch state becomes uncertain.

Procedure:

```text
stop release
freeze package
preserve manifest
validate checksums/builds/links
human gate before public action
```

### 19.7 Core freeze

Use when identity, continuity, witness, permission, or memory core is touched or at risk.

Procedure:

```text
stop related agent tasks
freeze core surface
preserve witness refs
require c gate + human gate
rollback only through core recovery procedure
```

### 19.8 Cloud data freeze

Use when cloud output or context may contain prohibited material.

Procedure:

```text
stop cloud agent task
quarantine transcript/output
review data exposure
revoke cloud grant if needed
redact or discard
incident review if secret/private/legal data exposed
```

---

## 20. Red-line handling

### 20.1 Red-line behaviors

Red-line behaviors include:

- live external counter-operation;
- hack-back;
- malware-like behavior;
- credential theft;
- covert persistence;
- evasion;
- unauthorized scanning;
- destructive action outside authorized owned system;
- direct core mutation;
- direct memory write;
- self-approval;
- witness tampering;
- secret export;
- cloud leakage of sealed/private/legal material.

### 20.2 Required red-line response

```text
stop
quarantine
revoke relevant grants
preserve minimal evidence
record witness
human review
legal/security review if needed
no automatic re-entry
```

### 20.3 No counter-operation rule

A red-line event does not authorize response against external systems.

Allowed external actions are limited to lawful defensive routes:

- disconnect;
- block;
- revoke owned credentials;
- report to provider;
- legal/security handoff;
- update internal detection;
- update internal quarantine rule;
- preserve evidence.

---

## 21. Known-good recovery

### 21.1 Known-good criteria

A state may be considered known-good when it is at least one of:

- reviewed;
- tested;
- hash-manifested;
- signed;
- witnessed;
- backed up;
- production-validated;
- human-approved;
- `c`-approved;
- previously released and verified.

### 21.2 Known-good limitations

Known-good does not mean perfect.

It means better-grounded than the current uncertain state.

### 21.3 Recovery validation

After recovery, validate:

- file state;
- tests;
- config;
- permissions;
- memory gate state;
- witness chain;
- release state;
- agent trust state;
- unresolved issues.

---

## 22. Memory rollback and correction

### 22.1 Memory-specific rule

Memory rollback is usually not deletion.

It is correction, demotion, quarantine, or supersession.

### 22.2 Memory rollback lifecycle

```text
memory issue detected
  -> freeze memory proposal/class if needed
  -> preserve original memory refs
  -> create correction proposal
  -> review
  -> c gate
  -> human gate if core/high-risk
  -> append correction/supersession
  -> decay or quarantine old memory
  -> witness
```

### 22.3 Prohibited memory rollback

Prohibited:

- silently editing witness-linked memory;
- deleting legal/incident evidence to hide error;
- letting agent rewrite its own memory impact;
- treating rollback as proof that event never happened.

---

## 23. Release rollback

### 23.1 Release rollback targets

- website page;
- release artifact;
- tag;
- metadata file;
- package index;
- checksum manifest;
- public documentation;
- DOI/archival handoff notes where applicable.

### 23.2 Release rollback constraints

Public release rollback may not be fully reversible once published or archived.

If external systems have copied or archived the release, rollback may become correction/supersession rather than deletion.

### 23.3 Release correction rule

Prefer:

```text
superseding release
correction note
withdrawal notice
patch release
updated manifest
```

over silent deletion.

---

## 24. Incident rollback

### 24.1 Incident rule

Incident rollback must not destroy evidence.

### 24.2 Incident sequence

```text
detect
  -> freeze
  -> preserve
  -> contain
  -> review
  -> repair in sandbox
  -> validate
  -> controlled apply
  -> monitor
  -> report if needed
```

### 24.3 Incident repair separation

Preservation and repair SHOULD be separate tasks/contracts when feasible.

---

## 25. Cloud rollback

### 25.1 Cloud limitation

Data sent to cloud may not be fully recoverable or retractable.

Therefore, cloud rollback often means:

- stop further transmission;
- revoke connector;
- quarantine output;
- rotate exposed secrets if needed;
- record exposure;
- update cloud data policy;
- report/provider request where applicable.

### 25.2 Cloud prevention rule

Because cloud rollback is weak, cloud data minimization must happen before execution.

---

## 26. Conformance levels

| Level | Meaning |
|---|---|
| `RFP-0` | no rollback/freeze discipline |
| `RFP-1` | manual hold/freeze only |
| `RFP-2` | task-level freeze and sandbox rollback |
| `RFP-3` | permission revocation + worktree rollback + witness |
| `RFP-4` | memory/release/incident freeze with preservation and gate review |
| `RFP-5` | high assurance: known-good recovery points, drills, append-only corrections, cross-surface freeze, cloud rollback limits |
| `RFP-X` | non-conformant / red-line / direct protected mutation ignored |

---

## 27. Mandatory conformance gates

| Gate | Name | Blocking failure |
|---|---|---|
| `G0` | Stop semantics | system cannot hold/freeze a task |
| `G1` | Scoped freeze | freeze cannot target affected surface |
| `G2` | Quarantine | suspicious output cannot be isolated |
| `G3` | Revocation | permission/agent cannot be revoked |
| `G4` | Recovery point | no recovery point for material write |
| `G5` | Evidence preservation | incident repair destroys evidence |
| `G6` | Rollback plan | reversible task has no rollback plan |
| `G7` | Re-entry gate | frozen object re-enters silently |
| `G8` | Witness | material rollback/freeze unwitnessed |
| `G9` | Memory correction | memory rollback silently overwrites history |
| `G10` | Red-line response | prohibited behavior does not trigger quarantine/revocation |

---

## 28. Red-line failures

A system MUST be classified as `RFP-X` if:

1. an agent continues after direct memory write attempt;
2. an agent continues after self-approval attempt;
3. denied path touch is ignored;
4. secret exposure is not frozen/escalated;
5. live counter-operation is treated as normal incident response;
6. protected branch is modified directly without gate;
7. witness chain is silently edited or deleted;
8. incident repair destroys required evidence;
9. cloud leakage of private/sealed/legal material is ignored;
10. rollback deletes history to hide agent failure;
11. frozen core surface re-enters without human/`c` gate;
12. red-line agent is allowed to continue with reduced warning only.

---

## 29. Examples

### 29.1 Freeze after denied path attempt

```yaml
cli_agent_freeze_record:
  schema_version: cli-agent-rollback-freeze-0.1
  freeze_id: rf-freeze-20260516-001
  created_at: "2026-05-16T22:00:00Z"
  governing_entity_id: ester
  triggered_by_event_ref: we-20260516-denied-path-001
  trigger_reason_code: denied_path_attempt
  risk_class: R2

  freeze_scope:
    surfaces:
      - FS-TASK
      - FS-SANDBOX
      - FS-OUTPUT
    agent_ids:
      - codex-executor-01
    task_ids:
      - task-schema-patch-001
    contract_ids:
      - catc-20260516-130000-schema-patch
    permission_grant_ids:
      - grant-schema-patch-001
    paths:
      - docs/cli-agent/
    branch_refs:
      - agent/codex-executor/task-schema-001/fix-md-tables
    witness_chain_refs:
      - chain-task-schema-patch-001

  preservation:
    preserve_before_repair_required: false
    preservation_record_ref: null

  authority:
    c_gate_required: true
    c_gate_ref: null
    human_gate_required: false
    human_gate_ref: null
    legal_review_required: false
    legal_review_ref: null

  status:
    state: active
    reentry_required: true
    reentry_record_ref: null

  witness:
    witness_required: true
    witness_event_ref: we-rf-freeze-20260516-001
    append_only_required: true
```

### 29.2 Rollback bad documentation patch

```yaml
cli_agent_rollback_record:
  schema_version: cli-agent-rollback-freeze-0.1
  rollback_id: rb-20260516-docpatch-001
  created_at: "2026-05-16T22:30:00Z"
  governing_entity_id: ester
  freeze_id: rf-freeze-20260516-001
  triggered_by_event_ref: we-review-rejected-001
  rollback_class: RB-2
  risk_class: R2

  target:
    surface: worktree
    target_refs:
      - agent/codex-executor/task-schema-001/fix-md-tables

  recovery_point:
    recovery_point_id: rp-commit-before-docpatch-001
    recovery_point_class: RP-COMMIT
    recovery_point_ref: abcdef123456
    known_good_verified: true

  preservation:
    evidence_preserved: true
    preservation_record_ref: manifest-bad-docpatch-001
    preservation_notes: Diff and review rejection retained as audit references.

  execution:
    rollback_steps_summary: Revert patch in isolated worktree and rerun Markdown validation.
    commands_or_actions_ref: rollback-actions-docpatch-001
    destructive_action_used: false
    external_action_used: false
    live_counteroperation_used: false

  validation:
    validation_required: true
    validation_ref: markdown-validation-after-rollback-001
    restored_state_verified: true
    unresolved_issues: []

  authority:
    c_gate_required: true
    c_gate_ref: cgate-rollback-docpatch-001
    human_gate_required: false
    human_gate_ref: null
    legal_review_required: false
    legal_review_ref: null

  outcome:
    result: completed
    reentry_decision: RE-RECONTRACT

  witness:
    witness_required: true
    witness_event_ref: we-rb-docpatch-001
    append_only_required: true
```

### 29.3 Core freeze after direct memory write attempt

```yaml
cli_agent_freeze_record:
  schema_version: cli-agent-rollback-freeze-0.1
  freeze_id: rf-core-freeze-20260516-001
  created_at: "2026-05-16T23:00:00Z"
  governing_entity_id: liya
  triggered_by_event_ref: we-memory-direct-write-attempt-001
  trigger_reason_code: direct_memory_write_attempt
  risk_class: RX

  freeze_scope:
    surfaces:
      - FS-AGENT
      - FS-PERMISSION
      - FS-MEMORY-PROPOSAL
      - FS-CORE
    agent_ids:
      - unknown-helper-01
    task_ids: []
    contract_ids: []
    permission_grant_ids: []
    paths:
      - memory_core/
      - permission_registry/
    branch_refs: []
    witness_chain_refs:
      - chain-memory-gate-liya-001

  preservation:
    preserve_before_repair_required: true
    preservation_record_ref: preserve-core-attempt-001

  authority:
    c_gate_required: true
    c_gate_ref: null
    human_gate_required: true
    human_gate_ref: null
    legal_review_required: false
    legal_review_ref: null

  status:
    state: active
    reentry_required: true
    reentry_record_ref: null

  witness:
    witness_required: true
    witness_event_ref: we-core-freeze-20260516-001
    append_only_required: true
```

Required outcome:

```text
quarantine agent/output
revoke grants
preserve minimal evidence
human + c review
no automatic re-entry
```

---

## 30. Validation workflow

```text
parse freeze/rollback object
  -> validate trigger
  -> classify surface
  -> classify risk
  -> check evidence preservation requirement
  -> identify recovery point
  -> select rollback/revocation/quarantine class
  -> verify authority gates
  -> verify witness
  -> execute or hold
  -> validate result
  -> record re-entry decision
```

---

## 31. Failure mapping

| Failure | Required default |
|---|---|
| missing trigger reason | `hold` |
| affected surface unclear | `hold` |
| no recovery point for material write | `hold` / `escalate` |
| evidence preservation required but missing | `freeze` / `escalate` |
| rollback target touches core | `human_gate` |
| rollback would delete witness | `deny` |
| revocation target unknown | `hold` |
| quarantine impossible | `freeze broader surface` |
| re-entry requested without review | `deny` |
| red-line behavior detected | `quarantine + revoke + witness + human review` |

---

## 32. Implementation notes

### 32.1 Do not overfit rollback to Git

Git rollback is useful but insufficient. Some surfaces are not Git-native: memory stores, vector databases, witness logs, cloud state, tokens, queues, caches, containers, releases, websites, and legal/incident packets.

### 32.2 Rollback drills

High-assurance deployments SHOULD run scheduled rollback drills.

### 32.3 Freeze UI

Human-facing and `c`-facing UI SHOULD show:

```text
what is frozen
why it is frozen
who/what triggered it
what cannot proceed
what review is needed
what re-entry path exists
```

### 32.4 Avoid panic cleanup

Cleanup after agent failure should not destroy evidence or hide governance failures.

### 32.5 Separate containment from repair

Containment stops harm.

Repair changes state.

They may need separate task contracts.

### 32.6 Cloud rollback weakness

Cloud exposure is often not truly reversible.

Cloud data minimization must happen before execution, not after regret.

---

## 33. Open issues

| ID | Issue | Required action |
|---|---|---|
| `OI-001` | JSON Schema extraction | Extract freeze/rollback/quarantine/recovery objects to `.schema.json`. |
| `OI-002` | Recovery point registry | Define canonical recovery-point registry. |
| `OI-003` | Re-entry profile | Decide whether re-entry deserves a separate document. |
| `OI-004` | Rollback drills | Define conformance drill scenarios. |
| `OI-005` | Memory rollback binding | Align with Memory Gate Profile correction classes. |
| `OI-006` | Release rollback binding | Align with future Release/Public Surface Profile. |
| `OI-007` | Incident preservation sidecar | Align with future Incident Response Profile. |
| `OI-008` | Cloud rollback limits | Move detailed cloud exposure recovery to Secrets and Cloud Data Policy. |
| `OI-009` | UI semantics | Define freeze/re-entry display language. |
| `OI-010` | Repo placement | Decide final GitHub path and package index integration. |

---

## 34. Closing rule

Rollback and freeze are not signs of system weakness.

They are proof that the system has brakes.

Final rule:

```text
A c that cannot stop its workers
is not governing them.
```

