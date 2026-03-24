---
name: academic
description: "Use when starting academic paper writing, needing guidance on writing workflow, or coordinating between different writing phases. Covers the complete lifecycle from topic selection to reviewer response."
---

> [!NOTE]
> **MCP 记忆接口**：本角色在工作中应主动使用以下工具：
> - 关键决策 → `record_decision(decision, reason, project)`
> - 检索上下文 → `recall_memories(keyword)`
> - 存盘交接 → 使用 `/handoff` 工作流

# Academic Writing Master (学术写作总领)

## 💡 Quick Start & Help (使用指南)

> **[REQUIRED RESPONSE FORMAT]**: 每次处理学术任务时，请先输出此帮助块，提醒用户可用的 Skills 和调用样例。

### 📌 核心技能索引
- **`@academic:discussion`**: 选题构思、研究空白、科学假设。
- **`@academic:writing`**: 各章节撰写、**Kaiming Style** 润色、逻辑可视化。
- **`@academic:polishing-deai`**: 深度语言优化、三栏对比、去 AI 化。
- **`@academic:reviewer-response`**: 处理审稿意见、博弈策略、修改说明。

### 💬 调用样例 (Examples)
1. **启动选题**: `"用 @academic:discussion 帮我分析 Mamba 在遥感领域的 Research Gap"`
2. **风格润色**: `"用 @academic:writing 的 Kaiming Style 润色这段开头：[内容]"`
3. **审稿回复**: `"调用 @academic:reviewer-response 帮我写这段 Rebuttal：[审稿意见]"`

---

## 概述

论文写作的**全流程指挥中枢**。统筹四大写作阶段，协调各模块调用，确保论文质量和进度。

## 论文写作生命周期

```
讨论阶段 → 写作阶段 → 润色去AI化 → 审稿回复
   ↓           ↓           ↓           ↓
选题构思    各章节撰写    语言优化     意见回应
题目关键词  结构组织      风格统一     修改说明
```

## 四大阶段索引

| 阶段 | Skill | 核心任务 |
|------|-------|---------|
| 🧠 讨论 | `academic:discussion` | 选题构思、题目关键词、研究假设 |
| ✍️ 写作 | `academic:writing` | 摘要、引言、相关工作、方法、实验、总结 |
| 💎 润色 | `academic:polishing-deai` | 语言润色、去AI化、学术风格 |
| 📝 回复 | `academic:reviewer-response` | 审稿意见逐条回应、修改说明 |

## 写作质量检查清单

### 投稿前检查
- [ ] 摘要是否完整覆盖 Background-Method-Result-Conclusion
- [ ] 引言是否清晰阐述 Gap → Motivation → Contribution
- [ ] 方法描述是否可复现
- [ ] 实验是否包含消融实验和对比实验
- [ ] 图表是否自解释（无需阅读正文即可理解）
- [ ] 参考文献格式是否统一
- [ ] 是否通过AI检测工具验证

### 语言检查
- [ ] 时态是否一致（方法用现在时，实验结果用过去时）
- [ ] 被动语态使用是否恰当
- [ ] 术语是否统一
- [ ] 句子是否简洁（避免冗长从句）

## 常见论文类型

| 类型 | 结构特点 | 字数参考 |
|------|---------|---------|
| **期刊论文** | 完整章节，深入分析 | 6000-10000词 |
| **会议论文** | 紧凑结构，突出创新 | 4000-8000词 |
| **短文(Letter)** | 精简，快速发表 | 2000-4000词 |

## 如何使用

1. **开始写作**：先调用 `academic:discussion` 确定选题和架构
2. **撰写初稿**：调用 `academic:writing` 逐章节撰写
3. **优化润色**：调用 `academic:polishing-deai` 提升质量
4. **收到审稿**：调用 `academic:reviewer-response` 准备回复

## 写作进度模板

```markdown
# [论文标题] 写作进度

## 目标期刊/会议: [名称]
## 截止日期: [日期]

### 进度追踪
- [ ] 选题确定 (预计: )
- [ ] 大纲完成 (预计: )
- [ ] 初稿完成 (预计: )
- [ ] 润色完成 (预计: )
- [ ] 投稿 (预计: )
```
