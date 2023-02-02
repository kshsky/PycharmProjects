import pandas as pd
import numpy as np

def uConditionV(u,v):
    u = u.astype(float)
    sortedu = np.sort(u)
    vid,vct = np.unique(v,return_counts=True)

    #t:uConditionV
    tdict={}

    #split point list
    tlist = []
    for i in range(0,len(sortedu)-1,1):
        tlist.append(np.mean([sortedu[i],sortedu[i+1]]))
    for i in tlist:
        xi = pd.Series.copy(u)
        xi[xi<=i]=0
        xi[xi>i]=1
        ent = [np.sum([p*np.log2(1/p) for p in ct/sum(ct)]) for ct in [np.unique(xi,return_counts=True)[1]]][0]
        uConditionVj=  [np.sum([p*np.log2(1/p) for p in ct/sum(ct)])  for ct in [np.unique(xi[v==i],return_counts=True)[1] for i in vid]]
        uConditionV = np.sum(np.array(uConditionVj) * (vct/np.sum(vct)))
        tdict.update({i: uConditionV})

    return {'best split point':max(tdict,key=tdict.get),'maxuConditionV':max(tdict.values())}

def gainuv(u,v):
    u = u.astype(float)
    sortedu = np.sort(u)
    vid,vct = np.unique(v,return_counts=True)

    #t:gain
    tdict={}

    #split point list
    tlist = []
    for i in range(0,len(sortedu)-1,1):
        tlist.append(np.mean([sortedu[i],sortedu[i+1]]))
    for i in tlist:
        xi = pd.Series.copy(u)
        xi[xi<=i]=0
        xi[xi>i]=1
        entu = [np.sum([p*np.log2(1/p) for p in ct/sum(ct)]) for ct in [np.unique(xi,return_counts=True)[1]]][0]
        uConditionVj=  [np.sum([p*np.log2(1/p) for p in ct/sum(ct)])  for ct in [np.unique(xi[v==i],return_counts=True)[1] for i in vid]]
        uConditionV = np.sum(np.array(uConditionVj) * (vct/np.sum(vct)))
        gain = entu -uConditionV
        tdict.update({i: gain})

    print(tdict)
    return {'best split point':max(tdict,key=tdict.get),'maxEntropyGain':max(tdict.values())}


columns=['色泽','根蒂','敲声','纹理','脐部','触感','密度','含糖率','好瓜']
data=[['青绿','蜷缩','浊响','清晰','凹陷','硬滑',0.697,0.460,'是'],
    ['乌黑','蜷缩','沉闷','清晰','凹陷','硬滑',0.774,0.376,'是'],
    ['乌黑','蜷缩','浊响','清晰','凹陷','硬滑',0.634,0.264,'是'],
    ['青绿','蜷缩','沉闷','清晰','凹陷','硬滑',0.608,0.318,'是'],
    ['浅白','蜷缩','浊响','清晰','凹陷','硬滑',0.556,0.215,'是'],
    ['青绿','稍蜷','浊响','清晰','稍凹','软粘',0.403,0.237,'是'],
    ['乌黑','稍蜷','浊响','稍糊','稍凹','软粘',0.481,0.149,'是'],
    ['乌黑','稍蜷','浊响','清晰','稍凹','硬滑',0.437,0.211,'是'],
    ['乌黑','稍蜷','沉闷','稍糊','稍凹','硬滑',0.666,0.091,'否'],
    ['青绿','硬挺','清脆','清晰','平坦','软粘',0.243,0.267,'否'],
    ['浅白','硬挺','清脆','模糊','平坦','硬滑',0.245,0.057,'否'],
    ['浅白','蜷缩','浊响','模糊','平坦','软粘',0.343,0.099,'否'],
    ['青绿','稍蜷','浊响','稍糊','凹陷','硬滑',0.639,0.161,'否'],
    ['浅白','稍蜷','沉闷','稍糊','凹陷','硬滑',0.657,0.198,'否'],
    ['乌黑','稍蜷','浊响','清晰','稍凹','软粘',0.360,0.370,'否'],
    ['浅白','蜷缩','浊响','模糊','平坦','硬滑',0.593,0.042,'否'],
    ['青绿','蜷缩','沉闷','稍糊','稍凹','硬滑',0.719,0.103,'否']]
df= pd.DataFrame(data=data,columns = columns)
print(df)

# entropy(u)
#
# print(gainuv(df['密度'],df.iloc[:,-1]))
# print(gainuv(df['含糖率'],df.iloc[:,-1]))
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

#-----------------------

