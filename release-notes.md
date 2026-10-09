## ThinkFromHere 0.2.48

- 关闭最后一个窗口或更新重启时，保存正在运行的任务并停止执行；重新打开后自动继续原卡片。
- Codex 接回原线程发起续接轮次；Chat 根据原问题与已生成内容继续。手动取消或已经完成的任务不会自动恢复。
- 修复恢复任务后界面仍显示停止，以及关闭窗口时主进程出现 “Object has been destroyed” 的错误。
- 修复开发模式重启竞争和加载失败后的白屏恢复。
- 「动态」保留已读记录，未读显示紫色点，新条目置顶；全局与每个 Canvas 显示未读数量。
- 动态超过 200 条时优先清理最旧的已读记录，未读条目始终保留。

## English

- Save and stop running tasks when closing the last window or restarting for an update, then continue on the original cards after reopening.
- Codex continues in its original thread with a new turn; Chat continues from the original request and partial answer. Completed and manually cancelled tasks are not restarted.
- Fix resumed cards showing a stopped state and the main-process “Object has been destroyed” error on window close.
- Fix development restart races and improve recovery from failed window loads.
- Activity retains read entries, marks unread entries with purple dots, sorts newest first, and shows global and per-canvas unread counts.
- Above 200 activity entries, remove the oldest read entries first while retaining all unread entries.

任务恢复会发起新请求，并非恢复已终止的网络流；第三方工具的外部副作用不能保证精确断点续执行。
Task recovery issues a new request rather than resuming a terminated network stream; external tool side effects cannot be guaranteed to resume exactly once.

iOS ZIP 为模拟器应用，不是真机安装包。
The iOS ZIP is a simulator app, not an iPhone installation package.

下载 / Download: https://www.thinkfromhere.ai/downloads/

源码提交 / Source revision: `0c0b918a410e962f0cdf59c6d424ebab0d196957`.
