import xgboost as xgb
'''
booster为gbtree表示采用XGBoost中的树模型。
参数eta表示学习率，类似于梯度下降中法的α，每次迭代完更新权重的步长。
参数gamma表示节点分裂时损失函数减小的最小值，此处为1.0，表示损失函数至少下降1.0该节点才会进行分裂。
参数min_child_weight表示叶子节点最小样本权重和，若节点分裂导致叶子节点的样本权重和小于该值，则节点不进行分裂。
参数max_depth表示决策树分裂的最大深度。
'''
xgb_train = xgb.DMatrix("dataFile/agaricus.txt.train")
xgb_test = xgb.DMatrix("dataFile/agaricus.txt.test")
# 模型训练
params = {
    "objective": "binary:logistic",
    "booster": "gbtree",
    "eval_metric":"logloss",
    "eta": 1.0,
    "gamma": 1.0,
    "min_child_weight": 1,
    "max_depth": 3
}

num_round = 2
watchlist = [(xgb_train, 'train'), (xgb_test, 'test')]

model = xgb.train(params, xgb_train, num_round, watchlist)

# 模型训练完成之后，可通过save_model方法将模型保存成模型文件，以供后续预测使用
model.save_model("dataFile/agaricus.model")
# 加载模型进行预测
bst = xgb.Booster()
bst.load_model("dataFile/agaricus.model")
pred = bst.predict(xgb_test)

print(pred)
# 输出结果是一个浮点数组成的数组，其中每个值代表对应样本的预测概率。预测完成后，输出文本格式的模型，
# 输出文本格式的模型（未做特征名称转换）
dump_model = bst.dump_model("dataFile/dump.raw.txt")
# 输出文本格式的模型（完成特征名称转换）
dump_model = bst.dump_model("dataFile/dump.nice.txt", "dataFile/featmap.txt")