from sklearn import datasets
import xgboost as xgb
import xgboost as xgb2
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics

# 加载数据
cancer = datasets.load_breast_cancer()
X = cancer.data
y = cancer.target
# 划分训练集、测试集
X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size = 1/5,random_state = 8)
# 加载乳腺癌数据
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn import metrics
# 决策树
clf = tree.DecisionTreeClassifier(max_depth=4)
# 训练模型
clf.fit(X_train,y_train)

# 预测
y_pred = clf.predict(X_test)

# 评估预测效果
print(classification_report(y_test, y_pred, target_names=['Benign','Malignant']))
print(metrics.accuracy_score(y_test, y_pred))



xgb_train = xgb.DMatrix(X_train, label=y_train)
xgb_test = xgb.DMatrix(X_test, label=y_test)

# 模型训练
params = {
    "objective": "binary:logistic",
    "booster": "gbtree",
    'eval_metric':'logloss',
    "eta": 0.1,
    "min_child_weight": 1,
    "max_depth": 5
}
num_round = 100
watchlist = [(xgb_train, 'train'), (xgb_test, 'test')]
model = xgb.train(params, xgb_train, num_round, watchlist,early_stopping_rounds=10)
print('提前停止。。。')
print('model.best_score：',model.best_score)
print('model.best_ntree_limit：',model.best_ntree_limit)
print('model.best_iteration：',model.best_iteration)
