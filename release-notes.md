修复检查更新因 GitHub API 匿名额度耗尽而返回 HTTP 403 的问题。

- 桌面端和 Android 改为读取公开静态更新清单，检查更新不再使用 GitHub Releases API，也不需要用户配置 Token。
- 安装包继续通过 GitHub Releases 下载，并保留 SHA-256 校验。
- 发布完成后自动刷新更新清单；安装包或校验文件不完整时保留上一份清单。
- 修复删除卡片后通知残留的问题。

旧版客户端仍使用原更新接口。若已经遇到限流，请先从本发布页手动安装 0.2.37，后续更新检查将使用静态清单。

包含 Windows x64、macOS universal、Linux x64 DEB / TAR.GZ、Android 正式签名 APK，以及仅供 macOS 模拟器使用的 iOS ZIP；各附 SHA-256 校验文件。

源码版本：DarrellDai/ThinkFromHere 的 1e07a45dee98fa3c0fdcbfe452e3799f233bf9e8（0.2.37）。
