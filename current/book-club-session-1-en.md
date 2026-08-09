---
type: book-club-session
session: 1
topic: FPF pattern B.2 (Meta-Holon Transition) — incompatible metrics across business units
status: bullet points ready
created: 2026-08-09
language: en (team is English-speaking — see ru version in book-club-session-1.md)
---

# Book Club, Session 1 — Bullet Points (EN)

> Case chosen on 26.07: FPF pattern **B.2 "Meta-Holon Transition" (MHT)** — instead
> of the originally proposed Dev/QA/Ops case (didn't fit, the team doesn't work
> that way). Discussion tool for the session — the 4 elements of MHTTriggerProfile.
> **Corrected 09.08:** elements are Boundary/Composition/Coordination/Stability
> (not B-O-S-C/Objective-Supervisor-Complexity as mistakenly noted on 26.07 —
> checked against the source, FPF Seminar 2, slide 26).

## Case for discussion

Incompatible metric definitions across business units: the same metric
(e.g. "done," "active customer," "conversion") means different things in
different parts of the company — and this creates conflict when comparing
reports or making decisions at the boundary between units.

## Warm-up (5 min)

- Each participant names one metric from their own practice that they suspect
  means different things in different teams/units.
- Don't dig into it yet — just collect the list on the board.

## Block 1 — why this isn't just "poor communication" (10 min)

- Pattern B.2 starts with a check: can the discrepancy be explained **without
  changing** the whole (holon) under consideration — just by refining the
  measurement, interval, or method?
- Question for the group: for your metric from the warm-up — is the
  discrepancy really about different things, or just an imprecisely worded
  measurement of the same thing?
- Key idea from the source: shifting the level of consideration (from a
  machine to a line, from a department to a company) doesn't by itself
  produce a new holon — it's just a different view of the same whole.

## Block 2 — four reasons for a real transition (20 min, core of the session)

If explanations with the prior whole aren't enough, we go through what
actually changed, element by element (MHTTriggerProfile):

| Element | Question for the metric case |
|---|---|
| **Boundary** | Who is included in the measurement at all? Did one unit widen the boundary (e.g. included contractors) while another didn't? |
| **Composition** | What parts make up the metric? One unit counts revenue with tax, another without; one includes returns, another doesn't? |
| **Coordination** | Does unit A's metric depend on a process that unit B simply doesn't have (a different workflow)? |
| **Stability** | Is the metric stable over time in one unit but volatile in another — because they're computed over different time windows? |

- For each metric from the warm-up — run it through all four elements, find
  at least one where a real discrepancy shows up.
- Practical takeaway from the source: MHTTriggerProfile is only a **record**
  of why the prior explanation isn't enough. It doesn't prove the transition
  by itself — you still need one concrete candidate for the new whole and a
  fact check.

## Block 3 — who verifies the transition is justified (10 min)

- In the pattern: an AI agent (or analyst) prepares **one specific candidate**
  for the new whole — not a list of options. An engineer (in this case, the
  metric owner or a unit representative) checks the facts and confirms or
  rejects it.
- Discussion: who in your organization should be this "engineer" for a
  metric — and why does this conversation usually not happen until it
  escalates into a conflict?

## Optional — if time allows (5 min)

- Related pattern **F.9 "Bridge and Alignment across Contexts"** — about a
  bridge between two local meanings of the same word in different contexts
  (source example: "done" means different things to a repair crew and an
  acceptance team). Possibly a closer fit for the metrics case than B.2 —
  worth keeping in mind as an alternative entry point for a second session.

## Session takeaway

- The 4-question checklist (Boundary/Composition/Coordination/Stability) can
  be applied to any disputed metric before it escalates.
- The difference between "refine the measurement" and "acknowledge these are
  different things" — the first is cheaper, but you can't skip the check.

---
**Source:** FPF Seminar 2, part 1, slide 26 (Meta-Holon Transition, B.2);
FPF Seminar 4, part 1, slide 11 (Bridge, F.9) — for the optional block.
