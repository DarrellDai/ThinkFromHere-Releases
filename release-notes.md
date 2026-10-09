## ThinkFromHere 0.2.42

- Agent / Remote 与同步请求自动比较现有入口、Supabase 直连和香港中继，选择更快的健康线路；海外直连更快时可跳过香港。
- 网络故障后后续请求切换线路，选路层不会重复发送指令。
- 减少远程状态轮询等待和重复读取；合并同步回执查询，并行拉取独立数据，改善同步等待。
- 请将电脑与手机都更新到 0.2.42，以启用新版通信与同步优化。

## English

- Agent / Remote and sync requests compare the existing gateway, direct Supabase access, and the Hong Kong relay, selecting a faster healthy route. Faster direct connections can bypass Hong Kong.
- Subsequent requests switch routes after network failures. Routing never replays commands.
- Reduced remote polling delays and duplicate reads; combined receipt queries and parallel reads of independent sync data reduce waiting.
- Update both desktop and mobile to 0.2.42 to enable these communication and sync improvements.

iOS ZIP 为模拟器应用，不是真机安装包。
The iOS ZIP is a simulator app, not an iPhone installation package.

下载 / Download: https://www.thinkfromhere.ai/downloads/

源码提交 / Source revision: `c26db99398017cc485ba3a641f6859d1b3ffd6b1`.
