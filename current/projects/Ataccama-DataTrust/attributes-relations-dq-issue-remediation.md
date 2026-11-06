---
type: model
date: 2026-11-06
course: R3.4:9, R3.4:Mod5
object: DQ Issue Remediation Control System
time_scope: design time (pre-operation readiness)
status: v0.4 (checked against FPF Library, snapshot 20261106T052652Z)
---

# Attributes and relations: DQ Issue Remediation Control System

> Assignment source: MimEcoSys/docs, `professional/modeling-2/04-practice-of-creating-models/16-object-descriptors-and-relationships.md` and `17-specifying-attributes-and-relations.md` (commit faed795, 2026-11-04).
> Builds on: `levels-of-detail-dq-issue-remediation.md` (v0.3), `classifiers-dq-issue-remediation.md` (v0.2), `glossary-dq-issue-remediation.md` (v0.3).

**Time scope: design time (pre-operation readiness).** The checklist checks that the way of working is *defined and set up*, not that the work *goes well*. Its subject is the system before launch. Values that appear during operation (per-issue times, trends, outcomes) belong to a different description - an operation report (FPF B.3.3:4, CC-B3.3.5: design-time and run-time claims keep distinct subjects, evidence and conditions).

How to read the tables below:
- **Table 1** is the **data model of future operation**. For the checklist, each attribute is a set-up item: the field exists in the register or platform, with its unit, time stance and classifier. Attribute *values* are not checked by the checklist (except the attributes of the readiness judgement itself and of set-up objects - system, subsystems, modules, team members, rules, SLA agreement).
- **Table 2** lists relations that will hold in operation. Their design-time counterpart is a set-up rule (e.g. "issue owner assignment rule configured"), not a specific assignment.

**Conventions (FPF C.16:5.2):**
- Every numeric attribute names its unit and its time stance ("When taken").
- "Working hours" / "working days" are counted by the declared team working calendar (country, working hours, public holidays) - to be fixed once for the system.
- Severity is an ordinal scale: no averaging; report only the distribution by class.

## Table 1. Attributes

Column "Scope": **D** - value is set at design time (checked by the checklist); **R** - field is set up at design time, value appears only in operation.

| Object | Attribute (interval marked) | Unit | When taken | Classifier | Scope |
|---|---|---|---|---|---|
| DQ Issue Remediation Control System | Identifier: system name | — | — | — | D |
| | Operating model | — | at readiness judgement date | DQ control operating models | D |
| | Coverage: number of data domains under control | count | at readiness judgement date | Data domains | D |
| | Date of the trial end-to-end run on pilot data | date | — | — | D |
| Subsystem (detection / registration / coordination) | Identifier: subsystem name | — | — | Functional subsystems of DQ control | D |
| | Setup status | — | at readiness judgement date | Setup statuses | D |
| DG/DQ platform module | Identifier: module name | — | — | DG/DQ platform modules | D |
| | Version | version number | at readiness judgement date | — | D |
| Team member | Identifier: corporate login | — | — | — | D |
| | Role | — | — | Data management roles | D |
| | Domain of responsibility | — | — | Data domains | D |
| | Planned share of time on the role | % FTE | per calendar month | — | D |
| Data Quality Issue | Identifier: **issue record number** DQ-NNNN | — | — | — | R |
| | Quality dimension | — | — | Issues by quality dimension | R |
| | Severity (ordinal) | — | at assignment | Issue severity classes (with membership criterion) | R |
| | Detection channel | — | — | Issues by detection channel | R |
| | Current state | — | at query time (state history kept separately) | Issue lifecycle states | R |
| | Detection date and time | date-time | — | — | R |
| | Number of affected records | count | at detection | — | R |
| | Closure outcome | — | at closure | Closure outcomes | R |
| DQ Rule | Identifier: rule code | — | — | — | D |
| | Rule type | — | — | DQ rule types | D |
| | Threshold: comparison operator + cut value (for a class of rules - **interval**, e.g. 95–99 %) | % of passed records | — | — | D |
| | Run frequency | runs per day | — | — | D |
| Check run | Identifier: rule code + run date-time | — | — | — | R |
| | Pass rate | % of passed records | at run time | — | R |
| | Number of checked records | count | at run time | — | R |
| | Number of failed records | count | at run time | — | R |
| Issue handling cycle | Wait time per stage | working hours | per one handling cycle | Issue lifecycle states (stage) | R |
| | Touch time | working hours | per one handling cycle | — | R |
| | Cycle time Open → Closed | working days | per one handling cycle | — | R |
| | Number of returns for rework | count | per one handling cycle | — | R |
| Remediation SLA agreement | Agreed time per severity class (**interval**, e.g. "critical: ≤ 2") | working days | — | Issue severity classes | D |
| Root cause claim | Root cause class | — | — | Root cause classes | R |
| | Supported by evidence | yes / no | — | — | R |
| Data Element | Identifier: system.table.field | — | — | — | D |
| | Data domain | — | — | Data domains | D |
| | Data class | — | — | Data classes by role in records | D |
| Source System | Identifier: code in the IT registry | — | — | — | D |
| | System class | — | — | Source system classes | D |
| Readiness judgement | Judgement date | date | — | — | D |
| | Verdict | — | at judgement date | Readiness verdicts | D |
| | Number of unmet checklist items | count | at judgement date | — | D |

## Table 2. Relations (S - P - O)

Column "Design-time counterpart": what the checklist checks instead of the operational relation.

| Subject | Relation | Object | Design-time counterpart |
|---|---|---|---|
| Check run | applies | DQ Rule | rule scheduled with run frequency |
| DQ Rule | checks | Data Element | rule bound to the data element (D) |
| Data Element | is stored in | Source System | source system identified for each data element in scope (D) |
| Data Quality Issue | is detected by | Check run | issue creation on threshold breach configured |
| Data Quality Issue | manifests in the values of | Data Element | issue record links to the data element (field exists) |
| Issue record | describes | Data Quality Issue | issue record template set up |
| Team member (role: issue owner) | is assigned to | Data Quality Issue | issue owner assignment rule configured |
| Team member (role: data steward) | is responsible for | Data domain | a steward assigned for each domain in scope (D) |
| Root cause claim | explains | Data Quality Issue | root cause field with classifier and evidence link set up |
| Root cause claim | is supported by | Evidence | — |
| Remediation | is performed in | Source System | remediation contact in each source system team agreed |
| Remediation | is aimed at | Root cause claim | — |
| Verification | checks the threshold after | Remediation | re-check step present in the workflow before closure |
| Remediation SLA agreement | applies to | Data Quality Issue (by severity class) | SLA agreed per severity class; working calendar fixed (D) |
| Checklist "How good looks like" | sets the criteria for | Readiness judgement | (D) |
| Readiness judgement | assesses | DQ Issue Remediation Control System | (D) |

## Was the root cause removed? - the rule trend is the evidence (operation)

This is a run-time question per issue: on the day of closure only the records are known to be fixed; whether the root cause is removed is seen later, from the trend of the same rule's runs, read on the **number of failed records** (not the pass rate), for a rule narrow enough (one data element in one source system).

**Design-time checklist item:** "After closure the rule stays in monitoring; review of the trend of the number of failed records is assigned (who, when - e.g. at Week Close)."

## Trial run - the only place the checklist relies on performed work

The readiness judgement uses one piece of performed work: a **trial end-to-end run on pilot data** (detection → assignment → remediation → verification → closure). Per CC-B3.3.5 it shows that *the configured loop can be passed*, not that *the system will perform in operation*. Checklist wording: "trial run on pilot data passed from detection to closure", not "the system works".

## FPF check (v0.1 → v0.4)

1. Time stance added to every numeric attribute (C.16:5.2, M-CSLC-4).
2. Working calendar declared for "working hours/days" (M-CSLC-2).
3. Severity: ordinal, no averaging (M-CSLC-2).
4. Issue identifier = issue record number (A.7, glossary v0.2).
5. "relates to" replaced with the direct relation "manifests in the values of" (A.6.H:4.4).
6. Causal relations kept within support (CAUSAL-USE): root cause is a claim that "explains" and "is supported by evidence"; remediation "is aimed at" it. v0.3: the evidence of success is the trend of the rule's number of failed records after closure.
7. Verification "checks the threshold after" remediation, instead of "confirms" it.
8. SLA is a commitment that "applies to" an issue (A.2.8).
9. v0.4: design time / run time separated (B.3.3:4, CC-B3.3.5): Scope column D/R in Table 1, design-time counterparts in Table 2, trial run named explicitly; "share of time on the role" made "planned".

## Open points

- Team working calendar - to be fixed.
- New classifier "Setup statuses" added to `classifiers-dq-issue-remediation.md` (v0.2).
