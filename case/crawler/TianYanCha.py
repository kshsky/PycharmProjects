import pandas as pd
from bs4 import BeautifulSoup
import requests
import random
import time


url='https://www.tianyancha.com/search?base=bj'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

response = requests.get(url,headers=headers)
response.encoding='utf8'
soup = BeautifulSoup(response.text,'lxml')
html = soup.prettify()

# print(html)

columns=['公司','状态','主要标签','法人','注册资本','成立日期','邮箱','地址']

item = soup.find(name = 'div',class_='result-list')
result_list = item.find_all('div','search-item sv-search-company')
# print(result_list[5])

name = result_list[5].find('a','name select-none').string
status  = result_list[5].find('div','tag-common -normal-bg').string
label = result_list[5].find('div','tag-list').text if result_list[5].find('div','tag-list')!=None else None
legal = result_list[5].find('a','legalPersonName link-click').text
capital = result_list[5].find('div','title -narrow text-ellipsis').find('span').text
build = result_list[5].find('div','title text-ellipsis').find('span').text
email = result_list[5].find_all('div','contact row')[0].find_all('div','col')[1].find_all('span')[1].text
address= result_list[5].find_all('div','contact row')[1].find('div','col').find_all('span')[1].text


#contact row 有0，1、2 三种情况
#0，email和address 都为None
#1，一定是address
#2，第一个是电话和邮箱，取邮箱；第二个是地址
# 复杂情况，用函数
def getContract(html):
	print('----------')
	email=None
	address = None

	contract_list = html.find_all('div','contact row')

	num =len(contract_list)

	print(contract_list)
	if num==0:
		return (email,address)

	if num==1:
		address =contract_list[0].find('div','col').find_all('span')[-1].text
		print(email,address)
		return (email,address)

	elif num==2:
		email = contract_list[0].find_all('div','col')[-1].find_all('span')[1].text if len(contract_list[0].find_all('div','col')) !=0 else None
		address = contract_list[1].find('div','col').find_all('span')[-1].text
		print(email,address)
		return (email,address)
	print('===========')

print(name,status,label,legal,capital,build,email,address)

data = []

name= []
status= []
label= []
legal= []
capital= []
build= []
email= []
address= []




for i in result_list:
	# print(i)
	i_name=i.find('a','name select-none').string
	i_status=i.find('div','tag-common -normal-bg').string if i.find('div','tag-common -normal-bg')!=None else None
	i_label=i.find('div','tag-list').text if i.find('div','tag-list')!=None else None
	i_legal =i.find('a','legalPersonName link-click').text if i.find('a','legalPersonName link-click') !=None else None
	i_capital=i.find('div','title -narrow text-ellipsis').find('span').text
	i_build=i.find('div','title text-ellipsis').find('span').text
	i_email,i_address = getContract(i)

	print(i_name,i_status,i_label,i_legal,i_capital,i_build,i_email,i_address)

	name.append(i_name)
	status.append(i_status)
	label.append(i_label)
	legal.append(i_legal)
	capital.append(i_capital)
	build.append(i_build)
	email.append(i_email)
	address.append(i_address)

for i in range(len(name)):
	data.append([name[i],status[i],label[i],legal[i],capital[i],build[i],email[i],address[i]])

df = pd.DataFrame(data = data ,columns=columns)
print(df)
