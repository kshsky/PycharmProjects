
import numpy as np
from numpy import nan as NA
import pandas as pd
from pandas import Series,DataFrame
df = pd.DataFrame (np.random .randn(8,7))
df.iloc[0,:] = NA
df.iloc[1,:6] = NA
df.iloc[2,:5] = NA
df.iloc[3,:4] = NA
df.iloc[4,:3] = NA
df.iloc[5,:2] = NA
df.iloc[6,0] = NA


print(df)
#保留非空数>=2的行，删除非空数<2的行
thresh = 2
print(df.dropna(thresh=thresh))
# print(df.dropna(thresh=thresh,inplace=True))
print(df.loc[df.isnull().sum(axis=1)>df.shape[1]-thresh])
print(df)

thresh = 4
print('显示空值个数大于 {} 的行,这些行，予以删除'.format(df.shape[1]-thresh))
print(df.loc[df.isnull().sum(axis=1)>df.shape[1]-thresh])

print('=======================================')
print(df.loc[df.isnull().sum(axis=1)==df.shape[1]-thresh])
print('=======================================')
print('显示非空个数大于等于 {} 的行，这些行，予以保留'.format(thresh))

df.columns=['a','b','c','d','e','f','g']
print(df)
print('删除 e,f 两列中含有空值的行')
print(df.dropna(subset=['e','f']))
print(df)
#保留非空数>=4的行，删除非空数<4的行
print(df.dropna(thresh=4))
df.dropna(thresh=4,inplace=True)
print(df)