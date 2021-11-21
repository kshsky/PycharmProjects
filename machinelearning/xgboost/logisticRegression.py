from sklearn import datasets
from sklearn import metrics

# 加载乳腺癌数据
from sklearn.metrics import classification_report

cancer = datasets.load_breast_cancer()
X = cancer.data
y = cancer.target
print(y)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size =1/5.,random_state = 20)
'''
class sklearn.linear_model.LogisticRegression(penalty='l2', dual=False,tol=0.0001, C=1.0, 
fit_intercept=True, intercept_scaling=1,class_weight=None,random_state=None, solver='liblinear', 
max_iter=100, multi_class='ovr',verbose=0, warm_start=False, n_jobs=1)
'''

from sklearn.linear_model import LogisticRegression

# 逻辑回归
lr = LogisticRegression(max_iter=10000)
# 训练模型
lr.fit(X_train, y_train)
# 预测
y_pred = lr.predict(X_test)

print(classification_report(y_test, y_pred, target_names=['Benign','Malignant']))
print(metrics.accuracy_score(y_test, y_pred))

import pandas as pd
import xgboost as xgb
import numpy as np
# 将数据转化为DMatrix格式
train_xgb = xgb.DMatrix(X_train, y_train)
num_round = 50
params = {"objective": "reg:logistic", "booster":"gblinear"}

model = xgb.train(dtrain=train_xgb,params=params,early_stopping_rounds=1)
print(model.best_score,model.best_iteation)
y_pred = model.predict(xgb.DMatrix(X_test))
print(y_pred)
#将概率大于0.5的预测分类标记为1，否则为0
ypred_bst = np.array(y_pred)
ypred_bst = ypred_bst > 0.5
ypred_bst = ypred_bst.astype(int)
print(ypred_bst)