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
    label = np.unique(df.iloc[:, -1])
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

treedict = createTreeDict(df)
print(treedict)

flatdict = createFlatDict(treedict)
print(flatdict)

# graphvizFlatDict(flatdict)

columns = ['age','prescript','astigmatic','tearRate','labels']
data = [['young','myope',' no', 'reduced','no lenses'],
     ['young','myope',' no', 'normal','soft'],
     ['young','myope','yes', 'reduced','no lenses'],
     ['young','myope','yes', 'normal','hard'],
     ['young','hyper',' no', 'reduced','no lenses'],
     ['young','hyper',' no', 'normal','soft'],
     ['young','hyper','yes', 'reduced','no lenses'],
     ['young','hyper','yes', 'normal','hard'],
       ['pre','myope',' no', 'reduced','no lenses'],
       ['pre','myope',' no', 'normal','soft'],
       ['pre','myope','yes', 'reduced','no lenses'],
       ['pre','myope','yes', 'normal','hard'],
       ['pre','hyper',' no', 'reduced','no lenses'],
       ['pre','hyper',' no', 'normal','soft'],
       ['pre','hyper','yes', 'reduced','no lenses'],
       ['pre','hyper','yes', 'normal','no lenses'],
['presbyopic','myope',' no', 'reduced','no lenses'],
['presbyopic','myope',' no', 'normal','no lenses'],
['presbyopic','myope','yes', 'reduced','no lenses'],
['presbyopic','myope','yes', 'normal','hard'],
['presbyopic','hyper',' no', 'reduced','no lenses'],
['presbyopic','hyper',' no', 'normal','soft'],
['presbyopic','hyper','yes', 'reduced','no lenses'],
['presbyopic','hyper','yes', 'normal','no lenses']]

df = pd.DataFrame(data = data,columns = columns)
v=df.iloc[:,-1]
vid = np.unique(v)
print(vid)
print(type(vid))