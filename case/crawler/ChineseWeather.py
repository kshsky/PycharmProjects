from bs4 import BeautifulSoup
import requests
import pandas as pd

url='http://www.weather.com.cn/weather/101010100.shtml'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

response=requests.get(url,headers=headers)
response.encoding='utf-8'
soup=BeautifulSoup(response.text,'lxml')
# print(soup.prettify())
print('-----')
#step1, 找到一个整体
ul_tag = soup.find(name='ul',class_='t clearfix')
columns=['date','weather','tempture','wind','windpower']
columns=['日期','天气','温度','方向','风力']

#step2,整体去掉壳子，找到纯粹的多个可以遍历的元素
li_tag = ul_tag.find_all('li')
print(li_tag)
#step3,获取将要遍历的单个元素,原则，连续定位
print('日期：',li_tag[0].h1.string)
print('天气：',li_tag[0].find('p','wea').string)
print('温度：',li_tag[0].find('p','tem').text.strip())
# 遇到有时1个元素，有时2个元素，就用  x if condition else y
print('风向：',li_tag[0].find('p','win').find_all('span')[0].attrs['title'] if len(li_tag[0].find('p','win').find_all('span'))==1 else li_tag[0].find('p','win').find_all('span')[0].attrs['title']+'转'+li_tag[0].find('p','win').find_all('span')[1].attrs['title'])
print('风力：',li_tag[0].find('p','win').find('i').string)
# step4,将每个字段值都用一个list存储
date=[]
weather=[]
tempture=[]
wind=[]
windpower=[]

#总列表
data=[]

for i in li_tag:

	i_date=i.h1.string.strip()
	i_weather=i.find('p','wea').string
	i_tempture=i.find('p','tem').text.strip()
	i_wind=i.find('p','win').find_all('span')[0].attrs['title'] if len(i.find('p','win').find_all('span'))==1 else i.find('p','win').find_all('span')[0].attrs['title']+'转'+i.find('p','win').find_all('span')[1].attrs['title']
	i_windpower=i.find('p','win').find('i').string


	print(i_date,i_weather,i_tempture,i_wind,i_windpower)
	date.append(i_date)
	weather.append(i_weather)
	tempture.append(i_tempture)
	wind.append(i_wind)
	windpower.append(i_windpower)
print('单个list组装完毕')
print(date)
print(weather)
print(tempture)
print(wind)
print(windpower)
#step5组合,每一天组成一个list
#data=[[day1],[dat2],[day3],……,[day7]]
for i in range(len(date)):
	data.append([date[i],weather[i],tempture[i],wind[i],windpower[i]])


df = pd.DataFrame(data=data,columns=columns)
print(df)
