import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6,6))
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
# xlist = [9,10,10.9,11.5,12,13]
xlist = np.arange(9,13,0.0001)
ylist1=[]
ylist2=[]
ylist3=[]
fp=11.5
pta=(fp-0.85-3)/0.7
for i in xlist:
    ylist1.append((10 - i) * 0.3 + 0.85 + i)
    if i <pta:
        ylist2.append((10 - i) * 0.3 + 0.85 + i)
        ylist3.append((10 - i) * 0.3 + 0.85)
    else:
        ylist2.append(fp)
        ylist3.append(fp - i)


plt.plot(xlist,ylist1,c='#1e90ff',ls='--',label='计算的总付款')
plt.plot(xlist,ylist2,c='darkkhaki',ls='-.',label='实际总付款')
plt.plot(xlist,ylist3,c='peru',ls='--',label='实际利润')

plt.axvline(pta,ls=':',c='b')
plt.axhline(fp,ls='dotted',c='#dcdcdc')
plt.axhline(0,ls='dotted',c='#dcdcdc')
plt.axvline(fp,ls='dotted',c='#dcdcdc')
plt.text(pta,0,str(round(pta,4)))
plt.text(pta+0.02,fp-0.3,'('+str(round(pta,4))+','+str(fp)+')')
plt.legend()
plt.show()