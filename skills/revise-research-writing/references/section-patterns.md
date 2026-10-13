# 按章节使用的功能模式与原创例子

所有英文例句及数字均为虚构教学材料，例中的事实作为已给定前提。Story模式可重组这些功能；sentence-only模式在原有功能内改善表达。共同的事实与范围规则见SKILL.md。

## Abstract：让中心结果回答开头的问题

先找摘要的一条主线：具体问题 → 回答它的关键选择 → 中心结果 → 结果带来的认识。保留能定义发现、提供比较参照或说明范围的数字，不必给每个模块和数据集分一句。方法论文可以从能力或资源需求出发；不必伪装成未知机制研究。没有结果时保留研究问题与计划状态。

以下是事实完整的虚构摘要。允许L4重组时，可以把它写成更紧密的论证；不是固定句数模板。

Before: “We study whether retaining earlier observations improves answers about objects that have left the camera's view. We add a memory to a frame-only system using the same image encoder. The memory retains observations from the previous 20 frames. Other settings are fixed. On a test set of 600 video clips, accuracy is 72% without memory and 78% with memory. Both systems have a measured latency of 20 ms per query. The comparison shows that retained observations remain useful for answering these questions after an object leaves the view.”

After: “We test whether retaining earlier observations improves answers about objects that have left the camera's view. We equip the frame-only system with a memory that retains observations from the previous 20 frames, keeping the image encoder and other settings fixed. On 600 test video clips, accuracy increases from 72% to 78%, while measured latency remains 20 ms per query. The comparison shows that retained observations remain useful for answering these questions after an object leaves the view.”

问题围绕历史信息是否有用；设计提供历史；比较给出收益和测得的代价；末句解释该结果对问题的回答。任务、20帧、600段、72%/78%、20 ms和固定条件均来自Before。末句若只重复读者已明确得到的判断，可以省去，不必为了“意义”另添一句口号。

句级例：
Before: “We perform an evaluation of reconstruction error for both settings.”
After: “We evaluate reconstruction error for both settings.”

<a id="introduction"></a>
## Introduction：让下一段接住同一个具体问题

每段让问题更具体：已有能力或条件 → 尚未满足的需求 → 本研究的选择。文献先说明什么已解决，再建立真正剩下的问题；“还没有人用我们的模块”本身不是重要缺口。转入本研究时，设计应直接接住前文留下的对象或困难，而不是突然报方法名。

以下两段均为虚构教学输入，允许L4–L5重组；不增加文献或机制事实。

Before:

“Earlier observations can provide information about objects that have left the view. Our task is to answer questions about these objects. A frame-only system receives no earlier observations.

We retain observations from the previous 20 frames in a memory and make them available to the question-answering system.”

After:

“Our task is to answer questions about objects that have left the view. Earlier observations can provide information about these objects, but a frame-only system receives no such observations.

We give the question-answering system access to this history through a memory that retains observations from the previous 20 frames.”

第一段建立任务与输入差别，下一段的this history接住缺少的信息。can仍表示可提供帮助，没有强化成所有问题都必须依赖历史。若研究没有比较记忆保留策略，就不另造“哪种策略最优”的缺口。引言末段可以交代主要发现，也可以收束到关键设计；清楚的CVPR贡献列表可以保留。

句级例：
Before: “The difference of the two settings is the availability of previous frames.”
After: “The two settings differ in whether previous frames are available.”

## Related Work：比较有关的选择，准确归属

功能：围绕信息来源、假设、目标或接口组织相关方法；说明为什么这一区别与本研究有关。不要每段只罗列作者名，也不要把“与我们不同”写成前人缺陷。

Before: “Method A predicts from a single image. Method B predicts from a video segment.”

当这确为已核实文献事实时，story revision可写：

After: “The two methods use different temporal inputs: Method A predicts from a single image, whereas Method B predicts from a video segment.”

这里将两个已有输入条件放到同一比较轴上，没有给文献添加新的训练或评估事实。

句级例：
Before: “Method A is different from Method B in the supervision utilized.”
After: “Method A and Method B use different supervision.”

上下文已说明具体监督类型时，这种缩写能减少重复；否则直接写出监督类型更清楚。

## Methods：概念依赖先于实现罗列

功能：先说明对象及输入输出，再写关系、设计、训练与推理。公式前让读者知道它定义/计算什么；公式后解释其操作或含义。不要删掉改变可复现性和可用输入的关键条件。

Before: “The utilization of a projection operation is adopted for the transformation of the feature vector into the score space.”
After: “A projection maps the feature vector into score space.”

若原式明确为linear，可以保留“linear projection”；不能因常见实现而自加linear。

衔接例：
Before: “The loss is defined below as a comparison between the predicted mask and the reference mask.”
After: “The loss below compares the predicted mask with the reference mask.”

这是已有对象和比较功能的整合；具体损失形式、归一化、权重和梯度路径保持原样。发现公式与文字不一致时单列，不用润色掩盖。

## Experiments：问题、条件、关键比较、含义

功能：用已有比较问题或中心发现领起本段，再给判断它所需的条件与关键证据。正文提取表中重要对照，不逐格报数；平均值、波动、预算和基线差异与结果放在一起。结尾只有在能回答开头问题或增加解释时才写，不必把数值再说一遍。

虚构输入：同一编码器、相同训练步数、三个种子；两种头的平均准确率为71%与73%；没有显著性检验。

Before: “Our head is significantly superior. The results are shown in Table 2.”

内容校准建议：
After: “With the same encoder and number of training steps, the new head reaches 73% mean accuracy, compared with 71% for the baseline across three seeds.”

这里用比较条件与实际差值代替空泛的superior。significantly的证据问题在审校说明中处理。

句级例：
Before: “We conduct the scoring of every prediction using the same threshold.”
After: “We score every prediction with the same threshold.”

<a id="analysis"></a>
## Analysis：从观测走到它支持的解释

先让读者看见实际变化，再说明该变化回答了什么问题。测量、解释和更广意义可以相邻，各自承担不同工作。主题句若已清楚报告发现，后句就提供条件、比较或解释，不再退回“We conduct an analysis”。

原创等义段落：

Before: “The average error is higher in the perturbed-calibration setting. The images and model weights are the same in both settings. These results suggest that calibration quality may affect prediction accuracy.”

After: “With the same images and model weights, the perturbed-calibration setting has a higher average error. This difference suggests that calibration quality may affect prediction accuracy.”

条件先让比较可读；this difference回指测量差别，suggests/may保留原有解释强度。没有把相关差别升级为已证机制。只允许固定句序/句数时，保留三句，仅局部接顺。

若本段只是报告“低位深内存更少、重建误差相同”，这一对照本身已回答资源权衡，可以直接停在结果句。更广的解释需要已有材料；不用自动追加防御句、未来计划或泛泛总结。

句级例：
Before: “The error increase is larger in images that contain thin structures.”
After: “Error increases more in images with thin structures.”

“increases more”保留变化量，不能改成“is higher”而混淆绝对误差。

## Limitations：具体条件、可见影响、真实未知

功能：说明在哪些输入/任务/资源条件下尚有限制，以及已观察或可能的影响。与相关结果相邻地陈述范围，专节再归纳；不必用泛化的“未来还有大量工作”结尾。

Before: “Our method has several limitations and may not work in all cases.”

仅当作者已有这一事实：
After: “The method requires calibrated cameras. Its behavior with inaccurate calibration has not been evaluated.”

具体输入要求和未评估条件，让读者知道结果的使用范围。

句级例：
Before: “Evaluation on images from other sensors remains to be conducted.”
After: “Evaluation on images from other sensors remains pending.”

pending精确表达当前状态，比泛泛的future work更直接。

## Captions：告诉读者看什么、如何读、范围是什么

功能：主题/比较关系 → 面板与坐标 → 关键条件与统计量 → 证据允许的观察。具体图不需要机械包含所有项；图注不能漏掉误差条定义、不同数据量、log坐标等会改变理解的条件。

虚构图：固定训练步数，横轴缓存长度，纵轴均值准确率，阴影为三个种子的标准差。

Before: “Results with different settings. Our method performs better.”
After: “Accuracy as a function of cache length at a fixed number of training steps. Curves show the mean over three seeds; shading shows one standard deviation.”

这是依据给定图元数据补全读法的L4修订，不是仅凭Before做等义润色。若图支持一个明确趋势，开头还可以用一句具体观察引导读者。

详见 [figures-and-captions.md](figures-and-captions.md)。

## Conclusion（需要时）：回到已经建立的判断

功能：说明已有结果改变了什么理解，保留实验范围；不在结尾首创结果、普适性或保证。没有独立结论节也不影响这一功能。

Before: “Our work solves efficient reconstruction and opens a new paradigm.”

若已知证据仅为一个数据集上内存降低且误差相同：
After: “The comparison shows that memory use can be reduced on the evaluated dataset while keeping reconstruction error unchanged.”

这个结尾把具体发现与资源意义连在一起。计划稿相应使用“tests whether”，由真实进度决定时态。

## 外部写法来源

摘要的信息功能另参考[Nature官方摘要指南](https://www.nature.com/documents/nature-summary-paragraph.pdf)（2019），段落与引言推进另参考[社区Nature类写作模块](reference-integration.md#nature)。它们是外部编辑思路，不作为源论文的新增统计。只取对当前论文有用的功能关系；目标会议、用户范围和已有科学内容决定最终写法。
