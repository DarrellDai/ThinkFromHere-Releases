桌面版 0.2.14：Linux 更新授权诊断。

- Linux 系统更新失败时区分取消授权与授权或命令执行失败，并保留 pkexec 退出码、stderr、信号及桌面会话诊断。
- 错误信息提供诊断 JSON 的保存位置，不自动重复安装。
- 首次更新不弹密码窗口的根因仍在排查，本版不宣称已修复。诊断能力从运行 0.2.14 起生效，旧版本升级到本版时仍使用旧更新器。

提供 Windows x64、macOS universal、Linux x64（DEB / TAR.GZ），每个安装包附有 SHA-256 校验文件。Android 和 iOS 模拟器继续提供原有 0.2.13 安装包，未重新构建。

iOS ZIP 仅用于 macOS 的 iOS Simulator，不适用于 iPhone/iPad 真机安装。

[下载页面](https://darrelldai.github.io/ThinkFromHere-Releases/)
