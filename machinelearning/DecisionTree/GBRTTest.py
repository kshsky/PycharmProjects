import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([5.56, 5.70, 5.91, 6.40, 6.80, 7.05, 8.90, 8.70, 9.00, 9.05])
split_point = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]

print('x',x)
print('y',y)
print('split_point',split_point)

k = 1
G={}
flag = True
while flag:
    G_temp={}
    print('-----------{}-----------'.format(k))
    for s in split_point:
        left = y[np.argwhere(x < s)]
        right = y[np.argwhere(x > s)]
        mse = np.sum((np.array(left) - np.mean(left)) ** 2) + np.sum((np.array(right) - np.mean(right)) ** 2)
        G_temp.update({s:mse})

    for kk in G_temp.keys():
        print(kk,G_temp.get(kk))
    best_split = min(G_temp,key=G_temp.get)

    print('最佳分割点：{}'.format(best_split))

    left = y[np.argwhere(x < best_split)]
    right = y[np.argwhere(x > best_split)]
    left_mean = np.mean(left)
    right_mean = np.mean(right)

    # 更新残差表
    print('--- 更新残差表 ---')
    y = np.vstack([left - left_mean, right - right_mean]).reshape(-1)
    print(y)
    # 更新树：
    G.update({(float('-inf'), best_split):left_mean})
    G.update({(best_split, float('inf')):right_mean})

    print(G)
    print('mse:{}'.format(np.sum(y ** 2)))
    if (np.sum(y ** 2) < 0.2):
        flag = False
        break
    k = k + 1

# 区间间隔分类
split_list = list(G.keys())
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
