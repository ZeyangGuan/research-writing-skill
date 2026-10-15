# 句子与衔接：按困难选卡

通常只选最相关的1–3张卡。默认L6–L8，保持原有命题与推进顺序；拆合句子服从用户的句数要求。每个Before/After均为自创等义教学例，Keep展示已经写好的情况。来源支持列出的写法，不是教学例中的研究事实。

- [S1 主体与动作](#s1)
- [S2 对象接力](#s2)
- [S3 关系名词回指](#s3)
- [S4 平行对照](#s4)
- [S5 阶段与限定](#s5)
- [S6 前置堆叠](#s6)
- [S7 完整条件](#s7)
- [S8 局部让步](#s8)
- [S9 信息单位与节奏](#s9)

<a id="s1"></a>
## S1 主体与动作

[观察维度：D1/D2](dimension-map.md)；日常使用不必打开映射。

**何时用**：读者要穿过“进行某项操作的实施”才找到动作；或为避免被动而把熟悉的模块藏进长宾语。

**怎么写**：圈出动作名词和现有施动者，将动作名词恢复为有限动词。 主语优先承接本段追踪对象；若本段关注被冻结的模块，保留该模块作被动句主语。 时间与输入条件仍限定原动作，不能把“随后被传入”写成“由这个模块传入”。

Before: The encoder performs the normalization of each input vector before the vector enters the prediction head.

After: The encoder normalizes each input vector before it enters the prediction head.

**改在哪里**：performs the normalization压为normalizes；重复vector换成唯一清楚的it。改善发生在谓语，不靠换一个高级动词。正式自然的表达依赖准确动作：use、measure、compare等常用学术词可以很直接；术语有技术区别时保留原名，不为简短改成含混口语。

**等义核对**：encoder仍归一化每个input vector，时点仍在进入prediction head之前；未补谁传递向量。

**Keep**: The encoder is frozen during adaptation.

句子正在交代encoder的状态，读者不需要知道谁执行冻结。改成We freeze并不必然有收益。

**源语境**（物理页；详情按ID追溯）：
- [H01](sources-and-patterns.md#h01) p4 §3.1末句：编码器只在训练中出现；此句解释它不会给推理增加模块。可学模块作被动主语，阶段紧贴使用动作。[所读版](https://arxiv.org/pdf/2605.10938)。
- [X12](sources-and-patterns.md#x12) p3 §3，verifiers/algorithms定义：两类函数分别接收不同输入、输出分数或候选噪声；重复骨架比名词堆叠更清楚。可学用输入—输出动词直接定义对象的工作。[所读版](https://openaccess.thecvf.com/content/CVPR2025/papers/Ma_Scaling_Inference_Time_Compute_for_Diffusion_Models_CVPR_2025_paper.pdf)。

<a id="s2"></a>
## S2 对象接力

[观察维度：D3/D4](dimension-map.md)；日常使用不必打开映射。

**何时用**：第二句退回pipeline/approach等泛称，读者必须自己找出它用的是前句哪个产物。

**怎么写**：先判断后句是在接输入、补条件、给证据还是解释。对于输入—输出关系，标记前句产物，在后句用this/these加稳定术语接住它。论证关系不必写成数据流：解释句可以回指已有difference或finding，对照句可以沿同一比较轴展开。连接词只表达已存在的关系。

**先让对象可用**：给新对象命名时，可用短同位语或关系从句把已有的角色、构成或用途一并交清，再让后句消费它。需要调整句序时，遵循本次编辑范围。定义本来清楚可得时，直接使用对象。

跨节时，同一对象还可能从“上一步产物”变成“下一步条件”；把旧名与新角色在一句中绑定。嵌套汇总时，让每次汇总的产物成为下一次的输入。需要具体示例时，再读[跨节短桥与统计接力](object-handoff-examples.md)。

Before: The encoder produces a confidence map. For the selector, this map is the input used to choose pixels.

After: The encoder produces a confidence map. The selector uses this map to choose pixels.

**改在哪里**：后句把原来的for the selector和the input used to改成selector uses；对象链不变，句法负担减少。

**等义核对**：encoder产出map，selector用同一map选pixels；没有新增阈值或后续操作。

对象链以外的等义承接例：

Before: The perturbed-calibration setting has a higher average error. These results suggest that calibration quality may affect prediction accuracy.

After: The perturbed-calibration setting has a higher average error. This difference suggests that calibration quality may affect prediction accuracy.

只把已有测量差别命名为difference；suggests/may不变。此处接的是证据与解释，写法参考[社区段落指导](reference-integration.md#nature)，不是新增算法依赖。

**Keep**: We measure accuracy. We also measure latency.

这两项是并列测量，没有前一产物成为后一输入；不必强改成对象链或因果。

**源语境**（物理页；详情按ID追溯）：
- [X08](sources-and-patterns.md#x08) p2 数据构建段：专家标注任务技能和认知类型；随后产物被用于模型表现切片。可学标注动作产出metadata，metadata支持后续分析。[所读版](https://proceedings.neurips.cc/paper_files/paper/2025/file/9712b78386cebdc3db7f1a48c2d20edb-Paper-Datasets_and_Benchmarks_Track.pdf)。
- [X03](sources-and-patterns.md#x03) p1摘要前两句、p6 §3.1 token→hidden state→projection→head接口：新对象先与角色绑定，再被后续动作使用；定义后的小关系从句可以就地交代用途。[所读版](https://arxiv.org/pdf/2605.22819v2)。
- [H11](sources-and-patterns.md#h11) p6 §4.5 Training：递归模块向下传递输出，直至像素层；this process回收整个传递动作。可学上一层输出成为下一层输入，同层级词保持稳定。[所读版](https://arxiv.org/pdf/2502.17437)。

<a id="s3"></a>
## S3 关系名词回指

[观察维度：D3/D4](dimension-map.md)；日常使用不必打开映射。

**何时用**：后句需要谈前句建立的“分工/对照/安排”，却把全部模块再说一遍；或者只写this而有多个合理先行对象。

**怎么写**：判定回指对象是一个实体、一个动作，还是两个对象之间的关系。 用恰好覆盖关系的名词，例如division、comparison、arrangement；不能把comparison改称cause。 读者有唯一先行词时保留it/these，不把所有代词都扩长。

Before: The extractor computes features, and the scorer ranks the candidates. This assignment of feature computation and candidate ranking to separate modules is shared by all variants.

After: The extractor computes features, and the scorer ranks the candidates. This division of labor is shared by all variants.

**改在哪里**：后句仍从整组分工出发，却无需重播两个动作。关系名词承担信息压缩，名词化在这里有用。

**等义核对**：两个模块分别计算特征、排序候选，所有variant共享该分工；未增加分工的效率收益。

**Keep**: The decoder receives a feature map. It predicts a score from that map.

it只有decoder这一合理先行词；扩成the proposed decoding architecture只会加重。

公式附近的“平均值”“分母”“该项”也需要唯一指代。例如先对每组有效测量取均值、再对各组取平均时，应说明缺失测量影响哪一层。原材料未交代时，标记内容待确认，不自行选择计算规则。

不要把有歧义的this直接换成猜测的原因；先标出歧义，仍可润色其他部分。

**源语境**（物理页；详情按ID追溯）：
- [X02](sources-and-patterns.md#x02) p1 Introduction第2–3段：论文先交代LLM文本编码和DiT去噪，再解释这一分工在VAE表示条件下为何合理。可学division回收编码与去噪的两方分工。[所读版](https://arxiv.org/pdf/2606.14700)。
- [X06](sources-and-patterns.md#x06) pp1–2 Introduction连接处：生成模型与表示学习分别介绍后，以同一关系名词进入其假设背景。可学separation回收两个研究方向的关系。[所读版](https://proceedings.iclr.cc/paper_files/paper/2026/file/3c4141c12660ad3625eb4ae845e0a6f9-Paper-Conference.pdf)。
- 保留例 [X11](sources-and-patterns.md#x11) pp2–3 §3.1末：text key/value状态已明确；these回指这些状态的不变性，并接缓存用途。可学唯一先行对象允许简短代词。[所读版](https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_Exploring_the_Deep_Fusion_of_Large_Language_Models_and_Diffusion_CVPR_2025_paper.pdf)。

<a id="s4"></a>
## S4 平行对照

[观察维度：D1/D3/D5](dimension-map.md)；日常使用不必打开映射。

**何时用**：两路方法或数据各自说得通，却用不同语法包装，读者难比较哪个对象承担哪个作用。

**怎么写**：找两路共享的比较轴，例如存储内容、数据用途或函数输入输出。 保留相同的主语—动词—宾语槽位，让真正差异出现在对应槽位。 语法可对称，收益不可强行对称；一边提升、一边不变就照实保留。

Before: The vector stores a single summary of the image, whereas for the grid, a feature is retained at each spatial location.

After: The vector stores a single summary of the image, whereas the grid retains a feature at each spatial location.

**改在哪里**：两边都让表示对象作主语、存储动词作谓语；读者只需更新被保存的内容。

**等义核对**：vector保存单一全图摘要，grid在每个空间位置保留特征；角色与粒度不变。

**Keep**: Text improves visual accuracy, whereas adding images leaves text accuracy unchanged.

对称句法已清楚承载非对称结果；不能为了对仗改成两种模态互相提升。

**源语境**（物理页；详情按ID追溯）：
- [H04](sources-and-patterns.md#h04) p1 Abstract中段：输出目标位于图像流形，损失定义在速度空间；while是角色对照，不是执行先后。可学相似分句分别承载预测空间和损失空间。[所读版](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lu26t/lu26t.pdf)。
- [X10](sources-and-patterns.md#x10) p2 Fig1图注及资源段：真实视频支持物理准确性评估，模拟视频支持后训练；同形式保持不同分工。可学两种视频作平行主语，各自接用途。[所读版](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bu/li25bu.pdf)。
- [X12](sources-and-patterns.md#x12) p3 §3，定义项目：验证器与搜索算法的输入和输出不同，重复句法维护对应关系。可学相同输入输出骨架定义不同接口。[所读版](https://openaccess.thecvf.com/content/CVPR2025/papers/Ma_Scaling_Inference_Time_Compute_for_Diffusion_Models_CVPR_2025_paper.pdf)。

<a id="s5"></a>
## S5 阶段与限定

[观察维度：D1/D4](dimension-map.md)；日常使用不必打开映射。

**何时用**：一句同时包含训练、适应、推理以及多组参数，读者需要回读才能知道何时更新谁。

**怎么写**：以During/After等时间框架限定本句。 让同一参数名称跨阶段稳定重复；更新与冻结分别有宾语或受事。 让only就近限定实际可更新对象，jointly继续约束原来的两个对象。

多设置并列时，将预算、初始化或日程限制放在实际适用的设置旁边；不要把局部配方扩成全局条件。

Before: Joint optimization of the backbone and the codes is performed during training. For each new sequence after training, optimization is restricted to its code, with the backbone kept fixed.

After: During training, the backbone and the codes are optimized jointly. After training, only the code for each new sequence is optimized; the backbone remains fixed.

**改在哪里**：两个前置框架降低阶段检索成本；第二句把更新对象与不变对象并排，重复backbone有导航价值。

**等义核对**：训练中联合优化backbone与codes；训练后每个新序列只优化其code，backbone固定。

**Keep**: We freeze the encoder and train only the head.

谁冻结、谁更新、only作用域已明确，保留。无需把主动句强改成两句被动。

**源语境**（物理页；详情按ID追溯）：
- [H09](sources-and-patterns.md#h09) p5 §3.5末三句：训练时共同优化权重和码本；新轨迹时固定网络，只优化潜码。可学真实训练与新轨迹阶段的参数状态平行。[所读版](https://arxiv.org/pdf/2503.07596)。
- [H03](sources-and-patterns.md#h03) p6 Fig3：预训练、离线训练和测试时训练中初始化、微调、冻结状态不同；名称重复避免混淆。可学重复模块名承载跨阶段状态变化。[所读版](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/11149.pdf)。

<a id="s6"></a>
## S6 前置堆叠

[观察维度：D1/D5](dimension-map.md)；日常使用不必打开映射。

**何时用**：读者走过两项长前提才看到主句；作者想保留完整设计依据，而不是只留一个响亮结论。

**怎么写**：把前置部分分成原文已有的观察单位，不新增或删去其中一项。 保留观察的认识状态，例如observe、appear、certain；不能全改成普适事实。 原文明示“依据这些观察”时，用based on these observations回收；若原文只有having的先后，不自行补therefore。

Before: On the basis of our observations that the representation preserves object boundaries and that the same boundaries remain visible after compression, we use the compressed representation as input to the decoder.

After: We observe that the representation preserves object boundaries and that the same boundaries remain visible after compression. Based on these observations, we use the compressed representation as input to the decoder.

**改在哪里**：第一句让长前提拥有自己的主谓；第二句主动作及时出现。信息增量为零，读取路径更短。

**等义核对**：两项观察、它们作为设计依据的地位、compressed representation作为decoder输入均保留。

**Keep**: Given a valid mask, the module returns one score per region.

前置条件短而必要，主谓没有被淹没；拆成三句没有收益。

句数必须不变时，可把依据移到主句后：We use the compressed representation as input to the decoder, based on our observations that the representation preserves object boundaries and that the same boundaries remain visible after compression. 若信息顺序也已冻结，则保留原顺序。

**源语境**（物理页；详情按ID追溯）：
- [H13](sources-and-patterns.md#h13) p4 §3.3首句：两项经验前提涉及token位置属性和扰动后的有效图像；可拆出两项发现，但不能删certain/appear等范围。可学两项前置发现共同支持编辑提议，主句出现较晚。[所读版](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beyer25a/beyer25a.pdf)。
- 对照机制 [X03](sources-and-patterns.md#x03) p1 Abstract前两句：极短中心判断之后，position/orientation定义共享坐标系及其跨帧关系；短句不替代必要解释。可学短中心句后用较长定义提供具体关系。[所读版](https://arxiv.org/pdf/2605.22819)。

<a id="s7"></a>
## S7 完整条件

[观察维度：D1/D4/D5](dimension-map.md)；日常使用不必打开映射。

**何时用**：机械拆短把主过程、末步例外或假设后果隔开，读者容易把局部性质理解成无条件性质。

**怎么写**：确认后句确实限定前句的时点、范围或条件。 用原义的until/when/if等从句把边界留在动作附近。 保留必要条件的方向与虚拟语气；only if、if、unless不能互换。

Before: The decoder updates continuous states up to the last step. At that final step, the output head converts the states into labels.

After: The decoder updates continuous states up to the last step, when the output head converts the states into labels.

**改在哪里**：when把时间边界直接接在last step后；一个句子承载同一过程的主体与例外，比无目的拆短更紧密。

**等义核对**：连续状态更新持续到末步，只有该时点写明由output head转换成labels；未增加共享参数等条件。

**Keep**: If the residual were zero, the estimate would satisfy the constraint.

if/were/would把假设状态与条件后果绑定。缩为The estimate satisfies the constraint会改变命题。

条件很多且主谓仍不易找到时，转S6；不是“有条件就必须写长句”。

**源语境**（物理页；详情按ID追溯）：
- [H01](sources-and-patterns.md#h01) p1 Abstract第6句附近：模型主要在连续空间运行，到最后一步才映射离散词元；时点是方法描述的一部分。可学主过程与最终词元转换同句保存。[所读版](https://arxiv.org/pdf/2605.10938)。
- [H10](sources-and-patterns.md#h10) p5 Training with Average Velocity，stop-gradient后：段落承认优化处理后，条件句说明零损失时满足恒等式；它不是已达到零损失的报告。可学if/were/would保存零损失下的条件联系。[所读版](https://papers.nips.cc/paper_files/paper/2025/file/6d13e085b79d454da5910e4ca82a3d9d-Paper-Conference.pdf)。
- [X06](sources-and-patterns.md#x06) p2 设计难点第1项：DiT拟合难点与宽度/token维度关系相连；删掉unless会扩大结论。可学unless将不能拟合的断言限定在宽度条件内。[所读版](https://proceedings.iclr.cc/paper_files/paper/2026/file/3c4141c12660ad3625eb4ae845e0a6f9-Paper-Conference.pdf)。

<a id="s8"></a>
## S8 局部让步

[观察维度：D1/D4](dimension-map.md)；日常使用不必打开映射。

**何时用**：句子要说“有效但不够”，却把两半写成笼统正负评价；或在压缩时只剩失败结论。

**怎么写**：先确定本句要交付的是收益、限制，还是已有的选择。把当前答案放在主句，已知取舍放在让步从句：讨论限制时，主句命名限制；解释选择时，主句说清选谁及原文给出的理由。需要两面同等权重时保留but并列，不为句式变化另造代价或偏好。

Before: A reduction in repeated reads is obtained with the shared cache, but no reduction in the cost of a first request is obtained.

After: Although the shared cache reduces repeated reads, it does not reduce the cost of a first request.

**改在哪里**：两个被动名词化改成同一主体的具体动作；在已知段落要讨论首次请求限制的前提下，主句给出该限制。

**等义核对**：减少的是重复读取，未降低的是首个请求的代价；两半都保留。does not reduce不自动等于unchanged：未降低也可能包含升高，不能擅自改成数值相等。

**Keep**: The cache reduces repeated reads, but it does not reduce the cost of a first request.

若两面需要同等权重，这句已直接清楚；不要只为出现although而改它。

解释选择的原创等义例（允许合句）：

Before: The tiled solver uses more memory than the streaming solver. We use the tiled solver because it avoids repeated disk access.

After: Although the tiled solver uses more memory than the streaming solver, we use it because it avoids repeated disk access.

**改在哪里**：内存代价成为让步，主句落在已有的选择，because保留原文的采用理由。若两句已清楚服务各自任务，保留原句；合句本身不是收益。

真实让步不是“无效反转”或禁词。能否删让步，要看它是否保留结论有效范围。

**源语境**（物理页；详情按ID追溯）：
- [H13](sources-and-patterns.md#h13) p4 §4开头：原有编辑可控制部分属性，但复杂属性和灵活性有限；让步没有否定全部编辑能力。可学承认粗粒度编辑能力后指出局部限制。[所读版](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beyer25a/beyer25a.pdf)。
- [X07](sources-and-patterns.md#x07) p2 Higher validation accuracy段：分类准确率更低与生成表现更好同时成立；让步用于校准默认预期，不意味着数学矛盾。可学对照同一目标编码器的两个评价维度。[所读版](https://proceedings.iclr.cc/paper_files/paper/2026/file/3929a7785bd56f57edcff0152ab41289-Paper-Conference.pdf)。
- [X11](sources-and-patterns.md#x11) p5 §6.1第二问题、表3后讨论末句：让步从句保留对齐代价，主句以选择动词及参数效率／结构简洁理由收束。可学把采用决定与经验结果分清，并让句法重心落在当前决定上。[所读版](https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_Exploring_the_Deep_Fusion_of_Large_Language_Models_and_Diffusion_CVPR_2025_paper.pdf)。
- [H15](sources-and-patterns.md#h15) p7 §4.3 Predict clean data：保留一个性能下降步骤是因为拆解目标；迁移句法时不能把该研究目的当成本稿目的。可学承认精度下降，同时保留不同研究目标。[所读版](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b52c29d1a77e3fcc6c8f90fa0ac0e8e-Paper-Conference.pdf)。

<a id="s9"></a>
## S9 信息单位与节奏

[观察维度：D3/D4/D5](dimension-map.md)；日常使用不必打开映射。

**何时用**：相邻短句虽各有信息，却把一项定义、过程或对照切碎；或句子负担相近、重音单调，使读者难辨主要动作、条件与落点。不变约束埋在过程里也是一种情形。

**怎么写**：先确定本句要交付的一项完整关系，再决定哪些事实共同承载它。用并列谓语对齐同一对象的不同动作，用关系从句就近交代新对象的用途，或将状态放到它限定的对象旁；主句仍须容易找到。已有的因果、时序和让步才用相应连接词。短句适合单独突出一个判断或约束，也可让条件留在同一句中；取决于当前重点，而非长短交替公式。合句后读相邻句：前句建立了什么，后句从哪里继续？

Before: At each step, the state changes. The score is recomputed because the state changes. The scorer uses the same weights at every step.

After: At each step, the state changes, so the score is recomputed. The scorer uses the same weights at every step.

**改在哪里**：第一句是一条动态关系；第二句在此需要单独突出稳定约束。这是当前信息分工的一种选择，不是每个状态都应独立成短句。

**等义核对**：状态变化导致score重算，scorer各步用相同weights；未把同权重改成训练期间冻结。

**Keep**: We update the state at every step while keeping the transition matrix fixed.

一句已经把变化与不变量清楚分工，拆句并不会自动更好。

不同动作也可组成一个信息单位：We train the head on labeled regions and evaluate it on held-out regions. 两个谓语和各自的数据条件都在，句界不必为每个动作单独保留。反过来，若两项各需展开不同证据，独立成句更便于推进。

**源语境**（物理页；详情按ID追溯）：
- [X02](sources-and-patterns.md#x02) p5 §3.2式2后：采样中噪声表示随步骤变化，conditioning随之重算；随后单独说明LLM保持causal。可学较长动态过程后接极短不变条件。[所读版](https://arxiv.org/pdf/2606.14700)。
- 保留例 [H12](sources-and-patterns.md#h12) p1 Abstract全段：连续We句承担理论解释、设计与期望，但句内仍用并列谓语把分析与经验检验相连，用关系从句及结果分词结构交代新模型的表现与意义。可学相同主语承载不同信息工作，同时把属于同一关系的事实组织在一句中；不是每个动作各占一句。[所读版](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25g/sun25g.pdf)。

## 可选微调：把本句重点留在句尾

当句意已清楚，只是读者容易记住次要条件时，调整条件位置即可。句尾不必永远放结果，取决于本段正在回答什么。

Before: Latency is reduced by 12% at a fixed memory budget.

After: At a fixed memory budget, latency is reduced by 12%.

已有预算条件和12%降幅都保留。若本段重在强调预算公平，原句把budget留在句尾更合适，直接Keep。这是[Orchestra写作指南](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/main/20-ml-paper-writing/ml-paper-writing/references/writing-guide.md)提供的可选焦点工具，经独立原创示例适配；未当作源论文的频率结论。

完成正向改写后，再做[定点语言清理](final-language-pass.md)。不要为轮换句型而破坏清楚的平行关系，也不要用更短或改得更多来判断优劣。
