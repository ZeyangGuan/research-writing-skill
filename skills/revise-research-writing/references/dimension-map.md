# 从来源到动作：L / D / S 对照

**L 是编辑尺度，D 是观察维度，S 是可调用的句子工具。** 三套编号服务不同问题，不是需要顺序完成的检查表。只在核对来源或选择工作尺度时读取本页。

The layer, dimension, and card IDs are lookup systems, not scores or measured frequencies. A paper may inform several dimensions; a sentence card uses only the mechanisms relevant to its task.

## 1. D1–D15：读论文时观察什么

| 维度 | 观察问题 | 常用编辑层级 | 运行入口 |
|---|---|---|---|
| D1 句子骨架 | 主语、谓语、对象与限定放在哪里？ | L6 / L8 | S1、S4–S8 |
| D2 用词与论证强度 | 动词和情态词如何区分操作、观察、解释与主张？ | L7 / L2 | S1；review-and-verify |
| D3 Given → new | 已知信息怎样交给下一句？ | L6 / L5 | S2、S3、S4、S9 |
| D4 指代与连接 | 指代、连接词怎样表达真实逻辑关系？ | L6 / L7 | S2、S3、S5、S7–S9 |
| D5 句长、节奏与密度 | 哪些信息该放在一起，哪些应该分开？ | L6 / L8 | S4、S6、S7、S9 |
| D6 段落功能 | 本段增加什么认识，怎样接到下一段？ | L5 / L4 | 八层工具 L5；章节模式 |
| D7 Abstract | 怎样压缩论证并保留适用范围？ | L4 / L1 | 章节模式 Abstract |
| D8 Introduction | 问题为什么重要，设计为什么需要？ | L1 / L4 | Story；章节模式 Introduction |
| D9 Related Work | 怎样组织比较轴并准确归属？ | L4 / L3 / L2 | 章节模式 Related Work |
| D10 Methods | 概念依赖与技术接口怎样展开？ | L4；涉及主张时 L2 | 章节模式 Methods |
| D11 Experiments | 比较问题、固定条件、测量与结论怎样对齐？ | L4 / L2 | 章节模式 Experiments |
| D12 Analysis | 观察、解释与更广意义怎样区分？ | L4 / L2 | 章节模式 Analysis |
| D13 Limitations | 怎样说明有限结果和真实未知？ | L4 / L2 | 章节模式 Limitations |
| D14 全文结构 | 主文和附录分别承担什么工作？ | L3 / L1 | 八层工具 L3；Story |
| D15 图表与图注 | 视觉组织怎样支持比较和读数？ | L2 / L3 / L4 | 图表与图注指南 |

上述层级是使用入口。涉及主张强度的小词也可能跨到L2；不能因改动短就认为它只属于语法。逐篇观察的实际D/L对应保留在[观察索引](observation-index.json)。

## 2. S1–S9：维度怎样变成可用动作

| 句卡 | 主要观察维度 | 直接机制来源 | 不能丢的边界 |
|---|---|---|---|
| [S1 主体与动作](sentence-craft.md#s1) | D1 / D2 | H01；X12 | 不虚构施动者；被动可突出模块状态 |
| [S2 对象接力](sentence-craft.md#s2) | D3 / D4 | X08；H11 | 并列观察不强凑因果或数据流 |
| [S3 关系名词回指](sentence-craft.md#s3) | D3 / D4 | X02；X06；X11 | division/comparison不是cause；清楚代词可保留 |
| [S4 平行对照](sentence-craft.md#s4) | D1 / D3 / D5 | H04；X10；X12 | 句法对称不代表收益对称 |
| [S5 阶段与限定](sentence-craft.md#s5) | D1 / D4 | H09；H03 | only、jointly、冻结与更新保持原作用域 |
| [S6 前置堆叠](sentence-craft.md#s6) | D1 / D5 | H13；X03 | 保留两项依据及其观察/假设地位 |
| [S7 完整条件](sentence-craft.md#s7) | D1 / D4 / D5 | H01；H10；X06 | if/only if/unless不能互换；假设不变成已实现 |
| [S8 局部让步](sentence-craft.md#s8) | D1 / D4 | H13；X07；H15 | 实际收益与局部限制都保留 |
| [S9 信息单位与节奏](sentence-craft.md#s9) | D3 / D4 / D5 | X02；H12 | 动态关系与不变量各自清楚；不机械拆短 |

这是编辑检索映射，不声称每条源观察都具有该行的全部D标签。九卡共有22条直接机制条目，来自17篇论文；30篇语料还支持章节、故事、论证和图表指导。不要把“30篇语料”说成“每张卡均经30篇验证”。

## 3. 四条完整追溯示例

- **H09 → D1/D4 → L6–L8 → S5。** p5 §3.5以训练与训练后两个时间框架交代不同参数状态。可用动作是对齐阶段与更新/冻结对象；不能把联合优化改成顺序优化。[来源与版本](sources-and-patterns.md#h09)
- **X02 → D4/D5 → L6–L8 → S9。** p5 §3.2将变化中的表示与需重算的条件放在一起，再单独写不变的causal约束。可用动作是按信息工作分配长短句，而不是统一平均句长。[来源与版本](sources-and-patterns.md#x02)
- **H08 → D1/D2/D4 → P7条件范围 → S7相关背景。** p4 §3.2限定何时某种直接输出才使用特定prediction名称；这是定义边界。p1的假设回指则让假设、设计判断与预期好处分层。两者支持保留范围，不新增九卡直接来源计数。[来源与版本](sources-and-patterns.md#h08)
- **X15 → D6/D8/D10 → L5/L4/L1。** p2由并行计算引出重排与通信代价，再让局部性设计回答同一问题。它支持问题接续和方法组织，不能硬塞成只需换词的句法规则。[来源与版本](sources-and-patterns.md#x15)

## 4. 怎样查，而不重读全部材料

1. 从句卡中的H/X编号找到[来源页](sources-and-patterns.md)的对应条目。
2. 需要D维度时，在[观察索引](observation-index.json)检索该论文ID；每项给出物理页/章节与编辑层级。
3. 用[语料清单](corpus-manifest.json)取得所读版本与官方记录。版本不同，页码也可能不同。

30篇各有D1–D15的定位，覆盖L1–L8。450个维度记录是结构化近读索引，不是450项独立实验，也不证明规律出现频率。完整版权论文由原站点提供；本包只提供原创分析、书目和定位。
