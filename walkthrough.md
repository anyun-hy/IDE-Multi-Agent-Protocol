# IMAP 规则同步工作流复盘 [PLAN]

## 🏗️ 动作回顾
1. **环境侦察**: 识别出 `Global_Rule_Template.md` 为核心同步目标。
2. **分支隔离**: 执行 `git checkout -b feature/sync-latest-rules`，确保 `main` 分支安全。
3. **精准注入**: 将 `RULE[user_global]` 全量同步至模板文件，引入 `S1-S3`, `Double-Lock` 及 `Manager 双核职责`。
4. **远程锚定**: 将变更推送至 GitHub。

## 🔍 核查状态
- [x] **Global_Rule_Template.md**: 已同步最新规则。
- [x] **task.md**: 已更新进度。
- [x] **Git Branch**: `feature/sync-latest-rules` 已推送到远端。
- [ ] **README 同步**: 经评估，`README_zh.md` 中的架构图及流程描述依然适用。

## 🏁 下一步建议
1. **合并主干**: 如果确认 feature 分支工作完美，可执行 `git checkout main && git merge feature/sync-latest-rules`。
2. **清理任务**: 合并后删除本地 `feature` 分支及辅助 `task.md`。

> [!TIP]
> 规则变更已生效在模板中，建议下次运行 `install.sh` 时或手动将内容同步至 IDE 的全局设置中。
