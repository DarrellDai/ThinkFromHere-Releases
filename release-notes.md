## ThinkFromHere 0.4.4

- 统一创建画布与卡片的模型名称：Codex 显示为 GPT 6.1 Sol，Claude 显示为 Opus 5.5。
- 修复未打开窗口账号的远程访问、远程请求超时和 Claude 模型列表加载阻塞。
- 修复未完成 Codex 会话分叉的上下文保留，以及过早或仅含推理内容的完成通知。
- 改善手机输入区和发送触控，调整 Activity 已读操作与数量显示。
- 移除空白卡片创建、卡片拆解与画布卡片上的回复复制按钮。

## English

- Use consistent model names in canvas creation and cards, including GPT 6.1 Sol and Opus 5.5.
- Restore remote access for accounts without open windows and bound remote requests and Claude catalog loading.
- Preserve context when branching unfinished Codex turns and suppress premature or reasoning-only completion notifications.
- Improve mobile composer touch handling and Activity read actions and counts.
- Remove blank-card creation, card decomposition, and response copy actions on canvas cards.

包含 Windows x64、macOS universal、Linux deb/tar.gz、Android APK 和 iOS 模拟器包，以及 SHA-256 校验文件。
iOS ZIP 仅适用于模拟器，不是真机安装包。

Download: https://www.thinkfromhere.ai/downloads/

Source revision: 3604eee18c18c46da26dcf99de918067c067bc2a (main).
