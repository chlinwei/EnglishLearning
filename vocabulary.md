# IT 英语单词本

> 定位：只收 **IT 相关英语**——技术术语、开发/运维/产品工作场景用语、开源与技术社区表达、技术面试英语。
> 记录格式：单词 / 音标 / 词性 / 释义 / **IT 语境** / 例句（IT 场景）/ 搭配 / 易混

---

## 分类索引

| 分类 | 说明 |
| --- | --- |
| 通用职场 | 团队协作、会议、沟通、流程 |
| 编程/开发 | 语言、范式、代码、数据结构 |
| 系统/运维 | 部署、网络、故障、监控 |
| 开源/社区 | 贡献流程、许可证、社区规范 |
| 技术面试 | 面试高频表达 |

---

## 1. code of conduct

- **音标**：/koʊd əv ˈkɑːndʌkt/
- **词性**：名词短语（noun phrase）
- **释义**：行为准则；行为规范
- **分类**：开源/社区 · 通用职场

**IT 语境**
开源社区里几乎每个项目都有一份 `CODE_OF_CONDUCT.md`（常见基于 Contributor Covenant 模板），规定贡献者该如何互相尊重地交流。公司内部的工程团队、技术大会也会有自己的 code of conduct。违反它可能导致 PR 被拒、被移出社区，甚至封号。

**例句（IT 场景）**
1. Most open-source projects include a **CODE_OF_CONDUCT.md** to keep contributors respectful.
   （多数开源项目都带一份行为准则，保证贡献者之间彼此尊重。）
2. Violating the project's **code of conduct** can get your pull request rejected.
   （违反项目的行为准则，可能导致你的 PR 被拒。）
3. We added a **code of conduct** to our repo after a heated issue thread.
   （在一个吵得很凶的 issue 讨论之后，我们给仓库加了行为准则。）

**搭配**
- `adhere to / follow the code of conduct` — 遵守行为准则
- `enforce the code of conduct` — 执行行为准则
- `violate the code of conduct` — 违反行为准则
- 缩写 **CoC**，在 issue、PR 讨论里常见

**易混点**
- `code of conduct`（行为准则）≠ `code of ethics`（职业道德规范，偏伦理层面）
- **conduct** 的重音随词性变化：
  - 名词「行为」重音在**前** → **ˈkɑːn**-dʌkt
  - 动词「进行/实施」重音在**后** → kən-**ˈdʌkt**
  - 规律同 record / present / object。IT 场景里 `conduct a test`、`conduct a code review` 都是动词用法
- `code` 本身一词多义：代码 / 密码 / 编码 / 法规。在 IT 文本里大多指「代码」，但 `code of conduct`、`building code` 里是「规范、法典」

---

## 2. velocity

- **音标**：/vəˈlɑːsəti/（美）· /vəˈlɒsəti/（英）
- **词性**：名词（noun）
- **释义**：速度；速率
- **分类**：编程/开发（敏捷开发）

**IT 语境**
敏捷开发（Scrum、XP）里的核心度量指标：一个团队在**一个 Sprint（迭代）内实际完成**的「故事点」总量。它的用途是**预测**——让团队知道下个迭代大概能承接多少工作量。它**不是**「开发快慢」，也不是用来考核绩效的。

**中文译法对比**

| 译法 | 评价 |
| --- | --- |
| **速率** | ✅ **行业主流**。国内 Scrum 圈通用译法，正式文档首选 |
| 速度 | ⚠️ 直译，**误导性强**。会让人以为是「开发快慢」，而 velocity 本质是「每迭代完成多少」 |
| 迭代速率 / 团队速率 | ✅ 语义更明确，适合文档中首次出现时使用 |
| 交付速率 | ✅ 强调「产出」，准确但不如「速率」常见 |
| 产能 | ❌ 不建议。这是 **capacity（容量）** 的译法，两者概念不同，会混淆 |
| 不译，直接用 velocity | ✅ **团队口头交流最常见**，尤其中英夹杂的工作环境 |

> **结论**：正式文档写「**速率（velocity）**」，首次出现标注英文；团队日常口头直接说 velocity。
> 不要用「速度」——这是最常见的错译。

**例句（IT 场景）**
1. Our team's **velocity** is about 40 story points per sprint.
   （我们团队的速率大约是每个迭代 40 个故事点。）
2. Don't compare **velocity** across teams — it's for forecasting, not performance review.
   （不要拿不同团队的速率来对比——它是用来做预测的，不是绩效评估。）
3. Our **velocity** dropped after two members went on leave.
   （两名成员休假之后，我们的速率下降了。）

**易混点（三个词别搞混）**
- **velocity（速率）**：过去**实际完成**了多少 → 用来**预测**
- **capacity（容量/产能）**：下个迭代**理论上能承接**多少（要扣掉休假、会议、支持时间）→ 用来决定**承诺**多少
- **speed（速度）**：日常语言里的「快慢」，敏捷语境下没有这个指标
- 一句话记忆：**capacity 决定你承诺多少，velocity 帮你猜你实际能做完多少。**

---

## 3. staging environment

- **音标**：/ˈsteɪdʒɪŋ ɪnˈvaɪrənmənt/
- **词性**：名词（noun）
- **释义**：预发布环境；过渡环境（口语常简称 **staging**）
- **分类**：系统/运维

**IT 语境**
位于「测试」和「生产」之间的一整套环境，配置尽量跟线上保持一致，用途是在真实用户流量到来之前做**最后一轮整体验证**。典型环境链：

`local（本地）→ dev（开发）→ test / QA（测试）→ staging（预发布）→ prod / production（生产）`

同义说法：**pre-prod**、**pre-production**、**UAT**（用户验收测试环境）。

**例句（IT 场景）**
1. We deploy to **staging** first to make sure nothing breaks.
2. The bug only shows up in **staging**, not in production.
3. **Staging** should mirror production as closely as possible.

**易混点**
- **test** 环境偏「功能对不对」；**staging** 偏「整套系统像线上一样跑起来对不对」
- **production**（简称 **prod**）才是真实用户使用的正式环境
- 常见环境变量名：`ENV=staging`、`staging.example.com`

---

## 4. canary deployment

- **音标**：/kəˈneri dɪˈplɔɪmənt/
- **词性**：名词（noun）
- **释义**：金丝雀发布；灰度发布（也说 **canary release**）
- **分类**：系统/运维

**IT 语境**
先把新版本只放给**一小部分流量**（比如 1%~10%），盯着监控指标看有没有异常，正常再逐步扩大比例，最后全量。名字来自煤矿工人带进矿洞的**金丝雀**——用它先探路，一旦有毒气它会先倒下。软件里同理：真出问题，只影响那一小撮用户，可以**快速回滚**。

**常见部署策略对比**

| 策略 | 做法 | 特点 |
| --- | --- | --- |
| **canary**（金丝雀/灰度） | 按流量比例逐步放量 | 出问题影响面小，可快速回滚 |
| **blue-green**（蓝绿） | 两套完整环境，一键切流量 | 切换快，但资源成本翻倍 |
| **rolling update**（滚动更新） | 逐台替换实例 | 默认方式，无需额外资源，但回滚较慢 |

**例句（IT 场景）**
1. We rolled out a **canary deployment** to 5% of users first.
2. If the error rate looks fine, we'll promote the **canary** to 100%.

**相关词**：`roll out` 部署/上线 · `roll back` 回滚 · `promote` 提升为全量 · `traffic split` 流量切分

---

## 5. spike

- **音标**：/spaɪk/
- **词性**：名词 / 动词
- **释义**：（指标的）尖峰、突增；动词：突然飙升
- **分类**：系统/运维

**IT 语境**
监控图表上指标突然冲高、又很快回落的那一段。搭配固定用 `a spike in + 指标`：`a spike in CPU usage`、`a traffic spike`、`a latency spike`。

**例句（IT 场景）**
1. We're seeing **spikes in CPU usage** on staging.
2. CPU **spiked** to 100% right after the deploy.

**易混点（三个「涨」不一样）**
- **spike**：短时间尖峰，随后迅速回落 —— 图上是个「尖角」
- **surge**：快速上涨，且可能维持一段时间 —— 强调「汹涌」
- **peak**：最高点（名词），只描述「顶点」位置，不强调过程

**相关表达**：`spiky traffic` 波动剧烈的流量 · `traffic peak` 流量高峰

---

## 6. observability

- **音标**：/əbˌzɜːrvəˈbɪləti/（美）· /əbˌzɜːvəˈbɪləti/（英）
- **词性**：名词（noun）· 形容词形式 **observable** /əbˈzɜːrvəbl/
- **释义**：可观测性
- **分类**：系统/运维

**怎么读（重点）**

| 音节 | 1 | 2 | 3 | **4** | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| 拼写 | ob | ser | va | **bil** | i | ty |
| 读音 | əb | ˌzɜːr | və | **ˈbɪl** | ə | ti |
| 谐音 | 呃b | 泽（卷舌，次重音） | və | **比尔（主重音）** | 呃 | 提 |

- **主重音在第 4 个音节 `-BIL-`**，不是在第 2 个
- ❌ 常见错读：ob-**SER**-va-bility（重音提前）
- 口诀：**ob-ser-va-BIL-i-ty**，读到「比尔」时最用力

> 🔑 **一条规律搞定一族词**：以 `-ability` 结尾的词，主重音**永远固定在 `-BIL-`** 上。
> `ability` · `capability` · `scalability` · `reliability` · `availability` · `observability` —— 全都一样。
> 这几个词在技术文档里出现频率极高，记住规律能一次性读对一串。

**IT 语境**
比 monitoring（监控）更进一步的能力。monitoring 是「预设好指标、看有没有超阈值」；observability 是「系统内部状态能被充分推断出来」，靠三大支柱：**logs（日志）、metrics（指标）、traces（链路追踪）**——合称 **the three pillars of observability**。典型工具：Prometheus、Grafana、Datadog、Jaeger。

**例句（IT 场景）**
1. Good **observability** is what lets us debug production without guessing.
   （良好的可观测性让我们不用靠猜就能排查线上问题。）
2. We invest in **observability** so that incidents get caught earlier.
3. The **three pillars of observability** are logs, metrics, and traces.

**易混点**
- **observability**（可观测性，系统的一种**能力**）≠ **monitoring**（监控，一种**手段/实践**）
- 形容词 `observable` 重音在 **-SER-**（/əbˈzɜːrvəbl/），和名词的重音位置**不一样**，注意区分

---

## 7. parking lot

- **音标**：/ˈpɑːrkɪŋ lɑːt/（美）· /ˈpɑːkɪŋ lɒt/（英）
- **词性**：名词（noun）；口语里也直接当动词：**park it / park that**
- **释义**：（会议用语）议题「停车场」——把跑题但确有价值的话题先搁置、留待后续处理
- **分类**：通用职场

**IT 语境**
站会（standup）、迭代评审、回顾会（retro）里的标配工具。主持人用它把**跑题但确实有价值**的话题从当前议程里分流出去：**不是否决，而是暂存**。作用是既不打断发言、也不得罪人，同时保住会议的时间盒（time box）——站会通常只有 15 分钟，一旦有人开始讨论方案，节奏立刻崩掉。白板上画一栏、或 Confluence 页面开一个列表，就是「停车场」。

**例句（IT 场景）**
1. That's a good point, but let's **park** it — I'll add it to the **parking lot**.
   （这点很好，但先搁一搁——我记进停车场。）
2. Can we keep standup to 15 minutes? Anything off-topic goes to the **parking lot**.
   （站会能控制在 15 分钟内吗？跑题的都进停车场。）
3. We followed up on the **parking lot items** right after the retrospective.
   （回顾会一结束我们就跟进了停车场里的条目。）
4. Let's put the database migration discussion in the **parking lot** and circle back with the DBA.
   （数据库迁移的讨论先搁进停车场，回头和 DBA 再聊。）
5. Let's **park** the caching discussion — drop it in the **parking lot** and we'll follow up after the retro.
   （缓存这块的讨论先放一放——记进停车场，回顾会之后再跟进。）
   > ⭐ 真实工作场景高频句（2026-10-09 练习句）。一句话里塞了 park / parking lot / follow up / retro 四个高频词，值得整句背下来。
   > 注意 `caching`（缓存，/kæʃ/）不是 `catching`（抓，/kætʃ/）。

**搭配**
- `put sth in / add sth to the parking lot` — 把……记进停车场
- `park that / park it` — 先搁一边（动词用法，口语高频）
- `parking lot item(s)` — 停车场里的待办条目
- `follow up on the parking lot` — 会后跟进停车场里的议题

**易混点**
- **parking lot vs take it offline**：parking lot 是「**有清单、会末或会后再处理**」；take it offline 只是「**现在别在会上聊**」，相关人私下解决，不一定留下记录。日常口语常混用，但正式会议纪要里要分清
- **别和 bike shed 混**：**bike shed**（自行车棚）指「无关紧要却被反复争论的细节」，跟「暂存」是两码事
- 词源就是字面的停车场：车不能一直开着，**先停进去——不是报废，是暂存**。这个「暂存而非丢弃」的语感是关键
- 中文对应说法：「停车场」「待议清单」「搁置区」；也有团队直接说英文 parking lot

---

## 8. surge

- **音标**：/sɜːrdʒ/（美）· /sɜːdʒ/（英）
- **词性**：名词 / 动词
- **释义**：激增；涌升；蜂拥而至（动词：急剧上涨）
- **分类**：系统/运维

**IT 语境**
指标**快速上涨、且往往维持一段时间**，不像 spike 那样来了就走。典型搭配：`a surge in traffic`、`a surge in demand`、`a surge in signups`。在负载均衡和自动扩缩容（autoscaling）场景里是高频词——突发的 surge 正是触发扩容的信号。

**例句（IT 场景）**
1. We saw a **surge in traffic** right after the post hit the front page.
   （那条帖子上了首页之后，流量激增。）
2. The **surge** in memory usage lasted all afternoon and finally triggered autoscaling.
   （内存占用整个下午一路涨，最后触发了自动扩缩容。）
3. Requests **surged** as soon as the marketing email went out.
   （营销邮件一发出去，请求量就暴涨。）

**易混点（和序号 5 的 spike 一起记）**
- **spike**：短促的**尖峰**，上得快、落得也快 —— 图上是个「尖角」
- **surge**：快速上涨、**可能维持一段时间** —— 图上是一段「陡坡」
- **peak**：最高点（名词），只标位置，不描述过程
- 记忆：spike 是**打一针就完**，surge 是**浪涌**。`a spike in CPU` 多出现在排障对话里，`a surge in traffic` 多出现在容量规划里

**相关表达**
- `traffic surge` 流量激增 · `demand surge` 需求暴增
- `surge pricing` 动态调价（打车、云资源等场景）
- 发音提示：结尾 `-rge` 只发一个音 /rdʒ/（像「之」），别拆成「尔-格」

---

## 9. retrospective

- **音标**：/ˌretrəˈspektɪv/ · 口语缩写 **retro** /ˈretroʊ/
- **词性**：名词 / 形容词
- **释义**：回顾会；复盘（名词）· 回顾的、追溯的（形容词）
- **分类**：编程/开发（敏捷开发）· 通用职场

**IT 语境**
敏捷开发里的**固定会议**：**Sprint Retrospective（迭代回顾会）**。每个迭代结束时团队内部开一次，复盘「这轮哪里做得好、哪里必须改」，产出是**改进项（action items）**——**它不是追责会，只谈流程怎么改**。

Scrum 的五个正式会议：Sprint Planning（计划会）· Daily Scrum / Standup（每日站会）· Sprint Review（评审会）· **Sprint Retrospective（回顾会）** · Backlog Refinement（待办梳理）。

> 🔥 **口语里一律简称 `retro`**——这才是真正的最高频形式，比全称常见得多：
> `Let's do a quick retro.` · `in the retro we agreed to...` · `retro action items`
> 还能动词化：`we retro'd on that`（我们复盘过了）。

**三个「复盘」别搞混**

| 说法 | 谁参加 | 目的 |
| --- | --- | --- |
| **Sprint Review** | 团队 + 产品/外部相关方 | 展示这轮**做出来的东西** |
| **Retrospective**（retro） | **仅团队内部** | 复盘**流程**，只谈怎么改进 |
| **postmortem** | 事故相关人 | 线上**故障复盘**，专查根因 |

**例句（IT 场景）**
1. Let's park the caching discussion — drop it in the parking lot and we'll follow up after the **retro**.
   （缓存这块的讨论先放一放——记进停车场，回顾会之后再跟进。）← ⭐ 2026-10-09 实际练习句，整句值得背
2. Our **retro** action items keep piling up and nobody owns them.
   （回顾会的改进项一直在堆积，没人认领。）
3. We **retro'd** on the incident and agreed to add more alerts.
   （我们对这次故障做了复盘，决定多加些告警。）
4. Add it to the **retro** board so we don't lose it.
   （记到回顾会看板上，别漏了。）

**搭配**
- `hold / run a retro` — 开回顾会
- `retro action items` — 回顾会产出的改进项（会议唯一的实质产出）
- `add it to the retro` — 留到回顾会上说（会上不方便聊时的标准托词）
- 正式书面：`Sprint Retrospective` / `retrospective meeting`

**易混点 / 发音**
- 重音在 **-SPEC-**：retro-**SPEC**-tive，别读成 **RE**-tro-spec-tive
- 但缩写 `retro` 的重音**在第一个音节**：**RE**-tro /ˈretroʊ/ —— 全称和缩写重音位置**不一样**，这是最容易读错的地方
- 词根拆解：`retro-`（向后）+ `-spect-`（看）= **向后看** → 回顾。同族词：inspect（向内看=检查）、respect、perspective
- ⚠️ 单独出现的 `retro` 还常表示「**复古/怀旧**」（retro style、retro UI）——那个 retro 是另一个来源，跟回顾会无关。看上下文判断
- 形容词义在技术写作里也常见：`a retrospective look at the migration`（对这次迁移的回顾）

---

## 10. of（方位 / 关系用法）：upstream of us

- **音标**：弱读 /əv/ · 强读 /ʌv/
- **词性**：介词（preposition）
- **释义**：（这类短语里）**以……为参照原点**、位于……的相对位置 —— ⚠️ **不是「的」**
- **分类**：系统/运维 · 通用职场

**IT 语境**

排障会议里判断**责任边界**的核心结构。`upstream` / `downstream` 是**相对词**，单独出现没有方向；必须配一个 `of + 参照物` 才知道是往哪边数：

```
upstream of us   = 从我们这一环往上游数 = 在我们前面那一环（CDN / LB / 网关 / 入口网络）
downstream of us = 从我们这一环往下游数 = 我们后面那一环（我们调用的 DB 或外部 API）
```

**中文和英文在这里走了两条路**：中文习惯说「这是**我们的**上游」（用「的」），英文这里的 `of` 是**坐标原点**，跟所有权无关。

**同一个 `of`，你早就认识（一次解决一整族）**

| 短语 | 望文生义（错） | 真实含义 |
| --- | --- | --- |
| **in front of us** | 我们的前面 ❌ | 在我们前面 |
| **north of us** | 我们的北 ❌ | 在我们北边 |
| **to the left of us** | 我们的左 ❌ | 在我们左边 |
| **upstream of us** | 我们的上游 ❌ | 在我们上游 |
| **two hops upstream of us** | —— | 在我们上两跳 |

没人会把 `in front of us` 理解成所有格 —— `upstream of us` 就是同一件事，只是把「前 / 后」换成了「上游 / 下游」。

**例句（IT 场景）**
1. **So it's upstream of us, then.**
   （那就是上游的问题。/ 那这么说，问题在我们前面那一环。）← ⭐ 素材 0007「排除应用侧：502 全来自一个可用区」，Dan 随后去拉 LB 指标，印证 upstream 指入口那侧
   > `So ..., then.` 里的 `then` 不是「然后」，是**「那么 / 这么说」**——排除法做完、下结论的语气。
2. It's two hops **upstream of us** — the gateway, not the DB.
   （在我们上游两跳——是网关那层，不是数据库。）
3. Nothing here is ours. It's all **upstream of the gateway**.
   （这儿没一处是我们的问题，全在网关上游。）
4. Just to be sure — is that **upstream of us** or **downstream of us**?
   （确认一下——那是在我们上游还是下游？）

**搭配**
- `upstream / downstream of + 参照物` — 参照物可以换：`of us` · `of the LB` · `of the gateway` · `of the ingress` · `of the DB`
  → **换掉那个词，责任边界就钉死了**
- `N hops upstream of us` — 在我们上游第 N 跳
- `on the way in` — 入口那侧（**同义，但不依赖 upstream 的方向歧义**，听不清时更保险）

**易混点（⚠️ 最重要的一条）**

- **想说「不归我们管」，必须说 `upstream of us`，别用 `our upstream`。**
  `our upstream` 在运维语境里指 **`nginx.conf` / Envoy / Istio 里那个 `upstream` 块**，即**我们调用的后端**——方向正好反过来。
- `upstream` / `downstream` 是业界公认的**「同一个词两套相反方向」**：
  - **请求流视角**（排障对话、事故会用）→ upstream = 把请求交给我们的那一方（CDN / LB / 网关）
  - **依赖 / 数据流视角**（nginx、Envoy、Istio 配置文件用）→ upstream = 我们调用的后端（DB、外部 API）
  - 经验值：排障时听到 `it's upstream of us`，**十次里九次是「不是我们的锅」**，因为说话人正在做责任切割。

**听不清时怎么办（发音 + 救急）**
- `of` 在句中**几乎总是弱读 /əv/**，还常和后面的词连成一团：`of us` ≈ «ə-vəs»，`of the` 里的 `the` 也几乎消失。**这是 `of us` 听起来「没发音」的真正原因**——它不是被吞掉，是弱读+连读。
- 听不清就别抓功能词，**抓重音**：`till ___ know more` 这个框架里能填的只有 we / you / they；结合「宣布冻结变更」的语境只能是 `we`。**功能词靠语法补，不靠耳朵抓。**
- 听到就反问确认：`Upstream of us — so the LB side?` · `Do you mean the gateway, not us?` · `On our side or theirs?`
