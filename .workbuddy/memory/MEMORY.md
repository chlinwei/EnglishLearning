# 项目长期记忆 — EnglishLearning

## 项目定位
英语学习项目，**专门记录 IT 相关英语**（非通用英语词典）。
范围：技术术语、开发/运维/产品工作场景用语、开源与技术社区表达、技术面试英语。

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
