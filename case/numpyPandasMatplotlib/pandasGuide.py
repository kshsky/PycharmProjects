import pandas as pd
import numpy as np
dates = pd.date_range('1/1/2000', periods=8)

df = pd.DataFrame(np.random.randn(8, 4),
                  index=dates, columns=['A', 'B', 'C', 'D'])

print(df)
df['index']=list(range(len(df.index)))
s = df['A']
print(s)
print(s[3])

df[['B', 'A']] = df[['A', 'B']]
print(df)
print(df.columns)

df.columns=['index','C','E','R','V']
print(df)

print(df.columns)
print(df[2:])
print(df[2:4])
print(df[0:3])
print(df[1:6])
print(df.iloc[2:])
print(df.iloc[2:4])

print(df)


df.pop('C')
print(df)

df.drop('index',axis=1,inplace=True)
print(df)

data=pd.read_csv('dataFile/drinks.csv')
print(data)
print(data[['continent','beer_servings']].groupby('continent').mean())
print(data.groupby('continent').mean())
print(data.groupby('continent').median())
#agg聚合函数
print(data.groupby('continent').agg({"beer_servings":np.mean,'wine_servings':np.sum}))
print(data.groupby('continent').agg([np.mean,np.sum]))
# agg自定义函数
data.groupby('continent').agg(lambda x:x.max()-x.min())  # 计算每个大陆每种酒类销售量的极差