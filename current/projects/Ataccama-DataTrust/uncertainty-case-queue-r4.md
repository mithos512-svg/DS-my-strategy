---
type: model
date: 2026-11-22
course: R4.2:7, R4.2:Mod3
problem_card: problem-cards-r4.md, B-2
interventions: interventions-case-queue-r4.md (v1.2)
status: v1.0 (checked against FPF Library C.11.DUA, OPS.10; snapshot 20261122T121956Z)
---

# Remaining uncertainty in the case-queue interventions

> Assignment source: MimEcoSys/docs, `professional/counterfactuality/02-problem-formulation-epistemology-and-problem-solving/12-assessing-and-evaluating-operational-uncertainty.md`; lesson R4.2:7 "Choice and uncertainty" (`11-making-choices-under-uncertainty-conditions.md`), commit faed795, 2026-11-04.

**Principle (R4.2:7):** "not enough information" is too general to help a choice. Name what remains unknown, what kind of unknown it is (a gap in knowledge, normal variability of the work, or someone else's decision), and ask: **"Under which answer does the best option stop being the best?"** The size of an unknown and the usefulness of reducing it are different characteristics.

**FPF guards:**
- Importance is judged relative to a named decision and horizon (C.11.DUA:4.1).
- For each inquiry: which plausible answer would change the choice, and what the inquiry costs - effort, delay, displaced work; compare with a smaller reversible step (C.11.DUA:4.2).
- Future authorization or agreement is not treated as obtained (CC-C11DUA.7).
- Waiting must not be "improved" by moving it outside the measured boundary; keep the requester's waiting origin; a service level computed from history is a conditional forecast, not a guarantee (OPS.10:4.1, 4.4, 4.5).

## Decision served and horizon

**Decision:** whether to launch intervention 1 (regular triage with an explicit "not now"), in what form, and in what order relative to interventions 2 and 3.
**Horizon:** launch in December 2026, check after 6-8 weeks.

## Uncertainty table

| # | Question reflecting uncertainty of the result | Domain | Kind of uncertainty | Importance (1-5) | Why this importance |
|---|---|---|---|---|---|
| 1 | How many of the 100 open cases are still relevant, and how many are obsolete or duplicates? | Observations | Knowledge gap | **3** | Does not change the choice: triage is needed whatever the share. Changes how the check is read: if half the cases are obsolete, the queue shrinks fast without any throughput growth. "Closed as not relevant" and "done" are different populations - counted separately. Cost of the answer: zero, the first 2-3 triage sessions give it. |
| 2 | Where is the constraint: triage (hypothesis a) or engineering pair capacity (hypothesis b)? | Explanation of the problem mechanism | Knowledge gap | **3** | The largest unknown in the model, but the first step does not depend on it: intervention 1 is cheap, reversible and itself distinguishes the hypotheses. The answer decides the second step (intervention 3 or a capacity conversation with the DG lead). A separate study before launch would answer later and cost more than the check of intervention 1. |
| 3 | What share of requesters, after "not now" or a long promised date, will work around the team - own extracts, shadow tables? | Forecast of intervention consequences (risk) | Knowledge gap about behaviour + spread between requesters | **5** | The only answer that can make the best option not the best. If the share is noticeable, the queue shrinks while data quality in the company gets worse - the opposite of the DG/DQ goal. Then "not now" cannot be given without an alternative, or the order of interventions changes. Not estimable as a number now. Interviewing requesters costs the same scarce PM hours, so the cheaper path is a smaller reversible step: **staged launch** (see below) plus a conversation with the 2-3 most frequent requesters. |
| 4 | Will management route urgent assignments through intake and triage, rather than directly to engineers and via chats? | Implementation (authority) | Not knowledge - a management decision | **4** | If urgent assignments bypass triage, intervention 1 controls only part of the arrivals and the check may show "revise" even if hypothesis (a) is true. Not 5: triage still helps. Cost: one conversation with the DG lead before launch. Until agreement exists, the check covers only tracker arrivals, and conclusions must say so. |
| 5 | What counts as "solved", and from which date is waiting measured: "≥ 5 closed per month", or "accepted arrivals ≤ closures, and waiting from the request date within the promised time"? | Criteria for checking the solution | Agreement + normal variability of case durations | **4** | With 9-13 arrivals per month, 5 closed per month still leaves the flow unstable - the criterion could declare success while the queue grows. Second trap: if waiting is counted only for accepted cases, the time a requester spent under "not now" falls outside the measure and the improvement is illusory. Waiting is counted **from the original request date**. Case durations stay spread whatever the data volume, so the criterion is probabilistic ("85 % within the promised time"); a level computed from history is a conditional forecast. The criterion is agreed with the DG lead before start. |

## Robustness of the choice

- Intervention 1 remains the best first step under any answer to questions 1, 2 and 5.
- A "no" from management on question 4 weakens it but does not cancel it.
- Only question 3 can reverse the choice - and it is closed by a staged launch rather than a separate study.
- Before start: two conversations - with the DG lead (urgent assignments, criterion of "solved") and with frequent requesters (workarounds).

## Launch condition for intervention 1 (from question 3)

1. **Stage 1 (first 4 weeks):** "not now" is given only in one case class (e.g., new functions not related to projects A and B); other classes are triaged as "accept / reject" with a date.
2. **Watch:** in the DG/DQ catalog - new unregistered extracts or tables in the domains of "not now" cases; requester reactions recorded at triage.
3. **Extend to all classes** if no workaround signs are found in 4 weeks.
4. **Change the form** if signs are found: "not now" goes only together with an alternative (self-service path, temporary dataset marked with its quality status), or intervention 2 or 3 moves earlier.

Transferred to `interventions-case-queue-r4.md` v1.2 (intervention 1, sections 2, 10, 11).

## Deliberately left out

- **Share of consultations in arrivals (~45 %, assumption) and whether questions are typical** - a large unknown, importance **2**: intervention 3 is third in sequence, and the answer comes for free once case classes exist in the tracker.
- **Where the PM's 1.5 h/week comes from** - not an uncertainty but the PM's own decision; kept as an open item in the interventions file.

## Changes

- v1.0 (2026-11-22): first version after the FPF check - decision and horizon stated; kind of uncertainty per question; cost of inquiry and smaller reversible step (question 3); agreement not treated as obtained (question 4); waiting origin = request date and history-based level as conditional forecast (question 5); separate populations for "closed as not relevant" and "done" (question 1).

---

Sources: R4.2:7, R4.2:Mod3 (MimEcoSys/docs, commit faed795); FPF Library `C.11.DUA:4`, `C.11.DUA:7` (https://fpf.tools/C.11.DUA:4), Operations Management DPF `OPS.10:4` (https://fpf.tools/OPS.10:4), snapshot 20261122T121956Z-917bf0c06314fe32.
