## ThinkFromHere 0.3.10

- 同步版本查询接口不可用时自动退回全量同步，五分钟后重试，避免旧中转接口返回 Not found 导致同步中断；鉴权和网络错误仍正常报告。
- 双击 Shift 打开搜索后立即聚焦输入框，可直接输入。
- 修复本地文件夹链接打开及错误提示，支持远程文件夹打包 ZIP 传输。
- 修复停止后未消费的追加消息在新卡片继续执行，并在活动回复旁展示用户提问。

## English

- Fall back to full synchronization when the revision endpoint is unavailable, then retry after five minutes. Authentication and network failures remain visible.
- Focus the search input immediately after opening search with a double tap of Shift.
- Fix local folder links and path errors, and transfer remote folders as ZIP archives.
- Continue unconsumed follow-ups on new cards after stopping, and show user prompts alongside activity replies.

包含 Windows x64、macOS universal、Linux deb/tar.gz、Android APK 和 iOS 模拟器包，以及 SHA-256 校验文件。
iOS ZIP 仅适用于模拟器，不是 iPhone 真机安装包。

Download: https://www.thinkfromhere.ai/downloads/

Source revision: 4febbe34201f58b9bb6e4686f28fbe0be1e70f97 (main).
