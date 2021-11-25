import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([5.56, 5.70, 5.91, 6.40, 6.80, 7.05, 8.90, 8.70, 9.00, 9.05])
split_point = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]

mse_list_tmp = []
mse_list = []
best_split_list = []
list_dict = []
i = 1
while True:
    print('-----------{}-----------'.format(i))
    mse_list_tmp.clear()
    for s in split_point:
        left = y[np.argwhere(x < s)]
        right = y[np.argwhere(x > s)]
        mse = np.sum((np.array(left) - np.mean(left)) ** 2) + np.sum((np.array(right) - np.mean(right)) ** 2)
        mse_list_tmp.append(mse)
    print(mse_list_tmp)
    min_mse = min(mse_list_tmp)
    mse_list.append(min_mse)
    best_split = split_point[np.argmin(mse_list_tmp)]
    best_split_list.append(best_split)
    print('最佳分割点：{}'.format(best_split_list))

    left_side = y[np.argwhere(x < best_split)]
    right_side = y[np.argwhere(x > best_split)]
    left_mean = round(np.mean(left_side), 2)
    right_mean = round(np.mean(right_side), 2)
    print(left_mean, right_mean)

    # 更新残差表
    y = np.vstack([left_side - left_mean, right_side - right_mean]).reshape(-1)

    # 更新树：
    key_list = [(float('-inf'), best_split), (best_split, float('inf'))]
    value_list = [left_mean, right_mean]

    tree_dict = dict(zip(key_list, value_list))

    print(tree_dict)
    list_dict.append(tree_dict)
    print('mse:{}'.format(np.sum(y ** 2)))
    if (np.sum(y ** 2) < 0.2):
        break
    i = i + 1

# 区间间隔分类
split_list = list(set(best_split_list))
split_list = [float('-inf')] + split_list + [float('inf')]
print(split_list)
final_interval = [(split_list[i], split_list[i + 1]) for i in range(len(split_list) - 1)]
final_interval

# 区间值加总
interval_value_list = []

for k in final_interval:
    k_value = 0
    for i in list_dict:
        for j in i:
            # print(k[0],j[0],k[1],j[1],i[j])
            if k[0] >= j[0] and k[1] <= j[1]:
                k_value += i[j]
    interval_value_list.append(round(k_value, 4))

interval_value_list
