import xgboost as xgb
import pandas as pd

#pandas读取默认会将第一行读取为columns列名，取消第一行读取为列名：header=None
oriData = pd.read_csv('dataFile/agaricus-lepiota.data',header=None)
x = oriData.iloc[:,1:]
y = oriData.iloc[:,1]

# oriData = xgb.DMatrix('dataFile/agaricus-lepiota.data')
# dtrain = xgb.DMatrix('demo/data/agaricus.txt.train')
# dtest = xgb.DMatrix('demo/data/agaricus.txt.test')
# # specify parameters via map
# param = {'max_depth':2, 'eta':1, 'objective':'binary:logistic' }
# num_round = 2
# bst = xgb.train(param, dtrain, num_round)
# # make prediction
# preds = bst.predict(dtest)
# print(oriData)


