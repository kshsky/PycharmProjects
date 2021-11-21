import scipy
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

#========================================================
row = []; col = []; dat = []
i = 0
# 解析数据文件
for arr in X_train:
    # 获取数据中元素的行号、列号及取值
    for k, v in enumerate(arr):
        row.append(i);col.append(int(k));dat.append(float(v))
    i += 1

# 构造CSR
csr = scipy.sparse.csr_matrix((dat, (row, col)))
# 加载CSR格式数据，并将其转为DMatrix
xgb_train = xgb.DMatrix(csr, label=y_train)
watchlist = [(xgb_test, 'eval'), (xgb_train, 'train')]
bst = xgb.train(params, xgb_train, num_round, watchlist)

# 构造CSC格式数据
csc = scipy.sparse.csc_matrix((dat, (row, col)))
xgb_train = xgb.DMatrix(csc, label=y_train)
watchlist = [(xgb_test, 'eval'), (xgb_train, 'train')]
bst = xgb.train(params, xgb_train, num_round, watchlist)

# 将CSR格式转为numpy array格式
nparr = csr.todense()
# 加载numpy array，并将其转为DMatrix
xgb_train = xgb.DMatrix(nparr, label = y_train)
watchlist  = [(xgb_test,'eval'), (xgb_train,'train')]
bst = xgb.train(params, xgb_train, num_round, watchlist)