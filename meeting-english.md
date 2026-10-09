# IT 会议英语场景手册

> 这不是单词本（单词本在 `vocabulary.md`）。这里是**场景手册**：哪类会议该说什么、听不懂时怎么救、以及配套的本地练习素材。
>
> 起点很具体：**听懂并参与和印度同事 / IT 团队的英文会议。**

---

## 0. 怎么用这份手册

别通读。每次开会前 3 分钟，翻到对应的会议类型看一遍句型；开完会 10 分钟内回来填「会后回流清单」。

一条原则先记住：

> **听不懂不是你的问题，硬猜才是。** 发现自己在硬猜，立刻跳到第 3 级救急。

---

## 1. 六类会议：每种要练的语言功能完全不同

「会议英语」不是一个东西。站会、计划会、回顾会、评审会、故障会、全员会，你要发的言根本不是一回事。

| 会议 | 频率 / 时长 | 你的角色 | 要练的语言功能 | 一句样板 |
|---|---|---|---|---|
| **Standup** 站会 | 每天 · 15 min | 必发言 | 极简报进度：做完 / 在做 / 被卡 | I finished the login fix. Today I'm on the payment webhook. I'm blocked on staging DB credentials. |
| **Sprint Planning** 计划会 | 每迭代 | 发言 | 估工作量 + 表态接不接 | I'd estimate this at three points. / That's a stretch for this sprint. |
| **Retrospective** 回顾会 | 每迭代 | 发言 | 提改进，且**不指名** | It would help if we… / One thing that worked well was… |
| **Design / Code Review** 评审会 | 不定期 | 提问、礼貌反对 | 质疑方案但不得罪人 | I see the trade-off, but have we considered…? / Let me play devil's advocate. |
| **Incident Call** 故障会 | 突发 · 高压 | 简报 | 现状 + 时间 + 下一步 | Investigating elevated 5xx on checkout. Next update in 15 minutes. |
| **All-Hands / 1:1** 全员会 / 一对一 | 月度 / 每周 | 基本只听 | 纯听力：抓决策和 action items | — |

**优先级**：站会是你唯一必须**每天开口**的会，先把它练到自动化。

---

## 2. 站会：三段式模板（背下来，20 秒说完）

站会的固定三问是：`What did you do yesterday? What will you do today? Any blockers?`
回答永远按这三段走，**不要讲故事**，一句一件事。

### 模板

```
1) 昨天：  Yesterday I finished / wrapped up / shipped <X>.
2) 今天：  Today I'm working on / starting <Y>.
3) 阻塞：  No blockers.  ← 或者 →  I'm blocked on <Z>. I need <某人/某物>.
```

### 三种常见状态的说法

| 状态 | 说法 |
|---|---|
| 做完了 | I finished it / It's done / It's in staging / It's ready for review |
| 在做 | I'm still on it / It's in progress / I'm halfway through |
| 卡住了 | I'm blocked on… / I'm stuck on… / I need X to move forward |
| 要延期 | My estimate was Wednesday, but I'm pushing it to Thursday / It slipped |
| 风险低 | It's non-critical and behind a feature flag / Low risk |

### 站会禁忌

- ❌ 讲细节技术方案 → 会后 `take it offline`
- ❌ 报流水账 → 一句一件事
- ❌ 说 "I'm working on many things" → 说具体的那一件

---

## 3. 四级救急阶梯（最实用的一节）

真正卡住你的往往不是不会说，是**听不懂之后怎么办**。

| 级别 | 动作 | 什么时候用 | 风险 |
|---|---|---|---|
| **1 硬猜** | 靠上下文猜 | 只扛 30 秒 | ⚠️ **唯一会出事的一级**——以为听懂了，做错方向 |
| **2 抓关键词** | 只抓功能词，放过内容词 | 全程默认状态 | 低 |
| **3 主动确认** | 用自己的话复述回去 | **发现自己在硬猜就跳到这里** | 几乎无 |
| **4 直接求援** | 让对方慢一点 / 打字 / 会后补 | 信息密度太高时 | 无，但要挑时机 |

### 第 3 级：主动确认句型包（直接背走）

```
So just to confirm — you mean we should roll back first, right?
Let me make sure I got that — the ETA is Thursday, not Friday?
I'm not sure I follow — do you mean X or Y?
Just to play it back — you want me to own the migration, correct?
```

**关键**：句尾用 `right?` / `correct?` / `is that right?`，对方只需回答 yes/no，成本最低。

### 第 4 级：求援句型包

```
Sorry, I didn't quite catch that. Could you say that again a bit slower?
Could you drop the link / that number in the chat?
Would you mind typing that in the chat so I can follow along?
Can we take this offline? I'd like to go through it properly.
```

> `take this offline` = 会后再单独聊（**不是**「下线」，是「这个话题挪出会议」）。

### 抓功能词清单（听力口径）

听英文会议**不要试图听懂每个词**。只盯这几个：

`who` · `what` · `blocked` · `ETA` · `by when` · `deadline` · `decision` · `action item` · `owner` · `risk`

内容词听漏不致命，**功能词听漏才致命**——因为那才是你要行动的部分。

---

## 4. 会议高频短语（按功能分类）

### 推进议程 / 控场

| 短语 | 意思 | 例句 |
|---|---|---|
| `circle back` | 回头再聊 | Let's circle back on this next week. |
| `take it offline` | 会后再单独聊 | That's a good point — let's take it offline. |
| `park it` / `parking lot` | 先搁一搁，记进待议清单 | Let's park it and move on. |
| `table it` | 暂缓（⚠️ 美式=搁置，英式反而=提上议程） | Let's table the discussion. |
| `hard stop` | 必须结束的时间点 | I have a hard stop at 10:30. |
| `walk through` | 逐条过一遍 | Let me walk you through the design. |
| `recap` | 复述要点 | Quick recap of where we landed. |

### 表态 / 给意见

| 短语 | 意思 | 例句 |
|---|---|---|
| `I see the trade-off, but…` | 我理解取舍，但是… | 礼貌反对的标准开场 |
| `Let me play devil's advocate` | 我唱个反调（先说好是角色） | — |
| `That's a stretch for this sprint` | 这个迭代做不完 | 拒绝加需求 |
| `I'd push back on that` | 这个我有异议 | 比 I disagree 缓和 |
| `+1` / `I second that` | 我附议 | 极短表态 |
| `I'm aligned` | 我同意 | 比 agree 更职场 |
| `Let's not boil the ocean` | 别一口吃成胖子 | 反对过度设计 |

### 时间与进度

| 短语 | 意思 |
|---|---|
| `ETA` | 预计完成时间（Estimated Time of Arrival） |
| `by EOD` / `by COB` | 今天下班前（End of Day / Close of Business） |
| `push it to Thursday` | 顺延到周四 |
| `slip` | 进度滑了 | Six points slipped. |
| `on track` / `at risk` / `off track` | 在轨 / 有风险 / 已脱轨 |
| `heads-down` | 埋头干活（别打扰） | I'm heads-down on the migration today. |
| `bandwidth` | 精力 / 余量（不是网络带宽） | Do you have bandwidth to review my PR? |

### 协作 / 通知

| 短语 | 意思 |
|---|---|
| `loop in` | 把人拉进讨论 | Loop me in on that thread. |
| `ping me` | 叫我一声 | Ping me when the build is green. |
| `flag it` | 标出来 / 提个醒 | Flag me if you get stuck. |
| `OOO` | 不在岗（Out of Office） |
| `action items` | 待办事项（会后必看） |
| `sync` / `async` | 同步（实时开会）/ 异步（Slack 留言） |
| `follow up` | 跟进 |

---

## 5. 印度英语适配（三动作）

发音规律本身在 `vocabulary.md` / 之前的讲解里（th→t/d、v≈w、t/d 卷舌、重音移位、s 前插元音、音节计时节奏）。**开会现场只做这三件事：**

1. **会前 5 分钟扫议程和文档** —— 有上下文，节奏再怪也听得住。这是投入产出比最高的一步。
2. **只听功能词**（见第 3 节清单）—— who / what / blocked / ETA / by when。
3. **把 chat 当外挂** —— 听不懂就让对方打字（第 4 级句型）。

### 印度职场特有表达（碰到别懵）

| 说法 | 意思 |
|---|---|
| `prepone` | 提前（postpone 的反义，英式英语里没有） |
| `do the needful` | 请照办 / 麻烦处理一下（老派但极常见） |
| `revert` | 回复我（不是「恢复」！） | Revert back to me. |
| `kindly` | 请（= please，语气更正式） |
| `out of station` | 出差 / 不在本地 |
| `I have a doubt` | 我有个疑问（= I have a question） |
| `updation` | 更新（update 的名词，非标准但常用） |
| `the same` | 指代前面提过的东西 | I'll send the same. |

---

## 6. 本地练习素材

`audio/standup/` 下 5 段真实站会对话，**印度英语音色**（第 5 段为英音），每段一个文件夹：

```
audio/standup/
├── 01-标准站会/            标准站会，谁被 blocked
│   ├── 01-标准站会.html    ← 独立练习页（阅读 + 听）
│   ├── 01-标准站会.mp3
│   ├── 01-标准站会.vtt     中英
│   ├── 01-标准站会.en.vtt  英文
│   └── 01-标准站会.zh.vtt  中文
├── 02-印度团队站会/        ⭐ 印度团队远程站会（Priya / Raj / James）
├── 03-迭代末站会/          迭代最后一天，visual regression、commit to that
├── 04-速率复盘/            velocity、slipped、spike
├── 05-跨时区站会/          英音，跨时区异步站会，OOO / async / recap
└── cues.json              全部台词 + 时间轴 + 中英对照
```

**命名规范：文件夹名 = 音频名 = 字幕名前缀 = HTML 名。** 每段一个文件夹、五件套齐全，所以：

- 双击 `<名>.html` → 在浏览器里**边看逐句稿边听**
- 用 PotPlayer 打开 `<名>.mp3` → 自动挂上同名字幕，右键 → 字幕 → 显示/隐藏字幕即可开关

### 三种用法

| 场景 | 打开什么 |
|---|---|
| 在电脑上精读 + 精听 | 该文件夹里的 `<名>.html`（独立练习页） |
| 通勤 / 手机 / 只放音频 | `<名>.mp3`（PotPlayer 或任意播放器） |
| 五段连着过一遍 | 仓库根目录 `standup-player.html`（带段落切换） |

每个独立练习页都带：字幕四档（关 / 英文 / 中英 / 中文）、语速 0.75×–1.25×、上一句 / 下一句、循环本句、逐句稿点击跳句，以及底部导航（上一段 / 全部 5 段 / 下一段）。
⚠️ 独立练习页引用的是**同目录的 mp3**，所以要**双击本地文件打开**；放进浏览器在线预览是放不出声音的。

### 练习三步闭环（每段 15 分钟）

1. **盲听**一遍，只记功能词：谁在做、谁被卡、ETA 变了没有
2. 换 **1.25×** 再听，抓细节（PR 多少行、谁要 review）
3. 对照 `.vtt` 逐句核，把听漏的词写进 `vocabulary.md`

### 单个文件夹的复现流程

一段素材 → 一个文件夹，**五件套**齐全（html + mp3 + 3 个字幕）。新素材（真实会议记录、同事口头禅、你自己的场景）都可以按同一结构做出来。

---

## 7. 会后回流清单（每次开会后 10 分钟内填）

> 这一步比多练一个练习有用。

```markdown
## 会议：______  日期：______

没听懂的原句（记英文，1–2 句就够）：
1.
2.

当时用了哪一级救急？结果如何：

下次可以补问的一句话：

新学到的词 / 短语（够格就加进 vocabulary.md）：
```

---

## 8. 每日节奏建议

| 时段 | 动作 | 时长 |
|---|---|---|
| 通勤 | 用 PotPlayer 听 `audio/standup/` 里一段的 MP3，盲听 | 10 min |
| 午休 | `standup-player.html` 精练一段，走三步闭环 | 15 min |
| 会前 3 min | 翻本手册对应会议类型 + 当天议程 | 3 min |
| 会后 10 min | 填第 7 节回流清单 | 5 min |

一个迭代（约两周）之后，第 1 节那张表里你会发现自己**站会已经不用打草稿了**。
