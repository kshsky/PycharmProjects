'''
CRIM：城镇人均犯罪率。
ZN：住宅用地超过25 000平方尺的比例。
INDUS：城镇非零售商业用地比例。
CHAS：查尔斯河（如果边界是河流，则为1，否则为0）。
NOX：一氧化碳浓度。
RM：住宅平均房屋数。
AGE：1940年之前建成的自用房屋比例。
DIS：到波士顿5个中心区域的加权距离。
RAD：辐射性公路的接近指数。
TAX：每万美元全值物业税税率。
PTRATIO：城镇教师和学生比例。
MEDV：自住房房价中位数。
'''
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error

# 加载波士顿房价数据
boston = datasets.load_boston()
X = boston.data
y = boston.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/5 ,random_state = 8)

# 线性回归
lr = LinearRegression()
# 训练模型
lr.fit(X_train,y_train)
# 预测
y_pred = lr.predict(X_test)
# 用均方误差评估预测效果
mse = mean_squared_error(y_test, y_pred)
print(mse)


import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_squared_error
# 将数据转化为DMatrix格式
train_xgb = xgb.DMatrix(X_train, y_train)
params = {"objective": "reg:squarederror", "booster":"gblinear"}
num_round=30
model = xgb.train(dtrain=train_xgb,params=params)
y_pred = model.predict(xgb.DMatrix(X_test))
# print(y_pred)
mse = mean_squared_error(y_test,y_pred)
print(mse)

import numpy as np
import matplotlib as mpl
import  matplotlib.pyplot as plt
import  pandas as pd
import  warnings
import sklearn
from sklearn.linear_model import LinearRegression,LassoCV,RidgeCV,ElasticNetCV
from sklearn.preprocessing import PolynomialFeatures  #多项式特征
from sklearn.pipeline import Pipeline
# from sklearn.linear_model.coordinate_descent import ConvergenceWarning #拦截异常的
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn import  metrics  #评价指标

def notEmpty(s):
    return s !=''    #是空的话就是FLASE，不是空的话就是TRUE

#设置字符集，防止中文乱码

mpl.rcParams['font.sans-serif']=[u'simHei']
mpl.rcParams['axes.unicode_minus']=False

# 加载数据
names = ['CRIM','ZN', 'INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT']  #前13个和房价相关的字段，LSTAT为房价
# 由于数据文件格式不统一，所以读取的时候，先按照一行一个字段属性读取数据，然后再安装每行数据进行处理
boston = datasets.load_boston()
X = boston.data
y = boston.target

#print(y[0:5])
ly=len(y)
# print(y.shape)
print('样本数据量:%d,特征个数:%d '%X.shape)
print('target样本数据量:%d'%y.shape[0])

print('-------------------------')
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LassoCV
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号, 注意['SimHei']对应这句不行.


oridata = datasets.load_boston()
data = oridata.data
label = oridata.target

##矩阵的长度：行数
dataLen = len(data)
##矩阵的宽度：列数
dataWid = len(data[0])
##每列的均值
xMeans = []
##每列的方差
xSD = []
##归一化样本集
xNorm = []
##归一化标签
lableNorm = []

##第一次处理数据：计算每列的均值和方差
for j in range(dataWid):
    ##读取每列的值
    x = [data[i][j] for i in range(dataLen)]
    ##每列的均值
    mean = np.mean(x)
    xMeans.append(mean)
    ##每列的方差
    sd = np.std(x)
    xSD.append(sd)

##第二次处理数据：归一化样本集和标签
for j in range(dataLen):
    ##样本集归一化
    xn = [(data[j][i] - xMeans[i]) / xSD[i] for i in range(dataWid - 1)]
    xNorm.append(xn)
    ##标签归一化
    ln = (data[j][dataWid - 1] - xMeans[dataWid - 1]) / xSD[dataWid - 1]
    lableNorm.append(ln)

##参数格式是数组形式，所以需要转换一下
X = np.array(xNorm)
Y = np.array(lableNorm)
##开始做交叉验证：cv=10表示采用10折交叉验证
wineModel = LassoCV(cv=10).fit(X, Y)

##打印出最佳解的每项的系数：
print(wineModel.coef_)
##打印出最佳解的惩罚系数：
print(wineModel.alpha_)

from sklearn.preprocessing import scale,StandardScaler,MinMaxScaler
df = pd.DataFrame(data = data , columns= names)
df['label']=label

scalaData = scale(df)

##开始做交叉验证：cv=10表示采用10折交叉验证
lassoCV = LassoCV(cv=10).fit(scalaData[:,:-1],scalaData[:,-1])


##打印出最佳解的每项的系数：
print(lassoCV.coef_)
##打印出最佳解的惩罚系数：
print(lassoCV.alpha_)
# ========================================
df = pd.DataFrame(data = data , columns= names)
df['label']=label

ss = StandardScaler()
stdData = ss.fit_transform(df)
##开始做交叉验证：cv=10表示采用10折交叉验证
lassoCVstd = LassoCV(cv=10).fit(stdData[:,:-1],stdData[:,-1])


##打印出最佳解的每项的系数：
print(lassoCVstd.coef_)
##打印出最佳解的惩罚系数：
print(lassoCVstd.alpha_)
# ========================================
df = pd.DataFrame(data = data , columns= names)
df['label']=label

mms = MinMaxScaler()
mms.fit(df)
mmData = mms.transform(df)

##开始做交叉验证：cv=10表示采用10折交叉验证
lassoCVmm = LassoCV(cv=10).fit(mmData[:,:-1],mmData[:,-1])


##打印出最佳解的每项的系数：
print(lassoCVmm.coef_)
##打印出最佳解的惩罚系数：
print(lassoCVmm.alpha_)
# ========================================
##绘图
plt.figure(figsize=(12,9))
ax = plt.subplot(221)

##随着alpha值的变化，均方误差的变化曲线
plt.plot(wineModel.alphas_, wineModel.mse_path_, ':')
##验证过程中，随着alpha值的变化，均方误差的平均曲线
plt.plot(wineModel.alphas_, wineModel.mse_path_.mean(axis=-1),
         label='Average MSE Across Folds', linewidth=2)
##每次验证系统认为的最合适的alpha值
plt.axvline(wineModel.alpha_, linestyle='--',
            label='CV Estimate of Best alpha')
plt.semilogx()
plt.legend()
ax = plt.gca()
ax.invert_xaxis()
plt.xlabel('alpha')
plt.ylabel('Mean Square Error')
plt.axis('tight')
plt.title('handle')
ax2 = plt.subplot(222)
##随着alpha值的变化，均方误差的变化曲线
plt.plot(lassoCV.alphas_, lassoCV.mse_path_, ':')
##验证过程中，随着alpha值的变化，均方误差的平均曲线
plt.plot(lassoCV.alphas_, lassoCV.mse_path_.mean(axis=-1),
         label='Average MSE Across Folds', linewidth=2)
##每次验证系统认为的最合适的alpha值
plt.axvline(lassoCV.alpha_, linestyle='--',
            label='CV Estimate of Best alpha')
plt.semilogx()
plt.legend()
ax2 = plt.gca()
ax2.invert_xaxis()
plt.xlabel('alpha')
plt.ylabel('Mean Square Error')
plt.axis('tight')
plt.title('scala')
ax3 = plt.subplot(223)
##随着alpha值的变化，均方误差的变化曲线
plt.plot(lassoCVstd.alphas_, lassoCVstd.mse_path_, ':')
##验证过程中，随着alpha值的变化，均方误差的平均曲线
plt.plot(lassoCVstd.alphas_, lassoCVstd.mse_path_.mean(axis=-1),
         label='Average MSE Across Folds', linewidth=2)
##每次验证系统认为的最合适的alpha值
plt.axvline(lassoCVstd.alpha_, linestyle='--',
            label='CV Estimate of Best alpha')
plt.semilogx()
plt.legend()
ax3 = plt.gca()
ax3.invert_xaxis()
plt.xlabel('alpha')
plt.ylabel('Mean Square Error')
plt.axis('tight')
plt.title('StanderScala')
ax4 = plt.subplot(224)
##随着alpha值的变化，均方误差的变化曲线
plt.plot(lassoCVmm.alphas_, lassoCVmm.mse_path_, ':')
##验证过程中，随着alpha值的变化，均方误差的平均曲线
plt.plot(lassoCVmm.alphas_, lassoCVmm.mse_path_.mean(axis=-1),
         label='Average MSE Across Folds', linewidth=2)
##每次验证系统认为的最合适的alpha值
plt.axvline(lassoCVmm.alpha_, linestyle='--',
            label='CV Estimate of Best alpha')
plt.semilogx()
plt.legend()
ax4 = plt.gca()
ax4.invert_xaxis()
plt.xlabel('alpha')
plt.ylabel('Mean Square Error')
plt.axis('tight')
plt.title('MinmaxScala')
plt.show()