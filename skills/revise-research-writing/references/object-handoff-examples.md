# 对象接力：两个按需实例

只在[S2](sentence-craft.md#s2)的短例不足以解释当前衔接时使用。以下全部是原创、虚构且两版事实相同的教学材料；来源只支持写作机制。

## 1. 跨节短桥：同一对象换了工作

前一节已经让读者认识一个对象，新一节可能按用途给它另一个名字。直接交代两者是同一量，以及它接下来做什么。短桥已经完成这种交接时，不必为了凑段长再加背景。

已给上下文：The segmenter returns a foreground probability map p for each frame.

Before:

This section describes weighted reconstruction. The foreground probability map p returned by the segmenter is used as the pixel-weight map w. The reconstruction loss uses w to weight each pixel's squared residual. No additional normalization is applied to p.

After（允许段内重组）:

The segmenter's probability map p serves as the pixel-weight map w for reconstruction, without additional normalization. The reconstruction loss uses w to weight each pixel's squared residual.

动作：将泛泛的章节宣告换成实际对象交接；第一句把旧名 p 与新角色 w 绑定，第二句让 w 承担已有操作。没有改变概率图、归一化方式或损失。这里“换名字”是角色说明，不是新增变换。

Keep: We use the probability map directly as reconstruction weights.

如果后文不需要符号 w，这句已经够用，不必额外创造功能名。

来源：[H01](sources-and-patterns.md#h01)，arXiv v2，物理 p6 §3.3，自条件与CFG之间的两句短桥。前句回收中间预测，后句将同一量归为条件 c，再交给外推公式。它是 S2 的具体用途，不是新的写作层级。[所读版本](https://arxiv.org/pdf/2605.10938v2)。

## 2. 统计顺序：让中间汇总成为下一步输入

Before:

We average three measurements for each of the four specimens. This gives one mean for each specimen. For the calculation of the group mean, we average the four means obtained for the four specimens.

After:

For each of the four specimens, we average three measurements to obtain one specimen mean. We then average these four specimen means to obtain the group mean.

动作：先用一个动词交出 specimen mean，再以 these four specimen means 接住它。三次测量→每个 specimen 的均值→四个均值的组均值保持不变；缩写发生在重复解释，不在统计层级。

Keep: We report the mean over four independent runs.

真正只有一层汇总时，这样已经清楚，不需要制造中间产物。

来源：[H03](sources-and-patterns.md#h03)，官方18页正文的物理 p9 §5.1 第一段。每个离线模型的两次适配先给出单模型分数，再汇总五个模型的分数；下一段才转向集成对象。该例借用对象交接机制，不复制论文的样本数或独立性结论。[所读版本](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/11149.pdf)。
