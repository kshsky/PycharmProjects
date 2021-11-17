from sklearn.datasets import load_boston

import pandas as pd

oridata = load_boston()
data = oridata.data
columns =oridata.feature_names
print(oridata)

df = pd.DataFrame(data = data,columns=columns)
'''
CRIM：城镇人均犯罪率。
ZN：住宅用地超过 25000 sq.ft. 的比例。
INDUS：城镇非零售商用土地的比例。
CHAS：查理斯河空变量（如果边界是河流，则为1；否则为0）。
NOX：一氧化氮浓度。
RM：住宅平均房间数。
AGE：1940 年之前建成的自用房屋比例。
DIS：到波士顿五个中心区域的加权距离。
RAD：辐射性公路的接近指数。
TAX：每 10000 美元的全值财产税率。
PTRATIO：城镇师生比例。
B：1000（Bk-0.63）^ 2，其中 Bk 指代城镇中黑人的比例。
LSTAT：人口中地位低下者的比例。
MEDV：自住房的平均房价，以千美元计。
预测平均值的基准性能的均方根误差（RMSE）是约 9.21 千美元。
'''

print(df)