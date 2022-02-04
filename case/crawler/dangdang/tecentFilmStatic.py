# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

headers = {

    'user-agent': user_agent                      #浏览器头文件信息

}


url= 'https://v.qq.com/'


resopnseStr=''

# response = requests.get(url=url,headers=headers)                           # 发送请求
#当当居然用gbk编码，牛气
# response.encoding='gbk'
# response.encoding='utf-8'
soup=BeautifulSoup(resopnseStr,'lxml')
#打印出整齐有排面的样式
print(soup.prettify())
print('========================================')
##########################################################################

#找到包含整个元素的最小单元unit
unit = soup.find_all(name='h2',class_='mod_title')
for i in unit:
    # print(i)
    print(i.text.strip())
    print('--------')

print('=================================================')
unit = soup.find_all(name='div', class_='mod_row_box')
c=0

for i in unit:
    c+=1
    print('--- '+str(c)+' ---')
    if i.find(name='h2',class_='mod_title') != None:
        print('>>> ：',i.find(name='h2',class_='mod_title').text.strip())
        detail = i.find_all(name='a',class_='figure_title figure_title_two_row')
        # detail = i.find_all(class_='figure_title figure_title_two_row')
        if len(detail)==0 :
            detail = i.find_all(class_='figure_title figure_title_two_row bold')

        # print(detail)
        for j in detail:
             # print('二级标题：',j.text)

             y = j.contents

             printContent = '>>>>>> ：';

             for k in range(0,len(y)):
                 x =y[k].string.strip()
                 printContent = printContent+x
             print(printContent)

    print('--------')

print('=================================================')
print('=================================================')
