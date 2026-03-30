---
name: reviewer-response
description: "Use when receiving reviewer comments, drafting response letters, or preparing revision explanations. Guides point-by-point response strategy with professional and diplomatic tone."
---

# Academic Reviewer Response (审稿意见回复)

## Overview

论文的**修订反馈阶段**。收到审稿意见后，撰写专业、有礼、有据的回复信，并准备相应的修改说明。

---

## 🔍 Review Analysis & Visualization (审稿意见可视化)

在开始回复前，先将复杂的审稿意见转化为结构化图表，制定回复策略。

### 1. Review Mindmap (问题拆解脑图)

将所有审稿人意见分类，形成修改清单。

```
Analyze the provided Reviewer Comments.
Generate a **Mermaid mindmap** to categorize all issues.
Root: Review Summary
Branches:
 - Reviewer 1
   - Major Concerns (Critical)
   - Methodology
   - Experiments
   - Minor Fixes
 - Reviewer 2
   - ...
 - Reviewer 3
   - ...
```

### 2. Strategy Flowchart (回复策略流程)

针对棘手问题（如要求补大实验），设计决策流程。

```
For the major comment "[CRITICAL COMMENT]", generate a **Mermaid flowchart** to plan the rebuttal strategy.
Steps: 
1. Acknowledge value
2. Clarify misunderstanding (if any)
3. New Experiment results (or Theoretical proof)
4. Revision in manuscript
```

---

## 回复信结构

### 标准格式

```markdown
Dear Editor and Reviewers,

We sincerely thank you for the valuable comments and constructive suggestions. 
We have carefully considered each comment and revised our manuscript accordingly. 
Below, we provide our point-by-point responses.

---

## Response to Reviewer #1

### Comment 1.1
> [原文引用审稿意见]

**Response:** 
[回应内容]

**Revision:** 
[修改说明，标注位置]

---

### Comment 1.2
...

---

## Response to Reviewer #2
...

---

We hope our revisions adequately address the concerns raised. 
Thank you again for your time and expertise.

Sincerely,
[Authors]
```

---

## 回复策略

### 态度原则

| 原则 | 说明 |
|------|------|
| **感谢** | 每条意见先表示感谢 |
| **认同** | 承认合理的批评 |
| **解释** | 清晰说明修改或为何未采纳 |
| **证据** | 提供数据/引用支持 |
| **尊重** | 即使不同意也保持礼貌 |

### 常用开场句

```
• We thank the reviewer for this insightful comment.
• This is an excellent point that has helped improve our manuscript.
• We appreciate this constructive suggestion.
• We are grateful for this thorough review.
```

---

## 不同类型意见的回复模板

### 1. 技术质疑

```
> [Reviewer] Questions the validity of [method/claim]

**Response:**
We appreciate this rigorous technical evaluation. To address this concern:

1. [理论解释]: We clarify that...
2. [实验验证]: We have conducted additional experiments as shown in Table X...
3. [文献支持]: This approach has been validated in prior work [citation]...

**Revision:**
We have added clarification in Section X (Page Y, Line Z).
```

### 2. 补充实验要求

```
> [Reviewer] Requests additional experiments on [aspect]

**Response:**
Thank you for this valuable suggestion. We have conducted the requested experiments:

[新实验结果表格或描述]

The results demonstrate that [结论], which further validates our method.

**Revision:**
New results are added in Section X.X and Table Y.
```

### 3. 写作/表达问题

```
> [Reviewer] The writing in Section X is unclear.

**Response:**
We thank the reviewer for pointing this out. We have thoroughly revised this section for clarity.

**Revision:**
Section X has been rewritten (Page Y, Lines Z-W).
```

### 4. 无法完全采纳的意见

```
> [Reviewer] Suggests [建议内容]

**Response:**
We greatly appreciate this thoughtful suggestion. We have carefully considered it and provide the following explanation:

[解释为什么未完全采纳]

However, we have partially addressed this by [部分采纳的修改].

**Revision:**
[具体修改位置]
```

---

## 修改标注方式

### 方法一：颜色标注

```latex
% LaTeX中使用颜色标注修改
\usepackage{xcolor}
\newcommand{\revision}[1]{\textcolor{blue}{#1}}

% 使用方式
\revision{This is the revised text.}
```

### 方法二：Change Bar

```latex
\usepackage{changebar}

\begin{changebar}
Revised content here.
\end{changebar}
```

### 方法三：文字说明

```
Page 5, Lines 120-125: Revised to clarify...
Section 3.2, Paragraph 2: Added explanation of...
```

---

## 回复信生成 Prompt (英文)

### 生成完整回复信

```
Act as a professional academic researcher. Write a polite and diplomatic response letter to the reviewers.
Reviewer comments are provided below.
For each comment, please:
1. Express gratitude for the comment (use varied expressions).
2. Clearly state whether we agree or partially agree.
3. Explain how we have revised the manuscript (or why we cannot).
4. Point out the specific location of the revision (e.g., "See Section 3.2").

Reviewer comments:
[PASTE COMMENTS HERE]
```

### 生成单条回复 (针对性)

```
Write a response to the following reviewer comment.
Tone: Professional, Respectful, Confident but Humble.

Comment: "[COMMENT]"
My Explanation/Fix: "[EXPLANATION]"
```

---

## 🎭 Advanced Response Strategies (高级回复策略)

### 1. The Art of Concession (让步的艺术)

当必须承认局限性时，如何“转危为机”。

```
Draft a response to a reviewer's point about a limitation (e.g., "[LIMITATION]").
Strategy:
- Acknowledge: "We agree that [LIMITATION] is an important factor."
- Contextualize: "In our current study focus ([FOCUS]), this was... (e.g., out of scope / data unavailable)."
- Mitigate: "However, we have addressed this by [PARTIAL FIX / DISCUSSION]."
- Future-proof: "We have added this as a 'Future Work' direction in Section X."
```

### 2. Managing Conflicting Reviews (处理冲突意见)

当 Reviewer 1 让你往左，Reviewer 2 让你往右时。

```
Reviewer 1 suggests: [SUGGESTION 1]
Reviewer 2 suggests: [SUGGESTION 2]
Task: Synthesize a diplomatic solution.
- Find common ground (if any).
- Decide on the most scientifically sound path.
- Draft a response to both: "While Reviewer [X] suggested [A], Reviewer [Y] noted [B]. We have chosen [PATH] because [REASON], and added a discussion on [OTHER PERSPECTIVE] to satisfy both."
```

### 3. Rebuttal Strategy Matrix (反驳矩阵)

| 审稿意见 | 推荐策略 | 核心话术 |
252: | 创新点不足 | 差异化策略 | "Unlike [X], we solve [Y] by..." |
253: | 实验不全 | 补做或论证策略 | "We have added [Experiment Z]..." |
254: | 写作极差 | 彻底检查策略 | "The manuscript has been polished by..." |
255: | 拒绝修改 | 解释策略 | "While we value the suggestion, we..." |

---

## ✅ 回复检查清单 (Response Checklist)

- [ ] 每条意见都在 Response Letter 中有对应解析
- [ ] 针对重大质疑有数据支持 (Evidence-based)
- [ ] 即使是拒绝修改的意见，也给出了合理的逻辑解释 (Diplomatic Refusal)
- [ ] 处理了多位审稿人之间的潜在矛盾 (Conflict Resolving)
- [ ] 修改后的正文位置 (Page/Line) 与回复信一一对应
- [ ] 语法和格式无误
- [ ] 态度始终保持 Humble yet Confident

---

## 🔄 Workflow Integration (工作流集成)

### 📥 Inputs
- **From Journal**: 审稿意见邮件 (Reviewer Comments)。

### 📤 Output Artifact
本阶段结束后，你应该得到：
1. **Response Letter** (回复信)
2. **Revision Plan** (修改计划)

### 🚀 Next Steps
1. **Execute Revision** (执行修改):
   - 拿着 **Revision Plan**，回到 `@academic:writing` 阶段修改正文。
   - *Example: "According to the plan, I need to rewrite the Methodology. Let's switch to writing mode."*

2. **Polish Revision** (润色修改稿):
   - 修改完的正文，别忘了再次调用 `@academic:polishing-deai` 进行润色。
   - *Tip: Don't let the new parts look different from the old parts!*
