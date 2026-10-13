# One paragraph, edited in place

This original teaching example uses a hypothetical method and result. The animation illustrates editing decisions; it is not a recording of a model run.

## Request

> Use $revise-research-writing to polish this paragraph. Keep the sentence order, technical claims, and conditions. Explain the important edits.

## Input

> We use a shared encoder to perform the extraction of a feature map. For the scoring head, this map is the input used to assign a score to each region. It is important to note that the encoder is frozen. We train the head on labeled regions. We evaluate the head on held-out regions. The head improves accuracy, but it increases latency.

## Revision

> We use a shared encoder to extract a feature map. The scoring head uses this map to assign a score to each region. The encoder is frozen. We train the head on labeled regions. We evaluate the head on held-out regions. The head improves accuracy, but it increases latency.

## What changes, and what stays

| Decision | Reason |
|---|---|
| Set a sentence-level scope | Keep the six sentences and their order; work on expression. |
| “perform the extraction of” → “extract” | Put the action in the verb. The shared encoder still produces the feature map. |
| “The scoring head uses this map…” | Name the actor and connect its input to the previous sentence. |
| Remove “It is important to note that” | The encoder's frozen state is the information to retain. |
| Keep “We train…” and “We evaluate…” | The sentences describe different research actions. |
| Keep “the head” | A consistent technical name makes the component easy to follow. |
| Keep “but it increases latency” | The result includes a benefit and a cost. Both belong in the paragraph. |

The last three sentences are unchanged. The edit preserves the shared encoder, feature map, one score per region, frozen encoder, training data, evaluation data, and accuracy–latency trade-off.

## 中文说明

这个例子先确定句级修改范围，再依次处理三个具体问题：动作藏在名词短语里、前后句衔接绕远、事实前面多了一层套话。

后面三句保留原样。“We train”和“We evaluate”分别承担训练与评估两个动作；反复使用“the head”能稳定指代同一个组件；“but”后的延迟代价是结果的一部分。这些写法有实际作用，保留后反而更清楚。

这里的“去 AI 味”指减少空话和机械改写。工具不判断作者是否使用 AI，也不针对检测分数修改文字。

## Related guidance

- [S1: subjects and verbs](../skills/revise-research-writing/references/sentence-craft.md#s1)
- [S2: connections between sentences](../skills/revise-research-writing/references/sentence-craft.md#s2)
- [Selective final language pass](../skills/revise-research-writing/references/final-language-pass.md)
- [More worked examples](before-after.md)

[Desktop still](../assets/workflow/desktop-still.svg) · [Mobile still](../assets/workflow/mobile-still.svg) · [Editable source and build notes](../assets/workflow/README.md)
