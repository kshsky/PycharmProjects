import xgboost as xgb
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
from decimal import *

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

print(df)
#create cart

className = ['benign' if i==0 else 'malignant' for i in y]

giniDict ={}

for i in columns[:-1]:
    gini = giniRegression(df.iloc[:,-1],df[i])
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
print(giniRegression(y_train,df['worst perimeter']))



'''
class sklearn.linear_model.LogisticRegression(penalty='l2', dual=False,tol=0.0001, C=1.0, 
fit_intercept=True, intercept_scaling=1,class_weight=None,random_state=None, solver='liblinear', 
max_iter=100, multi_class='ovr',verbose=0, warm_start=False, n_jobs=1)
'''

# from sklearn.linear_model import LogisticRegression
#
# # 逻辑回归
# lr = LogisticRegression(max_iter=10000)
# # 训练模型
# lr.fit(X_train, y_train)
# # 预测
# y_pred = lr.predict(X_test)
#
# print(metrics.classification_report(y_test, y_pred, target_names=['Benign','Malignant']))
# print(metrics.accuracy_score(y_test, y_pred))
#=========================
# from sklearn import tree
# # 决策树
# clf = tree.DecisionTreeClassifier(max_depth=4)
#
# # 训练模型
# clf.fit(X_train,y_train)
#   # 预测
# y_pred = clf.predict(X_test)
# print(metrics.classification_report(y_test, y_pred, target_names=['Benign','Malignant']))
# print(metrics.accuracy_score(y_test, y_pred))
#
# import graphviz
'''
sklearn.tree.export_graphviz(decision_tree, out_file=None, *, max_depth=None, 
feature_names=None, class_names=None, 
label='all', filled=False, leaves_parallel=False, 
impurity=True, node_ids=False, proportion=False, rotate=False, 
rounded=False, special_characters=False, precision=3,
fontname='helvetica')[source]¶
'''
# dot_data = tree.export_graphviz(clf, out_file="dataFile/breastCancerTree.dot",
#                          feature_names=cancer.feature_names,
#                          class_names=cancer.target_names,
#                          filled=True, rounded=True,
#                          special_characters=True)
# graph = graphviz.Source(dot_data)

#渲染dot文件
from graphviz import Source
# path = 'dataFile/breastCancerTree.dot'
# s = Source.from_file(path,format='png')
#默认format='pdf'
# s = Source.from_file(path)
# s.view()
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

print(split_point_list)
# 依次计算每个分界点分割后的gini系数
for i in split_point_list:
    # 分界后，就是二分类了
    xi=[1 if x.compare(i)==1 else 0 for x in xList]

    # 根据新分界点，计算权重（频数、概率）
    w_i = [[p for p in ct / np.sum(ct)] for ct in [np.unique(xi, return_counts=True)[1]]]
    print(np.unique(xi, return_counts=True))
    # 分类
    x_id, x_ct = np.unique(xi, return_counts=True)

    # 每个分界点分类的gini
    gini_x_id = [np.sum([(p - p ** 2) for p in ct / np.sum(ct)]) for ct in
                 [np.unique(y[xi == i], return_counts=True)[1] for i in x_id]]
    print(x_id,[np.unique(y[xi == i], return_counts=True) for i in x_id])
    print('gini_x_id',gini_x_id)
    # 计算每个分界点的gini
    gini = Decimal(str(np.sum(w_i * np.array(gini_x_id)))).quantize(Decimal('0.0000'),ROUND_HALF_UP)
    print(gini)
    split_point_gini.append(gini)
print(np.min(split_point_gini))
# 0.343
# ===============================================================
x = [66,27,58,25,27,46,62,21,44,56,21,48,36,44,48,25,34,47,25,18]
y = [1,0,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,0,0,0]
df = pd.DataFrame({'x':np.array(x),'y':np.array(y)})
print(giniRegression(df['y'],df['x']))
# 0.4105

# =================================================================
