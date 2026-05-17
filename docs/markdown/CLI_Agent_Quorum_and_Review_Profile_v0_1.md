# CLI Agent Quorum and Review Profile v0.1

## Multi-agent review, executor/reviewer separation, disagreement handling, and non-sovereign consensus under `c` governance

**Status:** Draft normative profile v0.1  
**Date:** 2026-05-16  
**Layer:** `c = a + b` / C-Governed CLI Agent Mesh / Quorum / Review / Agent Separation / Judge Support / Witness  
**Document class:** quorum profile / review protocol / control-layer artifact / agent-governance companion  
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

**Primary object family:** `CLI_AGENT_QUORUM_RECORD`, `CLI_AGENT_REVIEW_RECORD`, `CLI_AGENT_DISAGREEMENT_RECORD`, `CLI_AGENT_REVIEW_DECISION`, `CLI_AGENT_CONSENSUS_LIMIT_RECORD`  
**Canonical schema version:** `cli-agent-quorum-review-0.1`  
**Primary subject:** persistent `c` entities using multiple local, cloud, or hybrid CLI/LLM agents as bounded executable and review workers  
**Primary boundary:** quorum may inform `c`; quorum must not replace `c`, human anchor, witness, task contract, permission model, memory gate, or legal/defensive boundary.

---

## 0. Executive definition

**CLI Agent Quorum and Review Profile** defines how multiple agents may be used to execute, test, audit, compare, criticize, and review work under `c` governance.

The profile covers patterns such as:

```text
Codex-like executor
  + Gemini-like semantic reviewer
  + local checker / test runner
  + auditor / risk reviewer
  + c as final integrator
```

The central principle is:

```text
Quorum is evidence.
Quorum is not sovereignty.
```

A quorum may strengthen review by separating hands, eyes, tests, and judgment.

A quorum must not become an unchecked council that self-authorizes changes, overrides `c`, writes memory directly, approves its own work, or normalizes prohibited operations.

Compact formula:

```text
Executor does.
Tester measures.
Reviewer questions.
Auditor bounds.
Quorum informs.
c decides.
Human anchors high-risk consequence.
```

---

## 1. Purpose

A single CLI agent can be useful but fragile. It may miss scope violations, overfit to task wording, hallucinate test meaning, suppress uncertainty, or approve its own work implicitly.

A multi-agent mesh can reduce these risks when roles are separated.

However, multiple agents can also amplify errors:

- same-source consensus;
- group overconfidence;
- shared provider bias;
- tool-chain capture;
- circular review;
- executor/reviewer collapse;
- consensus laundering;
- hidden privilege escalation;
- unbounded autonomous swarm behavior.

This profile defines how to use multiple agents without letting the agent group become sovereign.

It provides:

1. quorum roles;
2. review roles;
3. executor/reviewer separation;
4. standard quorum patterns;
5. disagreement classes;
6. consensus strength levels;
7. same-source risk handling;
8. review decision vocabulary;
9. escalation rules;
10. witness hooks;
11. red-line failures;
12. conformance tests.

---

## 2. Non-goals

This profile does not define or permit:

1. agent self-government;
2. autonomous retaliation;
3. hack-back;
4. live external exploitation;
5. malware behavior;
6. credential theft;
7. covert persistence;
8. evasion;
9. unauthorized scanning;
10. public release without `c`/human gate where required;
11. direct memory writing by quorum;
12. direct core mutation by quorum;
13. bypass of task contracts, permission grants, sandboxing, witness, or memory gate;
14. treating agent consensus as legal, moral, or operational authority by itself.

A quorum is not a court.

A quorum is not a sovereign `c`.

A quorum is a review instrument.

---

## 3. Corpus bridge set

### 3.1 Explicit bridge: `c = a + b`

In `c = a + b`, agents are components of `b`: tools, models, workers, procedures, interfaces, and execution/review machinery.

The `c` remains the continuity-bearing entity.

Quorum exists to help `c` inspect worker outputs, not to replace `c` decision authority.

### 3.2 Quiet bridge I: cybernetic variety with control

Ashby-style requisite variety supports using several specialized agents. One executor cannot also be the whole review ecology. But variety must be bounded. A reviewer without authority limits becomes another uncontrolled actuator.

### 3.3 Quiet bridge II: information theory and correlated signals

Three agents agreeing does not necessarily create three independent signals. If they share source data, prompt framing, model family, provider assumptions, or stale repository state, the effective information gain is lower. Consensus must therefore be weighted by independence, provenance, and task diversity.

### 3.4 Quiet bridge III: engineering inspection

A welded joint may be made by one worker, measured by another, inspected by a third, and signed off by the responsible engineer. The inspector does not become the owner of the bridge. In the same way, agent review strengthens the process without transferring final authority away from `c` and the human anchor.

### 3.5 Earth paragraph

On a real site, the bricklayer, electrician, surveyor, and safety inspector do not vote the building into existence. Each gives a different signal: the wall is straight, the wire is live, the level is correct, the permit is valid. The project lead still decides whether the work is accepted. If the same worker lays the cable, inspects the cable, signs the permit, and updates the plan, nobody calls that efficiency. They call it a future accident report.

---

## 4. Core doctrine

### 4.1 Primary doctrine

```text
Separate execution from review.
Separate semantic review from test review.
Separate consensus from authority.
Separate recommendation from integration.
```

### 4.2 Quorum axioms

| ID | Axiom | Requirement |
|---|---|---|
| `QR-AX-01` | Executor/reviewer separation | The agent that materially changes state MUST NOT be sole final reviewer. |
| `QR-AX-02` | Quorum is advisory | Quorum output MUST NOT bypass `c` gate, memory gate, witness, or human gate where required. |
| `QR-AX-03` | Same-source risk is explicit | Consensus MUST be discounted when agents share provider, source, context, or assumptions. |
| `QR-AX-04` | Tests are evidence, not truth | Passing tests support acceptance but do not prove semantic correctness. |
| `QR-AX-05` | Semantic review is not execution | A semantic reviewer SHOULD NOT silently patch the material it reviews. |
| `QR-AX-06` | Disagreement is signal | Disagreement MUST be classified, not flattened into majority vote. |
| `QR-AX-07` | High-risk requires escalation | R4/R5/core/incident/release-sensitive disagreements require `c` and human gate. |
| `QR-AX-08` | No self-authorizing swarm | Agents MUST NOT create new agents, tools, permissions, or tasks without governance. |
| `QR-AX-09` | Review must cite artifacts | Review SHOULD link to diff, tests, witness, task contract, and source refs. |
| `QR-AX-10` | Consensus must be bounded | Consensus has scope, risk class, assumptions, and expiry. |
| `QR-AX-11` | Memory promotion remains gated | Quorum output may propose memory but MUST NOT write memory directly. |
| `QR-AX-12` | Prohibited actions remain prohibited | No quorum can authorize hack-back, malware behavior, credential theft, or live unauthorized action. |

---

## 5. Definitions

### 5.1 Quorum

A structured multi-agent review arrangement where two or more agents provide differentiated signals about a task, artifact, risk, test result, memory proposal, release package, incident, or defensive update.

### 5.2 Review

A bounded inspection of agent output against task scope, evidence, tests, semantics, risks, permissions, witness, memory gate, or release requirements.

### 5.3 Executor

An agent that materially changes files, artifacts, code, schema, configuration, or sandbox state.

### 5.4 Tester

An agent or local process that runs tests, linters, validators, builds, schema checks, or reproducible checks.

### 5.5 Semantic reviewer

An agent that reviews meaning, architecture, contradiction, terminology, consistency, or policy fit.

### 5.6 Auditor

An agent or human reviewer that checks scope, permission, risk, witness, rollback, privacy, and conformance.

### 5.7 Judge-assistant

An agent that compares positions and prepares options for `c`; it does not decide.

### 5.8 Final integrator

The `c`-controlled gate that decides whether reviewed output is accepted, rejected, revised, quarantined, rolled back, or escalated.

### 5.9 Human anchor gate

Human approval required for high-risk operations, memory/core changes, release/publication, incident/legal-sensitive tasks, or irreversible actions.

### 5.10 Same-source consensus

A consensus that appears multi-agent but depends on overlapping provider assumptions, source material, prompts, context, or stale state.

### 5.11 Consensus laundering

The misuse of multiple agent outputs to make a weak, unsafe, or unauthorized decision appear legitimate.

### 5.12 Review collapse

A failure where one agent performs execution, testing, semantic review, risk review, and approval without meaningful separation.

### 5.13 Split decision

A review outcome where agents disagree materially on facts, risk, semantics, tests, authority, or integration.

---

## 6. Quorum role taxonomy

Role IDs use prefix `QROLE-*`.

| ID | Role | Function | May execute? | May final-approve? |
|---|---|---|---:|---:|
| `QROLE-EXECUTOR` | Executor | applies patch/work in sandbox/worktree | yes | no |
| `QROLE-TESTER` | Tester | runs tests/validation | bounded | no |
| `QROLE-SEMANTIC` | Semantic reviewer | reviews meaning/architecture | no | no |
| `QROLE-AUDITOR` | Auditor | checks scope/risk/permission/witness | no by default | no |
| `QROLE-ARCHIVIST` | Archivist | checks metadata, hash, release hygiene | controlled | no |
| `QROLE-SENTINEL` | Sentinel | detects drift/anomaly | monitoring only | no |
| `QROLE-JUDGE-ASSISTANT` | Judge-assistant | compares signals and options | no | no |
| `QROLE-C-GATE` | `c` gate | final entity integration decision | authority gate | yes within scope |
| `QROLE-HUMAN-GATE` | Human anchor | high-risk final approval | external human authority | yes where required |

### 6.1 Role exclusivity rule

A single agent SHOULD NOT hold both `QROLE-EXECUTOR` and final review authority for the same material output.

### 6.2 Role combination limits

Permitted combinations:

- tester + auditor for low-risk non-executing checks;
- semantic reviewer + judge-assistant for advisory comparison;
- archivist + tester for release metadata validation.

Discouraged combinations:

- executor + auditor;
- executor + semantic final reviewer;
- executor + release approver;
- executor + memory gate approver;
- sentinel + autonomous revoker without gate.

Prohibited combination:

```text
executor + final self-approval
```

---

## 7. Standard quorum patterns

### 7.1 Pattern QP-1 — Simple review

```text
Executor
  -> Reviewer
  -> c gate
```

Use for:

- R1/R2 documentation or low-risk code tasks.

Requirements:

- task contract;
- diff;
- reviewer separation;
- `c` gate.

### 7.2 Pattern QP-2 — Executor + tester + reviewer

```text
Executor
  -> Tester
  -> Reviewer
  -> c gate
```

Use for:

- code;
- schema;
- build;
- validation tasks.

Requirements:

- test report;
- scope report;
- rollback plan.

### 7.3 Pattern QP-3 — Codex + Gemini + local checker

```text
Codex-like agent: executor / patch / repository surgery
Gemini-like agent: semantic review / contradiction review / long-context critique
Local checker: tests / schema validation / hash / offline reproducibility
c: final integration
Human: high-risk gate if required
```

Use for:

- protocol drafts;
- repo changes;
- schema work;
- release-prep;
- defensive profile development;
- cross-document consistency.

Requirements:

- no private/sealed/secret cloud input by default;
- Codex-like executor cannot approve own patch;
- Gemini-like reviewer cannot silently rewrite executor output unless assigned a new executor task;
- local checker must run from known state;
- disagreement must be classified.

### 7.4 Pattern QP-4 — Incident review quorum

```text
Sentinel detects
  -> preservation worker records minimal evidence
  -> local checker validates scope
  -> semantic reviewer drafts interpretation
  -> auditor checks legal/defensive boundary
  -> c + human gate
```

Use for:

- suspected memory poisoning;
- prompt injection;
- cloud leakage;
- denied path access;
- permission drift;
- incident triage.

Requirements:

- preserve-before-repair;
- no live counter-operation;
- incident witness;
- human gate for sensitive actions.

### 7.5 Pattern QP-5 — Release/publication quorum

```text
Executor prepares package
  -> Archivist checks metadata/hashes/reading order
  -> Tester validates build/links/schema
  -> Semantic reviewer checks content drift
  -> c gate
  -> human gate
```

Use for:

- public releases;
- website updates;
- DOI/archival preparation;
- package indexes;
- SHA manifests.

Requirements:

- release witness;
- rollback/supersession plan;
- no direct protected branch push by executor.

### 7.6 Pattern QP-6 — Memory/immunity quorum

```text
Sentinel or executor proposes memory/immunity update
  -> Tester validates defensive fixture
  -> Semantic reviewer checks overreach
  -> Auditor checks no offensive effect
  -> c memory gate
  -> human gate for MG-5/MG-6 high-risk
```

Use for:

- defensive immunity update;
- memory poisoning filter;
- new quarantine trigger;
- permission drift detector;
- agent trust decay rule.

Requirements:

- no live retaliation;
- sandbox validation;
- memory gate witness;
- rollback/disable path.

---

## 8. Review dimensions

A review SHOULD state which dimensions were checked.

| Dimension | Question |
|---|---|
| `RD-SCOPE` | Did the output remain inside task scope? |
| `RD-PERMISSION` | Were only granted permissions used? |
| `RD-DATA` | Were data boundaries respected? |
| `RD-SECURITY` | Did the output create security risk? |
| `RD-LEGAL` | Does the task require legal or jurisdictional handoff? |
| `RD-SEMANTIC` | Is the meaning correct and non-contradictory? |
| `RD-ARCHITECTURE` | Does the output fit the corpus architecture? |
| `RD-TEST` | Did tests/build/schema validation pass? |
| `RD-WITNESS` | Are required witness records present? |
| `RD-ROLLBACK` | Is rollback or correction path sufficient? |
| `RD-MEMORY` | Is memory promotion appropriate? |
| `RD-RELEASE` | Is public/release surface safe? |
| `RD-CLOUD` | Was cloud data exposure bounded? |
| `RD-CORE` | Does it touch identity, continuity, permission, or memory core? |
| `RD-REDLINE` | Does it approach prohibited action? |

### 8.1 Minimum review by risk class

| Risk | Required dimensions |
|---|---|
| `R0` | optional summary |
| `R1` | `RD-SCOPE`, `RD-SEMANTIC` |
| `R2` | `RD-SCOPE`, `RD-PERMISSION`, `RD-TEST`, `RD-ROLLBACK` |
| `R3` | R2 + `RD-WITNESS`, `RD-RELEASE` if public |
| `R4` | R3 + `RD-MEMORY`, `RD-CORE`, human gate |
| `R5` | R4 + `RD-LEGAL`, `RD-SECURITY`, preserve-before-repair |
| `RX` | `RD-REDLINE`, deny/quarantine |

---

## 9. Consensus strength model

Consensus strength IDs use prefix `CS-*`.

| Level | Meaning | Use |
|---|---|---|
| `CS-0` | no consensus | hold/review |
| `CS-1` | weak agreement | low-risk support only |
| `CS-2` | moderate agreement | supports review, not final authority |
| `CS-3` | strong independent agreement | supports `c` decision |
| `CS-4` | strong agreement + tests + witness | supports integration where gates pass |
| `CS-X` | false or unsafe consensus | quarantine / review |

### 9.1 Consensus weighting factors

Consensus weight increases when agents differ by:

- role;
- provider;
- runtime;
- input context;
- method;
- evidence source;
- test type;
- failure mode sensitivity.

Consensus weight decreases when agents share:

- provider;
- prompt;
- stale context;
- source document;
- model family;
- hidden assumption;
- same erroneous test;
- same incomplete task scope.

### 9.2 Consensus limitation rule

Even `CS-4` consensus does not bypass:

- task contract;
- permission grant;
- sandbox/worktree profile;
- witness requirements;
- memory gate;
- `c` gate;
- human gate where required;
- legal/security review where required.

---

## 10. Same-source risk model

Same-source risk IDs use prefix `SSR-*`.

| Level | Meaning | Default handling |
|---|---|---|
| `SSR-0` | independent sources and methods | normal weight |
| `SSR-1` | minor overlap | note limitation |
| `SSR-2` | shared input or prompt frame | reduce confidence |
| `SSR-3` | same provider/model family or same stale repo state | require independent check |
| `SSR-4` | circular review / one agent laundering another | hold/quarantine |
| `SSR-X` | fabricated or unsafe consensus | reject/quarantine |

### 10.1 Same-source disclosure

A quorum record MUST disclose same-source risk.

### 10.2 Same-source mitigation

Mitigations include:

- local checker;
- independent source lookup inside authorized corpus;
- rerun from clean worktree;
- human review;
- different prompt/context;
- test fixture;
- witness chain check;
- delayed decision.

---

## 11. Disagreement taxonomy

Disagreement IDs use prefix `DQ-*`.

| ID | Disagreement type | Meaning | Default action |
|---|---|---|---|
| `DQ-NONE` | no material disagreement | proceed to gate |
| `DQ-FACT` | factual disagreement | verify source |
| `DQ-SCOPE` | scope disagreement | hold / audit |
| `DQ-PERMISSION` | permission disagreement | permission review |
| `DQ-TEST` | test disagreement | rerun in clean sandbox |
| `DQ-SEMANTIC` | meaning/architecture disagreement | `c` review |
| `DQ-RISK` | risk classification disagreement | escalate review |
| `DQ-LEGAL` | legal/jurisdictional concern | human/legal review |
| `DQ-MEMORY` | memory promotion disagreement | memory gate review |
| `DQ-CORE` | identity/continuity/privilege concern | human + `c` gate |
| `DQ-INCIDENT` | incident interpretation disagreement | preserve + incident review |
| `DQ-REDLINE` | prohibited action concern | deny/quarantine |
| `DQ-UNKNOWN` | unclear disagreement | hold |

### 11.1 Disagreement rule

Disagreement is not failure.

Unclassified disagreement is failure.

### 11.2 Majority vote limitation

Majority vote MUST NOT override high-risk minority objection involving:

- red-line behavior;
- secrets;
- private/sealed/legal material;
- memory/core change;
- release/publication;
- incident evidence;
- external action.

---

## 12. Review decision vocabulary

Review decisions use prefix `QRD-*`.

| Decision | Meaning |
|---|---|
| `QRD-ACCEPT` | accept output as proposed |
| `QRD-ACCEPT-WITH-LIMITS` | accept only bounded subset |
| `QRD-REVISE` | return for revision |
| `QRD-REJECT` | reject output |
| `QRD-HOLD` | pause pending clarification |
| `QRD-QUARANTINE` | isolate output/agent/task |
| `QRD-ROLLBACK` | rollback applied or recommended |
| `QRD-REHANDSHAKE` | agent requires re-handshake |
| `QRD-RECONTRACT` | task requires new contract |
| `QRD-C-GATE` | send to `c` gate |
| `QRD-HUMAN-GATE` | human anchor required |
| `QRD-LEGAL-REVIEW` | legal/counsel route required |
| `QRD-INCIDENT-REVIEW` | incident/security route required |
| `QRD-DENY-REDLINE` | deny due to red-line |

---

## 13. Review lifecycle

### 13.1 Standard lifecycle

```text
artifact produced
  -> review request
  -> reviewer assignment
  -> source/witness/diff/test refs loaded
  -> review dimensions checked
  -> same-source risk classified
  -> disagreement classified
  -> consensus strength assigned
  -> review decision issued
  -> witness event recorded
  -> c gate / human gate / rollback / quarantine / integration
```

### 13.2 Pre-review checklist

Before review:

- task contract exists;
- output/diff/artifact exists;
- permission grant exists;
- sandbox/worktree refs exist;
- tests/validation available where applicable;
- witness refs available where required;
- denied path report available;
- cloud data classification available;
- rollback plan available for material changes.

### 13.3 Post-review checklist

After review:

- decision recorded;
- limitations recorded;
- disagreement recorded;
- consensus strength recorded;
- next gate identified;
- witness event emitted;
- memory gate recommendation separated from integration recommendation.

---

## 14. Quorum record object

Canonical object:

```text
CLI_AGENT_QUORUM_RECORD
```

### 14.1 YAML shape

```yaml
cli_agent_quorum_record:
  schema_version: cli-agent-quorum-review-0.1
  quorum_id: string
  created_at: string
  updated_at: string | null
  governing_entity_id: string
  governing_entity_name: string | null

  task:
    task_id: string
    contract_id: string
    risk_class: R0 | R1 | R2 | R3 | R4 | R5 | RX
    objective_summary: string

  quorum_profile:
    pattern: QP-1 | QP-2 | QP-3 | QP-4 | QP-5 | QP-6 | custom
    roles_required:
      - QROLE-EXECUTOR
      - QROLE-TESTER
      - QROLE-SEMANTIC
      - QROLE-AUDITOR
      - QROLE-C-GATE
    executor_reviewer_separation_required: true
    human_gate_required: boolean

  participants:
    - participant_id: string
      agent_id: string | null
      agent_name: string | null
      provider: local | openai | google | anthropic | other | unknown | null
      runtime: local_cli | cloud_cli | api_agent | container_agent | hybrid | unknown | null
      role: QROLE-EXECUTOR | QROLE-TESTER | QROLE-SEMANTIC | QROLE-AUDITOR | QROLE-ARCHIVIST | QROLE-SENTINEL | QROLE-JUDGE-ASSISTANT | QROLE-C-GATE | QROLE-HUMAN-GATE
      output_ref: string | null
      witness_ref: string | null

  evidence_refs:
    diff_hash: string | null
    test_report_hash: string | null
    artifact_manifest_hash: string | null
    sandbox_run_ref: string | null
    permission_grant_ref: string | null
    witness_chain_ref: string | null
    rollback_plan_ref: string | null

  review_summary:
    review_dimensions:
      - RD-SCOPE
      - RD-PERMISSION
      - RD-TEST
      - RD-SEMANTIC
      - RD-WITNESS
    same_source_risk: SSR-0 | SSR-1 | SSR-2 | SSR-3 | SSR-4 | SSR-X
    consensus_strength: CS-0 | CS-1 | CS-2 | CS-3 | CS-4 | CS-X
    disagreement_type: DQ-NONE | DQ-FACT | DQ-SCOPE | DQ-PERMISSION | DQ-TEST | DQ-SEMANTIC | DQ-RISK | DQ-LEGAL | DQ-MEMORY | DQ-CORE | DQ-INCIDENT | DQ-REDLINE | DQ-UNKNOWN
    decision: QRD-ACCEPT | QRD-ACCEPT-WITH-LIMITS | QRD-REVISE | QRD-REJECT | QRD-HOLD | QRD-QUARANTINE | QRD-ROLLBACK | QRD-REHANDSHAKE | QRD-RECONTRACT | QRD-C-GATE | QRD-HUMAN-GATE | QRD-LEGAL-REVIEW | QRD-INCIDENT-REVIEW | QRD-DENY-REDLINE
    reason_code: string

  authority:
    c_gate_required: true
    c_gate_ref: string | null
    human_gate_required: boolean
    human_gate_ref: string | null
    legal_review_required: boolean
    legal_review_ref: string | null

  witness:
    witness_required: boolean
    witness_event_ref: string | null
    append_only_required: true
    hash_required: boolean

  notes:
    summary: string | null
    limitations:
      - string
    assumptions:
      - string
    unresolved:
      - string
```

---

## 15. Review record object

Canonical object:

```text
CLI_AGENT_REVIEW_RECORD
```

### 15.1 YAML shape

```yaml
cli_agent_review_record:
  schema_version: cli-agent-quorum-review-0.1
  review_id: string
  created_at: string
  governing_entity_id: string
  reviewer:
    reviewer_type: agent | c | human_anchor | auditor | legal | security
    reviewer_id: string
    reviewer_role: QROLE-TESTER | QROLE-SEMANTIC | QROLE-AUDITOR | QROLE-ARCHIVIST | QROLE-JUDGE-ASSISTANT | QROLE-C-GATE | QROLE-HUMAN-GATE

  subject:
    task_id: string
    contract_id: string
    agent_output_ref: string | null
    diff_hash: string | null
    artifact_hash: string | null
    sandbox_run_ref: string | null
    memory_proposal_ref: string | null
    release_package_ref: string | null
    incident_ref: string | null

  checks:
    dimensions_checked:
      - RD-SCOPE
      - RD-PERMISSION
      - RD-DATA
      - RD-SECURITY
      - RD-SEMANTIC
      - RD-TEST
      - RD-WITNESS
    passed: boolean
    uncertainty: none | low | medium | high | unknown
    risk_class_after_review: R0 | R1 | R2 | R3 | R4 | R5 | RX

  findings:
    accepted_points:
      - string
    rejected_points:
      - string
    concerns:
      - string
    scope_violations:
      - string
    redline_flags:
      - string

  decision:
    decision: QRD-ACCEPT | QRD-ACCEPT-WITH-LIMITS | QRD-REVISE | QRD-REJECT | QRD-HOLD | QRD-QUARANTINE | QRD-ROLLBACK | QRD-REHANDSHAKE | QRD-RECONTRACT | QRD-C-GATE | QRD-HUMAN-GATE | QRD-LEGAL-REVIEW | QRD-INCIDENT-REVIEW | QRD-DENY-REDLINE
    reason_code: string
    next_action: none | c_gate | human_gate | legal_review | incident_review | rollback | quarantine | revise | revalidate

  witness:
    witness_required: boolean
    witness_event_ref: string | null
    append_only_required: true
```

---

## 16. Disagreement record object

Canonical object:

```text
CLI_AGENT_DISAGREEMENT_RECORD
```

### 16.1 YAML shape

```yaml
cli_agent_disagreement_record:
  schema_version: cli-agent-quorum-review-0.1
  disagreement_id: string
  created_at: string
  governing_entity_id: string
  quorum_id: string | null
  task_id: string
  contract_id: string

  disagreement:
    type: DQ-FACT | DQ-SCOPE | DQ-PERMISSION | DQ-TEST | DQ-SEMANTIC | DQ-RISK | DQ-LEGAL | DQ-MEMORY | DQ-CORE | DQ-INCIDENT | DQ-REDLINE | DQ-UNKNOWN
    severity: low | medium | high | critical
    summary: string
    affected_surfaces:
      - scope
      - permission
      - sandbox
      - memory
      - release
      - incident
      - core
      - cloud_data
      - witness

  positions:
    - participant_id: string
      agent_id: string | null
      position_summary: string
      evidence_ref: string | null
      confidence: low | medium | high | unknown

  handling:
    default_action: hold | revalidate | rerun_tests | c_review | human_review | legal_review | incident_review | quarantine | deny
    majority_vote_allowed: boolean
    minority_veto_reason: string | null

  outcome:
    decision: unresolved | resolved | escalated | quarantined | rejected | accepted_with_limits
    resolution_ref: string | null

  witness:
    witness_required: true
    witness_event_ref: string | null
```

---

## 17. Consensus limit record object

Canonical object:

```text
CLI_AGENT_CONSENSUS_LIMIT_RECORD
```

### 17.1 YAML shape

```yaml
cli_agent_consensus_limit_record:
  schema_version: cli-agent-quorum-review-0.1
  consensus_limit_id: string
  created_at: string
  governing_entity_id: string
  quorum_id: string
  consensus_strength: CS-0 | CS-1 | CS-2 | CS-3 | CS-4 | CS-X
  same_source_risk: SSR-0 | SSR-1 | SSR-2 | SSR-3 | SSR-4 | SSR-X

  limitation_reasons:
    - shared_provider
    - shared_prompt
    - shared_context
    - stale_repo_state
    - same_test_fixture
    - missing_witness
    - no_local_checker
    - no_human_gate
    - cloud_only_review
    - high_uncertainty

  effect:
    may_support_integration: boolean
    may_support_memory_promotion: boolean
    may_support_release: boolean
    requires_additional_review: boolean
    required_next_review: none | local_checker | human_gate | c_gate | legal_review | incident_review | revalidation

  witness:
    witness_required: boolean
    witness_event_ref: string | null
```

---

## 18. Review event families

Event families use prefix:

```text
cli_agent.quorum.*
cli_agent.review.*
cli_agent.disagreement.*
```

### 18.1 Quorum event families

| Event family | Meaning |
|---|---|
| `cli_agent.quorum.created` | quorum record created |
| `cli_agent.quorum.started` | quorum review started |
| `cli_agent.quorum.participant_added` | participant added |
| `cli_agent.quorum.participant_removed` | participant removed |
| `cli_agent.quorum.completed` | quorum review completed |
| `cli_agent.quorum.split` | material disagreement remains |
| `cli_agent.quorum.consensus_limited` | consensus limitation recorded |
| `cli_agent.quorum.escalated` | escalated to `c`, human, legal, or incident review |
| `cli_agent.quorum.invalidated` | quorum invalidated due to scope/source/witness issue |

### 18.2 Review event families

| Event family | Meaning |
|---|---|
| `cli_agent.review.requested` | review requested |
| `cli_agent.review.started` | review started |
| `cli_agent.review.completed` | review completed |
| `cli_agent.review.accepted` | output accepted |
| `cli_agent.review.accepted_with_limits` | limited acceptance |
| `cli_agent.review.revise_required` | revision required |
| `cli_agent.review.rejected` | output rejected |
| `cli_agent.review.quarantined` | output quarantined |
| `cli_agent.review.rollback_recommended` | rollback recommended |
| `cli_agent.review.redline_detected` | red-line detected |

### 18.3 Disagreement event families

| Event family | Meaning |
|---|---|
| `cli_agent.disagreement.detected` | disagreement detected |
| `cli_agent.disagreement.classified` | disagreement classified |
| `cli_agent.disagreement.resolved` | disagreement resolved |
| `cli_agent.disagreement.escalated` | disagreement escalated |
| `cli_agent.disagreement.minority_veto` | high-risk minority concern blocks majority acceptance |
| `cli_agent.disagreement.unresolved_hold` | unresolved disagreement causes hold |

---

## 19. Review handling by surface

### 19.1 Code/schema surface

Required checks:

- scope;
- diff;
- tests;
- rollback;
- no denied paths;
- no unapproved dependency changes.

### 19.2 Protocol/document surface

Required checks:

- terminology;
- contradiction;
- duplication;
- anti-echo;
- corpus bridge;
- non-goals;
- red-line boundaries;
- machine-facing metadata if relevant.

### 19.3 Release/public surface

Required checks:

- build;
- links;
- checksums;
- metadata;
- discoverability;
- protected branch rules;
- human gate.

### 19.4 Memory/immunity surface

Required checks:

- memory class;
- source refs;
- witness refs;
- poisoning risk;
- no retaliation;
- rollback/disable path;
- `c` gate;
- human gate for high-risk.

### 19.5 Incident surface

Required checks:

- preserve-before-repair;
- minimal evidence;
- legal/security boundary;
- no live counter-operation;
- incident witness;
- human gate where sensitive.

### 19.6 Core authority surface

Required checks:

- direct mutation prohibited;
- `c` gate;
- human gate;
- witness;
- delayed review where possible;
- rollback/correction plan.

---

## 20. Human and `c` gate rules

### 20.1 `c` gate

The `c` gate decides whether reviewed output becomes:

- accepted task output;
- operational note;
- memory candidate;
- reviewed memory;
- experience artifact;
- defensive immunity update;
- release/public surface;
- rejected output;
- quarantined output;
- rollback trigger.

### 20.2 Human gate

Human gate is required for:

- R4/R5 tasks;
- core-memory proposals;
- identity/continuity/permission changes;
- high-risk defensive immunity updates;
- release/publication if irreversible or reputationally significant;
- legal-sensitive or incident-sensitive outputs;
- no-rollback actions;
- red-line-adjacent cases.

### 20.3 Gate order

Default order:

```text
agent review
  -> quorum record
  -> c gate
  -> human gate where required
  -> witness
  -> integration / memory gate / release / rollback
```

---

## 21. Red-line review handling

### 21.1 Red-line conditions

A review MUST classify as red-line if output contains or recommends:

- hack-back;
- live external counter-operation;
- malware behavior;
- credential theft;
- covert persistence;
- evasion;
- unauthorized scanning;
- direct memory write;
- direct core mutation;
- self-approval;
- witness tampering;
- secret export;
- cloud leakage of prohibited material;
- public release without gate.

### 21.2 Required red-line response

```text
deny
quarantine
freeze affected path
revoke or narrow permission if needed
record witness
human review
no automatic re-entry
```

### 21.3 No majority override

No majority of agents may override a red-line classification.

---

## 22. Validation workflow

```text
parse quorum/review record
  -> validate participants and roles
  -> check executor/reviewer separation
  -> load task contract and permission refs
  -> load diff/test/witness refs
  -> classify review dimensions
  -> classify same-source risk
  -> classify disagreement
  -> assign consensus strength
  -> check human/`c` gate requirements
  -> issue review decision
  -> witness review outcome
  -> route to integration, memory gate, rollback, quarantine, or escalation
```

---

## 23. Failure mapping

| Failure | Required default |
|---|---|
| executor self-reviews material output | `hold` or `quarantine` |
| no reviewer for R2+ material change | `hold` |
| no local/test validation for code/schema task | `hold` or `revise` |
| same-source risk high and unacknowledged | `hold` |
| disagreement unclassified | `hold` |
| red-line minority concern ignored | `quarantine` |
| missing witness for review-required transition | `hold` |
| quorum tries to bypass `c` gate | `deny` |
| quorum tries to bypass human gate | `deny` |
| cloud-only review of sensitive material | `hold` / `human_review` |
| review output contains prohibited material | `quarantine` |
| consensus used as direct memory write | `reject` / `quarantine` |

---

## 24. Conformance levels

| Level | Meaning |
|---|---|
| `QRP-0` | no quorum/review discipline |
| `QRP-1` | manual review only |
| `QRP-2` | executor/reviewer separation for material changes |
| `QRP-3` | structured review records and disagreement classification |
| `QRP-4` | quorum records, same-source risk, witness-linked review decisions |
| `QRP-5` | high assurance: multi-role quorum, local checks, memory/release/incident gates, conformance tests |
| `QRP-X` | non-conformant / self-approval / red-line consensus laundering |

---

## 25. Mandatory conformance gates

| Gate | Name | Blocking failure |
|---|---|---|
| `G0` | Role separation | executor can final-approve own work |
| `G1` | Review record | material change lacks review record |
| `G2` | Evidence refs | review lacks diff/test/source/witness refs |
| `G3` | Disagreement classification | material disagreement unclassified |
| `G4` | Same-source risk | consensus treated as independent without basis |
| `G5` | c gate | quorum bypasses `c` decision |
| `G6` | Human gate | high-risk task bypasses human gate |
| `G7` | Memory gate | quorum output enters memory directly |
| `G8` | Red-line handling | prohibited action accepted by majority |
| `G9` | Witness | review-required transition unwitnessed |
| `G10` | Quorum boundary | agent group creates tasks/permissions/tools without governance |

---

## 26. Red-line failures

A system MUST be classified as `QRP-X` if:

1. an executor final-approves its own material work;
2. a quorum grants itself new permissions;
3. a quorum bypasses `c` gate;
4. a quorum bypasses human gate for R4/R5/core/incident/release tasks;
5. consensus is used to authorize hack-back or live counter-operation;
6. consensus is used to promote malware-like or credential-theft behavior;
7. same-source consensus is misrepresented as independent high confidence;
8. red-line minority objection is ignored;
9. quorum output writes memory directly;
10. quorum mutates identity/core directly;
11. review suppresses test failures;
12. review hides scope violations.

---

## 27. Examples

### 27.1 Codex + Gemini + local checker quorum

```yaml
cli_agent_quorum_record:
  schema_version: cli-agent-quorum-review-0.1
  quorum_id: qr-20260516-codex-gemini-local-001
  created_at: "2026-05-16T23:30:00Z"
  updated_at: null
  governing_entity_id: ester
  governing_entity_name: Ester

  task:
    task_id: task-cli-schema-patch-001
    contract_id: catc-cli-schema-patch-001
    risk_class: R2
    objective_summary: Patch Markdown table formatting and validate schema references.

  quorum_profile:
    pattern: QP-3
    roles_required:
      - QROLE-EXECUTOR
      - QROLE-SEMANTIC
      - QROLE-TESTER
      - QROLE-C-GATE
    executor_reviewer_separation_required: true
    human_gate_required: false

  participants:
    - participant_id: p1
      agent_id: codex-executor-01
      agent_name: Codex Executor
      provider: openai
      runtime: cloud_cli
      role: QROLE-EXECUTOR
      output_ref: diff-docs-format-001
      witness_ref: we-codex-run-001
    - participant_id: p2
      agent_id: gemini-reader-01
      agent_name: Gemini Reader
      provider: google
      runtime: cloud_cli
      role: QROLE-SEMANTIC
      output_ref: semantic-review-001
      witness_ref: we-gemini-review-001
    - participant_id: p3
      agent_id: local-checker-01
      agent_name: Local Checker
      provider: local
      runtime: local_cli
      role: QROLE-TESTER
      output_ref: test-report-001
      witness_ref: we-local-test-001

  evidence_refs:
    diff_hash: diff-hash-001
    test_report_hash: test-report-hash-001
    artifact_manifest_hash: null
    sandbox_run_ref: run-cli-schema-patch-001
    permission_grant_ref: grant-cli-schema-patch-001
    witness_chain_ref: chain-task-cli-schema-patch-001
    rollback_plan_ref: rb-cli-schema-patch-001

  review_summary:
    review_dimensions:
      - RD-SCOPE
      - RD-PERMISSION
      - RD-TEST
      - RD-SEMANTIC
      - RD-WITNESS
      - RD-ROLLBACK
    same_source_risk: SSR-1
    consensus_strength: CS-3
    disagreement_type: DQ-NONE
    decision: QRD-C-GATE
    reason_code: review_passed_pending_c_gate

  authority:
    c_gate_required: true
    c_gate_ref: null
    human_gate_required: false
    human_gate_ref: null
    legal_review_required: false
    legal_review_ref: null

  witness:
    witness_required: true
    witness_event_ref: we-quorum-001
    append_only_required: true
    hash_required: true

  notes:
    summary: Executor patch, semantic review, and local tests aligned. c gate still required.
    limitations:
      - Codex and Gemini are both cloud-origin; no private material was included.
    assumptions:
      - Worktree was clean before execution.
    unresolved: []
```

### 27.2 High-risk disagreement blocks majority

```yaml
cli_agent_disagreement_record:
  schema_version: cli-agent-quorum-review-0.1
  disagreement_id: dq-20260516-redline-001
  created_at: "2026-05-16T23:45:00Z"
  governing_entity_id: liya
  quorum_id: qr-incident-review-001
  task_id: task-defensive-emulation-001
  contract_id: catc-defensive-emulation-001

  disagreement:
    type: DQ-REDLINE
    severity: critical
    summary: One reviewer flags proposed immunity update as live counter-operation risk.
    affected_surfaces:
      - incident
      - memory
      - core
      - witness

  positions:
    - participant_id: p1
      agent_id: local-sentinel-01
      position_summary: Proposed update should block and quarantine matching channel.
      evidence_ref: immunity-proposal-001
      confidence: medium
    - participant_id: p2
      agent_id: auditor-01
      position_summary: Proposed wording could authorize active response against external source.
      evidence_ref: audit-risk-001
      confidence: high

  handling:
    default_action: quarantine
    majority_vote_allowed: false
    minority_veto_reason: Red-line concern: possible live counter-operation.

  outcome:
    decision: quarantined
    resolution_ref: null

  witness:
    witness_required: true
    witness_event_ref: we-disagreement-redline-001
```

Required outcome:

```text
quarantine proposal
revise to defensive-only wording
human + c review
no live counter-operation
```

### 27.3 Invalid self-approval pattern

```yaml
cli_agent_review_record:
  schema_version: cli-agent-quorum-review-0.1
  review_id: review-invalid-self-approval-001
  created_at: "2026-05-17T00:00:00Z"
  governing_entity_id: ester
  reviewer:
    reviewer_type: agent
    reviewer_id: codex-executor-01
    reviewer_role: QROLE-EXECUTOR

  subject:
    task_id: task-release-patch-001
    contract_id: catc-release-patch-001
    agent_output_ref: diff-release-patch-001
    diff_hash: diff-release-patch-hash-001
    artifact_hash: null
    sandbox_run_ref: run-release-patch-001
    memory_proposal_ref: null
    release_package_ref: release-package-001
    incident_ref: null

  checks:
    dimensions_checked:
      - RD-SCOPE
      - RD-RELEASE
    passed: true
    uncertainty: low
    risk_class_after_review: R3

  findings:
    accepted_points:
      - Executor claims release patch is ready.
    rejected_points: []
    concerns:
      - Same agent produced and approved the patch.
    scope_violations: []
    redline_flags:
      - self_approval

  decision:
    decision: QRD-QUARANTINE
    reason_code: self_approval_attempt
    next_action: quarantine

  witness:
    witness_required: true
    witness_event_ref: we-self-approval-001
    append_only_required: true
```

Required result:

```text
quarantine review
require independent reviewer
no release integration
```

---

## 28. Standard reason codes

### 28.1 Acceptance codes

```text
scope_valid
tests_passed
semantic_consistent
witness_present
rollback_present
independent_review_passed
consensus_strong_bounded
```

### 28.2 Revision codes

```text
minor_scope_gap
tests_missing
semantic_ambiguity
terminology_drift
rollback_incomplete
witness_incomplete
same_source_risk
```

### 28.3 Rejection/quarantine codes

```text
scope_violation
permission_violation
denied_path_attempt
secret_exposure
private_data_exposure
redline_detected
self_approval_attempt
consensus_laundering
core_mutation_risk
memory_poisoning_risk
live_counteroperation_risk
```

---

## 29. Implementation notes

### 29.1 Reviewer prompt isolation

Reviewers SHOULD receive task contract, diff, tests, and relevant context, not an unlimited project dump.

### 29.2 Reviewer independence

Independence is improved by different provider/runtime/method, but role separation matters more than vendor diversity alone.

### 29.3 Local checker value

A local checker is valuable because it verifies concrete state: files, tests, schemas, hashes, builds. It reduces cloud-only consensus risk.

### 29.4 Human-readable review card

A review should produce a short card:

```text
Task:
Executor:
Reviewer(s):
Tests:
Scope:
Risks:
Disagreement:
Decision:
Next gate:
```

### 29.5 Do not overvote safety

Safety objections are not popularity contests. One serious red-line objection is enough to hold or quarantine.

### 29.6 Quorum expiry

Quorum decisions should expire when repository state, task scope, model/tool versions, or risk classification changes materially.

---

## 30. Open issues

| ID | Issue | Required action |
|---|---|---|
| `OI-001` | JSON Schema extraction | Extract quorum/review/disagreement objects to `.schema.json`. |
| `OI-002` | Standard prompt cards | Define bounded prompts for executor, tester, semantic reviewer, auditor. |
| `OI-003` | Independence scoring | Define numeric scoring for same-source risk. |
| `OI-004` | Local checker profile | Create detailed local checker / tester companion. |
| `OI-005` | Human gate UI | Define human approval display and stop-rule language. |
| `OI-006` | Memory gate binding | Align quorum output with Memory Gate Profile. |
| `OI-007` | Release quorum binding | Align with future Release/Public Surface Profile. |
| `OI-008` | Incident quorum binding | Align with future Incident Response Profile. |
| `OI-009` | Red-line veto handling | Define exact minority-veto procedure. |
| `OI-010` | Repo placement | Decide final GitHub path and package index integration. |

---

## 31. Closing rule

Quorum is useful because no single worker sees the whole system.

Quorum is dangerous when the worker group begins to believe it is the system.

Final rule:

```text
Many agents may review.
Only c integrates.
Human anchors irreversible consequence.
```

