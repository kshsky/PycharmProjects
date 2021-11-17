import pandas as pd
import numpy as np

#熵
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

print('df')
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
flagColumn='好瓜'
usedColumn=[]
usedColumn.append(flagColumn)
#父node + 父edge ：子node
parentChildDict={}
#列增益字典
columnGainDict={}
#增益最大列分割字典
edgeSplitDfdict={}

#边和节点dict
edgeNodeEntropyGainDict={}


#每次遍历的开始
nodeColumns=[]
print('各列的熵：')
for i in columns:
    print(i,entU(df[i]))

print('各列的信息增益：')

for i in columns:
    if i not in usedColumn:
        columnGainDict.update({i:gainuv(df[flagColumn],df[i])})

for i in columnGainDict.keys():
    print(i,columnGainDict[i])

#信息增益最大的列
maxColumnName = max(columnGainDict, key=columnGainDict.get)
#增加父子节点字典
parentChildDict.update({-1:maxColumnName})
#增加used列列表
usedColumn.append(maxColumnName)
#更新nodeColumns , 最大增益列进入节点list
nodeColumns.append(maxColumnName)
# ===================================

newNodeDfDict={}
node = nodeColumns[0]
#根据增益最大列进行分割df，并存入字典
vid,vct = np.unique(df[node],return_counts=True)
nodeColumns.clear()
for i in vid:
    # print(df[df[node]==i])
    edgeSplitDfdict.update({i:df[df[node]==i]})

# print('maxColumnSplitDfdict：（最大增益列分割df）')
# print(maxColumnSplitDfdict)
#循环计算gainuv
#entropy=0,全为好瓜或坏瓜，纯度最高，是叶子节点
columnGainDict.clear()


for i in vid:
    columnGainDictTemp={}
    splitDf = edgeSplitDfdict[i]
    if entU(splitDf[flagColumn])==0:  #叶子节点
        leaf = list(set(splitDf[flagColumn]))[0]
        parentChildDict.update({node+'+'+i:leaf})
        print('leaf:', node + '+' + i,leaf)
    else:
        for j in columns:
            if j not in usedColumn:
                jgainuv= gainuv(splitDf[flagColumn],splitDf[j])
                columnGainDictTemp.update({j:jgainuv})
                print(i,j,jgainuv)
                # print(columnGainDict)
        # print(columnGainDictTemp)
        edgeNodeEntropyGainDict.update({i: columnGainDictTemp})

for i in parentChildDict.keys():
    print(i,parentChildDict[i])
for i in edgeNodeEntropyGainDict.keys():
    tempDict = edgeNodeEntropyGainDict[i]
    print(i,tempDict)
    newNode = max(tempDict,key= tempDict.get)
    print('newNode',newNode)
    parentChildDict.update({node+'+'+i:newNode})
    newNodeDfDict.update({newNode:edgeSplitDfdict[i]})
    nodeColumns.append(newNode)
for i in parentChildDict.keys():
    print(i,parentChildDict[i])

print(newNodeDfDict)
print('第一轮循环结束,第二轮循环开始：')
#第一轮循环结束,第二轮循环开始：
for ii in nodeColumns:
    node = ii
    print('=======================================================',ii)
    # 根据增益最大列进行分割df，并存入字典
    newDf =newNodeDfDict[ii]
    print(newDf)
    vid, vct = np.unique(newDf[node], return_counts=True)

    for i in vid:
        # print(df[df[node] == i])
        edgeSplitDfdict.update({i: newDf[newDf[node] == i]})
    #
    # print('maxColumnSplitDfdict：（最大增益列分割df）')
    # print(maxColumnSplitDfdict)
    # 循环计算gainuv
    # entropy=0,全为好瓜或坏瓜，纯度最高，是叶子节点
    columnGainDict.clear()
    edgeNodeDict = {}
    for i in vid:
        columnGainDictTemp = {}
        splitDf = edgeSplitDfdict[i]
        if entU(splitDf[flagColumn]) == 0:  # 叶子节点
            leaf = list(set(splitDf[flagColumn]))[0]
            parentChildDict.update({node + '+' + i: leaf})
            print('leaf:',node + '+' + i,leaf)
        else:
            for j in columns:
                if j not in usedColumn:
                    jgainuv = gainuv(splitDf[flagColumn], splitDf[j])
                    columnGainDictTemp.update({j: jgainuv})
                    print(i, j, jgainuv)
                    # print(columnGainDict)
            # print(columnGainDictTemp)
            edgeNodeDict.update({i: columnGainDictTemp})

    for i in parentChildDict.keys():
        print(i, parentChildDict[i])
    for i in edgeNodeDict.keys():
        tempDict = edgeNodeDict[i]
        print(i, tempDict)
        newNode = max(tempDict, key=tempDict.get)
        parentChildDict.update({node + '+' + i: newNode})
        newNodeDfDict.update({newNode: edgeSplitDfdict[i]})
        nodeColumns.append(newNode)
    for i in parentChildDict.keys():
        print(i, parentChildDict[i])