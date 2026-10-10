## ThinkFromHere 0.2.55

- 缺少 Codex standalone 版时，可在应用中一键安装；若已有 npm 版，会明确说明区别并保留原 npm 安装。
- 修复 standalone 安装后缺少后台服务或残留更新记录导致的连接失败，支持一键修复并自动连接。
- 安装、修复和连接过程显示滚动进度条。
- 精简错误提示并遵循应用语言设置，移除会话下方重复的内部错误详情。
- 在应用外卸载 standalone 后，重新识别安装状态，避免继续显示过期的修复提示。

## English

- Install the required Codex standalone edition from the app, with a clear explanation when an npm installation already exists. Existing npm installs are preserved.
- Repair missing background service packages and stale updater records, then reconnect automatically.
- Show an animated progress bar during installation, repair and connection.
- Use concise errors in the selected app language and remove duplicate internal diagnostics below sessions.
- Refresh setup status after standalone is removed outside the app.

包含 Windows x64、macOS universal、Linux deb/tar.gz、Android APK 和 iOS 模拟器包，以及各安装包的 SHA-256 校验文件。
The release includes Windows, macOS, Linux, Android and iOS simulator packages with SHA-256 checksums.

iOS ZIP 仅适用于模拟器，不是 iPhone 真机安装包。
The iOS ZIP is for the simulator only.

下载 / Download: https://www.thinkfromhere.ai/downloads/

Source revision: `f82e356157ddbfa83e89ca7a28f19ad41023f046`.
