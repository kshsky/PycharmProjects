import xgboost as xgb
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

print(metrics.classification_report(y_test, y_pred, target_names=['Benign','Malignant']))
print(metrics.accuracy_score(y_test, y_pred))
#=========================
from sklearn import tree
# 决策树
clf = tree.DecisionTreeClassifier(max_depth=4)
# 训练模型
clf.fit(X_train,y_train)
# 预测
y_pred = clf.predict(X_test)
print(metrics.classification_report(y_test, y_pred, target_names=['Benign','Malignant']))
print(metrics.accuracy_score(y_test, y_pred))

import graphviz
'''
sklearn.tree.export_graphviz(decision_tree, out_file=None, *, max_depth=None, 
feature_names=None, class_names=None, 
label='all', filled=False, leaves_parallel=False, 
impurity=True, node_ids=False, proportion=False, rotate=False, 
rounded=False, special_characters=False, precision=3,
fontname='helvetica')[source]¶
'''
dot_data = tree.export_graphviz(clf, out_file="dataFile/breastCancerTree.dot",
                         feature_names=cancer.feature_names,
                         class_names=cancer.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
graph = graphviz.Source(dot_data)

#渲染dot文件
from graphviz import Source
path = 'dataFile/breastCancerTree.dot'
# s = Source.from_file(path,format='png')
#默认format='pdf'
# s = Source.from_file(path)
# s.view()
#=======================================================
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
# 存储为二进制文件
xgb_test.save_binary('dataFile/binary_breast_cancer_test.buffer')

# 重新加载数据
xgb_test2 = xgb.DMatrix('dataFile/binary_breast_cancer_test.buffer')

# 用新数据预测
pred2 = model.predict(xgb_test2)
# print(pred2)

resultClass = np.array(pred2) >0.5
y_pred = resultClass.astype(int)
print(metrics.accuracy_score(y_test,y_pred))
print(metrics.classification_report(y_test,y_pred))

print('=================评价特征对单个样本的影响==========================')

# 以SHAP方法为例，其调用方法非常简单，只需在执行predict函数时将参数pred_contribs设置为True即可
pred_contribs = model.predict(xgb_test, pred_contribs=True)
print(pred_contribs)
# XGBoost还支持SHAP方法对任意两两交叉特征贡献值的评估，只需将参数pred_interactions置为True即可
pred_interactions = model.predict(xgb_test, pred_interactions=True)
# XGBoost还支持另外一种单样本归因方法Sabbas。相比SHAP方法，Sabbas实现简单、容易理解，但其弊端也是不可忽视的，即容易产生不一致的问题
approx_contribs = model.predict(xgb_test, pred_contribs=True, approx_contribs=True)
print(approx_contribs)


print('==================生成二叉树=========================')
import matplotlib.pyplot as plt
# def plot_tree(booster, fmap='', num_trees=0, rankdir=None, ax=None, **kwargs):
model = xgb.train(params, xgb_train, num_round, watchlist,early_stopping_rounds=10)
xgb.plot_tree(model, num_trees=1)
plt.show()