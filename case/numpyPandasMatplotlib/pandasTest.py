import pandas as pd
import numpy as np

data = np.array([[1,2,3,4,5],[6,7,8,9,10]]).T
index = ['A','B','C','D','E']
columns = ['数值1','数值2']   # 需要传入所有的列名

df = pd.DataFrame(data,index,columns)

print(df.index)
print(df)

# df.colunns = ['cccc','bb']

print(df.columns)
df.columns=['C','d']
print(df)


