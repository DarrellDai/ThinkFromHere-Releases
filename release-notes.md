## ThinkFromHere 0.2.45

- 修复历史附件异常导致手机持续显示 Sync error、并阻断后续正常附件下载的问题；异常附件单独提示需要恢复，文字与其他附件继续同步。
- 修复已读状态和收件箱已同步完成后仍残留在待同步队列、持续显示 Sync pending 的问题。
- 同步错误、待同步原因和附件异常可点击展开查看，手机也能查看详情。
- 手机支持取消单条排队中的远程消息，不中断正在执行的回复；此功能需要电脑端也更新到 0.2.45。
- 修复手机滑动阅读时卡片选中状态不跟随可见位置的问题，兼容键盘和视口尺寸变化。

## English

- Damaged historical attachments no longer report a global mobile sync failure or block later healthy downloads. They are listed separately for recovery while text and other attachments keep syncing.
- Fixed stale read-receipt and Inbox queue entries that kept displaying Sync pending after their data had already synced.
- Sync errors, pending reasons, and attachment warnings now expand on tap, including on mobile.
- Mobile can cancel an individual queued remote message without interrupting the running reply. Update the desktop app to 0.2.45 as well to use this feature.
- Fixed card selection during mobile reading gestures, including keyboard and viewport changes.

iOS ZIP 为模拟器应用，不是真机安装包。
The iOS ZIP is a simulator app, not an iPhone installation package.

下载 / Download: https://www.thinkfromhere.ai/downloads/

源码提交 / Source revision: `90f70935a99d07d41f664c1bdfe2ec15d2f0b2c6`.
