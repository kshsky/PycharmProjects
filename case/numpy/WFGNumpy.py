import numpy as np
print(np.__version__)
names = np.array(['Atom', 'Lucy', 'Kid', 'Atom', 'Kid', 'Atom'])
print(names)
print(np.unique(names))

#整数去重
ints = np.array([1,2,3,4,2,4,3,5])
print(ints)
print(np.unique(ints))


#布尔值去重
bools = np.array([False, True, True, False])
print(bools)
print(np.unique(bools))

#布尔值的any()和all()函数
print(bools.any()) #有一个True就返回True
print(bools.all()) #所有都为True才返回True

val_1 = np.array([4,5,6])
val_2 = np.array([2,3,4])
print('val_1:{}'.format(val_1))
print('val_2:{}'.format(val_2))

# 验证 val_1 中的元素是否在给出的序列中
print(np.in1d(val_1, [0, 5, 7]))

#求交集
print(np.intersect1d(val_1, val_2))

#求并集
print(np.union1d(val_1,val_2))

# 求差集
print(np.setdiff1d(val_1, val_2))
print(np.setdiff1d(val_2, val_1))

print('-------------------')
a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]

print(np.array(a)@np.array(b))
print(np.dot(a, b))