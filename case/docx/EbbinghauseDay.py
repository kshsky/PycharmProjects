from docx import Document
from docx.shared import Pt,RGBColor
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Cm
from docx.oxml.ns import qn
import datetime

weekdayDict={1:'MO',2:'TU',3:'WE',4:'TH',5:'FR',6:'SA',7:'SU'}

#设置单元格宽度
def set_col_widths(table,width_list):
    table.autofit = False
    for row in table.rows:
        for idx, width in enumerate(width_list):
            table.columns[idx].width = width
            row.cells[idx].width = width

def set_font(doc):
    # 设置正文字体
    doc.styles['Normal'].font.size = Pt(11)
    doc.styles['Normal'].font.name = u'宋体'
    doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
    doc.styles['Normal']._element.rPr.rFonts.set(qn('w:ascii'), 'Calibri')

path=r'C:\Users\87754\OneDrive\文档\document\work'
now = datetime.date(2022,6,23)
#当天之后，第1，2，4，7，15，30，90 天复习
delta_list=[0,1,2,4,7,15,30,90,180]
savename='{}/{}.docx'.format(path,now.strftime('%Y-%m-%d'))
repeat=[]

for i in delta_list:
    delta = datetime.timedelta(days=i)
    next = now+delta
    nextstr=next.strftime('%Y-%m-%d')
    repeat.append(nextstr)

print(repeat)

doc = Document()

set_font(doc)
p = doc.add_paragraph()
learn='python-docx 例子代码'

row_num=len(delta_list)
col_num=5

repeat=[]

week=[]
for i in delta_list:
    delta = datetime.timedelta(days=i)
    next = now+delta
    weekday = next.isoweekday()
    week.append(weekdayDict[weekday])
    nextstr=next.strftime('%Y-%m-%d')
    repeat.append(nextstr)

table = doc.add_table(rows=row_num,cols=col_num,style='Table Grid')
col_width_list=[Cm(6),Cm(0.6),Cm(2.8),Cm(1),Cm(4)]
#设置单元格宽度
set_col_widths(table,col_width_list)

for i in range(row_num):
    row = table.rows[i]
    row.cells[0].text=learn
    row.cells[1].text=str(i+1)
    row.cells[2].text=repeat[i]
    row.cells[3].text=week[i]

doc.save(savename)