import numpy as np
import pandas as pd
import matplotlib
import metrics
import sklearn
import xgboost


'''
metrics.confusion_matrix(y_true, y_pred, labels=None, sample_weight=None)
metrics.accuracy_score(y_true,y_pred)
metrics.average_precision_score(y_true, y_score, average='macro', sample_weight=None)
metrics.precision_score(y_true, y_pred, labels=None, pos_label=1, average='binary',)
metrics.recall_score(y_true, y_pred, labels=None, pos_label=1, average='binary', sample_weight=None)
metrics.f1_score(y_true, y_pred, labels=None, pos_label=1, average='binary', sample_weight=None)
precision,recall,thresholds=metrics.precision_recall_curve(y_true,y_pred)
>>> plt.plot(recall, precision)
fpr,tpr,thresholds = metrics.roc_curve(y_true, y_ pred, pos_label=None, sample_weight=None, drop_intermediate=True)
>>> plt.plot(fpr,tpr)

metrics.roc_auc_score(y_true, y_pred, average='macro', sample_weight=None)
metrics.auc(fpr, tpr)

metrics.mean_absolute_error(y_true, y_pred, sample_weight=none, multioutput='uniform_average')
metrics.mean_squared_error(y_true, y_pred, sample_weight=None, multioutput='uniform_average')
metrics.r2_score(y_true, y_pred, sample_weight=None, multioutput='uniform_average')
'''

def classificationModel(y_true,y_pred):
    nameValueDict={}
    #混淆矩阵
    confusionMatrix = metrics.confusion_matrix(y_true, y_pred)
    #准确率
    accuracyScore = metrics.accuracy_score(y_true, y_pred)
    #精确率
    precisionScore = metrics.precision_score(y_true, y_pred)
    #召回率
    recallScore = metrics.recall_score(y_true, y_pred)
    #f1
    f1Score = metrics.f1_score(y_true, y_pred)

    nameValueDict.update({})
    #pr曲线
    precision,recall,thresholds = metrics.precision_recall_curve(y_true,y_pred)

    matplotlib.plt.plot(recall, precision)
    fpr, tpr, thresholds = metrics.roc_curve(y_true, y_pred,drop_intermediate = True)
    # >> > plt.plot(fpr, tpr)

    rocAucScore = metrics.roc_auc_score(y_true, y_pred)
    aucArea = metrics.auc(fpr, tpr)

    nameValueDict.update({'accuracyScore':accuracyScore})
    nameValueDict.update({'precisionScore':precisionScore})
    nameValueDict.update({'recallScore':recallScore})
    nameValueDict.update({'f1Score':f1Score})
    nameValueDict.update({'auc':metrics.auc(fpr, tpr)})
    nameValueDict.update({'accuracyScore':accuracyScore})
    nameValueDict.update({'aucArea':aucArea})

    return nameValueDict


def regressionModel(y_true,y_pred):

    nameValueDict = {}
    MAE = metrics.mean_absolute_error(y_true, y_pred)
    MSE = metrics.mean_squared_error(y_true, y_pred)
    r2 = metrics.r2_score(y_true, y_pred)

    nameValueDict.update({'MAE':MAE})
    nameValueDict.update({'MSE':MSE})
    nameValueDict.update({'r2':r2})
    return nameValueDict


def entU(u):

    return [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(u, return_counts=True)[1]]][0]

#条件熵
def uConditionV(u,v):

    entu = [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(u, return_counts=True)[1]]][0]
    entv = [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(v, return_counts=True)[1]]][0]

    # v 解释变量
    vid, vct = np.unique(v, return_counts=True)

    # 条件信息
    vidEntropy = [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(u[v == i], return_counts=True)[1] for i in vid]]

    #条件熵
    entUconditonV= np.sum(np.array(vidEntropy) * (vct / np.sum(vct)))

    return entUconditonV

#信息增益
def gainuv(u,v):

    return entU(u) - uConditionV(u,v)

def gainRatio(u, v):
    return gainuv(u,v) / entU((v))

def display_version():
    print('np.version : ',np.__version__)
    print('pd.version : ',pd.__version__)
    print('matplotlib.version : ',matplotlib.__version__)
    print('sklearn.version : ',sklearn.__version__)
    print('xgboost.version : ',xgboost.__version__)

display_version()

#数据查看tool
def overview(data):

    print('\n======================= data overview =======================\n')

    print('\n重复行数 : ',data.duplicated().sum(axis=0))
    print('重复记录为：')
    print(data[data.duplicated()])

    print('\n数据总体缺失情况 : ')
    print('总记录数 : ',data.shape[0])
    print('\n各列没有缺失的样本数量：')
    print(data.notnull().sum())
    print('\n各列缺失的样本数量：')
    print(data.isnull().sum())
    print('\n各列缺失比例')
    print(data.isnull().mean())

    print('\n缺失行\n')
    print(data.loc[data.isnull().sum(axis=1)>0,:])
    print('\n缺失列\n')
    print(data.loc[:,data.isnull().sum(axis=0)>0])
    print('\n缺失区域【缺失行+缺失列】\n')
    print(data.loc[data.isnull().sum(axis=1) > 0, data.isnull().sum(axis=0) > 0])

    print('\n\n')
    print('\n所在列及缺失的行索引号\n')
    for i in data.columns:
        print(i,' : ',list(np.where(pd.isna(data[i]))[0]))
    print('\n\n')

def basicOperate(data):
    print('\n\n')
    print('\n删除重复行\n')
    data.drop_duplicates(inplace=True)
    print('\n\n')
    print('\n\n')
    print('\n\n')

def dropRank(data,thresh):
    threshold = thresh
    print('显示空值个数大于 {} 的行,这些行，予以删除'.format(data.shape[1] - threshold))
    print(data.loc[data.isnull().sum(axis=1) > data.shape[1] - threshold])
    print('=======================================')
    print(data.loc[data.isnull().sum(axis=1) == data.shape[1] - threshold])
    print('=======================================')
    print('显示非空个数大于等于 {} 的行，这些行，予以保留'.format(threshold))
    print(data.dropna(thresh=threshold))
    data.dropna(thresh=threshold,inplace=True)
