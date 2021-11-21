import pandas as pd
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

wine = load_wine()


Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data,wine.target,test_size=0.2,random_state=8)
clf = tree.DecisionTreeClassifier(criterion="gini")
# clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(Xtrain, Ytrain)

feature_name = ['酒精','苹果酸','灰','灰的碱性','镁','总酚','类黄酮','非黄烷类酚类','花青素','颜色强度','色调','od280/od315稀释葡萄酒','脯氨酸']

'''
sklearn.tree.export_graphviz(decision_tree, out_file=None, *, max_depth=None, 
feature_names=None, class_names=None, 
label='all', filled=False, leaves_parallel=False, 
impurity=True, node_ids=False, proportion=False, rotate=False, 
rounded=False, special_characters=False, precision=3,
fontname='helvetica')[source]¶


def export_graphviz(decision_tree, out_file=None, *, max_depth=None,
                    feature_names=None, class_names=None, label='all',
                    filled=False, leaves_parallel=False, impurity=True,
                    node_ids=False, proportion=False, rotate=False,
                    rounded=False, special_characters=False, precision=3):
'''
import graphviz
dot_data = tree.export_graphviz(clf, out_file="dataFile/wineTree.dot"
                                ,feature_names = feature_name
                                ,class_names=["琴酒","雪莉","贝尔摩德"]
                                ,filled=True,rounded=True)
graph = graphviz.Source(dot_data)


#渲染dot文件
from graphviz import Source
# path = 'dataFile/wineTree.dot'
# s = Source.from_file(path,format='png')
#默认format='pdf'
# s = Source.from_file(path)
# s.view()

with open('dataFile/wineTree.dot',encoding='utf-8') as f:
    dot_txt = f.read()
fromDot = graphviz.Source(dot_txt.replace('helvetica','FangSong'),directory='dataFile',filename='wineTree',format='pdf')
fromDot.view()