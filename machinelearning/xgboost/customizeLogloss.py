###
# 自定义目标函数
#
import xgboost as xgb
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

cancer = datasets.load_breast_cancer()
X = cancer.data
y = cancer.target

X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size =1/5.,random_state = 8)

xgb_train = xgb.DMatrix(X_train, label=y_train)
xgb_test = xgb.DMatrix(X_test, label=y_test)

watchlist  = [(xgb_test,'eval'), (xgb_train,'train')]
# 因为要自定义目标函数，此处objective不再指定

params = {
    "booster": "gbtree",
    "eta": 0.1,
    "max_depth": 5
}
num_round = 50


# 自定义目标函数logloss，给定预测值，返回一阶、二阶梯度
def logregobj(preds, dtrain):
    labels = dtrain.get_label()
    preds = 1.0 / (1.0 + np.exp(-preds))
    grad = preds - labels
    hess = preds * (1.0-preds)
    return grad, hess


# 用户自定义评估函数，返回指标名称和结果
def evalerror(preds, dtrain):
    labels = dtrain.get_label()
    # 因为是未进行sigmoid转换的，因此以0作为分类阈值
    return 'error', float(sum(labels != (preds > 0.0))) / len(labels)

# 通过自定义目标函数进行训练
bst = xgb.train(params, xgb_train, num_round, watchlist, obj = logregobj,feval = evalerror)