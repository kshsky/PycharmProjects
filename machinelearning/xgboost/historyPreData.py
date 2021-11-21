import xgboost as xgb
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

cancer = datasets.load_breast_cancer()
X = cancer.data
y = cancer.target

X_train, X_test, y_train, y_test = train_test_split(X, y , test_size = 1/5.,random_state = 8)

xgb_train = xgb.DMatrix(X_train, label=y_train)
xgb_train2 = xgb.DMatrix(X_train, label=y_train)
xgb_test = xgb.DMatrix(X_test, label=y_test)


watchlist  = [(xgb_test,'eval'), (xgb_train,'train')]
###
# 在初始预测值的基础上开始训练
#
# 指定训练参数
params = {
    "objective": "binary:logistic",
    "booster": "gbtree",
    'eval_metric':'logloss',
    "eta": 0.1,
    "max_depth": 5
}

# 训练模型，此处num_round设为10
bst = xgb.train(params, xgb_train, 10, watchlist )

# 通过上述模型对数据集进行预测
# 此处output_margin参数设为True，表示最终输出的预测值为未进行sigmoid转化的原始值
pred_train = bst.predict(xgb_train, output_margin=True)
pred_test  = bst.predict(xgb_test, output_margin=True)

# 设置预测值为初始值，这里设置的初始值需是未转化前的原始值
xgb_train.set_base_margin(pred_train)
xgb_test.set_base_margin(pred_test)

print ('以下是设置初始预测值后的运行结果：')
bst = xgb.train( params, xgb_train, 10, watchlist )
print('num_round=20')
bst = xgb.train( params, xgb_train2, 20, watchlist )