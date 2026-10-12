## ThinkFromHere 0.3.8

- 图片生成新增明确的输入与输出关系记录，只折叠有记录的修订图，保留独立图片；旧卡片没有关系记录时不猜测隐藏。
- 修复 Claude 图片在卡片正文与历史回复中被误拦截，完善图片保存位置与嵌入指引。
- 改进通知关闭按钮，移除提醒折叠控件。

## English

- Record explicit image input/output relationships and fold only recorded revisions, preserving independent images and legacy images without provenance.
- Fix blocked Claude image previews in current and historical replies, and clarify where to save and how to embed image deliverables.
- Clarify notification close buttons and remove reminder collapse controls.

图片关系记录需更新执行端与浏览端，并在后续生成中产生；旧图片不会自动补录关系。
包含 Windows x64、macOS universal、Linux deb/tar.gz、Android APK 和 iOS 模拟器包，以及 SHA-256 校验文件。
iOS ZIP 仅适用于模拟器，不是 iPhone 真机安装包。

Download: https://www.thinkfromhere.ai/downloads/

Source revision: 599575e7b8db58db9da8bd0ec49450afcdae398a (main).
