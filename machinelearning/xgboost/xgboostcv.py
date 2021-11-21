import xgboost as xgb
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

cancer = datasets.load_breast_cancer()
X = cancer.data
y = cancer.target

X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size =1/5.,random_state = 8)

xgb_train = xgb.DMatrix(X_train, label=y_train)
xgb_test = xgb.DMatrix(X_test, label=y_test)

watchlist  = [(xgb_test,'eval'), (xgb_train,'train')]

params = {
    "objective": "binary:logistic",
    "booster": "gbtree",
    'eval_metric':'logloss',
    "eta": 0.1,
    "max_depth": 5
}
num_round = 50


# 进行交叉验证
res = xgb.cv(params,
             xgb_train,
             num_round,
             nfold=5,
             metrics={'auc'},
             seed = 0,
             callbacks=[xgb.callback.EvaluationMonitor(show_stdv=True)])

print('===========================')
# 交叉验证，不输出标准差，若5轮评估指标未提升则停止训练
res2 = xgb.cv(params,
              xgb_train,
              num_boost_round=50,
              nfold=5,
              metrics={'auc'},
              seed = 0,
              early_stopping_rounds=5,
              callbacks=[
                  xgb.callback.EvaluationMonitor(show_stdv=False),
                  xgb.callback.EarlyStopping(rounds=5)
              ])
print('======3======')
res3 = xgb.cv(params,
              xgb_train,
              num_round,
              nfold=5,
              metrics={'auc'}, seed = 0,
               callbacks=[xgb.callback.EvaluationMonitor(),
                          xgb.callback.EarlyStopping(rounds=3)])

'''
def cv(params, dtrain, num_boost_round=10, nfold=3, stratified=False, folds=None,
       metrics=(), obj=None, feval=None, maximize=None, early_stopping_rounds=None,
       fpreproc=None, as_pandas=True, verbose_eval=None, show_stdv=True,
       seed=0, callbacks=None, shuffle=True):
       
#强烈不建议的callbacks    
def _configure_deprecated_callbacks(
        verbose_eval, early_stopping_rounds, maximize, start_iteration,
        num_boost_round, feval, evals_result, callbacks, show_stdv, cvfolds):
        
        
model = XGBClassifier()  
eval_set = [(X_test, y_test)]  
model.fit(X_train, y_train, early_stopping_rounds=10, eval_metric="logloss", eval_set=eval_set, verbose=True)  
# make predictions for
'''
print('========customized===========')
# 自定义预处理函数
# 该函数的功能是设置参数scale_pos_weight，解决正负样本悬殊的问题
def fpreproc(xgb_train, xgb_test, params):
    label = xgb_train.get_label()
    ratio = float(np.sum(label == 0)) / np.sum(label==1)
    params['scale_pos_weight'] = ratio
    return (xgb_train, xgb_test, params)


# 交叉验证，调用自定义预处理函数
xgb.cv(params, xgb_train, num_round, nfold=5,
       metrics={'auc'}, seed = 0,
       fpreproc = fpreproc,
       callbacks=[xgb.callback.EvaluationMonitor()]

       )
print('===============customized=========================')
# 在交叉验证中自定义目标函数

# 定义dict类型的变量存储评估结果
evals_result = {}
def logregobj(preds, xgb_train):
    labels = xgb_train.get_label()
    preds = 1.0 / (1.0 + np.exp(-preds))
    grad = preds - labels
    hess = preds * (1.0-preds)
    return grad, hess
def evalerror(preds, xgb_train):
    labels = xgb_train.get_label()
    return 'error', float(sum(labels != (preds > 0.0))) / len(labels)

xgb.cv(params, xgb_train, num_round, nfold = 5, seed = 0,
       obj = logregobj, feval=evalerror,
       evals_result=evals_result,
       callbacks=[xgb.callback.EvaluationMonitor(show_stdv=True)])


print(evals_result)