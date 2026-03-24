---
description: Manager 分析任务类型并生成 Agent 握手令牌，用于派发给新对话
---

# /dispatch 调度分析

## 1. 检查全局状态
// turbo
调用 MCP 工具 `get_project_status()` 和 `recall_memories()` 了解当前项目进度和最近决策。

## 2. 分析用户意图
根据用户描述的任务内容，参照以下路由表确定推荐角色：

| 任务关键词 | 推荐 Agent | Skill | @role |
|:---:|:---:|:---:|:---:|
| 模型/训练/实验/PyTorch/GPU/数据集/消融 | 🔬 Researcher | research | Researcher |
| 论文/写作/润色/审稿/引用/LaTeX/Abstract | 🎓 Writer | academic | Writer |
| Java/Spring/架构/数据库/API/后端/微服务 | ⚙️ Engineer | java-engineer | Engineer |
| Word/PPT/Excel/PDF/报告/文档/演示 | 📄 Office | office | Office |

如果任务涉及多个领域，拆分为多个子任务并为每个子任务推荐独立的 Agent。

## 3. 生成握手令牌
输出以下标准格式，供用户复制粘贴到新对话中：

```
[Agent 握手令牌]
@role: {角色名}
@project: {项目名，如适用}
@task: {具体任务描述}
@context: 请调用 load_context('{角色名}') 恢复上下文
```

## 4. 记录调度决策
// turbo
调用 `record_decision("派发 {角色名} 执行 {任务摘要}", "基于用户意图分析")` 留痕。

## 5. 提示用户
告知用户：请新建一个对话窗口，将上面的握手令牌粘贴进去，然后输入 `/switch` 即可启动对应角色。
