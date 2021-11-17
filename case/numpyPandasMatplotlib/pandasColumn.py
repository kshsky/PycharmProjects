import pandas as pd
import numpy as np

data = np.array([[1,2,3,4,5],[6,7,8,9,10]]).T
index = ['A','B','C','D','E']
columns = ['a','b']

df = pd.DataFrame(data,index,columns)

print(df)
'''
   a   b
A  1   6
B  2   7
C  3   8
D  4   9
E  5  10
'''
print(df[df.a>3])
'''
   a   b
D  4   9
E  5  10
'''
print(df['a'][df.a>3])
'''
D    4
E    5
'''
print(df['a'][df.b>7])
'''
C    3
D    4
E    5
'''
print(df[(df.a>2)&(df.a<4)])
'''
   a  b
C  3  8
'''