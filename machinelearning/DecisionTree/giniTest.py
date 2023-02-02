import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from sklearn.tree import export_graphviz
from graphviz import Digraph
import graphviz

from sklearn.tree import DecisionTreeClassifier  # CART分类树：基尼系数、信息增益
from sklearn.tree import DecisionTreeRegressor # CART回归树：MSE均方误差
from sklearn.datasets import load_wine  # 导入sklearn自有数据集：红酒数据集
from sklearn.model_selection import train_test_split   # 划分数据集


from sklearn.model_selection import GridSearchCV

import  warnings
warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号, 注意['SimHei']对应这句不行.
import numpy as np
import pandas as pd
from decimal import *
def entU(u):

    return [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(u, return_counts=True)[1]]][0]

#条件熵
def uConditionV(u,v):

    entu = [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(u, return_counts=True)[1]]][0]
    entv = [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(v, return_counts=True)[1]]][0]

    # v 解释变量
    vid, vct = np.unique(v, return_counts=True)

    # 条件信息
    uConditionVj = [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(u[v == i], return_counts=True)[1] for i in vid]]

    #条件熵
    uConditionV= np.sum(np.array(uConditionVj) * (vct / np.sum(vct)))

    return uConditionV

#信息增益
def gainuv(u,v):

    return entU(u) - uConditionV(u,v)



def giniRegression(y, x):
    xList=[]
    for i in x:
        xList.append(Decimal(i))
    # print(xList)
    sorted_x = np.sort(xList)
    split_point_list = []
    split_point_gini = []
    # 求分界点
    for i in range(0, len(sorted_x) - 1, 1):
        a = Decimal(str(sorted_x[i]))
        b = Decimal(str(sorted_x[i + 1]))
        split_point_list.append((a + b) / 2)

    # print(split_point_list)
    # 依次计算每个分界点分割后的gini系数
    for i in split_point_list:

        # 分界后，就是二分类了
        xi = [1 if x.compare(i) == 1 else 0 for x in xList]

        # 根据新分界点，计算权重（频数、概率）
        w_i = [[p for p in ct / np.sum(ct)] for ct in [np.unique(xi, return_counts=True)[1]]]

        # 分类
        x_id, x_ct = np.unique(xi, return_counts=True)

        # 每个分界点分类的gini
        gini_x_id = [np.sum([(p - p ** 2) for p in ct / np.sum(ct)]) for ct in
                     [np.unique(y[xi == i], return_counts=True)[1] for i in x_id]]
         # print('gini_x_id', gini_x_id)
        # 计算每个分界点的gini
        gini = Decimal(str(np.sum(w_i * np.array(gini_x_id)))).quantize(Decimal('0.0000'), ROUND_HALF_UP)
        # print(gini)
        split_point_gini.append(gini)
    minGini = np.min(split_point_gini)
    return minGini


def giniRegression(y, x):
    xList=[]
    for i in x:
        xList.append(Decimal(i))
    # print(xList)
    sorted_x = np.sort(xList)
    split_point_list = []
    split_point_gini = []
    # 求分界点
    for i in range(0, len(sorted_x) - 1, 1):
        a = Decimal(str(sorted_x[i]))
        b = Decimal(str(sorted_x[i + 1]))
        split_point_list.append((a + b) / 2)

    # print(split_point_list)
    # 依次计算每个分界点分割后的gini系数
    for i in split_point_list:

        # 分界后，就是二分类了
        xi = [1 if x.compare(i) == 1 else 0 for x in xList]

        # 根据新分界点，计算权重（频数、概率）
        w_i = [[p for p in ct / np.sum(ct)] for ct in [np.unique(xi, return_counts=True)[1]]]

        # 分类
        x_id, x_ct = np.unique(xi, return_counts=True)

        # 每个分界点分类的gini 2p(1-p)但是每个p被计算两次
        gini_x_id = [np.sum([(p - p ** 2) for p in ct / np.sum(ct)]) for ct in
                     [np.unique(y[xi == i], return_counts=True)[1] for i in x_id]]
         # print('gini_x_id', gini_x_id)
        # 计算每个分界点的gini
        gini = Decimal(str(np.sum(w_i * np.array(gini_x_id)))).quantize(Decimal('0.0000'), ROUND_HALF_UP)
        # print(gini)
        split_point_gini.append(gini)
    minGini = np.min(split_point_gini)
    return minGini


columnsy = ['有固定资产(X1)', '家庭类型(X2)', '月收入(X3)', 'VIP用户']
datay = np.array([
    ['是', 'C1', 13.3, '否'],
    ['是', 'C2', 10.0, '否'],
    ['否', 'C1', 7.2, '否'],
    ['是', 'C2', 12.7, '否'],
    ['否', 'C3', 10.5, '是'],
    ['否', 'C2', 6.3, '否'],
    ['是', 'C3', 21.2, '否'],
    ['否', 'C1', 8.6, '是'],
    ['是', 'C2', 7.0, '否'],
    ['否', 'C1', 9.4, '是']
])



# 离散型
def giniClassify(y, x):
    x_id, x_ct = np.unique(x, return_counts=True)
    p_x = [ct / sum(ct) for ct in [np.unique(x, return_counts=True)[1]]]
    gini = [1 - np.sum(p ** 2) for p in
            [ct / sum(ct) for ct in [np.unique(y[x == i], return_counts=True)[1] for i in x_id]]]


    return np.sum(np.array(p_x) * np.array(gini))


columnsl = ['ID','年龄','有工作','有自己的房子','信贷情况','类别']
datal = np.array([['1', '青年', '否', '否', '一般', '否'],
                 ['2', '青年', '否', '否', '好', '否'],
                 ['3', '青年', '是', '否', '好', '是'],
                 ['4', '青年', '是', '是', '一般', '是'],
                 ['5', '青年', '否', '否', '一般', '否'],
                 ['6', '中年', '否', '否', '一般', '否'],
                 ['7', '中年', '否', '否', '好', '否'],
                 ['8', '中年', '是', '是', '好', '是'],
                 ['9', '中年', '否', '是', '非常好', '是'],
                 ['10', '中年', '否', '是', '非常好', '是'],
                 ['11', '老年', '否', '是', '非常好', '是'],
                 ['12', '老年', '否', '是', '好', '是'],
                 ['13', '老年', '是', '否', '好', '是'],
                 ['14', '老年', '是', '否', '非常好', '是'],
                 ['15', '老年', '否', '否', '一般', '否']
                 ])



columnsz = ['色泽', '根蒂', '敲声', '纹理', '脐部', '触感', '好瓜']
dataz = np.array([
    ['青绿', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '是'],
    ['乌黑', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑', '是'],
    ['乌黑', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '是'],
    ['青绿', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑', '是'],
    ['浅白', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '是'],
    ['青绿', '稍蜷', '浊响', '清晰', '稍凹', '软粘', '是'],
    ['乌黑', '稍蜷', '浊响', '稍糊', '稍凹', '软粘', '是'],
    ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '硬滑', '是'],
    ['乌黑', '稍蜷', '沉闷', '稍糊', '稍凹', '硬滑', '否'],
    ['青绿', '硬挺', '清脆', '清晰', '平坦', '软粘', '否'],
    ['浅白', '硬挺', '清脆', '模糊', '平坦', '硬滑', '否'],
    ['浅白', '蜷缩', '浊响', '模糊', '平坦', '软粘', '否'],
    ['青绿', '稍蜷', '浊响', '稍糊', '凹陷', '硬滑', '否'],
    ['浅白', '稍蜷', '沉闷', '稍糊', '凹陷', '硬滑', '否'],
    ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '软粘', '否'],
    ['浅白', '蜷缩', '浊响', '模糊', '平坦', '硬滑', '否'],
    ['青绿', '蜷缩', '沉闷', '稍糊', '稍凹', '硬滑', '否']
])
dfy = pd.DataFrame(data=datay, columns=columnsy)
dfl = pd.DataFrame(data = datal,columns = columnsl)
dfz = pd.DataFrame(data=dataz, columns=columnsz)

def giniD(u,v):

    pFi =[ct/np.sum(ct) for ct in [np.unique(u,return_counts=True)[1]]]
    uid, uct = np.unique(u, return_counts=True)
    giniFi = [1- np.sum([p ** 2 for p in ct / np.sum(ct)]) for ct in
             [np.unique(v[u == i], return_counts=True)[1] for i in uid]]

    feature_gini = np.sum(pFi * np.array(giniFi))

    return Decimal(str(feature_gini)).quantize(Decimal('0.0000'))

def giniC(u,v):
    u = u.astype(float)
    sortedu = np.sort(u)

    tlist=[]
    tdict={}
    for i in range(len(u)-1):
        t = np.mean([sortedu[i],sortedu[i+1]])
        tlist.append(t)
    for i in tlist:
        ui = u.apply(lambda x: 0 if x <=i else 1)
        uid,uct = np.unique(ui,return_counts=True)
        pUi = [ct/sum(ct) for ct in [np.unique(ui,return_counts=True)[1]]]

        giniUi = [1-np.sum([p**2 for p in ct/sum(ct)]) for ct in [np.unique(v[ui==i],return_counts=True)[1] for i in uid]]
        tdict[i]=np.sum(pUi * np.array(giniUi))

    # 相同最大值，用最后一个
    klist = [k for k, v in tdict.items() if v == min(tdict.values())]
    return {'t': klist[-1], 'criterionvalue': min(tdict.values())}
    #return {'t':min(tdict,key=tdict.get),'criterionvalue':min(tdict.values())}

a = giniD(dfy.iloc[:,0],dfy.iloc[:,-1])
print('----------------',a)
print('----------------',giniD(dfy.iloc[:,1],dfy.iloc[:,-1]))


print('----------------',giniD(dfl.iloc[:,1],dfl.iloc[:,-1]))


u=dfl.iloc[:,1]
v=dfl.iloc[:,-1]
p =[ct/np.sum(ct) for ct in [np.unique(u,return_counts=True)[1]]]
uid, uct = np.unique(u, return_counts=True)
ginis = [1- np.sum([p ** 2 for p in ct / np.sum(ct)]) for ct in
         [np.unique(v[u == i], return_counts=True)[1] for i in uid]]
print(ginis)

print(giniC(dfy.iloc[:,2],dfy.iloc[:,-1]))

money=['125k','100k','70k','120k','95k','60k','220k','85k','75k','90k']
label=['no','no','no','no','yes','no','no','yes','no','yes']

money2 = pd.Series(money).apply(lambda x: int(x[:-1]))
label = pd.Series(label)
print(money2)
df = pd.DataFrame({'money':money2,'label':label})
print(df)
print(giniC(df['money'],df['label']))


A=[1,1,1,0,0]
B=[1,1,0,1,1]
label=[1,1,0,0,0]

df = pd.DataFrame({'a':A,'b':B,'c':label})
print(df)

print(giniD(df.a,df.c))
print(giniD(df.b,df.c))

columns=['Outlook',	    'Temp',	    'Humidity',	'Wind',	'Decision']
data=[['Sunny	    ','Hot	        ','High	    ','Weak	    ','No'],
['Sunny	    ','Hot	        ','High	    ','Strong	','No'],
['Overcast	','Hot	        ','High	    ','Weak	    ','Yes'],
['Rain	    ','Mild	        ','High	    ','Weak	    ','Yes'],
['Rain	    ','Cool	        ','Normal	','Weak	    ','Yes'],
['Rain	    ','Cool	        ','Normal	','Strong	','No'],
['Overcast	','Cool	        ','Normal	','Strong	','Yes'],
['Sunny	    ','Mild	        ','High	    ','Weak	    ','No'],
['Sunny	    ','Cool	        ','Normal	','Weak	    ','Yes'],
['Rain	    ','Mild	        ','Normal	','Weak	    ','Yes'],
['Sunny	    ','Mild	        ','Normal	','Strong	','Yes'],
['Overcast	','Mild	        ','High 	','Strong	','Yes'],
['Overcast	','Hot	        ','Normal	','Weak	    ','Yes'],
['Rain	    ','Mild	        ','High	    ','Strong	','No']]
df = pd.DataFrame(data = data,columns=columns)
print(df)
for i in columns:
    df[i]=df[i].apply(lambda x: x.strip())
print(df)
for i in columns[:-1]:
    print(i,giniD(df[i],df.iloc[:,-1]))