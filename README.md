<p align="center">
  <img src="assets/banner.svg" alt="Research Writing Skill — clear prose, intact science" width="100%">
</p>

<p align="center">
  <strong>Clear prose. Intact science.</strong><br>
  A source-grounded skill for revising English research papers.
</p>

<p align="center">
  <a href="#quick-start">Quick start</a> ·
  <a href="#before--after">Before / after</a> ·
  <a href="#where-the-patterns-come-from">Sources</a> ·
  <a href="#中文说明">中文说明</a>
</p>

---

Research writing gets better when the reader can see **what acts, what changes, and what follows**. This skill turns those decisions into small, reusable editing moves, with source links, original examples, and explicit reasons to keep a good sentence unchanged.

**30 papers · 8 editing layers · 9 sentence cards · on-demand references**

The corpus contains 15 papers with Kaiming He and 15 with Saining Xie as last-listed authors. The skill studies techniques in these **collaborative papers**; it does not attribute particular sentences to either person, reproduce their voice, or imply their endorsement.

## What it helps with

- **Sentence flow:** bring the action into view, resolve references, and hand information from one sentence to the next.
- **Precise comparisons:** align roles, stages, and conditions without manufacturing symmetric results.
- **Sections and stories:** revise the abstract, argument, or section order when you explicitly ask for that scope.
- **Faithful editing:** preserve claims, technical roles, evidence strength, numbers, and unfinished work.
- **Useful restraint:** keep a well-functioning passive, long sentence, repeated term, or unchanged passage.

The default is sentence-level editing. It does not silently redesign experiments or strengthen the science.

## Quick start

### Codex: local skill folder

Download or clone this repository, then run these commands **from its root**. This installs a new personal copy and stops if one already exists:

```sh
target="$HOME/.agents/skills/revise-research-writing"
mkdir -p "$HOME/.agents/skills"
if [ -e "$target" ]; then
  printf '%s\n' "Already installed: review and back up that copy before updating."
else
  cp -R skills/revise-research-writing "$target"
fi
```

For project-only use, copy the same folder into your project's `.agents/skills/` directory instead. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills) for current discovery and installation behavior. If the skill does not appear, restart the client.

Invoke it with a clear scope:

```text
Use $revise-research-writing to polish the paragraph below.
Keep the story, sentence order, technical claims, and all numbers unchanged.
Return the revision and explain only the important edits.
```

For a different task:

```text
Use $revise-research-writing to revise this abstract's argument.
You may reorder sentences, but may not invent results or broaden the claims.
```

### Other assistants

Provide [SKILL.md](skills/revise-research-writing/SKILL.md) together with its `references/` folder. Ask the assistant to follow the entrypoint and open only the relevant references. A single pasted file cannot make linked files available automatically.

No API key, model download, or runtime package is required. This repository contains instructions and examples; the optional validator uses only Python's standard library. Detailed reference guidance is primarily in Chinese, with original English editing examples.

## Before / after

These are actual edits of **original, hypothetical teaching inputs**, not excerpts from the source papers or research results.

### Reveal the action and keep the information moving

**Before**
> The encoder performs the extraction of a feature map. For the scoring head, this map is the input used to assign one score to each region.

**After**
> The encoder extracts a feature map. The scoring head uses this map to assign one score to each region.

The actor, map, and per-region output stay the same. The revision removes two layers of nominalized wording and keeps the map as the handoff. [S1 + S2](skills/revise-research-writing/references/sentence-craft.md#s1)

### Make the comparison parallel, not the result

**Before**
> Adding text improves image accuracy, whereas for text accuracy, the addition of images produces no change.

**After**
> Adding text improves image accuracy, whereas adding images leaves text accuracy unchanged.

The syntax is parallel; the benefits remain asymmetric. [S4](skills/revise-research-writing/references/sentence-craft.md#s4)

### Sometimes the best edit is no edit

> The encoder is frozen during adaptation. Only the region head is updated.

The stage and parameter states are already clear. A good revision can keep both sentences. [More worked examples](examples/before-after.md)

## Choose the smallest useful tool

| Card | Editing decision |
|---|---|
| S1 · Subjects and verbs | Put the existing action in the predicate |
| S2 · Object handoffs | Let the next sentence use what the previous one established |
| S3 · Relation nouns | Name a division, comparison, or arrangement without replaying it |
| S4 · Parallel comparisons | Put genuine differences in corresponding slots |
| S5 · Stages and qualifiers | Keep training, inference, only, and fixed attached correctly |
| S6 · Front-loaded premises | Expose a buried main clause without losing its premises |
| S7 · Intact conditions | Preserve a complete condition, even in a longer sentence |
| S8 · Local concessions | Keep both the actual benefit and its boundary |
| S9 · Information and rhythm | Group one relation; separate a different constraint |

Start with one to three cards. The [eight-layer toolkit](skills/revise-research-writing/references/eight-layer-toolkit.md) separates scientific story, argument, architecture, section logic, paragraph structure, sentence flow, wording, and grammar. It is a scope selector, not an eight-step ritual.

## Where the patterns come from

The [source guide](skills/revise-research-writing/references/sources-and-patterns.md) preserves the chain from individual papers to within-group observations, cross-group patterns, and operational cards. The [dimension map](skills/revise-research-writing/references/dimension-map.md) connects L1–L8, D1–D15, and S1–S9; the [observation index](skills/revise-research-writing/references/observation-index.json) provides per-paper page/section locations. Versions, author lists, and caveats are in the [corpus manifest](skills/revise-research-writing/references/corpus-manifest.json).

A few concrete examples:

- **H04, Pixel Mean Flows:** parallel clauses distinguish prediction and loss spaces → S4.
- **H09, Denoising Hamiltonian Network:** training and post-training frames distinguish updated and fixed parameters → S5.
- **X02, RepFusion:** a relation noun retrieves a division of labor; a dynamic process is followed by an invariant → S3 / S9.
- **X06, Representation Autoencoders:** the width condition stays attached to a fitting claim → S7.

The snapshot is dated **2026-10-12**. It is a bounded, qualitative corpus, not an exhaustive “latest papers” ranking, statistical style model, or proof of individual authorship. Some read versions are public author manuscripts; the manifest identifies those limits. No source PDFs, figures, or long paper excerpts are redistributed.

Nature's official summary-paragraph guide and several community writing/skill projects informed selected editorial tools. Their role is [documented separately](skills/revise-research-writing/references/reference-integration.md). They do not replace the He/Xie corpus or impose a Nature submission template on a computer-vision paper.

## Repository map

```text
skills/revise-research-writing/
├── SKILL.md                    Small entrypoint and scope router
├── agents/openai.yaml          Optional Codex UI metadata
└── references/
    ├── sentence-craft.md        Nine practical editing cards
    ├── eight-layer-toolkit.md   Choose the editing scale
    ├── section-patterns.md     Section-specific examples
    ├── story-revision.md        Explicitly authorized story work
    ├── final-language-pass.md  Selective cleanup
    ├── review-and-verify.md    Fidelity and old/new review
    ├── figures-and-captions.md Figure and caption guidance
    ├── dimension-map.md        L / D / S traceability
    ├── sources-and-patterns.md Source mechanisms and bibliography
    ├── corpus-manifest.json    Versions and provenance
    ├── observation-index.json Per-paper dimension locations
    └── reference-integration.md External influences and boundaries
examples/                       Original examples and behavioral cases
scripts/validate.py             Offline package checks
assets/banner.svg               Original editable artwork
```

The bibliography and observation index are lookup resources. Ordinary editing should not load them in full.

## Validation and contributions

```sh
python3 scripts/validate.py
```

The validator checks the skill structure, local links and anchors, source counts, dimension coverage, card references, and example data. It does **not** prove semantic equivalence or writing quality. [Behavioral cases](examples/acceptance-cases.json) specify constraints and failure modes for human or model-assisted review; they are test cases, not a claimed benchmark win.

Contributions should include a concrete difficulty, a faithful revision, a useful “keep” case, and a source locator when adding source-derived guidance. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License and attribution

Original instructions, examples, scripts, and artwork are released under the [MIT License](LICENSE). MIT permits straightforward reuse and adaptation while preserving the license notice. It does not license any linked paper, figure, third-party repository, name, or logo. See [ATTRIBUTION.md](ATTRIBUTION.md) for the source boundary and [CHANGELOG.md](CHANGELOG.md) for changes.

## 中文说明

这是一个把已有研究写清楚的论文写作 skill。它保留了何恺明、谢赛宁两组各15篇合作论文中的具体写法：对象接力、关系名词回指、平行对照、阶段限定、完整条件与自然节奏。学的是可迁移的技巧，不声称模仿本人执笔，也不代表作者背书。

- 默认只做 L6–L8 句级润色，保留故事、论证顺序和技术事实；明确允许时才调整段落、章节或故事。
- 日常先选 S1–S9 中最相关的1–3张卡，不必先读完30篇书目或所有规则。
- L1–L8 是使用尺度，D1–D15 是观察维度，S1–S9 是操作卡；[维度映射](skills/revise-research-writing/references/dimension-map.md)把它们连起来。
- 英文示例均为原创、虚构教学输入；“不改”也是有效输出。Nature及社区建议只补充局部信息组织方法，不覆盖原有语料。

示例请求：

```text
用 $revise-research-writing 润色下面这段英文。
故事和句序已定，只改表达；保留数字、限定条件、证据强度和未完成状态。
给出修订稿，只解释影响阅读的关键改动。
```
