# ThinkFromHere Downloads

ThinkFromHere 是一款“对话即流程图”的 AI 分支对话应用，支持桌面、Android 与 iOS。

## 下载平台

下载页提供 Windows、macOS、Linux、Android 和 iOS 模拟器构建：

- Windows x64：ThinkFromHere 0.1.11 EXE 安装程序
- macOS Intel + Apple Silicon：ThinkFromHere 0.1.11 Universal DMG
- Linux x64：ThinkFromHere 0.1.11 DEB
- Android 7.0 及以上：ThinkFromHere 0.1.20 Release APK
- iOS：ThinkFromHere 0.1.20 未签名模拟器 ZIP

## Android 0.1.20

- Android 7.0 及以上
- 文件大小约 25 MB
- 项目固定 Release 密钥签名
- SHA-256：`22ef7fdb42abc61f89668e49d2a94a46ade50b5eebc8296b63eb81181008ea1a`

当前版本支持本地画布、分支聊天、智能画布命名、Provider、长期记忆、删除撤销，
以及与桌面端共用账号的双向云同步。用户添加的 API Key 也可以同步，下载到手机后由
Android Keystore 加密保存，且不会在界面回显。当前版本内置 OpenAI、Claude、豆包、
DeepSeek V4 和 GLM 5.2，无需用户填写 API Key；国产模型已支持逐段流式输出，并在
WebView 流式连接不可用时自动可靠回退，开启联网时会先执行实时检索。多个发布编号
会折叠为一个模型名称，模型列表只显示当前 Provider 的模型。火山公共目录中存在但当前
账号无法调用的旧模型不会再显示。手机端点击方框时会同时
显示详情和底部输入框，不再需要额外点击“从这里继续聊”。
首次启动默认使用系统语言；此后登录页和登录验证邮件跟随 App 内选择的语言。
默认登录入口已改用证书稳定的 Cloudflare Pages 域名，以兼容更多企业网络。
登录、云同步、附件和内置模型服务现在统一通过该入口访问，避免企业网络单独拦截
`*.supabase.co` 导致“同步失败”。
桌面 0.1.11 也会隔离无法由 Electron SafeStorage 解密的旧 API Key 密文：云端有副本时
自动重新加密恢复；无法恢复时只要求重新输入对应 Key，不再阻断画布和设置同步。
Galaxy Z Fold7 等折叠屏会根据当前窗口宽度自动切换布局：外屏点击方框显示全屏详情，
展开内屏后显示 Canvas 与详情双栏；边缘箭头可以隐藏或恢复画布列表。

下载后，请允许浏览器或文件管理器“安装未知应用”，再打开 APK 安装。当前 APK 使用项目
固定的 Release 密钥签名，后续正式版本可直接覆盖升级。

## iOS 0.1.20

当前发布的是未签名的 iOS 模拟器构建，只能在 macOS 的 iPhone Simulator 中运行，
不能直接安装到 iPhone 真机。真机安装仍需要 Apple Developer 签名与分发配置。
SHA-256：`4f797dbc8c185365a93aa8e7ebaa0fa4a2aa0e4add1887c536fb9c8c741d98d2`

Linux 0.1.11 的 DEB 包名、安装摘要、应用菜单、可执行文件和应用图标均已统一为
ThinkFromHere，并会在安装时替换旧的 `forkchat-desktop` 包。Windows 与 macOS 也使用
同一套 ThinkFromHere 图标资源。Ubuntu 安装时会刷新图标缓存，应用菜单与 Dock 都能
正确显示 Logo；启动时还会清理旧版重复创建的登录 URL Handler。桌面触摸板的两指滑动
现在用于平移画布，捏合与 Ctrl/Command + 滚动继续缩放。

## 发布页

[Latest Release](https://github.com/DarrellDai/ThinkFromHere-Releases/releases/latest)
目前提供 Windows、macOS、Linux、Android 和 iOS 模拟器五个平台构建及 SHA-256 校验文件。

## 安全提示

当前安装包尚未购买代码签名证书。Windows 可能显示 SmartScreen 提示；macOS
首次打开时，需要在“系统设置 → 隐私与安全性”中选择“仍要打开”。
Android APK 使用项目固定的发布密钥签名，可由后续版本直接覆盖升级。

Release 中每个安装包均提供同名 `.sha256` 校验文件。
