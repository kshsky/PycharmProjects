import pandas as pd
import matplotlib.pyplot as plt
import random
# 产生1000个1-100的随机数
xx=[]
for i in range(0,10000):
    xx.append(random.randint(1,100))
#分组计算
print(min(xx),max(xx),(max(xx)-min(xx))/10)
#最小值1，最大值100，组距9.9
#分箱：
box,bins = pd.cut(pd.Series(xx),bins=10,retbins=True)

# box是Interval组成的list，是每个随机数对应的箱
# bins是右箱限组成的list
# 用箱限做key，每箱的数据个数为value组建dict
interval = set(box)
interval_ct_dict = {}
for i in interval:
    interval_ct_dict.update({i:0})
#print(bins)
#统计每箱的数据个数
for i in xx:
    for j in interval:
        if i in j:
            k = interval_ct_dict[j]
            interval_ct_dict.update({j: k+1})

#确定组中值；即hist图每个柱子的x_ticks
x_axis =[(bins[i]+bins[i+1])/2 for i in range(0,len(bins) -1)]
print('组中值为：',x_axis)
#组装text
xy = []
for i in x_axis:
    for j in interval_ct_dict.keys():
        if i in j:
            xy.append((i,interval_ct_dict[j]))

#画直方图
plt.hist(
x=xx,
# weights = y,
#分箱
bins=10,
color='#1e90ff',
align='mid',
#设置宽度
rwidth=0.3
)

# 画xticks和text
plt.xticks(x_axis,fontsize=10,color='red')
for i in xy:
    plt.text(i[0]-1.7,i[1]+5,i[1])
#显示grid
plt.grid(True,alpha=0.8)
plt.show()
