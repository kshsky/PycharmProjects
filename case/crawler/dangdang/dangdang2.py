# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

headers = {

    'user-agent': user_agent                      #浏览器头文件信息

}


url= 'http://product.dangdang.com/23464478.html#ddclick?act=click&pos=23464478_0_2_p&cat=01.00.00.00.00.00&key=&q\info=&pinfo=11287313_1_60&minfo=&ninfo=&custid=&permid=20170216140846297879631198545887287&ref=&rcount=&type=&t=1487225436000&searchapi_ver-sion=eb_split'

response = requests.get(url=url,headers=headers)                           # 发送请求
#当当居然用gbk编码，牛气
response.encoding='gbk'
# response.encoding='utf-8'
soup=BeautifulSoup(response.text,'lxml')
#打印出整齐有排面的样式
# print(soup.prettify())
print('========================================')
##########################################################################

#找到包含整个元素的最小单元unit
unit = soup.find(name='div',class_='product_main clearfix')

#作者
print('作者：',unit.find(id='author').find(name='a').string)
print('作者：',unit.find_all(class_='t1')[0].find_all(name='a')[0].string)
#图片
print('图片：',unit.find(class_='big_pic').find(name='img').attrs['src'])
#出版社
print('出版社：',unit.find_all(class_='t1')[1].find(name='a').string)
#出版时间
print('出版时间：',unit.find_all(class_='t1')[2].string)
#价格
print('价格',unit.find(id='original-price').get_text(strip=True))
print('价格',unit.find(id='original-price').get_text(strip=True)[1:])
print('价格',unit.find(id='original-price').contents[2])

book_detail = soup.find(name='ul',class_='key clearfix')

print(book_detail.find_all(name='li')[0].string)
print(book_detail.find_all(name='li')[1].string)
print(book_detail.find_all(name='li')[2].string)
print(book_detail.find_all(name='li')[3].string)
print(book_detail.find_all(name='li')[4].string)
print('=================================================')
print('=================================================')
