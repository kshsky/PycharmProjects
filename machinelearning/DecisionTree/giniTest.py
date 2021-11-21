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
    vidEntropy = [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(u[v == i], return_counts=True)[1] for i in vid]]

    #条件熵
    entUconditonV= np.sum(np.array(vidEntropy) * (vct / np.sum(vct)))

    return entUconditonV

#信息增益
def gainuv(u,v):

    return entU(u) - uConditionV(u,v)

columns = ['有固定资产(X1)', '家庭类型(X2)', '月收入(X3)', 'VIP用户']
data = np.array([
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
df = pd.DataFrame(data=data, columns=columns)


# 离散型
def giniClassify(y, x):
    x_id, x_ct = np.unique(x, return_counts=True)
    p_x = [ct / sum(ct) for ct in [np.unique(x, return_counts=True)[1]]]
    gini = [1 - np.sum(p ** 2) for p in
            [ct / sum(ct) for ct in [np.unique(y[x == i], return_counts=True)[1] for i in x_id]]]


    return np.sum(np.array(p_x) * np.array(gini))

x = df['有固定资产(X1)']
y=df['VIP用户']
print(round(giniClassify(y, x), 4))
# 0.24
x = df['家庭类型(X2)']
print(round(giniClassify(y, x), 4))
# 0.3


# 连续型分类变量
x = df['月收入(X3)'].astype(float)
y = df.VIP用户


def giniRegression(y, x):
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
        # split_point_gini.append(round(np.sum(w_i * np.array(gini_x_id)), 4))
        gini = Decimal(str(np.sum(w_i * np.array(gini_x_id)))).quantize(Decimal('0.0000'),ROUND_HALF_UP)
        split_point_gini.append(gini)

    # 封装成字典
    split_point_gini_dict = dict(zip(split_point_list, split_point_gini))


    return split_point_gini_dict

giniClassify(y, x)



# ID	年龄	有工作	有自己的房子	信贷情况	类别
# [1,'青年','否','否','一般','否'],
# [2,'青年','否','否','好','否']
# [3,'青年','是','否','好','是'],
# [4,'青年','是','是','一般','是'],
# [5,'青年','否','否','一般','否'],
# [6,'中年','否','否','一般','否'],
# [7,'中年','否','否','好','否'],
# [8,'中年','是','是','好','是'],
# [9,'中年','否','是','非常好','是'],
# [10,'中年','否','是','非常好','是'],
# [11,'老年','否','是','非常好','是'],
# [12,'老年','否','是','好','是'],
# [13,'老年','是','否','好','是'],
# [14,'老年','是','否','非常好','是'],
# [15,'老年','否','否','一般','否']




columns = ['ID','年龄','有工作','有自己的房子','信贷情况','类别']
data = np.array([['1', '青年', '否', '否', '一般', '否'],
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

data = pd.DataFrame(data = data,columns = columns)
print('gini')
for i in columns[1:-1]:
    print(i,giniClassify(data.iloc[:,-1],data[i]))

print('gianuv')
for i in columns[1:-1]:
    print(i,gainuv(data.iloc[:,-1],data[i]))

u = data.iloc[:,-1]
v = data.iloc[:,1]
vid,vct = np.unique(v,return_counts=True)
# [1 - np.sum(p ** 2) for p in
#             [ct / sum(ct) for ct in [np.unique(y[x == i], return_counts=True)[1] for i in x_id]]]

print([1- np.sum([p **2 for p in ct/np.sum(ct)]) for ct in [np.unique(u[v == i],return_counts = True)[1] for i in vid]])
# print(u)
# print(v)
print(np.unique(v,return_counts=True))
print([np.unique(u[v == i],return_counts = True)[1] for i in vid])
# print(data)
v = data.iloc[:,2]
vid,vct = np.unique(v,return_counts=True)
print(np.unique(v,return_counts=True))
print([np.unique(u[v == i],return_counts = True)[1] for i in vid])
print('==============西瓜=================')
columns = ['色泽', '根蒂', '敲声', '纹理', '脐部', '触感', '好瓜']
data = np.array([
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

df = pd.DataFrame(data=data, columns=columns)
df.to_excel('dataFile/xigua2.0.xlsx')
u = df.iloc[:,-1]
v = df.iloc[:,0]
vid,vct = np.unique(v,return_counts=True)
# print([1- np.sum([p **2 for p in ct/np.sum(ct)]) for ct in [np.unique(u[v == i],return_counts = True)[1] for i in vid]])
print(vid)
# print([np.unique(u[v != i],return_counts = True) for i in vid])
print([np.unique(v[v != i],return_counts = True)[1] for i in vid])
print([np.unique(v[v == i],return_counts = True)[1] for i in vid])
print([np.unique(u[v == i],return_counts = True)[1] for i in vid])
# print([1 - np.sum([p**2 for p in ct/np.sum(ct)]) for ct in [np.unique(v[v == i],return_counts = True)[1] for i in vid]])
print([[p for p in ct/np.sum(ct)] for ct in [np.unique(v[v != i],return_counts = True)[1] for i in vid]])

def gini_index(u,v):
    vid,vct = np.unique(v,return_counts=True)
    # p = [vid/len(v),len(v)-]
    uid,uct = [np.unique(u[i==vid],return_counts=True) for i in vid]