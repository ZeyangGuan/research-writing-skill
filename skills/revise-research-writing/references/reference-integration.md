# 参考流程与适配选择

本页用于追溯设计来源，不是日常润色的必读规则。所有新指导和英文示例独立撰写；没有安装或执行下列仓库代码，也没有照搬其模板。

## writing-dna：已有结构与后处理

[writing-dna-skill](https://github.com/larashero3-dotcom/writing-dna-skill)将语料、元数据、分层分析、归纳产物与写作使用相连。实读[根SKILL](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/SKILL.md)、[英文流程](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/references/workflow.en.md)及[成稿清理子skill](https://github.com/larashero3-dotcom/writing-dna-skill/blob/main/skills/lieflat-less-ai-tone/SKILL.md)。

对应到本包：manifest保存30篇来源与阅读覆盖；八层入口连接句子、章节、故事与图面工具；sources页保留逐篇→组内→跨组关系。没有采用固定重读全部产物和五篇原文的要求，也没有将词频、个人世界观或风格相似分数当成已完成研究。

- **v1.0**已有自然句法、信息衔接、好句保留，但没有独立成稿清理阶段，不能称为其附属模块已完整集成。
- **v1.1**新增[定点语言清理](final-language-pass.md)，按触发条件处理重复功能、空转提示、冗余反转、同义修饰和遮住动作的句法。该子skill原面向中文；本包为英文论文独立适配，不照搬中文频率或标点阈值。
- **v1.2**将正向句法重组为九张按困难调用的卡，并压缩后处理的重复说明。真实对照、学术编号、必要列举、连续We、被动与可读长句均按功能保留。不判断AI作者身份，不承诺降低检测分数。

## 社区仓库：具体采用了什么

以下为2026-10-12查阅的具体文件。项目的受欢迎程度不证明写法正确；运行规则按适用条件和证据取舍。

| 实读来源 | 采用的机制 | 本包落点 |
|---|---|---|
| [Anthropic skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | 同一真实请求的新旧独立对照；关注近邻误触发；删掉无产出的流程 | 版本对照与范围设计；SKILL描述区分论文编辑与实验设计/语料再研究 |
| [OpenAI skill-creator](https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md) | 短入口、清楚读取条件、按需加载 | 困难→1–3卡；来源页和manifest只按需检索 |
| [blader/humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md) | 现象→动作→例子→保留情况；弱信号不自动触发 | S1–S9与F1–F5；一次可用修订，不默认输出多轮草稿 |
| [K-Dense scientific-writing](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-writing/SKILL.md)及其[evidence workflow](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-writing/references/evidence_workflow.md) | 精确来源位置；区分证据存在与支持具体命题；保留条件 | 卡片源语境＋页节；涉及技术含义的位置才核对，不要求普通润色启动全套CSV/签核 |
| [Orchestra writing guide](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/main/20-ml-paper-writing/ml-paper-writing/references/writing-guide.md) | 主谓接近、旧→新信息、具体动词、可选句尾焦点 | S1/S2/S6及句尾焦点小工具；与30篇已有观察分别注明 |

取舍：不采用固定五句摘要、固定贡献条数、永远主动语态、禁用combine/extend等词、统一破折号禁令、随笔式情绪添加或整套投稿审计。科研语料中的必要条件、角色差异和自然节奏优先于外部模板。

## 许可与证据边界

writing-dna、blader/humanizer、K-Dense和Orchestra所读仓库许可为MIT；Anthropic与OpenAI所读skill-creator目录许可为Apache-2.0。许可核验针对实际文件，不能推定同仓库所有内容相同。

这里只独立归纳组织思想与通用写作方法，没有复制其代码、原示例或大段文案。将来若直接复制或实质改编受许可材料，应保留对应版权与许可声明。上述许可不覆盖30篇研究论文的PDF或图像；本包只保留书目信息、观察与原创示例。

<a id="nature"></a>
## v1.3：Nature官方信息功能与社区写作工具

官方校准来自[How to construct a Nature summary paragraph](https://www.nature.com/documents/nature-summary-paragraph.pdf)，文件标注September 2019，例文发表于2005。采用的是读者进入问题、认识中心结果、理解结果增加了什么认识的信息功能；未把该文档称为新发表指南，也未将其句数/篇幅示意套用到CVPR。

另实读三个社区项目的四个skill及对应参考。它们没有核实的Nature官方身份：

- [Yuan1z0825 nature-writing](https://github.com/Yuan1z0825/nature-skills/blob/e605b35611ab2849af46d0cf7831aefdcf85be07/skills/nature-writing/SKILL.md)及[paragraph-flow](https://github.com/Yuan1z0825/nature-skills/blob/e605b35611ab2849af46d0cf7831aefdcf85be07/skills/nature-writing/references/paragraph-flow.md)：中心发现→必要支持→具体意义；每段逐步收束问题。用于Abstract、Introduction、L5与S2。
- 同库[nature-polishing](https://github.com/Yuan1z0825/nature-skills/blob/e605b35611ab2849af46d0cf7831aefdcf85be07/skills/nature-polishing/SKILL.md)：区分句法困难和段落功能困难。没有采用其英文片段的10–30词句长限制；也不因诊断到结构问题就越过句级授权。
- [SyntaxSmith nature-writing](https://github.com/SyntaxSmith/nature-writing-skill/blob/c1a8716047b6304d922b9528a18421203e3e7acc/SKILL.md)：设计直接回答刚提出的具体困难；引言末段可以报告发现，也可以收束关键设计。没有采用固定摘要/引言句段数、数字密度或必须删移实验的清单。
- [Boom write-scientific-manuscript](https://github.com/Boom5426/Nature-Paper-Skills/blob/3bf56ea1ef17edd74a9a582893bb851dd2b85f1c/skills/core/write-scientific-manuscript/SKILL.md)：主题、必要铺垫、证据、解释和连接是可选的段落功能；不是每段五件套。用于L5与Analysis。

v1.3只替换或细化已有条目，没有扩成Nature投稿流程。CVPR的目标读者、贡献形式、实际模板和用户冻结范围优先；好用的贡献列表、短主题句与完整长条件句都可保留。社区作者自述的论文数量、模式频率和NMI阅读集未独立逐篇复核，不计入本包30篇语料。

许可核验：Yuan根LICENSE为Apache-2.0；SyntaxSmith README声明结构/框架为MIT，根目录未见独立LICENSE；Boom所读原创模块按其LICENSE和ATTRIBUTION为MIT，但仓库其他组件许可不一。这里只独立归纳写作思想并使用自创例子，不分发社区原文、其论文引文或代码。以上固定版本链接用于定位实际参考文件；许可声明不扩展到其引用的第三方材料。
