## ThinkFromHere 0.5.1

- 改善 Android Chat 后台运行和返回前台时的响应：生成期间启用前台服务，后台输出合并更新，避免逐片刷新拖慢页面。
- 改善手机跨设备消息同步：优先上传新消息，历史附件补齐为新消息让路，删除记录同步失败时保留已确认的进度。
- 修复 Codex 停止、完成和追加输入的竞态，限制流式界面的积压，改善停止按钮与账号切换的响应。
- 改善 Activity 任务导航、通知显示时机、小窗口详情工具栏及面板滑动手势，并减少重复云端故障提醒。

包含 Windows x64、macOS Intel / Apple Silicon、Linux x64 / ARM64（deb、tar.gz）、Android APK 和 iOS 模拟器 ZIP，共九种安装包及对应 SHA-256 校验文件。
iOS ZIP 仅适用于模拟器，不是真机安装包。Android 后台运行不包含强制关闭 App 后继续生成。

下载：https://www.thinkfromhere.ai/downloads/

Source revision: bce0b5bf36d21f7d6851c1b6873124cb58cae874。
