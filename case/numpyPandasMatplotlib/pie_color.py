import numpy as np
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(18,6))
ax1=plt.subplot(241)
x = np.arange(0,1,0.00001)
y = np.log((1-x)/x)*0.5
plt.axvline(0.5,linestyle='-.',c='r')
plt.axhline(0,linestyle='--',c='m')
plt.text(0.5005,0.06,'(0.5,0)',fontdict={'fontsize':15})
plt.xlabel('error',fontdict={'fontsize':15})
plt.ylabel('0.5 * np.log((1-e)/e)',fontdict={'fontsize':15})
plt.plot(x,y)

y=[2,5,8,3,10,4]
x=[1,2,3,4,5,6]
#折线图
ax2=plt.subplot(242)
ax2.plot(x,y,color='cornflowerblue',linestyle='-.',marker='o')
plt.ylim(0.5,10.5)
plt.xlim(0.5,6.5)
plt.grid(True,alpha=0.8)



ax3 = plt.subplot(243)

ax3.pie(
x=y,
labels=['springgreen','lightgreen','limegreen','forestgreen','green','lime'],
colors=['springgreen','lightgreen','limegreen','forestgreen','green','lime'],
explode=[0.3,0,0,0,0,0],
shadow=True,
# radius 半径
radius=1,
autopct='%.2f%%'
)

ax4 = plt.subplot(244)
import random
xx=[]
for i in range(1,10000):
    xx.append(random.randint(1,20))

ax4.hist(
x=xx,
# weights = y,
#分组
bins=10,
color='#1e90ff',
align='mid',
rwidth=1

)
ax4.grid(alpha=0.5)



ax5 = plt.subplot(245)


# def bar(self, x, height, width=0.8, bottom=None, *, align="center",
ax5.bar(
x=x,
height = y,
width=0.7,
color='peru',
align='center'

)
ax5.grid(alpha=0.5)




ax6 = plt.subplot(246)

ax6.pie(
x=y,
labels=['cornflowerblue','deepskyblue','blue','royalblue','mediumblue','doderblue'],
colors=['cornflowerblue','deepskyblue','blue','royalblue','mediumblue','#1E90FF'],
explode=[0.3,0,0,0,0,0],
shadow=True,
# radius 半径
radius=1,
autopct='%.2f%%'
)




ax7 = plt.subplot(247)

ax7.pie(
x=y,
labels=['purple','darkviolet','blueviolet','violet','coral','tomato'],
colors=['purple','darkviolet','blueviolet','violet','coral','tomato'],
explode=[0.3,0,0,0,0,0],
shadow=True,
# radius 半径
radius=1,
autopct='%.2f%%'
)


ax8 = plt.subplot(248)

ax8.pie(
x=y,
labels=['chocolate','peru','sandybrown','rosybrown','brown','sienna'],
colors=['chocolate','peru','sandybrown','rosybrown','brown','sienna'],
explode=[0.3,0,0,0,0,0],
shadow=True,
# radius 半径
radius=1,
autopct='%.2f%%'
)



plt.show()