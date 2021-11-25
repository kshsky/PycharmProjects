import xgboost as xgb
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
from decimal import *

def gini_CART_split_clf(u,v):
    vid, vct = np.unique(v, return_counts=True)
    #依照每个vid划分为两个子集
    d1 = [1 - np.sum([p ** 2 for p in ct / np.sum(ct)]) for ct in
            [np.unique(u[v == i], return_counts=True)[1] for i in vid]]
    d2 = [1 - np.sum([p ** 2 for p in ct / np.sum(ct)]) for ct in
            [np.unique(u[v != i], return_counts=True)[1] for i in vid]]
    d1p = [ct / np.sum(ct) for ct in [np.unique(v, return_counts=True)[1]]]
    d2p = np.ones_like(d1p) - d1p
    #每个子集的gini乘以每个子集的概率，然后相加，就是该划分节点的gini系数
    split_gini = np.array(d1) * np.array(d1p) + np.array(d2) * np.array(d2p)
    splitGiniDict={}
    for i in range(len(vid)):
        gini = Decimal(str(split_gini[0][i])).quantize(Decimal('0.0000'))
        splitGiniDict.update({vid[i]:gini})
    return splitGiniDict

def gini_CART_feature_clf(u,v):
    vid, vct = np.unique(v, return_counts=True)
    #依照每个vid划分为两个子集
    d1 = [1 - np.sum([p ** 2 for p in ct / np.sum(ct)]) for ct in
            [np.unique(u[v == i], return_counts=True)[1] for i in vid]]
    d2 = [1 - np.sum([p ** 2 for p in ct / np.sum(ct)]) for ct in
            [np.unique(u[v != i], return_counts=True)[1] for i in vid]]
    d1p = [ct / np.sum(ct) for ct in [np.unique(v, return_counts=True)[1]]]
    d2p = np.ones_like(d1p) - d1p
    #每个子集的gini乘以每个子集的概率，然后相加，
    split_gini = np.array(d1) * np.array(d1p) + np.array(d2) * np.array(d2p)
    gini = np.sum(np.array(d1p) * split_gini)
    return Decimal(str(gini)).quantize(Decimal('0.0000'))

def gini_book_feature_reg(y, x):
    gini_reg_dict={}
    xList=[]
    for i in x:
        xList.append(Decimal(i))
    # print(xList)
    sorted_x = np.sort(xList)
    split_point_list = []
    split_point_gini =[]
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
        # 分类
        x_id, x_ct = np.unique(xi, return_counts=True)

        # 根据新分界点，计算权重（频数、概率）
        d1p = [[p for p in ct / np.sum(ct)] for ct in [np.unique(xi, return_counts=True)[1]]]

        # 每个分界点分类的gini
        d1 = [1 - np.sum([p**2 for p in ct / np.sum(ct)]) for ct in
                     [np.unique(y[xi == i], return_counts=True)[1] for i in x_id]]

        # 计算每个分界点的gini
        gini = np.sum(np.array(d1)*np.array(d1p))
        gini_reg_dict.update({i:gini})
        split_point_gini.append(Decimal(str(gini)).quantize(Decimal('0.0000')))
    minGini = np.min(split_point_gini)
    return minGini

def yhl_gini_feature(u,v):
    print('--- feature 的 gini ---')
    p =[ct/np.sum(ct) for ct in [np.unique(v,return_counts=True)[1]]]
    vid, vct = np.unique(v, return_counts=True)
    ginis = [1- np.sum([p ** 2 for p in ct / np.sum(ct)]) for ct in
             [np.unique(u[v == i], return_counts=True)[1] for i in vid]]
    feature_gini = np.sum(p * np.array(ginis))
    return Decimal(str(feature_gini)).quantize(Decimal('0.0000'))

def gini_book_feature_clf(u,v):
    vid,vct = np.unique(v,return_counts=True)
    d = [1- np.sum([p**2 for p in ct/np.sum(ct)]) for ct in [np.unique(u[v == i],return_counts=True)[1] for i in vid]]
    dp = [ct/np.sum(ct) for ct in [np.unique(v,return_counts=True)[1]]]
    gini = np.sum(np.array(d)*np.array(dp))
    return Decimal(str(gini)).quantize(Decimal('0.0000'))


# 加载数据
cancer = datasets.load_breast_cancer()
# print(cancer)
columns = cancer.feature_names
print(columns)
X = cancer.data
y = cancer.target
# # 划分训练集、测试集
X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size = 1/5.,random_state = 8)

df = pd.DataFrame(data = X_train,columns=columns)
df['label']=y_train

#create cart

className = ['benign' if i==0 else 'malignant' for i in y]

giniDict ={}

for i in columns[:-1]:
    gini = gini_book_feature_reg(df.iloc[:,-1],df[i])
    giniDict.update({i:gini})

print('===============')
print(giniDict)
rootGini = min(giniDict,key=giniDict.get)
print('train',rootGini,giniDict.get(rootGini))

#依次截取相邻值的平均值作为分界点，得出n-1个gini值，取最小值，作为当前属性的gini值

'''
['mean radius' 'mean texture' 'mean perimeter' 'mean area'
 'mean smoothness' 'mean compactness' 'mean concavity'
 'mean concave points' 'mean symmetry' 'mean fractal dimension'
 'radius error' 'texture error' 'perimeter error' 'area error'
 'smoothness error' 'compactness error' 'concavity error'
 'concave points error' 'symmetry error' 'fractal dimension error'
 'worst radius' 'worst texture' 'worst perimeter' 'worst area'
 'worst smoothness' 'worst compactness' 'worst concavity'
 'worst concave points' 'worst symmetry' 'worst fractal dimension']
'''
df = pd.DataFrame(data = X_train,columns=columns)
df['label']=y_train
# print(giniRegression(y_train,df['worst perimeter']))

# ==========================================================
# 游皓麟 P165
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
print('--------------yhl----------------')
print(gini_book_feature_clf(df.iloc[:,-1],df.iloc[:,0]))
print(gini_CART_feature_clf(df.iloc[:,-1],df.iloc[:,0]))
print(gini_CART_split_clf(df.iloc[:,-1],df.iloc[:,0]))
print(gini_book_feature_clf(df.iloc[:,-1],df.iloc[:,1]))
print(gini_CART_feature_clf(df.iloc[:,-1],df.iloc[:,1]))
print(gini_CART_split_clf(df.iloc[:,-1],df.iloc[:,1]))
'''
--------------yhl----------------
0.2400
0.2400
{'否': Decimal('0.2400'), '是': Decimal('0.2400')}
0.3000
0.3467
{'C1': Decimal('0.3667'), 'C2': Decimal('0.3000'), 'C3': Decimal('0.4000')}

'''
x = df.iloc[:,2]
y = df.iloc[:,-1]
xList = []
for i in x:
    xList.append(Decimal(i))

# print(xList)
sorted_x = np.sort(xList)
# print(sorted_x)
split_point_list = []
split_point_gini = []
# 求分界点
for i in range(0, len(sorted_x) - 1, 1):
    a = Decimal(str(sorted_x[i]))
    b = Decimal(str(sorted_x[i + 1]))
    split_point_list.append((a+b)/2)

# 依次计算每个分界点分割后的gini系数
for i in split_point_list:
    # 分界后，就是二分类了
    xi=[1 if x.compare(i)==1 else 0 for x in xList]

    # 根据新分界点，计算权重（频数、概率）
    d1 = [[p for p in ct / np.sum(ct)] for ct in [np.unique(xi, return_counts=True)[1]]]
    # 分类
    x_id, x_ct = np.unique(xi, return_counts=True)

    # 每个分界点分类的gini
    d1p = [1- np.sum([ p**2 for p in ct / np.sum(ct)]) for ct in
                 [np.unique(y[xi == i], return_counts=True)[1] for i in x_id]]
    # 计算每个分界点的gini
    gini = Decimal(str(np.sum(d1 * np.array(d1p)))).quantize(Decimal('0.0000'),ROUND_HALF_UP)
    split_point_gini.append(gini)

print(np.min(split_point_gini))
# 0.3429
# ===============================================================
print('===========giniRegression================')
x = [66,27,58,25,27,46,62,21,44,56,21,48,36,44,48,25,34,47,25,18]
y = [1,0,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,0,0,0]
df = pd.DataFrame({'x':np.array(x),'y':np.array(y)})
print(gini_book_feature_reg(df['y'],df['x']))
# 0.4105

# =================================================================
'''
计算属性v的k个分类点的gini系数
对于每个分类点vid，划分为两个子集：d1和d2
对于子集d1,响应变量可能有k个类别，计算该划分节点的gini值
对于子集d2,响应变量可能有k个类别，计算该划分节点的gini值
计算每一个vid对应的该特征的gini值

'''


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

df_zzh = pd.DataFrame(data=data, columns=columns)
for i in df_zzh.columns[:-1]:
    v = df_zzh.loc[:,i]
    u = df_zzh.iloc[:,-1]
    print(gini_CART_split_clf(u,v))
    print('book-feature:',gini_book_feature_clf(u,v))
    print('cart-feature:',gini_CART_feature_clf(u,v))

'''
{'乌黑': Decimal('0.4563'), '浅白': Decimal('0.4373'), '青绿': Decimal('0.4973')}
book-feature: 0.4275
cart-feature: 0.4652
{'硬挺': Decimal('0.4392'), '稍蜷': Decimal('0.4958'), '蜷缩': Decimal('0.4559')}
book-feature: 0.4223
cart-feature: 0.4704
{'沉闷': Decimal('0.4941'), '浊响': Decimal('0.4504'), '清脆': Decimal('0.4392')}
book-feature: 0.4235
cart-feature: 0.4620
{'模糊': Decimal('0.4034'), '清晰': Decimal('0.2859'), '稍糊': Decimal('0.4373')}
book-feature: 0.2771
cart-feature: 0.3512
{'凹陷': Decimal('0.4151'), '平坦': Decimal('0.3620'), '稍凹': Decimal('0.4973')}
book-feature: 0.3445
cart-feature: 0.4316
{'硬滑': Decimal('0.4941'), '软粘': Decimal('0.4941')}
book-feature: 0.4941
cart-feature: 0.4941
'''

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
df_lh = pd.DataFrame(data=data, columns=columns)
for i in df_lh.columns[:-1]:
    v = df_lh.loc[:,i]
    u = df_lh.iloc[:,-1]
    print(gini_CART_split_clf(u,v))
    print('book-feature:',gini_book_feature_clf(u,v))
    print('cart-feature:',gini_CART_feature_clf(u,v))
'''
{'1': Decimal('0.4286'), '10': Decimal('0.4571'), '11': Decimal('0.4571'), '12': Decimal('0.4571'), '13': Decimal('0.4571'), '14': Decimal('0.4571'), '15': Decimal('0.4286'), '2': Decimal('0.4286'), '3': Decimal('0.4571'), '4': Decimal('0.4571'), '5': Decimal('0.4286'), '6': Decimal('0.4286'), '7': Decimal('0.4286'), '8': Decimal('0.4571'), '9': Decimal('0.4571')}
book-feature: 0.0000
cart-feature: 0.4457
{'中年': Decimal('0.4800'), '老年': Decimal('0.4400'), '青年': Decimal('0.4400')}
book-feature: 0.4267
cart-feature: 0.4533
{'否': Decimal('0.3200'), '是': Decimal('0.3200')}
book-feature: 0.3200
cart-feature: 0.3200
{'否': Decimal('0.2667'), '是': Decimal('0.2667')}
book-feature: 0.2667
cart-feature: 0.2667
{'一般': Decimal('0.3200'), '好': Decimal('0.4741'), '非常好': Decimal('0.3636')}
book-feature: 0.2844
cart-feature: 0.3933
'''