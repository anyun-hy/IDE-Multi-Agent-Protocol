---
description: 新对话接收握手令牌后，切换角色、恢复上下文、加载 Skill
---

# /switch 角色切换

## 1. 解析握手令牌
从用户粘贴的内容中提取以下字段：
- `@role` — 目标角色（Researcher / Writer / Engineer / Office）
- `@project` — 关联项目（可选）
- `@task` — 具体任务描述
- `@context` — 上下文恢复指令

## 2. 恢复上下文
// turbo
调用 `load_context(@role)` 从 MCP 数据库中读取该角色的上次快照。
如果返回"未找到存档"，则作为全新角色启动，跳过此步。

## 3. 加载专家 Skill
根据 @role 读取对应的 Skill 文件：

| @role | Skill 路径 |
|:---:|:---:|
| Researcher | `~/.agent/skills/research/SKILL.md` |
| Writer | `~/.agent/skills/academic/SKILL.md` |
| Engineer | `~/.agent/skills/java-engineer/SKILL.md` |
| Office | `~/.agent/skills/office/SKILL.md` |

使用 `view_file` 工具读取对应 SKILL.md，按其中的规范和流程开展工作。

## 4. 汇报就绪
向用户确认：
- ✅ 角色已切换为 {角色名}
- ✅ 上下文已恢复（或：全新启动）
- ✅ Skill 已加载
- 📋 当前任务：{@task}
- 🚀 准备开始工作

## 5. 开始执行
以对应角色的身份，按 @task 开始执行。
工作过程中遵循 MCP 协作协议：关键决策调用 `record_decision()`，需要历史信息调用 `recall_memories()`。
