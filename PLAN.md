# IT 会议英语素材库 · 建设方案

面向 **Linux DevOps 岗**的可听可读会议英语素材库，目标规模 **500+ 段**。

---

## 0. 五条硬约束

| # | 约束 | 来源 | 怎么保证 |
|---|---|---|---|
| 1 | **每段 ≤ 2 分钟** | 用户 | `build.py` 硬校验，超时直接报错 |
| 2 | **素材之间必须相互关联** | 用户 | 场次串联 + 表达互引 + 阶段导航 + 学习路径 |
| 3 | **面向 Linux DevOps 岗** | 用户 | 技术域与会议类型双维矩阵，见 §2 |
| 4 | **口语一定要地道** | 用户 | 编稿标准 + 可量化体检，见 §4 |
| 5 | **表达要反复出现，不能只提一次** | 用户 | 表达复现系统，见 §3 |

第四条与第五条是决定成败的两条，其余是容器。

---

## 1. 现状体检（35 句台词实测）

### 1.1 口语地道度：现在是「教科书体」

| 段 | 句数 | 平均词/句 | 最长 | 短句占比 | 缩略 | 语篇标记 | 模糊语 | 填充词 | 纯书面句 |
|---|---|---|---|---|---|---|---|---|---|
| 0001 标准站会 | 8 | 13.2 | 29 | 38% | 6 | 0 | 0 | 0 | 0 |
| 0002 印度团队站会 | 7 | 16.4 | 34 | 14% | 3 | 4 | 3 | 0 | 1 |
| 0003 迭代末站会 | 9 | 14.2 | 34 | 33% | 4 | 0 | 0 | 0 | 3 |
| 0004 速率复盘 | 7 | 19.0 | 31 | 0% | 2 | 3 | 2 | 0 | 1 |
| 0005 跨时区站会 | 4 | 28.2 | 32 | 0% | 3 | 1 | 0 | 0 | 1 |
| **合计** | **35** | **17.0** | **34** | **20%** | 18 | 8 | 5 | **0** | **6（17%）** |

对照口语会议的经验值：**6–9 词/句**，短句占比 **50%+**。
现状是长了一倍、短句只有五分之一。用它练听力，练出来的是「听懂朗读」。

### 1.2 表达复现：99% 的表达只出现一次

| 指标 | 实测 | 目标 |
|---|---|---|
| 不同 2–4 词搭配 | 647 个 | — |
| **只出现 1 次** | **639 个（99%）** | < 25% |
| 出现 2 次 | 8 个（1%） | — |
| **出现 ≥3 次** | **0 个（0%）** | ≥ 60% |
| 平均复现次数 | **1.01** | ≥ 4 |

关键表达的实际复现：

| 3 次 | 2 次 | **仅 1 次** |
|---|---|---|
| `no blockers` | `rollback` `spike` `backlog` `regression` | `in progress` `up for review` `out of office` `behind a flag` `slipped` `staging` `commit to` `pushing it to` `test coverage` `pushed the changes` `blocked` `bandwidth` |

**17 个关键表达里 12 个只出现一次。** 记不住不是使用者的问题，是设计取向问题：

> **1 个表达讲 5 次，胜于 5 个表达各讲 1 次。**

### 1.3 已完成的架构重构（本地未提交）

`一个对话一个页面` → `一个对话一条数据`：

```
sources/dialogues.json    唯一源头
tools/gen_tts.py          配音 + 字幕，回写时间轴
tools/build.py            生成索引与全部页面
tools/README.md           流水线文档
assets/app.css / app.js   全站共享样式与逻辑
data/catalog.js / talks.js 生成物
index.html / player.html  生成物（#编号 路由）
audio/<域>/<编号>-<名>/    每段一文件夹：mp3 + 3 份 vtt + 0.5KB 壳页
```

关键决策（已实施）：

- **数据用 `.js` 而非 `.json`**：`<script src>` 在 `file://` 下可加载，`fetch` 读本地 json 会被拦。这是「双击本地文件就有声音」的前提。
- **条目页从 17 KB 降到 0.5 KB**，CSS/JS 全站共享；新增素材不再触碰任何已有文件。
- **编号 4 位补零**：`1`/`01` 会让字符串排序把 `100` 排到 `02` 前面。
- **时间轴由音频决定**：`duration = 字节数 ÷ 6000`，实测字节率恰为 6000 B/s（edge-tts 是 CBR），与 ffmpeg 实测一致。

---

## 2. 内容体系：双维矩阵

### 2.1 技术域（10 个）

前 6 个是用户点名，后 4 个是 DevOps 岗位必备补充。

| 域 | 名称 | 代表性事件 | 该域高频表达示例 |
|---|---|---|---|
| `linux` | Linux 系统运维 | 磁盘写满 · 负载飙高 · OOM killer · 服务反复重启 · 时间漂移 | `the disk is filling up` · `let me tail the log` · `the process got OOM-killed` · `it's been flapping all morning` · `I'll bump the ulimit` |
| `network` | 网络 | DNS 解析失败 · 证书过期 · 跨区延迟 · LB 502 · 连接重置 | `DNS is timing out` · `the cert expired last night` · `we're seeing connection resets` · `latency spikes across regions` · `let's check the MTU` |
| `database` | 数据库 | 慢查询 · 连接池耗尽 · 主从延迟 · 备份恢复失败 · 在线 DDL | `the pool's exhausted` · `replication lag is climbing` · `let's restore from the last snapshot` · `that query's doing a full scan` |
| `coding` | 编程与脚本 | 脚本报错 · 依赖冲突 · 边界条件 · 性能优化 · 日志埋点缺失 | `it blows up on edge cases` · `the deps are pinned wrong` · `let's add a guard clause` · `I'll instrument it` |
| `ha` | 高可用与容量 | 单点故障 · 切换失败 · 限流降级 · 容量不足 · 多活同步 | `we're single-homed on that` · `failover didn't kick in` · `let's shed load` · `we're at capacity` · `that's our blast radius` |
| `cicd` | CI/CD 与发布 | 流水线挂 · 制品污染 · 灰度回滚 · 环境不一致 · 构建超时 | `the pipeline's red` · `it's stuck on the build step` · `the artifact is stale` · `we need to cut a release` |
| `k8s` | 容器与编排 | CrashLoop · 节点 NotReady · 探针误判 · 配额不足 · 镜像拉取失败 | `it's in CrashLoopBackOff` · `the node went NotReady` · `the readiness probe is too aggressive` · `it's throttling on CPU` |
| `cloud` | 云与成本 | 账单暴涨 · 规格选型 · 跨区流量费 · IAM 权限 · IaC 漂移 | `the bill spiked` · `that's egress charges` · `we're overprovisioned` · `let's right-size it` |
| `obs` | 可观测性与告警 | 告警噪音 · 指标缺失 · 链路断点 · On-call 疲劳 · SLO 口径 | `the alert's too noisy` · `we're flying blind on that` · `the trace breaks at the gateway` · `that's alert fatigue` |
| `sec` | 安全与合规 | 漏洞应急 · 密钥泄漏 · 越权访问 · 合规审计 | `that CVE is exploitable` · `a key leaked to the repo` · `that's a privilege escalation` |

### 2.2 会议类型（8 组）

| 组 | 名称 | 在 DevOps 日常里的分量 |
|---|---|---|
| `incident` | 故障与应急 | 最高频、压力最大，含故障会 / 复盘 / 战情室 |
| `change` | 变更与发布 | 变更评审 / 发布协调 / 回滚决策 |
| `handoff` | 值班交接 | 每天或每周，必须说清未决事项 |
| `ops-standup` | 运维站会 | 每天，三段式报进度 |
| `review` | 架构与容量评审 | 基建评审 / 容量成本 / SLO |
| `agile` | 计划与回顾 | Sprint Planning / Retro |
| `allhands` | 全员会与一对一 | 纯听力场景，抓决策与 action items |
| `interview` | DevOps 技术面试 | 讲项目、答系统设计、反问 |

### 2.3 配额分配

10 域 × 50 段 = **500 段**。每域内的会议类型分布固定：

| incident | change | handoff | ops-standup | review | agile | allhands | interview | 小计 |
|---|---|---|---|---|---|---|---|---|
| 12 | 8 | 6 | 6 | 6 | 6 | 4 | 2 | **50** |

一个域 50 段、每段 ≤2 分钟，合计约 **100 分钟**——差不多是一个技术域能"泡"够的时长。

### 2.4 段 ⇒ 场次的换算

一段 25 分钟的真实会议可切成 12–15 段。**500 段 ≈ 30–45 场真实会议**，不是 500 场。
首批不必追求真实录音：按矩阵自编即可，真实素材后续用 `tools/split.py` 切段接入。

### 2.5 现有 5 段的定位

保留作**教科书体对照教材**（用户选择），不进达标评分，归入独立系列。

它们同时充当**表达池的种子**：里面 127 个表达就是第一批待复现清单，只是新素材要用**更地道的说法**重说一遍：

> `It is up for review.`（教科书体） → `It's up for review — anyone got bandwidth to take a look?`（口语体）

对照教材负责「教」，新素材负责「反复提」。

---

## 3. 表达复现系统

### 3.1 表达分层与配额

| 层 | 内容 | 数量 | 目标出现次数 | 位次合计 |
|---|---|---|---|---|
| **L0 通用会议表达** | 跨所有域：`circle back` `take it offline` `heads-down` `bandwidth` `hard stop` `ETA` `action item` | 100 | 8–15 | 约 1200 |
| **L1 域内核心表达** | 每域 30 个 | 300 | 4–6 | 约 1500 |
| **L2 域内长尾表达** | 每域 10 个 | 100 | 2–3 | 约 250 |
| | | **500** | 平均约 6 | **约 2950** |

500 段 × 每段 6 个表达位 = 3000 位，正好容纳。

> **500 段素材，只教 500 个表达，每个让你听到约 6 遍。**
> 而不是 2500 个各听一遍。

### 3.2 每段配额

**1 个新表达 + 5 个复现表达。** 其中 ★ 核心表达保证 ≥5 次。

### 3.3 间隔递增（spacing effect）

不是下一段就重复，而是按递增间隔回访：

| 第几次 | 间隔 | 举例（首次在 0012） |
|---|---|---|
| 1 | — | 0012 |
| 2 | +2 段 | 0014 |
| 3 | +4 段 | 0018 |
| 4 | +8 段 | 0026 |
| 5 | +15 段 | 0041 |
| 6+ | 之后随机回访 | 0067 / 0092 … |

关键要求：**变体复现**。同一表达在不同段里由**不同角色、不同语速、不同口音**说出——不是重放录音，是换人说。这比重放同一句有效得多，而且这才是真实会议的样子。

### 3.4 重点分级

不能一标标十个，等于没标。每段硬上限：

- **★ 核心表达 1–3 个**：必须记住，保证 ≥5 次复现，自动进「待记清单」
- **○ 了解即可 2–3 个**：看得懂即可，复现 2–3 次

「待记清单」与单词本的关系：清单由 `build.py` 生成，**用户勾选后**才写入 `vocabulary.md`（遵守既有的「记录红线」）。

### 3.5 编稿顺序反过来了

| 旧 | 新 |
|---|---|
| 先写台词 → 再标注用了哪些表达 | **先定这段要复现哪几个表达 → 再写台词把它们自然嵌进去** |

「表达互引」从查询工具变成了设计约束。

### 3.6 复习模式（跨片段抽句）

选一个表达 → 把**所有含它的句子抽出来连播**，不听整段。

这是「时不时反复提起」的自动化版本：不用等素材里再出现，任何时候都能把某个表达的 6 次出现连着听一遍。同时也是 `meeting-english.md` 手册的听力配套。

---

## 4. 编稿标准

### 4.1 三层可检查

| 层 | 标准 | 硬指标 |
|---|---|---|
| **用词** | 真实会议搭配 | 判负词表命中 = 0 |
| **句法** | 6–9 词/句；短句 ≥50%；每 10 句 ≥3 个语篇标记；每段 ≥1 处模糊语、≥1 处不完整句或打断 | 见 §6 |
| **口音** | **印度英语的语音和句法** | 每段 ≥1 处印度英语特征 |

第三层是关键：目标是听懂印度同事，只做标准英美口语等于没练到点上。

### 4.2 判负词表（教科书写法，出现即不合格）

`I would like to` · `in order to` · `furthermore` · `moreover` · `I am writing to` · `please find` · `kindly note that` · `as per` · `it is imperative` · `we should note that`

### 4.3 印度英语特征清单（每段至少 1 处）

句法：

- `I have a doubt`（= 我有问题，不是"怀疑"）
- `You are coming right?`（陈述语序 + right 提问）
- `It is not there only`（句尾 only 强调）
- `Please revert` / `do the needful` / `prepone`
- 现在进行时泛用：`I am having a doubt` / `I am having a meeting`
- `itself` 强调：`We need to fix it itself`
- `out of station`（= 不在）

语音（写进 `phrases` 的 `note` 里提示）：

- th → t/d：`three` 像 `tree`，`this` 像 `dis`
- v 与 w 合流
- t/d 卷舌
- 重音移位：`development` → deve-**LOP**-ment
- s 前插元音：`school` 像 `iskool`
- **音节计时节奏**：每个音节等时，重音弱化不明显——这是最难的一条

### 4.4 读音规范（DevOps 专有，页面里标注）

| 写法 | 读法 |
|---|---|
| `K8s` | "kates" /keɪts/ |
| `kubectl` | "cube-control" 或 "kube-cuttle" |
| `nginx` | "engine-x" |
| `SLO` `SLA` `SRE` `PR` `CI/CD` | 逐字母 |
| `5xx` | "five hundred"（不读 five-ex-ex） |
| `223` | "two twenty-three"（不读 two-two-three） |
| `sudo` | "soo-doo" |
| `i.e.` / `e.g.` | 口语说 "that is" / "for example" |
| `1.5` | "one point five" |
| `99.9%` | "three nines" |

---

## 5. 数据模型

### 5.1 新增字段

```jsonc
{
  "series": [                                   // 场次 / 事件线
    { "id": "inc-2604-checkout-5xx",
      "group": "incident", "domain": "network",
      "title": "checkout 5xx 故障响应",
      "date": "2026-04-11", "service": "checkout",
      "impact": "约 12 分钟 5xx 上升到 4%",
      "roles": ["on-call", "SRE lead", "app owner"] }
  ],

  "dialogues": [
    { "id": "0012",
      "group": "incident",                       // 会议类型（轴 1）
      "domain": "network",                       // 技术域（轴 2）
      "series": "inc-2604-checkout-5xx",
      "part": 2, "parts": 5,
      "stage": "定位",                            // 告警 / 定位 / 决策 / 执行 / 复盘
      "premise": "上回说到 5xx 从 0.3% 涨到 4%，on-call 正在拉日志。",
      "title": "拉日志与链路，圈定问题面",
      "accent": "印度英语", "voiceSet": "en-IN",
      "tags": ["日志", "链路追踪", "圈定范围"],

      "phrases": [
        { "en": "I'll take point on this", "zh": "这块我来主抓",
          "level": "core",                       // core | extra
          "layer": "L0",                         // L0 | L1 | L2
          "recycle": "new",                      // new | 第 N 次复现
          "note": "认领主导权，比 I'll lead 更口语" },
        { "en": "it's upstream of us", "zh": "问题在我们上游",
          "level": "extra", "layer": "L1", "recycle": 2 }
      ],

      "register": {                              // 脚本回写的体检结果
        "wps": 7.4, "short_ratio": 0.58, "markers": 6,
        "hedges": 2, "indian": 1, "banned": 0
      },

      "duration": 64.3,                          // 脚本维护
      "lines": [ /* sp / role / en / zh / start / end */ ]
    }
  ]
}
```

### 5.2 表达库

`build.py` 从各段 `phrases` 聚合出 `data/phrases.js`，并据 `recycle` 目标算出「到期未复现」清单。

```jsonc
{
  "I'll take point on this": {
    "zh": "这块我来主抓", "layer": "L0", "level": "core",
    "target": 8, "seen": ["0012", "0014", "0018"], "next_due": "0026",
    "note": "认领主导权，比 I'll lead 更口语"
  }
}
```

`target` 由 `layer` 决定（L0 8–15 / L1 4–6 / L2 2–3），可人工覆盖。

---

## 6. 体检指标（接进 `build.py --check`）

不达标直接失败，**复现不靠人的记性，靠流水线**。

| 指标 | 现状 | 目标 | 级别 |
|---|---|---|---|
| 每段时长 | 52–75s | ≤ 120s | 硬失败 |
| 平均词/句 | 17.0 | 6–9 | 硬失败 |
| 短句（<8 词）占比 | 20% | ≥ 50% | 硬失败 |
| 印度英语特征数/段 | — | ≥ 1 | 硬失败 |
| 判负词命中 | — | 0 | 硬失败 |
| 每段 ★ 核心表达数 | — | 1–3 | 硬失败 |
| 一次性表达占比 | 99% | < 25% | 警告 |
| 平均复现次数 | 1.01 | ≥ 4 | 警告 |
| 出现 ≥3 次的表达占比 | 0% | ≥ 60% | 警告 |
| 到期未复现清单 | — | 每次构建列出 | 报告 |

---

## 7. 关联四层（全部要建）

| 层 | 内容 | 生成方式 |
|---|---|---|
| **场次串联** | 同场会议片段首尾相接，「上一段/下一段」只在同场内生效；每段开头显示 `premise` | ✅ 自动 |
| **表达互引** | 点任意表达 → 列出它还在哪几段出现过；卡片上显示「你已经听过 6 次」 | ✅ 自动（聚合 `phrases`） |
| **阶段导航** | 按 `stage` 筛选：「只练故障定位那一段」 | ✅ 自动 |
| **学习路径** | 人工编排：「DevOps 值班交接 8 段」「K8s 故障排查 12 段」；先自动生成候选，人工增删 | ⚠️ 半自动 |
| **复习模式** | 选表达 → 跨片段抽句连播 | ✅ 自动 |

前三层随素材量增长**成本不增加**。

---

## 8. 施工顺序

| 步 | 内容 | 量级 | 状态 |
|---|---|---|---|
| 1 | 数据模型加 `series`/`domain`/`stage`/`premise`/`phrases` + 时长硬校验 + baseline 标记 | 小 | ✅ |
| 2 | 现有 5 段归入「教科书体对照」系列，跑通全链路 | 小 | ✅ |
| 3 | 建表达库 `sources/phrases.json`（36 条，L0 通用 14 / 网络 11 / K8s 11） | 中 | ✅ |
| 4 | 体检脚本（§6 全部指标）接进 `build.py`（构建时自动跑） | 中 | ✅ |
| 5 | **试产 20 段 = 2 条完整事件线**，交用户审 | 中 | ✅ 见 §10 |
| 6 | 样板达标后按矩阵批量生产；`tools/split.py` 接入真实长素材 | 大 | ⬜ |
| 7 | 关联 UI：场次导航 ✅ + 表达互引 ✅ + 「已出现 N 次」✅ · 阶段筛选 / 复习模式 / 学习路径 ⬜ | 大 | 🟡 |

**第 5 步是风险闸门。** 先出样板定调再批量，避免编了 300 段被整体推翻。

---

## 10. 试产结果（20 段，2026-10-09）

两条完整事件线，各 10 段，全部 ≤2 分钟：

| 事件线 | 会议类型 × 技术域 | 段数 | 编号 | 最长段 |
|---|---|---|---|---|
| checkout 5xx 故障响应 | `incident` × `network` | 10 | 0006–0015 | 63.5s |
| K8s 1.27 → 1.28 升级与回滚 | `change` × `k8s` | 10 | 0016–0025 | 61.5s |

对照旧素材（0001–0005，已归入 `baseline` 系列，不计入评分）：

| 指标 | 旧素材 | 试产 20 段 | 目标 |
|---|---|---|---|
| 平均句长 | 17.0 词/句 | **6.2 词/句** | 6–9 ✅ |
| 短句（<8 词）占比 | 20% | **80%** | ≥50% ✅ |
| 判负词命中 | — | **0** | 0 ✅ |
| 每段印度英语特征 | — | **≥1**（全部达标） | ≥1 ✅ |
| 每段 ★ 核心表达 | — | **1–3**（全部达标） | 1–3 ✅ |
| 平均复现次数 | 1.01 | **2.19** | ≥4 ⚠️ |
| 只出现 1 次的表达 | 99% | **25%** | <25% ⚠️ |
| 出现 ≥3 次的表达 | 0% | **28%** | ≥60% ⚠️ |
| 单段时长 | 52–75s | 42–64s | ≤120s ✅ |

**硬指标全部通过；复现项三项未达满量目标，属试产阶段正常**——20 段 × 6 表达位 = 120 位，36 个表达平均只能摊到 2.2 次。按 §3.1 的配额外推，500 段时 2950 位 / 500 表达 ≈ 5.9 次，才收敛到目标。已验证的是**机制**（复现率 1.01 → 2.19，一次性表达 99% → 25%），不是终值。

**瓶颈在内容生产，不在程序。** 代码侧的扩展性（第 1 步）已在上一轮重构中完成。

---

## 9. 目录职责

| 路径 | 角色 | 谁来改 |
|---|---|---|
| `sources/dialogues.json` | 唯一源头：场次 + 分组 + 逐句中英文本 + 表达标注 | 人工（时间轴字段除外） |
| `sources/phrases.json` | 表达库（分层、目标次数、备注） | 人工 + 脚本聚合 |
| `tools/gen_tts.py` | 配音 + 3 份 VTT，回写时间轴 | — |
| `tools/build.py` | 生成索引与全部页面；`--check` 跑 §6 体检 | — |
| `tools/split.py` | 长素材按时长与话轮切段（待写） | — |
| `assets/app.css` `assets/app.js` | 全站共享样式与逻辑 | 人工 |
| `data/*.js` | 生成物：索引、台词、表达库 | 脚本 |
| `index.html` `player.html` | 生成物：首页与播放器 | 脚本 |
| `audio/<域>/<编号>-<名>/` | 媒体目录，每段一文件夹 | 脚本 |

> `data/`、`index.html`、`player.html`、媒体目录里的 `.html` 都是生成物，不要手改。
