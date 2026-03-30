---
name: discussion
description: "Use when exploring research topics, identifying research gaps, generating hypotheses, crafting paper titles, or selecting keywords. The initial brainstorming phase before actual writing."
---

# 讨论阶段 (Discussion Phase)

## 概述

论文写作的**起点**。在动笔之前，充分讨论选题方向、研究空白、创新点和论文架构。

---

## 🎯 选题与构思 (Scientific Reasoning)

### 1. 研究空白识别 (Gap Identification)

不要只是列出空白，要找出“学术矛盾点”。

```
Based on the following literature summaries, identify the "Research Gap":
- What is the current "State-of-the-Art" (SOTA)?
- What is the critical bottleneck or unresolved contradiction?
- Why do existing methods fail in specific scenarios (e.g., [SCENARIO])?
- Format the output as a "Gap Statement" suitable for the Introduction section.
```

### 2. 假设生成 (Hypothesis Formulation)

将模糊的想法转化为可测试的科学命题。

```
Formulate a research hypothesis for the topic: [TOPIC].
Please provide:
- Null Hypothesis (H0): The default assumption.
- Alternative Hypothesis (H1): Our proposed contribution/expectation.
- Testable Variable: What exactly will be measured to prove/disprove this?
```

### 3. 贡献预览 (Contribution Analysis)

在动笔前验证研究价值。

```
Analyze the potential contributions of this idea: [IDEA]
1. Theoretical Contribution: (New insight, new formula, new framework?)
2. Practical/Empirical Contribution: (Better accuracy, faster speed, new dataset?)
3. Reviewer's Perspective: What would be the 3 most likely "Reasons to Reject" and how can we mitigate them now?
```

### 4. 跨领域创新与探索 (Cross-domain & Exploration)

```
Suggest 5 titles for the following abstract: [ABSTRACT PARAGRAPH]
```

```
Suggest novel applications of [TOPIC SENTENCE] within [RESEARCH DOMAIN]
```

---

## 📝 题目与关键词

### 标题生成

```
Suggest 5 titles for the following abstract: [ABSTRACT PARAGRAPH]
```

### 主题句撰写

```
Write a topic sentence for this paragraph: [PARAGRAPH]
```

### 关键词提取

```
Provide 5 keywords for this: [PARAGRAPHS]
```

---

## ✅ 讨论阶段检查清单

- [ ] 研究问题是否明确
- [ ] 研究空白是否真实存在
- [ ] 创新点是否清晰
- [ ] 假设是否可验证
- [ ] 标题是否准确反映内容
- [ ] 关键词是否覆盖核心概念

---

## 🔄 Workflow Integration (工作流集成)

### 📤 Output Artifact
本阶段结束后，你应该得到一份 **"Research Proposal & Outline"**。

### 🚀 Next Steps
1. **Proceed to Writing**: 
   - 既然大纲已定，请调用 `@academic:writing` 开始撰写 Introduction 或 Methodology。
   - *Prompt: "Based on the outline we just discussed, let's start writing the Introduction section."*

2. **Iterate**:
   - 如果觉得选题不够新颖，请留在本阶段继续使用 "Research Gap" prompt 进行挖掘。
