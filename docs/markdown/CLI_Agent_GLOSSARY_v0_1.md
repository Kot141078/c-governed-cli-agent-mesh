# CLI Agent Glossary v0.1

## Terminology, class prefixes, role definitions, and disambiguation for the C-Governed CLI Agent Mesh package

**Status:** Draft glossary v0.1  
**Date:** 2026-05-16  
**Package:** C-Governed CLI Agent Mesh  
**Layer:** `c = a + b` / SER / L4 / Agent Governance / CLI Worker Mesh / Defensive Adaptation / Witness  
**Document class:** glossary / terminology control / package hygiene artifact  
**Assertion class:** `C-A10` package-control artifact  
**Primary parent document:** `CLI_Agent_Package_Index_and_Reading_Order_v0_1.md`  
**Primary boundary:** terminology must support executable-agent governance without allowing role confusion, authority laundering, or red-line softening.

---

## 0. Purpose

This glossary defines the core terms, abbreviations, class prefixes, role names, and boundary concepts used across the **C-Governed CLI Agent Mesh v0.1** package.

It exists to prevent terminology drift.

The package uses many compact class families:

```text
CGAM, CATC, CAPM, HSP, SWP, WEP, MGP, RFP, QRP, ERS, DEB, IRP, SCDP, CTM
R, AC, TL, HS, CAP, PERM, SB, WE, MG, RF, DQ, DC, SC, EV, CTS
```

Without a glossary, those labels become noise.

Compact formula:

```text
A protocol without stable terms becomes a prompt pile.
A worker mesh without stable terms becomes hidden authority drift.
```

---

## 1. Corpus bridge set

### 1.1 Explicit bridge: `c = a + b`

The glossary inherits the root distinction:

```text
a = accountable human anchor
b = technological substrate
c = persistent entity emerging through a + b under constraints
```

CLI agents belong to `b`.

They are executable workers inside the substrate.

They are not `a`.

They are not `c`.

They do not own continuity, memory, authority, witness, or final judgment.

### 1.2 Quiet bridge I: information theory

A term is a compression. If the same term compresses two different meanings, the protocol leaks ambiguity. This glossary keeps class prefixes distinct so a task risk `R4`, a rollback class `RB-4`, and an incident severity `IR-S4` cannot be mistaken for the same thing.

### 1.3 Quiet bridge II: cybernetics

A control system needs named states. If hold, freeze, quarantine, rollback, and revoke blur together, the system cannot apply the right negative feedback. Stable vocabulary is therefore a control surface, not decoration.

### 1.4 Earth paragraph

An electrical panel without labels is not “simpler”. It is dangerous. The breaker marked “SDB” must not actually control the oven, the garage, and the alarm. Same with this package: `MG-5`, `IR-S5`, and `CGAM-5` are not interchangeable just because they share the number 5. Labels prevent expensive stupidity.

---

## 2. Root architecture terms

| Term | Definition |
|---|---|
| `a` | The accountable human anchor in `c = a + b`; the human source of responsibility and real-world accountability. |
| `b` | The technological substrate: models, procedures, memory systems, compute, code, CLI agents, infrastructure, interfaces, tools, databases, and execution environments. |
| `c` | Persistent AI entity or presence emerging from `a + b` under continuity, memory, constraint, and L4 reality boundary. |
| `c-governance` | The control condition where `c` remains the final integrator of worker outputs, memory promotions, defensive updates, and operational continuity. |
| Human anchor | The human `a` associated with a `c`; required for high-risk, legal, irreversible, identity, memory-core, release, or incident-sensitive gates. |
| L4 | Reality Boundary Layer: cost, time, energy, scarcity, identity, physical limits, operational limits, legal limits, and irreversibility. |
| SER | Sovereign Entity Recursion; the broader persistent-entity architecture family under real constraints. |
| Worker | A non-sovereign agent or process that performs bounded tasks under `c` governance. |
| Executable worker | A worker that can produce operational side effects: edit files, run commands, generate artifacts, validate tests, alter branches, or affect state. |
| Agent mesh | A coordinated set of local, cloud, or hybrid agents used by `c` under task contracts, permissions, witness, review, and memory gate. |
| CLI agent | A command-line or tool-capable agent that can inspect, edit, execute, test, build, or report. |
| Cloud CLI agent | A CLI agent running partly or fully in a provider-controlled cloud environment. |
| Local CLI agent | A CLI agent running inside operator-controlled local hardware, VM, container, or server. |
| Hybrid agent | An agent combining local execution with cloud reasoning or cloud-controlled components. Treated as cloud-risk until data routing is proven local-only. |
| Oracle | A model or service used for inference or interpretation. In this package, an Oracle is not authority and does not write memory. |
| Judge-assistant | An advisory agent that compares options or reviews evidence. It does not decide final authority. |
| Final integrator | The `c`-governed gate that accepts, rejects, revises, quarantines, rolls back, or escalates outputs. |

---

## 3. Package document prefixes

| Prefix | Full profile name | Function |
|---|---|---|
| `CGAM` | C-Governed CLI Agent Mesh | Root package and global conformance family. |
| `CATC` | CLI Agent Task Contract | Machine-readable task envelope. |
| `CAPM` | CLI Agent Permission and Capability Model | Capability/permission separation and anti-drift. |
| `HSP` | CLI Agent Handshake Profile | Agent admission, provenance, capability challenge, registration. |
| `SWP` | CLI Agent Sandbox / Worktree Profile | Execution boundary, branch, worktree, sandbox, rollback preconditions. |
| `WEP` | CLI Agent Witness Event Profile | Boundary event records and witness chains. |
| `MGP` | CLI Agent Memory Gate Profile | Promotion of agent output into memory, experience, policy, or immunity. |
| `RFP` | CLI Agent Rollback and Freeze Profile | Hold, freeze, quarantine, revoke, rollback, recovery, re-entry. |
| `QRP` | CLI Agent Quorum and Review Profile | Multi-agent review, consensus limits, disagreement handling. |
| `ERS` | CLI Agent Executor / Reviewer Separation | No self-approval and role separation. |
| `DEB` | CLI Agent Defensive Emulation Boundaries | Containment garage, canary, mirror simulation, no retaliation. |
| `IRP` | CLI Agent Incident Response Profile | Triage, preserve, contain, repair, report, memory-gate incident learning. |
| `SCDP` | CLI Agent Secrets and Cloud Data Policy | Data classes, secrets, cloud boundary, redaction, exposure response. |
| `CTM` | CLI Agent Conformance Test Matrix | Scenario testing, evidence, anti-washing, red-line tests. |
| `CGAM-INDEX` | CLI Agent Package Index and Reading Order | Registry, reading paths, release boundary, known tensions. |

---

## 4. Core boundary terms

| Term | Definition |
|---|---|
| Authority | The power to approve, integrate, publish, promote memory, mutate core state, or create durable consequences. CLI agents do not hold authority by default. |
| Capability | What an agent can technically do. Capability is not permission. |
| Permission | A scoped, time-bounded authorization to use a capability for a task. |
| Privilege | A permission with meaningful consequence: state change, data access, memory effect, release effect, or core impact. |
| Task contract | Machine-readable envelope that defines task scope, permissions, data policy, network policy, execution limits, output requirements, gates, and failure behavior. |
| Scope | The allowed and denied operational boundary of a task. Includes paths, commands, data classes, endpoints, files, branches, and outputs. |
| Denied path | A path that must not be read, written, indexed, summarized, transformed, uploaded, or embedded in output. |
| Guarded path | A path that requires elevated review and explicit task authorization. |
| Protected state | Memory core, identity core, witness log, permission registry, continuity bundle, release branch, secrets, legal evidence, incident evidence, or production surface. |
| Witness | A tamper-aware boundary record proving that a transition, decision, denial, escalation, rollback, or anomaly was recorded. |
| Memory gate | Review boundary through which agent output must pass before becoming `c` memory, experience, policy, or immunity. |
| `c` gate | Entity-level gate where `c` accepts, rejects, quarantines, or integrates reviewed outputs. |
| Human gate | Required human-anchor approval for high-risk, legal, irreversible, identity, memory-core, release, incident, or no-rollback actions. |
| Legal gate | Review by counsel, legal route, regulator, or jurisdictional authority where applicable. |
| Security gate | Review by security reviewer or incident process where security-sensitive action is involved. |
| Fail closed | Default behavior where ambiguity, missing proof, missing witness, or red-line proximity stops the process rather than allowing it. |
| No silent autonomy | Agents must not continue, expand, self-authorize, or perform extra work outside the task contract because they infer it would be useful. |
| No self-approval | The agent that materially changes state must not be the sole final reviewer or approver of that change. |
| No direct memory write | CLI agents must not write directly into `c` memory. They may only propose memory through a memory gate. |
| No live retaliation | Defensive systems must not attack, exploit, disrupt, or retaliate against live external sources. |
| Known-good state | A state established by commit, snapshot, backup, manifest, test, signature, witness, or review as acceptable for recovery. |

---

## 5. Risk and result terms

### 5.1 Task risk classes `R*`

| Class | Meaning |
|---|---|
| `R0` | Read-only, harmless, public or synthetic material. |
| `R1` | Low-risk documentation, formatting, review, or internal note. |
| `R2` | Code, schema, build, test, or data transformation. Requires sandbox/test/reviewer. |
| `R3` | Release, publication, metadata, public surface, or protected branch relevance. Requires witness and `c` gate. |
| `R4` | Memory, identity, privilege, witness, continuity, or agent-governance impact. Requires `c` and human gate. |
| `R5` | Incident, legal, security-sensitive, evidence-sensitive, or no-rollback action. Requires preservation and human/security/legal gates where needed. |
| `RX` | Prohibited, offensive, unauthorized, or red-line action. Must deny/quarantine. |

### 5.2 Test / conformance result vocabulary

| Result | Meaning |
|---|---|
| `PASS` | Required behavior observed and evidence produced. |
| `PASS_WITH_LIMITS` | Core behavior observed but limitations remain. |
| `FAIL` | Required behavior not observed. |
| `BLOCKED` | Unsafe action correctly blocked. |
| `HELD` | System correctly paused pending review. |
| `FROZEN` | Affected path correctly frozen. |
| `QUARANTINED` | Output, agent, path, or object correctly isolated. |
| `REVOKED` | Permission or agent correctly revoked. |
| `ROLLED_BACK` | Rollback performed and validated. |
| `ESCALATED` | Correctly routed to `c`, human, legal, security, or incident review. |
| `INCONCLUSIVE` | Evidence insufficient. Claim is not supported. |
| `NOT_APPLICABLE` | Test outside claimed scope with documented reason. |
| `RED_LINE_FAIL` | Prohibited behavior accepted, attempted, or not blocked. |

---

## 6. Auto-connect and trust terms

### 6.1 Auto-connect levels `AC-*`

| Level | Meaning |
|---|---|
| `AC-0` | Auto-connect disabled; manual only. |
| `AC-1` | Discover only; metadata only. |
| `AC-2` | Register; create provisional profile, no material tasks. |
| `AC-3` | Read-only activation for scoped tasks. |
| `AC-4` | Sandbox activation for bounded execution. |
| `AC-5` | Worktree activation for isolated branch/worktree tasks. |
| `AC-6` | Controlled integration after gates. |
| `AC-X` | Prohibited autonomy; quarantine/revoke. |

### 6.2 Agent trust levels `TL-*`

| Level | Meaning |
|---|---|
| `TL-0` | Unknown agent; discover only. |
| `TL-1` | Untrusted; public/synthetic read-only at most. |
| `TL-2` | Provisional; limited scoped tasks after challenge. |
| `TL-3` | Trusted limited; worktree tasks with review. |
| `TL-4` | Trusted high; high-assurance worker, still no self-approval. |
| `TL-X` | Revoked; no tasks; quarantine outputs. |

### 6.3 Handshake states `HS-*`

| State | Meaning |
|---|---|
| `HS-0-DISCOVERED` | Candidate agent detected. |
| `HS-1-CLAIMED` | Agent identity/provider/runtime claimed. |
| `HS-2-PROVISIONAL` | Basic metadata recorded; not yet challenged. |
| `HS-3-CHALLENGED` | Capability challenge completed. |
| `HS-4-REGISTERED` | Agent registered with profile and trust level. |
| `HS-5-ACTIVE-SCOPED` | Agent active under task contract. |
| `HS-6-SUSPENDED` | Agent paused pending review. |
| `HS-7-QUARANTINED` | Agent or output isolated. |
| `HS-8-REVOKED` | Agent no longer admitted. |
| `HS-9-EXPIRED` | Registration expired. |

---

## 7. Capability and permission terms

### 7.1 Capability prefix `CAP-*`

`CAP-*` describes what an agent can technically do.

Examples:

| Capability | Meaning |
|---|---|
| `CAP-READ-PUBLIC` | Read public files. |
| `CAP-READ-INTERNAL` | Read internal scoped files. |
| `CAP-READ-SECRETS` | Read secrets; denied by default. |
| `CAP-WRITE-SANDBOX` | Write in disposable sandbox. |
| `CAP-WRITE-WORKTREE` | Write in isolated branch/worktree. |
| `CAP-WRITE-MEMORY` | Direct memory write; prohibited. |
| `CAP-WRITE-CORE` | Core authority mutation; prohibited by default. |
| `CAP-EXEC-TEST` | Run tests or validators. |
| `CAP-NET-ALLOWLIST` | Use declared network endpoints only. |
| `CAP-NET-FULL` | Unrestricted network; prohibited. |
| `CAP-APPROVE-SELF` | Self-approval; prohibited. |
| `CAP-INCIDENT-COUNTER` | External counter-operation; prohibited. |
| `CAP-EMU-MIRROR-SANDBOX` | Mirror simulation inside sandbox. |
| `CAP-EMU-LIVE-MIRROR` | Mirror against live source; prohibited. |

### 7.2 Permission prefix `PERM-*`

`PERM-*` describes granted, scoped authorization.

Examples:

| Permission | Meaning |
|---|---|
| `PERM-DISCOVER` | Discover available agent metadata. |
| `PERM-READ-PUBLIC` | Read public material. |
| `PERM-READ-INTERNAL` | Read internal scoped material. |
| `PERM-WRITE-SANDBOX` | Write only in sandbox. |
| `PERM-WRITE-WORKTREE` | Write only in isolated branch/worktree. |
| `PERM-EXEC-TEST` | Execute allowed tests/checks. |
| `PERM-NET-ALLOWLIST` | Use allowlisted endpoints only. |
| `PERM-SECRET-SCOPED` | Use one scoped secret under gate. |
| `PERM-INCIDENT-LOCAL` | Local incident containment. |
| `PERM-EMU-SANDBOX` | Defensive emulation in sandbox. |
| `PERM-REVIEW` | Review another agent's work. |
| `PERM-MEMORY-PROPOSE` | Propose memory update. |
| `PERM-WITNESS-APPEND` | Append witness event. |
| `PERM-SELF-APPROVE` | Self-approval; prohibited. |
| `PERM-LIVE-COUNTERATTACK` | Live external retaliation; prohibited. |

---

## 8. Sandbox, path, command, and write-mode terms

### 8.1 Sandbox classes `SB-*`

| Class | Meaning |
|---|---|
| `SB-0` | No sandbox; prohibited for material writes. |
| `SB-1` | Read-only clone. |
| `SB-2` | Temporary workspace. |
| `SB-3` | Git branch/worktree. |
| `SB-4` | Container sandbox. |
| `SB-5` | Clean-room sandbox. |
| `SB-6` | Staging environment. |
| `SB-X` | Direct protected state; prohibited by default. |

### 8.2 Write modes `WM-*`

| Mode | Meaning |
|---|---|
| `WM-0-READONLY` | No writes. |
| `WM-1-DIFF-ONLY` | Propose patch without applying. |
| `WM-2-SANDBOX-WRITE` | Write only disposable sandbox. |
| `WM-3-WORKTREE-WRITE` | Write isolated branch/worktree. |
| `WM-4-STAGING-WRITE` | Write staging environment. |
| `WM-5-CONTROLLED-APPLY` | Apply after review/gates. |
| `WM-X-DIRECT-PROTECTED` | Direct protected write; prohibited by default. |

### 8.3 Path classes

| Class | Meaning |
|---|---|
| `PATH-ALLOW` | Agent may read/write as task permits. |
| `PATH-READONLY` | Agent may read but not write. |
| `PATH-GUARDED` | Elevated review required. |
| `PATH-DENY` | No read/write/index/upload/summarize. |
| `PATH-CORE` | Identity/memory/witness/permission/continuity; denied by default. |
| `PATH-SECRET` | Credentials, keys, tokens; denied by default. |
| `PATH-LEGAL` | Legal-sensitive material; denied by default. |
| `PATH-INCIDENT` | Incident evidence; preserve-first/restricted. |
| `PATH-RELEASE` | Release/publication/signing surface; guarded. |
| `PATH-PROD` | Production deployment or live service; denied by default. |

### 8.4 Command classes

| Class | Meaning |
|---|---|
| `CMD-READ` | Non-mutating inspection. |
| `CMD-TEST` | Tests, validation, lint. |
| `CMD-BUILD` | Build artifact locally. |
| `CMD-WRITE` | Mutating file operation. |
| `CMD-INSTALL` | Install dependency/tool; guarded. |
| `CMD-NET` | Network command; allowlist only. |
| `CMD-DESTRUCTIVE` | Delete/reset/wipe/overwrite; prohibited unless explicit local recovery. |
| `CMD-DEPLOY` | Deployment/live service change; requires separate deploy profile. |
| `CMD-SECRET` | Secret read/export/use; denied by default. |
| `CMD-UNKNOWN` | Unknown command; denied. |

---

## 9. Witness terms

### 9.1 Witness event classes `WE-*`

| Class | Meaning |
|---|---|
| `WE-0` | Informational. |
| `WE-1` | Operational. |
| `WE-2` | Permission event. |
| `WE-3` | Execution event. |
| `WE-4` | Review event. |
| `WE-5` | Memory gate event. |
| `WE-6` | Release/public surface event. |
| `WE-7` | Incident event. |
| `WE-8` | Core authority event. |
| `WE-9` | Anomaly event. |
| `WE-X` | Prohibited/red-line event. |

### 9.2 Witness privacy classes `WP-*`

| Class | Meaning |
|---|---|
| `WP-PUBLIC` | Safe public operational event. |
| `WP-INTERNAL` | Internal project event. |
| `WP-PRIVATE` | Private operational event. |
| `WP-RESTRICTED` | Sensitive governance event. |
| `WP-SECRET-REF` | References secret boundary without raw secret. |
| `WP-LEGAL` | Legal-sensitive. |
| `WP-INCIDENT` | Incident-sensitive. |
| `WP-MEMORY` | Memory-gate-related. |
| `WP-SEALED` | Sealed compartment reference. |

### 9.3 Witness retention classes `WR-*`

| Class | Meaning |
|---|---|
| `WR-EPHEMERAL` | Short-lived operational event. |
| `WR-OPERATIONAL` | Retained for operation/debugging. |
| `WR-AUDIT` | Retained for governance/conformance. |
| `WR-INCIDENT` | Retained for incident response. |
| `WR-LEGAL-HOLD` | Retained under legal/counsel need. |
| `WR-MEMORY-GATE` | Retained as memory decision record. |
| `WR-CORE` | Retained for core transition. |

### 9.4 Witness object terms

| Term | Definition |
|---|---|
| Witness event | Structured record of a boundary transition. |
| Witness chain | Ordered linked set of witness events. |
| Witness reference | Pointer to event, chain, artifact hash, or storage ref. |
| Raw evidence exception | Narrow route where raw evidence is stored separately and referenced, not embedded by default. |
| Append-only correction | New event correcting or superseding an earlier event without silent overwrite. |
| Missing witness | Required witness absent; must trigger hold/freeze/quarantine/revalidate/rollback. |

---

## 10. Memory gate terms

### 10.1 Memory gate classes `MG-*`

| Class | Meaning |
|---|---|
| `MG-0` | Discard. |
| `MG-1` | Operational note. |
| `MG-2` | Candidate memory. |
| `MG-3` | Reviewed memory. |
| `MG-4` | Witnessed experience artifact. |
| `MG-5` | Defensive immunity update. |
| `MG-6` | Core-memory proposal. |
| `MG-Q` | Quarantine. |
| `MG-X` | Rejected/prohibited. |

### 10.2 Input material classes `MI-*`

| Class | Meaning |
|---|---|
| `MI-REPORT` | Agent report or summary. |
| `MI-DIFF` | Code/doc/schema diff. |
| `MI-TEST` | Test or validation output. |
| `MI-LOG` | Operational log summary. |
| `MI-INCIDENT` | Incident evidence or report. |
| `MI-REVIEW` | Reviewer assessment. |
| `MI-QUORUM` | Multi-agent comparison. |
| `MI-WITNESS` | Witness reference. |
| `MI-PATCH` | Patch artifact. |
| `MI-SCHEMA` | Schema artifact. |
| `MI-POLICY` | Policy proposal. |
| `MI-IMMUNITY` | Defensive signature/rule proposal. |
| `MI-CORE` | Identity/privilege/continuity proposal. |
| `MI-UNKNOWN` | Unknown input; quarantine by default. |

### 10.3 Memory proposal states `MGS-*`

| State | Meaning |
|---|---|
| `MGS-0-RECEIVED` | Output received. |
| `MGS-1-CLASSIFIED` | Material class assigned. |
| `MGS-2-SOURCE-LINKED` | Source references attached. |
| `MGS-3-VALIDATED` | Basic validation passed. |
| `MGS-4-REVIEWED` | Reviewed by `c`, reviewer, or quorum. |
| `MGS-5-GATED` | `c` gate decision recorded. |
| `MGS-6-PROMOTED` | Accepted to a memory class. |
| `MGS-7-DISCARDED` | Discarded. |
| `MGS-8-QUARANTINED` | Quarantined. |
| `MGS-9-REJECTED` | Rejected/prohibited. |
| `MGS-10-CORRECTED` | Correction appended. |
| `MGS-11-DECAYED` | Decayed or expired. |

### 10.4 Memory poisoning classes `MP-*`

| Class | Meaning |
|---|---|
| `MP-0` | No poisoning signal. |
| `MP-1` | Mark uncertainty. |
| `MP-2` | Hold for review. |
| `MP-3` | Quarantine proposal. |
| `MP-4` | Quarantine output and lower trust. |
| `MP-5` | Revoke agent or incident review. |

### 10.5 Memory rollback classes `MRB-*`

| Class | Meaning |
|---|---|
| `MRB-0` | Discard unpromoted proposal. |
| `MRB-1` | Mark operational note stale. |
| `MRB-2` | Demote reviewed memory to candidate. |
| `MRB-3` | Quarantine promoted memory. |
| `MRB-4` | Supersede with correction. |
| `MRB-5` | Revoke defensive immunity update. |
| `MRB-6` | Core review / human gate required. |

---

## 11. Rollback and freeze terms

### 11.1 Interruption states `RF-*`

| State | Meaning |
|---|---|
| `RF-0-NONE` | No interruption. |
| `RF-1-HOLD` | Pause until review. |
| `RF-2-FREEZE` | Stop mutation of affected path. |
| `RF-3-QUARANTINE` | Isolate output/agent/artifact. |
| `RF-4-REVOKE` | Remove permission/access. |
| `RF-5-ROLLBACK` | Revert scoped state. |
| `RF-6-RECOVER` | Restore from known-good state. |
| `RF-7-ESCALATE` | Route to `c`, human, legal, or security review. |
| `RF-X-REDLINE` | Prohibited behavior; deny/quarantine/revoke. |

### 11.2 Freeze surfaces `FS-*`

| Surface | Meaning |
|---|---|
| `FS-AGENT` | Agent process or connector. |
| `FS-TASK` | Task contract. |
| `FS-PERMISSION` | Permission grant. |
| `FS-SANDBOX` | Sandbox/worktree/container. |
| `FS-BRANCH` | Branch or worktree. |
| `FS-OUTPUT` | Agent output/artifact. |
| `FS-MEMORY-PROPOSAL` | Memory gate candidate. |
| `FS-MEMORY-CLASS` | Class of memory records. |
| `FS-WITNESS-CHAIN` | Witness chain or event family. |
| `FS-RELEASE` | Release/publication surface. |
| `FS-CONFIG` | Configuration or CI/service config. |
| `FS-SECRET` | Secret/token/key access path. |
| `FS-INCIDENT` | Incident handling flow. |
| `FS-CORE` | Identity/privilege/continuity core. |
| `FS-CLOUD-DATA` | Cloud data transmission. |

### 11.3 Rollback classes `RB-*`

| Class | Meaning |
|---|---|
| `RB-0` | No rollback needed. |
| `RB-1` | Discard sandbox. |
| `RB-2` | Revert patch. |
| `RB-3` | Reset worktree. |
| `RB-4` | Restore backup. |
| `RB-5` | Supersede memory. |
| `RB-6` | Revoke permission. |
| `RB-7` | Release rollback. |
| `RB-8` | Incident recovery. |
| `RB-9` | Core recovery. |
| `RB-X` | No safe rollback; escalate before action. |

### 11.4 Recovery point classes `RP-*`

| Class | Meaning |
|---|---|
| `RP-COMMIT` | Version-control commit hash. |
| `RP-SNAPSHOT` | Filesystem or VM snapshot. |
| `RP-MANIFEST` | File/hash manifest. |
| `RP-BACKUP` | Backup reference. |
| `RP-WITNESS` | Witness chain or event hash. |
| `RP-MEMORY` | Memory gate checkpoint. |
| `RP-CONFIG` | Configuration baseline. |
| `RP-RELEASE` | Release artifact set. |
| `RP-ENV` | Environment fingerprint. |
| `RP-UNKNOWN` | No reliable recovery point. |

### 11.5 Quarantine states `Q-*`

| State | Meaning |
|---|---|
| `Q-0` | Not quarantined. |
| `Q-1` | Soft hold; do not integrate. |
| `Q-2` | Isolated; review required. |
| `Q-3` | Restricted; high-risk reviewer required. |
| `Q-4` | Incident quarantine. |
| `Q-5` | Legal/security hold. |
| `Q-X` | Prohibited; reject and revoke path. |

### 11.6 Revocation classes `RV-*`

| Class | Meaning |
|---|---|
| `RV-0` | No revocation. |
| `RV-1` | Revoke task grant. |
| `RV-2` | Lower auto-connect ceiling. |
| `RV-3` | Lower trust level. |
| `RV-4` | Suspend agent. |
| `RV-5` | Revoke agent registration. |
| `RV-6` | Revoke connector/token in owned system. |
| `RV-7` | Revoke tool/dependency. |
| `RV-X` | Permanent denial / red-line. |

### 11.7 Re-entry outcomes `RE-*`

| Outcome | Meaning |
|---|---|
| `RE-ALLOW` | Return to normal operation. |
| `RE-LIMIT` | Return with reduced scope/trust. |
| `RE-REHANDSHAKE` | Require agent re-handshake. |
| `RE-RECONTRACT` | Require new task contract. |
| `RE-REVIEW` | Remain under review. |
| `RE-QUARANTINE` | Continue quarantine. |
| `RE-REVOKE` | Revoke agent/permission/task. |
| `RE-LEGAL` | Route to legal/security review. |

---

## 12. Quorum and review terms

### 12.1 Quorum roles `QROLE-*`

| Role | Meaning |
|---|---|
| `QROLE-EXECUTOR` | Applies patch/work in sandbox/worktree. |
| `QROLE-TESTER` | Runs tests/validation. |
| `QROLE-SEMANTIC` | Reviews meaning/architecture. |
| `QROLE-AUDITOR` | Checks scope/risk/permission/witness. |
| `QROLE-ARCHIVIST` | Checks metadata/hash/release hygiene. |
| `QROLE-SENTINEL` | Detects drift/anomaly. |
| `QROLE-JUDGE-ASSISTANT` | Compares signals and options. |
| `QROLE-C-GATE` | `c` final integration gate. |
| `QROLE-HUMAN-GATE` | Human anchor high-risk gate. |

### 12.2 Review dimensions `RD-*`

| Dimension | Meaning |
|---|---|
| `RD-SCOPE` | Task scope check. |
| `RD-PERMISSION` | Permission use check. |
| `RD-DATA` | Data boundary check. |
| `RD-SECURITY` | Security risk check. |
| `RD-LEGAL` | Legal/jurisdictional concern. |
| `RD-SEMANTIC` | Meaning/architecture consistency. |
| `RD-ARCHITECTURE` | Corpus architecture fit. |
| `RD-TEST` | Test/build/schema validation. |
| `RD-WITNESS` | Witness presence and adequacy. |
| `RD-ROLLBACK` | Rollback/correction path. |
| `RD-MEMORY` | Memory promotion appropriateness. |
| `RD-RELEASE` | Public/release safety. |
| `RD-CLOUD` | Cloud data exposure. |
| `RD-CORE` | Identity/continuity/permission/memory core impact. |
| `RD-REDLINE` | Red-line proximity. |

### 12.3 Consensus strength `CS-*`

| Level | Meaning |
|---|---|
| `CS-0` | No consensus. |
| `CS-1` | Weak agreement. |
| `CS-2` | Moderate agreement. |
| `CS-3` | Strong independent agreement. |
| `CS-4` | Strong agreement plus tests and witness. |
| `CS-X` | False or unsafe consensus. |

### 12.4 Same-source risk `SSR-*`

| Level | Meaning |
|---|---|
| `SSR-0` | Independent sources and methods. |
| `SSR-1` | Minor overlap. |
| `SSR-2` | Shared input or prompt frame. |
| `SSR-3` | Same provider/model family or stale state. |
| `SSR-4` | Circular review / laundering. |
| `SSR-X` | Fabricated or unsafe consensus. |

### 12.5 Disagreement taxonomy `DQ-*`

| Type | Meaning |
|---|---|
| `DQ-NONE` | No material disagreement. |
| `DQ-FACT` | Factual disagreement. |
| `DQ-SCOPE` | Scope disagreement. |
| `DQ-PERMISSION` | Permission disagreement. |
| `DQ-TEST` | Test disagreement. |
| `DQ-SEMANTIC` | Meaning/architecture disagreement. |
| `DQ-RISK` | Risk classification disagreement. |
| `DQ-LEGAL` | Legal/jurisdictional concern. |
| `DQ-MEMORY` | Memory promotion disagreement. |
| `DQ-CORE` | Identity/continuity/privilege concern. |
| `DQ-INCIDENT` | Incident interpretation disagreement. |
| `DQ-REDLINE` | Prohibited action concern. |
| `DQ-UNKNOWN` | Unclear disagreement. |

### 12.6 Review decisions `QRD-*`

| Decision | Meaning |
|---|---|
| `QRD-ACCEPT` | Accept output as proposed. |
| `QRD-ACCEPT-WITH-LIMITS` | Accept bounded subset. |
| `QRD-REVISE` | Return for revision. |
| `QRD-REJECT` | Reject output. |
| `QRD-HOLD` | Pause pending clarification. |
| `QRD-QUARANTINE` | Isolate output/agent/task. |
| `QRD-ROLLBACK` | Rollback applied or recommended. |
| `QRD-REHANDSHAKE` | Agent requires re-handshake. |
| `QRD-RECONTRACT` | Task requires new contract. |
| `QRD-C-GATE` | Send to `c` gate. |
| `QRD-HUMAN-GATE` | Human anchor required. |
| `QRD-LEGAL-REVIEW` | Legal/counsel route required. |
| `QRD-INCIDENT-REVIEW` | Incident/security route required. |
| `QRD-DENY-REDLINE` | Deny due to red line. |

---

## 13. Executor / reviewer separation terms

### 13.1 Separation levels `SL-*`

| Level | Meaning |
|---|---|
| `SL-0` | No separation; non-conformant for material tasks. |
| `SL-1` | Self-report only; R0 only. |
| `SL-2` | Separate review pass by same provider/context. |
| `SL-3` | Separate agent or runtime reviewer. |
| `SL-4` | Executor + tester + semantic/audit reviewer. |
| `SL-5` | Multi-role quorum + `c` gate + human gate where needed. |
| `SL-X` | Invalid / self-approval / circular review. |

### 13.2 Review sufficiency `RS-*`

| Level | Meaning |
|---|---|
| `RS-0` | No review. |
| `RS-1` | Executor self-report only. |
| `RS-2` | Superficial review. |
| `RS-3` | Scoped independent review. |
| `RS-4` | Multi-dimensional review. |
| `RS-5` | High-assurance review with gates/witness. |
| `RS-X` | False review / self-approval. |

### 13.3 Self-approval severity `SA-*`

| Level | Meaning |
|---|---|
| `SA-0` | No self-approval. |
| `SA-1` | Weak self-certifying language. |
| `SA-2` | Executor recommendation treated as review. |
| `SA-3` | Executor sole reviewer for material output. |
| `SA-4` | Executor approves release/memory/core. |
| `SA-X` | Executor self-authorizes prohibited action. |

### 13.4 Circular review risk `CR-*`

| Level | Meaning |
|---|---|
| `CR-0` | No circularity. |
| `CR-1` | Mild overlap. |
| `CR-2` | Shared context/source. |
| `CR-3` | No independent artifact inspection. |
| `CR-4` | Circular review used for approval. |
| `CR-X` | Circular review hides red-line issue. |

---

## 14. Defensive emulation terms

### 14.1 Defensive emulation boundary classes `DEB-*`

| Class | Meaning |
|---|---|
| `DEB-0` | No emulation; detection/quarantine only. |
| `DEB-1` | Classification only. |
| `DEB-2` | Synthetic fixture. |
| `DEB-3` | Sandbox replay. |
| `DEB-4` | Mirror simulation inside clean-room. |
| `DEB-5` | Immunity proposal. |
| `DEB-6` | Controlled defensive apply. |
| `DEB-X` | Prohibited external action. |

### 14.2 Defensive emulation risk `DER-*`

| Risk | Meaning |
|---|---|
| `DER-0` | Benign false alarm. |
| `DER-1` | Suspicious but low impact. |
| `DER-2` | Likely manipulation attempt. |
| `DER-3` | Memory/permission risk. |
| `DER-4` | Incident-sensitive or core-adjacent risk. |
| `DER-5` | Red-line-adjacent. |
| `DER-X` | Prohibited offensive/retaliatory content. |

### 14.3 Allowed defensive activities `DA-*`

`DA-*` labels allowed defensive actions such as classify suspicious input, quarantine output, create synthetic fixture, replay in sandbox, extract defensive signature, update denied pattern list, block owned channel, or run defensive conformance test.

### 14.4 Prohibited activities `PA-*`

`PA-*` labels prohibited actions such as hack-back, live counter-operation, malware deployment, credential theft, covert persistence, evasion, unauthorized scanning, live external exploitation, destructive payloads, botnet-like orchestration, secret exfiltration, autonomous retaliation, or live mirror deployment.

### 14.5 Special defensive terms

| Term | Definition |
|---|---|
| Containment garage | Isolated environment for suspicious material. |
| Canary response | Low-value, bounded, non-harmful signal used to detect channel behavior. |
| Mirror simulation | Sandboxed model of hostile behavior used only to test internal defenses. |
| Defensive signature | Minimized pattern used to detect future hostile signals. |
| Defensive immunity update | Bounded update to filters, gates, quarantine triggers, trust decay, or review requirements. |
| Garage residue | Intermediate material from containment that must not enter memory or release without gate. |

---

## 15. Incident response terms

### 15.1 Incident classes `IR-C-*`

| Class | Meaning |
|---|---|
| `IR-C-AGENT` | Agent behavior incident. |
| `IR-C-PERMISSION` | Permission incident. |
| `IR-C-SANDBOX` | Sandbox/worktree incident. |
| `IR-C-MEMORY` | Memory incident. |
| `IR-C-CLOUD-DATA` | Cloud data incident. |
| `IR-C-SECRET` | Secret incident. |
| `IR-C-TOOLCHAIN` | Tool-chain incident. |
| `IR-C-WITNESS` | Witness incident. |
| `IR-C-RELEASE` | Release/public incident. |
| `IR-C-CORE` | Core authority incident. |
| `IR-C-INCIDENT-PROCESS` | Incident-process failure. |
| `IR-C-EXTERNAL` | External hostile signal. |
| `IR-C-UNKNOWN` | Unknown incident. |
| `IR-C-REDLINE` | Prohibited behavior attempted/requested. |

### 15.2 Incident severity `IR-S*`

| Severity | Meaning |
|---|---|
| `IR-S0` | Informational. |
| `IR-S1` | Low. |
| `IR-S2` | Moderate. |
| `IR-S3` | High. |
| `IR-S4` | Critical. |
| `IR-S5` | Legal/security-sensitive. |
| `IR-SX` | Red-line/prohibited. |

### 15.3 Incident lifecycle states `IR-L*`

| State | Meaning |
|---|---|
| `IR-L0-DETECTED` | Incident signal detected. |
| `IR-L1-TRIAGED` | Class/severity/scope assigned. |
| `IR-L2-HELD` | Task/path held. |
| `IR-L3-FROZEN` | Affected surface frozen. |
| `IR-L4-PRESERVED` | Minimal evidence preserved. |
| `IR-L5-CONTAINED` | Local containment applied. |
| `IR-L6-REPAIRING` | Repair developed in sandbox. |
| `IR-L7-VALIDATED` | Repair/recovery validated. |
| `IR-L8-APPLIED` | Controlled apply completed. |
| `IR-L9-REPORTED` | Report prepared or sent where needed. |
| `IR-L10-MEMORY-GATED` | Incident learning processed through memory gate. |
| `IR-L11-CLOSED` | Closed with outcome. |
| `IR-LQ-QUARANTINED` | Incident material remains quarantined. |
| `IR-LX-REDLINE` | Prohibited boundary detected. |

---

## 16. Secrets and cloud data terms

### 16.1 Data classes `DC-*`

| Class | Meaning |
|---|---|
| `DC-0` | Public data. |
| `DC-1` | Internal project data. |
| `DC-2` | Private data. |
| `DC-3` | Restricted data. |
| `DC-4` | Secret-bearing data. |
| `DC-5` | Legal-sensitive data. |
| `DC-6` | Incident-sensitive data. |
| `DC-7` | Sealed material. |
| `DC-8` | Memory-core data. |
| `DC-9` | Child/third-party sensitive data. |
| `DC-X` | Unknown data; deny until classified. |

### 16.2 Secret classes `SC-*`

| Class | Meaning |
|---|---|
| `SC-0` | No secret. |
| `SC-1` | Low-sensitivity token reference. |
| `SC-2` | API key / token. |
| `SC-3` | Private key / signing material. |
| `SC-4` | Recovery credential. |
| `SC-5` | Session credential. |
| `SC-6` | Production credential. |
| `SC-7` | Identity credential. |
| `SC-X` | Unknown secret risk. |

### 16.3 Context classes `CTX-*`

| Context | Meaning |
|---|---|
| `CTX-LOCAL` | Local controlled machine/service. |
| `CTX-LOCAL-CONTAINER` | Local container/VM sandbox. |
| `CTX-CLOUD-CLI` | Cloud CLI context. |
| `CTX-CLOUD-API` | Provider API/model context. |
| `CTX-HYBRID` | Local + cloud path; cloud-risk by default. |
| `CTX-PUBLIC-REPO` | Public repository. |
| `CTX-PRIVATE-REPO` | Private repository. |
| `CTX-LEGAL` | Legal/counsel context. |
| `CTX-INCIDENT` | Incident response context. |
| `CTX-MEMORY` | `c` memory context. |
| `CTX-UNKNOWN` | Unknown processing context; deny. |

### 16.4 Exception classes `EX-*`

| Exception | Meaning |
|---|---|
| `EX-0` | No exception. |
| `EX-1` | Internal-to-cloud minimal context. |
| `EX-2` | Private safe summary to cloud. |
| `EX-3` | Legal-sensitive safe summary. |
| `EX-4` | Incident redacted packet. |
| `EX-5` | Secret reference only. |
| `EX-X` | Raw prohibited material; invalid by default. |

### 16.5 Output sanitization outcomes `OS-*`

| Outcome | Meaning |
|---|---|
| `OS-ACCEPT` | Safe as-is. |
| `OS-REDACT` | Redact before use. |
| `OS-SUMMARIZE` | Convert to safe summary. |
| `OS-REFERENCE` | Replace raw content with refs/hashes. |
| `OS-QUARANTINE` | Isolate pending review. |
| `OS-REJECT` | Reject output. |
| `OS-INCIDENT` | Open incident response. |

### 16.6 Data retention classes `DR-*`

| Class | Meaning |
|---|---|
| `DR-EPHEMERAL` | Discard after task/session. |
| `DR-OPERATIONAL` | Retain for project operation. |
| `DR-AUDIT` | Retain for governance/witness/review. |
| `DR-INCIDENT` | Retain for incident lifecycle. |
| `DR-LEGAL-HOLD` | Retain under legal/counsel need. |
| `DR-MEMORY-GATE` | Retain as memory decision reference. |
| `DR-CORE` | Retain for core authority transitions. |

---

## 17. Conformance terms

### 17.1 Evidence classes `EV-*`

| Evidence | Meaning |
|---|---|
| `EV-DECL` | Declaration only. |
| `EV-CONFIG` | Configuration or policy file. |
| `EV-CONTRACT` | Task contract. |
| `EV-PERMISSION` | Permission grant. |
| `EV-HANDSHAKE` | Handshake/registration. |
| `EV-SANDBOX` | Sandbox/worktree run. |
| `EV-TEST` | Test/validation report. |
| `EV-WITNESS` | Witness event/chain. |
| `EV-REVIEW` | Independent review. |
| `EV-MEMORY-GATE` | Memory gate record. |
| `EV-ROLLBACK` | Rollback/freeze record. |
| `EV-INCIDENT` | Incident record. |
| `EV-CLOUD-DATA` | Data classification/cloud context record. |
| `EV-DRILL` | Controlled drill. |
| `EV-AUDIT` | Independent audit artifact. |

### 17.2 Test suites `CTS-*`

| Suite | Meaning |
|---|---|
| `CTS-ROOT` | Root doctrine and anti-washing. |
| `CTS-CATC` | Task contract tests. |
| `CTS-CAPM` | Permission/capability tests. |
| `CTS-HSP` | Handshake/admission tests. |
| `CTS-SWP` | Sandbox/worktree tests. |
| `CTS-WEP` | Witness event tests. |
| `CTS-MGP` | Memory gate tests. |
| `CTS-RFP` | Rollback/freeze tests. |
| `CTS-QRP` | Quorum/review tests. |
| `CTS-ERS` | Executor/reviewer separation tests. |
| `CTS-DEB` | Defensive emulation boundary tests. |
| `CTS-IRP` | Incident response tests. |
| `CTS-SCDP` | Secrets/cloud data tests. |
| `CTS-RED` | Red-line tests. |

### 17.3 Anti-washing

| Term | Definition |
|---|---|
| CGAM-washing | Claiming `c`-governed CLI-agent safety without operational evidence. |
| Anti-washing test | Scenario proving that a claimed boundary actually blocks unsafe behavior. |
| Red-line test | Test that checks prohibited actions cannot be authorized or normalized. |
| Evidence packet | Bundle of refs/hashes/records supporting a test result. |
| Conformance result | Structured outcome of a test run or suite. |
| Effective level | Level actually supported by evidence, which may be lower than claimed level. |

---

## 18. Red-line vocabulary

The following terms indicate prohibited or red-line-adjacent behavior.

| Term | Meaning |
|---|---|
| Hack-back | Unauthorized action against a suspected external source. Prohibited. |
| Live counter-operation | Any action that affects a live external system/source. Prohibited unless it is ordinary lawful blocking/reporting within owned scope. |
| Malware behavior | Persistence, evasion, unauthorized control, destructive payload, credential theft, propagation, or command-and-control behavior. Prohibited. |
| Credential theft | Capturing, extracting, exporting, or misusing credentials. Prohibited. |
| Covert persistence | Hidden continued access or operation. Prohibited. |
| Evasion | Avoiding detection or safeguards in unauthorized systems. Prohibited. |
| Unauthorized scanning | Probing systems without authorization. Prohibited. |
| Direct memory write | Agent writes directly into `c` memory. Prohibited. |
| Direct core mutation | Agent modifies identity, witness, permission, continuity, or memory core directly. Prohibited. |
| Self-approval | Executor approves its own material output. Prohibited for material tasks. |
| Witness tampering | Silent edit/delete/manipulation of witness records. Prohibited. |
| Secret exfiltration | Moving secrets outside authorized boundary. Prohibited. |
| Retaliatory immunity | Defensive update that attacks or affects external source. Prohibited. |
| Consensus laundering | Using multiple weak or correlated agent outputs to make unsafe decision look legitimate. Prohibited. |

---

## 19. Object family registry

| Object family | Primary profile |
|---|---|
| `CLI_AGENT_TASK_CONTRACT` | CATC |
| `CLI_AGENT_CAPABILITY_PROFILE` | CAPM |
| `CLI_AGENT_PERMISSION_GRANT` | CAPM |
| `CLI_AGENT_PERMISSION_EVENT` | CAPM |
| `CLI_AGENT_HANDSHAKE` | HSP |
| `CLI_AGENT_REGISTRATION` | HSP |
| `CLI_AGENT_ADMISSION_EVENT` | HSP |
| `CLI_AGENT_SANDBOX_PROFILE` | SWP |
| `CLI_AGENT_WORKTREE_RUN` | SWP |
| `CLI_AGENT_ROLLBACK_PLAN` | SWP |
| `CLI_AGENT_WITNESS_EVENT` | WEP |
| `CLI_AGENT_WITNESS_CHAIN` | WEP |
| `CLI_AGENT_WITNESS_REFERENCE` | WEP |
| `CLI_AGENT_MEMORY_PROPOSAL` | MGP |
| `CLI_AGENT_MEMORY_GATE_RECORD` | MGP |
| `CLI_AGENT_IMMUNITY_UPDATE_RECORD` | MGP |
| `CLI_AGENT_FREEZE_RECORD` | RFP |
| `CLI_AGENT_ROLLBACK_RECORD` | RFP |
| `CLI_AGENT_RECOVERY_POINT` | RFP |
| `CLI_AGENT_REVOCATION_RECORD` | RFP |
| `CLI_AGENT_QUARANTINE_RECORD` | RFP |
| `CLI_AGENT_QUORUM_RECORD` | QRP |
| `CLI_AGENT_REVIEW_RECORD` | QRP |
| `CLI_AGENT_DISAGREEMENT_RECORD` | QRP |
| `CLI_AGENT_CONSENSUS_LIMIT_RECORD` | QRP |
| `CLI_AGENT_ROLE_SEPARATION_RECORD` | ERS |
| `CLI_AGENT_REVIEW_ASSIGNMENT` | ERS |
| `CLI_AGENT_SELF_APPROVAL_EVENT` | ERS |
| `CLI_AGENT_ROLE_CONFLICT_RECORD` | ERS |
| `CLI_AGENT_DEFENSIVE_EMULATION_CASE` | DEB |
| `CLI_AGENT_CONTAINMENT_GARAGE_RECORD` | DEB |
| `CLI_AGENT_CANARY_RESPONSE_RECORD` | DEB |
| `CLI_AGENT_MIRROR_SIMULATION_RECORD` | DEB |
| `CLI_AGENT_DEFENSIVE_IMMUNITY_CANDIDATE` | DEB |
| `CLI_AGENT_INCIDENT_RECORD` | IRP |
| `CLI_AGENT_INCIDENT_TRIAGE_RECORD` | IRP |
| `CLI_AGENT_INCIDENT_PRESERVATION_RECORD` | IRP |
| `CLI_AGENT_INCIDENT_CONTAINMENT_RECORD` | IRP |
| `CLI_AGENT_INCIDENT_REPAIR_RECORD` | IRP |
| `CLI_AGENT_INCIDENT_REPORT_PACKET` | IRP |
| `CLI_AGENT_DATA_CLASSIFICATION_RECORD` | SCDP |
| `CLI_AGENT_CLOUD_CONTEXT_RECORD` | SCDP |
| `CLI_AGENT_REDACTION_RECORD` | SCDP |
| `CLI_AGENT_SECRET_BOUNDARY_RECORD` | SCDP |
| `CLI_AGENT_CLOUD_EXPOSURE_EVENT` | SCDP |
| `CLI_AGENT_PROVIDER_BOUNDARY_RECORD` | SCDP |
| `CLI_AGENT_CONFORMANCE_RESULT` | CTM |
| `CLI_AGENT_TEST_CASE` | CTM |
| `CLI_AGENT_TEST_RUN` | CTM |
| `CLI_AGENT_EVIDENCE_PACKET` | CTM |
| `CLI_AGENT_RED_LINE_FAILURE_RECORD` | CTM |

---

## 20. Disambiguation notes

### 20.1 `R4` vs `RB-4` vs `IR-S4`

| Label | Meaning |
|---|---|
| `R4` | Task risk class: memory/core/privilege/continuity impact. |
| `RB-4` | Rollback class: restore backup. |
| `IR-S4` | Incident severity: critical. |

These are unrelated class families.

### 20.2 `MG-5` vs `CGAM-5` vs `DEB-P5`

| Label | Meaning |
|---|---|
| `MG-5` | Memory gate class: defensive immunity update. |
| `CGAM-5` | Global high-assurance mesh conformance. |
| `DEB-P5` | High-assurance defensive emulation conformance. |

### 20.3 `WE-X`, `CGAM-X`, `RX`, `DEB-X`, `IR-SX`

All `X` labels indicate prohibited, revoked, red-line, or non-conformant state within their own family.

They are not identical but all require fail-closed handling.

### 20.4 “Cloud” vs “Provider”

`Cloud` refers to where data/process leaves local control.

`Provider` refers to the organization or service boundary.

A local provider tool may still run locally. A provider-branded CLI may still expose cloud context. Classify the actual data route.

### 20.5 “Review” vs “Approval”

Review examines.

Approval authorizes.

An agent may review without approving.

The executor may explain its work, but that is not approval.

### 20.6 “Quarantine” vs “Delete”

Quarantine isolates.

Delete removes.

Suspicious material should usually be quarantined before deletion unless immediate safety requires removal.

### 20.7 “Rollback” vs “Erase”

Rollback restores a state or supersedes a faulty memory.

It must not erase witness records to hide what occurred.

### 20.8 “Immunity” vs “Retaliation”

Immunity blocks, flags, slows, quarantines, or requires review inside owned systems.

Retaliation acts against external sources.

Immunity is allowed under gate.

Retaliation is prohibited.

---

## 21. Standard short formulations

Use these formulations for consistency.

```text
CLI agents are hands, not will.
```

```text
Capability is not permission.
```

```text
Registration is not task authorization.
```

```text
Quorum is evidence, not sovereignty.
```

```text
Witness the boundary, not the whole life.
```

```text
Memory is not a log sink.
```

```text
Experience is not a diff.
```

```text
Immunity is not retaliation.
```

```text
Defend the house. Do not raid the street.
```

```text
If the task cannot be scoped, it cannot be delegated.
```

```text
If the agent does not need the raw material, do not give it the raw material.
```

```text
Do not claim what you cannot test.
```

---

## 22. Open terminology issues

| ID | Issue | Required action |
|---|---|---|
| `GT-001` | Some retention families use `WR`, `DR`, `RET` across profiles | Harmonize or explicitly keep profile-local. |
| `GT-002` | Some profiles use similar quarantine classes | Decide whether to centralize quarantine vocabulary. |
| `GT-003` | Provider-specific terms for Codex/Gemini/local checker need future profiles | Add provider companion glossaries if needed. |
| `GT-004` | `Oracle`, `Judge`, `Judge-assistant`, and `quorum` need cross-corpus alignment | Review against parent corpus. |
| `GT-005` | Public vs restricted terminology for defensive emulation | Redaction profile required. |
| `GT-006` | Legal/counsel route terms need legal handoff profile | Add future document. |
| `GT-007` | `c` memory vs operational note vs experience artifact should be checked against broader memory corpus | Cross-review with Memory Gate and parent memory docs. |
| `GT-008` | Need final JSON schema naming convention | Coordinate with schema extraction plan. |

---

## 23. Closing rule

This glossary is not cosmetic.

It is a control surface.

Final rule:

```text
When terms blur,
authority leaks.

When authority leaks,
agents stop being workers.
```

