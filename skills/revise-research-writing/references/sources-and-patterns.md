# 来源与可迁移模式

本页只在需要来源或规律核对时按H/X/P编号检索。日常润色直接读取相关[S1–S9卡](sentence-craft.md)。

## 语料与读法

固定快照：2026-10-12；两位目标作者各15篇，共30篇独立论文。窗口以2025-04-12至2026-10-12的正式venue/录用时间为准，不以最早预印本日期为准。第一/共同第一、末位或可核实通讯作者均可纳入；本次所选30篇均符合目标作者末位署名；Pixel Mean Flows、Fractal、Noise Conditioning与PISA另有明确通讯标记。

这是一组有边界的学习语料，不是全球穷尽性“最新30篇”证明。TMLR按同行评审ML期刊纳入，未改称TPAMI/IJCV；NeurIPS 2026条目在快照日期为已录用、会议未召开。DHN与Fractal所读为公开作者版，其最终期刊PDF未取得。Nat-ARC另行提及的独立补充未取得。各版本见下方书目及[corpus-manifest.json](corpus-manifest.json)。

语料观察包含正文与实质附录的章节分析和句子近读；逐篇维度定位见[观察索引](observation-index.json)，维度含义见[维度映射](dimension-map.md)。页码指所读PDF物理页。图面核验是有记录的抽样，不等于所有图逐张检查。作者身份用于选文，不能据此归因个人执笔。以下都是对合作论文的写作分析。

### 本轮独立复读与取优（2026-10-13）

两组各自分析既定15篇，再各选6篇作局部细读，最后按编辑任务取优。He组为H01/H03/H05/H06/H08/H14，Xie组为X02/X03/X08/X10/X11/X15；细读聚焦句子、对象交接和段际接口。

本轮主要细化已有机制，加入少量原创写法示例；分阶段的原创对照未显示稳定的整体优势。样本受研究题材、合作团队和可取得版本影响，各篇材料范围见下方书目及[语料清单](corpus-manifest.json)。

## 一、先看三组最有用的具体机制

### 1. 同一个对象，承担不同角色

- H04摘要将输出空间与损失空间放进对称分句；两个分句语法相似，回答的问题不同。
- X01引言用平行骨架比较表示用于生成输入与用于对齐目标的作用。
- X10引言让真实视频与模拟视频分别作主语，直接说明评估和训练分工。

**写作动作**：用相同骨架保留不同的主语、谓语或宾语，让真正的比较轴显露出来。不要把两路作用都压成“improves performance”。适合L6–L8的等义表达，也可服务更高层对比。

原创演示：

Before: “The vector is used for the summarization of the scene, while preservation of each feature’s position is the role of the map.”

After: “The vector summarizes the scene, while the map preserves the position of each feature.”

### 2. 前句产物成为后句起点

- H01先定义一套接口，再用具体关系名词回收它、说明新用途。
- H06一次目标重写揭示新的输入问题，新认识成为下一段主语。
- X08的标注动作产生metadata，metadata再支持诊断切片。
- X15的并行方式引出通信代价，通信代价成为设计局部性的理由。

**写作动作**：保留让信息向前走的那个名词。一个段落可以自然换主语，只要新主语来自前文，而不是为了句式多样性随机更换。

原创演示：

Before: “The annotators assign error-type labels to each failure. A comparison of how models fail is possible using these labels.”

After: “The annotators label each failure by error type. These labels let us compare how the models fail.”

### 3. 条件和阶段写在动作附近

- H01摘要用主句描述主要阶段，从句说明末步转换；方法中的被动句突出模块使用阶段。
- H09用训练/训练后两个框架，比较哪些参数更新、哪些保持不变。
- X06的条件从句限定不能拟合的情形；X08的结果短语限定无工具的测量。
- H13用额外训练这一参照对象解释资源节省，同时保留测试时优化。

**写作动作**：让only、until、unless、during等词紧邻被限定的动作。长句若承载一个完整条件关系，可以比拆成三句更清楚。

原创演示：

Before: “The system performs refinement on continuous states until the final step. At that step, a shared head performs the conversion of these states into event labels.”

After: “The system refines continuous states until the final step, when a shared head converts them into event labels.”

## 二、两组语料各自带来的写作选择

这些是本组选文中反复出现的动作，不是某位作者的固定个人口吻。题材、合作者和论文系列都会影响观察。

### 何恺明组：让对象与推导带动阅读

**H-A 概念对象持续推进。** H02、H04、H10、H11分别将分布变化、两种空间、平均速度、递归组合单元作为持续对象。可学的是每段在同一对象上增加一种关系；不是所有稿件都需要数学概念型开场。

**H-B 技术阶段用准确句法显露。** H01、H03、H09、H11、H12通过时点、并行框架、参数状态和不同遍历方式使流程易懂。被动语态和重复模块名有时正是清楚的来源。

**H-C 研究目的可以组织复杂结果。** H06的问题—解决路线、H14固定现象更换检验轴、H15保留局部下降以完成科学拆解，都说明实验不必是每一步都更高的排行榜。H13则把实践价值落到具体免除的资源。

### 谢赛宁组：让角色、比较轴与实践问题带动阅读

**X-A 先说旧选择为何合理，再说明前提变化。** X06、X02和X11把接口或融合设计放回原有条件中理解。可迁移的是设计理由，不能把每篇都包装成推翻旧范式。

**X-B 平行句法保留多种角色。** X01、X04、X10、X12、X14用对称骨架说明不同用途、非对称收益、输入输出或证据形式。相同句式有助比较，不需要机械轮换同义词。

**X-C 新增问题来自已有比较的范围。** X09从方法差异转向数据条件；X07由反预期例子进入系统检验；X05将旧任务上的进展与持续任务的难题接起来；X15由并行计算走向通信和优化。段落连贯来自问题实际相接。

归纳关系：H-A与X-A/X-C共同支持下文P2/P6；H-B与X-B共同支持P1/P3/P4/P9；H-B与X-C支持P5/P7；H-C与X-C支持P8。每组先有上述逐篇观察，再做这些跨组抽象；具体支持与反向例仍分别列出。

### 运行卡与研究归纳的关系

下表是检索映射，不把宽泛归纳当成每张卡的直接证据。卡内源语境和物理页说明具体支持的句法动作；本页后半给出30篇书目与版本。

| 运行卡 | 组内归纳 | 跨组模式 | 直接机制来源 |
|---|---|---|---|
| S1 主体与动作 | H-B、X-B | P1/P9 | H01、X12 |
| S2 对象接力 | H-A、H-B、X-C | P2 | X08、X03、H11；扩展示例H01、H03 |
| S3 关系名词回指 | H-A、X-A | P2/P5 | X02、X06、X11 |
| S4 平行对照 | H-B、X-B | P3 | H04、X10、X12 |
| S5 阶段与限定 | H-B、X-B | P3/P7 | H09、H03 |
| S6 前置堆叠 | H-B、X-B | P4 | H13、X03 |
| S7 完整条件 | H-B、X-B | P4/P7 | H01、H10、X06 |
| S8 局部让步 | H-C、X-C | P5/P8 | H13、X07、X11、H15 |
| S9 信息单位与节奏 | H-B、X-B | P2/P4/P9 | X02、H12 |

九张卡只收录与具体编辑动作直接有关的来源定位。其余论文仍支持章节、故事、图面和论证指导。原创教学例属于独立表达示范，不能倒推为来源论文的实验事实。

## 三、跨组反复模式与有用的反例

### P1 对象明确比词汇华丽重要（L6–L8）

支持：H01 p1/p4；H04 p1；X01 p3；X12 p3。将主语、动作和对象写清，定义接口时重复骨架可以帮助阅读。

选择条件：对象与操作已经确定。反例/代价：H07 p3的名词化概括整条协议，具有承接作用；名词化不应一律删除。

### P2 衔接来自信息依赖（L5–L6）

支持：H06 p4；H10 pp4–5；X02 p1/p5；X08 p2；X15 p2。前句对象、结果或代价成为下一句需要处理的事情。

选择条件：依赖关系真实存在。反例/代价：普通并列发现不需要硬凑因果；H04的论证first/then也不是算法执行次序。

### P3 平行骨架让差别可见（L6–L8）

支持：H04 p1；H05 p1；H09 p5；X01 p3；X04 p4；X10 p2；X12 p3。

选择条件：比较轴明确，保留各路不同宾语和条件。反例/代价：对称语法不代表结果对称；X04的两种模态并未被写成完全互相提升。

### P4 短判断接具体解释，长句承载完整关系（L6/L8）

支持：H03 p9；H05 p1；H13 p4；X03 p1；X02 p5。

选择条件：按功能决定长度。反例/代价：H13两项经验前提前置会延迟主谓，可拆成两项发现再引出提议；不能只保留一个响亮主句而丢掉理由。

### P5 连接词的意义在于它指向什么（L6/L7）

支持：H02 p3；H07 p4；H12 p5；X01 p3；X03 p3；X11 pp2–3。

选择条件：先识别对照、时间或推导。反例/代价：H14同时有叙述导航与实际执行顺序；同样的next/then不能不加区别地替换。

### P6 问题与设计一一接住（L1/L4）

支持：H06 p1/p4；H10 pp4–5；X03 p3；X12 p3；X15 p2。

选择条件：已有材料确实给出这些问题和设计。单篇特例：H12的挑战共识开场依赖实际反直觉结果；X11主动声明贡献类型的否定开头是其自选定位，不是所有论文的模板。

### P7 条件是结论的组成部分（L2/L4）

支持：H08 p4 §3.2的定义边界；H09 p8；H13 p9；H14 pp9–10；X06 p2；X08 p1；X09 pp1–2。

选择条件：读者需要就近知道任务、资源和比较设置。反例/代价：不要为每个普通陈述重复全部协议；保留会改变当前结论含义的条件即可。

### P8 有限结果可以推动理解（L2/L4）

支持：H15 pp7–8；X01 pp9–11；X05 p2；X10 p2；X11 p3。

选择条件：把收益、代价或另一种成功标准说具体。反例/代价：科学拆解可以保留局部性能较差的步骤，最优配方选择却未必应这样做；选择由研究目的决定。

### P9 好句不需要遵守统一外形（L6–L8）

支持：H01 p4被动突出阶段；H12 p1连续We承担不同工作；X05 p1的it有唯一清楚先行词；X12 p3重复接口句法。

选择条件：句法已经清楚完成工作时保留。真实局部反例：X13 p1出现重复情态动词的语法问题；修一个语法点不需要改变更高层论断。

这些“反复模式”指跨篇可定位的定性观察，不是统计显著性结论。上列支持不是全部语料中的出现次数；未计算词频或句长统计，就不声称存在频率规律。

## 四、逐篇书目与可迁移动作

以下H/X编号用于本包来源引用，不代表质量排名或同一会议批次的精确发表先后。

### H01

**ELF: Embedded Language Flows**

作者：Keya Hu; Linlu Qiu; Yiyang Lu; Hanhong Zhao; Tianhong Li; Yoon Kim; Jacob Andreas; Kaiming He。

Venue：NeurIPS 2026；状态：accepted/forthcoming。

[官方记录](https://neurips.cc/virtual/2026/poster/148278) · [所读版本](https://arxiv.org/pdf/2605.10938)

版本：arXiv v2, 2026-06-26; accepted venue confirmed separately

观察定位：p1摘要；p4 §3.1；p6 §3.3自条件到CFG的两句短桥，将同一中间预测命名为后续引导的条件 c。

可迁移动作：主句给连续空间中的主要动作，until/where从句给末步例外；具体名词回收一套关系，再引出新用途。被动语态可突出模块使用阶段。



### H02

**Generative Modeling via Drifting**

作者：Mingyang Deng; He Li; Tianhong Li; Yilun Du; Kaiming He。

Venue：NeurIPS 2026；状态：accepted/forthcoming。

[官方记录](https://neurips.cc/virtual/2026/poster/154240) · [所读版本](https://arxiv.org/pdf/2602.04770)

版本：arXiv v2, 2026-02-06; accepted venue confirmed separately

观察定位：p3 §3.1–3.2。

可迁移动作：从参数更新接到样本变化，再用已给定等式解释动作；理想要求、条件命题与已证性质各有明确语法位置。



### H03

**Natural Image Pretraining Improves Abstract Reasoning**

作者：Xiaoman Delores Ding; Keya Hu; Katelyn Gan; Victor Yin; Kaiming He。

Venue：ECCV 2026；状态：conference paper。

[官方记录](https://eccv.ecva.net/virtual/2026/poster/5527) · [所读版本](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/11149.pdf)

版本：Official ECCV conference-hosted PDF; 18 pages; separate supplement mentioned in text not linked on verified poster page

观察定位：p6 Fig3与p7–8 §4.3的阶段和模块比较；p9 §5.1第一段的适配→单模型分数→跨模型汇总。两处承担不同写作机制；p9不是冻结模块的主要证据。

可迁移动作：先说在既有流程中新增什么，再展开完整阶段；重复模块名来比较初始化、更新和冻结，比换近义词清楚。



### H04

**One-step Latent-free Image Generation with Pixel Mean Flows**

作者：Yiyang Lu; Susie Lu; Qiao Sun; Hanhong Zhao; Zhicheng Jiang; Xianbang Wang; Tianhong Li; Zhengyang Geng; Kaiming He。

Venue：ICML 2026；状态：published proceedings。

[官方记录](https://proceedings.mlr.press/v306/lu26t.html) · [所读版本](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lu26t/lu26t.pdf)

版本：Official PMLR volume 306, 81265–81277; PDF includes appendix

观察定位：p1摘要；p4 §4.2。

可迁移动作：将预测对象和损失所在空间拆成平行分句；先说两个边界，再处理一般情况，使形式推导具有阅读路线。



### H05

**Bidirectional Normalizing Flow: From Data to Noise and Back**

作者：Yiyang Lu; Qiao Sun; Xianbang Wang; Zhicheng Jiang; Hanhong Zhao; Kaiming He。

Venue：CVPR 2026；状态：published proceedings。

[官方记录](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_Bidirectional_Normalizing_Flow_From_Data_to_Noise_and_Back_CVPR_2026_paper.html) · [所读版本](https://openaccess.thecvf.com/content/CVPR2026/papers/Lu_Bidirectional_Normalizing_Flow_From_Data_to_Noise_and_Back_CVPR_2026_paper.pdf)

版本：CVF accepted version plus official separate supplement

观察定位：p1摘要；p4 §4.1。局部细读包括旧方案段尾与下一方案段首：先定位尚待解决的关系，再给继承对象及实际改动。

可迁移动作：冒号后的同构分句解释两个反向过程；先界定旧选择的具体限制，再让新操作解除同一限制。



### H06

**Improved Mean Flows: On the Challenges of Fastforward Generative Models**

作者：Zhengyang Geng; Yiyang Lu; Zongze Wu; Eli Shechtman; J. Zico Kolter; Kaiming He。

Venue：CVPR 2026；状态：published proceedings。

[官方记录](https://openaccess.thecvf.com/content/CVPR2026/html/Geng_Improved_Mean_Flows_On_the_Challenges_of_Fastforward_Generative_Models_CVPR_2026_paper.html) · [所读版本](https://openaccess.thecvf.com/content/CVPR2026/papers/Geng_Improved_Mean_Flows_On_the_Challenges_of_Fastforward_Generative_Models_CVPR_2026_paper.pdf)

版本：CVF accepted main text; verified CVF page has no supplement link; arXiv 13-page version additionally downloaded for appendix

观察定位：p1摘要；p4 §4.1。局部细读包括旧方案段尾与下一方案段首：先定位尚待解决的关系，再给继承对象及实际改动。

可迁移动作：问题与解法一一对应；一次改写的结果又成为下一问题的主语，使方法不是技巧清单。



### H07

**ARC Is a Vision Problem!**

作者：Keya Hu; Ali Cy; Linlu Qiu; Xiaoman Delores Ding; Runqian Wang; Yeyin Eva Zhu; Jacob Andreas; Kaiming He。

Venue：CVPR 2026；状态：published proceedings。

[官方记录](https://openaccess.thecvf.com/content/CVPR2026/html/Hu_ARC_Is_a_Vision_Problem_CVPR_2026_paper.html) · [所读版本](https://openaccess.thecvf.com/content/CVPR2026/papers/Hu_ARC_Is_a_Vision_Problem_CVPR_2026_paper.pdf)

版本：CVF accepted version plus official separate supplement

观察定位：p3 §3.1；p4 §3.3。

可迁移动作：用已给出的任务协议作为后续训练动作的依据；局部转折只修正类比失效的部分，而非否定整个视角。



### H08

**Back to Basics: Let Denoising Generative Models Denoise**

作者：Tianhong Li; Kaiming He。

Venue：CVPR 2026；状态：published proceedings。

[官方记录](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Back_to_Basics_Let_Denoising_Generative_Models_Denoise_CVPR_2026_paper.html) · [所读版本](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Back_to_Basics_Let_Denoising_Generative_Models_Denoise_CVPR_2026_paper.pdf)

版本：CVF accepted version plus official separate supplement

观察定位：p1摘要；p4 §3.2。

可迁移动作：假设先行，然后提出设计判断；明确预测空间的术语范围，再区分可合法生成与训练效果更好。



### H09

**Denoising Hamiltonian Network for Physical Reasoning**

作者：Congyue Deng; Brandon Y. Feng; Cecilia Garraffo; Alan Garbarz; Robin Walters; William T. Freeman; Leonidas Guibas; Kaiming He。

Venue：TMLR；状态：accepted journal article。

[官方记录](https://openreview.net/forum?id=KublEgx7Hv) · [所读版本](https://arxiv.org/pdf/2503.07596)

版本：Downloaded author arXiv 12-page manuscript, NOT final TMLR text. OpenReview final PDF HTTP403. PDF metadata mentions ICML 2025 template; this is NOT venue evidence.

观察定位：p5 §3.5；p8 §4.3。

可迁移动作：用对称时间框架说明训练与适配阶段谁冻结、谁更新；结果先给测试条件，模型排名变化因此容易理解。



### H10

**Mean Flows for One-step Generative Modeling**

作者：Zhengyang Geng; Mingyang Deng; Xingjian Bai; J. Zico Kolter; Kaiming He。

Venue：NeurIPS 2025；状态：published proceedings。

[官方记录](https://papers.neurips.cc/paper_files/paper/2025/hash/6d13e085b79d454da5910e4ca82a3d9d-Abstract-Conference.html) · [所读版本](https://papers.nips.cc/paper_files/paper/2025/file/6d13e085b79d454da5910e4ca82a3d9d-Paper-Conference.pdf)

版本：Official proceedings PDF used (23 pages, includes checklist and appendix); arXiv duplicate retained separately

观察定位：p4–5 §4。

可迁移动作：沿同一数学对象写推理好处、训练障碍、可行改写；从推导转到参数化时，短导航句说明论述层级。



### H11

**Fractal Generative Models**

作者：Tianhong Li; Qinyi Sun; Lijie Fan; Kaiming He。

Venue：TMLR；状态：published journal paper。

[官方记录](https://openreview.net/forum?id=Qk9kn6lOlW) · [所读版本](https://arxiv.org/pdf/2502.17437)

版本：Direct final OpenReview PDF returned HTTP403. Downloaded author arXiv version is 13 pages, and not claimed identical to the final TMLR version.

观察定位：p1摘要；p6 §4.5。

可迁移动作：先解释组合单元如何改变，再命名新概念；输入、输出、下一层的递归对象链让复杂层级可跟随。



### H12

**Is Noise Conditioning Necessary for Denoising Generative Models?**

作者：Qiao Sun; Zhicheng Jiang; Hanhong Zhao; Kaiming He。

Venue：ICML 2025；状态：published proceedings。

[官方记录](https://proceedings.mlr.press/v267/sun25g.html) · [所读版本](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25g/sun25g.pdf)

版本：Official PMLR final proceedings PDF; 34 pages including extensive appendix. PMLR volume publication date 2025-10-06; conference date used for consistency.

观察定位：p1摘要；p5 §4.4；p8 §6.2。

可迁移动作：连续We可以承担调查、解释、设计等不同工作；从单次误差到迭代累积误差，以系统性质作为中间桥。



### H13

**Highly Compressed Tokenizer Can Generate Without Training**

作者：Lukas Lao Beyer; Tianhong Li; Xinlei Chen; Sertac Karaman; Kaiming He。

Venue：ICML 2025；状态：published proceedings。

[官方记录](https://proceedings.mlr.press/v267/beyer25a.html) · [所读版本](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beyer25a/beyer25a.pdf)

版本：Official PMLR final proceedings PDF; 19 pages including appendix.

观察定位：p4 §3.3与§4；p9 §5.6。

可迁移动作：两项已有发现引出一个新操作；长前置结构可以拆为证据→提议。资源条件把免除的额外训练与仍需的测试时过程分清。



### H14

**A Decade’s Battle on Dataset Bias: Are We There Yet?**

作者：Zhuang Liu; Kaiming He。

Venue：ICLR 2025；状态：published proceedings。

[官方记录](https://proceedings.iclr.cc/paper_files/paper/2025/hash/66772e6aa61e54ae16443ae1d78a7319-Abstract-Conference.html) · [所读版本](https://proceedings.iclr.cc/paper_files/paper/2025/file/66772e6aa61e54ae16443ae1d78a7319-Paper-Conference.pdf)

版本：Official ICLR final proceedings PDF; 17 pages. Initial preprint predates the window; formal conference presentation falls inside it. Footnote star means work done at Meta/now MIT, not corresponding author.

观察定位：pp5–7 §4.2；pp9–10 §5.3–5.4。

可迁移动作：固定同一现象、逐项改变检查轴，重复句式有利扫描；从一种泛化进入另一种任务前，先界定此前证据范围。



### H15

**Deconstructing Denoising Diffusion Models for Self-Supervised Learning**

作者：Xinlei Chen; Zhuang Liu; Saining Xie; Kaiming He。

Venue：ICLR 2025；状态：published proceedings。

[官方记录](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8b52c29d1a77e3fcc6c8f90fa0ac0e8e-Abstract-Conference.html) · [所读版本](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b52c29d1a77e3fcc6c8f90fa0ac0e8e-Paper-Conference.pdf)

版本：Official ICLR final proceedings PDF; 15 pages. Initial preprint predates the window; formal conference presentation falls inside it.

观察定位：p4 §4；pp7–8 §4.3。

可迁移动作：路线段的动词与后文步骤同序；局部性能下降、研究目的与最终采用选择是不同判断，可在连贯段落中同时说清。



### X01

**Improved Baselines with Representation Autoencoders**

作者：Jaskirat Singh; Boyang Zheng; Zongze Wu; Richard Zhang; Eli Shechtman; Saining Xie。

Venue：NeurIPS 2026；状态：accepted_upcoming。

[官方记录](https://neurips.cc/virtual/2026/poster/149740) · [所读版本](https://arxiv.org/pdf/2605.18324)

版本：arXiv v2, 2026-06-15; author version, not camera-ready

观察定位：p3 Introduction；p4 Training efficiency。

可迁移动作：从旧取层默认到表示含义，再到新聚合操作；用平行分句比较同一表示的两种用途；为新的效率读数先解释它回答什么实践问题。



### X02

**RepFusion: Leveraging Multimodal Priors for Denoising in Representation Space**

作者：Xichen Pan; Aashu Singh; Satya Narayan Shukla; Xiangjun Fan; Shlok Kumar Mishra; Saining Xie。

Venue：NeurIPS 2026；状态：accepted_upcoming。

[官方记录](https://neurips.cc/virtual/2026/poster/153090) · [所读版本](https://arxiv.org/pdf/2606.14700)

版本：arXiv v1, 2026-06-12; author version lists 6 authors, while official venue lists 5. Both end with Saining Xie.

观察定位：p1 Introduction；p5 §3.2。定点句法补读：p1引言第一段末句→第二段首句的分工回指；p5 §3.2式2后动态依赖与不变约束。

可迁移动作：用具体名词回指两方分工，再解释前提如何变化；先概括条件输入差别，再落到token接口，长动态句后接短的不变约束。

作者版本差异：Read arXiv v1 p1 has six authors including Xiangjun Fan; NeurIPS official record lists five, omits Xiangjun Fan and orders Shukla before Singh. Saining Xie last in both. Official author-list difference retained, not silently reconciled.



### X03

**Cambrian-P: Pose-Grounded Video Understanding**

作者：Jihan Yang; Zifan Zhao; Xichen Pan; Shusheng Yang; Junyi Zhang; Hu Xu; Shang-Wen Li; Saining Xie。

Venue：ECCV 2026；状态：published。

[官方记录](https://link.springer.com/chapter/10.1007/978-3-032-37252-9_18) · [所读版本](https://arxiv.org/pdf/2605.22819)

版本：arXiv v2, 2026-07-23; author version has Bingyi Kang additional to publisher list. Both end with Saining Xie.

观察定位：p1摘要；p3 Introduction；p6 §3.1。定点句法补读：p1摘要前两句的判断→关系定义；p6 token→hidden state→projection→head的对象与接口链。

可迁移动作：短句提出关键判断，后一句用坐标关系解释其含义；简单接口与真实训练冲突分开，解决动作对应冲突。

作者版本差异：The listed authors follow the publisher metadata (eight authors); the read arXiv version includes Bingyi Kang as an additional author. Saining Xie is last in both.



### X04

**Beyond Language Modeling: An Exploration of Multimodal Pretraining**

作者：Shengbang Tong; David Fan; John Nguyen; Ellis L Brown Ii; Gaoyue Zhou; Shengyi Qian; Boyang Zheng; Théophane Vallaeys; Rob Fergus; Naila Murray; Marjan Ghazvininejad; Mike Lewis; Nicolas Ballas; Amir Bar; Michael Rabbat; Jakob Verbeek; Luke Zettlemoyer; Koustuv Sinha; Yann Lecun; Saining Xie。

Venue：ICML 2026；状态：published。

[官方记录](https://proceedings.mlr.press/v306/tong26c.html) · [所读版本](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tong26c/tong26c.pdf)

版本：PMLR 306 official PDF; authors differ from arXiv/current author homepages; use publisher version.

观察定位：p4 §4.3及数据来源段。

可迁移动作：已知兼容性引出是否主动受益的新问题；平行语法容纳非对称结果；互补性由不同来源的具体分工支持。



### X05

**Cambrian-S: Towards Spatial Supersensing in Video**

作者：Shusheng Yang; Jihan YANG; Pinzhi Huang; Ellis Brown; Zihao Yang; Yue Yu; Shengbang Tong; Zihan Zheng; Yifan Xu; Muhan Wang; Rob Fergus; Yann LeCun; Li Fei-Fei; Saining Xie。

Venue：ICLR 2026；状态：published。

[官方记录](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7e3dcf772fa2e8d9087b599c7c07d4cf-Abstract-Conference.html) · [所读版本](https://proceedings.iclr.cc/paper_files/paper/2026/file/7e3dcf772fa2e8d9087b599c7c07d4cf-Paper-Conference.pdf)

版本：ICLR official 41-page PDF; 14 authors, unlike 15-author 49-page arXiv version.

观察定位：p1 Introduction；p2 Second段。

可迁移动作：明确区分远景与当前初步贡献；先承认数据扩展有效，再用更严格任务的剩余困难引出下一阶段。



### X06

**Diffusion Transformers with Representation Autoencoders**

作者：Boyang Zheng; Nanye Ma; Shengbang Tong; Saining Xie。

Venue：ICLR 2026；状态：published。

[官方记录](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3c4141c12660ad3625eb4ae845e0a6f9-Abstract-Conference.html) · [所读版本](https://proceedings.iclr.cc/paper_files/paper/2026/file/3c4141c12660ad3625eb4ae845e0a6f9-Paper-Conference.pdf)

版本：ICLR official 30-page PDF.

观察定位：pp1–2 Introduction。

可迁移动作：用一个关系名词回收两个研究方向的隔离；条件从句贴近不能拟合这一谓语；可重建与可生成分开推进。



### X07

**What matters for Representation Alignment: Global Information or Spatial Structure?**

作者：Jaskirat Singh; Xingjian Leng; Zongze Wu; Liang Zheng; Richard Zhang; Eli Shechtman; Saining Xie。

Venue：ICLR 2026；状态：published。

[官方记录](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3929a7785bd56f57edcff0152ab41289-Abstract-Conference.html) · [所读版本](https://proceedings.iclr.cc/paper_files/paper/2026/file/3929a7785bd56f57edcff0152ab41289-Paper-Conference.pdf)

版本：ICLR official 39-page PDF.

观察定位：p1摘要；p2例子段。

可迁移动作：先定义共同对象，再问它的哪个属性有作用；反预期的数字配对引出系统检验，例子不取代全体证据。



### X08

**LiveCodeBench Pro: How Do Olympiad Medalists Judge LLMs in Competitive Programming?**

作者：Zihan Zheng; Zerui Cheng; Zeyu Shen; Shang Zhou; Kaiyuan Liu; Hansen He; Dongruixuan Li; Stanley Wei; Hangyi Hao; Jianzhu Yao; Peiyao Sheng; Zixuan Wang; Wenhao Chai; Aleksandra Korolova; Peter Henderson; Sanjeev Arora; Pramod Viswanath; Jingbo Shang; Saining Xie。

Venue：NeurIPS 2025 (Datasets and Benchmarks Track)；状态：published。

[官方记录](https://proceedings.neurips.cc/paper_files/paper/2025/hash/9712b78386cebdc3db7f1a48c2d20edb-Abstract-Datasets_and_Benchmarks_Track.html) · [所读版本](https://proceedings.neurips.cc/paper_files/paper/2025/file/9712b78386cebdc3db7f1a48c2d20edb-Paper-Datasets_and_Benchmarks_Track.pdf)

版本：NeurIPS official PDF; Datasets and Benchmarks Track explicitly distinguished.

观察定位：p1摘要；p2 Introduction。

可迁移动作：短问句分别打开不同诊断轴；标注动作产生metadata，再成为性能切片的输入；结果条件紧邻数值。



### X09

**Scaling Language-Free Visual Representation Learning**

作者：David Fan; Shengbang Tong; Jiachen Zhu; Koustuv Sinha; Zhuang Liu; Xinlei Chen; Michael Rabbat; Nicolas Ballas; Yann LeCun; Amir Bar; Saining Xie。

Venue：ICCV 2025；状态：published。

[官方记录](https://openaccess.thecvf.com/content/ICCV2025/html/Fan_Scaling_Language-Free_Visual_Representation_Learning_ICCV_2025_paper.html) · [所读版本](https://openaccess.thecvf.com/content/ICCV2025/papers/Fan_Scaling_Language-Free_Visual_Representation_Learning_ICCV_2025_paper.pdf)

版本：CVF official accepted main paper plus separate supplemental PDF.

观察定位：p1–2 Introduction与§2.1。

可迁移动作：将比较焦点从方法轴移到数据轴；平行描述两路数据安排，随后解释它控制的混杂。



### X10

**PISA Experiments: Exploring Physics Post-Training for Video Diffusion Models by Watching Stuff Drop**

作者：Chenyu Li; Oscar Michel; Xichen Pan; Sainan Liu; Mike Roberts; Saining Xie。

Venue：ICML 2025；状态：published。

[官方记录](https://proceedings.mlr.press/v267/li25bu.html) · [所读版本](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bu/li25bu.pdf)

版本：PMLR 267 official PDF with appendices.

观察定位：p1–2 Introduction；p3 §3.1假设及其分组用途；p7–8 §5.2双判准与对应测试。

可迁移动作：以受控研究的理由解释任务选择；真实和模拟数据用平行主语说明分工；单轨迹可行与分布正确是两种成功标准。



### X11

**Exploring the Deep Fusion of Large Language Models and Diffusion Transformers for Text-to-Image Synthesis**

作者：Bingda Tang; Boyang Zheng; Sayak Paul; Saining Xie。

Venue：CVPR 2025；状态：published。

[官方记录](https://openaccess.thecvf.com/content/CVPR2025/html/Tang_Exploring_the_Deep_Fusion_of_Large_Language_Models_and_Diffusion_CVPR_2025_paper.html) · [所读版本](https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_Exploring_the_Deep_Fusion_of_Large_Language_Models_and_Diffusion_CVPR_2025_paper.pdf)

版本：Official proceedings PDF; CVF accepted version with watermark

观察定位：p1摘要；pp2–3 §3.1；p3 Evaluation；p5 §6.1第二问题、四候选及表3后讨论。末句以让步从句交代代价，以主句选择动词和理由承载取舍。

可迁移动作：诚实标明经验研究的贡献类型；两种不变状态作为短代词的明确先行词，随后推出缓存用途；评估段提前说明指标权衡的读法。



### X12

**Scaling Inference Time Compute for Diffusion Models**

作者：Nanye Ma; Shangyuan Tong; Haolin Jia; Hexiang Hu; Yu-Chuan Su; Mingda Zhang; Xuan Yang; Yandong Li; Tommi Jaakkola; Xuhui Jia; Saining Xie。

Venue：CVPR 2025；状态：published。

[官方记录](https://openaccess.thecvf.com/content/CVPR2025/html/Ma_Scaling_Inference_Time_Compute_for_Diffusion_Models_CVPR_2025_paper.html) · [所读版本](https://openaccess.thecvf.com/content/CVPR2025/papers/Ma_Scaling_Inference_Time_Compute_for_Diffusion_Models_CVPR_2025_paper.pdf)

版本：Official proceedings PDF; CVF accepted version with watermark

观察定位：p3 §3。

可迁移动作：两个并列问题拆出验证器与搜索算法；重复输入→输出骨架来定义接口，使后续设计轴可定位。



### X13

**Science-T2I: Addressing Scientific Illusions in Image Synthesis**

作者：Jialuo Li; Wenhao Chai; Xingyu Fu; Haiyang Xu; Saining Xie。

Venue：CVPR 2025；状态：published。

[官方记录](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Science-T2I_Addressing_Scientific_Illusions_in_Image_Synthesis_CVPR_2025_paper.html) · [所读版本](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_Science-T2I_Addressing_Scientific_Illusions_in_Image_Synthesis_CVPR_2025_paper.pdf)

版本：Official proceedings PDF; CVF accepted version with watermark

观察定位：p1介绍段；p3 prompt定义。

可迁移动作：前一产物作为后一动作的工具，串成数据→评分→训练的依赖链；同一个例子固定其余信息以解释三个概念。



### X14

**Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces**

作者：Jihan Yang; Shusheng Yang; Anjali W. Gupta; Rilyn Han; Li Fei-Fei; Saining Xie。

Venue：CVPR 2025；状态：published。

[官方记录](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Thinking_in_Space_How_Multimodal_Large_Language_Models_See_Remember_CVPR_2025_paper.html) · [所读版本](https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_Thinking_in_Space_How_Multimodal_Large_Language_Models_See_Remember_CVPR_2025_paper.pdf)

版本：Official proceedings PDF; CVF accepted version with watermark

观察定位：p2 Introduction与§2。

可迁移动作：从日常例子接到明确空间属性；平行列出语言和视觉两种分析证据；由广义定义到当前输入，再收束研究范围。



### X15

**On Scaling Up 3D Gaussian Splatting Training**

作者：Hexu Zhao; Haoyang Weng; Daohan Lu; Ang Li; Jinyang Li; Aurojit Panda; Saining Xie。

Venue：ICLR 2025；状态：published。

[官方记录](https://proceedings.iclr.cc/paper_files/paper/2025/hash/57fabaa549352c52d5d312171b16970e-Abstract-Conference.html) · [所读版本](https://proceedings.iclr.cc/paper_files/paper/2025/file/57fabaa549352c52d5d312171b16970e-Paper-Conference.pdf)

版本：Official ICLR proceedings PDF

观察定位：p2关键观察与实现段。定点句法补读：按页内正文自然段计P4（观察）和P5（系统设计），二者以同一顺序连接并行方式、重排／通信、局部性与动态负载。

可迁移动作：并行方式引出数据重排代价，代价变成局部性设计的目标；首次术语用常用动作就地解释，下一阶段保留同样骨架。


## 五、流程设计参考

[writing-dna-skill](https://github.com/larashero3-dotcom/writing-dna-skill)提供了从完整语料和元数据提取分层规则、再回到写作任务使用的思路。本包采用论文专用八层入口、可追溯证据与按范围读取的方式；不用于冒充某位作者。实际查阅了其[SKILL.md](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/SKILL.md)及[英文流程](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/references/workflow.en.md)。

2026-10-12查阅的[LICENSE](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/LICENSE)为MIT。本包未复制其代码、模板或示例；指导文字与教学例句独立撰写。仓库许可不覆盖本语料论文的PDF或图像。本包不附这些材料。


v1.1增加独立的写作后定点清理阶段；v1.0自然表达指导与新阶段的差别见[参考流程映射](reference-integration.md)。
