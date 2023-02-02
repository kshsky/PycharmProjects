from docx import Document
from docx.shared import Pt,RGBColor
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Cm
from docx.oxml.ns import qn
import datetime
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
#纵向转横向
from docx.enum.section import WD_ORIENT


'''

学习当天	第1次	第2次	第3次	第4次	第5次	第6次	第7次
07-01-FR	①07-02-SA	②07-03-SU	③07-05-TU	④07-08-FR	⑤07-16-SA	⑥07-31-SU	⑦09-29-TH
07-02-SA	①07-03-SU	②07-04-MO	③07-06-WE	④07-09-SA	⑤07-17-SU	⑥08-01-MO	⑦09-30-FR

'''

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
    doc.styles['Normal'].font.size = Pt(12)
    doc.styles['Normal'].font.name = u'宋体'
    doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
    doc.styles['Normal']._element.rPr.rFonts.set(qn('w:ascii'), 'Courier New')


def get_repeat_date(date):
    # 当天之后，第1，2，4，7，15，30，90 天复习
    delta_list = [0, 1, 2, 4, 7, 15, 30, 90]
    repeat_list=[]
    date = datetime.datetime.strptime(date,'%Y-%m-%d')
    for i in delta_list:
        repeat = date + datetime.timedelta(days=i)
        weekday = repeat.isoweekday()
        repeatstr=repeat.strftime('%m-%d')+'-'+weekdayDict[weekday]
        repeat_list.append(repeatstr)

    # repeat_dict.update({date:repeat_list})
    return repeat_list


#表格的行添加颜色
def table_row_color_render(table,int,color):
    row = table.rows[int]
    for cell in row.cells:
        shading_elm = parse_xml(r'<w:shd {} w:fill="{}"/>'.format(nsdecls('w'),color))
        cell._tc.get_or_add_tcPr().append(shading_elm)


#表格的列添加颜色
def table_col_color_render(table,int,color):
    col = table.columns[int]
    for cell in col.cells:
        shading_elm = parse_xml(r'<w:shd {} w:fill="{}"/>'.format(nsdecls('w'),color))
        cell._tc.get_or_add_tcPr().append(shading_elm)
#===========================================


path=r'C:\Users\87754\OneDrive\文档\document\word\01-工\【记忆法】'

data={}
month=[]
year=2023
start = datetime.date(year,1,1)

end = datetime.date(year,12,31)
delta = datetime.timedelta(days=1)

now = start

while now <= end:
    nowstr = now.strftime('%Y-%m-%d')
    monthstr= nowstr[5:7]
    #第一次出现
    if monthstr not in month:
        month.append(monthstr)
        data.update({monthstr: []})

    data[monthstr].append(nowstr)
    now = now+delta


repeat_dict={}
# 组合 repeatday和weekday
for i in data:
    print(i,data[i])
    for j in data[i]:
        repeat = get_repeat_date(j)
        # print(j,repeat)
        repeat_dict.update({j:repeat})


#========================================================================
strtime=str(datetime.datetime.now())
strtime=strtime[:strtime.index('.')]
strtime=strtime.replace(':','').replace(' ','_')

savename='{}/Ebbinghause_new_{}.docx'.format(path,strtime)
doc = Document()

#-----------------纸张转向 start 全局参数
section = doc.sections[0]
section.page_height = Cm(29.7)
section.page_width = Cm(21.0)
new_width, new_height = section.page_height, section.page_width
section.orientation = WD_ORIENT.LANDSCAPE
section.page_width = new_width
section.page_height = new_height
#-----------------纸张转向 end
#设置页边距
sections = doc.sections
for section in sections:
    section.top_margin = Cm(0.5)
    section.bottom_margin = Cm(0.5)
    section.left_margin = Cm(1.5)
    section.right_margin = Cm(0.5)

    # section.top_margin = Cm(1.5)
    # section.bottom_margin = Cm(1.5)
    # section.left_margin = Cm(1.5)
    # section.right_margin = Cm(1.5)

set_font(doc)
#匹配12号字体
col_width_list=[Cm(2.5),Cm(5.0),Cm(2.9),Cm(2.9),Cm(2.9),Cm(2.9),Cm(2.9),Cm(2.9),Cm(2.9)]
#匹配11号字体
# col_width_list=[Cm(2.3),Cm(6.0),Cm(2.7),Cm(2.7),Cm(2.7),Cm(2.7),Cm(2.7),Cm(2.7),Cm(2.7)]
col_num=len(col_width_list)

title_list=['学习当天','学习内容','第1次','第2次','第3次','第4次','第5次','第6次','第7次']

for i in data:
    heading1=doc.add_heading(level=1)
    heading1.add_run( i + '月')
    heading1.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    daylist=data[i]
    row_num = len(daylist)+1
    table = doc.add_table(rows=row_num, cols=col_num, style='Table Grid')
    # 设置单元格宽度
    set_col_widths(table, col_width_list)
    # talbe的第一行【标题行】
    row = table.rows[0]
    for t in range(9):
        cell = row.cells[t]
        cell.text=title_list[t]
        cell.paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    table_row_color_render(table,0,'khaki')
    table_col_color_render(table,0,'d9d9d9')


    for j in range(1,row_num):

        row = table.rows[j]

        row.cells[0].text = repeat_dict[daylist[j-1]][0]
        row.cells[1].text = ' '
        row.cells[2].text = '①'+repeat_dict[daylist[j-1]][1]
        row.cells[3].text = '②'+repeat_dict[daylist[j-1]][2]
        row.cells[4].text = '③'+repeat_dict[daylist[j-1]][3]
        row.cells[5].text = '④'+repeat_dict[daylist[j-1]][4]
        row.cells[6].text = '⑤'+repeat_dict[daylist[j-1]][5]
        row.cells[7].text = '⑥'+repeat_dict[daylist[j-1]][6]
        row.cells[8].text = '⑦'+repeat_dict[daylist[j-1]][7]


    doc.add_page_break()

for paragraph in doc.paragraphs:
    paragraph.paragraph_format.space_before = Pt(0)
	# print(paragraph.text)

doc.save(savename)
print('create docx OK ... ')