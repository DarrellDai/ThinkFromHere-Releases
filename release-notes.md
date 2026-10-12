## ThinkFromHere 0.3.9

- 修复启动恢复后的中断状态未上传：执行电脑确认任务被应用退出中断后，更新同步版本并上传正确状态，避免云端持续显示运行中。
- 保护本机仍在执行的任务，不让其他设备同步来的“应用退出中断”错误覆盖实时输出或触发 Codex 停止；正常远程停止仍然有效。
- 补充桌面与手机启动恢复、执行归属和同步回归测试。

重启后自动继续任务仍需在执行电脑的设置中开启，且依赖退出时成功保存恢复记录；本版不保证断电或强制结束进程后的自动恢复，也不会自动重新启动已中断的历史任务。

## English

- Synchronize locally confirmed startup interruptions with a fresh revision so cloud views no longer remain stuck on running.
- Prevent startup-interruption errors synced from another device from overwriting live local output or stopping Codex; explicit remote Stop remains supported.
- Extend regression coverage for startup recovery, local execution ownership, and synchronization.

Automatic task resumption must be enabled on the execution computer and requires a recovery record saved on exit. This release does not guarantee recovery after power loss or forced termination, and does not automatically restart historical interrupted tasks.

包含 Windows x64、macOS universal、Linux deb/tar.gz、Android APK 和 iOS 模拟器包，以及 SHA-256 校验文件。
iOS ZIP 仅适用于模拟器，不是 iPhone 真机安装包。

Download: https://www.thinkfromhere.ai/downloads/

Source revision: 6d21af663249efd15ec6c444e4a87f6b45ad77ed (main).
