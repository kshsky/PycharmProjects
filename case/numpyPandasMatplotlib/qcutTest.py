import pandas as pd
import numpy as np

array=np.array([5,10,25,45,85,100])
labels=['a','b','c','d']
box,bins = pd.cut(array,4,labels=['a','b','c','d'],retbins=True)
qbox,qbins = pd.qcut(array,4,labels=['a','b','c','d'],retbins=True)

#把分箱界限拼接成区间，并存入区间字典
box_limit=[str(i)+'-'+str(bins[bins.tolist().index(i)+1]) if i !=max(bins) else np.nan for i in bins][0:len(bins)-1]
qbox_limit=[str(i)+'-'+str(qbins[qbins.tolist().index(i)+1]) if i !=max(qbins) else np.nan for i in qbins][0:len(qbins)-1]
box_limit_dict = dict(zip(labels,box_limit))
qbox_limit_dict = dict(zip(labels,qbox_limit))

df = pd.DataFrame({'data':array,'box':box,'qbox':qbox})
df['box_limit']=[box_limit_dict[i] for i in df.box]
df['qbox_limit']=[qbox_limit_dict[i] for i in df.qbox]

df['box_limit_floor']=bins[[np.where(x<=bins)[0][0]-1 for x in df.data]]
df['box_limit_ceiling']=bins[[np.where(x<=bins)[0][0] for x in df.data]]
df['qbox_limit_floor']=qbins[[np.where(x<=qbins)[0][0]-1 if np.where(x<=qbins)[0][0]>0 else 0 for x in df.data]]
df['qbox_limit_ceiling']=qbins[[np.where(x<=qbins)[0][0] if np.where(x<=qbins)[0][0]>0 else np.where(x<=qbins)[0][0]+1 for x in df.data]]
df['box_limit']='['+df.box_limit_floor.map(str)+','+df.box_limit_ceiling.map(str)+']'
df['qbox_limit']='['+df.qbox_limit_floor.map(str)+'-'+df.qbox_limit_ceiling.map(str)+']'
print(df[['data','box','box_limit','qbox','qbox_limit']])

box1 = pd.cut(array,bins=[0,10,20,50,90],labels=['a','b','c','d'])
for i in box1:
    print(i)
print('-------------')
box2 = pd.cut(array,bins=[0,10,20,50,100],labels=['a','b','c','d'])
for i in box2:
    print(i)
