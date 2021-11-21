import xgboost as xgb
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn import datasets
from sklearn.model_selection import train_test_split

cancer = datasets.load_breast_cancer()
X = cancer.data
y = cancer.target

X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size =1/5.,random_state = 8)

xgb_train = xgb.DMatrix(X_train, label=y_train)
xgb_test = xgb.DMatrix(X_test, label=y_test)

watchlist  = [(xgb_test,'eval'), (xgb_train,'train')]

params = {
    "objective": "binary:logistic",
    "booster": "gbtree",
    'eval_metric':'logloss',
    "eta": 0.1,
    "max_depth": 5
}
num_round = 50


watchlist = [(xgb_test,'eval'), (xgb_train,'train')]
# 定义dict类型的变量存储评估结果
evals_result = {}
bst = xgb.train(params, xgb_train, num_round, watchlist, evals_result=evals_result)
print(evals_result.keys())
print(evals_result['eval'])
print(evals_result['train'])


xgb_train = xgb.DMatrix(X_train, label=y_train)
xgb_test = xgb.DMatrix(X_test, label=y_test)

params = {
    "objective": "binary:logistic",
    "booster": "gbtree",
    "eta": 0.1,
    "max_depth": 5
}
num_round = 50
watchlist = [(xgb_test,'eval'), (xgb_train,'train')]

bst = xgb.train(params, xgb_train, num_round, watchlist)
# =======================================================================
print ('通过前n棵树进行预测')
# 使用前10棵树进行预测
label = xgb_test.get_label()
pred1 = bst.predict(xgb_test, iteration_range=(1,11))
# iteration_range: Tuple[int, int] = (0, 0),

# 默认情况使用所有决策树预测
pred2 = bst.predict(xgb_test)
print ('前10棵树预测值AUC为：%f' % roc_auc_score(y_test,pred1))
print ('所有树预测值AUC为：%f' % roc_auc_score(y_test,pred2))

