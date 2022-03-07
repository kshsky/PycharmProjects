from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
X,y = make_blobs(n_features=2,centers=4,random_state=1)
km = KMeans(n_clusters=5).fit(X)
print(km.cluster_centers_)
print(km.labels_)
print(km.inertia_)

import collections
print(collections.Counter('aaabbbcccccccdde'))
from sklearn.datasets import *
from sklearn.model_selection import *
from sklearn import tree
from sklearn.metrics import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#决策边界绘制函数
def plot_decision_boundary(X_in,y_in,pred_func):
    x_min, x_max = X_in[:, 0].min() - .5, X_in[:, 0].max() + .5
    y_min, y_max = X_in[:, 1].min() - .5, X_in[:, 1].max() + .5
    h = 0.01
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z,cmap=plt.get_cmap('GnBu'))
    plt.scatter(X_in[:, 0], X_in[:, 1], c=y_in,cmap=plt.get_cmap('GnBu'))
#在不同的正负样本比例下训练决策树，并画出决策边界，计算AUC
for weight_minority in [0.01,0.05,0.1,0.2,0.5]:
    X,y=make_classification(n_samples=500,n_features=2,n_redundant=0,random_state=2,n_clusters_per_class=1,weights=(weight_minority,1-weight_minority))
    plt.scatter(X[:,0],X[:,1],c=y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,random_state=6)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    plot_decision_boundary(X,y,lambda x: clf.predict(x))
    plt.ion()
    plt.title("Decision Tree with imbalance rate: "+str(weight_minority))
    plt.show()
    print("current auc:"+str(roc_auc_score(y_test, clf.predict(X_test))))
    print("----------------------------------")
from sklearn.preprocessing import OneHotEncoder

one = OneHotEncoder()