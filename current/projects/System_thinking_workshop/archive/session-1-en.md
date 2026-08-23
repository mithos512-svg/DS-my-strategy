---
type: systems-thinking-workshop-session
session: 1
topic: Systems Thinking Workshop, Session 1 — what is a system, and why the "same" metric isn't always the same thing
status: bullet points ready — v2, rebuilt 09.08 on verified FPF-Spec content (was oversimplified to 4 fields, actual MHTTriggerProfile has 7)
created: 2026-08-09
updated: 2026-08-09
language: en (team is English-speaking)
---

# Systems Thinking Workshop, Session 1 — Bullet Points (EN, v2 — rebuilt on verified spec)

> **Rebuilt 09.08** after checking the actual FPF specification (fpf.sh, not
> just seminar slides — see day-rhythm-config.md rule "FPF spec always wins
> over seminars"). The core check went from 4 simplified questions to the
> **7 real trigger fields** of MHTTriggerProfile (pattern B.2, verified at
> https://fpf.sh/generated/patterns/B.2). Two of the missing three —
> **Supervision** (who owns/governs the measurement) and **Objective** (what
> purpose it serves) — often turn out to be the actual root cause of metric
> conflicts in practice, more than the structural ones we had before.
>
> Renamed from "Book Club" to "Systems Thinking Workshop" per F.18 naming
> decision — see namecard.md. FPF pattern names and jargon kept out of the
> actual talking points; the room doesn't need the labels to get the value.

## Case for discussion

Incompatible metric definitions across business units: the same metric
(e.g. "done," "active customer," "conversion") means different things in
different parts of the company — and this creates conflict when comparing
reports or making decisions at the boundary between units.

## Warm-up (5 min)

- Each participant names one metric from their own practice that they suspect
  means different things in different teams/units.
- Just collect the list on the board — don't dig into it yet.

## Block 1 — What is a system? (10 min, foundation)

- A system isn't just a pile of parts. Put together, parts create something
  none of them has alone. Water is wet — but a hydrogen atom isn't wet, and
  neither is an oxygen atom. A team can be productive or dysfunctional — that's
  not a property of any one person, it's a property of the team as a whole.
- Systems nest inside each other: an engine sits inside a car, a car sits
  inside a fleet, a fleet sits inside a company.
- Crossing a level changes the whole conversation. Take a car: people who
  *drive* it talk about routes and destinations. People who look at *engine
  parts* talk about efficiency and wear. People who *manufacture standard
  components* don't talk about "the car" at all. People who talk about *raw
  materials* focus on strength and how hard something is to machine. Same car,
  four completely different conversations — because each role is looking at a
  different level.
- The skill worth noticing: which level is this conversation actually
  happening at right now?

## Block 2 — Why this matters for metrics (5 min, bridge)

- When two business units report the "same" metric, are they really looking
  at the same level — the same whole — or has the conversation quietly shifted
  levels without anyone flagging it?
- First check, always: can the mismatch be explained without saying "these are
  genuinely different things"? Sometimes it's just a formula, a rounding rule,
  or a reporting date that needs fixing — cheaper to fix than to declare a real
  disagreement.

## Block 3 — CORE: the 7-question check (20 min)

If a quick fix to the measurement doesn't resolve it, walk through these seven
questions. Each one is a different way the "whole" being measured can quietly
change between units. (An eighth possible trigger, "agency threshold," exists
in the framework but rarely applies to a metrics case — skip unless the
discussion turns to an AI or automated system acquiring new autonomy.)

| # | Question | What to look for in the metric case |
|---|---|---|
| 1 | **Who's included?** | Did one unit widen who/what counts (e.g. added contractors) while another didn't? |
| 2 | **What's it made of, and how do the parts relate?** | Does the number include the same components, connected the same way? Tax in or out; returns in or out? |
| 3 | **Who owns and approves how it's counted?** | Does each unit have someone who signs off on the counting method — and is it the same role, or does each unit decide on its own? |
| 4 | **What does it depend on?** | Does one unit's number rely on a process or step that the other unit simply doesn't have? |
| 5 | **What purpose is it actually serving?** | Are both units measuring the "same" number for different reasons — e.g. one for bonus calculation, the other for inventory planning? |
| 6 | **Does the same value mean the same capability?** | Could an identical number represent a different real-world state in each unit — e.g. "ready" meaning ready to ship vs. ready to invoice? |
| 7 | **Is the difference a one-off, or has it become a standing practice?** | Is one unit's different counting method a settled, repeated way of doing things — not a single mistake, but how they've always done it? |

- Run each metric from the warm-up through the seven questions. Find at least
  one where a real difference shows up.
- **Questions 3 and 5 (who owns it, what purpose it serves) are worth extra
  attention** — in practice they're often the real root cause, even though
  they're easy to skip past when the conversation stays on formulas and
  definitions.
- Important: naming which question applies doesn't *prove* the two units are
  measuring genuinely different things — it's a flag that says "worth a closer
  look," not a verdict.

## Block 4 — Who actually checks this (10 min)

- Someone needs to write down one specific, concrete explanation for the
  mismatch — not a list of five possible reasons. Then someone who owns the
  metric checks the facts and confirms or rejects it.
- Question for the group: who in your organization should play that role for a
  metric — and why does this conversation usually happen only *after* it's
  already turned into a conflict?

## Optional — if time allows (5 min)

- A related idea: the same word can mean genuinely different things to
  different teams without anyone noticing — "done" means one thing to a repair
  crew and something else to the team that accepts the finished work. Building
  a shared translation between the two meanings (not forcing one team to adopt
  the other's definition) is often the real fix. Worth keeping as a seed for a
  second session.

## Takeaway

- The 7-question check applies to any disputed metric before it turns into a
  conflict — pay special attention to ownership and purpose, not just
  structure.
- "Fix the measurement" is cheaper than "declare these are different things" —
  but you can't skip checking which one is actually true.

---
**Facilitator note (not for the room):** this session maps to FPF pattern B.2
"Meta-Holon Transition" — verified against the actual specification at
https://fpf.sh/generated/patterns/B.2 (not just seminar slides). The 7
questions correspond to `MHTTriggerProfile` content fields:
`changedDelimitationRelationRefs` (1, Boundary), `changedPartRelationRefs`
(2, Composition), `changedSupervisionRelationRefs` (3, Supervision — **new,
wasn't in the v1 four-question version**), `changedCoordinationRelationRefs`
(4, Coordination), `changedObjectiveClaimRef` (5, Objective — **new**),
`changedCapabilityClaimRef` (6, Capability — **new**),
`temporalConsolidationClaimRef` (7, Temporal Consolidation — re-defined from
v1's "is it stable or does it jump," which was a mismatched reading of this
field). An eighth field, `agencyThresholdClaimRef`, is in the spec but
excluded from the room script as inapplicable to a metrics case.

The optional block maps to F.9 "**Alignment and Bridge across Contexts**"
(corrected word order — verified at https://fpf.sh/generated/patterns/F.9;
earlier materials had it backwards as "Bridge and Alignment"). Systems-
thinking foundation (emergence, nesting, meta-system transition, car example)
— course "Введение в системное мышление," §2.01 and §5.5. Keep FPF names and
jargon out of the actual talking points; the room doesn't need the labels to
get the value.

**Version history:** v1 (09.08, morning) used 4 simplified fields based on
seminar slides only, further corrected once from an even less accurate first
pass ("B-O-S-C"). v2 (09.08, this version) rebuilt after checking fpf.sh
directly, per the new rule that the FPF specification always takes precedence
over seminar materials when a pattern's specific content is used in a
finished work product.
