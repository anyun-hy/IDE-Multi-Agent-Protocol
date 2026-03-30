---
name: writing
description: "Use when writing paper sections: abstract, introduction, related work, methodology, experiments, or conclusion. Provides templates and guidance for each chapter."
---

# Academic Writing (写作阶段)

## Overview

论文的**核心撰写阶段**。逐章节完成论文内容，确保逻辑清晰、结构完整。

## 章节索引

| 章节 | 文件 | 核心要点 |
|------|------|---------|
| 摘要 | abstract.md | 背景-方法-结果-结论 四段式 |
| 引言 | introduction.md | 背景-问题-动机-贡献 |
| 相关工作 | related-work.md | 分类综述、对比定位 |
| 方法 | methodology.md | 问题定义-框架-细节 |
| 实验 | experiments.md | 设置-结果-分析-消融 |
| 总结 | conclusion.md | 贡献总结-局限-展望 |

---

## 📋 Abstract (摘要)

### 结构模板 (150-300词)

```
[背景] [1-2句] 研究领域的重要性和当前挑战
[问题] [1句] 具体要解决的问题
[方法] [2-3句] 提出的方法和关键创新
[结果] [2-3句] 主要实验结果和提升
[结论] [1句] 工作意义
```

### 英文Prompt

```
Generate an abstract for a scientific paper based on this information for: [PARAGRAPHS]
```

---

## 📖 Introduction (引言)

### 结构：倒三角模型

```
┌─────────────────────────────────┐
│       大背景：领域重要性          │
├─────────────────────────────────┤
│     当前方法及其局限性            │
├─────────────────────────────────┤
│   研究空白 (Gap Statement)       │
├─────────────────────────────────┤
│  本文动机与方法概述              │
├─────────────────────────────────┤
│ 贡献列表 (Contributions)         │
├─────────────────────────────────┤
│论文结构说明                      │
└─────────────────────────────────┘
```

### 英文Prompt

```
Come up with an introduction for the following research topic: [TOPIC SENTENCE]
```

```
Rewrite this paragraph as an introduction: [PARAGRAPH]
```

---

## 📚 Related Work (相关工作)

### 组织方式

1. **按方法类别分**：传统方法 → 深度学习方法 → 最新方法
2. **按问题分**：问题A相关 → 问题B相关
3. **按技术分**：技术A → 技术B → 技术C

### 英文Prompt

```
Conduct a literature review on [TOPIC SENTENCE] and provide review paper references.
```

```
Summarize the scholarly literature, including in text citations on [PARAGRAPHS].
```

```
Compare and contrast [THEORY1] and [THEORY2] in the context of [RESEARCH DOMAIN].
```

---

## 🔧 Methodology (方法)

### 结构模板

```
1. Problem Formulation (问题定义)
   - 输入输出定义
   - 符号说明
   - 优化目标

2. Overview (方法总览)
   - 整体框架图
   - 各模块关系

3. Module Details (模块细节)
   - 每个模块的设计动机
   - 具体实现
   - 公式推导

4. Training/Inference (训练/推理)
   - 损失函数
   - 训练策略
```

### 公式写作规范

- 首次出现的符号必须定义
- 公式编号连续
- 复杂公式注释各部分含义

### 英文Prompt

```
Create objectives and methodology for [TOPIC SENTENCE].
```

```
Write a detailed methodology for the topic: [TOPIC SENTENCE].
```

```
Analyze the strengths and weaknesses of this methodology: [PARAGRAPHS].
```

---

## 🧪 Experiments (实验)

### 标准结构

```
1. Experimental Setup
   - Datasets (数据集描述)
   - Baselines (对比方法)
   - Evaluation Metrics (评价指标)
   - Implementation Details (实现细节)

2. Main Results (主要结果)
   - 对比实验表格
   - 结果分析

3. Ablation Study (消融实验)
   - 模块有效性验证
   - 参数敏感性分析

4. Visualization (可视化)
   - 定性结果
   - 注意力/特征可视化
```

### 英文Prompt

```
Design an experiment that [ACTION].
```

```
Write a result section for the following paragraphs. Please write this in the third person. [PARAGRAPHS].
```

```
Discuss these results: [RESULT PARAGRAPHS].
```

---

## 🎯 Conclusion (总结)

### 结构模板

```
[贡献总结] 2-3句，概括主要工作和创新
[实验验证] 1-2句，主要实验结论
[局限性] 1句，诚实承认不足（可选）
[未来展望] 1-2句，后续研究方向
```

### 英文Prompt

```
Generate a conclusion for this: [PARAGRAPHS]
```

```
Give recommendations and conclusion for: [PARAGRAPHS]
```

```
Can you suggest 3 directions for future research on this topic: [PARAGRAPH]?
```

---

---

## 🔝 Top-Tier Journal Writing Playbook (顶刊写作心法)

### 1. The "Dehydration" Rule for Novelty (原创概念“脱水”法则)
- 发明原创专有名词（如 Spatially Clustered Imbalance, Spatial Siege）时，立刻在同一句或下一句使用纯粹的理工科公理或统计术语（如 spatial dependence, strongly autocorrelated）进行解释。

### 2. Posture of a Builder (从容的建设者姿态)
- 避免使用：`prove`, `validate`, `expose vulnerabilities` 等带有审判色彩的词。
- 优选使用：`provides empirical support for (为...提供经验支撑)`, `facilitates future studies (促进未来研究)`, `offers a more interpretable view (提供更具解释性的视角)`。

### 3. Outcome Focus: Deployment-Oriented (面向部署的落脚点)
- 遥感/地学论文的最终价值不仅仅是“打榜”，必须始终将实验结论与 `Application readiness (应用就绪度)` 或 `Deployment-oriented conditions (面向部署的条件)` 挂钩。

### 4. Rhythmic Flow & Breath (呼吸感与衔接)
- 减少分裂节奏的括号（如尽量不用 `(e.g., ...)`），改用 `such as` 等将实例无缝嵌入主干。
- Introduction 部分严禁堆砌具体参数（如 14 个模型、1853 平方公里），将其留给 Section 3 和 4。

---

## 🧬 Drafting with Style (风格化写作)

### 1. The "Kaiming Style" (Focus: Simplicity & Insight)

模仿 Kaiming He (ResNet, MAE) 的顶级写作风格。核心：**Logic > Fancy Words**。

**Style Profile:**
- **Simplicity**: "We do X." (No jargon overload)
- **Active Voice**: "We present...", "We observe..." (Confident)
- **Contrast**: "Existing methods do X. In contrast, we do Y."
- **Insight-driven**: Every sentences adds information, no fluff.

**Prompt:**

```
Rewrite the following text in the style of Kaiming He (ResNet/MAE authors):
- Use extremely simple, direct English (Subject-Verb-Object).
- Avoid passive voice ("It is proposed...") -> Use active voice ("We propose...").
- Focus on the *logic* of why this is better, not just listing features.
- If describing a problem, contrast it sharply with our solution ("In contrast, we...").
- Remove all fluff and "academic-sounding" filler words.

Text to rewrite:
[INSERT CONTENT]
```

### 2. General Style Transfer (通用模仿)

如果你有其他喜欢的 paper (e.g., Ashish Vaswani's Attention paper)，可以用这个：

```
Analyze the writing style of the following excerpt (focus on sentence structure, vocabulary, and tone):
[PASTE EXAMPLE TEXT]

Now, rewrite my content using this exact style:
[MY CONTENT]
```

---

## 🔗 Logical Connectivity (语篇衔接)

顶级论文的段落之间是“咬合”的。

### 1. Transition Tool (过渡语工具箱)

```
Analyze the transition between Paragraph A and Paragraph B:
[CONTENT A]
[CONTENT B]
- Is there a logical leap?
- Suggest 3 transition phrases to bridge them (e.g., "Building upon this...", "Contrary to the assumption that...", "To validate this conjecture...").
```

### 2. High-Impact Connectives (精选连接词)
- **Contrast**: *Notwithstanding*, *Conversely*, *On the contrary*.
- **Causality**: *Consequently*, *Hence*, *Thereby*, *In light of this*.
- **Emphasis**: *Notably*, *Crucially*, *Paradoxically*.

---

## 🖼️ Impactful Captions (图表标题)

Kaiming He 的原则：**Captions should be self-contained.** (不读正文也能看懂图)。

### 1. Caption Generator

```
Write a self-contained caption for a [FIGURE/TABLE] showing [RESULTS/ARCHITECTURE].
Requirements:
- First sentence: A declarative title (The "So-what").
- Body: Brief explanation of components, axes, or trends.
- Clarity: Define labels and symbols used in the graphic.
- Style: Mimic the MAE or ResNet caption style.
```

---

## 📏 Mathematical Rigor (数学严谨性)

### 1. Notation Consistency Check

```
Scan my Methodology section for mathematical notations:
- Create a Table of Notations (Symbol | Meaning).
- Identify any "Overloaded" symbols (same symbol for different meanings).
- Suggest more standard LaTeX symbols if necessary (e.g., calligraphic \mathcal{S} for sets).
```

---

## 📊 Logic Visualization (逻辑可视化)

使用 Mermaid 图表检查论文逻辑结构，发现潜在的逻辑断层。

### 1. Reverse Outline (逆向大纲)

生成章节级逻辑流向图，检查段落安排是否合理。

```
Analyze the provided paper draft/outline. 
Generate a **Mermaid flowchart (TD)** to visualize the reverse outline.
Nodes should be the main claim of each section/paragraph.
Edges should represent the logical transition (e.g., "leads to", "supports", "contrasts").
```

### 2. Argument Flow (论证地图)

检查核心贡献是否得到充分支持。

```
Create a **Mermaid mindmap** analysis of the paper's argumentation.
Root: Main Contribution
Branches:
1. Motivation (Why we do this?)
2. Methodology (How we do this?)
3. Evidence (Experiments supports contribution?)
4. Impact (Why it matters?)
Identify any weak branches where evidence is insufficient.
```

---

## 写作阶段检查清单
- [ ] 各章节逻辑连贯 (通过 Flowchart 验证)
- [ ] 核心贡献有强证据支撑 (通过 Mindmap 验证)
- [ ] 术语和符号全文统一
- [ ] 图表编号和引用正确
- [ ] 公式编号连续
- [ ] 参考文献格式统一

---

## � Workflow Integration (工作流集成)

### 📥 Inputs
- **From Discussion**: 需要一份明确的 Research Outline 或 Hypothesis。
  - *If missing*: Call `@academic:discussion` first.

### 📤 Output Artifact
本阶段结束后，你应该得到一份 **"Draft Manuscript"** (初稿)。

### 🔗 Cross-Reference
1. **Stuck on Ideas?** (卡文了？)
   - Call `@academic:discussion` to brainstorm specific sub-problems.
   - *Example: "I'm stuck on the motivation part, let's brainstorm some gap statements."*

2. **Finished a Section?** (写完一章？)
   - Call `@academic:polishing-deai` **IMMEDIATELY** to polish the draft while it's fresh.
   - *Example: "I just finished the Abstract, please polish it."*

3. **Logic Check Needed?** (逻辑检查？)
   - Use the **Logic Visualization** module in this skill to generate a Reverse Outline.


---

## �📚 参考文献 (References)

### 格式转换

```
Here are some bibliography items, please transform them into bibtex style.
```

```
Convert this [BIBLIOGRAPHY] from MLA to APA style.
```

```
Write this in standard Harvard referencing [PARAGRAPH]
```
