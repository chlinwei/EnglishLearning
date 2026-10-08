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
