import numpy as np
from sklearn.impute import SimpleImputer
X=[[np.nan,2,3],[4,np.nan,6],[10,np.nan,9]]
imputer = SimpleImputer(missing_values=np.nan,strategy='mean')
# allowed_strategies = ["mean", "median", "most_frequent", "constant"]
xx= imputer.fit_transform(X)
print(xx)


from sklearn.impute import KNNImputer
X = [[1, 2, np.nan], [3, 4, 3], [np.nan, 6, 5], [8, 8, 7]]
imputer = KNNImputer(n_neighbors=2)
xx=imputer.fit_transform(X)
print(X)
print(xx)
