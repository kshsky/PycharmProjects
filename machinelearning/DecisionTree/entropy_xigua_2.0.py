import pandas as pd
import numpy as np


def entropy(u):

    return [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(u, return_counts=True)[1]]][0]

#条件熵
def uConditionV(u,v):

    # Vj
    vid, vct = np.unique(v, return_counts=True)

    # uConditionVj
    uConditionVj = [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(u[v == i], return_counts=True)[1] for i in vid]]

    #uConditionV
    uConditionV= np.sum(np.array(uConditionVj) * (vct / np.sum(vct)))

    return uConditionV

#信息增益
def gainuv(u,v):
    #entu
    entu = [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(u, return_counts=True)[1]]][0]
    entv = [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(v, return_counts=True)[1]]][0]
    # Vj
    vid, vct = np.unique(v, return_counts=True)

    # uConditionVj
    uConditionVj = [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(u[v == i], return_counts=True)[1] for i in vid]]

    #uConditionV
    uConditionV= np.sum(np.array(uConditionVj) * (vct / np.sum(vct)))

    return entu - uConditionV

#增益率
def gainRatio(u,v):
    #entu
    entu = [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(u, return_counts=True)[1]]][0]
    entv = [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(v, return_counts=True)[1]]][0]
    # Vj
    vid, vct = np.unique(v, return_counts=True)

    # uConditionVj
    uConditionVj = [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(u[v == i], return_counts=True)[1] for i in vid]]

    #uConditionV
    uConditionV= np.sum(np.array(uConditionVj) * (vct / np.sum(vct)))

    return (entu-uConditionV)/ entv

def gini(u,v):
    pass

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

u = df.iloc[:,0]
id,ct = np.unique(u,return_counts=True)
print(u.values)
print(np.unique(u,return_counts=True))
print(id)
print(ct)
print(type(ct))
p = [i/sum(ct) for i in ct]
print(p)
print(ct[0]/sum(ct),ct[1]/sum(ct),ct[2]/sum(ct))


def entU(u):

    return [np.sum([p * np.log2(1 / p) for p in ct / np.sum(ct)]) for ct in [np.unique(u, return_counts=True)[1]]][0]

entropyU = np.sum([i*np.log2(1/i) for i in p])
print(entropyU)
entropyCol = [np.sum([p*np.log2(1/p) for p in ct/sum(ct)]) for ct in [np.unique(u,return_counts=True)[1]]][0]
print(entropyCol)
print(entU(u))

print('各列的熵：：：')
for i in range(df.shape[1]-1):
    u = df.iloc[:,i]
    print(df.columns[i],'->',[np.sum([p*np.log2(1/p) for p in ct/sum(ct)]) for ct in [np.unique(u,return_counts=True)[1]]][0])
print('---------条件熵----------')
v=df.iloc[:,-1]
print(v.values)
vid,vct = np.unique(v,return_counts=True)
print(np.unique(v,return_counts=True))
u = df.iloc[:,0]
uUnderV = [np.unique(u[v==i],return_counts=True) for i in vid]
print(uUnderV)

uctUnderVj = [np.unique(u[v==i],return_counts=True)[1] for i in vid]
print(uctUnderVj)
puUnderVj =[i/sum(i) for i in uctUnderVj]
print(puUnderVj)

entuUnderVj = [np.sum(p*np.log2(1/p)) for p in puUnderVj]
print(entuUnderVj)
print([i/sum(vct) for i in vct])
UUnderV=np.vdot(np.array([i/sum(vct) for i in vct]),entuUnderVj)
print(UUnderV)
print(np.sum(np.array([i/sum(vct) for i in vct])*entuUnderVj))
print(uConditionV(u,v))

print('---------各列条件熵-----')
for i in columns[:-1]:
    print(i,'->',uConditionV(df[i],df.iloc[:,-1]))

print('----------各列信息增益-----------')
for i in columns[:-1]:
    print(i,'->',gainuv(df[i],df.iloc[:,-1]))


print('----------各列信息增益率-----------')
for i in columns[:-1]:
    print(i,'->',gainRatio(df[i],df.iloc[:,-1]))


 # --------------------------------
def maxFeatureEntGain(df):
    columns = df.columns
    featureEntGainDict={}
    for i in columns[:-1]:
        featureEntGainValue = featureEntGain(df[i],df.iloc[:,-1])
        featureEntGainDict[i]=featureEntGainValue
    return max(featureEntGainDict,key = featureEntGainDict.get)

def maxFeatureEntGainRatio(df):
    columns = df.columns
    flag = df.iloc[:,-1]
    featureEntGainDict={}
    for i in columns[:-1]:
        featureEntGain = featureEntGain(i,flag)
        featureEntGainDict[i]=featureEntGain
    return max(featureEntGainDict,key = featureEntGainDict.get)
para=['gain','ratio','gini']

def maxFeature(df,para):
    columns=df.columns
    label = df.iloc[:,-1]
    featureDict={}
    for i in columns[:-1]:
        featureValue=0
        if para=='gain':
            featureValue=gainuv(df[i],label)
        elif para=='ratio':
            featureValue = gainRatio(df[i], label)
        elif para=='gini':
            featureValue = gini(df[i], label)
        else:
            print('error para')
        featureDict[i]=featureValue
    return max(featureDict,key=featureDict.get)
'''
{'纹理': {'模糊': '否',
  '清晰': {'根蒂': {'硬挺': '否',
    '稍蜷': {'色泽': {'乌黑': {'触感': {'硬滑': '是', '软粘': '否'}}, '青绿': '是'}},
    '蜷缩': '是'}},
  '稍糊': {'触感': {'硬滑': '否', '软粘': '是'}}}}
'''
#建立递归嵌套字典,最后一列是标签列
def createTreeDict(df,para='gain'):
    root = maxFeature(df,para)
    treeDict={root:{}}
    vid,vct=np.unique(df[root],return_counts=True)
    for i in vid:
        newdf = df[df[root]==i]
        if len(set(newdf.iloc[:,-1]))==1:
            leaf = list(set(newdf.iloc[:,-1]))[0]
            treeDict[root][i]=leaf
        else:
            treeDict[root][i]=createTreeDict(newdf)
    return treeDict


# tree = createTreeDict(df,'entropy')

# print(tree)

print('===============')
def createFlatDict(treeDict):
    k=treeDict.get('k',0)
    flatDict={}
    for k0,v0 in treeDict.items():
        if type(v0) is dict:
            for k1,v1 in v0.items():
                if type(v1) is not dict:
                    flatDict[str(k)+'-'+k0+'-'+k1]=v1
                else:
                    #the key of v1 is feature
                    flatDict[str(k)+'-'+k0+'-'+k1]=list(v1.keys())[0]
                    v1['k']=k+1
                    # recursion
                    flatDict.update(createFlatDict(v1))
    return flatDict

def graphvizFlatDict(flatDict,df):
    from graphviz import Digraph
    import datetime
    dot = Digraph(directory='datafile',format='pdf',
                  node_attr={'style':'filled',"fontname":'Microsoft YaHei'},
                  edge_attr={"fontname":'Microsoft YaHei'})
    #leaf node all in label
    label=np.unique(df.iloc[:,-1])
    for k,v in flatDict.items():
        print(k,v)
        item = k.split('-')
        level=int(item[0])
        parent=item[1]
        edge=item[2]

        parentNode=item[0]+item[1]
        dot.node(name=parentNode,label=parent,shape='box')

        childNode=''
        if v in label:
            #leaf
            childNode = item[0]+item[1]+v
        else:
            childNode=str(level+1)+v
        dot.node(name=childNode,label=v)
        dot.edge(parentNode,childNode,edge)
    name = str(datetime.datetime.now().date())
    #设置保存名称
    dot.render(name, view=True)


treedict = createTreeDict(df)
flatdict = createFlatDict(treedict)
graphvizFlatDict(flatdict,df)