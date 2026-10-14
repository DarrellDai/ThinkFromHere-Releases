## ThinkFromHere 0.4.0

- 分支长期记忆支持来源节点与版本追踪；修正和遗忘只影响当前分支，分叉只继承所选节点之前的记忆，不带入后续节点或兄弟分支。
- Codex 与 Claude Code 接入分支记忆，并关闭 App 会话中的原生共享自动记忆；每轮刷新当前分支的记忆快照。
- 改善 Codex、Claude 的线性续聊与历史节点分叉，核验会话末端后复用已有会话；记忆开关变化时刷新会话配置。
- 输入框跟随正在阅读的卡片；Activity 新回复保持在顶部；画布缩略图支持点击和轻触定位；用户消息按纯文本显示。

遗忘长期记忆不会删除已有聊天文字，也不会回滚工作目录中的文件。建议电脑与手机同步升级。

## English

- Versioned branch memory inherits only the selected ancestor path. Corrections and forgetting stay within the current branch, excluding later turns and sibling branches.
- Codex and Claude Code use the same branch memory with fresh context on each turn; native shared automatic memory is disabled for app sessions.
- Reuse verified session tips for linear continuations and fork historical checkpoints; refresh configuration when memory settings change.
- Keep the composer aligned with the selected card, place new Activity replies first, support click/tap minimap navigation, and render user messages as plain text.

Forgetting long-term memory does not erase existing chat history or restore workspace files. Update desktop and mobile together.

包含 Windows x64、macOS universal、Linux deb/tar.gz、Android APK 和 iOS 模拟器包，以及 SHA-256 校验文件。
iOS ZIP 仅适用于模拟器，不是 iPhone 真机安装包。

Download: https://www.thinkfromhere.ai/downloads/

Source revision: 5f1bcd33766fe178d8fd4ff26de63c889a1d5a6b (main).
