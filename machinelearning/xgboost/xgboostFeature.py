'''
class sklearn.feature_selection.SelectFromModel(estimator, threshold=None,
prefit=False, norm_order=1)[source]


·estimator：构建transformer的基础estimator。estimator既可以是已拟合的（如果prefit设置为True），也可以是未拟合的，拟合过的estimator需要包含feature_importances_或coef_属性。

·threshold：特征提取的阈值。当特征重要性取值大于等于该阈值时，特征被选取，否则被丢弃。该参数可以是数值类型，也可以是字符串形式，如果设为"median"，则表示该阈值取值为特征重要性的中位数；设为"mean"，表示取值为特征重要性的平均值。另外，还可以加扩展因子，如"1.25*mean"。当参数为None时，如果estimator有L1正则参数，则默认使用阈值1e-5；如果没有L1正则参数，则默认使用"mean"。

·prefit：是否为预装模型，直接传给构造函数，如果设置为True，则必须直接调用transform，并且SelectFromModel不能和cross_val_score、GridSearchCV、克隆estimator的类似工具一起使用。如果设置为False，则先通过fit训练模型，再调用transform进行特征选择。

·norm_order：范数的阶，当estimator的coef_属性为二维时，用于过滤低于阈值的系数向量
'''

import xgboost as xgb
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import metrics
from sklearn.feature_selection import SelectFromModel
from decimal import *

cancer = datasets.load_breast_cancer()
X = cancer.data
y = cancer.target

X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size = 1/5.,random_state = 8)

model = xgb.XGBClassifier(max_depth=5, learning_rate=0.1,
                      n_estimators=50,use_label_encoder=False,
                      objective='binary:logistic', booster='gbtree')

model.fit(X_train, y_train,eval_metric='logloss')

# 对测试集进行预测，并计算AUC
y_pred = model.predict(X_test)
auc = metrics.roc_auc_score(y_test, y_pred)
print("AUC得分： %.2f" % (auc))

# 获取特征重要性评分
importances = model.feature_importances_

print(importances)
# 对特征重要性去重后作为候选阈值
thresholds = []
for importance in importances:
    print(Decimal(importance.astype(float)))
    if importance not in thresholds:
        thresholds.append(importance)
# 候选阈值排序
thresholds = sorted(thresholds)
print(thresholds)
# 遍历候选阈值
c=0
for threshold in thresholds:
    c+=1
    # 通过threshold进行特征选择
    selection = SelectFromModel(model, threshold=threshold, prefit=True)
    select_X_train = selection.transform(X_train)
    # 训练模型
    selection_model = xgb.XGBClassifier(max_depth=5, learning_rate=0.1,use_label_encoder=False,
                     n_estimators=50,objective='binary:logistic', booster='gbtree')
    selection_model.fit(select_X_train, y_train,eval_metric='logloss')

    # 评估模型
    select_X_test = selection.transform(X_test)
    y_pred = selection_model.predict(select_X_test)
    auc = metrics.roc_auc_score(y_test, y_pred)
    f1 = metrics.f1_score(y_test, y_pred)
    print(c,"阈值：%.3f, 特征数量：%d, AUC得分： %.2f ,f1得分： %.4f" % (threshold, select_X_train.shape[1], auc,f1))


selection = SelectFromModel(model, threshold=0.05, prefit=True)
select_X_train = selection.transform(X_train)
print(selection.get_support())
print(selection.get_support(True))
index =list(selection.get_support(True))
for i in index:
    print(type(i))
    ii = int(i)
    print(type(ii))
    print(ii)

