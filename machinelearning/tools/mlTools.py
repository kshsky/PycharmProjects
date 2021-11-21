import numpy as np
import pandas as pd
import matplotlib
import metrics
import sklearn
import xgboost
from sklearn import metrics
from decimal import *
import graphviz


'''
新細明體：PMingLiU
細明體：MingLiU
標楷體：DFKai-SB
黑体：SimHei
宋体：SimSun
新宋体：NSimSun
仿宋：FangSong
楷体：KaiTi
仿宋_GB2312：FangSong_GB2312
楷体_GB2312：KaiTi_GB2312
微軟正黑體：Microsoft JhengHei
微软雅黑体：Microsoft YaHei
————————————————

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


用于多分类，只有两个属性可以选择 ‘macro’ 和 ‘weighted’ 
' macro '：计算每个标签的指标，并计算它们的未加权平均值。不考虑样本类别是否平衡。
' weighted '：计算每个标签的指标，并找到它们的平均值，对(每个标签的真实实例的数量)进行加权。
'micro':整体计算TP、FN、FP，然后根据公式计算得分。
'''

def classificationModel(y_true,y_pred):
    nameValueDict={}
    #混淆矩阵
    confusionMatrix = metrics.confusion_matrix(y_true, y_pred)
    #准确率
    accuracyScore = metrics.accuracy_score(y_true, y_pred)
    #精确率
    precisionScore = metrics.precision_score(y_true, y_pred,average=None)
    #召回率
    recallScore = metrics.recall_score(y_true, y_pred,average=None)
    #f1 只对2分类问题有效
    # None, 'micro', 'macro', 'weighted'
    f1Score = metrics.f1_score(y_true, y_pred,average=None)

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
    # nameValueDict.update({'f1Score':f1Score})
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
    print('graphviz.version',graphviz.__version__)

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



# 离散型 gini系数 x是自变量，y是flag
def giniC(x, y):
    x_id, x_ct = np.unique(x, return_counts=True)
    p_x = [ct / sum(ct) for ct in [np.unique(x, return_counts=True)[1]]]
    gini = [1 - np.sum(p ** 2) for p in
            [ct / sum(ct) for ct in [np.unique(y[x == i], return_counts=True)[1] for i in x_id]]]


    return np.sum(np.array(p_x) * np.array(gini))

# 连续型 gini系数 x是自变量，y是flag
def giniS(y, x):
    # 将离散数据转成float
    x.astype(float)
    # 对离散数据排序
    sorted_x = np.sort(x)
    split_point_list = []
    split_point_gini = []
    # 求分界点
    for i in range(0, len(sorted_x) - 1, 1):
        split_point_list.append(np.mean([sorted_x[i], sorted_x[i + 1]]))

    # 依次计算每个分界点分割后的gini系数
    for i in split_point_list:
        # 分界后，就是二分类了
        xi = pd.Series.copy(x)
        xi[xi <= i] = 0
        xi[xi > i] = 1

        # 根据新分界点，计算权重（频数、概率）
        w_i = [[p for p in ct / np.sum(ct)] for ct in [np.unique(xi, return_counts=True)[1]]]

        # 分类
        x_id, x_ct = np.unique(xi, return_counts=True)

        # 每个分界点分类的gini
        gini_x_id = [np.sum([(p - p ** 2) for p in ct / np.sum(ct)]) for ct in
                     [np.unique(y[xi == i], return_counts=True)[1] for i in x_id]]

        # 计算每个分界点的gini
        gini = Decimal(str(np.sum(w_i * np.array(gini_x_id)))).quantize(Decimal('0.0000'),ROUND_HALF_UP)
        split_point_gini.append(gini)

    # 封装成字典
    split_point_gini_dict = dict(zip(split_point_list, split_point_gini))


    return split_point_gini_dict
