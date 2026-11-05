# Object journey "catalogued dataset in Ataccama" - model v0.3

**Status:** v0.3 (2026-10-16) - all open questions of v0.1-v0.2 are closed by
the user's answers; the final identity rule is adopted (§7). The model is
actionable; the next step is the first Flow Time measurement.

**Method:** object-journey ontology R2.6:7 (journeying object → states →
events → nodes of the creators' graph → contactors → work vs work cycle →
path → flow) + measurement per R2.6:4. Checked against FPF Library
(snapshot 20261015T182921Z, matching upstream on 16.10): `A.15.PROD`
(three production questions), `A.3.4` (transformation), `A.15.1` (work),
`E.24.PUB` (publication = availability to an audience, separate from completion).

**What changed in v0.2 (user's answers, 16.10):**
1. Catalog item statuses are the standard Ataccama ONE ones (approval workflow:
   draft → pending approval → approved; exact names depend on configuration).
2. The approval workflow (state 8) exists as a configured process → a closure
   rule in the sense of A.15.PROD exists: completion of the cataloguing work =
   the event "workflow approved".
3. **Identity rule:** a "catalogued dataset" exists from state
   **9 - published to consumers**, not from 2 and not from 8.
4. Lineage (7) is a **parallel branch**, not a mandatory state before 8.
5. Publication audience is **self-service UI**; **MCP** is coming soon
   (agents as a second audience).

---

## 1. The journeying object

Two objects, not to be mixed:

| Object | Type | Where it lives |
|---|---|---|
| **Dataset** (table/file in the source) | physical object, data carrier | SAP / GCP / BI / file storage |
| **Catalog item** about the dataset | **episteme** - a description of the dataset | Ataccama ONE Catalog |

The journeying object is the **catalog item**; the dataset is its referent.
"Catalogued dataset" = a dataset whose item is **published to
consumers** (state 9, user's decision of 16.10).

## 2. The three A.15.PROD questions - closed by answers

| A.15.PROD question | Answer for our setup | Consequence |
|---|---|---|
| **Work participation** | Cataloguing = composite work made of parts: import, profiling, classification/description, owner, DQ binding, lineage (parallel), approval, publication. Each part is its own work (`A.15.1`) | A report "N datasets catalogued" must state which state was counted. Import ≠ cataloguing |
| **Inception of existence** | Identity rule adopted: item in state 9 (published to the audience). `inceptionBoundary` = event "publication to self-service completed" | Items in 2-8 are *candidates*, not catalogued datasets. This must be agreed with the team, otherwise people will count by 2 or by 8 (R2.6:5 - different scales) |
| **Completion** | Two claims: (a) the item satisfies the approval checklist (state 8 = approved); (b) the cataloguing work is closed - the closure rule = approval workflow. Publication (9) is a separate `E.24.PUB` claim | Approval is not publication: between 8 and 9 there can be a gap (permissions, visibility) that nobody measures now |

**Important E.24.PUB consequence for MCP:** publication is described as
"publication P makes edition of episteme E available to audience A for use U
through form F on carrier C". Self-service UI and MCP are **two different forms F
and two audiences A** (humans and agents). Per E.24.PUB these are **two separate
publication events**, not one. So once MCP arrives, an item will have two
states 9: "published to humans" and "published to agents", and the criterion
"catalogued" will have to be refined - by the first, by both, or by the
primary one.

## 3. Methodological path: states and events

Sequence in methodological time (no clock). Lineage is moved to a parallel
branch.

| # | Item state | Entry event (how we know) | Node of the creators' graph | Contactor (role) | Work by method | Typical rollback |
|---|---|---|---|---|---|---|
| 0 | **Dataset exists, no item** (entry) | - | source (SAP/GCP/BI) | source system owner | - | - |
| 1 | **Source connected** | connector Connected, first successful scan | Ataccama ONE: Sources | Data Engineer / Platform | connector setup | credentials expired → 0 |
| 2 | **Metadata imported** (item exists technically, draft) | catalog item appeared | Catalog | automation + Data Engineer | discovery / metadata scan | schema changed → re-import |
| 3 | **Profiled** | profiling job finished | Catalog / Profiling | automation, triggered by Data Engineer / Steward | profiling | access error → 2 |
| 4 | **Classified and described** | terms and classification assigned, description filled in | Catalog / Business Glossary | Data Steward | classification, description | dispute over a term → stays in 4 (Wait) |
| 5 | **Owner assigned** | Owner/Steward filled in, owner confirmed | Catalog / Ownership | Data Governance Lead ↔ business owner | assignment + confirmation | owner refuses → escalation (Wait!) |
| 6 | **DQ binding done** | DQ rules assigned, first run exists | DQ module | Data Steward + DQ analyst | rule setup, run | rules fail → rework |
| 7∥ | **Lineage built** (parallel branch, does not block 8) | upstream/downstream visible | Lineage module | Data Engineer | lineage scan / manual linking | source not supported → manual lineage or open item |
| 8 | **Approved** (approval workflow) | workflow status = approved | Catalog / Workflow | approver (Governance Lead / Steward) | review against checklist | returned → 4-6 |
| 9 | **Published to consumers** = **catalogued dataset exists** | item visible in self-service UI to the target audience; (soon) available via MCP - a separate event | Catalog / Access | Platform + Governance | publication, permissions | audience cannot see it → not published, although approved |
| 10 | **In use** (exit) | first search/query by an analyst or agent on the item | consumers | analyst / business / agent via MCP | - | - |

Nodes **4, 5, 8** are where work goes into waiting (coordination with roles
outside the data team). Node **9** is a new candidate for an invisible gap:
approved but not published.

## 4. Work vs work cycle (R2.6:7)

"Work is complete when the needed object is in the needed state; a work cycle
can finish without that." For nodes 4-8 count the number of cycles:

- "sent to the owner for confirmation" is a cycle; "owner confirmed" is
  the work. Three emails without an answer = three cycles, work not complete.
- If there are regularly more than one cycle - change the performer or the method
  (e.g., an approval-readiness checklist instead of email threads - link to
  the dissatisfaction about checklists of 14.10, R2.6:2).

## 5. Paths and flow

- The **path** of one item deviates from the methodological one: reference data goes
  2 → 4 → 8 → 9 without DQ; some items get stuck in 5; some return from 8 to 4.
  Lineage can now explicitly finish after 9 - this is fine by the model.
- **Flow** = items of one class (e.g., the "product" domain). Metrics
  per R2.6:4: **throughput** = items entering 9 per week; **speed to
  result** = 0 → 9; **constraint** = the node with the maximum Wait Time
  (hypothesis: 5 or 8).
- Roadmap criterion "first certified dataset - product catalog"
  (Phase 1): under the adopted identity rule this is state **9**, not 8.
  Proposal - refine the milestone wording in the roadmap: "first
  dataset published to self-service after approval".

## 6. What to measure (minimum)

| Metric | How to get it in Ataccama | Why |
|---|---|---|
| Entry date into states 2-9 per item | catalog item audit log, workflow history | Flow Time per node |
| Number of cycles in nodes 5 and 8 | workflow history (returns, reminders) | where work does not complete the first time |
| Share of returns from 8 to 4-6 | workflow history | quality of preparation for approval |
| Wait Time in 4, 5, 8 | "sent" vs "confirmed" | flow constraint |
| (after MCP) share of approved items available to agents | MCP exposure configuration | second publication event; at MCP launch - progress of batch re-publication (§7.1) |

(The "8 → 9 gap" metric was dropped in v0.3: the transition is automatic, §7.2.)

## 7. Decisions v0.3 (user's answers of 16.10, closing the v0.2 questions)

1. **"Catalogued" = published to both audiences** - humans
   (self-service UI) and agents (MCP). Per E.24.PUB these are two publication
   events; the identity rule is a **conjunction**: `inceptionBoundary`
   = the moment of the second of the two events. Until MCP launches, the rule is
   temporarily satisfied by one event (UI) - this must be recorded explicitly as a
   transition period, otherwise after MCP launch all "catalogued"
   datasets will formally stop being so until exposed to
   agents. Practical consequence: **MCP launch = batch work
   "publish all approved items to agents"**, with its own measurement.
2. **The 8 → 9 transition is automatic** → the 8 → 9 gap is zero by
   construction; node 9 for humans collapses into 8 in measurements (the
   "8 → 9 gap" metric removed from §6). The publication contactor is automation. **But:** after
   MCP launch, check whether the second publication is automated too;
   if not, the 8 → 9(MCP) gap becomes a new manual node.
3. **Lineage: "complete" = "created", does not affect consumers** →
   branch 7∥ stays in the model as an item state but is part of neither
   the identity rule, nor the completion criterion, nor the flow metrics.
   It is not measured.

**Final identity rule (for the team glossary):**
"Dataset X is catalogued if the catalog item about X has passed the approval
workflow and is published to consumers through all enabled publication forms
(now: self-service UI; once MCP launches: UI and MCP)". One sentence,
one place, so that Data Engineer, Steward and business count by the same
state (R2.6:5).

## 8. Next step

First measurement: one dataset (product catalog, roadmap Phase 1) - entry
dates into states 2-8 from workflow history, number of cycles in nodes 5 and 8.
Result - v0.4 with the first Flow Time figures. Target - one pomodoro with
Ataccama open. Separately: add the identity rule from §7 to the roadmap
(Phase 1 milestone) and to the team glossary.

---

Sources: R2.6:4 "Measuring change", R2.6:7 "Object journey ontology"
(docs-courses, `professional/modeling-1/06-.../07-...md`,
`.../11-ontology-of-the-object-journey.md`); FPF Library `A.15.PROD`
(https://fpf.tools/A.15.PROD), `E.24.PUB` (https://fpf.tools/E.24.PUB:4),
`A.3.4` (https://fpf.tools/A.3.4:4.1), snapshot 20261015T182921Z-219aa77d287d7d2d.
Created: 2026-10-16 (v0.1). Updated: 2026-10-16 (v0.2, user's answers to
5 open questions). Translated to English: 2026-11-05 (content unchanged).
