# 听懂英语新闻：专项设计与首批辅助文本

## 2026-10-12 纠正：以真实媒体内容为课程来源

用户要求听懂CNN等主流媒体报道。此前50场景500段模板问答不满足这个目标，已撤下首页，仅保留为历史辅助草稿。下文关于该批次的数量与设计记录不表示它是合格新闻课程。

当前上线的是CNN01一个样例、10段文本理解练习。来源为[CNN This Morning 2025-02-10官方文字稿](https://transcripts.cnn.com/show/ctmo/date/2025-02-10/segment/01)，重点参考广播时钟05:10至05:20附近的政治报道。这些时钟标记不是YouTube播放时间码。只核对了文字稿，未听录音；CNN说明该快速文字稿可能修订。

源数据在 `sources/news-lessons.json`，通过 `tools/build_news_texts.py` 生成 `data/news.js`。发布流程不再把旧模板草稿写入浏览器数据。正文采用连续新闻叙述，不再使用一问一答；当前10段每段8句英文，配整段中文翻译。正文为原创新闻概述，不冒充CNN主播或嘉宾原话；少量重点词组明确注明是否出自文字稿，不复制完整报道。

下一步先定位对应官方音视频，确认实际语速、发音和时间段，再完成听力练习。当前没有核实YouTube链接，因此不编造链接或时间码，不声称完成真实听力验收。其他地区暂不以模板凑数，逐条选取主流媒体来源再扩充。

专项：public-affairs。编写与来源查阅日期：2026-10-12。
状态：文本试稿；无音频、无虚构时长、未接入正式播放索引。

## 50场景文本批次

按用户最新要求固定为每场景10段对话。第一轮批次保存在 [完整阅读文本](public-affairs-scenes.md) 和 [结构化草稿](public-affairs-scenes.json)，共50场景、500段、2000轮双语问答，每段4轮。美国15场、日本10场、韩国10场、欧洲15场。

这批使用PA01–PA50独立编号；下方早期样例改为EX编号，避免与正式批次混淆。批次是围绕2025年背景的主题训练，不是50条不同事件的新闻报道。部分提问框架复用，尚待逐段语言与去重复评审、记者解释长段扩写及真实视频绑定。生成器为 `tools/build_news_texts.py`，修改主题数据后可重建；不生成音频，不改变IT正式源数据。

## 学习目标

面向 YouTube 上主流英语媒体的新闻视频，训练抓住事件主旨、跟上记者解释、区分事实与消息来源、理解采访观点。首批话题仍为美国特朗普、日本、韩国、欧洲，时间范围为 2025 年以来。

成功标准不是背完对话，而是面对一段未练过的相关报道，能说明谁做了什么、何时发生、主要影响，以及哪些内容属于官方说法、推测或评价。文本和原创配音只能辅助，最终必须使用真实视频验证听力迁移；目前没有真实视频听力验收结果。

## 新闻听力单元结构

| 环节 | 文本设计 | 理解任务 |
|---|---|---|
| 事件卡 | 事件日期、背景、人物、机构、可核对来源 | 区分报道日期与事件日期 |
| 主播简讯 | 原创简化版与接近真实报道密度版；保留归因与不确定性 | 首遍抓事件和主旨，不要求逐词听懂 |
| 记者解释 | 背景、因果、对比、实施条件；不是简单加长聊天 | 抓为什么、影响谁、还有什么不确定 |
| 采访问答 | 自然追问、澄清、异议；观点由虚构角色承担 | 分清记者提问、受访者主张与已知事实 |
| 新闻语言 | 高频句式、数字、人名、机构名、词组切分 | 识别来源、转折、时间和语气强度 |
| 真实视频练习 | 核实官方频道、标题、发布日期、URL 和片段起止位置后填写 | 听后复述，并回答事实/声明/预测问题 |

BBC、Reuters、AP、CNN 等媒体可作为候选来源，不预设某一家代表所有新闻表达。先选单一事件短报道，再进阶到解释视频和长访谈。不同媒体的事实报道、分析和评论需要分别标注。

真实视频链接、字幕与时间段须实际核实，不编造。当前首批只有事件文件来源，尚未绑定具体 YouTube 视频。优先原创训练文本和视频链接；不复制整篇媒体报道或完整字幕。

## 优先训练的新闻语言

| 表达 | 含义 | 听力上要区分什么 |
|---|---|---|
| according to / officials say | 据某来源 / 官员表示 | 有来源归属，不代表独立核实 |
| is expected to / is likely to | 预计 / 很可能 | 预测，不是已发生 |
| has yet to | 尚未 | 未完成，不等于永远不会发生 |
| is set to | 预计或安排将要 | 表示计划或预期，不是完成证明 |
| comes amid | 发生在某种背景之下 | 背景相关不自动等于因果 |
| raises questions about | 引发对某事的疑问 | 引出争议或分析，不是证明失败 |
| marks a shift in | 标志着某方面的转变 | 要听清相对什么发生转变 |
| while / despite / however | 而 / 尽管 / 然而 | 注意后半句如何限定前半句 |

新闻文本允许较长的信息句、被动语态和名词短语，不沿用 IT 对话的平均短句硬指标。通过分层文本降低难度，不为了口语化删除关键限定词。练习词组边界和重音提示时不写成伪音标；连读、弱读和口音需要以后用真实音频训练。

## 编写规则

- 时间范围从 2025-01-01 起，首批选择有日期可核对的 2025 年事件，不冒充最新新闻。
- 以下角色均为虚构的普通读者，不是政客，也不代表各国民众的统一观点。
- 全部对话为原创学习材料，不是采访、新闻逐字稿或政治人物原话。
- 事件背景、官方声明、角色评价分开。官方文件能够证明某方说了什么，不自动证明其主张或预期已经实现。
- 使用常见缩写、短句、追问和自然异议，不套用 IT 专项的印度句法或口音配额。
- 加粗为优先记忆表达。地区名称不是需要反复背诵的句型；政治术语另列。
- 每场景按最新要求固定10段，逐步扩充上述新闻单元结构。下方EX01–EX04聊天保留为讨论与复述辅助，不代表主播报道或完整新闻听力单元。
- 不编造民调、政策成效或民众反应。不把欧盟等同于整个欧洲。关税税率和实施状态随时间变化，首批不写未经逐项核实的具体税率。

## 主题路线

| 编号 | 地区 | 首批主题 | 可继续发展的主题（须另查来源） |
|---|---|---|---|
| EX01 | 美国 / Trump | 第二任期开始：承诺与落实 | 关税与物价、行政命令与法院、移民政策的程序与成本 |
| EX02 | 日本 | 美日会谈：声明与实际变化 | 日本国内政策争论、生活成本、能源合作与供应链 |
| EX03 | 韩国 | 美韩会谈：投资承诺与就业 | 国内选举与治理、对外贸易、安全与预算取舍 |
| EX04 | 欧洲 / 欧盟 | 欧美贸易安排：妥协与确定性 | 成员国差异、英国与欧盟的区别、能源与公共预算 |

角色 Alex 和 Maya 在不同日期讨论新闻，四段不是同一天连续发生的对话。

## EX01 新闻式文本示范

状态：原创示范，基于下方 2025-01-20 就职演说来源；不是 BBC、CNN 或其他媒体的报道，也不是对视频的转写。时间视角固定为 2025-01-21。

### 主播简讯：简化版

Donald Trump began his second term as U.S. president on Monday. In his inaugural address, he outlined plans on trade and border policy. He also promised to bring down prices. Those are stated goals, not evidence that prices have already fallen.

特朗普周一开始了美国总统第二任期。他在就职演说中阐述了贸易和边境政策方面的计划，也承诺降低物价。这些是公开提出的目标，不是物价已经下降的证据。

### 主播简讯：较高信息密度版

Donald Trump began his second term on Monday, outlining a policy agenda that includes changes to trade and border enforcement. In his inaugural address, he pledged to bring down prices, but the speech itself does not establish how those proposals will be implemented or what their economic effects will be.

特朗普周一开始第二任期，阐述了包括贸易和边境执法调整在内的政策议程。他在就职演说中承诺降低物价，但演说本身不能说明这些提议最终将如何落实，也不能证明它们会产生何种经济影响。

词组切分：began his second term / outlining a policy agenda / pledged to bring down prices / how those proposals will be implemented。
重点：**outlined** 是阐述，不是落实；**pledged to** 是承诺，不是成效；**will be implemented** 是将如何实施，不是已经实施。

### 理解检查

1. 已发生的事件是什么？答案：特朗普开始第二任期并发表就职演说。
2. 降低物价属于已经验证的结果，还是演说中的承诺？答案：承诺。
3. 是否能从这段报道得出物价已经下降？答案：不能。
4. 下一步核查什么？答案：实际政策文件、实施安排，以及能够用于评估影响的数据。

此示范只有主播文本和理解题；记者解释、采访和真实视频绑定尚待补齐，不标为完整单元。

## EX01 · 美国：特朗普回到白宫，接下来关注什么

讨论设定日期：2025-01-21。场合：朋友看完就职相关新闻。
事实锚点：特朗普于 2025-01-20 开始第二任期；当日就职演说谈及贸易、边境与降低成本等政策目标。此处不宣称这些目标已经兑现。
来源：[白宫就职演说，2025-01-20](https://www.whitehouse.gov/remarks/2025/01/the-inaugural-address/)。这是当事方的一手讲话记录，演说中的评价不是独立事实核查结果。

1. **Alex:** Did you catch Trump's speech yesterday?
   你看了特朗普昨天的演说吗？
2. **Maya:** Yeah, parts of it. What **stood out to you**?
   看了，一部分。你觉得哪一点最引人注意？
3. **Alex:** The promises on prices and trade. I wonder **how that'll work in practice**.
   关于物价和贸易的承诺。我想知道实际会怎么落实。
4. **Maya:** Same here. A speech tells us what he wants, not what he'll get done.
   我也一样。演说说明他想做什么，不说明他最终能做成什么。
5. **Alex:** **To be fair**, people want to know what the plan is.
   公平地说，大家也希望知道计划是什么。
6. **Maya:** Sure. I just want to **see the details** before judging it.
   当然。我只是想先看细节，再作判断。
7. **Alex:** Which details would you look for?
   你会关注哪些细节？
8. **Maya:** What changes, when it starts, and who it affects.
   改什么、什么时候开始，以及影响谁。
9. **Alex:** And whether a promise needs Congress to act?
   还有某项承诺是否需要国会采取行动？
10. **Maya:** Exactly. **Let's not get ahead of ourselves**.
    没错。先别急着下结论。
11. **Alex:** Fair enough. Let's check the actual policy, not just the headline.
    有道理。我们看具体政策，别只看标题。
12. **Maya:** Right. Then we can talk about the costs and benefits.
    对。之后再讨论成本和收益。

重点：stand out to someone（让某人印象深刻）；in practice（实际操作中）；to be fair（公平地说）；see the details（看具体细节）；get ahead of ourselves（在条件不足时过早下结论或推进）。
术语：second term（第二任期）；Congress（美国国会）；policy（政策）。
复述任务：用三句英语说明“演说中的目标”与“已落实政策”的区别。

## EX02 · 日本：美日会谈之后，不只看合影

讨论设定日期：2025-02-08。场合：朋友讨论美日联合声明。
事实锚点：特朗普与当时的日本首相石破茂于 2025-02-07 在华盛顿会谈；联合声明涉及安全合作、投资、技术和能源，包括增加美国液化天然气对日出口的意向。
来源：[美日领导人联合声明，2025-02-07](https://www.whitehouse.gov/briefings-statements/2025/02/united-states-japan-joint-leaders-statement/)。这是双方公布的立场与意向，不是项目完成证明。

1. **Maya:** Did you read the statement after Trump met Ishiba?
   你看了特朗普和石破茂会谈后的声明吗？
2. **Alex:** I skimmed it. **What's the main takeaway**?
   我快速看了一下。主要值得记住的是什么？
3. **Maya:** They talked about security, investment, and energy cooperation.
   他们谈了安全、投资和能源合作。
4. **Alex:** So, more than just a photo opportunity.
   所以不只是合影亮相。
5. **Maya:** Yes, but **that doesn't necessarily mean** things change overnight.
   对，但这不一定意味着事情一夜之间就会改变。
6. **Alex:** Right. Did they announce completed projects or future plans?
   对。他们宣布的是已完成的项目，还是未来计划？
7. **Maya:** The energy section talks about increasing U.S. gas exports to Japan.
   能源部分谈的是增加美国对日本的天然气出口。
8. **Alex:** **What's the catch**? Would that depend on contracts and prices?
   有什么需要留意的条件？这会取决于合同和价格吗？
9. **Maya:** That's what I'd check. The statement alone doesn't tell us the final cost.
   我会查这个。仅凭声明还看不出最终成本。
10. **Alex:** I can see the appeal, though. More suppliers could give buyers options.
    不过我理解它的吸引力。供应商更多，买方可能就有更多选择。
11. **Maya:** **I see your point**. I'd still want to compare the terms.
    我明白你的意思。不过我还是想比较具体条件。
12. **Alex:** Agreed. Let's **keep an eye on** what actually gets signed.
    同意。我们继续关注最终真正签下了什么。

重点：what's the main takeaway（主要结论是什么）；that doesn't necessarily mean（那不一定意味着）；what's the catch（有什么隐含条件或问题）；I see your point（我理解你的看法）；keep an eye on（持续关注）。
使用提醒：what's the catch 带有“是否有不利条件”的怀疑，不适合用来中性询问所有细节。
术语：joint statement（联合声明）；LNG / liquefied natural gas（液化天然气）；alliance（同盟）。
复述任务：先说会谈涉及什么，再用一句话提醒“意向不等于完成”。

## EX03 · 韩国：投资数字很大，但怎么落实

讨论设定日期：2025-11-14。场合：朋友阅读美韩会谈的联合情况说明。
事实锚点：2025-11-13 发布的联合情况说明记载，特朗普于 2025-10-29 在庆州与韩国总统李在明会晤；文件涉及贸易投资、造船和同盟合作。
来源：[美韩联合情况说明，2025-11-13](https://www.whitehouse.gov/fact-sheets/2025/11/joint-fact-sheet-on-president-donald-j-trumps-meeting-with-president-lee-jae-myung/)。讨论基于公布的承诺，不宣称投资已经到位或就业效果已经出现。

1. **Alex:** Have you seen the new U.S.-Korea fact sheet?
   你看了新的美韩情况说明吗？
2. **Maya:** Yes. It's about Trump's meeting with Lee in Gyeongju.
   看了。讲的是特朗普和李在明在庆州的会谈。
3. **Alex:** The investment figures **caught my eye**.
   那些投资数字引起了我的注意。
4. **Maya:** Mine too. But I'd ask how the money will be put to work.
   我也是。不过我会问这些资金将怎么使用。
5. **Alex:** Are you saying the deal isn't worth much?
   你的意思是这个安排价值不大？
6. **Maya:** No, **that's not what I mean**. A commitment isn't the same as money already spent.
   不是，我不是这个意思。作出承诺和钱已经花出去不是一回事。
7. **Alex:** Fair point. The document also talks about shipbuilding.
   有道理。文件还谈到了造船。
8. **Maya:** Right. **The question is** what happens next: training, contracts, or new facilities?
   对。问题是接下来会发生什么：培训、合同，还是新设施？
9. **Alex:** I hope it creates jobs. But **it's too early to tell** how many.
   我希望它能创造就业。不过现在还看不出会有多少岗位。
10. **Maya:** Exactly. We'd need a timetable and actual project updates.
    没错。我们需要时间表和实际项目进展。
11. **Alex:** So we shouldn't treat every announced investment as a finished project.
    所以不能把每项宣布的投资都当成已完成的项目。
12. **Maya:** Right. Let's **see how it plays out**.
    对。看看它后续如何发展。

重点：catch someone's eye（引起注意）；that's not what I mean（我不是这个意思）；the question is（问题在于）；it's too early to tell（现在还无法判断）；see how it plays out（看看事情如何发展）。
术语：investment commitment（投资承诺）；shipbuilding（造船）；implementation（落实）。
复述任务：解释为什么投资承诺、资金投入和就业结果不能当作同一件事。

## EX04 · 欧洲：欧美贸易安排，是妥协还是坏交易

讨论设定日期：2025-07-28。场合：朋友讨论前一天宣布的欧美贸易安排。
事实锚点：欧盟委员会资料确认欧美于 2025 年 7 月达成贸易安排，页面列有 2025-07-27 的相关声明。对话只使用这一历史事件，不将动态页面上的 2026 年实施进展带回 2025 年。
来源：[欧盟委员会欧美贸易专题页](https://commission.europa.eu/topics/trade/eu-us-trade-deal_en)；[2025-07-27 声明入口](https://ec.europa.eu/commission/presscorner/detail/en/statement_25_1915)。专题页可读；声明正文此次抓取未返回，因此具体条款和税率不据此逐项断言。

1. **Maya:** Did you see the news about the EU-U.S. trade deal?
   你看到欧美贸易安排的新闻了吗？
2. **Alex:** Yes. **What's your take on it**?
   看到了。你怎么看？
3. **Maya:** I can see why businesses might want more certainty.
   我理解为什么企业可能希望有更大的确定性。
4. **Alex:** Sure, but a predictable cost can still be a high cost.
   是，不过可预期的成本仍然可能很高。
5. **Maya:** **That's a fair point**. Predictable doesn't mean cheap.
   这个观点有道理。可预期不等于便宜。
6. **Alex:** So, was it a good compromise?
   所以这是个不错的妥协吗？
7. **Maya:** **It depends on** the terms and the alternatives.
   这取决于具体条件，以及当时还有哪些选择。
8. **Alex:** You mean we should compare it with what might have happened without a deal?
   你是说，还应该比较如果没有达成安排，可能会发生什么？
9. **Maya:** Yes, but that's a scenario, not a fact we can directly observe.
   对，不过那是假设情景，不是我们能够直接观察到的事实。
10. **Alex:** And **we can't lump everyone together**. Different industries face different costs.
    而且不能把大家都混为一谈。不同行业面临不同成本。
11. **Maya:** Exactly. Also, the EU isn't the whole of Europe.
    没错。还有，欧盟不等于整个欧洲。
12. **Alex:** Let's **look at the bigger picture**, then check the details.
    那就先看整体情况，再核对细节。

重点：what's your take on it（你怎么看）；that's a fair point（有道理）；it depends on（取决于）；lump everyone together（把所有人或群体一概而论）；look at the bigger picture（看全局）。
术语：European Union / EU（欧盟）；tariff（关税）；compromise（妥协）；trade-off（取舍）。
复述任务：分别用一句话说出支持和担忧，再说明还有哪些事实需要核实。

## 下一步文本扩充

先评审四段的难度、口语风格与主题密度，再扩充。后续需覆盖真正的日本、韩国和欧洲国内议题，而非全部围绕美国外交。选举和政策新闻逐篇核实后再写，不从标题推断制度细节。
前端接入时使用独立 PA 编号与 public-affairs 专项，不占用 IT 的 S 编号或四位素材编号；需要单独支持无音频文本数据，不能伪造媒体字段来通过现有构建校验。