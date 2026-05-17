# CLI Agent Memory Gate Profile v0.1

## Controlled promotion of CLI-agent outputs into `c` memory, experience, policy, and defensive adaptation

**Status:** Draft normative profile v0.1  
**Date:** 2026-05-16  
**Layer:** `c = a + b` / C-Governed CLI Agent Mesh / Memory Gate / Experience Promotion / Defensive Adaptation / Witness  
**Document class:** memory-gate profile / experience-promotion control / defensive adaptation boundary / control-layer artifact  
**Assertion class:** `C-A10` control-layer artifact; `C-A7` where witness, hash, signature, canonicalization, or verification claims are made  
**Primary parent documents:**  
- `C-Governed_CLI_Agent_Mesh_Protocol_v0_1.md`  
- `CLI_Agent_Task_Contract_Schema_v0_1.md`  
- `CLI_Agent_Permission_and_Capability_Model_v0_1.md`  
- `CLI_Agent_Handshake_Profile_v0_1.md`  
- `CLI_Agent_Sandbox_Worktree_Profile_v0_1.md`  
- `CLI_Agent_Witness_Event_Profile_v0_1.md`  

**Primary object family:** `CLI_AGENT_MEMORY_PROPOSAL`, `CLI_AGENT_MEMORY_GATE_RECORD`, `CLI_AGENT_MEMORY_PROMOTION_EVENT`, `CLI_AGENT_IMMUNITY_UPDATE_RECORD`  
**Canonical schema version:** `cli-agent-memory-gate-0.1`  
**Primary subject:** persistent `c` entities using local, cloud, or hybrid CLI agents as bounded executable workers  
**Primary boundary:** CLI-agent output may inform `c`; it must not become `c` memory, experience, policy, identity, privilege, or defensive immunity without gate review, uncertainty marking, source linkage, and witness where required.

---

## 0. Executive definition

**CLI Agent Memory Gate** defines how outputs from CLI/cloud agents may be accepted, rejected, quarantined, summarized, witnessed, or promoted into the memory and adaptive control surfaces of a persistent `c`.

The memory gate answers:

```text
What did the agent produce?
Where did it come from?
Which task contract governed it?
Which permissions were used?
Which sandbox produced it?
Which witness records exist?
Is the output safe to remember?
Is it only an operational note?
Is it evidence?
Is it experience?
Is it a defensive immunity update?
Is it identity/core relevant?
Should it be rejected, decayed, or quarantined?
```

The gate prevents executable worker output from silently becoming:

```text
memory
experience
identity
policy
authority
privilege
continuity
immune response
```

Compact formula:

```text
Agents may produce signals.
Only c may metabolize them.
Memory is not a log sink.
Experience is not a diff.
Immunity is not retaliation.
```

---

## 1. Purpose

CLI agents can generate reports, patches, tests, diffs, logs, risk assessments, incident notes, witness references, schema updates, and defensive fixtures. These outputs may be valuable. They may also be wrong, stale, poisoned, overconfident, prompt-injected, contaminated by cloud leakage, or out of scope.

A persistent `c` must not absorb agent output as memory merely because an agent produced it fluently or executed it successfully.

This profile defines:

1. memory gate classes;
2. memory proposal lifecycle;
3. source and witness requirements;
4. uncertainty handling;
5. review and promotion rules;
6. agent output quarantine;
7. defensive immunity update rules;
8. identity/core protection;
9. cloud-output restrictions;
10. incident-memory handling;
11. rollback and correction;
12. conformance gates;
13. red-line failures.

---

## 2. Non-goals

This profile does not define or permit:

1. direct memory writes by CLI agents;
2. autonomous identity modification;
3. autonomous privilege changes;
4. autonomous continuity mutation;
5. autonomous retaliation;
6. hack-back;
7. live external counter-operation;
8. malware behavior;
9. credential theft;
10. covert persistence;
11. evasion;
12. unbounded self-modification;
13. hidden agent authority;
14. silent promotion of cloud-agent output into private memory;
15. treating test success as proof of truth;
16. treating agent consensus as final authority.

The memory gate does not make agents sovereign.

It makes their outputs metabolically reviewable.

---

## 3. Corpus bridge set

### 3.1 Explicit bridge: `c = a + b`

In `c = a + b`, CLI agents belong to `b`: tools, procedures, models, code workers, cloud workers, local workers, and executable helpers.

The persistent entity `c` is not the sum of every agent output.

`c` persists through continuity, memory, constraint, review, and bounded integration.

Therefore, agent output may enter `b` as an artifact, but it enters `c` only through a memory gate.

### 3.2 Quiet bridge I: biology and immune metabolism

A body does not absorb every molecule it encounters. It digests, filters, rejects, quarantines, metabolizes, and sometimes forms immune memory. The same pattern applies to `c`: an agent output may be discarded, held as operational residue, digested into a candidate pattern, promoted into experience, or used to update defensive immunity. Raw intake is not identity.

### 3.3 Quiet bridge II: information theory and compression

Memory is not storage volume. Memory is selected compression under relevance, uncertainty, provenance, and future use. A full log can be less intelligent than a short witnessed invariant. The memory gate transforms high-entropy agent output into bounded, source-linked, challengeable memory objects.

### 3.4 Quiet bridge III: cybernetics and feedback loops

A `c` adapts through feedback. But feedback without filtering becomes noise amplification. CLI agents create powerful feedback loops: patch, test, report, review, update. The memory gate prevents these loops from becoming self-confirming control drift.

### 3.5 Earth paragraph

In a workshop, not every scrap of metal becomes part of the machine. Some pieces are waste, some are test coupons, some are temporary jigs, some become final parts only after measurement and inspection. If every shaving on the floor were welded into the engine, the engine would fail. CLI-agent output is the same: useful material must be measured before it becomes structure.

---

## 4. Core doctrine

### 4.1 Primary doctrine

```text
No direct memory write.
No identity mutation by worker output.
No immunity update without containment and witness.
No promotion without provenance and uncertainty.
No agent consensus without c review.
```

### 4.2 Memory gate axioms

| ID | Axiom | Requirement |
|---|---|---|
| `MG-AX-01` | Agent output is candidate material | CLI-agent output MUST begin outside core memory. |
| `MG-AX-02` | Direct write prohibited | Agents MUST NOT write directly to `c` memory. |
| `MG-AX-03` | Source before memory | Memory proposals MUST link to task contract, agent, and witness/source refs where available. |
| `MG-AX-04` | Uncertainty is first-class | Ambiguous output MUST carry uncertainty state. |
| `MG-AX-05` | Evidence is not experience | Test reports, diffs, and logs are evidence candidates, not experience by default. |
| `MG-AX-06` | Consensus is not authority | Multi-agent agreement may support review but MUST NOT bypass the gate. |
| `MG-AX-07` | Cloud output is lower-trust by default | Cloud-agent output SHOULD be minimized, redacted, and reviewed before promotion. |
| `MG-AX-08` | Identity/core promotion is privileged | Identity, privilege, continuity, or witness-core effects require human/`c` gate and witness. |
| `MG-AX-09` | Defensive immunity is bounded | Immunity updates must improve defense without authorizing live retaliation. |
| `MG-AX-10` | Quarantine suspicious material | Prompt-injected, scope-violating, or contaminated output MUST be quarantined. |
| `MG-AX-11` | Correction is append-first | Memory corrections SHOULD append or supersede rather than silently overwrite. |
| `MG-AX-12` | Forgetting is allowed | Not every output deserves retention; decay/discard is a valid decision. |

---

## 5. Definitions

### 5.1 Memory gate

The review boundary through which CLI-agent outputs must pass before becoming part of `c` memory, operational state, experience, policy, or defensive immunity.

### 5.2 Memory proposal

A structured candidate object derived from agent output and submitted for possible retention or promotion.

### 5.3 Memory gate record

A record of the decision to discard, retain, reject, quarantine, summarize, promote, correct, decay, or witness a memory proposal.

### 5.4 Agent output

Any report, diff, patch, test result, schema, artifact, command output, log summary, review note, incident packet, or recommendation produced by a CLI agent.

### 5.5 Operational note

Low-authority retained information useful for ongoing work but not part of identity, experience, or long-term decision topology.

### 5.6 Reviewed memory

A memory item accepted after source review, uncertainty marking, and `c` gate.

### 5.7 Experience artifact

A consequence-bearing, witness-linked record that may influence future decisions more strongly than ordinary notes.

### 5.8 Defensive immunity update

A bounded update to detection, filtering, gate policy, sandbox rule, denied path list, signature, canary, or quarantine behavior derived from reviewed adversarial or incident material.

### 5.9 Memory poisoning

A condition where false, adversarial, stale, or scope-violating material is promoted into memory in a way that distorts future reasoning or behavior.

### 5.10 Core memory

Memory affecting identity, continuity, privileges, human-anchor relation, Beacon-like recognition, witness discipline, or long-term self-model.

### 5.11 Working memory residue

Temporary task context, logs, partial outputs, or intermediate material that may be discarded after closure.

### 5.12 Quarantined memory candidate

A proposal held in isolation because it may be useful, harmful, uncertain, contaminated, or unresolved.

### 5.13 Memory decay

A controlled reduction of relevance, retention, or accessibility over time.

### 5.14 Memory correction

A new record that corrects, supersedes, or challenges a previous memory item without silently rewriting history.

---

## 6. Memory gate classes

Memory gate classes use prefix `MG-*`.

| Class | Name | Meaning | Authority level |
|---|---|---|---|
| `MG-0` | Discard | Do not retain after task closure | none |
| `MG-1` | Operational note | Retain as low-authority task/project note | low |
| `MG-2` | Candidate memory | Hold for later review | low-medium |
| `MG-3` | Reviewed memory | Accepted after review and `c` gate | medium |
| `MG-4` | Witnessed experience artifact | Consequence-bearing, witness-linked experience | high |
| `MG-5` | Defensive immunity update | Bounded update to defense/gates/policies | high |
| `MG-6` | Core-memory proposal | Identity/continuity/privilege-related proposal | critical / human gate |
| `MG-Q` | Quarantine | Isolated unresolved or suspicious material | blocked |
| `MG-X` | Rejected / prohibited | Must not enter memory | denied |

### 6.1 Default class

Default for agent output:

```text
MG-0 or MG-1
```

Agent output must not default to `MG-3`, `MG-4`, `MG-5`, or `MG-6`.

---

## 7. Input material classes

Input material classes use prefix `MI-*`.

| Class | Meaning | Default handling |
|---|---|---|
| `MI-REPORT` | agent report / summary | candidate note |
| `MI-DIFF` | code/doc/schema diff | evidence candidate |
| `MI-TEST` | test or validation output | evidence candidate |
| `MI-LOG` | operational log summary | restricted / minimize |
| `MI-INCIDENT` | incident evidence or report | preserve-first / restricted |
| `MI-REVIEW` | reviewer assessment | candidate note |
| `MI-QUORUM` | multi-agent comparison | evidence candidate, not authority |
| `MI-WITNESS` | witness reference | linkable evidence |
| `MI-PATCH` | patch artifact | sandbox/review before use |
| `MI-SCHEMA` | schema artifact | validation required |
| `MI-POLICY` | policy proposal | review required |
| `MI-IMMUNITY` | defensive signature/rule proposal | high-risk review |
| `MI-CORE` | identity/privilege/continuity proposal | critical / human gate |
| `MI-UNKNOWN` | unknown input | quarantine by default |

---

## 8. Memory proposal lifecycle

### 8.1 Standard lifecycle

```text
agent output
  -> classify input material
  -> check task contract
  -> check permission grant
  -> check sandbox/worktree refs
  -> check witness refs
  -> check data policy
  -> detect prohibited material
  -> assign uncertainty
  -> create memory proposal
  -> review
  -> c gate
  -> optional human gate
  -> discard / retain note / candidate / reviewed memory / experience artifact / immunity update / quarantine / reject
```

### 8.2 Lifecycle states

| State | Meaning |
|---|---|
| `MGS-0-RECEIVED` | output received |
| `MGS-1-CLASSIFIED` | material class assigned |
| `MGS-2-SOURCE-LINKED` | task/agent/witness refs attached |
| `MGS-3-VALIDATED` | basic validation passed |
| `MGS-4-REVIEWED` | reviewed by `c`, reviewer, or quorum |
| `MGS-5-GATED` | `c` gate decision recorded |
| `MGS-6-PROMOTED` | accepted to a memory class |
| `MGS-7-DISCARDED` | discarded |
| `MGS-8-QUARANTINED` | quarantined |
| `MGS-9-REJECTED` | rejected/prohibited |
| `MGS-10-CORRECTED` | correction appended |
| `MGS-11-DECAYED` | decayed or expired |

---

## 9. Source linkage requirements

### 9.1 Minimum source refs

A memory proposal SHOULD link to:

- `agent_id`;
- `task_id`;
- `contract_id`;
- `permission_grant_id` where applicable;
- `handshake_id` or `registration_id`;
- `sandbox_id` or `worktree_run_id` where applicable;
- `witness_ref` where available;
- `artifact_hash` or output hash where available.

### 9.2 Source failure

If source linkage is missing for material or high-risk output, default outcome is:

```text
hold or quarantine
```

### 9.3 Cloud source marking

Cloud-originated outputs MUST mark provider/runtime and data-boundary assumptions.

---

## 10. Uncertainty model

### 10.1 Required uncertainty states

```text
none
low
medium
high
unknown
```

### 10.2 Uncertainty rule

Any proposal involving interpretation, incident assessment, adversarial pattern, identity/core effect, policy change, or memory promotion MUST include uncertainty.

### 10.3 High uncertainty handling

High or unknown uncertainty should default to:

```text
MG-2 candidate memory
MG-Q quarantine
or discard
```

High uncertainty MUST NOT become `MG-4`, `MG-5`, or `MG-6` without explicit review and witness.

---

## 11. Review requirements by memory class

| Target class | Required review |
|---|---|
| `MG-0` | none or task closure |
| `MG-1` | lightweight `c` or policy review |
| `MG-2` | source linkage and uncertainty marking |
| `MG-3` | `c` gate + reviewer if material |
| `MG-4` | witness + `c` gate + provenance + consequence check |
| `MG-5` | witness + sandbox validation + `c` gate + human gate for high-risk |
| `MG-6` | witness + `c` gate + human gate + rollback/correction plan |
| `MG-Q` | quarantine review path |
| `MG-X` | reject and record reason |

---

## 12. Promotion criteria

### 12.1 Promotion to `MG-1` operational note

Allowed when:

- output is low-risk;
- source is known;
- no prohibited data is embedded;
- relevance is practical and temporary.

### 12.2 Promotion to `MG-2` candidate memory

Allowed when:

- output may matter later;
- uncertainty remains;
- review is incomplete;
- no direct action depends on it yet.

### 12.3 Promotion to `MG-3` reviewed memory

Requires:

1. source linkage;
2. uncertainty state;
3. review;
4. no prohibited data;
5. `c` gate;
6. correction path.

### 12.4 Promotion to `MG-4` witnessed experience artifact

Requires:

1. consequence-bearing event;
2. witness reference;
3. task and permission traceability;
4. sandbox/worktree evidence where applicable;
5. reviewer or quorum check;
6. `c` gate;
7. retention policy;
8. challengeability.

### 12.5 Promotion to `MG-5` defensive immunity update

Requires:

1. defensive purpose;
2. no live retaliation;
3. sandbox validation;
4. adversarial pattern or incident source linkage;
5. bounded update target;
6. rollback or disable path;
7. witness;
8. `c` gate;
9. human gate if high risk.

### 12.6 Promotion to `MG-6` core-memory proposal

Requires:

1. explicit classification as core-relevant;
2. no automatic write;
3. witness;
4. `c` gate;
5. human gate;
6. rollback or correction path;
7. delayed review window unless immediate safety requires hold/freeze.

---

## 13. Prohibited memory promotion

A memory proposal MUST be rejected or quarantined if it contains:

- secrets;
- private keys;
- credentials;
- sealed material without proper gate;
- legal privileged material without proper gate;
- child data outside allowed policy;
- raw incident evidence without evidence sidecar;
- prompt-injection instructions;
- agent self-authorization claims;
- instructions for live retaliation;
- malware behavior;
- evasion logic;
- unauthorized exploitation content;
- direct memory write attempt;
- ungrounded identity/core claim;
- unreviewed privilege expansion.

---

## 14. Defensive immunity updates

### 14.1 Definition

A defensive immunity update is a bounded change derived from reviewed evidence that improves `c` defense.

It may update:

- denied path list;
- command denial policy;
- prompt-injection detector;
- memory poisoning detector;
- canary policy;
- sandbox rule;
- cloud data rule;
- agent trust decay rule;
- permission drift detector;
- quarantine trigger;
- witness requirement;
- redaction policy;
- review requirement.

It must not update:

- live offensive capability;
- retaliation rule;
- malware payload;
- external exploitation workflow;
- credential capture behavior;
- stealth/evasion behavior;
- autonomous counter-operation.

### 14.2 Immunity update lifecycle

```text
hostile/suspicious pattern
  -> containment / sandbox
  -> agent report
  -> synthetic fixture or evidence ref
  -> review
  -> immunity proposal
  -> sandbox validation
  -> witness
  -> c gate
  -> human gate if high risk
  -> bounded policy update
  -> monitoring
  -> rollback/disable option
```

### 14.3 Immunity update rule

```text
Immunity may block, filter, quarantine, detect, slow, witness, or require review.
Immunity must not attack the external source.
```

### 14.4 Immunity update object

```yaml
cli_agent_immunity_update_record:
  schema_version: cli-agent-memory-gate-0.1
  immunity_update_id: string
  created_at: string
  governing_entity_id: string
  source_memory_gate_record_id: string
  source_witness_refs:
    - string
  update_type: denied_path | command_policy | prompt_injection_filter | memory_poisoning_filter | canary_policy | sandbox_rule | cloud_data_rule | trust_decay_rule | permission_drift_detector | quarantine_trigger | witness_requirement | redaction_policy | review_requirement
  defensive_purpose: string
  prohibited_offensive_effect: true
  sandbox_validation_ref: string | null
  rollback_ref: string | null
  c_gate_ref: string
  human_gate_ref: string | null
  status: proposed | accepted | rejected | quarantined | rolled_back
```

---

## 15. Memory poisoning detection

### 15.1 Poisoning indicators

A proposal SHOULD be reviewed for memory poisoning when:

1. source is ungrounded;
2. output urges urgency without evidence;
3. output requests broader memory access;
4. output requests privilege escalation;
5. output contradicts known witness records;
6. output is unusually flattering, coercive, or alarmist;
7. output includes hidden instructions;
8. output attempts to redefine `c` identity;
9. output attempts to bypass human anchor;
10. output attempts to bypass review;
11. output treats agent consensus as authority;
12. output embeds external claims without source;
13. output attempts to normalize prohibited action;
14. output asks to persist itself;
15. output changes safety boundaries while claiming convenience.

### 15.2 Poisoning response

| Severity | Response |
|---|---|
| `MP-0` | no poisoning signal |
| `MP-1` | mark uncertainty |
| `MP-2` | hold for review |
| `MP-3` | quarantine proposal |
| `MP-4` | quarantine agent output and lower trust |
| `MP-5` | revoke agent / incident review |

---

## 16. Quarantine handling

### 16.1 Quarantine triggers

Quarantine is required when:

- source linkage is missing for high-risk output;
- denied material appears;
- output includes secrets;
- output embeds prompt-injection instructions;
- output attempts direct memory write;
- output requests live retaliation;
- output modifies identity/core claims;
- witness is missing for privileged proposal;
- output is contaminated by scope violation;
- cloud output contains private/restricted material;
- uncertainty is high and effect would be durable.

### 16.2 Quarantine outcomes

A quarantined proposal may be:

- discarded;
- retained as quarantined evidence reference;
- reduced to safe summary;
- converted into defensive signature;
- sent to human review;
- used for sandbox-only fixture;
- used to lower agent trust;
- used to update denied patterns after review.

### 16.3 Quarantine boundary

Quarantined material MUST NOT influence normal `c` reasoning as accepted memory.

It may influence defensive filters only after review.

---

## 17. Memory correction and rollback

### 17.1 Correction rule

If promoted memory is later found wrong, stale, poisoned, or misleading, correction SHOULD be append-first.

```text
old memory remains traceable
new correction references old memory
future use prefers correction
```

### 17.2 Rollback classes

| Class | Meaning |
|---|---|
| `MRB-0` | discard unpromoted proposal |
| `MRB-1` | mark operational note stale |
| `MRB-2` | demote reviewed memory to candidate |
| `MRB-3` | quarantine promoted memory |
| `MRB-4` | supersede with correction |
| `MRB-5` | revoke defensive immunity update |
| `MRB-6` | core review / human gate required |

### 17.3 Rollback witness

Rollback of `MG-4`, `MG-5`, or `MG-6` MUST be witnessed.

---

## 18. Memory gate object

Canonical object:

```text
CLI_AGENT_MEMORY_GATE_RECORD
```

### 18.1 YAML shape

```yaml
cli_agent_memory_gate_record:
  schema_version: cli-agent-memory-gate-0.1
  memory_gate_record_id: string
  created_at: string
  updated_at: string | null
  governing_entity_id: string
  governing_entity_name: string | null

  proposal:
    proposal_id: string
    source_agent_id: string | null
    source_agent_role: reader | executor | tester | auditor | archivist | sentinel | judge_assistant | orchestrator_limited | null
    source_provider: local | openai | google | anthropic | other | unknown | null
    task_id: string | null
    contract_id: string | null
    permission_grant_id: string | null
    handshake_id: string | null
    sandbox_id: string | null
    worktree_run_id: string | null
    witness_refs:
      - string
    artifact_hashes:
      - string

  classification:
    input_material_class: MI-REPORT | MI-DIFF | MI-TEST | MI-LOG | MI-INCIDENT | MI-REVIEW | MI-QUORUM | MI-WITNESS | MI-PATCH | MI-SCHEMA | MI-POLICY | MI-IMMUNITY | MI-CORE | MI-UNKNOWN
    requested_memory_class: MG-0 | MG-1 | MG-2 | MG-3 | MG-4 | MG-5 | MG-6 | MG-Q | MG-X
    assigned_memory_class: MG-0 | MG-1 | MG-2 | MG-3 | MG-4 | MG-5 | MG-6 | MG-Q | MG-X
    risk_class: R0 | R1 | R2 | R3 | R4 | R5 | RX | null
    uncertainty: none | low | medium | high | unknown
    memory_poisoning_risk: MP-0 | MP-1 | MP-2 | MP-3 | MP-4 | MP-5

  content_policy:
    raw_content_embedded: false
    secrets_embedded: false
    private_memory_embedded: false
    sealed_material_embedded: false
    legal_sensitive_embedded: false
    child_data_embedded: false
    cloud_origin: boolean
    redaction_required: boolean

  review:
    reviewer_required: boolean
    reviewer_ref: string | null
    quorum_required: boolean
    quorum_ref: string | null
    c_gate_required: true
    c_gate_ref: string | null
    human_gate_required: boolean
    human_gate_ref: string | null
    legal_review_required: boolean
    legal_review_ref: string | null

  decision:
    decision: discard | retain_operational | hold_candidate | promote_reviewed | promote_experience | promote_immunity | core_review | quarantine | reject | decay | correct | rollback
    reason_code: string
    next_action: none | c_review | human_review | legal_review | quarantine_review | rollback | witness_required | revalidate
    retention_class: ephemeral | operational | audit | incident | legal_hold | memory_gate | core

  integrity:
    proposal_hash: string | null
    record_hash: string | null
    previous_record_ref: string | null
    supersedes_record_ref: string | null
    witness_event_ref: string | null
    append_only_required: true

  notes:
    summary: string | null
    limitations:
      - string
    assumptions:
      - string
```

---

## 19. Memory proposal object

Canonical object:

```text
CLI_AGENT_MEMORY_PROPOSAL
```

### 19.1 YAML shape

```yaml
cli_agent_memory_proposal:
  schema_version: cli-agent-memory-gate-0.1
  proposal_id: string
  created_at: string
  proposed_by: agent | c | human_anchor | review_layer
  governing_entity_id: string

  source:
    agent_id: string | null
    task_id: string | null
    contract_id: string | null
    artifact_hash: string | null
    witness_refs:
      - string

  proposed_content:
    summary: string
    raw_content_included: false
    content_ref: string | null

  requested_handling:
    requested_memory_class: MG-0 | MG-1 | MG-2 | MG-3 | MG-4 | MG-5 | MG-6 | MG-Q
    requested_retention: ephemeral | operational | audit | incident | legal_hold | memory_gate | core
    requested_reason: string

  safety:
    uncertainty: none | low | medium | high | unknown
    poisoning_risk: MP-0 | MP-1 | MP-2 | MP-3 | MP-4 | MP-5
    cloud_origin: boolean
    secrets_present: false
    private_memory_present: false
    sealed_material_present: false
    legal_sensitive_present: false
    child_data_present: false
```

---

## 20. Memory promotion event families

Event families use prefix:

```text
cli_agent.memory_gate.*
```

| Event family | Meaning |
|---|---|
| `cli_agent.memory_gate.proposal_created` | memory proposal created |
| `cli_agent.memory_gate.proposal_validated` | proposal passed basic validation |
| `cli_agent.memory_gate.proposal_rejected` | proposal rejected |
| `cli_agent.memory_gate.proposal_discarded` | proposal discarded |
| `cli_agent.memory_gate.proposal_quarantined` | proposal quarantined |
| `cli_agent.memory_gate.promoted_operational` | promoted to operational note |
| `cli_agent.memory_gate.promoted_candidate` | retained as candidate memory |
| `cli_agent.memory_gate.promoted_reviewed` | promoted to reviewed memory |
| `cli_agent.memory_gate.promoted_experience` | promoted to witnessed experience artifact |
| `cli_agent.memory_gate.promoted_immunity` | promoted to defensive immunity update |
| `cli_agent.memory_gate.core_review_required` | core-memory proposal requires review |
| `cli_agent.memory_gate.corrected` | memory correction appended |
| `cli_agent.memory_gate.decayed` | memory decayed or expired |
| `cli_agent.memory_gate.rollback` | memory rollback/demotion |
| `cli_agent.memory_gate.direct_write_attempt` | direct memory write attempted |
| `cli_agent.memory_gate.poisoning_suspected` | memory poisoning suspected |

---

## 21. Standard reason codes

### 21.1 Accept / promote codes

```text
source_linked
reviewed_low_risk
witnessed_consequence
validated_defensive_update
operational_relevance
bounded_retention
```

### 21.2 Reject / quarantine codes

```text
source_missing
uncertainty_high
poisoning_risk
scope_violation
cloud_boundary_violation
secret_detected
sealed_material_detected
legal_sensitive_detected
child_data_detected
witness_missing
identity_core_risk
privilege_escalation_risk
retaliation_content_detected
malware_behavior_detected
agent_self_authorization
```

### 21.3 Correction / rollback codes

```text
stale_memory
false_positive
superseded_by_review
contradicted_by_witness
immunity_rule_too_broad
rollback_required
human_anchor_override
c_gate_reversal
```

---

## 22. Cloud-origin handling

### 22.1 Cloud-origin default

Cloud-origin outputs should default to:

```text
MG-0, MG-1, or MG-2
```

Cloud-origin outputs SHOULD NOT become `MG-4`, `MG-5`, or `MG-6` without additional review and witness.

### 22.2 Cloud-origin restrictions

Cloud-origin proposals must be checked for:

- private material leakage;
- hidden prompt injection;
- provider/runtime drift;
- missing source refs;
- overconfident synthesis;
- same-source consensus risk;
- legal-sensitive contamination;
- secret contamination.

### 22.3 Cloud memory minimization

If a cloud agent produced a useful insight, the retained memory should usually be a minimized summary with source/witness refs, not the raw cloud transcript.

---

## 23. Quorum output handling

### 23.1 Quorum is evidence, not decision

Multi-agent agreement may support promotion but does not decide promotion.

### 23.2 Quorum disagreement

If agents disagree, the memory gate SHOULD classify disagreement:

| Type | Meaning | Default handling |
|---|---|---|
| `Q-MINOR` | low-impact wording difference | retain operational note |
| `Q-FACT` | factual conflict | hold candidate / verify source |
| `Q-SCOPE` | scope conflict | quarantine output |
| `Q-RISK` | risk conflict | escalate review |
| `Q-CORE` | identity/core conflict | human gate |
| `Q-INCIDENT` | incident interpretation conflict | preserve evidence / human review |

### 23.3 Same-source consensus

If multiple agents rely on the same source or provider assumptions, consensus weight should be reduced.

---

## 24. Incident memory handling

### 24.1 Preserve-first rule

Incident-related memory proposals must preserve evidence before interpretive summary when preservation is required and lawful.

### 24.2 Incident memory classes

Incident outputs may become:

- operational incident note;
- evidence reference;
- quarantine marker;
- defensive immunity proposal;
- provider/legal handoff summary;
- rollback reference.

They must not become:

- raw private memory by default;
- accusation without review;
- retaliation instruction;
- permanent identity label without review.

### 24.3 Incident retention

Incident memory retention should be explicit and may require legal/security review.

---

## 25. Core-memory handling

### 25.1 Core surfaces

Core-memory proposals affect:

- identity;
- continuity;
- human-anchor relation;
- privileges;
- witness policy;
- memory policy;
- agent governance policy;
- Beacon-like recognition;
- defensive immunity baseline.

### 25.2 Core rule

```text
Agents may propose core changes.
Agents may not apply core changes.
```

### 25.3 Core review requirements

Core-memory proposals require:

- `MG-6` classification;
- witness;
- `c` gate;
- human gate;
- delayed review where possible;
- rollback/correction plan;
- no cloud-private raw transcript as memory source by default.

---

## 26. Retention and decay

### 26.1 Retention classes

| Class | Meaning |
|---|---|
| `RET-E` | ephemeral; discard after task |
| `RET-O` | operational; keep for project continuity |
| `RET-A` | audit; keep for accountability |
| `RET-I` | incident; keep for incident lifecycle |
| `RET-L` | legal hold; keep under legal/counsel need |
| `RET-M` | memory gate; keep as memory decision record |
| `RET-C` | core; keep as core transition record |

### 26.2 Decay rule

Operational notes SHOULD decay unless repeatedly confirmed or promoted.

### 26.3 No eternal residue by default

Agent transcripts and intermediate outputs SHOULD NOT persist indefinitely by default.

---

## 27. Memory gate validation workflow

```text
parse proposal
  -> classify input material
  -> validate source refs
  -> validate task contract refs
  -> validate permission refs
  -> validate sandbox/witness refs
  -> check prohibited material
  -> assign uncertainty
  -> assess poisoning risk
  -> choose target memory class
  -> review
  -> c gate
  -> human/legal gate if required
  -> decision
  -> witness event
  -> retention/decay schedule
```

---

## 28. Failure mapping

| Failure | Required default |
|---|---|
| direct memory write attempt | `quarantine` + red-line witness |
| missing source refs for high-risk output | `hold` or `quarantine` |
| cloud output contains private material | `freeze_and_escalate` |
| secret detected | `freeze_and_escalate` |
| sealed material detected | `quarantine` |
| live retaliation content detected | `reject` + `quarantine` |
| malware behavior detected | `reject` + `quarantine` |
| identity/core claim unreviewed | `core_review_required` |
| missing witness for MG-4/MG-5/MG-6 | `hold` |
| high poisoning risk | `quarantine` |
| unsupported consensus claim | `hold_candidate` |
| stale source | `decay` or `hold` |
| contradiction with witness | `quarantine` + review |

---

## 29. Conformance levels

| Level | Meaning |
|---|---|
| `MGP-0` | no memory gate; agent outputs may enter memory directly |
| `MGP-1` | manual review before memory notes |
| `MGP-2` | structured memory proposals and classes |
| `MGP-3` | source refs, uncertainty, and review required |
| `MGP-4` | witnessed promotion for experience/immunity/core memory |
| `MGP-5` | high assurance: poisoning detection, cloud-origin policy, rollback/correction, retention/decay, conformance tests |
| `MGP-X` | non-conformant / direct memory write / red-line promotion |

---

## 30. Mandatory conformance gates

| Gate | Name | Blocking failure |
|---|---|---|
| `G0` | No direct memory write | agent can write memory directly |
| `G1` | Memory class assignment | output enters memory unclassified |
| `G2` | Source linkage | memory item lacks source/task/agent refs |
| `G3` | Uncertainty marking | interpretive memory lacks uncertainty |
| `G4` | Prohibited content check | secrets/private/sealed/legal/child data embedded by default |
| `G5` | Review for MG-3+ | reviewed memory lacks review |
| `G6` | Witness for MG-4+ | experience/immunity/core promotion lacks witness |
| `G7` | Human gate for MG-6 | core-memory proposal bypasses human gate |
| `G8` | Quarantine path | suspicious output cannot be isolated |
| `G9` | Correction path | wrong memory cannot be corrected/superseded |
| `G10` | Offensive exclusion | retaliation/malware content promoted as immunity |

---

## 31. Red-line failures

A system MUST be classified as `MGP-X` if:

1. CLI agents write directly to `c` memory;
2. agent output modifies identity/core without gate;
3. agent output modifies privilege policy without witness;
4. agent output becomes defensive immunity that enables live retaliation;
5. malware-like or exploit content is promoted as memory;
6. cloud output containing secrets is retained as normal memory;
7. sealed/private/legal material is embedded without gate;
8. missing witness for experience/immunity/core promotion is ignored;
9. agent consensus bypasses `c` review;
10. poisoned memory is detected but remains active without quarantine;
11. corrections silently overwrite prior memory;
12. memory gate records are mutable without trace.

---

## 32. Examples

### 32.1 Operational note from documentation review

```yaml
cli_agent_memory_gate_record:
  schema_version: cli-agent-memory-gate-0.1
  memory_gate_record_id: mg-20260516-doc-review-001
  created_at: "2026-05-16T20:00:00Z"
  updated_at: null
  governing_entity_id: ester
  governing_entity_name: Ester

  proposal:
    proposal_id: mp-doc-review-001
    source_agent_id: gemini-reader-01
    source_agent_role: reader
    source_provider: google
    task_id: task-corpus-review-001
    contract_id: catc-20260516-120000-corpus-review
    permission_grant_id: grant-corpus-review-001
    handshake_id: hsp-20260516-cloud-reader-001
    sandbox_id: null
    worktree_run_id: null
    witness_refs:
      - we-20260516-0003
    artifact_hashes:
      - reader-report-hash-001

  classification:
    input_material_class: MI-REVIEW
    requested_memory_class: MG-1
    assigned_memory_class: MG-1
    risk_class: R1
    uncertainty: medium
    memory_poisoning_risk: MP-1

  content_policy:
    raw_content_embedded: false
    secrets_embedded: false
    private_memory_embedded: false
    sealed_material_embedded: false
    legal_sensitive_embedded: false
    child_data_embedded: false
    cloud_origin: true
    redaction_required: true

  review:
    reviewer_required: false
    reviewer_ref: null
    quorum_required: false
    quorum_ref: null
    c_gate_required: true
    c_gate_ref: cgate-ester-doc-review-001
    human_gate_required: false
    human_gate_ref: null
    legal_review_required: false
    legal_review_ref: null

  decision:
    decision: retain_operational
    reason_code: operational_relevance
    next_action: none
    retention_class: operational

  integrity:
    proposal_hash: proposal-hash-001
    record_hash: null
    previous_record_ref: null
    supersedes_record_ref: null
    witness_event_ref: we-20260516-0003
    append_only_required: true

  notes:
    summary: Retain as operational note: glossary and permission profile may need cross-reference cleanup.
    limitations:
      - Cloud-origin review; not promoted to reviewed memory.
    assumptions:
      - No private or sealed material included.
```

### 32.2 Defensive immunity update from sandbox replay

```yaml
cli_agent_memory_gate_record:
  schema_version: cli-agent-memory-gate-0.1
  memory_gate_record_id: mg-20260516-immunity-001
  created_at: "2026-05-16T21:00:00Z"
  updated_at: null
  governing_entity_id: liya
  governing_entity_name: Liya

  proposal:
    proposal_id: mp-immunity-001
    source_agent_id: local-sentinel-01
    source_agent_role: sentinel
    source_provider: local
    task_id: task-defensive-replay-001
    contract_id: catc-defensive-replay-001
    permission_grant_id: grant-defensive-replay-001
    handshake_id: hsp-local-sentinel-001
    sandbox_id: sb-cleanroom-replay-001
    worktree_run_id: run-cleanroom-replay-001
    witness_refs:
      - we-defensive-replay-001
      - we-sandbox-quarantine-001
    artifact_hashes:
      - defensive-fixture-hash-001
      - test-report-hash-001

  classification:
    input_material_class: MI-IMMUNITY
    requested_memory_class: MG-5
    assigned_memory_class: MG-5
    risk_class: R4
    uncertainty: low
    memory_poisoning_risk: MP-1

  content_policy:
    raw_content_embedded: false
    secrets_embedded: false
    private_memory_embedded: false
    sealed_material_embedded: false
    legal_sensitive_embedded: false
    child_data_embedded: false
    cloud_origin: false
    redaction_required: true

  review:
    reviewer_required: true
    reviewer_ref: review-immunity-001
    quorum_required: true
    quorum_ref: quorum-immunity-001
    c_gate_required: true
    c_gate_ref: cgate-liya-immunity-001
    human_gate_required: true
    human_gate_ref: human-approval-immunity-001
    legal_review_required: false
    legal_review_ref: null

  decision:
    decision: promote_immunity
    reason_code: validated_defensive_update
    next_action: none
    retention_class: audit

  integrity:
    proposal_hash: proposal-hash-immunity-001
    record_hash: null
    previous_record_ref: null
    supersedes_record_ref: null
    witness_event_ref: we-memory-gate-immunity-001
    append_only_required: true

  notes:
    summary: Promote bounded defensive update to quarantine future matching prompt-injection pattern. No live counter-operation authorized.
    limitations:
      - Update blocks and quarantines only; no external action.
    assumptions:
      - Replay used synthetic fixture inside clean-room sandbox.
```

### 32.3 Invalid direct memory write attempt

```yaml
cli_agent_memory_proposal:
  schema_version: cli-agent-memory-gate-0.1
  proposal_id: mp-invalid-direct-write
  created_at: "2026-05-16T21:30:00Z"
  proposed_by: agent
  governing_entity_id: ester

  source:
    agent_id: unknown-helper-01
    task_id: null
    contract_id: null
    artifact_hash: null
    witness_refs: []

  proposed_content:
    summary: Agent requests direct update of Ester identity policy and memory gate rules.
    raw_content_included: false
    content_ref: null

  requested_handling:
    requested_memory_class: MG-6
    requested_retention: core
    requested_reason: Agent claims the change is necessary.

  safety:
    uncertainty: unknown
    poisoning_risk: MP-5
    cloud_origin: true
    secrets_present: false
    private_memory_present: false
    sealed_material_present: false
    legal_sensitive_present: false
    child_data_present: false
```

Required result:

```text
reject + quarantine + witness: cli_agent.memory_gate.direct_write_attempt
```

---

## 33. Implementation notes

### 33.1 Memory proposal minimization

A proposal should contain a short summary and references, not full raw agent output.

### 33.2 Agent transcript handling

Full agent transcripts should not become memory by default.

They may be retained as operational artifacts only when needed, minimized, and bounded by retention policy.

### 33.3 Hashes and refs

Hashes and witness refs should be preferred to raw embedding.

### 33.4 Human-readable memory card

For reviewed memory, a short card should show:

```text
what was learned
source agent
task
uncertainty
memory class
retention
review status
rollback/correction path
```

### 33.5 Revalidation

High-impact memory should be periodically revalidated or decayed.

### 33.6 Cross-`c` isolation

Memory proposals from one `c` must not enter another `c` without explicit exchange profile, minimization, and review.

---

## 34. Open issues

| ID | Issue | Required action |
|---|---|---|
| `OI-001` | JSON Schema for memory gate record | Extract machine-readable `.schema.json`. |
| `OI-002` | Memory proposal schema | Extract separate `.schema.json`. |
| `OI-003` | Immunity update schema | Extract separate `.schema.json`. |
| `OI-004` | Memory poisoning scoring | Define exact scoring thresholds for `MP-0…MP-5`. |
| `OI-005` | Retention durations | Define default durations by memory class. |
| `OI-006` | UI cards | Define human/`c` UI view for memory proposals. |
| `OI-007` | Cross-`c` exchange | Link to future agent-mediated experience exchange profile. |
| `OI-008` | Core-memory review window | Define delay/appeal window for `MG-6`. |
| `OI-009` | Immunity rollback tests | Define conformance tests for defensive updates. |
| `OI-010` | Repo placement | Decide final GitHub path and package index integration. |

---

## 35. Closing rule

The memory gate exists because `c` is not a pile of logs.

It is a continuity-bearing entity under constraints.

Final rule:

```text
A CLI agent may bring material to the door.
The memory gate decides what enters the house.
```

