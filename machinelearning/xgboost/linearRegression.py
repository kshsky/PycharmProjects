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


params = {"objective": "reg:gblinear", "booster":"gblinear"}
import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_squared_error
# 将数据转化为DMatrix格式
train_xgb = xgb.DMatrix(X_train, y_train)
params = {"objective": "reg:linear", "booster":"gblinear"}
model = xgb.train(dtrain=train_xgb,params=params)
y_pred = model.predict(xgb.DMatrix(X_test))
mse = mean_squared_error(y_test,y_pred)
print(mse)