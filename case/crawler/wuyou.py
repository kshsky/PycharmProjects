import pandas as pd
from bs4 import BeautifulSoup
import requests
import random
import time


url='https://search.51job.com/list/010000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2596%25E6%258E%2598,2,1.html'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

response = requests.get(url,headers=headers)
response.encoding='gbk'


columns=['公司','状态','主要标签','法人','注册资本','成立日期','邮箱','地址']
# class="search-item sv-search-company"

print(response.text)