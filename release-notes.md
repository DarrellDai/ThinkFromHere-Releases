## ThinkFromHere 0.2.39

- Goal 右侧新增通用 @ 入口，可引用文件、文件夹、已安装应用、技能、MCP 工具和浏览器，支持搜索、多选及移除。
- 修复应用列表因远程发现超时而出现 “Could not load Apps” 的问题，优先读取已安装且可调用的应用。
- 桌面端内置 Playwright MCP 浏览器连接支持；通过浏览器扩展连接 Chrome 或 Edge。
- 修复开发模式默认浏览器登录配置，开发版与发布版使用独立回调。
- 继续提供自有域名下载和 SHA-256 校验；Android APK 与桌面安装包同步到香港下载镜像。

@ 引用目前用于本地 Codex 新消息；远程会话和运行中的任务暂不支持。
浏览器连接需要安装相应扩展并由用户选择授权标签页。
iOS ZIP 为模拟器应用，不是可安装到 iPhone 的发行包。

下载：https://www.thinkfromhere.ai/downloads/

全部六类安装包来自源码提交 `a7fcd9b0719108efdefcd62d7ca971c4bd71281f` 的 CI 构建。
