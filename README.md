# ThinkFromHere Downloads

ThinkFromHere 是一款“对话即流程图”的 AI 分支对话应用，支持桌面、Android 与 iOS。

## 当前版本

- Windows x64：ThinkFromHere Desktop 0.1.31 EXE
- macOS Intel + Apple Silicon：ThinkFromHere Desktop 0.1.31 Universal DMG
- Linux x64：ThinkFromHere Desktop 0.1.31 DEB
- Android 7.0 及以上：ThinkFromHere 0.1.41 Release APK
- iOS：ThinkFromHere 0.1.41 未签名模拟器 ZIP

## 本次更新（Desktop 0.1.31 / Mobile 0.1.41）

- 桌面端和 iPad 从方框详情发送后，会立即显示并跟随新生成的子方框，不再需要返回 Canvas 查找。
- Android 折叠窄屏与 iPhone 在详情中隐藏列表箭头；Android 展开屏与 iPad 保留列表入口，打开列表时不会关闭当前详情。
- 第一个根方框生成完成后不再显示紫色新内容边框；子方框仍保留完成提示。

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
