## ThinkFromHere 0.2.50

- 修复手机或查看端重启时，将仍在远程电脑执行的 Codex 任务误标为“应用退出导致中断”的问题。
- 远程会话运行中可保存模型、权限和推理强度设置，当前轮次结束后生效。
- 减少远程指令转交和确认的等待时间。
- 记住画布视角和侧栏状态；动态显示运行中任务。
- 改进系统通知，音量和静音设置独立保存在每台设备。
- 修复 Linux 打开生成文件后一直显示忙碌的问题。

## English

- Preserve running remote Codex tasks when a phone or viewing app restarts, avoiding false app-closed interruption errors.
- Save remote model, permission and reasoning settings during an active turn and apply them after that turn completes.
- Reduce remote command handoff and confirmation latency.
- Restore canvas viewport and sidebar state, and show running tasks in Activity.
- Improve system notifications and keep volume and mute preferences local to each device.
- Fix Linux generated-file opening remaining stuck in a busy state.

iOS ZIP 为模拟器应用，不是真机安装包。
The iOS ZIP is a simulator app, not an iPhone installation package.

下载 / Download: https://www.thinkfromhere.ai/downloads/

源码提交 / Source revision: `36b6af9` (tag `v0.2.50`).
