import time
# import datetime
from datetime import datetime,timedelta
localtime = time.asctime(time.localtime(time.time()))


print(localtime)#Fri Jun  4 15:08:25 2021

print(datetime.now())#2021-06-04 15:15:09.334441
dt_now = datetime.now()

print(dt_now.date())#2021-06-04
print(dt_now.time())#15:15:09.334441
print(dt_now.timestamp())#1622790909.334441
#把时间格式化成字符串
print(dt_now.strftime('%Y-%m-%d %H:%M:%S'))#2021-06-04 15:15:09

import calendar

#isleap 是否是闰年
print(calendar.isleap(time.localtime().tm_year))
print(calendar.firstweekday())
#calendar.monthrange 天数范围
print(calendar.monthrange(time.localtime().tm_year,time.localtime().tm_mon))#(1, 30)
print(time.localtime().tm_year)
print(time.localtime().tm_mon)
print(time.localtime().tm_mday)
print(time.localtime().tm_yday)
print(time.localtime().tm_wday)
#alendar.month(2021,6) 打印日历
print(calendar.month(time.localtime().tm_year,time.localtime().tm_mon))
#      June 2021
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30

day_list = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
print(len(day_list))
print(calendar.mdays)
today = datetime.today()
monthRange = calendar.monthrange(today.year,today.month)[1]
print(today)


import datetime
begin = datetime.date(2019,1,1)
end = datetime.date(2019,1,6)
d = begin
delta = datetime.timedelta(days=1)
while d <= end:
    print(d.strftime("%Y-%m-%d"))
    d += delta


print('-------------')
start = datetime.date(2022,6,1)
end = datetime.date(2022,6,2)
delta = datetime.timedelta(days=1)
d = start
while d <= end:
    # print(d.strftime('%Y%m/%d'))
    # d.weekday() 返回0-6
    # d.isoweekday() 返回1-7
    print(d.weekday(), '-', d.isoweekday(),'-',d.strftime('%Y/%m/%d'))
    d +=delta


print(datetime.datetime.now())

print(datetime.datetime.now().date())


