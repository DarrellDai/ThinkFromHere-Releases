# ForkChat Downloads

ForkChat 是一款“对话即流程图”的 AI 分支对话应用，支持桌面与 Android。

## 下载

前往 [Latest Release](https://github.com/DarrellDai/ForkChat-Releases/releases/latest)
下载对应平台的安装包：

- Windows x64：`ForkChat-*-windows-x64.exe`
- Linux x64（Debian / Ubuntu / Mint）：`ForkChat-*-linux-amd64.deb`
- macOS（Intel + Apple Silicon）：`ForkChat-*-macos-universal.dmg`
- Android 7.0 及以上：`ForkChat-*-android.apk`

Linux 安装命令：

```bash
sudo apt install ./ForkChat-*-linux-amd64.deb
```

Android 下载后，请允许浏览器或文件管理器“安装未知应用”，再打开 APK 安装。
Android 首版支持本地画布、分支聊天、Provider 和长期记忆；账号/云同步与附件尚未接入。

## 安全提示

当前安装包尚未购买代码签名证书。Windows 可能显示 SmartScreen 提示；macOS
首次打开时，需要在“系统设置 → 隐私与安全性”中选择“仍要打开”。
Android APK 使用项目固定的发布密钥签名，可由后续版本直接覆盖升级。

Release 中提供 SHA-256 校验信息；Android 另附同名 `.sha256` 文件。
