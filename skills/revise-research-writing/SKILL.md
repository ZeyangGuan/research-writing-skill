---
name: revise-research-writing
description: Improve English research-paper prose, sentence flow, academic wording, abstracts, methods, results, and captions. Keep sentence-only polishing separate from explicitly requested story or section revision. Not an experiment-design or corpus-reanalysis workflow.
---

# Revise Research Writing

Make the existing research easier to understand. Start with the current writing difficulty; use only the guidance needed to solve it. Keep good sentences. Explain edits in the user's language; write the revised prose in the requested language.

## Choose the authorized scale

“Polish,” “improve flow,” or “language only” defaults to **L6–L8**: preserve the story, paragraph functions, facts, and reasoning order. Respect sentence counts and order when the user explicitly fixes them. Otherwise, combining or splitting neighboring sentences to clarify an existing relation is within L6–L8; preserve the reasoning, not every sentence boundary. Enter higher layers only when the user requests paragraph, section, or story changes. Consult the [eight-layer toolkit](references/eight-layer-toolkit.md) when the scope needs clarification; do not output an eight-layer audit for routine edits.

## Choose a small tool

For ordinary prose, use the most relevant **one to three** [sentence cards](references/sentence-craft.md). Locate the card by ID rather than reading all nine. Read another card only for an unresolved difficulty.

| Difficulty | Start here |
|---|---|
| The action or its actor is buried | [S1: subjects and verbs](references/sentence-craft.md#s1) |
| Sentences do not hand information forward | [S2: object handoffs](references/sentence-craft.md#s2) |
| This/it has an unclear referent | [S3: naming a relation](references/sentence-craft.md#s3) |
| Two roles or settings are hard to compare | [S4: parallel comparisons](references/sentence-craft.md#s4) |
| Training, inference, or only has unclear scope | [S5: stages and qualifiers](references/sentence-craft.md#s5) |
| The main clause arrives too late | [S6: front-loaded premises](references/sentence-craft.md#s6) |
| Splitting a sentence would lose a condition | [S7: intact conditions](references/sentence-craft.md#s7) |
| A contrast erases a benefit or limitation | [S8: local concessions](references/sentence-craft.md#s8) |
| Repeated short sentences break one relation | [S9: information units and rhythm](references/sentence-craft.md#s9) |

Other requests use their own branch, not every reference:

- Authorized paragraph logic: L5 in the [toolkit](references/eight-layer-toolkit.md) and the relevant section example.
- A particular section: only that part of [section patterns](references/section-patterns.md).
- Explicit story or argument revision: [story revision](references/story-revision.md).
- Captions: Captions in the section guide; [figures and captions](references/figures-and-captions.md) only when the figure or editable source is involved.
- Old/new comparison or a sentence-by-sentence review: [review and verification](references/review-and-verify.md).

## Improve the prose, then clean selectively

Use positive editing actions first: clear objects and verbs, forward information flow, aligned comparisons, and nearby conditions. Read the passage as a whole: group related facts into complete relations and give each sentence a clear handoff to the next. Judge We, passive voice, long sentences, and technical repetition by their function.

Then use the [final language pass](references/final-language-pass.md) only on a specific remaining redundancy. Leave unmatched sentences alone; do not rewrite the whole passage again. Usually deliver the revision and only the reasons the user needs.

Check meaning where an edit touches numbers, negation, quantifiers, algorithms, technical roles, causality, comparison conditions, or completion status. Flag missing facts locally and continue independent language work. Keep a baseline for file edits and modify only the authorized scope. Report only the validation actually performed.

## Trace sources only when needed

Each card includes source IDs and page-level mechanisms. For attribution or evidence questions, use the relevant entry in [sources and patterns](references/sources-and-patterns.md); use the [dimension map](references/dimension-map.md) for L1–L8 / D1–D15 / S1–S9 relationships. The [manifest](references/corpus-manifest.json) holds versions and bibliographic records, and the [observation index](references/observation-index.json) holds per-paper dimension locators. **Do not load these large lookup files for routine polishing.**

The guidance draws on a selected corpus of collaborative research papers. Study transferable techniques; do not claim personal authorship, imitate an author's identity, or imply endorsement. Teaching examples are original and hypothetical. [External influences](references/reference-integration.md), including Nature-related guidance, are separate from corpus evidence and never impose a universal journal template.
