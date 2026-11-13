## ThinkFromHere 0.5.10

- 修复 Android 和 iOS 附件上传在 0% 立即报错（is not a constructor）的问题，保留真实上传进度与取消能力。
- 上传或发送准备失败时，明确提示指令尚未提交，不再误报电脑可能已开始执行。
- 防止某条远程指令准备卡住后阻塞电脑继续接单，保留原指令的迟到回执，避免重复执行。
- 修复后台同步巡检等待标准输入而超时的问题。
- 优化启动时会话历史快照处理，并修复远程提问附件和文件拖放。

远程功能建议手机与执行电脑同时更新。Android 正式安装包覆盖正式版，不覆盖独立的 ThinkFromHere Test。
提供 Windows x64、macOS Intel / Apple Silicon、Linux x64 / ARM64、Android 安装包及 SHA-256 校验文件。
iOS ZIP 仅用于模拟器，不可直接安装到 iPhone/iPad，也不是 App Store 发行包。

Source revision: b8ac92f56c46e2ebdb863e89a4ed20c37e4882dc
