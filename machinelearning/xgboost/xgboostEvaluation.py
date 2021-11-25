'''
XGBoost提供了两个获取特征重要性评分的方法：get_fscore和get_score。
get_fscore() = get_score(importance_type='weight')
-----------------------------------------------------------
def get_score(self, fmap='', importance_type='weight'):
    """Get feature importance of each feature.
    Importance type can be defined as:

    * 'weight': the number of times a feature is used to split the data across all trees.
    * 'gain': the average gain across all splits the feature is used in.
    * 'cover': the average coverage across all splits the feature is used in.
    * 'total_gain': the total gain across all splits the feature is used in.
    * 'total_cover': the total coverage across all splits the feature is used in.

    .. note:: Feature importance is defined only for tree boosters

        Feature importance is only defined when the decision tree model is chosen as base
        learner (`booster=gbtree`). It is not defined for other base learner types, such
        as linear learners (`booster=gblinear`).
'''

import xgboost as xgb
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd

cancer = datasets.load_breast_cancer()
X = cancer.data
y = cancer.target

X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size = 1/5.,random_state = 8)

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

fscore = bst.get_fscore()
weight = bst.get_score(importance_type='weight')
gain = bst.get_score(importance_type='gain')
cover = bst.get_score(importance_type='cover')
total_gain = bst.get_score(importance_type='total_gain')
total_cover = bst.get_score(importance_type='total_cover')

print(weight)
print(gain)
print(total_gain)
print(cover)
print(total_cover)
columns =['weight','gain','total_gain','cover','total_cover']
weightList=[]
gainList=[]
coverList=[]
total_gain_list = []
total_cover_list=[]
feature_list =[]
fscore_list = []
for i in weight.keys():
    feature_list.append(i)
    weightList.append(weight.get(i))
    gainList.append(gain.get(i))
    coverList.append(cover.get(i))
    total_gain_list.append(total_gain.get(i))
    total_cover_list.append(total_cover.get(i))
    fscore_list.append(fscore.get(i))

evaluationData = pd.DataFrame({'feature':feature_list,'weight':weightList,'gain':gainList,'cover':coverList,
                               'total_gain':total_gain_list,'toal_cover':total_cover_list,'fscore':fscore_list})
print(evaluationData.head(25))
print(evaluationData.sort_values(by=['fscore'],ascending=False))
importance_ = [i/np.sum(evaluationData['fscore']) for i in evaluationData['fscore']]
evaluationData['importance']=importance_
print(evaluationData.sort_values('fscore',ascending=False))
# ==================================================
'''
xgboost.plot_importance(booster, 
ax=None, 
height=0.2, 
xlim=None, 
ylim=None, 
title='Feature importance', 
xlabel='F score', 
ylabel='Features', 
importance_type='weight', 
max_num_features=None, 
grid=True, 
show_values=True, 
**kwargs)
'''
import matplotlib.pyplot as plt
# xgb.plot_importance(bst)
# xgb.plot_importance(bst,importance_type='gain',xlabel='gain score')
# xgb.plot_importance(bst,importance_type='cover',xlabel='cover score')
# xgb.plot_importance(bst,importance_type='total_gain',xlabel='total_gain score')
# xgb.plot_importance(bst,importance_type='total_cover',xlabel='total_cover score')
xarr = np.ones_like(evaluationData['importance'])
plt.bar(evaluationData['feature'],evaluationData['importance'])

plt.show()