---
type: model
date: 2026-11-06
course: R3.4:9, R3.4:Mod5
object: DQ Issue Remediation Control System
status: v0.3 (checked against FPF Library, snapshot 20261106T052652Z)
---

# Attributes and relations: DQ Issue Remediation Control System

> Assignment source: MimEcoSys/docs, `professional/modeling-2/04-practice-of-creating-models/16-object-descriptors-and-relationships.md` and `17-specifying-attributes-and-relations.md` (commit faed795, 2026-11-04).
> Builds on: `levels-of-detail-dq-issue-remediation.md` (v0.2), `classifiers-dq-issue-remediation.md` (v0.2), `glossary-dq-issue-remediation.md` (v0.2).

**Conventions (FPF C.16:5.2):**
- Every numeric attribute names its unit and its time stance ("When taken").
- "Working hours" / "working days" are counted by the declared team working calendar (country, working hours, public holidays) - to be fixed once for the system.
- Severity is an ordinal scale: no averaging; report only the distribution by class.

## Table 1. Attributes

| Object | Attribute (interval marked) | Unit | When taken | Classifier |
|---|---|---|---|---|
| DQ Issue Remediation Control System | Identifier: system name | — | — | — |
| | Operating model | — | at readiness judgement date | DQ control operating models |
| | Coverage: number of data domains under control | count | at readiness judgement date | Data domains |
| | Date of the first end-to-end cycle run | date | — | — |
| Subsystem (detection / registration / coordination) | Identifier: subsystem name | — | — | Functional subsystems of DQ control |
| | Setup status | — | at readiness judgement date | Setup statuses |
| DG/DQ platform module | Identifier: module name | — | — | DG/DQ platform modules |
| | Version | version number | at readiness judgement date | — |
| Team member | Identifier: corporate login | — | — | — |
| | Role | — | — | Data management roles |
| | Domain of responsibility | — | — | Data domains |
| | Share of time on the role | % FTE | per calendar month | — |
| Data Quality Issue | Identifier: **issue record number** DQ-NNNN | — | — | — |
| | Quality dimension | — | — | Issues by quality dimension |
| | Severity (ordinal) | — | at assignment | Issue severity classes (with membership criterion) |
| | Detection channel | — | — | Issues by detection channel |
| | Current state | — | at query time (state history kept separately) | Issue lifecycle states |
| | Detection date and time | date-time | — | — |
| | Number of affected records | count | at detection | — |
| | Closure outcome | — | at closure | Closure outcomes |
| DQ Rule | Identifier: rule code | — | — | — |
| | Rule type | — | — | DQ rule types |
| | Threshold: comparison operator + cut value (for a class of rules - **interval**, e.g. 95–99 %) | % of passed records | — | — |
| | Run frequency | runs per day | — | — |
| Check run | Identifier: rule code + run date-time | — | — | — |
| | Pass rate | % of passed records | at run time | — |
| | Number of checked records | count | at run time | — |
| | Number of failed records | count | at run time | — |
| Issue handling cycle | Wait time per stage | working hours | per one handling cycle | Issue lifecycle states (stage) |
| | Touch time | working hours | per one handling cycle | — |
| | Cycle time Open → Closed | working days | per one handling cycle | — |
| | Number of returns for rework | count | per one handling cycle | — |
| Remediation SLA agreement | Agreed time per severity class (**interval**, e.g. "critical: ≤ 2") | working days | — | Issue severity classes |
| Root cause claim | Root cause class | — | — | Root cause classes |
| | Supported by evidence | yes / no | — | — |
| Data Element | Identifier: system.table.field | — | — | — |
| | Data domain | — | — | Data domains |
| | Data class | — | — | Data classes by role in records |
| Source System | Identifier: code in the IT registry | — | — | — |
| | System class | — | — | Source system classes |
| Readiness judgement | Judgement date | date | — | — |
| | Verdict | — | at judgement date | Readiness verdicts |
| | Number of unmet checklist items | count | at judgement date | — |

## Table 2. Relations (S - P - O)

| Subject | Relation | Object |
|---|---|---|
| Check run | applies | DQ Rule |
| DQ Rule | checks | Data Element |
| Data Element | is stored in | Source System |
| Data Quality Issue | is detected by | Check run |
| Data Quality Issue | manifests in the values of | Data Element |
| Issue record | describes | Data Quality Issue |
| Team member (role: issue owner) | is assigned to | Data Quality Issue |
| Team member (role: data steward) | is responsible for | Data domain |
| Root cause claim | explains | Data Quality Issue |
| Root cause claim | is supported by | Evidence |
| Remediation | is performed in | Source System |
| Remediation | is aimed at | Root cause claim |
| Verification | checks the threshold after | Remediation |
| Remediation SLA agreement | applies to | Data Quality Issue (by severity class) |
| Checklist "How good looks like" | sets the criteria for | Readiness judgement |
| Readiness judgement | assesses | DQ Issue Remediation Control System |

## Was the root cause removed? - the rule trend is the evidence

On the day of closure only the records are known to be fixed. Whether the root cause is removed is seen later, from the trend of the same rule's runs:
- the rule stays in monitoring after closure with its usual run frequency;
- the trend is read on the **number of failed records** (count), not on the pass rate: 300 new failures in 100,000 records move the pass rate from 100 % to 99.7 % and look like noise, while the count goes 0 → 300;
- this works when the rule is narrow enough - one data element in one source system. For a rule spanning several systems the trend shows recurrence but not where.

No separate recurrence attribute or matching procedure is needed (decision of 2026-11-06).

## FPF check (v0.1 → v0.2 → v0.3)

1. Time stance added to every numeric attribute (C.16:5.2, M-CSLC-4).
2. Working calendar declared for "working hours/days" (M-CSLC-2).
3. Severity: ordinal, no averaging (M-CSLC-2).
4. Issue identifier = issue record number (A.7, glossary v0.2).
5. "relates to" replaced with the direct relation "manifests in the values of" (A.6.H:4.4).
6. Causal relations kept within support (CAUSAL-USE): root cause is a claim that "explains" and "is supported by evidence"; remediation "is aimed at" it. v0.3: the evidence of success is the trend of the rule's number of failed records after closure (replaces the v0.2 attribute "recurred within 30 days").
7. Verification "checks the threshold after" remediation, instead of "confirms" it.
8. SLA is a commitment that "applies to" an issue (A.2.8).

## Open points

- Team working calendar - to be fixed.
- New classifier "Setup statuses" added to `classifiers-dq-issue-remediation.md` (v0.2).
