## ThinkFromHere 0.3.1

- Claude Code 连续多轮复用进程，减少重复启动开销；从旧卡片继续时按消息检查点建立独立分支。
- 远程电脑和手机可看到工具执行的具体命令、描述及完成状态。
- 修复长回复和长思考内容被截断后停止实时更新的问题，持续显示最新内容。
- Claude 未返回可见思考文字时仍保留思考面板，并明确显示空内容提示。
- 支持同一电脑上的开发版与正式版共享 Claude 会话，恢复已验证的连接，并同步执行耗时。
- 改善 Claude 排队输入与刚启动的远程会话操作，Agent 引擎选择中优先显示 Codex。

## English

- Reuse the Claude Code process across consecutive turns; preserve independent branches using message checkpoints when continuing from older cards.
- Show tool commands, descriptions and execution status on remote computers and phones.
- Keep long answers and reasoning previews updating after snapshot truncation.
- Keep the Claude reasoning panel visible with an explicit placeholder when no visible reasoning is returned.
- Share Claude sessions between development and release instances on the same computer, restore verified connections and synchronize turn duration.
- Improve queued input and actions on newly started remote Claude sessions; list Codex first in the engine selector.

包含 Windows x64、macOS universal、Linux deb/tar.gz、Android APK 和 iOS 模拟器包，以及 SHA-256 校验文件。
iOS ZIP 仅适用于模拟器，不是 iPhone 真机安装包。

Download: https://www.thinkfromhere.ai/downloads/

Source revision: `34e2cefeae0f10447b2114d53128adf9291be6fb` (main).
