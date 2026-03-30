import sys
import argparse
import subprocess
import os

try:
    import docx
    from docx.shared import Pt, Cm, RGBColor
    from docx.oxml.ns import qn
    from docx.enum.text import WD_ALIGN_PARAGRAPH
except ImportError:
    print("[错误] 未找到 python-docx 模块。请在终端运行: pip install python-docx")
    sys.exit(1)

CONFIG = {
    # 字体配置 (Strict Western/EastAsia Split)
    "font_ascii": "Times New Roman",
    "font_eastAsia": "宋体",
    
    # 物理字号定义 (Units: Pt)
    "size_title": 18,  # 小二 (18pt)
    "size_normal": 12, # 小四 (12pt)
    "size_h1": 16,     # 三号 (16pt)
    "size_h2": 15,     # 小三 (15pt)
    "size_h3": 14,     # 四号 (14pt)
    "size_h4": 12,     # 小四 (12pt)
    
    # 页面版式 (A4 standard: 21.0 x 29.7 cm)
    "margin_top": 2.5,
    "margin_bottom": 2.5,
    "margin_left": 3.0,
    "margin_right": 2.5,
    
    # 段落排版
    "line_spacing": 1.5,
}

def run_pandoc(input_md, output_docx):
    """调用 Pandoc 执行初步架构映射"""
    print(f"[引擎执行] 正在调度底层 Pandoc 进行无损结构渲染: {input_md}")
    cmd = [
        "pandoc",
        input_md,
        "-o", output_docx,
        "--standalone" # 支持 YAML Frontmatter/Title 转换
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("[引擎执行] Pandoc 结构生成成功，YAML 元数据与复杂组件已注入。")
    except subprocess.CalledProcessError as e:
        print(f"[错误] Pandoc 初始化失败: {e.stderr.decode('utf-8')}")
        sys.exit(1)
    except FileNotFoundError:
        print("[错误] 环境未检测到 pandoc 指令。")
        sys.exit(1)

def apply_styles(docx_path):
    """接管 Word 原生底层，执行样式精修"""
    print(f"[引擎执行] 正在执行高级样式覆写与对齐偏置修正...")
    doc = docx.Document(docx_path)
    
    # 1. 页面边距硬写
    for section in doc.sections:
        section.top_margin = Cm(CONFIG["margin_top"])
        section.bottom_margin = Cm(CONFIG["margin_bottom"])
        section.left_margin = Cm(CONFIG["margin_left"])
        section.right_margin = Cm(CONFIG["margin_right"])
        
    # 2. 正文库 (Normal) 系统级更新
    if 'Normal' in doc.styles:
        style = doc.styles['Normal']
        style.font.name = CONFIG["font_ascii"]
        style.font.size = Pt(CONFIG["size_normal"])
        style.paragraph_format.line_spacing = CONFIG["line_spacing"]
        style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        style.paragraph_format.first_line_indent = Pt(CONFIG["size_normal"] * 2) # 首行缩进两字宽
        
        rPr = style._element.get_or_add_rPr()
        fonts = rPr.get_or_add_rFonts()
        fonts.set(qn('w:eastAsia'), CONFIG["font_eastAsia"])

    # 3. 文档总标题 (Title) 特修
    if 'Title' in doc.styles:
        t_style = doc.styles['Title']
        t_style.font.name = CONFIG["font_ascii"]
        t_style.font.size = Pt(CONFIG["size_title"])
        t_style.font.color.rgb = RGBColor(0, 0, 0)
        t_style.font.bold = True
        t_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        t_style.paragraph_format.first_line_indent = Pt(0)
        
        rPr = t_style._element.get_or_add_rPr()
        fonts = rPr.get_or_add_rFonts()
        fonts.set(qn('w:eastAsia'), CONFIG["font_eastAsia"])
        
    # 4. 大纲标题 (Heading 1-4) 左对齐修复
    heading_sizes = {
        'Heading 1': CONFIG["size_h1"],
        'Heading 2': CONFIG["size_h2"],
        'Heading 3': CONFIG["size_h3"],
        'Heading 4': CONFIG["size_h4"]
    }
    
    for style_name, size in heading_sizes.items():
        if style_name in doc.styles:
            h_style = doc.styles[style_name]
            h_style.font.name = CONFIG["font_ascii"]
            h_style.font.size = Pt(size)
            h_style.font.color.rgb = RGBColor(0, 0, 0)
            h_style.font.bold = True
            h_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            h_style.paragraph_format.first_line_indent = Pt(0)
            
            rPr = h_style._element.get_or_add_rPr()
            fonts = rPr.get_or_add_rFonts()
            fonts.set(qn('w:eastAsia'), CONFIG["font_eastAsia"])

    # 5. 图片与图注：探测、对齐及加固
    for p in doc.paragraphs:
        is_caption_or_figure = False
        
        # 判定是否属于图注/图片块
        if p.style is not None and (p.style.name.startswith('Caption') or p.style.name.startswith('Figure') or 'Image' in p.style.name):
            is_caption_or_figure = True
            
        if p._element is not None and p._element.xml is not None:
            if any(tag in p._element.xml for tag in ['graphicData', 'w:drawing', 'pic:pic']):
                is_caption_or_figure = True
                
        if is_caption_or_figure:
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.first_line_indent = Pt(0) # 剥夺缩进，确保位于物理中心

        # 样式补全：强制去除标题中可能残余的蓝色
        if p.style is not None and (p.style.name == 'Title' or p.style.name.startswith('Heading')):
            for run in p.runs:
                run.font.color.rgb = RGBColor(0, 0, 0)

    # 6. 图片物理比例缩放 (防止撑破页边距)
    available_width = Cm(21.0 - CONFIG["margin_left"] - CONFIG["margin_right"])
    for shape in doc.inline_shapes:
        if shape.width > available_width:
            aspect_ratio = shape.height / shape.width
            shape.width = available_width
            shape.height = int(available_width * aspect_ratio)

    # 7. 全自动图注编号 (依据 Caption 特征前置)
    fig_count = 0
    for p in doc.paragraphs:
        if p.style is not None and ('Caption' in p.style.name or '图注' in p.style.name):
            if p.text.strip() and not p.text.startswith('图'):
                fig_count += 1
                prefix = f"图 {fig_count}： "
                if p.runs:
                    p.runs[0].text = prefix + p.runs[0].text
                else:
                    p.add_run(prefix)

    doc.save(docx_path)

def set_table_borders(table):
    """底层强制写入表格边框 (Table Grid 模拟) - OXML 兼容层"""
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    
    tbl = table._tbl
    tblPr = tbl.tblPr
    if tblPr is None:
        tblPr = OxmlElement('w:tblPr')
        tbl.insert(0, tblPr)
        
    tblBorders = tblPr.find(qn('w:tblBorders'))
    if tblBorders is None:
        tblBorders = OxmlElement('w:tblBorders')
        tblPr.append(tblBorders)
    
    border_names = ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']
    for border_name in border_names:
        old = tblBorders.find(qn(f'w:{border_name}'))
        if old is not None:
            tblBorders.remove(old)
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '4')   
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), '000000') 
        tblBorders.append(border)

def apply_table_fixes(docx_path):
    """表格专项版式修复模块"""
    doc = docx.Document(docx_path)
    for table in doc.tables:
        set_table_borders(table)
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    paragraph.paragraph_format.first_line_indent = Pt(0)
                    paragraph.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    for run in paragraph.runs:
                        run.font.name = CONFIG["font_ascii"]
                        run.font.size = Pt(CONFIG["size_normal"])
                        run.font.color.rgb = RGBColor(0, 0, 0)
                        rPr = run._element.get_or_add_rPr()
                        fonts = rPr.get_or_add_rFonts()
                        fonts.set(qn('w:eastAsia'), CONFIG["font_eastAsia"])
    doc.save(docx_path)

def main():
    parser = argparse.ArgumentParser(description="【@office - Universal】Markdown to DOCX High-Fidelity Engine")
    parser.add_argument("input", help="Input Markdown file path")
    parser.add_argument("-o", "--output", required=True, help="Output DOCX file path")
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        sys.exit(1)
        
    run_pandoc(args.input, args.output)
    apply_styles(args.output)
    apply_table_fixes(args.output)
    print("✅ High-fidelity conversion completed successfully.")

if __name__ == "__main__":
    main()
