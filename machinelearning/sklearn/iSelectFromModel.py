import xgboost as xgb
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd


from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LassoCV,Lasso,Ridge,RidgeCV
import matplotlib.pyplot as plt
# ==============================================
X = [[0.87, -1.34, 0.31],[-2.79, -0.02, -0.85],[-1.34, -0.48, -2.55],[1.92, 1.48, 0.65]]
y = [0, 1, 0, 1]
selector = SelectFromModel(estimator=LogisticRegression()).fit(X, y)

print(selector.estimator_.coef_)
print(selector.threshold_)
print(selector.get_support())
print(selector.transform(X))
'''
[[-0.3252302   0.83462377  0.49750423]]
0.5524527319086916
[False  True False]
[[-1.34]
 [-0.02]
 [-0.48]
 [ 1.48]
'''
print('==================LogisticRegression============================')
logre = LogisticRegression()
logre.fit(X,y)
print(logre.coef_)
print(logre.intercept_)
print('==============================================')

print('===================load_diabetes===========================')
diabetes = datasets.load_diabetes()

X = diabetes.data
y = diabetes.target
feature_names = diabetes.feature_names
print(feature_names)
print('===========LassoCV===================================')
LassoCV = LassoCV().fit(X, y)
importance = np.abs(LassoCV.coef_)
print(importance)
print(LassoCV.coef_)

# print(importance.argsort())
# idx_third = importance.argsort()[-3]
# threshold = importance[idx_third] + 0.01
#
# idx_features = (-importance).argsort()[:2]
# name_features = np.array(feature_names)[idx_features]
# print('Selected features: {}'.format(name_features))
# sfm = SelectFromModel(LassoCV, threshold=threshold)
# sfm.fit(X, y)
# X_transform = sfm.transform(X)


print('==============Lasso================================')
Lasso = Lasso().fit(X, y)
importance = np.abs(Lasso.coef_)
print(importance)
print(Lasso.coef_)
print('==============Ridge================================')
Ridge = Ridge().fit(X, y)
importance = np.abs(Ridge.coef_)
print(importance)
print(Ridge.coef_)
print('==============RidgeCV================================')
RidgeCV = RidgeCV().fit(X, y)
importance = np.abs(RidgeCV.coef_)
print(importance)
print(RidgeCV.coef_)

'''
[  0.           0.         367.70185207   6.30190419   0.
   0.           0.           0.         307.6057       0.        ]
[  0.          -0.         367.70185207   6.30190419   0.
   0.          -0.           0.         307.6057       0.        ]
'''

#
#
# plt.title(
#     "Features from diabets using SelectFromModel with "
#     "threshold %0.3f." % sfm.threshold)
# feature1 = X_transform[:, 0]
# feature2 = X_transform[:, 1]
# plt.plot(feature1, feature2, 'r.')
# plt.xlabel("First feature: {}".format(name_features[0]))
# plt.ylabel("Second feature: {}".format(name_features[1]))
# plt.ylim([np.min(feature2), np.max(feature2)])
# plt.show()

# ===============================================
print('# ===============================================')
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import load_boston
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LassoCV

# Load the boston dataset.
X, y = load_boston(return_X_y=True)

# We use the base estimator LassoCV since the L1 norm promotes sparsity of features.
clf = LassoCV()

# Set a minimum threshold of 0.25
sfm = SelectFromModel(clf, threshold=0.25)
sfm.fit(X, y)
n_features = sfm.transform(X).shape[1]

print()
# Reset the threshold till the number of features equals two.
# Note that the attribute can be set directly instead of repeatedly
# fitting the metatransformer.
while n_features > 2:
    sfm.threshold += 0.1
    X_transform = sfm.transform(X)
    n_features = X_transform.shape[1]

# Plot the selected two features from X.
plt.title(
    "Features selected from Boston using SelectFromModel with "
    "threshold %0.3f." % sfm.threshold)
feature1 = X_transform[:, 0]
feature2 = X_transform[:, 1]
plt.plot(feature1, feature2, 'r.')
plt.xlabel("Feature number 1")
plt.ylabel("Feature number 2")
plt.ylim([np.min(feature2), np.max(feature2)])
plt.show()

print('# ===============================================')
print('# ===============================================')
print('# ===============================================')
# ===============================================
# ===============================================

# oriData = datasets.load_breast_cancer()
oriData = datasets.load_boston()
X = oriData.data
y = oriData.target

X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size = 1/5.,random_state = 8)

# xgb_train = xgb.DMatrix(X_train, label=y_train)
# xgb_test = xgb.DMatrix(X_test, label=y_test)
#
# params = {
#     "objective": "reg:squarederror",
#     # "objective": "binary:logistic",
#     "booster": "gbtree",
#     "eval_metric":"logloss",
#     "eta": 0.1,
#     "max_depth": 5
# }
# num_round = 50
#
#
# watchlist = [(xgb_test,'eval'), (xgb_train,'train')]
#
# bst = xgb.train(params, xgb_train, num_round, watchlist)

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn import tree

linrg = LinearRegression()
linrg.fit(X_train,y_train)
#
# logrg = LogisticRegression()
# logrg.fit(X_train,y_train)

# treecf = tree.DecisionTreeClassifier()
# treecf.fit(X_train,y_train)

# treerg = tree.DecisionTreeRegressor()
# treerg .fit(X_train,y_train)
# sklearn.exceptions.NotFittedError: Since 'prefit=True', call transform directly
# selector_linrg = SelectFromModel(estimator=linrg,prefit=True).fit(X_train,y_train)
# selector_linrg1 = SelectFromModel(estimator=linrg,max_features=3).fit_transform(X_train,y_train)
# print(selector_linrg1)
# # selector = SelectFromModel(estimator=LogisticRegression()).fit(X, y)
# print(selector_linrg1.estimator_.coef_)
# print(selector_linrg1.threshold_)
# print(selector_linrg1.get_support())
# print(selector_linrg1.transform(X_train))

