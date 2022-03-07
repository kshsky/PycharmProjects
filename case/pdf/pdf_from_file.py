import pdfkit
from datetime import datetime

# option 是匹配 html标签的内容的
options = {
    # --disable - smart - shrinking         不使用智能收缩策略
    # --enable - smart - shrinking          使用智能收缩策略(这是默认设置)
    '--disable-smart-shrinking': True,
    '--title': '[title]',  # 展示 h1、h2、h3等各级标题作为大纲
    '--page-size': 'Letter',
    '--encoding': "UTF-8",
    '--minimum-font-size': 14,
    # '--header-left':pub,#页眉左边,
    # '--header-right':'我是右边页眉',#页眉右边，添加页码,
    '--footer-right': '[page]/[toPage]',  # 页脚右边，添加页码,
    # '--header-line':'--header-line', #添在页眉下方显示一条直线分隔正文
    # '--header-spacing':'5' #页眉与正文之间的距离(默认为零)
}
config = pdfkit.configuration(wkhtmltopdf=r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
name='SVM'
file_in_path=r'C:\Users\87754\Downloads\{}.html'.format(name)
file_out_path=r'F:\PDF\机器学习\ipynb_pdf\{}.pdf'.format(name)

start = datetime.now()
# pdfkit.from_string(body, file_name, options=options, configuration=config)
pdfkit.from_file(file_in_path, file_out_path, options=options, configuration=config)
end = datetime.now()

print('pdf文件生成完成，用时 {} 秒'.format(end - start))
