# Worked examples

All inputs and revisions below are original and hypothetical. They demonstrate the skill's decisions, not claims about a real study. The examples are not a comparative model benchmark.

## 1. Make the action visible and hand off the object

**Scope:** Sentence-only; preserve two sentences and their order. **Cards:** S1, S2.

Before:
> The encoder performs the extraction of a feature map. For the scoring head, this map is the input used to assign one score to each region.

After:
> The encoder extracts a feature map. The scoring head uses this map to assign one score to each region.

**Preserved:** The encoder creates the map; the scoring head uses that map; every region receives one score. No threshold, supervision, or performance claim has been added.

**Why it helps:** The verbs now carry the two existing actions. The map links the sentences without repeating a generic “pipeline” label.

## 2. Parallel syntax can preserve asymmetric findings

**Scope:** Sentence-only. **Card:** S4.

Before:
> Adding text improves image accuracy, whereas for text accuracy, the addition of images produces no change.

After:
> Adding text improves image accuracy, whereas adding images leaves text accuracy unchanged.

**Preserved:** Only one direction improves. “Mutually beneficial” would be a false rewrite.

## 3. Unpack the premises without turning them into proof

**Scope:** Sentence-only; splitting is allowed. **Card:** S6.

Before:
> Based on our observations that the map preserves local boundaries and that these boundaries remain visible after compression, we use the compressed map as the decoder input.

After:
> We observe that the map preserves local boundaries and that these boundaries remain visible after compression. Based on these observations, we use the compressed map as the decoder input.

**Preserved:** Both observations, the post-compression condition, and their stated role in choosing the decoder input. Neither “lossless compression” nor a universal guarantee follows.

**When to keep it:** If one sentence or the original information order is required, do not force this split. A short initial condition does not need unpacking.

## 4. Keep a condition in one sentence

**Scope:** Sentence-only. **Card:** S7.

Before:
> The decoder updates continuous states up to the last step. At that final step, the output head converts the states into labels.

After:
> The decoder updates continuous states up to the last step, when the output head converts the states into labels.

**Preserved:** The main process, its final-step boundary, and the module responsible for label conversion. The sentence is longer because it holds one complete temporal relation.

## 5. A clear sentence can stay unchanged

Input and output:
> The encoder is frozen during adaptation. Only the region head is updated.

**Decision:** Keep. The subject and passive voice foreground the relevant parameter state. Changing both subjects to “we” offers no necessary improvement.

## 6. Mark a local ambiguity instead of inventing causality

Input:
> The encoder shares weights with the teacher, and the head uses a separate loss. This reduces memory use.

**Decision:** Ask which operation “This” refers to, or flag that referent for the author. Do not silently rewrite it as “Weight sharing reduces memory use.” The original text does not establish that interpretation.

## 7. Broader revision needs broader permission

**Scope:** Paragraph reordering explicitly permitted. All supplied facts remain fixed.

Before:
> The shared cache does not reduce the cost of a first request. We add the cache to avoid repeated reads of the same document. Repeated requests perform fewer reads with the cache.

After:
> We add a shared cache to avoid repeated reads of the same document. Repeated requests perform fewer reads with the cache, but the cache does not reduce the cost of a first request.

**Preserved:** The motivation, the repeated-request benefit, and the first-request limitation. “Does not reduce” is not rewritten as “unchanged,” which would assert equality. No latency measurement or new strategy has appeared. This is a paragraph edit, not a sentence-order-preserving polish.

---

[Sentence cards](../skills/revise-research-writing/references/sentence-craft.md) · [Review guide](../skills/revise-research-writing/references/review-and-verify.md) · [Behavioral cases](acceptance-cases.json)
