## ThinkFromHere 0.3.12

- 修复同机开发版与正式版之间的 Codex 会话状态恢复：执行端退出后，另一实例不再一直显示过期的“生成中”。
- 停止、追加消息和队列轮询前核验本机执行记录，避免把已结束的本地会话继续路由给离线实例。
- 从经过核验的本地线程记录恢复断开后完成的最终回复；仍在执行的任务不会被接管，未确认的停止不会被误报为成功。

## English

- Recover stale Codex conversation states across development and release instances on the same computer.
- Reconcile verified local execution records before stopping, adding live input, or polling queued messages.
- Restore final replies completed after the owning app disconnected, without taking over active tasks or reporting an unconfirmed stop as successful.

包含 Windows x64、macOS universal、Linux deb/tar.gz、Android APK 和 iOS 模拟器包，以及 SHA-256 校验文件。
iOS ZIP 仅适用于模拟器，不是 iPhone 真机安装包。

Download: https://www.thinkfromhere.ai/downloads/

Source revision: cc7740f2a5ee6eb60177319957dd26474e868e1b (main).
