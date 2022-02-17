import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#
from machinelearning.tools.mlTools import overview

data = pd.read_table('dataFile/student_grade_empty.txt')
# data = pd.read_csv('datafile/titanic.csv')
print(data)
print(data.info())
#
print(data.describe(include='all'))

print('\n缺失行\n')
print(data.loc[data.isnull().sum(axis=1) > 0])
print('\n缺失列\n')
print(data.loc[:,data.isnull().sum(axis=0) > 0])
print('\n缺失区域【缺失行+缺失列】\n')
emptyArea = data.loc[data.isnull().sum(axis=1) > 0, data.isnull().sum(axis=0) > 0]
print(emptyArea)
#所在列缺失的行号
for i in data.columns:
    print(i, ' : ', list(np.where(pd.isna(data[i]))[0]))

print(data.isnull().sum())

print(data.duplicated())
print(data[data.duplicated()])
# data.drop_duplicates(inplace=True)
print('总记录数：',data.shape[0])

# overview(data)
# print(data.dropna(axis=0,how='all'))
print(data.shape[0])
thresh = 4
print('删除空值个数大于 {} 的行'.format(data.shape[1]-thresh))
print('显示空值个数大于 {} 的行,这些行，予以删除'.format(data.shape[1]-thresh))
print(data.loc[data.isnull().sum(axis=1)>data.shape[1]-thresh])

print('=======================================')
print(data.loc[data.isnull().sum(axis=1)==data.shape[1]-thresh])
print('=======================================')
print('显示非空个数大于等于 {} 的行，这些行，予以保留'.format(thresh))
print(data.dropna(thresh=thresh))
# data.dropna(thresh=4,inplace=True)
print(data.shape[0])

print(data.dropna(subset=['姓名']))
print(data['姓名'].value_counts())
print(np.unique(data['语文'],return_counts=True))
overview(data)
#缺失值填充
print('语文使用众数进行填充')
chineseEmpty = data.loc[data['语文'].isnull()]
indexList= chineseEmpty.index
print(indexList)
print(data.loc[data['语文'].isnull()])
print(data['语文'].mode()[0])
data.语文.fillna(data.语文.mode()[0],inplace=True)
print(data.loc[indexList,:])
print('数学使用均值进行填充')
mathEmpty = data.loc[data['数学'].isnull()]
indexList= mathEmpty.index
print(indexList)
print(data.loc[data['数学'].isnull()])
print(data['数学'].mean())
data.数学.fillna(data.数学.mean(),inplace=True)
print(data.loc[indexList,:])

print('英语使用前项进行填充')
englishEmpty = data.loc[data['英语'].isnull()]
indexList= englishEmpty.index
findexList = englishEmpty.index -1
print(indexList)
print(data.loc[data['英语'].isnull()])
# print(data['英语'].mean())
data.英语.fillna(method='ffill',inplace=True)
print(data.loc[findexList,:])
print(data.loc[indexList,:])

print('姓名使用后项进行填充')
data.loc[35,'姓名']=None
nameEmpty = data.loc[data['姓名'].isnull()]
indexList= nameEmpty.index
bindexList= nameEmpty.index +1
print(indexList)
print(bindexList)
print(data.loc[data['姓名'].isnull()])
# print(data['数学'].mean())
data.姓名.fillna(method='bfill',inplace=True)
print(data.loc[indexList,:])
print(data.loc[bindexList,:])

print(data.loc[data['总分'].isnull()])
print('重新计算总分')
data.总分= data.iloc[:,1:4].sum(axis=1)
print(data)
print(data.iloc[:,1:4].sum(axis=1))
print(data.iloc[-5:,:])

print(emptyArea)
emptyAreaIndexList = emptyArea.index
print(emptyAreaIndexList)
print(data.iloc[emptyAreaIndexList,:])
print(data.总分.median())

print('查找总分异常值')
print(data.总分.values)
plt.scatter(list(data.总分.values),np.ones(data.shape[0]))
# plt.show()
q1 = data.总分.quantile(q=0.25)
q3 = data.总分.quantile(q=0.75)
iqr = q3 -q1
k=1.5
minLimit = q1- k * iqr
maxLimit = q3+ k * iqr
print(data[(data.总分>maxLimit )|( data.总分 < minLimit)])
