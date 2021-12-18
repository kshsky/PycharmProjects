import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# rc参数
plt.rcParams['font.family'] = 'SimHei'    # 显示中文 windows
# plt.rcParams['font.family'] = 'Arial Unicode MS'   # 显示中文 mac
plt.rcParams['axes.unicode_minus'] = False   # 显示负号

data = np.load('dataFile/国民经济核算季度数据-0821-pm.npz',allow_pickle=True)
print(data['values'])
print(data['columns'])

values = data['values']
columns = data['columns']


# 创建画布
fig = plt.figure(figsize=(18,12))

# 子图1
ax1 = fig.add_subplot(3,4,1)
# 第一产业
plt.scatter(values[:,0],values[:,3])
# 第二产业
plt.scatter(values[:,0],values[:,4],marker='+')
# 第三产业
plt.scatter(values[:,0],values[:,5],marker='^')
plt.title('2000-2017各产业季度生产总值散点图')
plt.ylabel('生产总值（亿元）')
plt.legend(['第一产业','第二产业','第三产业'])

# 子图2
ax2 = fig.add_subplot(3,4,2)
for i in range(6,15):
    plt.scatter(values[:,1],values[:,i],s=10)
print(values[:,1])
plt.xlabel('年份')
plt.ylabel('生产总值（亿元）')
plt.legend(['农业','工业','建筑','批发','交通','餐饮','金融','房地产','其他'])
# plt.xticks(range(0,70,4),rotation=20);

plt.xticks(range(0,70,4),rotation=20);



# 子图3
ax3 = fig.add_subplot(3,4,3)
# 第一产业
plt.plot(values[:,0],values[:,3],'b-')
# 第二产业
plt.plot(values[:,0],values[:,4],'r-')
# 第三产业
plt.plot(values[:,0],values[:,5],'g-')
plt.title('2000-2017各产业季度生产总值折线图')
plt.ylabel('生产总值（亿元）')
plt.legend(['第一产业','第二产业','第三产业'])

# 子图4
ax4 = fig.add_subplot(3,4,4)
for i in range(6,15):
    plt.plot(values[:,1],values[:,i])

plt.xlabel('年份')
plt.ylabel('生产总值（亿元）')
plt.legend(['农业','工业','建筑','批发','交通','餐饮','金融','房地产','其他'])
plt.xticks(range(0,70,4),rotation=45);


label1 = ['第一产业','第二产业','第三产业']
label2 = ['农业','工业','建筑','批发','交通','餐饮','金融','房地产','其他']

# 子图1 2000年第一季度三产业
ax5 = fig.add_subplot(3,4,5)
plt.bar(label1,values[0,3:6],width=0.5)
plt.title('2000年第一季度生产总值柱状图')
plt.xlabel('产业')
plt.ylabel('生产总值（亿元）')

# 子图4 2017年第一季度行业
ax6 = fig.add_subplot(3,4,6)
plt.bar(label2,values[-1,6:],width=0.5)
plt.title('2017年第一季度行业生产总值柱状图')
plt.xlabel('行业')
plt.ylabel('生产总值（亿元）');




# 子图72017年第一季度行业
ax7 = fig.add_subplot(3,4,7)
s=pd.Series(np.random.randn(10000))
plt.hist(s,
        density=True,
        histtype='step',
        orientation='vertical')
s.plot(kind='kde')# 需要将density设置为True

label1 = ['第一产业','第二产业','第三产业']
label2 = ['农业','工业','建筑','批发','交通','餐饮','金融','房地产','其他']


# 子图1 2000-2017年三产业
ax8 = fig.add_subplot(3,4,8)
plt.boxplot(values[:,3:6],labels=label1,notch=True)

# 子图1 2000-2017年行业
ax9 = fig.add_subplot(3,4,9)
plt.boxplot(values[:,6:],labels=label2,notch=True);


plt.show()