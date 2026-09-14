# ThinkFromHere Downloads

ThinkFromHere 是一款“对话即流程图”的 AI 分支对话应用，支持桌面、Android 与 iOS。

## 当前版本

- Windows x64：ThinkFromHere Desktop 0.1.43 EXE
- macOS Intel + Apple Silicon：ThinkFromHere Desktop 0.1.43 Universal DMG
- Linux x64：ThinkFromHere Desktop 0.1.43 DEB / TAR.GZ
- Android 7.0 及以上：ThinkFromHere 0.1.44 Release APK
- iOS：ThinkFromHere 0.1.44 未签名模拟器 ZIP

## 本次更新（Desktop 0.1.43 / Mobile 0.1.44）

- Codex 执行中 Enter 追加：等待并入时单独显示，确认并入后才加入卡片正文并移除提示。
- Ctrl+Enter 排队到下一轮，自动生成子卡片并沿用同一 Session；Esc 停止执行。
- 附件旁新增 Fast 与 Goal；Goal 使用聊天框内容，不指定 token 预算，发送成功后关闭本次开关。
- 新卡片布局避让已有卡片；共享 Session 的卡片删除时保护仍被引用的会话。
- Android 与 iOS 保持 0.1.44。

## 上次更新（Desktop 0.1.42 / Mobile 0.1.44）

- 导入 Codex Session 时继承可读取的模型、权限模式和思考程度；无法准确继承的自定义权限需手动选择，不修改 CLI 全局设置。
- 已有 Session 固定使用原工作目录，在输入框上方以只读方式显示完整路径。
- 英文模式默认画布标题使用英文。
- 修复 Linux 更新器生成的 TryExec 路径引号导致 GNOME 隐藏应用入口的问题。
- Linux 更新安装后等待点击“立即重启”，防止旧启动器误回滚新版本。
- Android 与 iOS 保持 0.1.44。旧更新器存在入口或重启问题时，请手动安装新版一次；已生成的错误个人入口仍可能需要移除 TryExec 引号。

## 上次更新（Desktop 0.1.41 / Mobile 0.1.44）

- Codex 历史按轮次与消息分页读取，支持忽略大小写的会话标题搜索；转换画布保留原轮次用于续聊。
- 工作目录默认使用上次目录，没有记录时使用 Home；修复目录登记失效及下拉选项为空的问题。
- 修复重复启动时窗口早于同步接口注册的问题；更新下载显示真实百分比，安装显示阶段及动态进度条。
- 对话结束或需要输入时支持内容通知和提示音，可分别关闭；隔离 Warp 终端通知环境变量。
- Android 与 iOS 保持 0.1.44。旧 Linux 更新器若仍报应用文件缺失，请手动安装新版一次。

## 上次更新（Desktop 0.1.40 / Mobile 0.1.44）

- Chat / Codex 提问弹窗作为可选功能，默认关闭；支持选项和自由回答，2 分钟未回答自动跳过，不影响权限审批。
- Codex 工作目录在会话开始时选择一次并记住上次选择，后续仅在首个节点显示；调整 Session 入口位置，删除重复状态。
- Codex 附件支持任意文件和文件夹路径，粘贴图片仍作为图片发送；菜单增加图标并修复文字逐字换行。
- Android 与 iOS 保持 0.1.44。

## 上次更新（Desktop 0.1.39 / Mobile 0.1.44）

- 修复英文模式下 Codex Session 导入、同步、代理与错误提示中的中文，以及历史占位文字；会话正文保持原样。
- Codex 每轮回复末尾显示执行耗时，支持中英文；导入历史使用原始耗时，缺少可靠记录时不显示。
- 同一已完成方框支持并行 fork，无需等待子分支结束。上下文独立，Codebase 文件仍共享；并行修改同一文件可能互相覆盖。
- 沙盒和审批设置不变。Android 与 iOS 保持 0.1.44。

## 上次更新（Desktop 0.1.37 / Mobile 0.1.44）

- 将已有 Codex Session 导入为可继续对话的 Canvas，按原轮次保留分支上下文。
- 导入后绑定原 Session，隐藏重复导入入口；当前画布每 10 秒及切回应用时读取外部更新，保留本地分支和删除记录。
- 支持保存 Codex 代理配置并重连，改善 403 错误提示；优化浅色模式对比度，不再每轮显示 Ready。
- Android 与 iOS 本次保持 0.1.44 不变。

## 上次更新（Desktop 0.1.36 / Mobile 0.1.44）

- 桌面本地数据库与附件加密；支持复用 Codex CLI 登录、只读查看已有会话。
- 修复 Ubuntu Codex 路径识别、Linux 更新安装，以及 macOS 通用包的原生模块打包；下载和安装均显示进度。
- 旧版 Linux 若自动更新仍失败，请手动下载安装本次版本。Android 与 iOS 本次保持 0.1.44 不变。

## 上次更新（Desktop 0.1.34 / Mobile 0.1.44）

- 桌面端新增 Codex Agent 模式，可连接本机 Codex CLI 与账号，在聊天框内选择 Codex 模型和推理强度，并把每个方框作为独立执行分支。
- Agent 会展示推理说明、命令与文件操作进度；停止、异常断连和审批都有明确终态，已生成内容会保留，工作区也会安全释放。
- 默认仅允许工作区写入并按需审批，也支持只读与显式确认后的完全访问。Codex Agent 当前仅支持桌面端，移动端会稳定拒绝误发的 Agent 请求。

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
