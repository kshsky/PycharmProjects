from pandas.api.types import CategoricalDtype
import pandas as pd
cats = ['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']
df = pd.DataFrame({'Grades':cats})
cat_type = CategoricalDtype(categories=cats, ordered=True)
df['Grades'] = df['Grades'].astype(cat_type)
print (df)
print('--------------')

from pandas.api.types import CategoricalDtype

cats = ['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']
cat_type = CategoricalDtype(categories=cats, ordered=True)
df['Grades'] = df['Grades'].astype(cat_type)
print (df)
print('--------------')

df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                      index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)

df = df['Grades'].astype('category',categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],ordered=True)


print(df)