---
type: glossary
date: 2026-11-05
course: R3.4:Tasks2
object: DQ Issue Remediation / Контроль устранения проблем с качеством данных
status: draft v0.2 (checked against FPF Library, snapshot 20261105T075950Z)
---

# Glossary: DQ Issue Remediation

> Source of the assignment: MimEcoSys/docs, `professional/modeling-2/04-practice-of-creating-models/08-compiling-a-domain-glossary-optional-assignment.md` (commit faed795, 2026-11-04).
> Description it serves: "Check-list How good look like for DQ Issue Remediation" (R3.4:Mod1–Mod2). Languages: English, DQ domain, project domain.

## 1. Exocortex and glossary method

**Exocortex:** my personal IWE repository (`DS-my-strategy` on GitHub), made of plain Markdown files under version control and indexed for search by the IWE assistant.

**How the glossary is kept:**
- one file per domain (`glossary-dq-issue-remediation.md`), one section per concept;
- every entry has the same fields: *Definition*, *Type* (individual / class, and the kind: object, role, state, work, method, description, characteristic, condition, commitment, judgement), *Related*, *Not to be confused with*;
- cross-references are Markdown anchor links (`[DQ Rule](#dq-rule)`), so the glossary works as a small concept graph;
- Git history shows when and why a definition changed. A definition gets revised when using it in the checklist exposes a gap.

## 2. Key concepts

### Data Quality Issue
- **Definition:** a mismatch between data and an agreed quality expectation, detected by a [DQ Check](#dq-check) or reported by a user, and handled until [Closure](#closure). The issue record in the register is a description of the issue, not the issue itself.
- **Type:** class (each specific issue is an individual; the issue ID identifies its record).
- **Related:** [DQ Rule](#dq-rule), [Issue Lifecycle](#issue-lifecycle), [Issue Owner](#issue-owner).
- **Not to be confused with:** an *incident* (ITSM: a service disruption) or a *defect in the data itself*. An issue can turn out to be a false positive.

### DQ Rule
- **Definition:** a stated expectation about data (for example, "GTIN is 13 digits and passes the checksum"), linked to a [DQ Dimension](#dq-dimension) and a [Threshold](#threshold).
- **Type:** class of descriptions (a method-level description, not a run).
- **Related:** [DQ Check](#dq-check), [Data Element](#data-element).
- **Not to be confused with:** a DQ Check. The rule is the description; the check is the work of applying it.

### DQ Check
- **Definition:** one execution of a [DQ Rule](#dq-rule) against a dataset at a given time, producing a pass rate.
- **Type:** class of work (each run is an individual work occurrence). The pass rate is a characteristic value on a % scale.
- **Related:** [Threshold](#threshold), [Data Quality Issue](#data-quality-issue), [Verification](#verification).

### DQ Dimension
- **Definition:** the characteristic of data a rule refers to: completeness, validity, uniqueness, consistency, timeliness or accuracy.
- **Type:** characteristic (each with its own scale).
- **Related:** [DQ Rule](#dq-rule).

### Threshold
- **Definition:** a condition on a check result, for example "pass rate ≥ 98 %". If the condition is not met, a [Data Quality Issue](#data-quality-issue) is raised.
- **Type:** condition (comparison operator + cut value on a declared scale).
- **Related:** [DQ Rule](#dq-rule), [DQ Check](#dq-check).
- **Not to be confused with:** the check result itself, or with a decision.

### Data Element
- **Definition:** the attribute or field that a rule evaluates, located in a [Source System](#source-system) and catalogued in the DG/DQ system.
- **Type:** class (each catalogued attribute is an individual).
- **Related:** [DQ Rule](#dq-rule), [Data Steward](#data-steward).

### Source System
- **Definition:** the system where the data is created or changed, and therefore where [Remediation](#remediation) has to happen.
- **Type:** class of systems (individuals: SAP ERP, CRM, …).
- **Related:** [Issue Owner](#issue-owner), [Root Cause](#root-cause).

### Issue Owner
- **Definition:** the role of driving one issue to [Closure](#closure): deciding the fix, coordinating the source team and confirming the result.
- **Type:** role. *Assignment:* a specific person is assigned to each issue; being accountable is that person's commitment, not part of the role.
- **Related:** [Data Steward](#data-steward), [Remediation SLA](#remediation-sla).
- **Not to be confused with:** the person who performs the fix, who often sits in the source-system team.

### Data Steward
- **Definition:** the role of looking after data quality in a domain: triaging issues, assigning [Issue Owners](#issue-owner) and keeping [DQ Rules](#dq-rule) relevant.
- **Type:** role. *Assignment:* a specific person is assigned per data domain.
- **Related:** [Issue Owner](#issue-owner), [Data Element](#data-element).

### Root Cause
- **Definition:** the reason the data became wrong (a process gap, an input-form error, an integration bug), as distinct from the symptom the check detected.
- **Type:** class (a claim about a cause, supported by evidence).
- **Related:** [Remediation](#remediation).

### Remediation
- **Definition:** the work of fixing the issue: correcting the affected records and, where feasible, removing the [Root Cause](#root-cause) so the issue does not recur.
- **Type:** class of work.
- **Related:** [Verification](#verification), [Source System](#source-system).
- **Not to be confused with:** *resolution*. An issue can be resolved without remediation (false positive, accepted risk).

### Verification
- **Definition:** re-running the [DQ Check](#dq-check) after [Remediation](#remediation) to confirm that the result meets the [Threshold](#threshold).
- **Type:** class of work. It is the step that turns tracking into control.
- **Related:** [Closure](#closure).

### Issue Lifecycle
- **Definition:** the model of states an issue moves through: *Open → Assigned → In Remediation → Verification → Closed*, with exits to *Rejected* (false positive) and *Accepted Risk*.
- **Type:** description (a state model shared by all issues). The actual state history of a specific issue is a separate, individual description.
- **Related:** [Closure](#closure), [Remediation SLA](#remediation-sla).

### Closure
- **Definition:** the final state of an issue, reached only after successful [Verification](#verification) or a documented decision to reject the issue or accept the risk.
- **Type:** state of an issue.
- **Related:** [Issue Lifecycle](#issue-lifecycle).

### Remediation SLA
- **Definition:** a commitment to bring an issue to [Closure](#closure) within an agreed time, per lifecycle stage or end to end. Its fulfilment is checked against the actual cycle time, measured separately as wait time and touch time.
- **Type:** commitment; the actual cycle time is a characteristic (days).
- **Related:** [Issue Lifecycle](#issue-lifecycle), [Issue Owner](#issue-owner).

### Readiness (project domain)
- **Definition:** a judgement that the new DQ Issue Remediation system meets the checklist criteria and can play its role in the supersystem: rules, owners, lifecycle and SLA are agreed, and the loop has been run end to end at least once.
- **Type:** judgement about the state of the system being introduced, against declared criteria; the checklist "How good looks like" states the criteria.
- **Related:** all of the above.
- **Not to be confused with:** the state of the system itself, or a score.

---

## Changes v0.1 → v0.2 (FPF check, 05.11)

- Data Quality Issue: issue ≠ issue record (A.7).
- DQ Dimension: characteristic, not a class (C.16.P:5).
- Threshold: condition with operator and cut value, not a characteristic value (C.16.P:5).
- Remediation SLA: commitment, measured by cycle time (A.2.8, A.2.3).
- Readiness: judgement against declared criteria (FPF.Reference:7, C.16.P:5).
- Issue Owner, Data Steward: role vs assignment vs commitment (A.2).
- Issue Lifecycle: shared state model vs individual state history.

## Open points (to check against the real setup)

- SLA value, lifecycle states and the example source systems (SAP ERP, CRM) are placeholders.
- Next step for R3.4:Tasks2: publish in the blog and add the link here.
