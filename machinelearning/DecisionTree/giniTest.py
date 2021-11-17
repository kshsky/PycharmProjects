import numpy as np
import pandas as pd

columns = ['有固定资产(X1)', '家庭类型(X2)', '月收入(X3)', 'VIP用户']
data = np.array([
    ['是', 'C1', 13.3, '否'],
    ['是', 'C2', 10.0, '否'],
    ['否', 'C1', 7.2, '否'],
    ['是', 'C2', 12.7, '否'],
    ['否', 'C3', 10.5, '是'],
    ['否', 'C2', 6.3, '否'],
    ['是', 'C3', 21.2, '否'],
    ['否', 'C1', 8.6, '是'],
    ['是', 'C2', 7.0, '否'],
    ['否', 'C1', 9.4, '是']
])
df = pd.DataFrame(data=data, columns=columns)


# 离散型
def giniC(x, y):
    x_id, x_ct = np.unique(x, return_counts=True)
    p_x = [ct / sum(ct) for ct in [np.unique(x, return_counts=True)[1]]]
    gini = [1 - np.sum(p ** 2) for p in
            [ct / sum(ct) for ct in [np.unique(y[x == i], return_counts=True)[1] for i in x_id]]]


    return np.sum(np.array(p_x) * np.array(gini))

x = df['有固定资产(X1)']
y=df['VIP用户']
print(round(giniC(x, y), 4))
# 0.24
x = df['家庭类型(X2)']
print(round(giniC(x, y), 4))
# 0.3


# 连续型分类变量
x = df['月收入(X3)'].astype(float)
y = df.VIP用户


def giniS(y, x):
    # 将离散数据转成float
    x.astype(float)
    # 对离散数据排序
    sorted_x = np.sort(x)
    split_point_list = []
    split_point_gini = []
    # 求分界点
    for i in range(0, len(sorted_x) - 1, 1):
        split_point_list.append(np.mean([sorted_x[i], sorted_x[i + 1]]))

    # 依次计算每个分界点分割后的gini系数
    for i in split_point_list:
        # 分界后，就是二分类了
        xi = pd.Series.copy(x)
        xi[xi <= i] = 0
        xi[xi > i] = 1

        # 根据新分界点，计算权重（频数、概率）
        w_i = [[p for p in ct / np.sum(ct)] for ct in [np.unique(xi, return_counts=True)[1]]]

        # 分类
        x_id, x_ct = np.unique(xi, return_counts=True)

        # 每个分界点分类的gini
        gini_x_id = [np.sum([(p - p ** 2) for p in ct / np.sum(ct)]) for ct in
                     [np.unique(y[xi == i], return_counts=True)[1] for i in x_id]]

        # 计算每个分界点的gini
        split_point_gini.append(round(np.sum(w_i * np.array(gini_x_id)), 4))

    # 封装成字典
    split_point_gini_dict = dict(zip(split_point_list, split_point_gini))


    return split_point_gini_dict

giniS(y, x)

