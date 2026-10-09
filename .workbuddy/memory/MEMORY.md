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

### 练习素材与工具链
- `audio/standup/`：5 段站会对话，**每段一个独立文件夹**（用户明确要求，为方便 PotPlayer）。文件夹名 = 音频文件名，内含 `<名>.mp3` + `<名>.vtt`（中英）+ `<名>.en.vtt` + `<名>.zh.vtt`；**PotPlayer 打开 mp3 会自动挂上同名字幕**。
- 文件夹：`01-标准站会` / `02-印度团队站会` / `03-迭代末站会` / `04-速率复盘` / `05-跨时区站会`；另有 `audio/standup/cues.json`（台词 + 时间轴 + 中英对照）。
- ⚠️ **MP4 已于 2026-10-09 按用户要求删除，不要再主动生成。** 用户选了「MP3 + 外挂字幕」方案，理由：MP3 才能通勤/手机听，且 PotPlayer 里外挂 `.vtt` 同样能开关字幕，MP4 是重复的。
- `standup-player.html`（仓库根目录）：单文件练习播放器，字幕四档（关/英/中英/中）、变速 0.75–1.25×、逐句循环与跳转。音频源全部指向 `.mp3`。
- **每个文件夹内另有独立练习页 `<文件夹名>.html`**（2026-10-09 按用户要求新增：「规范点，每个会议都要有一个便于阅读和听的 html」）：单文件、无外部依赖、内嵌该段台词与时间轴，音频走相对路径。生成器 **`D:/tmp/build_per_meeting.py`**（读 `cues.json`，改台词后重跑即可，幂等）。
  - **命名规范：文件夹名 = mp3 名 = 字幕名前缀 = html 名。**
  - ⚠️ 音频是相对引用，**必须双击本地文件打开**；在线预览面板只服务单个文件，会没声音（别误判为坏了）。
  - 预览可取巧：`python -m http.server 8765 --bind 127.0.0.1 --directory D:/workspace/EnglishLearning`，再用 `http://127.0.0.1:8765/...` 打开，音频即可播放。
- 音色用 edge-tts 的 **en-IN-NeerjaNeural / en-IN-NeerjaExpressiveNeural / en-IN-PrabhatNeural**（印度口音，按说话人分派）+ en-GB-SoniaNeural（英音）。**逐句合成**，用「字节数 ÷ 6000」换算每句时长，因此字幕可精确逐句同步。
- 这套流程可复用：任意会议素材（真实录音稿、自写场景）都能做成「音频 + 逐句中英字幕 + 播放器」。
- 本机装 Python 包**必须**用腾讯云镜像：`pip install -i https://mirrors.cloud.tencent.com/pypi/simple <包名>`（环境有本地代理 `127.0.0.1:62074`，直连 PyPI 会永久卡住）。静态 ffmpeg 7.1 已装在 `envs/default/Lib/site-packages/imageio_ffmpeg/binaries/`。

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
- 用户常直接贴**真实工作场景的英文句子**（如 DevOps 工程师的 Slack 消息）问意思。讲解流程：
  1. 给整句中文意思 + 时态/单复数等细节提示
  2. 逐个拆解句中的 IT 术语
  3. **（仅在用户要求记录时）** 才把术语写入 `vocabulary.md`
- 讲发音时：给出音标、音节拆分、谐音、常见错读，并尽量总结**可复用的拼读规律**（如「-ability 结尾的词重音固定在 -BIL-」）
- 讲解尽量配一张 SVG 示意图辅助理解（已用：capacity vs velocity、canary 流量切分、音节重音拆解）——示意图只展示在对话里，不等于要写进单词本
