from docx import Document
from docx.shared import Pt,RGBColor
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Cm
from docx.oxml.ns import qn
import datetime
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
#纵向转横向
from docx.enum.section import WD_ORIENT

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


path=r'C:\Users\87754\OneDrive\文档\document\03-工\【记忆术】'

data={}
month=[]
year=2022
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

savename='{}/{}.docx'.format(path,now.strftime('艾宾浩斯曲线记忆重复字典-2022-color'))
doc = Document()
#-----------------纸张转向 start 全局参数
section = doc.sections[0]
new_width, new_height = section.page_height, section.page_width
section.orientation = WD_ORIENT.LANDSCAPE
section.page_width = new_width
section.page_height = new_height
#-----------------纸张转向 end
#设置页边距
sections = doc.sections
for section in sections:
    section.top_margin = Cm(1.5)
    section.bottom_margin = Cm(2)
    section.left_margin = Cm(2.54)
    section.right_margin = Cm(2.54)

set_font(doc)

col_width_list=[Cm(2.9),Cm(2.9),Cm(2.9),Cm(2.9),Cm(2.9),Cm(2.9),Cm(2.9),Cm(2.9)]
col_num=len(col_width_list)

for i in data:

    doc.add_heading(str(year)+'年'+i+'月', level=1)
    # p = doc.add_paragraph()
    daylist=data[i]
    row_num = len(daylist)+1
    table = doc.add_table(rows=row_num, cols=col_num, style='Table Grid')
    # 设置单元格宽度
    set_col_widths(table, col_width_list)
    # talbe的第一行【标题行】
    row = table.rows[0]
    row.cells[0].text = '学习当天'
    row.cells[1].text = '第1次'
    row.cells[2].text = '第2次'
    row.cells[3].text = '第3次'
    row.cells[4].text = '第4次'
    row.cells[5].text = '第5次'
    row.cells[6].text = '第6次'
    row.cells[7].text = '第7次'
    table_row_color_render(table,0,'khaki')
    table_col_color_render(table,0,'d9d9d9')
    for j in range(1,row_num):

        row = table.rows[j]

        row.cells[0].text = repeat_dict[daylist[j-1]][0]
        row.cells[1].text = repeat_dict[daylist[j-1]][1]
        row.cells[2].text = repeat_dict[daylist[j-1]][2]
        row.cells[3].text = repeat_dict[daylist[j-1]][3]
        row.cells[4].text = repeat_dict[daylist[j-1]][4]
        row.cells[5].text = repeat_dict[daylist[j-1]][5]
        row.cells[6].text = repeat_dict[daylist[j-1]][6]
        row.cells[7].text = repeat_dict[daylist[j-1]][7]
        # print(repeat_dict[daylist[j]])

    doc.add_page_break()
doc.save(savename)
print('create docx OK ... ')