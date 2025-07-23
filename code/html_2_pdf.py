#coding:utf-8

from utils import list_files_only
#from util_pdf import process_html_files

from xhtml2pdf import pisa
from io import BytesIO

def html_to_pdf(html_path, pdf_path):
    with open(html_path, 'r', encoding='utf-8') as html_file:
        html = html_file.read()

    result_file = open(pdf_path, "wb")

    # 转换为 PDF
    pisa_status = pisa.CreatePDF(
        html,
        dest=result_file,
        encoding='utf-8'
    )

    result_file.close()
    return not pisa_status.err

# 指定最终输出的 PDF 文件名
output_pdf = "combined_output.pdf"
path = "../output_data/one_rec/"
files = list_files_only(path)
#process_html_files(path+files, path+output_pdf)


# 使用示例
print(path+files[0])
html_to_pdf(path+files[0], 'output.pdf')

print('finish')