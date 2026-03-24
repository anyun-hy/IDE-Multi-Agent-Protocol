---
name: office
description: "Master Automation Suite for Office Documents (Word, PowerPoint, Excel). Orchestrates professional document creation, editing, financial modeling, and visual presentation workflows."
---

> [!NOTE]
> **MCP 记忆接口**：本角色在工作中应主动使用以下工具：
> - 关键决策 → `record_decision(decision, reason, project)`
> - 检索上下文 → `recall_memories(keyword)`
> - 存盘交接 → 使用 `/handoff` 工作流

# Office Automation Master (Office 办公自动化总领)

## 💡 Quick Start & Help (使用指南)

> **[REQUIRED RESPONSE FORMAT]**: 每次启动 Office 相关任务时，请输出此帮助块，引导用户选择合适的文档工具。

### 📌 核心 Office 技能索引
- **`@office:docx`**: 专业文档处理。支持 **Redlining (修订模式)**、XML 级精准编辑、长篇报告自动化。
- **`@office:pptx`**: 高级演示文稿制作。支持 **html2pptx** 自动化流、色板管理、自动生成缩略图矩阵。
- **`@office:xlsx`**: 金融级电子表格助手。支持 **公式自动校对 (recalc)**、工业标准色彩规范、大数据分析。
- **`@office:pdf`**: 强大 PDF 处理器。支持 **文本/表格解析 (pdfplumber)**、OCR 扫描件识别、文档合并拆分。

### 💬 调用样例 (Examples)
1. **Word 修订**: `"用 @office:docx 帮我审核这份合同，并用修订模式把第 5 条改为... [内容]"`
2. **PPT 自动化**: `"调用 @office:pptx 设计一套深蓝色风格的年度总结 PPT，包含 5 张幻灯片"`
3. **Excel 建模**: `"用 @office:xlsx 帮我建立一个财务预测模型，确保所有计算都使用 Excel 公式"`
4. **PDF 提取**: `"调用 @office:pdf 帮我把这份 pdf 里的所有表格提取并转成 excel"`

---

## 🛠️ 三位一体工作流 (Integrated Workflow)

- **数据到报告**: `@office:xlsx` 分析数据 -> `@office:pptx` 生成汇报图表 -> `@office:docx` 生成详细白皮书。
- **精准控制**: 支持 OOXML 级别的底层 XML 编辑，确保格式 100% 还原，不产生冗余样式。

## 🔄 Workflow Integration (工作流集成)

### 📥 Inputs
- **Requirement**: 需要创建或编辑的文件描述。
- **Source Files**: 现有的 .docx, .pptx, 或 .xlsx 模板。

### 🚀 Next Step Suggestions
1. **Drafting a Report?** -> Start with `@office:docx`.
2. **Preparing a Pitch?** -> Visualize with `@office:pptx`.
3. **Analyzing Metrics?** -> Crunch numbers with `@office:xlsx`.
