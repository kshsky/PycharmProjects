import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# x是施肥量，y是小麦产量
x=np.array([15,20,25,30,35,40,45])
y=np.array([330,345,365,405,445,450,455])
# 1.sklearn的算法
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x.reshape(-1,1),y)
b=model.intercept_
w=model.coef_
print('LinearRegression 计算结果：')
print('截距b的值：{}'.format(model.intercept_))
print('权重系数w的值： {}'.format(model.coef_))
print('--------------------------------------')
print('person系数:')
XY=np.sum(x[:,None]*y[:,None],axis=1)
r=(np.mean(XY)-np.mean(x)*np.mean(y))/np.sqrt(np.var(x)*np.var(y))

print('person相关系数：(EXY-EXEY)/(DXDY)={}'.format(r))

df=pd.DataFrame({'x':x,'y':y})
print('df.x.corr(df.y)={}'.format(df.x.corr(df.y)))
print('np.corrcoef(x,y)={}'.format(np.corrcoef(x,y)[0,1]))
print('--------------------------------------')

# 2.直接计算   beta1 = (EXY -EXEY)/DX
print('beta1 = (EXY -EXEY)/DX')
b1 = (np.mean(XY)-np.mean(x)*np.mean(y))/np.var(x)
print('Cov(xy)={}'.format(np.mean(XY)-np.mean(x)*np.mean(y)))

b0=np.mean(y)-b1*np.mean(x)
print('b1=(np.mean(XY)-np.mean(x)*np.mean(y))/np.var(x)={}'.format(b1))
print('b0=np.mean(y)-b1*np.mean(x)={}'.format(b0))

print('--------------------------------------')
# 3. numpy的矩阵计算:beta
print('np.matmul计算')
x=np.array([15,20,25,30,35,40,45])
y=np.array([330,345,365,405,445,450,455])
xi=x[:,None]
y2=y[:,None]
xi = np.concatenate((np.ones_like(xi),xi),axis=1)
beta =np.matmul(np.matmul(np.linalg.pinv(np.matmul(xi.T, xi)), xi.T), y2)
print('beta={}'.format(beta))

plt.figure(figsize=(9,6))
for i,j in zip(x,y):
    plt.scatter(i,j)

# 画直线，需要准备xy轴数据
xx=[]
yy=[]
for i in np.arange(np.min(x), np.max(x), 1):
    xx.append(i)
    yy.append(w[0] * i + b)
for i,j in zip(xx,yy):
    plt.plot(xx,yy,'peru')

plt.xlim(np.min(x) - 5, np.max(x) + 5)
plt.ylim(np.min(y) - 10, np.max(y) + 20)
plt.show()
