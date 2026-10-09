## ThinkFromHere 0.2.51

- CLI 账号模式连接本机共享 Codex 后台，历史读取与续聊使用同一后台版本；独立账号登录继续使用私有服务。
- 修复导入会话分支失败后，再次发送会静默丢失原始上下文的问题，并保留服务器原始错误。
- 断开仅关闭本应用连接，取消仅针对本应用任务，不停止共享后台或干预其他客户端审批。
- 保留退出应用时请求中断本应用任务的行为；后台停止状态无法确认时明确提示。

- 补齐导入分支失败和共享后台提示的英文翻译。

## English

- Connect CLI accounts and history readers to the shared local Codex daemon while keeping independent account sessions isolated.
- Prevent silent context loss when sending again after an imported session fork fails, and preserve the original server error.
- Disconnect only the app's connection, interrupt only its tasks, and leave other clients' approvals untouched.
- Keep interruption requests on app exit and report when backend termination cannot be confirmed.

- Add missing English translations for imported fork failures and shared daemon notices.

iOS ZIP 为模拟器应用，不是真机安装包。
The iOS ZIP is a simulator app, not an iPhone installation package.

下载 / Download: https://www.thinkfromhere.ai/downloads/

源码提交 / Source revision: `926bc6bb2ac4481edee3994535128b128d4a7983`.
