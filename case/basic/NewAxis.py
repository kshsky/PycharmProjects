import numpy as np
print(np.newaxis is None)
print(np.newaxis)
print('===========')
print('\n\n----------- x是： [1 2 3] y是： [3 4]--------------------')
x = np.array([1, 2, 3])
print('x是：', x)
y = np.arange(3, 5)
print('y是：', y)
print('x.shape是：{} y.shape是：{}'.format(x.shape, y.shape))
print('维度扩充之后：')
print('x[:, None].shape - {}'.format(x[:, None].shape))
print('x[None, :].shape - {}'.format(x[None, :].shape))
print('y[:, None].shape - {}'.format(y[:, None].shape))
print('y[None, :].shape - {}'.format(y[None, :].shape))

# x是： [1 2 3] y是： [3 4]
z1 = x[:, None] * y[None, :]
z2 = y[None, :] * x[:, None]

z3 = x[None, :] * y[:, None]
z4 = y[:, None] * x[None, :]

print('x[:, None] * y[None, :] \n{}'.format(z1))
print('y[None, :] * x[:, None] \n{}'.format(z2))
print('x[None, :] * y[:, None] \n{}'.format(z3))
print('y[:, None] * x[None, :] \n{}'.format(z4))

z1 = x[:, None] * y
z2 = y * x[:, None]

# z3 = x[None, :] * y
# z4 = y * x[None, :]

print('error >>> x[None, :].shape{} - y.shape{}'.format(x[None, :].shape, y.shape))

print('x[:, None] * y \n{}'.format(z1))
print('y * x[:, None] \n{}'.format(z2))
print('x[None, :] * y \n{}'.format(z3))
print('y * x[None, :] \n{}'.format(z4))

# z1 = x * y[None, :]
# z2 = y[None, :] * x
z3 = x * y[:, None]
z4 = y[:, None] * x

print('error >>> y[None, :].shape{} - x.shape{}'.format(y[None, :].shape, x.shape))

# print('x * y[None, :] \n{}'.format(z1))
# print('y[None, :] * x \n{}'.format(z2))
print('x * y[:, None] \n{}'.format(z3))
print('y[:, None] * x \n{}'.format(z4))

print('''   一维变量x向右扩展维度，一维变量y向左扩展维度，扩展后两者相乘，结果为x_size行，y_size列，乘法满足交换律
			一维变量x向左扩展维度，一维变量y向右扩展维度，扩展后两者相乘，结果为y_size行，x_size列
			一维变量x向右扩展后[:,None]可以乘以一维变量y,[默认y向左扩展]结果x决定行，y决定列，

			一维变量向左扩展后[None,:]不能乘以一维变量，除非这两个一维变量size一样，那么，结果为各元素相乘

			numpy[:,None]=numpy[None]默认向左扩充
			向右扩展维度的决定行，向左扩展维度的决定列。
			[:,None]决定行，[None,:]决定列''')
