---
name: polishing-deai
description: "Use when polishing paper language, reducing AI-generated text markers, improving academic expression, or ensuring natural human writing style. Combines polishing and de-AI functions."
---

# Academic Polishing & De-AI (润色与去AI化)

## Overview

论文的**质量提升阶段**。润色语言表达和消除AI写作痕迹是一体化流程，共同目标是让论文读起来**自然、专业、人性化**。

---

## 💎 语言润色

### 主要英文Prompt

```
Below is a paragraph from an academic paper. Polish the writing to meet the academic style, 
improve the spelling, grammar, clarity, concision and overall readability. 
When necessary, rewrite the whole sentence. 
Firstly, you should provide the polished paragraph. 
Secondly, you should list all your modification and explain the reasons to do so in markdown table.
```

### 输出格式：三行两列对照

| 原文 | [原始段落内容] |
| 问题 | [语法/表达/风格问题描述] |
| 修改 | [修改后的内容] |

### 语法检查Prompt

```
Help me ensure that the grammar and the spelling is correct. 
Do not try to polish the text, if no mistake is found, tell me that this paragraph is good. 
If you find grammar or spelling mistakes, please list mistakes you find in a two-column markdown table, 
put the original text the first column, put the corrected text in the second column 
and highlight the key words you fixed.
```

### 连贯性提升Prompt

```
Write a transition sentence to connect the following two paragraphs: [PARAGRAPH1] [PARAGRAPH2]
```

### 问题诊断Prompt

```
What 3 points would you suggest to improve this paragraph?: [PARAGRAPH]
```

```
Provide me a list of words and phrases which were repeatedly / more than 3 times used: [PARAGRAPHS]
```

### 常用学术表达替换

| 口语化 | 学术化 |
|--------|--------|
| a lot of | numerous / substantial |
| show | demonstrate / illustrate |
| get | obtain / acquire |
| use | utilize / employ |
| big | significant / considerable |
| good | effective / promising |
| bad | suboptimal / limited |

---

## 🔒 去AI化处理

### AI写作特征识别

**典型AI痕迹：**
- 过度使用连接词（Furthermore, Moreover, Additionally）
- 句式过于整齐、平行
- 措辞过于"完美"、缺乏个性
- 过度使用被动语态
- 缺少领域特定俚语/惯用表达
- 段落结构高度模式化

### 去AI化策略

#### 1. 打破模式化结构

```
将以下段落重写，打破其模式化结构：
[AI生成段落]

要求：
1. 变化句子长度（长短交替）
2. 减少连接词使用
3. 增加主动语态
4. 加入领域惯用表达
```

#### 2. 注入个人风格

```
以下是AI生成的内容，请改写使其更像人类写作：
[内容]

增加以下人类写作特征：
1. 偶尔的短句或省略
2. 个人观点表达（"We believe...", "Interestingly..."）
3. 不那么"完美"的表达
4. 领域内常见的表述习惯
```

#### 3. 变异策略清单

- [ ] 将3个连续"Moreover"替换为其他过渡
- [ ] 每段至少一个短句（<10词）
- [ ] 增加领域引用习惯（"As shown in [xx]"）
- [ ] 减少"However"、"Therefore"密度
- [ ] 加入数字和具体细节
- [ ] 适当使用括号补充说明

### AI检测工具验证

| 工具 | 网址 | 特点 |
|------|------|------|
| GPTZero | gptzero.me | 学术论文友好 |
| Originality.ai | originality.ai | 精度较高 |
| ZeroGPT | zerogpt.com | 免费使用 |

**验证流程：**
1. 初稿完成后检测
2. 标记高AI概率段落
3. 针对性重写
4. 再次检测验证

---

## 一体化润色流程

```
┌─────────────────┐
│   初稿完成       │
└────────┬────────┘
         ↓
┌─────────────────┐
│  AI检测初筛     │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 标记问题段落     │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 语言润色+去AI化  │
└────────┬────────┘
         ↓
┌─────────────────┐
│  再次AI检测     │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 人工复核调整     │
└─────────────────┘
```

---

## 综合提示词

```
请对以下学术论文段落进行润色和去AI化处理：

[段落内容]

处理要求：
1. 【语言润色】提升学术表达，使用专业术语
2. 【去AI化】打破模式化句式，增加人类写作特征
3. 【风格统一】保持与上下文风格一致
4. 【保留原意】不改变核心含义

输出润色后的段落，并列出主要修改点。
```

---

## 🛠️ Advanced De-AI Techniques (高级去 AI 味)

### 1. Sentence Variance Analysis (句子长短交替)

AI 往往喜欢写长度均匀的句子。

```
Analyze the sentence length and rhythm of this paragraph:
[CONTENT]
- Compute the "Word Count" per sentence.
- If they are too similar, rewrite the paragraph to follow the "Short-Long-Short" rhythm. 
- Use brief, punchy sentences for key findings.
```

### 2. Scientific Hedging (学术措辞分寸)

```
Adjust the 'Confidence Level' of the following claims:
[CLAIMS]
Options:
- [HEDGE]: Soften the claim (e.g., "This may suggest...", "Specifically in our context...").
- [ASSERT]: Strengthen the claim (e.g., "This confirms...", "Our results clearly demonstrate...").
- [NEUTRAL]: Objective reporting.
```

### 3. Specifics Injection (细节注入)

这是最有效的去 AI 方法：将抽象描述转化为具体观察。

```
Identify "Vague/Generic" phrases in the following text (e.g., "High efficiency", "Good results").
Replace them with placeholders for quantitative or specific data:
- e.g., "The model performed well" -> "The model achieved a [XX]% improvement on the [DATASET] test set."
- e.g., "Significantly faster" -> "Reduced inference time by [XX]ms per frame."
```

---

## ✅ 检查清单 (Polishing Checklist)

- [ ] AI检测得分低于阈值 (建议 < 20%)
- [ ] 句式长度有明显变化 (Sentence Variance)
- [ ] 逻辑衔接词不重复且准确 (Logical Connectives)
- [ ] 核心断言使用了正确的学术妥协语 (Hedging)
- [ ] 注入了具体的性能指标或观察细节 (Specifics Injection)
- [ ] 语法/拼写无误
- [ ] 符合目标期刊格式

---

## 🔄 Workflow Integration (工作流集成)

### 📥 Inputs
- **From Writing**: 需要一段或一章待润色的文本 (Draft Text)。

### 📤 Output Artifact
本阶段结束后，你应该得到一份 **"Polished Manuscript"** (定稿)。

### 🚀 Next Steps
1. **Ready to Submit?** (准备投稿？)
   - 恭喜！你的论文已经准备好了。
   - 如果收到审稿意见，请调用 `@academic:reviewer-response`。

2. **Logic Issues Found?** (发现逻辑问题？)
   - 如果润色过程中发现逻辑不通，不要强行润色。
   - Call `@academic:writing` 并使用 **Reverse Outline** 功能重构段落。
   - *Example: "This paragraph is confusing. Let's go back to writing mode to restructure it."*
