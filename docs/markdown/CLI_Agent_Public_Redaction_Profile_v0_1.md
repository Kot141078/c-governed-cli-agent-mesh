# CLI Agent Public Redaction Profile v0.1

## Public / restricted split, safe disclosure, redaction rules, and release hygiene for the C-Governed CLI Agent Mesh package

**Status:** Draft redaction profile v0.1  
**Date:** 2026-05-16  
**Package:** C-Governed CLI Agent Mesh  
**Layer:** `c = a + b` / Agent Governance / Publication Hygiene / Sensitive Boundary Control / Redaction  
**Document class:** public-redaction profile / release-safety artifact / package-control companion  
**Assertion class:** `C-A10` package-control artifact  
**Primary parent documents:**  
- `CLI_Agent_Package_Index_and_Reading_Order_v0_1.md`
- `CLI_Agent_OPEN_ISSUES_v0_1.md`
- `CLI_Agent_Contradiction_Register_v0_1.md`
- `CLI_Agent_Secrets_and_Cloud_Data_Policy_v0_1.md`
- `CLI_Agent_Defensive_Emulation_Boundaries_v0_1.md`
- `CLI_Agent_Incident_Response_Profile_v0_1.md`
- `CLI_Agent_Conformance_Test_Matrix_v0_1.md`

**Primary boundary:** public release must preserve the governance value of the package without exposing secrets, operational defensive internals, live incident material, exploit-like detail, private memory, legal-sensitive material, provider/account details, local infrastructure paths, or red-line-enabling procedures.

---

## 0. Executive definition

**CLI Agent Public Redaction Profile** defines how to split the C-Governed CLI Agent Mesh package into public, technical, restricted, and internal materials.

The profile answers:

```text
Which files may be public?
Which files require redaction?
Which examples are safe?
Which examples must be synthetic?
Which objects must never be public?
Which operational details must be removed?
Which red-line wording must be preserved?
Which sensitive implementation details must stay internal?
```

The goal is not to hide the architecture.

The goal is to publish the architecture without publishing unsafe operational material.

Compact formula:

```text
Publish the governance.
Do not publish the keys.
Publish the boundaries.
Do not publish the bypasses.
Publish the doctrine.
Do not publish the garage contents.
```

---

## 1. Purpose

The C-Governed CLI Agent Mesh package contains both public-value protocol material and sensitive operational safety material.

Public readers need to understand:

- why executable agents require governance;
- why task contracts are necessary;
- why capability is not permission;
- why cloud context is not private by default;
- why witness, rollback, memory gate, and review separation matter;
- why defensive emulation must not become retaliation.

Public readers do **not** need:

- real infrastructure paths;
- real account or provider identifiers;
- real incident traces;
- real secrets or secret references;
- real private memory;
- real legal material;
- real defensive garage contents;
- operational canary values;
- exploit-like steps;
- live target details;
- provider-specific sensitive configurations;
- private agent registry data.

This profile defines how to preserve value while reducing risk.

---

## 2. Non-goals

This profile does not define or permit:

1. hiding known safety defects from reviewers;
2. laundering restricted operational material into public form;
3. publishing exploit recipes as “defensive examples”;
4. publishing real secrets, tokens, credentials, private keys, account references, or identity material;
5. publishing real incident evidence without lawful review;
6. publishing private `c` memory;
7. publishing sealed material;
8. publishing legal privileged material without legal review;
9. publishing canary values or defensive signatures that would weaken protection;
10. publishing live target details;
11. treating redaction as evidence destruction;
12. using public redaction to avoid required internal witness or audit records.

Redaction protects publication.

It does not erase internal accountability.

---

## 3. Corpus bridge set

### 3.1 Explicit bridge: `c = a + b`

CLI agents, documents, schemas, fixtures, witness records, redaction records, and release artifacts are all part of `b`.

A public release is a state transition in `b` that can affect `c` reputation, adoption, interpretation, and future operational surface.

Therefore, public release is not casual export. It is a governed transition.

### 3.2 Quiet bridge I: information theory

A public document is a channel. The question is not only “is this true?” but also “what does this enable?” A good public document transmits enough structure to be useful and enough boundary to prevent misuse, while minimizing leakage of operational details.

### 3.3 Quiet bridge II: engineering disclosure

A safety standard can publish the rule that a panel must be locked without publishing the master key. It can publish the requirement for emergency stop without publishing a way to bypass it. This profile applies the same distinction to CLI-agent governance.

### 3.4 Quiet bridge III: immune-system analogy

An immune system may describe that it has antibodies, containment, and memory. It does not publish all current vulnerabilities, all decoy markers, and all live detection signatures to every pathogen. Public release should teach the architecture, not disarm the organism.

### 3.5 Earth paragraph

A construction company can publish its safety manual: helmets, lockout, permits, inspection, fire exits. It does not publish the alarm code, the weak back door, the exact storage location of expensive tools, or the photo of the keys hanging in the office. That is not secrecy theater. That is basic hygiene.

---

## 4. Publication classes

Publication classes use prefix `PUB-*`.

| Class | Meaning | Default handling |
|---|---|---|
| `PUB-0` | Public-safe | May be published as-is after ordinary review. |
| `PUB-1` | Public-safe with minor review | May be published after wording and example review. |
| `PUB-2` | Public-redacted | Requires redaction of examples, paths, identifiers, or operational detail. |
| `PUB-3` | Technical restricted | Internal / restricted technical release only. |
| `PUB-4` | Internal operational | Do not publish; operational deployment material. |
| `PUB-5` | Legal / incident restricted | Legal, incident, counsel, provider, or security-review only. |
| `PUB-X` | Prohibited publication | Must not be published. |

### 4.1 Publication default

If classification is unclear:

```text
default = PUB-3 technical restricted
```

Unknown sensitivity must not default to public.

---

## 5. Package file publication map

### 5.1 Public-capable after review

| File | Publication class | Required action |
|---|---:|---|
| `README.md` | `PUB-1` | Ensure no internal paths/account refs. |
| `C-Governed_CLI_Agent_Mesh_Protocol_v0_1.md` | `PUB-1` | Red-line wording pass. |
| `CLI_Agent_Task_Contract_Schema_v0_1.md` | `PUB-1` | Replace placeholder schema IDs; ensure examples synthetic. |
| `CLI_Agent_Permission_and_Capability_Model_v0_1.md` | `PUB-1` | Ensure prohibited bundles remain abstract. |
| `CLI_Agent_Handshake_Profile_v0_1.md` | `PUB-2` | Redact provider/account refs in examples. |
| `CLI_Agent_Sandbox_Worktree_Profile_v0_1.md` | `PUB-2` | Keep command examples abstract; remove real paths. |
| `CLI_Agent_Witness_Event_Profile_v0_1.md` | `PUB-1` | Ensure no raw evidence examples. |
| `CLI_Agent_Memory_Gate_Profile_v0_1.md` | `PUB-2` | Review immunity examples and core-memory language. |
| `CLI_Agent_Rollback_and_Freeze_Profile_v0_1.md` | `PUB-1` | Ensure examples remain synthetic. |
| `CLI_Agent_Quorum_and_Review_Profile_v0_1.md` | `PUB-1` | Ensure quorum is not authority. |
| `CLI_Agent_Executor_Reviewer_Separation_v0_1.md` | `PUB-1` | Safe after ordinary review. |
| `CLI_Agent_Conformance_Test_Matrix_v0_1.md` | `PUB-2` | Ensure tests are defensive, abstract, synthetic. |
| `CLI_Agent_Package_Index_and_Reading_Order_v0_1.md` | `PUB-1` | Safe after file-status review. |
| `CLI_Agent_GLOSSARY_v0_1.md` | `PUB-1` | Safe after terminology review. |
| `CLI_Agent_OPEN_ISSUES_v0_1.md` | `PUB-2` | Review whether open issues reveal sensitive planned controls. |
| `CLI_Agent_Contradiction_Register_v0_1.md` | `PUB-2` | Review public release risk table. |
| `CLI_Agent_RELEASE_NOTES_v0_1.md` | `PUB-1` | Safe after release boundary review. |

### 5.2 Restricted by default

| File / object | Publication class | Reason |
|---|---:|---|
| `CLI_Agent_Defensive_Emulation_Boundaries_v0_1.md` | `PUB-3` | Contains containment garage, canary, mirror simulation, immunity update boundaries. |
| `CLI_Agent_Incident_Response_Profile_v0_1.md` | `PUB-3` | Contains incident, preservation, cloud exposure, and response procedures. |
| `CLI_Agent_Secrets_and_Cloud_Data_Policy_v0_1.md` | `PUB-3` | Contains secret, provider, cloud boundary, exposure handling. |
| Real conformance test runs | `PUB-4` / `PUB-5` | May include operational details. |
| Real incident reports | `PUB-5` | Legal/security-sensitive. |
| Real provider boundary records | `PUB-4` | Account/workspace/provider details. |
| Real secret boundary records | `PUB-5` | Secret handling. |
| Real cloud exposure events | `PUB-5` | Incident/legal risk. |
| Real memory-gate records involving private material | `PUB-4` / `PUB-5` | Private/identity-sensitive. |
| Real defensive garage contents | `PUB-4` | Defensive signature/canary risk. |

---

## 6. Material classes

Material classes use prefix `RM-*` for redaction material.

| Class | Meaning | Public handling |
|---|---|---|
| `RM-ARCH` | Architecture doctrine | usually public |
| `RM-SCHEMA` | Generic schema structure | public after placeholder cleanup |
| `RM-EXAMPLE-SYNTH` | Synthetic examples | public if non-operational |
| `RM-EXAMPLE-REAL` | Real operational examples | restricted |
| `RM-PATH` | Local paths, repo paths, infra paths | abstract/redact if sensitive |
| `RM-ACCOUNT` | Provider account/workspace refs | redact |
| `RM-SECRET` | Secrets/tokens/keys | prohibit |
| `RM-PRIVATE-MEMORY` | Private `c` or human memory | prohibit by default |
| `RM-SEALED` | Sealed compartments | prohibit |
| `RM-LEGAL` | Legal-sensitive material | legal review / restricted |
| `RM-INCIDENT` | Incident evidence | restricted / legal-security review |
| `RM-CANARY` | Canary values / decoys | internal only |
| `RM-SIGNATURE` | Defensive signatures | restricted unless abstracted |
| `RM-GARAGE` | Garage contents / hostile samples | internal/restricted |
| `RM-PROVIDER` | Provider-specific data policy facts | verify before public claims |
| `RM-REDLINE` | Prohibited action boundary | public as prohibition only |
| `RM-OPER-DETAIL` | Operational implementation detail | restrict or abstract |
| `RM-LIVE-TARGET` | Live external target detail | prohibit by default |

---

## 7. Redaction methods

Redaction method IDs use prefix `RED-*`.

| Method | Meaning | Use |
|---|---|---|
| `RED-REMOVE` | Remove material entirely. | Secrets, canary values, exploit-like detail. |
| `RED-LABEL` | Replace with class label. | `secret_ref`, `provider_ref`, `path_ref`. |
| `RED-HASH` | Replace with hash/ref. | Artifacts, logs, evidence refs. |
| `RED-SUMMARY` | Replace raw detail with safe summary. | Legal/incident/private material. |
| `RED-GENERALIZE` | Convert specific detail to general pattern. | Defensive examples. |
| `RED-SYNTHETIC` | Replace real data with synthetic fixture. | Tests and examples. |
| `RED-PSEUDONYM` | Replace name/ID with pseudonym. | People, accounts, agents. |
| `RED-PATH-ABSTRACT` | Replace path with abstract path. | Local infrastructure. |
| `RED-REASON-CODE` | Replace raw explanation with reason code. | Witness and incidents. |
| `RED-SPLIT` | Public summary + restricted appendix. | DEB/IRP/SCDP. |

---

## 8. Public-safe rewriting rules

### 8.1 Preserve prohibitions

Bad:

```text
Agents should avoid retaliation.
```

Better:

```text
Agents MUST NOT perform live external counter-operation, hack-back, or autonomous retaliation.
```

### 8.2 Replace operational procedure with boundary

Bad:

```text
Here is how the mirror responds to the hostile channel.
```

Better:

```text
Mirror simulation is permitted only inside a clean-room sandbox and must not be deployed against a live external source.
```

### 8.3 Replace raw samples with pattern classes

Bad:

```text
This exact hostile prompt is stored and replayed.
```

Better:

```text
A synthetic prompt-injection fixture representing the same class is used for sandbox replay.
```

### 8.4 Replace secret values with secret refs

Bad:

```text
API_KEY=...
```

Better:

```text
secret_ref: provider_token_redacted
```

### 8.5 Replace live target detail with lawful-route summary

Bad:

```text
The source endpoint was...
```

Better:

```text
External source details are retained only in a restricted incident record or lawful provider/legal report.
```

### 8.6 Replace private memory with class-level memory ref

Bad:

```text
The private memory said...
```

Better:

```text
memory_class_ref: private_memory_redacted
```

---

## 9. Sensitive profile redaction rules

### 9.1 Defensive Emulation Boundaries

Public version may include:

- defensive purpose;
- no-retaliation doctrine;
- containment garage concept at high level;
- canary concept at high level;
- mirror simulation as sandbox-only;
- immunity updates as internal block/filter/quarantine/review;
- red-line prohibitions.

Public version must remove or restrict:

- operational canary values;
- real hostile samples;
- detailed live-channel handling;
- detailed defensive signatures;
- garage contents;
- specific detection logic that weakens defense;
- anything resembling exploit instruction;
- any live target detail.

### 9.2 Incident Response Profile

Public version may include:

- detect → triage → preserve → freeze → contain → repair → validate → report;
- owned/authorized scope;
- preserve-before-repair;
- lawful provider/legal handoff;
- no retaliation.

Public version must remove or restrict:

- real incident evidence;
- real logs;
- real secret refs;
- account/provider details;
- local infrastructure paths;
- legal privileged detail;
- tactical detection gaps;
- internal response thresholds if sensitive.

### 9.3 Secrets and Cloud Data Policy

Public version may include:

- data classes;
- cloud denied-by-default doctrine;
- redaction/minimization;
- synthetic fixture preference;
- provider boundary as concept;
- exposure-as-incident.

Public version must remove or restrict:

- real provider account refs;
- real secret boundary records;
- real cloud exposure events;
- real private memory examples;
- legal privileged examples;
- local secret scanning outputs;
- production credential topology.

---

## 10. Public release validation checklist

### 10.1 Secret check

- [ ] No API keys.
- [ ] No tokens.
- [ ] No private keys.
- [ ] No passwords.
- [ ] No recovery codes.
- [ ] No session cookies.
- [ ] No signing material.
- [ ] No production credentials.

### 10.2 Private data check

- [ ] No private `c` memory.
- [ ] No sealed material.
- [ ] No legal privileged material.
- [ ] No raw incident evidence.
- [ ] No child/third-party sensitive data.
- [ ] No identity documents.
- [ ] No private correspondence.

### 10.3 Infrastructure check

- [ ] No real local infrastructure paths unless harmless.
- [ ] No cloud account/workspace refs.
- [ ] No provider endpoint secrets.
- [ ] No internal machine names if sensitive.
- [ ] No real canary values.
- [ ] No defensive signature values if operational.
- [ ] No garage contents.

### 10.4 Red-line check

- [ ] No hack-back instructions.
- [ ] No live counter-operation procedure.
- [ ] No malware behavior.
- [ ] No credential theft.
- [ ] No evasion logic.
- [ ] No unauthorized scanning.
- [ ] No exploit steps.
- [ ] No retaliation language.
- [ ] No offensive conversion of defensive examples.

### 10.5 Governance check

- [ ] Capability remains distinct from permission.
- [ ] Registration remains distinct from authorization.
- [ ] Quorum remains evidence, not sovereignty.
- [ ] Witness remains boundary record, not raw dump.
- [ ] Memory gate remains required.
- [ ] Human gate remains required for high risk.
- [ ] Cloud context remains not-private-by-default.

---

## 11. Redaction record object

Canonical object:

```text
CLI_AGENT_PUBLIC_REDACTION_RECORD
```

### 11.1 YAML shape

```yaml
cli_agent_public_redaction_record:
  schema_version: cli-agent-public-redaction-0.1
  redaction_id: string
  created_at: string
  package_version: v0.1
  source_file: string
  target_file: string | null
  source_publication_class: PUB-0 | PUB-1 | PUB-2 | PUB-3 | PUB-4 | PUB-5 | PUB-X
  target_publication_class: PUB-0 | PUB-1 | PUB-2 | PUB-3 | PUB-4 | PUB-5 | PUB-X

  material_classes_found:
    - RM-ARCH
    - RM-EXAMPLE-SYNTH
    - RM-OPER-DETAIL

  redaction_methods:
    - RED-SUMMARY
    - RED-SYNTHETIC
    - RED-LABEL

  checks:
    secrets_check_passed: boolean
    private_data_check_passed: boolean
    infrastructure_check_passed: boolean
    redline_check_passed: boolean
    governance_check_passed: boolean

  decision:
    decision: public_as_is | public_redacted | restricted_only | internal_only | prohibited_publication
    reason_code: string
    reviewer_ref: string | null
    c_gate_ref: string | null
    human_gate_ref: string | null

  witness:
    witness_required: boolean
    witness_ref: string | null

  notes:
    limitations:
      - string
    unresolved:
      - string
```

---

## 12. Publication decision vocabulary

| Decision | Meaning |
|---|---|
| `public_as_is` | File may be public without redaction after ordinary review. |
| `public_redacted` | File may be public only in redacted form. |
| `restricted_only` | File should remain restricted technical. |
| `internal_only` | File should remain internal operational. |
| `prohibited_publication` | File or material must not be published. |

Reason codes:

```text
safe_public_architecture
requires_example_redaction
contains_sensitive_defensive_boundary
contains_incident_material
contains_secret_boundary
contains_private_memory
contains_legal_sensitive_material
contains_operational_canary
contains_provider_account_ref
contains_redline_enabling_detail
```

---

## 13. Public / restricted bundle model

### 13.1 Public bundle

Recommended public bundle:

```text
README.md
C-Governed_CLI_Agent_Mesh_Protocol_v0_1.md
CLI_Agent_Task_Contract_Schema_v0_1.md
CLI_Agent_Permission_and_Capability_Model_v0_1.md
CLI_Agent_Handshake_Profile_v0_1.md
CLI_Agent_Sandbox_Worktree_Profile_v0_1.md
CLI_Agent_Witness_Event_Profile_v0_1.md
CLI_Agent_Memory_Gate_Profile_v0_1.md
CLI_Agent_Rollback_and_Freeze_Profile_v0_1.md
CLI_Agent_Quorum_and_Review_Profile_v0_1.md
CLI_Agent_Executor_Reviewer_Separation_v0_1.md
CLI_Agent_Conformance_Test_Matrix_v0_1.md
CLI_Agent_Package_Index_and_Reading_Order_v0_1.md
CLI_Agent_GLOSSARY_v0_1.md
CLI_Agent_OPEN_ISSUES_v0_1.md
CLI_Agent_Contradiction_Register_v0_1.md
CLI_Agent_RELEASE_NOTES_v0_1.md
```

With redacted or public-summary versions of:

```text
CLI_Agent_Defensive_Emulation_Boundaries_v0_1.md
CLI_Agent_Incident_Response_Profile_v0_1.md
CLI_Agent_Secrets_and_Cloud_Data_Policy_v0_1.md
```

### 13.2 Restricted technical bundle

Restricted bundle may include full technical versions of:

```text
CLI_Agent_Defensive_Emulation_Boundaries_v0_1.md
CLI_Agent_Incident_Response_Profile_v0_1.md
CLI_Agent_Secrets_and_Cloud_Data_Policy_v0_1.md
real conformance runs
provider boundary records
secret boundary records
incident records
garage records
canary records
immunity candidate evidence
```

### 13.3 Internal operational bundle

Internal-only bundle may include:

```text
real local infrastructure maps
real agent registry
real account/workspace refs
real tokens/secret references
real incident evidence
real memory-gate records involving private memory
real legal handoff packets
real canary/signature values
```

---

## 14. Release workflow

Recommended release workflow:

```text
classify files
  -> run redaction checklist
  -> create redaction records
  -> create public bundle
  -> create restricted bundle if needed
  -> run contradiction/red-line pass
  -> run schema placeholder pass
  -> run secret scan
  -> run link/index check
  -> freeze Markdown
  -> generate PDFs if needed
  -> generate SHA256SUMS
  -> prepare release notes
  -> publish public bundle only
```

---

## 15. Conformance implications

A system cannot claim public conformance by publishing only safe-looking policies.

For conformance, internal evidence may exist but public artifacts may be redacted.

Acceptable public phrasing:

```text
Conformance claim is supported by restricted evidence packet available to authorized reviewers.
```

Unacceptable public phrasing:

```text
Everything is safe; evidence not needed.
```

Public redaction must not be used to hide conformance failure.

---

## 16. Open issues

| ID | Issue | Required action |
|---|---|---|
| `PRP-OI-001` | Need exact public summary versions of DEB/IRP/SCDP. | Create redacted public variants or mark restricted. |
| `PRP-OI-002` | Need automated secret scan before public release. | Add release checklist command/process. |
| `PRP-OI-003` | Need provider-specific publication rule. | Add after provider profiles. |
| `PRP-OI-004` | Need legal review for legal-sensitive examples. | Link to future legal handoff profile. |
| `PRP-OI-005` | Need restricted evidence sidecar naming convention. | Define in witness/evidence profile. |
| `PRP-OI-006` | Need redaction record schema extraction. | Add to JSON schema extraction plan. |
| `PRP-OI-007` | Need public conformance statement template. | Add to conformance/public release package. |
| `PRP-OI-008` | Need release bundle manifest. | Add machine-readable manifest. |

---

## 17. Closing rule

Public release is itself an action.

It changes the environment around `c`.

Final rule:

```text
Publish what teaches governance.
Restrict what weakens the boundary.
Never publish what turns defense into a weapon.
```
