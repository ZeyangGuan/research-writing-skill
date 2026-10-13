# One paragraph, edited for flow

This original teaching example uses a hypothetical method and result. It illustrates editing decisions, not a recording of a model run.

## Request

> Use $revise-research-writing to improve the flow of this paragraph. Keep the technical claims, conditions, and progression from method to evaluation to result. You may combine sentences and move short modifiers. Explain the important edits.

## Before

> We use a shared encoder to perform the extraction of a feature map. For the scoring head, this map is the input used to assign a score to each region. It is important to note that the encoder is frozen. We train the head on labeled regions. We evaluate the head on held-out regions. The head improves accuracy, but it increases latency.

## After

> A shared, frozen encoder extracts a feature map that the scoring head uses to assign a score to each region. We train the head on labeled regions and evaluate it on held-out regions. The head improves accuracy but increases latency.

## Five editing moves

### 1. Recover the actors and actions

> We use a shared encoder to extract a feature map. The scoring head uses this map to assign a score to each region. It is important to note that the encoder is frozen. We train the head on labeled regions. We evaluate the head on held-out regions. The head improves accuracy, but it increases latency.

“Extract” names the encoder's action; “the scoring head uses this map” makes the input relationship explicit. These local improvements are a starting point. The passage still needs its related facts grouped.

### 2. Attach the state to its object

> A shared, frozen encoder extracts a feature map. The scoring head uses this map to assign a score to each region. We train the head on labeled regions. We evaluate the head on held-out regions. The head improves accuracy, but it increases latency.

The encoder is now the subject of its own operation, and “frozen” stays beside that encoder. The state has no separate argumentative role here, so it need not interrupt the method description with another sentence. This would be different in a paragraph comparing updated and frozen encoders.

### 3. Keep the interface in one sentence

> A shared, frozen encoder extracts a feature map that the scoring head uses to assign a score to each region. We train the head on labeled regions. We evaluate the head on held-out regions. The head improves accuracy, but it increases latency.

The main clause gives the representation; the relative clause immediately gives its use. The sentence now completes the encoder–map–head relationship, ending on what the head produces. It introduces the head that the next sentence will train and evaluate. No new causal claim is needed.

### 4. Pair the protocol, keeping its two conditions

> A shared, frozen encoder extracts a feature map that the scoring head uses to assign a score to each region. We train the head on labeled regions and evaluate it on held-out regions. The head improves accuracy, but it increases latency.

“Train” and “evaluate” remain different actions, each with its own data condition. Shared subject and object let them form one protocol sentence. The first-person subject marks the experimental actions; the component names organize the method and result. Repeating “We” would also be legitimate where two separately developed points need it.

### 5. Let the result land

> A shared, frozen encoder extracts a feature map that the scoring head uses to assign a score to each region. We train the head on labeled regions and evaluate it on held-out regions. The head improves accuracy but increases latency.

The final sentence keeps the benefit and cost at equal grammatical rank. Sharing the subject removes a small restart, while “latency” remains the closing limitation. The short sentence works because it completes a result after the fuller interface and protocol sentences, not because short sentences are intrinsically clearer.

## What the paragraph now does

The first sentence establishes how the representation reaches the region-scoring operation. The next takes the established head into training and evaluation, ending on the held-out setting. The last reports the head's accuracy–latency trade-off. The research progression has not changed; the sentence boundaries now match its three local jobs.

The shared encoder, frozen state, feature map, one score per region, training data, evaluation data, and both sides of the result are retained. No baseline, numerical gain, reason for freezing, causal explanation, deployment setting, or preference between accuracy and latency has been added.

## 中文说明

这里改的不是“短句太多，所以一律拉长”，而是原稿把一组完整关系切成了几个同等重音的陈述。第一句让主句交代表示、从句交代用途；第二句把训练与评估放在同一协议中，但分别保留数据条件；末句用短句收住收益与代价。head 的身份、两个实验动作和真实转折都保留，重复的 We、句界和代词则可以调整。

## Related guidance

- [S1: subjects and verbs](../skills/revise-research-writing/references/sentence-craft.md#s1)
- [S2: connections between sentences](../skills/revise-research-writing/references/sentence-craft.md#s2)
- [S9: information units and rhythm](../skills/revise-research-writing/references/sentence-craft.md#s9)
- [Selective final language pass](../skills/revise-research-writing/references/final-language-pass.md)
- [More worked examples](before-after.md)
