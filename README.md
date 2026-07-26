# ThinkFromHere Downloads

ThinkFromHere 是一款“对话即流程图”的 AI 分支对话应用，支持桌面、Android 与 iOS。

## 下载平台

下载页提供 Windows、macOS、Linux 和 Android 安装包：

- Windows x64：ThinkFromHere 0.1.2 EXE 安装程序
- macOS Intel + Apple Silicon：ThinkFromHere 0.1.2 Universal DMG
- Linux x64：ThinkFromHere 0.1.2 DEB
- Android 7.0 及以上：ThinkFromHere 0.1.7 Release APK

## Android 0.1.7

- Android 7.0 及以上
- 文件大小约 25 MB
- 项目固定 Release 密钥签名
- SHA-256：`40d80cdfc2759195c841ab906d60b353ce754d05df790b24b31b4634932bbee6`

当前版本支持本地画布、分支聊天、智能画布命名、Provider、长期记忆、删除撤销，
以及与桌面端共用账号的双向云同步。用户添加的 API Key 也可以同步，下载到手机后由
Android Keystore 加密保存，且不会在界面回显。现在还内置 DeepSeek，无需用户填写
API Key；手机端点击方框时会同时显示详情和底部输入框，不再需要额外点击“从这里继续聊”。
Galaxy Z Fold7 等折叠屏会根据当前窗口宽度自动切换布局：外屏点击方框显示全屏详情，
展开内屏后显示 Canvas 与详情双栏；边缘箭头可以隐藏或恢复画布列表。

下载后，请允许浏览器或文件管理器“安装未知应用”，再打开 APK 安装。当前 APK 使用项目
固定的 Release 密钥签名，后续正式版本可直接覆盖升级。

## 发布页

[Latest Release](https://github.com/DarrellDai/ThinkFromHere-Releases/releases/latest)
目前提供 Windows、macOS、Linux 和 Android 四个平台的安装包及 SHA-256 校验文件。

## 安全提示

当前安装包尚未购买代码签名证书。Windows 可能显示 SmartScreen 提示；macOS
首次打开时，需要在“系统设置 → 隐私与安全性”中选择“仍要打开”。
Android APK 使用项目固定的发布密钥签名，可由后续版本直接覆盖升级。

Release 中每个安装包均提供同名 `.sha256` 校验文件。
