---
type: model
date: 2026-11-05
course: R3.4:8, R3.4:Mod4
object: DQ Issue Remediation Control System
status: v0.1 (checked against FPF Library C.16.P:5)
---

# Classifiers: DQ Issue Remediation Control System

> Assignment source: MimEcoSys/docs, `professional/modeling-2/04-practice-of-creating-models/14-classifiers-and-classification-schemes.md` and `15-specifying-classifiers-and-categories.md` (commit faed795, 2026-11-04).
> Description: checklist template "How good looks like for DQ Issue Remediation". Upper ontology: 4D extensionalism (BORO), as in the course. Objects and parts come from `levels-of-detail-dq-issue-remediation.md` (v0.2); terms from `glossary-dq-issue-remediation.md` (v0.2).

Types (R3.2): CFO - class of functional objects; CMO - class of material objects; TP - temporal part; D - description.

## Table for R3.4:Mod4

| Object | Classifier (class of classes) | Example classes |
|---|---|---|
| DQ Issue Remediation Control System :: CFO | DQ control operating models | centralised; federated (by domain); hybrid |
| Subsystem (detection / registration / coordination) :: CFO | Functional subsystems of DQ control | issue detection; registration and routing; remediation coordination; reporting |
| DG/DQ platform module :: CMO | DG/DQ platform modules | data catalog; DQ module; issue register and workflow; lineage |
| Team member :: CMO (in a role) | Data management roles | data steward; data owner; issue owner; data engineer |
| Data Quality Issue | Issues by quality dimension | completeness issue; validity issue; uniqueness issue; timeliness issue |
| | Issue severity classes | critical; high; medium; low |
| | Issues by detection channel | automated check; user report; audit |
| | Closure outcomes | remediated; rejected (false positive); risk accepted |
| DQ Rule :: D | DQ rule types | format rule; allowed-values rule; referential-integrity rule; cross-system consistency rule |
| Issue handling cycle and its parts :: TP | Issue lifecycle states | open; assigned; in remediation; in verification; closed |
| Root Cause | Root cause classes | input error; process gap; integration failure; change in source system |
| Data Element (context) | Data domains | product; customer; supplier; material |
| | Data classes by role in records | master data; reference data; transactional data |
| Source System (context) | Source system classes | ERP; CRM; PLM; file extracts |
| Readiness (checklist judgement) | Readiness verdicts | ready; ready with remarks; not ready |

## Notes

**Meta-U sources (do not invent):** roles and quality dimensions - DAMA-DMBOK; data quality characteristics - ISO/IEC 25012; data domains and source system classes - the organisation's MDM / reference data practice (R3.4:8 links classifiers directly to master data management).

**FPF check (C.16.P:5):**
- A *quality dimension* is a characteristic, not a class. The classifier therefore classifies issues ("issues by quality dimension"), not dimensions.
- *Severity* is a characteristic on an ordinal scale. Its values may serve as classes only with a membership criterion in the template, e.g. "critical - blocks reporting or a regulatory submission". Without it, severity is assigned by feel.

**Not included:** threshold and remediation SLA are a condition and a commitment; their values are attributes (R3.4:Mod5), not classifiers.

## Open points

- Operating model, platform modules and data domains are placeholders - replace with the real setup.
- Severity membership criteria to be agreed with the team.
