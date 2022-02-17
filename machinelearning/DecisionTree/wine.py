import pandas as pd
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

wine = load_wine()
print(wine.feature_names)
# print(wine.target)

criterion="gini"
# criterion="entropy"

Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data,wine.target,test_size=0.2,random_state=8)
#默认gini作为分类依据，CART算法
clf = tree.DecisionTreeClassifier(criterion=criterion)
clf= clf.fit(Xtrain, Ytrain)

# feature_name = ['酒精','苹果酸','灰','灰的碱性','镁','总酚','类黄酮','非黄烷类酚类','花青素','颜色强度','色调','od280/od315稀释葡萄酒','脯氨酸']
feature_name = ['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']

'''
sklearn.tree.export_graphviz(decision_tree, out_file=None, *, max_depth=None, 
                    feature_names=None, class_names=None, 
                    label='all', filled=False, leaves_parallel=False, 
                    impurity=True, node_ids=False, proportion=False, rotate=False, 
                    rounded=False, special_characters=False, precision=3,
                    fontname='helvetica')[source]
'''
import graphviz

dot_data = tree.export_graphviz(clf
                                , out_file="dataFile/wineTree.dot"
                                ,feature_names = wine.feature_names
                                ,class_names=["琴酒","雪莉","贝尔摩德"]
                                ,filled=True,rounded=True)
graph_entropy = graphviz.Source(dot_data)

#渲染dot文件
from graphviz import Source

# source.from_file(path) 不能修改原来helvetica字体乱码问题
# path = 'datafile/wineTree.dot'
# s = Source.from_file(path,format='png')
# 默认format='pdf'
# s = Source.from_file(path)
# s.view()

with open('dataFile/wineTree.dot',encoding='utf-8') as f:
    dot_txt = f.read()
fromDot = graphviz.Source(dot_txt.replace('helvetica','FangSong'),directory='datafile',filename='wineTree',format='png')
fromDot.view()