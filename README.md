# ForkChat Downloads

ForkChat 是一款“对话即流程图”的 AI 分支对话应用，支持桌面与 Android。

## Android 0.1.6 测试版

[直接下载 APK](https://raw.githubusercontent.com/DarrellDai/ForkChat-Releases/gh-pages/downloads/ForkChat-0.1.6-android-debug.apk)

- Android 7.0 及以上
- 文件大小约 27 MB
- Debug 签名
- SHA-256：`84df67c161c97cb4e27808fe008bc091ad97794fc1db1f5c23256215c40a0776`

当前版本支持本地画布、分支聊天、智能画布命名、Provider、长期记忆、删除撤销，
以及与桌面端共用账号的双向云同步。用户添加的 API Key 也可以同步，下载到手机后由
Android Keystore 加密保存，且不会在界面回显。现在还内置 DeepSeek，无需用户填写
API Key；手机端点击方框时会同时显示详情和底部输入框，不再需要额外点击“从这里继续聊”。

下载后，请允许浏览器或文件管理器“安装未知应用”，再打开 APK 安装。如果旧版使用不同
签名，Android 不允许直接覆盖；请先完成云同步或备份重要本机数据，再决定是否卸载旧版。

## 正式发布

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

## 安全提示

当前安装包尚未购买代码签名证书。Windows 可能显示 SmartScreen 提示；macOS
首次打开时，需要在“系统设置 → 隐私与安全性”中选择“仍要打开”。
正式 Android APK 使用项目固定的发布密钥签名，可由后续版本直接覆盖升级；本页
0.1.6 测试包使用 Debug 签名，不保证能覆盖其他签名的安装包。

Release 中提供 SHA-256 校验信息；Android 另附同名 `.sha256` 文件。
