import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(6,6))
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
# xlist = [9,10,10.9,11.5,12,13]
xlist = np.arange(4,15,0.0001)
#实际费用
ylist1=[]
#总付款
ylist2=[]
targetcost=10
targetfee=0.75
maxfee=1.35
minfee=0.3
p=0.15
xdotlist=[4,6,9,10,13,14]

cut = targetcost-(maxfee-targetfee)/p
makeup = targetcost-(minfee-targetfee)/p
for i in xlist:
    if i <=cut:
        ylist1.append(maxfee)
        ylist2.append(i + maxfee)
    elif i>cut and i <= makeup:
        ylist1.append((targetcost-i)*p+targetfee)
        ylist2.append(i+(targetcost-i)*p+targetfee)
    else:
        ylist1.append(minfee)
        ylist2.append(i + minfee)

plt.plot(xlist,ylist1,c='#1e90ff',ls='--',label='实际费用(利润)')
plt.plot(xlist,ylist2,c='darkkhaki',ls='-.',label='实际总付款')

plt.axvline(cut,ls='dotted',c='b')
plt.axvline(makeup,ls='dotted',c='b')

plt.grid()
plt.legend()
plt.show()