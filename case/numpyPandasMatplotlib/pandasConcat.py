import pandas as pd
import numpy as np

#join='outer' 默认
#ignore_index=False 默认不重排索引
#axis=1时，有索引，按照索引concat，没有索引直接拼接

# 定义df1
df1 = pd.DataFrame({'cn':['春','夏','夏','秋','秋'],
                  'num1':[1,2,3,6,5],
                    'en':['spring-1','summer-2','summer-3','autumn-6','autumn-5']})
# 定义df2
df2 = pd.DataFrame({'cn':['夏','秋','冬'], 'en':['summer-5','autumn-3','winter-2'],
                  'num2':[5,3,2],
                 'color':['green','gold','white']})

df22 = pd.DataFrame({'cn':['夏','秋','冬'],
                     'en':['summer-5','autumn-3','winter-2'],
                   'num2':[5,3,2],
                  'color':['green','gold','white']})

df3 = pd.concat([df1,df2],axis=0)
df4 = pd.concat([df1,df2],axis=1)
df5 = pd.concat([df1,df2,df22],axis=1)

df1.set_index(['num1'],inplace=True)
df2.set_index(['num2'],inplace=True)

df6 = pd.concat([df1,df2],axis=0)
df7 = pd.concat([df1,df2],axis=0,ignore_index=True)
df8 = pd.concat([df1,df2],axis=1)

print(df1)
print(df2)
print(df3)
print(df4)
print(df5)
print(df6)
print(df7)
print(df8)


