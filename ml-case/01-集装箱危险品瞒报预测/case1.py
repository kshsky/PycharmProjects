from collections import Counter
import itertools

from flask import Flask
from hyperopt import hp, fmin, tpe
from hyperopt.base import Trials, STATUS_OK
from imblearn.over_sampling import SMOTE
from matplotlib._layoutbox import align
from numpy.random.mtrand import np
from pandas.core.frame import DataFrame
from pip._vendor.webencodings.tests import test_labels
from scipy.io import arff
from sklearn import datasets, preprocessing, metrics
from sklearn.cluster.k_means_ import KMeans
from sklearn.datasets.base import load_iris
from sklearn.datasets.samples_generator import make_blobs
from sklearn.decomposition.pca import PCA
from sklearn.ensemble.forest import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, \
    HashingVectorizer
from sklearn.feature_selection.variance_threshold import VarianceThreshold
from sklearn.linear_model.logistic import LogisticRegressionCV
from sklearn.linear_model.randomized_l1 import RandomizedLogisticRegression
from sklearn.metrics.classification import confusion_matrix, recall_score, \
    precision_score
from sklearn.metrics.ranking import roc_auc_score, roc_curve
from sklearn.model_selection._split import KFold, train_test_split
from sklearn.model_selection._validation import cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors.classification import KNeighborsClassifier
from sklearn.neural_network.multilayer_perceptron import MLPClassifier
from sklearn.preprocessing._encoders import OneHotEncoder
from sklearn.preprocessing.data import normalize, scale, MinMaxScaler
from sklearn.preprocessing.imputation import Imputer
from sklearn.preprocessing.label import LabelEncoder
from sklearn.svm.classes import SVC
from sklearn.tree.tree import DecisionTreeClassifier, ExtraTreeClassifier
from sklearn.tree import _tree
from treeinterpreter import treeinterpreter as ti
import waterfall_chart

import matplotlib.pyplot as plt
import missingno as msno
import pandas as pd
from paper.tree_interp_functions import plot_obs_feature_contrib
import seaborn as sns

paper = Flask(__name__)


@paper.route('/preprocessing')
def preprocessing1():
    data = pd.read_excel('E://09-PYTHON/preprocessing.xlsx')
    
    # data.CONSIGNEE[data.CONSIGNEE.isnull()] = data.SHIPPER[data.CONSIGNEE.isnull()]
    # 缺失值填充
    # data = missingData(data)
    # 箱图异常值处理
    # data = outlierDetection(data, "WEIGHT", 'IS_WT_ABNORMAL');
    # data = outlierDetection(data, "VOL", 'IS_VOL_ABNORMAL');
    # 联系人合作频率离散化
    data = coopLvlDiscretization(data, 'SH_COOP_QTY', 'SH_COOP_LVL', 5);
    # data = coopLvlDiscretization(data, 'CN_COOP_QTY', 'CN_COOP_LVL', 3);
    # data = coopLvlDiscretization(data, 'FW_COOP_QTY', 'FW_COOP_LVL', 3);
    # 编码处理
    # data = encoder(data)
    
    return data


def missingData(data):
    # 缺失值
    total = data.isnull().sum().sort_values(ascending=False)
    percent = (data.isnull().sum() / data.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    missing_data.head(20)
    # 无效矩阵的数据密集显示
    msno.matrix(data)
    # data.CONSIGNEE[data.CONSIGNEE.isnull()] = data.SHIPPER[data.CONSIGNEE.isnull()]
    return ""  # KNN(k=3).fit_transform(data)


def outlierDetection(data, fieldNme, newFieldNme):
    # 按货物品名分组
    dataByCgo = pd.read_excel('E://09-PYTHON/wtGrp.xlsx')
    # 分别统计每一种货物属性的上下限
    limitByCgo = pd.DataFrame(columns=['CGO_BRIEF_CDE', 'QU', 'QL'])
    for cgo in dataByCgo.columns.values.tolist():
        list = dataByCgo[cgo].tolist()
        qu = np.percentile(list, 75)
        ql = np.percentile(list, 25)
        limitByCgo = limitByCgo.append({ 'CGO_BRIEF_CDE':cgo, 'QU': qu, 'QL': ql }, ignore_index=True)
    # 通过JOIN合并数据集
    data = pd.merge(left=data, right=limitByCgo, how='left')
    # 判断数据是否为异常值
    newFieldData = []
    for i in data.index:
        Qu = data.loc[i]['QU']
        Ql = data.loc[i]['QL']
        IQR = Qu - Ql
        outlier_step = 1.5 * IQR
        currValue = data.loc[i][fieldNme]
        newFieldData.append((currValue > Qu + outlier_step) | (currValue < Ql - outlier_step))
    # 合并添加新列
    data = pd.concat([data, pd.DataFrame(newFieldData, columns=[newFieldNme]) ], axis=1)
    return data


# 通过K-Means算法对连续属性值进行聚类，聚类后分为k个簇，得到每个簇对应的分类值形成新的特征，并添加到原数据集中。
# 参数说明。。。
def coopLvlDiscretization(data, fieldNme, newFieldNme, k):
    fieldData = data[fieldNme].copy()
    # K-Means算法(k为离散化后簇的数量)
    kmodel = KMeans(n_clusters=k)
    kmodel.fit(fieldData.values.reshape((len(fieldData), 1)))
    kCenter = pd.DataFrame(kmodel.cluster_centers_, columns=list('a'))
    kCenter = kCenter.sort_values(by='a')
    # 确定分类边界
    kBorder = kCenter.rolling(2).mean().iloc[1:]
    kBorder = [0] + list(kBorder.values[:, 0]) + [fieldData.max()]
    # 切分数据，实现离散化
    newFieldData = pd.cut(fieldData, kBorder, labels=range(k))
    # 合并添加新列
    data = pd.concat([data, newFieldData.rename(newFieldNme)], axis=1)
    return data


def encoder(data):
    X = data.loc[:, ['AGMT', 'EB', 'GRP', 'SH', 'FW', 'CN']].values
    y = data.loc[:, ['IS_CONCEAL']].values
    
    # 类别数据,需要进行标签编码
    leAgmt = preprocessing.LabelEncoder()
    leAgmt = leAgmt.fit(X[:, 0])
    X[:, 0] = leAgmt.transform(X[:, 0])
    
    leEB = preprocessing.LabelEncoder()
    leEB = leEB.fit(X[:, 1])
    X[:, 1] = leEB.transform(X[:, 1])
    
    leGrp = preprocessing.LabelEncoder()
    leGrp = leGrp.fit(X[:, 2])
    X[:, 2] = leGrp.transform(X[:, 2])
    
    leSH = preprocessing.LabelEncoder()
    leSH = leSH.fit(X[:, 3])
    X[:, 3] = leSH.transform(X[:, 3])
    
    leFW = preprocessing.LabelEncoder()
    leFW = leFW.fit(X[:, 4])
    X[:, 4] = leFW.transform(X[:, 4])
    
    leCN = preprocessing.LabelEncoder()
    leCN = leCN.fit(X[:, 5])
    X[:, 5] = leCN.transform(X[:, 5])
    
    # 将y转为一维
    y = LabelEncoder().fit_transform(y.ravel()) 
    
    ohe = OneHotEncoder(sparse=False, categories='auto')
    ohe = ohe.fit(X[:, [ 2, 3, 4, 5]])
    ohe.transform(X[:, [ 2, 3, 4, 5]])
    
    joblib.dump(leAgmt, 'E://09-PYTHON/leAgmt.pkl')
    joblib.dump(leEB, 'E://09-PYTHON/leEB.pkl')
    joblib.dump(leGrp, 'E://09-PYTHON/leGrp.pkl')
    joblib.dump(leSH, 'E://09-PYTHON/leSH.pkl')
    joblib.dump(leFW, 'E://09-PYTHON/leFW.pkl')
    joblib.dump(leCN, 'E://09-PYTHON/leCN.pkl')
    joblib.dump(ohe, 'E://09-PYTHON/ohe.pkl')
    
    return


@paper.route('/randomForestClassifier')
def randomForestClassifier():
    # allData = pd.read_excel('E://09-PYTHON/data.xlsx')
    
#     # 缺失值
#     total = allData.isnull().sum().sort_values(ascending=False)
#     percent = (allData.isnull().sum() / allData.isnull().count()).sort_values(ascending=False)
#     missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
#     missing_data.head(20)
#     
#     # 箱图
#     plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
#     plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
#     plt.figure(1, figsize=(13, 26))  # 可设定图像大小
#     p = allData.boxplot()
#     p = allData.boxplot(return_type='dict')
#     x = p['fliers'][0].get_xdata()
#     y = p['fliers'][0].get_ydata()
#     y.sort()  # 从小到大排序
#     for i in range(len(x)): 
#         if i > 0:
#             plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
#         else:
#             plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))
#     plt.show()  # 展示箱线图

    # msno.bar(allData)
    
    # 使用出现次数最多的值填补
    # allData['GSRP'] = allData['GRP'].fillna('S')
    # allData.GRP[allData.GRP.isnull()]=allData.GRP.dropna().mode().values    
    
#     imr = Imputer(missing_values = 'NaN', strategy = 'most_frequent', axis = 0 )
#     imr = imr.fit(allData.values)
#     allData = imr.transform(allData.values)    

#     corrmat = allData.corr(method='kendall')  # 得到相关系数
#     f, ax = plt.subplots(figsize=(12, 9))
#     sns.heatmap(corrmat,vmax = .8,square = True,cmap = 'hot')  # 热点图
# 
#     # 取出相关性最大的前十个，做出热点图表示
#     k = 10  # number of variables for heatmap
#     cols = corrmat.nlargest(k, 'IS_CONCEAL')['IS_CONCEAL'].index
#     cm = np.corrcoef(allData[cols].values.T)
#     sns.set(font_scale=1.25)
#     hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
#     plt.show()

    allData = pd.read_excel('E://09-PYTHON/ForPython.xlsx')
    allData2 = pd.read_excel('E://09-PYTHON/ForPythonTest.xlsx')
    
    encoder(pd.concat([allData, allData2], axis=0, ignore_index=True))
    leAgmt = joblib.load('E://09-PYTHON/leAgmt.pkl')
    leEB = joblib.load('E://09-PYTHON/leEB.pkl')
    leGrp = joblib.load('E://09-PYTHON/leGrp.pkl')
    leSH = joblib.load('E://09-PYTHON/leSH.pkl')
    leFW = joblib.load('E://09-PYTHON/leFW.pkl')
    leCN = joblib.load('E://09-PYTHON/leCN.pkl')
    ohe = joblib.load('E://09-PYTHON/ohe.pkl')
    
    A = allData[['AGMT', 'EB', 'GRP', 'SH', 'FW', 'CN']]
    B = allData.IS_CONCEAL
    A2 = allData2[['AGMT', 'EB', 'GRP', 'SH', 'FW', 'CN']]
    B2 = allData2.IS_CONCEAL
    
    # 分为训练集和测试集7：3
    # A, A2, B, B2 = train_test_split(allData[['AGMT', 'EB', 'GRP', 'SH', 'FW', 'CN']], allData.IS_CONCEAL, random_state=1234567, test_size=0.3)
    
    X = A.values
    y = B.values
    
    X2 = A2.values
    y2 = B2.values
    
    # 类别数据,需要进行标签编码
    X[:, 0] = leAgmt.transform(X[:, 0])
    X[:, 1] = leEB.transform(X[:, 1])
    X[:, 2] = leGrp.transform(X[:, 2])
    X[:, 3] = leSH.transform(X[:, 3])
    X[:, 4] = leFW.transform(X[:, 4])
    X[:, 5] = leCN.transform(X[:, 5])
    
    X2[:, 0] = leAgmt.transform(X2[:, 0])
    X2[:, 1] = leEB.transform(X2[:, 1])
    X2[:, 2] = leGrp.transform(X2[:, 2])
    X2[:, 3] = leSH.transform(X2[:, 3])
    X2[:, 4] = leFW.transform(X2[:, 4])
    X2[:, 5] = leCN.transform(X2[:, 5])
    
    # 将y转为一维
    y = LabelEncoder().fit_transform(y.ravel()) 
    y2 = LabelEncoder().fit_transform(y2.ravel()) 

    # 对离散特征进行独热编码，扩维
    X = np.hstack((X[:, [0, 1]], ohe.transform(X[:, [ 2, 3, 4, 5]])))
    X2 = np.hstack((X2[:, [0, 1]], ohe.transform(X2[:, [ 2, 3, 4, 5]])))
        
    # 数据平衡
#     print(len(X))
#     print(Counter(y))
#     over_samples = SMOTE(random_state=123456, k_neighbors=5, ratio=2.0) 
#     X, y = over_samples.fit_sample(X, y)
#     print(len(X))
#     print(Counter(y))
 
    decisionTreeClf = DecisionTreeClassifier()
    decisionTreeClf.fit(X, y)
#     predTrainTree = decisionTreeClf.predict(X)
#     # 模型在测试集上的预测
    predTree = decisionTreeClf.predict(X2)
#     # 模型的预测准确率
#     print(metrics.accuracy_score(y2, predTree))
#     print(metrics.classification_report(y2, predTree))
#     cm = confusion_matrix(y2, predTree)
    y2_scoreTree = decisionTreeClf.predict_proba(X2)[:, 1] 
#     fpr, tpr, threshold = metrics.roc_curve(B2.map({False:0, True:1}), y2_score) 

    mlp = MLPClassifier()
    mlp.fit(X, y)
    # predTrain = mlp.predict(X)
    predMlp = mlp.predict(X2)
    # print(metrics.accuracy_score(y2, pred))
    # print(metrics.classification_report(y2, pred))
    # cm = confusion_matrix(y2, pred)
    y2_scoreMlp = mlp.predict_proba(X2)[:, 1] 
    # fpr, tpr, threshold = metrics.roc_curve(B2.map({False:0, True:1}), y2_score)

    lr = LogisticRegressionCV()
    lr.fit(X, y)
    # 模型在测试集上的预测
    predLogic = lr.predict(X2)
    # 模型的预测准确率
    # print(metrics.accuracy_score(y2, predLogic))
    # print(metrics.classification_report(y2, predLogic))
    # cm = confusion_matrix(y2, pred)
    y2_scoreLogic = lr.predict_proba(X2)[:, 1] 
    # fpr, tpr, threshold = metrics.roc_curve(B2.map({False:0, True:1}), y2_scoreLogic)
    
    oldRandomForestClf = RandomForestClassifier(n_estimators=50)
    oldRandomForestClf.fit(X, y)
    y2_scoreOldRf = oldRandomForestClf.predict_proba(X2)[:, 1] 
    predOldRf = oldRandomForestClf.predict(X2)
    
    randomForestClf = RandomForestClassifier(n_estimators=50, improve=True)
    randomForestClf.fit(X, y)
    # randomForestClf.oob_score_
    # 模型在测试集上的预测
    pred = randomForestClf.predict(X2)
    # 模型的预测准确率
    # print(metrics.accuracy_score(y2, pred))
    # 模型评估报告
    # print(metrics.classification_report(y2, pred))
    
    # 绘制ROC曲线
    y2_score = randomForestClf.predict_proba(X2)[:, 1] 
    fpr, tpr, threshold = metrics.roc_curve(B2.map({False:0, True:1}), y2_score)
    evaluate_model(pred, y2_score, y2, predLogic, y2_scoreOldRf, y2_scoreLogic, predMlp, y2_scoreMlp, predTree, y2_scoreTree, predBys, y2_scoreBys)
    
#     # 计算AUC的值
#     roc_auc = metrics.auc(fpr, tpr)
#     print(roc_auc)
#     # 绘制面积图
#     plt.stackplot(fpr, tpr, color='steelblue', alpha=0.5, edgecolor='black')
#     # 添加边际线
#     plt.plot(fpr, tpr, color='black', lw=1)
#     # 添加对角线
#     plt.plot([0, 1], [0, 1], color='red', linestyle='--')
#     # 添加文本信息
#     plt.text(0.5, 0.3, 'ROC curve (area = %0.3f)' % roc_auc)
#     # 添加x轴与y轴标签
#     plt.xlabel('1-Specificity') 
#     plt.ylabel('Sensitivity')
#     # 显示图形
#     plt.show()
        
    # 特征重要性
#     importances = randomForestClf.feature_importances_
#     indices = np.argsort(importances)[::-1]
#     
#     featureNames = ['AGMT', 'EB']
#     for featureName in list(leGrp.classes_):
#         featureNames.append("GRP_%s" % (featureName))
#     for featureName in list(leSH.classes_):
#         featureNames.append("SH_%s" % (featureName))
#     for featureName in list(leFW.classes_):
#         featureNames.append("FW_%s" % (featureName))    
#     for featureName in list(leCN.classes_):
#         featureNames.append("CN_%s" % (featureName))
# 
#     # 扩维后重要性和属性对应，输入特征排行
#     for f in range(X.shape[1]):
#         print("%2d) %-*s %f" % (f + 1, 30, featureNames[indices[f]], importances[indices[f]]))
#     
#     plt.title('Features Importances')
#     plt.bar(range(10), importances[indices][:10], color='lightblue', align='center')
#     plt.xticks(range(10), np.array(featureNames)[indices][:10], rotation=90)
#     plt.xlim([-1, 10]) 
#     # plt.ylim(0.02, 1)
#     plt.tight_layout()
#     plt.show()
    
    # 训练模型持久化joblib
#     joblib.dump(randomForestClf, 'E://09-PYTHON/randomForestClf.pkl')

    return "isConceal"


@paper.route('/demo')
def demo():
    X, y = make_blobs(n_samples=1000, n_features=6, centers=50, random_state=0)
    
    decisionTreeClf = DecisionTreeClassifier(max_depth=None, min_samples_split=2, random_state=0)
    decisionTreeScores = cross_val_score(decisionTreeClf, X, y)
    print("DecisionTreeClassifier:", decisionTreeScores.mean())
    
    randomForestClf = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
    randomForestScores = cross_val_score(randomForestClf, X, y)
    print("RandomForestClassifier:", randomForestScores.mean())
     
    return "demo"


@paper.route('/iris')
def iris():
    iris = datasets.load_iris() 
    print(iris.data)
    print(iris.target)
    print(iris.feature_names)
    print(iris.filename)
    print(iris.DESCR)
    return "iris"


@paper.route('/cgoDescClassifier')
def cgoDescClassifier():
    allData = pd.read_excel('E://09-PYTHON/data92.xlsx')  # 5130067180
    
    # 比较TF-IDF HashingVectorizer
    cgoDescTrain, cgoDescTest, cgoCdeTrain, cgoCdeTest = train_test_split(allData.FULL_DESC, allData.CGO_CDE, random_state=12, test_size=0.3)
    
#     hv = HashingVectorizer(stop_words='english', non_negative=True)
#     fea_train = hv.fit_transform(list(cgoDescTrain.values.ravel()))
#     fea_test = hv.fit_transform(list(cgoDescTest.values.ravel()))
#     print('Size of fea_train:' + repr(fea_train.shape))
#     print('Size of fea_train:' + repr(fea_test.shape))
#     svclf = SVC(kernel='linear')  # default with 'rbf'
#     svclf.fit(fea_train, LabelEncoder().fit_transform(cgoCdeTrain.values.ravel()))
#     pred = svclf.predict(fea_test)
#     calculate_result(LabelEncoder().fit_transform(cgoCdeTest.values.ravel()), pred)
    
    tv = TfidfVectorizer(min_df=1)
    tv_train = tv.fit_transform(list(cgoDescTrain.values.ravel()))
    tv2 = TfidfVectorizer(vocabulary=tv.vocabulary_)
    tv_test = tv2.fit_transform(list(cgoDescTest.values.ravel()))
    print("the shape of train is " + repr(tv_train.shape))
    print("the shape of test is " + repr(tv_test.shape))
    tv.get_feature_names()   
    
    print("SVM:")
    svclf = SVC(kernel='linear', C=1)  # default with 'rbf'
    svclf.fit(tv_train, LabelEncoder().fit_transform(cgoCdeTrain.values.ravel()))
    pred = svclf.predict(tv_test)
    le = preprocessing.LabelEncoder()
    le = le.fit(cgoCdeTest.values.ravel())
    calculate_result(le.fit_transform(cgoCdeTest.values.ravel()), pred)
    tv3 = TfidfVectorizer(vocabulary=tv.vocabulary_)
    tv_test3 = tv3.fit_transform(['aaa'])
    le.inverse_transform(svclf.predict(tv_test3))
    
    print("KNN:")
    knnclf = KNeighborsClassifier() 
    knnclf.fit(tv_train, LabelEncoder().fit_transform(cgoCdeTrain.values.ravel()))
    pred = knnclf.predict(tv_test)
    calculate_result(LabelEncoder().fit_transform(cgoCdeTest.values.ravel()), pred)
    
    print("NB:")
    nbClf = MultinomialNB(alpha=0.01) 
    nbClf.fit(tv_train, LabelEncoder().fit_transform(cgoCdeTrain.values.ravel()))
    pred = nbClf.predict(tv_test)
    calculate_result(LabelEncoder().fit_transform(cgoCdeTest.values.ravel()), pred)
    
    return "cgoDescClassifier"


def calculate_result(actual, pred):
    m_precision = metrics.precision_score(actual, pred, average='macro')
    m_recall = metrics.recall_score(actual, pred, average='macro')
    print('predict info:')
    print('precision:{0:.3f}'.format(m_precision))
    print('recall:{0:0.3f}'.format(m_recall))
    print('f1-score:{0:.3f}'.format(metrics.f1_score(actual, pred, average='macro')))


def cluster_plot(d, k, data):
    # 可视化
    # cluster_plot(newData, 5, newFieldData).show()
    
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    
    plt.figure(figsize=(12, 4))
    for j in range(0, k):
        plt.plot(data[d == j], [j for i in d[d == j]], 'o')
        
    plt.ylim(-0.5, k - 0.5)
    return plt


@paper.route('/smote')
def smote():
    data = pd.read_excel('E://09-PYTHON/data.xlsx')
    
    encoder(data)
    leAgmt = joblib.load('E://09-PYTHON/leAgmt.pkl')
    leEB = joblib.load('E://09-PYTHON/leEB.pkl')
    leGrp = joblib.load('E://09-PYTHON/leGrp.pkl')
    leSH = joblib.load('E://09-PYTHON/leSH.pkl')
    leFW = joblib.load('E://09-PYTHON/leFW.pkl')
    leCN = joblib.load('E://09-PYTHON/leCN.pkl')
    ohe = joblib.load('E://09-PYTHON/ohe.pkl')
    
    # 分为训练集和测试集7：3
    A, A2, B, B2 = train_test_split(data[['AGMT', 'EB', 'GRP', 'SH', 'FW', 'CN']], data.IS_CONCEAL, random_state=1234567, test_size=0.3)
    
    X = A.values
    y = B.values
    
    X2 = A2.values
    y2 = B2.values
    
    # 类别数据,需要进行标签编码
    X[:, 0] = leAgmt.transform(X[:, 0])
    X[:, 1] = leEB.transform(X[:, 1])
    X[:, 2] = leGrp.transform(X[:, 2])
    X[:, 3] = leSH.transform(X[:, 3])
    X[:, 4] = leFW.transform(X[:, 4])
    X[:, 5] = leCN.transform(X[:, 5])
    
    X2[:, 0] = leAgmt.transform(X2[:, 0])
    X2[:, 1] = leEB.transform(X2[:, 1])
    X2[:, 2] = leGrp.transform(X2[:, 2])
    X2[:, 3] = leSH.transform(X2[:, 3])
    X2[:, 4] = leFW.transform(X2[:, 4])
    X2[:, 5] = leCN.transform(X2[:, 5])
    
    # 将y转为一维
    y = LabelEncoder().fit_transform(y.ravel()) 
    y2 = LabelEncoder().fit_transform(y2.ravel()) 

    # 对离散特征进行独热编码，扩维
#     X = np.hstack((X[:, [0, 1]], ohe.transform(X[:, [ 2, 3, 4, 5]])))
#     X2 = np.hstack((X2[:, [0, 1]], ohe.transform(X2[:, [ 2, 3, 4, 5]])))    
    
    return "Success"


@paper.route('/featureSelection')
def featureSelection():
    data = pd.read_excel('E://09-PYTHON/data.xlsx')
    
    A = data[['AGMT', 'EB', 'GRP', 'SH', 'FW', 'CN']]
    B = data[['IS_CONCEAL']]
    
    X = A.values
    y = B.values
    
    leAgmt = joblib.load('E://09-PYTHON/leAgmt.pkl')
    leEB = joblib.load('E://09-PYTHON/leEB.pkl')
    leGrp = joblib.load('E://09-PYTHON/leGrp.pkl')
    leSH = joblib.load('E://09-PYTHON/leSH.pkl')
    leFW = joblib.load('E://09-PYTHON/leFW.pkl')
    leCN = joblib.load('E://09-PYTHON/leCN.pkl')
    ohe = joblib.load('E://09-PYTHON/ohe.pkl')
    
    # 类别数据,需要进行标签编码
    X[:, 0] = leAgmt.transform(X[:, 0])
    X[:, 1] = leEB.transform(X[:, 1])
    X[:, 2] = leGrp.transform(X[:, 2])
    X[:, 3] = leSH.transform(X[:, 3])
    X[:, 4] = leFW.transform(X[:, 4])
    X[:, 5] = leCN.transform(X[:, 5])

    # 将y转为一维
    y = LabelEncoder().fit_transform(y.ravel()) 

    # 对离散特征进行独热编码，扩维
    X = np.hstack((X[:, [0, 1]], ohe.transform(X[:, [ 2, 3, 4, 5]])))
    
#     sel = VarianceThreshold(threshold=(.9 * (1 - .9)))
#     sel.fit_transform(X)
    
    rlasso = RandomizedLogisticRegression()
    rlasso.fit(X, y)
    
    featureNames = ['AGMT', 'EB']
    for featureName in list(leGrp.classes_):
        featureNames.append("GRP_%s" % (featureName))
    for featureName in list(leSH.classes_):
        featureNames.append("SH_%s" % (featureName))
    for featureName in list(leFW.classes_):
        featureNames.append("FW_%s" % (featureName))    
    for featureName in list(leCN.classes_):
        featureNames.append("CN_%s" % (featureName))
# 
    a = rank_to_dict(np.abs(rlasso.scores_), featureNames)
    
    return "Success"


def rank_to_dict(ranks, names, order=1):
    minmax = MinMaxScaler()
    ranks = minmax.fit_transform(order * np.array([ranks]).T).T[0]
    ranks = map(lambda x: round(x, 2), ranks)
    return dict(zip(names, ranks))


@paper.route('/calcTreeSimilarity')
def calcTreeSimilarity():
    allData = pd.read_excel('E://09-PYTHON/data.xlsx')
    allData2 = pd.read_excel('E://09-PYTHON/data.xlsx')
    
    encoder(pd.concat([allData, allData2], axis=0, ignore_index=True))
    leAgmt = joblib.load('E://09-PYTHON/leAgmt.pkl')
    leEB = joblib.load('E://09-PYTHON/leEB.pkl')
    leGrp = joblib.load('E://09-PYTHON/leGrp.pkl')
    leSH = joblib.load('E://09-PYTHON/leSH.pkl')
    leFW = joblib.load('E://09-PYTHON/leFW.pkl')
    leCN = joblib.load('E://09-PYTHON/leCN.pkl')
    ohe = joblib.load('E://09-PYTHON/ohe.pkl')
    
    A = allData[['AGMT', 'EB', 'GRP', 'SH', 'FW', 'CN']]
    B = allData.IS_CONCEAL
    A2 = allData2[['AGMT', 'EB', 'GRP', 'SH', 'FW', 'CN']]
    B2 = allData2.IS_CONCEAL
    
    X = A.values
    y = B.values
    
    X2 = A2.values
    y2 = B2.values
    
    # 类别数据,需要进行标签编码
    X[:, 0] = leAgmt.transform(X[:, 0])
    X[:, 1] = leEB.transform(X[:, 1])
    X[:, 2] = leGrp.transform(X[:, 2])
    X[:, 3] = leSH.transform(X[:, 3])
    X[:, 4] = leFW.transform(X[:, 4])
    X[:, 5] = leCN.transform(X[:, 5])
    
    X2[:, 0] = leAgmt.transform(X2[:, 0])
    X2[:, 1] = leEB.transform(X2[:, 1])
    X2[:, 2] = leGrp.transform(X2[:, 2])
    X2[:, 3] = leSH.transform(X2[:, 3])
    X2[:, 4] = leFW.transform(X2[:, 4])
    X2[:, 5] = leCN.transform(X2[:, 5])
    
    # 将y转为一维
    y = LabelEncoder().fit_transform(y.ravel()) 
    y2 = LabelEncoder().fit_transform(y2.ravel()) 

    # 对离散特征进行独热编码，扩维
    X = np.hstack((X[:, [0, 1]], ohe.transform(X[:, [ 2, 3, 4, 5]])))
    X2 = np.hstack((X2[:, [0, 1]], ohe.transform(X2[:, [ 2, 3, 4, 5]])))
    
    tree = DecisionTreeClassifier()
    tree.fit(X, y)
    
    tree_ = tree.tree_
    featureNames = ['AGMT', 'EB']
    for featureName in list(leGrp.classes_):
        featureNames.append("GRP_%s" % (featureName))
    for featureName in list(leSH.classes_):
        featureNames.append("SH_%s" % (featureName))
    for featureName in list(leFW.classes_):
        featureNames.append("FW_%s" % (featureName))    
    for featureName in list(leCN.classes_):
        featureNames.append("CN_%s" % (featureName))
        
    feature_name = [
        featureNames[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    
    currRules, allRules = [], []

    def recurse(node, depth):
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            print("{}if {} <= {}:".format(indent, name, threshold))
            recurse(tree_.children_left[node], depth + 1)
            print("{}else:  # if {} > {}".format(indent, name, threshold))
            recurse(tree_.children_right[node], depth + 1)
        else:
            print("{}return {}".format(indent, tree_.value[node]))

    # 递归获取树的规则集
    def getTreeRules(node, depth):
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            currRules.append("{} <= {}".format(name, tree_.threshold[node]))
            getTreeRules(tree_.children_left[node], depth + 1)
            currRules.pop(len(currRules) - 1)
            currRules.append("{} > {}".format(name, tree_.threshold[node]))
            getTreeRules(tree_.children_right[node], depth + 1)
        else:
            allRules.append(currRules.copy())
            
    getTreeRules(0, 1)
    
    allRules1 = allRules.copy()
    allRules2 = allRules.copy()

    # 比较规则集
    sum = 0 
    for i in range(len(allRules1)):
        subSim = 0  # 每一条规则取最大的相似度
        rule1 = allRules1[i]
        for j in range(len(allRules2)):
            rule2 = allRules2[j]
            currSubSim = 0;
            # 均为分类属性，子规则仅比较是否相同即可
            for p in range(len(rule1)):
                if(len(rule2) > p and  rule1[p] == rule2[p]):
                    currSubSim = currSubSim + 1
            currSubSim = currSubSim / max(len(rule1), len(rule2))
            subSim = max(subSim, currSubSim)
            if(subSim == 1):
                break;
        sum = sum + subSim
    sum = sum / len(allRules1)
        
    return ""


# 混淆矩阵
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Oranges):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    Source: http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
 
    print(cm)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.figure(figsize=(5, 5))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title, size=16)
    plt.colorbar(aspect=4)
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, size=14)
    plt.yticks(tick_marks, classes, rotation=90, size=14)
 
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
     
    # Labeling the plot
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt), fontsize=20,
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
         
    plt.grid(None)
    plt.tight_layout()
    plt.ylabel('实际值', size=14)
    plt.xlabel('预测值', size=14)


def evaluate_model(predictions, probs, test_labels, predLogic, y2_scoreOldRf, y2_scoreLogic, predMlp, y2_scoreMlp, predTree, y2_scoreTree, predBys, y2_scoreBys):
    """Compare machine learning model to baseline performance.
    Computes statistics and shows ROC curve."""
    
    baseline = {}
    baseline['recall'] = recall_score(test_labels, [1 for _ in range(len(test_labels))])
    baseline['precision'] = precision_score(test_labels, [1 for _ in range(len(test_labels))])
    baseline['roc'] = 0.5
    
    results = {}
    results['recall'] = recall_score(test_labels, predictions)
    results['precision'] = precision_score(test_labels, predictions)
    results['roc'] = roc_auc_score(test_labels, probs)
    
    resultsLogic = {}
    resultsLogic['recall'] = recall_score(test_labels, predLogic)
    resultsLogic['precision'] = precision_score(test_labels, predLogic)
    resultsLogic['roc'] = roc_auc_score(test_labels, y2_scoreLogic)
    
#     for metric in ['recall', 'precision', 'roc']:
#         print(f'{metric.capitalize()} Baseline: {round(baseline[metric], 2)} Test: {round(results[metric], 2)} Train: {round(train_results[metric], 2)}')
    
    # Calculate false positive rates and true positive rates
    base_fpr, base_tpr, _ = roc_curve(test_labels, [1 for _ in range(len(test_labels))])
    model_fpr, model_tpr, _ = roc_curve(test_labels, probs)
    old_rf_fpr, old_rf_tpr, _ = roc_curve(test_labels, y2_scoreOldRf)
    logic_fpr, logic_tpr, _ = roc_curve(test_labels, y2_scoreLogic)
    mlp_fpr, mlp_tpr, _ = roc_curve(test_labels, y2_scoreMlp)
    tree_fpr, tree_tpr, _ = roc_curve(test_labels, y2_scoreTree)
    bys_fpr, bys_tpr, _ = roc_curve(test_labels, y2_scoreBys)

    plt.figure(figsize=(8, 6))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['font.size'] = 12
    
    # Plot both curves
    plt.plot(base_fpr, base_tpr, 'b', label='baseline')
    plt.plot(model_fpr, model_tpr, 'r', label='改进随机森林')
    plt.plot(old_rf_fpr, old_rf_tpr, 'k', label='传统随机森林')
    plt.plot(logic_fpr, logic_tpr, 'y', label='逻辑回归')
    plt.plot(mlp_fpr, mlp_tpr, 'm', label='神经网络')
    plt.plot(tree_fpr, tree_tpr, 'g', label='决策树')
    plt.plot(bys_fpr, bys_tpr, 'c', label='贝叶斯网络')
    plt.legend();
    plt.xlabel('假阳性率'); plt.ylabel('真阳性率'); plt.title('ROC 曲线');


best = 0


@paper.route('/hyperoptParamAdjust')
def hyperoptParamAdjust():
    allData = pd.read_excel('E://09-PYTHON/aaa.xlsx')
    encoder(allData)
    leAgmt = joblib.load('E://09-PYTHON/leAgmt.pkl')
    leEB = joblib.load('E://09-PYTHON/leEB.pkl')
    leGrp = joblib.load('E://09-PYTHON/leGrp.pkl')
    leSH = joblib.load('E://09-PYTHON/leSH.pkl')
    leFW = joblib.load('E://09-PYTHON/leFW.pkl')
    leCN = joblib.load('E://09-PYTHON/leCN.pkl')
    ohe = joblib.load('E://09-PYTHON/ohe.pkl')
    
    # 分为训练集和测试集7：3
    A, A2, B, B2 = train_test_split(allData[['AGMT', 'EB', 'GRP', 'SH', 'FW', 'CN']], allData.IS_CONCEAL, random_state=1234567, test_size=0.3)
    
    X = A.values
    y = B.values
    
    X2 = A2.values
    y2 = B2.values
    
    # 类别数据,需要进行标签编码
    X[:, 0] = leAgmt.transform(X[:, 0])
    X[:, 1] = leEB.transform(X[:, 1])
    X[:, 2] = leGrp.transform(X[:, 2])
    X[:, 3] = leSH.transform(X[:, 3])
    X[:, 4] = leFW.transform(X[:, 4])
    X[:, 5] = leCN.transform(X[:, 5])
    
    X2[:, 0] = leAgmt.transform(X2[:, 0])
    X2[:, 1] = leEB.transform(X2[:, 1])
    X2[:, 2] = leGrp.transform(X2[:, 2])
    X2[:, 3] = leSH.transform(X2[:, 3])
    X2[:, 4] = leFW.transform(X2[:, 4])
    X2[:, 5] = leCN.transform(X2[:, 5])
    
    # 将y转为一维
    y = LabelEncoder().fit_transform(y.ravel()) 
    y2 = LabelEncoder().fit_transform(y2.ravel()) 

    # 对离散特征进行独热编码，扩维
    X = np.hstack((X[:, [0, 1]], ohe.transform(X[:, [ 2, 3, 4, 5]])))
    X2 = np.hstack((X2[:, [0, 1]], ohe.transform(X2[:, [ 2, 3, 4, 5]])))
    
    space4rf = {
        'n_estimators': hp.choice('n_estimators', range(1, 50)),
        'max_features': hp.choice('max_features', range(1, 10)),
        'criterion': hp.choice('criterion', ["gini", "entropy"]),
        'max_depth': hp.choice('max_depth', range(1, 30)),
        'min_samples_split': hp.choice('min_samples_split', range(2, 5)),
        'min_samples_leaf': hp.choice('min_samples_leaf', range(1, 5))
    }

    def hyperopt_train_test(params):
        X_ = X[:]
        if 'normalize' in params:
            if params['normalize'] == 1:
                X_ = normalize(X_)
                del params['normalize']
     
        if 'scale' in params:
            if params['scale'] == 1:
                X_ = scale(X_)
                del params['scale']
        clf = RandomForestClassifier(**params)
        return cross_val_score(clf, X, y).mean()

    def f(params):
        global best
        acc = hyperopt_train_test(params)
        if acc > best:
            best = acc
            print('new best:'), best, params
            print(best)
            print(params)
        return {'loss':-acc, 'status': STATUS_OK}
    
#     def f(params):
#         auc = calcRfAuc(params)
#         return {'loss':-auc, 'status': STATUS_OK}
    
    trials = Trials()
    best = fmin(f, space4rf, algo=tpe.suggest, max_evals=250, trials=trials)
    print('best:')
    print(best)

    parameters = ['n_estimators', 'max_features', 'criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf' ]
    f, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))
    cmap = plt.cm.jet
    for i, val in enumerate(parameters):
        xs = np.array([t['misc']['vals'][val] for t in trials.trials]).ravel()
        ys = [-t['result']['loss'] for t in trials.trials]
        xs, ys = list(zip(*sorted(list(zip(xs, ys)))))
        ys = np.array(ys)
        axes[int(i / 3), int(i % 3)].scatter(xs, ys, s=20, linewidth=0.01, alpha=0.5, c=cmap(float(i) / len(parameters)))
        axes[int(i / 3), int(i % 3)].set_title(val)
        # axes[i/3,i%3].set_ylim([0.9,1.0])

    return ""


@paper.route('/hyperoptParamAdjustTree')
def hyperoptParamAdjustTree():
    allData = pd.read_excel('E://09-PYTHON/aaa.xlsx')
    encoder(allData)
    leAgmt = joblib.load('E://09-PYTHON/leAgmt.pkl')
    leEB = joblib.load('E://09-PYTHON/leEB.pkl')
    leGrp = joblib.load('E://09-PYTHON/leGrp.pkl')
    leSH = joblib.load('E://09-PYTHON/leSH.pkl')
    leFW = joblib.load('E://09-PYTHON/leFW.pkl')
    leCN = joblib.load('E://09-PYTHON/leCN.pkl')
    ohe = joblib.load('E://09-PYTHON/ohe.pkl')
    
    # 分为训练集和测试集7：3
    A, A2, B, B2 = train_test_split(allData[['AGMT', 'EB', 'GRP', 'SH', 'FW', 'CN']], allData.IS_CONCEAL, random_state=1234567, test_size=0.3)
    
    X = A.values
    y = B.values
    
    X2 = A2.values
    y2 = B2.values
    
    # 类别数据,需要进行标签编码
    X[:, 0] = leAgmt.transform(X[:, 0])
    X[:, 1] = leEB.transform(X[:, 1])
    X[:, 2] = leGrp.transform(X[:, 2])
    X[:, 3] = leSH.transform(X[:, 3])
    X[:, 4] = leFW.transform(X[:, 4])
    X[:, 5] = leCN.transform(X[:, 5])
    
    X2[:, 0] = leAgmt.transform(X2[:, 0])
    X2[:, 1] = leEB.transform(X2[:, 1])
    X2[:, 2] = leGrp.transform(X2[:, 2])
    X2[:, 3] = leSH.transform(X2[:, 3])
    X2[:, 4] = leFW.transform(X2[:, 4])
    X2[:, 5] = leCN.transform(X2[:, 5])
    
    # 将y转为一维
    y = LabelEncoder().fit_transform(y.ravel()) 
    y2 = LabelEncoder().fit_transform(y2.ravel()) 

    # 对离散特征进行独热编码，扩维
    X = np.hstack((X[:, [0, 1]], ohe.transform(X[:, [ 2, 3, 4, 5]])))
    X2 = np.hstack((X2[:, [0, 1]], ohe.transform(X2[:, [ 2, 3, 4, 5]])))
    
    space4rf = {
        'max_depth': hp.choice('max_depth', range(1, 30)),
        'max_features': hp.choice('max_features', range(1, 10)),
        'criterion': hp.choice('criterion', ["gini", "entropy"]),
        'min_samples_split': hp.choice('min_samples_split', range(2, 5)),
        'min_samples_leaf': hp.choice('min_samples_leaf', range(1, 5))
    }

    def hyperopt_train_test(params):
        X_ = X[:]
        if 'normalize' in params:
            if params['normalize'] == 1:
                X_ = normalize(X_)
                del params['normalize']
     
        if 'scale' in params:
            if params['scale'] == 1:
                X_ = scale(X_)
                del params['scale']
        clf = DecisionTreeClassifier(**params)
        return cross_val_score(clf, X, y).mean()

    def f(params):
        acc = hyperopt_train_test(params)
        return {'loss':-acc, 'status': STATUS_OK}
    
    trials = Trials()
    best = fmin(f, space4rf, algo=tpe.suggest, max_evals=50, trials=trials)
    print('best:')
    print(best)

    parameters = [ 'max_depth', 'max_features', 'criterion', 'min_samples_split', 'min_samples_leaf' ]
    f, axes = plt.subplots(nrows=1, ncols=5, figsize=(15, 10))
    cmap = plt.cm.jet
    for i, val in enumerate(parameters):
        xs = np.array([t['misc']['vals'][val] for t in trials.trials]).ravel()
        ys = [-t['result']['loss'] for t in trials.trials]
        xs, ys = list(zip(*sorted(list(zip(xs, ys)))))
        ys = np.array(ys)
        axes[i].scatter(xs, ys, s=20, linewidth=0.01, alpha=0.5, c=cmap(float(i) / len(parameters)))
        axes[i].set_title(val)
    return ""


@paper.route('/hyperoptParamAdjustMLP')
def hyperoptParamAdjustMLP():
    allData = pd.read_excel('E://09-PYTHON/aaa.xlsx')
    encoder(allData)
    leAgmt = joblib.load('E://09-PYTHON/leAgmt.pkl')
    leEB = joblib.load('E://09-PYTHON/leEB.pkl')
    leGrp = joblib.load('E://09-PYTHON/leGrp.pkl')
    leSH = joblib.load('E://09-PYTHON/leSH.pkl')
    leFW = joblib.load('E://09-PYTHON/leFW.pkl')
    leCN = joblib.load('E://09-PYTHON/leCN.pkl')
    ohe = joblib.load('E://09-PYTHON/ohe.pkl')
    
    # 分为训练集和测试集7：3
    A, A2, B, B2 = train_test_split(allData[['AGMT', 'EB', 'GRP', 'SH', 'FW', 'CN']], allData.IS_CONCEAL, random_state=1234567, test_size=0.3)
    
    X = A.values
    y = B.values
    
    X2 = A2.values
    y2 = B2.values
    
    # 类别数据,需要进行标签编码
    X[:, 0] = leAgmt.transform(X[:, 0])
    X[:, 1] = leEB.transform(X[:, 1])
    X[:, 2] = leGrp.transform(X[:, 2])
    X[:, 3] = leSH.transform(X[:, 3])
    X[:, 4] = leFW.transform(X[:, 4])
    X[:, 5] = leCN.transform(X[:, 5])
    
    X2[:, 0] = leAgmt.transform(X2[:, 0])
    X2[:, 1] = leEB.transform(X2[:, 1])
    X2[:, 2] = leGrp.transform(X2[:, 2])
    X2[:, 3] = leSH.transform(X2[:, 3])
    X2[:, 4] = leFW.transform(X2[:, 4])
    X2[:, 5] = leCN.transform(X2[:, 5])
    
    # 将y转为一维
    y = LabelEncoder().fit_transform(y.ravel()) 
    y2 = LabelEncoder().fit_transform(y2.ravel()) 

    # 对离散特征进行独热编码，扩维
    X = np.hstack((X[:, [0, 1]], ohe.transform(X[:, [ 2, 3, 4, 5]])))
    X2 = np.hstack((X2[:, [0, 1]], ohe.transform(X2[:, [ 2, 3, 4, 5]])))
    
    space4rf = {
        'solver': hp.choice('solver', ['lbfgs', 'sgd', 'adam'])
    }

    def hyperopt_train_test(params):
        clf = MLPClassifier(**params)
        return cross_val_score(clf, X, y).mean()

    def f(params):
        acc = hyperopt_train_test(params)
        return {'loss':-acc, 'status': STATUS_OK}
    
    trials = Trials()
    best = fmin(f, space4rf, algo=tpe.suggest, max_evals=5, trials=trials)
    print('best:')
    print(best)

    parameters = [ 'solver' ]
    f, axes = plt.subplots(nrows=1, ncols=1, figsize=(15, 10))
    cmap = plt.cm.jet
    for i, val in enumerate(parameters):
        xs = np.array([t['misc']['vals'][val] for t in trials.trials]).ravel()
        ys = [-t['result']['loss'] for t in trials.trials]
        xs, ys = list(zip(*sorted(list(zip(xs, ys)))))
        ys = np.array(ys)
        axes[i].scatter(xs, ys, s=20, linewidth=0.01, alpha=0.5, c=cmap(float(i) / len(parameters)))
        axes[i].set_title(val)
    return ""


@paper.route('/isConceal')
def isConceal():
    data = pd.read_excel('E://09-PYTHON/data3.xlsx')
    
    X = data.ix[:, ['AGMT', 'DR', 'EB', 'CGO_GRP', 'SH_LVL', 'FW_LVL', 'CN_LVL']].values
    y = data.ix[:, ['IS_CONCEAL']].values
    
    # 类别数据,需要进行标签编码
    X[:, 0] = LabelEncoder().fit_transform(X[:, 0])
    X[:, 1] = LabelEncoder().fit_transform(X[:, 1])
    X[:, 2] = LabelEncoder().fit_transform(X[:, 2])
    X[:, 3] = LabelEncoder().fit_transform(X[:, 3])
    X[:, 4] = LabelEncoder().fit_transform(X[:, 4])
    X[:, 5] = LabelEncoder().fit_transform(X[:, 5])
    X[:, 6] = LabelEncoder().fit_transform(X[:, 6])
    y = LabelEncoder().fit_transform(y)  
    X = OneHotEncoder(categorical_features=[4]).fit_transform(X).toarray()
    X = OneHotEncoder(categorical_features=[5]).fit_transform(X).toarray()
    X = OneHotEncoder(categorical_features=[6]).fit_transform(X).toarray()
    print(y)
    print(X)

    decisionTreeClf = DecisionTreeClassifier(max_depth=None, min_samples_split=2, random_state=0)
#     decisionTreeClf = decisionTreeClf.fit(X, y)
    decisionTreeScores = cross_val_score(decisionTreeClf, X, y)
    print("DecisionTreeClassifier:", decisionTreeScores.mean())
    
    randomForestClf = RandomForestClassifier(n_estimators=100, max_depth=None, min_samples_split=2, random_state=0, n_jobs=5)
#     randomForestClf = randomForestClf.fit(X, y)
    randomForestScores = cross_val_score(randomForestClf, X, y)
    print("RandomForestClassifier:", randomForestScores.mean())

    return "isConceal"


@paper.route('/forest')
def forest():
#     iris = datasets.load_iris()
#     rf = RandomForestClassifier(max_depth=4)
#     idx = list(range(len(iris.target)))
#     np.random.shuffle(idx)
#      
#     rf.fit(iris.data[idx][:100], iris.target[idx][:100])
#     instance = iris.data[idx][100:101]
#     print(rf.predict_proba(instance))
#     
#     prediction, bias, contributions = ti.predict(rf, instance)
#     print("Prediction", prediction)
#     print("Bias (trainset prior)", bias)
#     print("Feature contributions:")
#     for c, feature in zip(contributions[0],
#                                  iris.feature_names):
#         print(feature, c)
    
    leAgmt = joblib.load('E://09-PYTHON/leAgmt.pkl')
    leEB = joblib.load('E://09-PYTHON/leEB.pkl')
    leGrp = joblib.load('E://09-PYTHON/leGrp.pkl')
    leSH = joblib.load('E://09-PYTHON/leSH.pkl')
    leFW = joblib.load('E://09-PYTHON/leFW.pkl')
    leCN = joblib.load('E://09-PYTHON/leCN.pkl')
    ohe = joblib.load('E://09-PYTHON/ohe.pkl')
    
    clf = joblib.load('E://09-PYTHON/randomForestClf.pkl')
    
    data = pd.read_excel('E://09-PYTHON/forcast.xlsx')
    data = data.head(1)
    A = data.loc[:, ['AGMT', 'EB', 'GRP', 'SH', 'FW', 'CN']]
    B = data.IS_CONCEAL
    
    X = A.values
    y = B.values
    
    X[:, 0] = leAgmt.transform(X[:, 0])
    X[:, 1] = leEB.transform(X[:, 1])
    X[:, 2] = leGrp.transform(X[:, 2])
    X[:, 3] = leSH.transform(X[:, 3])
    X[:, 4] = leFW.transform(X[:, 4])
    X[:, 5] = leCN.transform(X[:, 5])
    
    X = np.hstack((X[:, [0, 1]], ohe.transform(X[:, [ 2, 3, 4, 5]])))
    
    print(clf.predict(X))
    
    prediction, bias, contributions = ti.predict(clf, X)

    print ("Prediction", prediction)
    print ("Bias (trainset prior)", bias)
    print ("Feature contributions:")
    for c, feature in zip(newContributions[0], A.columns._data):
        print(feature, c)
    
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    waterfall_chart.plot(['BIAS', 'AGMT', 'EB', 'GRP', 'SH', 'FW', 'CN'], mergeContributions, net_label='PRED', formatting="{:,.3f}", Title="瞒报预测特征贡献")

    plot_obs_feature_contrib(clf, newContributions, A, B, len(X) - 5, order_by='contribution', violin=True, class_index=1)
    plt.tight_layout()
    plt.savefig('plots/contribution_plot_rf.png')
        
    return "forest"


if __name__ == "__main__":
    paper.run(debug=True)
 
