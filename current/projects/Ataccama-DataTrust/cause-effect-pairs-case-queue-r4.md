---
type: model
date: 2026-11-26
course: R4.3:3, R4.3:Tasks2
problem_card: problem-cards-r4.md, B-2
hypotheses: hypotheses-case-queue-r4.md (v1.0)
status: v1.0 (checked against FPF Library C.28.CM:4, C.28:4.1, Library.Reference:6.5.3.2; snapshot 20261125T054841Z)
---

# Cause-effect pairs for the case queue

> Assignment source: MimEcoSys/docs, `professional/counterfactuality/03-understanding-causality-and-counterfactual-thinking/05-finding-causes-and-effects-practice.md`; lesson R4.3:3 "Types of causes" (`04-types-of-causes-in-causality.md`), commit faed795, 2026-11-04. Continues `hypotheses-case-queue-r4.md` (R4.3:Tasks1).

**Types of causes (R4.3:3), all within P(B | do(A)) > P(B):**
- **Necessary** - without A there is no B; A does not guarantee B.
- **Sufficient** - A brings B regardless of anything else; B can also come from another cause.
- **Contributing** - A raises the probability of B; under some conditions B does not follow.

**FPF guards:**
- Necessary-condition reasoning finds prerequisites; sufficient-cause reasoning examines how conditions **together** produce an effect (Library.Reference:6.5.3.2). In an organisation a single A is rarely sufficient - a sufficient cause is written as a conjunction with its conditions.
- "Direct" and the type of a cause are relative to the variables kept in the model (C.28.CM:4.3). Many necessary causes here are set by **rules**, not by nature - changing the rule removes them.
- "Why did the queue start?", "why does it persist?" and "what shortens it now?" can need different mechanisms (C.28.CM:4.1).
- Feedback is unfolded in time (t → t+1), not erased to get an acyclic picture (C.28.CM:4.4).
- Separate the subject event from its registration (C.28.CM:4.2) and watch selection of cases (C.28.CM:4.4).

## 1. Pairs from the hypotheses (Tasks1)

| # | Cause (A) | Effect (B) | Type | Hypothesis | Comment |
|---|---|---|---|---|---|
| 1 | Arrivals exceed "done" + "closed as not relevant" for months | Open cases grow | **Necessary and sufficient - by accounting** | frame | A balance identity (conservation of cases), not an empirical law. Useful as a frame: every other cause acts through arrivals or completions |
| 2 | No regular triage slot | Time from request to decision > 1 month | **Contributing** | H1a | Ad hoc decisions still happen (urgent, loud requesters); the absence of triage raises the probability of long waiting, it does not guarantee it |
| 3 | Weekly triage slot held **and** triage time per case ≤ slot / arrivals | Every new case gets a decision within a week | **Sufficient (as a conjunction)** | H1a | The target state of intervention 1. Without the second condition the slot is not enough |
| 4 | ≈ 21 cases in progress per pair | Switching and restarts → fewer cases "done" per month | **Contributing** | H1b | Size of switching losses not measured |
| 5 | Free pair time | Progress on a case | **Necessary** | H2 | Nothing replaces engineering time for development and DQ rule work |
| 6 | Platform support and consultations take engineering time | Less time for cases → lower output | **Contributing** | H2 | Invisible work, not recorded in the tracker |
| 7 | Urgent management assignment (under the current rule "urgent preempts everything") | The pair stops all other cases that week | **Sufficient - by the current rule** | H3 | The user's observation: "при срочных вопросах все остальные кейсы стоят". Sufficient only because of the rule; another rule (reserve) removes it |
| 8 | Pair stopped for a week | Lower "done" in that week | **Contributing** | H3 | A case finished just before the interruption still closes |

## 2. Additional pairs important for the explanation

| # | Cause (A) | Effect (B) | Type | Why it matters |
|---|---|---|---|---|
| 9 | Long waiting at time t | Escalation to management at t+1 | **Contributing** | Start of the feedback loop |
| 10 | Escalation at t+1 | Urgent assignment at t+1 | **Contributing** | Escalations become urgent assignments - the reverse arrow of H3 |
| 11 | Budget cycle / quarter end | Urgent assignments **and** distraction of engineers | **Contributing (common cause)** | Produces an association between urgents and low output without urgents causing it |
| 12 | Requester answer / input data | Completion of the case | **Necessary** | Blocked cases: the pair cannot finish without the requester. Needed for the WIP-limit rule (intervention 1b) |
| 13 | Case accepted at triage | Start of work | **Necessary - by the target rule** | Today it is not necessary (engineers start without triage); intervention 1 makes it necessary |
| 14 | "Not now" or a long promised date | Requester works around the team (own extract, shadow table) | **Contributing (risk)** | The only uncertainty that can reverse the choice (`uncertainty-case-queue-r4.md`, question 3) |
| 15 | Shadow extracts | Worse data quality downstream | **Contributing** | The DG/DQ goal is hurt even if the queue shrinks |
| 16 | Closing obsolete cases at triage | "Closed" per month goes up | **Sufficient - for the measure "closed"** | Not a cause of more "done"; this is why "done" and "closed as not relevant" are counted separately |
| 17 | Case classes in the tracker | Service level expectation (SLE) per class | **Necessary** | Without classes only one overall SLE is possible (intervention 2) |

**Feedback loop (unfolded in time):** long waiting (t) → escalation (t+1) → urgent assignment (t+1) → pair stops (t+1) → lower output (t+1) → longer waiting (t+2). Pairs 9, 10, 7, 8 form a reinforcing loop: urgents both follow from the queue and feed it. So "urgents cause low output" and "low output causes urgents" can both be true; the question is which link to break. Intervention 1 (urgents through triage) breaks link 10 → 7; intervention 2 (promised dates) weakens link 9.

## 3. Three different questions (C.28.CM:4.1)

| Question | Mechanism that answers it |
|---|---|
| Why did the queue start growing? | Pair 1: arrivals rose (catalog and DQ became visible - more requests) while capacity stayed at four engineers - pairs 5, 6 |
| Why does it persist? | The loop 9 → 10 → 7 → 8 and parallel work (pair 4): the queue produces the urgents that keep it long |
| What shortens it now? | Breaking the loop (urgents through triage), WIP limit (pair 4), cheap decisions on obsolete cases (pair 16 - only for the open count, not for output) |

## 4. Registration and selection traps

- **Subject vs registration (C.28.CM:4.2):** a "case" in the tracker is a record of a request. Urgent assignments and chat requests are requests without records; analysing the tracker alone underestimates arrivals and hides H3.
- **Selection (C.28.CM:4.4):** computing flow time from **closed** cases only selects the short ones - long cases are still open. A service level expectation built this way will be too optimistic. Include open cases (their age so far) when estimating.

## 5. Counterfactual reasoning

**CF-1. The GTIN case in a world with triage and a WIP limit since spring (rung 3, concrete case).**

*Possible world:* everything as in the real 2026 - the same requests arriving on the same dates, the same four engineers split 50/50, the same urgent assignments - except two rules: weekly triage since April and at most four cases in progress per pair.

*Reasoning:* the factual history fixes what stays: the GTIN request date, its effort, the requester's response time, the urgents. Quantities that depend on the changed rules are recomputed: the case gets a decision in the first week (pair 3); it enters the DQ pair's work only when one of its four slots frees up, so its start depends on the order of accepted cases; once started it is interrupted only by the urgents (pair 7 still holds - the urgent rule did not change in this world).

*What it tells us:* if in this world the GTIN case still closes late because of urgents, then H1a and H1b do not explain its delay and H3 does; if it closes earlier, waiting for a decision and parallel work explain most of the delay. It also shows that the rung-3 answer depends on unrecorded facts (when exactly the urgents happened) - another reason to start recording them.

**CF-2. A world where urgent assignments go to a planned reserve (a world arranged differently).**

*Possible world:* the company has the rule "management requests use a 20 % capacity reserve of each pair and go through triage"; urgency of requests is the same as in our world.

*Reasoning:* if in that world output does not dip after urgent requests, then the cause in pair 7 is not urgency itself but the rule "urgent preempts everything". Pair 7 changes type from sufficient to contributing, and the loop 9 → 10 → 7 loses its strongest link.

*What it tells us:* the "sufficient" cause in pair 7 is a property of our rule, not of the work. That is why the intervention targets the rule (urgents through triage) and not the urgency.

## 6. Conclusions

- Of 17 pairs only one is sufficient regardless of rules - the accounting identity (pair 1). The other "sufficient" causes are conjunctions (pair 3) or are sufficient only under the current rule (pair 7) or only for a measure (pair 16).
- Many necessary causes are set by rules (pair 13) - they can be designed.
- The strongest structure found is a feedback loop between long waiting, escalations and urgent assignments; it explains why the queue persists, not only why it started.
- New measurement needs: record urgent assignments and escalations with dates; estimate flow time including open cases.

## Changes

- v1.0 (2026-11-26): first version after the FPF check - sufficient causes written as conjunctions or rule-dependent; types marked as relative to rules; feedback loop unfolded in time; three questions (start / persistence / shortening) separated; registration and selection traps added.

---

Sources: R4.3:3, R4.3:Tasks2 (MimEcoSys/docs, commit faed795); FPF Library `C.28.CM:4` (https://fpf.tools/C.28.CM:4), `C.28:4.1` (https://fpf.tools/C.28:4.1), `Library.Reference:6.5.3.2` (https://fpf.tools/Library.Reference:6.5.3.2), snapshot 20261125T054841Z-7b084255babf17c2.
