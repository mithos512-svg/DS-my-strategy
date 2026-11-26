---
type: model
date: 2026-11-26
course: R4.3:3, R4.3:Tasks2
problem_card: problem-cards-r4.md, B-2
hypotheses: hypotheses-case-queue-r4.md (v1.0)
status: v1.2 (checked against FPF Library C.28.CM:4, C.28:4.1, Library.Reference:6.5.3.2, HCD.Reference:3, A.2.8:4; snapshot 20261125T054841Z)
---

# Cause-effect pairs for the case queue

> Assignment source: MimEcoSys/docs, `professional/counterfactuality/03-understanding-causality-and-counterfactual-thinking/05-finding-causes-and-effects-practice.md`; lesson R4.3:3 "Types of causes" (`04-types-of-causes-in-causality.md`), commit faed795, 2026-11-04. Continues `hypotheses-case-queue-r4.md` (R4.3:Tasks1).

**Types of causes (R4.3:3), all within P(B | do(A)) > P(B):**
- **Necessary** - without A there is no B; A does not guarantee B.
- **Sufficient** - A brings B regardless of anything else; B can also come from another cause.
- **Contributing** - A raises the probability of B; under some conditions B does not follow.

**FPF guards:**
- Necessary-condition reasoning finds prerequisites; sufficient-cause reasoning examines how conditions **together** produce an effect (Library.Reference:6.5.3.2). In an organisation a single A is rarely sufficient - a sufficient cause is written as a conjunction with its conditions.
- "Direct" and the type of a cause are relative to the variables kept in the model (C.28.CM:4.3). Many necessary causes here are set by **rules and role boundaries**, not by nature - changing the rule removes them.
- "Why did the queue start?", "why does it persist?" and "what shortens it now?" can need different mechanisms (C.28.CM:4.1).
- Feedback is unfolded in time (t → t+1), not erased to get an acyclic picture (C.28.CM:4.4).
- Separate the subject event from its registration (C.28.CM:4.2) and watch selection of cases (C.28.CM:4.4).
- A training session held, a capability of the trained person and a change in their work are different claims, each needing its own evidence (HCD.Reference:3).
- The bearer of a duty and the actual performer of the work are different; work is attributed to whoever actually performs it, not inferred from the duty or the position. "Responsible" does not follow from a position or an "owner" label, and an undefined duty boundary is a missing rule, not a proven refusal of a duty (A.2.8:4.2, 4.6).

## 0. Domain facts (user, 26.11)

- More and more business functions are getting interested in DG/DQ.
- A large part of the team's time goes to explaining what Data Governance and Data Quality are, what is required from a function, and which functionality the platform offers.
- The team does **not** resolve detected data quality problems - **data stewards** in the functions do.
- Most urgent assignments are about **engaging and training data stewards** for functions.
- A **separate department is responsible for engaging new functions** in DG/DQ. Its staff do not go into technical details and forward even simple questions to the DG/DQ team, asking it to communicate with each function directly.

## 1. Pairs from the hypotheses (Tasks1)

| # | Cause (A) | Effect (B) | Type | Hypothesis | Comment |
|---|---|---|---|---|---|
| 1 | Arrivals exceed "done" + "closed as not relevant" for months | Open cases grow | **Necessary and sufficient - by accounting** | frame | A balance identity (conservation of cases), not an empirical law. Useful as a frame: every other cause acts through arrivals or completions |
| 2 | No regular triage slot | Time from request to decision > 1 month | **Contributing** | H1a | Ad hoc decisions still happen (urgent, loud requesters); the absence of triage raises the probability of long waiting, it does not guarantee it |
| 3 | Weekly triage slot held **and** triage time per case ≤ slot / arrivals | Every new case gets a decision within a week | **Sufficient (as a conjunction)** | H1a | The target state of intervention 1. Without the second condition the slot is not enough |
| 4 | ≈ 21 cases in progress per pair | Switching and restarts → fewer cases "done" per month | **Contributing** | H1b | Size of switching losses not measured |
| 5 | Free pair time | Progress on a case | **Necessary** | H2 | Nothing replaces engineering time for development and DQ rule work |
| 6 | Explaining DG/DQ, requirements and functionality to functions; platform support | Less time for cases → lower output | **Contributing** | H2 | Invisible work, not recorded in the tracker; per the user, explanation is a large share |
| 7 | Urgent management assignment - mostly engaging and training stewards for a function (under the current rule "urgent preempts everything") | The pair stops all other cases that week | **Sufficient - by the current rule** | H3 | The user's observation: "при срочных вопросах все остальные кейсы стоят". Sufficient only because of the rule; another rule or a planned onboarding removes it |
| 8 | Pair stopped for a week | Lower "done" in that week | **Contributing** | H3 | A case finished just before the interruption still closes |

## 2. Additional pairs important for the explanation

| # | Cause (A) | Effect (B) | Type | Why it matters |
|---|---|---|---|---|
| 9 | Long waiting at time t | Escalation to management at t+1 | **Contributing** | Start of the feedback loop |
| 10 | Escalation at t+1 | Urgent assignment at t+1 | **Contributing** | Escalations become urgent assignments - the reverse arrow of H3 |
| 11 | Rollout of DG/DQ to new functions, driven by the engagement department; budget cycle / quarter end | Urgent assignments **and** more arrivals / distraction of engineers | **Contributing (common cause)** | Produces an association between urgents and low output without urgents causing it. The rollout is the main common cause found |
| 12 | Requester answer / input data | Completion of the case | **Necessary** | Blocked cases: the pair cannot finish without the requester. Needed for the WIP-limit rule (intervention 1b) |
| 13 | Case accepted at triage | Start of work | **Necessary - by the target rule** | Today it is not necessary (engineers start without triage); intervention 1 makes it necessary |
| 14 | "Not now" or a long promised date | Requester works around the team (own extract, shadow table) | **Contributing (risk)** | The only uncertainty that can reverse the choice (`uncertainty-case-queue-r4.md`, question 3) |
| 15 | Shadow extracts | Worse data quality downstream | **Contributing** | The DG/DQ goal is hurt even if the queue shrinks |
| 16 | Closing obsolete cases at triage | "Closed" per month goes up | **Sufficient - for the measure "closed"** | Not a cause of more "done"; this is why "done" and "closed as not relevant" are counted separately |
| 17 | Case classes in the tracker | Service level expectation (SLE) per class | **Necessary** | Without classes only one overall SLE is possible (intervention 2) |
| 18 | A new function becomes interested in DG/DQ | Demand for explanation reaches the DG/DQ team | **Sufficient - by the current arrangement** | Works through pair 23: the engagement department forwards the questions. A different arrangement (first line at the engagement department, a standard kit, cohorts) makes it contributing |
| 19 | An engaged, trained data steward in the function | Detected DQ problems in that function get resolved | **Necessary - by the role boundary** | The team does not resolve DQ problems; without a steward, detected problems stay open whatever the team does |
| 20 | Explanation / training sessions by the team | The steward can resolve DQ problems on their own | **Contributing** | A session held ≠ capability (HCD.Reference:3). Evidence of effect is the steward resolving issues without team help, not attendance |
| 21 | Trained stewards in a function (t) | Fewer repeated questions from that function (t+1) | **Contributing (conjecture)** | A balancing loop: onboarding now reduces demand later. Not observed yet |
| 22 | No trained steward in a function | DQ problems are routed to the team as cases | **Contributing (conjecture)** | Misrouted demand adds arrivals the team cannot close by its role. To check in the tracker |
| 23 | The engagement department does not go into technical details and forwards questions (current practice) | Every question of a new function, even a simple one, lands on the DG/DQ team | **Sufficient - by the current practice** | The duty to engage functions sits with the engagement department; the explanation work is actually performed by the DG/DQ team and is not counted as its work (A.2.8:4.6) |
| 24 | Request "communicate with each function directly" | Individual onboarding per function, no reuse - explanation time grows with every new function | **Contributing** | Removes the economies of a cohort or a kit; the same explanation is repeated function by function |
| 25 | No agreed rule on which questions the engagement department answers itself | Simple questions are forwarded too | **Contributing** | The boundary of the department's duty is undefined - a missing rule, not a proven refusal (A.2.8:4.2). Agreeing the boundary is a design move |
| 26 | Engagement department's success (more functions engaged) | Higher load on the DG/DQ team | **Contributing** | Benefits and costs of the rollout fall on different departments; the team's capacity is not part of the rollout plan |

**Loops (unfolded in time):**
- *Reinforcing:* long waiting (t) → escalation (t+1) → urgent assignment (t+1) → pair stops (t+1) → lower output (t+1) → longer waiting (t+2). Pairs 9, 10, 7, 8.
- *Balancing (conjecture):* steward onboarding (t) → trained stewards → fewer repeated questions and fewer misrouted DQ problems (t+1) → lower arrivals. Pairs 20, 21, 22.
- *Rollout chain:* engagement department's success (26) → more functions (18) → forwarded questions and individual onboarding (23, 24) → urgent onboarding (7) → stopped case work. The faster the rollout, the more the team's case work stops.
- Under the current arrangement the balancing loop is fed only through urgent assignments - so onboarding, which should reduce demand later, now stops case work and lengthens the queue. The loops compete for the same engineering time.

## 3. Three different questions (C.28.CM:4.1)

| Question | Mechanism that answers it |
|---|---|
| Why did the queue start growing? | More and more functions joined DG/DQ (pair 18, common cause 11). The engagement department forwards their questions and asks the team to talk to each function directly (pairs 23, 24); stewards must be engaged and trained (pairs 19, 20); the team stayed at four engineers (pair 5) |
| Why does it persist? | The reinforcing loop 9 → 10 → 7 → 8, where urgent onboarding requests preempt cases; the rollout chain keeps feeding it (26 → 18 → 23 → 7); parallel work (pair 4) |
| What shortens it now? | An agreed division of labour with the engagement department (first line there, technical questions to the team through triage - pairs 23, 25); a repeatable onboarding kit and cohorts instead of individual urgent onboarding (pairs 24, 7); urgents through triage; WIP limit (pair 4); routing DQ problems to stewards (pair 22) |

## 4. Registration and selection traps

- **Subject vs registration (C.28.CM:4.2):** a "case" in the tracker is a record of a request. Urgent onboarding requests, forwarded questions and chat questions are requests without records; analysing the tracker alone underestimates arrivals and hides H3 and the explanation load.
- **Selection (C.28.CM:4.4):** computing flow time from **closed** cases only selects the short ones - long cases are still open. A service level expectation built this way will be too optimistic. Include open cases (their age so far) when estimating.
- **Training vs capability (HCD.Reference:3):** counting sessions held or stewards "trained" does not show that stewards can resolve issues; observe DQ issues resolved by stewards without team help.
- **Duty vs performer (A.2.8:4.6):** in the engagement department's reporting, a function counts as "engaged" by that department; the explanation work behind it was performed by the DG/DQ team. Without recording who actually performed it, the team's contribution is invisible in both departments' numbers.

## 5. Counterfactual reasoning

**CF-1. The GTIN case in a world with triage and a WIP limit since spring (rung 3, concrete case).**

*Possible world:* everything as in the real 2026 - the same requests arriving on the same dates, the same four engineers split 50/50, the same urgent assignments - except two rules: weekly triage since April and at most four cases in progress per pair.

*Reasoning:* the factual history fixes what stays: the GTIN request date, its effort, the requester's response time, the urgents. Quantities that depend on the changed rules are recomputed: the case gets a decision in the first week (pair 3); it enters the DQ pair's work only when one of its four slots frees up; once started it is interrupted only by the urgents (pair 7 still holds - the urgent rule did not change in this world).

*What it tells us:* if in this world the GTIN case still closes late because of urgents, then H1a and H1b do not explain its delay and H3 does; if it closes earlier, waiting for a decision and parallel work explain most of the delay. The rung-3 answer depends on unrecorded facts (when exactly the urgents happened) - another reason to start recording them.

**CF-2. A world with an agreed first line at the engagement department and planned onboarding (a world arranged differently).**

*Possible world:* the same number of functions join DG/DQ in 2026, with the same interest and the same need for stewards, and the engagement department is still responsible for engaging them. But two rules differ: (1) the engagement department answers basic questions itself, using a standard kit prepared once by the DG/DQ team (what DG/DQ is, the steward role and what is required, the main platform functionality); only technical questions go to the team, through triage; (2) new functions join through a monthly cohort with a fixed reserve of engineering time, not through individual urgent requests.

*Reasoning:* the demand for explanation (pair 18) is the same, but most of it no longer reaches the team (pair 23 becomes contributing), and the rest arrives on a schedule and is served once per cohort (pair 24 disappears). Urgent assignments lose their main content, so pair 7 rarely fires; the reinforcing loop loses its strongest link. The balancing loop (pairs 20-22) works without stopping case work.

*What it tells us:* the cause of the dips is not the growth of interest in DG/DQ - that is a success - but the arrangement "the engagement department forwards everything, and each function is onboarded individually and urgently by the DG/DQ team". The strongest intervention is then an agreement on the division of labour plus a repeatable onboarding product - an intervention that **needs others** (the engagement department and the managers who can set its duty boundary). Evidence of effect: share of forwarded questions that are technical; stewards resolving DQ issues without team help.

## 6. Conclusions

- Of 26 pairs only one is sufficient regardless of rules - the accounting identity (pair 1). The other "sufficient" causes are conjunctions (pair 3), or are sufficient only under the current rule, arrangement or practice (pairs 7, 18, 23), or only for a measure (pair 16).
- Many necessary and sufficient causes are set by rules and role boundaries (pairs 13, 19, 23) - they can be designed, but some of them only together with another department.
- The queue started growing because more functions joined DG/DQ; the engagement department forwards their questions and asks for direct, individual communication, so each new function adds explanation and onboarding work to the DG/DQ team. It persists because urgent onboarding preempts case work in a reinforcing loop fed by the rollout itself.
- The boundary of the engagement department's duty is undefined - this is a missing rule to agree, not a fault to assign.
- New measurement needs: record forwarded questions (from whom, technical or basic); record urgent assignments with subject and dates; record explanation time; observe DQ issues resolved by stewards; estimate flow time including open cases.

## 7. Changes to other models (applied 26.11: hypotheses v1.1, interventions v1.4)

- `hypotheses-case-queue-r4.md`: refine H2 (invisible work = mainly explanation and steward onboarding forwarded by the engagement department) and H3 (urgents = mainly steward onboarding for new functions); add common cause "rollout of DG/DQ to new functions" and a new hypothesis H4 "the undefined division of labour with the engagement department routes basic onboarding work to the DG/DQ team".
- `interventions-case-queue-r4.md`: add an intervention that **needs others** - an agreed division of labour with the engagement department (first line there with a standard kit, technical questions to the team through triage), to be raised with the DG lead and, if needed, the D&A lead; re-target intervention 3 from a generic knowledge base to a **repeatable onboarding product** (kit + cohorts) and consider moving it earlier.

## Changes

- v1.2 (2026-11-26): new domain fact - a separate department is responsible for engaging functions, does not go into technical details and forwards even simple questions, asking the team to talk to each function directly. Pairs 23-26 added; pairs 11 and 18 refined; rollout chain added to loops; section 3 rewritten; CF-2 reworked (first line at the engagement department + planned onboarding); duty vs performer trap and A.2.8 guard added; proposals extended (H4, division-of-labour intervention).
- v1.1 (2026-11-26): domain facts - growth from more functions joining DG/DQ; explanation and steward onboarding take much time; the team does not resolve DQ problems (stewards do); urgents are mostly steward onboarding. Pairs 18-22, balancing loop, CF-2 planned onboarding, training vs capability guard (HCD.Reference:3).
- v1.0 (2026-11-26): first version after the FPF check - sufficient causes written as conjunctions or rule-dependent; types relative to rules; feedback loop unfolded in time; three questions separated; registration and selection traps.

---

Sources: R4.3:3, R4.3:Tasks2 (MimEcoSys/docs, commit faed795); FPF Library `C.28.CM:4` (https://fpf.tools/C.28.CM:4), `C.28:4.1` (https://fpf.tools/C.28:4.1), `Library.Reference:6.5.3.2` (https://fpf.tools/Library.Reference:6.5.3.2), `A.2.8:4` (https://fpf.tools/A.2.8:4), Human Capability Development DPF `HCD.Reference:3` (https://fpf.tools/HCD.Reference:3), snapshot 20261125T054841Z-7b084255babf17c2.
