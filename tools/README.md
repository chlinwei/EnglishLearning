# tools/ — 素材流水线

把「文本」变成「能听能读的练习素材」。**源头只有一个文件**：`sources/dialogues.json`。

## 目录职责

| 路径 | 角色 | 谁来改 |
|---|---|---|
| `sources/dialogues.json` | 唯一源头：分组定义、每段对话的元数据与逐句中英文本 | **人工**（`start`/`end`/`duration` 除外，见下） |
| `tools/gen_tts.py` | 配音 + 字幕，并把时间轴回写源头 | — |
| `tools/build.py` | 生成索引与全部 HTML | — |
| `assets/app.css` `assets/app.js` | 全站共享样式与逻辑（**不随素材数量增长**） | 人工 |
| `data/catalog.js` `data/talks.js` | 生成物：索引 + 全部台词 | 脚本 |
| `index.html` `player.html` | 生成物：首页与播放器 | 脚本 |
| `audio/<分组>/<编号>-<名称>/` | 媒体目录，每段一个文件夹 | 脚本（`<名称>.html` 由 build 生成） |

> ⚠️ `data/`、`index.html`、`player.html`、媒体目录里的 `.html` 都是生成物，不要手改，会被覆盖。
> `build.py` 会清理「由它生成但已不在索引里」的条目页，手写的 HTML 不会被碰。

## 三条命令

```bash
# 1) 配音 + 出字幕（会回写时间轴；--missing 只补没配过的段落）
python tools/gen_tts.py --missing

# 2) 生成索引与页面
python tools/build.py

# 3) 只校验不写文件（提交前跑一下）
python tools/build.py --check
```

配音时的其它开关：

```bash
python tools/gen_tts.py --check              # 校验音色是否都可用（不合成）
python tools/gen_tts.py --dry-run            # 只看音色分配，不合成
python tools/gen_tts.py --only 0003,0007     # 只重做指定段落
python tools/gen_tts.py --rate -10%          # 整体降速重配
```

依赖：`edge-tts`（必需）、`imageio-ffmpeg`（可选，用于校准时长）。

## 新增一段素材

1. 在 `sources/dialogues.json` 的 `dialogues` 里追加一条（编号接着往下排）；
2. 在 `audio/<分组>/` 下建好文件夹并把文件放进去 —— 或者干脆跳过，让 `gen_tts.py` 自己生成；
3. `python tools/gen_tts.py --missing` → `python tools/build.py`。

**不需要改动任何已有文件**：导航、搜索、分组、进度都是从索引渲染的，加 1 段和加 500 段的代价一样。

## 数据格式

```jsonc
{
  "version": 1,
  "mediaRoot": "audio",          // 媒体根目录，将来换网盘/CDN 只改这一行
  "voices": {                    // 音色池，按 voiceSet 引用
    "en-IN": { "female": ["en-IN-NeerjaNeural", "en-IN-NeerjaExpressiveNeural"],
               "male": ["en-IN-PrabhatNeural"], "narrator": "en-IN-PrabhatNeural" }
  },
  "speakers": { "Priya": "F", "Raj": "M" },   // 说话人性别，决定用哪个音色池
  "groups": [
    { "id": "standup", "name": "站会", "en": "Standup", "desc": "…", "order": 1 }
  ],
  "dialogues": [
    {
      "id": "0002",                    // 4 位补零，决定排序与 URL（player.html#0002）
      "group": "standup",
      "seq": 2,                        // 组内序号，用于显示
      "title": "印度团队远程站会",
      "scene": "远程视频站会，三位参与者。",
      "dir": "standup/0002-印度团队站会",   // 相对 mediaRoot
      "audio": "0002-印度团队站会.mp3",
      "accent": "印度英语",
      "voiceSet": "en-IN",
      "tags": ["PR 评审", "bandwidth"],
      "roles": ["Priya（Tech Lead）", "Raj", "James"],
      "duration": 64.3,                // ← 脚本维护
      "lines": [
        { "sp": "Priya", "role": "Tech Lead", "en": "…", "zh": "…",
          "start": 5.232, "end": 11.88 }    // ← 脚本维护
      ]
    }
  ]
}
```

**哪些字段是脚本维护的**：`start` / `end` / `duration` 由 `gen_tts.py` 从音频算出来，
因为时间轴必须和音频严格对齐。改文本后重跑配音即可，不要手改这三个值。

## 几个刻意的设计

- **编号 4 位补零**：`0001`…`0500`。用 `1`/`01` 的话，字符串排序下 `100` 会排在 `02` 前面，
  文件管理器里的顺序就乱了。
- **每段一个文件夹，四个文件同名**：`<名>.mp3` + `<名>.vtt`/`.en.vtt`/`.zh.vtt`。
  PotPlayer 打开 MP3 会自动挂上同名字幕，右键即可显示/隐藏。
- **页面只有 0.5 KB**：每段素材的 HTML 只是个壳子，CSS 与 JS 全站共享一份
  （否则 500 段各内嵌一份样式，光是重复内容就有好几 MB）。
- **数据用 `.js` 而不是 `.json` 加载**：`<script src="data/catalog.js">` 在 `file://` 下能正常加载，
  而 `fetch`/`XMLHttpRequest` 读本地 `.json` 会被浏览器的同源策略拦掉。
  所以**双击本地文件打开页面也能听到声音**，不需要起本地服务。
- **时间轴由音频决定**：`duration = 音频字节数 ÷ 6000`（edge-tts 是 CBR，实测精确成立）。
  有了 ffmpeg 时还会用真实时长校准一次。

## 规模

| 素材量 | 页面总体积 | 索引+台词 | 音频 |
|---|---|---|---|
| 5 段 | 2.5 KB | 12.8 KB | 1.9 MB |
| 500 段 | 250 KB | 约 1 MB | 约 190 MB |

---

## 表达库与编稿体检（2026-10-09 新增）

### `sources/phrases.json` —— 表达库（一等公民）

每条表达记录 `id / en / zh / layer(L0|L1|L2) / level(core|extra) / target / note`。

段落通过 `phrases` 字段引用表达 id。**允许写成 `p010:extra`**，表示「这条表达在本段降级为 ○」——
全局 `level` 是默认值，每段的 ★ 核心表达因此能被压到 3 个以内（硬指标）。

编稿顺序是**反的**：先定这段要复现哪几个表达，再写台词把它们嵌进去。
`build.py` 会把实际出现位置聚合进 `data/phrases.js`，页面据此显示「已出现 N 次」与「也出现在 0006 / 0009」。

### 编稿体检（`build.py` 构建时自动跑）

硬指标不达标直接列进「硬指标未达标」；复现类指标为警告。判据见 `PLAN.md` §4 / §6。

| 类别 | 指标 |
|---|---|
| 时长 | 每段 ≤120s |
| 句法 | 平均句长 5–9.5 词（**只统计 ≥3 词的完整句**，Okay./Me. 这类应声句不算句）、短句(<8 词)占比 ≥50% |
| 口音 | 每段印度英语特征 ≥1（按「句」匹配，only / right? 等模式依赖句尾标点，所以切句时保留标点） |
| 用词 | 判负词表命中 = 0 |
| 重点 | 每段 ★ 核心表达 1–3 个 |
| 复现 | 平均复现次数、只出现 1 次占比、出现 ≥3 次占比、复现不足清单 |

baseline 系列（旧 5 段教科书体素材）不计入评分，只作对照。

### 目录布局（域优先）

```
sources/dialogues.json     唯一源头：场次 + 分组 + 逐句中英文本 + 表达引用
sources/phrases.json       表达库
tools/gen_tts.py           配音 + 3 份 VTT，回写时间轴（支持 doc/item 级 voiceOf 固定音色）
tools/build.py             生成索引与页面 + 跑体检
data/catalog.js            索引（含 series / domain / part / stage / premise / 解析后的 phrases）
data/talks.js              全部台词与时间轴
data/phrases.js            表达库 + 实际出现位置
audio/<域>/<编号>-<名>/     每段一文件夹：mp3 + 3 份 vtt + 0.5KB 壳页
```

**同一角色跨段固定音色**：在段落里写 `voiceOf: {"Sam": "en-IN-PrabhatNeural"}`。
en-IN 男声只有 Prabhat 一个，4 人会议必须靠 `voiceOf` 混入 en-GB / en-US 才不会撞声。
