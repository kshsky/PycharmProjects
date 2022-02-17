import xgboost as xgb
import sklearn.linear_model
from sklearn.model_selection import train_test_split
import pandas as pd

#pandas读取默认会将第一行读取为columns列名，取消第一行读取为列名：header=None
# oriData = pd.read_csv('datafile/agaricus-lepiota.data',header=None)
#
# data = oriData.iloc[:,1:]
# target = oriData.iloc[:,0]
# X_train,X_test,y_train,y_test = train_test_split(data,target,random_state=0)
# print(data)
# print(target)


# oriData = xgb.DMatrix('datafile/agaricus-lepiota.data')

xgb_train = xgb.DMatrix('datafile/agaricus.txt.train')
xgb_test = xgb.DMatrix('datafile/agaricus.txt.test')
# 数据读取
# 定义模型训练参数
params = {
"objective": "binary:logistic",
"booster": "gbtree",
"max_depth": 3
}
# 训练轮数
num_round = 5
# 训练过程中实时输出评估结果
watchlist = [(xgb_train, 'train'), (xgb_test, 'test')]
# 模型训练
model = xgb.train(params, xgb_train, num_round, watchlist)
preds = model.predict(xgb_test)
print(preds)

