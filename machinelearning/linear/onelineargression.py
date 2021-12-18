import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


from sklearn.linear_model import LinearRegression


# x是施肥量，y是小麦产量
x = np.array([15, 20, 25, 30, 35, 40, 45])
y = np.array([330, 345, 365, 405, 445, 450, 455])
model = LinearRegression()
model.fit(x.reshape(-1,1),y)
b=model.intercept_
w=model.coef_

print('LinearRegression 计算结果：')
print('截距b的值：{}'.format(model.intercept_))
print('权重系数w的值： {}'.format(model.coef_))

# ==============================================
plt.figure(figsize=(9, 6))
for i, j in zip(x, y):
    plt.scatter(i, j)

# 画直线，需要准备xy轴数据
xx = []
yy = []
for i in np.arange(np.min(x), np.max(x), 1):
    xx.append(i)
    yy.append(w[0] * i + b)
for i, j in zip(xx, yy):
    plt.plot(xx, yy, 'm')

plt.xlim(np.min(x) - 5, np.max(x) + 5)
plt.ylim(np.min(y) - 10, np.max(y) + 20)
plt.grid(True)
plt.show()

