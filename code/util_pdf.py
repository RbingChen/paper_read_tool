

# 安装依赖：pip install PyPDF2 pdfplumber

import PyPDF2
import pdfplumber

# 使用 PyPDF2 提取文本
def extract_text_pypdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = []
        for page in reader.pages:
            text.append(page.extract_text())
        return text

# 使用 pdfplumber 提取文本（支持复杂排版）

def extract_text_pdfplumber(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = []
        for page in pdf.pages:
            text.append(page.extract_text())
        return text

# 示例
#print(extract_text_pypdf("example.pdf"))





