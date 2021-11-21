import xgboost as xgb

import numpy as np
from sklearn.model_selection import KFold, train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn import datasets
from sklearn.metrics import roc_auc_score

print("二分类，乳腺癌数据集")
cancer = datasets.load_breast_cancer()
X = cancer.data
y = cancer.target

kf = KFold(n_splits=3, shuffle=True)
i = 0
# objective="binary:logistic", use_label_encoder=True【默认需要将label转化成int格式】
for train_idx, test_idx in kf.split(X):
    model = xgb.XGBClassifier(use_label_encoder=False).fit(X[train_idx],y[train_idx],eval_metric='logloss')
    preds = model.predict(X[test_idx])
    labels = y[test_idx]
    print("kfold-%d AUC为：%f"% (i, roc_auc_score(labels, preds)))
    i += 1

print("回归，波士顿房价数据集")
boston = datasets.load_boston()
X = boston.data
y = boston.target
kf = KFold(n_splits=3, shuffle=True)
i = 0
for train_idx, test_idx in kf.split(X):
    model = xgb.XGBRegressor().fit(X[train_idx],y[train_idx],eval_metric='logloss')
    preds = model.predict(X[test_idx])
    labels = y[test_idx]
    print("kfold-%d MSE为：%f"% (i, mean_squared_error(labels, preds)))
    i += 1

'''
class XGBClassifier(XGBModel, XGBClassifierBase):
    # pylint: disable=missing-docstring,invalid-name,too-many-instance-attributes
    @_deprecate_positional_args
    def __init__(self, *, objective="binary:logistic", use_label_encoder=True, **kwargs):
        self.use_label_encoder = use_label_encoder
        super().__init__(objective=objective, **kwargs)

    @_deprecate_positional_args
    def fit(
        self,
        X,
        y,
        *,
        sample_weight=None,
        base_margin=None,
        eval_set=None,
        eval_metric=None,
        early_stopping_rounds=None,
        verbose=True,
        xgb_model=None,
        sample_weight_eval_set=None,
        base_margin_eval_set=None,
        feature_weights=None,
        callbacks=None
    ):


'''
# C:\Users\87754\AppData\Roaming\Python\Python38\site-packages\xgboost\sklearn.py:1146:
#  UserWarning: The use of label encoder in XGBClassifier is deprecated and will be removed in a future release.
#   To remove this warning, do the following:
#   1) Pass option use_label_encoder=False when constructing XGBClassifier object; and
#   2) Encode your labels (y) as integers starting with 0, i.e. 0, 1, 2, ..., [num_class - 1].
#   warnings.warn(label_encoder_deprecation_msg, UserWarning)
from sklearn.datasets import load_boston
from sklearn.model_selection import GridSearchCV
import xgboost as xgb

print("超参数调优")
cancer = datasets.load_breast_cancer()
X = cancer.data
y = cancer.target
model = xgb.XGBClassifier(use_label_encoder=False)
clf = GridSearchCV(model,
                   {'max_depth': [4,5,6],
                    'n_estimators': [20,50,70],
                    'learning_rate': [0.05,0.1,0.2]
                   })
clf.fit(X,y,eval_metric='logloss')
print(clf.best_score_)
print(clf.best_params_)
