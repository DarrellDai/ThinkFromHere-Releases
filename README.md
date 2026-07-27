# ThinkFromHere Downloads

ThinkFromHere 是一款“对话即流程图”的 AI 分支对话应用，支持桌面、Android 与 iOS。

## 下载平台

下载页提供 Windows、macOS、Linux、Android 和 iOS 模拟器构建：

- Windows x64：ThinkFromHere 0.1.16 EXE 安装程序
- macOS Intel + Apple Silicon：ThinkFromHere 0.1.16 Universal DMG
- Linux x64：ThinkFromHere 0.1.16 DEB
- Android 7.0 及以上：ThinkFromHere 0.1.25 Release APK
- iOS：ThinkFromHere 0.1.25 未签名模拟器 ZIP

## Android 0.1.25

- Android 7.0 及以上
- 文件大小约 25 MB
- 项目固定 Release 密钥签名
- SHA-256：`a2d9f1d79bd19e6f267e8daa4143202c81a14a0329a037b0b5bd76f58f840728`

当前版本支持本地画布、分支聊天、智能画布命名、Provider、长期记忆、删除撤销，
以及与桌面端共用账号的双向云同步。用户添加的 API Key 也可以同步，下载到手机后由
Android Keystore 加密保存，且不会在界面回显。当前版本内置 OpenAI、Claude、豆包、
DeepSeek V4 和 GLM 5.2，无需用户填写 API Key。画布现在可以持续保存“深思”开关；
开启后会分开展示模型的推理内容与最终答案，关闭后国产模型会显式关闭隐藏思考，
避免长时间没有可见输出。OpenAI GPT-5+ 会显示推理摘要，Claude 4.5+/5 会显示
summarized thinking。豆包、DeepSeek V4 与 GLM 5.2 开启联网时会优先使用单次
Responses 流式搜索，在 WebView 流式连接不可用时仍会自动可靠回退。多个发布编号
会折叠为一个模型名称，模型列表只显示当前 Provider 的模型。火山公共目录中存在但当前
账号无法调用的旧模型不会再显示。手机端点击方框时会同时
显示详情和底部输入框，不再需要额外点击“从这里继续聊”。
首次启动默认使用系统语言；此后登录页和登录验证邮件跟随 App 内选择的语言。
默认登录入口已改用证书稳定的 Cloudflare Pages 域名，以兼容更多企业网络。
登录、云同步、附件和内置模型服务现在统一通过该入口访问，避免企业网络单独拦截
`*.supabase.co` 导致“同步失败”。
桌面 0.1.16 也会隔离无法由 Electron SafeStorage 解密的旧 API Key 密文：云端有副本时
自动重新加密恢复；无法恢复时只要求重新输入对应 Key，不再阻断画布和设置同步。
Galaxy Z Fold7 等折叠屏会根据当前窗口宽度自动切换布局：外屏点击方框显示全屏详情，
展开内屏后显示 Canvas 与详情双栏；边缘箭头可以隐藏或恢复画布列表。
带厂商命名空间的 OpenAI GPT-5+ 模型现在也能正确启用联网和深思，同时保留网关要求的
完整模型 ID。模型生成时，只要用户向上滚动详情就会立即暂停自动跟随；回到底部附近或
点击“↓”后恢复。发送按钮旁的快捷键提示已移除，按钮仍固定在输入框最右侧。
本次更新让 iOS 与 Android 的内置 OpenAI 目录也会刷新并缓存最新 GPT-5+ 模型；
目录请求失败时继续使用最后一次成功结果，不再退回只到 GPT-5.2 的旧列表。同步刷新、
快速终态和流式增量同时发生时，画布方框不再闪烁、消失或被空状态覆盖；深思内容框的
展开状态也会在当前轮与历史路径之间保持稳定。

下载后，请允许浏览器或文件管理器“安装未知应用”，再打开 APK 安装。当前 APK 使用项目
固定的 Release 密钥签名，后续正式版本可直接覆盖升级。

## iOS 0.1.25

当前发布的是未签名的 iOS 模拟器构建，只能在 macOS 的 iPhone Simulator 中运行，
不能直接安装到 iPhone 真机。真机安装仍需要 Apple Developer 签名与分发配置。
SHA-256：`57e2910dbd5d19703b7fe8b90cdb384d86527741d25a8adb22e22f895c454ef5`

Linux 0.1.16 的 DEB 包名、安装摘要、应用菜单、可执行文件和应用图标均已统一为
ThinkFromHere，并会在安装时替换旧的 `forkchat-desktop` 包。Windows 与 macOS 也使用
同一套 ThinkFromHere 图标资源。Ubuntu 安装时会刷新图标缓存，应用菜单与 Dock 都能
正确显示 Logo；启动时还会清理旧版重复创建的登录 URL Handler。桌面触摸板的两指滑动
现在用于平移画布，捏合与 Ctrl/Command + 滚动继续缩放。
登录流程中的“打开登录页”、成功和错误提示会跟随 App 内选择的语言，并在跳转系统
浏览器后继续保持该语言。

## 发布页

[Latest Release](https://github.com/DarrellDai/ThinkFromHere-Releases/releases/latest)
目前提供 Windows、macOS、Linux、Android 和 iOS 模拟器五个平台构建及 SHA-256 校验文件。

## 安全提示

当前安装包尚未购买代码签名证书。Windows 可能显示 SmartScreen 提示；macOS
首次打开时，需要在“系统设置 → 隐私与安全性”中选择“仍要打开”。
Android APK 使用项目固定的发布密钥签名，可由后续版本直接覆盖升级。

Release 中每个安装包均提供同名 `.sha256` 校验文件。
