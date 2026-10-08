## ThinkFromHere 0.2.40

- 修复多个提问同时出现时无法找回前面问题的情况：提问表单新增数量提示和问题切换列表。
- 切换问题时保留各自已填写的答案；回答或关闭一个问题不会移除其他问题。
- 表单收起时仍可切换问题，已结束的问题会显示状态。
- 包含启动时自动连接 Codex agent 的修复。

## English

- Added a question switcher and request count so earlier questions remain accessible when multiple requests are open.
- Draft answers are preserved when switching questions. Answering or closing one request leaves the others available.
- The switcher remains visible when the form is collapsed; ended requests are labeled.
- Includes the fix to automatically connect the Codex agent at startup.

iOS ZIP 为模拟器应用，不是真机安装包。
The iOS ZIP is a simulator app, not an iPhone installation package.

下载 / Download: https://www.thinkfromhere.ai/downloads/

全部六类安装包来自源码提交 `02e53f023700de99a5394130abecbc3f8ba9b947` 的 CI 构建。
All six packages are built by CI from source commit `02e53f023700de99a5394130abecbc3f8ba9b947`.
