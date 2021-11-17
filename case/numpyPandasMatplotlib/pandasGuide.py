import pandas as pd
import numpy as np
dates = pd.date_range('1/1/2000', periods=8)

df = pd.DataFrame(np.random.randn(8, 4),
                  index=dates, columns=['A', 'B', 'C', 'D'])

print(df)

s = df['A']
print(s)
print(s[3])

df[['B', 'A']] = df[['A', 'B']]
print(df)
print(df.columns)

df.columns=['C','E','R','V']
print(df)

print(df.columns)
