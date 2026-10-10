# 项目长期记忆 — EnglishLearning

## 项目定位
英语学习项目，**专门记录 IT 相关英语**（非通用英语词典）。
范围：技术术语、开发/运维/产品工作场景用语、开源与技术社区表达、技术面试英语。

## 用户的学习目标与薄弱环节（2026-10-08 用户主动说明）
- **核心痛点：听不懂和印度同事 / IT 团队开英文会议。** 想知道会议里会出现哪些表达，并要学习方法 + 音视频资源。
- **（2026-10-09 明确收窄）学习重心 = 「IT 英语会议」相关**。用户主动说「我主要是想学习 IT 英语会议相关的内容」。通用 IT 术语仍收，但**讲解优先排会议场景**；另据其反馈「单纯学习效果不好」，需偏互动/游戏化练习形式。
- 讲解与选词时优先靠拢：**会议/协作场景英语**、**印度英语发音规律**、**听不懂时的救急句型**。
- 已讲过的框架（可复用，勿重复科普）：
  - 印度英语六条发音规律：th→t/d · v 与 w 合流 · t/d 卷舌 · 重音移位 · s 前插元音 · **音节计时节奏**（最关键）
  - 练习闭环：精听 20 min → 跟读 10 min → 会前预装 3 句 → 会后复盘回流
  - 印度职场特有表达：`prepone`、`do the needful`、`revert`、`kindly`、`out of station`、`I have a doubt`、`updation`
    - ⚠️ **2026-10-10 教训：清单式罗列对用户无效。** 这批词当时一次性列过，但用户 10-10 又重新问 `do the needful`。以后这类词**逐条单讲**，并给「听 vs 说」的用法决策 + 替代表达（如 `I'll handle it with support.`）。
- 资源清单已给过：NPTEL 印度公开课、Great Learning、印度新闻频道、Sundar Pichai / Satya Nadella 访谈、B 站与中国大学 MOOC、AI 陪练（ELSA Speak、流利说、有道 Hi Echo 等）。
- ~~待办：用户尚未决定是否把会议英语整理成独立文件（如 `meeting-english.md`）放进仓库。~~ **2026-10-09 已完成：`meeting-english.md` 已建成并推送。**

## 版本控制 / GitHub

- **远程仓库：https://github.com/chlinwei/EnglishLearning（公开）**，默认分支 `main`，本地 `main` 已与 `origin/main` 关联。
- 2026-10-08 完成首次提交与推送，commit `75487b8`「初始化 IT 英语单词本」。
- `.workbuddy/` 目录**一并提交**（用户确认，明知会公开）；`.gitignore` 只忽略系统/编辑器垃圾文件。
- git 作者身份（已写入全局配置）：`chlinwei` / `chlinwei@users.noreply.github.com`（用隐私邮箱）。
- GitHub 账号：**chlinwei**。
- ⚠️ **已解决的环境坑：`git push` 曾永久卡住不动。**
  - **根因**：WorkBuddy 自带的 PortableGit 在**系统级** gitconfig（`resources/vendor/PortableGit/etc/gitconfig`）里写了 `credential.helper = helper-selector`，即 `git-credential-helper-selector`——一个会**弹窗让用户选凭据助手**的程序。git 按顺序尝试所有 helper，撞上它就无限等待（追踪日志里能看到 `HTTP/1.1 401 Unauthorized` 后卡在此处）。
  - **修复**：在全局 `~/.gitconfig` 用**空值重置** helper 列表（这样才能顶掉系统级配置），再指定无 UI 的 GCM：
    ```bash
    git config --global --unset-all credential.helper
    git config --global --add credential.helper ""
    git config --global --add credential.helper '!f() { git-credential-manager "$@" --no-ui; }; f'
    ```
  - 修复后普通 `git push` 恢复正常。
  - **备用手段**（若将来再卡）：`git-credential-manager get --no-ui` 取令牌 → 用内联凭据推送
    `git push "https://chlinwei:<TOKEN>@github.com/chlinwei/EnglishLearning.git" main:main`
- GitHub OAuth 授权方式：`git-credential-manager github login`（会弹窗 + 开浏览器，用户点一次同意即可）。
- 本机**未安装 `gh` CLI**（曾下载作备用，已删除）；需调 GitHub API 时直接用 `curl`。

### 会议英语场景手册 `meeting-english.md`（2026-10-09 建）
- 定位：**场景手册**，与 `vocabulary.md` 分工（一本查词 / 一本查场景）。章节：六类会议对照表 · 站会三段式模板 · 四级救急阶梯 + 句型包 · 会议高频短语（控场/表态/时间/协作）· 印度英语适配三动作 + 印度职场特有表达 · 本地练习素材 · 会后回流清单 · 每日节奏。
- 改这份手册**不受单词本的记录红线约束**（红线只针对 `vocabulary.md` 的自动追加）。

### 疑问台账 `questions.md`（2026-10-10 建，用户要求）
- **定位：可自测的「问题卡」集合**，与 `vocabulary.md`（查词）/ `meeting-english.md`（查场景）分工 —— 这本是 **查「我自己的卡点」**。
- 用户原话：「帮我记录下我得疑问到专门得文档中以便于后续强化」→ 目的是**间隔复习、把一次性听懂变成永久听懂**。
- 结构：A 小词/功能词 · B 术语行话 · C 语音听感 · D 方法类 · E 规律聚类 · F 素材改进项 · G 复习节奏（2 天→7 天→15 天）。
- **每张卡的写法（新卡照此追加）**：`出处（4 位编号 + 说话人 + 原句，卡点加粗）` → `当时的疑问`（用用户原话）→ `要点`（结构解释 + 同族对照表）→ `自测`（一问一答）→ `复现`（全库出现几处、在哪些段）→ `状态`（待复习 / 待复习·已过 N 遍 / 已掌握）。
- **维护约定**：只记**真实卡点**，不记已会的词；讲解完发现新卡点就追加到对应分类，并在「进度」行更新计数；用户自测讲得出来才移入「已掌握」。
- ⚠️ 建这份台账时顺带得出的结论（写进了其 §E）：
  1. **用户卡的全部是功能词**（`of`/`over`/`though`/`out`/`land`/`up`），不是生词 → 瓶颈在**结构敏感度**，不在词汇量。
  2. 英语习惯**用空间词量时间/关系**（upstream of us / moving over / thirty days out / landed）→ 可整族一起拿下。
  3. 「觉得发音怪」要分两类：**真语音现象**（靠语法补）vs **TTS 产物**（句内 0.88s 硬停顿，别当听力样本）。
  4. **新增一类陷阱：分离式短语动词**（`write + 宾语 + up`）。宾语把动词劈成两半后，后半截会贴到宾语屁股后面，看起来像新短语——用户把 `writing that rule up` 读成了 `rule up`。同机制：`write it up` / `send it over` / `log them up` / `take it offline`。**代词宾语必须夹中间（`write it up` ✓ / `write up it` ✗）**，这是识别它的最快线索。以后遇到「用户读出一个不存在的短语」，**先怀疑是宾语劈开了短语动词**。

## ★ 用户岗位（2026-10-09 用户主动说明，最高权重）
**用户是 Linux DevOps 工程师。** 所有选词、场景、例句、素材的**权重排序都要按 DevOps 排**，不是通用开发：
- 优先场景：**故障会 / 事故复盘 / 值班交接 / 变更评审 / 发布协调与回滚 / 容量与成本 / SLO 错误预算 / 基建架构评审**；其次才是通用敏捷会议（站会、计划会、回顾会）。
- 高频技术域：K8s、CI/CD、监控告警、Linux、网络、云与账单、IaC。
- 出例句、编素材时默认站在「运维当事人」视角（被 @ 的人、要发 update 的人、要解释回滚的人）。

## 四条硬约束（2026-10-09 用户陆续提出，做任何素材都要同时满足）
1. **每段素材 ≤ 2 分钟**（用户原话「每个视频最多2分钟」）。现有 5 段 52–75s 合规。
2. **素材之间必须相互关联**（原话「每个素材对话要相互关联」）—— 不能是 500 个孤岛。
3. **面向 Linux DevOps 岗**（见上）。
4. **口语一定要地道**（原话），不能是教科书英语。
> 用户明确要求：**先给方案再动手**（「你先别着急做」「你要先给我方案」）。涉及架构级改动必须先出方案、等确认。

### 架构（2026-10-09 重构完成，未提交）
```
sources/dialogues.json    唯一源头：分组 + 元数据 + 逐句中英文本（start/end/duration 由脚本回写）
tools/gen_tts.py          配音 + 3 份 VTT，回写时间轴（--check/--dry-run/--missing/--only/--rate）
tools/build.py            生成 data/*.js、index.html、player.html、每条目页（--check 只校验）
tools/README.md           流水线文档
assets/app.css / app.js   全站共享样式与逻辑
data/catalog.js / talks.js 生成物
index.html / player.html  生成物（player.html 用 #编号 路由）
audio/<组>/<编号>-<名>/    每段一个文件夹：mp3 + .vtt/.en.vtt/.zh.vtt + 0.5KB 壳页
```
- **数据必须是 `.js`（`window.CATALOG = ...`）而不是 `.json`**：`<script src>` 在 `file://` 下可加载，`fetch` 读本地 json 会被同源策略拦掉。这是「双击本地文件也有声音」的前提。
- **编号一律 4 位补零**（`0001`…`0500`）：`1`/`01` 会让字符串排序把 `100` 排到 `02` 前面。
- **时间轴由音频决定**：`duration = 音频字节数 ÷ 6000`，实测字节率恰为 **6000 B/s**（edge-tts 是 CBR），与 ffmpeg 实测一致。
- 音色分配：按首次出场顺序在同性音色池轮转（配置在 `sources` 的 `voices` / `speakers`）。
- ⚠️ **MP4 已于 2026-10-09 按用户要求删除，不要再主动生成。** 用户选「MP3 + 外挂字幕」：MP3 才能通勤/手机听，且 PotPlayer 里外挂 `.vtt` 同样能开关字幕。
- 旧文件已删：`standup-player.html`、`audio/standup/cues.json`、`audio/standup/vtt/`。生成器 `D:/tmp/build_per_meeting.py` 等**已被 tools/ 取代**。
- 本机装 Python 包**必须**用腾讯云镜像：`pip install -i https://mirrors.cloud.tencent.com/pypi/simple <包名>`（环境有本地代理 `127.0.0.1:62074`，直连 PyPI 会永久卡住）。静态 ffmpeg 7.1 已装在 `envs/default/Lib/site-packages/imageio_ffmpeg/binaries/`。
- 本地预览：`python -m http.server 8765 --bind 127.0.0.1 --directory D:/workspace/EnglishLearning`。

## 约定

### 单词本 `vocabulary.md`
- 每条词条的字段：单词 / 音标 / 词性 / 释义 / **IT 语境** / 例句（IT 场景）/ 搭配 / 易混点
- 例句优先使用技术场景（代码、PR、部署、面试等），不要用学校、体育等无关场景
- 每条词条标注「分类」，分类索引：通用职场 / 编程开发 / 系统运维 / 开源社区 / 技术面试
- 词条按添加顺序编号（## 1. xxx、## 2. xxx …）
- 只收与 IT 相关的词；纯日常词（如 apple、weather）不收

### ⚠️ 记录红线（2026-10-08 用户明确要求，最高优先级）
- **只有用户明说「记下来」时才写入 `vocabulary.md`。** 平时只做讲解，绝不动文件。
- **禁止**以「用户没反对」「顺手」「这个词很有用」为由自作主张追加词条。已因此被纠正过一次（一口气加了 5 条，被要求删除 mitigate）。
- 觉得某词值得记时，最多在回复末尾**建议一句**，等用户明确同意再写。
- 用户已知的词不要再讲一遍基础义项（如 mitigate），讲解要挑信息量大的部分。

### 交互约定
- **（2026-10-10 观察到的稳定模式）用户会直接贴素材里的单句 + 圈出一个词问用法**（已问：`of us` / 句尾 `though` / `moving over` / `the needful` / `play it back` / `elevated`）。
  讲解模板（已验证有效，照此办）：① 定位到具体素材 id/段号/说话人/时间轴 → ② 用**结构**解释（不是词义科普）→ ③ 给**同族对照表**（3 个近义词并列）→ ④ 给**听力/发音提示** → ⑤ 结尾若发现译文偏差或语料复现问题，**只说不动文件**，等用户发话。
- 每次讲解后把「素材 id + 问的词 + 结论」追加到当日日志；若发现译稿或复现问题，一并记录。
- 用户常直接贴**真实工作场景的英文句子**（如 DevOps 工程师的 Slack 消息）问意思。讲解流程：
  1. 给整句中文意思 + 时态/单复数等细节提示
  2. 逐个拆解句中的 IT 术语
  3. **（仅在用户要求记录时）** 才把术语写入 `vocabulary.md`
- 讲发音时：给出音标、音节拆分、谐音、常见错读，并尽量总结**可复用的拼读规律**（如「-ability 结尾的词重音固定在 -BIL-」）
- 讲解尽量配一张 SVG 示意图辅助理解（已用：capacity vs velocity、canary 流量切分、音节重音拆解）——示意图只展示在对话里，不等于要写进单词本

## 素材库 v2：数据驱动 + 场次串联（2026-10-09）

**架构**：`一个对话一个页面` → `一个对话一条数据`。唯一源头是 `sources/`，页面与索引全是生成物（不要手改）。
```
sources/dialogues.json   场次 + 分组 + 逐句中英文本 + 表达引用
sources/phrases.json     表达库（36 条：L0 通用 14 / network 11 / k8s 11）
tools/gen_tts.py         配音 + 3 份 VTT，回写时间轴
tools/build.py           生成索引与页面 **并自动跑编稿体检**
data/catalog.js talks.js phrases.js
index.html player.html   生成物
audio/<域>/<编号>-<名>/   每段一文件夹（mp3 + 3 字幕 + 0.5KB 壳页）
```
- **分组改成 DevOps 会议类型 9 组**；旧的 standup/planning/retro/review/other 全部并入 **`baseline`（教科书体对照，不计分）**，旧 5 段目录在 `audio/baseline/`。
- **编号 4 位补零**（`100-` 会排到 `02-` 前面）。新素材按域建目录：`audio/network/`、`audio/k8s/`。
- ⚠️ **en-IN 只有 Prabhat 一个男声**，多人会议必须用**逐段 `voiceOf` 映射**混入 en-GB/en-US，否则撞声。
- 表达引用可写 **`p010:extra`** → 在本段降级为 ○，用来把每段 ★ 压到 ≤3 个。
- 体检硬指标：时长≤120s · 平均句长 5–9.5 词（**剔除 ≤2 词应声句**）· 短句≥50% · 印度特征≥1/段 · 判负词=0 · ★每段 1–3。
- ⚠️ **切句必须保留句末标点**，否则 `right?` / 句尾 `only` 这类印度英语模式全部漏检。
- 前端口径：段落页显示「场次面包屑 + 阶段 + 第 N/M 段 + 上回说到 + 本段重点表达（已出现 N 次、也出现在哪几段）+ 同场次前后导航」。
- 本机装包必须走腾讯云镜像（不改）；预览用 `python -m http.server <端口> --bind 127.0.0.1 --directory D:/workspace/EnglishLearning`。
- **`PLAN.md`** 是完整建设方案（500 段目标、10 域 × 8 会议类型矩阵、表达复现系统、编稿标准、体检指标、施工顺序）。试产结果见其 §10。
