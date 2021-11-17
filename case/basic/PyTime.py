import time
# import datetime
from datetime import datetime,timedelta
localtime = time.asctime(time.localtime(time.time()))


print(localtime)#Fri Jun  4 15:08:25 2021
print(time.localtime().tm_year)#2021
print(time.localtime().tm_mon)#6
print(time.localtime().tm_mday)#4
print(time.localtime().tm_yday)#155
print(time.localtime().tm_wday)#4
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))#2021-06-04 15:08:25
print(time.strftime('%Y-%m-%d %H:%M:%S'))#2021-06-04 15:08:25
print(time.strftime('%Y-%m-%d %X'))#2021-06-04 15:08:25

print(datetime.now())#2021-06-04 15:15:09.334441
dt_now = datetime.now()

print(dt_now.date())#2021-06-04
print(dt_now.time())#15:15:09.334441
print(dt_now.timestamp())#1622790909.334441
#把时间格式化成字符串
print(dt_now.strftime('%Y-%m-%d %H:%M:%S'))#2021-06-04 15:15:09

#把字符串变成时间
datetime1 = datetime.strptime('2021-06-04 15:15:09','%Y-%m-%d %H:%M:%S')

datetime2 = datetime1 + timedelta(seconds=33)
datetime3 = datetime1 + timedelta(weeks=1,days=1,hours=1,minutes=1,seconds=1)
print(datetime1)
print(datetime2)
print(datetime3)

import calendar

#isleap 是否是闰年
print(calendar.isleap(time.localtime().tm_year))
print(calendar.firstweekday())
#calendar.monthrange 天数范围
print(calendar.monthrange(time.localtime().tm_year,time.localtime().tm_mon))#(1, 30)
#alendar.month(2021,6) 打印日历
print(calendar.month(time.localtime().tm_year,time.localtime().tm_mon))
#      June 2021
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30