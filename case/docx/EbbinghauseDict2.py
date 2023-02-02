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
【SA】01-01	【①SU】01-02【②MO】01-03【③WE】01-05【④SA】01-08【⑤SU】01-16【⑥MO】01-31【⑦FR】04-01
【SU】01-02	【①MO】01-03【②TU】01-04【③TH】01-06【④SU】01-09【⑤MO】01-17【⑥TU】02-01【⑦SA】04-02

'''
weekdayDict={1:'MO',2:'TU',3:'WE',4:'TH',5:'FR',6:'SA',7:'SU'}
#1-7次复习
orderdict={'1':'①','2':'②','3':'③','4':'④','5':'⑤','6':'⑥','7':'⑦'}

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
    # doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'LXGW WenKai')
    doc.styles['Normal']._element.rPr.rFonts.set(qn('w:ascii'), 'Courier New')


def get_repeat_date(date):
    # 当天之后，第1，2，4，7，15，30，90 天复习
    delta_list = [0, 1, 2, 4, 7, 15, 30, 90]
    learn_day=''
    repeat_day=''
    date = datetime.datetime.strptime(date,'%Y-%m-%d')
    for i in delta_list:
        repeat = date + datetime.timedelta(days=i)
        weekday = repeat.isoweekday()
        # repeatstr='【'+weekdayDict[weekday]+'】'+repeat.strftime('%m-%d')
        if delta_list.index(i)==0:
            learn_day=weekdayDict[weekday]+repeat.strftime('%m-%d')
        else:
            repeat_day+=orderdict[str(delta_list.index(i))]+weekdayDict[weekday]+repeat.strftime('%m-%d')
    return (learn_day,repeat_day)


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

savename='{}/Ebbinghause_01_闰-平{}.docx'.format(path,strtime)
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

col_width_list=[Cm(2.8),Cm(20.3)]
col_num=len(col_width_list)

for i in data:
    # doc.add_heading(str(year)+'年'+i+'月', level=1)
    title_=doc.add_heading(level=1)
    title_.add_run( i + '月')
    title_.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    daylist=data[i]
    row_num = len(daylist)
    table = doc.add_table(rows=row_num, cols=col_num, style='Table Grid')
    # 设置单元格宽度
    set_col_widths(table, col_width_list)
    table_col_color_render(table,0,'d9d9d9')
    for j in range(0,row_num):
        row = table.rows[j]
        row.cells[0].text = repeat_dict[daylist[j]][0]
        row.cells[1].text = repeat_dict[daylist[j]][1]


    doc.add_page_break()

for paragraph in doc.paragraphs:
    paragraph.paragraph_format.space_before = Pt(0)
	# print(paragraph.text)

doc.save(savename)
print('create docx OK ... ')