# -*- coding: utf-8 -*-

import pymysql
from docx import Document
from docx.shared import Pt,RGBColor
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Cm
from docx.oxml.ns import qn

def get_data(ip,port,db,user,passwod,sql,num):
    conn = pymysql.connect(host=ip,db=db,user=user,password=password)
    cursor = conn.cursor()
    cursor.execute(sql)
    if num==0:
        result=cursor.fetchall()
    elif num==1:
        result=cursor.fetchone()
    else:
        result =cursor.fetchmany(num)
    return result
    cursor.close()
    conn.close()
'''
设置单元格宽度
'''
def set_col_widths(table,width_list):
    table.autofit = False
    for row in table.rows:
        for idx, width in enumerate(width_list):
            table.columns[idx].width = width
            row.cells[idx].width = width

def get_paragraph(doc,style,data):
    doc.add_heading(style,2)
    table = doc.add_table(rows=1,cols=5,style=style)

    #设置单元格宽度
    width_list=(Cm(4),Cm(1.2),Cm(5),Cm(1.6),Cm(4))
    set_col_widths(table,width_list)

    row = table.rows[0]

    row.cells[0].text='名称'
    row.cells[1].text='状态'
    row.cells[2].text='标签'
    row.cells[3].text='法人'
    row.cells[4].text='电子邮箱'

    for i in range(len(data)):

        row = table.add_row()

        row.cells[0].text =data[i][0]
        row.cells[1].text = data[i][1]
        row.cells[2].text = data[i][2]
        row.cells[3].text = data[i][3]
        row.cells[4].text = data[i][4]

sql = 'select name,normal,tag,legalPerson,email from skyeye'
ip='192.168.10.108'
port=3306
db='scrapy'
user='root'
password='123456'

# data = get_data(ip,port,db,user,password,sql,0)

#静态数据
data=[['北京大学', '正常', '事业单位;火炬计划项目企业;北京大学', ' ', ' '], ['中国中信集团有限公司', '存续', '中信集团;投资机构;企业集团', '朱鹤新', 'lili@citic.com'], ['中国铁路发展基金股份有限公司', '存续', '投资机构;企业集团', '黄桂章', 'cric@cric-china.com.cn'], ['中国石化集团国际石油勘探开发有限公司', '存续', '战略融资;中国石油化工;企业集团', '武恒志', 'sipcinfo22.sipc@sinopec.com'], ['中国长江三峡集团有限公司', '存续', '央企;三峡集团;投资机构;企业集团', '雷鸣山', 'ctg@ctg.com.cn'], ['中国移动通信集团有限公司', '存续', 'IPO上市;央企;创新型企业;中国移动;投资机构;企业集团', '杨杰', '10086@139.com'], ['中国证券金融股份有限公司', '存续', '中证金融;投资机构', '聂庆平', 'csf1@csf.com.cn'], ['中国石油化工集团有限公司', '存续', '央企;创新型企业;中国石化集团;投资机构;企业集团', '马永生', 'master@sinopec.com'], ['中国联合网络通信有限公司', '存续', '国企;沃易购;投资机构;企业集团', '刘烈宏', 'hqs-unicomlaw@chinaunicom.cn'], ['国家电力公司', '存续', '企业集团', '高严', ' '], ['国务院国有资产监督管理委员会', '正常', '国务院国资委', ' ', ' '], ['中央汇金投资有限责任公司', '存续', '中央汇金', '彭纯', 'huodl@china-inv.cn'], ['北京市基础设施投资有限公司（原北京地铁集团有限责任公司）', '存续', '小微企业;京投;企业集团', '张燕友', 'bangongshi1@bii.com.cn'], ['中国政企合作投资基金股份有限公司', '存续', '出资设立;小微企业;中国PPP基金;投资机构;企业集团', '冯晋平', 'contact@cpppf.org'], ['中国海洋石油集团有限公司', '存续', '央企;中国海洋石油总公司;投资机构;企业集团', '汪东进', 'suff@cnooc.com.cn'], ['中投国际有限责任公司', '存续', '小微企业;投资机构;企业集团', '彭纯', 'huodl@china-inv.cn'], ['中国进出口银行', '存续', '中国进出口银行;企业集团', '胡晓炼', 'exim@eximbank.gov.cn'], ['国家开发银行', '存续', 'A轮;国家开发银行;投资机构;企业集团', '赵欢', 'webmaster@cdb.cn'], ['国家能源投资集团有限责任公司', '存续', '央企;创新型企业;国家能源集团;投资机构;企业集团', '王祥喜', 'zzbs@chnenergy.com.cn'], ['中国国家铁路集团有限公司', '存续', '中国铁路集团;企业集团', '陆东福', 'liuliyan345@163.com']]

for i,j in enumerate(data):
    print(i+1,j)

#1900-2019
doc = Document()
#设置正文字体
doc.styles['Normal'].font.size=Pt(11)
doc.styles['Normal'].font.name = u'宋体'
doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
doc.styles['Normal']._element.rPr.rFonts.set(qn('w:ascii'), 'DejaVu Sans Mono')
#level=0是段落标题
doc.add_heading('天眼查数据',level=0)

doc.add_heading('table style',1)

doc.add_heading('no style',2)
table = doc.add_table(rows=1,cols=5)

row = table.rows[0]

row.cells[0].text='名称'
row.cells[1].text='状态'
row.cells[2].text='标签'
row.cells[3].text='法人'
row.cells[4].text='电子邮箱'

for i in range(len(data)):

    row = table.add_row()
    row.cells[0].text =data[i][0]
    row.cells[1].text = data[i][1]
    row.cells[2].text = data[i][2]
    row.cells[3].text = data[i][3]
    row.cells[4].text = data[i][4]

doc.add_heading('Light List Accent 5',2)
table = doc.add_table(rows=1,cols=5)
table.style="Light List Accent 5"
row = table.rows[0]
row.cells[0].text='名称'
row.cells[1].text='状态'
row.cells[2].text='标签'
row.cells[3].text='法人'
row.cells[4].text='电子邮箱'

for i in range(len(data)):
    row = table.add_row()
    row.cells[0].text =data[i][0]
    row.cells[1].text = data[i][1]
    row.cells[2].text = data[i][2]
    row.cells[3].text = data[i][3]
    row.cells[4].text = data[i][4]


get_paragraph(doc,'Normal Table',data)
get_paragraph(doc,'Table Grid',data)

namelist=['Light Shading','Light List','Light Grid',
          'Medium Shading 1','Medium Shading 2','Medium List 1','Medium List 2','Medium Grid 1','Medium Grid 2','Medium Grid 3',
          'Dark List','Colorful Shading','Colorful List','Colorful Grid']
for k in namelist:
    for i in range(6):
        if i == 0:
            style = k
        else:
            style = '{} Accent {}'.format(k,i)
        get_paragraph(doc, style, data)

doc.save(r'C:\Users\87754\OneDrive\文档\document\03-工\【记忆术】/{}.docx'.format('table_style'))
print('create docx OK ...')




