import pandas as pd
import numpy as np


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

#增益率
def gainRatio(u, v):
    return gainuv(u,v) / entU((v))
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

flagColumn='好瓜'

columnEntropy={}
for i in columns:
    print(np.unique(df[i],return_counts=True))
    columnEntropy.update({i:entU(df[i])})


print('============\n各列的熵：')
for i,j in columnEntropy.items():
    print(i,j)
##########################################
root1=entU(df.iloc[:,-1])
root1Name=columns[-1]
print('root1 - 根节点的熵(根据\"{}\"进行划分)：{}'.format(root1Name,root1))
##########################################    1
columnConditionEntropy={}
for i in columns:
    columnConditionEntropy.update({i:gainuv(df[flagColumn],df[i])})
print('============\n各列的条件熵：')
for i in columns[:-1]:
    print(i,columnConditionEntropy[i])

print('============\n各列的信息增益：')
gainList=[]
for i in columns[:-1]:
    print(i,root1 - columnConditionEntropy[i])
    gainList.append(root1 - columnConditionEntropy[i])
print('最大增益是：',columns[np.argmax(gainList)],max(gainList))
root2Name=columns[np.argmax(gainList)]
root2 = max(gainList)
print('root2 - 根节点的熵(根据\"{}\"进行划分)：{}'.format(root2Name,root2))
##########################################     2

name,namect = np.unique(df[root2Name],return_counts=True)
print(name)

columnConditionEntropy={}
columnGains={}
for ii in name:
    splitdf = df[df[root2Name]==ii]
    tempConditions={}
    tempGains={}
    for i in columns:
        if i not in[root1Name,root2Name]:
            concatpd = pd.concat([splitdf[root1Name],splitdf[i]],axis=1)
            tempConditions.update({i:gainuv(concatpd[root1Name],concatpd[i])})
            tempGains.update({i:gainuv(concatpd[root1Name],concatpd[i])})
    columnConditionEntropy.update({ii:tempConditions})
    columnGains.update({ii:tempGains})
print('============\n各列的条件熵：')
for ii in columnConditionEntropy.keys():
    print(ii,columnConditionEntropy[ii])
print('============\n各列的信息增益：')
for ii in columnGains.keys():
    print(ii,columnGains[ii])

print('============\n各列的信息增益率：')
for i in columns:
    print(i,gainRatio(df[flagColumn],df[i]))


print(entU(df.index))
