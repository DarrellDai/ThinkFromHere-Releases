# ThinkFromHere Downloads

ThinkFromHere 是一款“对话即流程图”的 AI 分支对话应用，支持桌面、Android 与 iOS。

## 当前版本

- Windows x64：ThinkFromHere Desktop 0.1.30 EXE
- macOS Intel + Apple Silicon：ThinkFromHere Desktop 0.1.30 Universal DMG
- Linux x64：ThinkFromHere Desktop 0.1.30 DEB
- Android 7.0 及以上：ThinkFromHere 0.1.40 Release APK
- iOS：ThinkFromHere 0.1.40 未签名模拟器 ZIP

## 本次更新（Desktop 0.1.30 / Mobile 0.1.40）

- 桌面、Android 与 iOS 会持久保存并正确刷新 OAuth 会话，重启或令牌到期后不再反复登录。
- Android 应用内更新完成后会正确打开安装流程；移动端联网开关重新开启时立即显示完整启用状态。
- 从方框详情发送后会立即显示并跟随新子方框；iPad 横竖屏、宽屏与 Stage Manager 均保持当前详情。
- iPad、iPhone 与 Android 的附件菜单会按软键盘上方空间限高并滚动，所有附件选项都可访问。

本次版本加入应用内更新功能：应用启动和打开设置时会自动检查最新公开版本；桌面版会在
下载后验证安装包大小与 SHA-256，再打开系统安装器。Android 会打开新版 APK 下载，
iOS 当前仍提供未签名模拟器构建。

下载站会通过 GitHub Release API 自动读取最新的五个平台安装包和对应 SHA-256 文件，
即使静态回退链接尚未重新部署，也会优先显示最新公开版本。

## 下载

- [ThinkFromHere 下载站](https://darrelldai.github.io/ThinkFromHere-Releases/)
- [Latest Release](https://github.com/DarrellDai/ThinkFromHere-Releases/releases/latest)

## 安全提示

当前桌面安装包尚未购买代码签名证书。Windows 可能显示 SmartScreen 提示；macOS
首次打开时，需要在“系统设置 → 隐私与安全性”中选择“仍要打开”。

Android APK 使用项目固定的 Release 密钥签名，可由后续版本直接覆盖升级。iOS 文件为
未签名的模拟器构建，不能直接安装到 iPhone 真机。

Release 中每个安装包均提供同名 `.sha256` 校验文件。
