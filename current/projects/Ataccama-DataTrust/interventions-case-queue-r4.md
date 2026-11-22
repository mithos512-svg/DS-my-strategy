---
type: templates
date: 2026-11-22
course: R4.2:6, R4.2:Tasks2
problem_card: problem-cards-r4.md, B-2
status: v1.0
---

# Intervention template and interventions for the case queue

> Assignment source: MimEcoSys/docs, `professional/counterfactuality/02-problem-formulation-epistemology-and-problem-solving/10-planning-and-designing-strategic-interventions.md`; lesson R4.2:6 (commit faed795, 2026-11-04).

**Principle (R4.2:6):** solving a problem needs two explanations - a **negative** one (why the current state is bad) and a **positive** one (why the intervention improves it, for whom, and **which side effects** it causes). Distinguish changes we make **ourselves**, changes that need **others**, and circumstances **outside our control**. Besides removing the cause, consider indirect directions: damage reduction, prevention of recurrence, adaptation, abandoning the activity - and always **"do nothing"**.

## Intervention template

| # | Section | How to fill in |
|---|---|---|
| 0 | Problem and negative explanation | Link to the problem card and its general statement. Short mechanism of how the unfavourable state arises now; if several explanations exist, name them and the one the intervention relies on. |
| 1 | Direction | remove the cause / reduce damage / prevent recurrence / adapt / abandon the activity / do nothing |
| 2 | What we change | Concrete changes in rules, method, tracker, time allocation. For each: **we ourselves** / **needs others (whom)** / **outside our control**. |
| 3 | Mechanism affected | The link of the negative explanation the change acts on; if none (damage reduction, adaptation), say so. |
| 4 | Positive explanation | Chain "change → mechanism → effect → for whom". Without the chain an intervention is a wish. |
| 5 | Undesired consequence reduced or stopped | From the "for whom unfavourable" block of the problem card. |
| 6 | What we adapt to | The condition we do not change - because we cannot or should not. |
| 7 | Feasibility | Resources (time, people, tools), authority (who must agree), time to effect. |
| 8 | Side effects | Now and **under changed circumstances** (demand growth, a person leaving, management priorities change). Who may be worse off. |
| 9 | Compatibility with other measures | Reinforce, hinder or neutral; what must not be introduced at the same time because effects could not be told apart. |
| 10 | Check | **Observe** (quantity, unit, source); **compare with** (baseline before the intervention, observation window); **"solved"** result (threshold); **"revise"** result (threshold or sign); what would show that the rival explanation is true. |

## Problem (card B-2)

**Requests to the DG/DQ team wait for months and the queue keeps growing.**

Negative explanation - two hypotheses, not yet distinguished: (a) triage is done ad hoc and became the constraint (40 untriaged, triage ≈ 270 %); (b) engineering capacity is insufficient regardless of triage (≈ 115 %, 9-13 arrive per month, 2-3 closed). Amplifier: urgent management assignments interrupt other work.

## Intervention 0. Do nothing

- **Direction:** do nothing.
- **What happens:** WIP grows by 7-10 cases/month; ≈ 150 in six months; flow time for new cases keeps growing; projects A and B get results only when their cases break through as urgent.
- **Why consider:** baseline for comparison and the cost of inaction - an argument for the DG lead.

## Intervention 1. Regular triage with an explicit "not now"

0. **Relies on hypothesis (a).**
1. **Direction:** remove the cause + restructure the process.
2. **What we change:** weekly triage slot 1.5 h - **ourselves** (PM); intake template (class, subject, need, date, reason) - **ourselves**; each case gets "accept / not now / reject", "not now" is communicated with a review date - **ourselves**, needs **requesters' agreement** that "not now" is not a refusal; assignments from chats go to the tracker (#workitems post 255) - **ourselves**, needs **agreement with management**.
3. **Mechanism:** the queue before triage and the implicit "everything is accepted".
4. **Positive explanation:** slot + template bring triage utilisation from ≈ 270 % to ≈ 73 % → the 40 untriaged cases get a decision within 4-6 weeks → only accepted cases reach engineers, in priority order → A and B go to their dates, "not now" stops hanging silently in the queue.
5. **Reduces:** months of waiting without an answer; invisibility of demand for management.
6. **Adapts to:** engineering capacity (unchanged).
7. **Feasibility:** 1.5 h/week of PM; template 1-2 days; within team authority; effect in 2-4 weeks.
8. **Side effects:** requesters with "not now" may escalate to management → more urgent assignments. If (a) is wrong, queues just move to the engineers.
9. **Compatibility:** reinforced by 2 ("not now" gets a date); not at the same time as 3 (effects indistinguishable).
10. **Check:** observe - untriaged cases (weekly), cases closed per month, queues at engineering pairs; compare with - baseline 13.11 (40 untriaged, 2-3 closed/month, 21 per pair); **solved** - untriaged ≤ 10 after 6 weeks, closed ≥ 5/month after 2 months; **revise** - throughput flat while engineering queues grow → hypothesis (b), the constraint is at the engineers; talk to the DG lead about capacity.

## Intervention 2. Realistic promises and protection of projects A and B

0. **Not tied to a hypothesis:** acts on consequences, not causes.
1. **Direction:** reduce damage + adapt.
2. **What we change:** publish expected flow time per class with probability (SLE, e.g. "85 % of consultations within N weeks") from tracker history - **ourselves**; the requester gets the expected date at intake, early notice if at risk - **ourselves**; A and B cases get class "fixed date" and a separate time reserve - **needs DG lead and project leads**.
3. **Mechanism:** neither triage nor capacity; changes requesters' expectations and the order for dated work.
4. **Positive explanation:** the requester knows the real date → can re-plan or find a workaround → fewer "when?" follow-ups and fewer surprises; A and B get results by their dates at the expense of other cases.
5. **Reduces:** damage from unknown dates; risk of slipping A and B.
6. **Adapts to:** current capacity and throughput.
7. **Feasibility:** SLE - one day if the tracker has created/closed dates; reserve for A and B - DG lead decision; effect immediately after publication.
8. **Side effects:** published dates may be long (months) and visible; with growing demand dates must be revised constantly; the reserve for A and B slows everything else.
9. **Compatibility:** reinforces 1; no conflict with 3.
10. **Check:** observe - share of cases closed within the promised date, number of status follow-ups, A and B results by their dates; compare with - now no dates are promised; follow-up baseline from the last month (tracker or mail); **solved** - ≥ 85 % within the promised date, follow-ups halved, no A/B slips caused by the team; **revise** - promised dates keep growing → without changing capacity or entry (1 or 3) this only records deterioration.

## Intervention 3. Reduce consultation demand through self-service

0. **Relies on part of hypothesis (b):** capacity is eaten by repeated consultations (~45 % of arrivals).
1. **Direction:** prevent recurrence + change the method.
2. **What we change:** knowledge base of answers to typical questions (finding a dataset, term meaning, technical vs business metadata) - **ourselves**; each consultation starts with checking the base, a new answer is added - **ourselves**; link to the base in the intake template and catalog UI - **ourselves**, possibly with **vendor or IT** for the UI.
3. **Mechanism:** arrivals of consultation cases (incoming load).
4. **Positive explanation:** users close part of the questions themselves → consultation arrivals drop → engineering time is freed for new functions → function throughput grows, incl. for A and B.
5. **Reduces:** engineers' load with repeated questions.
6. **Adapts to:** headcount (hiring an analyst is outside team authority).
7. **Feasibility:** first 20-30 answers ≈ a week of work spread across engineers, taken from cases - throughput drops temporarily; effect in 2-3 months.
8. **Side effects:** the base gets outdated without maintenance and gives wrong answers; users may not find answers and write anyway; temporary throughput drop at start; a platform change would require reworking the base.
9. **Compatibility:** fits 1 and 2, but **not at the same time as 1** - if throughput grows, the cause would be unclear. Sequence: 1 → after 4-6 weeks 3.
10. **Check:** observe - share of consultations in arrivals, base hits, new function throughput; compare with - baseline ≈ 45 % (assumption from R4.1, refine by tracker after classes are introduced); **solved** - consultations ≤ 30 % after 3 months and function throughput up; **revise** - base hardly used or share unchanged → questions are not typical, the option does not work.

## Overall compatibility

**Recommended sequence: 1 → 2 → 3.** Intervention 1 first: cheap, within team authority, and **distinguishes hypotheses (a) and (b)**. Intervention 2 can be added right after: it acts on consequences and does not disturb the check of 1. Intervention 3 - once it is clear where the constraint is. If 1 ends in "revise", the next step is not 3 but a capacity conversation with the DG lead - an "involves others" option deliberately left out of the three (adding people is outside team authority).
