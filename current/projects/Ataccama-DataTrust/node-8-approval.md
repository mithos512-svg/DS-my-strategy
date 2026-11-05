# Creators' graph node "Catalog item approval" (node 8) - description, role, methods

**Status:** v0.1, 2026-10-18. Answer to the R2.6 assignment "choose the most familiar
node of the creators' graph, describe it, name the role and methods". Model source -
`journey-catalogued-dataset.md` v0.3, node checklist - `checklist-approval-readiness.md`.

**Assumption (to verify):** node 8 - approval workflow - is chosen as the most
familiar, because in it the user, as Product Manager of the DG/DQ
system, either acts as approver or owns the approval method. If
the user's actual role in the node is different (e.g., the Governance Lead
approves and the PM only owns the regulation) - replace in §3 and §4.

Terms follow the R2.6:7 ontology: creators' graph node = functional
location; interaction/contact ≠ place of contact; contactor = role
performer who interacts with the object; work by method; work cycle.
Checked against FPF (`A.15.PROD`, snapshot 20261015T182921Z): role via `A.13`
(`U.SystemRoleAssignment` - assignment of a role to an agent), method - `A.3.1`
(`U.Method`: "governed way of doing, intended production effect, applicability"),
work - `A.15.1` (`U.Work`, dated event, enactsMethod).

---

## 1. The node: what it is and where it is

| Parameter | Value |
|---|---|
| **Functional location** | The "Approval" node in the DG/DQ system approval workflow |
| **Physical place** | Workflow task screen in the DG/DQ web UI (the approver's "pending approval" queue); notifications - email/Teams |
| **Node entry** (event) | Steward clicked "Submit for approval" → item in state "pending approval", task appeared in the approver's queue |
| **Node exit** (events) | (a) "approved" → item in state "approved", then automatically "published"; (b) "returned" → item goes back to 4-6, the work cycle ended without the needed state |
| **Object in focus** | Catalog item about dataset X (episteme); the dataset is the referent and is not touched in the node |
| **Neighbouring nodes** | Entry from 4-6 (classification, owner, DQ); exit to 9 (publication, automatic) or back to 4-6 |
| **What happens to the object here** (transformation, `A.3.4`) | The item's **status** changes and a **decision with a comment** appears; item content is not edited in the node (editing happens in 4-6) |

## 2. Interaction (contact), not to be confused with the place

The contact in the node is the **review**: the approver reads the item and checks it
against the checklist, then records the decision. Three separate actions:

1. open the task and the item (entering the contact);
2. check rows A-D of the checklist (the interaction itself);
3. record the decision approved / returned with row references (exit).

A "touchpoint" in the marketing sense does not apply here - per R2.6:7 we
separate the place (workflow task) and the contact (review).

## 3. Contactor role

| Parameter | Value |
|---|---|
| **Role** | **Catalog item approver** (in our organisation - Data Governance Lead / Product Manager of the DG/DQ system) |
| **Assignment of the role to an agent** (`A.13`) | Assigned via workflow permissions: the user is in the Approvers group for a domain. One agent can be approver for several domains; for one domain - one approver (verify there aren't several) |
| **What the role keeps in attention** | Item completeness (checklist blocks A-C), unambiguous link to the asset, confirmed owner, readiness for publication (block D) |
| **What the role does NOT do** | Does not edit the item (that is the steward), does not assign the owner (that is 5), does not set permissions (that is Platform). If the approver starts "filling it in themselves", that is a role switch inside the node (R2.6:1) and must be noticed |
| **Neighbouring roles in the node** | Data Steward (submitter, receives the return), business owner (may be asked to confirm B3), Platform (if D1 is not met) |
| **Role interests** (R2.6:1 - its own objects and questions) | "Can this be published to consumers without harm?" - not "is the dataset described correctly" (that is the steward's question) |

## 4. Methods by which the agent acts in the approver role

Methods are descriptions in classes (`A.3.1`); work is a specific review of item X
on a specific date (`A.15.1`).

| # | Method | Input | Output (target state of the object) | Method source | Where described |
|---|---|---|---|---|---|
| M1 | **Review against the readiness checklist** | item "pending approval" + checklist filled in by the steward | rows A-D marked by the approver; discrepancies named by row number | R2.6:2-3 (checklist = subjects + states); FPF A.15.PROD (three questions) | `checklist-approval-readiness.md` |
| M2 | **Decision approved / returned** | result of M1 | item status changed; on return - a list of rows, no email | R2.6:5 (decision = choice on the "precision/speed" scale: the approver consciously chooses where to stop on completeness) | checklist legend, §4 |
| M3 | **Identity rule check** | item + rule "catalogued = approved and published to all audiences" | confirmation that the item claims state 9, not "is in the catalog" (row B1) | FPF A.15.PROD question 2 (entity-identity inception); E.24.PUB (audiences) | `journey-catalogued-dataset.md` §7 |
| M4 | **Cycle accounting** | workflow history of the item | cycle number in the checklist instance; at cycle ≥2 - the question "change the performer or the method" | R2.6:7 (work vs work cycle) | checklist instance, field "Cycle #" |
| M5 | **Escalation** (rare) | B3 not met - owner has not confirmed | task to the owner / Governance; item stays "pending approval" in a waiting state (Wait Time grows) | R2.6:2 (Wait Time, TameFlow); R1.3:3 (spontaneous/hidden work - account for it) | not described separately - a candidate for the regulation |

**What of this is actually written down as a method today, and what is in someone's head:** M1 and
M2 are written (checklist v0.1, legend); M3 is written as a rule in the model but not yet
communicated to the team; M4 is only an idea, cycles are not tracked; M5 is
oral practice. So the node runs on 2 of the 5 described methods -
the other three are performed "from memory", which per R2.6:3 is the source
of omissions.

## 5. What the node does to the flow (R2.6:4)

- Node 8 is a candidate flow **constraint** (together with 5): Wait Time
  accumulates here (the approver's queue) along with returns.
- Two different times in the node: **queue wait time** (the item waits for the
  approver) and **touch time** (the review itself, usually minutes). If the first
  is many times larger than the second, the constraint is not in the review method but in the role's
  load or the number of approvers.
- Measurement: entry date "pending approval" → decision date; share returned; cycle #.

## 6. Critique of my own node model (per R2.6:Tasks4 item 2)

1. Not verified whether there is one approver per domain - if several, the node must
   be split or the selection rule described.
2. M5 (escalation) is not formalised - this is exactly where, from experience, weeks are lost.
3. An approver who "fills it in themselves" is a real pattern; the model forbids it,
   practice does not. Either allow it explicitly (then it is a different role in the same
   node) or catch it with the checklist.
4. Not described what happens when the referent dataset changes after
   approval (schema changed) - is that a re-entry into the node or a new object
   (temporal part, R2.6:1-2)? Open.

## 7. Object state as a result of the interaction

Per R2.6:7 we distinguish the **object state** and the **work state**: "work
is complete when the needed object is in the needed state; a work cycle can
finish without that". So the description has two layers, then per FPF
`A.15.PROD:4.6` - as a state-satisfaction claim.

### 7.1. Target object state: "item approved"

The catalog item about dataset X must be in the state
**"approved"**, which means all of the following at once:

| State component | Value in the target state | How we observe it (event) |
|---|---|---|
| Workflow status | `approved` | item status field; item left the approver's queue |
| Approver's decision | recorded, with date and author | entry in workflow history |
| Readiness checklist | filled in by **two** roles, rows A-C without "no", D1 and D3 without "no" | checklist instance with the steward's and approver's marks |
| Item content | **unchanged** in the node (description, terms, owner, DQ rules same as at entry) | diff of the item at entry and exit is empty except for status and decision |
| Link to the identity rule | item recognised as a candidate for the state "published to all audiences" (B1) | B1 mark = yes |
| Readiness for the next node | publication permissions set (D1), sensitivity marked (D3) | item visible in test self-service; PII classification set |

In short: **an approved item = an item whose content is recognised as complete against the
checklist, with a recorded decision, with no edits in the node, ready for
automatic publication.**

What the target state is **not** (so as not to confuse it with neighbours):
- not "published" - that is state 9, reached automatically afterwards; per
  `E.24.PUB` it is a separate availability event;
- not "dataset catalogued" - that is the identity rule, satisfied
  only after publication to all audiences;
- not "owner assigned" - that is state 5; in node 8 it is only
  *checked* (B3), not achieved.

### 7.2. Three outcomes of the interaction

| Outcome | Object state after | Work state | What next |
|---|---|---|---|
| **Success** | "approved" (as in 7.1) | node work complete, cycle = 1 (or N if there were returns) | automatic transition to 9 |
| **Return** (returned) | "in rework": status `returned`, list of checklist rows with "no", content unchanged | **cycle finished, work not complete** (R2.6:7); cycle # +1 | item goes to 4-6 to the steward; at cycle ≥2 - the question "change the performer or the method" (M4) |
| **Stall** (neither) | "pending approval" with no decision | work not started or interrupted; Wait Time grows, not Touch Time | flow constraint (§5); escalation M5 if the cause is B3 |

The third outcome must be named separately: per R2.6:2 the item at this point is
both "in progress" (WIP) and "waiting" - and this is exactly the state most
often invisible in reports, because the status "pending approval" looks
normal.

### 7.3. The same in FPF terms (A.15.PROD:4.6)

State-satisfaction claim for node 8:

- `completionSubject` - the catalog item about dataset X (not the dataset, not the
  approver's work);
- `completionBoundary` - the moment the approved decision is recorded in the workflow
  (date/time from history);
- `productionCompletionCriterion` - "the item satisfies the readiness
  checklist: A-C without 'no', D1/D3 without 'no', content unchanged in the node";
- boundary facts - the filled-in checklist instance + the history entry.

Separately - the production-work-completion
claim: the work "approval of item X" is closed **because** the approval
workflow, per the team's regulation, treats the approved decision as the closing
event (closure governor). Without this second claim, per A.15.PROD,
"item in state approved" does not yet mean "node work complete" -
for example, if the regulation requires two approvers and there is only one decision.

This gives a practical test for the checklist: row C3 ("decision against the
checklist, not via email") is the closure rule in explicit form.

## 8. Control questions of node 8

Per R2.6:3, control questions are the last step of the checklist-building method:
they must allow assessing (a) whether actions per methods M1-M5 were performed and
(b) whether the object reached the needed states; per the assignment also (c) taking
measurements of change (R2.6:4). The questions are phrased so that the answer is
observable in the system, not "by feel". Three groups.

### 8.1. Were the method actions performed (questions about the approver's work)

| # | Question | Method | Answer observable in |
|---|---|---|---|
| Q1 | Were the item and the steward's attached checklist opened before the decision was made? | M1 | view history / time between task opening and decision > 0 |
| Q2 | Did the approver mark **all** rows A-D, not only the "problematic" ones? | M1 | checklist instance: no empty cells in the approver's column |
| Q3 | Was row B1 checked - does the approver recognise the item as a candidate for "published to all audiences", not "is in the catalog"? | M3 | B1 mark signed by the approver |
| Q4 | If the decision is returned: are the row numbers with discrepancies named, and is there no email instead of them? | M2 | field "rows: …" in the decision filled in; no email thread about the item |
| Q5 | If the decision is approved: is there not a single "no" in A-C and in D1/D3? | M2 | checklist instance |
| Q6 | Is the cycle number entered in the checklist instance? | M4 | field "Cycle #" |
| Q7 | If B3 is not met (owner did not confirm) - was an escalation task created, rather than the item simply left in the queue? | M5 | task to the owner/Governance exists, creation date |
| Q8 | Did the approver edit the item content in the node (role switch inside the node, R2.6:1)? | role boundary | item diff at entry/exit: only status and decision changed |

### 8.2. Did the object reach the needed state (questions about the item)

| # | Question | State | Answer observable in |
|---|---|---|---|
| Q9 | Item status = approved? | 7.1 | status field |
| Q10 | Is there an entry about the decision with date and author in workflow history? | 7.1 | history |
| Q11 | Does the item content at exit match the content at entry (except status and decision)? | 7.1 | diff |
| Q12 | Is the item visible to the self-service test group (D1 = yes)? | readiness for 9 | test view |
| Q13 | Is data sensitivity marked (D3 = yes)? | readiness for 9 | PII classification field |
| Q14 | Did the item leave the approver's queue (no "stall", outcome 3 of 7.2)? | 7.2 | workflow queue |
| Q15 | If returned - is the item with the steward in state "in rework", not "pending approval"? | 7.2 | status + task assignee |
| Q16 | If approved - did the automatic publication (state 9) happen within the expected time? | node boundary | date of visibility in self-service; this is already a check of the **next** node, but without it approved "hangs" |

### 8.3. Measurements of change (R2.6:4, TameFlow from R2.6:2)

Questions whose answer is a number, taken per item and
aggregated over the flow at Week Close.

| # | Question | Quantity | Source | Why (R2.6:4) |
|---|---|---|---|---|
| Q17 | How long did the item wait in the queue from "pending approval" to the approver's first opening? | Wait Time (queue) | history: submit → first open | flow constraint in the role's load or number of approvers |
| Q18 | How long did the review itself take - from opening to decision? | Touch Time | history: open → decision | speed of work by method M1-M2 |
| Q19 | How much time in total did the item spend in node 8 (all cycles together)? | node Flow Time | history: first submit → final approved | speed to result for the node |
| Q20 | What is the cycle number of the final approved? | number of cycles | checklist instance | work vs work cycle (R2.6:7); cycle ≥2 - a signal to change the performer or the method |
| Q21 | Which checklist rows produced "no" in returns? | distribution of "no" by row | comments on "no" | where the method, not the performer, is the issue; the most frequent rows are candidates for moving the check into nodes 4-6 |
| Q22 | How many returns were made without a row reference? | number | approver's decisions | checklist completeness (signal to add a row) |
| Q23 | How many escalations (M5) were created and how many days was each open? | number, duration | escalation tasks | hidden/spontaneous work of the node (R1.3:3), share in Wait Time |
| Q24 | What share of the flow's items passed the node in cycle 1? | % | aggregate of Q20 over the flow | does the checklist work as a method (before/after rollout comparison) |
| Q25 | What are the median and 85th percentile of the node's Flow Time over the flow for the week? | percentiles | aggregate of Q19 | forecast "when will it be approved" by distribution, not by average (Vacanti - external link, the lesson only refers to it) |
| Q26 | How did Q24-Q25 change after the checklist rollout relative to the baseline? | rate/acceleration (R2.6:4, step 6) | two periods | assess the impact on the constraint; compare impacts via jerk (step 7) |

**Baseline measurement:** before the checklist is rolled out, take Q17-Q25 for
the last 10-20 items from workflow history - otherwise Q26 has nothing to compare against.
This is the "first measurement" from §8 of the journey model.

### 8.4. How the questions map to roles and moments

| When | Who | Questions |
|---|---|---|
| Before the decision | approver | Q1-Q3, Q6-Q8 |
| At the decision | approver | Q4-Q5 |
| Right after the decision | approver (or automation) | Q9-Q15 |
| Next day | steward / automation | Q16 |
| At Week Close | method owner (PM / Governance Lead) | Q17-Q26 aggregated over the flow |

Q1-Q16 go into the checklist instance (the approver's operational exocortex, R2.6:3:
where it is filled in); Q17-Q26 go into the flow report (list/dashboard), not into
the checklist of an individual item.

---

Sources: R2.6:1, R2.6:2, R2.6:3, R2.6:4, R2.6:5, R2.6:7, R2.6:Tasks4
(docs-courses, `professional/modeling-1/06-...`); FPF Library `A.15.PROD`
(https://fpf.tools/A.15.PROD - links to A.13, A.3.1, A.15.1, A.3.4),
`E.24.PUB` (https://fpf.tools/E.24.PUB:4), snapshot
20261015T182921Z-219aa77d287d7d2d. Created: 2026-10-18. Translated to English: 2026-11-05 (content unchanged; "Product Owner" → "Product Manager" per the user's correction of 24.10).
