## ThinkFromHere 0.2.46

- 收件箱改为「动态」：未读显示紫色点，查看后保留记录，新的动态排在最上面。
- 全局动态与每个 Canvas 显示未读数量；Canvas 卡片底部左侧显示时间，右侧使用固定大小的图标，未读为 0 时隐藏数字。
- 超过 200 条动态时，从最旧的已读记录开始清理；未读记录始终保留。
- 动态弹窗只保留列表滚动，标题与说明固定，修复双层滚动条。
- 已读状态持久保存，并支持跨设备同步。

## English

- Inbox is now Activity: purple dots identify unread entries, viewed entries remain in the list, and new activity appears first.
- Global and per-canvas unread counts. Canvas cards show the time on the left and a fixed-size activity icon on the right; zero counts are hidden.
- Above 200 entries, the oldest read entries are removed first. Unread entries are always retained.
- Activity uses a single scrolling list with a fixed header, eliminating nested scrollbars.
- Read states persist across restarts and sync across devices.

iOS ZIP 为模拟器应用，不是真机安装包。
The iOS ZIP is a simulator app, not an iPhone installation package.

下载 / Download: https://www.thinkfromhere.ai/downloads/

源码提交 / Source revision: `d878f79d1c68f4786fc5d713746f1315d0a1eadf`.
