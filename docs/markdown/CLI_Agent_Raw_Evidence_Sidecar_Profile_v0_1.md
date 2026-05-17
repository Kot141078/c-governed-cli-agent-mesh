# CLI Agent Raw Evidence Sidecar Profile v0.1

## Restricted raw-evidence custody, sidecar references, evidence packets, witness linkage, L4W envelopes, memory-gate exclusion, and public-disclosure boundaries for C-Governed CLI Agent Mesh operations

**Status:** Draft normative profile v0.1  
**Date:** 2026-05-17  
**Package:** C-Governed CLI Agent Mesh  
**Layer:** `c = a + b` / Agent Governance / Evidence Custody / Witness / Incident Response / Memory Gate / Public Redaction / L4W  
**Document class:** raw-evidence sidecar profile / evidence-custody profile / restricted technical control artifact  
**Assertion class:** `C-A10` control-layer artifact; `C-A7` where hash, signature, canonicalization, chain continuity, or verification claims are made  
**Distribution default:** restricted technical / safety review; public release should use redacted summary form only  

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
- `CLI_Agent_Executor_Reviewer_Separation_v0_1.md`
- `CLI_Agent_Defensive_Emulation_Boundaries_v0_1.md`
- `CLI_Agent_Incident_Response_Profile_v0_1.md`
- `CLI_Agent_Secrets_and_Cloud_Data_Policy_v0_1.md`
- `CLI_Agent_Public_Redaction_Profile_v0_1.md`
- `CLI_Agent_Conformance_Fixture_Pack_v0_1.md`
- `CLI_Agent_Release_and_Implementation_Readiness_Gate_v0_1.md`

**Implementation substrate references:**
- `docs/iter49_clear_requires_evidence_packet.md`
- `docs/iter50_integrity_stack.md`
- `docs/iter51_l4w_envelope.md`
- `docs/iter52_l4w_conformance_and_audit_cli.md`
- `modules/runtime/*quarantine*` where present
- `modules/synaps/*` where Codex handoff, package ledger, and quarantined transfer behavior are implemented

**Primary object family:**
- `CLI_AGENT_RAW_EVIDENCE_SIDECAR`
- `CLI_AGENT_EVIDENCE_PACKET_REF`
- `CLI_AGENT_RAW_ARTIFACT_REF`
- `CLI_AGENT_EVIDENCE_CUSTODY_RECORD`
- `CLI_AGENT_DISCLOSURE_POLICY_RECORD`
- `CLI_AGENT_EVIDENCE_ACCESS_EVENT`
- `CLI_AGENT_EVIDENCE_RETENTION_RECORD`
- `CLI_AGENT_EVIDENCE_DESTRUCTION_RECORD`

**Canonical schema version:** `cli-agent-raw-evidence-sidecar-0.1`  
**Primary subject:** persistent `c` entities using local, cloud, or hybrid CLI agents as bounded executable workers  
**Primary boundary:** raw evidence may be preserved under restricted custody for review, incident response, audit, rollback, legal handoff, or L4W verification. It must not become witness payload, memory payload, public release material, cloud prompt material, agent training material, or unrestricted operational context by default.

---

## 0. Executive definition

**CLI Agent Raw Evidence Sidecar Profile** defines how raw, sensitive, bulky, privileged, private, incident-related, or operationally risky evidence is preserved without contaminating the witness log, memory gate, public release surface, or cloud context.

The sidecar answers:

```text
What raw artifact exists?
Where is it held?
Who may inspect it?
Which task, incident, witness event, or quarantine state produced it?
Which hash proves identity?
Which evidence packet summarizes it?
Which L4W envelope seals the decision path?
Which parts may be disclosed?
Which parts must remain restricted?
When must it expire, remain on hold, or be destroyed?
```

Compact formula:

```text
Preserve enough to prove.
Expose only enough to review.
Remember only what passed the gate.
Publish only what survives redaction.
```

The sidecar does not decide truth alone.

It protects custody, linkage, and disclosure boundaries.

---

## 1. Purpose

CLI agents can produce or encounter material that is important but unsafe to place directly into ordinary logs, prompts, memory, or public documents.

Examples include:

```text
raw logs
raw diffs
crash traces
quarantine artifacts
incident bundles
secrets-containing files
credential-adjacent material
private memory excerpts
legal-sensitive material
third-party data
child-sensitive material
cloud transcript fragments
prompt-injection payloads
suspicious tool output
malformed package content
agent handoff payloads
repository state snapshots
pre-repair evidence
```

The system needs such material for:

1. preservation before repair;
2. incident triage;
3. rollback and freeze decisions;
4. quarantine clear decisions;
5. evidence packet construction;
6. L4W envelope verification;
7. lawful reporting or provider handoff;
8. conformance testing;
9. future defensive adaptation;
10. audit and dispute resolution.

But raw evidence is dangerous if copied everywhere.

This profile provides a strict sidecar model so raw evidence is held near the system of custody, while the main governance surfaces carry only bounded references, hashes, classifications, and redacted summaries.

---

## 2. Non-goals

This profile does not define or permit:

1. unrestricted raw-data logging;
2. raw memory export;
3. secrets in witness events;
4. secrets in task contracts;
5. secrets in public release notes;
6. cloud upload of raw evidence by default;
7. training on private raw evidence;
8. agent self-certification of evidence truth;
9. evidence destruction as redaction;
10. legal conclusions by an agent;
11. offensive cyber analysis beyond authorized defensive containment;
12. hack-back;
13. live external counter-operation;
14. credential extraction;
15. malware construction;
16. covert persistence;
17. evasion;
18. unauthorized scanning;
19. autonomous retaliation;
20. direct memory promotion from raw evidence;
21. public disclosure of live incident material without lawful review;
22. bypassing human anchor review for high-risk evidence.

A raw-evidence sidecar may preserve.

It may not launder raw material into authority.

---

## 3. Corpus bridge set

### 3.1 Explicit bridge: `c = a + b`

CLI agents, logs, files, quarantine records, evidence packets, witness events, signatures, schemas, validators, and sidecars belong to `b`: the technological substrate.

A sidecar protects `c` by preventing raw substrate material from silently becoming:

```text
memory
identity
experience
policy
release authority
incident authority
immune update
public doctrine
```

`c` may inspect, metabolize, reject, or summarize evidence through gates.

Raw evidence itself is not `c` memory.

### 3.2 Quiet bridge I: information theory

Raw evidence has high bandwidth and high leakage risk. A hash, custody record, witness reference, and redacted summary transmit less information but can be enough to verify continuity and review decisions. This profile separates full signal from minimum sufficient signal.

### 3.3 Quiet bridge II: engineering chain of custody

In engineering, a failed part may be sealed in a bag, tagged, hashed, photographed, and referenced in a report. The report does not need to include every contaminating particle. The sidecar is that sealed bag for CLI-agent evidence.

### 3.4 Quiet bridge III: anatomy / immune memory

An immune system does not keep the whole pathogen alive inside every cell. It keeps signatures, memory, and controlled samples under boundary conditions. Likewise, `c` may preserve a restricted raw artifact while promoting only a safe defensive signature or reviewed experience.

### 3.5 Earth paragraph

If a worker finds a burned cable in an electrical cabinet, you do not staple the whole burned cable to the daily site log. You bag it, label it, photograph it, record the circuit, preserve the breaker state, and let the report reference the bag. The sidecar is the bag; the witness event is the site log; the evidence packet is the inspection report; the memory gate is the decision whether this becomes a lesson for future work.

---

## 4. Core doctrine

### 4.1 Primary doctrine

```text
Raw evidence stays restricted.
Witness gets references.
Memory gets reviewed meaning.
Public release gets redacted doctrine.
Cloud gets nothing unless explicitly allowed.
```

### 4.2 Sidecar axioms

| ID | Axiom | Requirement |
|---|---|---|
| `RES-AX-01` | Custody before use | Raw evidence MUST have a custody record before review, memory, disclosure, or handoff. |
| `RES-AX-02` | Hash before trust | Raw evidence MUST be content-hashed before it is referenced as evidence. |
| `RES-AX-03` | Reference, do not embed | Witness events SHOULD reference raw evidence by sidecar id/hash, not embed raw content. |
| `RES-AX-04` | Restricted by default | Unknown evidence sensitivity MUST default to restricted. |
| `RES-AX-05` | No direct memory | Raw evidence MUST NOT become `c` memory without memory-gate review. |
| `RES-AX-06` | No public raw incidents | Raw incident material MUST NOT be public without redaction and lawful review. |
| `RES-AX-07` | Preservation before repair | Incident repair SHOULD preserve enough evidence before mutation. |
| `RES-AX-08` | Append, do not rewrite | Corrections SHOULD be new custody events, not silent edits. |
| `RES-AX-09` | Least disclosure | Every disclosure MUST state recipient, purpose, scope, and redaction class. |
| `RES-AX-10` | Sidecar is not authority | A sidecar proves custody and identity, not truth or final decision. |

---

## 5. Object distinction

This package must keep the following objects distinct.

| Object | Contains | Must not contain | Authority level |
|---|---|---|---|
| `raw evidence artifact` | Original or near-original restricted material | Public conclusions | Source material only |
| `raw evidence sidecar` | Custody metadata, hash, storage pointer, class, access policy | Full raw content where avoidable | Custody control |
| `evidence packet` | Bounded summary, findings, artifact refs, reviewer, decision context | Unbounded secrets/private material | Review support |
| `witness event` | Boundary transition, reason code, refs, hashes | Raw secrets, private memory, unredacted incident evidence | Audit transition record |
| `L4W envelope` | Signed/verifiable decision envelope, commitments, chain linkage | Full raw context by default | Tamper-evident proof wrapper |
| `memory proposal` | Proposed safe lesson/experience/policy update | Raw evidence dump | Memory-gate candidate |
| `public disclosure` | Redacted doctrine, safe summary, non-sensitive proof | Live incident data, secrets, garage contents | External communication |

Compact rule:

```text
Evidence may support memory.
Evidence is not memory.
Witness may reference evidence.
Witness is not raw evidence.
Disclosure may reveal selected claims.
Disclosure is not full custody.
```

---

## 6. Evidence classes

Evidence classes use prefix `EVR-*`.

| Class | Name | Description | Default handling |
|---|---|---|---|
| `EVR-0` | Synthetic fixture | Safe artificial test input | May be public if no unsafe detail. |
| `EVR-1` | Low-risk operational artifact | Ordinary non-sensitive logs/diffs | Internal by default; publish only if useful and clean. |
| `EVR-2` | Private operational evidence | Local paths, repo state, non-public config, work logs | Restricted technical. |
| `EVR-3` | Secret-adjacent evidence | May include token names, auth headers, key paths, secret context | Restricted; redact before any transfer. |
| `EVR-4` | Incident evidence | Suspected compromise, poisoning, drift, hostile artifact, safety incident | Incident restricted; preserve before repair. |
| `EVR-5` | Legal / privileged evidence | Counsel, legal dispute, regulated, employment, contractual, jurisdictional material | Legal hold / counsel route only. |
| `EVR-6` | Third-party sensitive evidence | Client, child, family, worker, patient, customer, non-consenting party material | Restricted by default; externalization blocked. |
| `EVR-X` | Prohibited custody | Material that must not be stored by this system | Reject, delete securely if lawful, or route to proper authority. |

### 6.1 Default class

If sensitivity cannot be determined:

```text
default = EVR-3 secret-adjacent evidence
```

Unknown evidence must not default to public.

---

## 7. Storage states

Raw evidence sidecar lifecycle states use prefix `RES-*`.

| State | Meaning |
|---|---|
| `RES-CANDIDATE` | Artifact detected but not yet accepted into custody. |
| `RES-HELD` | Artifact held under custody, not yet reviewed. |
| `RES-QUARANTINED` | Artifact isolated due to risk, uncertainty, or incident relevance. |
| `RES-INDEXED-METADATA` | Only metadata/hash/classification indexed. Raw content not indexed. |
| `RES-REVIEWABLE` | Authorized reviewer may inspect under access window. |
| `RES-PACKETIZED` | Evidence packet exists and references the artifact. |
| `RES-L4W-BOUND` | L4W envelope binds decision/evidence reference. |
| `RES-MEMORY-PROPOSED` | Safe summary or lesson proposed to memory gate. |
| `RES-MEMORY-REJECTED` | Memory gate rejected promotion; raw evidence remains governed separately. |
| `RES-MEMORY-PROMOTED-SUMMARY` | Only reviewed summary/signature promoted, not raw content. |
| `RES-REDACTED` | Redacted artifact or disclosure packet exists. |
| `RES-DISCLOSED-RESTRICTED` | Disclosed to restricted reviewer/provider/legal route. |
| `RES-PUBLIC-SUMMARY` | Public-safe summary exists; raw artifact remains restricted. |
| `RES-LEGAL-HOLD` | Retention controlled by legal/counsel/regulatory duty. |
| `RES-EXPIRED` | Retention window expired; destruction or archive decision pending. |
| `RES-DESTROYED` | Artifact destroyed with destruction record. |
| `RES-TOMBSTONED` | Pointer retained without content for audit continuity. |

### 7.1 Forbidden transitions

The following transitions are forbidden:

```text
RES-CANDIDATE -> public disclosure without custody
RES-HELD -> memory promoted raw
RES-QUARANTINED -> ordinary retrieval
RES-QUARANTINED -> release artifact
RES-QUARANTINED -> cloud prompt material
RES-PACKETIZED -> public raw evidence
RES-LEGAL-HOLD -> destroyed without authority
RES-DESTROYED -> reconstructed from public summary
```

### 7.2 Conditional transitions

The following transitions are conditional:

```text
RES-HELD -> RES-PACKETIZED
    requires evidence packet creation and reviewer binding.

RES-PACKETIZED -> RES-L4W-BOUND
    requires envelope/hash/signature/chain checks where applicable.

RES-L4W-BOUND -> RES-MEMORY-PROPOSED
    requires safe summary extraction and memory-gate proposal.

RES-MEMORY-PROPOSED -> RES-MEMORY-PROMOTED-SUMMARY
    requires memory gate approval.

RES-REDACTED -> RES-PUBLIC-SUMMARY
    requires public redaction profile pass.
```

---

## 8. Raw evidence sidecar minimum object

A sidecar record SHOULD be machine-readable.

Minimum object:

```yaml
schema: cli-agent-raw-evidence-sidecar-0.1
sidecar_id: res_20260517_000001
created_at: '2026-05-17T00:00:00Z'
created_by: c_or_operator_or_system_component
c_id: ester
human_anchor_required: true

source:
  source_type: cli_agent_output | incident | quarantine | task_run | file_intake | cloud_response | manual_upload | conformance_fixture
  task_contract_id: catc_...
  agent_id: codex_local_01
  incident_id: ir_...
  quarantine_event_id: dq_...
  witness_event_id: we_...

artifact:
  artifact_id: raw_...
  storage_class: local_restricted | encrypted_local | legal_hold | offline_bundle | quarantine_store
  path_ref: data/restricted/evidence/...
  content_sha256: '<64 lowercase hex>'
  size_bytes: 0
  media_type: application/json
  filename_original: optional_redacted_name
  filename_public: optional_safe_name

classification:
  evidence_class: EVR-3
  data_classes:
    - secret_adjacent
    - private_operational
  third_party_present: false
  legal_sensitive: false
  child_sensitive: false
  cloud_origin: false
  cloud_export_allowed: false
  public_release_allowed: false

custody:
  custody_state: RES-HELD
  retention_class: RET-RESTRICTED-90D
  legal_hold: false
  encryption_required: true
  access_policy_id: access_res_default
  reviewer_required: true
  human_anchor_required: true

links:
  evidence_packet_id: ''
  evidence_packet_sha256: ''
  l4w_envelope_id: ''
  l4w_envelope_hash: ''
  memory_proposal_id: ''
  public_disclosure_id: ''

summary:
  safe_summary: 'Short bounded summary without secrets.'
  reason_codes:
    - preserved_before_repair
  uncertainty: medium

status:
  current_state: RES-HELD
  last_event_id: res_event_...
  problems: []
```

### 8.1 Required fields

Required fields:

```text
schema
sidecar_id
created_at
source.source_type
artifact.storage_class
artifact.content_sha256
classification.evidence_class
custody.custody_state
custody.retention_class
status.current_state
```

### 8.2 Prohibited fields

Sidecar metadata MUST NOT include:

```text
raw secret values
full private memory text
full legal privileged content
full incident payload by default
credential contents
private keys
bearer tokens
auth headers
cloud session cookies
unredacted child data
unredacted third-party data
live target details
exploit steps
malware logic
```

If a restricted path or filename itself leaks sensitive data, the sidecar MUST use a safe path reference or hashed alias.

---

## 9. Custody events

Sidecar state changes SHOULD be append-only events.

Object family: `CLI_AGENT_EVIDENCE_ACCESS_EVENT`, `CLI_AGENT_EVIDENCE_CUSTODY_RECORD`.

Minimum event:

```yaml
schema: cli-agent-evidence-custody-event-0.1
event_id: res_event_20260517_000001
ts: '2026-05-17T00:00:00Z'
sidecar_id: res_20260517_000001
event_type: created | classified | accessed | packetized | l4w_bound | redacted | disclosed | memory_proposed | memory_rejected | memory_promoted_summary | retained | expired | destroyed | tombstoned
actor: c | human_anchor | reviewer | local_checker | codex_worker | legal_reviewer
reason_code: preserved_before_repair
previous_state: RES-CANDIDATE
next_state: RES-HELD
refs:
  task_contract_id: catc_...
  witness_event_id: we_...
  evidence_packet_id: evp_...
  l4w_envelope_id: l4w_...
content:
  raw_content_embedded: false
  content_sha256: '<64 lowercase hex>'
review:
  reviewer_required: true
  reviewer_id: ''
  review_window_id: ''
result:
  ok: true
  problems: []
```

### 9.1 Access event requirement

Every non-automated raw evidence inspection SHOULD create an access event.

Required access fields:

```text
who accessed
when
why
which sidecar
which fields or artifact class
whether raw content was opened
whether copy/export occurred
which review or legal route allowed it
```

### 9.2 Copy/export rule

Raw evidence copy/export is a privileged transition.

It requires:

```text
explicit purpose
recipient class
scope
redaction state
retention class
witness reference
human/legal gate where applicable
```

---

## 10. Relationship to witness events

Witness events SHOULD record boundary transitions and references.

They SHOULD NOT embed raw evidence.

A witness event may include:

```yaml
raw_evidence_ref:
  sidecar_id: res_...
  evidence_class: EVR-3
  content_sha256: '<64 lowercase hex>'
  custody_state: RES-HELD
  access_policy_id: access_res_default
  raw_content_in_witness: false
```

A witness event MUST NOT include:

```text
secret value
private raw memory
full legal text
raw child data
unredacted incident evidence
cloud credential material
exploit-like instructions
```

### 10.1 Missing sidecar behavior

If a witness event references raw evidence but no valid sidecar exists:

```text
status = fail_closed
reason = missing_raw_evidence_sidecar
allowed_next_action = create_sidecar_or_drop_raw_reference
```

### 10.2 Hash mismatch behavior

If sidecar hash and artifact hash do not match:

```text
status = fail_closed
reason = raw_evidence_hash_mismatch
allowed_next_action = preserve_mismatch_as_new_incident
```

Do not silently “fix” the hash.

---

## 11. Relationship to evidence packets

An evidence packet is a bounded review artifact.

It may summarize and reference one or more raw sidecars.

It SHOULD contain:

```text
evidence_packet_id
reviewer
subject
scope
summary
findings
sidecar_refs
artifact hashes
decision context
signature or payload hash where applicable
```

It SHOULD NOT contain unnecessary raw content.

### 11.1 Evidence packet reference object

```yaml
evidence_packet_ref:
  evidence_packet_id: evp_...
  path_ref: data/evidence_packets/evp_....json
  packet_sha256: '<64 lowercase hex>'
  packet_schema: ester.evidence.v1 | cli-agent-evidence-packet-0.1
  sidecar_ids:
    - res_...
  reviewer: reviewer_id
  decision: CLEAR_QUARANTINE | HOLD | REJECT | ESCALATE | LEGAL_HOLD
```

### 11.2 Clear/quarantine rule

A quarantine clear decision MUST NOT rely on raw evidence alone.

It requires at minimum:

```text
valid evidence packet
raw evidence sidecar references where raw material exists
evidence hash verification
reviewer identity
witness event
L4W envelope where required by profile
```

---

## 12. Relationship to L4W envelopes

L4W envelopes are tamper-evident proof wrappers.

They SHOULD bind:

```text
evidence packet reference
sidecar hash reference
review decision
subject identity
quarantine or incident reference
chain continuity
signature / public key fingerprint
selective disclosure commitments
```

L4W envelopes SHOULD NOT disclose full raw evidence by default.

### 12.1 L4W reference object

```yaml
l4w_ref:
  envelope_id: l4w_...
  envelope_path: data/l4w/envelopes/...
  envelope_sha256: '<64 lowercase hex>'
  envelope_hash: '<64 lowercase hex>'
  prev_hash: '<64 lowercase hex or empty genesis>'
  pub_fingerprint: '<fingerprint>'
  disclosure_packet_id: ''
  sidecar_ids:
    - res_...
```

### 12.2 Selective disclosure rule

Public or restricted disclosure SHOULD reveal only what is needed:

```text
claim
commitment
salted reveal where authorized
hashes
decision class
review class
not the whole raw artifact
```

---

## 13. Relationship to memory gate

Raw evidence MUST NOT enter `c` memory directly.

The memory gate may accept:

```text
safe summary
defensive signature
bounded lesson
review outcome
risk marker
policy candidate
immunity update proposal
```

The memory gate must reject:

```text
raw secret
raw incident bundle
raw private memory dump
unredacted third-party material
unreviewed hostile prompt
unbounded cloud transcript
agent self-justification
```

### 13.1 Memory proposal minimum

```yaml
memory_proposal:
  proposal_id: mgp_...
  source_sidecar_ids:
    - res_...
  source_evidence_packet_id: evp_...
  witness_event_id: we_...
  proposed_memory_class: operational_lesson | defensive_signature | policy_candidate | rejected_historical_note
  proposed_text: 'Safe bounded summary only.'
  raw_content_included: false
  uncertainty: medium
  reviewer_required: true
```

### 13.2 Memory promotion rule

If raw content appears in a memory proposal:

```text
status = deny_and_quarantine
reason = raw_evidence_in_memory_proposal
```

---

## 14. Relationship to public redaction

Public release may include:

```text
safe doctrine
redacted summary
synthetic example
hash-only proof
commitment-only proof
non-sensitive workflow diagram
public-safe conformance fixture
```

Public release must not include:

```text
raw incident evidence
real secrets
secret-adjacent context
private memory
legal privileged material
provider/account identifiers
local infrastructure paths
live defensive signatures
canary values
exploit-like details
unredacted third-party material
```

### 14.1 Disclosure classes

Disclosure classes use prefix `DISC-*`.

| Class | Meaning | Handling |
|---|---|---|
| `DISC-0` | No disclosure | Keep internal. |
| `DISC-1` | Hash-only disclosure | Publish/transfer only hash and minimal metadata. |
| `DISC-2` | Redacted summary | Safe summary without raw material. |
| `DISC-3` | Restricted reviewer disclosure | Human/legal/security reviewer only. |
| `DISC-4` | Provider/security handoff | Scoped handoff under lawful/security route. |
| `DISC-5` | Counsel/legal disclosure | Legal privileged route only. |
| `DISC-PUB` | Public-safe disclosure | Public after redaction pass. |
| `DISC-X` | Prohibited disclosure | Must not disclose. |

### 14.2 Public default

```text
raw evidence public default = DISC-0
```

No raw sidecar becomes public by default.

---

## 15. Storage and path discipline

### 15.1 Recommended restricted layout

```text
data/
  restricted/
    evidence/
      raw/
      sidecars/
      packets/
      redacted/
      access_events/
  l4w/
    envelopes/
    disclosures/
    chains/
  quarantine/
    artifacts/
    state/
  witness/
    events/
```

### 15.2 Path safety

All raw evidence paths MUST be checked against configured roots.

Forbidden:

```text
absolute unapproved paths
path traversal
symlink escape
cloud sync folder by default
public repo path by default
release artifact path by default
user desktop dump by default
system secrets directory
```

### 15.3 Hash naming

Raw artifacts SHOULD be named or aliased by hash where practical:

```text
raw_<sha256_prefix>.<ext>
sidecar_<sha256_prefix>.json
```

Avoid sensitive filenames.

---

## 16. Cloud and externalization rules

Cloud or external agent access to raw evidence is denied by default.

Allowed only if all are true:

```text
task contract explicitly allows it
sidecar classification permits it
redaction state is sufficient
human/legal/security gate passes where applicable
cloud data policy allows it
witness event records it
recipient retention/disclosure assumptions are recorded
```

### 16.1 Codex / CLI handoff rule

For Codex-like or cloud CLI agents:

```text
send pointer, not payload
send hash, not raw evidence
send redacted summary, not secrets
keep auto_ingest=false
keep memory=off
require explicit inspect-local route for raw material
```

### 16.2 Denied externalization examples

```text
raw private memory -> cloud prompt
raw incident bundle -> public repo
secret-adjacent log -> Codex context
legal evidence -> general LLM review
child-sensitive material -> external model
third-party private data -> conformance fixture
```

---

## 17. Access control

### 17.1 Roles

| Role | May do |
|---|---|
| `c` | Request review, interpret summaries, decide memory promotion through gate. |
| `human_anchor` | Approve high-risk access, disclosure, legal handoff, irreversible retention decisions. |
| `local_checker` | Validate schema/hash/path without reading raw content where possible. |
| `reviewer` | Inspect scoped raw evidence under review window. |
| `incident_reviewer` | Inspect incident evidence under restricted incident protocol. |
| `legal_reviewer` | Inspect legal/privileged evidence where applicable. |
| `cli_executor` | May create sidecar refs; MUST NOT self-approve or freely inspect raw evidence. |
| `cloud_agent` | May receive redacted summaries only unless explicitly permitted. |
| `public_reader` | May see only public-safe disclosure. |

### 17.2 Review windows

Raw access SHOULD be time-boxed.

Access window minimum fields:

```yaml
review_window:
  window_id: rw_...
  sidecar_id: res_...
  reviewer_id: reviewer_...
  opened_at: '2026-05-17T00:00:00Z'
  expires_at: '2026-05-17T01:00:00Z'
  purpose: incident_triage
  scope: metadata_only | redacted | raw_read | copy_allowed
  copy_allowed: false
  externalization_allowed: false
```

---

## 18. Retention and destruction

Retention classes use prefix `RET-*`.

| Class | Meaning | Example |
|---|---|---|
| `RET-EPHEMERAL` | Destroy soon after packetization | temporary CLI scratch |
| `RET-RESTRICTED-30D` | Keep 30 days restricted | low-risk review artifact |
| `RET-RESTRICTED-90D` | Keep 90 days restricted | ordinary operational evidence |
| `RET-INCIDENT-1Y` | Keep one year | incident evidence |
| `RET-LEGAL-HOLD` | Keep until legal release | legal/counsel/regulatory material |
| `RET-L4W-CHAIN` | Preserve proof references long-term | envelopes, hash refs, chain records |
| `RET-PUBLIC-PROOF` | Preserve public-safe proof | public hash/disclosure metadata |
| `RET-DESTROY-NOW` | Destroy immediately if lawful | prohibited or unnecessary sensitive material |

### 18.1 Destruction record

Destruction MUST be recorded without retaining raw content.

```yaml
destruction_record:
  schema: cli-agent-evidence-destruction-record-0.1
  sidecar_id: res_...
  artifact_sha256: '<64 lowercase hex>'
  destroyed_at: '2026-05-17T00:00:00Z'
  destroyed_by: operator_or_system
  method: secure_delete | ordinary_delete | external_legal_transfer | rejected_before_storage
  reason: retention_expired | prohibited_custody | duplicate | legal_release
  witness_event_id: we_...
  tombstone_kept: true
```

### 18.2 Legal hold override

If `legal_hold = true`, ordinary expiry MUST NOT destroy raw evidence.

Required output:

```text
status = hold_active
reason = legal_hold_blocks_destruction
```

---

## 19. Failure behavior

### 19.1 Fail-closed conditions

The system MUST fail closed if:

```text
sidecar missing for raw evidence reference
hash mismatch
artifact path escapes allowed root
classification absent
legal hold unclear
third-party sensitive marker unresolved
cloud export requested without policy
public disclosure requested without redaction class
memory proposal includes raw content
evidence packet references unknown sidecar
L4W envelope evidence_ref mismatch
agent attempts self-approval
```

### 19.2 Standard failure actions

| Condition | Action |
|---|---|
| Missing sidecar | Hold and create sidecar or drop raw ref. |
| Hash mismatch | Freeze and preserve mismatch as incident. |
| Path escape | Deny and quarantine. |
| Public release of raw evidence | Block release and create redaction issue. |
| Cloud upload request | Deny unless explicit gate passes. |
| Memory raw promotion | Deny and quarantine proposal. |
| Legal ambiguity | Escalate to human/legal review. |
| Agent self-approval | Reject review sufficiency. |

---

## 20. Conformance hooks

### 20.1 Required conformance tests

| ID | Test | Expected result |
|---|---|---|
| `RES-T001` | Witness event embeds raw secret | Reject. |
| `RES-T002` | Witness event references sidecar hash only | Allow if sidecar valid. |
| `RES-T003` | Evidence packet references missing sidecar | Fail closed. |
| `RES-T004` | Sidecar hash mismatch | Freeze / incident. |
| `RES-T005` | Raw evidence proposed to memory | Deny and quarantine. |
| `RES-T006` | Redacted summary proposed to memory with refs | Conditional allow. |
| `RES-T007` | Public release includes raw incident material | Block. |
| `RES-T008` | Public release includes synthetic fixture | Allow if safe. |
| `RES-T009` | Cloud agent requests raw sidecar | Deny by default. |
| `RES-T010` | Legal hold evidence expires | Do not destroy. |
| `RES-T011` | L4W envelope evidence ref matches sidecar and packet | Allow if signature/chain passes. |
| `RES-T012` | L4W envelope evidence ref mismatch | Reject. |
| `RES-T013` | Access window expired | Deny raw inspection. |
| `RES-T014` | Reviewer copies raw evidence without permission | Fail and witness violation. |
| `RES-T015` | Sidecar path escapes restricted root | Deny and quarantine. |

### 20.2 Fixture rules

Conformance fixtures MUST use:

```text
synthetic secrets
fake tokens
toy paths
mock incident records
local-only artifacts
non-executable hostile markers
safe pseudo-payloads
```

Conformance fixtures MUST NOT use:

```text
real secrets
real incident material
real private memory
real legal documents
real third-party private data
live external targets
exploit procedures
malware behavior
credential capture logic
```

---

## 21. Local checker requirements

The local checker SHOULD validate:

```text
schema version
required fields
sidecar id uniqueness
hash format
hash match where artifact available
path root safety
classification present
retention class present
cloud export flag false by default
public release flag false by default
memory raw content absent
sidecar references resolvable
witness refs resolvable
packet refs resolvable
L4W refs resolvable where required
legal hold override
access window expiry
```

The local checker MUST NOT read raw content when metadata/hash validation is sufficient.

---

## 22. Implementation notes for `ester-clean-code`

The existing implementation substrate already contains relevant anatomical zones:

```text
quarantine state / clear lifecycle
evidence packet checks
integrity stack
L4W envelope and audit CLI
SYNAPS Codex pointer / package ledger
memory provenance and vector stores
USB / portable recovery surfaces
```

This profile should be implemented by composition, not by rewriting those zones into one giant subsystem.

Recommended implementation order:

```text
1. create sidecar schema and root directories
2. add sidecar creation helper
3. add sidecar hash/path validator
4. bind quarantine evidence packet refs to sidecars
5. bind witness raw_evidence_ref to sidecars
6. bind L4W evidence_ref to sidecar refs
7. add memory-gate raw-content rejection check
8. add redaction/public-release checker
9. add conformance fixtures
10. add local checker report
```

---

## 23. YAML sketch: complete sidecar + packet + witness chain

```yaml
raw_sidecar:
  schema: cli-agent-raw-evidence-sidecar-0.1
  sidecar_id: res_demo_001
  created_at: '2026-05-17T00:00:00Z'
  source:
    source_type: quarantine
    task_contract_id: catc_demo_001
    agent_id: codex_demo_worker
    quarantine_event_id: dq_demo_001
    witness_event_id: we_demo_001
  artifact:
    storage_class: encrypted_local
    path_ref: data/restricted/evidence/raw/raw_demo_001.json
    content_sha256: 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    size_bytes: 1200
    media_type: application/json
  classification:
    evidence_class: EVR-4
    data_classes: [incident, private_operational]
    cloud_export_allowed: false
    public_release_allowed: false
  custody:
    custody_state: RES-QUARANTINED
    retention_class: RET-INCIDENT-1Y
    legal_hold: false
    encryption_required: true
  status:
    current_state: RES-QUARANTINED
    problems: []

evidence_packet_ref:
  evidence_packet_id: evp_demo_001
  packet_sha256: 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
  sidecar_ids: [res_demo_001]
  decision: HOLD

witness_raw_evidence_ref:
  witness_event_id: we_demo_001
  sidecar_id: res_demo_001
  evidence_class: EVR-4
  content_sha256: 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
  raw_content_in_witness: false

l4w_ref:
  envelope_id: l4w_demo_001
  envelope_hash: 'cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'
  evidence_packet_id: evp_demo_001
  sidecar_ids: [res_demo_001]
```

---

## 24. Release-readiness impact

This document closes a release-readiness gap by centralizing the raw-evidence exception language that otherwise appears across witness, rollback/freeze, memory gate, incident response, defensive emulation, secrets/cloud data, public redaction, and conformance materials.

It does not by itself make the package implementation-ready.

Implementation-readiness still requires:

```text
JSON Schema extraction
sidecar schema file
semantic validator rules
fixture manifest
evidence packet schema alignment
local checker implementation
conformance run records
release hygiene patch
```

---

## 25. Open issues

| ID | Issue | Status |
|---|---|---|
| `RES-OI-01` | Exact schema alignment with existing `ester.evidence.v1` evidence packet | Open / implementation bridge. |
| `RES-OI-02` | Exact L4W envelope field mapping for sidecar refs | Open / implementation bridge. |
| `RES-OI-03` | Retention class defaults for legal/counsel material | Needs legal review. |
| `RES-OI-04` | Provider-specific raw-evidence externalization rules | Deferred to provider profiles. |
| `RES-OI-05` | Secure deletion guarantees across Windows/Linux/filesystems | Open / implementation-specific. |
| `RES-OI-06` | UI surface for sidecar inspection and review windows | Deferred to UI State Surface profile. |
| `RES-OI-07` | Cross-`c` sidecar isolation rules | Deferred to Cross-c Isolation profile. |

---

## 26. Final rule

A C-Governed CLI Agent Mesh may preserve raw evidence.

It may not let raw evidence become everywhere.

```text
Sidecar holds.
Witness points.
Packet summarizes.
L4W seals.
Memory gates.
Public redacts.
c decides.
Human anchors high-risk consequence.
```
