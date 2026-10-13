# Worked examples

These original teaching examples use hypothetical methods and results. Each shows an editing choice and the meaning it preserves.

## 1. Put the action in the verb

**Scope:** Sentence-only; preserve two sentences and their order. **Cards:** S1, S2.

Before:
> The encoder performs the extraction of a feature map. For the scoring head, this map is the input used to assign one score to each region.

After:
> The encoder extracts a feature map. The scoring head uses this map to assign one score to each region.

**Meaning:** The encoder creates the map, the scoring head uses it, and each region receives one score.

**Why it helps:** “Extracts” and “uses” state the actions directly. The same map connects the two sentences.

## 2. Make the two directions easy to compare

**Scope:** Sentence-only. **Card:** S4.

Before:
> Adding text improves image accuracy, whereas for text accuracy, the addition of images produces no change.

After:
> Adding text improves image accuracy, whereas adding images leaves text accuracy unchanged.

**Meaning:** Adding text helps image accuracy; adding images leaves text accuracy unchanged. Matching the clause structure makes this difference easier to see.

## 3. Give a long opening room to breathe

**Scope:** Sentence-only; splitting is allowed. **Card:** S6.

Before:
> Based on our observations that the map preserves local boundaries and that these boundaries remain visible after compression, we use the compressed map as the decoder input.

After:
> We observe that the map preserves local boundaries and that these boundaries remain visible after compression. Based on these observations, we use the compressed map as the decoder input.

**Meaning:** Both observations remain, including the post-compression condition and their role in choosing the decoder input. They are observations about visible boundaries, not evidence that compression is lossless.

**When to keep it:** Keep the original if the task requires one sentence or its existing order. Splitting helps here because the opening contains two observations.

## 4. Keep a condition in one sentence

**Scope:** Sentence-only. **Card:** S7.

Before:
> The decoder updates continuous states up to the last step. At that final step, the output head converts the states into labels.

After:
> The decoder updates continuous states up to the last step, when the output head converts the states into labels.

**Meaning:** The decoder updates the states until the final step, when the output head converts them into labels. Keeping the timing in one sentence makes the transition easier to follow.

## 5. A clear sentence can stay unchanged

Input and output:
> The encoder is frozen during adaptation. Only the region head is updated.

**Decision:** Keep both sentences. The passive voice puts the parameter states first, which is what matters here.

## 6. Resolve an unclear “this”

Input:
> The encoder shares weights with the teacher, and the head uses a separate loss. This reduces memory use.

**Decision:** Ask the author which operation reduces memory use. Once that is clear, name it in the second sentence. The current wording leaves the referent unresolved.

## 7. Lead a paragraph with its purpose

**Scope:** Paragraph reordering explicitly permitted. All supplied facts remain fixed.

Before:
> The shared cache does not reduce the cost of a first request. We add the cache to avoid repeated reads of the same document. Repeated requests perform fewer reads with the cache.

After:
> We add a shared cache to avoid repeated reads of the same document. Repeated requests perform fewer reads with the cache, but the cache does not reduce the cost of a first request.

**Meaning:** The revision begins with the reason for adding the cache, then brings the benefit and limitation together. “Does not reduce” stays as written: “unchanged” would make the stronger claim that the cost is equal. Reordering is appropriate here because the requested scope includes paragraph structure.

---

[Sentence cards](../skills/revise-research-writing/references/sentence-craft.md) · [Review guide](../skills/revise-research-writing/references/review-and-verify.md) · [Behavioral cases](acceptance-cases.json)
