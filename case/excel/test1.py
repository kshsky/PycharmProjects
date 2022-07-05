import xlwings as xw

app = xw.App(visible=True,add_book=False)
for i in range(1,21):
    workbook = app.books.add()
    workbook.save(f'e:/CDA/excelfiles/compay_{i}.xlsx')
    workbook.close()
app.quit()


import xlwings as xw
app = xw.App(visible = False)
workbook = app.books.add()
worksheet = workbook.sheets.add('产品统计表')
worksheet.range('A1').value = '编号'
workbook.save(r'e:/CDA/excelfiles/北京.xlsx')
workbook.close()
app.quit()