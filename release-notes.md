## ThinkFromHere 0.4.5

- 修复 Codex、Claude 删除卡片时被其他运行任务误拦截的问题；删除分支不会要求停止保留分支。
- 正在使用的共享会话记录延后清理，保留其他分支的上下文和运行状态，并支持重启后继续清理。
- 修复 Codex 独立上下文校验中的空字段误报，以及桌面端 Claude 完成通知。
- 已通过 8 个真实对话场景、46 轮对话验证，以及 231 项回归测试和类型检查。

## English

- Fix card deletion being blocked by other running Codex or Claude tasks. Retained branches can continue running.
- Defer cleanup of shared session history until it is safe, preserve surviving branch context, and resume cleanup after restart.
- Fix optional-field validation when preserving Codex history and restore desktop Claude completion notifications.
- Verified with 46 real conversation turns across 8 scenarios, 231 regression tests, and type checks.

包含 Windows x64、macOS universal、Linux deb/tar.gz、Android APK 和 iOS 模拟器包，以及 SHA-256 校验文件。
iOS ZIP 仅适用于模拟器，不是真机安装包。

Download: https://www.thinkfromhere.ai/downloads/

Source revision: ade6038bb296d0172d38715b2d0890b2dce60839 (main).
