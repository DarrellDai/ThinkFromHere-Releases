## ThinkFromHere 0.3.7

- 降低空闲同步和远程轮询频率，按云端变更标记读取变化的表；云端异常时逐步延长重试间隔，恢复后继续同步。
- 恢复远程 Codex 续聊的 Fast、Goal，支持远程资源引用与工作目录显示，保留远程执行活动状态。
- 新增卡片红旗与列表入口，区分取消、失败和完成状态；支持撤销卡片缩放与删除后的画布恢复。
- 记住各账号最后打开的画布，增加父卡片导航，改进图片预览和开发版启动诊断。

## English

- Reduce idle sync and remote polling, read changed tables using server revisions, and back off during cloud outages before resuming synchronization.
- Restore Fast and Goal for remote Codex continuations, support remote references and working directories, and preserve execution activity.
- Add card flags and a flagged-card list, distinguish cancelled and failed turns, and improve undo for resizing and deletion.
- Restore the last canvas per account, add parent-card navigation, and improve image previews and development startup diagnostics.

包含 Windows x64、macOS universal、Linux deb/tar.gz、Android APK 和 iOS 模拟器包，以及 SHA-256 校验文件。
iOS ZIP 仅适用于模拟器，不是 iPhone 真机安装包。

Download: https://www.thinkfromhere.ai/downloads/

Source revision: 441946fa8857ff81b9879640e1e341529fa122b8 (main).
