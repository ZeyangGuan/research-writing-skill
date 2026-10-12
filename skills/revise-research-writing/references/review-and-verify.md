# 客观旧新对比与交付验证

## 1. 分开三个问题

- **表达**：对象、动作、衔接、歧义与阅读负担是否改善？
- **故事**：问题、观点、论证顺序和贡献关系是否更易跟随？
- **研究与证据**：事实、结果、方法新意或支撑范围是否真的改变？

不能用“句子更流畅”推导“贡献更强”或“更可能录用”。研究完全未变时，故事可能更清楚，但证据没有增量。不要因为版本名较新就默认更好。

## 2. 逐项决策，不用改动率评质量

对重要改动给出以下之一：

- **保留原句**：说明它已经完成什么工作，或者改写损失了什么。
- **采用修订**：给出具体障碍与收益，并说明必要代价。
- **撤回修订**：新句更空、更绕、改变范围或缺少依据。
- **内容待审**：研究口径、事实、新增归属或主张强度发生变化，超出本轮纯语言授权。

短任务不必给每个冠词做登记；整章若用户要求逐句审核，则覆盖修改与保留句，不只展示成功案例。逐句对应可以一对一、一对多或多对一，不能让拆合句隐藏删掉的信息。

## 3. 原创对照：新句可能更差

Original: “The model uses a fixed-size memory to store recent observations.”
Candidate: “Our powerful framework effectively leverages an advanced memory mechanism for robust temporal understanding.”
Decision: 撤回。候选丢掉fixed-size与recent两项含义，新增未经证实的能力，动作更模糊。

Original: “We compare the two heads using the same frozen encoder.”
Candidate: “The two heads are compared.”
Decision: 保留原句。简短的候选删去了公平比较条件。

Original: “The larger head improves average accuracy, but it is slower.”
Candidate: “The larger head improves accuracy.”
Decision: 撤回。删掉平均范围与速度代价并非润色。

Original: “We will evaluate the model on a second dataset.”
Candidate: “The model generalizes to a second dataset.”
Decision: 撤回。计划变成已证实的泛化结论。

Original: “We utilize a shared encoder for both views.”
Candidate: “We use a shared encoder for both views.”
Decision: 可采用，理由仅为常用词更直接；不把这一词替换夸大成故事改善。

## 4. 语义保真清单

根据稿件实际内容核对：

1. 对象与角色：谁预测、谁监督、什么进入模型、什么只用于评估。
2. 阶段与时间：joint不是sequential，训练时可用不等于推理时可用，过去信息不是未来信息。
3. 范围：all / some / average，may / can / must，only / without，具体任务与数据集。
4. 比较条件：预算、骨干、数据曝光量、样本数、分辨率、模型容量、选择协议。
5. 数值：符号、单位、分母、百分数与百分点、均值与单次结果、误差条定义。
6. 论证强度：目标、设计意图、观察、解释、因果、证明分别是什么。
7. 状态：已完成、待完成、失败、未知不可互换。
8. 引用：作者、归属、版本和文献事实没有被润色悄悄增加。

固定词元/数字检查可以抓意外改动，不能证明等义。“less data”与“better at fixed data”可能没有任何数字变化，却已改变研究问题。

## 5. 文件与版面验证

- 核查只改了授权文件；保留可对比的旧版与可编辑新版。
- LaTeX/Word等源稿检查公式、标签、引用、表图、标题与未完成标记；不要为“洁净稿”删掉必要待办事实。
- 若实际修改可编译稿，能运行编译时检查编译结果与引用；渲染后查看溢出、断行、图注与页数变化。
- 若未编译或没有工具，只报告文本/静态检查，不把旧PDF当新PDF交付。
- 交付前检查附件与源是否是同一版，不把撤回候选当最终稿。

## 6. 简短报告样式

“本轮为句级润色。采用的主要改动是明确执行对象、减少名词堆叠、修复指代；保留原有论证顺序与技术条件。某处范围冲突已单列待审，未夹带修改。可读性局部改善；研究问题和证据未变。已核对源文本与差异；版面未检查。”

依实际发生的工作填写，不机械照抄，不虚构计数。用户要求评分时，可按具体维度解释判断依据，但不要用伪精确总分掩盖证据缺口，也不要以改动数量、字数下降或新版本身份加分。
