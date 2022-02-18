import pandas as pd
import numpy as np

#熵
from graphviz import Digraph


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

def display(idict):
    for i in idict.keys():
        print(i,idict[i])
# columns = ['色泽', '根蒂', '敲声', '纹理', '脐部', '触感', '好瓜']
# data = np.array([
#     ['青绿', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '是'],
#     ['乌黑', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑', '是'],
#     ['乌黑', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '是'],
#     ['青绿', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑', '是'],
#     ['浅白', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '是'],
#     ['青绿', '稍蜷', '浊响', '清晰', '稍凹', '软粘', '是'],
#     ['乌黑', '稍蜷', '浊响', '稍糊', '稍凹', '软粘', '是'],
#     ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '硬滑', '是'],
#     ['乌黑', '稍蜷', '沉闷', '稍糊', '稍凹', '硬滑', '否'],
#     ['青绿', '硬挺', '清脆', '清晰', '平坦', '软粘', '否'],
#     ['浅白', '硬挺', '清脆', '模糊', '平坦', '硬滑', '否'],
#     ['浅白', '蜷缩', '浊响', '模糊', '平坦', '软粘', '否'],
#     ['青绿', '稍蜷', '浊响', '稍糊', '凹陷', '硬滑', '否'],
#     ['浅白', '稍蜷', '沉闷', '稍糊', '凹陷', '硬滑', '否'],
#     ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '软粘', '否'],
#     ['浅白', '蜷缩', '浊响', '模糊', '平坦', '硬滑', '否'],
#     ['青绿', '蜷缩', '沉闷', '稍糊', '稍凹', '硬滑', '否']
# ])

# df_xigua = pd.DataFrame(data=data, columns=columns)
import pandas as pd
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

wine = load_wine()
print(wine.feature_names)
# print(wine.target)

# criterion="gini"
# criterion="entropy"

Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data,wine.target,test_size=0.2,random_state=8)
columns= ['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']
columns.append('target')
# 其中第1类有59个样本，第2类有71个样本，第3类有48个样本。
print(columns)
#默认gini作为分类依据，CART算法
# clf = tree.DecisionTreeClassifier(criterion=criterion)
# clf= clf.fit(Xtrain, Ytrain)
print(type(Xtrain),type(Ytrain))
df = pd.concat([pd.DataFrame(Xtrain),pd.DataFrame({13:Ytrain})],axis=1)


print(df)
# print(df)

# 字典构造分析：
#                                  纹理-node
#            |(清晰)                  |(稍糊)        |(模糊)
#           根蒂 -node               触感            否 - leaf
#  |(蜷缩)   |(稍蜷)    |(硬挺)    |(硬滑) |(软粘)
# 好-leaf   色泽-node  否-leaf    否      是
#可见
# node ：parentnode 对分支节点有效，对叶子节点无效
# 解决方案： 采用 parentNode + parentEdge : node  方式构造字典，key唯一
# node 值为flagcolumn是为叶子节点，shape=ellipse
# 分支节点，shape=box

# 全局var
flagColumn='target'

#level + 父node + 父edge ：子node
parentChildDict={}
#列增益字典
columnGainDict={}
#增益最大列分割字典
edgeSplitDfdict={}
nodeDfDict={}
#每次遍历的开始
nodelist = []

#层级
k=0
flag=True
while True:
    if len(nodelist)==0:
        print('寻找根节点')
        for i in columns[:-1]:
            columnGainDict.update({i:gainuv(df[flagColumn],df[i])})

        for i in columnGainDict.keys():
            print(i,columnGainDict[i])

        #信息增益最大的列
        maxColumnName = max(columnGainDict, key=columnGainDict.get)
        print('根节点',maxColumnName)
        #增加父子节点字典
        parentChildDict.update({0:maxColumnName})


        nodelist.append(maxColumnName)
        nodeDfDict.update({maxColumnName:df})
        k+=1
        print('-----{}------'.format(k))
    else:
        newnodelist = nodelist
        nodelist=[]
        for ii in newnodelist:
            node = ii
            print('=======================================================',ii)
            # 根据增益最大列进行分割df，并存入字典
            newDf =nodeDfDict[node]
            print(newDf)
            #这里做判断，是否进行循环

            vid, vct = np.unique(newDf[node], return_counts=True)
            columnGainDict.clear()
            edgeNodeDict = {}
            for i in vid:
                columnGainDictTemp = {}
                splitDf = newDf[newDf[node] == i]
                # edgeSplitDfdict -> nodeDfDict 重新进入循环
                edgeSplitDfdict.update({i: newDf[newDf[node] == i]})
                if entU(splitDf[node])==0 and entU(splitDf[flagColumn]) == 0:
                    #叶子节点
                    leaf = list(set(splitDf[flagColumn]))[0]
                    parentChildDict.update({str(k)+node + '+' + i: leaf})
                    print('leaf:',node + '+' + i,leaf)
                else:
                    for j in columns[:-1]:
                        jgainuv = gainuv(splitDf[flagColumn], splitDf[j])
                        columnGainDictTemp.update({j: jgainuv})
                        print(i, j, jgainuv)
                        # print(columnGainDict)
                    # print(columnGainDictTemp)
                    edgeNodeDict.update({i: columnGainDictTemp})

            for i in parentChildDict.keys():
                print(i, parentChildDict[i])
            print('----before')
            for i in edgeNodeDict.keys():
                tempDict = edgeNodeDict[i]
                print(i, tempDict)
                newNode = max(tempDict, key=tempDict.get)
                parentChildDict.update({str(k)+node + '+' + i: newNode})
                nodeDfDict.update({newNode: edgeSplitDfdict[i]})
                nodelist.append(newNode)
            print('----after')
            for i in parentChildDict.keys():
                print(i, parentChildDict[i])
            print('---------------------------------------------------')
            print(nodelist)
            print('-----{}------'.format(k))
            if len(nodelist)==0:
                flag=False
                break
        k += 1
        if flag==False:
            break
    if flag==False:
        break

display(parentChildDict)

#format='pdf'
dot = Digraph(name='decisionTreeGannuv', format="png",
              node_attr={'style':'filled',"fontname":'Microsoft YaHei'},
              edge_attr={"fontname":'Microsoft YaHei'})

for i in parentChildDict.keys():
    print()
    if i ==0:
        dot.node(name=str(1)+parentChildDict[i])
    else:
        levelstr = ''.join(list(filter(str.isdigit,i)))
        parentNode,edge = i.split('+')
        print(levelstr,parentNode,edge)
        levelint = int(levelstr)
        childnode = parentChildDict[i]
        newparentnode = parentNode[len(levelstr):]
        leafAttrList = list(set(df[flagColumn]))
        #叶子节点
        if childnode in leafAttrList:
            newchildnode= str(levelint+1)+edge+childnode
            dot.node(name= newchildnode,label=childnode)
        else:
            #非叶子节点
            newchildnode= str(levelint+1)+childnode
            dot.node(name= newchildnode,label=childnode,shape='box')

        dot.node(name = parentNode,label=newparentnode)
        dot.edge(parentNode,newchildnode,edge)
print(dot.source)
dot.render('datafile/decisionTreeGainuv.dot', view=True)
# 0 纹理
# 1纹理+模糊 否
# 1纹理+清晰 根蒂
# 1纹理+稍糊 触感
# 2根蒂+硬挺 否
# 2根蒂+蜷缩 是
# 2根蒂+稍蜷 色泽
# 2触感+硬滑 否
# 2触感+软粘 是
# 3色泽+青绿 是
# 3色泽+乌黑 触感
# 4触感+硬滑 是
# 4触感+软粘 否




