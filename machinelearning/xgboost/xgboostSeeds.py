'''

XGBoost中解决多分类问题的主要参数如下。

1）num_class：说明在该分类任务的类别数量。

2）objective：该参数中的multi:softmax和multi:softprob均是指定学习任务为多分类。
multi:softmax通过softmax函数解决多分类问题。
multi:softprob和multi:softmax一样，主要区别在于其输出的是一个ndata*nclass向量，表示样本属于每个分类的预测概率。

3）eval_metric：与多分类相关的评估函数有merror和mlogloss。
merror也称多分类错误率，通过判断样本所有分类预测值中预测值最大的分类和样本label是否一致来确定预测是否正确，其计算方式和error相似。
mlogloss也是多分类问题中常用的评估指标。

'''
# 已知小麦种子数据集包含7个特征，分别为面积、周长、紧凑度、籽粒长度、籽粒宽度、不对称系数、籽粒腹沟长度，且均为连续型特征，以及小麦类别字段，共有3个类别，分别用1、2、3表示

import pandas as pd
import xgboost as xgb
import numpy as np
from sklearn import metrics

# 使label取值在0到num_class -1范围内
data = pd.read_csv('dataFile/seeds_dataset.txt', header=None, sep='\s+', converters={7: lambda x:int(x) - 1})

# 将最后一列字段名设置为label
data.rename(columns={7:'label'}, inplace=True)
print(data.head())
print(data.shape)

# 生成一个随机数并选择小于0.8的数据
mask = np.random.rand(len(data)) < 0.8
train = data[mask]
test = data[~mask]

# 生成DMatrix
xgb_train = xgb.DMatrix(train.iloc[:, :6], label=train.label)
xgb_test = xgb.DMatrix(test.iloc[:, :6], label=test.label)
# 设置模型训练参数。设置参数objective为multi:softmax，表示采用softmax进行多分类，

# 通过softmax进行多分类
params = {
    'objective': 'multi:softmax',
    'eval_metric':'mlogloss',
    'eta': 0.1,
    'max_depth': 5,
    'num_class': 3
}

watchlist = [(xgb_train, 'train'), (xgb_test, 'test')]
num_round = 50
bst = xgb.train(params, xgb_train, num_round, watchlist)
# 模型预测
pred = bst.predict(xgb_test)
error_rate = np.sum(pred != test.label) / test.shape[0]
print('测试集错误率（softmax）：{}'.format(error_rate))
print(metrics.accuracy_score(test.label,pred))

# 采用multi:softprob方法重新训练模型
# 重新训练模型，输出概率值
params['objective'] = 'multi:softprob'
bst = xgb.train(params, xgb_train, num_round, watchlist)
# 模型预测
pred_prob = bst.predict(xgb_test)
print(pred_prob)

# 取向量中预测值最大的分类作为预测类别
pred_label = np.argmax(pred_prob, axis=1)
print(pred_label)
print(metrics.accuracy_score(test.label,pred_label))
# 计算测试集错误率
error_rate = np.sum(pred_label != test.label) / test.shape[0]
print('测试集错误率（softprob）：{}'.format(error_rate))