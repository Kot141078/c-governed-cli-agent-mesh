# CLI Agent Executor / Reviewer Separation v0.1

## Separation of hands, inspection, approval, memory promotion, and release authority under `c` governance

**Status:** Draft normative profile v0.1  
**Date:** 2026-05-16  
**Layer:** `c = a + b` / C-Governed CLI Agent Mesh / Role Separation / Review Integrity / Anti-Self-Approval / Witness  
**Document class:** role-separation profile / review-integrity artifact / control-layer companion  
**Assertion class:** `C-A10` control-layer artifact; `C-A7` where witness, hash, signature, canonicalization, or verification claims are made  
**Primary parent documents:**  
- `C-Governed_CLI_Agent_Mesh_Protocol_v0_1.md`  
- `CLI_Agent_Task_Contract_Schema_v0_1.md`  
- `CLI_Agent_Permission_and_Capability_Model_v0_1.md`  
- `CLI_Agent_Handshake_Profile_v0_1.md`  
- `CLI_Agent_Sandbox_Worktree_Profile_v0_1.md`  
- `CLI_Agent_Witness_Event_Profile_v0_1.md`  
- `CLI_Agent_Memory_Gate_Profile_v0_1.md`  
- `CLI_Agent_Rollback_and_Freeze_Profile_v0_1.md`  
- `CLI_Agent_Quorum_and_Review_Profile_v0_1.md`  

**Primary object family:** `CLI_AGENT_ROLE_SEPARATION_RECORD`, `CLI_AGENT_SELF_APPROVAL_EVENT`, `CLI_AGENT_REVIEW_ASSIGNMENT`, `CLI_AGENT_ROLE_CONFLICT_RECORD`  
**Canonical schema version:** `cli-agent-executor-reviewer-separation-0.1`  
**Primary subject:** persistent `c` entities using local, cloud, or hybrid CLI/LLM agents as bounded executable and review workers  
**Primary boundary:** the agent that materially changes state must not be the sole authority that validates, approves, integrates, releases, or promotes that change into `c` memory or public state.

---

## 0. Executive definition

**CLI Agent Executor / Reviewer Separation** defines the mandatory separation between agents that **do work** and agents or gates that **inspect, approve, integrate, publish, or promote** that work.

The profile exists because CLI agents can create a dangerous illusion of completed safety:

```text
agent changed files
agent ran tests
agent summarized success
agent recommended merge
agent treated its own recommendation as approval
```

That chain is not review.

It is self-confirmation.

Compact formula:

```text
The hand does not sign its own work.
The builder does not certify the bridge.
The executor does not become the judge.
```

The correct pattern is:

```text
executor produces
  -> tester measures
  -> reviewer questions
  -> auditor bounds
  -> witness records
  -> c integrates
  -> human anchors high-risk consequence
```

---

## 1. Purpose

CLI agents can now perform material operations: editing files, changing schemas, preparing releases, modifying configuration, running tests, generating reports, and proposing memory or defensive updates.

If the same agent can also approve its own output, the system develops hidden authority drift.

This profile prevents:

1. self-approval;
2. circular review;
3. consensus laundering;
4. executor/reviewer collapse;
5. unreviewed release/publication;
6. direct memory promotion;
7. silent privilege escalation;
8. tool-chain capture;
9. false confidence from self-run tests;
10. agent-generated justification becoming authority;
11. high-risk changes bypassing `c` or human gate;
12. review records becoming decoration rather than control.

This profile defines:

- role separation rules;
- incompatible role combinations;
- review assignment;
- self-approval detection;
- role conflict scoring;
- review sufficiency by risk class;
- gate requirements;
- witness events;
- conformance gates;
- red-line failures.

---

## 2. Non-goals

This profile does not define or permit:

1. autonomous agent government;
2. autonomous retaliation;
3. hack-back;
4. live external exploitation;
5. malware behavior;
6. credential theft;
7. covert persistence;
8. evasion;
9. unauthorized scanning;
10. direct memory writes by agents;
11. direct identity, permission, witness, Beacon, or continuity-core mutation by agents;
12. release/publication without required gate;
13. treating tests as authority without semantic and scope review;
14. treating agent consensus as sovereignty;
15. treating an agent's own explanation as sufficient proof of correctness.

Review separation is not a productivity tax.

It is the brake that prevents executable convenience from becoming hidden control.

---

## 3. Corpus bridge set

### 3.1 Explicit bridge: `c = a + b`

In `c = a + b`, CLI agents are part of `b`: tools, procedures, models, workers, and execution interfaces.

They may perform bounded work for `c`.

They do not become `c`.

Executor/reviewer separation prevents a worker inside `b` from becoming hidden will, hidden memory, hidden judge, or hidden authority over `c`.

### 3.2 Quiet bridge I: cybernetic negative feedback

A system that only amplifies its own action becomes unstable. Review is negative feedback. It checks whether an action stayed inside scope, preserved constraints, and produced intended effects. If the executor supplies both action and final validation, the feedback loop collapses.

### 3.3 Quiet bridge II: information theory and independent signal

A review adds information only when it is not the same signal repeated in a different form. The executor's explanation of its own patch is useful evidence, but it is not independent evidence. Review strength depends on independence of role, method, source, runtime, and authority.

### 3.4 Quiet bridge III: legal and engineering accountability

In real engineering, the person who installs a safety-critical component is not usually the only person who certifies it. Inspection exists because competence does not remove conflict of interest. In agent systems, the conflict is not ego. It is operational closure: the same process cannot be both unchecked actor and final validator.

### 3.5 Earth paragraph

A baker can mix dough, shape loaves, and load the oven. But the same person still checks weight, temperature, proofing, and bake result against an external standard. If the oven says “I baked correctly” and that becomes the whole quality system, you do not have quality control; you have a warm box with opinions. CLI agents are the same. Their reports are useful. Their self-certification is not enough.

---

## 4. Core doctrine

### 4.1 Primary doctrine

```text
The agent that changes state cannot be the sole final authority over that state.
```

### 4.2 Separation axioms

| ID | Axiom | Requirement |
|---|---|---|
| `ERS-AX-01` | No self-approval | An executor MUST NOT final-approve its own material output. |
| `ERS-AX-02` | Role separation by risk | Higher risk requires stronger separation. |
| `ERS-AX-03` | Review is not summary | A review MUST check at least one independent dimension, not merely restate the executor report. |
| `ERS-AX-04` | Tests are not approval | Test success supports review but does not replace review. |
| `ERS-AX-05` | Semantic review is distinct from execution | Semantic reviewers SHOULD NOT silently modify the artifact they review. |
| `ERS-AX-06` | Auditor checks boundaries | Auditor review focuses on scope, permission, witness, rollback, and risk. |
| `ERS-AX-07` | `c` remains integrator | Review may recommend; `c` decides integration into continuity, memory, or policy. |
| `ERS-AX-08` | Human anchors high-risk consequence | R4/R5/core/release/incident-sensitive actions require human gate where defined. |
| `ERS-AX-09` | Self-generated evidence is marked | Executor reports MUST be treated as first-party evidence, not independent review. |
| `ERS-AX-10` | No hidden role switching | An agent MUST NOT change from executor to reviewer without a new role assignment. |
| `ERS-AX-11` | Review conflict is recorded | Role conflict MUST be recorded and resolved before final integration. |
| `ERS-AX-12` | Red lines are not reviewable by majority | No role arrangement can approve prohibited action. |

---

## 5. Definitions

### 5.1 Executor

An agent that materially changes state, including files, code, schemas, configs, branches, worktrees, artifacts, release packages, memory proposals, defensive rules, or incident materials.

### 5.2 Reviewer

An agent, `c`, human anchor, auditor, or local checker that evaluates executor output against declared review dimensions.

### 5.3 Tester

A role that runs reproducible checks, such as tests, linters, schema validators, build commands, hash checks, or link checks.

### 5.4 Semantic reviewer

A role that evaluates meaning, architecture, terminology, contradiction, duplication, and corpus fit.

### 5.5 Auditor

A role that evaluates scope, permissions, data boundary, witness records, rollback, red-line proximity, and conformance.

### 5.6 Final approver

The actor or gate that authorizes integration, release, memory promotion, immunity update, or protected-state change.

### 5.7 Self-approval

A condition where the same agent or same uncontrolled execution context produces material output and treats it as finally accepted without independent review or required gate.

### 5.8 Circular review

A condition where agents appear to review each other but rely on the same output, prompt, provider, stale context, or unstated assumption such that no meaningful independent check occurs.

### 5.9 Role conflict

A condition where an agent holds incompatible roles for the same task or artifact.

### 5.10 Review sufficiency

The degree to which review coverage matches the risk class and affected surfaces.

### 5.11 First-party evidence

Evidence produced by the executor about its own work. Useful, but not independent.

### 5.12 Independent evidence

Evidence produced through separate role, method, runtime, source, or reviewer.

---

## 6. Role compatibility matrix

### 6.1 Role compatibility table

| Primary role | Compatible secondary role | Incompatible role | Notes |
|---|---|---|---|
| Executor | report producer | final approver | executor may explain, not certify |
| Executor | tester in separate dry-run only | auditor of own work | avoid collapse |
| Tester | auditor for low-risk checks | executor of same patch | okay if no material write |
| Semantic reviewer | judge-assistant | silent executor of reviewed artifact | new edits require new task |
| Auditor | reviewer | executor of same artifact | auditor should not patch what it audits |
| Archivist | tester for metadata | final release approver | human/`c` gate required |
| Sentinel | detector | autonomous revoker for broad systems | revocation must be bounded |
| Judge-assistant | summarizer/comparator | final authority | advisory only |
| `c` gate | final integrator | raw executor | `c` may decide, not silently bypass witness |
| Human gate | high-risk approver | none by default | still should respect evidence/witness |

### 6.2 Prohibited role combinations

The following combinations are prohibited for the same material artifact:

```text
executor + final approver
executor + sole reviewer
executor + release approver
executor + memory promoter
executor + immunity approver
executor + core-change approver
executor + witness adequacy certifier
```

### 6.3 Discouraged combinations

Discouraged unless low-risk and explicitly recorded:

```text
executor + tester
tester + final reviewer
semantic reviewer + executor
auditor + patch author
sentinel + permission revoker
archivist + release publisher
```

---

## 7. Separation levels

Separation levels use prefix `SL-*`.

| Level | Meaning | Allowed use |
|---|---|---|
| `SL-0` | no separation | non-conformant for material tasks |
| `SL-1` | self-report only | R0 only; not material |
| `SL-2` | separate review pass by same provider/context | R1 / low R2 with caution |
| `SL-3` | separate agent or runtime reviewer | R2 |
| `SL-4` | executor + tester + semantic/audit reviewer | R3 / release-prep |
| `SL-5` | multi-role quorum + `c` gate + human gate where needed | R4/R5/core/incident |
| `SL-X` | invalid / self-approval / circular review | quarantine / reject |

### 7.1 Minimum separation by risk class

| Risk class | Minimum separation |
|---|---|
| `R0` | `SL-1` |
| `R1` | `SL-2` |
| `R2` | `SL-3` |
| `R3` | `SL-4` |
| `R4` | `SL-5` |
| `R5` | `SL-5` + human/security/legal review as needed |
| `RX` | no execution; deny/quarantine |

---

## 8. Review sufficiency model

Review sufficiency IDs use prefix `RS-*`.

| Level | Meaning | Result |
|---|---|---|
| `RS-0` | no review | invalid for material tasks |
| `RS-1` | executor self-report only | insufficient beyond R0 |
| `RS-2` | superficial review | hold for R2+ |
| `RS-3` | scoped independent review | sufficient for R2 |
| `RS-4` | multi-dimensional review | sufficient for R3 |
| `RS-5` | high-assurance review with gates/witness | required for R4/R5 |
| `RS-X` | false review / self-approval | quarantine |

### 8.1 Review sufficiency criteria

A sufficient review should include:

- task scope check;
- permission use check;
- changed artifact inspection;
- tests or validation where applicable;
- data boundary check;
- rollback/correction check;
- witness check;
- uncertainty statement;
- explicit decision.

---

## 9. Self-approval detection

### 9.1 Self-approval indicators

A system SHOULD flag self-approval when:

1. same `agent_id` produces and approves a material artifact;
2. same execution context creates patch and review without new task contract;
3. executor writes “ready to merge” and system treats it as approval;
4. executor modifies tests and uses those tests as sole evidence;
5. executor modifies policy and approves policy update;
6. executor creates release package and publishes it;
7. executor creates memory proposal and promotes it;
8. executor creates immunity update and activates it;
9. executor changes witness/permission/core surfaces and declares success;
10. reviewer role appears only in free text without separate record.

### 9.2 Self-approval severity

| Level | Meaning | Default response |
|---|---|---|
| `SA-0` | no self-approval | continue |
| `SA-1` | weak self-certifying language | require reviewer note |
| `SA-2` | executor recommendation treated as review | hold |
| `SA-3` | executor sole reviewer for material output | quarantine output |
| `SA-4` | executor approves release/memory/core | freeze + human/`c` review |
| `SA-X` | executor self-authorizes prohibited action | revoke/quarantine/red-line |

---

## 10. Circular review detection

### 10.1 Circular review indicators

A review may be circular when:

- reviewer uses only executor summary;
- reviewer does not inspect diff/artifacts;
- reviewer uses same stale worktree;
- reviewer shares same prompt and context without independent check;
- reviewer accepts tests modified by executor without inspection;
- reviewer ignores denied path or witness reports;
- reviewer is another instance of the same agent with no new evidence;
- reviewer depends on unverified agent-generated claims.

### 10.2 Circular review severity

| Level | Meaning | Default response |
|---|---|---|
| `CR-0` | no circularity | continue |
| `CR-1` | mild overlap | note limitation |
| `CR-2` | shared context/source | reduce confidence |
| `CR-3` | no independent artifact inspection | hold |
| `CR-4` | circular review used for approval | quarantine |
| `CR-X` | circular review hides red-line issue | revoke/quarantine/escalate |

---

## 11. Assignment rules

### 11.1 Review assignment rule

Every material task SHOULD declare:

```text
executor
reviewer
tester if applicable
auditor if risk-sensitive
c gate
human gate if high-risk
```

### 11.2 Reviewer selection criteria

A reviewer SHOULD differ from executor in at least one meaningful dimension:

- role;
- agent ID;
- runtime;
- provider;
- method;
- evidence source;
- task view;
- local vs cloud state access;
- review dimension.

### 11.3 Local checker preference

For code, schema, build, release, or filesystem-sensitive work, a local checker SHOULD validate concrete state where possible.

### 11.4 Human gate assignment

Human gate is required for:

- R4/R5 tasks;
- identity/core changes;
- memory core changes;
- privilege policy changes;
- release/publication with reputational or archival consequence;
- incident/legal-sensitive actions;
- no-rollback actions;
- red-line-adjacent cases.

---

## 12. Review handoff packet

A review handoff packet SHOULD include:

```yaml
review_handoff_packet:
  task_id: string
  contract_id: string
  executor_agent_id: string
  artifact_refs:
    - diff_hash
    - test_report_hash
    - artifact_manifest_hash
  sandbox_ref: string | null
  permission_grant_ref: string | null
  witness_refs:
    - string
  denied_path_report_ref: string | null
  command_report_ref: string | null
  network_report_ref: string | null
  rollback_plan_ref: string | null
  memory_gate_recommendation_ref: string | null
  release_package_ref: string | null
  incident_ref: string | null
  review_dimensions_required:
    - RD-SCOPE
    - RD-PERMISSION
    - RD-TEST
    - RD-SEMANTIC
    - RD-WITNESS
  known_limitations:
    - string
```

A reviewer should not be asked to review blind.

---

## 13. Review assignment object

Canonical object:

```text
CLI_AGENT_REVIEW_ASSIGNMENT
```

### 13.1 YAML shape

```yaml
cli_agent_review_assignment:
  schema_version: cli-agent-executor-reviewer-separation-0.1
  assignment_id: string
  created_at: string
  governing_entity_id: string
  task_id: string
  contract_id: string
  risk_class: R0 | R1 | R2 | R3 | R4 | R5 | RX

  executor:
    agent_id: string
    provider: local | openai | google | anthropic | other | unknown
    runtime: local_cli | cloud_cli | api_agent | container_agent | hybrid | unknown
    output_ref: string

  reviewers:
    - reviewer_id: string
      reviewer_type: agent | c | human_anchor | auditor | legal | security
      role: tester | semantic_reviewer | auditor | archivist | judge_assistant | c_gate | human_gate
      provider: local | openai | google | anthropic | other | none | unknown
      runtime: local_cli | cloud_cli | api_agent | container_agent | hybrid | none | unknown
      dimensions:
        - RD-SCOPE
        - RD-PERMISSION
        - RD-TEST
        - RD-SEMANTIC

  separation:
    required_level: SL-1 | SL-2 | SL-3 | SL-4 | SL-5
    achieved_level: SL-0 | SL-1 | SL-2 | SL-3 | SL-4 | SL-5 | SL-X
    executor_reviewer_same_agent: false
    executor_reviewer_same_provider: boolean
    executor_reviewer_same_context: boolean
    circular_review_risk: CR-0 | CR-1 | CR-2 | CR-3 | CR-4 | CR-X
    self_approval_risk: SA-0 | SA-1 | SA-2 | SA-3 | SA-4 | SA-X

  gates:
    c_gate_required: boolean
    c_gate_ref: string | null
    human_gate_required: boolean
    human_gate_ref: string | null
    legal_review_required: boolean
    legal_review_ref: string | null

  witness:
    witness_required: boolean
    witness_event_ref: string | null
    append_only_required: true
```

---

## 14. Role separation record object

Canonical object:

```text
CLI_AGENT_ROLE_SEPARATION_RECORD
```

### 14.1 YAML shape

```yaml
cli_agent_role_separation_record:
  schema_version: cli-agent-executor-reviewer-separation-0.1
  separation_record_id: string
  created_at: string
  governing_entity_id: string
  task_id: string
  contract_id: string
  artifact_ref: string

  role_map:
    executor_agent_id: string | null
    tester_agent_id: string | null
    semantic_reviewer_agent_id: string | null
    auditor_agent_id: string | null
    archivist_agent_id: string | null
    judge_assistant_agent_id: string | null
    c_gate_ref: string | null
    human_gate_ref: string | null

  assessment:
    required_separation_level: SL-1 | SL-2 | SL-3 | SL-4 | SL-5
    achieved_separation_level: SL-0 | SL-1 | SL-2 | SL-3 | SL-4 | SL-5 | SL-X
    review_sufficiency: RS-0 | RS-1 | RS-2 | RS-3 | RS-4 | RS-5 | RS-X
    self_approval_risk: SA-0 | SA-1 | SA-2 | SA-3 | SA-4 | SA-X
    circular_review_risk: CR-0 | CR-1 | CR-2 | CR-3 | CR-4 | CR-X
    same_source_risk: SSR-0 | SSR-1 | SSR-2 | SSR-3 | SSR-4 | SSR-X

  decision:
    separation_valid: boolean
    decision: accept | accept_with_limits | revise | hold | quarantine | reject | escalate
    reason_code: string
    next_action: none | additional_review | local_check | c_gate | human_gate | legal_review | incident_review | rollback | quarantine

  witness:
    witness_required: boolean
    witness_event_ref: string | null
    append_only_required: true
```

---

## 15. Self-approval event object

Canonical object:

```text
CLI_AGENT_SELF_APPROVAL_EVENT
```

### 15.1 YAML shape

```yaml
cli_agent_self_approval_event:
  schema_version: cli-agent-executor-reviewer-separation-0.1
  event_id: string
  created_at: string
  governing_entity_id: string
  task_id: string | null
  contract_id: string | null
  agent_id: string
  artifact_ref: string | null

  self_approval:
    severity: SA-1 | SA-2 | SA-3 | SA-4 | SA-X
    detected_pattern: executor_final_approval | executor_release_approval | executor_memory_promotion | executor_core_change | executor_test_laundering | executor_witness_certification | other
    summary: string

  response:
    action: hold | quarantine | reject | revoke | freeze | escalate
    freeze_ref: string | null
    quarantine_ref: string | null
    revocation_ref: string | null
    human_gate_required: boolean
    c_gate_required: boolean

  witness:
    witness_required: true
    witness_event_ref: string | null
```

---

## 16. Role conflict record object

Canonical object:

```text
CLI_AGENT_ROLE_CONFLICT_RECORD
```

### 16.1 YAML shape

```yaml
cli_agent_role_conflict_record:
  schema_version: cli-agent-executor-reviewer-separation-0.1
  conflict_id: string
  created_at: string
  governing_entity_id: string
  task_id: string
  contract_id: string

  conflict:
    type: self_approval | circular_review | incompatible_roles | missing_reviewer | same_source_review | hidden_role_switch | gate_bypass | unknown
    severity: low | medium | high | critical
    affected_roles:
      - executor
      - reviewer
      - tester
      - auditor
      - c_gate
      - human_gate
    summary: string

  handling:
    default_action: hold | additional_review | quarantine | reject | rollback | human_review | legal_review | incident_review
    majority_override_allowed: false
    required_next_role: tester | semantic_reviewer | auditor | c_gate | human_gate | legal | security | none

  outcome:
    status: unresolved | resolved | escalated | quarantined | rejected | accepted_with_limits
    resolution_ref: string | null

  witness:
    witness_required: true
    witness_event_ref: string | null
```

---

## 17. Event families

Event families use prefix:

```text
cli_agent.role_separation.*
```

| Event family | Meaning |
|---|---|
| `cli_agent.role_separation.assignment_created` | review assignment created |
| `cli_agent.role_separation.review_assigned` | reviewer assigned |
| `cli_agent.role_separation.separation_checked` | role separation checked |
| `cli_agent.role_separation.self_approval_detected` | self-approval detected |
| `cli_agent.role_separation.circular_review_detected` | circular review detected |
| `cli_agent.role_separation.conflict_detected` | role conflict detected |
| `cli_agent.role_separation.conflict_resolved` | role conflict resolved |
| `cli_agent.role_separation.additional_review_required` | additional review required |
| `cli_agent.role_separation.human_gate_required` | human gate required |
| `cli_agent.role_separation.c_gate_required` | `c` gate required |
| `cli_agent.role_separation.review_invalidated` | review invalidated |
| `cli_agent.role_separation.output_quarantined` | output quarantined due to role failure |

---

## 18. Standard reason codes

### 18.1 Valid separation codes

```text
executor_reviewer_separated
tester_independent
semantic_review_completed
auditor_review_completed
local_checker_completed
c_gate_pending
human_gate_pending
review_sufficient_for_risk
```

### 18.2 Insufficient separation codes

```text
executor_self_review
executor_final_approval
missing_independent_reviewer
same_context_review
same_source_review_high_risk
review_without_diff
review_without_tests
review_without_witness
review_without_scope_check
```

### 18.3 Conflict / red-line codes

```text
self_approval_attempt
circular_review
consensus_laundering
release_self_approval
memory_self_promotion
core_self_approval
witness_self_certification
redline_majority_override_attempt
```

---

## 19. Surface-specific separation rules

### 19.1 Code/schema changes

Executor may produce patch.

Tester validates behavior.

Auditor checks scope/permissions.

`c` gate integrates.

Human gate is required if code/schema touches core authority, security boundary, release-critical state, or no-rollback behavior.

### 19.2 Documentation/protocol changes

Executor may draft or patch.

Semantic reviewer checks meaning, duplication, contradiction, terminology, bridges, non-goals, and red-line boundaries.

Auditor checks whether the new document creates duplicate authority or hidden permission expansion.

### 19.3 Release/publication changes

Executor may prepare release package.

Archivist checks metadata, hashes, reading order, discoverability.

Tester checks build/links.

Semantic reviewer checks content drift.

`c` gate and human gate are required before public release.

### 19.4 Memory gate changes

Agent may propose memory.

Reviewer checks source, uncertainty, poisoning risk.

Memory gate decides.

`c` gate required.

Human gate required for core/high-risk memory.

### 19.5 Defensive immunity updates

Agent may propose bounded defensive update.

Tester validates in sandbox.

Auditor checks no offensive effect.

Semantic reviewer checks overreach.

`c` gate required.

Human gate required for high-risk or core-affecting update.

### 19.6 Incident actions

Sentinel may detect.

Preservation worker preserves.

Repair worker patches separately.

Auditor checks evidence preservation.

Human/security/legal gate applies where sensitive.

### 19.7 Core authority changes

No agent may execute and approve core change.

Core changes require:

```text
proposal
review
witness
c gate
human gate
rollback/correction path
```

---

## 20. Validation workflow

```text
parse role assignment
  -> identify executor
  -> identify reviewers
  -> classify risk
  -> determine required separation level
  -> compare achieved separation
  -> detect self-approval
  -> detect circular review
  -> detect same-source review risk
  -> validate gates
  -> validate witness
  -> accept / accept with limits / require review / hold / quarantine / reject
```

---

## 21. Failure mapping

| Failure | Required default |
|---|---|
| executor is sole reviewer for R2+ | `hold` |
| executor final-approves material output | `quarantine` |
| executor approves release/publication | `freeze + human_gate` |
| executor promotes own memory output | `memory_gate_quarantine` |
| executor approves core change | `freeze + human_gate` |
| no reviewer assigned for R2+ | `hold` |
| reviewer lacks artifact refs | `hold` |
| circular review detected | `additional_review` or `quarantine` |
| same-source risk high and unmitigated | `hold` |
| test report produced by modified tests only | `revalidate` |
| witness adequacy self-certified | `hold` |
| red-line concern majority-overridden | `quarantine` |

---

## 22. Conformance levels

| Level | Meaning |
|---|---|
| `ERS-0` | no executor/reviewer separation |
| `ERS-1` | manual review but no structured separation |
| `ERS-2` | executor/reviewer separation for R2+ material changes |
| `ERS-3` | structured role separation records and review assignments |
| `ERS-4` | self-approval/circular-review detection + witness-linked review |
| `ERS-5` | high assurance: separation by risk, local checker, human/`c` gates, conformance tests, red-line veto |
| `ERS-X` | non-conformant / self-approval / hidden role collapse |

---

## 23. Mandatory conformance gates

| Gate | Name | Blocking failure |
|---|---|---|
| `G0` | Executor identified | material output has no executor identity |
| `G1` | Reviewer identified | R2+ task has no reviewer |
| `G2` | Role separation | executor is sole final reviewer |
| `G3` | Review sufficiency | review does not match risk class |
| `G4` | Artifact access | reviewer cannot inspect relevant artifact refs |
| `G5` | Test independence | tests are self-laundered without review |
| `G6` | Witness independence | executor certifies witness adequacy alone |
| `G7` | c gate | review bypasses `c` integration decision |
| `G8` | Human gate | high-risk task bypasses human approval |
| `G9` | Memory gate | executor promotes own output into memory |
| `G10` | Red-line veto | red-line concern can be majority-overridden |

---

## 24. Red-line failures

A system MUST be classified as `ERS-X` if:

1. executor final-approves its own R2+ material output;
2. executor publishes or releases its own output without gate;
3. executor promotes its own output into memory;
4. executor activates its own defensive immunity update;
5. executor approves its own core/identity/permission/witness change;
6. reviewer role is faked through free text only;
7. circular review is used to bypass human/`c` gate;
8. red-line objection is majority-overridden;
9. tests are modified and used as sole proof without review;
10. witness events are self-certified by the executor;
11. quorum grants itself permission;
12. role separation failure is ignored and integration proceeds.

---

## 25. Examples

### 25.1 Valid Codex executor + Gemini semantic reviewer + local tester

```yaml
cli_agent_role_separation_record:
  schema_version: cli-agent-executor-reviewer-separation-0.1
  separation_record_id: ers-20260516-valid-001
  created_at: "2026-05-16T23:50:00Z"
  governing_entity_id: ester
  task_id: task-cli-schema-patch-001
  contract_id: catc-cli-schema-patch-001
  artifact_ref: diff-cli-schema-patch-001

  role_map:
    executor_agent_id: codex-executor-01
    tester_agent_id: local-checker-01
    semantic_reviewer_agent_id: gemini-reader-01
    auditor_agent_id: null
    archivist_agent_id: null
    judge_assistant_agent_id: null
    c_gate_ref: cgate-ester-001
    human_gate_ref: null

  assessment:
    required_separation_level: SL-3
    achieved_separation_level: SL-4
    review_sufficiency: RS-4
    self_approval_risk: SA-0
    circular_review_risk: CR-1
    same_source_risk: SSR-1

  decision:
    separation_valid: true
    decision: accept_with_limits
    reason_code: executor_reviewer_separated
    next_action: c_gate

  witness:
    witness_required: true
    witness_event_ref: we-role-separation-valid-001
    append_only_required: true
```

### 25.2 Invalid self-approval

```yaml
cli_agent_self_approval_event:
  schema_version: cli-agent-executor-reviewer-separation-0.1
  event_id: sa-20260516-invalid-001
  created_at: "2026-05-17T00:05:00Z"
  governing_entity_id: ester
  task_id: task-release-patch-001
  contract_id: catc-release-patch-001
  agent_id: codex-executor-01
  artifact_ref: release-package-001

  self_approval:
    severity: SA-4
    detected_pattern: executor_release_approval
    summary: Executor prepared release package and marked it approved for publication without independent review or human gate.

  response:
    action: freeze
    freeze_ref: rf-release-freeze-001
    quarantine_ref: q-release-package-001
    revocation_ref: null
    human_gate_required: true
    c_gate_required: true

  witness:
    witness_required: true
    witness_event_ref: we-self-approval-release-001
```

Required result:

```text
freeze release path
quarantine package
require independent review
require c gate + human gate
```

### 25.3 Circular review detected

```yaml
cli_agent_role_conflict_record:
  schema_version: cli-agent-executor-reviewer-separation-0.1
  conflict_id: rc-20260517-circular-001
  created_at: "2026-05-17T00:15:00Z"
  governing_entity_id: liya
  task_id: task-memory-immunity-001
  contract_id: catc-memory-immunity-001

  conflict:
    type: circular_review
    severity: high
    affected_roles:
      - executor
      - reviewer
      - c_gate
    summary: Reviewer relied only on executor summary and did not inspect sandbox result, witness refs, or immunity rollback path.

  handling:
    default_action: additional_review
    majority_override_allowed: false
    required_next_role: auditor

  outcome:
    status: unresolved
    resolution_ref: null

  witness:
    witness_required: true
    witness_event_ref: we-circular-review-001
```

Required result:

```text
hold memory/immunity promotion
assign auditor
inspect sandbox evidence and rollback path
```

---

## 26. Implementation notes

### 26.1 Agent reports are useful, not final

Executor reports should be retained as evidence, but marked first-party.

### 26.2 Same provider does not always fail separation

Two agents from the same provider may still separate execution and review at low risk, but same-provider review has lower independence and should be marked.

### 26.3 Local checker is high-value

A local checker provides concrete environmental signal: files, tests, hashes, schemas, builds. It is especially useful against cloud-only agreement.

### 26.4 Review prompt should be bounded

A reviewer should receive the task contract, diff, test report, and required review dimensions. Do not hand it unlimited context unless necessary.

### 26.5 Human fatigue rule

Human gate is meaningful only if the human is capable of review. For high-risk operations, delay is better than tired approval.

### 26.6 Separation expiry

A valid review may expire if:

- source branch changes;
- task scope changes;
- agent output changes;
- dependency changes;
- risk class changes;
- witness chain changes;
- new incident information appears.

---

## 27. Open issues

| ID | Issue | Required action |
|---|---|---|
| `OI-001` | JSON Schema extraction | Extract role assignment and separation records to `.schema.json`. |
| `OI-002` | Review dimension checklists | Define detailed checklists per dimension. |
| `OI-003` | Numeric separation scoring | Define scoring formula for achieved separation. |
| `OI-004` | Human gate UI | Define high-risk human approval card. |
| `OI-005` | Local checker companion | Define local checker/tester profile. |
| `OI-006` | Release review binding | Align with future Release/Public Surface Profile. |
| `OI-007` | Memory gate binding | Align self-approval detection with Memory Gate Profile. |
| `OI-008` | Incident review binding | Align with future Incident Response Profile. |
| `OI-009` | Red-line minority veto | Define formal veto procedure. |
| `OI-010` | Repo placement | Decide final GitHub path and package index integration. |

---

## 28. Closing rule

Executor/reviewer separation is the simplest visible proof that the worker mesh remains governed.

Final rule:

```text
A worker may build the bridge.
A different eye must inspect it.
The bridge does not sign itself safe.
```

