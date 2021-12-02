import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([5.56, 5.70, 5.91, 6.40, 6.80, 7.05, 8.90, 8.70, 9.00, 9.05])
split_point = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]

print('x',x)
print('y',y)
print('split_point',split_point)

k = 1

inerval_split_list=[]
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
    inerval_split_list.append((float('-inf'), best_split,left_mean))
    inerval_split_list.append((best_split, float('inf'),right_mean))
    print('mse:{}'.format(np.sum(y ** 2)))
    if (np.sum(y ** 2) < 0.2):
        flag = False
        break
    k = k + 1

# 区间间隔分类
print(inerval_split_list)
'''
(-inf, 6.5, 6.236666666666667)
(6.5, inf, 8.912500000000001)
(-inf, 3.5, -0.513333333333334)
(3.5, inf, 0.219999999999999)
(-inf, 6.5, 0.14666666666666692)
(6.5, inf, -0.2200000000000003)
(-inf, 4.5, -0.16083333333333338)
(4.5, inf, 0.10722222222222222)
(-inf, 6.5, 0.07148148148148149)
(6.5, inf, -0.10722222222222222)
(-inf, 2.5, -0.15064814814814842)
(2.5, inf, 0.03766203703703709)
'''
interval_point_list = []
# 获取所有区间点：
for i in inerval_split_list:
    interval_point_list.append(i[0])
    interval_point_list.append(i[1])
    print(i)
print(interval_point_list)
interval = sorted(list(set(interval_point_list)))
print(interval)
print(type(interval))
print(len(interval))

# [-inf  2.5  3.5  4.5  6.5  inf]
# 组合区间
final_interval = [(interval[i], interval[i + 1]) for i in range(len(interval) - 1)]
print(final_interval)
# [(-inf, 2.5), (2.5, 3.5), (3.5, 4.5), (4.5, 6.5), (6.5, inf)]
# 区间值加
interval_value_list = []

G={}
for k in final_interval:
    value= 0
    for i in inerval_split_list:
        #区间值截取
        if i[0]<=k[0] and i[1]>=k[1]:
            value =value + i[2]
            G.update({k:value})

print(G)
# {(-inf, 2.5): 5.63, (2.5, 3.5): 5.818310185185186, (3.5, 4.5): 6.551643518518518, (4.5, 6.5): 6.819699074074074, (6.5, inf): 8.950162037037037}