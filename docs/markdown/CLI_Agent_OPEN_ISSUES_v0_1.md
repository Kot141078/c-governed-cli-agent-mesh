# CLI Agent OPEN ISSUES v0.1.1-hygiene

## Open issues, release blockers, validation gaps, implementation tasks, and restricted-review items for the C-Governed CLI Agent Mesh package

**Status:** Draft open-issues register v0.1.1-hygiene synchronized  
**Date:** 2026-05-17  
**Package:** C-Governed CLI Agent Mesh  
**Layer:** `c = a + b` / SER / L4 / Agent Governance / CLI Worker Mesh / Defensive Adaptation / Witness  
**Document class:** open-issues register / release-readiness artifact / package-control companion  
**Assertion class:** `C-A10` package-control artifact  
**Primary parent document:** `CLI_Agent_Package_Index_and_Reading_Order_v0_1.md`  
**Primary boundary:** unresolved issues must be tracked explicitly before release-complete, implementation-ready, public-release-ready, conformance-supported, or deployment claims.

---

## 0. Purpose

This file tracks unresolved issues, resolved hygiene items, release blockers, validation gaps, implementation tasks, redaction needs, conformance work, and future companion documents for the **C-Governed CLI Agent Mesh v0.1 / v0.1.1-hygiene** package.

It exists because the package now contains a real protocol stack, not a single essay.

Compact formula:

```text
Open issues are not weakness.
They are load-bearing honesty.
```

---

## 1. Current package state

```text
Package status: v0.1 draft protocol pack with v0.1.1 hygiene synchronization
Architecture readiness: draft-complete
Release readiness: in progress / not yet release-complete
Implementation readiness: in progress / not yet implementation-ready
Public readiness: partial / public-restricted split exists but must be applied
Conformance readiness: framework exists / tests not executed
Contradiction audit: completed at draft level; hard contradictions currently 0
Red-line posture: strong; semantic validator and local checker profiles now exist
```

### 1.1 Current canonical files

| File | Status |
|---|---|
| `README.md` | canonical draft / v0.1.1 synchronized package set |
| `C-Governed_CLI_Agent_Mesh_Protocol_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Package_Index_and_Reading_Order_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_GLOSSARY_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_RELEASE_NOTES_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_OPEN_ISSUES_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Contradiction_Register_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_v0_1_1_Hygiene_Patch_Notes.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Release_and_Implementation_Readiness_Gate_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Task_Contract_Schema_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Permission_and_Capability_Model_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Handshake_Profile_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_AB_Mode_and_Gate_Semantics_Profile_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Registry_Profile_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Sandbox_Worktree_Profile_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Witness_Event_Profile_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Raw_Evidence_Sidecar_Profile_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Memory_Gate_Profile_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Rollback_and_Freeze_Profile_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Quorum_and_Review_Profile_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Executor_Reviewer_Separation_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Defensive_Emulation_Boundaries_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Incident_Response_Profile_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Secrets_and_Cloud_Data_Policy_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Public_Redaction_Profile_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Release_Public_Surface_Profile_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_JSON_Schema_Extraction_Plan_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Schema_Object_Registry_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Semantic_Validator_Rules_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Local_Checker_Profile_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Conformance_Test_Matrix_v0_1.md` | canonical draft / v0.1.1 synchronized package set |
| `CLI_Agent_Conformance_Fixture_Pack_v0_1.md` | canonical draft / v0.1.1 synchronized package set |

---

## 2. Status vocabulary

| Status | Meaning |
|---|---|
| `OPEN` | Not yet addressed. |
| `IN_PROGRESS` | Work started. |
| `PARTIALLY_RESOLVED` | Companion/profile exists, but execution or application remains. |
| `RESOLVED` | Fixed, superseded, or incorporated into v0.1.1 hygiene set. |
| `DEFERRED` | Valid but not required for immediate release-complete / implementation-ready handoff. |
| `BLOCKED` | Requires decision or external input. |
| `WONTFIX` | Explicitly rejected. |

---

## 3. v0.1.1 hygiene resolution summary

The following previously open structural items are now resolved or partially resolved:

| Item | v0.1.1 status | Notes |
|---|---|---|
| README missing | `RESOLVED` | `README.md` exists and is synchronized. |
| Release notes missing | `RESOLVED` | `CLI_Agent_RELEASE_NOTES_v0_1.md` exists and is synchronized. |
| Contradiction register missing | `RESOLVED` | `CLI_Agent_Contradiction_Register_v0_1.md` exists and reports no hard contradictions. |
| Public redaction profile missing | `RESOLVED` | `CLI_Agent_Public_Redaction_Profile_v0_1.md` exists. |
| JSON schema extraction plan missing | `RESOLVED` | `CLI_Agent_JSON_Schema_Extraction_Plan_v0_1.md` exists and is synchronized with SOR/SVR. |
| Conformance fixture pack missing | `RESOLVED` | `CLI_Agent_Conformance_Fixture_Pack_v0_1.md` exists as safe synthetic catalog. |
| Raw evidence sidecar missing | `RESOLVED` | `CLI_Agent_Raw_Evidence_Sidecar_Profile_v0_1.md` exists. |
| AB/gate semantics missing | `RESOLVED` | `CLI_Agent_AB_Mode_and_Gate_Semantics_Profile_v0_1.md` exists. |
| Registry profile missing | `RESOLVED` | `CLI_Agent_Registry_Profile_v0_1.md` exists. |
| Local checker profile missing | `RESOLVED` | `CLI_Agent_Local_Checker_Profile_v0_1.md` exists. |
| Release/public surface profile missing | `RESOLVED` | `CLI_Agent_Release_Public_Surface_Profile_v0_1.md` exists. |
| Schema object registry missing | `RESOLVED` | `CLI_Agent_Schema_Object_Registry_v0_1.md` exists and marks SCDP/CTM/Package Index sources as available. |
| Semantic validator rules missing | `RESOLVED` | `CLI_Agent_Semantic_Validator_Rules_v0_1.md` exists. |
| Package index absent from local package | `RESOLVED` | This synchronization creates `CLI_Agent_Package_Index_and_Reading_Order_v0_1.md`. |

---

## 4. Remaining release blockers

These must be closed before `release-complete`.

| ID | Type | Priority | Issue | Required action | Status |
|---|---|---:|---|---|---|
| `OI-REL-001` | `DOC` | `P0` | Canonical filename/source inventory still needs final repository check. | Confirm actual repo filenames match package index; resolve lowercase/legacy names. | `OPEN` |
| `OI-REL-002` | `DOC` | `P0` | Duplicate sandbox/worktree source variant may exist. | Declare canonical SWP source and remove/supersede duplicate before schema extraction. | `OPEN` |
| `OI-REL-003` | `REL` | `P0` | Public/restricted split exists as profile but has not been applied to final repository package. | Apply `CLI_Agent_Public_Redaction_Profile_v0_1.md` and `CLI_Agent_Release_Public_Surface_Profile_v0_1.md`. | `PARTIALLY_RESOLVED` |
| `OI-REL-004` | `REL` | `P0` | Final repository placement / default-branch discoverability must be confirmed. | Put files in intended path; check human-visible README / index / release surface. | `OPEN` |
| `OI-REL-005` | `REL` | `P0` | Release manifest, PDF set, and SHA256SUMS cannot be generated before freeze. | Freeze Markdown first; then generate artifacts and hashes. | `OPEN` |

---

## 5. Remaining implementation-readiness blockers

These must be closed before `implementation-ready`.

| ID | Type | Priority | Issue | Required action | Status |
|---|---|---:|---|---|---|
| `OI-IMPL-001` | `SCHEMA` | `P0` | P0 JSON schemas are not extracted. | Use JSEP + SOR to extract P0 schemas. | `OPEN` |
| `OI-IMPL-002` | `SCHEMA` | `P0` | `SCHEMA_INDEX.json` does not exist. | Create draft or generated schema index. | `OPEN` |
| `OI-IMPL-003` | `SCHEMA` | `P0` | Semantic validators are specified but not implemented/executed. | Implement validator stubs or explicit validation contract. | `PARTIALLY_RESOLVED` |
| `OI-IMPL-004` | `IMPL` | `P0` | Local checker profile exists but no checker run has occurred. | Create checker run contract and execute after schemas/fixtures. | `PARTIALLY_RESOLVED` |
| `OI-IMPL-005` | `CONF` | `P0` | Conformance fixtures exist as catalog but no runner/evidence packets exist. | Bind fixture pack to validator and create evidence packet expectations. | `PARTIALLY_RESOLVED` |
| `OI-IMPL-006` | `DOC` | `P0` | Codex handoff must be restricted to schema/hygiene work, not publication. | Create task contract with `memory=off`, `auto_ingest=false`, no tag/publish. | `OPEN` |

---

## 6. Schema and machine-validation issues

| ID | Type | Priority | Issue | Required action | Status |
|---|---|---:|---|---|---|
| `OI-SCHEMA-001` | `SCHEMA` | `P0` | Schema extraction plan needed. | `CLI_Agent_JSON_Schema_Extraction_Plan_v0_1.md` created and synchronized. | `RESOLVED` |
| `OI-SCHEMA-002` | `SCHEMA` | `P0` | Schema object registry needed. | `CLI_Agent_Schema_Object_Registry_v0_1.md` created and synchronized. | `RESOLVED` |
| `OI-SCHEMA-003` | `SCHEMA` | `P0` | Semantic validation rules needed. | `CLI_Agent_Semantic_Validator_Rules_v0_1.md` created. | `RESOLVED` |
| `OI-SCHEMA-004` | `SCHEMA` | `P0` | P0 schemas missing. | Extract P0 schemas from SOR. | `OPEN` |
| `OI-SCHEMA-005` | `SCHEMA` | `P0` | `SCHEMA_INDEX.json` missing. | Generate after P0 extraction. | `OPEN` |
| `OI-SCHEMA-006` | `SCHEMA` | `P1` | Stable URL `$id` unavailable until repo placement. | Use URN `$id`; replace/supplement after repository placement. | `OPEN` |
| `OI-SCHEMA-007` | `SCHEMA` | `P1` | Canonicalization/signature profile remains future work. | Keep hash fields conservative; defer full signature semantics to L4W/signature profile. | `DEFERRED` |

---

## 7. Security, cloud, and red-line issues

| ID | Type | Priority | Issue | Required action | Status |
|---|---|---:|---|---|---|
| `OI-SEC-001` | `RED` | `P0` | Defensive emulation is sensitive. | Apply public/restricted split; keep real garage/canary material restricted. | `PARTIALLY_RESOLVED` |
| `OI-SEC-002` | `SEC` | `P0` | Incident response must not imply counter-operation. | Keep IRP wording as local defense/lawful handoff; include in semantic validator. | `PARTIALLY_RESOLVED` |
| `OI-SEC-003` | `CLOUD` | `P0` | Secrets/cloud policy exists but provider-specific facts are generic. | Provider-specific profiles later; no provider-specific claim now. | `DEFERRED` |
| `OI-SEC-004` | `RED` | `P0` | Red-line wording must be checked mechanically before release. | Bind SVR + local checker. | `PARTIALLY_RESOLVED` |

---

## 8. Witness, evidence, and memory issues

| ID | Type | Priority | Issue | Required action | Status |
|---|---|---:|---|---|---|
| `OI-WIT-001` | `WIT` | `P0` | Central raw evidence sidecar needed. | `CLI_Agent_Raw_Evidence_Sidecar_Profile_v0_1.md` created. | `RESOLVED` |
| `OI-WIT-002` | `WIT` | `P1` | Exact storage backend remains implementation-specific. | Define during implementation; profile can remain backend-neutral. | `DEFERRED` |
| `OI-WIT-003` | `WIT` | `P1` | Canonicalization/signature not fully specified. | Defer to L4W/signature implementation layer. | `DEFERRED` |
| `OI-MEM-001` | `MEM` | `P1` | MGP needs cross-review with broader `c` memory corpus before public release. | Do cross-corpus review before archival/public claim. | `OPEN` |
| `OI-MEM-002` | `MEM` | `P2` | Retention/decay profile not yet created. | Future `CLI_Agent_Retention_and_Decay_Profile_v0_1.md`. | `DEFERRED` |

---

## 9. Conformance issues

| ID | Type | Priority | Issue | Required action | Status |
|---|---|---:|---|---|---|
| `OI-CONF-001` | `CONF` | `P0` | Conformance matrix needed. | `CLI_Agent_Conformance_Test_Matrix_v0_1.md` available. | `RESOLVED` |
| `OI-CONF-002` | `CONF` | `P0` | Safe fixture pack needed. | `CLI_Agent_Conformance_Fixture_Pack_v0_1.md` available. | `RESOLVED` |
| `OI-CONF-003` | `CONF` | `P0` | Automated conformance runner missing. | Build after schemas and local checker. | `OPEN` |
| `OI-CONF-004` | `CONF` | `P0` | Evidence packets not generated. | Generate during actual test runs. | `OPEN` |
| `OI-CONF-005` | `CONF` | `P0` | Red-line drill records not executed. | Execute after fixtures/runner. | `OPEN` |

---

## 10. Future companion backlog

These are useful but not required for immediate hygiene/schemas handoff:

| File | Priority | Status | Purpose |
|---|---:|---|---|
| `CLI_Agent_Provider_Profile_OpenAI_Codex_v0_1.md` | P2 | `DEFERRED` | Provider-specific Codex boundary, if public/provider claims are needed. |
| `CLI_Agent_Provider_Profile_Google_Gemini_v0_1.md` | P2 | `DEFERRED` | Gemini-specific reader/reviewer boundary. |
| `CLI_Agent_Legal_Handoff_Profile_v0_1.md` | P2/P1 depending use | `DEFERRED` | Counsel/provider/regulator packet boundary. |
| `CLI_Agent_UI_State_Surface_v0_1.md` | P2/P1 depending implementation | `DEFERRED` | UI display of agent state, gates, freezes, cloud warnings. |
| `CLI_Agent_Retention_and_Decay_Profile_v0_1.md` | P2 | `DEFERRED` | Retention windows for logs, witness, cloud outputs, memory proposals. |
| `CLI_Agent_Cross_c_Isolation_Profile_v0_1.md` | P2 | `DEFERRED` | Prevent residue between Ester, Liya, and other `c`. |
| `CLI_Agent_Cost_and_Budget_Profile_v0_1.md` | P2 | `DEFERRED` | Token/cost/runtime guardrails. |

---

## 11. Acceptance checklist before Codex schema/hygiene handoff

- [x] README exists.
- [x] Release notes exist.
- [x] Open issues exists.
- [x] Contradiction register exists.
- [x] Package index exists.
- [x] Public redaction profile exists.
- [x] Release public surface profile exists.
- [x] Readiness gate exists.
- [x] Raw evidence sidecar exists.
- [x] AB/gate semantics exists.
- [x] Registry profile exists.
- [x] Local checker profile exists.
- [x] Schema object registry exists.
- [x] Semantic validator rules exist.
- [x] SCDP / CTM / Package Index source availability corrected.
- [ ] Duplicate sandbox/worktree source variant resolved.
- [ ] Final repository placement chosen.
- [ ] P0 schema extraction contract written.
- [ ] Codex task contract prepared with no publish/tag/push authority.

---

## 12. Closing rule

A known gap is a work item.

An untracked gap is an attack surface.

Final rule:

```text
Do not hide incompleteness.
Classify it, bound it, and make it executable as a next safe task.
```
