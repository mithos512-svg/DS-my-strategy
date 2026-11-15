---
type: model
date: 2026-11-15
course: R4.1:12, R4.1:Tasks4
object: Case flow of the DG/DQ team
time_scope: run time (current operation) + plan
status: v1.0 (checked against FPF Library, snapshot 20261114T101245Z)
builds_on: case-journey-flow-r4.md, case-flow-physics-r4.md, case-flow-constraint-r4.md
---

# Operational mantra - progress of the case flow

> Assignment source: MimEcoSys/docs, `professional/counterfactuality/01-using-workflow-models-in-enterprise-operations/17-applying-the-operational-mantra-in-practice.md` (commit faed795, 2026-11-04).

**Context:** the company produces chocolate; the team develops the data catalog and data quality. Team: product manager (triage), 2 engineers DQ, 2 engineers Data Catalog / Lineage, no analysts. **All changes in steps 7-9 are planned, none introduced yet (2026-11-15).**

| # | Mantra step | Status | Content |
|---|---|---|---|
| 1 | Enterprise output and its link to our work | partly | output: chocolate; our contribution: trusted data (catalogued, quality-checked, with lineage) for product data, planning, labelling, reporting; impact on financial throughput not visible to the team |
| 2 | Enterprise throughput rate | not done | outside the team's authority (no access to output and money data) |
| 3 | Object path through the enterprise | partly | data path modelled in R2 (catalog item journey); no enterprise-level model |
| 4 | Our place and our output | done (analysis) | object: case; throughput 2-3/month vs arrivals 9-13; 100 open; Little ≥ 40 months, unstable. Gap is visible to the PM, not yet shown to management |
| 5 | Critical chain | identified | projects A and B wait for our participation and work products; their cases sit in the common queue without a "blocks project" flag. Plan: flag at triage, start first; late start for the rest, keep tracking |
| 6 | Constraint and causes | hypothesis | triage (PM): demand ≈ 11.5 h/month vs ≈ 4.3 h, ≈ 270 %, 40 untriaged; next: both engineering pairs (≈ 115 %); policy constraint: urgent management questions stop everything. **Rival:** engineers are the constraint, untriaged queue is a symptom. **Distinguish:** after regular triage - throughput up → triage was the constraint; engineering queues up, throughput flat → engineers (OPS.9:0) |
| 7 | Subordinate to the constraint | plan | weekly triage slot 1.5 h (accept / not now / reject); DBR buffer of 2-3 clarified new functions per pair, pulled by the pair; duty engineer per pair for urgent questions. Adding people: not in the team's authority; "not yet supported by data" (OPS.9:0) - measurements can become the basis |
| 8 | Method changes | plan | intake template (class, domain, need, date, dependency on A/B); case classes and per-station statuses; knowledge base for typical questions |
| 9 | Org changes and expected acceleration | plan | dedicated case time; duty rule for urgent questions; regular arrivals/closed report to management |

## Step 9 - prediction (to be tested, OPS.16)

- Triage slot alone: triage utilisation ≈ 270 % → ≈ 180 % (6.5 h/month vs 11.5 h demand).
- Slot + intake template (triage 0.25 h/case, clarification 0.5 h/function): demand ≈ 4.7 h/month → ≈ 73 %; triage stops being the constraint.
- Duty rotation: should reduce switching losses.
- **Predicted throughput: 5-6 cases/month after two months.** Check in the tracker; if not reached, find the failed assumption.
- Still below arrivals (9-13): without explicit "not now" the queue keeps growing.

## Jerk (C.16)

Jerk = acceleration of acceleration: throughput rate (cases/month) → acceleration (change per month) → jerk (change of acceleration per month). Needs at least 3-4 monthly points after the changes - not computable yet. Comparison now only by time to effect and expected growth shape:

| Option | Time to effect | Expected shape | Cost |
|---|---|---|---|
| Triage slot + intake template | 2-4 weeks | step | almost free |
| Duty rotation in pairs | 1-2 months | gradual | team agreement |
| More engineer time for cases | immediately | step | takes time from projects incl. A and B |
| Analyst in the team | months | growth after onboarding | budget, outside the team's authority |

## FPF check

- Constraint account with a rival explanation and a distinguishing observation (OPS.9:0).
- Prediction separated from observation and implementation decision (OPS.16:4.1).
- "Jerk" used in the course's sense; time-to-effect named as a different characteristic (C.16:5.2).
- Causal wording within support: "should reduce", not "removes" (CAUSAL-USE).
- "Infeasible" restated as an authority boundary, not a physical limit.
