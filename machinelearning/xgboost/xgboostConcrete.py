import pandas as pd
import xgboost as xgb
import numpy as np
from sklearn import metrics

data = pd.read_excel('dataFile/Concrete_Data.xls')
print(data.columns)
data.rename(columns={"Concrete compressive strength(MPa, megapascals) ":'label'}, inplace=True)

print(data.head())
# 生成一个随机数并选择小于0.8的数据
mask = np.random.rand(len(data)) < 0.8
train = data[mask]
test = data[~mask]


xgb_train = xgb.DMatrix(train.iloc[:, :7], label=train.label)
xgb_test = xgb.DMatrix(test.iloc[:, :7], label=test.label)


#模型训练
params = {
    # "objective": "reg:linear", 废止
    "objective": "reg:squarederror",
    "booster": "gbtree",
    "eta": 0.1,
    "min_child_weight": 1,
    "max_depth": 5
    }

num_round = 50
watchlist = [(xgb_train, 'train'), (xgb_test, 'test')]

model = xgb.train(params, xgb_train, num_round, watchlist)
model.save_model("dataFile/concrete-model.xgb")


# 加载模型进行预测
bst = xgb.Booster()
bst.load_model("dataFile/concrete-model.xgb")
pred = bst.predict(xgb_test)

print(pred)
# 输出格式化后的模型
dump_model = bst.dump_model("dataFile/concrete-dump.txt")
print(metrics.mean_squared_error(test.label,pred))