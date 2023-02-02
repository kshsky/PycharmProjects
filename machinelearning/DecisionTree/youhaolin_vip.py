import numpy as np
import pandas as pd
columns=['有固定资产(X1)','家庭类型(X2)','月收入(X3)','VIP用户']
data = np.array([
    ['是','C1',13.3,'否'],
    ['是','C2',10.0,'否'],
    ['否','C1',7.2,'否'],
    ['是','C2',12.7,'否'],
    ['否','C3',10.5,'是'],
    ['否','C2',6.3,'否'],
    ['是','C3',21.2,'否'],
    ['否','C1',8.6,'是'],
    ['是','C2',7.0,'否'],
    ['否','C1',9.4,'是']
])
df = pd.DataFrame(data=data,columns=columns)
print(df)

def entropy(u):

    u=u.astype(float)

    sortedu = np.sort(u)
    #t:entropy
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
        tdict.update({i:entu})

    return {'best split point':max(tdict,key=tdict.get),'maxEntropy':max(tdict.values())}
def uConditionV(u,v):
    u = u.astype(float)
    sortedu = np.sort(u)
    vid,vct = np.unique(v,return_counts=True)

    #t:uConditionV
    tdict={}

    #split point list
    tlist = []
    for i in range(0,len(sortedu)-1):
        tlist.append(np.mean([sortedu[i],sortedu[i+1]]))
    for i in tlist:
        xi = u.apply(lambda x :0 if x<=i else 1)
        ent = [np.sum([p*np.log2(1/p) for p in ct/sum(ct)]) for ct in [np.unique(xi,return_counts=True)[1]]][0]
        uConditionVj=  [np.sum([p*np.log2(1/p) for p in ct/sum(ct)])  for ct in [np.unique(xi[v==i],return_counts=True)[1] for i in vid]]
        uConditionV = np.sum(np.array(uConditionVj) * (vct/np.sum(vct)))
        tdict.update({i: uConditionV})

    return {'best split point':max(tdict,key=tdict.get),'maxuConditionV':max(tdict.values())}
print(entropy(df['月收入(X3)']))

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
        ent = [np.sum([p*np.log2(1/p) for p in ct/sum(ct)]) for ct in [np.unique(xi,return_counts=True)[1]]][0]
        uConditionVj=  [np.sum([p*np.log2(1/p) for p in ct/sum(ct)])  for ct in [np.unique(xi[v==i],return_counts=True)[1] for i in vid]]
        uConditionV = np.sum(np.array(uConditionVj) * (vct/np.sum(vct)))
        gain = ent -uConditionV
        tdict.update({i: gain})

    print(tdict)
    return {'best split point':max(tdict,key=tdict.get),'maxEntropyGain':max(tdict.values())}

def gini(u):
    id,ct = np.unique(u,return_counts = True)
    p = [i/sum(ct) for i in ct]
    return 1-np.sum([i**2 for i in p])

print(gainuv(df['月收入(X3)'],df['VIP用户']))
print(uConditionV(df['月收入(X3)'],df['VIP用户']))

print(gini(df['有固定资产(X1)']))