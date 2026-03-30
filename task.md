# 任务状态: 规则库版本同步计划 [PLAN]

## 🎯 业务目标
实现本地系统规则集 (`RULE[user_global]`) 与 `IDE-Multi-Agent-Protocol` GitHub 仓库的自动化/半自动化同步，并确保护航机制（双锁确认）到位。

## 📋 任务流水
- [x] **[P0] 环境核实 & 备份**:
    - [x] 基准：当前规则版本（含 S1-S3 协议、双锁模式、Agent 路由表、MCP 协作协议）。
    - [x] 备份：创建新的 Git 分支 `feature/sync-latest-rules`。
- [x] **[P1] 文件同步更新**:
    - [x] 覆盖：`Global_Rule_Template.md` → 采用最新的系统规则。
    - [ ] 校验：检查 `README_zh.md` 中的引导性文字是否与新规则冲突或过时。(经初步核查暂无冲突)
- [x] **[P2] 打包推送**:
    - [x] 合规：Git Commit (无夸大、事实驱动)。
    - [x] 推送：GitHub 远程推送完成。
    - [ ] 最终合入：(建议手动完成或由我执行 merge)

## 🛠️ 技术选型
- **流程规范**: 严格执行 S1-S3 咨询协议。
- **工具链**: `write_to_file` & `git`。

## ⚠️ 风险控制
1. **防止丢失**: 推送前先 `git commit` 保存本地状态。
2. **文本冲突**: 确保 `RULE[user_global]` 块在 `Global_Rule_Template.md` 中被完整、高质量地替换。
