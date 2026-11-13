---
type: model
date: 2026-11-13
course: R4.1:Tasks1
object: Case in the DG/DQ team case management
time_scope: run time (current operation)
status: v1.0 (checked against FPF Library, snapshot 20261112T230943Z)
---

# Case journey through the DG/DQ team - production chain and flow

> Assignment source: MimEcoSys/docs, `professional/counterfactuality/01-using-workflow-models-in-enterprise-operations/05-describing-and-mapping-the-production-chain.md` (commit faed795, 2026-11-04).
> Object changed on 2026-11-13: first draft used the catalog item journey (R2.6); replaced by the case journey because cases show the real flow problem of the team.

## 1. The journeying object

A **case** in the team's case management: a request to the DG/DQ team that goes from acceptance to a result confirmed by the case requester. The request (work to be done) and the case card in the tracker (its description) are kept apart; we measure by the card and talk about the movement of the request (FPF A.7).

Case classes (different routes and touch times):

| Class | Example |
|---|---|
| User consultation | "how do I find a dataset", "what does this term mean" |
| Management question | request for a summary, analysis, status |
| New function | configuration, new rule, new report |
| System development | larger changes, integrations - **counted as a separate class** (decision 2026-11-13) |

## 2. Segment and workstations

| Workstation | Who works | Classes |
|---|---|---|
| Triage and prioritisation | team lead / duty person | all |
| Clarification with the requester | assignee ↔ requester | all, often |
| Analysis and solution | analyst / steward / engineer | all |
| Implementation (configuration, development) | engineer; sometimes IT or vendor | new function, development |
| Review | second team member / testing | new function, development |
| Hand-over and confirmation | assignee → requester | all |

The queue before triage (created, not yet accepted) is outside the segment - but the tracker does not separate it today (see §8).

## 3. Start event and state

**Event:** case accepted into work - triaged, assignee set, priority set (commitment point).
**State:** it is known who works on it and with which priority; the request content may still be incomplete.

## 4. End event and state

**Event:** the requester received the result and confirmed it; the case is closed as resolved.
**State:** result delivered and accepted. Cases closed without resolution (duplicate, rejected, "not ours") are not throughput; counted separately.

## 5-7. Observed figures and flow time

| Quantity | Value | Status |
|---|---|---|
| Open cases (WIP) | 100 | observation, 2026-11-13; no split by class; includes cases not yet accepted |
| Throughput (closed) | 2-3 per month | observation |
| Arrivals (created) | 2-3 per week ≈ 9-13 per month | observation |
| Little's law: WIP / throughput | 100 / 2-3 ≈ 33-50 months (≈ 40) | calculation - valid only for a stable flow, see below |

**The flow is not stable.** Arrivals (≈ 9-13 per month) are about four times the throughput (2-3 per month). WIP grows by about 7-10 cases per month. Under these conditions Little's law does not describe a steady state (FPF OPS.Reference:1.3: it relates consistent long-run averages); the ≈ 40 months is a **lower bound** for a new case under first-in-first-out, and it keeps growing. With prioritisation, some cases pass quickly and others effectively never.

## 8. Touch time (estimate from experience)

| Class | Touch time |
|---|---|
| User consultation | 0.5-2 h |
| Management question | 1-4 h |
| New function | 1-3 working days |
| System development | weeks |

Even at one full working day per case on average, touch time is under 0.1 % of the computed flow time.

## 9. Where the waiting comes from

**Observation (2026-11-13):** all 10 oldest open cases are waiting for resources to be freed. This confirms real overload and rejects, for these cases, the hypotheses "resolved but not closed" and "no longer relevant". Caveat: the oldest cases are a biased sample - they are likely the deprioritised ones; the rest of the 100 may contain resolved or dead cases.

**Main explanation:** a capacity gap. The team closes 2-3 cases per month while 9-13 arrive. Cases most likely get the capacity left over from other work (projects, operations) - there is no reserved capacity for the case flow. Waiting is therefore mostly **queue time for a free resource**, not waiting inside the work.

Further hypotheses (to check by reading case histories, since the tracker has no waiting statuses):

| Hypothesis | Check |
|---|---|
| Management questions jump the queue and interrupt started work | cases of other classes paused while an urgent case was done |
| Waiting for clarification from requesters | time between assignee question and requester answer in comments |
| Waiting for other teams (IT, vendor) | mentions of external teams in history |
| Many cases per person, switching | open cases per assignee |
| Closure lag (result delivered, not confirmed) | time from hand-over to closure |

## Data limitations

- No split by case class - the average mixes one-hour consultations and multi-month development.
- No waiting statuses - waiting causes can be checked only by sampling histories.
- No "created" vs "accepted" separation - the start boundary is blurred; WIP includes the queue before triage.

## Inputs for the next R4 tasks (improvement candidates)

- Make the capacity gap explicit: arrivals vs throughput per month, reported regularly.
- Reserve capacity for the case flow, or limit admission (WIP limit, explicit "not now" decision).
- Introduce case classes and a separate "accepted into work" point.
- Introduce waiting statuses (waiting for requester / external team).
- Review the open backlog: close resolved and no longer relevant cases.

## FPF check

- Little's law applied with consistent boundaries and checked for stability (OPS.Reference:1.3); instability stated explicitly.
- Measurement constructions named: interval start/end, population, window (OPS.15.1:2).
- Units: flow time in calendar months; touch time in working hours/days (C.16:5.2).
- Epistemic status per figure: observation / calculation / estimate / hypothesis; waiting causes kept as hypotheses with checks (CAUSAL-USE).
