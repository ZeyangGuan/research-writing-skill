# 成稿定点清理

完成指定层级的修改后，只清理下列可定位的问题。没命中就原样保留，不再次润色全部文字，不重开故事。保持标题、段落数量和顺序、公式、图表与引用；句子拆合服从用户要求。

这一步改善表达，不检测AI作者身份，也不承诺改变检测分数。全部英文例句为原创教学文本，前后实质信息相同。

## F1 重复同一工作

**看什么**：相邻句在相同条件下重复同一命题，后句没有新增信息或必要解释。相同主语、相同骨架不算命中。

**怎么改**：合并重复命题，留下全部不同信息。

Before: “We use one fixed threshold to score all predictions. All predictions are scored with this single fixed threshold.”

After: “We score all predictions with one fixed threshold.”

**保留**：“We measure accuracy on the validation set. We measure latency on the deployment device.” 两句测量对象与条件不同，整齐有助比较。

依据：H12 p1连续We承担不同研究动作；X12 p3重复输入—输出骨架定义不同接口。

## F2 没有信息的提示或总结

**看什么**：提示壳仅宣布要说明一件事，或总结只是同义复述；缩短后不损失命题、指代或必要导航。

**怎么改**：直接给已有判断；保留真正的新解释和文档入口。

Before: “We would like to point out that both heads use the same frozen encoder.”

After: “Both heads use the same frozen encoder.”

**保留**：“The two cached states remain constant during denoising. This allows the model to reuse them at every step.” 后句给实现后果，不能按this allows开头删除。

依据：X11 pp2–3从状态不变接到缓存；H06 p4从目标重写接到下一问题。

## F3 反转包装重复同一命题

**看什么**：否定—转折只重复并抬高同一个命题，没有排除真实可能性，也没有独立的否定事实、设置差别或让步。

**怎么改**：把重复的正面命题直接说清。真实对照的两半都保留。

Before: “This is not just a comparison; it is a controlled comparison at a fixed memory budget.”

After: “This is a controlled comparison at a fixed memory budget.”

**保留**：“The encoder is updated during training, but it is frozen at inference.” 参数状态确实不同，不能删一半。

依据：H09 p5阶段对照；H15 pp7–8让步说明局部下降与研究目的；H12 p1反预期结论由真实结果支撑。

## F4 同义修饰堆叠

**看什么**：相邻修饰仅重复同一种评价，没有增加技术属性或程度差别。可能对应独立主张的词不在这一步擅改。

**怎么改**：保留准确修饰，去掉同义重复。

Before: “We use a simple and straightforward projection to map features to scores.”

After: “We use a simple projection to map features to scores.”

**保留**：“We use a sparse, low-rank projection to map features to scores.” sparse与low-rank是不同属性。统计意义的significant也不能当装饰删除。

依据：X09 pp1–3的language-free有明确阶段；H13 p9的额外训练限定对应具体资源。

## F5 标点或名词化绕远了简单关系

**看什么**：插入停顿割碎一个简单属性，或名词化遮住已有执行者与动作；没有承担定义、对照或公式入口功能。

**怎么改**：属性放回名词旁，已有动作恢复为动词。

Before: “We use the same encoder—the encoder is frozen—for both heads.”

After: “We use the same frozen encoder for both heads.”

Before: “The computation of each score is performed by applying the same linear projection.”

After: “The same linear projection computes each score.”

**保留**：“The predictor has two outputs: a score and an uncertainty estimate.” 冒号给完整定义；引出公式的句子、编号与必要列举也保留。

依据：H05 p1冒号解释双向过程；H07 p3名词化承接协议；H01 p4被动句突出模块状态。名词化、被动或长句本身不触发。

## 交付前四个判断

- 能指出每次修改解决F1–F5中的哪个问题；未命中句逐字保持。
- 对象、动作、数字、算法、量词、条件、否定/让步、引用与结果状态没变。
- 没有把两档比较写成趋势，或新增主体、因果、实验目的。
- 原句更好就恢复；内容疑点单列。较宽的旧新比较另用[review-and-verify.md](review-and-verify.md)。

需要核对某条来源时，按H/X编号查看[sources-and-patterns.md](sources-and-patterns.md)对应条目；常规清理无需加载整份来源或manifest。
