import numpy as np
import pandas as pd

# 1:Male 0:Female
flag=['1','0','1','1','0','0','1','1','1','0']

# 1 Yes 0 No
datalist = [['1','0','0','0'],
            ['1','1','1','1'],
            ['0','0','0','0'],
            ['1','1','1','1'],
            ['1','0','1','0'],
            ['0','0','0','0'],
            ['1','1','1','1'],
            ['0','0','0','0'],
            ['1','0','0','0'],
            ['1','1','1','0']]
columns=['magazine','watch','insurance','creditcard']

data = pd.DataFrame(data = datalist,columns=columns)

data['flag']=flag
print(data)
flag = data['flag']

# np.unique(flag,return_counts=True)
# (array(['0', '1'], dtype=object), array([4, 6], dtype=int64))
c,ct= np.unique(flag,return_counts=True)

p=[i/sum(ct) for i in ct]
pc0=p[0]
pc1=p[1]

m = data['magazine']
magazine =  [np.unique(m[flag == i], return_counts=True) for i in c]
# [(array(['0', '1'], dtype=object), array([1, 3], dtype=int64)),
# (array(['0', '1'], dtype=object), array([2, 4], dtype=int64))]
m_c0=magazine[0][1]
pm_c0=[i/sum(m_c0) for i in m_c0]
pm0_c0=pm_c0[0]
pm1_c0=pm_c0[1]

m_c1=magazine[1][1]
pm_c1=[i/sum(m_c1) for i in m_c1]
pm0_c1=pm_c1[0]
pm1_c1=pm_c1[1]
print(pm0_c0,pm1_c0,pm0_c1,pm1_c1)
# =========================
w = data['watch']
watch =  [np.unique(w[flag == i], return_counts=True) for i in c]

w_c0=watch[0][1]
pw_c0=[i/sum(w_c0) for i in w_c0]
pw0_c0=pw_c0[0]
pw1_c0=pw_c0[1]


w_c1=watch[1][1]
pw_c1=[i/sum(w_c1) for i in w_c1]
pw0_c1=pw_c1[0]
pw1_c1=pw_c1[1]

print(pw0_c0,pw1_c0,pw0_c1,pw1_c1)

# =========================
ii = data['insurance']
insurance =  [np.unique(ii[flag == i], return_counts=True) for i in c]

i_c0=insurance[0][1]
pi_c0=[i/sum(i_c0) for i in i_c0]
pi0_c0=pi_c0[0]
pi1_c0=pi_c0[1]


i_c1=insurance[1][1]
pi_c1=[i/sum(i_c1) for i in i_c1]
pi0_c1=pi_c1[0]
pi1_c1=pi_c1[1]

print(pi0_c0,pi1_c0,pi0_c1,pi1_c1)

# =========================
cc = data['creditcard']
creditcard =  [np.unique(cc[flag == c], return_counts=True) for c in c]

c_c0=creditcard[0][1]
pc_c0=[c/sum(c_c0) for c in c_c0]
pc0_c0=pc_c0[0]
pc1_c0=pc_c0[1]


c_c1=creditcard[1][1]
pc_c1=[c/sum(c_c1) for c in c_c1]
pc0_c1=pc_c1[0]
pc1_c1=pc_c1[1]


print(pc0_c0,pc1_c0,pc0_c1,pc1_c1)

# m=1,w=1,i=0,c=0
pXc1=pm1_c1*pw1_c1*pi0_c1*pc0_c1*pc1
pXc0=pm1_c0*pw1_c0*pi0_c0*pc0_c1*pc0
print('pXc1:{} ,pXc0:{} , 所以性别是：{}'.format(pXc1,pXc0,'Male' if pXc1>pXc0 else 'Female'))
